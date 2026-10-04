Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 1:3; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/1_3/DM.r13.images.r13.map3.nohft.tool.tool.tool/1_3.reading.tr.md (prose paragraphs numbered) =====
## Bir cümlenin ortasında iki ad

[¶1] Üçüncü ayet yalnızca iki kelimedir ve kendi başına bir cümle kurmaz. Fiili de öznesi de yoktur. İki kelime ikinci ayetteki Allah adına bağlanır, onunla aynı hâlde okunur ve onu niteler. Cümle ikinci ayette başlar, üçüncüden geçer, dördüncüde tamamlanır: Hamd, âlemlerin Rabbi, Rahmân, Rahîm ve din gününün sahibi olan Allah'adır. Bu yüzden ayetin anlamı yanındaki ayetlerden ayrılamaz. Merhamet, bir cümlenin tam ortasında, Rab ile hükümdar arasında durur.

[¶2] Okuyan bu iki kelimeyi az önce duymuştur, çünkü birinci ayet de aynı ikiliyle biter: {ar:بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:bismillâhi'r-rahmâni'r-rahîm, gloss:Rahmân ve Rahîm olan Allah'ın adıyla, source:1:1}. Orada iki ad, okuyanın söze başlarken andığı adın parçasıdır. Burada ise hamdın içindedir ve övülenin neden övüldüğünü söyler. Yedi ayetlik bir surede aynı iki kelime iki kez geçer, ama aynı işi görmez. Birincide bir başlangıcın, ikincide bir övgünün parçasıdır.

[¶3] Yerleri de önemlidir. Önlerinde âlemlerin Rabbi, arkalarında bir günün sahibi vardır. Ardından beşinci ayette konuşan değişir ve kul doğrudan "yalnız sana" diye seslenir. Kul daha bir şey istemeden, seslendiği kişi iki kez merhametle anılmıştır. Merhamet istenmeden önce söylenir. Âlemler ile merhamet arasındaki bu yakınlığı Kur'an başka bir yerde tek cümlede kurar. Enbiyâ suresinde birçok peygamberin kıssası anlatıldıktan sonra Allah Peygambere şöyle der: {ar:وَمَآ أَرْسَلْنَٰكَ إِلَّا رَحْمَةًۭ لِّلْعَٰلَمِينَ, tr:ve mâ erselnâke illâ rahmeten li'l-âlemîn, gloss:seni ancak âlemlere bir rahmet olarak gönderdik, source:21:107}. İkinci ayetteki "âlemîn" kelimesi orada merhametin ulaştığı yer olarak geçer.

## Taşan merhamet, kalıcı merhamet

[¶4] İki kelime aynı kökten gelir ama iki ayrı kalıba dökülmüştür. Birinci kelime Rahmân, esirgemesi her şeyi kuşatan Tanrı'nın adıdır {source:"ر ح م,B001"}. İkinci kelime Rahîm, çok esirgeyen ve bol bol iyilik eden demektir {source:"ر ح م,B001"}. Arapçada Rahmân'ın kalıbı, içi dolup taşan bir hâli anlatır. "Susuz" ve "öfkeli" anlamına gelen kelimeler de bu kalıptadır. Rahîm'in kalıbı ise yerleşmiş ve süren bir niteliği anlatır. Biri taşkınlığı, öbürü sürekliliği öne çıkarır. Bu yüzden ikinci kelime birincinin tekrarı değildir, onu tamamlar.

[¶5] Kur'an bu farkı kullanımıyla da gösterir. Rahmân orada neredeyse bir özel isim gibidir. Allah Peygambere şunu söyletir: {ar:قُلِ ٱدْعُوا۟ ٱللَّهَ أَوِ ٱدْعُوا۟ ٱلرَّحْمَٰنَ, tr:kulid'ullâhe evid'u'r-rahmân, gloss:de ki: ister Allah diye çağırın ister Rahmân diye, source:17:110}. İnkâr edenler bu adı bir yabancıyı sorar gibi sorarlar. Onlara Rahmân'a secde etmeleri söylendiğinde şöyle derler: {ar:وَمَا ٱلرَّحْمَٰنُ, tr:ve mâ'r-rahmân, gloss:Rahmân da nedir, source:25:60}. Rahmân bütün varlığı ilgilendiren yerlerde anılır. Arşın üzerinde O vardır: {ar:ٱلرَّحْمَٰنُ عَلَى ٱلْعَرْشِ ٱسْتَوَىٰ, tr:er-rahmânu ale'l-arşi'stevâ, gloss:Rahmân arşa kurulmuştur, source:20:5}. Kanat açıp kapayan kuşları havada O tutar: {ar:مَا يُمْسِكُهُنَّ إِلَّا ٱلرَّحْمَٰنُ, tr:mâ yümsikuhünne ille'r-rahmân, gloss:onları Rahmân'dan başkası tutmaz, source:67:19}. Göklerin yaratılışı da O'nun yaratılışı olarak gösterilir: {ar:مَّا تَرَىٰ فِى خَلْقِ ٱلرَّحْمَٰنِ مِن تَفَٰوُتٍۢ, tr:mâ terâ fî halkı'r-rahmâni min tefâvüt, gloss:Rahmân'ın yaratışında bir uyumsuzluk göremezsin, source:67:3}. Kur'an Rahmân kelimesini hiçbir insan için kullanmaz. Rahîm ise bir insan için de söylenebilir. Allah inananlara gelen elçiyi şöyle anlatır: {ar:بِٱلْمُؤْمِنِينَ رَءُوفٌۭ رَّحِيمٌۭ, tr:bi'l-mü'minîne raûfün rahîm, gloss:inananlara karşı şefkatli ve merhametlidir, source:9:128}. Rahîm çoğu zaman belli kişilere yönelir: {ar:وَكَانَ بِٱلْمُؤْمِنِينَ رَحِيمًۭا, tr:ve kâne bi'l-mü'minîne rahîmâ, gloss:O inananlara karşı merhametlidir, source:33:43}. Cennettekilere verilen selam da bu kelimeyi ikinci ayetin kelimesiyle birlikte taşır: {ar:سَلَٰمٌۭ قَوْلًۭا مِّن رَّبٍّۢ رَّحِيمٍۢ, tr:selâmün kavlen min rabbin rahîm, gloss:merhametli bir Rabden söz olarak selam, source:36:58}.

[¶6] İki kelimenin bu iki hareketi Kur'an'da tek bir cevapta da görülür. Musa, kavminden seçtiği yetmiş kişiyi sarsıntı yakalayınca Rabbine yalvarır {source:7:155}. Aldığı cevapta önce sınırsız bir genişlik, ardından bir yazılış vardır: {ar:وَرَحْمَتِى وَسِعَتْ كُلَّ شَىْءٍۢ ۚ فَسَأَكْتُبُهَا لِلَّذِينَ يَتَّقُونَ, tr:ve rahmetî vesi'at külle şey', fe-se-ektübühâ lillezîne yettekûn, gloss:rahmetim her şeyi kuşatmıştır; onu sakınanlara yazacağım, source:7:156}. Her şeyi kuşatan merhamet Rahmân'ın, belli kişilere yazılan ve onlarla kalan merhamet Rahîm'in sesine yakındır. Arşı taşıyan melekler de aynı genişlikle dua eder: {ar:رَبَّنَا وَسِعْتَ كُلَّ شَىْءٍۢ رَّحْمَةًۭ وَعِلْمًۭا, tr:rabbenâ vesi'te külle şey'in rahmeten ve ilmâ, gloss:Rabbimiz, rahmetin ve bilginle her şeyi kuşattın, source:40:7}. Bu duada da merhamet Rab diye seslenilen birine söylenir, tıpkı Fâtiha'da ikinci ayetten üçüncüye geçerken olduğu gibi.

## Rahim: içinde büyütülen ev

[¶7] Bu kökün ailesinde ana karnındaki döl yatağı da vardır. Aşağıdaki görüntüler ayetteki "merhametli" anlamının yerine geçmez, onun yanında duyulur. Türkçe okur bu kelimeyi tıp dilinden "rahim" olarak tanır. Döl yatağı "rahim", ayetteki sıfat ise uzun "i" ile "Rahîm" diye okunur. İkisi ayrı kelimelerdir ama aynı köke aittir. Araplar döl yatağını şöyle tarif ederdi: {ar:الرحم بيت منبت الولد ووعاؤه في البطن, tr:er-rahimu beytü menbiti'l-veledi ve vi'âühû fi'l-batn, gloss:rahim, karında çocuğun bittiği ev ve onun kabıdır, source:"ر ح م,B003"}. Bu evin nasıl işlediğine bakmak gerekir. Çocuğu dışarıdan kapar ve korur, annenin bedeninden beslenmesini sağlar, onu halden hale geçirerek büyütür. Bütün bunlar, çocuk bir şey isteyemeden, hatta bilemeden olur. Verilen her şey istekten önce gelir. Fâtiha'daki sıra da bunu yansıtır: Merhamet üçüncü ayette anılır, yardım ve yol isteği ise ancak beşinci ve altıncı ayetlerde gelir.

[¶8] Kur'an bu evi bir yaratılış sahnesi olarak anlatır. İnsanlara hitap eden bir ayette şöyle denir: {ar:يَخْلُقُكُمْ فِى بُطُونِ أُمَّهَٰتِكُمْ خَلْقًۭا مِّنۢ بَعْدِ خَلْقٍۢ فِى ظُلُمَٰتٍۢ ثَلَٰثٍۢ, tr:yahlukuküm fî butûni ümmehâtiküm halkan min ba'di halkın fî zulümâtin selâs, gloss:sizi annelerinizin karınlarında, üç karanlık içinde, yaratılıştan yaratılışa geçirerek yaratır, source:39:6}. Aynı ayet hemen ardından şöyle devam eder: {ar:ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ لَهُ ٱلْمُلْكُ, tr:zâlikümullâhu rabbüküm lehü'l-mülk, gloss:işte bu Allah'tır, Rabbinizdir, mülk O'nundur, source:39:6}. Karanlık bir evde büyütme, Rab ve mülk aynı ayette sıralanır. Bu sıra Fâtiha'nın ikinci, üçüncü ve dördüncü ayetlerinin sırasıdır. Bir başka ayet aynı evin içindeki işi bir kelimeyle söyler: {ar:هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ, tr:hüvellezî yusavvirukum fi'l-erhâmi keyfe yeşâ', gloss:sizi rahimlerde dilediği gibi biçimlendiren O'dur, source:3:6}. Bu ev, surenin ikinci ayetindeki Rab kelimesiyle birlikte bir sahne kurar. O kelimenin ailesi çocuğu halden hale büyütmeyi anlatır. Döl yatağı ile büyütme o sahnede bir aradadır.

[¶9] Ev, içinden çıkanları birbirine de bağlar. Akrabalığa da aynı ad verilir ve gerekçesi açıkça söylenir: {ar:استعير الرحم للقرابة لكونهم خارجين من رحم واحدة, tr:üstüîre'r-rahimu li'l-karâbe li-kevnihim hâricîne min rahimin vâhide, gloss:rahim adı akrabalığa ödünç verildi, çünkü akrabalar tek bir rahimden çıkmıştır, source:"ر ح م,B002"}. İki kişi arasında yakın bir bağ olduğunu anlatmak için {ar:بينهما رحم أي قرابة قريبة, tr:beynehümâ rahim, gloss:aralarında yakın bir akrabalık var, source:"ر ح م,B002"} denirdi. Bu bağ sürdürülebilir de koparılabilir de {source:"ر ح م,B002"}. Kur'an insanlara tek bir candan yaratıldıklarını hatırlattığı ayette Allah'ın adını ve bu bağları yan yana anar: {ar:وَٱتَّقُوا۟ ٱللَّهَ ٱلَّذِى تَسَآءَلُونَ بِهِۦ وَٱلْأَرْحَامَ, tr:vettekullâhellezî tesâelûne bihî ve'l-erhâm, gloss:adını anarak birbirinizden dilekte bulunduğunuz Allah'tan ve akrabalık bağlarından sakının, source:4:1}. Savaştan geri duranlara yöneltilen bir soruda ise bağı koparmak, yeryüzünü bozmakla birlikte anılır: {ar:أَن تُفْسِدُوا۟ فِى ٱلْأَرْضِ وَتُقَطِّعُوٓا۟ أَرْحَامَكُمْ, tr:en tüfsidû fi'l-ardı ve tukatti'û erhâmeküm, gloss:yeryüzünde bozgunculuk yapmanız ve akrabalık bağlarınızı koparmanız, source:47:22}. Bu ayetlerin yanında okununca Rahmân ve Rahîm sıfatları, verilen bir iyiliğin yanı sıra kurulan ve korunan bir bağı da duyurur. Çok yakın bir ilişkinin adı olur.

[¶10] Aynı ailede bu evin bedeli de vardır. Araplar {ar:الرحوم الناقة التي تشتكي رحمها بعد النتاج, tr:er-rahûmu'n-nâkatü'lletî teştekî rahimehâ ba'de'n-nitâc, gloss:rahûm, doğurduktan sonra rahminden acı çeken dişi devedir, source:"ر ح م,B004"} derlerdi. Doğurduktan sonra eşini atamayan koyun için de bir kelimeleri vardı {source:"ر ح م,B004"}. Bu görüntü yaratılmışların merhametine aittir. Ayetteki Rahmân hiçbir yerde bir acıyla anılmaz. Görüntü insan merhametinin neye mal olduğunu gösterir. Kur'an da anneyi böyle anar: {ar:حَمَلَتْهُ أُمُّهُۥ كُرْهًۭا وَوَضَعَتْهُ كُرْهًۭا, tr:hamelethü ümmühû kürhen ve vada'athü kürhâ, gloss:annesi onu zorlukla taşıdı ve zorlukla doğurdu, source:46:15}. Aynı ayette kırk yaşına gelen insan şöyle dua eder: {ar:رَبِّ أَوْزِعْنِىٓ أَنْ أَشْكُرَ نِعْمَتَكَ ٱلَّتِىٓ أَنْعَمْتَ عَلَىَّ وَعَلَىٰ وَٰلِدَىَّ, tr:rabbi evzi'nî en eşküra ni'meteke'lletî en'amte aleyye ve alâ vâlideyye, gloss:Rabbim, bana ve anne babama verdiğin nimete şükretmemi sağla, source:46:15}. Rahmin taşıdığı yük, sonunda Rabbe yöneltilen bir teşekküre dönüşür. Bu duada ikinci ayetin Rab'bi ile yedinci ayetin "en'amte" kelimesi bir arada duyulur. Lokmân suresinde de annenin "zayıflık üstüne zayıflıkla" taşıdığı söylendikten sonra Allah hem kendisine hem anne babaya şükredilmesini ister {source:31:14}.

## İyiliğe dönüşen incelik

[¶11] Kökün temel anlamı bir duygudur: {ar:أصل واحد يدل على الرقة والعطف والرأفة, tr:aslun vâhidun yedüllü ale'r-rikkati ve'l-atfi ve'r-ra'fe, gloss:incelik, şefkatle eğilme ve acıma anlamına gelen tek bir kök, source:"ر ح م,B001"}. Ancak bu duygu içeride kalmaz: {ar:الرحمة رقة تقتضي الإحسان إلى المرحوم, tr:er-rahmetü rikkatün tektedi'l-ihsâne ile'l-merhûm, gloss:rahmet, merhamet edilene iyilik etmeyi gerektiren bir inceliktir, source:"ر ح م,B001"}. Önce yürek yumuşar, sonra el uzanır. Bu merhametin özellikle yöneldiği biri de vardır: {ar:ورحمة الضعيف والتعطف عليه, tr:ve rahmetü'd-da'îfi ve't-teattufu aleyh, gloss:güçsüze merhamet etmek ve şefkatle üzerine eğilmek, source:"ر ح م,B001"}. Güçlü olan, güçsüzün üzerine eğilir.

[¶12] Türkçe bu ailenin kelimelerini daraltarak almıştır. "Merhamet" çoğunlukla içte duyulan bir acıma olarak kalmış, Arapçadaki iyilik etme zorunluluğu ondan düşmüştür. "Rahmet" ise gündelik dilde yağmura ya da "rahmetli" kelimesinde ölmüş bir kişiye bağlanmıştır. Yağmur anlamı aslında Kur'an'dan gelen bir izi korur. Kur'an rüzgârların {ar:بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ, tr:büşran beyne yedey rahmetih, gloss:rahmetinin önünden müjdeci olarak, source:7:57} gönderildiğini söyler. O rüzgârlar ağır bulutları ölü bir toprağa sürer ve su indirir. Başka bir ayet bu iyiliğin gözle görülen izlerine bakmayı ister: {ar:فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ, tr:fenzur ilâ âsâri rahmetillâhi keyfe yuhyi'l-arda ba'de mevtihâ, gloss:Allah'ın rahmetinin izlerine bak, toprağı ölümünden sonra nasıl diriltiyor, source:30:50}. Burada rahmet bir duygu olarak değil, toprağa inen ve bitki bitiren bir iş olarak görünür. Türkçenin yağmura "rahmet" demesi bu işi hatırlatır. "Merhamet" kelimesinin yalnızca acıma anlamına daralması ise onu unutturur.

[¶13] İnsan merhameti de Kur'an'da bir iş ve bir zahmet olarak anlatılır. Beled suresinde Allah, malını harcadığıyla övünen insanın aşmadığı sarp yokuşu tarif eder: {ar:فَكُّ رَقَبَةٍ, tr:fekkü rakabe, gloss:bir boynu kölelikten kurtarmak, source:90:13}, açlık gününde {ar:يَتِيمًۭا ذَا مَقْرَبَةٍ, tr:yetîmen zâ makrabe, gloss:yakınlığı olan bir yetimi, source:90:15} doyurmak. Yokuşun sonunda bu işleri yapanlar şöyle anılır: {ar:وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ, tr:ve tevâsav bi'l-merhame, gloss:birbirlerine merhameti öğütlediler, source:90:17}. Yetimin "yakınlığı" başka bir köktendir. Yine de rahim kelimesinin akrabalığı anlatan kullanımının yanında okununca merhametin önce en yakındaki güçsüze uzandığını gösterir.

[¶14] İyiliği gerektiren incelik tanımı bir şeyi daha açıklar. Merhamet, görünüşüyle değil, merhamet edilene ulaşan iyilikle ölçülür. Kehf suresinde Musa yanında bir yol arkadaşıyla yürür. Bu kişiyi Allah {ar:ءَاتَيْنَٰهُ رَحْمَةًۭ مِّنْ عِندِنَا, tr:âteynâhü rahmeten min indinâ, gloss:ona katımızdan bir rahmet vermiştik, source:18:65} diye tanıtır. Rahmet verilmiş bu kul, Musa'nın gözü önünde bir çocuğu öldürür. Musa buna itiraz eder {source:18:74}. Sonradan yapılan açıklamada çocuğun inanan anne babasını azgınlığa ve inkâra sürükleyeceğinden korkulduğu söylenir {source:18:80}. Ardından şu gelir: {ar:فَأَرَدْنَآ أَن يُبْدِلَهُمَا رَبُّهُمَا خَيْرًۭا مِّنْهُ زَكَوٰةًۭ وَأَقْرَبَ رُحْمًۭا, tr:fe-eradnâ en yübdilehümâ rabbühümâ hayran minhü zekâten ve akrabe ruhmâ, gloss:Rablerinin onlara, ondan daha temiz ve anne babasına daha yakın, daha merhametli bir çocuk vermesini istedik, source:18:81}. Bu ayetteki "ruhm" kelimesi, anne babasına daha iyi davranan ve onlara daha yakın olan kişiyi anlatır {source:"ر ح م,B001"}. Yıkılmak üzere olan duvarın düzeltilmesi de {ar:رَحْمَةًۭ مِّن رَّبِّكَ, tr:rahmeten min rabbik, gloss:Rabbinden bir rahmet olarak, source:18:82} yapılmıştır. Rahmetin ilk görünüşü sert olabilir. Asıl yüzü, sonunda kime hangi iyiliği ulaştırdığında ortaya çıkar.

## Günün sahibi Rahmân'dır

[¶15] Üçüncü ayetin hemen ardından gelen dördüncü ayet bir günden ve o günün sahibinden söz eder. İlk bakışta merhamet ile hesap birbirine karşıt görünebilir. Kur'an ise ikisini aynı adda birleştirir. Göğün bulutlarla yarılıp meleklerin indirildiği gün anlatılırken şöyle denir: {ar:ٱلْمُلْكُ يَوْمَئِذٍ ٱلْحَقُّ لِلرَّحْمَٰنِ, tr:el-mülkü yevmeizini'l-hakku li'r-rahmân, gloss:o gün gerçek mülk Rahmân'ındır, source:25:26}. Aynı ayet o günün inkâr edenlere zor geleceğini de ekler. Nebe suresinde, sakınanlara verilecek karşılık anlatıldıktan sonra, Fâtiha'nın ikinci, üçüncü ve dördüncü ayetlerinin kelimeleri neredeyse aynı sırayla gelir: {ar:رَّبِّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا ٱلرَّحْمَٰنِ ۖ لَا يَمْلِكُونَ مِنْهُ خِطَابًۭا, tr:rabbi's-semâvâti ve'l-ardı ve mâ beynehüme'r-rahmân, lâ yemlikûne minhü hitâbâ, gloss:göklerin, yerin ve aralarındakilerin Rabbi, Rahmân; O'na karşı söz söylemeye güçleri yetmez, source:78:37}. Ardından o gün gelir: {ar:يَوْمَ يَقُومُ ٱلرُّوحُ وَٱلْمَلَٰٓئِكَةُ صَفًّۭا ۖ لَّا يَتَكَلَّمُونَ إِلَّا مَنْ أَذِنَ لَهُ ٱلرَّحْمَٰنُ, tr:yevme yekûmu'r-rûhu ve'l-melâiketü saffâ, lâ yetekellemûne illâ men ezine lehü'r-rahmân, gloss:Ruh ve melekler saf saf durduğu gün, Rahmân'ın izin verdiğinden başkası konuşmaz, source:78:38}. Rab, Rahmân, sahip olma ve gün aynı yerde bir aradadır. Tâhâ suresinde de o günün sessizliği bu ada bağlanır: {ar:وَخَشَعَتِ ٱلْأَصْوَاتُ لِلرَّحْمَٰنِ فَلَا تَسْمَعُ إِلَّا هَمْسًۭا, tr:ve haşa'ati'l-asvâtu li'r-rahmâni fe-lâ tesme'u illâ hemsâ, gloss:sesler Rahmân'ın önünde kısılır, fısıltıdan başka bir şey duymazsın, source:20:108}.

[¶16] Merhamet ile toplanma günü, Kur'an'da tek bir nefeste de söylenir. Peygambere, göklerde ve yerde olanların kime ait olduğunu sorup cevabı da kendisinin vermesi emredilir. Ardından şu gelir: {ar:كَتَبَ عَلَىٰ نَفْسِهِ ٱلرَّحْمَةَ ۚ لَيَجْمَعَنَّكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ, tr:ketebe alâ nefsihi'r-rahmete le-yecme'annekum ilâ yevmi'l-kıyâmeh, gloss:rahmeti kendi üzerine yazmıştır; sizi kıyamet gününe mutlaka toplayacaktır, source:6:12}. Günün sahibinin rahmeti kendine yazmış olması, o günü bir tehdit olmaktan çıkarıp bir sözün yerine gelmesine dönüştürür. Fâtiha'da üçüncü ayetin dördüncüden önce gelmesi de aynı şeyi söyler. Hesabı görecek olan, önce iki kez merhametle anılmıştır.

[¶17] Bu merhamet hafife alınacak bir yumuşaklık da değildir. Meryem suresinde İbrahim, şeytana kulluk eden babasına yalvarırken şöyle der: {ar:يَٰٓأَبَتِ إِنِّىٓ أَخَافُ أَن يَمَسَّكَ عَذَابٌۭ مِّنَ ٱلرَّحْمَٰنِ, tr:yâ ebeti innî ehâfu en yemesseke azâbün mine'r-rahmân, gloss:babacığım, sana Rahmân'dan bir azabın dokunmasından korkuyorum, source:19:45}. Uyarının kime fayda vereceği anlatılırken de aynı ad geçer: {ar:وَخَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ, tr:ve haşiye'r-rahmâne bi'l-gayb, gloss:görmediği hâlde Rahmân'dan saygıyla korkan, source:36:11}. Korkulan şey merhametin kendisi değildir. Korku, o merhameti kaybetmekten ve bu kadar geniş bir iyiliğin sahibinin önünde boş çıkmaktandır. Üçüncü ayet ile dördüncü ayet bu yüzden birbirini dengeler. Merhamet hesabı yumuşatır, hesap da merhameti ciddiye aldırır.

[¶18] Ardından beşinci ayetin kulu konuşur. Kur'an bu kulluğu Rahmân adına bağlar: {ar:إِن كُلُّ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ إِلَّآ ءَاتِى ٱلرَّحْمَٰنِ عَبْدًۭا, tr:in küllü men fi's-semâvâti ve'l-ardı illâ âti'r-rahmâni abdâ, gloss:göklerde ve yerde olan herkes Rahmân'a ancak kul olarak gelir, source:19:93}. O kulların yeryüzünde yürüyüşü de bir başka surede anlatılır: {ar:وَعِبَادُ ٱلرَّحْمَٰنِ ٱلَّذِينَ يَمْشُونَ عَلَى ٱلْأَرْضِ هَوْنًۭا, tr:ve ibâdü'r-rahmâni'llezîne yemşûne ale'l-ardı hevnâ, gloss:Rahmân'ın kulları yeryüzünde yumuşak adımlarla yürüyenlerdir, source:25:63}. "Yalnız sana kulluk ederiz" diyen ses, üçüncü ayette anılan Rahmân'a seslenmektedir. Bu kulların yürüyüşü, altıncı ayette istenen yolla bir sahne kurar.

===== _commentary/v16/out/1_3/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: fa'lān pattern conveys a full, overflowing state (as in ʿaṭshān, ghaḍbān)
- memory: faʿīl pattern conveys a settled, lasting quality
- memory: raḥmān is never used of a human in the Quran (not checked across the whole text)
- memory: Turkish rahmet = rain, rahmetli = the deceased, merhamet narrowed to pity
- not written: ewe not expelling afterbirth (B004) - only named, adds nothing beyond rahūm
- not written: tarahhum, asking God's mercy for someone (B001) - no theme needed it
- not written: 17:24 rabb/raḥma/upbringing scene - belongs to surah commentary; recalled only through 1:2
- not written: 55:1-4 Rahmān as teacher - teaching thread is 1:2's rabb, not this ayah
- not written: Maryam surah frequency of al-Raḥmān - count unverified
- not written: 30:21 mawadda wa raḥma between spouses - kinship already grounded by 4:1, 47:22
- not written: 39:53 despair of mercy - did not reshape any theme

===== passages not cited (331) =====
## strong (this ayah's own list) (35)

- (3:159) [listed for 1:3] فَبِمَا رَحْمَةٍۢ مِّنَ ٱللَّهِ لِنتَ لَهُمْ ۖ وَلَوْ كُنتَ فَظًّا غَلِيظَ ٱلْقَلْبِ لَٱنفَضُّوا۟ مِنْ حَوْلِكَ ۖ فَٱعْفُ عَنْهُمْ وَٱسْتَغْفِرْ لَهُمْ وَشَاوِرْهُمْ فِى ٱلْأَمْرِ ۖ فَإِذَا عَزَمْتَ فَتَوَكَّلْ عَلَى ٱللَّهِ ۚ إِنَّ ٱللَّهَ يُحِبُّ ٱلْمُتَوَكِّلِينَ
- (4:106) [listed for 1:3] وَٱسْتَغْفِرِ ٱللَّهَ ۖ إِنَّ ٱللَّهَ كَانَ غَفُورًۭا رَّحِيمًۭا
- (4:175) [listed for 1:3] فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ بِٱللَّهِ وَٱعْتَصَمُوا۟ بِهِۦ فَسَيُدْخِلُهُمْ فِى رَحْمَةٍۢ مِّنْهُ وَفَضْلٍۢ وَيَهْدِيهِمْ إِلَيْهِ صِرَٰطًۭا مُّسْتَقِيمًۭا
- (6:12) [listed for 1:3] [cited in ¶16] قُل لِّمَن مَّا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ قُل لِّلَّهِ ۚ كَتَبَ عَلَىٰ نَفْسِهِ ٱلرَّحْمَةَ ۚ لَيَجْمَعَنَّكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ ۚ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ فَهُمْ لَا يُؤْمِنُونَ
- (6:54) [listed for 1:3] وَإِذَا جَآءَكَ ٱلَّذِينَ يُؤْمِنُونَ بِـَٔايَٰتِنَا فَقُلْ سَلَٰمٌ عَلَيْكُمْ ۖ كَتَبَ رَبُّكُمْ عَلَىٰ نَفْسِهِ ٱلرَّحْمَةَ ۖ أَنَّهُۥ مَنْ عَمِلَ مِنكُمْ سُوٓءًۢا بِجَهَٰلَةٍۢ ثُمَّ تَابَ مِنۢ بَعْدِهِۦ وَأَصْلَحَ فَأَنَّهُۥ غَفُورٌۭ رَّحِيمٌۭ
- (7:156) [listed for 1:3] [cited in ¶6] ۞ وَٱكْتُبْ لَنَا فِى هَٰذِهِ ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ إِنَّا هُدْنَآ إِلَيْكَ ۚ قَالَ عَذَابِىٓ أُصِيبُ بِهِۦ مَنْ أَشَآءُ ۖ وَرَحْمَتِى وَسِعَتْ كُلَّ شَىْءٍۢ ۚ فَسَأَكْتُبُهَا لِلَّذِينَ يَتَّقُونَ وَيُؤْتُونَ ٱلزَّكَوٰةَ وَٱلَّذِينَ هُم بِـَٔايَٰتِنَا يُؤْمِنُونَ
- (12:64) [listed for 1:3] قَالَ هَلْ ءَامَنُكُمْ عَلَيْهِ إِلَّا كَمَآ أَمِنتُكُمْ عَلَىٰٓ أَخِيهِ مِن قَبْلُ ۖ فَٱللَّهُ خَيْرٌ حَٰفِظًۭا ۖ وَهُوَ أَرْحَمُ ٱلرَّٰحِمِينَ
- (12:92) [listed for 1:3] قَالَ لَا تَثْرِيبَ عَلَيْكُمُ ٱلْيَوْمَ ۖ يَغْفِرُ ٱللَّهُ لَكُمْ ۖ وَهُوَ أَرْحَمُ ٱلرَّٰحِمِينَ
- (17:82) [listed for 1:3] وَنُنَزِّلُ مِنَ ٱلْقُرْءَانِ مَا هُوَ شِفَآءٌۭ وَرَحْمَةٌۭ لِّلْمُؤْمِنِينَ ۙ وَلَا يَزِيدُ ٱلظَّٰلِمِينَ إِلَّا خَسَارًۭا
- (18:58) [listed for 1:3] وَرَبُّكَ ٱلْغَفُورُ ذُو ٱلرَّحْمَةِ ۖ لَوْ يُؤَاخِذُهُم بِمَا كَسَبُوا۟ لَعَجَّلَ لَهُمُ ٱلْعَذَابَ ۚ بَل لَّهُم مَّوْعِدٌۭ لَّن يَجِدُوا۟ مِن دُونِهِۦ مَوْئِلًۭا
- (19:96) [listed for 1:3] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ سَيَجْعَلُ لَهُمُ ٱلرَّحْمَٰنُ وُدًّۭا
- (20:5) [listed for 1:3] [cited in ¶5] ٱلرَّحْمَٰنُ عَلَى ٱلْعَرْشِ ٱسْتَوَىٰ
- (20:90) [listed for 1:3] وَلَقَدْ قَالَ لَهُمْ هَٰرُونُ مِن قَبْلُ يَٰقَوْمِ إِنَّمَا فُتِنتُم بِهِۦ ۖ وَإِنَّ رَبَّكُمُ ٱلرَّحْمَٰنُ فَٱتَّبِعُونِى وَأَطِيعُوٓا۟ أَمْرِى
- (20:109) [listed for 1:3] يَوْمَئِذٍۢ لَّا تَنفَعُ ٱلشَّفَٰعَةُ إِلَّا مَنْ أَذِنَ لَهُ ٱلرَّحْمَٰنُ وَرَضِىَ لَهُۥ قَوْلًۭا
- (21:107) [listed for 1:3] [cited in ¶3] وَمَآ أَرْسَلْنَٰكَ إِلَّا رَحْمَةًۭ لِّلْعَٰلَمِينَ
- (21:112) [listed for 1:3] قَٰلَ رَبِّ ٱحْكُم بِٱلْحَقِّ ۗ وَرَبُّنَا ٱلرَّحْمَٰنُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ
- (23:109) [listed for 1:3] إِنَّهُۥ كَانَ فَرِيقٌۭ مِّنْ عِبَادِى يَقُولُونَ رَبَّنَآ ءَامَنَّا فَٱغْفِرْ لَنَا وَٱرْحَمْنَا وَأَنتَ خَيْرُ ٱلرَّٰحِمِينَ
- (23:118) [listed for 1:3] وَقُل رَّبِّ ٱغْفِرْ وَٱرْحَمْ وَأَنتَ خَيْرُ ٱلرَّٰحِمِينَ
- (25:59) [listed for 1:3] ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَمَا بَيْنَهُمَا فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ ۚ ٱلرَّحْمَٰنُ فَسْـَٔلْ بِهِۦ خَبِيرًۭا
- (25:63) [listed for 1:3] [cited in ¶18] وَعِبَادُ ٱلرَّحْمَٰنِ ٱلَّذِينَ يَمْشُونَ عَلَى ٱلْأَرْضِ هَوْنًۭا وَإِذَا خَاطَبَهُمُ ٱلْجَٰهِلُونَ قَالُوا۟ سَلَٰمًۭا
- (30:21) [listed for 1:3] وَمِنْ ءَايَٰتِهِۦٓ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَٰجًۭا لِّتَسْكُنُوٓا۟ إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةًۭ وَرَحْمَةً ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَتَفَكَّرُونَ
- (37:118) [listed for 1:3] وَهَدَيْنَٰهُمَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- (39:53) [listed for 1:3] ۞ قُلْ يَٰعِبَادِىَ ٱلَّذِينَ أَسْرَفُوا۟ عَلَىٰٓ أَنفُسِهِمْ لَا تَقْنَطُوا۟ مِن رَّحْمَةِ ٱللَّهِ ۚ إِنَّ ٱللَّهَ يَغْفِرُ ٱلذُّنُوبَ جَمِيعًا ۚ إِنَّهُۥ هُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- (40:7) [listed for 1:3] [cited in ¶6] ٱلَّذِينَ يَحْمِلُونَ ٱلْعَرْشَ وَمَنْ حَوْلَهُۥ يُسَبِّحُونَ بِحَمْدِ رَبِّهِمْ وَيُؤْمِنُونَ بِهِۦ وَيَسْتَغْفِرُونَ لِلَّذِينَ ءَامَنُوا۟ رَبَّنَا وَسِعْتَ كُلَّ شَىْءٍۢ رَّحْمَةًۭ وَعِلْمًۭا فَٱغْفِرْ لِلَّذِينَ تَابُوا۟ وَٱتَّبَعُوا۟ سَبِيلَكَ وَقِهِمْ عَذَابَ ٱلْجَحِيمِ
- (42:28) [listed for 1:3] وَهُوَ ٱلَّذِى يُنَزِّلُ ٱلْغَيْثَ مِنۢ بَعْدِ مَا قَنَطُوا۟ وَيَنشُرُ رَحْمَتَهُۥ ۚ وَهُوَ ٱلْوَلِىُّ ٱلْحَمِيدُ
- (46:12) [listed for 1:3] وَمِن قَبْلِهِۦ كِتَٰبُ مُوسَىٰٓ إِمَامًۭا وَرَحْمَةًۭ ۚ وَهَٰذَا كِتَٰبٌۭ مُّصَدِّقٌۭ لِّسَانًا عَرَبِيًّۭا لِّيُنذِرَ ٱلَّذِينَ ظَلَمُوا۟ وَبُشْرَىٰ لِلْمُحْسِنِينَ
- (55:1) [listed for 1:3] ٱلرَّحْمَٰنُ
- (55:2) [listed for 1:3] عَلَّمَ ٱلْقُرْءَانَ
- (55:3) [listed for 1:3] خَلَقَ ٱلْإِنسَٰنَ
- (55:4) [listed for 1:3] عَلَّمَهُ ٱلْبَيَانَ
- (57:28) [listed for 1:3] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَءَامِنُوا۟ بِرَسُولِهِۦ يُؤْتِكُمْ كِفْلَيْنِ مِن رَّحْمَتِهِۦ وَيَجْعَل لَّكُمْ نُورًۭا تَمْشُونَ بِهِۦ وَيَغْفِرْ لَكُمْ ۚ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌۭ
- (59:10) [listed for 1:3] وَٱلَّذِينَ جَآءُو مِنۢ بَعْدِهِمْ يَقُولُونَ رَبَّنَا ٱغْفِرْ لَنَا وَلِإِخْوَٰنِنَا ٱلَّذِينَ سَبَقُونَا بِٱلْإِيمَٰنِ وَلَا تَجْعَلْ فِى قُلُوبِنَا غِلًّۭا لِّلَّذِينَ ءَامَنُوا۟ رَبَّنَآ إِنَّكَ رَءُوفٌۭ رَّحِيمٌ
- (59:22) [listed for 1:3] هُوَ ٱللَّهُ ٱلَّذِى لَآ إِلَٰهَ إِلَّا هُوَ ۖ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۖ هُوَ ٱلرَّحْمَٰنُ ٱلرَّحِيمُ
- (78:38) [listed for 1:3] [cited in ¶15] يَوْمَ يَقُومُ ٱلرُّوحُ وَٱلْمَلَٰٓئِكَةُ صَفًّۭا ۖ لَّا يَتَكَلَّمُونَ إِلَّا مَنْ أَذِنَ لَهُ ٱلرَّحْمَٰنُ وَقَالَ صَوَابًۭا
- (90:17) [listed for 1:3] [cited in ¶13] ثُمَّ كَانَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ وَتَوَاصَوْا۟ بِٱلصَّبْرِ وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ

## medium (this ayah's own list) (64)

- (2:163) [listed for 1:3] وَإِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ ۖ لَّآ إِلَٰهَ إِلَّا هُوَ ٱلرَّحْمَٰنُ ٱلرَّحِيمُ
- (3:8) [listed for 1:3] رَبَّنَا لَا تُزِغْ قُلُوبَنَا بَعْدَ إِذْ هَدَيْتَنَا وَهَبْ لَنَا مِن لَّدُنكَ رَحْمَةً ۚ إِنَّكَ أَنتَ ٱلْوَهَّابُ
- (3:74) [listed for 1:3] يَخْتَصُّ بِرَحْمَتِهِۦ مَن يَشَآءُ ۗ وَٱللَّهُ ذُو ٱلْفَضْلِ ٱلْعَظِيمِ
- (3:101) [listed for 1:3] وَكَيْفَ تَكْفُرُونَ وَأَنتُمْ تُتْلَىٰ عَلَيْكُمْ ءَايَٰتُ ٱللَّهِ وَفِيكُمْ رَسُولُهُۥ ۗ وَمَن يَعْتَصِم بِٱللَّهِ فَقَدْ هُدِىَ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- (4:1) [listed for 1:3] [cited in ¶9] يَٰٓأَيُّهَا ٱلنَّاسُ ٱتَّقُوا۟ رَبَّكُمُ ٱلَّذِى خَلَقَكُم مِّن نَّفْسٍۢ وَٰحِدَةٍۢ وَخَلَقَ مِنْهَا زَوْجَهَا وَبَثَّ مِنْهُمَا رِجَالًۭا كَثِيرًۭا وَنِسَآءًۭ ۚ وَٱتَّقُوا۟ ٱللَّهَ ٱلَّذِى تَسَآءَلُونَ بِهِۦ وَٱلْأَرْحَامَ ۚ إِنَّ ٱللَّهَ كَانَ عَلَيْكُمْ رَقِيبًۭا
- (4:2) [listed for 1:3] وَءَاتُوا۟ ٱلْيَتَٰمَىٰٓ أَمْوَٰلَهُمْ ۖ وَلَا تَتَبَدَّلُوا۟ ٱلْخَبِيثَ بِٱلطَّيِّبِ ۖ وَلَا تَأْكُلُوٓا۟ أَمْوَٰلَهُمْ إِلَىٰٓ أَمْوَٰلِكُمْ ۚ إِنَّهُۥ كَانَ حُوبًۭا كَبِيرًۭا
- (4:113) [listed for 1:3] وَلَوْلَا فَضْلُ ٱللَّهِ عَلَيْكَ وَرَحْمَتُهُۥ لَهَمَّت طَّآئِفَةٌۭ مِّنْهُمْ أَن يُضِلُّوكَ وَمَا يُضِلُّونَ إِلَّآ أَنفُسَهُمْ ۖ وَمَا يَضُرُّونَكَ مِن شَىْءٍۢ ۚ وَأَنزَلَ ٱللَّهُ عَلَيْكَ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَعَلَّمَكَ مَا لَمْ تَكُن تَعْلَمُ ۚ وَكَانَ فَضْلُ ٱللَّهِ عَلَيْكَ عَظِيمًۭا
- (6:147) [listed for 1:3] فَإِن كَذَّبُوكَ فَقُل رَّبُّكُمْ ذُو رَحْمَةٍۢ وَٰسِعَةٍۢ وَلَا يُرَدُّ بَأْسُهُۥ عَنِ ٱلْقَوْمِ ٱلْمُجْرِمِينَ
- (7:56) [listed for 1:3] وَلَا تُفْسِدُوا۟ فِى ٱلْأَرْضِ بَعْدَ إِصْلَٰحِهَا وَٱدْعُوهُ خَوْفًۭا وَطَمَعًا ۚ إِنَّ رَحْمَتَ ٱللَّهِ قَرِيبٌۭ مِّنَ ٱلْمُحْسِنِينَ
- (7:151) [listed for 1:3] قَالَ رَبِّ ٱغْفِرْ لِى وَلِأَخِى وَأَدْخِلْنَا فِى رَحْمَتِكَ ۖ وَأَنتَ أَرْحَمُ ٱلرَّٰحِمِينَ
- (9:21) [listed for 1:3] يُبَشِّرُهُمْ رَبُّهُم بِرَحْمَةٍۢ مِّنْهُ وَرِضْوَٰنٍۢ وَجَنَّٰتٍۢ لَّهُمْ فِيهَا نَعِيمٌۭ مُّقِيمٌ
- (9:99) [listed for 1:3] وَمِنَ ٱلْأَعْرَابِ مَن يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَيَتَّخِذُ مَا يُنفِقُ قُرُبَٰتٍ عِندَ ٱللَّهِ وَصَلَوَٰتِ ٱلرَّسُولِ ۚ أَلَآ إِنَّهَا قُرْبَةٌۭ لَّهُمْ ۚ سَيُدْخِلُهُمُ ٱللَّهُ فِى رَحْمَتِهِۦٓ ۗ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (10:107) [listed for 1:3] وَإِن يَمْسَسْكَ ٱللَّهُ بِضُرٍّۢ فَلَا كَاشِفَ لَهُۥٓ إِلَّا هُوَ ۖ وَإِن يُرِدْكَ بِخَيْرٍۢ فَلَا رَآدَّ لِفَضْلِهِۦ ۚ يُصِيبُ بِهِۦ مَن يَشَآءُ مِنْ عِبَادِهِۦ ۚ وَهُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- (11:28) [listed for 1:3] قَالَ يَٰقَوْمِ أَرَءَيْتُمْ إِن كُنتُ عَلَىٰ بَيِّنَةٍۢ مِّن رَّبِّى وَءَاتَىٰنِى رَحْمَةًۭ مِّنْ عِندِهِۦ فَعُمِّيَتْ عَلَيْكُمْ أَنُلْزِمُكُمُوهَا وَأَنتُمْ لَهَا كَٰرِهُونَ
- (11:119) [listed for 1:3] إِلَّا مَن رَّحِمَ رَبُّكَ ۚ وَلِذَٰلِكَ خَلَقَهُمْ ۗ وَتَمَّتْ كَلِمَةُ رَبِّكَ لَأَمْلَأَنَّ جَهَنَّمَ مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ أَجْمَعِينَ
- (12:18) [listed for 1:3] وَجَآءُو عَلَىٰ قَمِيصِهِۦ بِدَمٍۢ كَذِبٍۢ ۚ قَالَ بَلْ سَوَّلَتْ لَكُمْ أَنفُسُكُمْ أَمْرًۭا ۖ فَصَبْرٌۭ جَمِيلٌۭ ۖ وَٱللَّهُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ
- (12:56) [listed for 1:3] وَكَذَٰلِكَ مَكَّنَّا لِيُوسُفَ فِى ٱلْأَرْضِ يَتَبَوَّأُ مِنْهَا حَيْثُ يَشَآءُ ۚ نُصِيبُ بِرَحْمَتِنَا مَن نَّشَآءُ ۖ وَلَا نُضِيعُ أَجْرَ ٱلْمُحْسِنِينَ
- (12:98) [listed for 1:3] قَالَ سَوْفَ أَسْتَغْفِرُ لَكُمْ رَبِّىٓ ۖ إِنَّهُۥ هُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- (14:36) [listed for 1:3] رَبِّ إِنَّهُنَّ أَضْلَلْنَ كَثِيرًۭا مِّنَ ٱلنَّاسِ ۖ فَمَن تَبِعَنِى فَإِنَّهُۥ مِنِّى ۖ وَمَنْ عَصَانِى فَإِنَّكَ غَفُورٌۭ رَّحِيمٌۭ
- (15:49) [listed for 1:3] ۞ نَبِّئْ عِبَادِىٓ أَنِّىٓ أَنَا ٱلْغَفُورُ ٱلرَّحِيمُ
- (16:18) [listed for 1:3] وَإِن تَعُدُّوا۟ نِعْمَةَ ٱللَّهِ لَا تُحْصُوهَآ ۗ إِنَّ ٱللَّهَ لَغَفُورٌۭ رَّحِيمٌۭ
- (16:64) [listed for 1:3] وَمَآ أَنزَلْنَا عَلَيْكَ ٱلْكِتَٰبَ إِلَّا لِتُبَيِّنَ لَهُمُ ٱلَّذِى ٱخْتَلَفُوا۟ فِيهِ ۙ وَهُدًۭى وَرَحْمَةًۭ لِّقَوْمٍۢ يُؤْمِنُونَ
- (17:28) [listed for 1:3] وَإِمَّا تُعْرِضَنَّ عَنْهُمُ ٱبْتِغَآءَ رَحْمَةٍۢ مِّن رَّبِّكَ تَرْجُوهَا فَقُل لَّهُمْ قَوْلًۭا مَّيْسُورًۭا
- (17:57) [listed for 1:3] أُو۟لَٰٓئِكَ ٱلَّذِينَ يَدْعُونَ يَبْتَغُونَ إِلَىٰ رَبِّهِمُ ٱلْوَسِيلَةَ أَيُّهُمْ أَقْرَبُ وَيَرْجُونَ رَحْمَتَهُۥ وَيَخَافُونَ عَذَابَهُۥٓ ۚ إِنَّ عَذَابَ رَبِّكَ كَانَ مَحْذُورًۭا
- (17:87) [listed for 1:3] إِلَّا رَحْمَةًۭ مِّن رَّبِّكَ ۚ إِنَّ فَضْلَهُۥ كَانَ عَلَيْكَ كَبِيرًۭا
- (18:10) [listed for 1:3] إِذْ أَوَى ٱلْفِتْيَةُ إِلَى ٱلْكَهْفِ فَقَالُوا۟ رَبَّنَآ ءَاتِنَا مِن لَّدُنكَ رَحْمَةًۭ وَهَيِّئْ لَنَا مِنْ أَمْرِنَا رَشَدًۭا
- (18:16) [listed for 1:3] وَإِذِ ٱعْتَزَلْتُمُوهُمْ وَمَا يَعْبُدُونَ إِلَّا ٱللَّهَ فَأْوُۥٓا۟ إِلَى ٱلْكَهْفِ يَنشُرْ لَكُمْ رَبُّكُم مِّن رَّحْمَتِهِۦ وَيُهَيِّئْ لَكُم مِّنْ أَمْرِكُم مِّرْفَقًۭا
- (18:65) [listed for 1:3] [cited in ¶14] فَوَجَدَا عَبْدًۭا مِّنْ عِبَادِنَآ ءَاتَيْنَٰهُ رَحْمَةًۭ مِّنْ عِندِنَا وَعَلَّمْنَٰهُ مِن لَّدُنَّا عِلْمًۭا
- (19:2) [listed for 1:3] ذِكْرُ رَحْمَتِ رَبِّكَ عَبْدَهُۥ زَكَرِيَّآ
- (21:42) [listed for 1:3] قُلْ مَن يَكْلَؤُكُم بِٱلَّيْلِ وَٱلنَّهَارِ مِنَ ٱلرَّحْمَٰنِ ۗ بَلْ هُمْ عَن ذِكْرِ رَبِّهِم مُّعْرِضُونَ
- (21:75) [listed for 1:3] وَأَدْخَلْنَٰهُ فِى رَحْمَتِنَآ ۖ إِنَّهُۥ مِنَ ٱلصَّٰلِحِينَ
- (21:84) [listed for 1:3] فَٱسْتَجَبْنَا لَهُۥ فَكَشَفْنَا مَا بِهِۦ مِن ضُرٍّۢ ۖ وَءَاتَيْنَٰهُ أَهْلَهُۥ وَمِثْلَهُم مَّعَهُمْ رَحْمَةًۭ مِّنْ عِندِنَا وَذِكْرَىٰ لِلْعَٰبِدِينَ
- (22:24) [listed for 1:3] وَهُدُوٓا۟ إِلَى ٱلطَّيِّبِ مِنَ ٱلْقَوْلِ وَهُدُوٓا۟ إِلَىٰ صِرَٰطِ ٱلْحَمِيدِ
- (22:65) [listed for 1:3] أَلَمْ تَرَ أَنَّ ٱللَّهَ سَخَّرَ لَكُم مَّا فِى ٱلْأَرْضِ وَٱلْفُلْكَ تَجْرِى فِى ٱلْبَحْرِ بِأَمْرِهِۦ وَيُمْسِكُ ٱلسَّمَآءَ أَن تَقَعَ عَلَى ٱلْأَرْضِ إِلَّا بِإِذْنِهِۦٓ ۗ إِنَّ ٱللَّهَ بِٱلنَّاسِ لَرَءُوفٌۭ رَّحِيمٌۭ
- (23:75) [listed for 1:3] ۞ وَلَوْ رَحِمْنَٰهُمْ وَكَشَفْنَا مَا بِهِم مِّن ضُرٍّۢ لَّلَجُّوا۟ فِى طُغْيَٰنِهِمْ يَعْمَهُونَ
- (24:10) [listed for 1:3] وَلَوْلَا فَضْلُ ٱللَّهِ عَلَيْكُمْ وَرَحْمَتُهُۥ وَأَنَّ ٱللَّهَ تَوَّابٌ حَكِيمٌ
- (24:20) [listed for 1:3] وَلَوْلَا فَضْلُ ٱللَّهِ عَلَيْكُمْ وَرَحْمَتُهُۥ وَأَنَّ ٱللَّهَ رَءُوفٌۭ رَّحِيمٌۭ
- (24:21) [listed for 1:3] ۞ يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَتَّبِعُوا۟ خُطُوَٰتِ ٱلشَّيْطَٰنِ ۚ وَمَن يَتَّبِعْ خُطُوَٰتِ ٱلشَّيْطَٰنِ فَإِنَّهُۥ يَأْمُرُ بِٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۚ وَلَوْلَا فَضْلُ ٱللَّهِ عَلَيْكُمْ وَرَحْمَتُهُۥ مَا زَكَىٰ مِنكُم مِّنْ أَحَدٍ أَبَدًۭا وَلَٰكِنَّ ٱللَّهَ يُزَكِّى مَن يَشَآءُ ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌۭ
- (24:22) [listed for 1:3] وَلَا يَأْتَلِ أُو۟لُوا۟ ٱلْفَضْلِ مِنكُمْ وَٱلسَّعَةِ أَن يُؤْتُوٓا۟ أُو۟لِى ٱلْقُرْبَىٰ وَٱلْمَسَٰكِينَ وَٱلْمُهَٰجِرِينَ فِى سَبِيلِ ٱللَّهِ ۖ وَلْيَعْفُوا۟ وَلْيَصْفَحُوٓا۟ ۗ أَلَا تُحِبُّونَ أَن يَغْفِرَ ٱللَّهُ لَكُمْ ۗ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌ
- (25:60) [listed for 1:3] [cited in ¶5] وَإِذَا قِيلَ لَهُمُ ٱسْجُدُوا۟ لِلرَّحْمَٰنِ قَالُوا۟ وَمَا ٱلرَّحْمَٰنُ أَنَسْجُدُ لِمَا تَأْمُرُنَا وَزَادَهُمْ نُفُورًۭا ۩
- (26:104) [listed for 1:3] وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (26:217) [listed for 1:3] وَتَوَكَّلْ عَلَى ٱلْعَزِيزِ ٱلرَّحِيمِ
- (27:19) [listed for 1:3] فَتَبَسَّمَ ضَاحِكًۭا مِّن قَوْلِهَا وَقَالَ رَبِّ أَوْزِعْنِىٓ أَنْ أَشْكُرَ نِعْمَتَكَ ٱلَّتِىٓ أَنْعَمْتَ عَلَىَّ وَعَلَىٰ وَٰلِدَىَّ وَأَنْ أَعْمَلَ صَٰلِحًۭا تَرْضَىٰهُ وَأَدْخِلْنِى بِرَحْمَتِكَ فِى عِبَادِكَ ٱلصَّٰلِحِينَ
- (27:30) [listed for 1:3] إِنَّهُۥ مِن سُلَيْمَٰنَ وَإِنَّهُۥ بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- (27:63) [listed for 1:3] أَمَّن يَهْدِيكُمْ فِى ظُلُمَٰتِ ٱلْبَرِّ وَٱلْبَحْرِ وَمَن يُرْسِلُ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦٓ ۗ أَءِلَٰهٌۭ مَّعَ ٱللَّهِ ۚ تَعَٰلَى ٱللَّهُ عَمَّا يُشْرِكُونَ
- (28:46) [listed for 1:3] وَمَا كُنتَ بِجَانِبِ ٱلطُّورِ إِذْ نَادَيْنَا وَلَٰكِن رَّحْمَةًۭ مِّن رَّبِّكَ لِتُنذِرَ قَوْمًۭا مَّآ أَتَىٰهُم مِّن نَّذِيرٍۢ مِّن قَبْلِكَ لَعَلَّهُمْ يَتَذَكَّرُونَ
- (28:73) [listed for 1:3] وَمِن رَّحْمَتِهِۦ جَعَلَ لَكُمُ ٱلَّيْلَ وَٱلنَّهَارَ لِتَسْكُنُوا۟ فِيهِ وَلِتَبْتَغُوا۟ مِن فَضْلِهِۦ وَلَعَلَّكُمْ تَشْكُرُونَ
- (28:86) [listed for 1:3] وَمَا كُنتَ تَرْجُوٓا۟ أَن يُلْقَىٰٓ إِلَيْكَ ٱلْكِتَٰبُ إِلَّا رَحْمَةًۭ مِّن رَّبِّكَ ۖ فَلَا تَكُونَنَّ ظَهِيرًۭا لِّلْكَٰفِرِينَ
- (30:5) [listed for 1:3] بِنَصْرِ ٱللَّهِ ۚ يَنصُرُ مَن يَشَآءُ ۖ وَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (30:46) [listed for 1:3] وَمِنْ ءَايَٰتِهِۦٓ أَن يُرْسِلَ ٱلرِّيَاحَ مُبَشِّرَٰتٍۢ وَلِيُذِيقَكُم مِّن رَّحْمَتِهِۦ وَلِتَجْرِىَ ٱلْفُلْكُ بِأَمْرِهِۦ وَلِتَبْتَغُوا۟ مِن فَضْلِهِۦ وَلَعَلَّكُمْ تَشْكُرُونَ
- (33:43) [listed for 1:3] [cited in ¶5] هُوَ ٱلَّذِى يُصَلِّى عَلَيْكُمْ وَمَلَٰٓئِكَتُهُۥ لِيُخْرِجَكُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۚ وَكَانَ بِٱلْمُؤْمِنِينَ رَحِيمًۭا
- (36:5) [listed for 1:3] تَنزِيلَ ٱلْعَزِيزِ ٱلرَّحِيمِ
- (36:11) [listed for 1:3] [cited in ¶17] إِنَّمَا تُنذِرُ مَنِ ٱتَّبَعَ ٱلذِّكْرَ وَخَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ ۖ فَبَشِّرْهُ بِمَغْفِرَةٍۢ وَأَجْرٍۢ كَرِيمٍ
- (36:58) [listed for 1:3] [cited in ¶5] سَلَٰمٌۭ قَوْلًۭا مِّن رَّبٍّۢ رَّحِيمٍۢ
- (41:2) [listed for 1:3] تَنزِيلٌۭ مِّنَ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- (42:8) [listed for 1:3] وَلَوْ شَآءَ ٱللَّهُ لَجَعَلَهُمْ أُمَّةًۭ وَٰحِدَةًۭ وَلَٰكِن يُدْخِلُ مَن يَشَآءُ فِى رَحْمَتِهِۦ ۚ وَٱلظَّٰلِمُونَ مَا لَهُم مِّن وَلِىٍّۢ وَلَا نَصِيرٍ
- (44:6) [listed for 1:3] رَحْمَةًۭ مِّن رَّبِّكَ ۚ إِنَّهُۥ هُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (44:42) [listed for 1:3] إِلَّا مَن رَّحِمَ ٱللَّهُ ۚ إِنَّهُۥ هُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (45:30) [listed for 1:3] فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَيُدْخِلُهُمْ رَبُّهُمْ فِى رَحْمَتِهِۦ ۚ ذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْمُبِينُ
- (48:25) [listed for 1:3] هُمُ ٱلَّذِينَ كَفَرُوا۟ وَصَدُّوكُمْ عَنِ ٱلْمَسْجِدِ ٱلْحَرَامِ وَٱلْهَدْىَ مَعْكُوفًا أَن يَبْلُغَ مَحِلَّهُۥ ۚ وَلَوْلَا رِجَالٌۭ مُّؤْمِنُونَ وَنِسَآءٌۭ مُّؤْمِنَٰتٌۭ لَّمْ تَعْلَمُوهُمْ أَن تَطَـُٔوهُمْ فَتُصِيبَكُم مِّنْهُم مَّعَرَّةٌۢ بِغَيْرِ عِلْمٍۢ ۖ لِّيُدْخِلَ ٱللَّهُ فِى رَحْمَتِهِۦ مَن يَشَآءُ ۚ لَوْ تَزَيَّلُوا۟ لَعَذَّبْنَا ٱلَّذِينَ كَفَرُوا۟ مِنْهُمْ عَذَابًا أَلِيمًا
- (49:10) [listed for 1:3] إِنَّمَا ٱلْمُؤْمِنُونَ إِخْوَةٌۭ فَأَصْلِحُوا۟ بَيْنَ أَخَوَيْكُمْ ۚ وَٱتَّقُوا۟ ٱللَّهَ لَعَلَّكُمْ تُرْحَمُونَ
- (64:14) [listed for 1:3] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّ مِنْ أَزْوَٰجِكُمْ وَأَوْلَٰدِكُمْ عَدُوًّۭا لَّكُمْ فَٱحْذَرُوهُمْ ۚ وَإِن تَعْفُوا۟ وَتَصْفَحُوا۟ وَتَغْفِرُوا۟ فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌ
- (76:31) [listed for 1:3] يُدْخِلُ مَن يَشَآءُ فِى رَحْمَتِهِۦ ۚ وَٱلظَّٰلِمِينَ أَعَدَّ لَهُمْ عَذَابًا أَلِيمًۢا
- (78:37) [listed for 1:3] [cited in ¶15] رَّبِّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا ٱلرَّحْمَٰنِ ۖ لَا يَمْلِكُونَ مِنْهُ خِطَابًۭا

## named by the passage's own list as strong for this ayah (5)

- (17:110) [listed for 1:3] [cited in ¶5] قُلِ ٱدْعُوا۟ ٱللَّهَ أَوِ ٱدْعُوا۟ ٱلرَّحْمَٰنَ ۖ أَيًّۭا مَّا تَدْعُوا۟ فَلَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ وَلَا تَجْهَرْ بِصَلَاتِكَ وَلَا تُخَافِتْ بِهَا وَٱبْتَغِ بَيْنَ ذَٰلِكَ سَبِيلًۭا
- (25:26) [listed for 1:3] [cited in ¶15] ٱلْمُلْكُ يَوْمَئِذٍ ٱلْحَقُّ لِلرَّحْمَٰنِ ۚ وَكَانَ يَوْمًا عَلَى ٱلْكَٰفِرِينَ عَسِيرًۭا
- (26:9) [listed for 1:3] وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (26:159) [listed for 1:3] وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (41:32) [listed for 1:3] نُزُلًۭا مِّنْ غَفُورٍۢ رَّحِيمٍۢ

## named by the passage's own list as medium for this ayah (45)

- (2:37) [listed for 1:3] فَتَلَقَّىٰٓ ءَادَمُ مِن رَّبِّهِۦ كَلِمَٰتٍۢ فَتَابَ عَلَيْهِ ۚ إِنَّهُۥ هُوَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (2:64) [listed for 1:3] ثُمَّ تَوَلَّيْتُم مِّنۢ بَعْدِ ذَٰلِكَ ۖ فَلَوْلَا فَضْلُ ٱللَّهِ عَلَيْكُمْ وَرَحْمَتُهُۥ لَكُنتُم مِّنَ ٱلْخَٰسِرِينَ
- (3:132) [listed for 1:3] وَأَطِيعُوا۟ ٱللَّهَ وَٱلرَّسُولَ لَعَلَّكُمْ تُرْحَمُونَ
- (4:96) [listed for 1:3] دَرَجَٰتٍۢ مِّنْهُ وَمَغْفِرَةًۭ وَرَحْمَةًۭ ۚ وَكَانَ ٱللَّهُ غَفُورًۭا رَّحِيمًا
- (6:16) [listed for 1:3] مَّن يُصْرَفْ عَنْهُ يَوْمَئِذٍۢ فَقَدْ رَحِمَهُۥ ۚ وَذَٰلِكَ ٱلْفَوْزُ ٱلْمُبِينُ
- (6:154) [listed for 1:3] ثُمَّ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ تَمَامًا عَلَى ٱلَّذِىٓ أَحْسَنَ وَتَفْصِيلًۭا لِّكُلِّ شَىْءٍۢ وَهُدًۭى وَرَحْمَةًۭ لَّعَلَّهُم بِلِقَآءِ رَبِّهِمْ يُؤْمِنُونَ
- (7:49) [listed for 1:3] أَهَٰٓؤُلَآءِ ٱلَّذِينَ أَقْسَمْتُمْ لَا يَنَالُهُمُ ٱللَّهُ بِرَحْمَةٍ ۚ ٱدْخُلُوا۟ ٱلْجَنَّةَ لَا خَوْفٌ عَلَيْكُمْ وَلَآ أَنتُمْ تَحْزَنُونَ
- (7:180) [listed for 1:3] وَلِلَّهِ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ فَٱدْعُوهُ بِهَا ۖ وَذَرُوا۟ ٱلَّذِينَ يُلْحِدُونَ فِىٓ أَسْمَٰٓئِهِۦ ۚ سَيُجْزَوْنَ مَا كَانُوا۟ يَعْمَلُونَ
- (9:27) [listed for 1:3] ثُمَّ يَتُوبُ ٱللَّهُ مِنۢ بَعْدِ ذَٰلِكَ عَلَىٰ مَن يَشَآءُ ۗ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌۭ
- (9:128) [listed for 1:3] [cited in ¶5] لَقَدْ جَآءَكُمْ رَسُولٌۭ مِّنْ أَنفُسِكُمْ عَزِيزٌ عَلَيْهِ مَا عَنِتُّمْ حَرِيصٌ عَلَيْكُم بِٱلْمُؤْمِنِينَ رَءُوفٌۭ رَّحِيمٌۭ
- (10:21) [listed for 1:3] وَإِذَآ أَذَقْنَا ٱلنَّاسَ رَحْمَةًۭ مِّنۢ بَعْدِ ضَرَّآءَ مَسَّتْهُمْ إِذَا لَهُم مَّكْرٌۭ فِىٓ ءَايَاتِنَا ۚ قُلِ ٱللَّهُ أَسْرَعُ مَكْرًا ۚ إِنَّ رُسُلَنَا يَكْتُبُونَ مَا تَمْكُرُونَ
- (10:58) [listed for 1:3] قُلْ بِفَضْلِ ٱللَّهِ وَبِرَحْمَتِهِۦ فَبِذَٰلِكَ فَلْيَفْرَحُوا۟ هُوَ خَيْرٌۭ مِّمَّا يَجْمَعُونَ
- (10:86) [listed for 1:3] وَنَجِّنَا بِرَحْمَتِكَ مِنَ ٱلْقَوْمِ ٱلْكَٰفِرِينَ
- (12:111) [listed for 1:3] لَقَدْ كَانَ فِى قَصَصِهِمْ عِبْرَةٌۭ لِّأُو۟لِى ٱلْأَلْبَٰبِ ۗ مَا كَانَ حَدِيثًۭا يُفْتَرَىٰ وَلَٰكِن تَصْدِيقَ ٱلَّذِى بَيْنَ يَدَيْهِ وَتَفْصِيلَ كُلِّ شَىْءٍۢ وَهُدًۭى وَرَحْمَةًۭ لِّقَوْمٍۢ يُؤْمِنُونَ
- (13:30) [listed for 1:3] كَذَٰلِكَ أَرْسَلْنَٰكَ فِىٓ أُمَّةٍۢ قَدْ خَلَتْ مِن قَبْلِهَآ أُمَمٌۭ لِّتَتْلُوَا۟ عَلَيْهِمُ ٱلَّذِىٓ أَوْحَيْنَآ إِلَيْكَ وَهُمْ يَكْفُرُونَ بِٱلرَّحْمَٰنِ ۚ قُلْ هُوَ رَبِّى لَآ إِلَٰهَ إِلَّا هُوَ عَلَيْهِ تَوَكَّلْتُ وَإِلَيْهِ مَتَابِ
- (15:56) [listed for 1:3] قَالَ وَمَن يَقْنَطُ مِن رَّحْمَةِ رَبِّهِۦٓ إِلَّا ٱلضَّآلُّونَ
- (15:87) [listed for 1:3] وَلَقَدْ ءَاتَيْنَٰكَ سَبْعًۭا مِّنَ ٱلْمَثَانِى وَٱلْقُرْءَانَ ٱلْعَظِيمَ
- (17:66) [listed for 1:3] رَّبُّكُمُ ٱلَّذِى يُزْجِى لَكُمُ ٱلْفُلْكَ فِى ٱلْبَحْرِ لِتَبْتَغُوا۟ مِن فَضْلِهِۦٓ ۚ إِنَّهُۥ كَانَ بِكُمْ رَحِيمًۭا
- (17:100) [listed for 1:3] قُل لَّوْ أَنتُمْ تَمْلِكُونَ خَزَآئِنَ رَحْمَةِ رَبِّىٓ إِذًۭا لَّأَمْسَكْتُمْ خَشْيَةَ ٱلْإِنفَاقِ ۚ وَكَانَ ٱلْإِنسَٰنُ قَتُورًۭا
- (18:81) [listed for 1:3] [cited in ¶14] فَأَرَدْنَآ أَن يُبْدِلَهُمَا رَبُّهُمَا خَيْرًۭا مِّنْهُ زَكَوٰةًۭ وَأَقْرَبَ رُحْمًۭا
- (18:82) [listed for 1:3] [cited in ¶14] وَأَمَّا ٱلْجِدَارُ فَكَانَ لِغُلَٰمَيْنِ يَتِيمَيْنِ فِى ٱلْمَدِينَةِ وَكَانَ تَحْتَهُۥ كَنزٌۭ لَّهُمَا وَكَانَ أَبُوهُمَا صَٰلِحًۭا فَأَرَادَ رَبُّكَ أَن يَبْلُغَآ أَشُدَّهُمَا وَيَسْتَخْرِجَا كَنزَهُمَا رَحْمَةًۭ مِّن رَّبِّكَ ۚ وَمَا فَعَلْتُهُۥ عَنْ أَمْرِى ۚ ذَٰلِكَ تَأْوِيلُ مَا لَمْ تَسْطِع عَّلَيْهِ صَبْرًۭا
- (19:44) [listed for 1:3] يَٰٓأَبَتِ لَا تَعْبُدِ ٱلشَّيْطَٰنَ ۖ إِنَّ ٱلشَّيْطَٰنَ كَانَ لِلرَّحْمَٰنِ عَصِيًّۭا
- (19:50) [listed for 1:3] وَوَهَبْنَا لَهُم مِّن رَّحْمَتِنَا وَجَعَلْنَا لَهُمْ لِسَانَ صِدْقٍ عَلِيًّۭا
- (19:85) [listed for 1:3] يَوْمَ نَحْشُرُ ٱلْمُتَّقِينَ إِلَى ٱلرَّحْمَٰنِ وَفْدًۭا
- (21:83) [listed for 1:3] ۞ وَأَيُّوبَ إِذْ نَادَىٰ رَبَّهُۥٓ أَنِّى مَسَّنِىَ ٱلضُّرُّ وَأَنتَ أَرْحَمُ ٱلرَّٰحِمِينَ
- (26:68) [listed for 1:3] وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (26:122) [listed for 1:3] وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (26:140) [listed for 1:3] وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (26:175) [listed for 1:3] وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (26:191) [listed for 1:3] وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (29:21) [listed for 1:3] يُعَذِّبُ مَن يَشَآءُ وَيَرْحَمُ مَن يَشَآءُ ۖ وَإِلَيْهِ تُقْلَبُونَ
- (29:23) [listed for 1:3] وَٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِ ٱللَّهِ وَلِقَآئِهِۦٓ أُو۟لَٰٓئِكَ يَئِسُوا۟ مِن رَّحْمَتِى وَأُو۟لَٰٓئِكَ لَهُمْ عَذَابٌ أَلِيمٌۭ
- (32:6) [listed for 1:3] ذَٰلِكَ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (35:2) [listed for 1:3] مَّا يَفْتَحِ ٱللَّهُ لِلنَّاسِ مِن رَّحْمَةٍۢ فَلَا مُمْسِكَ لَهَا ۖ وَمَا يُمْسِكْ فَلَا مُرْسِلَ لَهُۥ مِنۢ بَعْدِهِۦ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (36:52) [listed for 1:3] قَالُوا۟ يَٰوَيْلَنَا مَنۢ بَعَثَنَا مِن مَّرْقَدِنَا ۜ ۗ هَٰذَا مَا وَعَدَ ٱلرَّحْمَٰنُ وَصَدَقَ ٱلْمُرْسَلُونَ
- (38:9) [listed for 1:3] أَمْ عِندَهُمْ خَزَآئِنُ رَحْمَةِ رَبِّكَ ٱلْعَزِيزِ ٱلْوَهَّابِ
- (43:81) [listed for 1:3] قُلْ إِن كَانَ لِلرَّحْمَٰنِ وَلَدٌۭ فَأَنَا۠ أَوَّلُ ٱلْعَٰبِدِينَ
- (45:20) [listed for 1:3] هَٰذَا بَصَٰٓئِرُ لِلنَّاسِ وَهُدًۭى وَرَحْمَةٌۭ لِّقَوْمٍۢ يُوقِنُونَ
- (52:28) [listed for 1:3] إِنَّا كُنَّا مِن قَبْلُ نَدْعُوهُ ۖ إِنَّهُۥ هُوَ ٱلْبَرُّ ٱلرَّحِيمُ
- (67:19) [listed for 1:3] [cited in ¶5] أَوَلَمْ يَرَوْا۟ إِلَى ٱلطَّيْرِ فَوْقَهُمْ صَٰٓفَّٰتٍۢ وَيَقْبِضْنَ ۚ مَا يُمْسِكُهُنَّ إِلَّا ٱلرَّحْمَٰنُ ۚ إِنَّهُۥ بِكُلِّ شَىْءٍۭ بَصِيرٌ
- (67:20) [listed for 1:3] أَمَّنْ هَٰذَا ٱلَّذِى هُوَ جُندٌۭ لَّكُمْ يَنصُرُكُم مِّن دُونِ ٱلرَّحْمَٰنِ ۚ إِنِ ٱلْكَٰفِرُونَ إِلَّا فِى غُرُورٍ
- (67:29) [listed for 1:3] قُلْ هُوَ ٱلرَّحْمَٰنُ ءَامَنَّا بِهِۦ وَعَلَيْهِ تَوَكَّلْنَا ۖ فَسَتَعْلَمُونَ مَنْ هُوَ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (78:36) [listed for 1:3] جَزَآءًۭ مِّن رَّبِّكَ عَطَآءً حِسَابًۭا
- (85:14) [listed for 1:3] وَهُوَ ٱلْغَفُورُ ٱلْوَدُودُ
- (85:15) [listed for 1:3] ذُو ٱلْعَرْشِ ٱلْمَجِيدُ

## weak (this ayah's own list) (24)

- (2:54) [listed for 1:3] وَإِذْ قَالَ مُوسَىٰ لِقَوْمِهِۦ يَٰقَوْمِ إِنَّكُمْ ظَلَمْتُمْ أَنفُسَكُم بِٱتِّخَاذِكُمُ ٱلْعِجْلَ فَتُوبُوٓا۟ إِلَىٰ بَارِئِكُمْ فَٱقْتُلُوٓا۟ أَنفُسَكُمْ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ عِندَ بَارِئِكُمْ فَتَابَ عَلَيْكُمْ ۚ إِنَّهُۥ هُوَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (2:128) [listed for 1:3] رَبَّنَا وَٱجْعَلْنَا مُسْلِمَيْنِ لَكَ وَمِن ذُرِّيَّتِنَآ أُمَّةًۭ مُّسْلِمَةًۭ لَّكَ وَأَرِنَا مَنَاسِكَنَا وَتُبْ عَلَيْنَآ ۖ إِنَّكَ أَنتَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (2:143) [listed for 1:3] وَكَذَٰلِكَ جَعَلْنَٰكُمْ أُمَّةًۭ وَسَطًۭا لِّتَكُونُوا۟ شُهَدَآءَ عَلَى ٱلنَّاسِ وَيَكُونَ ٱلرَّسُولُ عَلَيْكُمْ شَهِيدًۭا ۗ وَمَا جَعَلْنَا ٱلْقِبْلَةَ ٱلَّتِى كُنتَ عَلَيْهَآ إِلَّا لِنَعْلَمَ مَن يَتَّبِعُ ٱلرَّسُولَ مِمَّن يَنقَلِبُ عَلَىٰ عَقِبَيْهِ ۚ وَإِن كَانَتْ لَكَبِيرَةً إِلَّا عَلَى ٱلَّذِينَ هَدَى ٱللَّهُ ۗ وَمَا كَانَ ٱللَّهُ لِيُضِيعَ إِيمَٰنَكُمْ ۚ إِنَّ ٱللَّهَ بِٱلنَّاسِ لَرَءُوفٌۭ رَّحِيمٌۭ
- (2:160) [listed for 1:3] إِلَّا ٱلَّذِينَ تَابُوا۟ وَأَصْلَحُوا۟ وَبَيَّنُوا۟ فَأُو۟لَٰٓئِكَ أَتُوبُ عَلَيْهِمْ ۚ وَأَنَا ٱلتَّوَّابُ ٱلرَّحِيمُ
- (2:192) [listed for 1:3] فَإِنِ ٱنتَهَوْا۟ فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (2:218) [listed for 1:3] إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَٱلَّذِينَ هَاجَرُوا۟ وَجَٰهَدُوا۟ فِى سَبِيلِ ٱللَّهِ أُو۟لَٰٓئِكَ يَرْجُونَ رَحْمَتَ ٱللَّهِ ۚ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌۭ
- (3:6) [listed for 1:3] [cited in ¶8] هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (3:89) [listed for 1:3] إِلَّا ٱلَّذِينَ تَابُوا۟ مِنۢ بَعْدِ ذَٰلِكَ وَأَصْلَحُوا۟ فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌ
- (4:23) [listed for 1:3] حُرِّمَتْ عَلَيْكُمْ أُمَّهَٰتُكُمْ وَبَنَاتُكُمْ وَأَخَوَٰتُكُمْ وَعَمَّٰتُكُمْ وَخَٰلَٰتُكُمْ وَبَنَاتُ ٱلْأَخِ وَبَنَاتُ ٱلْأُخْتِ وَأُمَّهَٰتُكُمُ ٱلَّٰتِىٓ أَرْضَعْنَكُمْ وَأَخَوَٰتُكُم مِّنَ ٱلرَّضَٰعَةِ وَأُمَّهَٰتُ نِسَآئِكُمْ وَرَبَٰٓئِبُكُمُ ٱلَّٰتِى فِى حُجُورِكُم مِّن نِّسَآئِكُمُ ٱلَّٰتِى دَخَلْتُم بِهِنَّ فَإِن لَّمْ تَكُونُوا۟ دَخَلْتُم بِهِنَّ فَلَا جُنَاحَ عَلَيْكُمْ وَحَلَٰٓئِلُ أَبْنَآئِكُمُ ٱلَّذِينَ مِنْ أَصْلَٰبِكُمْ وَأَن تَجْمَعُوا۟ بَيْنَ ٱلْأُخْتَيْنِ إِلَّا مَا قَدْ سَلَفَ ۗ إِنَّ ٱللَّهَ كَانَ غَفُورًۭا رَّحِيمًۭا
- (4:32) [listed for 1:3] وَلَا تَتَمَنَّوْا۟ مَا فَضَّلَ ٱللَّهُ بِهِۦ بَعْضَكُمْ عَلَىٰ بَعْضٍۢ ۚ لِّلرِّجَالِ نَصِيبٌۭ مِّمَّا ٱكْتَسَبُوا۟ ۖ وَلِلنِّسَآءِ نَصِيبٌۭ مِّمَّا ٱكْتَسَبْنَ ۚ وَسْـَٔلُوا۟ ٱللَّهَ مِن فَضْلِهِۦٓ ۗ إِنَّ ٱللَّهَ كَانَ بِكُلِّ شَىْءٍ عَلِيمًۭا
- (5:74) [listed for 1:3] أَفَلَا يَتُوبُونَ إِلَى ٱللَّهِ وَيَسْتَغْفِرُونَهُۥ ۚ وَٱللَّهُ غَفُورٌۭ رَّحِيمٌۭ
- (7:57) [listed for 1:3] [cited in ¶12] وَهُوَ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۖ حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًۭا ثِقَالًۭا سُقْنَٰهُ لِبَلَدٍۢ مَّيِّتٍۢ فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ
- (9:104) [listed for 1:3] أَلَمْ يَعْلَمُوٓا۟ أَنَّ ٱللَّهَ هُوَ يَقْبَلُ ٱلتَّوْبَةَ عَنْ عِبَادِهِۦ وَيَأْخُذُ ٱلصَّدَقَٰتِ وَأَنَّ ٱللَّهَ هُوَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (9:118) [listed for 1:3] وَعَلَى ٱلثَّلَٰثَةِ ٱلَّذِينَ خُلِّفُوا۟ حَتَّىٰٓ إِذَا ضَاقَتْ عَلَيْهِمُ ٱلْأَرْضُ بِمَا رَحُبَتْ وَضَاقَتْ عَلَيْهِمْ أَنفُسُهُمْ وَظَنُّوٓا۟ أَن لَّا مَلْجَأَ مِنَ ٱللَّهِ إِلَّآ إِلَيْهِ ثُمَّ تَابَ عَلَيْهِمْ لِيَتُوبُوٓا۟ ۚ إِنَّ ٱللَّهَ هُوَ ٱلتَّوَّابُ ٱلرَّحِيمُ
- (19:69) [listed for 1:3] ثُمَّ لَنَنزِعَنَّ مِن كُلِّ شِيعَةٍ أَيُّهُمْ أَشَدُّ عَلَى ٱلرَّحْمَٰنِ عِتِيًّۭا
- (19:88) [listed for 1:3] وَقَالُوا۟ ٱتَّخَذَ ٱلرَّحْمَٰنُ وَلَدًۭا
- (21:26) [listed for 1:3] وَقَالُوا۟ ٱتَّخَذَ ٱلرَّحْمَٰنُ وَلَدًۭا ۗ سُبْحَٰنَهُۥ ۚ بَلْ عِبَادٌۭ مُّكْرَمُونَ
- (21:86) [listed for 1:3] وَأَدْخَلْنَٰهُمْ فِى رَحْمَتِنَآ ۖ إِنَّهُم مِّنَ ٱلصَّٰلِحِينَ
- (23:76) [listed for 1:3] وَلَقَدْ أَخَذْنَٰهُم بِٱلْعَذَابِ فَمَا ٱسْتَكَانُوا۟ لِرَبِّهِمْ وَمَا يَتَضَرَّعُونَ
- (28:16) [listed for 1:3] قَالَ رَبِّ إِنِّى ظَلَمْتُ نَفْسِى فَٱغْفِرْ لِى فَغَفَرَ لَهُۥٓ ۚ إِنَّهُۥ هُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- (36:23) [listed for 1:3] ءَأَتَّخِذُ مِن دُونِهِۦٓ ءَالِهَةً إِن يُرِدْنِ ٱلرَّحْمَٰنُ بِضُرٍّۢ لَّا تُغْنِ عَنِّى شَفَٰعَتُهُمْ شَيْـًۭٔا وَلَا يُنقِذُونِ
- (42:5) [listed for 1:3] تَكَادُ ٱلسَّمَٰوَٰتُ يَتَفَطَّرْنَ مِن فَوْقِهِنَّ ۚ وَٱلْمَلَٰٓئِكَةُ يُسَبِّحُونَ بِحَمْدِ رَبِّهِمْ وَيَسْتَغْفِرُونَ لِمَن فِى ٱلْأَرْضِ ۗ أَلَآ إِنَّ ٱللَّهَ هُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- (43:17) [listed for 1:3] وَإِذَا بُشِّرَ أَحَدُهُم بِمَا ضَرَبَ لِلرَّحْمَٰنِ مَثَلًۭا ظَلَّ وَجْهُهُۥ مُسْوَدًّۭا وَهُوَ كَظِيمٌ
- (67:3) [listed for 1:3] [cited in ¶5] ٱلَّذِى خَلَقَ سَبْعَ سَمَٰوَٰتٍۢ طِبَاقًۭا ۖ مَّا تَرَىٰ فِى خَلْقِ ٱلرَّحْمَٰنِ مِن تَفَٰوُتٍۢ ۖ فَٱرْجِعِ ٱلْبَصَرَ هَلْ تَرَىٰ مِن فُطُورٍۢ

## named by the passage's own list as weak for this ayah (51)

- (2:105) [listed for 1:3] مَّا يَوَدُّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَلَا ٱلْمُشْرِكِينَ أَن يُنَزَّلَ عَلَيْكُم مِّنْ خَيْرٍۢ مِّن رَّبِّكُمْ ۗ وَٱللَّهُ يَخْتَصُّ بِرَحْمَتِهِۦ مَن يَشَآءُ ۚ وَٱللَّهُ ذُو ٱلْفَضْلِ ٱلْعَظِيمِ
- (3:107) [listed for 1:3] وَأَمَّا ٱلَّذِينَ ٱبْيَضَّتْ وُجُوهُهُمْ فَفِى رَحْمَةِ ٱللَّهِ هُمْ فِيهَا خَٰلِدُونَ
- (4:83) [listed for 1:3] وَإِذَا جَآءَهُمْ أَمْرٌۭ مِّنَ ٱلْأَمْنِ أَوِ ٱلْخَوْفِ أَذَاعُوا۟ بِهِۦ ۖ وَلَوْ رَدُّوهُ إِلَى ٱلرَّسُولِ وَإِلَىٰٓ أُو۟لِى ٱلْأَمْرِ مِنْهُمْ لَعَلِمَهُ ٱلَّذِينَ يَسْتَنۢبِطُونَهُۥ مِنْهُمْ ۗ وَلَوْلَا فَضْلُ ٱللَّهِ عَلَيْكُمْ وَرَحْمَتُهُۥ لَٱتَّبَعْتُمُ ٱلشَّيْطَٰنَ إِلَّا قَلِيلًۭا
- (6:133) [listed for 1:3] وَرَبُّكَ ٱلْغَنِىُّ ذُو ٱلرَّحْمَةِ ۚ إِن يَشَأْ يُذْهِبْكُمْ وَيَسْتَخْلِفْ مِنۢ بَعْدِكُم مَّا يَشَآءُ كَمَآ أَنشَأَكُم مِّن ذُرِّيَّةِ قَوْمٍ ءَاخَرِينَ
- (7:72) [listed for 1:3] فَأَنجَيْنَٰهُ وَٱلَّذِينَ مَعَهُۥ بِرَحْمَةٍۢ مِّنَّا وَقَطَعْنَا دَابِرَ ٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِنَا ۖ وَمَا كَانُوا۟ مُؤْمِنِينَ
- (7:153) [listed for 1:3] وَٱلَّذِينَ عَمِلُوا۟ ٱلسَّيِّـَٔاتِ ثُمَّ تَابُوا۟ مِنۢ بَعْدِهَا وَءَامَنُوٓا۟ إِنَّ رَبَّكَ مِنۢ بَعْدِهَا لَغَفُورٌۭ رَّحِيمٌۭ
- (7:154) [listed for 1:3] وَلَمَّا سَكَتَ عَن مُّوسَى ٱلْغَضَبُ أَخَذَ ٱلْأَلْوَاحَ ۖ وَفِى نُسْخَتِهَا هُدًۭى وَرَحْمَةٌۭ لِّلَّذِينَ هُمْ لِرَبِّهِمْ يَرْهَبُونَ
- (7:203) [listed for 1:3] وَإِذَا لَمْ تَأْتِهِم بِـَٔايَةٍۢ قَالُوا۟ لَوْلَا ٱجْتَبَيْتَهَا ۚ قُلْ إِنَّمَآ أَتَّبِعُ مَا يُوحَىٰٓ إِلَىَّ مِن رَّبِّى ۚ هَٰذَا بَصَآئِرُ مِن رَّبِّكُمْ وَهُدًۭى وَرَحْمَةٌۭ لِّقَوْمٍۢ يُؤْمِنُونَ
- (7:204) [listed for 1:3] وَإِذَا قُرِئَ ٱلْقُرْءَانُ فَٱسْتَمِعُوا۟ لَهُۥ وَأَنصِتُوا۟ لَعَلَّكُمْ تُرْحَمُونَ
- (9:61) [listed for 1:3] وَمِنْهُمُ ٱلَّذِينَ يُؤْذُونَ ٱلنَّبِىَّ وَيَقُولُونَ هُوَ أُذُنٌۭ ۚ قُلْ أُذُنُ خَيْرٍۢ لَّكُمْ يُؤْمِنُ بِٱللَّهِ وَيُؤْمِنُ لِلْمُؤْمِنِينَ وَرَحْمَةٌۭ لِّلَّذِينَ ءَامَنُوا۟ مِنكُمْ ۚ وَٱلَّذِينَ يُؤْذُونَ رَسُولَ ٱللَّهِ لَهُمْ عَذَابٌ أَلِيمٌۭ
- (9:117) [listed for 1:3] لَّقَد تَّابَ ٱللَّهُ عَلَى ٱلنَّبِىِّ وَٱلْمُهَٰجِرِينَ وَٱلْأَنصَارِ ٱلَّذِينَ ٱتَّبَعُوهُ فِى سَاعَةِ ٱلْعُسْرَةِ مِنۢ بَعْدِ مَا كَادَ يَزِيغُ قُلُوبُ فَرِيقٍۢ مِّنْهُمْ ثُمَّ تَابَ عَلَيْهِمْ ۚ إِنَّهُۥ بِهِمْ رَءُوفٌۭ رَّحِيمٌۭ
- (11:90) [listed for 1:3] وَٱسْتَغْفِرُوا۟ رَبَّكُمْ ثُمَّ تُوبُوٓا۟ إِلَيْهِ ۚ إِنَّ رَبِّى رَحِيمٌۭ وَدُودٌۭ
- (16:7) [listed for 1:3] وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ ۚ إِنَّ رَبَّكُمْ لَرَءُوفٌۭ رَّحِيمٌۭ
- (17:24) [listed for 1:3] وَٱخْفِضْ لَهُمَا جَنَاحَ ٱلذُّلِّ مِنَ ٱلرَّحْمَةِ وَقُل رَّبِّ ٱرْحَمْهُمَا كَمَا رَبَّيَانِى صَغِيرًۭا
- (18:98) [listed for 1:3] قَالَ هَٰذَا رَحْمَةٌۭ مِّن رَّبِّى ۖ فَإِذَا جَآءَ وَعْدُ رَبِّى جَعَلَهُۥ دَكَّآءَ ۖ وَكَانَ وَعْدُ رَبِّى حَقًّۭا
- (19:18) [listed for 1:3] قَالَتْ إِنِّىٓ أَعُوذُ بِٱلرَّحْمَٰنِ مِنكَ إِن كُنتَ تَقِيًّۭا
- (19:45) [listed for 1:3] [cited in ¶17] يَٰٓأَبَتِ إِنِّىٓ أَخَافُ أَن يَمَسَّكَ عَذَابٌۭ مِّنَ ٱلرَّحْمَٰنِ فَتَكُونَ لِلشَّيْطَٰنِ وَلِيًّۭا
- (19:53) [listed for 1:3] وَوَهَبْنَا لَهُۥ مِن رَّحْمَتِنَآ أَخَاهُ هَٰرُونَ نَبِيًّۭا
- (19:78) [listed for 1:3] أَطَّلَعَ ٱلْغَيْبَ أَمِ ٱتَّخَذَ عِندَ ٱلرَّحْمَٰنِ عَهْدًۭا
- (19:91) [listed for 1:3] أَن دَعَوْا۟ لِلرَّحْمَٰنِ وَلَدًۭا
- (19:92) [listed for 1:3] وَمَا يَنۢبَغِى لِلرَّحْمَٰنِ أَن يَتَّخِذَ وَلَدًا
- (19:93) [listed for 1:3] [cited in ¶18] إِن كُلُّ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ إِلَّآ ءَاتِى ٱلرَّحْمَٰنِ عَبْدًۭا
- (20:108) [listed for 1:3] [cited in ¶15] يَوْمَئِذٍۢ يَتَّبِعُونَ ٱلدَّاعِىَ لَا عِوَجَ لَهُۥ ۖ وَخَشَعَتِ ٱلْأَصْوَاتُ لِلرَّحْمَٰنِ فَلَا تَسْمَعُ إِلَّا هَمْسًۭا
- (24:56) [listed for 1:3] وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَأَطِيعُوا۟ ٱلرَّسُولَ لَعَلَّكُمْ تُرْحَمُونَ
- (25:6) [listed for 1:3] قُلْ أَنزَلَهُ ٱلَّذِى يَعْلَمُ ٱلسِّرَّ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ إِنَّهُۥ كَانَ غَفُورًۭا رَّحِيمًۭا
- (25:48) [listed for 1:3] وَهُوَ ٱلَّذِىٓ أَرْسَلَ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۚ وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ طَهُورًۭا
- (26:5) [listed for 1:3] وَمَا يَأْتِيهِم مِّن ذِكْرٍۢ مِّنَ ٱلرَّحْمَٰنِ مُحْدَثٍ إِلَّا كَانُوا۟ عَنْهُ مُعْرِضِينَ
- (27:77) [listed for 1:3] وَإِنَّهُۥ لَهُدًۭى وَرَحْمَةٌۭ لِّلْمُؤْمِنِينَ
- (28:43) [listed for 1:3] وَلَقَدْ ءَاتَيْنَا مُوسَى ٱلْكِتَٰبَ مِنۢ بَعْدِ مَآ أَهْلَكْنَا ٱلْقُرُونَ ٱلْأُولَىٰ بَصَآئِرَ لِلنَّاسِ وَهُدًۭى وَرَحْمَةًۭ لَّعَلَّهُمْ يَتَذَكَّرُونَ
- (29:51) [listed for 1:3] أَوَلَمْ يَكْفِهِمْ أَنَّآ أَنزَلْنَا عَلَيْكَ ٱلْكِتَٰبَ يُتْلَىٰ عَلَيْهِمْ ۚ إِنَّ فِى ذَٰلِكَ لَرَحْمَةًۭ وَذِكْرَىٰ لِقَوْمٍۢ يُؤْمِنُونَ
- (30:33) [listed for 1:3] وَإِذَا مَسَّ ٱلنَّاسَ ضُرٌّۭ دَعَوْا۟ رَبَّهُم مُّنِيبِينَ إِلَيْهِ ثُمَّ إِذَآ أَذَاقَهُم مِّنْهُ رَحْمَةً إِذَا فَرِيقٌۭ مِّنْهُم بِرَبِّهِمْ يُشْرِكُونَ
- (30:50) [listed for 1:3] [cited in ¶12] فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ ذَٰلِكَ لَمُحْىِ ٱلْمَوْتَىٰ ۖ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (31:3) [listed for 1:3] هُدًۭى وَرَحْمَةًۭ لِّلْمُحْسِنِينَ
- (33:59) [listed for 1:3] يَٰٓأَيُّهَا ٱلنَّبِىُّ قُل لِّأَزْوَٰجِكَ وَبَنَاتِكَ وَنِسَآءِ ٱلْمُؤْمِنِينَ يُدْنِينَ عَلَيْهِنَّ مِن جَلَٰبِيبِهِنَّ ۚ ذَٰلِكَ أَدْنَىٰٓ أَن يُعْرَفْنَ فَلَا يُؤْذَيْنَ ۗ وَكَانَ ٱللَّهُ غَفُورًۭا رَّحِيمًۭا
- (36:15) [listed for 1:3] قَالُوا۟ مَآ أَنتُمْ إِلَّا بَشَرٌۭ مِّثْلُنَا وَمَآ أَنزَلَ ٱلرَّحْمَٰنُ مِن شَىْءٍ إِنْ أَنتُمْ إِلَّا تَكْذِبُونَ
- (36:44) [listed for 1:3] إِلَّا رَحْمَةًۭ مِّنَّا وَمَتَٰعًا إِلَىٰ حِينٍۢ
- (36:45) [listed for 1:3] وَإِذَا قِيلَ لَهُمُ ٱتَّقُوا۟ مَا بَيْنَ أَيْدِيكُمْ وَمَا خَلْفَكُمْ لَعَلَّكُمْ تُرْحَمُونَ
- (36:51) [listed for 1:3] وَنُفِخَ فِى ٱلصُّورِ فَإِذَا هُم مِّنَ ٱلْأَجْدَاثِ إِلَىٰ رَبِّهِمْ يَنسِلُونَ
- (38:43) [listed for 1:3] وَوَهَبْنَا لَهُۥٓ أَهْلَهُۥ وَمِثْلَهُم مَّعَهُمْ رَحْمَةًۭ مِّنَّا وَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
- (39:38) [listed for 1:3] وَلَئِن سَأَلْتَهُم مَّنْ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ لَيَقُولُنَّ ٱللَّهُ ۚ قُلْ أَفَرَءَيْتُم مَّا تَدْعُونَ مِن دُونِ ٱللَّهِ إِنْ أَرَادَنِىَ ٱللَّهُ بِضُرٍّ هَلْ هُنَّ كَٰشِفَٰتُ ضُرِّهِۦٓ أَوْ أَرَادَنِى بِرَحْمَةٍ هَلْ هُنَّ مُمْسِكَٰتُ رَحْمَتِهِۦ ۚ قُلْ حَسْبِىَ ٱللَّهُ ۖ عَلَيْهِ يَتَوَكَّلُ ٱلْمُتَوَكِّلُونَ
- (40:9) [listed for 1:3] وَقِهِمُ ٱلسَّيِّـَٔاتِ ۚ وَمَن تَقِ ٱلسَّيِّـَٔاتِ يَوْمَئِذٍۢ فَقَدْ رَحِمْتَهُۥ ۚ وَذَٰلِكَ هُوَ ٱلْفَوْزُ ٱلْعَظِيمُ
- (41:50) [listed for 1:3] وَلَئِنْ أَذَقْنَٰهُ رَحْمَةًۭ مِّنَّا مِنۢ بَعْدِ ضَرَّآءَ مَسَّتْهُ لَيَقُولَنَّ هَٰذَا لِى وَمَآ أَظُنُّ ٱلسَّاعَةَ قَآئِمَةًۭ وَلَئِن رُّجِعْتُ إِلَىٰ رَبِّىٓ إِنَّ لِى عِندَهُۥ لَلْحُسْنَىٰ ۚ فَلَنُنَبِّئَنَّ ٱلَّذِينَ كَفَرُوا۟ بِمَا عَمِلُوا۟ وَلَنُذِيقَنَّهُم مِّنْ عَذَابٍ غَلِيظٍۢ
- (42:48) [listed for 1:3] فَإِنْ أَعْرَضُوا۟ فَمَآ أَرْسَلْنَٰكَ عَلَيْهِمْ حَفِيظًا ۖ إِنْ عَلَيْكَ إِلَّا ٱلْبَلَٰغُ ۗ وَإِنَّآ إِذَآ أَذَقْنَا ٱلْإِنسَٰنَ مِنَّا رَحْمَةًۭ فَرِحَ بِهَا ۖ وَإِن تُصِبْهُمْ سَيِّئَةٌۢ بِمَا قَدَّمَتْ أَيْدِيهِمْ فَإِنَّ ٱلْإِنسَٰنَ كَفُورٌۭ
- (43:32) [listed for 1:3] أَهُمْ يَقْسِمُونَ رَحْمَتَ رَبِّكَ ۚ نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَرَفَعْنَا بَعْضَهُمْ فَوْقَ بَعْضٍۢ دَرَجَٰتٍۢ لِّيَتَّخِذَ بَعْضُهُم بَعْضًۭا سُخْرِيًّۭا ۗ وَرَحْمَتُ رَبِّكَ خَيْرٌۭ مِّمَّا يَجْمَعُونَ
- (46:8) [listed for 1:3] أَمْ يَقُولُونَ ٱفْتَرَىٰهُ ۖ قُلْ إِنِ ٱفْتَرَيْتُهُۥ فَلَا تَمْلِكُونَ لِى مِنَ ٱللَّهِ شَيْـًٔا ۖ هُوَ أَعْلَمُ بِمَا تُفِيضُونَ فِيهِ ۖ كَفَىٰ بِهِۦ شَهِيدًۢا بَيْنِى وَبَيْنَكُمْ ۖ وَهُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- (47:22) [listed for 1:3] [cited in ¶9] فَهَلْ عَسَيْتُمْ إِن تَوَلَّيْتُمْ أَن تُفْسِدُوا۟ فِى ٱلْأَرْضِ وَتُقَطِّعُوٓا۟ أَرْحَامَكُمْ
- (50:33) [listed for 1:3] مَّنْ خَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ وَجَآءَ بِقَلْبٍۢ مُّنِيبٍ
- (57:27) [listed for 1:3] ثُمَّ قَفَّيْنَا عَلَىٰٓ ءَاثَٰرِهِم بِرُسُلِنَا وَقَفَّيْنَا بِعِيسَى ٱبْنِ مَرْيَمَ وَءَاتَيْنَٰهُ ٱلْإِنجِيلَ وَجَعَلْنَا فِى قُلُوبِ ٱلَّذِينَ ٱتَّبَعُوهُ رَأْفَةًۭ وَرَحْمَةًۭ وَرَهْبَانِيَّةً ٱبْتَدَعُوهَا مَا كَتَبْنَٰهَا عَلَيْهِمْ إِلَّا ٱبْتِغَآءَ رِضْوَٰنِ ٱللَّهِ فَمَا رَعَوْهَا حَقَّ رِعَايَتِهَا ۖ فَـَٔاتَيْنَا ٱلَّذِينَ ءَامَنُوا۟ مِنْهُمْ أَجْرَهُمْ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
- (60:12) [listed for 1:3] يَٰٓأَيُّهَا ٱلنَّبِىُّ إِذَا جَآءَكَ ٱلْمُؤْمِنَٰتُ يُبَايِعْنَكَ عَلَىٰٓ أَن لَّا يُشْرِكْنَ بِٱللَّهِ شَيْـًۭٔا وَلَا يَسْرِقْنَ وَلَا يَزْنِينَ وَلَا يَقْتُلْنَ أَوْلَٰدَهُنَّ وَلَا يَأْتِينَ بِبُهْتَٰنٍۢ يَفْتَرِينَهُۥ بَيْنَ أَيْدِيهِنَّ وَأَرْجُلِهِنَّ وَلَا يَعْصِينَكَ فِى مَعْرُوفٍۢ ۙ فَبَايِعْهُنَّ وَٱسْتَغْفِرْ لَهُنَّ ٱللَّهَ ۖ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (78:39) [listed for 1:3] ذَٰلِكَ ٱلْيَوْمُ ٱلْحَقُّ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ مَـَٔابًا
- (112:2) [listed for 1:3] ٱللَّهُ ٱلصَّمَدُ

## neighbours: within two ayat of a passage the commentary cites (107)

- (3:4) [next to 3:6] مِن قَبْلُ هُدًۭى لِّلنَّاسِ وَأَنزَلَ ٱلْفُرْقَانَ ۗ إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِ ٱللَّهِ لَهُمْ عَذَابٌۭ شَدِيدٌۭ ۗ وَٱللَّهُ عَزِيزٌۭ ذُو ٱنتِقَامٍ
- (3:5) [next to 3:6] إِنَّ ٱللَّهَ لَا يَخْفَىٰ عَلَيْهِ شَىْءٌۭ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ
- (3:7) [next to 3:6] هُوَ ٱلَّذِىٓ أَنزَلَ عَلَيْكَ ٱلْكِتَٰبَ مِنْهُ ءَايَٰتٌۭ مُّحْكَمَٰتٌ هُنَّ أُمُّ ٱلْكِتَٰبِ وَأُخَرُ مُتَشَٰبِهَٰتٌۭ ۖ فَأَمَّا ٱلَّذِينَ فِى قُلُوبِهِمْ زَيْغٌۭ فَيَتَّبِعُونَ مَا تَشَٰبَهَ مِنْهُ ٱبْتِغَآءَ ٱلْفِتْنَةِ وَٱبْتِغَآءَ تَأْوِيلِهِۦ ۗ وَمَا يَعْلَمُ تَأْوِيلَهُۥٓ إِلَّا ٱللَّهُ ۗ وَٱلرَّٰسِخُونَ فِى ٱلْعِلْمِ يَقُولُونَ ءَامَنَّا بِهِۦ كُلٌّۭ مِّنْ عِندِ رَبِّنَا ۗ وَمَا يَذَّكَّرُ إِلَّآ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
- (4:0) [next to 4:1] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (4:3) [next to 4:1] وَإِنْ خِفْتُمْ أَلَّا تُقْسِطُوا۟ فِى ٱلْيَتَٰمَىٰ فَٱنكِحُوا۟ مَا طَابَ لَكُم مِّنَ ٱلنِّسَآءِ مَثْنَىٰ وَثُلَٰثَ وَرُبَٰعَ ۖ فَإِنْ خِفْتُمْ أَلَّا تَعْدِلُوا۟ فَوَٰحِدَةً أَوْ مَا مَلَكَتْ أَيْمَٰنُكُمْ ۚ ذَٰلِكَ أَدْنَىٰٓ أَلَّا تَعُولُوا۟
- (6:10) [next to 6:12] وَلَقَدِ ٱسْتُهْزِئَ بِرُسُلٍۢ مِّن قَبْلِكَ فَحَاقَ بِٱلَّذِينَ سَخِرُوا۟ مِنْهُم مَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ
- (6:11) [next to 6:12] قُلْ سِيرُوا۟ فِى ٱلْأَرْضِ ثُمَّ ٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ
- (6:13) [next to 6:12] ۞ وَلَهُۥ مَا سَكَنَ فِى ٱلَّيْلِ وَٱلنَّهَارِ ۚ وَهُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (6:14) [next to 6:12] قُلْ أَغَيْرَ ٱللَّهِ أَتَّخِذُ وَلِيًّۭا فَاطِرِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَهُوَ يُطْعِمُ وَلَا يُطْعَمُ ۗ قُلْ إِنِّىٓ أُمِرْتُ أَنْ أَكُونَ أَوَّلَ مَنْ أَسْلَمَ ۖ وَلَا تَكُونَنَّ مِنَ ٱلْمُشْرِكِينَ
- (7:55) [next to 7:57] ٱدْعُوا۟ رَبَّكُمْ تَضَرُّعًۭا وَخُفْيَةً ۚ إِنَّهُۥ لَا يُحِبُّ ٱلْمُعْتَدِينَ
- (7:58) [next to 7:57] وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ ۖ وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًۭا ۚ كَذَٰلِكَ نُصَرِّفُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَشْكُرُونَ
- (7:59) [next to 7:57] لَقَدْ أَرْسَلْنَا نُوحًا إِلَىٰ قَوْمِهِۦ فَقَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥٓ إِنِّىٓ أَخَافُ عَلَيْكُمْ عَذَابَ يَوْمٍ عَظِيمٍۢ
- (7:157) [next to 7:155] ٱلَّذِينَ يَتَّبِعُونَ ٱلرَّسُولَ ٱلنَّبِىَّ ٱلْأُمِّىَّ ٱلَّذِى يَجِدُونَهُۥ مَكْتُوبًا عِندَهُمْ فِى ٱلتَّوْرَىٰةِ وَٱلْإِنجِيلِ يَأْمُرُهُم بِٱلْمَعْرُوفِ وَيَنْهَىٰهُمْ عَنِ ٱلْمُنكَرِ وَيُحِلُّ لَهُمُ ٱلطَّيِّبَٰتِ وَيُحَرِّمُ عَلَيْهِمُ ٱلْخَبَٰٓئِثَ وَيَضَعُ عَنْهُمْ إِصْرَهُمْ وَٱلْأَغْلَٰلَ ٱلَّتِى كَانَتْ عَلَيْهِمْ ۚ فَٱلَّذِينَ ءَامَنُوا۟ بِهِۦ وَعَزَّرُوهُ وَنَصَرُوهُ وَٱتَّبَعُوا۟ ٱلنُّورَ ٱلَّذِىٓ أُنزِلَ مَعَهُۥٓ ۙ أُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (7:158) [next to 7:156] قُلْ يَٰٓأَيُّهَا ٱلنَّاسُ إِنِّى رَسُولُ ٱللَّهِ إِلَيْكُمْ جَمِيعًا ٱلَّذِى لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ لَآ إِلَٰهَ إِلَّا هُوَ يُحْىِۦ وَيُمِيتُ ۖ فَـَٔامِنُوا۟ بِٱللَّهِ وَرَسُولِهِ ٱلنَّبِىِّ ٱلْأُمِّىِّ ٱلَّذِى يُؤْمِنُ بِٱللَّهِ وَكَلِمَٰتِهِۦ وَٱتَّبِعُوهُ لَعَلَّكُمْ تَهْتَدُونَ
- (9:126) [next to 9:128] أَوَلَا يَرَوْنَ أَنَّهُمْ يُفْتَنُونَ فِى كُلِّ عَامٍۢ مَّرَّةً أَوْ مَرَّتَيْنِ ثُمَّ لَا يَتُوبُونَ وَلَا هُمْ يَذَّكَّرُونَ
- (9:127) [next to 9:128] وَإِذَا مَآ أُنزِلَتْ سُورَةٌۭ نَّظَرَ بَعْضُهُمْ إِلَىٰ بَعْضٍ هَلْ يَرَىٰكُم مِّنْ أَحَدٍۢ ثُمَّ ٱنصَرَفُوا۟ ۚ صَرَفَ ٱللَّهُ قُلُوبَهُم بِأَنَّهُمْ قَوْمٌۭ لَّا يَفْقَهُونَ
- (9:129) [next to 9:128] فَإِن تَوَلَّوْا۟ فَقُلْ حَسْبِىَ ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ عَلَيْهِ تَوَكَّلْتُ ۖ وَهُوَ رَبُّ ٱلْعَرْشِ ٱلْعَظِيمِ
- (17:108) [next to 17:110] وَيَقُولُونَ سُبْحَٰنَ رَبِّنَآ إِن كَانَ وَعْدُ رَبِّنَا لَمَفْعُولًۭا
- (17:109) [next to 17:110] وَيَخِرُّونَ لِلْأَذْقَانِ يَبْكُونَ وَيَزِيدُهُمْ خُشُوعًۭا ۩
- (17:111) [next to 17:110] وَقُلِ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى لَمْ يَتَّخِذْ وَلَدًۭا وَلَمْ يَكُن لَّهُۥ شَرِيكٌۭ فِى ٱلْمُلْكِ وَلَمْ يَكُن لَّهُۥ وَلِىٌّۭ مِّنَ ٱلذُّلِّ ۖ وَكَبِّرْهُ تَكْبِيرًۢا
- (18:63) [next to 18:65] قَالَ أَرَءَيْتَ إِذْ أَوَيْنَآ إِلَى ٱلصَّخْرَةِ فَإِنِّى نَسِيتُ ٱلْحُوتَ وَمَآ أَنسَىٰنِيهُ إِلَّا ٱلشَّيْطَٰنُ أَنْ أَذْكُرَهُۥ ۚ وَٱتَّخَذَ سَبِيلَهُۥ فِى ٱلْبَحْرِ عَجَبًۭا
- (18:64) [next to 18:65] قَالَ ذَٰلِكَ مَا كُنَّا نَبْغِ ۚ فَٱرْتَدَّا عَلَىٰٓ ءَاثَارِهِمَا قَصَصًۭا
- (18:66) [next to 18:65] قَالَ لَهُۥ مُوسَىٰ هَلْ أَتَّبِعُكَ عَلَىٰٓ أَن تُعَلِّمَنِ مِمَّا عُلِّمْتَ رُشْدًۭا
- (18:67) [next to 18:65] قَالَ إِنَّكَ لَن تَسْتَطِيعَ مَعِىَ صَبْرًۭا
- (18:72) [next to 18:74] قَالَ أَلَمْ أَقُلْ إِنَّكَ لَن تَسْتَطِيعَ مَعِىَ صَبْرًۭا
- (18:73) [next to 18:74] قَالَ لَا تُؤَاخِذْنِى بِمَا نَسِيتُ وَلَا تُرْهِقْنِى مِنْ أَمْرِى عُسْرًۭا
- (18:75) [next to 18:74] ۞ قَالَ أَلَمْ أَقُل لَّكَ إِنَّكَ لَن تَسْتَطِيعَ مَعِىَ صَبْرًۭا
- (18:76) [next to 18:74] قَالَ إِن سَأَلْتُكَ عَن شَىْءٍۭ بَعْدَهَا فَلَا تُصَٰحِبْنِى ۖ قَدْ بَلَغْتَ مِن لَّدُنِّى عُذْرًۭا
- (18:78) [next to 18:80] قَالَ هَٰذَا فِرَاقُ بَيْنِى وَبَيْنِكَ ۚ سَأُنَبِّئُكَ بِتَأْوِيلِ مَا لَمْ تَسْتَطِع عَّلَيْهِ صَبْرًا
- (18:79) [next to 18:80] أَمَّا ٱلسَّفِينَةُ فَكَانَتْ لِمَسَٰكِينَ يَعْمَلُونَ فِى ٱلْبَحْرِ فَأَرَدتُّ أَنْ أَعِيبَهَا وَكَانَ وَرَآءَهُم مَّلِكٌۭ يَأْخُذُ كُلَّ سَفِينَةٍ غَصْبًۭا
- (18:83) [next to 18:81] وَيَسْـَٔلُونَكَ عَن ذِى ٱلْقَرْنَيْنِ ۖ قُلْ سَأَتْلُوا۟ عَلَيْكُم مِّنْهُ ذِكْرًا
- (18:84) [next to 18:82] إِنَّا مَكَّنَّا لَهُۥ فِى ٱلْأَرْضِ وَءَاتَيْنَٰهُ مِن كُلِّ شَىْءٍۢ سَبَبًۭا
- (19:43) [next to 19:45] يَٰٓأَبَتِ إِنِّى قَدْ جَآءَنِى مِنَ ٱلْعِلْمِ مَا لَمْ يَأْتِكَ فَٱتَّبِعْنِىٓ أَهْدِكَ صِرَٰطًۭا سَوِيًّۭا
- (19:46) [next to 19:45] قَالَ أَرَاغِبٌ أَنتَ عَنْ ءَالِهَتِى يَٰٓإِبْرَٰهِيمُ ۖ لَئِن لَّمْ تَنتَهِ لَأَرْجُمَنَّكَ ۖ وَٱهْجُرْنِى مَلِيًّۭا
- (19:47) [next to 19:45] قَالَ سَلَٰمٌ عَلَيْكَ ۖ سَأَسْتَغْفِرُ لَكَ رَبِّىٓ ۖ إِنَّهُۥ كَانَ بِى حَفِيًّۭا
- (19:94) [next to 19:93] لَّقَدْ أَحْصَىٰهُمْ وَعَدَّهُمْ عَدًّۭا
- (19:95) [next to 19:93] وَكُلُّهُمْ ءَاتِيهِ يَوْمَ ٱلْقِيَٰمَةِ فَرْدًا
- (20:3) [next to 20:5] إِلَّا تَذْكِرَةًۭ لِّمَن يَخْشَىٰ
- (20:4) [next to 20:5] تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى
- (20:6) [next to 20:5] لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ وَمَا بَيْنَهُمَا وَمَا تَحْتَ ٱلثَّرَىٰ
- (20:7) [next to 20:5] وَإِن تَجْهَرْ بِٱلْقَوْلِ فَإِنَّهُۥ يَعْلَمُ ٱلسِّرَّ وَأَخْفَى
- (20:106) [next to 20:108] فَيَذَرُهَا قَاعًۭا صَفْصَفًۭا
- (20:107) [next to 20:108] لَّا تَرَىٰ فِيهَا عِوَجًۭا وَلَآ أَمْتًۭا
- (20:110) [next to 20:108] يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلَا يُحِيطُونَ بِهِۦ عِلْمًۭا
- (21:105) [next to 21:107] وَلَقَدْ كَتَبْنَا فِى ٱلزَّبُورِ مِنۢ بَعْدِ ٱلذِّكْرِ أَنَّ ٱلْأَرْضَ يَرِثُهَا عِبَادِىَ ٱلصَّٰلِحُونَ
- (21:106) [next to 21:107] إِنَّ فِى هَٰذَا لَبَلَٰغًۭا لِّقَوْمٍ عَٰبِدِينَ
- (21:108) [next to 21:107] قُلْ إِنَّمَا يُوحَىٰٓ إِلَىَّ أَنَّمَآ إِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ ۖ فَهَلْ أَنتُم مُّسْلِمُونَ
- (21:109) [next to 21:107] فَإِن تَوَلَّوْا۟ فَقُلْ ءَاذَنتُكُمْ عَلَىٰ سَوَآءٍۢ ۖ وَإِنْ أَدْرِىٓ أَقَرِيبٌ أَم بَعِيدٌۭ مَّا تُوعَدُونَ
- (25:24) [next to 25:26] أَصْحَٰبُ ٱلْجَنَّةِ يَوْمَئِذٍ خَيْرٌۭ مُّسْتَقَرًّۭا وَأَحْسَنُ مَقِيلًۭا
- (25:25) [next to 25:26] وَيَوْمَ تَشَقَّقُ ٱلسَّمَآءُ بِٱلْغَمَٰمِ وَنُزِّلَ ٱلْمَلَٰٓئِكَةُ تَنزِيلًا
- (25:27) [next to 25:26] وَيَوْمَ يَعَضُّ ٱلظَّالِمُ عَلَىٰ يَدَيْهِ يَقُولُ يَٰلَيْتَنِى ٱتَّخَذْتُ مَعَ ٱلرَّسُولِ سَبِيلًۭا
- (25:28) [next to 25:26] يَٰوَيْلَتَىٰ لَيْتَنِى لَمْ أَتَّخِذْ فُلَانًا خَلِيلًۭا
- (25:58) [next to 25:60] وَتَوَكَّلْ عَلَى ٱلْحَىِّ ٱلَّذِى لَا يَمُوتُ وَسَبِّحْ بِحَمْدِهِۦ ۚ وَكَفَىٰ بِهِۦ بِذُنُوبِ عِبَادِهِۦ خَبِيرًا
- (25:61) [next to 25:60] تَبَارَكَ ٱلَّذِى جَعَلَ فِى ٱلسَّمَآءِ بُرُوجًۭا وَجَعَلَ فِيهَا سِرَٰجًۭا وَقَمَرًۭا مُّنِيرًۭا
- (25:62) [next to 25:60] وَهُوَ ٱلَّذِى جَعَلَ ٱلَّيْلَ وَٱلنَّهَارَ خِلْفَةًۭ لِّمَنْ أَرَادَ أَن يَذَّكَّرَ أَوْ أَرَادَ شُكُورًۭا
- (25:64) [next to 25:63] وَٱلَّذِينَ يَبِيتُونَ لِرَبِّهِمْ سُجَّدًۭا وَقِيَٰمًۭا
- (25:65) [next to 25:63] وَٱلَّذِينَ يَقُولُونَ رَبَّنَا ٱصْرِفْ عَنَّا عَذَابَ جَهَنَّمَ ۖ إِنَّ عَذَابَهَا كَانَ غَرَامًا
- (30:48) [next to 30:50] ٱللَّهُ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ فَتُثِيرُ سَحَابًۭا فَيَبْسُطُهُۥ فِى ٱلسَّمَآءِ كَيْفَ يَشَآءُ وَيَجْعَلُهُۥ كِسَفًۭا فَتَرَى ٱلْوَدْقَ يَخْرُجُ مِنْ خِلَٰلِهِۦ ۖ فَإِذَآ أَصَابَ بِهِۦ مَن يَشَآءُ مِنْ عِبَادِهِۦٓ إِذَا هُمْ يَسْتَبْشِرُونَ
- (30:49) [next to 30:50] وَإِن كَانُوا۟ مِن قَبْلِ أَن يُنَزَّلَ عَلَيْهِم مِّن قَبْلِهِۦ لَمُبْلِسِينَ
- (30:51) [next to 30:50] وَلَئِنْ أَرْسَلْنَا رِيحًۭا فَرَأَوْهُ مُصْفَرًّۭا لَّظَلُّوا۟ مِنۢ بَعْدِهِۦ يَكْفُرُونَ
- (30:52) [next to 30:50] فَإِنَّكَ لَا تُسْمِعُ ٱلْمَوْتَىٰ وَلَا تُسْمِعُ ٱلصُّمَّ ٱلدُّعَآءَ إِذَا وَلَّوْا۟ مُدْبِرِينَ
- (31:12) [next to 31:14] وَلَقَدْ ءَاتَيْنَا لُقْمَٰنَ ٱلْحِكْمَةَ أَنِ ٱشْكُرْ لِلَّهِ ۚ وَمَن يَشْكُرْ فَإِنَّمَا يَشْكُرُ لِنَفْسِهِۦ ۖ وَمَن كَفَرَ فَإِنَّ ٱللَّهَ غَنِىٌّ حَمِيدٌۭ
- (31:13) [next to 31:14] وَإِذْ قَالَ لُقْمَٰنُ لِٱبْنِهِۦ وَهُوَ يَعِظُهُۥ يَٰبُنَىَّ لَا تُشْرِكْ بِٱللَّهِ ۖ إِنَّ ٱلشِّرْكَ لَظُلْمٌ عَظِيمٌۭ
- (31:15) [next to 31:14] وَإِن جَٰهَدَاكَ عَلَىٰٓ أَن تُشْرِكَ بِى مَا لَيْسَ لَكَ بِهِۦ عِلْمٌۭ فَلَا تُطِعْهُمَا ۖ وَصَاحِبْهُمَا فِى ٱلدُّنْيَا مَعْرُوفًۭا ۖ وَٱتَّبِعْ سَبِيلَ مَنْ أَنَابَ إِلَىَّ ۚ ثُمَّ إِلَىَّ مَرْجِعُكُمْ فَأُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- (31:16) [next to 31:14] يَٰبُنَىَّ إِنَّهَآ إِن تَكُ مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍۢ فَتَكُن فِى صَخْرَةٍ أَوْ فِى ٱلسَّمَٰوَٰتِ أَوْ فِى ٱلْأَرْضِ يَأْتِ بِهَا ٱللَّهُ ۚ إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌۭ
- (33:41) [next to 33:43] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱذْكُرُوا۟ ٱللَّهَ ذِكْرًۭا كَثِيرًۭا
- (33:42) [next to 33:43] وَسَبِّحُوهُ بُكْرَةًۭ وَأَصِيلًا
- (33:44) [next to 33:43] تَحِيَّتُهُمْ يَوْمَ يَلْقَوْنَهُۥ سَلَٰمٌۭ ۚ وَأَعَدَّ لَهُمْ أَجْرًۭا كَرِيمًۭا
- (33:45) [next to 33:43] يَٰٓأَيُّهَا ٱلنَّبِىُّ إِنَّآ أَرْسَلْنَٰكَ شَٰهِدًۭا وَمُبَشِّرًۭا وَنَذِيرًۭا
- (36:9) [next to 36:11] وَجَعَلْنَا مِنۢ بَيْنِ أَيْدِيهِمْ سَدًّۭا وَمِنْ خَلْفِهِمْ سَدًّۭا فَأَغْشَيْنَٰهُمْ فَهُمْ لَا يُبْصِرُونَ
- (36:10) [next to 36:11] وَسَوَآءٌ عَلَيْهِمْ ءَأَنذَرْتَهُمْ أَمْ لَمْ تُنذِرْهُمْ لَا يُؤْمِنُونَ
- (36:12) [next to 36:11] إِنَّا نَحْنُ نُحْىِ ٱلْمَوْتَىٰ وَنَكْتُبُ مَا قَدَّمُوا۟ وَءَاثَٰرَهُمْ ۚ وَكُلَّ شَىْءٍ أَحْصَيْنَٰهُ فِىٓ إِمَامٍۢ مُّبِينٍۢ
- (36:13) [next to 36:11] وَٱضْرِبْ لَهُم مَّثَلًا أَصْحَٰبَ ٱلْقَرْيَةِ إِذْ جَآءَهَا ٱلْمُرْسَلُونَ
- (36:56) [next to 36:58] هُمْ وَأَزْوَٰجُهُمْ فِى ظِلَٰلٍ عَلَى ٱلْأَرَآئِكِ مُتَّكِـُٔونَ
- (36:57) [next to 36:58] لَهُمْ فِيهَا فَٰكِهَةٌۭ وَلَهُم مَّا يَدَّعُونَ
- (36:59) [next to 36:58] وَٱمْتَٰزُوا۟ ٱلْيَوْمَ أَيُّهَا ٱلْمُجْرِمُونَ
- (36:60) [next to 36:58] ۞ أَلَمْ أَعْهَدْ إِلَيْكُمْ يَٰبَنِىٓ ءَادَمَ أَن لَّا تَعْبُدُوا۟ ٱلشَّيْطَٰنَ ۖ إِنَّهُۥ لَكُمْ عَدُوٌّۭ مُّبِينٌۭ
- (39:4) [next to 39:6] لَّوْ أَرَادَ ٱللَّهُ أَن يَتَّخِذَ وَلَدًۭا لَّٱصْطَفَىٰ مِمَّا يَخْلُقُ مَا يَشَآءُ ۚ سُبْحَٰنَهُۥ ۖ هُوَ ٱللَّهُ ٱلْوَٰحِدُ ٱلْقَهَّارُ
- (39:5) [next to 39:6] خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۖ يُكَوِّرُ ٱلَّيْلَ عَلَى ٱلنَّهَارِ وَيُكَوِّرُ ٱلنَّهَارَ عَلَى ٱلَّيْلِ ۖ وَسَخَّرَ ٱلشَّمْسَ وَٱلْقَمَرَ ۖ كُلٌّۭ يَجْرِى لِأَجَلٍۢ مُّسَمًّى ۗ أَلَا هُوَ ٱلْعَزِيزُ ٱلْغَفَّٰرُ
- (39:7) [next to 39:6] إِن تَكْفُرُوا۟ فَإِنَّ ٱللَّهَ غَنِىٌّ عَنكُمْ ۖ وَلَا يَرْضَىٰ لِعِبَادِهِ ٱلْكُفْرَ ۖ وَإِن تَشْكُرُوا۟ يَرْضَهُ لَكُمْ ۗ وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۗ ثُمَّ إِلَىٰ رَبِّكُم مَّرْجِعُكُمْ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (39:8) [next to 39:6] ۞ وَإِذَا مَسَّ ٱلْإِنسَٰنَ ضُرٌّۭ دَعَا رَبَّهُۥ مُنِيبًا إِلَيْهِ ثُمَّ إِذَا خَوَّلَهُۥ نِعْمَةًۭ مِّنْهُ نَسِىَ مَا كَانَ يَدْعُوٓا۟ إِلَيْهِ مِن قَبْلُ وَجَعَلَ لِلَّهِ أَندَادًۭا لِّيُضِلَّ عَن سَبِيلِهِۦ ۚ قُلْ تَمَتَّعْ بِكُفْرِكَ قَلِيلًا ۖ إِنَّكَ مِنْ أَصْحَٰبِ ٱلنَّارِ
- (40:5) [next to 40:7] كَذَّبَتْ قَبْلَهُمْ قَوْمُ نُوحٍۢ وَٱلْأَحْزَابُ مِنۢ بَعْدِهِمْ ۖ وَهَمَّتْ كُلُّ أُمَّةٍۭ بِرَسُولِهِمْ لِيَأْخُذُوهُ ۖ وَجَٰدَلُوا۟ بِٱلْبَٰطِلِ لِيُدْحِضُوا۟ بِهِ ٱلْحَقَّ فَأَخَذْتُهُمْ ۖ فَكَيْفَ كَانَ عِقَابِ
- (40:6) [next to 40:7] وَكَذَٰلِكَ حَقَّتْ كَلِمَتُ رَبِّكَ عَلَى ٱلَّذِينَ كَفَرُوٓا۟ أَنَّهُمْ أَصْحَٰبُ ٱلنَّارِ
- (40:8) [next to 40:7] رَبَّنَا وَأَدْخِلْهُمْ جَنَّٰتِ عَدْنٍ ٱلَّتِى وَعَدتَّهُمْ وَمَن صَلَحَ مِنْ ءَابَآئِهِمْ وَأَزْوَٰجِهِمْ وَذُرِّيَّٰتِهِمْ ۚ إِنَّكَ أَنتَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (46:13) [next to 46:15] إِنَّ ٱلَّذِينَ قَالُوا۟ رَبُّنَا ٱللَّهُ ثُمَّ ٱسْتَقَٰمُوا۟ فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
- (46:14) [next to 46:15] أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْجَنَّةِ خَٰلِدِينَ فِيهَا جَزَآءًۢ بِمَا كَانُوا۟ يَعْمَلُونَ
- (46:16) [next to 46:15] أُو۟لَٰٓئِكَ ٱلَّذِينَ نَتَقَبَّلُ عَنْهُمْ أَحْسَنَ مَا عَمِلُوا۟ وَنَتَجَاوَزُ عَن سَيِّـَٔاتِهِمْ فِىٓ أَصْحَٰبِ ٱلْجَنَّةِ ۖ وَعْدَ ٱلصِّدْقِ ٱلَّذِى كَانُوا۟ يُوعَدُونَ
- (46:17) [next to 46:15] وَٱلَّذِى قَالَ لِوَٰلِدَيْهِ أُفٍّۢ لَّكُمَآ أَتَعِدَانِنِىٓ أَنْ أُخْرَجَ وَقَدْ خَلَتِ ٱلْقُرُونُ مِن قَبْلِى وَهُمَا يَسْتَغِيثَانِ ٱللَّهَ وَيْلَكَ ءَامِنْ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ فَيَقُولُ مَا هَٰذَآ إِلَّآ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- (47:20) [next to 47:22] وَيَقُولُ ٱلَّذِينَ ءَامَنُوا۟ لَوْلَا نُزِّلَتْ سُورَةٌۭ ۖ فَإِذَآ أُنزِلَتْ سُورَةٌۭ مُّحْكَمَةٌۭ وَذُكِرَ فِيهَا ٱلْقِتَالُ ۙ رَأَيْتَ ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌۭ يَنظُرُونَ إِلَيْكَ نَظَرَ ٱلْمَغْشِىِّ عَلَيْهِ مِنَ ٱلْمَوْتِ ۖ فَأَوْلَىٰ لَهُمْ
- (47:21) [next to 47:22] طَاعَةٌۭ وَقَوْلٌۭ مَّعْرُوفٌۭ ۚ فَإِذَا عَزَمَ ٱلْأَمْرُ فَلَوْ صَدَقُوا۟ ٱللَّهَ لَكَانَ خَيْرًۭا لَّهُمْ
- (47:23) [next to 47:22] أُو۟لَٰٓئِكَ ٱلَّذِينَ لَعَنَهُمُ ٱللَّهُ فَأَصَمَّهُمْ وَأَعْمَىٰٓ أَبْصَٰرَهُمْ
- (47:24) [next to 47:22] أَفَلَا يَتَدَبَّرُونَ ٱلْقُرْءَانَ أَمْ عَلَىٰ قُلُوبٍ أَقْفَالُهَآ
- (67:1) [next to 67:3] تَبَٰرَكَ ٱلَّذِى بِيَدِهِ ٱلْمُلْكُ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌ
- (67:2) [next to 67:3] ٱلَّذِى خَلَقَ ٱلْمَوْتَ وَٱلْحَيَوٰةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًۭا ۚ وَهُوَ ٱلْعَزِيزُ ٱلْغَفُورُ
- (67:4) [next to 67:3] ثُمَّ ٱرْجِعِ ٱلْبَصَرَ كَرَّتَيْنِ يَنقَلِبْ إِلَيْكَ ٱلْبَصَرُ خَاسِئًۭا وَهُوَ حَسِيرٌۭ
- (67:5) [next to 67:3] وَلَقَدْ زَيَّنَّا ٱلسَّمَآءَ ٱلدُّنْيَا بِمَصَٰبِيحَ وَجَعَلْنَٰهَا رُجُومًۭا لِّلشَّيَٰطِينِ ۖ وَأَعْتَدْنَا لَهُمْ عَذَابَ ٱلسَّعِيرِ
- (67:17) [next to 67:19] أَمْ أَمِنتُم مَّن فِى ٱلسَّمَآءِ أَن يُرْسِلَ عَلَيْكُمْ حَاصِبًۭا ۖ فَسَتَعْلَمُونَ كَيْفَ نَذِيرِ
- (67:18) [next to 67:19] وَلَقَدْ كَذَّبَ ٱلَّذِينَ مِن قَبْلِهِمْ فَكَيْفَ كَانَ نَكِيرِ
- (67:21) [next to 67:19] أَمَّنْ هَٰذَا ٱلَّذِى يَرْزُقُكُمْ إِنْ أَمْسَكَ رِزْقَهُۥ ۚ بَل لَّجُّوا۟ فِى عُتُوٍّۢ وَنُفُورٍ
- (78:35) [next to 78:37] لَّا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا كِذَّٰبًۭا
- (78:40) [next to 78:38] إِنَّآ أَنذَرْنَٰكُمْ عَذَابًۭا قَرِيبًۭا يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ وَيَقُولُ ٱلْكَافِرُ يَٰلَيْتَنِى كُنتُ تُرَٰبًۢا
- (90:11) [next to 90:13] فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ
- (90:12) [next to 90:13] وَمَآ أَدْرَىٰكَ مَا ٱلْعَقَبَةُ
- (90:14) [next to 90:13] أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ
- (90:16) [next to 90:15] أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ
- (90:18) [next to 90:17] أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ
- (90:19) [next to 90:17] وَٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا هُمْ أَصْحَٰبُ ٱلْمَشْـَٔمَةِ

