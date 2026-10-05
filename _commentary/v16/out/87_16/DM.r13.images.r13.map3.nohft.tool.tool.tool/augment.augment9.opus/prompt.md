Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:16; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_16/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_16.reading.tr.md (prose paragraphs numbered) =====
## "Bel": cümlenin döndüğü yer

[¶1] Surenin on dördüncü ve on beşinci ayetleri kurtuluşa ereni üç fiille anlatır: arındı, Rabbinin adını andı, namaz kıldı. Üçü de geçmiş zamandadır, tamamlanmış ve kapanmış işlerdir. On altıncı ayet bu tablonun hemen ardından gelir ve iki şeyi birden değiştirir. Önce konuşulan kişi değişir. Sure o ana kadar ya Peygamber'e tekil "sen" diye seslenmiş (tesbih et, sana okutacağız, öğüt ver) ya da "kim arınırsa" diyerek üçüncü bir kişiden söz etmişti. Şimdi birden çoğul bir "siz" gelir. Dokuzuncu ayette Peygamber'e kimlere öğüt götürmesi emredildiyse söz artık doğrudan onlara döner. Sonra zaman değişir: {ar:تُؤْثِرُونَ, tr:tü'sirûne, gloss:öne koyuyorsunuz, tercih ediyorsunuz, source:87:16} şimdiki ve geniş zamanı birlikte taşır. Bir kerelik bir kararı değil, süregiden bir hali, her gün yeniden yapılan bir sıralamayı anlatır.

[¶2] Cümleyi açan {ar:بَلْ, tr:bel, gloss:hayır, asıl durum şu ki, source:87:16}, söylenmiş olanı bir yana bırakıp asıl duruma geçer. Kurtuluşun yolu az önce açıkça söylenmiştir. "Bel" dinleyenlerin o yolda olmadığını bildirir ve nedenini de söyler. Burada dikkat çeken bir şey var: ayet dinleyenleri inkârla da bilgisizlikle de suçlamaz. Onlara yüklediği şey bir sıralamadır. Ne olduğunu biliyorlar, ama neyi öne koyacaklarını yanlış seçiyorlar. On birinci ayet öğütten {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebühe'l-eşkâ, gloss:en bedbaht olan ondan uzak durur, source:87:11} demişti. Bu uzak durmanın altında yatan hal burada adını bulur: önü başka bir şey kapatmıştır.

[¶3] Arapçada bu fiil normalde iki şey ister: neyin, neye karşı öne konduğu. Ayet ikincisini söylemez. Öne konan bellidir, ama neyin karşısında öne konduğu açıkta kalır. Boşluğu on yedinci ayet doldurur ve bunu fiille değil, fiilsiz bir isim cümlesiyle yapar: {ar:وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:ve'l-âhiratü hayrun ve ebkâ, gloss:oysa ahiret daha hayırlı ve daha kalıcıdır, source:87:17}. Süregiden bir davranışa zamana bağlı olmayan bir hüküm karşılık verir. Onlar her gün yeniden sıralar, ahiret ise sıralamadan bağımsız olarak hep aynı yerde durur.

[¶4] Aynı kuruluş Kur'an'da bir başka surede, şaşırtıcı ölçüde benzer bir yerde karşımıza çıkar. Orada Allah Peygamber'e vahyi aceleyle tekrarlamamasını söyler: {ar:لَا تُحَرِّكْ بِهِۦ لِسَانَكَ لِتَعْجَلَ بِهِۦٓ, tr:lâ tüharrik bihî lisâneke li-ta'cele bih, gloss:onu aceleyle almak için dilini kıpırdatma, source:75:16}, {ar:إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ, tr:inne aleynâ cem'ahû ve kur'ânehû, gloss:onu toplamak ve okutmak bize düşer, source:75:17}. Birkaç ayet sonra söz insanlara döner: {ar:كَلَّا بَلْ تُحِبُّونَ ٱلْعَاجِلَةَ, tr:kellâ bel tühibbûne'l-âcile, gloss:hayır; siz çabucak geleni seviyorsunuz, source:75:20}, {ar:وَتَذَرُونَ ٱلْءَاخِرَةَ, tr:ve tezerûne'l-âhira, gloss:ve sonra geleni bırakıyorsunuz, source:75:21}. İki surede de önce Peygamber'e okunan sözün korunacağı vaat edilir. Bizim surede bu vaat altıncı ayette, "sana okutacağız da unutmayacaksın" sözüyle gelir. Ardından bir "bel" gelir ve çoğul "siz"in neyi öne koyduğu söylenir. Söz korunur, ama dinleyenin gözü yakındadır.

## Başköşeyi vermek

[¶5] Türkçe çeviri burada "tercih" der. Bu kelime terazinin bir kefesini ağır bastırma fikrinden gelir, yani soğuk bir tartmayı anlatır. Ayetteki fiilin merkezinde ise tartı değil, ağırlama vardır. Araplar sevip başköşeye oturttukları kişiye bu kökten bir adla seslenirdi: {ar:الأثير الكريم عليك الذي تؤثره بفضلك وصلتك, tr:el-esîru'l-kerîmu aleyke'llezî tü'sirühû bi-fadlike ve sılatik, gloss:esîr senin gözünde değerli olandır; ona ikramını ve bağışını öncelikle verirsin, source:"ء ث ر,B005"}. "Tü'sirûne" demek, yakın hayata bu yeri vermek demektir: ikramın ilk ona gider, bağış önce ona ayrılır. Fiilin kökünde bir de öne koyma vardır: {ar:له أصل تقديم الشيء, tr:lehû aslu takdîmi'ş-şey', gloss:bir şeyi öne koyma anlamında bir kökü vardır, source:"ء ث ر,B001"}. "Her şeyden önce" anlamına gelen kalıp da bu köktendir: {ar:آثرا ما وآثر ذي أثير أي أول كل شيء, tr:âsiran mâ ve âsira zî esîr, ey evvele külli şey', gloss:her şeyden önce, ilk iş olarak, source:"ء ث ر,B001"}. Bir işe kendini veren kişi için de şöyle denirdi: {ar:وقد أثر أن يفعل ذلك الأمر أي فرغ له وعزم عليه, tr:ve kad esira en yef'ale zâlike'l-emr, ey ferağa lehû ve azeme aleyh, gloss:o işi yapmaya karar verdi; kendini ona ayırıp kesin niyet etti, source:"ء ث ر,B001"}. Böylece fiilin içinde üç hareket birlikte duyulur: öne koymak, başköşeyi vermek, insanın kendini o şeye ayırması. Bu duyulanlar fiilin ayetteki anlamının yerini almaz, onun yanında işitilir. Ayet yine de "dünya hayatını tercih ediyorsunuz" der. Ama bu tercihin bir sevgi ve bir yer verme olduğu da kulağa gelir.

[¶6] Türkçede aynı kelimeden gelen "îsar" yalnızca bir erdemin adı olarak kalmıştır: kişinin başkasını kendine tercih etmesi. Arapça fiil ise yön bakımından tarafsızdır. İyi ya da kötü olması, neyin öne konduğuna bağlıdır. Kur'an iki yönü de gösterir. Yusuf'un kardeşleri yıllar sonra kıtlık yüzünden Mısır'a gelir ve karşılarındaki yöneticinin Yusuf olduğunu anlayınca şöyle derler: {ar:تَٱللَّهِ لَقَدْ ءَاثَرَكَ ٱللَّهُ عَلَيْنَا, tr:tallâhi lekad âserakallâhü aleynâ, gloss:Allah'a andolsun, Allah seni bize üstün tuttu, source:12:91}. Burada öne koyan Allah'tır. Bir başka yerde Kur'an, yurtlarından ve mallarından çıkarılıp göç edenleri barındıran yerleşik topluluğu anlatır. Bu insanlar kendilerine gelenleri sever, onlara verilenden içlerinde bir kıskançlık duymaz ve {ar:وَيُؤْثِرُونَ عَلَىٰٓ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌۭ, tr:ve yü'sirûne alâ enfüsihim ve lev kâne bihim hasâsa, gloss:kendileri yoksulluk içinde olsalar bile onları kendilerine tercih ederler, source:59:9}. Ayet {ar:فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ, tr:fe-ülâike hümü'l-müflihûn, gloss:işte kurtuluşa erenler onlardır, source:59:9} diye biter. Bizim surenin on dördüncü ayetindeki "kurtuluşa erdi" fiili de bu köktendir. Aynı fiil o ayette insanı kurtuluşa götürür, bizim ayette ise kurtuluşun yolundan çevirir. Aradaki fark yalnızca neyin başköşeye oturtulduğudur.

[¶7] Fiilin bir türevi daha bu sahneye ışık tutar. Bir şeyi başkalarını dışarıda bırakarak kendine ayıran, arkadaşlarının hakkını da kendine çeken kişiye {ar:رجل أثر وهو الذي يستأثر على أصحابه, tr:racülün esirun ve hüve'llezî yeste'sirü alâ ashâbih, gloss:esir adam, arkadaşlarını dışarıda bırakıp her şeyi kendine ayırandır, source:"ء ث ر,B006"} denirdi. Aynı fiil Allah için de kullanılırdı: {ar:استأثر الله بالبقاء أي انفرد بالبقاء, tr:iste'serallâhü bi'l-bekâ', ey infarade bi'l-bekâ', gloss:Allah kalıcılığı kendine ayırdı, yani kalıcılıkta tektir, source:"ء ث ر,B006"}. Bu söyleyişte, tercih fiilinin kendi ailesi kalıcılığı yalnızca Allah'a ait bir şey olarak anar. On yedinci ayet de ahireti tam bu sıfatla, "daha kalıcı" diye niteler. Yakın hayatı öne koyan, elinde tutamayacağı bir şeyi kendine ayırmaya çalışır. Kalıcılık ise dilin kendi deyişiyle bile başkasınındır.

[¶8] Kur'an bu fiili ayetimizin dört kelimesiyle birlikte bir tehdit sahnesinde kullanır. Firavun Musa'nın karşısına çıkarmak için sihirbazları toplamıştır. Musa'nın değneği onların yaptıklarını yutunca sihirbazlar secdeye kapanıp iman ederler. Firavun ellerini ve ayaklarını çaprazlama kestirip onları hurma kütüklerine asacağını söyler. Sihirbazların cevabı şudur: {ar:قَالُوا۟ لَن نُّؤْثِرَكَ عَلَىٰ مَا جَآءَنَا مِنَ ٱلْبَيِّنَٰتِ وَٱلَّذِى فَطَرَنَا ۖ فَٱقْضِ مَآ أَنتَ قَاضٍ ۖ إِنَّمَا تَقْضِى هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:kâlû len nü'sirake alâ mâ câenâ mine'l-beyyinâti ve'llezî fataranâ, fakdı mâ ente kâd, innemâ takdî hâzihi'l-hayâte'd-dünyâ, gloss:bize gelen apaçık delillere ve bizi yaratana seni asla tercih etmeyiz; vereceğin hükmü ver; sen ancak bu dünya hayatında hüküm verebilirsin dediler, source:20:72}. Sözlerini şöyle bağlarlar: {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhü hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73}. Bizim ayette söylenmeyen "neye karşı" sorusu onların ağzında açıkça söylenir: apaçık delillere ve yaratana karşı. Cümlede bir şey daha var: yakın hayat, Firavun'un hükmünün ulaşabildiği yerdir. Onu başköşeye oturtan, kendini her Firavun'un hükmünün erişebileceği yere koyar. Sihirbazlar ise tercihlerini tam o hükmün yetmediği yere taşır.

[¶9] Bir başka surede aynı fiil, büyük felaketin geldiği ve {ar:يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ, tr:yevme yetezekkerü'l-insânü mâ seâ, gloss:insanın neyin peşinde koştuğunu hatırladığı gün, source:79:35} diye anılan günün hesabında yer alır: {ar:فَأَمَّا مَن طَغَىٰ, tr:fe-emmâ men tağâ, gloss:azana gelince, source:79:37}, {ar:وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:ve âsera'l-hayâte'd-dünyâ, gloss:ve dünya hayatını tercih edene, source:79:38}, {ar:فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ, tr:fe-inne'l-cahîme hiye'l-me'vâ, gloss:artık barınağı cehennemdir, source:79:39}. Karşı tarafta ise {ar:وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ, tr:ve emmâ men hâfe makâme rabbihî ve nehe'n-nefse ani'l-hevâ, gloss:Rabbinin huzurunda duracağından korkan ve nefsini hevesten alıkoyana gelince, source:79:40} vardır. Orada fiil geçmiş zamandadır, çünkü hesap kapanmıştır ve söylenen sonuçtur. Bizim ayette ise fiil süren zamandadır ve "siz" diye doğrudan seslenilir. Sıralama hâlâ değiştirilebilir.

## Yakın olan hayat

[¶10] Türkçede "dünya" bir isimdir: üzerinde yaşadığımız küre, haritası ve coğrafyası olan bir yer. Ayette ise {ar:ٱلدُّنْيَا, tr:ed-dünyâ, gloss:daha yakın olan, source:87:16} hayatı niteleyen bir sıfattır: "daha yakın" anlamındaki edna'nın dişil biçimidir. "El-hayâtü'd-dünyâ" sözü kelimesi kelimesine "yakın hayat", "berideki hayat" demektir. Adın nedenini Araplar açıkça söylerdi: {ar:سميت الدنيا لدنوها, tr:sümmiyeti'd-dünyâ li-dünüvvihâ, gloss:dünyâya yakınlığından ötürü bu ad verildi, source:"د ن و,B002"}. Bu yüzden kelime her zaman bir "uzak" olanı gerektirir. Bir yer bildirmez, bir mesafe bildirir. Türkçedeki "dünya" bu karşılaştırmayı artık taşımaz. Ayetteki kelime ise ancak yanında bir ötesi bulunduğu için yakındır.

[¶11] Kur'an bu kelimeyi hiçbir mecaz katmadan, düpedüz bir arazi tarifinde de kullanır. Allah müminlere iki topluluğun karşılaştığı günü hatırlatırken şöyle der: {ar:إِذْ أَنتُم بِٱلْعُدْوَةِ ٱلدُّنْيَا وَهُم بِٱلْعُدْوَةِ ٱلْقُصْوَىٰ, tr:iz entüm bi'l-udveti'd-dünyâ ve hüm bi'l-udveti'l-kusvâ, gloss:o gün siz vadinin yakın yamacındaydınız, onlar uzak yamacındaydı, source:8:42}. Burada "dünyâ" yalnızca bir yamaçtır, karşısında uzak bir yamaç vardır. Aynı ayet o karşılaşmanın amacını da söyler: {ar:وَيَحْيَىٰ مَنْ حَىَّ عَنۢ بَيِّنَةٍۢ, tr:ve yahyâ men hayye an beyyine, gloss:yaşayan da apaçık bir delil üzerine yaşasın diye, source:8:42}. Bir ayetin içinde hem yakın yamaç hem de yaşamak fiili geçer. Yaşamayı belirleyen şey ise kişinin hangi yamaçta durduğu değil, apaçık delildir.

[¶12] Kelimenin bir başka kullanımı da onu ilk olanla eşler. {ar:يعبر بالأدنى تارة عن الأصغر وتارة عن الأول وتارة عن الأقرب, tr:yu'abbaru bi'l-ednâ târaten ani'l-asğar ve târaten ani'l-evvel ve târaten ani'l-akrab, gloss:edna bazen daha küçüğü, bazen ilki, bazen en yakını anlatır, source:"د ن و,B002"}. Biriyle karşılaştığında yaptığı ilk iş için Arap {ar:لقيته أدنى دنى أي أول شيء, tr:lakıytühû ednâ denî, ey evvele şey', gloss:onunla karşılaştım, ilk iş olarak, source:"د ن و,B002"} derdi. Tercih fiilinin kökünde de "her şeyden önce" anlamına gelen bir kalıp vardı. Ayetin iki kelimesi böylece aynı yere bakar: öne konan şey zaten önde olandır. Yakın hayat zaman bakımından zaten ilktir. Hata, onu değer bakımından da ilk sıraya koymaktır. Ahiretin adı ise "sonra gelen" demektir. Surenin bütününde, on beşinci ayetin namaz kılanı ile on yedinci ayetin "sonra gelen"i arasında, önde koşanın yarışı kazanmadığı bir at dizisi de duyulur. Bu sahnenin yeri surenin bütününü ele alan okumadır.

[¶13] Aynı kök, dişi devenin ya da kısrağın doğumunun yaklaşmasını da adlandırır: {ar:أدنت الناقة إذا دنا نتاجها, tr:edneti'n-nâkatü izâ denâ nitâcühâ, gloss:dişi devenin doğumu yaklaştı, source:"د ن و,B004"}. Burada yakınlık bir dinlenme yeri değildir, bir sonuca yaklaşmaktır. İçindeki şey dışarı çıkmak üzeredir. Bu kullanım ayetteki kelimenin anlamı olmasa da onun yanında, bir benzetme olarak şunu duyurur: yakın hayat da kendinden doğacak bir şeye yakındır, vadesi gelmek üzeredir. Surenin ikinci ayetindeki biçimlendirme ve altıncı ayetteki "okutma" fiillerinde de rahim ve doğum yankılanır. Bu kelime o insan ömrü sahnesinde kendi yerini alır.

[¶14] Kökün bir de aşağı tarafı vardır. İnsanlardan zayıf ve değersiz olana {ar:الدني من الرجال الضعيف الدون, tr:ed-deniyyü mine'r-ricâli'd-daîfü'd-dûn, gloss:insanların denîsi zayıf ve aşağı olandır, source:"د ن و,B003"} denirdi. İşlerin küçüğünün ve bayağısının peşine düşen için {ar:يدني في الأمور تدنية أي يتتبع صغيرها وخسيسها, tr:yüdennî fi'l-umûri tedniyeten, ey yetetebbau sağîrahâ ve hasîsehâ, gloss:işlerde ufak ve bayağı olanın peşinden gider, source:"د ن و,B003"} denirdi. Edna, en aşağılık olanı anlatmak için de kullanılırdı: {ar:الأدنى عن الأرذل, tr:el-ednâ ani'l-erzel, gloss:edna en bayağı olanı da anlatır, source:"د ن و,B003"}. Sure "en yüce" olan Rabbin adıyla açılmıştı. Burada "aşağıdaki" hayatı anar. Bu iki kelimenin aynı eksenin iki ucunda durduğu sahne surenin bütününe aittir.

[¶15] Bu aşağılık ile yakınlık Kur'an'da tek bir sahnede, üstelik surenin son ayetinde adı geçen Musa'nın ağzından birleşir. İsrailoğulları çölde bulut gölgesinde yaşamakta, kendilerine kudret helvası ve bıldırcın indirilmektedir. Onlar Musa'ya şöyle derler: {ar:لَن نَّصْبِرَ عَلَىٰ طَعَامٍۢ وَٰحِدٍۢ فَٱدْعُ لَنَا رَبَّكَ يُخْرِجْ لَنَا مِمَّا تُنۢبِتُ ٱلْأَرْضُ مِنۢ بَقْلِهَا وَقِثَّآئِهَا وَفُومِهَا وَعَدَسِهَا وَبَصَلِهَا, tr:len nasbira alâ taâmin vâhidin fed'u lenâ rabbeke yuhric lenâ mimmâ tünbitü'l-ardu min baklihâ ve kıssâihâ ve fûmihâ ve adesihâ ve basalihâ, gloss:tek bir yemeğe dayanamayız; Rabbine dua et de bize yerin bitirdiklerinden, sebzesinden, hıyarından, sarımsağından, merciminden ve soğanından çıkarsın, source:2:61}. Musa'nın cevabı şudur: {ar:أَتَسْتَبْدِلُونَ ٱلَّذِى هُوَ أَدْنَىٰ بِٱلَّذِى هُوَ خَيْرٌ, tr:e-testebdilûne'llezî hüve ednâ bi'llezî hüve hayr, gloss:daha aşağı olanı daha hayırlı olanla değiştirmek mi istiyorsunuz, source:2:61}. Bu cümlede "edna" ve "hayr", yani bizim on altıncı ve on yedinci ayetlerimizin iki kutbu yan yana gelir. İstenen şey de yerin bitirdiğidir, surenin dördüncü ayetindeki otlak gibi elin altındaki yeşilliktir. Aşağı olan burada hem yakındır, çünkü yerden biter, hem de daha değersizdir. Musa onlara {ar:ٱهْبِطُوا۟ مِصْرًۭا, tr:ihbitû mısran, gloss:bir şehre inin, source:2:61} der. Aşağı olana inilerek varılır.

[¶16] Kur'an aynı kavmin sonraki kuşaklarını da bu kelimeyle anlatır. Kitabı miras alan bir nesil hakkında şöyle denir: {ar:يَأْخُذُونَ عَرَضَ هَٰذَا ٱلْأَدْنَىٰ وَيَقُولُونَ سَيُغْفَرُ لَنَا, tr:ye'huzûne arada hâze'l-ednâ ve yekûlûne seyuğfaru lenâ, gloss:bu yakın olanın geçici malını alıyor ve bizim günahımız bağışlanacak diyorlar, source:7:169}. Ayet onların kitabın içindekini okuyup öğrendiklerini de söyler ve şöyle biter: {ar:وَٱلدَّارُ ٱلْءَاخِرَةُ خَيْرٌۭ لِّلَّذِينَ يَتَّقُونَ ۗ أَفَلَا تَعْقِلُونَ, tr:ve'd-dârü'l-âhiratü hayrun li'llezîne yettekûn, e-felâ ta'kılûn, gloss:sakınanlar için ahiret yurdu daha hayırlıdır; aklınızı kullanmaz mısınız, source:7:169}. Hemen ardından gelen ayet karşı tarafı anlatır: {ar:وَٱلَّذِينَ يُمَسِّكُونَ بِٱلْكِتَٰبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ, tr:ve'llezîne yümessikûne bi'l-kitâbi ve ekâmü's-salâh, gloss:kitaba sımsıkı sarılanlar ve namazı dosdoğru kılanlar, source:7:170}. Kitabı okumuş olmak tek başına sıralamayı düzeltmez. Bizim sure de "bu ilk sayfalarda vardır" diyerek kapanır. Yine de kurtuluşa ereni sayfaları bilmesiyle değil, Rabbinin adını anıp namaz kılmasıyla tanımlar. Bir şey daha dikkat çekici: 7:169 "bu yakın olan" der, sihirbazlar da "bu dünya hayatı" demişti. İşaret zamiri elin altındaki şeyi gösterir. Yakın hayat parmakla gösterilebilecek kadar yakındır.

## Hayat dediğimiz şey

[¶17] {ar:ٱلْحَيَوٰةَ, tr:el-hayâte, gloss:hayatı, source:87:16} ilk bakışta ölümün karşıtıdır: {ar:الحياة ضد الموت والحي ضد الميت, tr:el-hayâtü ziddü'l-mevt ve'l-hayyü ziddü'l-meyyit, gloss:hayat ölümün, diri de ölünün karşıtıdır, source:"ح ي ي,B001"}. Ama Araplar bu kökü yeşeren şeyler için de kullanırdı. Yağmura hayâ derlerdi: {ar:يسمى المطر حيا لأن به حياة الأرض, tr:yüsemma'l-matarü hayan li-enne bihî hayâte'l-ard, gloss:yağmura hayâ denir, çünkü toprağın hayatı onunladır, source:"ح ي ي,B002"}. Bitkinin taze olanına "diri" derlerdi: {ar:الحي من النبات ما كان طريا يهتز, tr:el-hayyü mine'n-nebâti mâ kâne tariyyen yehtezz, gloss:bitkinin dirisi taze olup salınandır, source:"ح ي ي,B002"}. Böylece "yakın hayat" sözü, rüzgârda salınan taze ot görüntüsünü de yanında taşır. Sure bu otu dördüncü ve beşinci ayetlerde zaten göstermişti: Rab otlağı çıkarır, sonra onu kararmış bir çerçöpe çevirir. O sahnenin bütünü surenin okumasına aittir. Burada önemli olan şu: tercih edilen hayat, adında bile o salınan yeşilliğin hayatıdır.

[¶18] Kur'an bu benzetmeyi açıkça kurar. Allah Peygamber'e şöyle der: {ar:وَٱضْرِبْ لَهُم مَّثَلَ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ فَأَصْبَحَ هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ, tr:vadrib lehüm meselel-hayâti'd-dünyâ ke-mâin enzelnâhü mine's-semâi fahtalata bihî nebâtü'l-ardi fe-asbaha heşîmen tezrûhü'r-riyâh, gloss:onlara dünya hayatının örneğini ver: gökten indirdiğimiz bir su gibidir; yerin bitkisi onunla karışıp gürleşir, sonra rüzgârların savurduğu kuru çöpe döner, source:18:45}. Hemen ardından şöyle gelir: {ar:ٱلْمَالُ وَٱلْبَنُونَ زِينَةُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا, tr:el-mâlü ve'l-benûne zînetü'l-hayâti'd-dünyâ, ve'l-bâkıyâtü's-sâlihâtü hayrun inde rabbike sevâbâ, gloss:mal ve oğullar dünya hayatının süsüdür; kalıcı iyi işler ise Rabbinin katında karşılık bakımından daha hayırlıdır, source:18:46}. Bizim on yedinci ayetin iki sıfatı, "hayırlı" ve "kalıcı", burada kuruyan otun hemen yanında durur.

[¶19] Arapçada "hayat" kelimesi bir şeyin işe yarayıp yaramadığını anlatmak için de kullanılırdı. Hiçbir faydası olmayan biri için {ar:ليس بفلان حياة أي ليس عنده نفع ولا خير, tr:leyse bi-fülânin hayâtün, ey leyse indehû nef'un ve lâ hayr, gloss:falancada hayat yok, yani onda ne fayda var ne hayır, source:"ح ي ي,B013"} denirdi. Bu söyleyişte hayat fayda ve hayırla ölçülür. Sure dokuzuncu ayette öğüdü fayda vermesi şartına bağlamış, on yedinci ayette de ahireti "daha hayırlı" diye nitelemiştir. Bu ölçüyle ahiretin içinde, "hayat" kelimesinin anlattığı şeyden daha fazlası vardır. Bir şey daha: Araplar birbirlerini "Allah sana hayat versin" diye selamlarlardı ve bunu şöyle açıklarlardı: {ar:وحياك الله أي أبقاك, tr:ve hayyâkallâh, ey ebkâk, gloss:Allah sana hayat versin, yani seni kalıcı kılsın, source:"ح ي ي,B007"}. İnsanların birbirine dilediği hayat kalıcı olan hayattır. On yedinci ayet "daha kalıcı" sıfatını ahirete verir. Yakın hayatı öne koyanlar, birbirlerine her gün diledikleri şeyin, yani kalıcılığın daha az olduğu hayatı seçmiş olurlar.

[¶20] Kur'an kalıcı hayatı bu kökten bir başka kelimeyle anar. Allah, gökten su indirip toprağı ölümünden sonra diriltenin kim olduğu sorulduğunda insanların "Allah" diyeceğini bildirir. Ardından şöyle der: {ar:وَمَا هَٰذِهِ ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا لَهْوٌۭ وَلَعِبٌۭ ۚ وَإِنَّ ٱلدَّارَ ٱلْءَاخِرَةَ لَهِىَ ٱلْحَيَوَانُ, tr:ve mâ hâzihi'l-hayâtü'd-dünyâ illâ lehvün ve leıb, ve inne'd-dâre'l-âhirate lehiye'l-hayevân, gloss:bu dünya hayatı bir eğlence ve oyundan başka bir şey değildir; ahiret yurdu ise asıl hayatın ta kendisidir, source:29:64}. Bu kelime şöyle açıklanırdı: {ar:الحيوان مقر الحياة وما له الحاسة وما له البقاء الأبدي, tr:el-hayevânü makarrü'l-hayât ve mâ lehü'l-hâsse ve mâ lehü'l-bekâü'l-ebediyy, gloss:hayevân hayatın yerleştiği yer, duyusu olan ve sonsuz kalıcılığı bulunandır, source:"ح ي ي,B003"}. Kelimeyi başka bir kökle çözümleyenler hayevânı cennette bir suyun adı olarak da anarlardı: değdiği her şey Allah'ın izniyle dirilir {source:"ح ي و,B003"}. Ayetteki hayat "yakın" sıfatını almıştır. Asıl ve kalıcı hayat ise başka bir yerdedir. Surenin on üçüncü ayeti, ateşe gireni "orada ne ölür ne yaşar" diye anlatırken bu kökün fiilini kullanır. Yakın hayatı öne koymanın götürdüğü yerde hayat kelimesinin kendisi olumsuzlanır. Bu iki ucun bağlantısı surenin bütününde kurulur.

[¶21] Kur'an bu kelimenin öbür tarafa geçtiği anı da gösterir. Yerin dövüldükçe dövüldüğü, Rabbin geldiği, meleklerin saf saf dizildiği ve cehennemin getirildiği gün için şöyle denir: {ar:يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ, tr:yevmeizin yetezekkerü'l-insân ve ennâ lehü'z-zikrâ, gloss:o gün insan hatırlar, ama hatırlamanın ona ne faydası var, source:89:23}. Burada bizim surenin dokuzuncu ve onuncu ayetlerindeki öğüt kelimeleri geç kalmış biçimde yeniden belirir. İnsan o gün şöyle der: {ar:يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى, tr:yekûlü yâ leytenî kaddemtü li-hayâtî, gloss:keşke hayatım için önceden bir şey gönderseydim, der, source:89:24}. "Hayatım" kelimesi artık yakın hayatı değil, ötedekini gösterir. Fiil de "öne koymak" fiilidir, tercih fiilinin kökünün tanımında geçen "takdim"in ta kendisidir. Bir şeyi öne koymanın iki yolu vardır. Yakın hayatı başköşeye oturtabilirsin ya da ötedeki hayat için öne bir şey gönderebilirsin. Fiil aynıdır, yönleri birbirinin tersidir.

## Öne konan ve ardında bıraktığı

[¶22] Türk okuru tercih fiilinin kökünü aslında tanır. "Eser", "âsâr", "tesir" hep bu köktendir. "Eser" bugün daha çok sanat ya da yazı ürününü anlatır. Ama "ortada eseri yok" derken eski anlamı, yani izi hâlâ yaşar. Arapçada kökün bu yüzü açıktır: {ar:الأثر بقية ما يرى من كل شيء وما لا يرى بعد أن تبقى فيه علقة, tr:el-eserü bakıyyetü mâ yürâ min külli şey' ve mâ lâ yürâ ba'de en tebkâ fîhi ulka, gloss:eser, her şeyin görünen ya da görünmeyip bir ilişiği kalan artığıdır, source:"ء ث ر,B003"}. Yara izi de böyle anlatılırdı: {ar:الأثر من الجرح وغيره في الجسد يبرأ ويبقى أثره, tr:el-eserü mine'l-cürhi ve ğayrihî fi'l-ceset, yebrau ve yebkâ eseruh, gloss:bedendeki yara iyileşir, izi kalır, source:"ء ث ر,B003"}. Öne koymak ile iz bırakmak aynı köktedir. Bu iki anlamı birbirine bağlayan şey, ayetin söylediği bir şey değil, bir yorumdur. Ama kök bu yorumu çağırır: ne öne konursa geride bir iz bırakır.

[¶23] Kökün bir kullanımı bunu somut bir aletle gösterir. Deve sahipleri devenin tabanını bir demirle işaretlerdi: {ar:المئثرة حديدة يؤثر بها خف البعير ليعرف أثره في الأرض, tr:el-mi'sera hadîdetün yü'serü bihâ huffü'l-baîri li-yu'rafe eseruhû fi'l-ard, gloss:mi'sera, devenin tabanına iz basılan demirdir; böylece yerdeki izi tanınır, source:"ء ث ر,B008"}. Bu işin nasıl yapıldığı da anlatılır: {ar:الأثرة أن يسحى باطن خف البعير بحديدة وتلك الحديدة مئثرة, tr:el-üsretü en yüshâ bâtınü huffi'l-baîri bi-hadîde ve tilke'l-hadîdetü mi'sera, gloss:üsre, devenin tabanının iç yüzünün bir demirle kazınmasıdır; o demire mi'sera denir, source:"ء ث ر,B008"}. Aletin işi şöyledir: işaret tabanın altındadır, deve onu göremez. Ama attığı her adımda kumda kendine özgü bir iz kalır. Kaybolan ya da çalınan deveyi sahibi o izden bulur. Ayetin yanında bu alet şunu duyurur: insanın öne koyduğu şey adımlarının altına basılır. Kişi izini kendisi görmez, ama yürüdüğü yol onu ele verir. Birinci ayetteki "ad" ile on ikinci ayetteki "ateş" kelimelerinde de bir damga yankılanır. Bu damga sahnesi surenin bütününe aittir. Bu ayetin kelimesi ona tabanın altındaki demiri katar.

[¶24] Kur'an izlerin kaydını açıkça söyler. Allah Peygamber'e şöyle der: {ar:إِنَّمَا تُنذِرُ مَنِ ٱتَّبَعَ ٱلذِّكْرَ وَخَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ, tr:innemâ tünziru meni'ttebea'z-zikra ve haşiye'r-rahmâne bi'l-ğayb, gloss:sen ancak öğüde uyan ve görmediği halde Rahmân'dan korkanı uyarabilirsin, source:36:11}. Öğüt ile korku burada bizim surenin onuncu ayetindeki gibi yan yanadır. Hemen ardından şu gelir: {ar:إِنَّا نَحْنُ نُحْىِ ٱلْمَوْتَىٰ وَنَكْتُبُ مَا قَدَّمُوا۟ وَءَاثَٰرَهُمْ, tr:innâ nahnü nuhyi'l-mevtâ ve nektübü mâ kaddemû ve âsârahüm, gloss:ölüleri biz diriltiriz; öne gönderdiklerini ve izlerini de biz yazarız, source:36:12}. Tek bir ayette diriltme, öne gönderme ve izler bir aradadır. Bizim ayetin hayat kelimesi, tercih fiilinin içindeki "öne koyma" ve aynı kökün "iz"i birlikte geçer.

[¶25] Kök bir adım daha ileri gider. "Birinin ardından gelmek" de bu kökle söylenirdi: {ar:جاء فلان على إثري وأثري وجاء في أثره وإثره, tr:câe fülânün alâ isrî ve eserî ve câe fî eserihî ve isrih, gloss:falanca peşimden geldi; onun izinden geldi, source:"ء ث ر,B004"}. Ömrün sonuna da aynı adla eser denirdi ve nedeni şöyle açıklanırdı: {ar:وسمي الأجل أثرا لأنه يتبع العمر, tr:ve sümmiye'l-ecelü eseran li-ennehû yetbaü'l-ömr, gloss:ecele eser denir, çünkü ömrün ardından gelir, source:"ء ث ر,B010"}. Aynı kök hem "öne koymak" hem de "ardından gelmek" demektir. Yakın hayatı öne koyanın ardında, aynı kelimenin bir başka kullanımıyla, o hayatın vadesi yürür. Bu bir analojidir, ayetin sözü değildir. Ama ayetin kelimesi bu iki ucu kendi içinde taşır.

[¶26] İz yalnızca kişinin ardında kalmaz, başkalarının yürüdüğü bir yol da olur. Allah Peygamber'e, ondan önce hangi kasabaya bir uyarıcı gönderildiyse oranın refah içinde yaşayanlarının hep aynı şeyi söylediğini bildirir: {ar:إِنَّا وَجَدْنَآ ءَابَآءَنَا عَلَىٰٓ أُمَّةٍۢ وَإِنَّا عَلَىٰٓ ءَاثَٰرِهِم مُّقْتَدُونَ, tr:innâ vecednâ âbâenâ alâ ümmetin ve innâ alâ âsârihim muktedûn, gloss:biz atalarımızı bir yol üzerinde bulduk ve biz onların izlerine uyuyoruz, source:43:23}. Bir neslin öne koyduğu şey, sonrakilerin ayak bastığı ize dönüşür. Uyarıcıya karşı ilk çıkanların refah içindekiler olması da tesadüf değildir. Yakın hayatı en çok tadanlar onun izini en derin basanlardır.

## Aktarılan söz

[¶27] Kökün bir yüzü daha surenin sonuna doğru açılır. Bir sözü başkasından nakletmek de bu fiille söylenirdi: {ar:أثرت الحديث إذا ذكرته عن غيرك وحديث مأثور, tr:esertü'l-hadîse izâ zekertehû an ğayrike ve hadîsün me'sûr, gloss:bir sözü başkasından aktardığında esertü denir; aktarılagelen söze me'sûr denir, source:"ء ث ر,B002"}. Bir insanın anlatılagelen güzel işlerine de bu kökten ad verilirdi: {ar:المآثر ما يروى من مكارم الإنسان, tr:el-meâsiru mâ yürvâ min mekârimi'l-insân, gloss:measir, insanın anlatılagelen değerli işleridir, source:"ء ث ر,B002"}. Bir insan öldükten sonra ondan anlatılan şey, hayattayken neyi öne koyduğudur.

[¶28] On sekizinci ayet şöyle der: {ar:إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:inne hâzâ le-fi's-suhufi'l-ûlâ, gloss:bu elbette ilk sayfalarda vardır, source:87:18}. "Bu" kelimesinin en yakın göndermesi, yakın hayatın öne konması ve ahiretin daha hayırlı ve daha kalıcı oluşudur. Bu hüküm, İbrahim'in ve Musa'nın sayfalarından gelen, aktarılagelmiş bir sözdür. Altıncı ayetteki okutma ve unutmama ile son ayetteki sayfaların toplanması surenin bütününe ait bir sahnedir. Bu ayetin kelimesi o sahneye "nakledilen söz" anlamıyla girer. Bu farklı anlamlar arasında bir bağ kurmaktır. Ama aynı kök, öne koymayı ve kuşaktan kuşağa aktarılan sözü birlikte taşır.

[¶29] Kur'an bu kökün aktarma anlamını, sözü reddeden birinin ağzından da verir. Allah ona okunan ayetlere karşı düşünüp taşınan birini anlatır: {ar:إِنَّهُۥ فَكَّرَ وَقَدَّرَ, tr:innehû fekkera ve kaddar, gloss:o düşündü ve ölçüp biçti, source:74:18}, {ar:فَقُتِلَ كَيْفَ قَدَّرَ, tr:fe-kutile keyfe kaddar, gloss:kahrolası, nasıl da ölçüp biçti, source:74:19}. Bu ölçüp biçme fiili, bizim surenin üçüncü ayetinde Rabbin her şeyi ölçüsüne koymasını anlatan fiildir. Burada ise ters yöne işler. Adamın vardığı hüküm şudur: {ar:فَقَالَ إِنْ هَٰذَآ إِلَّا سِحْرٌۭ يُؤْثَرُ, tr:fe-kâle in hâzâ illâ sihrun yü'ser, gloss:bu ancak aktarılagelen bir büyüdür, dedi, source:74:24}. Ona göre söz eski ve el değiştirmiş bir şeydir, bu yüzden değersizdir. Bizim sure aynı gerçeği başka bir değerle söyler. Söz gerçekten aktarılagelmiştir, ama büyücülerden değil, ilk sayfalardan. Bir başka yerde Allah Peygamber'e, Allah'tan başkasına yalvaranlara şöyle demesini emreder: {ar:ٱئْتُونِى بِكِتَٰبٍۢ مِّن قَبْلِ هَٰذَآ أَوْ أَثَٰرَةٍۢ مِّنْ عِلْمٍ, tr:i'tûnî bi-kitâbin min kabli hâzâ ev esâratin min ilm, gloss:bana bundan önceki bir kitap ya da bilgiden kalma bir iz getirin, source:46:4}. Onların ellerinde böyle bir iz yoktur. Surenin öğüdünün ise İbrahim'e ve Musa'ya uzanan bir izi vardır. Dinleyenlerin her gün yeniden öne koyduğu yakın hayatın karşısında, sure en eski ve en uzun ömürlü izi koyar: kuşaktan kuşağa aktarılan, "ahiret daha hayırlı ve daha kalıcıdır" sözü.

===== _commentary/v16/out/87_16/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: Turkish "tercih" derives from Arabic tarjīḥ (رجح, tipping the scale)
- memory: الدنيا is feminine elative of أدنى, adjective qualifying الحياة
- memory: بل here marks iḍrāb (turning from preceding to the real state)
- memory: nominal sentence in 87:17 conveys a standing, non-temporal judgment
- not written: Abu ʿAmr's reading بل يؤثرون (third person) - qira'a report outside supplied texts; avoided
- not written: sword's firind / مأثور sword (ء ث ر B007) - no work in the ayah's themes
- not written: residual fat / essence of ghee (ء ث ر B009) - no grounding link to preference or near life
- not written: skill sense (ء ث ر B011) and udder bag (B012) - no thematic work
- not written: echo root ث و ر - sound-family only, not identity; nothing it would ground
- not written: ḥayāʾ shame, snake, tribe, womb, face senses of ح ي ي - do not join a theme here
- not written: 20:84 Moses "on my track" hastening to his Lord - ambiguous (20:85 people misled); would complicate without support
- not written: 82:5 "what it sent forward and held back" - redundant with 36:12 and 89:24
- not written: waw spelling الحيوة noted by al-Khalil - orthographic, adds nothing to the reading
- not written: د ن و B005 (hunched man) - no thematic work

===== passages not cited (235) =====
## strong (this ayah's own list) (42)

- (3:145) [listed for 87:16] وَمَا كَانَ لِنَفْسٍ أَن تَمُوتَ إِلَّا بِإِذْنِ ٱللَّهِ كِتَٰبًۭا مُّؤَجَّلًۭا ۗ وَمَن يُرِدْ ثَوَابَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَن يُرِدْ ثَوَابَ ٱلْءَاخِرَةِ نُؤْتِهِۦ مِنْهَا ۚ وَسَنَجْزِى ٱلشَّٰكِرِينَ
- (3:152) [listed for 87:16] وَلَقَدْ صَدَقَكُمُ ٱللَّهُ وَعْدَهُۥٓ إِذْ تَحُسُّونَهُم بِإِذْنِهِۦ ۖ حَتَّىٰٓ إِذَا فَشِلْتُمْ وَتَنَٰزَعْتُمْ فِى ٱلْأَمْرِ وَعَصَيْتُم مِّنۢ بَعْدِ مَآ أَرَىٰكُم مَّا تُحِبُّونَ ۚ مِنكُم مَّن يُرِيدُ ٱلدُّنْيَا وَمِنكُم مَّن يُرِيدُ ٱلْءَاخِرَةَ ۚ ثُمَّ صَرَفَكُمْ عَنْهُمْ لِيَبْتَلِيَكُمْ ۖ وَلَقَدْ عَفَا عَنكُمْ ۗ وَٱللَّهُ ذُو فَضْلٍ عَلَى ٱلْمُؤْمِنِينَ
- (4:74) [listed for 87:16] ۞ فَلْيُقَٰتِلْ فِى سَبِيلِ ٱللَّهِ ٱلَّذِينَ يَشْرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْءَاخِرَةِ ۚ وَمَن يُقَٰتِلْ فِى سَبِيلِ ٱللَّهِ فَيُقْتَلْ أَوْ يَغْلِبْ فَسَوْفَ نُؤْتِيهِ أَجْرًا عَظِيمًۭا
- (4:77) [listed for 87:16] أَلَمْ تَرَ إِلَى ٱلَّذِينَ قِيلَ لَهُمْ كُفُّوٓا۟ أَيْدِيَكُمْ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ فَلَمَّا كُتِبَ عَلَيْهِمُ ٱلْقِتَالُ إِذَا فَرِيقٌۭ مِّنْهُمْ يَخْشَوْنَ ٱلنَّاسَ كَخَشْيَةِ ٱللَّهِ أَوْ أَشَدَّ خَشْيَةًۭ ۚ وَقَالُوا۟ رَبَّنَا لِمَ كَتَبْتَ عَلَيْنَا ٱلْقِتَالَ لَوْلَآ أَخَّرْتَنَآ إِلَىٰٓ أَجَلٍۢ قَرِيبٍۢ ۗ قُلْ مَتَٰعُ ٱلدُّنْيَا قَلِيلٌۭ وَٱلْءَاخِرَةُ خَيْرٌۭ لِّمَنِ ٱتَّقَىٰ وَلَا تُظْلَمُونَ فَتِيلًا
- (4:134) [listed for 87:16] مَّن كَانَ يُرِيدُ ثَوَابَ ٱلدُّنْيَا فَعِندَ ٱللَّهِ ثَوَابُ ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۚ وَكَانَ ٱللَّهُ سَمِيعًۢا بَصِيرًۭا
- (6:32) [listed for 87:16] وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا لَعِبٌۭ وَلَهْوٌۭ ۖ وَلَلدَّارُ ٱلْءَاخِرَةُ خَيْرٌۭ لِّلَّذِينَ يَتَّقُونَ ۗ أَفَلَا تَعْقِلُونَ
- (6:130) [listed for 87:16] يَٰمَعْشَرَ ٱلْجِنِّ وَٱلْإِنسِ أَلَمْ يَأْتِكُمْ رُسُلٌۭ مِّنكُمْ يَقُصُّونَ عَلَيْكُمْ ءَايَٰتِى وَيُنذِرُونَكُمْ لِقَآءَ يَوْمِكُمْ هَٰذَا ۚ قَالُوا۟ شَهِدْنَا عَلَىٰٓ أَنفُسِنَا ۖ وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا وَشَهِدُوا۟ عَلَىٰٓ أَنفُسِهِمْ أَنَّهُمْ كَانُوا۟ كَٰفِرِينَ
- (8:67) [listed for 87:16] مَا كَانَ لِنَبِىٍّ أَن يَكُونَ لَهُۥٓ أَسْرَىٰ حَتَّىٰ يُثْخِنَ فِى ٱلْأَرْضِ ۚ تُرِيدُونَ عَرَضَ ٱلدُّنْيَا وَٱللَّهُ يُرِيدُ ٱلْءَاخِرَةَ ۗ وَٱللَّهُ عَزِيزٌ حَكِيمٌۭ
- (9:24) [listed for 87:16] قُلْ إِن كَانَ ءَابَآؤُكُمْ وَأَبْنَآؤُكُمْ وَإِخْوَٰنُكُمْ وَأَزْوَٰجُكُمْ وَعَشِيرَتُكُمْ وَأَمْوَٰلٌ ٱقْتَرَفْتُمُوهَا وَتِجَٰرَةٌۭ تَخْشَوْنَ كَسَادَهَا وَمَسَٰكِنُ تَرْضَوْنَهَآ أَحَبَّ إِلَيْكُم مِّنَ ٱللَّهِ وَرَسُولِهِۦ وَجِهَادٍۢ فِى سَبِيلِهِۦ فَتَرَبَّصُوا۟ حَتَّىٰ يَأْتِىَ ٱللَّهُ بِأَمْرِهِۦ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلْفَٰسِقِينَ
- (9:38) [listed for 87:16] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ مَا لَكُمْ إِذَا قِيلَ لَكُمُ ٱنفِرُوا۟ فِى سَبِيلِ ٱللَّهِ ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ ۚ أَرَضِيتُم بِٱلْحَيَوٰةِ ٱلدُّنْيَا مِنَ ٱلْءَاخِرَةِ ۚ فَمَا مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا فِى ٱلْءَاخِرَةِ إِلَّا قَلِيلٌ
- (10:7) [listed for 87:16] إِنَّ ٱلَّذِينَ لَا يَرْجُونَ لِقَآءَنَا وَرَضُوا۟ بِٱلْحَيَوٰةِ ٱلدُّنْيَا وَٱطْمَأَنُّوا۟ بِهَا وَٱلَّذِينَ هُمْ عَنْ ءَايَٰتِنَا غَٰفِلُونَ
- (10:24) [listed for 87:16] إِنَّمَا مَثَلُ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ مِمَّا يَأْكُلُ ٱلنَّاسُ وَٱلْأَنْعَٰمُ حَتَّىٰٓ إِذَآ أَخَذَتِ ٱلْأَرْضُ زُخْرُفَهَا وَٱزَّيَّنَتْ وَظَنَّ أَهْلُهَآ أَنَّهُمْ قَٰدِرُونَ عَلَيْهَآ أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًۭا فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ ۚ كَذَٰلِكَ نُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَتَفَكَّرُونَ
- (11:16) [listed for 87:16] أُو۟لَٰٓئِكَ ٱلَّذِينَ لَيْسَ لَهُمْ فِى ٱلْءَاخِرَةِ إِلَّا ٱلنَّارُ ۖ وَحَبِطَ مَا صَنَعُوا۟ فِيهَا وَبَٰطِلٌۭ مَّا كَانُوا۟ يَعْمَلُونَ
- (13:26) [listed for 87:16] ٱللَّهُ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ وَفَرِحُوا۟ بِٱلْحَيَوٰةِ ٱلدُّنْيَا وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا فِى ٱلْءَاخِرَةِ إِلَّا مَتَٰعٌۭ
- (14:3) [listed for 87:16] ٱلَّذِينَ يَسْتَحِبُّونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًا ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۭ بَعِيدٍۢ
- (16:96) [listed for 87:16] مَا عِندَكُمْ يَنفَدُ ۖ وَمَا عِندَ ٱللَّهِ بَاقٍۢ ۗ وَلَنَجْزِيَنَّ ٱلَّذِينَ صَبَرُوٓا۟ أَجْرَهُم بِأَحْسَنِ مَا كَانُوا۟ يَعْمَلُونَ
- (16:107) [listed for 87:16] ذَٰلِكَ بِأَنَّهُمُ ٱسْتَحَبُّوا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَأَنَّ ٱللَّهَ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
- (17:18) [listed for 87:16] مَّن كَانَ يُرِيدُ ٱلْعَاجِلَةَ عَجَّلْنَا لَهُۥ فِيهَا مَا نَشَآءُ لِمَن نُّرِيدُ ثُمَّ جَعَلْنَا لَهُۥ جَهَنَّمَ يَصْلَىٰهَا مَذْمُومًۭا مَّدْحُورًۭا
- (17:19) [listed for 87:16] وَمَنْ أَرَادَ ٱلْءَاخِرَةَ وَسَعَىٰ لَهَا سَعْيَهَا وَهُوَ مُؤْمِنٌۭ فَأُو۟لَٰٓئِكَ كَانَ سَعْيُهُم مَّشْكُورًۭا
- (18:45) [listed for 87:16] [cited in ¶18] وَٱضْرِبْ لَهُم مَّثَلَ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ فَٱخْتَلَطَ بِهِۦ نَبَاتُ ٱلْأَرْضِ فَأَصْبَحَ هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ ۗ وَكَانَ ٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ مُّقْتَدِرًا
- (18:46) [listed for 87:16] [cited in ¶18] ٱلْمَالُ وَٱلْبَنُونَ زِينَةُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا وَخَيْرٌ أَمَلًۭا
- (20:72) [listed for 87:16] [cited in ¶8] قَالُوا۟ لَن نُّؤْثِرَكَ عَلَىٰ مَا جَآءَنَا مِنَ ٱلْبَيِّنَٰتِ وَٱلَّذِى فَطَرَنَا ۖ فَٱقْضِ مَآ أَنتَ قَاضٍ ۖ إِنَّمَا تَقْضِى هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ
- (20:131) [listed for 87:16] وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ زَهْرَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا لِنَفْتِنَهُمْ فِيهِ ۚ وَرِزْقُ رَبِّكَ خَيْرٌۭ وَأَبْقَىٰ
- (28:60) [listed for 87:16] وَمَآ أُوتِيتُم مِّن شَىْءٍۢ فَمَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا وَزِينَتُهَا ۚ وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰٓ ۚ أَفَلَا تَعْقِلُونَ
- (28:61) [listed for 87:16] أَفَمَن وَعَدْنَٰهُ وَعْدًا حَسَنًۭا فَهُوَ لَٰقِيهِ كَمَن مَّتَّعْنَٰهُ مَتَٰعَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ثُمَّ هُوَ يَوْمَ ٱلْقِيَٰمَةِ مِنَ ٱلْمُحْضَرِينَ
- (29:64) [listed for 87:16] [cited in ¶20] وَمَا هَٰذِهِ ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا لَهْوٌۭ وَلَعِبٌۭ ۚ وَإِنَّ ٱلدَّارَ ٱلْءَاخِرَةَ لَهِىَ ٱلْحَيَوَانُ ۚ لَوْ كَانُوا۟ يَعْلَمُونَ
- (30:7) [listed for 87:16] يَعْلَمُونَ ظَٰهِرًۭا مِّنَ ٱلْحَيَوٰةِ ٱلدُّنْيَا وَهُمْ عَنِ ٱلْءَاخِرَةِ هُمْ غَٰفِلُونَ
- (31:33) [listed for 87:16] يَٰٓأَيُّهَا ٱلنَّاسُ ٱتَّقُوا۟ رَبَّكُمْ وَٱخْشَوْا۟ يَوْمًۭا لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ وَلَا مَوْلُودٌ هُوَ جَازٍ عَن وَالِدِهِۦ شَيْـًٔا ۚ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ ۖ فَلَا تَغُرَّنَّكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا وَلَا يَغُرَّنَّكُم بِٱللَّهِ ٱلْغَرُورُ
- (33:28) [listed for 87:16] يَٰٓأَيُّهَا ٱلنَّبِىُّ قُل لِّأَزْوَٰجِكَ إِن كُنتُنَّ تُرِدْنَ ٱلْحَيَوٰةَ ٱلدُّنْيَا وَزِينَتَهَا فَتَعَالَيْنَ أُمَتِّعْكُنَّ وَأُسَرِّحْكُنَّ سَرَاحًۭا جَمِيلًۭا
- (33:29) [listed for 87:16] وَإِن كُنتُنَّ تُرِدْنَ ٱللَّهَ وَرَسُولَهُۥ وَٱلدَّارَ ٱلْءَاخِرَةَ فَإِنَّ ٱللَّهَ أَعَدَّ لِلْمُحْسِنَٰتِ مِنكُنَّ أَجْرًا عَظِيمًۭا
- (40:39) [listed for 87:16] يَٰقَوْمِ إِنَّمَا هَٰذِهِ ٱلْحَيَوٰةُ ٱلدُّنْيَا مَتَٰعٌۭ وَإِنَّ ٱلْءَاخِرَةَ هِىَ دَارُ ٱلْقَرَارِ
- (42:20) [listed for 87:16] مَن كَانَ يُرِيدُ حَرْثَ ٱلْءَاخِرَةِ نَزِدْ لَهُۥ فِى حَرْثِهِۦ ۖ وَمَن كَانَ يُرِيدُ حَرْثَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِن نَّصِيبٍ
- (42:36) [listed for 87:16] فَمَآ أُوتِيتُم مِّن شَىْءٍۢ فَمَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰ لِلَّذِينَ ءَامَنُوا۟ وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ
- (43:35) [listed for 87:16] وَزُخْرُفًۭا ۚ وَإِن كُلُّ ذَٰلِكَ لَمَّا مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَٱلْءَاخِرَةُ عِندَ رَبِّكَ لِلْمُتَّقِينَ
- (45:35) [listed for 87:16] ذَٰلِكُم بِأَنَّكُمُ ٱتَّخَذْتُمْ ءَايَٰتِ ٱللَّهِ هُزُوًۭا وَغَرَّتْكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ فَٱلْيَوْمَ لَا يُخْرَجُونَ مِنْهَا وَلَا هُمْ يُسْتَعْتَبُونَ
- (46:20) [listed for 87:16] وَيَوْمَ يُعْرَضُ ٱلَّذِينَ كَفَرُوا۟ عَلَى ٱلنَّارِ أَذْهَبْتُمْ طَيِّبَٰتِكُمْ فِى حَيَاتِكُمُ ٱلدُّنْيَا وَٱسْتَمْتَعْتُم بِهَا فَٱلْيَوْمَ تُجْزَوْنَ عَذَابَ ٱلْهُونِ بِمَا كُنتُمْ تَسْتَكْبِرُونَ فِى ٱلْأَرْضِ بِغَيْرِ ٱلْحَقِّ وَبِمَا كُنتُمْ تَفْسُقُونَ
- (47:36) [listed for 87:16] إِنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌۭ وَلَهْوٌۭ ۚ وَإِن تُؤْمِنُوا۟ وَتَتَّقُوا۟ يُؤْتِكُمْ أُجُورَكُمْ وَلَا يَسْـَٔلْكُمْ أَمْوَٰلَكُمْ
- (57:20) [listed for 87:16] ٱعْلَمُوٓا۟ أَنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌۭ وَلَهْوٌۭ وَزِينَةٌۭ وَتَفَاخُرٌۢ بَيْنَكُمْ وَتَكَاثُرٌۭ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ ۖ كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا ۖ وَفِى ٱلْءَاخِرَةِ عَذَابٌۭ شَدِيدٌۭ وَمَغْفِرَةٌۭ مِّنَ ٱللَّهِ وَرِضْوَٰنٌۭ ۚ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
- (75:20) [listed for 87:16] [cited in ¶4] كَلَّا بَلْ تُحِبُّونَ ٱلْعَاجِلَةَ
- (75:21) [listed for 87:16] [cited in ¶4] وَتَذَرُونَ ٱلْءَاخِرَةَ
- (79:38) [listed for 87:16] [cited in ¶9] وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- (79:39) [listed for 87:16] [cited in ¶9] فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ

## medium (this ayah's own list) (55)

- (2:86) [listed for 87:16] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْءَاخِرَةِ ۖ فَلَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنصَرُونَ
- (2:96) [listed for 87:16] وَلَتَجِدَنَّهُمْ أَحْرَصَ ٱلنَّاسِ عَلَىٰ حَيَوٰةٍۢ وَمِنَ ٱلَّذِينَ أَشْرَكُوا۟ ۚ يَوَدُّ أَحَدُهُمْ لَوْ يُعَمَّرُ أَلْفَ سَنَةٍۢ وَمَا هُوَ بِمُزَحْزِحِهِۦ مِنَ ٱلْعَذَابِ أَن يُعَمَّرَ ۗ وَٱللَّهُ بَصِيرٌۢ بِمَا يَعْمَلُونَ
- (2:200) [listed for 87:16] فَإِذَا قَضَيْتُم مَّنَٰسِكَكُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَذِكْرِكُمْ ءَابَآءَكُمْ أَوْ أَشَدَّ ذِكْرًۭا ۗ فَمِنَ ٱلنَّاسِ مَن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ
- (2:201) [listed for 87:16] وَمِنْهُم مَّن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ حَسَنَةًۭ وَقِنَا عَذَابَ ٱلنَّارِ
- (2:212) [listed for 87:16] زُيِّنَ لِلَّذِينَ كَفَرُوا۟ ٱلْحَيَوٰةُ ٱلدُّنْيَا وَيَسْخَرُونَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ ۘ وَٱلَّذِينَ ٱتَّقَوْا۟ فَوْقَهُمْ يَوْمَ ٱلْقِيَٰمَةِ ۗ وَٱللَّهُ يَرْزُقُ مَن يَشَآءُ بِغَيْرِ حِسَابٍۢ
- (3:14) [listed for 87:16] زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ مِنَ ٱلنِّسَآءِ وَٱلْبَنِينَ وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ مِنَ ٱلذَّهَبِ وَٱلْفِضَّةِ وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ ۗ ذَٰلِكَ مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلْمَـَٔابِ
- (3:148) [listed for 87:16] فَـَٔاتَىٰهُمُ ٱللَّهُ ثَوَابَ ٱلدُّنْيَا وَحُسْنَ ثَوَابِ ٱلْءَاخِرَةِ ۗ وَٱللَّهُ يُحِبُّ ٱلْمُحْسِنِينَ
- (3:185) [listed for 87:16] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۗ وَإِنَّمَا تُوَفَّوْنَ أُجُورَكُمْ يَوْمَ ٱلْقِيَٰمَةِ ۖ فَمَن زُحْزِحَ عَنِ ٱلنَّارِ وَأُدْخِلَ ٱلْجَنَّةَ فَقَدْ فَازَ ۗ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
- (4:94) [listed for 87:16] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا ضَرَبْتُمْ فِى سَبِيلِ ٱللَّهِ فَتَبَيَّنُوا۟ وَلَا تَقُولُوا۟ لِمَنْ أَلْقَىٰٓ إِلَيْكُمُ ٱلسَّلَٰمَ لَسْتَ مُؤْمِنًۭا تَبْتَغُونَ عَرَضَ ٱلْحَيَوٰةِ ٱلدُّنْيَا فَعِندَ ٱللَّهِ مَغَانِمُ كَثِيرَةٌۭ ۚ كَذَٰلِكَ كُنتُم مِّن قَبْلُ فَمَنَّ ٱللَّهُ عَلَيْكُمْ فَتَبَيَّنُوٓا۟ ۚ إِنَّ ٱللَّهَ كَانَ بِمَا تَعْمَلُونَ خَبِيرًۭا
- (4:109) [listed for 87:16] هَٰٓأَنتُمْ هَٰٓؤُلَآءِ جَٰدَلْتُمْ عَنْهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا فَمَن يُجَٰدِلُ ٱللَّهَ عَنْهُمْ يَوْمَ ٱلْقِيَٰمَةِ أَم مَّن يَكُونُ عَلَيْهِمْ وَكِيلًۭا
- (6:29) [listed for 87:16] وَقَالُوٓا۟ إِنْ هِىَ إِلَّا حَيَاتُنَا ٱلدُّنْيَا وَمَا نَحْنُ بِمَبْعُوثِينَ
- (6:70) [listed for 87:16] وَذَرِ ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَعِبًۭا وَلَهْوًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ وَذَكِّرْ بِهِۦٓ أَن تُبْسَلَ نَفْسٌۢ بِمَا كَسَبَتْ لَيْسَ لَهَا مِن دُونِ ٱللَّهِ وَلِىٌّۭ وَلَا شَفِيعٌۭ وَإِن تَعْدِلْ كُلَّ عَدْلٍۢ لَّا يُؤْخَذْ مِنْهَآ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ أُبْسِلُوا۟ بِمَا كَسَبُوا۟ ۖ لَهُمْ شَرَابٌۭ مِّنْ حَمِيمٍۢ وَعَذَابٌ أَلِيمٌۢ بِمَا كَانُوا۟ يَكْفُرُونَ
- (7:51) [listed for 87:16] ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَهْوًۭا وَلَعِبًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ فَٱلْيَوْمَ نَنسَىٰهُمْ كَمَا نَسُوا۟ لِقَآءَ يَوْمِهِمْ هَٰذَا وَمَا كَانُوا۟ بِـَٔايَٰتِنَا يَجْحَدُونَ
- (7:169) [listed for 87:16] [cited in ¶16] فَخَلَفَ مِنۢ بَعْدِهِمْ خَلْفٌۭ وَرِثُوا۟ ٱلْكِتَٰبَ يَأْخُذُونَ عَرَضَ هَٰذَا ٱلْأَدْنَىٰ وَيَقُولُونَ سَيُغْفَرُ لَنَا وَإِن يَأْتِهِمْ عَرَضٌۭ مِّثْلُهُۥ يَأْخُذُوهُ ۚ أَلَمْ يُؤْخَذْ عَلَيْهِم مِّيثَٰقُ ٱلْكِتَٰبِ أَن لَّا يَقُولُوا۟ عَلَى ٱللَّهِ إِلَّا ٱلْحَقَّ وَدَرَسُوا۟ مَا فِيهِ ۗ وَٱلدَّارُ ٱلْءَاخِرَةُ خَيْرٌۭ لِّلَّذِينَ يَتَّقُونَ ۗ أَفَلَا تَعْقِلُونَ
- (8:24) [listed for 87:16] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱسْتَجِيبُوا۟ لِلَّهِ وَلِلرَّسُولِ إِذَا دَعَاكُمْ لِمَا يُحْيِيكُمْ ۖ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَحُولُ بَيْنَ ٱلْمَرْءِ وَقَلْبِهِۦ وَأَنَّهُۥٓ إِلَيْهِ تُحْشَرُونَ
- (8:42) [listed for 87:16] [cited in ¶11] إِذْ أَنتُم بِٱلْعُدْوَةِ ٱلدُّنْيَا وَهُم بِٱلْعُدْوَةِ ٱلْقُصْوَىٰ وَٱلرَّكْبُ أَسْفَلَ مِنكُمْ ۚ وَلَوْ تَوَاعَدتُّمْ لَٱخْتَلَفْتُمْ فِى ٱلْمِيعَٰدِ ۙ وَلَٰكِن لِّيَقْضِىَ ٱللَّهُ أَمْرًۭا كَانَ مَفْعُولًۭا لِّيَهْلِكَ مَنْ هَلَكَ عَنۢ بَيِّنَةٍۢ وَيَحْيَىٰ مَنْ حَىَّ عَنۢ بَيِّنَةٍۢ ۗ وَإِنَّ ٱللَّهَ لَسَمِيعٌ عَلِيمٌ
- (10:56) [listed for 87:16] هُوَ يُحْىِۦ وَيُمِيتُ وَإِلَيْهِ تُرْجَعُونَ
- (10:64) [listed for 87:16] لَهُمُ ٱلْبُشْرَىٰ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَفِى ٱلْءَاخِرَةِ ۚ لَا تَبْدِيلَ لِكَلِمَٰتِ ٱللَّهِ ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (10:88) [listed for 87:16] وَقَالَ مُوسَىٰ رَبَّنَآ إِنَّكَ ءَاتَيْتَ فِرْعَوْنَ وَمَلَأَهُۥ زِينَةًۭ وَأَمْوَٰلًۭا فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا رَبَّنَا لِيُضِلُّوا۟ عَن سَبِيلِكَ ۖ رَبَّنَا ٱطْمِسْ عَلَىٰٓ أَمْوَٰلِهِمْ وَٱشْدُدْ عَلَىٰ قُلُوبِهِمْ فَلَا يُؤْمِنُوا۟ حَتَّىٰ يَرَوُا۟ ٱلْعَذَابَ ٱلْأَلِيمَ
- (11:15) [listed for 87:16] مَن كَانَ يُرِيدُ ٱلْحَيَوٰةَ ٱلدُّنْيَا وَزِينَتَهَا نُوَفِّ إِلَيْهِمْ أَعْمَٰلَهُمْ فِيهَا وَهُمْ فِيهَا لَا يُبْخَسُونَ
- (13:34) [listed for 87:16] لَّهُمْ عَذَابٌۭ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَعَذَابُ ٱلْءَاخِرَةِ أَشَقُّ ۖ وَمَا لَهُم مِّنَ ٱللَّهِ مِن وَاقٍۢ
- (16:41) [listed for 87:16] وَٱلَّذِينَ هَاجَرُوا۟ فِى ٱللَّهِ مِنۢ بَعْدِ مَا ظُلِمُوا۟ لَنُبَوِّئَنَّهُمْ فِى ٱلدُّنْيَا حَسَنَةًۭ ۖ وَلَأَجْرُ ٱلْءَاخِرَةِ أَكْبَرُ ۚ لَوْ كَانُوا۟ يَعْلَمُونَ
- (16:65) [listed for 87:16] وَٱللَّهُ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَسْمَعُونَ
- (16:97) [listed for 87:16] مَنْ عَمِلَ صَٰلِحًۭا مِّن ذَكَرٍ أَوْ أُنثَىٰ وَهُوَ مُؤْمِنٌۭ فَلَنُحْيِيَنَّهُۥ حَيَوٰةًۭ طَيِّبَةًۭ ۖ وَلَنَجْزِيَنَّهُمْ أَجْرَهُم بِأَحْسَنِ مَا كَانُوا۟ يَعْمَلُونَ
- (18:28) [listed for 87:16] وَٱصْبِرْ نَفْسَكَ مَعَ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ وَلَا تَعْدُ عَيْنَاكَ عَنْهُمْ تُرِيدُ زِينَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُۥ عَن ذِكْرِنَا وَٱتَّبَعَ هَوَىٰهُ وَكَانَ أَمْرُهُۥ فُرُطًۭا
- (18:104) [listed for 87:16] ٱلَّذِينَ ضَلَّ سَعْيُهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَهُمْ يَحْسَبُونَ أَنَّهُمْ يُحْسِنُونَ صُنْعًا
- (20:84) [listed for 87:16] قَالَ هُمْ أُو۟لَآءِ عَلَىٰٓ أَثَرِى وَعَجِلْتُ إِلَيْكَ رَبِّ لِتَرْضَىٰ
- (20:96) [listed for 87:16] قَالَ بَصُرْتُ بِمَا لَمْ يَبْصُرُوا۟ بِهِۦ فَقَبَضْتُ قَبْضَةًۭ مِّنْ أَثَرِ ٱلرَّسُولِ فَنَبَذْتُهَا وَكَذَٰلِكَ سَوَّلَتْ لِى نَفْسِى
- (22:11) [listed for 87:16] وَمِنَ ٱلنَّاسِ مَن يَعْبُدُ ٱللَّهَ عَلَىٰ حَرْفٍۢ ۖ فَإِنْ أَصَابَهُۥ خَيْرٌ ٱطْمَأَنَّ بِهِۦ ۖ وَإِنْ أَصَابَتْهُ فِتْنَةٌ ٱنقَلَبَ عَلَىٰ وَجْهِهِۦ خَسِرَ ٱلدُّنْيَا وَٱلْءَاخِرَةَ ۚ ذَٰلِكَ هُوَ ٱلْخُسْرَانُ ٱلْمُبِينُ
- (23:37) [listed for 87:16] إِنْ هِىَ إِلَّا حَيَاتُنَا ٱلدُّنْيَا نَمُوتُ وَنَحْيَا وَمَا نَحْنُ بِمَبْعُوثِينَ
- (26:81) [listed for 87:16] وَٱلَّذِى يُمِيتُنِى ثُمَّ يُحْيِينِ
- (28:77) [listed for 87:16] وَٱبْتَغِ فِيمَآ ءَاتَىٰكَ ٱللَّهُ ٱلدَّارَ ٱلْءَاخِرَةَ ۖ وَلَا تَنسَ نَصِيبَكَ مِنَ ٱلدُّنْيَا ۖ وَأَحْسِن كَمَآ أَحْسَنَ ٱللَّهُ إِلَيْكَ ۖ وَلَا تَبْغِ ٱلْفَسَادَ فِى ٱلْأَرْضِ ۖ إِنَّ ٱللَّهَ لَا يُحِبُّ ٱلْمُفْسِدِينَ
- (28:79) [listed for 87:16] فَخَرَجَ عَلَىٰ قَوْمِهِۦ فِى زِينَتِهِۦ ۖ قَالَ ٱلَّذِينَ يُرِيدُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا يَٰلَيْتَ لَنَا مِثْلَ مَآ أُوتِىَ قَٰرُونُ إِنَّهُۥ لَذُو حَظٍّ عَظِيمٍۢ
- (30:50) [listed for 87:16] فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ ذَٰلِكَ لَمُحْىِ ٱلْمَوْتَىٰ ۖ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (32:21) [listed for 87:16] وَلَنُذِيقَنَّهُم مِّنَ ٱلْعَذَابِ ٱلْأَدْنَىٰ دُونَ ٱلْعَذَابِ ٱلْأَكْبَرِ لَعَلَّهُمْ يَرْجِعُونَ
- (34:37) [listed for 87:16] وَمَآ أَمْوَٰلُكُمْ وَلَآ أَوْلَٰدُكُم بِٱلَّتِى تُقَرِّبُكُمْ عِندَنَا زُلْفَىٰٓ إِلَّا مَنْ ءَامَنَ وَعَمِلَ صَٰلِحًۭا فَأُو۟لَٰٓئِكَ لَهُمْ جَزَآءُ ٱلضِّعْفِ بِمَا عَمِلُوا۟ وَهُمْ فِى ٱلْغُرُفَٰتِ ءَامِنُونَ
- (35:5) [listed for 87:16] يَٰٓأَيُّهَا ٱلنَّاسُ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ ۖ فَلَا تَغُرَّنَّكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۖ وَلَا يَغُرَّنَّكُم بِٱللَّهِ ٱلْغَرُورُ
- (36:12) [listed for 87:16] [cited in ¶24] إِنَّا نَحْنُ نُحْىِ ٱلْمَوْتَىٰ وَنَكْتُبُ مَا قَدَّمُوا۟ وَءَاثَٰرَهُمْ ۚ وَكُلَّ شَىْءٍ أَحْصَيْنَٰهُ فِىٓ إِمَامٍۢ مُّبِينٍۢ
- (37:70) [listed for 87:16] فَهُمْ عَلَىٰٓ ءَاثَٰرِهِمْ يُهْرَعُونَ
- (39:10) [listed for 87:16] قُلْ يَٰعِبَادِ ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ رَبَّكُمْ ۚ لِلَّذِينَ أَحْسَنُوا۟ فِى هَٰذِهِ ٱلدُّنْيَا حَسَنَةٌۭ ۗ وَأَرْضُ ٱللَّهِ وَٰسِعَةٌ ۗ إِنَّمَا يُوَفَّى ٱلصَّٰبِرُونَ أَجْرَهُم بِغَيْرِ حِسَابٍۢ
- (39:26) [listed for 87:16] فَأَذَاقَهُمُ ٱللَّهُ ٱلْخِزْىَ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَعَذَابُ ٱلْءَاخِرَةِ أَكْبَرُ ۚ لَوْ كَانُوا۟ يَعْلَمُونَ
- (40:21) [listed for 87:16] ۞ أَوَلَمْ يَسِيرُوا۟ فِى ٱلْأَرْضِ فَيَنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلَّذِينَ كَانُوا۟ مِن قَبْلِهِمْ ۚ كَانُوا۟ هُمْ أَشَدَّ مِنْهُمْ قُوَّةًۭ وَءَاثَارًۭا فِى ٱلْأَرْضِ فَأَخَذَهُمُ ٱللَّهُ بِذُنُوبِهِمْ وَمَا كَانَ لَهُم مِّنَ ٱللَّهِ مِن وَاقٍۢ
- (40:51) [listed for 87:16] إِنَّا لَنَنصُرُ رُسُلَنَا وَٱلَّذِينَ ءَامَنُوا۟ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَيَوْمَ يَقُومُ ٱلْأَشْهَٰدُ
- (40:82) [listed for 87:16] أَفَلَمْ يَسِيرُوا۟ فِى ٱلْأَرْضِ فَيَنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلَّذِينَ مِن قَبْلِهِمْ ۚ كَانُوٓا۟ أَكْثَرَ مِنْهُمْ وَأَشَدَّ قُوَّةًۭ وَءَاثَارًۭا فِى ٱلْأَرْضِ فَمَآ أَغْنَىٰ عَنْهُم مَّا كَانُوا۟ يَكْسِبُونَ
- (43:22) [listed for 87:16] بَلْ قَالُوٓا۟ إِنَّا وَجَدْنَآ ءَابَآءَنَا عَلَىٰٓ أُمَّةٍۢ وَإِنَّا عَلَىٰٓ ءَاثَٰرِهِم مُّهْتَدُونَ
- (46:4) [listed for 87:16] [cited in ¶29] قُلْ أَرَءَيْتُم مَّا تَدْعُونَ مِن دُونِ ٱللَّهِ أَرُونِى مَاذَا خَلَقُوا۟ مِنَ ٱلْأَرْضِ أَمْ لَهُمْ شِرْكٌۭ فِى ٱلسَّمَٰوَٰتِ ۖ ٱئْتُونِى بِكِتَٰبٍۢ مِّن قَبْلِ هَٰذَآ أَوْ أَثَٰرَةٍۢ مِّنْ عِلْمٍ إِن كُنتُمْ صَٰدِقِينَ
- (53:29) [listed for 87:16] فَأَعْرِضْ عَن مَّن تَوَلَّىٰ عَن ذِكْرِنَا وَلَمْ يُرِدْ إِلَّا ٱلْحَيَوٰةَ ٱلدُّنْيَا
- (53:44) [listed for 87:16] وَأَنَّهُۥ هُوَ أَمَاتَ وَأَحْيَا
- (57:27) [listed for 87:16] ثُمَّ قَفَّيْنَا عَلَىٰٓ ءَاثَٰرِهِم بِرُسُلِنَا وَقَفَّيْنَا بِعِيسَى ٱبْنِ مَرْيَمَ وَءَاتَيْنَٰهُ ٱلْإِنجِيلَ وَجَعَلْنَا فِى قُلُوبِ ٱلَّذِينَ ٱتَّبَعُوهُ رَأْفَةًۭ وَرَحْمَةًۭ وَرَهْبَانِيَّةً ٱبْتَدَعُوهَا مَا كَتَبْنَٰهَا عَلَيْهِمْ إِلَّا ٱبْتِغَآءَ رِضْوَٰنِ ٱللَّهِ فَمَا رَعَوْهَا حَقَّ رِعَايَتِهَا ۖ فَـَٔاتَيْنَا ٱلَّذِينَ ءَامَنُوا۟ مِنْهُمْ أَجْرَهُمْ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
- (63:9) [listed for 87:16] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُلْهِكُمْ أَمْوَٰلُكُمْ وَلَآ أَوْلَٰدُكُمْ عَن ذِكْرِ ٱللَّهِ ۚ وَمَن يَفْعَلْ ذَٰلِكَ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (64:15) [listed for 87:16] إِنَّمَآ أَمْوَٰلُكُمْ وَأَوْلَٰدُكُمْ فِتْنَةٌۭ ۚ وَٱللَّهُ عِندَهُۥٓ أَجْرٌ عَظِيمٌۭ
- (77:26) [listed for 87:16] أَحْيَآءًۭ وَأَمْوَٰتًۭا
- (79:37) [listed for 87:16] [cited in ¶9] فَأَمَّا مَن طَغَىٰ
- (89:24) [listed for 87:16] [cited in ¶21] يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى
- (102:1) [listed for 87:16] أَلْهَىٰكُمُ ٱلتَّكَاثُرُ

## named by the passage's own list as strong for this ayah (27)

- (2:204) [listed for 87:16] وَمِنَ ٱلنَّاسِ مَن يُعْجِبُكَ قَوْلُهُۥ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَيُشْهِدُ ٱللَّهَ عَلَىٰ مَا فِى قَلْبِهِۦ وَهُوَ أَلَدُّ ٱلْخِصَامِ
- (3:196) [listed for 87:16] لَا يَغُرَّنَّكَ تَقَلُّبُ ٱلَّذِينَ كَفَرُوا۟ فِى ٱلْبِلَٰدِ
- (3:197) [listed for 87:16] مَتَٰعٌۭ قَلِيلٌۭ ثُمَّ مَأْوَىٰهُمْ جَهَنَّمُ ۚ وَبِئْسَ ٱلْمِهَادُ
- (10:23) [listed for 87:16] فَلَمَّآ أَنجَىٰهُمْ إِذَا هُمْ يَبْغُونَ فِى ٱلْأَرْضِ بِغَيْرِ ٱلْحَقِّ ۗ يَٰٓأَيُّهَا ٱلنَّاسُ إِنَّمَا بَغْيُكُمْ عَلَىٰٓ أَنفُسِكُم ۖ مَّتَٰعَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ ثُمَّ إِلَيْنَا مَرْجِعُكُمْ فَنُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- (10:70) [listed for 87:16] مَتَٰعٌۭ فِى ٱلدُّنْيَا ثُمَّ إِلَيْنَا مَرْجِعُهُمْ ثُمَّ نُذِيقُهُمُ ٱلْعَذَابَ ٱلشَّدِيدَ بِمَا كَانُوا۟ يَكْفُرُونَ
- (12:91) [listed for 87:16] [cited in ¶6] قَالُوا۟ تَٱللَّهِ لَقَدْ ءَاثَرَكَ ٱللَّهُ عَلَيْنَا وَإِن كُنَّا لَخَٰطِـِٔينَ
- (15:3) [listed for 87:16] ذَرْهُمْ يَأْكُلُوا۟ وَيَتَمَتَّعُوا۟ وَيُلْهِهِمُ ٱلْأَمَلُ ۖ فَسَوْفَ يَعْلَمُونَ
- (16:95) [listed for 87:16] وَلَا تَشْتَرُوا۟ بِعَهْدِ ٱللَّهِ ثَمَنًۭا قَلِيلًا ۚ إِنَّمَا عِندَ ٱللَّهِ هُوَ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
- (16:109) [listed for 87:16] لَا جَرَمَ أَنَّهُمْ فِى ٱلْءَاخِرَةِ هُمُ ٱلْخَٰسِرُونَ
- (17:10) [listed for 87:16] وَأَنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ أَعْتَدْنَا لَهُمْ عَذَابًا أَلِيمًۭا
- (17:21) [listed for 87:16] ٱنظُرْ كَيْفَ فَضَّلْنَا بَعْضَهُمْ عَلَىٰ بَعْضٍۢ ۚ وَلَلْءَاخِرَةُ أَكْبَرُ دَرَجَٰتٍۢ وَأَكْبَرُ تَفْضِيلًۭا
- (18:34) [listed for 87:16] وَكَانَ لَهُۥ ثَمَرٌۭ فَقَالَ لِصَٰحِبِهِۦ وَهُوَ يُحَاوِرُهُۥٓ أَنَا۠ أَكْثَرُ مِنكَ مَالًۭا وَأَعَزُّ نَفَرًۭا
- (18:35) [listed for 87:16] وَدَخَلَ جَنَّتَهُۥ وَهُوَ ظَالِمٌۭ لِّنَفْسِهِۦ قَالَ مَآ أَظُنُّ أَن تَبِيدَ هَٰذِهِۦٓ أَبَدًۭا
- (23:56) [listed for 87:16] نُسَارِعُ لَهُمْ فِى ٱلْخَيْرَٰتِ ۚ بَل لَّا يَشْعُرُونَ
- (23:74) [listed for 87:16] وَإِنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ عَنِ ٱلصِّرَٰطِ لَنَٰكِبُونَ
- (26:207) [listed for 87:16] مَآ أَغْنَىٰ عَنْهُم مَّا كَانُوا۟ يُمَتَّعُونَ
- (27:4) [listed for 87:16] إِنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ زَيَّنَّا لَهُمْ أَعْمَٰلَهُمْ فَهُمْ يَعْمَهُونَ
- (28:80) [listed for 87:16] وَقَالَ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ وَيْلَكُمْ ثَوَابُ ٱللَّهِ خَيْرٌۭ لِّمَنْ ءَامَنَ وَعَمِلَ صَٰلِحًۭا وَلَا يُلَقَّىٰهَآ إِلَّا ٱلصَّٰبِرُونَ
- (28:83) [listed for 87:16] تِلْكَ ٱلدَّارُ ٱلْءَاخِرَةُ نَجْعَلُهَا لِلَّذِينَ لَا يُرِيدُونَ عُلُوًّۭا فِى ٱلْأَرْضِ وَلَا فَسَادًۭا ۚ وَٱلْعَٰقِبَةُ لِلْمُتَّقِينَ
- (31:24) [listed for 87:16] نُمَتِّعُهُمْ قَلِيلًۭا ثُمَّ نَضْطَرُّهُمْ إِلَىٰ عَذَابٍ غَلِيظٍۢ
- (38:31) [listed for 87:16] إِذْ عُرِضَ عَلَيْهِ بِٱلْعَشِىِّ ٱلصَّٰفِنَٰتُ ٱلْجِيَادُ
- (38:32) [listed for 87:16] فَقَالَ إِنِّىٓ أَحْبَبْتُ حُبَّ ٱلْخَيْرِ عَن ذِكْرِ رَبِّى حَتَّىٰ تَوَارَتْ بِٱلْحِجَابِ
- (53:25) [listed for 87:16] فَلِلَّهِ ٱلْءَاخِرَةُ وَٱلْأُولَىٰ
- (62:11) [listed for 87:16] وَإِذَا رَأَوْا۟ تِجَٰرَةً أَوْ لَهْوًا ٱنفَضُّوٓا۟ إِلَيْهَا وَتَرَكُوكَ قَآئِمًۭا ۚ قُلْ مَا عِندَ ٱللَّهِ خَيْرٌۭ مِّنَ ٱللَّهْوِ وَمِنَ ٱلتِّجَٰرَةِ ۚ وَٱللَّهُ خَيْرُ ٱلرَّٰزِقِينَ
- (76:27) [listed for 87:16] إِنَّ هَٰٓؤُلَآءِ يُحِبُّونَ ٱلْعَاجِلَةَ وَيَذَرُونَ وَرَآءَهُمْ يَوْمًۭا ثَقِيلًۭا
- (77:46) [listed for 87:16] كُلُوا۟ وَتَمَتَّعُوا۟ قَلِيلًا إِنَّكُم مُّجْرِمُونَ
- (93:4) [listed for 87:16] وَلَلْءَاخِرَةُ خَيْرٌۭ لَّكَ مِنَ ٱلْأُولَىٰ

## named by the passage's own list as medium for this ayah (21)

- (2:61) [listed for 87:16] [cited in ¶15] وَإِذْ قُلْتُمْ يَٰمُوسَىٰ لَن نَّصْبِرَ عَلَىٰ طَعَامٍۢ وَٰحِدٍۢ فَٱدْعُ لَنَا رَبَّكَ يُخْرِجْ لَنَا مِمَّا تُنۢبِتُ ٱلْأَرْضُ مِنۢ بَقْلِهَا وَقِثَّآئِهَا وَفُومِهَا وَعَدَسِهَا وَبَصَلِهَا ۖ قَالَ أَتَسْتَبْدِلُونَ ٱلَّذِى هُوَ أَدْنَىٰ بِٱلَّذِى هُوَ خَيْرٌ ۚ ٱهْبِطُوا۟ مِصْرًۭا فَإِنَّ لَكُم مَّا سَأَلْتُمْ ۗ وَضُرِبَتْ عَلَيْهِمُ ٱلذِّلَّةُ وَٱلْمَسْكَنَةُ وَبَآءُو بِغَضَبٍۢ مِّنَ ٱللَّهِ ۗ ذَٰلِكَ بِأَنَّهُمْ كَانُوا۟ يَكْفُرُونَ بِـَٔايَٰتِ ٱللَّهِ وَيَقْتُلُونَ ٱلنَّبِيِّۦنَ بِغَيْرِ ٱلْحَقِّ ۗ ذَٰلِكَ بِمَا عَصَوا۟ وَّكَانُوا۟ يَعْتَدُونَ
- (3:157) [listed for 87:16] وَلَئِن قُتِلْتُمْ فِى سَبِيلِ ٱللَّهِ أَوْ مُتُّمْ لَمَغْفِرَةٌۭ مِّنَ ٱللَّهِ وَرَحْمَةٌ خَيْرٌۭ مِّمَّا يَجْمَعُونَ
- (3:176) [listed for 87:16] وَلَا يَحْزُنكَ ٱلَّذِينَ يُسَٰرِعُونَ فِى ٱلْكُفْرِ ۚ إِنَّهُمْ لَن يَضُرُّوا۟ ٱللَّهَ شَيْـًۭٔا ۗ يُرِيدُ ٱللَّهُ أَلَّا يَجْعَلَ لَهُمْ حَظًّۭا فِى ٱلْءَاخِرَةِ ۖ وَلَهُمْ عَذَابٌ عَظِيمٌ
- (5:100) [listed for 87:16] قُل لَّا يَسْتَوِى ٱلْخَبِيثُ وَٱلطَّيِّبُ وَلَوْ أَعْجَبَكَ كَثْرَةُ ٱلْخَبِيثِ ۚ فَٱتَّقُوا۟ ٱللَّهَ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ لَعَلَّكُمْ تُفْلِحُونَ
- (7:176) [listed for 87:16] وَلَوْ شِئْنَا لَرَفَعْنَٰهُ بِهَا وَلَٰكِنَّهُۥٓ أَخْلَدَ إِلَى ٱلْأَرْضِ وَٱتَّبَعَ هَوَىٰهُ ۚ فَمَثَلُهُۥ كَمَثَلِ ٱلْكَلْبِ إِن تَحْمِلْ عَلَيْهِ يَلْهَثْ أَوْ تَتْرُكْهُ يَلْهَث ۚ ذَّٰلِكَ مَثَلُ ٱلْقَوْمِ ٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِنَا ۚ فَٱقْصُصِ ٱلْقَصَصَ لَعَلَّهُمْ يَتَفَكَّرُونَ
- (9:69) [listed for 87:16] كَٱلَّذِينَ مِن قَبْلِكُمْ كَانُوٓا۟ أَشَدَّ مِنكُمْ قُوَّةًۭ وَأَكْثَرَ أَمْوَٰلًۭا وَأَوْلَٰدًۭا فَٱسْتَمْتَعُوا۟ بِخَلَٰقِهِمْ فَٱسْتَمْتَعْتُم بِخَلَٰقِكُمْ كَمَا ٱسْتَمْتَعَ ٱلَّذِينَ مِن قَبْلِكُم بِخَلَٰقِهِمْ وَخُضْتُمْ كَٱلَّذِى خَاضُوٓا۟ ۚ أُو۟لَٰٓئِكَ حَبِطَتْ أَعْمَٰلُهُمْ فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (10:58) [listed for 87:16] قُلْ بِفَضْلِ ٱللَّهِ وَبِرَحْمَتِهِۦ فَبِذَٰلِكَ فَلْيَفْرَحُوا۟ هُوَ خَيْرٌۭ مِّمَّا يَجْمَعُونَ
- (12:20) [listed for 87:16] وَشَرَوْهُ بِثَمَنٍۭ بَخْسٍۢ دَرَٰهِمَ مَعْدُودَةٍۢ وَكَانُوا۟ فِيهِ مِنَ ٱلزَّٰهِدِينَ
- (16:55) [listed for 87:16] لِيَكْفُرُوا۟ بِمَآ ءَاتَيْنَٰهُمْ ۚ فَتَمَتَّعُوا۟ ۖ فَسَوْفَ تَعْلَمُونَ
- (18:7) [listed for 87:16] إِنَّا جَعَلْنَا مَا عَلَى ٱلْأَرْضِ زِينَةًۭ لَّهَا لِنَبْلُوَهُمْ أَيُّهُمْ أَحْسَنُ عَمَلًۭا
- (20:73) [listed for 87:16] [cited in ¶8] إِنَّآ ءَامَنَّا بِرَبِّنَا لِيَغْفِرَ لَنَا خَطَٰيَٰنَا وَمَآ أَكْرَهْتَنَا عَلَيْهِ مِنَ ٱلسِّحْرِ ۗ وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ
- (26:205) [listed for 87:16] أَفَرَءَيْتَ إِن مَّتَّعْنَٰهُمْ سِنِينَ
- (43:32) [listed for 87:16] أَهُمْ يَقْسِمُونَ رَحْمَتَ رَبِّكَ ۚ نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَرَفَعْنَا بَعْضَهُمْ فَوْقَ بَعْضٍۢ دَرَجَٰتٍۢ لِّيَتَّخِذَ بَعْضُهُم بَعْضًۭا سُخْرِيًّۭا ۗ وَرَحْمَتُ رَبِّكَ خَيْرٌۭ مِّمَّا يَجْمَعُونَ
- (43:33) [listed for 87:16] وَلَوْلَآ أَن يَكُونَ ٱلنَّاسُ أُمَّةًۭ وَٰحِدَةًۭ لَّجَعَلْنَا لِمَن يَكْفُرُ بِٱلرَّحْمَٰنِ لِبُيُوتِهِمْ سُقُفًۭا مِّن فِضَّةٍۢ وَمَعَارِجَ عَلَيْهَا يَظْهَرُونَ
- (44:9) [listed for 87:16] بَلْ هُمْ فِى شَكٍّۢ يَلْعَبُونَ
- (69:23) [listed for 87:16] قُطُوفُهَا دَانِيَةٌۭ
- (75:5) [listed for 87:16] بَلْ يُرِيدُ ٱلْإِنسَٰنُ لِيَفْجُرَ أَمَامَهُۥ
- (89:20) [listed for 87:16] وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
- (91:10) [listed for 87:16] وَقَدْ خَابَ مَن دَسَّىٰهَا
- (102:2) [listed for 87:16] حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ
- (103:1) [listed for 87:16] وَٱلْعَصْرِ

## weak (this ayah's own list) (18)

- (2:154) [listed for 87:16] وَلَا تَقُولُوا۟ لِمَن يُقْتَلُ فِى سَبِيلِ ٱللَّهِ أَمْوَٰتٌۢ ۚ بَلْ أَحْيَآءٌۭ وَلَٰكِن لَّا تَشْعُرُونَ
- (2:179) [listed for 87:16] وَلَكُمْ فِى ٱلْقِصَاصِ حَيَوٰةٌۭ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ لَعَلَّكُمْ تَتَّقُونَ
- (2:243) [listed for 87:16] ۞ أَلَمْ تَرَ إِلَى ٱلَّذِينَ خَرَجُوا۟ مِن دِيَٰرِهِمْ وَهُمْ أُلُوفٌ حَذَرَ ٱلْمَوْتِ فَقَالَ لَهُمُ ٱللَّهُ مُوتُوا۟ ثُمَّ أَحْيَٰهُمْ ۚ إِنَّ ٱللَّهَ لَذُو فَضْلٍ عَلَى ٱلنَّاسِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَشْكُرُونَ
- (2:258) [listed for 87:16] أَلَمْ تَرَ إِلَى ٱلَّذِى حَآجَّ إِبْرَٰهِۦمَ فِى رَبِّهِۦٓ أَنْ ءَاتَىٰهُ ٱللَّهُ ٱلْمُلْكَ إِذْ قَالَ إِبْرَٰهِۦمُ رَبِّىَ ٱلَّذِى يُحْىِۦ وَيُمِيتُ قَالَ أَنَا۠ أُحْىِۦ وَأُمِيتُ ۖ قَالَ إِبْرَٰهِۦمُ فَإِنَّ ٱللَّهَ يَأْتِى بِٱلشَّمْسِ مِنَ ٱلْمَشْرِقِ فَأْتِ بِهَا مِنَ ٱلْمَغْرِبِ فَبُهِتَ ٱلَّذِى كَفَرَ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلظَّٰلِمِينَ
- (2:259) [listed for 87:16] أَوْ كَٱلَّذِى مَرَّ عَلَىٰ قَرْيَةٍۢ وَهِىَ خَاوِيَةٌ عَلَىٰ عُرُوشِهَا قَالَ أَنَّىٰ يُحْىِۦ هَٰذِهِ ٱللَّهُ بَعْدَ مَوْتِهَا ۖ فَأَمَاتَهُ ٱللَّهُ مِا۟ئَةَ عَامٍۢ ثُمَّ بَعَثَهُۥ ۖ قَالَ كَمْ لَبِثْتَ ۖ قَالَ لَبِثْتُ يَوْمًا أَوْ بَعْضَ يَوْمٍۢ ۖ قَالَ بَل لَّبِثْتَ مِا۟ئَةَ عَامٍۢ فَٱنظُرْ إِلَىٰ طَعَامِكَ وَشَرَابِكَ لَمْ يَتَسَنَّهْ ۖ وَٱنظُرْ إِلَىٰ حِمَارِكَ وَلِنَجْعَلَكَ ءَايَةًۭ لِّلنَّاسِ ۖ وَٱنظُرْ إِلَى ٱلْعِظَامِ كَيْفَ نُنشِزُهَا ثُمَّ نَكْسُوهَا لَحْمًۭا ۚ فَلَمَّا تَبَيَّنَ لَهُۥ قَالَ أَعْلَمُ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (3:117) [listed for 87:16] مَثَلُ مَا يُنفِقُونَ فِى هَٰذِهِ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَثَلِ رِيحٍۢ فِيهَا صِرٌّ أَصَابَتْ حَرْثَ قَوْمٍۢ ظَلَمُوٓا۟ أَنفُسَهُمْ فَأَهْلَكَتْهُ ۚ وَمَا ظَلَمَهُمُ ٱللَّهُ وَلَٰكِنْ أَنفُسَهُمْ يَظْلِمُونَ
- (5:46) [listed for 87:16] وَقَفَّيْنَا عَلَىٰٓ ءَاثَٰرِهِم بِعِيسَى ٱبْنِ مَرْيَمَ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ مِنَ ٱلتَّوْرَىٰةِ ۖ وَءَاتَيْنَٰهُ ٱلْإِنجِيلَ فِيهِ هُدًۭى وَنُورٌۭ وَمُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ مِنَ ٱلتَّوْرَىٰةِ وَهُدًۭى وَمَوْعِظَةًۭ لِّلْمُتَّقِينَ
- (7:152) [listed for 87:16] إِنَّ ٱلَّذِينَ ٱتَّخَذُوا۟ ٱلْعِجْلَ سَيَنَالُهُمْ غَضَبٌۭ مِّن رَّبِّهِمْ وَذِلَّةٌۭ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَكَذَٰلِكَ نَجْزِى ٱلْمُفْتَرِينَ
- (9:55) [listed for 87:16] فَلَا تُعْجِبْكَ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُمْ ۚ إِنَّمَا يُرِيدُ ٱللَّهُ لِيُعَذِّبَهُم بِهَا فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَتَزْهَقَ أَنفُسُهُمْ وَهُمْ كَٰفِرُونَ
- (9:74) [listed for 87:16] يَحْلِفُونَ بِٱللَّهِ مَا قَالُوا۟ وَلَقَدْ قَالُوا۟ كَلِمَةَ ٱلْكُفْرِ وَكَفَرُوا۟ بَعْدَ إِسْلَٰمِهِمْ وَهَمُّوا۟ بِمَا لَمْ يَنَالُوا۟ ۚ وَمَا نَقَمُوٓا۟ إِلَّآ أَنْ أَغْنَىٰهُمُ ٱللَّهُ وَرَسُولُهُۥ مِن فَضْلِهِۦ ۚ فَإِن يَتُوبُوا۟ يَكُ خَيْرًۭا لَّهُمْ ۖ وَإِن يَتَوَلَّوْا۟ يُعَذِّبْهُمُ ٱللَّهُ عَذَابًا أَلِيمًۭا فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۚ وَمَا لَهُمْ فِى ٱلْأَرْضِ مِن وَلِىٍّۢ وَلَا نَصِيرٍۢ
- (9:85) [listed for 87:16] وَلَا تُعْجِبْكَ أَمْوَٰلُهُمْ وَأَوْلَٰدُهُمْ ۚ إِنَّمَا يُرِيدُ ٱللَّهُ أَن يُعَذِّبَهُم بِهَا فِى ٱلدُّنْيَا وَتَزْهَقَ أَنفُسُهُمْ وَهُمْ كَٰفِرُونَ
- (30:3) [listed for 87:16] فِىٓ أَدْنَى ٱلْأَرْضِ وَهُم مِّنۢ بَعْدِ غَلَبِهِمْ سَيَغْلِبُونَ
- (43:23) [listed for 87:16] [cited in ¶26] وَكَذَٰلِكَ مَآ أَرْسَلْنَا مِن قَبْلِكَ فِى قَرْيَةٍۢ مِّن نَّذِيرٍ إِلَّا قَالَ مُتْرَفُوهَآ إِنَّا وَجَدْنَآ ءَابَآءَنَا عَلَىٰٓ أُمَّةٍۢ وَإِنَّا عَلَىٰٓ ءَاثَٰرِهِم مُّقْتَدُونَ
- (47:12) [listed for 87:16] إِنَّ ٱللَّهَ يُدْخِلُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ وَٱلَّذِينَ كَفَرُوا۟ يَتَمَتَّعُونَ وَيَأْكُلُونَ كَمَا تَأْكُلُ ٱلْأَنْعَٰمُ وَٱلنَّارُ مَثْوًۭى لَّهُمْ
- (48:29) [listed for 87:16] مُّحَمَّدٌۭ رَّسُولُ ٱللَّهِ ۚ وَٱلَّذِينَ مَعَهُۥٓ أَشِدَّآءُ عَلَى ٱلْكُفَّارِ رُحَمَآءُ بَيْنَهُمْ ۖ تَرَىٰهُمْ رُكَّعًۭا سُجَّدًۭا يَبْتَغُونَ فَضْلًۭا مِّنَ ٱللَّهِ وَرِضْوَٰنًۭا ۖ سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ ۚ ذَٰلِكَ مَثَلُهُمْ فِى ٱلتَّوْرَىٰةِ ۚ وَمَثَلُهُمْ فِى ٱلْإِنجِيلِ كَزَرْعٍ أَخْرَجَ شَطْـَٔهُۥ فَـَٔازَرَهُۥ فَٱسْتَغْلَظَ فَٱسْتَوَىٰ عَلَىٰ سُوقِهِۦ يُعْجِبُ ٱلزُّرَّاعَ لِيَغِيظَ بِهِمُ ٱلْكُفَّارَ ۗ وَعَدَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِنْهُم مَّغْفِرَةًۭ وَأَجْرًا عَظِيمًۢا
- (67:5) [listed for 87:16] وَلَقَدْ زَيَّنَّا ٱلسَّمَآءَ ٱلدُّنْيَا بِمَصَٰبِيحَ وَجَعَلْنَٰهَا رُجُومًۭا لِّلشَّيَٰطِينِ ۖ وَأَعْتَدْنَا لَهُمْ عَذَابَ ٱلسَّعِيرِ
- (74:24) [listed for 87:16] [cited in ¶29] فَقَالَ إِنْ هَٰذَآ إِلَّا سِحْرٌۭ يُؤْثَرُ
- (75:40) [listed for 87:16] أَلَيْسَ ذَٰلِكَ بِقَٰدِرٍ عَلَىٰٓ أَن يُحْۦِىَ ٱلْمَوْتَىٰ

## named by the passage's own list as weak for this ayah (6)

- (5:32) [listed for 87:16] مِنْ أَجْلِ ذَٰلِكَ كَتَبْنَا عَلَىٰ بَنِىٓ إِسْرَٰٓءِيلَ أَنَّهُۥ مَن قَتَلَ نَفْسًۢا بِغَيْرِ نَفْسٍ أَوْ فَسَادٍۢ فِى ٱلْأَرْضِ فَكَأَنَّمَا قَتَلَ ٱلنَّاسَ جَمِيعًۭا وَمَنْ أَحْيَاهَا فَكَأَنَّمَآ أَحْيَا ٱلنَّاسَ جَمِيعًۭا ۚ وَلَقَدْ جَآءَتْهُمْ رُسُلُنَا بِٱلْبَيِّنَٰتِ ثُمَّ إِنَّ كَثِيرًۭا مِّنْهُم بَعْدَ ذَٰلِكَ فِى ٱلْأَرْضِ لَمُسْرِفُونَ
- (27:66) [listed for 87:16] بَلِ ٱدَّٰرَكَ عِلْمُهُمْ فِى ٱلْءَاخِرَةِ ۚ بَلْ هُمْ فِى شَكٍّۢ مِّنْهَا ۖ بَلْ هُم مِّنْهَا عَمُونَ
- (53:8) [listed for 87:16] ثُمَّ دَنَا فَتَدَلَّىٰ
- (53:22) [listed for 87:16] تِلْكَ إِذًۭا قِسْمَةٌۭ ضِيزَىٰٓ
- (77:25) [listed for 87:16] أَلَمْ نَجْعَلِ ٱلْأَرْضَ كِفَاتًا
- (82:14) [listed for 87:16] وَإِنَّ ٱلْفُجَّارَ لَفِى جَحِيمٍۢ

## neighbours: within two ayat of a passage the commentary cites (66)

- (2:59) [next to 2:61] فَبَدَّلَ ٱلَّذِينَ ظَلَمُوا۟ قَوْلًا غَيْرَ ٱلَّذِى قِيلَ لَهُمْ فَأَنزَلْنَا عَلَى ٱلَّذِينَ ظَلَمُوا۟ رِجْزًۭا مِّنَ ٱلسَّمَآءِ بِمَا كَانُوا۟ يَفْسُقُونَ
- (2:60) [next to 2:61] ۞ وَإِذِ ٱسْتَسْقَىٰ مُوسَىٰ لِقَوْمِهِۦ فَقُلْنَا ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۖ كُلُوا۟ وَٱشْرَبُوا۟ مِن رِّزْقِ ٱللَّهِ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
- (2:62) [next to 2:61] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَٱلَّذِينَ هَادُوا۟ وَٱلنَّصَٰرَىٰ وَٱلصَّٰبِـِٔينَ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَعَمِلَ صَٰلِحًۭا فَلَهُمْ أَجْرُهُمْ عِندَ رَبِّهِمْ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (2:63) [next to 2:61] وَإِذْ أَخَذْنَا مِيثَٰقَكُمْ وَرَفَعْنَا فَوْقَكُمُ ٱلطُّورَ خُذُوا۟ مَآ ءَاتَيْنَٰكُم بِقُوَّةٍۢ وَٱذْكُرُوا۟ مَا فِيهِ لَعَلَّكُمْ تَتَّقُونَ
- (7:167) [next to 7:169] وَإِذْ تَأَذَّنَ رَبُّكَ لَيَبْعَثَنَّ عَلَيْهِمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ مَن يَسُومُهُمْ سُوٓءَ ٱلْعَذَابِ ۗ إِنَّ رَبَّكَ لَسَرِيعُ ٱلْعِقَابِ ۖ وَإِنَّهُۥ لَغَفُورٌۭ رَّحِيمٌۭ
- (7:168) [next to 7:169] وَقَطَّعْنَٰهُمْ فِى ٱلْأَرْضِ أُمَمًۭا ۖ مِّنْهُمُ ٱلصَّٰلِحُونَ وَمِنْهُمْ دُونَ ذَٰلِكَ ۖ وَبَلَوْنَٰهُم بِٱلْحَسَنَٰتِ وَٱلسَّيِّـَٔاتِ لَعَلَّهُمْ يَرْجِعُونَ
- (7:171) [next to 7:169] ۞ وَإِذْ نَتَقْنَا ٱلْجَبَلَ فَوْقَهُمْ كَأَنَّهُۥ ظُلَّةٌۭ وَظَنُّوٓا۟ أَنَّهُۥ وَاقِعٌۢ بِهِمْ خُذُوا۟ مَآ ءَاتَيْنَٰكُم بِقُوَّةٍۢ وَٱذْكُرُوا۟ مَا فِيهِ لَعَلَّكُمْ تَتَّقُونَ
- (7:172) [next to 7:170] وَإِذْ أَخَذَ رَبُّكَ مِنۢ بَنِىٓ ءَادَمَ مِن ظُهُورِهِمْ ذُرِّيَّتَهُمْ وَأَشْهَدَهُمْ عَلَىٰٓ أَنفُسِهِمْ أَلَسْتُ بِرَبِّكُمْ ۖ قَالُوا۟ بَلَىٰ ۛ شَهِدْنَآ ۛ أَن تَقُولُوا۟ يَوْمَ ٱلْقِيَٰمَةِ إِنَّا كُنَّا عَنْ هَٰذَا غَٰفِلِينَ
- (8:40) [next to 8:42] وَإِن تَوَلَّوْا۟ فَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ مَوْلَىٰكُمْ ۚ نِعْمَ ٱلْمَوْلَىٰ وَنِعْمَ ٱلنَّصِيرُ
- (8:41) [next to 8:42] ۞ وَٱعْلَمُوٓا۟ أَنَّمَا غَنِمْتُم مِّن شَىْءٍۢ فَأَنَّ لِلَّهِ خُمُسَهُۥ وَلِلرَّسُولِ وَلِذِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَٱبْنِ ٱلسَّبِيلِ إِن كُنتُمْ ءَامَنتُم بِٱللَّهِ وَمَآ أَنزَلْنَا عَلَىٰ عَبْدِنَا يَوْمَ ٱلْفُرْقَانِ يَوْمَ ٱلْتَقَى ٱلْجَمْعَانِ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (8:43) [next to 8:42] إِذْ يُرِيكَهُمُ ٱللَّهُ فِى مَنَامِكَ قَلِيلًۭا ۖ وَلَوْ أَرَىٰكَهُمْ كَثِيرًۭا لَّفَشِلْتُمْ وَلَتَنَٰزَعْتُمْ فِى ٱلْأَمْرِ وَلَٰكِنَّ ٱللَّهَ سَلَّمَ ۗ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (8:44) [next to 8:42] وَإِذْ يُرِيكُمُوهُمْ إِذِ ٱلْتَقَيْتُمْ فِىٓ أَعْيُنِكُمْ قَلِيلًۭا وَيُقَلِّلُكُمْ فِىٓ أَعْيُنِهِمْ لِيَقْضِىَ ٱللَّهُ أَمْرًۭا كَانَ مَفْعُولًۭا ۗ وَإِلَى ٱللَّهِ تُرْجَعُ ٱلْأُمُورُ
- (12:89) [next to 12:91] قَالَ هَلْ عَلِمْتُم مَّا فَعَلْتُم بِيُوسُفَ وَأَخِيهِ إِذْ أَنتُمْ جَٰهِلُونَ
- (12:90) [next to 12:91] قَالُوٓا۟ أَءِنَّكَ لَأَنتَ يُوسُفُ ۖ قَالَ أَنَا۠ يُوسُفُ وَهَٰذَآ أَخِى ۖ قَدْ مَنَّ ٱللَّهُ عَلَيْنَآ ۖ إِنَّهُۥ مَن يَتَّقِ وَيَصْبِرْ فَإِنَّ ٱللَّهَ لَا يُضِيعُ أَجْرَ ٱلْمُحْسِنِينَ
- (12:92) [next to 12:91] قَالَ لَا تَثْرِيبَ عَلَيْكُمُ ٱلْيَوْمَ ۖ يَغْفِرُ ٱللَّهُ لَكُمْ ۖ وَهُوَ أَرْحَمُ ٱلرَّٰحِمِينَ
- (12:93) [next to 12:91] ٱذْهَبُوا۟ بِقَمِيصِى هَٰذَا فَأَلْقُوهُ عَلَىٰ وَجْهِ أَبِى يَأْتِ بَصِيرًۭا وَأْتُونِى بِأَهْلِكُمْ أَجْمَعِينَ
- (18:43) [next to 18:45] وَلَمْ تَكُن لَّهُۥ فِئَةٌۭ يَنصُرُونَهُۥ مِن دُونِ ٱللَّهِ وَمَا كَانَ مُنتَصِرًا
- (18:44) [next to 18:45] هُنَالِكَ ٱلْوَلَٰيَةُ لِلَّهِ ٱلْحَقِّ ۚ هُوَ خَيْرٌۭ ثَوَابًۭا وَخَيْرٌ عُقْبًۭا
- (18:47) [next to 18:45] وَيَوْمَ نُسَيِّرُ ٱلْجِبَالَ وَتَرَى ٱلْأَرْضَ بَارِزَةًۭ وَحَشَرْنَٰهُمْ فَلَمْ نُغَادِرْ مِنْهُمْ أَحَدًۭا
- (18:48) [next to 18:46] وَعُرِضُوا۟ عَلَىٰ رَبِّكَ صَفًّۭا لَّقَدْ جِئْتُمُونَا كَمَا خَلَقْنَٰكُمْ أَوَّلَ مَرَّةٍۭ ۚ بَلْ زَعَمْتُمْ أَلَّن نَّجْعَلَ لَكُم مَّوْعِدًۭا
- (20:70) [next to 20:72] فَأُلْقِىَ ٱلسَّحَرَةُ سُجَّدًۭا قَالُوٓا۟ ءَامَنَّا بِرَبِّ هَٰرُونَ وَمُوسَىٰ
- (20:71) [next to 20:72] قَالَ ءَامَنتُمْ لَهُۥ قَبْلَ أَنْ ءَاذَنَ لَكُمْ ۖ إِنَّهُۥ لَكَبِيرُكُمُ ٱلَّذِى عَلَّمَكُمُ ٱلسِّحْرَ ۖ فَلَأُقَطِّعَنَّ أَيْدِيَكُمْ وَأَرْجُلَكُم مِّنْ خِلَٰفٍۢ وَلَأُصَلِّبَنَّكُمْ فِى جُذُوعِ ٱلنَّخْلِ وَلَتَعْلَمُنَّ أَيُّنَآ أَشَدُّ عَذَابًۭا وَأَبْقَىٰ
- (20:74) [next to 20:72] إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- (20:75) [next to 20:73] وَمَن يَأْتِهِۦ مُؤْمِنًۭا قَدْ عَمِلَ ٱلصَّٰلِحَٰتِ فَأُو۟لَٰٓئِكَ لَهُمُ ٱلدَّرَجَٰتُ ٱلْعُلَىٰ
- (29:62) [next to 29:64] ٱللَّهُ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ وَيَقْدِرُ لَهُۥٓ ۚ إِنَّ ٱللَّهَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (29:63) [next to 29:64] وَلَئِن سَأَلْتَهُم مَّن نَّزَّلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ مِنۢ بَعْدِ مَوْتِهَا لَيَقُولُنَّ ٱللَّهُ ۚ قُلِ ٱلْحَمْدُ لِلَّهِ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْقِلُونَ
- (29:65) [next to 29:64] فَإِذَا رَكِبُوا۟ فِى ٱلْفُلْكِ دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ فَلَمَّا نَجَّىٰهُمْ إِلَى ٱلْبَرِّ إِذَا هُمْ يُشْرِكُونَ
- (29:66) [next to 29:64] لِيَكْفُرُوا۟ بِمَآ ءَاتَيْنَٰهُمْ وَلِيَتَمَتَّعُوا۟ ۖ فَسَوْفَ يَعْلَمُونَ
- (36:9) [next to 36:11] وَجَعَلْنَا مِنۢ بَيْنِ أَيْدِيهِمْ سَدًّۭا وَمِنْ خَلْفِهِمْ سَدًّۭا فَأَغْشَيْنَٰهُمْ فَهُمْ لَا يُبْصِرُونَ
- (36:10) [next to 36:11] وَسَوَآءٌ عَلَيْهِمْ ءَأَنذَرْتَهُمْ أَمْ لَمْ تُنذِرْهُمْ لَا يُؤْمِنُونَ
- (36:13) [next to 36:11] وَٱضْرِبْ لَهُم مَّثَلًا أَصْحَٰبَ ٱلْقَرْيَةِ إِذْ جَآءَهَا ٱلْمُرْسَلُونَ
- (36:14) [next to 36:12] إِذْ أَرْسَلْنَآ إِلَيْهِمُ ٱثْنَيْنِ فَكَذَّبُوهُمَا فَعَزَّزْنَا بِثَالِثٍۢ فَقَالُوٓا۟ إِنَّآ إِلَيْكُم مُّرْسَلُونَ
- (43:21) [next to 43:23] أَمْ ءَاتَيْنَٰهُمْ كِتَٰبًۭا مِّن قَبْلِهِۦ فَهُم بِهِۦ مُسْتَمْسِكُونَ
- (43:24) [next to 43:23] ۞ قَٰلَ أَوَلَوْ جِئْتُكُم بِأَهْدَىٰ مِمَّا وَجَدتُّمْ عَلَيْهِ ءَابَآءَكُمْ ۖ قَالُوٓا۟ إِنَّا بِمَآ أُرْسِلْتُم بِهِۦ كَٰفِرُونَ
- (43:25) [next to 43:23] فَٱنتَقَمْنَا مِنْهُمْ ۖ فَٱنظُرْ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ
- (46:2) [next to 46:4] تَنزِيلُ ٱلْكِتَٰبِ مِنَ ٱللَّهِ ٱلْعَزِيزِ ٱلْحَكِيمِ
- (46:3) [next to 46:4] مَا خَلَقْنَا ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَمَا بَيْنَهُمَآ إِلَّا بِٱلْحَقِّ وَأَجَلٍۢ مُّسَمًّۭى ۚ وَٱلَّذِينَ كَفَرُوا۟ عَمَّآ أُنذِرُوا۟ مُعْرِضُونَ
- (46:5) [next to 46:4] وَمَنْ أَضَلُّ مِمَّن يَدْعُوا۟ مِن دُونِ ٱللَّهِ مَن لَّا يَسْتَجِيبُ لَهُۥٓ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ وَهُمْ عَن دُعَآئِهِمْ غَٰفِلُونَ
- (46:6) [next to 46:4] وَإِذَا حُشِرَ ٱلنَّاسُ كَانُوا۟ لَهُمْ أَعْدَآءًۭ وَكَانُوا۟ بِعِبَادَتِهِمْ كَٰفِرِينَ
- (59:7) [next to 59:9] مَّآ أَفَآءَ ٱللَّهُ عَلَىٰ رَسُولِهِۦ مِنْ أَهْلِ ٱلْقُرَىٰ فَلِلَّهِ وَلِلرَّسُولِ وَلِذِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَٱبْنِ ٱلسَّبِيلِ كَىْ لَا يَكُونَ دُولَةًۢ بَيْنَ ٱلْأَغْنِيَآءِ مِنكُمْ ۚ وَمَآ ءَاتَىٰكُمُ ٱلرَّسُولُ فَخُذُوهُ وَمَا نَهَىٰكُمْ عَنْهُ فَٱنتَهُوا۟ ۚ وَٱتَّقُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- (59:8) [next to 59:9] لِلْفُقَرَآءِ ٱلْمُهَٰجِرِينَ ٱلَّذِينَ أُخْرِجُوا۟ مِن دِيَٰرِهِمْ وَأَمْوَٰلِهِمْ يَبْتَغُونَ فَضْلًۭا مِّنَ ٱللَّهِ وَرِضْوَٰنًۭا وَيَنصُرُونَ ٱللَّهَ وَرَسُولَهُۥٓ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلصَّٰدِقُونَ
- (59:10) [next to 59:9] وَٱلَّذِينَ جَآءُو مِنۢ بَعْدِهِمْ يَقُولُونَ رَبَّنَا ٱغْفِرْ لَنَا وَلِإِخْوَٰنِنَا ٱلَّذِينَ سَبَقُونَا بِٱلْإِيمَٰنِ وَلَا تَجْعَلْ فِى قُلُوبِنَا غِلًّۭا لِّلَّذِينَ ءَامَنُوا۟ رَبَّنَآ إِنَّكَ رَءُوفٌۭ رَّحِيمٌ
- (59:11) [next to 59:9] ۞ أَلَمْ تَرَ إِلَى ٱلَّذِينَ نَافَقُوا۟ يَقُولُونَ لِإِخْوَٰنِهِمُ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ لَئِنْ أُخْرِجْتُمْ لَنَخْرُجَنَّ مَعَكُمْ وَلَا نُطِيعُ فِيكُمْ أَحَدًا أَبَدًۭا وَإِن قُوتِلْتُمْ لَنَنصُرَنَّكُمْ وَٱللَّهُ يَشْهَدُ إِنَّهُمْ لَكَٰذِبُونَ
- (74:16) [next to 74:18] كَلَّآ ۖ إِنَّهُۥ كَانَ لِءَايَٰتِنَا عَنِيدًۭا
- (74:17) [next to 74:18] سَأُرْهِقُهُۥ صَعُودًا
- (74:20) [next to 74:18] ثُمَّ قُتِلَ كَيْفَ قَدَّرَ
- (74:21) [next to 74:19] ثُمَّ نَظَرَ
- (74:22) [next to 74:24] ثُمَّ عَبَسَ وَبَسَرَ
- (74:23) [next to 74:24] ثُمَّ أَدْبَرَ وَٱسْتَكْبَرَ
- (74:25) [next to 74:24] إِنْ هَٰذَآ إِلَّا قَوْلُ ٱلْبَشَرِ
- (74:26) [next to 74:24] سَأُصْلِيهِ سَقَرَ
- (75:14) [next to 75:16] بَلِ ٱلْإِنسَٰنُ عَلَىٰ نَفْسِهِۦ بَصِيرَةٌۭ
- (75:15) [next to 75:16] وَلَوْ أَلْقَىٰ مَعَاذِيرَهُۥ
- (75:18) [next to 75:16] فَإِذَا قَرَأْنَٰهُ فَٱتَّبِعْ قُرْءَانَهُۥ
- (75:19) [next to 75:17] ثُمَّ إِنَّ عَلَيْنَا بَيَانَهُۥ
- (75:22) [next to 75:20] وُجُوهٌۭ يَوْمَئِذٍۢ نَّاضِرَةٌ
- (75:23) [next to 75:21] إِلَىٰ رَبِّهَا نَاظِرَةٌۭ
- (79:33) [next to 79:35] مَتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
- (79:34) [next to 79:35] فَإِذَا جَآءَتِ ٱلطَّآمَّةُ ٱلْكُبْرَىٰ
- (79:36) [next to 79:35] وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ
- (79:41) [next to 79:39] فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ
- (79:42) [next to 79:40] يَسْـَٔلُونَكَ عَنِ ٱلسَّاعَةِ أَيَّانَ مُرْسَىٰهَا
- (89:21) [next to 89:23] كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا
- (89:22) [next to 89:23] وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
- (89:25) [next to 89:23] فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- (89:26) [next to 89:24] وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ

