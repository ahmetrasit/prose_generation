Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 88:6; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/88_6/DM.r13.images.r13.map3.nohft.tool.tool.tool/88_6.reading.tr.md (prose paragraphs numbered) =====
## Yüzden bedene

[¶1] İkinci ayetten beşinci ayete kadar anlatılan şey yüzlerdir. Yorulan, ateşe giren ve içirilen hep yüzdür ve fiiller tekil, dişil olarak ona uyar: {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4}; {ar:تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:tuskâ min aynin âniye, gloss:son derece kaynamış bir pınardan içirilir, source:88:5}. Altıncı ayette dil birden değişir: {ar:لَّيْسَ لَهُمْ, tr:leyse lehum, gloss:onların yoktur, source:88:6}. Yüz artık "onlar" olmuştur, yani kişiler. Bu değişiklik konudan gelir. İçecek yüze dökülebilir, ama yemek bir bedene gider. Yedinci ayet de bedenin diliyle konuşur: {ar:لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ, tr:lâ yusminu ve lâ yuğnî min cû', gloss:ne semirtir ne de açlığı giderir, source:88:7}. Semizlik de açlık da yüzün hali değildir, karnın ve kemiğin halidir. Sure böylece yüzün görünen yorgunluğundan bedenin içindeki boşluğa iner.

[¶2] Cümle bu boşluğu iki adımda kurar. İlk adım olumsuzluktur ve ardından gelen "yemek" kelimesi belirsizdir. Böylece tek bir yemek değil, yemek türünün tamamı reddedilir. Araplar bu olumsuzluk sözünü bazen bir türün hiç bulunmadığını söyleyen olumsuzluk yerine kullanırdı: {ar:وربما جاءت ليس بمعنى لا التبرئة, tr:ve rubbemâ câet leyse bi-ma'nâ lâ't-tebrie, gloss:leyse bazen bir türü bütünüyle yok sayan "lâ" anlamında gelir, source:"ل ي س,B003"}. Hiçbir yemek yoktur. İkinci adım istisnadır, ve istisna da "darî'" demez, "darî'den" der: {ar:إِلَّا مِن ضَرِيعٍۢ, tr:illâ min darî', gloss:darî'den olan dışında, source:88:6}. Yemek diye verilen şey, darî'den alınabilen kadardır.

[¶3] Yemeğin kökü çiğnemekle değil tatmakla başlar: {ar:أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء, tr:aslun fî tezevvuki'ş-şey' ve't-taâmu huve'l-me'kûl ve'l-it'âmu yekau hatta'l-mâ', gloss:kök bir şeyi tatmaktır; taâm yenendir; doyurmak suyu bile kapsar, source:"ط ع م,B001"}; {ar:الطعم ذوقه والطعام اسم جامع لكل ما يؤكل, tr:et-ta'mu zevkuhû ve't-taâmu ismun câmiun li-külli mâ yu'kel, gloss:ta'm bir şeyin tadıdır; taâm yenen her şeyin genel adıdır, source:"ط ع م,B001"}. Kur'an bu fiili su için de kullanır. Tâlût askerleriyle yola çıktığında onlara Allah'ın kendilerini bir ırmakla sınayacağını söyler ve şöyle der: {ar:فَمَن شَرِبَ مِنْهُ فَلَيْسَ مِنِّى وَمَن لَّمْ يَطْعَمْهُ فَإِنَّهُۥ مِنِّىٓ, tr:fe-men şeribe minhu fe-leyse minnî ve men lem yat'amhu fe-innehû minnî, gloss:ondan içen benden değildir; onu tatmayan bendendir, source:2:249}. Irmağın suyu orada "tadılan" şeydir. Beşinci ayetteki kaynar içecek ile bu ayetteki yemek, böylece tek bir öğünün iki yanı olur. Kur'an aynı kuruluşu tatma fiiliyle bir başka yerde de kurar. Cehennemin azgınları beklediği anlatılırken şöyle denir: {ar:لَّا يَذُوقُونَ فِيهَا بَرْدًۭا وَلَا شَرَابًا, tr:lâ yezûkûne fîhâ berden ve lâ şerâbâ, gloss:orada ne bir serinlik ne bir içecek tadarlar, source:78:24}; {ar:إِلَّا حَمِيمًۭا وَغَسَّاقًۭا, tr:illâ hamîmen ve ğassâkâ, gloss:kaynar su ve irinden başka, source:78:25}. Önce bir tür bütünüyle reddedilir, sonra istisna gelir ve istisna, reddedilenin yokluğunu daha da ağırlaştırır.

## Kuruyunca verilen ad

[¶4] ضريع bir bitkinin adıdır, ama o bitkinin belirli bir halinin adıdır: {ar:الضريع يبيس الشبرق وهو نبت, tr:ed-darîu yebîsu'ş-şibrik ve huve nebt, gloss:darî' kurumuş şibriktir; bir bitkidir, source:"ض ر ع,B005"}. Hicaz halkının bu adı ne zaman kullandığı da söylenir: {ar:الضريع نبت يقال له الشبرق وأهل الحجاز يسمونه الضريع إذا يبس, tr:ed-darîu nebtun yukâlü lehu'ş-şibrik ve ehlü'l-Hicâzi yüsemmûnehu'd-darîa izâ yebis, gloss:şibrik denen bir bitkidir; Hicaz halkı kuruyunca ona darî' der, source:"ض ر ع,B005"}. Başka bir tarife göre ise kırmızı ve kötü kokulu bir bitkidir: {ar:قيل هو يبيس الشبرق وقيل نبات أحمر منتن الريح, tr:kîle huve yebîsu'ş-şibrik ve kîle nebâtun ahmeru müntinü'r-rîh, gloss:kurumuş şibrik ya da kırmızı ve pis kokulu bir bitki, source:"ض ر ع,B005"}. Şibrik dikenli bir ottur. Yeşilken bir adı vardır, kuruyunca başka bir ad alır. Ayetteki yemek yaşayan bir bitki değildir. Suyu çekilmiş bir bitkinin geriye kalanıdır.

[¶5] Kur'an yemeğin nereden geldiğini bir başka surede adım adım gösterir. İnsana kendi yaratılışı hatırlatıldıktan sonra şöyle denir: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakınca gördüğü şey bir sıradır: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:suyu bol bol döktük, source:80:25}; {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:summe şakakne'l-arda şakkâ, gloss:sonra yeri yardıkça yardık, source:80:26}; {ar:فَأَنۢبَتْنَا فِيهَا حَبًّۭا, tr:fe-enbetnâ fîhâ habbâ, gloss:orada tane bitirdik, source:80:27}. Ardından üzüm, yonca, zeytin, hurma, meyve ve otlar sayılır ve sıra şöyle biter: {ar:مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ, tr:metâan lekum ve li-en'âmikum, gloss:size ve hayvanlarınıza yararlanma olsun diye, source:80:32}. Orada yemek, suyun toprakta gördüğü iştir. Darî' bu sıranın sonundan geriye doğru okunur: su gelmemiş, ot kurumuş ve yemek diye geriye bu kalmıştır. İkinci ayetteki {ar:خَٰشِعَةٌ, tr:hâşia, gloss:eğik, çökmüş, source:88:2} kelimesi Arapçada yağmur almamış, kuruyup çökmüş toprak için de söylenir. Bu yüzden kuru yüz ile kuru yemek surenin kendi sahnesinde yan yana durur.

[¶6] Kur'an cehennemin başka bir bitkisini de yemek diye anar: {ar:إِنَّ شَجَرَتَ ٱلزَّقُّومِ, tr:inne şeceratez-zakkûm, gloss:zakkum ağacı, source:44:43}; {ar:طَعَامُ ٱلْأَثِيمِ, tr:taâmu'l-esîm, gloss:günahkârın yemeğidir, source:44:44}. Bahçe ehlinin sofrası anlatıldıktan sonra soru şöyle sorulur: {ar:أَذَٰلِكَ خَيْرٌۭ نُّزُلًا أَمْ شَجَرَةُ ٱلزَّقُّومِ, tr:e-zâlike hayrun nuzulen em şeceratü'z-zakkûm, gloss:konuğa sunulan ağırlama olarak bu mu hayırlı, yoksa zakkum ağacı mı, source:37:62}. O ağaç {ar:شَجَرَةٌۭ تَخْرُجُ فِىٓ أَصْلِ ٱلْجَحِيمِ, tr:şeceratun tahrucu fî asli'l-cahîm, gloss:cehennemin dibinde çıkan bir ağaç, source:37:64} diye anlatılır ve yiyenler için {ar:فَمَالِـُٔونَ مِنْهَا ٱلْبُطُونَ, tr:fe-mâliûne minhe'l-butûn, gloss:karınlarını ondan dolduracaklar, source:37:66} denir. Zakkum hiç değilse karnı doldurur. Darî' için yedinci ayet açlığı gidermeyi bile esirger.

[¶7] Bu ayette darî' bir ottur. Kökün öteki dallarından gelen resimler bu anlamın yerine geçmez, onun yanında duyulur. Bu kökten gelen dar' kelimesi, tabanlı ya da tırnaklı her hayvanın memesidir: {ar:الضرع لكل ذات خف أو ظلف, tr:ed-dar'u li-külli zâti huffin ev zılf, gloss:dar' tabanlı ve tırnaklı her hayvanın memesidir, source:"ض ر ع,B001"}. Memenin adını yumuşaklığından aldığı söylenirdi: {ar:ضرع الشاة وغيرها سمي بذلك لما فيه من لين, tr:dar'u'ş-şâti ve ğayrihâ summiye bi-zâlike limâ fîhi min lîn, gloss:koyunun ve başka hayvanların memesi, içindeki yumuşaklık yüzünden böyle adlandırılmıştır, source:"ض ر ع,B001"}. Meme sütü toplayan ve veren organdır. Doğum yaklaşınca dolar: {ar:أضرعت الشاة نزل لبنها قبيل النتاج, tr:edraati'ş-şâtu nezele lebenühâ kubeyle'n-nitâc, gloss:koyunun sütü doğumdan hemen önce memeye indi, source:"ض ر ع,B001"}. Memesi iri koyuna da tam ayetteki kalıpla darî' denirdi: {ar:شاة ضريع وضريعة عظيمة الضرع, tr:şâtun darîun ve darîatun azîmetü'd-dar', gloss:memesi iri koyun, source:"ض ر ع,B001"}. Aynı kelime ayette kupkuru, sert bir otun adıdır. Otlakta ise yumuşak ve sütle dolu bir hayvanın adıdır. Yemek diye verilen ot, adının öbür ucunda o yemeğin hiç taşımadığı bolluğu taşır. On yedinci ayet bakışı {ar:ٱلْإِبِلِ, tr:el-ibil, gloss:develer, source:88:17} üzerine çevirdiğinde, bu memenin dünyadaki sahibi de göz önüne gelmiş olur. Kökün bir başka dalında ise darî' ince, sulu bir içecektir: {ar:الضريع الشراب الرقيق, tr:ed-darîu'ş-şerâbü'r-rakîk, gloss:darî' ince içecektir, source:"ض ر ع,B011"}. Kuru ot da ince içecek de aynı eksiği paylaşır: ikisinde de doyuracak bir öz yoktur.

## Tat, ilik ve olgunluk

[¶8] Yemek kelimesinin akrabaları, bir şeyin ne zaman yemek olduğunu da söyler. Hurmanın meyvesi olgunlaşınca ona "tat aldı" denirdi: {ar:أطعمت النخلة واطعمت البسرة صار لها طعم وأخذت الطعم, tr:at'ameti'n-nahle ve't'ameti'l-busra sâra lehâ ta'mun ve ehazeti't-ta'm, gloss:hurma ağacı meyveye durdu; ham hurma tat kazandı, source:"ط ع م,B005"}. Ham meyve henüz yemek sayılmaz, tadı oluşunca yemek olur. Hayvanda da aynı ölçü kullanılırdı. Kesilecek devenin iliğinde yağın tadı varsa ona bu kökten bir ad verilirdi: {ar:المطعم من الإبل الذي يوجد في مخه طعم الشحم, tr:el-mut'imu mine'l-ibili'llezî yûcedu fî muhhihî ta'mu'ş-şahm, gloss:iliğinde yağ tadı bulunan deve, source:"ط ع م,B007"}. Zayıf ile semiz arasındaki deve için de {ar:جزور طعوم وطعيم بين الغثة والسمينة, tr:cezûrun taûmun ve taîmun beyne'l-ğasseti ve's-semîne, gloss:cılız ile semiz arasında kalan kesimlik deve, source:"ط ع م,B007"} denirdi. İlik, kemiğin içindeki yumuşak dokudur. Orada yağ bulunması, beslenmenin bedende en derine kadar işlediğini gösterir. İnsan için de aynı söz kullanılırdı: {ar:ما فلان بذي طعم إذا كان غثا, tr:mâ fulânun bi-zî ta'm izâ kâne ğassâ, gloss:cılız ve değersiz olan için "onun tadı yok" denir, source:"ط ع م,B008"}; {ar:رجل ذو طعم أي ذو عقل وحزم, tr:racülün zû ta'm ey zû aklin ve hazm, gloss:tadı olan adam akıllı ve kararlı adamdır, source:"ط ع م,B008"}. Ta'm böylece bir şeyin içinde biriken özün adıdır: meyvede tat, kemikte yağ, insanda akıl.

[¶9] Yedinci ayetin ilk olumsuzluğu tam bu öze dokunur: {ar:لَّا يُسْمِنُ, tr:lâ yusmin, gloss:semirtmez, source:88:7}. Yemek kelimesinin akrabaları yemeği yağla ve olgunlukla ölçer. Darî'in akrabaları ise zayıflığı adlandırır: {ar:لضارع الجسم أي نحيف ضعيف, tr:le-dâriu'l-cism ey nahîfun daîf, gloss:bedeni cılız ve güçsüz, source:"ض ر ع,B003"}; {ar:رجل ضرع ضعيف, tr:racülün daraun daîf, gloss:dara' adam güçsüz adamdır, source:"ض ر ع,B003"}. Kökün bir dalı da kaburga kemiğini etin altında örten ince zarın adıdır: {ar:الجلدة التي على العظم تحت اللحم من الضلع هي الضريع, tr:el-cildetü'lletî ale'l-azmi tahte'l-lahmi mine'd-dıl'ı hiye'd-darî', gloss:kaburgada etin altında kemiğin üstündeki ince deri darî'dir, source:"ض ر ع,B012"}. Bu, etin altında kemiğe en yakın kattır. Ayetin bir ucundaki kelime, ilikteki yağı ve olgun meyvenin tadını taşır. Öbür ucundaki kelime cılız bedeni ve kemiğe yapışık zarı taşır. Bu iki kelime arasında bir kök bağı yoktur. Bağ, iki ayrı kökün kendi dallarının bu ayette karşı karşıya düşmesinden doğar.

## Ocaktaki tencere, batan güneş

[¶10] Darî'in kökü bazı kalıp sözlerde bir şeyin sonuna yaklaştığı anı adlandırırdı. Ocağa konmuş tencere için şöyle denirdi: {ar:ضرعت القدر أي حان أن تدرك, tr:daraati'l-kıdru ey hâne en tudrik, gloss:tencerenin pişme vakti geldi, source:"ض ر ع,B007"}. Tencere ateşin üstünde içindekini ısıtır ve yemek yavaş yavaş kıvamına gelir. Bu söz, kıvamın vaktinin geldiği anı söyler. Güneş batmaya yaklaştığında da aynı kök kullanılırdı: {ar:تضريع الشمس دنوها للمغيب, tr:tadrîu'ş-şems dunuvvuhâ li'l-mağîb, gloss:güneşin batmaya yaklaşması, source:"ض ر ع,B006"}. Gölge kısaldığında da: {ar:تضرع الظل قل وقلص, tr:tedarraa'z-zıll kalle ve kalas, gloss:gölge azaldı ve kısaldı, source:"ض ر ع,B008"}. Üçünde de bir şey kendi ucuna varmıştır: pişme kıvamına, günün sonuna, gölgenin azalmasına.

[¶11] Kur'an yemeğin pişme vaktini bir başka yerde anar. Allah müminlere Peygamber'in evlerine izinsiz girmemelerini ve yemeğe çağrıldıklarında pişmesini gözleyerek beklememelerini söyler: {ar:إِلَىٰ طَعَامٍ غَيْرَ نَٰظِرِينَ إِنَىٰهُ, tr:ilâ taâmin ğayra nâzırîne inâh, gloss:pişme vaktini gözetmeden bir yemeğe, source:33:53}. Oradaki "pişme vakti", beşinci ayetteki ءَانِيَةٍ kelimesinin köküdür. Dördüncü ayetteki kızgın ateş ve beşinci ayetteki kaynamış pınar, darî'in tencere anlamıyla birlikte bir mutfağın dilini konuşur. Ama darî' otu da kendi ucuna varmış bir bitkidir. Yeşil hali geçmiş, kurumuştur. Olgunlaşınca "tat alan" hurma meyvesinin tersine, bu ot olgunluğu çoktan geride bırakmıştır. Önlerine konan şey, vakti geçmiş bir şeydir.

## Tazarru: yemeğin adındaki boyun eğiş

[¶12] Türkçede "tazarru" bu kökten gelir ve bugün yalnızca dua dilinde, "yalvarma, yakarış" anlamında yaşar. Arapçada aynı kök çok daha geniştir: alçalmak, ihtiyacını açıkça göstermek, cılız ve korkak olmak da bu köktedir. Türkçe kelime bu geniş anlamın yalnızca Allah'a dönen yüzünü taşır. Kökün aslında önce alçalış vardır: {ar:ضرع الرجل ضراعة إذا ذل, tr:dara'a'r-raculu darâaten izâ zell, gloss:adam alçalınca dara'a denir, source:"ض ر ع,B002"}. Bu alçalışın içinde de bir ihtiyaç bulunur: {ar:مظهرين الضراعة وهي شدة الفقر إلى الشيء والحاجة إليه, tr:muzhirîne'd-darâata ve hiye şiddetü'l-fakri ile'ş-şey'i ve'l-hâceti ileyh, gloss:darâayı göstererek; darâa bir şeye şiddetle muhtaç olmaktır, source:"ض ر ع,B002"}. Birine boyun eğip ondan bir şey istemek de böyle anlatılırdı: {ar:ضرع له إذا تخشع له وسأله, tr:dara'a lehû izâ tehaşşea lehû ve seeleh, gloss:birine eğilip ondan istediğinde dara'a lehû denir, source:"ض ر ع,B002"}. Allah'a yönelince de söz duaya döner: {ar:تضرع إلى الله أي ابتهل, tr:tedarraa ilallâh ey ibtehel, gloss:Allah'a yalvardı, source:"ض ر ع,B002"}. Aynı kökün bir dalı korkak adamı da adlandırır: {ar:الضرع الرجل الجبان, tr:ed-daraur-raculu'l-cebân, gloss:dara' korkak adamdır, source:"ض ر ع,B003"}.

[¶13] Kur'an bu kelimeyi en çok, verilmiş ama kullanılmamış bir fırsat için kullanır. Allah Peygamber'e, ondan önce gönderilen topluluklara ne yaptığını anlatır: {ar:فَأَخَذْنَٰهُم بِٱلْبَأْسَآءِ وَٱلضَّرَّآءِ لَعَلَّهُمْ يَتَضَرَّعُونَ, tr:fe-ehaznâhum bi'l-be'sâi ve'd-darrâi leallehum yetedarraûn, gloss:belki boyun eğip yalvarırlar diye onları darlık ve sıkıntıyla yakaladık, source:6:42}. Ardından şunu söyler: {ar:فَلَوْلَآ إِذْ جَآءَهُم بَأْسُنَا تَضَرَّعُوا۟ وَلَٰكِن قَسَتْ قُلُوبُهُمْ, tr:fe-levlâ iz câehum be'sunâ tedarraû ve lâkin kaset kulûbuhum, gloss:keşke baskımız gelince yalvarsalardı; ama kalpleri katılaştı, source:6:43}. Başka bir yerde, sıkıntıları kaldırılsa bile azgınlıklarında direneceklerini söylediği topluluk için Allah şöyle der: {ar:وَلَقَدْ أَخَذْنَٰهُم بِٱلْعَذَابِ فَمَا ٱسْتَكَانُوا۟ لِرَبِّهِمْ وَمَا يَتَضَرَّعُونَ, tr:ve lekad ehaznâhum bi'l-azâbi fe-me'stekânû li-rabbihim ve mâ yetedarraûn, gloss:onları azapla yakaladık; yine de Rablerine boyun eğmediler, yalvarmadılar, source:23:76}. Dua ise bu kelimeyle öğretilir: {ar:ٱدْعُوا۟ رَبَّكُمْ تَضَرُّعًۭا وَخُفْيَةً, tr:ud'û rabbekum tedarruan ve hufyeh, gloss:Rabbinize yalvararak ve gizlice dua edin, source:7:55}.

[¶14] Dünyada tazarru bir davetti ve kapısı açıktı. Darlıkla sarsılan topluluklar ona çağrıldı ve gelmediler. Gâşiye'nin anlattığı insanlar da yirmi üçüncü ayette böyle adlandırılır: {ar:إِلَّا مَن تَوَلَّىٰ وَكَفَرَ, tr:illâ men tevellâ ve kefer, gloss:yüz çeviren ve inkâr eden hariç, source:88:23}. Dünyada kendi istekleriyle girmedikleri boyun eğiş, şimdi önlerine konan tek yemeğin adında durur. Bu boyun eğişi seçmemişlerdir, ama önlerine konmuştur. İkinci ayetteki yüzün eğikliği de Arapçada bu kelimeyle açıklanır: {ar:الخشوع الضراعة, tr:el-huşûu'd-darâa, gloss:huşu boyun eğiştir, source:"خ ش ع,B001"}. Onuncu ayetteki {ar:جَنَّةٍ عَالِيَةٍۢ, tr:cennetin âliye, gloss:yüksek bir bahçe, source:88:10} ile kurulan alçalma ve yükselme karşıtlığı da bu yemeğin adından geçer.

## Doyuran el, kapalı el

[¶15] Yemek kökü yalnızca yemeyi değil, doyurmayı ve doyurulmak istemeyi de taşır: {ar:استطعمه سأله أن يطعمه وأطعمته الطعام, tr:istat'amehû seelehû en yut'imehû ve at'amtühü't-taâm, gloss:ondan kendisini doyurmasını istedi; ona yemek yedirdim, source:"ط ع م,B002"}. İyi beslenen adamın hali de cömert ev sahibinin adı da bu köktendir: {ar:رجل طاعم حسن الحال ومطعام كثير القرى, tr:racülün tâimun hasenü'l-hâl ve mit'âmun kesîrü'l-kırâ, gloss:tâim adam hali iyi adamdır; mit'âm konuğa çok ikram edendir, source:"ط ع م,B004"}. Darî'in kökünde de malı birine açıp sunmak vardır: {ar:أضرعت له مالي أي بذلته له, tr:edra'tü lehû mâlî ey bezeltühû leh, gloss:malımı ona açtım, cömertçe sundum, source:"ض ر ع,B009"}; {ar:ماله لي مضرع أي مبذول, tr:mâluhû lî mudra'un ey mebzûl, gloss:onun malı bana açıktır, source:"ض ر ع,B009"}.

[¶16] Gâşiye bu insanların neden bu yemekle kaldığını tek bir sözle söyler: yüz çevirdiler ve inkâr ettiler. Kur'an'ın başka sahneleri aynı boş tabağı kapalı bir ele bağlar. Kitabı solundan verilen kişi pişmanlığını söyledikten sonra, onun hakkında verilen hüküm şöyle gerekçelendirilir: {ar:إِنَّهُۥ كَانَ لَا يُؤْمِنُ بِٱللَّهِ ٱلْعَظِيمِ, tr:innehû kâne lâ yu'minu billâhi'l-azîm, gloss:o, yüce Allah'a inanmıyordu, source:69:33}; {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ taâmi'l-miskîn, gloss:yoksulu doyurmaya teşvik etmiyordu, source:69:34}. Ve ardından: {ar:فَلَيْسَ لَهُ ٱلْيَوْمَ هَٰهُنَا حَمِيمٌۭ, tr:fe-leyse lehü'l-yevme hâhunâ hamîm, gloss:bugün burada onun yakın bir dostu yoktur, source:69:35}; {ar:وَلَا طَعَامٌ إِلَّا مِنْ غِسْلِينٍۢ, tr:ve lâ taâmun illâ min ğıslîn, gloss:irinden başka bir yemeği de yoktur, source:69:36}. Bu ayetle aynı kalıptır: olumsuzluk, "onun", yemek, istisna ve "-den". Orada sebep de söylenmiştir. Dünyada yoksulun yemeğini önemsemeyen, orada kendi yemeğini bulamaz. Gâşiye'den hemen sonra gelen surede de aynı kınama yapılır: {ar:كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ, tr:kellâ bel lâ tukrimûne'l-yetîm, gloss:hayır, siz yetime ikram etmiyorsunuz, source:89:17}; {ar:وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ tehâddûne alâ taâmi'l-miskîn, gloss:yoksulu doyurmaya birbirinizi teşvik etmiyorsunuz, source:89:18}. Cehennemin kızgın ateşine girenlere ne sebeple oraya düştükleri sorulduğunda da cevaplarından biri budur: {ar:وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ, tr:ve lem neku nut'imu'l-miskîn, gloss:yoksulu doyurmuyorduk, source:74:44}.

[¶17] Kur'an karşı resmi de çizer. Bahçeye kavuşanlar için şöyle denir: {ar:وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا وَأَسِيرًا, tr:ve yut'imûne't-taâme alâ hubbihî miskînen ve yetîmen ve esîrâ, gloss:kendileri sevdikleri halde yemeği yoksula, yetime ve esire yedirirler, source:76:8}. Doyurdukları kişilere de şunu söylerler: {ar:إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ, tr:innemâ nut'imukum li-vechillâh, gloss:sizi yalnızca Allah'ın yüzü için doyuruyoruz, source:76:9}. Gâşiye'nin iki yüz grubu, ikinci ayetteki eğik yüzler ve sekizinci ayetteki {ar:نَّاعِمَةٌۭ, tr:nâime, gloss:yumuşak ve mutlu, source:88:8} yüzler, bu sözün yanında başka bir anlam kazanır. Yemeğini Allah'ın yüzü için veren, o gün yüzünü taze bulur. Kur'an doyurmanın asıl sahibini de söyler: {ar:وَهُوَ يُطْعِمُ وَلَا يُطْعَمُ, tr:ve huve yut'imu ve lâ yut'am, gloss:O doyurur, kendisi doyurulmaz, source:6:14}. Kureyş'e de {ar:ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ, tr:ellezî at'amehum min cû', gloss:onları açlıktan doyuran, source:106:4} diye hatırlatılır. Oradaki "açlıktan" sözü yedinci ayettekiyle aynıdır. Dünyada açlıktan doyurulan ama doyurulmayı başkasına geçirmeyen bir el, burada açlıktan kurtarmayan bir yemekle karşılaşır. Darî'in kökündeki "malını açıp sunmak" anlamı ayetteki otun anlamına girmez. Ama malını kimseye açmamış insanların önüne, adında bu anlam da bulunan bir ot konması, ayetin yanında duyulan bir yankıdır.

## Yemeğe benzeyen

[¶18] Darî'in kökü bir de benzerliği adlandırır: {ar:المضارعة هي التشابه بين الشيئين, tr:el-mudâraatü hiye't-teşâbühü beyne'ş-şey'eyn, gloss:mudâraa iki şeyin birbirine benzemesidir, source:"ض ر ع,B004"}; {ar:هذا ضرع هذا وصرعه أي مثله, tr:hâzâ dar'u hâzâ ve sar'uhû ey misluh, gloss:bu onun dengidir, benzeridir, source:"ض ر ع,B004"}. Arap dilcileri şimdiki ve gelecek zaman fiiline de bu yüzden muzâri' dediler: {ar:الفعل المستقبل مضارع لمشاكلته الأسماء, tr:el-fi'lü'l-müstakbel mudâriun li-müşâkeletihi'l-esmâ', gloss:gelecek zaman fiili adlara benzediği için muzâri' denir, source:"ض ر ع,B004"}. Türk dilbilgisindeki "muzari" adı da buradan gelir.

[¶19] Ayetin kuruluşu bu anlamı yan anlam olarak çağırır. İstisna darî'i yemeklerin arasına koyar: "yemek yoktur, şu hariç." Yedinci ayet ise ondan yemeğin iki işini de geri alır. Geriye, yemeğin yerinde duran ve ona benzeyen ama yemek olmayan bir şey kalır. Kur'an aynı boşluğu bir gölge için de kurar. Yalanlayanlara yalanladıkları şeye gitmeleri söylendiğinde şöyle denir: {ar:ٱنطَلِقُوٓا۟ إِلَىٰ ظِلٍّۢ ذِى ثَلَٰثِ شُعَبٍۢ, tr:intalikû ilâ zıllin zî selâsi şuab, gloss:üç kollu bir gölgeye gidin, source:77:30}; {ar:لَّا ظَلِيلٍۢ وَلَا يُغْنِى مِنَ ٱللَّهَبِ, tr:lâ zalîlin ve lâ yuğnî mine'l-leheb, gloss:ne gölgelendirir ne de alevden korur, source:77:31}. Oradaki "korumaz" fiili, yedinci ayetteki "gidermez" fiilinin aynısıdır. Gölgenin adı vardır ama gölgenin işi yoktur. Darî'in de yemek yerinde bir yeri vardır ama yemeğin işi yoktur.

[¶20] Bahçede benzerlik tam tersine çalışır. Kur'an bahçe ehlinin meyveleri için şöyle der: {ar:قَالُوا۟ هَٰذَا ٱلَّذِى رُزِقْنَا مِن قَبْلُ ۖ وَأُتُوا۟ بِهِۦ مُتَشَٰبِهًۭا, tr:kâlû hâzellezî ruziknâ min kabl ve ütû bihî müteşâbihâ, gloss:bu daha önce bize verilen rızıktır derler; o onlara birbirine benzer olarak getirilir, source:2:25}. Buradaki benzerlik kelimesi başka bir köktendir. Bu yüzden bağ bir kök bağı değil, bir karşıtlıktır. Orada benzerlik tanıdık bir lezzeti daha dolgun olarak geri getirir. Burada ise yemeğe benzeyen şey, yemeğin bütün işlerinden boşalmıştır.

===== _commentary/v16/out/88_6/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: "min" in illā min ḍarīʿ read as "out of / from" ḍarīʿ
- memory: shibriq is a thorny plant
- memory: muḍāriʿ is the source of the Turkish grammar term "muzari"
- not written: ل ي س B004–B008 (alyas: brave, immovable man, camels staying at the trough, load-bearing camel, weak judgement, dayyūth) - a negation particle here; these images do not bear on it
- not written: ط ع م B003 asking for speech / prompting the imam - no tie to the ayah's theme
- not written: ط ع م B006, B009, B010, B011, B013, B014 (hunting bow, horse's muzzle, graft taking, power, kissing, continuous build) - no support in the ayah or surah
- not written: ط ع م B012 throat grip (maṭʿama) with 73:13 choking food - 88 says nothing of throat or swallowing
- not written: ض ر ع B010 horse overpowering rider, B013 rope strands - no theme in the ayah

===== passages not cited (192) =====
## strong (this ayah's own list) (14)

- (6:42) [listed for 88:6] [cited in ¶13] وَلَقَدْ أَرْسَلْنَآ إِلَىٰٓ أُمَمٍۢ مِّن قَبْلِكَ فَأَخَذْنَٰهُم بِٱلْبَأْسَآءِ وَٱلضَّرَّآءِ لَعَلَّهُمْ يَتَضَرَّعُونَ
- (6:43) [listed for 88:6] [cited in ¶13] فَلَوْلَآ إِذْ جَآءَهُم بَأْسُنَا تَضَرَّعُوا۟ وَلَٰكِن قَسَتْ قُلُوبُهُمْ وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ مَا كَانُوا۟ يَعْمَلُونَ
- (14:16) [listed for 88:6] مِّن وَرَآئِهِۦ جَهَنَّمُ وَيُسْقَىٰ مِن مَّآءٍۢ صَدِيدٍۢ
- (20:118) [listed for 88:6] إِنَّ لَكَ أَلَّا تَجُوعَ فِيهَا وَلَا تَعْرَىٰ
- (37:66) [listed for 88:6] [cited in ¶6] فَإِنَّهُمْ لَءَاكِلُونَ مِنْهَا فَمَالِـُٔونَ مِنْهَا ٱلْبُطُونَ
- (44:44) [listed for 88:6] [cited in ¶6] طَعَامُ ٱلْأَثِيمِ
- (44:45) [listed for 88:6] كَٱلْمُهْلِ يَغْلِى فِى ٱلْبُطُونِ
- (44:46) [listed for 88:6] كَغَلْىِ ٱلْحَمِيمِ
- (56:53) [listed for 88:6] فَمَالِـُٔونَ مِنْهَا ٱلْبُطُونَ
- (56:54) [listed for 88:6] فَشَٰرِبُونَ عَلَيْهِ مِنَ ٱلْحَمِيمِ
- (56:55) [listed for 88:6] فَشَٰرِبُونَ شُرْبَ ٱلْهِيمِ
- (69:36) [listed for 88:6] [cited in ¶16] وَلَا طَعَامٌ إِلَّا مِنْ غِسْلِينٍۢ
- (78:24) [listed for 88:6] [cited in ¶3] لَّا يَذُوقُونَ فِيهَا بَرْدًۭا وَلَا شَرَابًا
- (78:25) [listed for 88:6] [cited in ¶3] إِلَّا حَمِيمًۭا وَغَسَّاقًۭا

## medium (this ayah's own list) (57)

- (5:75) [listed for 88:6] مَّا ٱلْمَسِيحُ ٱبْنُ مَرْيَمَ إِلَّا رَسُولٌۭ قَدْ خَلَتْ مِن قَبْلِهِ ٱلرُّسُلُ وَأُمُّهُۥ صِدِّيقَةٌۭ ۖ كَانَا يَأْكُلَانِ ٱلطَّعَامَ ۗ ٱنظُرْ كَيْفَ نُبَيِّنُ لَهُمُ ٱلْءَايَٰتِ ثُمَّ ٱنظُرْ أَنَّىٰ يُؤْفَكُونَ
- (5:89) [listed for 88:6] لَا يُؤَاخِذُكُمُ ٱللَّهُ بِٱللَّغْوِ فِىٓ أَيْمَٰنِكُمْ وَلَٰكِن يُؤَاخِذُكُم بِمَا عَقَّدتُّمُ ٱلْأَيْمَٰنَ ۖ فَكَفَّٰرَتُهُۥٓ إِطْعَامُ عَشَرَةِ مَسَٰكِينَ مِنْ أَوْسَطِ مَا تُطْعِمُونَ أَهْلِيكُمْ أَوْ كِسْوَتُهُمْ أَوْ تَحْرِيرُ رَقَبَةٍۢ ۖ فَمَن لَّمْ يَجِدْ فَصِيَامُ ثَلَٰثَةِ أَيَّامٍۢ ۚ ذَٰلِكَ كَفَّٰرَةُ أَيْمَٰنِكُمْ إِذَا حَلَفْتُمْ ۚ وَٱحْفَظُوٓا۟ أَيْمَٰنَكُمْ ۚ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمْ ءَايَٰتِهِۦ لَعَلَّكُمْ تَشْكُرُونَ
- (6:63) [listed for 88:6] قُلْ مَن يُنَجِّيكُم مِّن ظُلُمَٰتِ ٱلْبَرِّ وَٱلْبَحْرِ تَدْعُونَهُۥ تَضَرُّعًۭا وَخُفْيَةًۭ لَّئِنْ أَنجَىٰنَا مِنْ هَٰذِهِۦ لَنَكُونَنَّ مِنَ ٱلشَّٰكِرِينَ
- (6:138) [listed for 88:6] وَقَالُوا۟ هَٰذِهِۦٓ أَنْعَٰمٌۭ وَحَرْثٌ حِجْرٌۭ لَّا يَطْعَمُهَآ إِلَّا مَن نَّشَآءُ بِزَعْمِهِمْ وَأَنْعَٰمٌ حُرِّمَتْ ظُهُورُهَا وَأَنْعَٰمٌۭ لَّا يَذْكُرُونَ ٱسْمَ ٱللَّهِ عَلَيْهَا ٱفْتِرَآءً عَلَيْهِ ۚ سَيَجْزِيهِم بِمَا كَانُوا۟ يَفْتَرُونَ
- (6:145) [listed for 88:6] قُل لَّآ أَجِدُ فِى مَآ أُوحِىَ إِلَىَّ مُحَرَّمًا عَلَىٰ طَاعِمٍۢ يَطْعَمُهُۥٓ إِلَّآ أَن يَكُونَ مَيْتَةً أَوْ دَمًۭا مَّسْفُوحًا أَوْ لَحْمَ خِنزِيرٍۢ فَإِنَّهُۥ رِجْسٌ أَوْ فِسْقًا أُهِلَّ لِغَيْرِ ٱللَّهِ بِهِۦ ۚ فَمَنِ ٱضْطُرَّ غَيْرَ بَاغٍۢ وَلَا عَادٍۢ فَإِنَّ رَبَّكَ غَفُورٌۭ رَّحِيمٌۭ
- (7:55) [listed for 88:6] [cited in ¶13] ٱدْعُوا۟ رَبَّكُمْ تَضَرُّعًۭا وَخُفْيَةً ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُعْتَدِينَ
- (7:94) [listed for 88:6] وَمَآ أَرْسَلْنَا فِى قَرْيَةٍۢ مِّن نَّبِىٍّ إِلَّآ أَخَذْنَآ أَهْلَهَا بِٱلْبَأْسَآءِ وَٱلضَّرَّآءِ لَعَلَّهُمْ يَضَّرَّعُونَ
- (7:205) [listed for 88:6] وَٱذْكُر رَّبَّكَ فِى نَفْسِكَ تَضَرُّعًۭا وَخِيفَةًۭ وَدُونَ ٱلْجَهْرِ مِنَ ٱلْقَوْلِ بِٱلْغُدُوِّ وَٱلْءَاصَالِ وَلَا تَكُن مِّنَ ٱلْغَٰفِلِينَ
- (10:4) [listed for 88:6] إِلَيْهِ مَرْجِعُكُمْ جَمِيعًۭا ۖ وَعْدَ ٱللَّهِ حَقًّا ۚ إِنَّهُۥ يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ لِيَجْزِىَ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ بِٱلْقِسْطِ ۚ وَٱلَّذِينَ كَفَرُوا۟ لَهُمْ شَرَابٌۭ مِّنْ حَمِيمٍۢ وَعَذَابٌ أَلِيمٌۢ بِمَا كَانُوا۟ يَكْفُرُونَ
- (16:66) [listed for 88:6] وَإِنَّ لَكُمْ فِى ٱلْأَنْعَٰمِ لَعِبْرَةًۭ ۖ نُّسْقِيكُم مِّمَّا فِى بُطُونِهِۦ مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ
- (18:29) [listed for 88:6] وَقُلِ ٱلْحَقُّ مِن رَّبِّكُمْ ۖ فَمَن شَآءَ فَلْيُؤْمِن وَمَن شَآءَ فَلْيَكْفُرْ ۚ إِنَّآ أَعْتَدْنَا لِلظَّٰلِمِينَ نَارًا أَحَاطَ بِهِمْ سُرَادِقُهَا ۚ وَإِن يَسْتَغِيثُوا۟ يُغَاثُوا۟ بِمَآءٍۢ كَٱلْمُهْلِ يَشْوِى ٱلْوُجُوهَ ۚ بِئْسَ ٱلشَّرَابُ وَسَآءَتْ مُرْتَفَقًا
- (20:119) [listed for 88:6] وَأَنَّكَ لَا تَظْمَؤُا۟ فِيهَا وَلَا تَضْحَىٰ
- (22:19) [listed for 88:6] ۞ هَٰذَانِ خَصْمَانِ ٱخْتَصَمُوا۟ فِى رَبِّهِمْ ۖ فَٱلَّذِينَ كَفَرُوا۟ قُطِّعَتْ لَهُمْ ثِيَابٌۭ مِّن نَّارٍۢ يُصَبُّ مِن فَوْقِ رُءُوسِهِمُ ٱلْحَمِيمُ
- (22:20) [listed for 88:6] يُصْهَرُ بِهِۦ مَا فِى بُطُونِهِمْ وَٱلْجُلُودُ
- (22:28) [listed for 88:6] لِّيَشْهَدُوا۟ مَنَٰفِعَ لَهُمْ وَيَذْكُرُوا۟ ٱسْمَ ٱللَّهِ فِىٓ أَيَّامٍۢ مَّعْلُومَٰتٍ عَلَىٰ مَا رَزَقَهُم مِّنۢ بَهِيمَةِ ٱلْأَنْعَٰمِ ۖ فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْبَآئِسَ ٱلْفَقِيرَ
- (22:36) [listed for 88:6] وَٱلْبُدْنَ جَعَلْنَٰهَا لَكُم مِّن شَعَٰٓئِرِ ٱللَّهِ لَكُمْ فِيهَا خَيْرٌۭ ۖ فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ ۖ فَإِذَا وَجَبَتْ جُنُوبُهَا فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْقَانِعَ وَٱلْمُعْتَرَّ ۚ كَذَٰلِكَ سَخَّرْنَٰهَا لَكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (23:19) [listed for 88:6] فَأَنشَأْنَا لَكُم بِهِۦ جَنَّٰتٍۢ مِّن نَّخِيلٍۢ وَأَعْنَٰبٍۢ لَّكُمْ فِيهَا فَوَٰكِهُ كَثِيرَةٌۭ وَمِنْهَا تَأْكُلُونَ
- (23:21) [listed for 88:6] وَإِنَّ لَكُمْ فِى ٱلْأَنْعَٰمِ لَعِبْرَةًۭ ۖ نُّسْقِيكُم مِّمَّا فِى بُطُونِهَا وَلَكُمْ فِيهَا مَنَٰفِعُ كَثِيرَةٌۭ وَمِنْهَا تَأْكُلُونَ
- (23:76) [listed for 88:6] [cited in ¶13] وَلَقَدْ أَخَذْنَٰهُم بِٱلْعَذَابِ فَمَا ٱسْتَكَانُوا۟ لِرَبِّهِمْ وَمَا يَتَضَرَّعُونَ
- (26:79) [listed for 88:6] وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ
- (36:33) [listed for 88:6] وَءَايَةٌۭ لَّهُمُ ٱلْأَرْضُ ٱلْمَيْتَةُ أَحْيَيْنَٰهَا وَأَخْرَجْنَا مِنْهَا حَبًّۭا فَمِنْهُ يَأْكُلُونَ
- (36:34) [listed for 88:6] وَجَعَلْنَا فِيهَا جَنَّٰتٍۢ مِّن نَّخِيلٍۢ وَأَعْنَٰبٍۢ وَفَجَّرْنَا فِيهَا مِنَ ٱلْعُيُونِ
- (36:35) [listed for 88:6] لِيَأْكُلُوا۟ مِن ثَمَرِهِۦ وَمَا عَمِلَتْهُ أَيْدِيهِمْ ۖ أَفَلَا يَشْكُرُونَ
- (37:62) [listed for 88:6] [cited in ¶6] أَذَٰلِكَ خَيْرٌۭ نُّزُلًا أَمْ شَجَرَةُ ٱلزَّقُّومِ
- (37:63) [listed for 88:6] إِنَّا جَعَلْنَٰهَا فِتْنَةًۭ لِّلظَّٰلِمِينَ
- (37:64) [listed for 88:6] [cited in ¶6] إِنَّهَا شَجَرَةٌۭ تَخْرُجُ فِىٓ أَصْلِ ٱلْجَحِيمِ
- (37:65) [listed for 88:6] طَلْعُهَا كَأَنَّهُۥ رُءُوسُ ٱلشَّيَٰطِينِ
- (37:67) [listed for 88:6] ثُمَّ إِنَّ لَهُمْ عَلَيْهَا لَشَوْبًۭا مِّنْ حَمِيمٍۢ
- (37:68) [listed for 88:6] ثُمَّ إِنَّ مَرْجِعَهُمْ لَإِلَى ٱلْجَحِيمِ
- (40:71) [listed for 88:6] إِذِ ٱلْأَغْلَٰلُ فِىٓ أَعْنَٰقِهِمْ وَٱلسَّلَٰسِلُ يُسْحَبُونَ
- (40:72) [listed for 88:6] فِى ٱلْحَمِيمِ ثُمَّ فِى ٱلنَّارِ يُسْجَرُونَ
- (44:43) [listed for 88:6] [cited in ¶6] إِنَّ شَجَرَتَ ٱلزَّقُّومِ
- (44:47) [listed for 88:6] خُذُوهُ فَٱعْتِلُوهُ إِلَىٰ سَوَآءِ ٱلْجَحِيمِ
- (44:48) [listed for 88:6] ثُمَّ صُبُّوا۟ فَوْقَ رَأْسِهِۦ مِنْ عَذَابِ ٱلْحَمِيمِ
- (47:15) [listed for 88:6] مَّثَلُ ٱلْجَنَّةِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۖ فِيهَآ أَنْهَٰرٌۭ مِّن مَّآءٍ غَيْرِ ءَاسِنٍۢ وَأَنْهَٰرٌۭ مِّن لَّبَنٍۢ لَّمْ يَتَغَيَّرْ طَعْمُهُۥ وَأَنْهَٰرٌۭ مِّنْ خَمْرٍۢ لَّذَّةٍۢ لِّلشَّٰرِبِينَ وَأَنْهَٰرٌۭ مِّنْ عَسَلٍۢ مُّصَفًّۭى ۖ وَلَهُمْ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَمَغْفِرَةٌۭ مِّن رَّبِّهِمْ ۖ كَمَنْ هُوَ خَٰلِدٌۭ فِى ٱلنَّارِ وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ
- (55:44) [listed for 88:6] يَطُوفُونَ بَيْنَهَا وَبَيْنَ حَمِيمٍ ءَانٍۢ
- (56:51) [listed for 88:6] ثُمَّ إِنَّكُمْ أَيُّهَا ٱلضَّآلُّونَ ٱلْمُكَذِّبُونَ
- (56:52) [listed for 88:6] لَءَاكِلُونَ مِن شَجَرٍۢ مِّن زَقُّومٍۢ
- (56:56) [listed for 88:6] هَٰذَا نُزُلُهُمْ يَوْمَ ٱلدِّينِ
- (56:93) [listed for 88:6] فَنُزُلٌۭ مِّنْ حَمِيمٍۢ
- (56:94) [listed for 88:6] وَتَصْلِيَةُ جَحِيمٍ
- (69:34) [listed for 88:6] [cited in ¶16] وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- (69:37) [listed for 88:6] لَّا يَأْكُلُهُۥٓ إِلَّا ٱلْخَٰطِـُٔونَ
- (74:44) [listed for 88:6] [cited in ¶16] وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ
- (76:8) [listed for 88:6] [cited in ¶17] وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا وَأَسِيرًا
- (80:24) [listed for 88:6] [cited in ¶5] فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ
- (80:25) [listed for 88:6] [cited in ¶5] أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا
- (80:26) [listed for 88:6] [cited in ¶5] ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا
- (80:27) [listed for 88:6] [cited in ¶5] فَأَنۢبَتْنَا فِيهَا حَبًّۭا
- (80:28) [listed for 88:6] وَعِنَبًۭا وَقَضْبًۭا
- (80:29) [listed for 88:6] وَزَيْتُونًۭا وَنَخْلًۭا
- (80:30) [listed for 88:6] وَحَدَآئِقَ غُلْبًۭا
- (80:31) [listed for 88:6] وَفَٰكِهَةًۭ وَأَبًّۭا
- (80:32) [listed for 88:6] [cited in ¶5] مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
- (89:18) [listed for 88:6] [cited in ¶16] وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- (106:4) [listed for 88:6] [cited in ¶17] ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ
- (107:3) [listed for 88:6] وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ

## named by the passage's own list as strong for this ayah (4)

- (14:17) [listed for 88:6] يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ وَيَأْتِيهِ ٱلْمَوْتُ مِن كُلِّ مَكَانٍۢ وَمَا هُوَ بِمَيِّتٍۢ ۖ وَمِن وَرَآئِهِۦ عَذَابٌ غَلِيظٌۭ
- (69:31) [listed for 88:6] ثُمَّ ٱلْجَحِيمَ صَلُّوهُ
- (73:13) [listed for 88:6] وَطَعَامًۭا ذَا غُصَّةٍۢ وَعَذَابًا أَلِيمًۭا
- (78:30) [listed for 88:6] فَذُوقُوا۟ فَلَن نَّزِيدَكُمْ إِلَّا عَذَابًا

## named by the passage's own list as medium for this ayah (11)

- (3:88) [listed for 88:6] خَٰلِدِينَ فِيهَا لَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنظَرُونَ
- (7:41) [listed for 88:6] لَهُم مِّن جَهَنَّمَ مِهَادٌۭ وَمِن فَوْقِهِمْ غَوَاشٍۢ ۚ وَكَذَٰلِكَ نَجْزِى ٱلظَّٰلِمِينَ
- (19:71) [listed for 88:6] وَإِن مِّنكُمْ إِلَّا وَارِدُهَا ۚ كَانَ عَلَىٰ رَبِّكَ حَتْمًۭا مَّقْضِيًّۭا
- (25:13) [listed for 88:6] وَإِذَآ أُلْقُوا۟ مِنْهَا مَكَانًۭا ضَيِّقًۭا مُّقَرَّنِينَ دَعَوْا۟ هُنَالِكَ ثُبُورًۭا
- (46:34) [listed for 88:6] وَيَوْمَ يُعْرَضُ ٱلَّذِينَ كَفَرُوا۟ عَلَى ٱلنَّارِ أَلَيْسَ هَٰذَا بِٱلْحَقِّ ۖ قَالُوا۟ بَلَىٰ وَرَبِّنَا ۚ قَالَ فَذُوقُوا۟ ٱلْعَذَابَ بِمَا كُنتُمْ تَكْفُرُونَ
- (70:15) [listed for 88:6] كَلَّآ ۖ إِنَّهَا لَظَىٰ
- (74:42) [listed for 88:6] مَا سَلَكَكُمْ فِى سَقَرَ
- (78:23) [listed for 88:6] لَّٰبِثِينَ فِيهَآ أَحْقَابًۭا
- (82:14) [listed for 88:6] وَإِنَّ ٱلْفُجَّارَ لَفِى جَحِيمٍۢ
- (84:12) [listed for 88:6] وَيَصْلَىٰ سَعِيرًا
- (90:14) [listed for 88:6] أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ

## weak (this ayah's own list) (43)

- (2:57) [listed for 88:6] وَظَلَّلْنَا عَلَيْكُمُ ٱلْغَمَامَ وَأَنزَلْنَا عَلَيْكُمُ ٱلْمَنَّ وَٱلسَّلْوَىٰ ۖ كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ ۖ وَمَا ظَلَمُونَا وَلَٰكِن كَانُوٓا۟ أَنفُسَهُمْ يَظْلِمُونَ
- (2:61) [listed for 88:6] وَإِذْ قُلْتُمْ يَٰمُوسَىٰ لَن نَّصْبِرَ عَلَىٰ طَعَامٍۢ وَٰحِدٍۢ فَٱدْعُ لَنَا رَبَّكَ يُخْرِجْ لَنَا مِمَّا تُنۢبِتُ ٱلْأَرْضُ مِنۢ بَقْلِهَا وَقِثَّآئِهَا وَفُومِهَا وَعَدَسِهَا وَبَصَلِهَا ۖ قَالَ أَتَسْتَبْدِلُونَ ٱلَّذِى هُوَ أَدْنَىٰ بِٱلَّذِى هُوَ خَيْرٌ ۚ ٱهْبِطُوا۟ مِصْرًۭا فَإِنَّ لَكُم مَّا سَأَلْتُمْ ۗ وَضُرِبَتْ عَلَيْهِمُ ٱلذِّلَّةُ وَٱلْمَسْكَنَةُ وَبَآءُو بِغَضَبٍۢ مِّنَ ٱللَّهِ ۗ ذَٰلِكَ بِأَنَّهُمْ كَانُوا۟ يَكْفُرُونَ بِـَٔايَٰتِ ٱللَّهِ وَيَقْتُلُونَ ٱلنَّبِيِّۦنَ بِغَيْرِ ٱلْحَقِّ ۗ ذَٰلِكَ بِمَا عَصَوا۟ وَّكَانُوا۟ يَعْتَدُونَ
- (2:184) [listed for 88:6] أَيَّامًۭا مَّعْدُودَٰتٍۢ ۚ فَمَن كَانَ مِنكُم مَّرِيضًا أَوْ عَلَىٰ سَفَرٍۢ فَعِدَّةٌۭ مِّنْ أَيَّامٍ أُخَرَ ۚ وَعَلَى ٱلَّذِينَ يُطِيقُونَهُۥ فِدْيَةٌۭ طَعَامُ مِسْكِينٍۢ ۖ فَمَن تَطَوَّعَ خَيْرًۭا فَهُوَ خَيْرٌۭ لَّهُۥ ۚ وَأَن تَصُومُوا۟ خَيْرٌۭ لَّكُمْ ۖ إِن كُنتُمْ تَعْلَمُونَ
- (2:249) [listed for 88:6] [cited in ¶3] فَلَمَّا فَصَلَ طَالُوتُ بِٱلْجُنُودِ قَالَ إِنَّ ٱللَّهَ مُبْتَلِيكُم بِنَهَرٍۢ فَمَن شَرِبَ مِنْهُ فَلَيْسَ مِنِّى وَمَن لَّمْ يَطْعَمْهُ فَإِنَّهُۥ مِنِّىٓ إِلَّا مَنِ ٱغْتَرَفَ غُرْفَةًۢ بِيَدِهِۦ ۚ فَشَرِبُوا۟ مِنْهُ إِلَّا قَلِيلًۭا مِّنْهُمْ ۚ فَلَمَّا جَاوَزَهُۥ هُوَ وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ قَالُوا۟ لَا طَاقَةَ لَنَا ٱلْيَوْمَ بِجَالُوتَ وَجُنُودِهِۦ ۚ قَالَ ٱلَّذِينَ يَظُنُّونَ أَنَّهُم مُّلَٰقُوا۟ ٱللَّهِ كَم مِّن فِئَةٍۢ قَلِيلَةٍ غَلَبَتْ فِئَةًۭ كَثِيرَةًۢ بِإِذْنِ ٱللَّهِ ۗ وَٱللَّهُ مَعَ ٱلصَّٰبِرِينَ
- (3:93) [listed for 88:6] ۞ كُلُّ ٱلطَّعَامِ كَانَ حِلًّۭا لِّبَنِىٓ إِسْرَٰٓءِيلَ إِلَّا مَا حَرَّمَ إِسْرَٰٓءِيلُ عَلَىٰ نَفْسِهِۦ مِن قَبْلِ أَن تُنَزَّلَ ٱلتَّوْرَىٰةُ ۗ قُلْ فَأْتُوا۟ بِٱلتَّوْرَىٰةِ فَٱتْلُوهَآ إِن كُنتُمْ صَٰدِقِينَ
- (4:18) [listed for 88:6] وَلَيْسَتِ ٱلتَّوْبَةُ لِلَّذِينَ يَعْمَلُونَ ٱلسَّيِّـَٔاتِ حَتَّىٰٓ إِذَا حَضَرَ أَحَدَهُمُ ٱلْمَوْتُ قَالَ إِنِّى تُبْتُ ٱلْـَٰٔنَ وَلَا ٱلَّذِينَ يَمُوتُونَ وَهُمْ كُفَّارٌ ۚ أُو۟لَٰٓئِكَ أَعْتَدْنَا لَهُمْ عَذَابًا أَلِيمًۭا
- (4:123) [listed for 88:6] لَّيْسَ بِأَمَانِيِّكُمْ وَلَآ أَمَانِىِّ أَهْلِ ٱلْكِتَٰبِ ۗ مَن يَعْمَلْ سُوٓءًۭا يُجْزَ بِهِۦ وَلَا يَجِدْ لَهُۥ مِن دُونِ ٱللَّهِ وَلِيًّۭا وَلَا نَصِيرًۭا
- (5:5) [listed for 88:6] ٱلْيَوْمَ أُحِلَّ لَكُمُ ٱلطَّيِّبَٰتُ ۖ وَطَعَامُ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ حِلٌّۭ لَّكُمْ وَطَعَامُكُمْ حِلٌّۭ لَّهُمْ ۖ وَٱلْمُحْصَنَٰتُ مِنَ ٱلْمُؤْمِنَٰتِ وَٱلْمُحْصَنَٰتُ مِنَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلِكُمْ إِذَآ ءَاتَيْتُمُوهُنَّ أُجُورَهُنَّ مُحْصِنِينَ غَيْرَ مُسَٰفِحِينَ وَلَا مُتَّخِذِىٓ أَخْدَانٍۢ ۗ وَمَن يَكْفُرْ بِٱلْإِيمَٰنِ فَقَدْ حَبِطَ عَمَلُهُۥ وَهُوَ فِى ٱلْءَاخِرَةِ مِنَ ٱلْخَٰسِرِينَ
- (5:68) [listed for 88:6] قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ لَسْتُمْ عَلَىٰ شَىْءٍ حَتَّىٰ تُقِيمُوا۟ ٱلتَّوْرَىٰةَ وَٱلْإِنجِيلَ وَمَآ أُنزِلَ إِلَيْكُم مِّن رَّبِّكُمْ ۗ وَلَيَزِيدَنَّ كَثِيرًۭا مِّنْهُم مَّآ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ طُغْيَٰنًۭا وَكُفْرًۭا ۖ فَلَا تَأْسَ عَلَى ٱلْقَوْمِ ٱلْكَٰفِرِينَ
- (5:95) [listed for 88:6] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَقْتُلُوا۟ ٱلصَّيْدَ وَأَنتُمْ حُرُمٌۭ ۚ وَمَن قَتَلَهُۥ مِنكُم مُّتَعَمِّدًۭا فَجَزَآءٌۭ مِّثْلُ مَا قَتَلَ مِنَ ٱلنَّعَمِ يَحْكُمُ بِهِۦ ذَوَا عَدْلٍۢ مِّنكُمْ هَدْيًۢا بَٰلِغَ ٱلْكَعْبَةِ أَوْ كَفَّٰرَةٌۭ طَعَامُ مَسَٰكِينَ أَوْ عَدْلُ ذَٰلِكَ صِيَامًۭا لِّيَذُوقَ وَبَالَ أَمْرِهِۦ ۗ عَفَا ٱللَّهُ عَمَّا سَلَفَ ۚ وَمَنْ عَادَ فَيَنتَقِمُ ٱللَّهُ مِنْهُ ۗ وَٱللَّهُ عَزِيزٌۭ ذُو ٱنتِقَامٍ
- (6:70) [listed for 88:6] وَذَرِ ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَعِبًۭا وَلَهْوًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ وَذَكِّرْ بِهِۦٓ أَن تُبْسَلَ نَفْسٌۢ بِمَا كَسَبَتْ لَيْسَ لَهَا مِن دُونِ ٱللَّهِ وَلِىٌّۭ وَلَا شَفِيعٌۭ وَإِن تَعْدِلْ كُلَّ عَدْلٍۢ لَّا يُؤْخَذْ مِنْهَآ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ أُبْسِلُوا۟ بِمَا كَسَبُوا۟ ۖ لَهُمْ شَرَابٌۭ مِّنْ حَمِيمٍۢ وَعَذَابٌ أَلِيمٌۢ بِمَا كَانُوا۟ يَكْفُرُونَ
- (6:99) [listed for 88:6] وَهُوَ ٱلَّذِىٓ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦ نَبَاتَ كُلِّ شَىْءٍۢ فَأَخْرَجْنَا مِنْهُ خَضِرًۭا نُّخْرِجُ مِنْهُ حَبًّۭا مُّتَرَاكِبًۭا وَمِنَ ٱلنَّخْلِ مِن طَلْعِهَا قِنْوَانٌۭ دَانِيَةٌۭ وَجَنَّٰتٍۢ مِّنْ أَعْنَابٍۢ وَٱلزَّيْتُونَ وَٱلرُّمَّانَ مُشْتَبِهًۭا وَغَيْرَ مُتَشَٰبِهٍ ۗ ٱنظُرُوٓا۟ إِلَىٰ ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَيَنْعِهِۦٓ ۚ إِنَّ فِى ذَٰلِكُمْ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
- (6:141) [listed for 88:6] ۞ وَهُوَ ٱلَّذِىٓ أَنشَأَ جَنَّٰتٍۢ مَّعْرُوشَٰتٍۢ وَغَيْرَ مَعْرُوشَٰتٍۢ وَٱلنَّخْلَ وَٱلزَّرْعَ مُخْتَلِفًا أُكُلُهُۥ وَٱلزَّيْتُونَ وَٱلرُّمَّانَ مُتَشَٰبِهًۭا وَغَيْرَ مُتَشَٰبِهٍۢ ۚ كُلُوا۟ مِن ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَءَاتُوا۟ حَقَّهُۥ يَوْمَ حَصَادِهِۦ ۖ وَلَا تُسْرِفُوٓا۟ ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُسْرِفِينَ
- (7:61) [listed for 88:6] قَالَ يَٰقَوْمِ لَيْسَ بِى ضَلَٰلَةٌۭ وَلَٰكِنِّى رَسُولٌۭ مِّن رَّبِّ ٱلْعَٰلَمِينَ
- (7:67) [listed for 88:6] قَالَ يَٰقَوْمِ لَيْسَ بِى سَفَاهَةٌۭ وَلَٰكِنِّى رَسُولٌۭ مِّن رَّبِّ ٱلْعَٰلَمِينَ
- (7:160) [listed for 88:6] وَقَطَّعْنَٰهُمُ ٱثْنَتَىْ عَشْرَةَ أَسْبَاطًا أُمَمًۭا ۚ وَأَوْحَيْنَآ إِلَىٰ مُوسَىٰٓ إِذِ ٱسْتَسْقَىٰهُ قَوْمُهُۥٓ أَنِ ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنۢبَجَسَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۚ وَظَلَّلْنَا عَلَيْهِمُ ٱلْغَمَٰمَ وَأَنزَلْنَا عَلَيْهِمُ ٱلْمَنَّ وَٱلسَّلْوَىٰ ۖ كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ ۚ وَمَا ظَلَمُونَا وَلَٰكِن كَانُوٓا۟ أَنفُسَهُمْ يَظْلِمُونَ
- (11:16) [listed for 88:6] أُو۟لَٰٓئِكَ ٱلَّذِينَ لَيْسَ لَهُمْ فِى ٱلْءَاخِرَةِ إِلَّا ٱلنَّارُ ۖ وَحَبِطَ مَا صَنَعُوا۟ فِيهَا وَبَٰطِلٌۭ مَّا كَانُوا۟ يَعْمَلُونَ
- (13:43) [listed for 88:6] وَيَقُولُ ٱلَّذِينَ كَفَرُوا۟ لَسْتَ مُرْسَلًۭا ۚ قُلْ كَفَىٰ بِٱللَّهِ شَهِيدًۢا بَيْنِى وَبَيْنَكُمْ وَمَنْ عِندَهُۥ عِلْمُ ٱلْكِتَٰبِ
- (15:42) [listed for 88:6] إِنَّ عِبَادِى لَيْسَ لَكَ عَلَيْهِمْ سُلْطَٰنٌ إِلَّا مَنِ ٱتَّبَعَكَ مِنَ ٱلْغَاوِينَ
- (16:10) [listed for 88:6] هُوَ ٱلَّذِىٓ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ ۖ لَّكُم مِّنْهُ شَرَابٌۭ وَمِنْهُ شَجَرٌۭ فِيهِ تُسِيمُونَ
- (16:11) [listed for 88:6] يُنۢبِتُ لَكُم بِهِ ٱلزَّرْعَ وَٱلزَّيْتُونَ وَٱلنَّخِيلَ وَٱلْأَعْنَٰبَ وَمِن كُلِّ ٱلثَّمَرَٰتِ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَتَفَكَّرُونَ
- (16:67) [listed for 88:6] وَمِن ثَمَرَٰتِ ٱلنَّخِيلِ وَٱلْأَعْنَٰبِ تَتَّخِذُونَ مِنْهُ سَكَرًۭا وَرِزْقًا حَسَنًا ۗ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَعْقِلُونَ
- (16:69) [listed for 88:6] ثُمَّ كُلِى مِن كُلِّ ٱلثَّمَرَٰتِ فَٱسْلُكِى سُبُلَ رَبِّكِ ذُلُلًۭا ۚ يَخْرُجُ مِنۢ بُطُونِهَا شَرَابٌۭ مُّخْتَلِفٌ أَلْوَٰنُهُۥ فِيهِ شِفَآءٌۭ لِّلنَّاسِ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَتَفَكَّرُونَ
- (16:112) [listed for 88:6] وَضَرَبَ ٱللَّهُ مَثَلًۭا قَرْيَةًۭ كَانَتْ ءَامِنَةًۭ مُّطْمَئِنَّةًۭ يَأْتِيهَا رِزْقُهَا رَغَدًۭا مِّن كُلِّ مَكَانٍۢ فَكَفَرَتْ بِأَنْعُمِ ٱللَّهِ فَأَذَٰقَهَا ٱللَّهُ لِبَاسَ ٱلْجُوعِ وَٱلْخَوْفِ بِمَا كَانُوا۟ يَصْنَعُونَ
- (18:19) [listed for 88:6] وَكَذَٰلِكَ بَعَثْنَٰهُمْ لِيَتَسَآءَلُوا۟ بَيْنَهُمْ ۚ قَالَ قَآئِلٌۭ مِّنْهُمْ كَمْ لَبِثْتُمْ ۖ قَالُوا۟ لَبِثْنَا يَوْمًا أَوْ بَعْضَ يَوْمٍۢ ۚ قَالُوا۟ رَبُّكُمْ أَعْلَمُ بِمَا لَبِثْتُمْ فَٱبْعَثُوٓا۟ أَحَدَكُم بِوَرِقِكُمْ هَٰذِهِۦٓ إِلَى ٱلْمَدِينَةِ فَلْيَنظُرْ أَيُّهَآ أَزْكَىٰ طَعَامًۭا فَلْيَأْتِكُم بِرِزْقٍۢ مِّنْهُ وَلْيَتَلَطَّفْ وَلَا يُشْعِرَنَّ بِكُمْ أَحَدًا
- (20:53) [listed for 88:6] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ مَهْدًۭا وَسَلَكَ لَكُمْ فِيهَا سُبُلًۭا وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ
- (20:54) [listed for 88:6] كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ
- (20:81) [listed for 88:6] كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ وَلَا تَطْغَوْا۟ فِيهِ فَيَحِلَّ عَلَيْكُمْ غَضَبِى ۖ وَمَن يَحْلِلْ عَلَيْهِ غَضَبِى فَقَدْ هَوَىٰ
- (21:8) [listed for 88:6] وَمَا جَعَلْنَٰهُمْ جَسَدًۭا لَّا يَأْكُلُونَ ٱلطَّعَامَ وَمَا كَانُوا۟ خَٰلِدِينَ
- (23:51) [listed for 88:6] يَٰٓأَيُّهَا ٱلرُّسُلُ كُلُوا۟ مِنَ ٱلطَّيِّبَٰتِ وَٱعْمَلُوا۟ صَٰلِحًا ۖ إِنِّى بِمَا تَعْمَلُونَ عَلِيمٌۭ
- (32:27) [listed for 88:6] أَوَلَمْ يَرَوْا۟ أَنَّا نَسُوقُ ٱلْمَآءَ إِلَى ٱلْأَرْضِ ٱلْجُرُزِ فَنُخْرِجُ بِهِۦ زَرْعًۭا تَأْكُلُ مِنْهُ أَنْعَٰمُهُمْ وَأَنفُسُهُمْ ۖ أَفَلَا يُبْصِرُونَ
- (33:53) [listed for 88:6] [cited in ¶11] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَدْخُلُوا۟ بُيُوتَ ٱلنَّبِىِّ إِلَّآ أَن يُؤْذَنَ لَكُمْ إِلَىٰ طَعَامٍ غَيْرَ نَٰظِرِينَ إِنَىٰهُ وَلَٰكِنْ إِذَا دُعِيتُمْ فَٱدْخُلُوا۟ فَإِذَا طَعِمْتُمْ فَٱنتَشِرُوا۟ وَلَا مُسْتَـْٔنِسِينَ لِحَدِيثٍ ۚ إِنَّ ذَٰلِكُمْ كَانَ يُؤْذِى ٱلنَّبِىَّ فَيَسْتَحْىِۦ مِنكُمْ ۖ وَٱللَّهُ لَا يَسْتَحْىِۦ مِنَ ٱلْحَقِّ ۚ وَإِذَا سَأَلْتُمُوهُنَّ مَتَٰعًۭا فَسْـَٔلُوهُنَّ مِن وَرَآءِ حِجَابٍۢ ۚ ذَٰلِكُمْ أَطْهَرُ لِقُلُوبِكُمْ وَقُلُوبِهِنَّ ۚ وَمَا كَانَ لَكُمْ أَن تُؤْذُوا۟ رَسُولَ ٱللَّهِ وَلَآ أَن تَنكِحُوٓا۟ أَزْوَٰجَهُۥ مِنۢ بَعْدِهِۦٓ أَبَدًا ۚ إِنَّ ذَٰلِكُمْ كَانَ عِندَ ٱللَّهِ عَظِيمًا
- (36:47) [listed for 88:6] وَإِذَا قِيلَ لَهُمْ أَنفِقُوا۟ مِمَّا رَزَقَكُمُ ٱللَّهُ قَالَ ٱلَّذِينَ كَفَرُوا۟ لِلَّذِينَ ءَامَنُوٓا۟ أَنُطْعِمُ مَن لَّوْ يَشَآءُ ٱللَّهُ أَطْعَمَهُۥٓ إِنْ أَنتُمْ إِلَّا فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (42:11) [listed for 88:6] فَاطِرُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ جَعَلَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَٰجًۭا وَمِنَ ٱلْأَنْعَٰمِ أَزْوَٰجًۭا ۖ يَذْرَؤُكُمْ فِيهِ ۚ لَيْسَ كَمِثْلِهِۦ شَىْءٌۭ ۖ وَهُوَ ٱلسَّمِيعُ ٱلْبَصِيرُ
- (46:32) [listed for 88:6] وَمَن لَّا يُجِبْ دَاعِىَ ٱللَّهِ فَلَيْسَ بِمُعْجِزٍۢ فِى ٱلْأَرْضِ وَلَيْسَ لَهُۥ مِن دُونِهِۦٓ أَوْلِيَآءُ ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۢ مُّبِينٍ
- (48:17) [listed for 88:6] لَّيْسَ عَلَى ٱلْأَعْمَىٰ حَرَجٌۭ وَلَا عَلَى ٱلْأَعْرَجِ حَرَجٌۭ وَلَا عَلَى ٱلْمَرِيضِ حَرَجٌۭ ۗ وَمَن يُطِعِ ٱللَّهَ وَرَسُولَهُۥ يُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۖ وَمَن يَتَوَلَّ يُعَذِّبْهُ عَذَابًا أَلِيمًۭا
- (51:57) [listed for 88:6] مَآ أُرِيدُ مِنْهُم مِّن رِّزْقٍۢ وَمَآ أُرِيدُ أَن يُطْعِمُونِ
- (53:39) [listed for 88:6] وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ
- (53:58) [listed for 88:6] لَيْسَ لَهَا مِن دُونِ ٱللَّهِ كَاشِفَةٌ
- (56:92) [listed for 88:6] وَأَمَّآ إِن كَانَ مِنَ ٱلْمُكَذِّبِينَ ٱلضَّآلِّينَ
- (65:11) [listed for 88:6] رَّسُولًۭا يَتْلُوا۟ عَلَيْكُمْ ءَايَٰتِ ٱللَّهِ مُبَيِّنَٰتٍۢ لِّيُخْرِجَ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۚ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ قَدْ أَحْسَنَ ٱللَّهُ لَهُۥ رِزْقًا
- (83:22) [listed for 88:6] إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍ
- (89:19) [listed for 88:6] وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا

## named by the passage's own list as weak for this ayah (6)

- (3:173) [listed for 88:6] ٱلَّذِينَ قَالَ لَهُمُ ٱلنَّاسُ إِنَّ ٱلنَّاسَ قَدْ جَمَعُوا۟ لَكُمْ فَٱخْشَوْهُمْ فَزَادَهُمْ إِيمَٰنًۭا وَقَالُوا۟ حَسْبُنَا ٱللَّهُ وَنِعْمَ ٱلْوَكِيلُ
- (5:93) [listed for 88:6] لَيْسَ عَلَى ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ جُنَاحٌۭ فِيمَا طَعِمُوٓا۟ إِذَا مَا ٱتَّقَوا۟ وَّءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ ثُمَّ ٱتَّقَوا۟ وَّءَامَنُوا۟ ثُمَّ ٱتَّقَوا۟ وَّأَحْسَنُوا۟ ۗ وَٱللَّهُ يُحِبُّ ٱلْمُحْسِنِينَ
- (12:37) [listed for 88:6] قَالَ لَا يَأْتِيكُمَا طَعَامٌۭ تُرْزَقَانِهِۦٓ إِلَّا نَبَّأْتُكُمَا بِتَأْوِيلِهِۦ قَبْلَ أَن يَأْتِيَكُمَا ۚ ذَٰلِكُمَا مِمَّا عَلَّمَنِى رَبِّىٓ ۚ إِنِّى تَرَكْتُ مِلَّةَ قَوْمٍۢ لَّا يُؤْمِنُونَ بِٱللَّهِ وَهُم بِٱلْءَاخِرَةِ هُمْ كَٰفِرُونَ
- (56:2) [listed for 88:6] لَيْسَ لِوَقْعَتِهَا كَاذِبَةٌ
- (56:71) [listed for 88:6] أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ
- (111:3) [listed for 88:6] سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ

## neighbours: within two ayat of a passage the commentary cites (57)

- (2:23) [next to 2:25] وَإِن كُنتُمْ فِى رَيْبٍۢ مِّمَّا نَزَّلْنَا عَلَىٰ عَبْدِنَا فَأْتُوا۟ بِسُورَةٍۢ مِّن مِّثْلِهِۦ وَٱدْعُوا۟ شُهَدَآءَكُم مِّن دُونِ ٱللَّهِ إِن كُنتُمْ صَٰدِقِينَ
- (2:24) [next to 2:25] فَإِن لَّمْ تَفْعَلُوا۟ وَلَن تَفْعَلُوا۟ فَٱتَّقُوا۟ ٱلنَّارَ ٱلَّتِى وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ ۖ أُعِدَّتْ لِلْكَٰفِرِينَ
- (2:26) [next to 2:25] ۞ إِنَّ ٱللَّهَ لَا يَسْتَحْىِۦٓ أَن يَضْرِبَ مَثَلًۭا مَّا بَعُوضَةًۭ فَمَا فَوْقَهَا ۚ فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ فَيَعْلَمُونَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّهِمْ ۖ وَأَمَّا ٱلَّذِينَ كَفَرُوا۟ فَيَقُولُونَ مَاذَآ أَرَادَ ٱللَّهُ بِهَٰذَا مَثَلًۭا ۘ يُضِلُّ بِهِۦ كَثِيرًۭا وَيَهْدِى بِهِۦ كَثِيرًۭا ۚ وَمَا يُضِلُّ بِهِۦٓ إِلَّا ٱلْفَٰسِقِينَ
- (2:27) [next to 2:25] ٱلَّذِينَ يَنقُضُونَ عَهْدَ ٱللَّهِ مِنۢ بَعْدِ مِيثَٰقِهِۦ وَيَقْطَعُونَ مَآ أَمَرَ ٱللَّهُ بِهِۦٓ أَن يُوصَلَ وَيُفْسِدُونَ فِى ٱلْأَرْضِ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (2:247) [next to 2:249] وَقَالَ لَهُمْ نَبِيُّهُمْ إِنَّ ٱللَّهَ قَدْ بَعَثَ لَكُمْ طَالُوتَ مَلِكًۭا ۚ قَالُوٓا۟ أَنَّىٰ يَكُونُ لَهُ ٱلْمُلْكُ عَلَيْنَا وَنَحْنُ أَحَقُّ بِٱلْمُلْكِ مِنْهُ وَلَمْ يُؤْتَ سَعَةًۭ مِّنَ ٱلْمَالِ ۚ قَالَ إِنَّ ٱللَّهَ ٱصْطَفَىٰهُ عَلَيْكُمْ وَزَادَهُۥ بَسْطَةًۭ فِى ٱلْعِلْمِ وَٱلْجِسْمِ ۖ وَٱللَّهُ يُؤْتِى مُلْكَهُۥ مَن يَشَآءُ ۚ وَٱللَّهُ وَٰسِعٌ عَلِيمٌۭ
- (2:248) [next to 2:249] وَقَالَ لَهُمْ نَبِيُّهُمْ إِنَّ ءَايَةَ مُلْكِهِۦٓ أَن يَأْتِيَكُمُ ٱلتَّابُوتُ فِيهِ سَكِينَةٌۭ مِّن رَّبِّكُمْ وَبَقِيَّةٌۭ مِّمَّا تَرَكَ ءَالُ مُوسَىٰ وَءَالُ هَٰرُونَ تَحْمِلُهُ ٱلْمَلَٰٓئِكَةُ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لَّكُمْ إِن كُنتُم مُّؤْمِنِينَ
- (2:250) [next to 2:249] وَلَمَّا بَرَزُوا۟ لِجَالُوتَ وَجُنُودِهِۦ قَالُوا۟ رَبَّنَآ أَفْرِغْ عَلَيْنَا صَبْرًۭا وَثَبِّتْ أَقْدَامَنَا وَٱنصُرْنَا عَلَى ٱلْقَوْمِ ٱلْكَٰفِرِينَ
- (2:251) [next to 2:249] فَهَزَمُوهُم بِإِذْنِ ٱللَّهِ وَقَتَلَ دَاوُۥدُ جَالُوتَ وَءَاتَىٰهُ ٱللَّهُ ٱلْمُلْكَ وَٱلْحِكْمَةَ وَعَلَّمَهُۥ مِمَّا يَشَآءُ ۗ وَلَوْلَا دَفْعُ ٱللَّهِ ٱلنَّاسَ بَعْضَهُم بِبَعْضٍۢ لَّفَسَدَتِ ٱلْأَرْضُ وَلَٰكِنَّ ٱللَّهَ ذُو فَضْلٍ عَلَى ٱلْعَٰلَمِينَ
- (6:12) [next to 6:14] قُل لِّمَن مَّا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ قُل لِّلَّهِ ۚ كَتَبَ عَلَىٰ نَفْسِهِ ٱلرَّحْمَةَ ۚ لَيَجْمَعَنَّكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ ۚ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ فَهُمْ لَا يُؤْمِنُونَ
- (6:13) [next to 6:14] ۞ وَلَهُۥ مَا سَكَنَ فِى ٱلَّيْلِ وَٱلنَّهَارِ ۚ وَهُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (6:15) [next to 6:14] قُلْ إِنِّىٓ أَخَافُ إِنْ عَصَيْتُ رَبِّى عَذَابَ يَوْمٍ عَظِيمٍۢ
- (6:16) [next to 6:14] مَّن يُصْرَفْ عَنْهُ يَوْمَئِذٍۢ فَقَدْ رَحِمَهُۥ ۚ وَذَٰلِكَ ٱلْفَوْزُ ٱلْمُبِينُ
- (6:40) [next to 6:42] قُلْ أَرَءَيْتَكُمْ إِنْ أَتَىٰكُمْ عَذَابُ ٱللَّهِ أَوْ أَتَتْكُمُ ٱلسَّاعَةُ أَغَيْرَ ٱللَّهِ تَدْعُونَ إِن كُنتُمْ صَٰدِقِينَ
- (6:41) [next to 6:42] بَلْ إِيَّاهُ تَدْعُونَ فَيَكْشِفُ مَا تَدْعُونَ إِلَيْهِ إِن شَآءَ وَتَنسَوْنَ مَا تُشْرِكُونَ
- (6:44) [next to 6:42] فَلَمَّا نَسُوا۟ مَا ذُكِّرُوا۟ بِهِۦ فَتَحْنَا عَلَيْهِمْ أَبْوَٰبَ كُلِّ شَىْءٍ حَتَّىٰٓ إِذَا فَرِحُوا۟ بِمَآ أُوتُوٓا۟ أَخَذْنَٰهُم بَغْتَةًۭ فَإِذَا هُم مُّبْلِسُونَ
- (6:45) [next to 6:43] فَقُطِعَ دَابِرُ ٱلْقَوْمِ ٱلَّذِينَ ظَلَمُوا۟ ۚ وَٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- (7:53) [next to 7:55] هَلْ يَنظُرُونَ إِلَّا تَأْوِيلَهُۥ ۚ يَوْمَ يَأْتِى تَأْوِيلُهُۥ يَقُولُ ٱلَّذِينَ نَسُوهُ مِن قَبْلُ قَدْ جَآءَتْ رُسُلُ رَبِّنَا بِٱلْحَقِّ فَهَل لَّنَا مِن شُفَعَآءَ فَيَشْفَعُوا۟ لَنَآ أَوْ نُرَدُّ فَنَعْمَلَ غَيْرَ ٱلَّذِى كُنَّا نَعْمَلُ ۚ قَدْ خَسِرُوٓا۟ أَنفُسَهُمْ وَضَلَّ عَنْهُم مَّا كَانُوا۟ يَفْتَرُونَ
- (7:54) [next to 7:55] إِنَّ رَبَّكُمُ ٱللَّهُ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ يُغْشِى ٱلَّيْلَ ٱلنَّهَارَ يَطْلُبُهُۥ حَثِيثًۭا وَٱلشَّمْسَ وَٱلْقَمَرَ وَٱلنُّجُومَ مُسَخَّرَٰتٍۭ بِأَمْرِهِۦٓ ۗ أَلَا لَهُ ٱلْخَلْقُ وَٱلْأَمْرُ ۗ تَبَارَكَ ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
- (7:56) [next to 7:55] وَلَا تُفْسِدُوا۟ فِى ٱلْأَرْضِ بَعْدَ إِصْلَٰحِهَا وَٱدْعُوهُ خَوْفًۭا وَطَمَعًا ۚ إِنَّ رَحْمَتَ ٱللَّهِ قَرِيبٌۭ مِّنَ ٱلْمُحْسِنِينَ
- (7:57) [next to 7:55] وَهُوَ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۖ حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًۭا ثِقَالًۭا سُقْنَٰهُ لِبَلَدٍۢ مَّيِّتٍۢ فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ
- (23:74) [next to 23:76] وَإِنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ عَنِ ٱلصِّرَٰطِ لَنَٰكِبُونَ
- (23:75) [next to 23:76] ۞ وَلَوْ رَحِمْنَٰهُمْ وَكَشَفْنَا مَا بِهِم مِّن ضُرٍّۢ لَّلَجُّوا۟ فِى طُغْيَٰنِهِمْ يَعْمَهُونَ
- (23:77) [next to 23:76] حَتَّىٰٓ إِذَا فَتَحْنَا عَلَيْهِم بَابًۭا ذَا عَذَابٍۢ شَدِيدٍ إِذَا هُمْ فِيهِ مُبْلِسُونَ
- (23:78) [next to 23:76] وَهُوَ ٱلَّذِىٓ أَنشَأَ لَكُمُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ ۚ قَلِيلًۭا مَّا تَشْكُرُونَ
- (33:51) [next to 33:53] ۞ تُرْجِى مَن تَشَآءُ مِنْهُنَّ وَتُـْٔوِىٓ إِلَيْكَ مَن تَشَآءُ ۖ وَمَنِ ٱبْتَغَيْتَ مِمَّنْ عَزَلْتَ فَلَا جُنَاحَ عَلَيْكَ ۚ ذَٰلِكَ أَدْنَىٰٓ أَن تَقَرَّ أَعْيُنُهُنَّ وَلَا يَحْزَنَّ وَيَرْضَيْنَ بِمَآ ءَاتَيْتَهُنَّ كُلُّهُنَّ ۚ وَٱللَّهُ يَعْلَمُ مَا فِى قُلُوبِكُمْ ۚ وَكَانَ ٱللَّهُ عَلِيمًا حَلِيمًۭا
- (33:52) [next to 33:53] لَّا يَحِلُّ لَكَ ٱلنِّسَآءُ مِنۢ بَعْدُ وَلَآ أَن تَبَدَّلَ بِهِنَّ مِنْ أَزْوَٰجٍۢ وَلَوْ أَعْجَبَكَ حُسْنُهُنَّ إِلَّا مَا مَلَكَتْ يَمِينُكَ ۗ وَكَانَ ٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ رَّقِيبًۭا
- (33:54) [next to 33:53] إِن تُبْدُوا۟ شَيْـًٔا أَوْ تُخْفُوهُ فَإِنَّ ٱللَّهَ كَانَ بِكُلِّ شَىْءٍ عَلِيمًۭا
- (33:55) [next to 33:53] لَّا جُنَاحَ عَلَيْهِنَّ فِىٓ ءَابَآئِهِنَّ وَلَآ أَبْنَآئِهِنَّ وَلَآ إِخْوَٰنِهِنَّ وَلَآ أَبْنَآءِ إِخْوَٰنِهِنَّ وَلَآ أَبْنَآءِ أَخَوَٰتِهِنَّ وَلَا نِسَآئِهِنَّ وَلَا مَا مَلَكَتْ أَيْمَٰنُهُنَّ ۗ وَٱتَّقِينَ ٱللَّهَ ۚ إِنَّ ٱللَّهَ كَانَ عَلَىٰ كُلِّ شَىْءٍۢ شَهِيدًا
- (37:60) [next to 37:62] إِنَّ هَٰذَا لَهُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (37:61) [next to 37:62] لِمِثْلِ هَٰذَا فَلْيَعْمَلِ ٱلْعَٰمِلُونَ
- (44:41) [next to 44:43] يَوْمَ لَا يُغْنِى مَوْلًى عَن مَّوْلًۭى شَيْـًۭٔا وَلَا هُمْ يُنصَرُونَ
- (44:42) [next to 44:43] إِلَّا مَن رَّحِمَ ٱللَّهُ ۚ إِنَّهُۥ هُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (69:32) [next to 69:33] ثُمَّ فِى سِلْسِلَةٍۢ ذَرْعُهَا سَبْعُونَ ذِرَاعًۭا فَٱسْلُكُوهُ
- (69:38) [next to 69:36] فَلَآ أُقْسِمُ بِمَا تُبْصِرُونَ
- (74:43) [next to 74:44] قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ
- (74:45) [next to 74:44] وَكُنَّا نَخُوضُ مَعَ ٱلْخَآئِضِينَ
- (74:46) [next to 74:44] وَكُنَّا نُكَذِّبُ بِيَوْمِ ٱلدِّينِ
- (76:6) [next to 76:8] عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا
- (76:7) [next to 76:8] يُوفُونَ بِٱلنَّذْرِ وَيَخَافُونَ يَوْمًۭا كَانَ شَرُّهُۥ مُسْتَطِيرًۭا
- (76:10) [next to 76:8] إِنَّا نَخَافُ مِن رَّبِّنَا يَوْمًا عَبُوسًۭا قَمْطَرِيرًۭا
- (76:11) [next to 76:9] فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا
- (77:28) [next to 77:30] وَيْلٌۭ يَوْمَئِذٍۢ لِّلْمُكَذِّبِينَ
- (77:29) [next to 77:30] ٱنطَلِقُوٓا۟ إِلَىٰ مَا كُنتُم بِهِۦ تُكَذِّبُونَ
- (77:32) [next to 77:30] إِنَّهَا تَرْمِى بِشَرَرٍۢ كَٱلْقَصْرِ
- (77:33) [next to 77:31] كَأَنَّهُۥ جِمَٰلَتٌۭ صُفْرٌۭ
- (78:22) [next to 78:24] لِّلطَّٰغِينَ مَـَٔابًۭا
- (78:26) [next to 78:24] جَزَآءًۭ وِفَاقًا
- (78:27) [next to 78:25] إِنَّهُمْ كَانُوا۟ لَا يَرْجُونَ حِسَابًۭا
- (80:22) [next to 80:24] ثُمَّ إِذَا شَآءَ أَنشَرَهُۥ
- (80:23) [next to 80:24] كَلَّا لَمَّا يَقْضِ مَآ أَمَرَهُۥ
- (80:33) [next to 80:32] فَإِذَا جَآءَتِ ٱلصَّآخَّةُ
- (80:34) [next to 80:32] يَوْمَ يَفِرُّ ٱلْمَرْءُ مِنْ أَخِيهِ
- (89:15) [next to 89:17] فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ
- (89:16) [next to 89:17] وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ
- (89:20) [next to 89:18] وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
- (106:2) [next to 106:4] إِۦلَٰفِهِمْ رِحْلَةَ ٱلشِّتَآءِ وَٱلصَّيْفِ
- (106:3) [next to 106:4] فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ

