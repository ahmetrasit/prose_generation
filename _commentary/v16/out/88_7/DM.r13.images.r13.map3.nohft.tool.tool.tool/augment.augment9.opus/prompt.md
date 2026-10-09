Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 88:7; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/88_7/DM.r13.images.r13.map3.nohft.tool.tool.tool/88_7.reading.tr.md (prose paragraphs numbered) =====
## Adı kalıp işi olmayan yemek

[¶1] Yedinci ayetin kendine ait bir öznesi yoktur. Bir önceki cümleyi sürdürür ve onun son kelimesini niteler. Altıncı ayet önce yemeği tümden kaldırır, sonra tek bir istisna bırakır: {ar:لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ, tr:leyse lehum taâmun illâ min darî', gloss:onlar için darî'den başka yemek yoktur, source:88:6}. Bu istisna kuru, dikenli bir bitkiye "yemek" adını bırakmış gibidir. Yedinci ayet ise o adı işinden boşaltır: {ar:لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ, tr:lâ yusminu ve lâ yuğnî min cû', gloss:ne besleyip semirtir ne de açlıktan kurtarır, source:88:7}. Ayet darî'i ne olduğuyla değil, ne yapmadığıyla tanıtır. Bir yemeği yemek yapan şey gördüğü iştir. O iş yoksa geriye yalnızca ad kalır.

[¶2] Ayetin saydığı iki iş farklı hızlarda işler. Semirtmek yavaş bir iştir. Günler boyunca yenen yemek bedene et ve yağ olarak geçer, onu doldurur ve güçlendirir. Açlıktan kurtarmak ise anlık bir iştir ve boş midenin sızısını o an dindirir. Ayet önce büyük olanı, sonra en küçüğünü reddeder. Bu yemek bedeni kurmaz, bir öğünlük açlığı bile bastırmaz. Sıralama aşağı doğru iner ve en dipte de bir şey bulmaz.

[¶3] Açlık burada yalnızca bir eksiklik değildir. Araplar açlığı önce tokluğun karşıtı olarak tanımlarlardı: {ar:الجوع ضد الشبع, tr:el-cû'u diddu'ş-şiba', gloss:açlık tokluğun zıddıdır, source:"ج و ع,B001"}. Onu bir acı olarak da anlatırlardı: {ar:الألم الذي ينال الحيوان من خلو المعدة من الطعام, tr:el-elemu'llezî yenâlü'l-hayevâne min hulüvvi'l-mi'deti mine't-taâm, gloss:midenin yemekten boş kalmasıyla canlıya gelen acı, source:"ج و ع,B001"}. Dördüncü ayette yüzler kızgın bir ateşe girer, beşinci ayette kaynar bir pınardan içirilir. Yedinci ayet acıyı bedenin içine taşır. Dışarıda ateş yanarken içeride boş bir mide sızlar ve ona verilen şey bu sızıyı dindirmez. "Açlıktan" sözündeki "min" edatı bir uzaklaştırmayı anlatır. Yemek insanı açlıktan alıp onun dışına çıkarmalıydı. Bu yemek ise onu açlığın içinde bırakır. Altıncı ayetteki darî' kelimesinin harfleri zayıf düşmüş bedeni {source:"ض ر ع,B003"} ve bir şeye şiddetle muhtaç olmayı {source:"ض ر ع,B002"} da adlandırır. Böylece o yemeğin adı ile bu ayetin iki olumsuzluğu, surenin yemek sahnesinde karşı karşıya durur.

## Semizlik: bedeni kuran yemek

[¶4] Ayetin ilk fiili semizlik kelimesinden gelir. Semizlik zayıflığın karşıtı diye tanımlanırdı: {ar:السمن نقيض الهزال, tr:es-simenu nakîdu'l-hüzâl, gloss:semizlik zayıflığın zıddıdır, source:"س م ن,B001"}. Semiz olan da zayıflamış olanın karşısına konurdu: {ar:السمين خلاف المهزول, tr:es-semînu hılâfu'l-mehzûl, gloss:semiz, zayıf düşmüşün karşıtıdır, source:"س م ن,B001"}. Ayetteki biçim ettirgendir ve birini semiz kılmak demektir: {ar:أسمنته وسمنته جعلته سمينا, tr:esmentuhû ve semmentuhû ce'altuhû semînen, gloss:onu semirttim, yani semiz kıldım, source:"س م ن,B001"}. Bugünün okuru şişmanlığı çoğu zaman bir kusur diye duyar. Bu dilin dünyasında ise semizlik sağlıktı, bolluktu, yeterince yemiş bir bedenin işaretiydi. Zayıflık ise yokluğun izini taşırdı. Öyle ki kadınları semirtmek için bir ilaç bile hazırlanırdı: {ar:السمنة دواء تسمن به النساء, tr:es-sumnetu devâun tusammenu bihi'n-nisâ', gloss:sumne kadınların semirtildiği bir ilaçtır, source:"س م ن,B001"}. "Semirtmez" sözü bu yüzden yemeğin bedeni zayıflıktan doluluğa taşıyan asıl işini reddeder.

[¶5] Kur'an semizlik ile açlığı bir rüyada yan yana koyar. Yusuf kıssasında hükümdar adamlarına gördüğü düşü anlatır: {ar:إِنِّىٓ أَرَىٰ سَبْعَ بَقَرَٰتٍۢ سِمَانٍۢ يَأْكُلُهُنَّ سَبْعٌ عِجَافٌۭ, tr:innî erâ seb'a bekarâtin simânin ye'kuluhunne seb'un icâf, gloss:yedi semiz ineği yedi cılız ineğin yediğini görüyorum, source:12:43}. Buradaki "semiz" kelimesi ayetteki fiille aynı köktendir. Yusuf rüyayı yıllar olarak yorumlar. Yedi yıl ekip biçilecek ve ürün başağında saklanacaktır. Ardından gelecek yedi zor yıl için şöyle der: {ar:سَبْعٌۭ شِدَادٌۭ يَأْكُلْنَ مَا قَدَّمْتُمْ لَهُنَّ, tr:seb'un şidâdun ye'kulne mâ kaddemtum lehunn, gloss:sizin onlar için önceden hazırladığınızı yiyip bitirecek yedi çetin yıl, source:12:48}. Araplar böyle bir yıla açlık yılı derlerdi: {ar:المجاعة عام فيه جوع, tr:el-mecâatu âmun fîhi cû', gloss:mecâa içinde açlık olan yıldır, source:"ج و ع,B002"}. Rüyada semizlik ve açlık birbirini izleyen yıllardır ve tedbirli olan bolluk yıllarından kıtlık yıllarına azık ayırır. Yedinci ayetteki yemekte ise semiz yanı hiç gelmez, ayrılmış bir azık da yoktur.

[¶6] Surenin başka bir kelimesi aynı bedeni öbür ucundan gösterir. İkinci ayetteki "hâşia" kelimesinin ailesi, yorgunluktan hörgücünün yağı erimiş deveyi de anlatır: {ar:خشع سنام البعير إذا أنضي فذهب شحمه وتطأطأ شرفه, tr:haşaa senâmü'l-baîri izâ undiye fe-zehebe şahmuhû ve teta'tae şerefuh, gloss:yorulan devenin hörgücünün yağı gidip tepesi çöktü, source:"خ ش ع,B004"}. O çökük hörgüç ile semirtmeyen yemek aynı bedenin iki ucunda durur.

## Tereyağı ve ters çevrilmiş sofra

[¶7] Aynı harfler bir yiyeceğin de adıdır. Semn, sütten çıkarılıp eritilen ve arıtılan yağdır: {ar:السمن سلاء اللبن, tr:es-semnu sulâü'l-leben, gloss:semn sütten eritilip arıtılan yağdır, source:"س م ن,B002"}. Bu yağ yemeğe katılarak onu zenginleştirirdi. Bir topluluk için yemek hazırlayan kişi şöyle derdi: {ar:سمنت لهم الطعام إذا لتته بالسمن, tr:sementu lehumu't-taâme izâ lettetuhû bi's-semn, gloss:yemeği onlar için tereyağıyla karıştırdım, source:"س م ن,B002"}. Yola çıkanlara azık olarak da verilirdi: {ar:سمنت القوم تسمينا زودتهم السمن, tr:semmentu'l-kavme tesmînen zevvedtuhumu's-semn, gloss:topluluğa azık olarak tereyağı verdim, source:"س م ن,B002"}. Biri kapıya gelip bu yağı armağan olarak isteyebilirdi: {ar:جاءوا يستسمنون أي يطلبون أن يوهب لهم السمن, tr:câû yestesminûne ey yatlubûne en yûhebe lehumu's-semn, gloss:tereyağı armağan edilmesini istemeye geldiler, source:"س م ن,B002"}. Bu resimler ayetteki anlamın yerine geçmez, onun yanında duyulur. Ayette fiil semirtmek demektir. Yanında ise yemeğe yağ katan, yolcuya azık veren ve isteyeni geri çevirmeyen bir ev sahibinin eli duyulur.

[¶8] Kur'an konuk ağırlamanın ölçüsünü bu kökün bir kelimesiyle verir. İbrahim'e gelen konuklar {ar:ضَيْفِ إِبْرَٰهِيمَ ٱلْمُكْرَمِينَ, tr:dayfi İbrâhîme'l-mükremîn, gloss:İbrahim'in ağırlanan konukları, source:51:24} diye anılır. Selam verip içeri girerler. İbrahim onları tanımaz, yine de sessizce ailesinin yanına gider: {ar:فَجَآءَ بِعِجْلٍۢ سَمِينٍۢ, tr:fe-câe bi-iclin semîn, gloss:semiz bir buzağı getirdi, source:51:26}. Sonra onu konuklarına yaklaştırır ve {ar:أَلَا تَأْكُلُونَ, tr:e-lâ te'kulûn, gloss:yemez misiniz, source:51:27} der. Bilinmeyen konuğa bile sunulan yemek semizdir.

[¶9] Aynı Kur'an bu sofranın tersini de kurar. Solun ehli anlatılırken önce kavurucu bir rüzgârın ve kaynar suyun içinde oldukları söylenir. Sonra bir gölgeleri olduğu bildirilir, ama o gölge kara bir dumandandır: {ar:لَّا بَارِدٍۢ وَلَا كَرِيمٍ, tr:lâ bâridin ve lâ kerîm, gloss:ne serindir ne de cömert, source:56:44}. Buradaki "cömert" kelimesi, İbrahim'in "ağırlanan" konuklarını niteleyen kelimeyle aynı köktendir. Bu gölgede ağırlama yoktur. Ardından o insanların daha önce bolluk içinde şımarıp yaşadıkları hatırlatılır {source:56:45}. Sonra yemekleri gelir. Zakkum ağacından yiyecekler {source:56:52}, karınlarını ondan dolduracaklar {source:56:53}, üstüne kaynar sudan susuzluğu dinmeyen develer gibi içeceklerdir: {ar:فَشَٰرِبُونَ شُرْبَ ٱلْهِيمِ, tr:fe-şâribûne şurbe'l-hîm, gloss:susuzluğu dinmeyen develerin içişi gibi içecekler, source:56:55}. Sahne şöyle kapanır: {ar:هَٰذَا نُزُلُهُمْ يَوْمَ ٱلدِّينِ, tr:hâzâ nuzuluhum yevme'd-dîn, gloss:bu, hesap gününde onlara sunulan konuk sofrasıdır, source:56:56}. Nüzül, yeni gelen konuğun önüne konan ilk sofradır. Burada karın dolar ama semizlik yoktur, içecek içilir ama susuzluk geçmez. Gâşiye'nin altıncı ve yedinci ayetleri aynı ters sofrayı kurar. Gelenin önüne bir diken konur ve bu diken, İbrahim'in semiz buzağısının göreceği işin hiçbirini görmez.

[¶10] Bu ailede bir de serinlik vardır. Araplar bir şeyi soğutmaya da bu harflerle ad verirlerdi: {ar:سمنت الشيء إذا بردته, tr:semmentu'ş-şey'e izâ berradtuh, gloss:bir şeyi soğuttum, source:"س م ن,B003"}. Bu da yalnızca yan anlamdır. Yine de dördüncü ayetin kızgın ateşi ve beşinci ayetin kaynar pınarı arasında olumsuzlanan bu fiil, "ne serindir ne cömert" denen gölgenin yanında duyulur. Ateş ehlinden hem besleyen zenginlik hem de serinletme esirgenmiştir.

## Yetmek ve birinin yerini tutmak

[¶11] Ayetin ikinci fiili yetmek demektir: {ar:الغناء بالفتح الكفاية ولا يغني أي لا يكفي, tr:el-ğanâu bi'l-feth el-kifâye ve lâ yuğnî ey lâ yekfî, gloss:ğanâ yeterliliktir; lâ yuğnî yetmez demektir, source:"غ ن ي,B002"}. Bir şeyin işe yaramadığını söylemek için de bu fiil kullanılırdı: {ar:ما يغني عنك هذا أي ما يجزئ وما ينفع, tr:mâ yuğnî anke hâzâ ey mâ yuczi' ve mâ yenfa', gloss:bu sana yetmez ve yarar sağlamaz, source:"غ ن ي,B002"}. İşi görüp başkasının yerini tutan adama da bu kökten ad verilirdi: {ar:ورجل مغن أي مجزئ كاف, tr:ve racülün muğnin ey muczi'un kâfin, gloss:muğnî, işi gören ve yeten adamdır, source:"غ ن ي,B002"}. Fiil, eksik olanın yerine geçip onun işini tam olarak görmeyi anlatır. Kökün merkezindeki zenginlik de mal yığını olarak değil, ihtiyacın ortadan kalkması olarak tarif edilir: {ar:عدم الحاجات وقلة الحاجات وكثرة القنيات, tr:ademü'l-hâcâti ve kılletü'l-hâcâti ve kesretü'l-kınyât, gloss:ihtiyaçların yokluğu ya da azlığı ve edinilen malın çokluğu, source:"غ ن ي,B001"}. "Açlıktan kurtarmak" sözü bu yüzden kelimesi kelimesine insanı açlığa karşı ihtiyaçsız kılmaktır. Her lokma, açlık karşısında küçük bir zenginliktir. Darî' ise bu küçük zenginliği bile vermez.

[¶12] Türkçe bu kelimeyi iki daralmış biçimde taşır. "Gani gani" yalnızca bolluğu söyler, "gına gelmek" ise bıkkınlığı. İkisinde de Arapçadaki asıl iş kaybolmuştur. O iş, eksik olanın yerine geçip ihtiyacı bitirmektir.

[¶13] Kur'an bu fiili "min" edatıyla birlikte, adı olup işi olmayan şeyler için kullanır. Ayırma gününde yalanlayıcılara yalanladıkları şeye gitmeleri söylenir, ardından da şöyle denir: {ar:ٱنطَلِقُوٓا۟ إِلَىٰ ظِلٍّۢ ذِى ثَلَٰثِ شُعَبٍۢ, tr:intalikû ilâ zıllin zî selâsi şuab, gloss:üç kola ayrılan bir gölgeye gidin, source:77:30}. Gölgenin ne olduğu hemen söylenir: {ar:لَّا ظَلِيلٍۢ وَلَا يُغْنِى مِنَ ٱللَّهَبِ, tr:lâ zalîlin ve lâ yuğnî mine'l-leheb, gloss:ne gölgelendirir ne de alevden korur, source:77:31}. Bu cümle yedinci ayetle aynı biçimde kurulmuştur: önce bir olumsuzluk gelir, sonra "ve lâ yuğnî min" gelir. Gölge adını taşır ama gölge işini görmez, yemek de adını taşır ama yemek işini görmez. Aynı fiil bilgi için de kullanılır. Ahirete inanmayıp meleklere dişi adları verenler için şöyle denir: {ar:وَإِنَّ ٱلظَّنَّ لَا يُغْنِى مِنَ ٱلْحَقِّ شَيْـًۭٔا, tr:ve inne'z-zanne lâ yuğnî mine'l-hakkı şey'â, gloss:zan, gerçeğin yerini hiçbir şekilde tutmaz, source:53:28}. Zan da bilginin kılığına girer ama bilginin işini görmez. Kur'an'da bu fiil, sahte gölgeyi, sahte bilgiyi ve sahte yemeği aynı ölçüyle tartar.

[¶14] Surenin öbür ayetleri bu ölçünün karşı ucunu taşır. On yedinci ayetteki devenin kökü, suya muhtaç olmadan yaş otla yetinen hayvanı anlatır: {ar:أبلت الإبل والوحش اجتزأت بالرطب عن الماء, tr:ebeleti'l-ibilu ve'l-vahşu'ctezeet bi'r-ratbi ani'l-mâ', gloss:develer ve yaban hayvanları sudan vazgeçip yaş otla yetindi, source:"ء ب ل,B002"}. Son ayetteki hesap kelimesinin kökü ise yetecek kadar verilen bağışı da adlandırır {source:"ح س ب,B003"}. Üçüncü ayetteki yorgun emek, bu "yeter" ile yedinci ayetteki "yetmez" arasında tartılır.

## Kendini yeterli sanan

[¶15] Bu kökün en tehlikeli biçimi, insanın kendini ihtiyaçsız görmesidir. "Oku" diye açılan bir surede Allah insan hakkında şöyle der: {ar:كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ, tr:kellâ inne'l-insâne le-yatğâ, gloss:hayır, insan gerçekten azar, source:96:6}; {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en raâhu'staḡnâ, gloss:kendini ihtiyaçsız gördüğü için, source:96:7}. Hemen ardından {ar:إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ, tr:inne ilâ rabbike'r-ruc'â, gloss:dönüş şüphesiz Rabbinedir, source:96:8} gelir. Gâşiye de neredeyse aynı cümleyle kapanır: {ar:إِنَّ إِلَيْنَآ إِيَابَهُمْ, tr:inne ileynâ iyâbehum, gloss:onların dönüşü şüphesiz Bizedir, source:88:25}. Türkçede istiğna bir gönül tokluğu, bir erdem olarak yaşar. Kökün kendisi de az şeyle yetinmeyi tanır. Ama o ayetteki istiğna, insanın kendine dair bir yanılgısıdır.

[¶16] Başka bir surede iki insan karşılaştırılır. Biri verir ve sakınır. Öbürü için {ar:وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ, tr:ve emmâ men bahıle ve'staḡnâ, gloss:cimrilik edip kendini ihtiyaçsız sayana gelince, source:92:8} denir. Onun sonu yedinci ayetteki fiille anlatılır: {ar:وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ, tr:ve mâ yuğnî anhu mâluhû izâ teraddâ, gloss:yuvarlanıp düştüğünde malı ona hiçbir yarar sağlamaz, source:92:11}. Dünyada kendini ihtiyaçsız sanan kişi, düştüğü yerde hiçbir şeyin kendisine yetmediğini görür.

[¶17] Kitabı solundan verilen kişinin sözleri bu iki çizgiyi tek bir sahnede birleştirir. Kitabını alınca keşke verilmeseydi der {source:69:25}, sonra şöyle yakınır: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ, tr:mâ ağnâ annî mâliyeh, gloss:malım bana hiçbir yarar sağlamadı, source:69:28}; {ar:هَلَكَ عَنِّى سُلْطَٰنِيَهْ, tr:heleke annî sultâniyeh, gloss:gücüm elimden gitti, source:69:29}. Onun suçu sayılırken şu da söylenir: {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ taâmi'l-miskîn, gloss:yoksulu doyurmaya teşvik etmezdi, source:69:34}. Az sonra da onun yemeği bildirilir: {ar:وَلَا طَعَامٌ إِلَّا مِنْ غِسْلِينٍۢ, tr:ve lâ taâmun illâ min ğıslîn, gloss:irinden başka yemeği de yoktur, source:69:36}. Malı yetmeyen, aç olanı doyurmayan kişiye, doyurmayan bir yemek verilir.

[¶18] Semizlik kelimesinin ailesi de bu yanılgının bir adını taşır. Kendilerinde olmayan bir iyilikle övünenler için bu kökten bir fiil kullanılırdı: {ar:يتسمنون أي يتكثرون بما ليس فيهم من الخير ويدعون ما ليس لهم من الشرف, tr:yetesemmenûne ey yetekesserûne bimâ leyse fîhim mine'l-hayr ve yeddeûne mâ leyse lehum mine'ş-şeref, gloss:kendilerinde olmayan iyilikle çoğalmış görünür, kendilerine ait olmayan şerefi sahiplenirler, source:"س م ن,B010"}. Bu, semizlik taslamaktır. Dünyada iki tür sahte doyum vardır: semizlik taslamak ve kendini ihtiyaçsız saymak. Yedinci ayet bu ikisinin karşısına iki gerçek yoksunluk koyar: yemek ne semirtir ne de ihtiyacı giderir. Kur'an yalanlayanların dünyadaki yiyişini de anlatır: {ar:وَٱلَّذِينَ كَفَرُوا۟ يَتَمَتَّعُونَ وَيَأْكُلُونَ كَمَا تَأْكُلُ ٱلْأَنْعَٰمُ وَٱلنَّارُ مَثْوًۭى لَّهُمْ, tr:vellezîne keferû yetemetteûne ve ye'kulûne kemâ te'kulu'l-en'âmu ve'n-nâru mesven lehum, gloss:inkâr edenler yararlanır ve hayvanların yediği gibi yerler; ateş ise onların konaklama yeridir, source:47:12}. Orada yenen şey, sonunda konakladıkları yerin yemeğine dönüşür.

[¶19] Kur'an ihtiyaçsızlığı tek bir yere ayırır: {ar:يَٰٓأَيُّهَا ٱلنَّاسُ أَنتُمُ ٱلْفُقَرَآءُ إِلَى ٱللَّهِ ۖ وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:yâ eyyuhe'n-nâsu entumu'l-fukarâu ila'llâh, va'llâhu huve'l-ğaniyyu'l-hamîd, gloss:ey insanlar, Allah'a muhtaç olan sizsiniz; Allah ise ihtiyaçsız olandır, övülmeye layık olandır, source:35:15}. Peygamber'e söylenen başka bir sözde de bu ayrım yemekle kurulur. Göklerin ve yerin yaratıcısı için {ar:وَهُوَ يُطْعِمُ وَلَا يُطْعَمُ, tr:ve huve yut'imu ve lâ yut'am, gloss:O doyurur ama doyurulmaz, source:6:14} denir. Açlık, insanın muhtaç olduğunun en çıplak işaretidir. Yedinci ayet bu işareti ortadan kaldırmaz, onu hiç dinmeyen bir hale getirir.

## Açlıktan doyuran el

[¶20] Yedinci ayetin son iki kelimesi Kur'an'da bir kez daha, tam tersi bir cümlede geçer. Kureyş'in kış ve yaz yolculuklarına alıştırıldığı hatırlatılır {source:106:2}, sonra bu evin Rabbine kulluk etmeleri istenir {source:106:3}. Bu Rab şöyle tanıtılır: {ar:ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ, tr:ellezî at'amehum min cûin ve âmenehum min havf, gloss:onları açlıktan doyuran ve korkudan güvene erdiren, source:106:4}. Orada "açlıktan" diye söylenen kelimeler ile yedinci ayettekiler aynıdır. Dünyada insanı açlıktan çıkaran bir el vardır. Yedinci ayet, o eli tanımayıp yüz çevirenin önüne açlıktan çıkarmayan bir yemek koyar. Surenin yirmi üçüncü ayeti bu kişiyi {ar:إِلَّا مَن تَوَلَّىٰ وَكَفَرَ, tr:illâ men tevellâ ve kefer, gloss:ancak yüz çevirip inkâr eden, source:88:23} diye anar.

[¶21] Kur'an açlığın bir nimetin geri alınması olarak gelebileceğini de anlatır. Allah bir kasabayı örnek verir. Bu kasaba güven içindedir, rızkı her yerden bol bol gelir. Sonra Allah'ın nimetlerine nankörlük eder: {ar:فَأَذَٰقَهَا ٱللَّهُ لِبَاسَ ٱلْجُوعِ وَٱلْخَوْفِ, tr:fe-ezâkahallâhu libâse'l-cûi ve'l-havf, gloss:Allah da ona açlığın ve korkunun elbisesini tattırdı, source:16:112}. Açlık burada bir elbise gibi bütün bedeni sarar. Üstelik bu elbise tadılır. Yani hem dıştan kuşatır hem de içe işler. Yedinci ayetteki açlık da böyledir. Dışarıda ateş, içeride dinmeyen bir boşluk vardır.

[¶22] Bahçe ise açlığın olmadığı yer olarak tanımlanır. Allah Âdem'i eşiyle birlikte uyarırken bahçenin ona sağladıklarını sayar: {ar:إِنَّ لَكَ أَلَّا تَجُوعَ فِيهَا وَلَا تَعْرَىٰ, tr:inne leke ellâ tecûa fîhâ ve lâ ta'râ, gloss:orada acıkmaman ve çıplak kalmaman senin hakkındır, source:20:118}. Hemen ardından susamamak ve güneşte yanmamak da eklenir {source:20:119}. Gâşiye'nin bahçesinde de bir pınar, yükseltilmiş sedirler, kadehler, yastıklar ve halılar sayılır, ama hiçbir yemek adı geçmez. Orada açlık giderilecek bir sorun olarak bile görünmez. Ateş yarısında ise her şey bir ihtiyacın etrafında döner: içilen kaynar sudur, yenen kuru dikendir ve yedinci ayet bu yemeğin ihtiyaca ne bedeni kurarak ne de sızıyı dindirerek dokunabildiğini söyler.

===== _commentary/v16/out/88_7/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: نُزُل = meal set before an arriving guest
- memory: الهيم = camels with unquenchable thirst
- memory: Turkish "gani" and "gına" derive from Arabic ġanī / ġinā
- memory: كريم (56:44) and المكرمين (51:24) share root ك ر م
- not written: س م ن B004 quail possibly identified with salwā (2:57) - identification only reported as disputed; too thin to carry a theme
- not written: س م ن B005-B009 (Samaniyya sect, dyes, place name, share-equalizing, worn wrappers) - no work in the ayah's themes
- not written: غ ن ي B003 singing, B005 ġāniya, B006 marriage - no link to feeding or sufficiency here
- not written: غ ن ي B004 dwelling long (cf. 10:24 كأن لم تغن بالأمس) - vanished crop image tempting but reaches the ayah only through another plant
- not written: ج و ع B003 deliberate hunger for cure - no role in a scene of imposed hunger
- not written: ج و ع B004 longing / "hungry pot" (kalıp) - fixed expressions only; hospitality theme already carried by سمن
- not written: 12:49 year of relief after famine - would add a hope the ayah's scene does not offer

===== passages not cited (193) =====
## strong (this ayah's own list) (12)

- (3:116) [listed for 88:7] إِنَّ ٱلَّذِينَ كَفَرُوا۟ لَن تُغْنِىَ عَنْهُمْ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُم مِّنَ ٱللَّهِ شَيْـًۭٔا ۖ وَأُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۚ هُمْ فِيهَا خَٰلِدُونَ
- (12:47) [listed for 88:7] قَالَ تَزْرَعُونَ سَبْعَ سِنِينَ دَأَبًۭا فَمَا حَصَدتُّمْ فَذَرُوهُ فِى سُنۢبُلِهِۦٓ إِلَّا قَلِيلًۭا مِّمَّا تَأْكُلُونَ
- (12:48) [listed for 88:7] [cited in ¶5] ثُمَّ يَأْتِى مِنۢ بَعْدِ ذَٰلِكَ سَبْعٌۭ شِدَادٌۭ يَأْكُلْنَ مَا قَدَّمْتُمْ لَهُنَّ إِلَّا قَلِيلًۭا مِّمَّا تُحْصِنُونَ
- (16:112) [listed for 88:7] [cited in ¶21] وَضَرَبَ ٱللَّهُ مَثَلًۭا قَرْيَةًۭ كَانَتْ ءَامِنَةًۭ مُّطْمَئِنَّةًۭ يَأْتِيهَا رِزْقُهَا رَغَدًۭا مِّن كُلِّ مَكَانٍۢ فَكَفَرَتْ بِأَنْعُمِ ٱللَّهِ فَأَذَٰقَهَا ٱللَّهُ لِبَاسَ ٱلْجُوعِ وَٱلْخَوْفِ بِمَا كَانُوا۟ يَصْنَعُونَ
- (22:28) [listed for 88:7] لِّيَشْهَدُوا۟ مَنَٰفِعَ لَهُمْ وَيَذْكُرُوا۟ ٱسْمَ ٱللَّهِ فِىٓ أَيَّامٍۢ مَّعْلُومَٰتٍ عَلَىٰ مَا رَزَقَهُم مِّنۢ بَهِيمَةِ ٱلْأَنْعَٰمِ ۖ فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْبَآئِسَ ٱلْفَقِيرَ
- (22:36) [listed for 88:7] وَٱلْبُدْنَ جَعَلْنَٰهَا لَكُم مِّن شَعَٰٓئِرِ ٱللَّهِ لَكُمْ فِيهَا خَيْرٌۭ ۖ فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ ۖ فَإِذَا وَجَبَتْ جُنُوبُهَا فَكُلُوا۟ مِنْهَا وَأَطْعِمُوا۟ ٱلْقَانِعَ وَٱلْمُعْتَرَّ ۚ كَذَٰلِكَ سَخَّرْنَٰهَا لَكُمْ لَعَلَّكُمْ تَشْكُرُونَ
- (36:47) [listed for 88:7] وَإِذَا قِيلَ لَهُمْ أَنفِقُوا۟ مِمَّا رَزَقَكُمُ ٱللَّهُ قَالَ ٱلَّذِينَ كَفَرُوا۟ لِلَّذِينَ ءَامَنُوٓا۟ أَنُطْعِمُ مَن لَّوْ يَشَآءُ ٱللَّهُ أَطْعَمَهُۥٓ إِنْ أَنتُمْ إِلَّا فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (69:34) [listed for 88:7] [cited in ¶17] وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- (76:8) [listed for 88:7] وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا وَأَسِيرًا
- (77:31) [listed for 88:7] [cited in ¶13] لَّا ظَلِيلٍۢ وَلَا يُغْنِى مِنَ ٱللَّهَبِ
- (80:24) [listed for 88:7] فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ
- (106:4) [listed for 88:7] [cited in ¶20] ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ

## medium (this ayah's own list) (46)

- (2:155) [listed for 88:7] وَلَنَبْلُوَنَّكُم بِشَىْءٍۢ مِّنَ ٱلْخَوْفِ وَٱلْجُوعِ وَنَقْصٍۢ مِّنَ ٱلْأَمْوَٰلِ وَٱلْأَنفُسِ وَٱلثَّمَرَٰتِ ۗ وَبَشِّرِ ٱلصَّٰبِرِينَ
- (2:254) [listed for 88:7] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَنفِقُوا۟ مِمَّا رَزَقْنَٰكُم مِّن قَبْلِ أَن يَأْتِىَ يَوْمٌۭ لَّا بَيْعٌۭ فِيهِ وَلَا خُلَّةٌۭ وَلَا شَفَٰعَةٌۭ ۗ وَٱلْكَٰفِرُونَ هُمُ ٱلظَّٰلِمُونَ
- (2:255) [listed for 88:7] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْحَىُّ ٱلْقَيُّومُ ۚ لَا تَأْخُذُهُۥ سِنَةٌۭ وَلَا نَوْمٌۭ ۚ لَّهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ مَن ذَا ٱلَّذِى يَشْفَعُ عِندَهُۥٓ إِلَّا بِإِذْنِهِۦ ۚ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ وَلَا يُحِيطُونَ بِشَىْءٍۢ مِّنْ عِلْمِهِۦٓ إِلَّا بِمَا شَآءَ ۚ وَسِعَ كُرْسِيُّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ ۖ وَلَا يَـُٔودُهُۥ حِفْظُهُمَا ۚ وَهُوَ ٱلْعَلِىُّ ٱلْعَظِيمُ
- (2:273) [listed for 88:7] لِلْفُقَرَآءِ ٱلَّذِينَ أُحْصِرُوا۟ فِى سَبِيلِ ٱللَّهِ لَا يَسْتَطِيعُونَ ضَرْبًۭا فِى ٱلْأَرْضِ يَحْسَبُهُمُ ٱلْجَاهِلُ أَغْنِيَآءَ مِنَ ٱلتَّعَفُّفِ تَعْرِفُهُم بِسِيمَٰهُمْ لَا يَسْـَٔلُونَ ٱلنَّاسَ إِلْحَافًۭا ۗ وَمَا تُنفِقُوا۟ مِنْ خَيْرٍۢ فَإِنَّ ٱللَّهَ بِهِۦ عَلِيمٌ
- (3:173) [listed for 88:7] ٱلَّذِينَ قَالَ لَهُمُ ٱلنَّاسُ إِنَّ ٱلنَّاسَ قَدْ جَمَعُوا۟ لَكُمْ فَٱخْشَوْهُمْ فَزَادَهُمْ إِيمَٰنًۭا وَقَالُوا۟ حَسْبُنَا ٱللَّهُ وَنِعْمَ ٱلْوَكِيلُ
- (4:130) [listed for 88:7] وَإِن يَتَفَرَّقَا يُغْنِ ٱللَّهُ كُلًّۭا مِّن سَعَتِهِۦ ۚ وَكَانَ ٱللَّهُ وَٰسِعًا حَكِيمًۭا
- (5:3) [listed for 88:7] حُرِّمَتْ عَلَيْكُمُ ٱلْمَيْتَةُ وَٱلدَّمُ وَلَحْمُ ٱلْخِنزِيرِ وَمَآ أُهِلَّ لِغَيْرِ ٱللَّهِ بِهِۦ وَٱلْمُنْخَنِقَةُ وَٱلْمَوْقُوذَةُ وَٱلْمُتَرَدِّيَةُ وَٱلنَّطِيحَةُ وَمَآ أَكَلَ ٱلسَّبُعُ إِلَّا مَا ذَكَّيْتُمْ وَمَا ذُبِحَ عَلَى ٱلنُّصُبِ وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ ۚ ذَٰلِكُمْ فِسْقٌ ۗ ٱلْيَوْمَ يَئِسَ ٱلَّذِينَ كَفَرُوا۟ مِن دِينِكُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِ ۚ ٱلْيَوْمَ أَكْمَلْتُ لَكُمْ دِينَكُمْ وَأَتْمَمْتُ عَلَيْكُمْ نِعْمَتِى وَرَضِيتُ لَكُمُ ٱلْإِسْلَٰمَ دِينًۭا ۚ فَمَنِ ٱضْطُرَّ فِى مَخْمَصَةٍ غَيْرَ مُتَجَانِفٍۢ لِّإِثْمٍۢ ۙ فَإِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (7:48) [listed for 88:7] وَنَادَىٰٓ أَصْحَٰبُ ٱلْأَعْرَافِ رِجَالًۭا يَعْرِفُونَهُم بِسِيمَىٰهُمْ قَالُوا۟ مَآ أَغْنَىٰ عَنكُمْ جَمْعُكُمْ وَمَا كُنتُمْ تَسْتَكْبِرُونَ
- (7:50) [listed for 88:7] وَنَادَىٰٓ أَصْحَٰبُ ٱلنَّارِ أَصْحَٰبَ ٱلْجَنَّةِ أَنْ أَفِيضُوا۟ عَلَيْنَا مِنَ ٱلْمَآءِ أَوْ مِمَّا رَزَقَكُمُ ٱللَّهُ ۚ قَالُوٓا۟ إِنَّ ٱللَّهَ حَرَّمَهُمَا عَلَى ٱلْكَٰفِرِينَ
- (8:62) [listed for 88:7] وَإِن يُرِيدُوٓا۟ أَن يَخْدَعُوكَ فَإِنَّ حَسْبَكَ ٱللَّهُ ۚ هُوَ ٱلَّذِىٓ أَيَّدَكَ بِنَصْرِهِۦ وَبِٱلْمُؤْمِنِينَ
- (8:64) [listed for 88:7] يَٰٓأَيُّهَا ٱلنَّبِىُّ حَسْبُكَ ٱللَّهُ وَمَنِ ٱتَّبَعَكَ مِنَ ٱلْمُؤْمِنِينَ
- (9:28) [listed for 88:7] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّمَا ٱلْمُشْرِكُونَ نَجَسٌۭ فَلَا يَقْرَبُوا۟ ٱلْمَسْجِدَ ٱلْحَرَامَ بَعْدَ عَامِهِمْ هَٰذَا ۚ وَإِنْ خِفْتُمْ عَيْلَةًۭ فَسَوْفَ يُغْنِيكُمُ ٱللَّهُ مِن فَضْلِهِۦٓ إِن شَآءَ ۚ إِنَّ ٱللَّهَ عَلِيمٌ حَكِيمٌۭ
- (9:74) [listed for 88:7] يَحْلِفُونَ بِٱللَّهِ مَا قَالُوا۟ وَلَقَدْ قَالُوا۟ كَلِمَةَ ٱلْكُفْرِ وَكَفَرُوا۟ بَعْدَ إِسْلَٰمِهِمْ وَهَمُّوا۟ بِمَا لَمْ يَنَالُوا۟ ۚ وَمَا نَقَمُوٓا۟ إِلَّآ أَنْ أَغْنَىٰهُمُ ٱللَّهُ وَرَسُولُهُۥ مِن فَضْلِهِۦ ۚ فَإِن يَتُوبُوا۟ يَكُ خَيْرًۭا لَّهُمْ ۖ وَإِن يَتَوَلَّوْا۟ يُعَذِّبْهُمُ ٱللَّهُ عَذَابًا أَلِيمًۭا فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۚ وَمَا لَهُمْ فِى ٱلْأَرْضِ مِن وَلِىٍّۢ وَلَا نَصِيرٍۢ
- (11:68) [listed for 88:7] كَأَن لَّمْ يَغْنَوْا۟ فِيهَآ ۗ أَلَآ إِنَّ ثَمُودَا۟ كَفَرُوا۟ رَبَّهُمْ ۗ أَلَا بُعْدًۭا لِّثَمُودَ
- (12:46) [listed for 88:7] يُوسُفُ أَيُّهَا ٱلصِّدِّيقُ أَفْتِنَا فِى سَبْعِ بَقَرَٰتٍۢ سِمَانٍۢ يَأْكُلُهُنَّ سَبْعٌ عِجَافٌۭ وَسَبْعِ سُنۢبُلَٰتٍ خُضْرٍۢ وَأُخَرَ يَابِسَٰتٍۢ لَّعَلِّىٓ أَرْجِعُ إِلَى ٱلنَّاسِ لَعَلَّهُمْ يَعْلَمُونَ
- (12:49) [listed for 88:7] ثُمَّ يَأْتِى مِنۢ بَعْدِ ذَٰلِكَ عَامٌۭ فِيهِ يُغَاثُ ٱلنَّاسُ وَفِيهِ يَعْصِرُونَ
- (12:68) [listed for 88:7] وَلَمَّا دَخَلُوا۟ مِنْ حَيْثُ أَمَرَهُمْ أَبُوهُم مَّا كَانَ يُغْنِى عَنْهُم مِّنَ ٱللَّهِ مِن شَىْءٍ إِلَّا حَاجَةًۭ فِى نَفْسِ يَعْقُوبَ قَضَىٰهَا ۚ وَإِنَّهُۥ لَذُو عِلْمٍۢ لِّمَا عَلَّمْنَٰهُ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (19:42) [listed for 88:7] إِذْ قَالَ لِأَبِيهِ يَٰٓأَبَتِ لِمَ تَعْبُدُ مَا لَا يَسْمَعُ وَلَا يُبْصِرُ وَلَا يُغْنِى عَنكَ شَيْـًۭٔا
- (20:118) [listed for 88:7] [cited in ¶22] إِنَّ لَكَ أَلَّا تَجُوعَ فِيهَا وَلَا تَعْرَىٰ
- (26:207) [listed for 88:7] مَآ أَغْنَىٰ عَنْهُم مَّا كَانُوا۟ يُمَتَّعُونَ
- (35:15) [listed for 88:7] [cited in ¶19] ۞ يَٰٓأَيُّهَا ٱلنَّاسُ أَنتُمُ ٱلْفُقَرَآءُ إِلَى ٱللَّهِ ۖ وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ
- (39:7) [listed for 88:7] إِن تَكْفُرُوا۟ فَإِنَّ ٱللَّهَ غَنِىٌّ عَنكُمْ ۖ وَلَا يَرْضَىٰ لِعِبَادِهِ ٱلْكُفْرَ ۖ وَإِن تَشْكُرُوا۟ يَرْضَهُ لَكُمْ ۗ وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۗ ثُمَّ إِلَىٰ رَبِّكُم مَّرْجِعُكُمْ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
- (40:47) [listed for 88:7] وَإِذْ يَتَحَآجُّونَ فِى ٱلنَّارِ فَيَقُولُ ٱلضُّعَفَٰٓؤُا۟ لِلَّذِينَ ٱسْتَكْبَرُوٓا۟ إِنَّا كُنَّا لَكُمْ تَبَعًۭا فَهَلْ أَنتُم مُّغْنُونَ عَنَّا نَصِيبًۭا مِّنَ ٱلنَّارِ
- (44:41) [listed for 88:7] يَوْمَ لَا يُغْنِى مَوْلًى عَن مَّوْلًۭى شَيْـًۭٔا وَلَا هُمْ يُنصَرُونَ
- (44:42) [listed for 88:7] إِلَّا مَن رَّحِمَ ٱللَّهُ ۚ إِنَّهُۥ هُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ
- (45:10) [listed for 88:7] مِّن وَرَآئِهِمْ جَهَنَّمُ ۖ وَلَا يُغْنِى عَنْهُم مَّا كَسَبُوا۟ شَيْـًۭٔا وَلَا مَا ٱتَّخَذُوا۟ مِن دُونِ ٱللَّهِ أَوْلِيَآءَ ۖ وَلَهُمْ عَذَابٌ عَظِيمٌ
- (45:19) [listed for 88:7] إِنَّهُمْ لَن يُغْنُوا۟ عَنكَ مِنَ ٱللَّهِ شَيْـًۭٔا ۚ وَإِنَّ ٱلظَّٰلِمِينَ بَعْضُهُمْ أَوْلِيَآءُ بَعْضٍۢ ۖ وَٱللَّهُ وَلِىُّ ٱلْمُتَّقِينَ
- (51:26) [listed for 88:7] [cited in ¶8] فَرَاغَ إِلَىٰٓ أَهْلِهِۦ فَجَآءَ بِعِجْلٍۢ سَمِينٍۢ
- (52:46) [listed for 88:7] يَوْمَ لَا يُغْنِى عَنْهُمْ كَيْدُهُمْ شَيْـًۭٔا وَلَا هُمْ يُنصَرُونَ
- (53:26) [listed for 88:7] ۞ وَكَم مِّن مَّلَكٍۢ فِى ٱلسَّمَٰوَٰتِ لَا تُغْنِى شَفَٰعَتُهُمْ شَيْـًٔا إِلَّا مِنۢ بَعْدِ أَن يَأْذَنَ ٱللَّهُ لِمَن يَشَآءُ وَيَرْضَىٰٓ
- (53:28) [listed for 88:7] [cited in ¶13] وَمَا لَهُم بِهِۦ مِنْ عِلْمٍ ۖ إِن يَتَّبِعُونَ إِلَّا ٱلظَّنَّ ۖ وَإِنَّ ٱلظَّنَّ لَا يُغْنِى مِنَ ٱلْحَقِّ شَيْـًۭٔا
- (53:48) [listed for 88:7] وَأَنَّهُۥ هُوَ أَغْنَىٰ وَأَقْنَىٰ
- (56:19) [listed for 88:7] لَّا يُصَدَّعُونَ عَنْهَا وَلَا يُنزِفُونَ
- (56:20) [listed for 88:7] وَفَٰكِهَةٍۢ مِّمَّا يَتَخَيَّرُونَ
- (56:21) [listed for 88:7] وَلَحْمِ طَيْرٍۢ مِّمَّا يَشْتَهُونَ
- (56:44) [listed for 88:7] [cited in ¶9] لَّا بَارِدٍۢ وَلَا كَرِيمٍ
- (69:28) [listed for 88:7] [cited in ¶17] مَآ أَغْنَىٰ عَنِّى مَالِيَهْ ۜ
- (78:24) [listed for 88:7] لَّا يَذُوقُونَ فِيهَا بَرْدًۭا وَلَا شَرَابًا
- (80:25) [listed for 88:7] أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا
- (80:27) [listed for 88:7] فَأَنۢبَتْنَا فِيهَا حَبًّۭا
- (89:17) [listed for 88:7] كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ
- (90:14) [listed for 88:7] أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ
- (92:8) [listed for 88:7] [cited in ¶16] وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ
- (93:8) [listed for 88:7] وَوَجَدَكَ عَآئِلًۭا فَأَغْنَىٰ
- (96:7) [listed for 88:7] [cited in ¶15] أَن رَّءَاهُ ٱسْتَغْنَىٰٓ
- (107:3) [listed for 88:7] وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ

## named by the passage's own list as strong for this ayah (10)

- (14:16) [listed for 88:7] مِّن وَرَآئِهِۦ جَهَنَّمُ وَيُسْقَىٰ مِن مَّآءٍۢ صَدِيدٍۢ
- (44:43) [listed for 88:7] إِنَّ شَجَرَتَ ٱلزَّقُّومِ
- (44:44) [listed for 88:7] طَعَامُ ٱلْأَثِيمِ
- (56:56) [listed for 88:7] [cited in ¶9] هَٰذَا نُزُلُهُمْ يَوْمَ ٱلدِّينِ
- (69:31) [listed for 88:7] ثُمَّ ٱلْجَحِيمَ صَلُّوهُ
- (69:36) [listed for 88:7] [cited in ¶17] وَلَا طَعَامٌ إِلَّا مِنْ غِسْلِينٍۢ
- (69:37) [listed for 88:7] لَّا يَأْكُلُهُۥٓ إِلَّا ٱلْخَٰطِـُٔونَ
- (73:13) [listed for 88:7] وَطَعَامًۭا ذَا غُصَّةٍۢ وَعَذَابًا أَلِيمًۭا
- (78:25) [listed for 88:7] إِلَّا حَمِيمًۭا وَغَسَّاقًۭا
- (78:30) [listed for 88:7] فَذُوقُوا۟ فَلَن نَّزِيدَكُمْ إِلَّا عَذَابًا

## named by the passage's own list as medium for this ayah (23)

- (3:88) [listed for 88:7] خَٰلِدِينَ فِيهَا لَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنظَرُونَ
- (7:41) [listed for 88:7] لَهُم مِّن جَهَنَّمَ مِهَادٌۭ وَمِن فَوْقِهِمْ غَوَاشٍۢ ۚ وَكَذَٰلِكَ نَجْزِى ٱلظَّٰلِمِينَ
- (12:43) [listed for 88:7] [cited in ¶5] وَقَالَ ٱلْمَلِكُ إِنِّىٓ أَرَىٰ سَبْعَ بَقَرَٰتٍۢ سِمَانٍۢ يَأْكُلُهُنَّ سَبْعٌ عِجَافٌۭ وَسَبْعَ سُنۢبُلَٰتٍ خُضْرٍۢ وَأُخَرَ يَابِسَٰتٍۢ ۖ يَٰٓأَيُّهَا ٱلْمَلَأُ أَفْتُونِى فِى رُءْيَٰىَ إِن كُنتُمْ لِلرُّءْيَا تَعْبُرُونَ
- (19:71) [listed for 88:7] وَإِن مِّنكُمْ إِلَّا وَارِدُهَا ۚ كَانَ عَلَىٰ رَبِّكَ حَتْمًۭا مَّقْضِيًّۭا
- (23:55) [listed for 88:7] أَيَحْسَبُونَ أَنَّمَا نُمِدُّهُم بِهِۦ مِن مَّالٍۢ وَبَنِينَ
- (25:13) [listed for 88:7] وَإِذَآ أُلْقُوا۟ مِنْهَا مَكَانًۭا ضَيِّقًۭا مُّقَرَّنِينَ دَعَوْا۟ هُنَالِكَ ثُبُورًۭا
- (26:79) [listed for 88:7] وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ
- (37:62) [listed for 88:7] أَذَٰلِكَ خَيْرٌۭ نُّزُلًا أَمْ شَجَرَةُ ٱلزَّقُّومِ
- (37:68) [listed for 88:7] ثُمَّ إِنَّ مَرْجِعَهُمْ لَإِلَى ٱلْجَحِيمِ
- (44:46) [listed for 88:7] كَغَلْىِ ٱلْحَمِيمِ
- (46:34) [listed for 88:7] وَيَوْمَ يُعْرَضُ ٱلَّذِينَ كَفَرُوا۟ عَلَى ٱلنَّارِ أَلَيْسَ هَٰذَا بِٱلْحَقِّ ۖ قَالُوا۟ بَلَىٰ وَرَبِّنَا ۚ قَالَ فَذُوقُوا۟ ٱلْعَذَابَ بِمَا كُنتُمْ تَكْفُرُونَ
- (55:44) [listed for 88:7] يَطُوفُونَ بَيْنَهَا وَبَيْنَ حَمِيمٍ ءَانٍۢ
- (56:52) [listed for 88:7] [cited in ¶9] لَءَاكِلُونَ مِن شَجَرٍۢ مِّن زَقُّومٍۢ
- (56:53) [listed for 88:7] [cited in ¶9] فَمَالِـُٔونَ مِنْهَا ٱلْبُطُونَ
- (56:54) [listed for 88:7] فَشَٰرِبُونَ عَلَيْهِ مِنَ ٱلْحَمِيمِ
- (56:94) [listed for 88:7] وَتَصْلِيَةُ جَحِيمٍ
- (70:15) [listed for 88:7] كَلَّآ ۖ إِنَّهَا لَظَىٰ
- (78:23) [listed for 88:7] لَّٰبِثِينَ فِيهَآ أَحْقَابًۭا
- (80:5) [listed for 88:7] أَمَّا مَنِ ٱسْتَغْنَىٰ
- (80:37) [listed for 88:7] لِكُلِّ ٱمْرِئٍۢ مِّنْهُمْ يَوْمَئِذٍۢ شَأْنٌۭ يُغْنِيهِ
- (82:14) [listed for 88:7] وَإِنَّ ٱلْفُجَّارَ لَفِى جَحِيمٍۢ
- (89:23) [listed for 88:7] وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- (111:3) [listed for 88:7] سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ

## weak (this ayah's own list) (28)

- (2:233) [listed for 88:7] ۞ وَٱلْوَٰلِدَٰتُ يُرْضِعْنَ أَوْلَٰدَهُنَّ حَوْلَيْنِ كَامِلَيْنِ ۖ لِمَنْ أَرَادَ أَن يُتِمَّ ٱلرَّضَاعَةَ ۚ وَعَلَى ٱلْمَوْلُودِ لَهُۥ رِزْقُهُنَّ وَكِسْوَتُهُنَّ بِٱلْمَعْرُوفِ ۚ لَا تُكَلَّفُ نَفْسٌ إِلَّا وُسْعَهَا ۚ لَا تُضَآرَّ وَٰلِدَةٌۢ بِوَلَدِهَا وَلَا مَوْلُودٌۭ لَّهُۥ بِوَلَدِهِۦ ۚ وَعَلَى ٱلْوَارِثِ مِثْلُ ذَٰلِكَ ۗ فَإِنْ أَرَادَا فِصَالًا عَن تَرَاضٍۢ مِّنْهُمَا وَتَشَاوُرٍۢ فَلَا جُنَاحَ عَلَيْهِمَا ۗ وَإِنْ أَرَدتُّمْ أَن تَسْتَرْضِعُوٓا۟ أَوْلَٰدَكُمْ فَلَا جُنَاحَ عَلَيْكُمْ إِذَا سَلَّمْتُم مَّآ ءَاتَيْتُم بِٱلْمَعْرُوفِ ۗ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ بِمَا تَعْمَلُونَ بَصِيرٌۭ
- (2:263) [listed for 88:7] ۞ قَوْلٌۭ مَّعْرُوفٌۭ وَمَغْفِرَةٌ خَيْرٌۭ مِّن صَدَقَةٍۢ يَتْبَعُهَآ أَذًۭى ۗ وَٱللَّهُ غَنِىٌّ حَلِيمٌۭ
- (2:267) [listed for 88:7] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَنفِقُوا۟ مِن طَيِّبَٰتِ مَا كَسَبْتُمْ وَمِمَّآ أَخْرَجْنَا لَكُم مِّنَ ٱلْأَرْضِ ۖ وَلَا تَيَمَّمُوا۟ ٱلْخَبِيثَ مِنْهُ تُنفِقُونَ وَلَسْتُم بِـَٔاخِذِيهِ إِلَّآ أَن تُغْمِضُوا۟ فِيهِ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ غَنِىٌّ حَمِيدٌ
- (3:10) [listed for 88:7] إِنَّ ٱلَّذِينَ كَفَرُوا۟ لَن تُغْنِىَ عَنْهُمْ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُم مِّنَ ٱللَّهِ شَيْـًۭٔا ۖ وَأُو۟لَٰٓئِكَ هُمْ وَقُودُ ٱلنَّارِ
- (4:6) [listed for 88:7] وَٱبْتَلُوا۟ ٱلْيَتَٰمَىٰ حَتَّىٰٓ إِذَا بَلَغُوا۟ ٱلنِّكَاحَ فَإِنْ ءَانَسْتُم مِّنْهُمْ رُشْدًۭا فَٱدْفَعُوٓا۟ إِلَيْهِمْ أَمْوَٰلَهُمْ ۖ وَلَا تَأْكُلُوهَآ إِسْرَافًۭا وَبِدَارًا أَن يَكْبَرُوا۟ ۚ وَمَن كَانَ غَنِيًّۭا فَلْيَسْتَعْفِفْ ۖ وَمَن كَانَ فَقِيرًۭا فَلْيَأْكُلْ بِٱلْمَعْرُوفِ ۚ فَإِذَا دَفَعْتُمْ إِلَيْهِمْ أَمْوَٰلَهُمْ فَأَشْهِدُوا۟ عَلَيْهِمْ ۚ وَكَفَىٰ بِٱللَّهِ حَسِيبًۭا
- (4:98) [listed for 88:7] إِلَّا ٱلْمُسْتَضْعَفِينَ مِنَ ٱلرِّجَالِ وَٱلنِّسَآءِ وَٱلْوِلْدَٰنِ لَا يَسْتَطِيعُونَ حِيلَةًۭ وَلَا يَهْتَدُونَ سَبِيلًۭا
- (5:76) [listed for 88:7] قُلْ أَتَعْبُدُونَ مِن دُونِ ٱللَّهِ مَا لَا يَمْلِكُ لَكُمْ ضَرًّۭا وَلَا نَفْعًۭا ۚ وَٱللَّهُ هُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (6:133) [listed for 88:7] وَرَبُّكَ ٱلْغَنِىُّ ذُو ٱلرَّحْمَةِ ۚ إِن يَشَأْ يُذْهِبْكُمْ وَيَسْتَخْلِفْ مِنۢ بَعْدِكُم مَّا يَشَآءُ كَمَآ أَنشَأَكُم مِّن ذُرِّيَّةِ قَوْمٍ ءَاخَرِينَ
- (7:92) [listed for 88:7] ٱلَّذِينَ كَذَّبُوا۟ شُعَيْبًۭا كَأَن لَّمْ يَغْنَوْا۟ فِيهَا ۚ ٱلَّذِينَ كَذَّبُوا۟ شُعَيْبًۭا كَانُوا۟ هُمُ ٱلْخَٰسِرِينَ
- (8:19) [listed for 88:7] إِن تَسْتَفْتِحُوا۟ فَقَدْ جَآءَكُمُ ٱلْفَتْحُ ۖ وَإِن تَنتَهُوا۟ فَهُوَ خَيْرٌۭ لَّكُمْ ۖ وَإِن تَعُودُوا۟ نَعُدْ وَلَن تُغْنِىَ عَنكُمْ فِئَتُكُمْ شَيْـًۭٔا وَلَوْ كَثُرَتْ وَأَنَّ ٱللَّهَ مَعَ ٱلْمُؤْمِنِينَ
- (9:93) [listed for 88:7] ۞ إِنَّمَا ٱلسَّبِيلُ عَلَى ٱلَّذِينَ يَسْتَـْٔذِنُونَكَ وَهُمْ أَغْنِيَآءُ ۚ رَضُوا۟ بِأَن يَكُونُوا۟ مَعَ ٱلْخَوَالِفِ وَطَبَعَ ٱللَّهُ عَلَىٰ قُلُوبِهِمْ فَهُمْ لَا يَعْلَمُونَ
- (10:36) [listed for 88:7] وَمَا يَتَّبِعُ أَكْثَرُهُمْ إِلَّا ظَنًّا ۚ إِنَّ ٱلظَّنَّ لَا يُغْنِى مِنَ ٱلْحَقِّ شَيْـًٔا ۚ إِنَّ ٱللَّهَ عَلِيمٌۢ بِمَا يَفْعَلُونَ
- (11:95) [listed for 88:7] كَأَن لَّمْ يَغْنَوْا۟ فِيهَآ ۗ أَلَا بُعْدًۭا لِّمَدْيَنَ كَمَا بَعِدَتْ ثَمُودُ
- (14:8) [listed for 88:7] وَقَالَ مُوسَىٰٓ إِن تَكْفُرُوٓا۟ أَنتُمْ وَمَن فِى ٱلْأَرْضِ جَمِيعًۭا فَإِنَّ ٱللَّهَ لَغَنِىٌّ حَمِيدٌ
- (15:84) [listed for 88:7] فَمَآ أَغْنَىٰ عَنْهُم مَّا كَانُوا۟ يَكْسِبُونَ
- (22:64) [listed for 88:7] لَّهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَإِنَّ ٱللَّهَ لَهُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ
- (24:33) [listed for 88:7] وَلْيَسْتَعْفِفِ ٱلَّذِينَ لَا يَجِدُونَ نِكَاحًا حَتَّىٰ يُغْنِيَهُمُ ٱللَّهُ مِن فَضْلِهِۦ ۗ وَٱلَّذِينَ يَبْتَغُونَ ٱلْكِتَٰبَ مِمَّا مَلَكَتْ أَيْمَٰنُكُمْ فَكَاتِبُوهُمْ إِنْ عَلِمْتُمْ فِيهِمْ خَيْرًۭا ۖ وَءَاتُوهُم مِّن مَّالِ ٱللَّهِ ٱلَّذِىٓ ءَاتَىٰكُمْ ۚ وَلَا تُكْرِهُوا۟ فَتَيَٰتِكُمْ عَلَى ٱلْبِغَآءِ إِنْ أَرَدْنَ تَحَصُّنًۭا لِّتَبْتَغُوا۟ عَرَضَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۚ وَمَن يُكْرِههُّنَّ فَإِنَّ ٱللَّهَ مِنۢ بَعْدِ إِكْرَٰهِهِنَّ غَفُورٌۭ رَّحِيمٌۭ
- (27:40) [listed for 88:7] قَالَ ٱلَّذِى عِندَهُۥ عِلْمٌۭ مِّنَ ٱلْكِتَٰبِ أَنَا۠ ءَاتِيكَ بِهِۦ قَبْلَ أَن يَرْتَدَّ إِلَيْكَ طَرْفُكَ ۚ فَلَمَّا رَءَاهُ مُسْتَقِرًّا عِندَهُۥ قَالَ هَٰذَا مِن فَضْلِ رَبِّى لِيَبْلُوَنِىٓ ءَأَشْكُرُ أَمْ أَكْفُرُ ۖ وَمَن شَكَرَ فَإِنَّمَا يَشْكُرُ لِنَفْسِهِۦ ۖ وَمَن كَفَرَ فَإِنَّ رَبِّى غَنِىٌّۭ كَرِيمٌۭ
- (32:19) [listed for 88:7] أَمَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَلَهُمْ جَنَّٰتُ ٱلْمَأْوَىٰ نُزُلًۢا بِمَا كَانُوا۟ يَعْمَلُونَ
- (39:36) [listed for 88:7] أَلَيْسَ ٱللَّهُ بِكَافٍ عَبْدَهُۥ ۖ وَيُخَوِّفُونَكَ بِٱلَّذِينَ مِن دُونِهِۦ ۚ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍۢ
- (40:82) [listed for 88:7] أَفَلَمْ يَسِيرُوا۟ فِى ٱلْأَرْضِ فَيَنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلَّذِينَ مِن قَبْلِهِمْ ۚ كَانُوٓا۟ أَكْثَرَ مِنْهُمْ وَأَشَدَّ قُوَّةًۭ وَءَاثَارًۭا فِى ٱلْأَرْضِ فَمَآ أَغْنَىٰ عَنْهُم مَّا كَانُوا۟ يَكْسِبُونَ
- (55:70) [listed for 88:7] فِيهِنَّ خَيْرَٰتٌ حِسَانٌۭ
- (58:17) [listed for 88:7] لَّن تُغْنِىَ عَنْهُمْ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُم مِّنَ ٱللَّهِ شَيْـًٔا ۚ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (59:7) [listed for 88:7] مَّآ أَفَآءَ ٱللَّهُ عَلَىٰ رَسُولِهِۦ مِنْ أَهْلِ ٱلْقُرَىٰ فَلِلَّهِ وَلِلرَّسُولِ وَلِذِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَٱبْنِ ٱلسَّبِيلِ كَىْ لَا يَكُونَ دُولَةًۢ بَيْنَ ٱلْأَغْنِيَآءِ مِنكُمْ ۚ وَمَآ ءَاتَىٰكُمُ ٱلرَّسُولُ فَخُذُوهُ وَمَا نَهَىٰكُمْ عَنْهُ فَٱنتَهُوا۟ ۚ وَٱتَّقُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
- (64:6) [listed for 88:7] ذَٰلِكَ بِأَنَّهُۥ كَانَت تَّأْتِيهِمْ رُسُلُهُم بِٱلْبَيِّنَٰتِ فَقَالُوٓا۟ أَبَشَرٌۭ يَهْدُونَنَا فَكَفَرُوا۟ وَتَوَلَّوا۟ ۚ وَّٱسْتَغْنَى ٱللَّهُ ۚ وَٱللَّهُ غَنِىٌّ حَمِيدٌۭ
- (70:10) [listed for 88:7] وَلَا يَسْـَٔلُ حَمِيمٌ حَمِيمًۭا
- (92:11) [listed for 88:7] [cited in ¶16] وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
- (111:2) [listed for 88:7] مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ

## named by the passage's own list as weak for this ayah (8)

- (20:119) [listed for 88:7] [cited in ¶22] وَأَنَّكَ لَا تَظْمَؤُا۟ فِيهَا وَلَا تَضْحَىٰ
- (24:32) [listed for 88:7] وَأَنكِحُوا۟ ٱلْأَيَٰمَىٰ مِنكُمْ وَٱلصَّٰلِحِينَ مِنْ عِبَادِكُمْ وَإِمَآئِكُمْ ۚ إِن يَكُونُوا۟ فُقَرَآءَ يُغْنِهِمُ ٱللَّهُ مِن فَضْلِهِۦ ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌۭ
- (29:6) [listed for 88:7] وَمَن جَٰهَدَ فَإِنَّمَا يُجَٰهِدُ لِنَفْسِهِۦٓ ۚ إِنَّ ٱللَّهَ لَغَنِىٌّ عَنِ ٱلْعَٰلَمِينَ
- (37:47) [listed for 88:7] لَا فِيهَا غَوْلٌۭ وَلَا هُمْ عَنْهَا يُنزَفُونَ
- (37:64) [listed for 88:7] إِنَّهَا شَجَرَةٌۭ تَخْرُجُ فِىٓ أَصْلِ ٱلْجَحِيمِ
- (68:18) [listed for 88:7] وَلَا يَسْتَثْنُونَ
- (84:12) [listed for 88:7] وَيَصْلَىٰ سَعِيرًا
- (87:13) [listed for 88:7] ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ

## neighbours: within two ayat of a passage the commentary cites (66)

- (6:12) [next to 6:14] قُل لِّمَن مَّا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ قُل لِّلَّهِ ۚ كَتَبَ عَلَىٰ نَفْسِهِ ٱلرَّحْمَةَ ۚ لَيَجْمَعَنَّكُمْ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَا رَيْبَ فِيهِ ۚ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ فَهُمْ لَا يُؤْمِنُونَ
- (6:13) [next to 6:14] ۞ وَلَهُۥ مَا سَكَنَ فِى ٱلَّيْلِ وَٱلنَّهَارِ ۚ وَهُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ
- (6:15) [next to 6:14] قُلْ إِنِّىٓ أَخَافُ إِنْ عَصَيْتُ رَبِّى عَذَابَ يَوْمٍ عَظِيمٍۢ
- (6:16) [next to 6:14] مَّن يُصْرَفْ عَنْهُ يَوْمَئِذٍۢ فَقَدْ رَحِمَهُۥ ۚ وَذَٰلِكَ ٱلْفَوْزُ ٱلْمُبِينُ
- (12:41) [next to 12:43] يَٰصَىٰحِبَىِ ٱلسِّجْنِ أَمَّآ أَحَدُكُمَا فَيَسْقِى رَبَّهُۥ خَمْرًۭا ۖ وَأَمَّا ٱلْءَاخَرُ فَيُصْلَبُ فَتَأْكُلُ ٱلطَّيْرُ مِن رَّأْسِهِۦ ۚ قُضِىَ ٱلْأَمْرُ ٱلَّذِى فِيهِ تَسْتَفْتِيَانِ
- (12:42) [next to 12:43] وَقَالَ لِلَّذِى ظَنَّ أَنَّهُۥ نَاجٍۢ مِّنْهُمَا ٱذْكُرْنِى عِندَ رَبِّكَ فَأَنسَىٰهُ ٱلشَّيْطَٰنُ ذِكْرَ رَبِّهِۦ فَلَبِثَ فِى ٱلسِّجْنِ بِضْعَ سِنِينَ
- (12:44) [next to 12:43] قَالُوٓا۟ أَضْغَٰثُ أَحْلَٰمٍۢ ۖ وَمَا نَحْنُ بِتَأْوِيلِ ٱلْأَحْلَٰمِ بِعَٰلِمِينَ
- (12:45) [next to 12:43] وَقَالَ ٱلَّذِى نَجَا مِنْهُمَا وَٱدَّكَرَ بَعْدَ أُمَّةٍ أَنَا۠ أُنَبِّئُكُم بِتَأْوِيلِهِۦ فَأَرْسِلُونِ
- (12:50) [next to 12:48] وَقَالَ ٱلْمَلِكُ ٱئْتُونِى بِهِۦ ۖ فَلَمَّا جَآءَهُ ٱلرَّسُولُ قَالَ ٱرْجِعْ إِلَىٰ رَبِّكَ فَسْـَٔلْهُ مَا بَالُ ٱلنِّسْوَةِ ٱلَّٰتِى قَطَّعْنَ أَيْدِيَهُنَّ ۚ إِنَّ رَبِّى بِكَيْدِهِنَّ عَلِيمٌۭ
- (16:110) [next to 16:112] ثُمَّ إِنَّ رَبَّكَ لِلَّذِينَ هَاجَرُوا۟ مِنۢ بَعْدِ مَا فُتِنُوا۟ ثُمَّ جَٰهَدُوا۟ وَصَبَرُوٓا۟ إِنَّ رَبَّكَ مِنۢ بَعْدِهَا لَغَفُورٌۭ رَّحِيمٌۭ
- (16:111) [next to 16:112] ۞ يَوْمَ تَأْتِى كُلُّ نَفْسٍۢ تُجَٰدِلُ عَن نَّفْسِهَا وَتُوَفَّىٰ كُلُّ نَفْسٍۢ مَّا عَمِلَتْ وَهُمْ لَا يُظْلَمُونَ
- (16:113) [next to 16:112] وَلَقَدْ جَآءَهُمْ رَسُولٌۭ مِّنْهُمْ فَكَذَّبُوهُ فَأَخَذَهُمُ ٱلْعَذَابُ وَهُمْ ظَٰلِمُونَ
- (16:114) [next to 16:112] فَكُلُوا۟ مِمَّا رَزَقَكُمُ ٱللَّهُ حَلَٰلًۭا طَيِّبًۭا وَٱشْكُرُوا۟ نِعْمَتَ ٱللَّهِ إِن كُنتُمْ إِيَّاهُ تَعْبُدُونَ
- (20:116) [next to 20:118] وَإِذْ قُلْنَا لِلْمَلَٰٓئِكَةِ ٱسْجُدُوا۟ لِءَادَمَ فَسَجَدُوٓا۟ إِلَّآ إِبْلِيسَ أَبَىٰ
- (20:117) [next to 20:118] فَقُلْنَا يَٰٓـَٔادَمُ إِنَّ هَٰذَا عَدُوٌّۭ لَّكَ وَلِزَوْجِكَ فَلَا يُخْرِجَنَّكُمَا مِنَ ٱلْجَنَّةِ فَتَشْقَىٰٓ
- (20:120) [next to 20:118] فَوَسْوَسَ إِلَيْهِ ٱلشَّيْطَٰنُ قَالَ يَٰٓـَٔادَمُ هَلْ أَدُلُّكَ عَلَىٰ شَجَرَةِ ٱلْخُلْدِ وَمُلْكٍۢ لَّا يَبْلَىٰ
- (20:121) [next to 20:119] فَأَكَلَا مِنْهَا فَبَدَتْ لَهُمَا سَوْءَٰتُهُمَا وَطَفِقَا يَخْصِفَانِ عَلَيْهِمَا مِن وَرَقِ ٱلْجَنَّةِ ۚ وَعَصَىٰٓ ءَادَمُ رَبَّهُۥ فَغَوَىٰ
- (35:13) [next to 35:15] يُولِجُ ٱلَّيْلَ فِى ٱلنَّهَارِ وَيُولِجُ ٱلنَّهَارَ فِى ٱلَّيْلِ وَسَخَّرَ ٱلشَّمْسَ وَٱلْقَمَرَ كُلٌّۭ يَجْرِى لِأَجَلٍۢ مُّسَمًّۭى ۚ ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ لَهُ ٱلْمُلْكُ ۚ وَٱلَّذِينَ تَدْعُونَ مِن دُونِهِۦ مَا يَمْلِكُونَ مِن قِطْمِيرٍ
- (35:14) [next to 35:15] إِن تَدْعُوهُمْ لَا يَسْمَعُوا۟ دُعَآءَكُمْ وَلَوْ سَمِعُوا۟ مَا ٱسْتَجَابُوا۟ لَكُمْ ۖ وَيَوْمَ ٱلْقِيَٰمَةِ يَكْفُرُونَ بِشِرْكِكُمْ ۚ وَلَا يُنَبِّئُكَ مِثْلُ خَبِيرٍۢ
- (35:16) [next to 35:15] إِن يَشَأْ يُذْهِبْكُمْ وَيَأْتِ بِخَلْقٍۢ جَدِيدٍۢ
- (35:17) [next to 35:15] وَمَا ذَٰلِكَ عَلَى ٱللَّهِ بِعَزِيزٍۢ
- (47:10) [next to 47:12] ۞ أَفَلَمْ يَسِيرُوا۟ فِى ٱلْأَرْضِ فَيَنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلَّذِينَ مِن قَبْلِهِمْ ۚ دَمَّرَ ٱللَّهُ عَلَيْهِمْ ۖ وَلِلْكَٰفِرِينَ أَمْثَٰلُهَا
- (47:11) [next to 47:12] ذَٰلِكَ بِأَنَّ ٱللَّهَ مَوْلَى ٱلَّذِينَ ءَامَنُوا۟ وَأَنَّ ٱلْكَٰفِرِينَ لَا مَوْلَىٰ لَهُمْ
- (47:13) [next to 47:12] وَكَأَيِّن مِّن قَرْيَةٍ هِىَ أَشَدُّ قُوَّةًۭ مِّن قَرْيَتِكَ ٱلَّتِىٓ أَخْرَجَتْكَ أَهْلَكْنَٰهُمْ فَلَا نَاصِرَ لَهُمْ
- (47:14) [next to 47:12] أَفَمَن كَانَ عَلَىٰ بَيِّنَةٍۢ مِّن رَّبِّهِۦ كَمَن زُيِّنَ لَهُۥ سُوٓءُ عَمَلِهِۦ وَٱتَّبَعُوٓا۟ أَهْوَآءَهُم
- (51:22) [next to 51:24] وَفِى ٱلسَّمَآءِ رِزْقُكُمْ وَمَا تُوعَدُونَ
- (51:23) [next to 51:24] فَوَرَبِّ ٱلسَّمَآءِ وَٱلْأَرْضِ إِنَّهُۥ لَحَقٌّۭ مِّثْلَ مَآ أَنَّكُمْ تَنطِقُونَ
- (51:25) [next to 51:24] إِذْ دَخَلُوا۟ عَلَيْهِ فَقَالُوا۟ سَلَٰمًۭا ۖ قَالَ سَلَٰمٌۭ قَوْمٌۭ مُّنكَرُونَ
- (51:28) [next to 51:26] فَأَوْجَسَ مِنْهُمْ خِيفَةًۭ ۖ قَالُوا۟ لَا تَخَفْ ۖ وَبَشَّرُوهُ بِغُلَٰمٍ عَلِيمٍۢ
- (51:29) [next to 51:27] فَأَقْبَلَتِ ٱمْرَأَتُهُۥ فِى صَرَّةٍۢ فَصَكَّتْ وَجْهَهَا وَقَالَتْ عَجُوزٌ عَقِيمٌۭ
- (53:27) [next to 53:28] إِنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ لَيُسَمُّونَ ٱلْمَلَٰٓئِكَةَ تَسْمِيَةَ ٱلْأُنثَىٰ
- (53:29) [next to 53:28] فَأَعْرِضْ عَن مَّن تَوَلَّىٰ عَن ذِكْرِنَا وَلَمْ يُرِدْ إِلَّا ٱلْحَيَوٰةَ ٱلدُّنْيَا
- (53:30) [next to 53:28] ذَٰلِكَ مَبْلَغُهُم مِّنَ ٱلْعِلْمِ ۚ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ وَهُوَ أَعْلَمُ بِمَنِ ٱهْتَدَىٰ
- (56:42) [next to 56:44] فِى سَمُومٍۢ وَحَمِيمٍۢ
- (56:43) [next to 56:44] وَظِلٍّۢ مِّن يَحْمُومٍۢ
- (56:46) [next to 56:44] وَكَانُوا۟ يُصِرُّونَ عَلَى ٱلْحِنثِ ٱلْعَظِيمِ
- (56:47) [next to 56:45] وَكَانُوا۟ يَقُولُونَ أَئِذَا مِتْنَا وَكُنَّا تُرَابًۭا وَعِظَٰمًا أَءِنَّا لَمَبْعُوثُونَ
- (56:50) [next to 56:52] لَمَجْمُوعُونَ إِلَىٰ مِيقَٰتِ يَوْمٍۢ مَّعْلُومٍۢ
- (56:51) [next to 56:52] ثُمَّ إِنَّكُمْ أَيُّهَا ٱلضَّآلُّونَ ٱلْمُكَذِّبُونَ
- (56:57) [next to 56:55] نَحْنُ خَلَقْنَٰكُمْ فَلَوْلَا تُصَدِّقُونَ
- (56:58) [next to 56:56] أَفَرَءَيْتُم مَّا تُمْنُونَ
- (69:23) [next to 69:25] قُطُوفُهَا دَانِيَةٌۭ
- (69:24) [next to 69:25] كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَآ أَسْلَفْتُمْ فِى ٱلْأَيَّامِ ٱلْخَالِيَةِ
- (69:26) [next to 69:25] وَلَمْ أَدْرِ مَا حِسَابِيَهْ
- (69:27) [next to 69:25] يَٰلَيْتَهَا كَانَتِ ٱلْقَاضِيَةَ
- (69:30) [next to 69:28] خُذُوهُ فَغُلُّوهُ
- (69:32) [next to 69:34] ثُمَّ فِى سِلْسِلَةٍۢ ذَرْعُهَا سَبْعُونَ ذِرَاعًۭا فَٱسْلُكُوهُ
- (69:33) [next to 69:34] إِنَّهُۥ كَانَ لَا يُؤْمِنُ بِٱللَّهِ ٱلْعَظِيمِ
- (69:35) [next to 69:34] فَلَيْسَ لَهُ ٱلْيَوْمَ هَٰهُنَا حَمِيمٌۭ
- (69:38) [next to 69:36] فَلَآ أُقْسِمُ بِمَا تُبْصِرُونَ
- (77:28) [next to 77:30] وَيْلٌۭ يَوْمَئِذٍۢ لِّلْمُكَذِّبِينَ
- (77:29) [next to 77:30] ٱنطَلِقُوٓا۟ إِلَىٰ مَا كُنتُم بِهِۦ تُكَذِّبُونَ
- (77:32) [next to 77:30] إِنَّهَا تَرْمِى بِشَرَرٍۢ كَٱلْقَصْرِ
- (77:33) [next to 77:31] كَأَنَّهُۥ جِمَٰلَتٌۭ صُفْرٌۭ
- (92:6) [next to 92:8] وَصَدَّقَ بِٱلْحُسْنَىٰ
- (92:7) [next to 92:8] فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
- (92:9) [next to 92:8] وَكَذَّبَ بِٱلْحُسْنَىٰ
- (92:10) [next to 92:8] فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- (92:12) [next to 92:11] إِنَّ عَلَيْنَا لَلْهُدَىٰ
- (92:13) [next to 92:11] وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- (96:4) [next to 96:6] ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ
- (96:5) [next to 96:6] عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ
- (96:9) [next to 96:7] أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ
- (96:10) [next to 96:8] عَبْدًا إِذَا صَلَّىٰٓ
- (106:0) [next to 106:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (106:1) [next to 106:2] لِإِيلَٰفِ قُرَيْشٍ

