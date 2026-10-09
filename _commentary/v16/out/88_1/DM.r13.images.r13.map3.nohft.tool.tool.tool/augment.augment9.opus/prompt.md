Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 88:1; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/88_1/DM.r13.images.r13.map3.nohft.tool.tool.tool/88_1.reading.tr.md (prose paragraphs numbered) =====
## Soru kılığında gelen haber

[¶1] Ayet dört kelimedir ve bir soru cümlesidir. Başta bir soru edatı durur; ardından geçmiş zamanda bir fiil gelir, "geldi", ve bu fiilin nesnesi tekil bir "sen"dir. Gelen şey cümlenin öznesidir, yani haber; haber de kime ait olduğunu tamlamayla söyler: Gâşiye'nin haberi. Soru bilgi almak için sorulmaz. Konuşan cevap beklemeden haberi anlatmaya başlar ve ikinci ayetten itibaren gelen her şey o haberin kendisidir: {ar:وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ, tr:vucûhun yevmeizin hâşia, gloss:o gün birtakım yüzler eğilmiş ve ezilmiştir, source:88:2}. Soru, dinleyeni bir haberin eşiğine getirir ve kulağını açar.

[¶2] Kur'an bu açılışı başka yerlerde de kullanır, ve her seferinde ardından geçmişte yaşanmış bir kıssa gelir. Tâhâ suresinde Musa'nın haberi sorulur, sonra onun yolda bir ateş görüp ailesine "siz burada kalın" deyip ona yöneldiği anlatılır: {ar:وَهَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ, tr:ve hel etâke hadîsü Mûsâ, gloss:Musa'nın haberi sana geldi mi, source:20:9}. Nâziât suresinde aynı soru, Rabbinin ona kutsal vadide seslendiği anı açar {source:79:15}. Zâriyât suresinde soru, İbrahim'in yanına girip selam veren ağırlanmış konuklara yönelir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ضَيْفِ إِبْرَٰهِيمَ ٱلْمُكْرَمِينَ, tr:hel etâke hadîsü dayfi İbrâhîme'l-mükramîn, gloss:İbrahim'in ağırlanan konuklarının haberi sana geldi mi, source:51:24}. Bürûc suresinde sorulan, orduların haberidir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْجُنُودِ, tr:hel etâke hadîsü'l-cunûd, gloss:orduların haberi sana geldi mi, source:85:17}; ve ordular hemen adlandırılır: {ar:فِرْعَوْنَ وَثَمُودَ, tr:Fir'avne ve Semûd, gloss:Firavun ve Semud, source:85:18}. Bu açılışların hepsinde haberin sahibi bir kişi ya da bir topluluktur ve olay geride kalmıştır. Bu ayette haberin sahibi bir özel ad bile değildir; bir iştir, "örten". İkinci ayetteki "o gün" sözü de anlatılan şeyin henüz gelmemiş bir gün olduğunu gösterir. Geçmiş kıssaları açan kalıp burada geleceği açar; gelecek, çoktan anlatılmış bir hikâyenin sesiyle anlatılır.

[¶3] Kur'an gelmekte olan bir şey için geçmiş zamanlı "geldi" fiilini başka bir yerde açıkça kullanır. Nahl suresi şöyle açılır: {ar:أَتَىٰٓ أَمْرُ ٱللَّهِ فَلَا تَسْتَعْجِلُوهُ, tr:etâ emrullâhi felâ testa'cilûh, gloss:Allah'ın emri geldi; artık onu acele istemeyin, source:16:1}. "Geldi" denen şeyin acele istenmesi yasaklanır; demek ki gelmiş sayılan şey hâlâ beklenmektedir. Bu ayette ise "geldi" fiili olayın kendisine değil, haberine bağlanır: olay ileridedir, haberi şimdi kapıdadır.

[¶4] Soru tekil bir "sen"e yönelir ve sure bu "sen"in kim olduğunu kendisi söyler. Yirmi birinci ayette ona {ar:فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ, tr:fe-zekkir innemâ ente müzekkir, gloss:öyleyse hatırlat; sen yalnızca hatırlatansın, source:88:21} denir. Haberi ilk alan, onu taşıyacak olandır. Ama soru tekil olduğu için her okuyucu da kendini bu "sen"in yerinde bulur.

## Hadîs: olup biten şeyin sözü

[¶5] Ayette "haber" diye okunan kelime hadîstir. Kökü önce bir şeyin yokken var olmasını anlatır: {ar:كون الشيء لم يكن, tr:kevnu'ş-şey'i lem yekun, gloss:olmayan bir şeyin olması, source:"ح د ث,B001"}. Bir işin vuku bulması da bu fiille söylenir: {ar:وحدث أمر أي وقع, tr:ve hadese emrun ey vakaa, gloss:bir iş oldu, yani vuku buldu, source:"ح د ث,B001"}. Söze hadîs denmesinin sebebi de aynı harekette aranır: {ar:الحديث لأنه كلام يحدث منه الشيء بعد الشيء, tr:el-hadîsu li-ennehû kelâmun yahdüsu minhu'ş-şey'u ba'de'ş-şey', gloss:söze hadîs denir, çünkü ondan bir şey ardından bir şey doğar, source:"ح د ث,B003"}. Hadîs, önüne bir anda konan bir hüküm değil, parça parça açılan bir anlatıdır. Sure de haberi böyle verir: önce yüzler, sonra onların yorgun emeği, sonra ateş, içecek ve yiyecek; ardından öteki yüzler, bahçe, pınar, sedirler. Soru tek kelimeyle "kıyamet" demez; bir anlatı başlatır ve onu sahne sahne sürdürür. Hadîs aynı zamanda insana kulaktan ulaşan sözdür: {ar:كل كلام يبلغ الإنسان من جهة السمع أو الوحي يقال له حديث, tr:küllü kelâmin yeblüğu'l-insâne min cihetı's-sem'i evi'l-vahyi yukâlü lehû hadîs, gloss:insana işitme ya da vahiy yoluyla ulaşan her söze hadîs denir, source:"ح د ث,B003"}. Sure göze seslenmeden önce kulağa seslenir; on yedinci ayetteki "bakmazlar mı" sorusu ancak bu dinlemenin ardından gelir.

[¶6] Aynı kök "yeni" demektir: {ar:الحديث الجديد من الأشياء, tr:el-hadîsu'l-cedîdu mine'l-eşyâ', gloss:hadîs, şeylerin yenisidir, source:"ح د ث,B002"}. Kur'an kendisine gelen uyarıyı bu kökten bir sıfatla anar. Enbiyâ suresi, hesapları yaklaşmışken insanların gaflet içinde yüz çevirdiğini söyleyerek açılır: {ar:ٱقْتَرَبَ لِلنَّاسِ حِسَابُهُمْ, tr:ikterabe li'n-nâsi hısâbuhum, gloss:insanların hesabı yaklaştı, source:21:1}; ve sürer: {ar:مَا يَأْتِيهِم مِّن ذِكْرٍۢ مِّن رَّبِّهِم مُّحْدَثٍ إِلَّا ٱسْتَمَعُوهُ وَهُمْ يَلْعَبُونَ, tr:mâ ye'tîhim min zikrin min rabbihim muhdesin illestemeûhu ve hum yel'abûn, gloss:Rablerinden kendilerine yeni gelen hiçbir hatırlatma yoktur ki onu oyun oynarken dinlemesinler, source:21:2}. Orada bu ayetin iki kelimesi, gelmek fiili ve hadîsin kökü, bir hatırlatmanın içinde yan yana durur, ve hepsinin başında hesap vardır. Bu surenin son kelimesi de aynı hesaptır: {ar:ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم, tr:summe inne aleynâ hısâbehum, gloss:sonra hesapları da şüphesiz Bize aittir, source:88:26}. Enbiyâ'nın açılışında bir arada duran gelen yeni söz, hatırlatma ve hesap, bu surede ilk ayete, yirmi birinci ayete ve son ayete dağılmıştır.

[¶7] Türkçede kelime iki ayrı yola girmiştir. "Hadis" bugün yalnızca Peygamber'den aktarılan sözleri anlatır; "hâdise" ise olay demektir. Arapçada bu ikisi tek kelimenin iki yüzüdür: hadîs hem anlatılan söz hem de olup biten şeydir. Türkçe okuyucunun "Gâşiye'nin haberi" sözünde kaçırdığı budur: haber, anlattığı olayla aynı kökten konuşur.

[¶8] Bu kelimenin akrabaları arasında ağır bir olay da vardır. Bundan sonra gelen bütün resimler için bir kural geçerlidir: kelimenin ailesinden gelen bir resim, kelimenin bu ayetteki anlamının yerine geçmez, onun yanında duyulur. Ayette hadîs "haber"dir. Ama aynı kökten başa inen yıkıcı olaya da ad verilir: {ar:الحادثة النازلة العارضة وجمعها حوادث, tr:el-hâdisetü'n-nâziletü'l-âridatu ve cem'uhâ havâdis, gloss:hâdise, ansızın inip baş gösteren belâdır, çoğulu havâdistir, source:"ح د ث,B005"}. Araplar zamanın musibetlerini de bu kökle anarlardı: {ar:حدثان الدهر نوائبه, tr:hadesânü'd-dehri nevâibuh, gloss:zamanın hadesânı onun musibetleridir, source:"ح د ث,B005"}. Bu anlam ayetteki haberin yanında duyulduğunda haberle haber verilen şey arasındaki mesafe daralır: anlatılan Gâşiye, kendisi de inen bir hâdisedir.

[¶9] Bir başka kol, anlatının insanı nasıl içine aldığını gösterir. Hakkında çok konuşulan biri için {ar:صار فلان أحدوثة أي كثروا فيه الأحاديث, tr:sâra fülânun uhdûseten ey kesurû fîhi'l-ehâdîs, gloss:falan dillere düştü, yani hakkında çok söz edildi, source:"ح د ث,B004"} derlerdi. Kur'an bunu helak edilen topluluklar için söyler. Mü'minûn suresinde Allah, elçilerini birbiri ardınca gönderdiğini ve her topluluğun kendi elçisini yalanladığını anlatır, sonra sonucu bildirir: {ar:فَأَتْبَعْنَا بَعْضَهُم بَعْضًۭا وَجَعَلْنَٰهُمْ أَحَادِيثَ, tr:fe-etba'nâ ba'dahum ba'dan ve cealnâhum ehâdîs, gloss:onları da birbiri ardınca götürdük ve onları anlatılan hikâyelere çevirdik, source:23:44}. Sebe' halkı da Rablerinden yolculuklarının arasını uzatmasını isteyip kendilerine zulmettiklerinde aynı sona varır {source:34:19}. Hadîsin ailesinde dinleyenle anlatılan yer değiştirebilir. Bu ayetin sorusu bir haberi dinleyene uzatır; onu dinlemeyen, bir gün başkalarına anlatılan bir haber olabilir.

## Gâşiye: adını işinden alan

[¶10] Gâşiye, "örtmek" fiilinden yapılmış dişil bir sıfattır: örten, kaplayan. Ayet o şeyin ne olduğunu söylemez, ne yaptığını söyler; ad, işin kendisidir. Kökün temel işi bir şeyi başka bir şeyle kaplamaktır: {ar:أصل صحيح يدل على تغطية شيء بشيء, tr:aslun sahîhun yedullü alâ tağtiyeti şey'in bi-şey', gloss:bir şeyin bir şeyle örtülmesini gösteren sağlam bir kök, source:"غ ش و,B001"}.

[¶11] Kelimenin elle tutulur bir nesnesi vardır. Eyerin üstüne atılan örtüye de bu ad verilir: {ar:وغاشية السرج غطاؤه, tr:ve ğâşiyetü's-serci ğıtâuh, gloss:eyerin gâşiyesi onun örtüsüdür, source:"غ ش و,B001"}. Böyle bir örtü eyerin üstüne yukarıdan bırakılır, kenarları aşağı sarkar ve eyeri her yanından sararak gözden saklar; altındaki artık görünmez, yalnızca örtü görünür. Kıyamet bu adla anıldığında aynı hareket bütün yaratılmışlara uygulanır: {ar:الغاشية القيامة لأنها تغشى الخلق بإفزاعها, tr:el-ğâşiyetü'l-kıyâmetü li-ennehâ tağşe'l-halka bi-ifzâıhâ, gloss:Gâşiye kıyamettir, çünkü yaratılmışları dehşetleriyle örter, source:"غ ش و,B002"}. Örten şey burada bir kumaş değil dehşettir, ve tek bir eyeri değil bütün halkı kaplar. Bir başka tarif, örtünün kimseyi dışarıda bırakmadığını vurgular: {ar:غاشية من عذاب الله أي عقوبة مجللة تعمهم, tr:ğâşiyetun min azâbillâhi ey ukûbetun mücelleletun teummuhum, gloss:Allah'ın azabından bir gâşiye, yani hepsini kaplayıp kuşatan bir ceza, source:"غ ش و,B002"}.

[¶12] Kur'an örtünün ne olduğunu çoğu zaman adlandırmaz; aynı fiili tekrarlayıp açık bırakır. Musa'ya kullarını yola çıkarması ve onlara denizde kuru bir yol açması vahyedilir {source:20:77}; Firavun peşlerine düşer: {ar:فَأَتْبَعَهُمْ فِرْعَوْنُ بِجُنُودِهِۦ فَغَشِيَهُم مِّنَ ٱلْيَمِّ مَا غَشِيَهُمْ, tr:fe-etbeahum Fir'avnu bi-cunûdihî fe-ğaşiyehum mine'l-yemmi mâ ğaşiyehum, gloss:Firavun ordularıyla onların peşine düştü; denizden onları örten şey örttü, source:20:78}. Bürûc suresinde sorulan "orduların haberi"nin Firavun'a ait yüzü işte bu tek fiilde anlatılmıştır: deniz onları bir örtü gibi kapatmış, ne olduğu ise yalnızca "örten şey" diye bırakılmıştır. Necm suresinde helak edilen kentin sonu da aynı söyleyişle biter: {ar:فَغَشَّىٰهَا مَا غَشَّىٰ, tr:fe-ğaşşâhâ mâ ğaşşâ, gloss:onu örttüğü şeyle örttü, source:53:54}. Gâşiye adı bu tavrın en yoğun hâlidir: örtünün kendisi tarif edilmez, yalnızca yaptığı söylenir, çünkü onu anlatacak her başka kelime onu daraltırdı.

[¶13] Örtü bazen yukarıdan, bazen her yandan gelir. Duhan suresinde Allah, kuşku içinde oyalananlar karşısında Peygamber'e beklemesini söyler: {ar:فَٱرْتَقِبْ يَوْمَ تَأْتِى ٱلسَّمَآءُ بِدُخَانٍۢ مُّبِينٍۢ, tr:fertekıb yevme te'ti's-semâu bi-duhânin mubîn, gloss:göğün apaçık bir duman getireceği günü gözle, source:44:10}; o duman için de {ar:يَغْشَى ٱلنَّاسَ ۖ هَٰذَا عَذَابٌ أَلِيمٌۭ, tr:yağşe'n-nâs hâzâ azâbun elîm, gloss:insanları örter; bu acı bir azaptır, source:44:11} denir. Ankebût suresinde Peygamber'den azabı acele getirmesini isteyenlere cevap verilir, ve o azap onları alttan da kapatacaktır: {ar:يَوْمَ يَغْشَىٰهُمُ ٱلْعَذَابُ مِن فَوْقِهِمْ وَمِن تَحْتِ أَرْجُلِهِمْ, tr:yevme yağşâhumu'l-azâbu min fevkıhim ve min tahti ercülihim, gloss:azabın onları üstlerinden ve ayaklarının altından örteceği gün, source:29:55}. Eyer örtüsü yalnızca üstten sarardı; bu örtünün altında basacak bir yer de kalmaz.

[¶14] Örtü dışta da kalmaz. Aynı fiil edilgen kullanıldığında bayılmayı anlatır; başa gelen bir şey anlayışı kapatmıştır: {ar:غشي على فلان إذا نابه ما غشي فهمه, tr:ğuşiye alâ fülânin izâ nâbehû mâ ğaşiye fehmeh, gloss:başına gelen şey anlayışını örtünce falan için "üstü örtüldü", yani bayıldı denir, source:"غ ش و,B005"}. Ölüm baygınlığı da bu adla anılır: {ar:وكذلك غشية الموت, tr:ve kezâlike ğaşyetü'l-mevt, gloss:ölüm baygınlığı da böyledir, source:"غ ش و,B005"}. Kur'an bu hâli bir bakışta gösterir. Muhammed suresinde iman edenler bir sure indirilmesini isterler; içinde savaşın anıldığı kesin bir sure indiğinde ise kalplerinde hastalık olanların Peygamber'e nasıl baktığı anlatılır: {ar:يَنظُرُونَ إِلَيْكَ نَظَرَ ٱلْمَغْشِىِّ عَلَيْهِ مِنَ ٱلْمَوْتِ, tr:yanzurûne ileyke nazara'l-mağşiyyi aleyhi mine'l-mevt, gloss:ölümden bayılmış birinin bakışıyla sana bakarlar, source:47:20}. Gözler açıktır, ama arkasındaki kavrayış örtülmüştür. Bir başka kalıp örtüyü bedenin içine taşır; birine kötülük dilerken {ar:رماه الله بغاشية وهي داء يأخذ في الجوف, tr:ramâhullâhu bi-ğâşiyetin ve hiye dâun ye'huzu fi'l-cevf, gloss:Allah ona bir gâşiye atsın; bu, insanı içinden tutan bir hastalıktır, source:"غ ش و,B002"} derlerdi. Bu kullanımların yanında duyulduğunda Gâşiye yalnızca dışarıdan saran bir örtü değildir; aklın ve bedenin içine kadar işleyen bir kaplamadır.

[¶15] Bir kullanım örtüyü bir darbeye çevirir. Birini kamçıyla dövene {ar:غشيت الرجل بالسوط ضربته, tr:ğaşîtü'r-racule bi's-savt darabtuh, gloss:adamı kamçıyla örttüm, yani dövdüm, source:"غ ش و,B006"} dedirten bir söyleyiş vardı, ve bu söyleyiş giydirmek ve sarık sarmakla aynı kalıpta kurulurdu: {ar:غشيته سوطا أو سيفا ككسوته وعممته, tr:ğaşîtuhû savten ev seyfen ke-kesevtuhû ve ammemtuh, gloss:onu kamçıyla ya da kılıçla örttüm, tıpkı onu giydirdim, ona sarık sardım der gibi, source:"غ ش و,B006"}. Darbe, insanın üstüne bir elbise gibi iner. Gâşiye'nin dehşeti de bu resmin yanında, üstüne giydirilen ve çıkarılamayan bir elbise gibi duyulur.

[¶16] Yine de fiil kendi başına korku taşımaz; neyin ve kimin örttüğüne bağlıdır. Enfâl suresinde Allah, Rablerinden yardım dileyen müminlere {source:8:9} bir savaş gününü hatırlatır: {ar:إِذْ يُغَشِّيكُمُ ٱلنُّعَاسَ أَمَنَةًۭ مِّنْهُ, tr:iz yuğaşşîkumu'n-nuâse emeneten minh, gloss:hani O, kendinden bir güven olarak sizi uykuyla örtüyordu, source:8:11}. Aynı fiil orada korkunun ortasında huzur getirir. Surede de örtü tek yüzlü değildir: ikinci ayetteki yüzlerin üstüne inen örtünün karşısında onuncu ayette {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüce bir bahçede, source:88:10} bir bahçe durur, ve yirmi üçüncü ayetteki inkâr da kendi kökünde örtmeyi taşır; bu örtülerin karşılaşması surenin bütününde kurulur.

[¶17] Kur'an o günün bir başka adını da aynı biçimde bir işten yapar ve anlatısını açıkça "hadîs" diye anar. Necm suresi, helak edilen eski toplulukları saydıktan {source:53:50} ve bunun önceki uyarılar gibi bir uyarı olduğunu söyledikten {source:53:56} sonra şöyle sürer: {ar:أَزِفَتِ ٱلْءَازِفَةُ, tr:ezifeti'l-âzife, gloss:yaklaşan yaklaştı, source:53:57}; {ar:لَيْسَ لَهَا مِن دُونِ ٱللَّهِ كَاشِفَةٌ, tr:leyse lehâ min dûnillâhi kâşife, gloss:onu Allah'tan başka açıp kaldıracak yoktur, source:53:58}; {ar:أَفَمِنْ هَٰذَا ٱلْحَدِيثِ تَعْجَبُونَ, tr:e-fe-min hâze'l-hadîsi ta'cebûn, gloss:bu habere mi şaşıyorsunuz, source:53:59}. Orada da gün ne yaptığıyla adlandırılır, ve karşısına "açan" kelimesi konur. Gâşiye örtense, o örtüyü kaldırabilecek tek el Allah'ındır. Necm'de bu habere gülüp ağlamayanlara sitem edilir {source:53:60} ve sure secdeye çağrıyla kapanır {source:53:62}.

## Cilalayan söz, örten perde

[¶18] Hadîsin kökünde beklenmedik bir zanaat resmi de vardır. Kılıcı cilalayıp pasını gidermeye bu kökten ad verilirdi: {ar:محادثة السيف جلاؤه, tr:muhâdesetü's-seyfi cilâuh, gloss:kılıcın muhâdesesi onun cilalanmasıdır, source:"ح د ث,B007"}. Kılıcın yüzü tekrar tekrar sürtülür, üstündeki matlık kalkar, demir yeniden parlar ve keskinliği ortaya çıkar. Aynı fiil yüreğe de uygulanırdı: {ar:أحدث الرجل سيفه وحادثه إذا جلاه وحادثوا هذه القلوب أي اجلوها بالمواعظ, tr:ahdese'r-raculu seyfehû ve hâdesehû izâ celâhu ve hâdisû hâzihi'l-kulûbe eyi'clûhâ bi'l-mevâız, gloss:adam kılıcını parlattı denir; bu yürekleri cilalayın, yani öğütlerle parlatın, source:"ح د ث,B007"}. Bu resim ayetteki haberin yanında duyulduğunda haber yalnızca bilgi taşımaz; yüreğin üstünden tekrar tekrar geçerek onun yüzünü açar.

[¶19] Gâşiye'nin kökü ise tam karşı işi yapan bir perdeyi adlandırır: {ar:الغشاوة ما غشي القلب من رين الطبع, tr:el-ğışâvetu mâ ğaşiye'l-kalbe min reyni't-tab', gloss:gışâve, mühürlenmenin pasından yüreği örten şeydir, source:"غ ش و,B001"}. Burada örtü bir pastır, cilanın kaldırdığı şeyin ta kendisi. Kur'an pası da perdeyi de anar. Mutaffifîn suresinde, ayetler kendisine okunduğunda "öncekilerin masalları" diyen kimse için {ar:كَلَّا ۖ بَلْ ۜ رَانَ عَلَىٰ قُلُوبِهِم مَّا كَانُوا۟ يَكْسِبُونَ, tr:kellâ bel râne alâ kulûbihim mâ kânû yeksibûn, gloss:hayır; kazandıkları şey yüreklerinin üstünde pas tuttu, source:83:14} denir; "pas tuttu" fiili, perdenin tarifindeki pasla aynı kelimedir. Câsiye suresinde Allah, hevasını tanrı edinen kimseyi gösterir; kulağı ve yüreği mühürlenmiştir, ve ayet şöyle biter: {ar:وَجَعَلَ عَلَىٰ بَصَرِهِۦ غِشَٰوَةًۭ فَمَن يَهْدِيهِ مِنۢ بَعْدِ ٱللَّهِ ۚ أَفَلَا تَذَكَّرُونَ, tr:ve ceale alâ basarihî ğışâveten fe-men yehdîhi min ba'dillâh e-fe-lâ tezekkerûn, gloss:gözüne bir perde çekti; Allah'tan sonra onu kim yola getirir; hiç düşünüp hatırlamaz mısınız, source:45:23}. Perdenin hemen ardından hatırlama çağrısı gelir.

[¶20] Hadîs ile gâşiye ayrı köklerdir; aralarındaki bağ ortak bir kökten değil, ayetin onları bir tamlamada birleştirmesinden ve iki kelimenin taşıdığı resimlerin karşılaşmasından doğar. Ayet, cilalayan bir sözü örten bir günün haberi yapar. Haber bugün yüreğe gelir, onu ovar ve açar; anlattığı gün ise geldiğinde örter. Yüreği pas tutmuş biri için aynı söz yalnızca "masal" olur, Mutaffifîn'deki adamın dediği gibi; söz cilalamazsa, örtü sözden önce inmiş demektir. Yirmi birinci ayette Peygamber'e verilen iş, {ar:فَذَكِّرْ, tr:fe-zekkir, gloss:öyleyse hatırlat, source:88:21}, bu cilanın işidir.

## Gelen ve gelip örten

[¶21] Ayetin fiili gelmektir, ve bu geliş zorlanmış bir varış değildir: {ar:الإتيان مجيء بسهولة, tr:el-ityânu mecîun bi-suhûle, gloss:ityân kolayca gelmektir, source:"ء ت ي,B001"}. Fiil iyilik için de kötülük için de kullanılır: {ar:الإتيان يقال في الخير وفي الشر, tr:el-ityânu yukâlü fi'l-hayri ve fi'ş-şerr, gloss:ityân hem hayır hem şer için söylenir, source:"ء ت ي,B011"}. Kötü yüzü edilgen kullanımda belirginleşir. Düşman birinin tepesine dikildiğinde {ar:أتي فلان إذا أطل عليه العدو, tr:utiye fülânun izâ atalle aleyhi'l-aduvv, gloss:düşman tepesine dikilince falana "gelindi" denir, source:"ء ت ي,B011"} derlerdi; ölüm ya da belâ birini bulduğunda da {ar:أتى على فلان أتو أي موت أو بلاء أصابه, tr:etâ alâ fülânin etvun ey mevtun ev belâun asâbeh, gloss:falanın üstüne bir geliş geldi, yani onu ölüm ya da belâ buldu, source:"ء ت ي,B011"} denirdi. Ayette fiilin öznesi haberdir, ve haberin gelişi bir uyarının yumuşak gelişidir; ama haberin taşıdığı şey, fiilin bu öteki yüzüyle gelecek olandır.

[¶22] Aynı kökten bir isim, gelişin bu iki katını somut bir resimde birleştirir. Kurak bir vadiye yağmur yağmadan sel gelebilir; Araplar böyle sele ayrı bir ad verirdi: {ar:سيل أتي وأتاوي إذا جاءك ولم يصبك مطره, tr:seylun etiyyun ve etâviyyun izâ câeke ve lem yusıbke mataruh, gloss:yağmuru sana değmeden gelen sele etiyy denir, source:"ء ت ي,B005"}. Yağmur uzakta, başka bir yerde yağmıştır: {ar:الأتي السيل بعينه يأتيك من بلد مطر من غير بلدك, tr:el-etiyyu's-seylu bi-aynihî ye'tîke min beledin mutıra min ğayri beledik, gloss:etiyy, senin yurdun dışında yağmur almış bir yerden sana gelen seldir, source:"ء ت ي,B005"}. Vadide oturan bulutu görmemiş, gök gürültüsünü duymamıştır; ama su kapısına dayanmıştır. Bu resim ayetin fiilinin yanında duyulduğunda haberin gelişi böyle bir sele benzer: Gâşiye'nin kendisi henüz dinleyenin göğünde değildir, ama ondan kopan haber şimdiden onun vadisine ulaşmıştır.

[¶23] Kur'an Gâşiye'nin kendisinin nasıl geleceğini de söyler: ansızın ve fark edilmeden. Yusuf kıssasının sonunda Allah, göklerde ve yerde nice işaretin yanından yüz çevirerek geçenleri anlatır {source:12:105} ve sorar: {ar:أَفَأَمِنُوٓا۟ أَن تَأْتِيَهُمْ غَٰشِيَةٌۭ مِّنْ عَذَابِ ٱللَّهِ أَوْ تَأْتِيَهُمُ ٱلسَّاعَةُ بَغْتَةًۭ وَهُمْ لَا يَشْعُرُونَ, tr:e-fe-eminû en te'tiyehum ğâşiyetun min azâbillâhi ev te'tiyehumu's-sâatu bağteten ve hum lâ yeş'urûn, gloss:Allah'ın azabından örten bir şeyin kendilerine gelmesinden ya da o saatin, onlar farkında değilken ansızın gelmesinden emin mi oldular, source:12:107}. Bu surenin ilk ayetindeki iki kelime orada aynı cümlededir: bir gâşiye gelir. Orada kelime belirsizdir, "bir örten", olası örtülerden herhangi biri. Bu surede ise belirlilik takısıyla gelir, "o örten": artık bilinen ve tek olan. Ankebût suresinde de azabı acele isteyenlere aynı şey söylenir: {ar:وَلَيَأْتِيَنَّهُم بَغْتَةًۭ وَهُمْ لَا يَشْعُرُونَ, tr:ve le-ye'tiyennehum bağteten ve hum lâ yeş'urûn, gloss:o onlara mutlaka, farkında değilken ansızın gelecektir, source:29:53}. Örtünün kendisi habersiz gelir; bu ayette ise önce haberi gelir. "Sana geldi mi" sorusu dinleyene ansızın olmayan tek gelişi sunar: Gâşiye'yi haberinden tanımak, onu farkında değilken karşılamamanın yoludur.

[¶24] Örtmek fiili de bir geliştir. Bir yere varmak için kullanılır ve gelmek fiiliyle açıklanır: {ar:غشيت موضع كذا أتيته, tr:ğaşîtü mevdia kezâ eteytüh, gloss:falan yeri "örttüm", yani oraya geldim, source:"غ ش و,B003"}; {ar:غشيه غشيانا أي جاءه, tr:ğaşiyehû ğaşeyânen ey câeh, gloss:onu örttü, yani ona geldi, source:"غ ش و,B003"}. Bir adamın kapısına sık sık gelenlere de onun gâşiyesi denirdi: {ar:وغاشية الرجل من ينتابه من زواره وأصدقائه, tr:ve ğâşiyetü'r-raculi men yentâbuhû min zuvvârihî ve asdikâih, gloss:adamın gâşiyesi, ona gelip giden ziyaretçileri ve dostlarıdır, source:"غ ش و,B003"}. Bu kullanımın yanında Gâşiye kapıya gelen biri gibidir; ama bu gelen kapıda beklemez, gelişi zaten kaplamaktır. Ayetin iki ana kelimesi böylece birbirini açar: haber gelir, ve haberin anlattığı şeyin adı da gelip kaplayandır. Duhan suresindeki dumanda bu iki fiil arka arkaya durur: gök dumanı getirir, duman insanları örter {source:44:10}.

[¶25] Gelmek fiilinin bir kullanımı da yürüyen devenin adımına bakar: {ar:ما أحسن أتو يدي هذه الناقة وأتي أيضا أي رجع يديها في السير, tr:mâ ahsene etve yedey hâzihi'n-nâkati ve etiyye eydan ey rac'a yedeyhâ fi's-seyr, gloss:bu dişi devenin ön ayaklarının etvi ne güzel, yani yürürken ön ayaklarını geri toplayışı, source:"ء ت ي,B009"}. Deve yürürken ön ayağını ileri atar ve geri toplar; her adım bir gidiş ve bir dönüştür, ve iyi yürüyen hayvan bu salınımın düzgünlüğüyle övülürdü. Surenin ilk fiilindeki bu deve adımı, yirmi beşinci ayetin {ar:إِنَّ إِلَيْنَآ إِيَابَهُمْ, tr:inne ileynâ iyâbehum, gloss:dönüşleri şüphesiz Bizedir, source:88:25} sözündeki dönüş kelimesiyle ve on yedinci ayetin develeriyle {source:88:17} birlikte surede bir yolculuk resmi kurar.

===== _commentary/v16/out/88_1/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: ghāshiya is the feminine active participle of the verb "to cover"
- memory: āzifa (53:57) = "the approaching one", kāshifa (53:58) = "one who uncovers"; roots not supplied
- memory: jannah (88:10) and kufr (88:23) roots carry "covering"
- memory: rāna (83:14) is the same word as rayn "rust" in the ghishāwa definition
- memory: muḥdath (21:2) read as "newly come"
- memory: Turkish "hadis" narrowed to prophetic reports, "hâdise" = event
- not written: ء ت ي B002 giving - only as "bring" in 44:10, no theme of its own
- not written: ء ت ي B003 suitable way, B004 water channel - no grip on the ayah's act
- not written: ء ت ي B006 stranger - echoes the flood "from elsewhere" but adds nothing the flood lacks
- not written: ء ت ي B007 yield, B008 tribute, B010 road/goal, B012, B013 - no link to the report or the covering
- not written: ح د ث B006 revealing, B008 inspired person - would only restate the report theme
- not written: غ ش و B004 marital union (7:189 tagashshāhā) - covering that yields life; no support in this surah's frame
- not written: غ ش و B007 white-headed animal - colour image, no work in a theme
- not written: 53:16 covering of the lote tree - positive vague covering, 8:11 already carries the point
- not written: echo root غ ش ي - not identity, withheld

===== passages not cited (158) =====
## strong (this ayah's own list) (14)

- (6:47) [listed for 88:1] قُلْ أَرَءَيْتَكُمْ إِنْ أَتَىٰكُمْ عَذَابُ ٱللَّهِ بَغْتَةً أَوْ جَهْرَةً هَلْ يُهْلَكُ إِلَّا ٱلْقَوْمُ ٱلظَّٰلِمُونَ
- (6:158) [listed for 88:1] هَلْ يَنظُرُونَ إِلَّآ أَن تَأْتِيَهُمُ ٱلْمَلَٰٓئِكَةُ أَوْ يَأْتِىَ رَبُّكَ أَوْ يَأْتِىَ بَعْضُ ءَايَٰتِ رَبِّكَ ۗ يَوْمَ يَأْتِى بَعْضُ ءَايَٰتِ رَبِّكَ لَا يَنفَعُ نَفْسًا إِيمَٰنُهَا لَمْ تَكُنْ ءَامَنَتْ مِن قَبْلُ أَوْ كَسَبَتْ فِىٓ إِيمَٰنِهَا خَيْرًۭا ۗ قُلِ ٱنتَظِرُوٓا۟ إِنَّا مُنتَظِرُونَ
- (7:41) [listed for 88:1] لَهُم مِّن جَهَنَّمَ مِهَادٌۭ وَمِن فَوْقِهِمْ غَوَاشٍۢ ۚ وَكَذَٰلِكَ نَجْزِى ٱلظَّٰلِمِينَ
- (10:27) [listed for 88:1] وَٱلَّذِينَ كَسَبُوا۟ ٱلسَّيِّـَٔاتِ جَزَآءُ سَيِّئَةٍۭ بِمِثْلِهَا وَتَرْهَقُهُمْ ذِلَّةٌۭ ۖ مَّا لَهُم مِّنَ ٱللَّهِ مِنْ عَاصِمٍۢ ۖ كَأَنَّمَآ أُغْشِيَتْ وُجُوهُهُمْ قِطَعًۭا مِّنَ ٱلَّيْلِ مُظْلِمًا ۚ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (12:107) [listed for 88:1] [cited in ¶23] أَفَأَمِنُوٓا۟ أَن تَأْتِيَهُمْ غَٰشِيَةٌۭ مِّنْ عَذَابِ ٱللَّهِ أَوْ تَأْتِيَهُمُ ٱلسَّاعَةُ بَغْتَةًۭ وَهُمْ لَا يَشْعُرُونَ
- (14:50) [listed for 88:1] سَرَابِيلُهُم مِّن قَطِرَانٍۢ وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ
- (18:55) [listed for 88:1] وَمَا مَنَعَ ٱلنَّاسَ أَن يُؤْمِنُوٓا۟ إِذْ جَآءَهُمُ ٱلْهُدَىٰ وَيَسْتَغْفِرُوا۟ رَبَّهُمْ إِلَّآ أَن تَأْتِيَهُمْ سُنَّةُ ٱلْأَوَّلِينَ أَوْ يَأْتِيَهُمُ ٱلْعَذَابُ قُبُلًۭا
- (29:55) [listed for 88:1] [cited in ¶13] يَوْمَ يَغْشَىٰهُمُ ٱلْعَذَابُ مِن فَوْقِهِمْ وَمِن تَحْتِ أَرْجُلِهِمْ وَيَقُولُ ذُوقُوا۟ مَا كُنتُمْ تَعْمَلُونَ
- (34:3) [listed for 88:1] وَقَالَ ٱلَّذِينَ كَفَرُوا۟ لَا تَأْتِينَا ٱلسَّاعَةُ ۖ قُلْ بَلَىٰ وَرَبِّى لَتَأْتِيَنَّكُمْ عَٰلِمِ ٱلْغَيْبِ ۖ لَا يَعْزُبُ عَنْهُ مِثْقَالُ ذَرَّةٍۢ فِى ٱلسَّمَٰوَٰتِ وَلَا فِى ٱلْأَرْضِ وَلَآ أَصْغَرُ مِن ذَٰلِكَ وَلَآ أَكْبَرُ إِلَّا فِى كِتَٰبٍۢ مُّبِينٍۢ
- (39:23) [listed for 88:1] ٱللَّهُ نَزَّلَ أَحْسَنَ ٱلْحَدِيثِ كِتَٰبًۭا مُّتَشَٰبِهًۭا مَّثَانِىَ تَقْشَعِرُّ مِنْهُ جُلُودُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُمْ ثُمَّ تَلِينُ جُلُودُهُمْ وَقُلُوبُهُمْ إِلَىٰ ذِكْرِ ٱللَّهِ ۚ ذَٰلِكَ هُدَى ٱللَّهِ يَهْدِى بِهِۦ مَن يَشَآءُ ۚ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍ
- (44:11) [listed for 88:1] [cited in ¶13] يَغْشَى ٱلنَّاسَ ۖ هَٰذَا عَذَابٌ أَلِيمٌۭ
- (79:15) [listed for 88:1] [cited in ¶2] هَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ
- (85:17) [listed for 88:1] [cited in ¶2] هَلْ أَتَىٰكَ حَدِيثُ ٱلْجُنُودِ
- (99:4) [listed for 88:1] يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا

## medium (this ayah's own list) (32)

- (2:38) [listed for 88:1] قُلْنَا ٱهْبِطُوا۟ مِنْهَا جَمِيعًۭا ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَن تَبِعَ هُدَاىَ فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (2:210) [listed for 88:1] هَلْ يَنظُرُونَ إِلَّآ أَن يَأْتِيَهُمُ ٱللَّهُ فِى ظُلَلٍۢ مِّنَ ٱلْغَمَامِ وَٱلْمَلَٰٓئِكَةُ وَقُضِىَ ٱلْأَمْرُ ۚ وَإِلَى ٱللَّهِ تُرْجَعُ ٱلْأُمُورُ
- (5:60) [listed for 88:1] قُلْ هَلْ أُنَبِّئُكُم بِشَرٍّۢ مِّن ذَٰلِكَ مَثُوبَةً عِندَ ٱللَّهِ ۚ مَن لَّعَنَهُ ٱللَّهُ وَغَضِبَ عَلَيْهِ وَجَعَلَ مِنْهُمُ ٱلْقِرَدَةَ وَٱلْخَنَازِيرَ وَعَبَدَ ٱلطَّٰغُوتَ ۚ أُو۟لَٰٓئِكَ شَرٌّۭ مَّكَانًۭا وَأَضَلُّ عَن سَوَآءِ ٱلسَّبِيلِ
- (6:4) [listed for 88:1] وَمَا تَأْتِيهِم مِّنْ ءَايَةٍۢ مِّنْ ءَايَٰتِ رَبِّهِمْ إِلَّا كَانُوا۟ عَنْهَا مُعْرِضِينَ
- (6:68) [listed for 88:1] وَإِذَا رَأَيْتَ ٱلَّذِينَ يَخُوضُونَ فِىٓ ءَايَٰتِنَا فَأَعْرِضْ عَنْهُمْ حَتَّىٰ يَخُوضُوا۟ فِى حَدِيثٍ غَيْرِهِۦ ۚ وَإِمَّا يُنسِيَنَّكَ ٱلشَّيْطَٰنُ فَلَا تَقْعُدْ بَعْدَ ٱلذِّكْرَىٰ مَعَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
- (7:53) [listed for 88:1] هَلْ يَنظُرُونَ إِلَّا تَأْوِيلَهُۥ ۚ يَوْمَ يَأْتِى تَأْوِيلُهُۥ يَقُولُ ٱلَّذِينَ نَسُوهُ مِن قَبْلُ قَدْ جَآءَتْ رُسُلُ رَبِّنَا بِٱلْحَقِّ فَهَل لَّنَا مِن شُفَعَآءَ فَيَشْفَعُوا۟ لَنَآ أَوْ نُرَدُّ فَنَعْمَلَ غَيْرَ ٱلَّذِى كُنَّا نَعْمَلُ ۚ قَدْ خَسِرُوٓا۟ أَنفُسَهُمْ وَضَلَّ عَنْهُم مَّا كَانُوا۟ يَفْتَرُونَ
- (7:185) [listed for 88:1] أَوَلَمْ يَنظُرُوا۟ فِى مَلَكُوتِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا خَلَقَ ٱللَّهُ مِن شَىْءٍۢ وَأَنْ عَسَىٰٓ أَن يَكُونَ قَدِ ٱقْتَرَبَ أَجَلُهُمْ ۖ فَبِأَىِّ حَدِيثٍۭ بَعْدَهُۥ يُؤْمِنُونَ
- (13:3) [listed for 88:1] وَهُوَ ٱلَّذِى مَدَّ ٱلْأَرْضَ وَجَعَلَ فِيهَا رَوَٰسِىَ وَأَنْهَٰرًۭا ۖ وَمِن كُلِّ ٱلثَّمَرَٰتِ جَعَلَ فِيهَا زَوْجَيْنِ ٱثْنَيْنِ ۖ يُغْشِى ٱلَّيْلَ ٱلنَّهَارَ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَتَفَكَّرُونَ
- (18:70) [listed for 88:1] قَالَ فَإِنِ ٱتَّبَعْتَنِى فَلَا تَسْـَٔلْنِى عَن شَىْءٍ حَتَّىٰٓ أُحْدِثَ لَكَ مِنْهُ ذِكْرًۭا
- (19:61) [listed for 88:1] جَنَّٰتِ عَدْنٍ ٱلَّتِى وَعَدَ ٱلرَّحْمَٰنُ عِبَادَهُۥ بِٱلْغَيْبِ ۚ إِنَّهُۥ كَانَ وَعْدُهُۥ مَأْتِيًّۭا
- (20:9) [listed for 88:1] [cited in ¶2] وَهَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ
- (20:78) [listed for 88:1] [cited in ¶12] فَأَتْبَعَهُمْ فِرْعَوْنُ بِجُنُودِهِۦ فَغَشِيَهُم مِّنَ ٱلْيَمِّ مَا غَشِيَهُمْ
- (20:126) [listed for 88:1] قَالَ كَذَٰلِكَ أَتَتْكَ ءَايَٰتُنَا فَنَسِيتَهَا ۖ وَكَذَٰلِكَ ٱلْيَوْمَ تُنسَىٰ
- (21:2) [listed for 88:1] [cited in ¶6] مَا يَأْتِيهِم مِّن ذِكْرٍۢ مِّن رَّبِّهِم مُّحْدَثٍ إِلَّا ٱسْتَمَعُوهُ وَهُمْ يَلْعَبُونَ
- (23:49) [listed for 88:1] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ لَعَلَّهُمْ يَهْتَدُونَ
- (24:40) [listed for 88:1] أَوْ كَظُلُمَٰتٍۢ فِى بَحْرٍۢ لُّجِّىٍّۢ يَغْشَىٰهُ مَوْجٌۭ مِّن فَوْقِهِۦ مَوْجٌۭ مِّن فَوْقِهِۦ سَحَابٌۭ ۚ ظُلُمَٰتٌۢ بَعْضُهَا فَوْقَ بَعْضٍ إِذَآ أَخْرَجَ يَدَهُۥ لَمْ يَكَدْ يَرَىٰهَا ۗ وَمَن لَّمْ يَجْعَلِ ٱللَّهُ لَهُۥ نُورًۭا فَمَا لَهُۥ مِن نُّورٍ
- (26:5) [listed for 88:1] وَمَا يَأْتِيهِم مِّن ذِكْرٍۢ مِّنَ ٱلرَّحْمَٰنِ مُحْدَثٍ إِلَّا كَانُوا۟ عَنْهُ مُعْرِضِينَ
- (28:48) [listed for 88:1] فَلَمَّا جَآءَهُمُ ٱلْحَقُّ مِنْ عِندِنَا قَالُوا۟ لَوْلَآ أُوتِىَ مِثْلَ مَآ أُوتِىَ مُوسَىٰٓ ۚ أَوَلَمْ يَكْفُرُوا۟ بِمَآ أُوتِىَ مُوسَىٰ مِن قَبْلُ ۖ قَالُوا۟ سِحْرَانِ تَظَٰهَرَا وَقَالُوٓا۟ إِنَّا بِكُلٍّۢ كَٰفِرُونَ
- (31:32) [listed for 88:1] وَإِذَا غَشِيَهُم مَّوْجٌۭ كَٱلظُّلَلِ دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ فَلَمَّا نَجَّىٰهُمْ إِلَى ٱلْبَرِّ فَمِنْهُم مُّقْتَصِدٌۭ ۚ وَمَا يَجْحَدُ بِـَٔايَٰتِنَآ إِلَّا كُلُّ خَتَّارٍۢ كَفُورٍۢ
- (34:7) [listed for 88:1] وَقَالَ ٱلَّذِينَ كَفَرُوا۟ هَلْ نَدُلُّكُمْ عَلَىٰ رَجُلٍۢ يُنَبِّئُكُمْ إِذَا مُزِّقْتُمْ كُلَّ مُمَزَّقٍ إِنَّكُمْ لَفِى خَلْقٍۢ جَدِيدٍ
- (45:6) [listed for 88:1] تِلْكَ ءَايَٰتُ ٱللَّهِ نَتْلُوهَا عَلَيْكَ بِٱلْحَقِّ ۖ فَبِأَىِّ حَدِيثٍۭ بَعْدَ ٱللَّهِ وَءَايَٰتِهِۦ يُؤْمِنُونَ
- (51:24) [listed for 88:1] [cited in ¶2] هَلْ أَتَىٰكَ حَدِيثُ ضَيْفِ إِبْرَٰهِيمَ ٱلْمُكْرَمِينَ
- (53:16) [listed for 88:1] إِذْ يَغْشَى ٱلسِّدْرَةَ مَا يَغْشَىٰ
- (53:54) [listed for 88:1] [cited in ¶12] فَغَشَّىٰهَا مَا غَشَّىٰ
- (53:59) [listed for 88:1] [cited in ¶17] أَفَمِنْ هَٰذَا ٱلْحَدِيثِ تَعْجَبُونَ
- (56:81) [listed for 88:1] أَفَبِهَٰذَا ٱلْحَدِيثِ أَنتُم مُّدْهِنُونَ
- (65:1) [listed for 88:1] يَٰٓأَيُّهَا ٱلنَّبِىُّ إِذَا طَلَّقْتُمُ ٱلنِّسَآءَ فَطَلِّقُوهُنَّ لِعِدَّتِهِنَّ وَأَحْصُوا۟ ٱلْعِدَّةَ ۖ وَٱتَّقُوا۟ ٱللَّهَ رَبَّكُمْ ۖ لَا تُخْرِجُوهُنَّ مِنۢ بُيُوتِهِنَّ وَلَا يَخْرُجْنَ إِلَّآ أَن يَأْتِينَ بِفَٰحِشَةٍۢ مُّبَيِّنَةٍۢ ۚ وَتِلْكَ حُدُودُ ٱللَّهِ ۚ وَمَن يَتَعَدَّ حُدُودَ ٱللَّهِ فَقَدْ ظَلَمَ نَفْسَهُۥ ۚ لَا تَدْرِى لَعَلَّ ٱللَّهَ يُحْدِثُ بَعْدَ ذَٰلِكَ أَمْرًۭا
- (68:52) [listed for 88:1] وَمَا هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (77:50) [listed for 88:1] فَبِأَىِّ حَدِيثٍۭ بَعْدَهُۥ يُؤْمِنُونَ
- (92:1) [listed for 88:1] وَٱلَّيْلِ إِذَا يَغْشَىٰ
- (93:11) [listed for 88:1] وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ
- (101:11) [listed for 88:1] نَارٌ حَامِيَةٌۢ

## named by the passage's own list as strong for this ayah (4)

- (18:48) [listed for 88:1] وَعُرِضُوا۟ عَلَىٰ رَبِّكَ صَفًّۭا لَّقَدْ جِئْتُمُونَا كَمَا خَلَقْنَٰكُمْ أَوَّلَ مَرَّةٍۭ ۚ بَلْ زَعَمْتُمْ أَلَّن نَّجْعَلَ لَكُم مَّوْعِدًۭا
- (74:10) [listed for 88:1] عَلَى ٱلْكَٰفِرِينَ غَيْرُ يَسِيرٍۢ
- (79:34) [listed for 88:1] فَإِذَا جَآءَتِ ٱلطَّآمَّةُ ٱلْكُبْرَىٰ
- (101:2) [listed for 88:1] مَا ٱلْقَارِعَةُ

## named by the passage's own list as medium for this ayah (7)

- (11:120) [listed for 88:1] وَكُلًّۭا نَّقُصُّ عَلَيْكَ مِنْ أَنۢبَآءِ ٱلرُّسُلِ مَا نُثَبِّتُ بِهِۦ فُؤَادَكَ ۚ وَجَآءَكَ فِى هَٰذِهِ ٱلْحَقُّ وَمَوْعِظَةٌۭ وَذِكْرَىٰ لِلْمُؤْمِنِينَ
- (38:21) [listed for 88:1] ۞ وَهَلْ أَتَىٰكَ نَبَؤُا۟ ٱلْخَصْمِ إِذْ تَسَوَّرُوا۟ ٱلْمِحْرَابَ
- (68:44) [listed for 88:1] فَذَرْنِى وَمَن يُكَذِّبُ بِهَٰذَا ٱلْحَدِيثِ ۖ سَنَسْتَدْرِجُهُم مِّنْ حَيْثُ لَا يَعْلَمُونَ
- (71:7) [listed for 88:1] وَإِنِّى كُلَّمَا دَعَوْتُهُمْ لِتَغْفِرَ لَهُمْ جَعَلُوٓا۟ أَصَٰبِعَهُمْ فِىٓ ءَاذَانِهِمْ وَٱسْتَغْشَوْا۟ ثِيَابَهُمْ وَأَصَرُّوا۟ وَٱسْتَكْبَرُوا۟ ٱسْتِكْبَارًۭا
- (74:9) [listed for 88:1] فَذَٰلِكَ يَوْمَئِذٍۢ يَوْمٌ عَسِيرٌ
- (76:1) [listed for 88:1] هَلْ أَتَىٰ عَلَى ٱلْإِنسَٰنِ حِينٌۭ مِّنَ ٱلدَّهْرِ لَمْ يَكُن شَيْـًۭٔا مَّذْكُورًا
- (91:4) [listed for 88:1] وَٱلَّيْلِ إِذَا يَغْشَىٰهَا

## weak (this ayah's own list) (20)

- (2:7) [listed for 88:1] خَتَمَ ٱللَّهُ عَلَىٰ قُلُوبِهِمْ وَعَلَىٰ سَمْعِهِمْ ۖ وَعَلَىٰٓ أَبْصَٰرِهِمْ غِشَٰوَةٌۭ ۖ وَلَهُمْ عَذَابٌ عَظِيمٌۭ
- (2:76) [listed for 88:1] وَإِذَا لَقُوا۟ ٱلَّذِينَ ءَامَنُوا۟ قَالُوٓا۟ ءَامَنَّا وَإِذَا خَلَا بَعْضُهُمْ إِلَىٰ بَعْضٍۢ قَالُوٓا۟ أَتُحَدِّثُونَهُم بِمَا فَتَحَ ٱللَّهُ عَلَيْكُمْ لِيُحَآجُّوكُم بِهِۦ عِندَ رَبِّكُمْ ۚ أَفَلَا تَعْقِلُونَ
- (2:109) [listed for 88:1] وَدَّ كَثِيرٌۭ مِّنْ أَهْلِ ٱلْكِتَٰبِ لَوْ يَرُدُّونَكُم مِّنۢ بَعْدِ إِيمَٰنِكُمْ كُفَّارًا حَسَدًۭا مِّنْ عِندِ أَنفُسِهِم مِّنۢ بَعْدِ مَا تَبَيَّنَ لَهُمُ ٱلْحَقُّ ۖ فَٱعْفُوا۟ وَٱصْفَحُوا۟ حَتَّىٰ يَأْتِىَ ٱللَّهُ بِأَمْرِهِۦٓ ۗ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (2:118) [listed for 88:1] وَقَالَ ٱلَّذِينَ لَا يَعْلَمُونَ لَوْلَا يُكَلِّمُنَا ٱللَّهُ أَوْ تَأْتِينَآ ءَايَةٌۭ ۗ كَذَٰلِكَ قَالَ ٱلَّذِينَ مِن قَبْلِهِم مِّثْلَ قَوْلِهِمْ ۘ تَشَٰبَهَتْ قُلُوبُهُمْ ۗ قَدْ بَيَّنَّا ٱلْءَايَٰتِ لِقَوْمٍۢ يُوقِنُونَ
- (2:148) [listed for 88:1] وَلِكُلٍّۢ وِجْهَةٌ هُوَ مُوَلِّيهَا ۖ فَٱسْتَبِقُوا۟ ٱلْخَيْرَٰتِ ۚ أَيْنَ مَا تَكُونُوا۟ يَأْتِ بِكُمُ ٱللَّهُ جَمِيعًا ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (3:154) [listed for 88:1] ثُمَّ أَنزَلَ عَلَيْكُم مِّنۢ بَعْدِ ٱلْغَمِّ أَمَنَةًۭ نُّعَاسًۭا يَغْشَىٰ طَآئِفَةًۭ مِّنكُمْ ۖ وَطَآئِفَةٌۭ قَدْ أَهَمَّتْهُمْ أَنفُسُهُمْ يَظُنُّونَ بِٱللَّهِ غَيْرَ ٱلْحَقِّ ظَنَّ ٱلْجَٰهِلِيَّةِ ۖ يَقُولُونَ هَل لَّنَا مِنَ ٱلْأَمْرِ مِن شَىْءٍۢ ۗ قُلْ إِنَّ ٱلْأَمْرَ كُلَّهُۥ لِلَّهِ ۗ يُخْفُونَ فِىٓ أَنفُسِهِم مَّا لَا يُبْدُونَ لَكَ ۖ يَقُولُونَ لَوْ كَانَ لَنَا مِنَ ٱلْأَمْرِ شَىْءٌۭ مَّا قُتِلْنَا هَٰهُنَا ۗ قُل لَّوْ كُنتُمْ فِى بُيُوتِكُمْ لَبَرَزَ ٱلَّذِينَ كُتِبَ عَلَيْهِمُ ٱلْقَتْلُ إِلَىٰ مَضَاجِعِهِمْ ۖ وَلِيَبْتَلِىَ ٱللَّهُ مَا فِى صُدُورِكُمْ وَلِيُمَحِّصَ مَا فِى قُلُوبِكُمْ ۗ وَٱللَّهُ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (4:140) [listed for 88:1] وَقَدْ نَزَّلَ عَلَيْكُمْ فِى ٱلْكِتَٰبِ أَنْ إِذَا سَمِعْتُمْ ءَايَٰتِ ٱللَّهِ يُكْفَرُ بِهَا وَيُسْتَهْزَأُ بِهَا فَلَا تَقْعُدُوا۟ مَعَهُمْ حَتَّىٰ يَخُوضُوا۟ فِى حَدِيثٍ غَيْرِهِۦٓ ۚ إِنَّكُمْ إِذًۭا مِّثْلُهُمْ ۗ إِنَّ ٱللَّهَ جَامِعُ ٱلْمُنَٰفِقِينَ وَٱلْكَٰفِرِينَ فِى جَهَنَّمَ جَمِيعًا
- (7:54) [listed for 88:1] إِنَّ رَبَّكُمُ ٱللَّهُ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ يُغْشِى ٱلَّيْلَ ٱلنَّهَارَ يَطْلُبُهُۥ حَثِيثًۭا وَٱلشَّمْسَ وَٱلْقَمَرَ وَٱلنُّجُومَ مُسَخَّرَٰتٍۭ بِأَمْرِهِۦٓ ۗ أَلَا لَهُ ٱلْخَلْقُ وَٱلْأَمْرُ ۗ تَبَارَكَ ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
- (7:189) [listed for 88:1] ۞ هُوَ ٱلَّذِى خَلَقَكُم مِّن نَّفْسٍۢ وَٰحِدَةٍۢ وَجَعَلَ مِنْهَا زَوْجَهَا لِيَسْكُنَ إِلَيْهَا ۖ فَلَمَّا تَغَشَّىٰهَا حَمَلَتْ حَمْلًا خَفِيفًۭا فَمَرَّتْ بِهِۦ ۖ فَلَمَّآ أَثْقَلَت دَّعَوَا ٱللَّهَ رَبَّهُمَا لَئِنْ ءَاتَيْتَنَا صَٰلِحًۭا لَّنَكُونَنَّ مِنَ ٱلشَّٰكِرِينَ
- (9:52) [listed for 88:1] قُلْ هَلْ تَرَبَّصُونَ بِنَآ إِلَّآ إِحْدَى ٱلْحُسْنَيَيْنِ ۖ وَنَحْنُ نَتَرَبَّصُ بِكُمْ أَن يُصِيبَكُمُ ٱللَّهُ بِعَذَابٍۢ مِّنْ عِندِهِۦٓ أَوْ بِأَيْدِينَا ۖ فَتَرَبَّصُوٓا۟ إِنَّا مَعَكُم مُّتَرَبِّصُونَ
- (12:49) [listed for 88:1] ثُمَّ يَأْتِى مِنۢ بَعْدِ ذَٰلِكَ عَامٌۭ فِيهِ يُغَاثُ ٱلنَّاسُ وَفِيهِ يَعْصِرُونَ
- (12:101) [listed for 88:1] ۞ رَبِّ قَدْ ءَاتَيْتَنِى مِنَ ٱلْمُلْكِ وَعَلَّمْتَنِى مِن تَأْوِيلِ ٱلْأَحَادِيثِ ۚ فَاطِرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ أَنتَ وَلِىِّۦ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۖ تَوَفَّنِى مُسْلِمًۭا وَأَلْحِقْنِى بِٱلصَّٰلِحِينَ
- (18:15) [listed for 88:1] هَٰٓؤُلَآءِ قَوْمُنَا ٱتَّخَذُوا۟ مِن دُونِهِۦٓ ءَالِهَةًۭ ۖ لَّوْلَا يَأْتُونَ عَلَيْهِم بِسُلْطَٰنٍۭ بَيِّنٍۢ ۖ فَمَنْ أَظْلَمُ مِمَّنِ ٱفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًۭا
- (23:60) [listed for 88:1] وَٱلَّذِينَ يُؤْتُونَ مَآ ءَاتَوا۟ وَّقُلُوبُهُمْ وَجِلَةٌ أَنَّهُمْ إِلَىٰ رَبِّهِمْ رَٰجِعُونَ
- (26:89) [listed for 88:1] إِلَّا مَنْ أَتَى ٱللَّهَ بِقَلْبٍۢ سَلِيمٍۢ
- (33:19) [listed for 88:1] أَشِحَّةً عَلَيْكُمْ ۖ فَإِذَا جَآءَ ٱلْخَوْفُ رَأَيْتَهُمْ يَنظُرُونَ إِلَيْكَ تَدُورُ أَعْيُنُهُمْ كَٱلَّذِى يُغْشَىٰ عَلَيْهِ مِنَ ٱلْمَوْتِ ۖ فَإِذَا ذَهَبَ ٱلْخَوْفُ سَلَقُوكُم بِأَلْسِنَةٍ حِدَادٍ أَشِحَّةً عَلَى ٱلْخَيْرِ ۚ أُو۟لَٰٓئِكَ لَمْ يُؤْمِنُوا۟ فَأَحْبَطَ ٱللَّهُ أَعْمَٰلَهُمْ ۚ وَكَانَ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرًۭا
- (37:54) [listed for 88:1] قَالَ هَلْ أَنتُم مُّطَّلِعُونَ
- (52:34) [listed for 88:1] فَلْيَأْتُوا۟ بِحَدِيثٍۢ مِّثْلِهِۦٓ إِن كَانُوا۟ صَٰدِقِينَ
- (68:41) [listed for 88:1] أَمْ لَهُمْ شُرَكَآءُ فَلْيَأْتُوا۟ بِشُرَكَآئِهِمْ إِن كَانُوا۟ صَٰدِقِينَ
- (92:16) [listed for 88:1] ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ

## named by the passage's own list as weak for this ayah (9)

- (6:67) [listed for 88:1] لِّكُلِّ نَبَإٍۢ مُّسْتَقَرٌّۭ ۚ وَسَوْفَ تَعْلَمُونَ
- (22:21) [listed for 88:1] وَلَهُم مَّقَٰمِعُ مِنْ حَدِيدٍۢ
- (36:9) [listed for 88:1] وَجَعَلْنَا مِنۢ بَيْنِ أَيْدِيهِمْ سَدًّۭا وَمِنْ خَلْفِهِمْ سَدًّۭا فَأَغْشَيْنَٰهُمْ فَهُمْ لَا يُبْصِرُونَ
- (39:40) [listed for 88:1] مَن يَأْتِيهِ عَذَابٌۭ يُخْزِيهِ وَيَحِلُّ عَلَيْهِ عَذَابٌۭ مُّقِيمٌ
- (89:5) [listed for 88:1] هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ
- (101:3) [listed for 88:1] وَمَآ أَدْرَىٰكَ مَا ٱلْقَارِعَةُ
- (101:10) [listed for 88:1] وَمَآ أَدْرَىٰكَ مَا هِيَهْ
- (102:1) [listed for 88:1] أَلْهَىٰكُمُ ٱلتَّكَاثُرُ
- (104:5) [listed for 88:1] وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ

## neighbours: within two ayat of a passage the commentary cites (72)

- (8:7) [next to 8:9] وَإِذْ يَعِدُكُمُ ٱللَّهُ إِحْدَى ٱلطَّآئِفَتَيْنِ أَنَّهَا لَكُمْ وَتَوَدُّونَ أَنَّ غَيْرَ ذَاتِ ٱلشَّوْكَةِ تَكُونُ لَكُمْ وَيُرِيدُ ٱللَّهُ أَن يُحِقَّ ٱلْحَقَّ بِكَلِمَٰتِهِۦ وَيَقْطَعَ دَابِرَ ٱلْكَٰفِرِينَ
- (8:8) [next to 8:9] لِيُحِقَّ ٱلْحَقَّ وَيُبْطِلَ ٱلْبَٰطِلَ وَلَوْ كَرِهَ ٱلْمُجْرِمُونَ
- (8:10) [next to 8:9] وَمَا جَعَلَهُ ٱللَّهُ إِلَّا بُشْرَىٰ وَلِتَطْمَئِنَّ بِهِۦ قُلُوبُكُمْ ۚ وَمَا ٱلنَّصْرُ إِلَّا مِنْ عِندِ ٱللَّهِ ۚ إِنَّ ٱللَّهَ عَزِيزٌ حَكِيمٌ
- (8:12) [next to 8:11] إِذْ يُوحِى رَبُّكَ إِلَى ٱلْمَلَٰٓئِكَةِ أَنِّى مَعَكُمْ فَثَبِّتُوا۟ ٱلَّذِينَ ءَامَنُوا۟ ۚ سَأُلْقِى فِى قُلُوبِ ٱلَّذِينَ كَفَرُوا۟ ٱلرُّعْبَ فَٱضْرِبُوا۟ فَوْقَ ٱلْأَعْنَاقِ وَٱضْرِبُوا۟ مِنْهُمْ كُلَّ بَنَانٍۢ
- (8:13) [next to 8:11] ذَٰلِكَ بِأَنَّهُمْ شَآقُّوا۟ ٱللَّهَ وَرَسُولَهُۥ ۚ وَمَن يُشَاقِقِ ٱللَّهَ وَرَسُولَهُۥ فَإِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- (12:103) [next to 12:105] وَمَآ أَكْثَرُ ٱلنَّاسِ وَلَوْ حَرَصْتَ بِمُؤْمِنِينَ
- (12:104) [next to 12:105] وَمَا تَسْـَٔلُهُمْ عَلَيْهِ مِنْ أَجْرٍ ۚ إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
- (12:106) [next to 12:105] وَمَا يُؤْمِنُ أَكْثَرُهُم بِٱللَّهِ إِلَّا وَهُم مُّشْرِكُونَ
- (12:108) [next to 12:107] قُلْ هَٰذِهِۦ سَبِيلِىٓ أَدْعُوٓا۟ إِلَى ٱللَّهِ ۚ عَلَىٰ بَصِيرَةٍ أَنَا۠ وَمَنِ ٱتَّبَعَنِى ۖ وَسُبْحَٰنَ ٱللَّهِ وَمَآ أَنَا۠ مِنَ ٱلْمُشْرِكِينَ
- (12:109) [next to 12:107] وَمَآ أَرْسَلْنَا مِن قَبْلِكَ إِلَّا رِجَالًۭا نُّوحِىٓ إِلَيْهِم مِّنْ أَهْلِ ٱلْقُرَىٰٓ ۗ أَفَلَمْ يَسِيرُوا۟ فِى ٱلْأَرْضِ فَيَنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلَّذِينَ مِن قَبْلِهِمْ ۗ وَلَدَارُ ٱلْءَاخِرَةِ خَيْرٌۭ لِّلَّذِينَ ٱتَّقَوْا۟ ۗ أَفَلَا تَعْقِلُونَ
- (16:0) [next to 16:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (16:2) [next to 16:1] يُنَزِّلُ ٱلْمَلَٰٓئِكَةَ بِٱلرُّوحِ مِنْ أَمْرِهِۦ عَلَىٰ مَن يَشَآءُ مِنْ عِبَادِهِۦٓ أَنْ أَنذِرُوٓا۟ أَنَّهُۥ لَآ إِلَٰهَ إِلَّآ أَنَا۠ فَٱتَّقُونِ
- (16:3) [next to 16:1] خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۚ تَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (20:7) [next to 20:9] وَإِن تَجْهَرْ بِٱلْقَوْلِ فَإِنَّهُۥ يَعْلَمُ ٱلسِّرَّ وَأَخْفَى
- (20:8) [next to 20:9] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ
- (20:10) [next to 20:9] إِذْ رَءَا نَارًۭا فَقَالَ لِأَهْلِهِ ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى
- (20:11) [next to 20:9] فَلَمَّآ أَتَىٰهَا نُودِىَ يَٰمُوسَىٰٓ
- (20:75) [next to 20:77] وَمَن يَأْتِهِۦ مُؤْمِنًۭا قَدْ عَمِلَ ٱلصَّٰلِحَٰتِ فَأُو۟لَٰٓئِكَ لَهُمُ ٱلدَّرَجَٰتُ ٱلْعُلَىٰ
- (20:76) [next to 20:77] جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ
- (20:79) [next to 20:77] وَأَضَلَّ فِرْعَوْنُ قَوْمَهُۥ وَمَا هَدَىٰ
- (20:80) [next to 20:78] يَٰبَنِىٓ إِسْرَٰٓءِيلَ قَدْ أَنجَيْنَٰكُم مِّنْ عَدُوِّكُمْ وَوَٰعَدْنَٰكُمْ جَانِبَ ٱلطُّورِ ٱلْأَيْمَنَ وَنَزَّلْنَا عَلَيْكُمُ ٱلْمَنَّ وَٱلسَّلْوَىٰ
- (21:0) [next to 21:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (21:3) [next to 21:1] لَاهِيَةًۭ قُلُوبُهُمْ ۗ وَأَسَرُّوا۟ ٱلنَّجْوَى ٱلَّذِينَ ظَلَمُوا۟ هَلْ هَٰذَآ إِلَّا بَشَرٌۭ مِّثْلُكُمْ ۖ أَفَتَأْتُونَ ٱلسِّحْرَ وَأَنتُمْ تُبْصِرُونَ
- (21:4) [next to 21:2] قَالَ رَبِّى يَعْلَمُ ٱلْقَوْلَ فِى ٱلسَّمَآءِ وَٱلْأَرْضِ ۖ وَهُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (23:42) [next to 23:44] ثُمَّ أَنشَأْنَا مِنۢ بَعْدِهِمْ قُرُونًا ءَاخَرِينَ
- (23:43) [next to 23:44] مَا تَسْبِقُ مِنْ أُمَّةٍ أَجَلَهَا وَمَا يَسْتَـْٔخِرُونَ
- (23:45) [next to 23:44] ثُمَّ أَرْسَلْنَا مُوسَىٰ وَأَخَاهُ هَٰرُونَ بِـَٔايَٰتِنَا وَسُلْطَٰنٍۢ مُّبِينٍ
- (23:46) [next to 23:44] إِلَىٰ فِرْعَوْنَ وَمَلَإِي۟هِۦ فَٱسْتَكْبَرُوا۟ وَكَانُوا۟ قَوْمًا عَالِينَ
- (29:51) [next to 29:53] أَوَلَمْ يَكْفِهِمْ أَنَّآ أَنزَلْنَا عَلَيْكَ ٱلْكِتَٰبَ يُتْلَىٰ عَلَيْهِمْ ۚ إِنَّ فِى ذَٰلِكَ لَرَحْمَةًۭ وَذِكْرَىٰ لِقَوْمٍۢ يُؤْمِنُونَ
- (29:52) [next to 29:53] قُلْ كَفَىٰ بِٱللَّهِ بَيْنِى وَبَيْنَكُمْ شَهِيدًۭا ۖ يَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۗ وَٱلَّذِينَ ءَامَنُوا۟ بِٱلْبَٰطِلِ وَكَفَرُوا۟ بِٱللَّهِ أُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (29:54) [next to 29:53] يَسْتَعْجِلُونَكَ بِٱلْعَذَابِ وَإِنَّ جَهَنَّمَ لَمُحِيطَةٌۢ بِٱلْكَٰفِرِينَ
- (29:56) [next to 29:55] يَٰعِبَادِىَ ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّ أَرْضِى وَٰسِعَةٌۭ فَإِيَّٰىَ فَٱعْبُدُونِ
- (29:57) [next to 29:55] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۖ ثُمَّ إِلَيْنَا تُرْجَعُونَ
- (34:17) [next to 34:19] ذَٰلِكَ جَزَيْنَٰهُم بِمَا كَفَرُوا۟ ۖ وَهَلْ نُجَٰزِىٓ إِلَّا ٱلْكَفُورَ
- (34:18) [next to 34:19] وَجَعَلْنَا بَيْنَهُمْ وَبَيْنَ ٱلْقُرَى ٱلَّتِى بَٰرَكْنَا فِيهَا قُرًۭى ظَٰهِرَةًۭ وَقَدَّرْنَا فِيهَا ٱلسَّيْرَ ۖ سِيرُوا۟ فِيهَا لَيَالِىَ وَأَيَّامًا ءَامِنِينَ
- (34:20) [next to 34:19] وَلَقَدْ صَدَّقَ عَلَيْهِمْ إِبْلِيسُ ظَنَّهُۥ فَٱتَّبَعُوهُ إِلَّا فَرِيقًۭا مِّنَ ٱلْمُؤْمِنِينَ
- (34:21) [next to 34:19] وَمَا كَانَ لَهُۥ عَلَيْهِم مِّن سُلْطَٰنٍ إِلَّا لِنَعْلَمَ مَن يُؤْمِنُ بِٱلْءَاخِرَةِ مِمَّنْ هُوَ مِنْهَا فِى شَكٍّۢ ۗ وَرَبُّكَ عَلَىٰ كُلِّ شَىْءٍ حَفِيظٌۭ
- (44:8) [next to 44:10] لَآ إِلَٰهَ إِلَّا هُوَ يُحْىِۦ وَيُمِيتُ ۖ رَبُّكُمْ وَرَبُّ ءَابَآئِكُمُ ٱلْأَوَّلِينَ
- (44:9) [next to 44:10] بَلْ هُمْ فِى شَكٍّۢ يَلْعَبُونَ
- (44:12) [next to 44:10] رَّبَّنَا ٱكْشِفْ عَنَّا ٱلْعَذَابَ إِنَّا مُؤْمِنُونَ
- (44:13) [next to 44:11] أَنَّىٰ لَهُمُ ٱلذِّكْرَىٰ وَقَدْ جَآءَهُمْ رَسُولٌۭ مُّبِينٌۭ
- (45:21) [next to 45:23] أَمْ حَسِبَ ٱلَّذِينَ ٱجْتَرَحُوا۟ ٱلسَّيِّـَٔاتِ أَن نَّجْعَلَهُمْ كَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ سَوَآءًۭ مَّحْيَاهُمْ وَمَمَاتُهُمْ ۚ سَآءَ مَا يَحْكُمُونَ
- (45:22) [next to 45:23] وَخَلَقَ ٱللَّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ وَلِتُجْزَىٰ كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ وَهُمْ لَا يُظْلَمُونَ
- (45:24) [next to 45:23] وَقَالُوا۟ مَا هِىَ إِلَّا حَيَاتُنَا ٱلدُّنْيَا نَمُوتُ وَنَحْيَا وَمَا يُهْلِكُنَآ إِلَّا ٱلدَّهْرُ ۚ وَمَا لَهُم بِذَٰلِكَ مِنْ عِلْمٍ ۖ إِنْ هُمْ إِلَّا يَظُنُّونَ
- (45:25) [next to 45:23] وَإِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَٰتُنَا بَيِّنَٰتٍۢ مَّا كَانَ حُجَّتَهُمْ إِلَّآ أَن قَالُوا۟ ٱئْتُوا۟ بِـَٔابَآئِنَآ إِن كُنتُمْ صَٰدِقِينَ
- (47:18) [next to 47:20] فَهَلْ يَنظُرُونَ إِلَّا ٱلسَّاعَةَ أَن تَأْتِيَهُم بَغْتَةًۭ ۖ فَقَدْ جَآءَ أَشْرَاطُهَا ۚ فَأَنَّىٰ لَهُمْ إِذَا جَآءَتْهُمْ ذِكْرَىٰهُمْ
- (47:19) [next to 47:20] فَٱعْلَمْ أَنَّهُۥ لَآ إِلَٰهَ إِلَّا ٱللَّهُ وَٱسْتَغْفِرْ لِذَنۢبِكَ وَلِلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ ۗ وَٱللَّهُ يَعْلَمُ مُتَقَلَّبَكُمْ وَمَثْوَىٰكُمْ
- (47:21) [next to 47:20] طَاعَةٌۭ وَقَوْلٌۭ مَّعْرُوفٌۭ ۚ فَإِذَا عَزَمَ ٱلْأَمْرُ فَلَوْ صَدَقُوا۟ ٱللَّهَ لَكَانَ خَيْرًۭا لَّهُمْ
- (47:22) [next to 47:20] فَهَلْ عَسَيْتُمْ إِن تَوَلَّيْتُمْ أَن تُفْسِدُوا۟ فِى ٱلْأَرْضِ وَتُقَطِّعُوٓا۟ أَرْحَامَكُمْ
- (51:22) [next to 51:24] وَفِى ٱلسَّمَآءِ رِزْقُكُمْ وَمَا تُوعَدُونَ
- (51:23) [next to 51:24] فَوَرَبِّ ٱلسَّمَآءِ وَٱلْأَرْضِ إِنَّهُۥ لَحَقٌّۭ مِّثْلَ مَآ أَنَّكُمْ تَنطِقُونَ
- (51:25) [next to 51:24] إِذْ دَخَلُوا۟ عَلَيْهِ فَقَالُوا۟ سَلَٰمًۭا ۖ قَالَ سَلَٰمٌۭ قَوْمٌۭ مُّنكَرُونَ
- (51:26) [next to 51:24] فَرَاغَ إِلَىٰٓ أَهْلِهِۦ فَجَآءَ بِعِجْلٍۢ سَمِينٍۢ
- (53:48) [next to 53:50] وَأَنَّهُۥ هُوَ أَغْنَىٰ وَأَقْنَىٰ
- (53:49) [next to 53:50] وَأَنَّهُۥ هُوَ رَبُّ ٱلشِّعْرَىٰ
- (53:51) [next to 53:50] وَثَمُودَا۟ فَمَآ أَبْقَىٰ
- (53:52) [next to 53:50] وَقَوْمَ نُوحٍۢ مِّن قَبْلُ ۖ إِنَّهُمْ كَانُوا۟ هُمْ أَظْلَمَ وَأَطْغَىٰ
- (53:53) [next to 53:54] وَٱلْمُؤْتَفِكَةَ أَهْوَىٰ
- (53:55) [next to 53:54] فَبِأَىِّ ءَالَآءِ رَبِّكَ تَتَمَارَىٰ
- (53:61) [next to 53:59] وَأَنتُمْ سَٰمِدُونَ
- (79:13) [next to 79:15] فَإِنَّمَا هِىَ زَجْرَةٌۭ وَٰحِدَةٌۭ
- (79:14) [next to 79:15] فَإِذَا هُم بِٱلسَّاهِرَةِ
- (79:16) [next to 79:15] إِذْ نَادَىٰهُ رَبُّهُۥ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًى
- (79:17) [next to 79:15] ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ
- (83:12) [next to 83:14] وَمَا يُكَذِّبُ بِهِۦٓ إِلَّا كُلُّ مُعْتَدٍ أَثِيمٍ
- (83:13) [next to 83:14] إِذَا تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا قَالَ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- (83:15) [next to 83:14] كَلَّآ إِنَّهُمْ عَن رَّبِّهِمْ يَوْمَئِذٍۢ لَّمَحْجُوبُونَ
- (83:16) [next to 83:14] ثُمَّ إِنَّهُمْ لَصَالُوا۟ ٱلْجَحِيمِ
- (85:15) [next to 85:17] ذُو ٱلْعَرْشِ ٱلْمَجِيدُ
- (85:16) [next to 85:17] فَعَّالٌۭ لِّمَا يُرِيدُ
- (85:19) [next to 85:17] بَلِ ٱلَّذِينَ كَفَرُوا۟ فِى تَكْذِيبٍۢ
- (85:20) [next to 85:18] وَٱللَّهُ مِن وَرَآئِهِم مُّحِيطٌۢ

