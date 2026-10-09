Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 88:4; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/88_4/DM.r13.images.r13.map3.nohft.tool.tool.tool/88_4.reading.tr.md (prose paragraphs numbered) =====
## Ateşi yüklenmek

[¶1] Ayet üç kelimedir: {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşi yüklenir, ona girer, source:88:4}. Fiilin öznesi ikinci ayetteki yüzlerdir: {ar:وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ, tr:vucûhun yevmeizin hâşia, gloss:o gün birtakım yüzler eğik ve ezik, source:88:2}. Arapçada fiil dişil çekilmiştir ve bu yüzleri izler: üçüncü ayette çalışıp yorulan, burada ateşe giren, beşinci ayette kaynar bir pınardan içirilen hep aynı yüzlerdir. Yüz insanın karşıya dönük tarafıdır, ateşle ilk karşılaşan da odur. Kur'an başka bir yerde, terazisi hafif gelenlerin cehennemde kalacağını söyledikten hemen sonra, bu karşılaşmayı açıkça anlatır: {ar:تَلْفَحُ وُجُوهَهُمُ ٱلنَّارُ وَهُمْ فِيهَا كَٰلِحُونَ, tr:telfehu vucûhehumu'n-nâru ve hum fîhâ kâlihûn, gloss:ateş yüzlerini yalar, onlar orada yüzleri buruşmuş halde kalırlar, source:23:104}.

[¶2] Türkçe çeviri "kızgın bir ateşte yanar" der ve ateşi bir yer yapar. Arapçada ise ateş bir yer bildirmez; edatsız, doğrudan nesne olarak gelir. Yüzler ateşin "içinde" değildir yalnızca, ateşi alırlar, onu üstlenirler. Araplar bu fiili tam böyle kullanırdı: {ar:صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها, tr:salâ'l-kâfiru nâran fe-huve yaslâhâ ey kâsâ harrahâ ve şiddetehâ, gloss:kâfir ateşe girdi, yani onun sıcağını ve şiddetini çekti, source:"ص ل ي,B003"}. Fiil ateşin ne yaptığını değil, ateşe uğrayanın ne çektiğini anlatır. Bir başka kullanımda iş süreklilik kazanır: ateşe giren, ondan ayrılmayan kişidir, {ar:من يصلى في النار أي يلزم النار, tr:men yuslâ fi'n-nâri ey yelzemu'n-nâr, gloss:ateşe giren, yani ateşten ayrılmayan, source:"ص ل ي,B003"}. Fiil yalnız ateş için de kullanılmazdı. Ağır bir işin sıkıntısını çeken, bir belaya düşen kişi için de aynı fiil söylenirdi: {ar:صلي بالنار وبكذا أي بلي بها, tr:saliye bi'n-nâri ve bi-kezâ ey buliye bihâ, gloss:ateşle ya da şununla sınandı, ona uğradı, source:"ص ل ي,B003"}. Böylece ayetteki fiil bir yanma anını değil, bir katlanma halini adlandırır.

[¶3] Fiilin şimdiki-geniş zaman kipi de bu hali açık bırakır. Ayet bir başlangıç ya da bitiş göstermez; yüzler ateşi yüklenmektedir. Kur'an bu açıklığın nasıl işlediğini, ayetlerini inkâr edenler için Allah'ın sözüyle anlatır: {ar:سَوْفَ نُصْلِيهِمْ نَارًۭا كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا, tr:sevfe nuslîhim nâran küllemâ nadicet cülûduhum beddelnâhum cülûden ğayrahâ, gloss:onlara bir ateşi yükleteceğiz; derileri piştikçe yerine başka deriler koyacağız, source:4:56}. Aynı kalıp, fiil ve ardından belirsiz bir ateş, Kur'an'da birkaç kez tekrar eder. Malı kendisine hiçbir yarar sağlamayan Ebû Leheb için {ar:سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ, tr:se-yaslâ nâran zâte leheb, gloss:alevli bir ateşi yüklenecek, source:111:3} denir. Kitabı arkasından verilen kişi için de {ar:وَيَصْلَىٰ سَعِيرًا, tr:ve yaslâ saîrâ, gloss:alevlenmiş bir ateşe girer, source:84:12} denir. Bir önceki surede ise ateş belirlidir ve sıfatı "en büyük"tür: {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasla'n-nâre'l-kübrâ, gloss:en büyük ateşe girecek olan, source:87:12}. Bizim ayetimizde ateş belirsizdir: "bir ateş". Adı konmamış, tarif edilmemiştir; yalnızca tek bir sıfatı vardır. Belirsizlik ateşi küçültmez, kavranamaz bırakır. Sıfat ise ateşin ne olduğunu değil, ne halde olduğunu söyler.

## Yakıt, kebap ve kamp

[¶4] Bir kelimenin akrabalarından gelen resimler, o kelimenin ayetteki anlamının yerine geçmez; ayetteki "ateşi yüklenmek" anlamının yanında duyulur. Ateşe girme fiilinin harfleri, çöl hayatında ateşin çevresindeki her şeyi adlandırırdı. Yakıta ad verirdi: {ar:الصلاء ما يصطلى به وما يذكى به النار ويوقد, tr:es-silâu mâ yustalâ bihî ve mâ yuzkâ bihi'n-nâru ve yûkad, gloss:silâ, başında ısınılan, ateşin onunla canlandırılıp tutuşturulduğu yakıttır, source:"ص ل ي,B004"}. Ateşte pişen ete ad verirdi: {ar:صليت اللحم صليا شويته, tr:saleytü'l-lahme salyen şeveytüh, gloss:eti ateşte kızarttım, source:"ص ل ي,B004"}. Bir ustalık işine de ad verirdi. Eğri bir değneği düzeltmek isteyen kişi onu ateşin üstünde döndürür; ısınan tahta yumuşar, el onu sıcakken doğrultur, soğuyunca da o biçimde kalır: {ar:صلى عصاه إذا أدارها على النار يثقفها, tr:salâ asâhu izâ edârahâ ale'n-nâri yusakkıfuhâ, gloss:değneğini ateşin üstünde döndürüp doğrulttu, source:"ص ل ي,B004"}. Bu kullanımda ateş eğriyi düzelten bir araçtır. Aynı harfler develerin otladığı iri başaklı bir bitkiye de ad verirdi; Araplar bu bitkiyi develerin ekmeği diye anardı: {ar:تسميها العرب خبزة الإبل, tr:tüsemmîhe'l-arabu hubzete'l-ibil, gloss:Araplar ona develerin ekmeği der, source:"ص ل ي,B010"}. Bir konak yeri için gereken her şey, ısınılacak ateş, yakıt, kızarmış et, sürünün yemi, bu harflerle anılır. Dördüncü ayetten başlayarak sure bu konağın nimetlerini tersine çevirir: ateş ısıtmaz yakar, beşinci ayetteki pınar serinletmez kaynar, altıncı ve yedinci ayetteki yiyecek doyurmaz.

[¶5] Yakıt resmi bir adım daha ilerler. Yakıtı tarif eden cümledeki "tutuşturulmak" fiili, Kur'an'ın bir ateşin yakıtı için kullandığı kelimeyle aynı köktendir. Allah müminlere şöyle seslenir: {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:kû enfusekum ve ehlîkum nâran vekûduhe'n-nâsu ve'l-hicâra, gloss:kendinizi ve ailenizi yakıtı insanlar ve taşlar olan bir ateşten koruyun, source:66:6}. Orada da ateş belirsizdir ve yakıtı insandır. Ebû Leheb'in karısı da Kur'an'da odun taşıyıcısı olarak anılır {source:111:4}. Ateşe girme fiilinin ailesinde ateşi çeken ile ateşi besleyen yakıt aynı harflerle adlandırılır. Bu bir köken iddiası değildir; iki kullanımın yan yana duyulmasıdır. Ama yan yana duyulduğunda ayetteki yüz ateşin karşısında duran bir seyirci gibi değil, ateşin içine katılan bir şey gibi görünür.

[¶6] Aynı harfler av için kurulan kapanı da adlandırırdı: {ar:المصالي شبيهة بالشرك تنصب للطير وغيرها, tr:el-masâlî şebîhetün bi'ş-şereki tunsabu li't-tayri ve ğayrihâ, gloss:masâlî, kuş ve başka hayvanlar için kurulan tuzağa benzer kapanlardır, source:"ص ل ي,B005"}. Kapan önceden kurulur ve bekler; kuş kendi ayağıyla girer, kapan ancak o zaman kapanır. Bu harflerle birini yıkıma düşürecek gizli bir düzen kurmak da anlatılırdı {source:"ص ل ي,B005"}. Kapanı tarif eden "kurmak" fiili, üçüncü ayette yüzlerin yorgunluğunu anlatan kelimeyle aynı köktendir; bu iki komşu ayet yan yana okunduğunda kendi kurduğu kapana yürüyen bir yorgunluk duyulur. Ayetin söylediği yine ateştir; kapan yalnızca ateşe nasıl varıldığını sezdiren bir yan resimdir.

## Uzaktan görülen ateş

[¶7] Ateşin adı ile ışığın adı aynı köktendir. Araplar ikisinin de aynı işten adını aldığını söylerdi: {ar:النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة, tr:en-nûru ve'n-nâru summiyâ bi-zâlike min tarîkati'l-idâeti ve li-enne zâlike yekûnu muzdariben serîa'l-hareke, gloss:ışık ve ateş, aydınlatmalarından ve kıpır kıpır, hızla hareket etmelerinden ötürü bu adları aldı, source:"ن و ر,B002"}. Kökün özü de böyle tarif edilirdi: {ar:أصل صحيح يدل على إضاءة واضطراب وقلة ثبات, tr:aslun sahîhun yedullü alâ idâetin ve'dtırâbin ve killeti sebât, gloss:aydınlığı, çalkantıyı ve kararsızlığı gösteren sağlam kök, source:"ن و ر,B001"}. Türkçede "nur" kutsal bir aydınlığa daralmış, ateşle bağını yitirmiştir. Arapçada ise nûr ile nâr aynı titreyen, hiç durmayan alevin iki yüzüdür: biri aydınlatır, öteki yakar.

[¶8] Çöl yolcusu için gecenin ateşi uzaktan görülen bir işaretti. Araplar karanlıkta bir ateşi uzaktan seçip ona yönelmeyi ayrı bir fiille anlatırdı: {ar:تنورت نارا قصدت إليها, tr:tenevvertü nâran kasadtü ileyhâ, gloss:bir ateşi gözümle seçip ona yöneldim, source:"ن و ر,B003"}; {ar:تنورت النار من بعيد, tr:tenevverte'n-nâra min baîd, gloss:ateşi uzaktan seçtin, source:"ن و ر,B003"}. Yol gösteren yüksek yerlere bilerek ateş yakılırdı: {ar:كانوا ينورون في الجاهلية ليهتدى ويقتدى بها, tr:kânû yunevvirûne fi'l-câhiliyyeti li-yuhtedâ ve yuktedâ bihâ, gloss:cahiliye döneminde yol bulunsun ve izlensin diye ateş yakarlardı, source:"ن و ر,B005"}. Ateşe yaklaşıp başında ısınmak ise, ayetteki fiilin kendi ailesinden bir kelimeyle söylenirdi: {ar:واصطلى بها, tr:ve'stalâ bihâ, gloss:ve onunla ısındı, source:"ص ل ي,B003"}.

[¶9] Kur'an bu çöl ateşini bir peygamberin hikâyesinde anlatır. Musa, süresini tamamlayıp ailesiyle yola çıktığında Tûr'un yanında bir ateş görür ve ailesine şöyle der: {ar:ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ جَذْوَةٍۢ مِّنَ ٱلنَّارِ لَعَلَّكُمْ تَصْطَلُونَ, tr:umkusû innî ânestü nâran lealli âtîkum minhâ bi-haberin ev cezvetin mine'n-nâri lealleküm tastalûn, gloss:burada kalın, ben bir ateş gördüm; belki oradan size bir haber ya da bir ateş koru getiririm de ısınırsınız, source:28:29}. Aynı anın bir başka anlatımında umduğu şey yol bulmaktır: {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ev ecidu ale'n-nâri hudâ, gloss:ya da ateşin başında bir yol gösterici bulurum, source:20:10}. Musa'nın ateşi uzaktan görülür, ona yaklaşılır; ısıtır, haber verir, yol gösterir. "Isınırsınız" diye çevrilen fiil, dördüncü ayetteki "yüklenir" fiiliyle aynı köktendir. İki fiil arasındaki fark mesafedir. Isınan, ateşin başında oturur; ayetteki yüzler ise ateşin kendisini almıştır. Uzaktan seçilecek, yönelinecek, başında haber beklenecek bir aralık kalmamıştır.

[¶10] Kur'an dünyadaki ateşin bu işini bir hatırlatma olarak da anar. Vâkıa suresinde Allah, toprak ve kemik olduktan sonra diriltilmeyi soranlara {source:56:47} ektikleri tohumu, içtikleri suyu sorar ve sonunda ateşe gelir: {ar:أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ, tr:e-fe-raeytumu'n-nâra'lletî tûrûn, gloss:çakıp yaktığınız ateşi gördünüz mü, source:56:71}; {ar:نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا لِّلْمُقْوِينَ, tr:nahnu cealnâhâ tezkiraten ve metâan li'l-mukvîn, gloss:onu bir hatırlatma ve ıssız yerlerde kalanlar için bir yararlanma kıldık, source:56:73}. Ayet ateşin neyi hatırlattığını söylemez. Ama yolcunun başında ısındığı ateş, insanın elinde tuttuğu küçük bir örnektir ve dördüncü ayetteki ateş o örneğin bilinmeyen büyüğüdür. Surenin yirmi birinci ayetinde Peygamber'e verilen görev de aynı kökün sözüdür: {ar:فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ, tr:fe-zekkir innemâ ente müzekkir, gloss:hatırlat, sen yalnızca hatırlatıcısın, source:88:21}.

## Kızgın: fırın, demir ve damga

[¶11] Ateşin sıcak olduğunu söylemek gereksiz görünebilir. Ama hâmiye yalnızca "sıcak" demek değildir; sıcaklığı yükselmiş, kızmış olanı anlatır: {ar:الحامية الحارة, tr:el-hâmiyetü'l-hârra, gloss:hâmiye sıcak olandır, source:"ح م ي,B001"}; {ar:حمى النهار وحمي التنور أي اشتد حره, tr:hamiye'n-nehâru ve hamiye't-tennûru ey iştedde harruh, gloss:gün kızdı, tandır kızdı, yani sıcağı şiddetlendi, source:"ح م ي,B001"}. Kelimenin en elle tutulur kullanımı demirciden gelir: {ar:أحميت الحديد في النار فهو محمى, tr:ahmeytü'l-hadîde fi'n-nâri fe-huve muhmâ, gloss:demiri ateşte kızdırdım, o artık kızgındır, source:"ح م ي,B001"}. Demir ateşe sokulur, rengi değişir, kızarır, yumuşar. Hâmiye bir ateşin bu kızdırma gücünü taşır: içine konanı kızdıracak kadar kızmış bir ateştir. Araplar koşudan ısınıp terleyen at için de aynı fiili kullanırdı: {ar:حمي الفرس إذا عرق يحمى حميا, tr:hamiye'l-ferasu izâ arika yahmâ hamyen, gloss:at terlediğinde hamiye denir, source:"ح م ي,B001"}. Bu sıcaklık emekten doğar; üçüncü ayetteki yüzler çalışıp yorulmuştu, ama dördüncü ayette onları saran sıcaklık kendi koşularının sıcağı değil, ateşinkidir.

[¶12] Kur'an aynı iki kelimeyi başka bir surede bir tanım olarak kullanır. Kâria suresinde tartıları hafif gelen kişinin sığınağı, "anası" bir uçurum olarak anılır; ardından sorulur ve cevap verilir: {ar:وَمَآ أَدْرَىٰكَ مَا هِيَهْ, tr:ve mâ edrâke mâ hiyeh, gloss:onun ne olduğunu sana ne bildirdi, source:101:10}; {ar:نَارٌ حَامِيَةٌۢ, tr:nârun hâmiye, gloss:kızgın bir ateş, source:101:11}. Orada da ateş belirsizdir ve tek sıfatı budur. Kur'an bilinmeyeni bu iki kelimeyle tanımlar; Gâşiye de aynı iki kelimeyle yetinir.

[¶13] Kızdırma bazen arıtır. Altın ve gümüş için şöyle denirdi: {ar:هذا الذهب والفضة لحسن الحماء أي خرج من الحماء حسنا, tr:hâze'z-zehebu ve'l-fiddatu le-hasenü'l-hamâ' ey harace mine'l-hamâi hasenâ, gloss:bu altın ve gümüş kızdırmadan güzel çıkmıştır, source:"ح م ي,B001"}. Kuyumcunun ateşi madeni temizler. Kur'an aynı kızdırma fiilini altın ve gümüşle birlikte kullanır, ama orada ateş arıtmaz. Allah müminlere, insanların mallarını haksızca yiyenleri anlattıktan sonra altın ve gümüşü yığıp Allah yolunda harcamayanları acı bir azapla müjdelemesini söyler {source:9:34} ve o azabı şöyle tarif eder: {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhuhum ve cunûbuhum ve zuhûruhum, gloss:o gün bunlar cehennem ateşinde kızdırılır ve onlarla alınları, yanları ve sırtları dağlanır, source:9:35}. Yığılmış altın, arıtılacak bir maden olmaktan çıkıp dağlama demiri olur.

[¶14] Bu dağlama, ateşin adının kendisinde de vardır. Araplar bir devenin damgasını ateşin adıyla anardı: {ar:ما نار هذه الناقة أي ما سمتها, tr:mâ nâru hâzihi'n-nâkati ey mâ simetühâ, gloss:bu devenin ateşi ne, yani damgası ne, source:"ن و ر,B002"}. Damganın işi şöyledir: sahip demiri ateşte kızdırır ve devenin derisine bastırır; yanık iz kalıcı olur ve hayvanın kime, hangi sürüye ait olduğunu söyler. Bu yüzden şöyle denirdi: {ar:نجارها نارها, tr:nicâruhâ nâruhâ, gloss:soyu damgasıdır, source:"ن و ر,B002"}. Ateşin bıraktığı iz, kimin neye ait olduğunun okunduğu yerdir. Dokuzuncu surenin ayeti de dağlamanın ardından bunu söyler: {ar:هَٰذَا مَا كَنَزْتُمْ لِأَنفُسِكُمْ, tr:hâzâ mâ keneztum li-enfusikum, gloss:bu, kendiniz için yığdığınız şeydir, source:9:35}. Damga orada da bir aidiyeti okur; ve ilk dağlanan yer alındır, yani yüzdür. Gâşiye'nin ikinci ayetindeki yüzler, dördüncü ayette kızgın bir ateşi yüklenirken, bu ateş adının bir kullanımında yüzü taşıyanın kime ait olduğunu yazan bir damgadır. Ayetteki anlam yine ateştir; damga, ateşin adının yanında duyulan bir resimdir.

## Koruyan harfler, içten kızan yürek

[¶15] Hâmiye'nin harfleri Türkçeye tanıdık kelimeler vermiştir: himaye, hâmi, hamiyet. Türkçede himaye korumaktır, hamiyet ise övülen bir onur gayretidir. Türkçe bu kelimelerde sıcaklığı tamamen yitirmiştir. Arapçada ise aynı harfler hem kızmayı hem korumayı adlandırırdı; Araplar ikisini de kullanırdı ve biri ötekinin yerine geçmezdi.

[¶16] Koruma yüzünde bu harfler bir yeri adlandırırdı: {ar:الحمى موضع فيه كلأ يحمى من الناس أن يرعى, tr:el-himâ mevziun fîhi keleun yuhmâ mine'n-nâsi en yur'â, gloss:himâ, otu olup insanların otlatmasından korunan yerdir, source:"ح م ي,B002"}. Himâ çölde sınırı belli, otu bol, ama hayvan sokulmayan bir alandır; ona dokunulmaz, yaklaşılmaz: {ar:هذا شيء حمى أي محظور لا يقرب, tr:hâzâ şey'un himen ey mahzûrun lâ yukrab, gloss:bu korunmuş bir şeydir, yani yasaktır, ona yaklaşılmaz, source:"ح م ي,B002"}. Aynı fiil hastayı zararlı yiyecekten uzak tutmayı da anlatırdı: {ar:حميت المريض حمية منعته أكل ما يضره, tr:hameytü'l-marîda himyeten mena'tuhû ekle mâ yadurruh, gloss:hastayı perhize soktum, ona zarar vereni yemesini engelledim, source:"ح م ي,B002"}. Korumak, bir şeyi yaklaşmaması gereken şeyden uzak tutmaktır. Ayetteki ateş ise uzak tutulamamış olandır. Kur'an müminlere bir ateşten kendilerini ve ailelerini korumalarını buyurur {source:66:6}; o ayetteki fiil başka bir köktendir, ama yaptığı iş himâyı kuranın işidir. Onuncu ayetteki bahçe de kökünde örten, gölgeleyen bir yerdir; dördüncü ayetteki yüzler için ise koruyan hiçbir şey kalmamıştır.

[¶17] Isınma yüzünde ise bu harfler dışarıdaki bir ateşle sınırlı kalmazdı; içten yükselen, yayılan bir sıcağı da anlatırdı. Akrebin ve yılanın zehri için şöyle denirdi: {ar:هي فوعة السم أي حرارته وفورته, tr:hiye fev'atü's-sem ey harâratühû ve fevratüh, gloss:o, zehrin kabarışı, yani sıcaklığı ve kaynamasıdır, source:"ح م ي,B007"}. İçkinin içene yayılan ilk dalgası ve ağrının kabaran keskinliği de aynı harflerle adlandırılırdı: {ar:حميا الكأس أول سورتها, tr:humeyye'l-ke'si evvelü sevratihâ, gloss:kadehin humeyyâsı, onun ilk saldırışıdır, source:"ح م ي,B008"}; {ar:حموة الألم سورته, tr:hamvetü'l-elemi sevratüh, gloss:ağrının hamvesi kabarmasıdır, source:"ح م ي,B008"}. Öfke de bu kabarıştır: {ar:حميت عن كذا حمية ومحمية إذا أنفت منه وداخلك عار وأنفة, tr:hamîtü an kezâ hamiyyeten ve mahmiyyeten izâ enifte minhu ve dâhaleke ârun ve enefe, gloss:bir şeye karşı hamiyyet duydun, yani ondan burun kıvırdın, içine utanç ve kibir girdi, source:"ح م ي,B003"}. Türkçenin övdüğü hamiyet, Arapçada önce içe giren ve orada kızışan bir sıcaktır; neye karşı duyulduğuna göre övülür ya da yerilir.

[¶18] Kur'an bu iç sıcağını inkâr edenlerin yüreğine yerleştirir. Mescid-i Haram'a gitmek isteyen müminleri oradan engelleyen ve kurbanlık hayvanları yerine ulaşmaktan alıkoyanları anlattıktan sonra {source:48:25} şöyle der: {ar:إِذْ جَعَلَ ٱلَّذِينَ كَفَرُوا۟ فِى قُلُوبِهِمُ ٱلْحَمِيَّةَ حَمِيَّةَ ٱلْجَٰهِلِيَّةِ فَأَنزَلَ ٱللَّهُ سَكِينَتَهُۥ عَلَىٰ رَسُولِهِۦ وَعَلَى ٱلْمُؤْمِنِينَ, tr:iz cealellezîne keferû fî kulûbihimu'l-hamiyyete hamiyyete'l-câhiliyyeti fe-enzelallâhu sekînetehû alâ rasûlihî ve ale'l-mü'minîn, gloss:inkâr edenler yüreklerine kızgınlığı, cahiliye kızgınlığını koyduğunda Allah da elçisine ve müminlere sükûnetini indirdi, source:48:26}. Ayette iki şey karşı karşıyadır: aşağıda, yüreklerde kızışan bir sıcak; yukarıdan inen bir dinginlik. Hamiyye kelimesi hâmiye ile aynı köktendir, aynı kelime değildir; ayetler de birbirine değinmez. Ama yan yana duyulduklarında, yirmi üçüncü ayetteki yüz çeviren ve inkâr eden kişinin {ar:إِلَّا مَن تَوَلَّىٰ وَكَفَرَ, tr:illâ men tevellâ ve kefer, gloss:yüz çevirip inkâr eden müstesna, source:88:23} dünyada içinde taşıdığı kızgınlık ile dördüncü ayette yüzlerin yüklendiği kızgın ateş aynı harflerle konuşur. Biri içten yükselir ve kişi onu kendi yüreğine koyar; öteki dışarıdan kuşatır ve yüz onu yüklenir.

## Namaz ve ateş

[¶19] Ayetteki fiilin harfleri Arapçada bir başka büyük kelimeyi de taşır: namaz. Rükû ve secdeden oluşan ibadet bu harflerle anılırdı: {ar:الصلاة التي جاء بها الشرع من الركوع والسجود, tr:es-salâtü'lletî câe bihe'ş-şer'u mine'r-rukûi ve's-sucûd, gloss:dinin getirdiği, rükû ve secdeden oluşan namaz, source:"ص ل ي,B001"}. Aynı kelime, öznesi Allah ya da melekler olduğunda başka bir anlam kazanırdı: {ar:الصلاة من الملائكة دعاء واستغفار ومن الله سبحانه رحمة, tr:es-salâtü mine'l-melâiketi duâun ve'stiğfârun ve mina'llâhi subhânehû rahme, gloss:meleklerden gelen salât dua ve bağış dilemek, Allah'tan gelen salât ise rahmettir, source:"ص ل ي,B002"}. Ateşe girmek ile namaz aynı harflerle yazılır. Biri ötekinden türemiş değildir; iki ayrı kullanım yan yana durur ve birlikte duyulur.

[¶20] Kur'an bu iki kullanımı, ayetimizin iki köküyle birlikte, tam ters yönde işleyen bir cümlede bir araya getirir. Allah müminlere kendisini çokça anmalarını, sabah akşam tesbih etmelerini söyledikten sonra şöyle der: {ar:هُوَ ٱلَّذِى يُصَلِّى عَلَيْكُمْ وَمَلَٰٓئِكَتُهُۥ لِيُخْرِجَكُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ, tr:huve'llezî yusallî aleykum ve melâiketuhû li-yuhricekum mine'z-zulumâti ile'n-nûr, gloss:sizi karanlıklardan aydınlığa çıkarmak için size rahmet eden O'dur, melekleri de sizin için dua eder, source:33:43}. Bu ayette "salât" fiili ve nûr kelimesi vardır; dördüncü ayette aynı iki kökten "ateşi yüklenmek" ve nâr. Birinde Allah'ın rahmeti insanları alıp aydınlığa çıkarır. Ötekinde yüzler, aydınlığın kardeşi olan ateşi bir yük olarak alır. Harfler aynıdır, yön terstir: biri karanlıktan ışığa doğru bir çıkış, öteki ateşin içine bir giriş.

[¶21] Bir önceki sure bu iki kullanımı birkaç ayet arayla yan yana koymuştu: en büyük ateşe girecek olan bedbahttan söz ettikten sonra {source:87:12}, kurtuluşa ereni şöyle anar: {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve zekera'sme rabbihî fe-sallâ, gloss:Rabbinin adını anıp namaz kıldı, source:87:15}. Gâşiye'de ise dördüncü ayetin fiili, ikinci ayetin eğik yüzü ve üçüncü ayetin ayakta yorulan yüzüyle birlikte, rükûyu, kıyamı ve namazı yan anlam olarak taşıyan üç kelimelik bir dizinin son halkasıdır. Ayetin söylediği, bu yüzlerin ateşi yüklendiğidir. Ama yüklenme fiilinin harflerinde, bir zamanlar bu yüzlere açık duran öteki yol, rahmetle aydınlığa çıkaran salât, sessizce durmaya devam eder.

===== _commentary/v16/out/88_4/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: kālihūn (23:104) = faces shrunk, lips drawn back
- memory: tūrūn (56:71) = strike/kindle fire
- memory: muqwīn (56:73) = those in empty desert / without provision
- memory: ānastu = perceived from afar; jadhwa = live ember
- memory: tukwā (9:35) = branded with hot iron
- memory: iṣṭalā / taṣṭalūn is form VIII of the same root as taṣlā
- memory: waqūd (66:6) and yūqad share root w-q-d
- memory: hāwiya (101:9) rendered as abyss/chasm
- memory: Turkish himaye, hâmi, hamiyet derive from ḥ-m-y
- memory: sakīna = stillness, calm
- not written: variant reading tuṣlā (passive) - a report outside the Quran text
- not written: ṣ-l-y B006 rump, B007 second horse, B008 temple, B009 pounding stone - no work in a theme
- not written: n-w-r B004 blossom, B006 shying away, B007 feud, B009 depilatory, B010, B011 - no work in a theme
- not written: n-w-r B008 tattoo soot pricked into skin - would duplicate the brand image
- not written: ḥ-m-y B004 in-laws, B006 black mud, B009 calf muscle, B010 hoof edges, B011 well-lining stones, B012 blackening - no work in a theme
- not written: ḥ-m-y B005 ḥāmī stud camel (5:103) - protection theme already grounded
- not written: Iblis's pride in being made of fire (7:12) - would pull the prayer theme away from the ayah
- not written: fire from the green tree (36:80) - overlaps 56:71-73

===== passages not cited (272) =====
## strong (this ayah's own list) (37)

- (9:81) [listed for 88:4] فَرِحَ ٱلْمُخَلَّفُونَ بِمَقْعَدِهِمْ خِلَٰفَ رَسُولِ ٱللَّهِ وَكَرِهُوٓا۟ أَن يُجَٰهِدُوا۟ بِأَمْوَٰلِهِمْ وَأَنفُسِهِمْ فِى سَبِيلِ ٱللَّهِ وَقَالُوا۟ لَا تَنفِرُوا۟ فِى ٱلْحَرِّ ۗ قُلْ نَارُ جَهَنَّمَ أَشَدُّ حَرًّۭا ۚ لَّوْ كَانُوا۟ يَفْقَهُونَ
- (14:17) [listed for 88:4] يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ وَيَأْتِيهِ ٱلْمَوْتُ مِن كُلِّ مَكَانٍۢ وَمَا هُوَ بِمَيِّتٍۢ ۖ وَمِن وَرَآئِهِۦ عَذَابٌ غَلِيظٌۭ
- (20:74) [listed for 88:4] إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- (22:20) [listed for 88:4] يُصْهَرُ بِهِۦ مَا فِى بُطُونِهِمْ وَٱلْجُلُودُ
- (22:22) [listed for 88:4] كُلَّمَآ أَرَادُوٓا۟ أَن يَخْرُجُوا۟ مِنْهَا مِنْ غَمٍّ أُعِيدُوا۟ فِيهَا وَذُوقُوا۟ عَذَابَ ٱلْحَرِيقِ
- (32:20) [listed for 88:4] وَأَمَّا ٱلَّذِينَ فَسَقُوا۟ فَمَأْوَىٰهُمُ ٱلنَّارُ ۖ كُلَّمَآ أَرَادُوٓا۟ أَن يَخْرُجُوا۟ مِنْهَآ أُعِيدُوا۟ فِيهَا وَقِيلَ لَهُمْ ذُوقُوا۟ عَذَابَ ٱلنَّارِ ٱلَّذِى كُنتُم بِهِۦ تُكَذِّبُونَ
- (37:64) [listed for 88:4] إِنَّهَا شَجَرَةٌۭ تَخْرُجُ فِىٓ أَصْلِ ٱلْجَحِيمِ
- (37:67) [listed for 88:4] ثُمَّ إِنَّ لَهُمْ عَلَيْهَا لَشَوْبًۭا مِّنْ حَمِيمٍۢ
- (38:57) [listed for 88:4] هَٰذَا فَلْيَذُوقُوهُ حَمِيمٌۭ وَغَسَّاقٌۭ
- (39:16) [listed for 88:4] لَهُم مِّن فَوْقِهِمْ ظُلَلٌۭ مِّنَ ٱلنَّارِ وَمِن تَحْتِهِمْ ظُلَلٌۭ ۚ ذَٰلِكَ يُخَوِّفُ ٱللَّهُ بِهِۦ عِبَادَهُۥ ۚ يَٰعِبَادِ فَٱتَّقُونِ
- (40:46) [listed for 88:4] ٱلنَّارُ يُعْرَضُونَ عَلَيْهَا غُدُوًّۭا وَعَشِيًّۭا ۖ وَيَوْمَ تَقُومُ ٱلسَّاعَةُ أَدْخِلُوٓا۟ ءَالَ فِرْعَوْنَ أَشَدَّ ٱلْعَذَابِ
- (40:71) [listed for 88:4] إِذِ ٱلْأَغْلَٰلُ فِىٓ أَعْنَٰقِهِمْ وَٱلسَّلَٰسِلُ يُسْحَبُونَ
- (40:72) [listed for 88:4] فِى ٱلْحَمِيمِ ثُمَّ فِى ٱلنَّارِ يُسْجَرُونَ
- (43:48) [listed for 88:4] وَمَا نُرِيهِم مِّنْ ءَايَةٍ إِلَّا هِىَ أَكْبَرُ مِنْ أُخْتِهَا ۖ وَأَخَذْنَٰهُم بِٱلْعَذَابِ لَعَلَّهُمْ يَرْجِعُونَ
- (44:43) [listed for 88:4] إِنَّ شَجَرَتَ ٱلزَّقُّومِ
- (44:44) [listed for 88:4] طَعَامُ ٱلْأَثِيمِ
- (44:45) [listed for 88:4] كَٱلْمُهْلِ يَغْلِى فِى ٱلْبُطُونِ
- (44:46) [listed for 88:4] كَغَلْىِ ٱلْحَمِيمِ
- (44:48) [listed for 88:4] ثُمَّ صُبُّوا۟ فَوْقَ رَأْسِهِۦ مِنْ عَذَابِ ٱلْحَمِيمِ
- (47:15) [listed for 88:4] مَّثَلُ ٱلْجَنَّةِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۖ فِيهَآ أَنْهَٰرٌۭ مِّن مَّآءٍ غَيْرِ ءَاسِنٍۢ وَأَنْهَٰرٌۭ مِّن لَّبَنٍۢ لَّمْ يَتَغَيَّرْ طَعْمُهُۥ وَأَنْهَٰرٌۭ مِّنْ خَمْرٍۢ لَّذَّةٍۢ لِّلشَّٰرِبِينَ وَأَنْهَٰرٌۭ مِّنْ عَسَلٍۢ مُّصَفًّۭى ۖ وَلَهُمْ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَمَغْفِرَةٌۭ مِّن رَّبِّهِمْ ۖ كَمَنْ هُوَ خَٰلِدٌۭ فِى ٱلنَّارِ وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ
- (55:44) [listed for 88:4] يَطُوفُونَ بَيْنَهَا وَبَيْنَ حَمِيمٍ ءَانٍۢ
- (56:93) [listed for 88:4] فَنُزُلٌۭ مِّنْ حَمِيمٍۢ
- (69:32) [listed for 88:4] ثُمَّ فِى سِلْسِلَةٍۢ ذَرْعُهَا سَبْعُونَ ذِرَاعًۭا فَٱسْلُكُوهُ
- (70:15) [listed for 88:4] كَلَّآ ۖ إِنَّهَا لَظَىٰ
- (70:16) [listed for 88:4] نَزَّاعَةًۭ لِّلشَّوَىٰ
- (74:28) [listed for 88:4] لَا تُبْقِى وَلَا تَذَرُ
- (74:29) [listed for 88:4] لَوَّاحَةٌۭ لِّلْبَشَرِ
- (77:31) [listed for 88:4] لَّا ظَلِيلٍۢ وَلَا يُغْنِى مِنَ ٱللَّهَبِ
- (77:32) [listed for 88:4] إِنَّهَا تَرْمِى بِشَرَرٍۢ كَٱلْقَصْرِ
- (78:24) [listed for 88:4] لَّا يَذُوقُونَ فِيهَا بَرْدًۭا وَلَا شَرَابًا
- (78:25) [listed for 88:4] إِلَّا حَمِيمًۭا وَغَسَّاقًۭا
- (87:12) [listed for 88:4] [cited in ¶3, ¶21] ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ
- (101:11) [listed for 88:4] [cited in ¶12] نَارٌ حَامِيَةٌۢ
- (102:6) [listed for 88:4] لَتَرَوُنَّ ٱلْجَحِيمَ
- (102:7) [listed for 88:4] ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ
- (104:7) [listed for 88:4] ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ
- (111:3) [listed for 88:4] [cited in ¶3] سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ

## medium (this ayah's own list) (88)

- (3:185) [listed for 88:4] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۗ وَإِنَّمَا تُوَفَّوْنَ أُجُورَكُمْ يَوْمَ ٱلْقِيَٰمَةِ ۖ فَمَن زُحْزِحَ عَنِ ٱلنَّارِ وَأُدْخِلَ ٱلْجَنَّةَ فَقَدْ فَازَ ۗ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
- (4:10) [listed for 88:4] إِنَّ ٱلَّذِينَ يَأْكُلُونَ أَمْوَٰلَ ٱلْيَتَٰمَىٰ ظُلْمًا إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا ۖ وَسَيَصْلَوْنَ سَعِيرًۭا
- (4:56) [listed for 88:4] [cited in ¶3] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا سَوْفَ نُصْلِيهِمْ نَارًۭا كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا لِيَذُوقُوا۟ ٱلْعَذَابَ ۗ إِنَّ ٱللَّهَ كَانَ عَزِيزًا حَكِيمًۭا
- (7:41) [listed for 88:4] لَهُم مِّن جَهَنَّمَ مِهَادٌۭ وَمِن فَوْقِهِمْ غَوَاشٍۢ ۚ وَكَذَٰلِكَ نَجْزِى ٱلظَّٰلِمِينَ
- (7:50) [listed for 88:4] وَنَادَىٰٓ أَصْحَٰبُ ٱلنَّارِ أَصْحَٰبَ ٱلْجَنَّةِ أَنْ أَفِيضُوا۟ عَلَيْنَا مِنَ ٱلْمَآءِ أَوْ مِمَّا رَزَقَكُمُ ٱللَّهُ ۚ قَالُوٓا۟ إِنَّ ٱللَّهَ حَرَّمَهُمَا عَلَى ٱلْكَٰفِرِينَ
- (9:35) [listed for 88:4] [cited in ¶13, ¶14] يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ ۖ هَٰذَا مَا كَنَزْتُمْ لِأَنفُسِكُمْ فَذُوقُوا۟ مَا كُنتُمْ تَكْنِزُونَ
- (14:16) [listed for 88:4] مِّن وَرَآئِهِۦ جَهَنَّمُ وَيُسْقَىٰ مِن مَّآءٍۢ صَدِيدٍۢ
- (14:29) [listed for 88:4] جَهَنَّمَ يَصْلَوْنَهَا ۖ وَبِئْسَ ٱلْقَرَارُ
- (18:29) [listed for 88:4] وَقُلِ ٱلْحَقُّ مِن رَّبِّكُمْ ۖ فَمَن شَآءَ فَلْيُؤْمِن وَمَن شَآءَ فَلْيَكْفُرْ ۚ إِنَّآ أَعْتَدْنَا لِلظَّٰلِمِينَ نَارًا أَحَاطَ بِهِمْ سُرَادِقُهَا ۚ وَإِن يَسْتَغِيثُوا۟ يُغَاثُوا۟ بِمَآءٍۢ كَٱلْمُهْلِ يَشْوِى ٱلْوُجُوهَ ۚ بِئْسَ ٱلشَّرَابُ وَسَآءَتْ مُرْتَفَقًا
- (19:70) [listed for 88:4] ثُمَّ لَنَحْنُ أَعْلَمُ بِٱلَّذِينَ هُمْ أَوْلَىٰ بِهَا صِلِيًّۭا
- (19:71) [listed for 88:4] وَإِن مِّنكُمْ إِلَّا وَارِدُهَا ۚ كَانَ عَلَىٰ رَبِّكَ حَتْمًۭا مَّقْضِيًّۭا
- (21:39) [listed for 88:4] لَوْ يَعْلَمُ ٱلَّذِينَ كَفَرُوا۟ حِينَ لَا يَكُفُّونَ عَن وُجُوهِهِمُ ٱلنَّارَ وَلَا عَن ظُهُورِهِمْ وَلَا هُمْ يُنصَرُونَ
- (22:19) [listed for 88:4] ۞ هَٰذَانِ خَصْمَانِ ٱخْتَصَمُوا۟ فِى رَبِّهِمْ ۖ فَٱلَّذِينَ كَفَرُوا۟ قُطِّعَتْ لَهُمْ ثِيَابٌۭ مِّن نَّارٍۢ يُصَبُّ مِن فَوْقِ رُءُوسِهِمُ ٱلْحَمِيمُ
- (22:21) [listed for 88:4] وَلَهُم مَّقَٰمِعُ مِنْ حَدِيدٍۢ
- (25:13) [listed for 88:4] وَإِذَآ أُلْقُوا۟ مِنْهَا مَكَانًۭا ضَيِّقًۭا مُّقَرَّنِينَ دَعَوْا۟ هُنَالِكَ ثُبُورًۭا
- (25:14) [listed for 88:4] لَّا تَدْعُوا۟ ٱلْيَوْمَ ثُبُورًۭا وَٰحِدًۭا وَٱدْعُوا۟ ثُبُورًۭا كَثِيرًۭا
- (25:65) [listed for 88:4] وَٱلَّذِينَ يَقُولُونَ رَبَّنَا ٱصْرِفْ عَنَّا عَذَابَ جَهَنَّمَ ۖ إِنَّ عَذَابَهَا كَانَ غَرَامًا
- (25:66) [listed for 88:4] إِنَّهَا سَآءَتْ مُسْتَقَرًّۭا وَمُقَامًۭا
- (33:64) [listed for 88:4] إِنَّ ٱللَّهَ لَعَنَ ٱلْكَٰفِرِينَ وَأَعَدَّ لَهُمْ سَعِيرًا
- (33:65) [listed for 88:4] خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ لَّا يَجِدُونَ وَلِيًّۭا وَلَا نَصِيرًۭا
- (33:66) [listed for 88:4] يَوْمَ تُقَلَّبُ وُجُوهُهُمْ فِى ٱلنَّارِ يَقُولُونَ يَٰلَيْتَنَآ أَطَعْنَا ٱللَّهَ وَأَطَعْنَا ٱلرَّسُولَا۠
- (33:67) [listed for 88:4] وَقَالُوا۟ رَبَّنَآ إِنَّآ أَطَعْنَا سَادَتَنَا وَكُبَرَآءَنَا فَأَضَلُّونَا ٱلسَّبِيلَا۠
- (33:68) [listed for 88:4] رَبَّنَآ ءَاتِهِمْ ضِعْفَيْنِ مِنَ ٱلْعَذَابِ وَٱلْعَنْهُمْ لَعْنًۭا كَبِيرًۭا
- (35:36) [listed for 88:4] وَٱلَّذِينَ كَفَرُوا۟ لَهُمْ نَارُ جَهَنَّمَ لَا يُقْضَىٰ عَلَيْهِمْ فَيَمُوتُوا۟ وَلَا يُخَفَّفُ عَنْهُم مِّنْ عَذَابِهَا ۚ كَذَٰلِكَ نَجْزِى كُلَّ كَفُورٍۢ
- (36:63) [listed for 88:4] هَٰذِهِۦ جَهَنَّمُ ٱلَّتِى كُنتُمْ تُوعَدُونَ
- (36:64) [listed for 88:4] ٱصْلَوْهَا ٱلْيَوْمَ بِمَا كُنتُمْ تَكْفُرُونَ
- (36:80) [listed for 88:4] ٱلَّذِى جَعَلَ لَكُم مِّنَ ٱلشَّجَرِ ٱلْأَخْضَرِ نَارًۭا فَإِذَآ أَنتُم مِّنْهُ تُوقِدُونَ
- (37:62) [listed for 88:4] أَذَٰلِكَ خَيْرٌۭ نُّزُلًا أَمْ شَجَرَةُ ٱلزَّقُّومِ
- (37:163) [listed for 88:4] إِلَّا مَنْ هُوَ صَالِ ٱلْجَحِيمِ
- (38:56) [listed for 88:4] جَهَنَّمَ يَصْلَوْنَهَا فَبِئْسَ ٱلْمِهَادُ
- (38:58) [listed for 88:4] وَءَاخَرُ مِن شَكْلِهِۦٓ أَزْوَٰجٌ
- (39:71) [listed for 88:4] وَسِيقَ ٱلَّذِينَ كَفَرُوٓا۟ إِلَىٰ جَهَنَّمَ زُمَرًا ۖ حَتَّىٰٓ إِذَا جَآءُوهَا فُتِحَتْ أَبْوَٰبُهَا وَقَالَ لَهُمْ خَزَنَتُهَآ أَلَمْ يَأْتِكُمْ رُسُلٌۭ مِّنكُمْ يَتْلُونَ عَلَيْكُمْ ءَايَٰتِ رَبِّكُمْ وَيُنذِرُونَكُمْ لِقَآءَ يَوْمِكُمْ هَٰذَا ۚ قَالُوا۟ بَلَىٰ وَلَٰكِنْ حَقَّتْ كَلِمَةُ ٱلْعَذَابِ عَلَى ٱلْكَٰفِرِينَ
- (43:74) [listed for 88:4] إِنَّ ٱلْمُجْرِمِينَ فِى عَذَابِ جَهَنَّمَ خَٰلِدُونَ
- (44:47) [listed for 88:4] خُذُوهُ فَٱعْتِلُوهُ إِلَىٰ سَوَآءِ ٱلْجَحِيمِ
- (44:49) [listed for 88:4] ذُقْ إِنَّكَ أَنتَ ٱلْعَزِيزُ ٱلْكَرِيمُ
- (44:50) [listed for 88:4] إِنَّ هَٰذَا مَا كُنتُم بِهِۦ تَمْتَرُونَ
- (48:26) [listed for 88:4] [cited in ¶18] إِذْ جَعَلَ ٱلَّذِينَ كَفَرُوا۟ فِى قُلُوبِهِمُ ٱلْحَمِيَّةَ حَمِيَّةَ ٱلْجَٰهِلِيَّةِ فَأَنزَلَ ٱللَّهُ سَكِينَتَهُۥ عَلَىٰ رَسُولِهِۦ وَعَلَى ٱلْمُؤْمِنِينَ وَأَلْزَمَهُمْ كَلِمَةَ ٱلتَّقْوَىٰ وَكَانُوٓا۟ أَحَقَّ بِهَا وَأَهْلَهَا ۚ وَكَانَ ٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمًۭا
- (50:24) [listed for 88:4] أَلْقِيَا فِى جَهَنَّمَ كُلَّ كَفَّارٍ عَنِيدٍۢ
- (50:30) [listed for 88:4] يَوْمَ نَقُولُ لِجَهَنَّمَ هَلِ ٱمْتَلَأْتِ وَتَقُولُ هَلْ مِن مَّزِيدٍۢ
- (52:13) [listed for 88:4] يَوْمَ يُدَعُّونَ إِلَىٰ نَارِ جَهَنَّمَ دَعًّا
- (52:14) [listed for 88:4] هَٰذِهِ ٱلنَّارُ ٱلَّتِى كُنتُم بِهَا تُكَذِّبُونَ
- (52:16) [listed for 88:4] ٱصْلَوْهَا فَٱصْبِرُوٓا۟ أَوْ لَا تَصْبِرُوا۟ سَوَآءٌ عَلَيْكُمْ ۖ إِنَّمَا تُجْزَوْنَ مَا كُنتُمْ تَعْمَلُونَ
- (55:35) [listed for 88:4] يُرْسَلُ عَلَيْكُمَا شُوَاظٌۭ مِّن نَّارٍۢ وَنُحَاسٌۭ فَلَا تَنتَصِرَانِ
- (55:43) [listed for 88:4] هَٰذِهِۦ جَهَنَّمُ ٱلَّتِى يُكَذِّبُ بِهَا ٱلْمُجْرِمُونَ
- (56:42) [listed for 88:4] فِى سَمُومٍۢ وَحَمِيمٍۢ
- (56:43) [listed for 88:4] وَظِلٍّۢ مِّن يَحْمُومٍۢ
- (56:44) [listed for 88:4] لَّا بَارِدٍۢ وَلَا كَرِيمٍ
- (56:94) [listed for 88:4] وَتَصْلِيَةُ جَحِيمٍ
- (59:17) [listed for 88:4] فَكَانَ عَٰقِبَتَهُمَآ أَنَّهُمَا فِى ٱلنَّارِ خَٰلِدَيْنِ فِيهَا ۚ وَذَٰلِكَ جَزَٰٓؤُا۟ ٱلظَّٰلِمِينَ
- (59:20) [listed for 88:4] لَا يَسْتَوِىٓ أَصْحَٰبُ ٱلنَّارِ وَأَصْحَٰبُ ٱلْجَنَّةِ ۚ أَصْحَٰبُ ٱلْجَنَّةِ هُمُ ٱلْفَآئِزُونَ
- (66:6) [listed for 88:4] [cited in ¶5, ¶16] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ عَلَيْهَا مَلَٰٓئِكَةٌ غِلَاظٌۭ شِدَادٌۭ لَّا يَعْصُونَ ٱللَّهَ مَآ أَمَرَهُمْ وَيَفْعَلُونَ مَا يُؤْمَرُونَ
- (67:6) [listed for 88:4] وَلِلَّذِينَ كَفَرُوا۟ بِرَبِّهِمْ عَذَابُ جَهَنَّمَ ۖ وَبِئْسَ ٱلْمَصِيرُ
- (67:7) [listed for 88:4] إِذَآ أُلْقُوا۟ فِيهَا سَمِعُوا۟ لَهَا شَهِيقًۭا وَهِىَ تَفُورُ
- (69:30) [listed for 88:4] خُذُوهُ فَغُلُّوهُ
- (69:31) [listed for 88:4] ثُمَّ ٱلْجَحِيمَ صَلُّوهُ
- (70:17) [listed for 88:4] تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ
- (70:18) [listed for 88:4] وَجَمَعَ فَأَوْعَىٰٓ
- (71:25) [listed for 88:4] مِّمَّا خَطِيٓـَٰٔتِهِمْ أُغْرِقُوا۟ فَأُدْخِلُوا۟ نَارًۭا فَلَمْ يَجِدُوا۟ لَهُم مِّن دُونِ ٱللَّهِ أَنصَارًۭا
- (72:23) [listed for 88:4] إِلَّا بَلَٰغًۭا مِّنَ ٱللَّهِ وَرِسَٰلَٰتِهِۦ ۚ وَمَن يَعْصِ ٱللَّهَ وَرَسُولَهُۥ فَإِنَّ لَهُۥ نَارَ جَهَنَّمَ خَٰلِدِينَ فِيهَآ أَبَدًا
- (73:13) [listed for 88:4] وَطَعَامًۭا ذَا غُصَّةٍۢ وَعَذَابًا أَلِيمًۭا
- (74:26) [listed for 88:4] سَأُصْلِيهِ سَقَرَ
- (74:27) [listed for 88:4] وَمَآ أَدْرَىٰكَ مَا سَقَرُ
- (74:30) [listed for 88:4] عَلَيْهَا تِسْعَةَ عَشَرَ
- (76:4) [listed for 88:4] إِنَّآ أَعْتَدْنَا لِلْكَٰفِرِينَ سَلَٰسِلَا۟ وَأَغْلَٰلًۭا وَسَعِيرًا
- (77:30) [listed for 88:4] ٱنطَلِقُوٓا۟ إِلَىٰ ظِلٍّۢ ذِى ثَلَٰثِ شُعَبٍۢ
- (77:33) [listed for 88:4] كَأَنَّهُۥ جِمَٰلَتٌۭ صُفْرٌۭ
- (78:21) [listed for 88:4] إِنَّ جَهَنَّمَ كَانَتْ مِرْصَادًۭا
- (78:30) [listed for 88:4] فَذُوقُوا۟ فَلَن نَّزِيدَكُمْ إِلَّا عَذَابًا
- (79:36) [listed for 88:4] وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ
- (79:39) [listed for 88:4] فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ
- (82:14) [listed for 88:4] وَإِنَّ ٱلْفُجَّارَ لَفِى جَحِيمٍۢ
- (83:15) [listed for 88:4] كَلَّآ إِنَّهُمْ عَن رَّبِّهِمْ يَوْمَئِذٍۢ لَّمَحْجُوبُونَ
- (83:16) [listed for 88:4] ثُمَّ إِنَّهُمْ لَصَالُوا۟ ٱلْجَحِيمِ
- (84:11) [listed for 88:4] فَسَوْفَ يَدْعُوا۟ ثُبُورًۭا
- (85:10) [listed for 88:4] إِنَّ ٱلَّذِينَ فَتَنُوا۟ ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ ثُمَّ لَمْ يَتُوبُوا۟ فَلَهُمْ عَذَابُ جَهَنَّمَ وَلَهُمْ عَذَابُ ٱلْحَرِيقِ
- (89:23) [listed for 88:4] وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- (90:19) [listed for 88:4] وَٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا هُمْ أَصْحَٰبُ ٱلْمَشْـَٔمَةِ
- (90:20) [listed for 88:4] عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ
- (92:15) [listed for 88:4] لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- (98:6) [listed for 88:4] إِنَّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ ۚ أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ
- (101:10) [listed for 88:4] [cited in ¶12] وَمَآ أَدْرَىٰكَ مَا هِيَهْ
- (104:4) [listed for 88:4] كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ
- (104:5) [listed for 88:4] وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ
- (104:6) [listed for 88:4] نَارُ ٱللَّهِ ٱلْمُوقَدَةُ
- (104:8) [listed for 88:4] إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ
- (104:9) [listed for 88:4] فِى عَمَدٍۢ مُّمَدَّدَةٍۭ
- (111:4) [listed for 88:4] [cited in ¶5] وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ
- (111:5) [listed for 88:4] فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ

## named by the passage's own list as strong for this ayah (18)

- (2:24) [listed for 88:4] فَإِن لَّمْ تَفْعَلُوا۟ وَلَن تَفْعَلُوا۟ فَٱتَّقُوا۟ ٱلنَّارَ ٱلَّتِى وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ ۖ أُعِدَّتْ لِلْكَٰفِرِينَ
- (8:14) [listed for 88:4] ذَٰلِكُمْ فَذُوقُوهُ وَأَنَّ لِلْكَٰفِرِينَ عَذَابَ ٱلنَّارِ
- (8:50) [listed for 88:4] وَلَوْ تَرَىٰٓ إِذْ يَتَوَفَّى ٱلَّذِينَ كَفَرُوا۟ ۙ ٱلْمَلَٰٓئِكَةُ يَضْرِبُونَ وُجُوهَهُمْ وَأَدْبَٰرَهُمْ وَذُوقُوا۟ عَذَابَ ٱلْحَرِيقِ
- (10:52) [listed for 88:4] ثُمَّ قِيلَ لِلَّذِينَ ظَلَمُوا۟ ذُوقُوا۟ عَذَابَ ٱلْخُلْدِ هَلْ تُجْزَوْنَ إِلَّا بِمَا كُنتُمْ تَكْسِبُونَ
- (18:53) [listed for 88:4] وَرَءَا ٱلْمُجْرِمُونَ ٱلنَّارَ فَظَنُّوٓا۟ أَنَّهُم مُّوَاقِعُوهَا وَلَمْ يَجِدُوا۟ عَنْهَا مَصْرِفًۭا
- (20:101) [listed for 88:4] خَٰلِدِينَ فِيهِ ۖ وَسَآءَ لَهُمْ يَوْمَ ٱلْقِيَٰمَةِ حِمْلًۭا
- (34:42) [listed for 88:4] فَٱلْيَوْمَ لَا يَمْلِكُ بَعْضُكُمْ لِبَعْضٍۢ نَّفْعًۭا وَلَا ضَرًّۭا وَنَقُولُ لِلَّذِينَ ظَلَمُوا۟ ذُوقُوا۟ عَذَابَ ٱلنَّارِ ٱلَّتِى كُنتُم بِهَا تُكَذِّبُونَ
- (37:68) [listed for 88:4] ثُمَّ إِنَّ مَرْجِعَهُمْ لَإِلَى ٱلْجَحِيمِ
- (39:24) [listed for 88:4] أَفَمَن يَتَّقِى بِوَجْهِهِۦ سُوٓءَ ٱلْعَذَابِ يَوْمَ ٱلْقِيَٰمَةِ ۚ وَقِيلَ لِلظَّٰلِمِينَ ذُوقُوا۟ مَا كُنتُمْ تَكْسِبُونَ
- (42:45) [listed for 88:4] وَتَرَىٰهُمْ يُعْرَضُونَ عَلَيْهَا خَٰشِعِينَ مِنَ ٱلذُّلِّ يَنظُرُونَ مِن طَرْفٍ خَفِىٍّۢ ۗ وَقَالَ ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّ ٱلْخَٰسِرِينَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ وَأَهْلِيهِمْ يَوْمَ ٱلْقِيَٰمَةِ ۗ أَلَآ إِنَّ ٱلظَّٰلِمِينَ فِى عَذَابٍۢ مُّقِيمٍۢ
- (54:48) [listed for 88:4] يَوْمَ يُسْحَبُونَ فِى ٱلنَّارِ عَلَىٰ وُجُوهِهِمْ ذُوقُوا۟ مَسَّ سَقَرَ
- (56:53) [listed for 88:4] فَمَالِـُٔونَ مِنْهَا ٱلْبُطُونَ
- (56:56) [listed for 88:4] هَٰذَا نُزُلُهُمْ يَوْمَ ٱلدِّينِ
- (69:36) [listed for 88:4] وَلَا طَعَامٌ إِلَّا مِنْ غِسْلِينٍۢ
- (74:10) [listed for 88:4] عَلَى ٱلْكَٰفِرِينَ غَيْرُ يَسِيرٍۢ
- (77:29) [listed for 88:4] ٱنطَلِقُوٓا۟ إِلَىٰ مَا كُنتُم بِهِۦ تُكَذِّبُونَ
- (92:14) [listed for 88:4] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- (101:9) [listed for 88:4] فَأُمُّهُۥ هَاوِيَةٌۭ

## named by the passage's own list as medium for this ayah (42)

- (2:39) [listed for 88:4] وَٱلَّذِينَ كَفَرُوا۟ وَكَذَّبُوا۟ بِـَٔايَٰتِنَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (2:175) [listed for 88:4] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلضَّلَٰلَةَ بِٱلْهُدَىٰ وَٱلْعَذَابَ بِٱلْمَغْفِرَةِ ۚ فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ
- (3:12) [listed for 88:4] قُل لِّلَّذِينَ كَفَرُوا۟ سَتُغْلَبُونَ وَتُحْشَرُونَ إِلَىٰ جَهَنَّمَ ۚ وَبِئْسَ ٱلْمِهَادُ
- (3:88) [listed for 88:4] خَٰلِدِينَ فِيهَا لَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنظَرُونَ
- (3:106) [listed for 88:4] يَوْمَ تَبْيَضُّ وُجُوهٌۭ وَتَسْوَدُّ وُجُوهٌۭ ۚ فَأَمَّا ٱلَّذِينَ ٱسْوَدَّتْ وُجُوهُهُمْ أَكَفَرْتُم بَعْدَ إِيمَٰنِكُمْ فَذُوقُوا۟ ٱلْعَذَابَ بِمَا كُنتُمْ تَكْفُرُونَ
- (4:121) [listed for 88:4] أُو۟لَٰٓئِكَ مَأْوَىٰهُمْ جَهَنَّمُ وَلَا يَجِدُونَ عَنْهَا مَحِيصًۭا
- (7:47) [listed for 88:4] ۞ وَإِذَا صُرِفَتْ أَبْصَٰرُهُمْ تِلْقَآءَ أَصْحَٰبِ ٱلنَّارِ قَالُوا۟ رَبَّنَا لَا تَجْعَلْنَا مَعَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
- (11:106) [listed for 88:4] فَأَمَّا ٱلَّذِينَ شَقُوا۟ فَفِى ٱلنَّارِ لَهُمْ فِيهَا زَفِيرٌۭ وَشَهِيقٌ
- (14:50) [listed for 88:4] سَرَابِيلُهُم مِّن قَطِرَانٍۢ وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ
- (15:43) [listed for 88:4] وَإِنَّ جَهَنَّمَ لَمَوْعِدُهُمْ أَجْمَعِينَ
- (16:29) [listed for 88:4] فَٱدْخُلُوٓا۟ أَبْوَٰبَ جَهَنَّمَ خَٰلِدِينَ فِيهَا ۖ فَلَبِئْسَ مَثْوَى ٱلْمُتَكَبِّرِينَ
- (18:100) [listed for 88:4] وَعَرَضْنَا جَهَنَّمَ يَوْمَئِذٍۢ لِّلْكَٰفِرِينَ عَرْضًا
- (19:86) [listed for 88:4] وَنَسُوقُ ٱلْمُجْرِمِينَ إِلَىٰ جَهَنَّمَ وِرْدًۭا
- (23:104) [listed for 88:4] [cited in ¶1] تَلْفَحُ وُجُوهَهُمُ ٱلنَّارُ وَهُمْ فِيهَا كَٰلِحُونَ
- (23:108) [listed for 88:4] قَالَ ٱخْسَـُٔوا۟ فِيهَا وَلَا تُكَلِّمُونِ
- (24:57) [listed for 88:4] لَا تَحْسَبَنَّ ٱلَّذِينَ كَفَرُوا۟ مُعْجِزِينَ فِى ٱلْأَرْضِ ۚ وَمَأْوَىٰهُمُ ٱلنَّارُ ۖ وَلَبِئْسَ ٱلْمَصِيرُ
- (25:11) [listed for 88:4] بَلْ كَذَّبُوا۟ بِٱلسَّاعَةِ ۖ وَأَعْتَدْنَا لِمَن كَذَّبَ بِٱلسَّاعَةِ سَعِيرًا
- (25:12) [listed for 88:4] إِذَا رَأَتْهُم مِّن مَّكَانٍۭ بَعِيدٍۢ سَمِعُوا۟ لَهَا تَغَيُّظًۭا وَزَفِيرًۭا
- (25:15) [listed for 88:4] قُلْ أَذَٰلِكَ خَيْرٌ أَمْ جَنَّةُ ٱلْخُلْدِ ٱلَّتِى وُعِدَ ٱلْمُتَّقُونَ ۚ كَانَتْ لَهُمْ جَزَآءًۭ وَمَصِيرًۭا
- (25:69) [listed for 88:4] يُضَٰعَفْ لَهُ ٱلْعَذَابُ يَوْمَ ٱلْقِيَٰمَةِ وَيَخْلُدْ فِيهِۦ مُهَانًا
- (37:31) [listed for 88:4] فَحَقَّ عَلَيْنَا قَوْلُ رَبِّنَآ ۖ إِنَّا لَذَآئِقُونَ
- (40:52) [listed for 88:4] يَوْمَ لَا يَنفَعُ ٱلظَّٰلِمِينَ مَعْذِرَتُهُمْ ۖ وَلَهُمُ ٱللَّعْنَةُ وَلَهُمْ سُوٓءُ ٱلدَّارِ
- (40:76) [listed for 88:4] ٱدْخُلُوٓا۟ أَبْوَٰبَ جَهَنَّمَ خَٰلِدِينَ فِيهَا ۖ فَبِئْسَ مَثْوَى ٱلْمُتَكَبِّرِينَ
- (41:28) [listed for 88:4] ذَٰلِكَ جَزَآءُ أَعْدَآءِ ٱللَّهِ ٱلنَّارُ ۖ لَهُمْ فِيهَا دَارُ ٱلْخُلْدِ ۖ جَزَآءًۢ بِمَا كَانُوا۟ بِـَٔايَٰتِنَا يَجْحَدُونَ
- (43:77) [listed for 88:4] وَنَادَوْا۟ يَٰمَٰلِكُ لِيَقْضِ عَلَيْنَا رَبُّكَ ۖ قَالَ إِنَّكُم مَّٰكِثُونَ
- (45:34) [listed for 88:4] وَقِيلَ ٱلْيَوْمَ نَنسَىٰكُمْ كَمَا نَسِيتُمْ لِقَآءَ يَوْمِكُمْ هَٰذَا وَمَأْوَىٰكُمُ ٱلنَّارُ وَمَا لَكُم مِّن نَّٰصِرِينَ
- (45:35) [listed for 88:4] ذَٰلِكُم بِأَنَّكُمُ ٱتَّخَذْتُمْ ءَايَٰتِ ٱللَّهِ هُزُوًۭا وَغَرَّتْكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ فَٱلْيَوْمَ لَا يُخْرَجُونَ مِنْهَا وَلَا هُمْ يُسْتَعْتَبُونَ
- (46:34) [listed for 88:4] وَيَوْمَ يُعْرَضُ ٱلَّذِينَ كَفَرُوا۟ عَلَى ٱلنَّارِ أَلَيْسَ هَٰذَا بِٱلْحَقِّ ۖ قَالُوا۟ بَلَىٰ وَرَبِّنَا ۚ قَالَ فَذُوقُوا۟ ٱلْعَذَابَ بِمَا كُنتُمْ تَكْفُرُونَ
- (51:13) [listed for 88:4] يَوْمَ هُمْ عَلَى ٱلنَّارِ يُفْتَنُونَ
- (55:15) [listed for 88:4] وَخَلَقَ ٱلْجَآنَّ مِن مَّارِجٍۢ مِّن نَّارٍۢ
- (56:71) [listed for 88:4] [cited in ¶10] أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ
- (64:10) [listed for 88:4] وَٱلَّذِينَ كَفَرُوا۟ وَكَذَّبُوا۟ بِـَٔايَٰتِنَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ خَٰلِدِينَ فِيهَا ۖ وَبِئْسَ ٱلْمَصِيرُ
- (73:12) [listed for 88:4] إِنَّ لَدَيْنَآ أَنكَالًۭا وَجَحِيمًۭا
- (78:23) [listed for 88:4] لَّٰبِثِينَ فِيهَآ أَحْقَابًۭا
- (79:34) [listed for 88:4] فَإِذَا جَآءَتِ ٱلطَّآمَّةُ ٱلْكُبْرَىٰ
- (80:41) [listed for 88:4] تَرْهَقُهَا قَتَرَةٌ
- (81:12) [listed for 88:4] وَإِذَا ٱلْجَحِيمُ سُعِّرَتْ
- (84:12) [listed for 88:4] [cited in ¶3] وَيَصْلَىٰ سَعِيرًا
- (85:5) [listed for 88:4] ٱلنَّارِ ذَاتِ ٱلْوَقُودِ
- (87:13) [listed for 88:4] ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- (92:4) [listed for 88:4] إِنَّ سَعْيَكُمْ لَشَتَّىٰ
- (101:1) [listed for 88:4] ٱلْقَارِعَةُ

## weak (this ayah's own list) (23)

- (2:17) [listed for 88:4] مَثَلُهُمْ كَمَثَلِ ٱلَّذِى ٱسْتَوْقَدَ نَارًۭا فَلَمَّآ أَضَآءَتْ مَا حَوْلَهُۥ ذَهَبَ ٱللَّهُ بِنُورِهِمْ وَتَرَكَهُمْ فِى ظُلُمَٰتٍۢ لَّا يُبْصِرُونَ
- (2:174) [listed for 88:4] إِنَّ ٱلَّذِينَ يَكْتُمُونَ مَآ أَنزَلَ ٱللَّهُ مِنَ ٱلْكِتَٰبِ وَيَشْتَرُونَ بِهِۦ ثَمَنًۭا قَلِيلًا ۙ أُو۟لَٰٓئِكَ مَا يَأْكُلُونَ فِى بُطُونِهِمْ إِلَّا ٱلنَّارَ وَلَا يُكَلِّمُهُمُ ٱللَّهُ يَوْمَ ٱلْقِيَٰمَةِ وَلَا يُزَكِّيهِمْ وَلَهُمْ عَذَابٌ أَلِيمٌ
- (2:257) [listed for 88:4] ٱللَّهُ وَلِىُّ ٱلَّذِينَ ءَامَنُوا۟ يُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۖ وَٱلَّذِينَ كَفَرُوٓا۟ أَوْلِيَآؤُهُمُ ٱلطَّٰغُوتُ يُخْرِجُونَهُم مِّنَ ٱلنُّورِ إِلَى ٱلظُّلُمَٰتِ ۗ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (2:266) [listed for 88:4] أَيَوَدُّ أَحَدُكُمْ أَن تَكُونَ لَهُۥ جَنَّةٌۭ مِّن نَّخِيلٍۢ وَأَعْنَابٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ لَهُۥ فِيهَا مِن كُلِّ ٱلثَّمَرَٰتِ وَأَصَابَهُ ٱلْكِبَرُ وَلَهُۥ ذُرِّيَّةٌۭ ضُعَفَآءُ فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمُ ٱلْءَايَٰتِ لَعَلَّكُمْ تَتَفَكَّرُونَ
- (4:14) [listed for 88:4] وَمَن يَعْصِ ٱللَّهَ وَرَسُولَهُۥ وَيَتَعَدَّ حُدُودَهُۥ يُدْخِلْهُ نَارًا خَٰلِدًۭا فِيهَا وَلَهُۥ عَذَابٌۭ مُّهِينٌۭ
- (4:30) [listed for 88:4] وَمَن يَفْعَلْ ذَٰلِكَ عُدْوَٰنًۭا وَظُلْمًۭا فَسَوْفَ نُصْلِيهِ نَارًۭا ۚ وَكَانَ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرًا
- (4:115) [listed for 88:4] وَمَن يُشَاقِقِ ٱلرَّسُولَ مِنۢ بَعْدِ مَا تَبَيَّنَ لَهُ ٱلْهُدَىٰ وَيَتَّبِعْ غَيْرَ سَبِيلِ ٱلْمُؤْمِنِينَ نُوَلِّهِۦ مَا تَوَلَّىٰ وَنُصْلِهِۦ جَهَنَّمَ ۖ وَسَآءَتْ مَصِيرًا
- (5:29) [listed for 88:4] إِنِّىٓ أُرِيدُ أَن تَبُوٓأَ بِإِثْمِى وَإِثْمِكَ فَتَكُونَ مِنْ أَصْحَٰبِ ٱلنَّارِ ۚ وَذَٰلِكَ جَزَٰٓؤُا۟ ٱلظَّٰلِمِينَ
- (5:64) [listed for 88:4] وَقَالَتِ ٱلْيَهُودُ يَدُ ٱللَّهِ مَغْلُولَةٌ ۚ غُلَّتْ أَيْدِيهِمْ وَلُعِنُوا۟ بِمَا قَالُوا۟ ۘ بَلْ يَدَاهُ مَبْسُوطَتَانِ يُنفِقُ كَيْفَ يَشَآءُ ۚ وَلَيَزِيدَنَّ كَثِيرًۭا مِّنْهُم مَّآ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ طُغْيَٰنًۭا وَكُفْرًۭا ۚ وَأَلْقَيْنَا بَيْنَهُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ ۚ كُلَّمَآ أَوْقَدُوا۟ نَارًۭا لِّلْحَرْبِ أَطْفَأَهَا ٱللَّهُ ۚ وَيَسْعَوْنَ فِى ٱلْأَرْضِ فَسَادًۭا ۚ وَٱللَّهُ لَا يُحِبُّ ٱلْمُفْسِدِينَ
- (7:12) [listed for 88:4] قَالَ مَا مَنَعَكَ أَلَّا تَسْجُدَ إِذْ أَمَرْتُكَ ۖ قَالَ أَنَا۠ خَيْرٌۭ مِّنْهُ خَلَقْتَنِى مِن نَّارٍۢ وَخَلَقْتَهُۥ مِن طِينٍۢ
- (9:63) [listed for 88:4] أَلَمْ يَعْلَمُوٓا۟ أَنَّهُۥ مَن يُحَادِدِ ٱللَّهَ وَرَسُولَهُۥ فَأَنَّ لَهُۥ نَارَ جَهَنَّمَ خَٰلِدًۭا فِيهَا ۚ ذَٰلِكَ ٱلْخِزْىُ ٱلْعَظِيمُ
- (17:18) [listed for 88:4] مَّن كَانَ يُرِيدُ ٱلْعَاجِلَةَ عَجَّلْنَا لَهُۥ فِيهَا مَا نَشَآءُ لِمَن نُّرِيدُ ثُمَّ جَعَلْنَا لَهُۥ جَهَنَّمَ يَصْلَىٰهَا مَذْمُومًۭا مَّدْحُورًۭا
- (38:27) [listed for 88:4] وَمَا خَلَقْنَا ٱلسَّمَآءَ وَٱلْأَرْضَ وَمَا بَيْنَهُمَا بَٰطِلًۭا ۚ ذَٰلِكَ ظَنُّ ٱلَّذِينَ كَفَرُوا۟ ۚ فَوَيْلٌۭ لِّلَّذِينَ كَفَرُوا۟ مِنَ ٱلنَّارِ
- (38:59) [listed for 88:4] هَٰذَا فَوْجٌۭ مُّقْتَحِمٌۭ مَّعَكُمْ ۖ لَا مَرْحَبًۢا بِهِمْ ۚ إِنَّهُمْ صَالُوا۟ ٱلنَّارِ
- (39:8) [listed for 88:4] ۞ وَإِذَا مَسَّ ٱلْإِنسَٰنَ ضُرٌّۭ دَعَا رَبَّهُۥ مُنِيبًا إِلَيْهِ ثُمَّ إِذَا خَوَّلَهُۥ نِعْمَةًۭ مِّنْهُ نَسِىَ مَا كَانَ يَدْعُوٓا۟ إِلَيْهِ مِن قَبْلُ وَجَعَلَ لِلَّهِ أَندَادًۭا لِّيُضِلَّ عَن سَبِيلِهِۦ ۚ قُلْ تَمَتَّعْ بِكُفْرِكَ قَلِيلًا ۖ إِنَّكَ مِنْ أَصْحَٰبِ ٱلنَّارِ
- (40:6) [listed for 88:4] وَكَذَٰلِكَ حَقَّتْ كَلِمَتُ رَبِّكَ عَلَى ٱلَّذِينَ كَفَرُوٓا۟ أَنَّهُمْ أَصْحَٰبُ ٱلنَّارِ
- (52:8) [listed for 88:4] مَّا لَهُۥ مِن دَافِعٍۢ
- (58:8) [listed for 88:4] أَلَمْ تَرَ إِلَى ٱلَّذِينَ نُهُوا۟ عَنِ ٱلنَّجْوَىٰ ثُمَّ يَعُودُونَ لِمَا نُهُوا۟ عَنْهُ وَيَتَنَٰجَوْنَ بِٱلْإِثْمِ وَٱلْعُدْوَٰنِ وَمَعْصِيَتِ ٱلرَّسُولِ وَإِذَا جَآءُوكَ حَيَّوْكَ بِمَا لَمْ يُحَيِّكَ بِهِ ٱللَّهُ وَيَقُولُونَ فِىٓ أَنفُسِهِمْ لَوْلَا يُعَذِّبُنَا ٱللَّهُ بِمَا نَقُولُ ۚ حَسْبُهُمْ جَهَنَّمُ يَصْلَوْنَهَا ۖ فَبِئْسَ ٱلْمَصِيرُ
- (92:12) [listed for 88:4] إِنَّ عَلَيْنَا لَلْهُدَىٰ
- (92:18) [listed for 88:4] ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
- (92:20) [listed for 88:4] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- (101:2) [listed for 88:4] مَا ٱلْقَارِعَةُ
- (101:5) [listed for 88:4] وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ ٱلْمَنفُوشِ

## named by the passage's own list as weak for this ayah (12)

- (5:37) [listed for 88:4] يُرِيدُونَ أَن يَخْرُجُوا۟ مِنَ ٱلنَّارِ وَمَا هُم بِخَٰرِجِينَ مِنْهَا ۖ وَلَهُمْ عَذَابٌۭ مُّقِيمٌۭ
- (9:68) [listed for 88:4] وَعَدَ ٱللَّهُ ٱلْمُنَٰفِقِينَ وَٱلْمُنَٰفِقَٰتِ وَٱلْكُفَّارَ نَارَ جَهَنَّمَ خَٰلِدِينَ فِيهَا ۚ هِىَ حَسْبُهُمْ ۚ وَلَعَنَهُمُ ٱللَّهُ ۖ وَلَهُمْ عَذَابٌۭ مُّقِيمٌۭ
- (18:96) [listed for 88:4] ءَاتُونِى زُبَرَ ٱلْحَدِيدِ ۖ حَتَّىٰٓ إِذَا سَاوَىٰ بَيْنَ ٱلصَّدَفَيْنِ قَالَ ٱنفُخُوا۟ ۖ حَتَّىٰٓ إِذَا جَعَلَهُۥ نَارًۭا قَالَ ءَاتُونِىٓ أُفْرِغْ عَلَيْهِ قِطْرًۭا
- (27:7) [listed for 88:4] إِذْ قَالَ مُوسَىٰ لِأَهْلِهِۦٓ إِنِّىٓ ءَانَسْتُ نَارًۭا سَـَٔاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ ءَاتِيكُم بِشِهَابٍۢ قَبَسٍۢ لَّعَلَّكُمْ تَصْطَلُونَ
- (29:55) [listed for 88:4] يَوْمَ يَغْشَىٰهُمُ ٱلْعَذَابُ مِن فَوْقِهِمْ وَمِن تَحْتِ أَرْجُلِهِمْ وَيَقُولُ ذُوقُوا۟ مَا كُنتُمْ تَعْمَلُونَ
- (38:64) [listed for 88:4] إِنَّ ذَٰلِكَ لَحَقٌّۭ تَخَاصُمُ أَهْلِ ٱلنَّارِ
- (39:19) [listed for 88:4] أَفَمَنْ حَقَّ عَلَيْهِ كَلِمَةُ ٱلْعَذَابِ أَفَأَنتَ تُنقِذُ مَن فِى ٱلنَّارِ
- (40:41) [listed for 88:4] ۞ وَيَٰقَوْمِ مَا لِىٓ أَدْعُوكُمْ إِلَى ٱلنَّجَوٰةِ وَتَدْعُونَنِىٓ إِلَى ٱلنَّارِ
- (70:5) [listed for 88:4] فَٱصْبِرْ صَبْرًۭا جَمِيلًا
- (82:15) [listed for 88:4] يَصْلَوْنَهَا يَوْمَ ٱلدِّينِ
- (82:16) [listed for 88:4] وَمَا هُمْ عَنْهَا بِغَآئِبِينَ
- (85:4) [listed for 88:4] قُتِلَ أَصْحَٰبُ ٱلْأُخْدُودِ

## neighbours: within two ayat of a passage the commentary cites (52)

- (4:54) [next to 4:56] أَمْ يَحْسُدُونَ ٱلنَّاسَ عَلَىٰ مَآ ءَاتَىٰهُمُ ٱللَّهُ مِن فَضْلِهِۦ ۖ فَقَدْ ءَاتَيْنَآ ءَالَ إِبْرَٰهِيمَ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَءَاتَيْنَٰهُم مُّلْكًا عَظِيمًۭا
- (4:55) [next to 4:56] فَمِنْهُم مَّنْ ءَامَنَ بِهِۦ وَمِنْهُم مَّن صَدَّ عَنْهُ ۚ وَكَفَىٰ بِجَهَنَّمَ سَعِيرًا
- (4:57) [next to 4:56] وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ سَنُدْخِلُهُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ لَّهُمْ فِيهَآ أَزْوَٰجٌۭ مُّطَهَّرَةٌۭ ۖ وَنُدْخِلُهُمْ ظِلًّۭا ظَلِيلًا
- (4:58) [next to 4:56] ۞ إِنَّ ٱللَّهَ يَأْمُرُكُمْ أَن تُؤَدُّوا۟ ٱلْأَمَٰنَٰتِ إِلَىٰٓ أَهْلِهَا وَإِذَا حَكَمْتُم بَيْنَ ٱلنَّاسِ أَن تَحْكُمُوا۟ بِٱلْعَدْلِ ۚ إِنَّ ٱللَّهَ نِعِمَّا يَعِظُكُم بِهِۦٓ ۗ إِنَّ ٱللَّهَ كَانَ سَمِيعًۢا بَصِيرًۭا
- (9:32) [next to 9:34] يُرِيدُونَ أَن يُطْفِـُٔوا۟ نُورَ ٱللَّهِ بِأَفْوَٰهِهِمْ وَيَأْبَى ٱللَّهُ إِلَّآ أَن يُتِمَّ نُورَهُۥ وَلَوْ كَرِهَ ٱلْكَٰفِرُونَ
- (9:33) [next to 9:34] هُوَ ٱلَّذِىٓ أَرْسَلَ رَسُولَهُۥ بِٱلْهُدَىٰ وَدِينِ ٱلْحَقِّ لِيُظْهِرَهُۥ عَلَى ٱلدِّينِ كُلِّهِۦ وَلَوْ كَرِهَ ٱلْمُشْرِكُونَ
- (9:36) [next to 9:34] إِنَّ عِدَّةَ ٱلشُّهُورِ عِندَ ٱللَّهِ ٱثْنَا عَشَرَ شَهْرًۭا فِى كِتَٰبِ ٱللَّهِ يَوْمَ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ مِنْهَآ أَرْبَعَةٌ حُرُمٌۭ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ ۚ فَلَا تَظْلِمُوا۟ فِيهِنَّ أَنفُسَكُمْ ۚ وَقَٰتِلُوا۟ ٱلْمُشْرِكِينَ كَآفَّةًۭ كَمَا يُقَٰتِلُونَكُمْ كَآفَّةًۭ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ مَعَ ٱلْمُتَّقِينَ
- (9:37) [next to 9:35] إِنَّمَا ٱلنَّسِىٓءُ زِيَادَةٌۭ فِى ٱلْكُفْرِ ۖ يُضَلُّ بِهِ ٱلَّذِينَ كَفَرُوا۟ يُحِلُّونَهُۥ عَامًۭا وَيُحَرِّمُونَهُۥ عَامًۭا لِّيُوَاطِـُٔوا۟ عِدَّةَ مَا حَرَّمَ ٱللَّهُ فَيُحِلُّوا۟ مَا حَرَّمَ ٱللَّهُ ۚ زُيِّنَ لَهُمْ سُوٓءُ أَعْمَٰلِهِمْ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
- (20:8) [next to 20:10] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ
- (20:9) [next to 20:10] وَهَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ
- (20:11) [next to 20:10] فَلَمَّآ أَتَىٰهَا نُودِىَ يَٰمُوسَىٰٓ
- (20:12) [next to 20:10] إِنِّىٓ أَنَا۠ رَبُّكَ فَٱخْلَعْ نَعْلَيْكَ ۖ إِنَّكَ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًۭى
- (23:102) [next to 23:104] فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
- (23:103) [next to 23:104] وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُمْ فِى جَهَنَّمَ خَٰلِدُونَ
- (23:105) [next to 23:104] أَلَمْ تَكُنْ ءَايَٰتِى تُتْلَىٰ عَلَيْكُمْ فَكُنتُم بِهَا تُكَذِّبُونَ
- (23:106) [next to 23:104] قَالُوا۟ رَبَّنَا غَلَبَتْ عَلَيْنَا شِقْوَتُنَا وَكُنَّا قَوْمًۭا ضَآلِّينَ
- (28:27) [next to 28:29] قَالَ إِنِّىٓ أُرِيدُ أَنْ أُنكِحَكَ إِحْدَى ٱبْنَتَىَّ هَٰتَيْنِ عَلَىٰٓ أَن تَأْجُرَنِى ثَمَٰنِىَ حِجَجٍۢ ۖ فَإِنْ أَتْمَمْتَ عَشْرًۭا فَمِنْ عِندِكَ ۖ وَمَآ أُرِيدُ أَنْ أَشُقَّ عَلَيْكَ ۚ سَتَجِدُنِىٓ إِن شَآءَ ٱللَّهُ مِنَ ٱلصَّٰلِحِينَ
- (28:28) [next to 28:29] قَالَ ذَٰلِكَ بَيْنِى وَبَيْنَكَ ۖ أَيَّمَا ٱلْأَجَلَيْنِ قَضَيْتُ فَلَا عُدْوَٰنَ عَلَىَّ ۖ وَٱللَّهُ عَلَىٰ مَا نَقُولُ وَكِيلٌۭ
- (28:30) [next to 28:29] فَلَمَّآ أَتَىٰهَا نُودِىَ مِن شَٰطِئِ ٱلْوَادِ ٱلْأَيْمَنِ فِى ٱلْبُقْعَةِ ٱلْمُبَٰرَكَةِ مِنَ ٱلشَّجَرَةِ أَن يَٰمُوسَىٰٓ إِنِّىٓ أَنَا ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
- (28:31) [next to 28:29] وَأَنْ أَلْقِ عَصَاكَ ۖ فَلَمَّا رَءَاهَا تَهْتَزُّ كَأَنَّهَا جَآنٌّۭ وَلَّىٰ مُدْبِرًۭا وَلَمْ يُعَقِّبْ ۚ يَٰمُوسَىٰٓ أَقْبِلْ وَلَا تَخَفْ ۖ إِنَّكَ مِنَ ٱلْءَامِنِينَ
- (33:41) [next to 33:43] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱذْكُرُوا۟ ٱللَّهَ ذِكْرًۭا كَثِيرًۭا
- (33:42) [next to 33:43] وَسَبِّحُوهُ بُكْرَةًۭ وَأَصِيلًا
- (33:44) [next to 33:43] تَحِيَّتُهُمْ يَوْمَ يَلْقَوْنَهُۥ سَلَٰمٌۭ ۚ وَأَعَدَّ لَهُمْ أَجْرًۭا كَرِيمًۭا
- (33:45) [next to 33:43] يَٰٓأَيُّهَا ٱلنَّبِىُّ إِنَّآ أَرْسَلْنَٰكَ شَٰهِدًۭا وَمُبَشِّرًۭا وَنَذِيرًۭا
- (48:23) [next to 48:25] سُنَّةَ ٱللَّهِ ٱلَّتِى قَدْ خَلَتْ مِن قَبْلُ ۖ وَلَن تَجِدَ لِسُنَّةِ ٱللَّهِ تَبْدِيلًۭا
- (48:24) [next to 48:25] وَهُوَ ٱلَّذِى كَفَّ أَيْدِيَهُمْ عَنكُمْ وَأَيْدِيَكُمْ عَنْهُم بِبَطْنِ مَكَّةَ مِنۢ بَعْدِ أَنْ أَظْفَرَكُمْ عَلَيْهِمْ ۚ وَكَانَ ٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرًا
- (48:27) [next to 48:25] لَّقَدْ صَدَقَ ٱللَّهُ رَسُولَهُ ٱلرُّءْيَا بِٱلْحَقِّ ۖ لَتَدْخُلُنَّ ٱلْمَسْجِدَ ٱلْحَرَامَ إِن شَآءَ ٱللَّهُ ءَامِنِينَ مُحَلِّقِينَ رُءُوسَكُمْ وَمُقَصِّرِينَ لَا تَخَافُونَ ۖ فَعَلِمَ مَا لَمْ تَعْلَمُوا۟ فَجَعَلَ مِن دُونِ ذَٰلِكَ فَتْحًۭا قَرِيبًا
- (48:28) [next to 48:26] هُوَ ٱلَّذِىٓ أَرْسَلَ رَسُولَهُۥ بِٱلْهُدَىٰ وَدِينِ ٱلْحَقِّ لِيُظْهِرَهُۥ عَلَى ٱلدِّينِ كُلِّهِۦ ۚ وَكَفَىٰ بِٱللَّهِ شَهِيدًۭا
- (56:45) [next to 56:47] إِنَّهُمْ كَانُوا۟ قَبْلَ ذَٰلِكَ مُتْرَفِينَ
- (56:46) [next to 56:47] وَكَانُوا۟ يُصِرُّونَ عَلَى ٱلْحِنثِ ٱلْعَظِيمِ
- (56:48) [next to 56:47] أَوَءَابَآؤُنَا ٱلْأَوَّلُونَ
- (56:49) [next to 56:47] قُلْ إِنَّ ٱلْأَوَّلِينَ وَٱلْءَاخِرِينَ
- (56:69) [next to 56:71] ءَأَنتُمْ أَنزَلْتُمُوهُ مِنَ ٱلْمُزْنِ أَمْ نَحْنُ ٱلْمُنزِلُونَ
- (56:70) [next to 56:71] لَوْ نَشَآءُ جَعَلْنَٰهُ أُجَاجًۭا فَلَوْلَا تَشْكُرُونَ
- (56:72) [next to 56:71] ءَأَنتُمْ أَنشَأْتُمْ شَجَرَتَهَآ أَمْ نَحْنُ ٱلْمُنشِـُٔونَ
- (56:74) [next to 56:73] فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ
- (56:75) [next to 56:73] ۞ فَلَآ أُقْسِمُ بِمَوَٰقِعِ ٱلنُّجُومِ
- (66:4) [next to 66:6] إِن تَتُوبَآ إِلَى ٱللَّهِ فَقَدْ صَغَتْ قُلُوبُكُمَا ۖ وَإِن تَظَٰهَرَا عَلَيْهِ فَإِنَّ ٱللَّهَ هُوَ مَوْلَىٰهُ وَجِبْرِيلُ وَصَٰلِحُ ٱلْمُؤْمِنِينَ ۖ وَٱلْمَلَٰٓئِكَةُ بَعْدَ ذَٰلِكَ ظَهِيرٌ
- (66:5) [next to 66:6] عَسَىٰ رَبُّهُۥٓ إِن طَلَّقَكُنَّ أَن يُبْدِلَهُۥٓ أَزْوَٰجًا خَيْرًۭا مِّنكُنَّ مُسْلِمَٰتٍۢ مُّؤْمِنَٰتٍۢ قَٰنِتَٰتٍۢ تَٰٓئِبَٰتٍ عَٰبِدَٰتٍۢ سَٰٓئِحَٰتٍۢ ثَيِّبَٰتٍۢ وَأَبْكَارًۭا
- (66:7) [next to 66:6] يَٰٓأَيُّهَا ٱلَّذِينَ كَفَرُوا۟ لَا تَعْتَذِرُوا۟ ٱلْيَوْمَ ۖ إِنَّمَا تُجْزَوْنَ مَا كُنتُمْ تَعْمَلُونَ
- (66:8) [next to 66:6] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ تُوبُوٓا۟ إِلَى ٱللَّهِ تَوْبَةًۭ نَّصُوحًا عَسَىٰ رَبُّكُمْ أَن يُكَفِّرَ عَنكُمْ سَيِّـَٔاتِكُمْ وَيُدْخِلَكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ يَوْمَ لَا يُخْزِى ٱللَّهُ ٱلنَّبِىَّ وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ ۖ نُورُهُمْ يَسْعَىٰ بَيْنَ أَيْدِيهِمْ وَبِأَيْمَٰنِهِمْ يَقُولُونَ رَبَّنَآ أَتْمِمْ لَنَا نُورَنَا وَٱغْفِرْ لَنَآ ۖ إِنَّكَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (84:10) [next to 84:12] وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ وَرَآءَ ظَهْرِهِۦ
- (84:13) [next to 84:12] إِنَّهُۥ كَانَ فِىٓ أَهْلِهِۦ مَسْرُورًا
- (84:14) [next to 84:12] إِنَّهُۥ ظَنَّ أَن لَّن يَحُورَ
- (87:10) [next to 87:12] سَيَذَّكَّرُ مَن يَخْشَىٰ
- (87:11) [next to 87:12] وَيَتَجَنَّبُهَا ٱلْأَشْقَى
- (87:14) [next to 87:12] قَدْ أَفْلَحَ مَن تَزَكَّىٰ
- (87:16) [next to 87:15] بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- (87:17) [next to 87:15] وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ
- (101:8) [next to 101:10] وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ
- (111:1) [next to 111:3] تَبَّتْ يَدَآ أَبِى لَهَبٍۢ وَتَبَّ
- (111:2) [next to 111:3] مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ

