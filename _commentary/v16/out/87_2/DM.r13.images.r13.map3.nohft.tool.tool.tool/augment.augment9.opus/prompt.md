Follow the brief below (augment.md) exactly. The commentary is a reading of the ayah 87:2; its ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/87_2/DM.r13.images.r13.map3.nohft.tool.tool.tool/87_2.reading.tr.md (prose paragraphs numbered) =====
## Kim olduğunu işleri söyleyen Rab

[¶1] Ayet yeni bir cümleyle başlamaz. Birinci ayetin emrine bağlı bir ilgi cümlesidir: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1}. Hemen ardından gelen {ar:ٱلَّذِى, tr:elleẕî, gloss:o ki, source:87:2} bu Rabbin kim olduğunu söyler. Ama bunu bir sıfatla yapmaz, bir işle yapar. "En yüce" diye anılan kişi göğün ötesine taşınmaz. Yaptığı işin içinde tanınır. Bu ilgi kelimesi sure açılırken üç kez tekrarlanır. İkinci ayette çıplak gelir, üçüncü ve dördüncü ayette başına "ve" alır. Böylece tesbih emri, hepsi aynı kişiyi anlatan üç basamaklı bir merdivene yaslanır.

[¶2] İki fiil de geçmiş zamandadır, ikisinin de nesnesi yoktur: {ar:خَلَقَ فَسَوَّىٰ, tr:halaka fe-sevvâ, gloss:yarattı ve düzene koydu, source:87:2}. Kur'an aynı ikiliyi başka yerlerde nesnesiyle söyler. İnsana {ar:ٱلَّذِى خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ, tr:elleẕî halakake fe-sevvâke fe-adeleke, gloss:seni yaratan, seni düzene koyup dengeleyen, source:82:7} diye seslenilir. Bir yeminde nefis anılır: {ar:وَنَفْسٍۢ وَمَا سَوَّىٰهَا, tr:ve nefsin ve mâ sevvâhâ, gloss:nefse ve onu düzene koyana andolsun, source:91:7}. Gök de anılır. Allah yaratılması daha zor olanın insanlar mı yoksa gök mü olduğunu sorar, sonra göğü kurduğunu ve {ar:رَفَعَ سَمْكَهَا فَسَوَّىٰهَا, tr:rafea semkehâ fe-sevvâhâ, gloss:tavanını yükseltip onu düzene koydu, source:79:28} der. Bizim ayetimizde nesne düşmüştür. Bu yüzden fiil bunların hepsini birden kapsar. Ayeti dinleyen kişi de kapsamın içindedir, çünkü birinci ayet "senin Rabbin" demiştir. Tesbih edilen ad, dinleyenin kendi bedeninde izini bulabileceği bir işin sahibidir.

[¶3] İki fiil arasındaki {ar:فَ, tr:fe, gloss:ve hemen ardından, source:87:2} da bir şey söyler. Arapçada bu bağlaç ara vermeden gelen sırayı bildirir, "sonra" anlamındaki ŝumme ise araya zaman koyar. İki bahçe benzetmesinde, bahçesine güvenen adama arkadaşı {source:18:37} "seni yarattı, sonra bir adam olarak düzene koydu" der. Orada araya bir ömür girer. Burada düzene koymak, yaratmadan sonra gelen ikinci bir yapım değildir. Aynı işin tamamlanışıdır.

[¶4] Kur'an aynı sırayı bir başka surede de kurar ve sürdürür. Göğün düzene konduğunu söyleyen ayetten birkaç ayet sonra yeryüzü için {ar:أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا, tr:ahrace minhâ mâehâ ve mer'âhâ, gloss:ondan suyunu ve otlağını çıkardı, source:79:31} denir. Bu, dördüncü ayetin {ar:أَخْرَجَ ٱلْمَرْعَىٰ, tr:ahraca'l-mer'â, gloss:otlağı çıkardı, source:87:4} sözünün aynısıdır. İki surede de düzene koymaktan otlağa giden bir yol vardır.

## Kesmeden önce ölçen el

[¶5] خَلَقَ fiili bugün "yarattı" diye çevrilir ve bu doğrudur. Ama Araplar aynı fiili bir zanaatkârın işi için de kullanırlardı. Bundan sonra anılacak aile görüntüleri ayetteki anlamın yerine geçmez, onun yanında duyulur. Bir su tulumu yapılacakken deri önce ölçülür: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme iẕâ kaddertuhû kable'l-kat', gloss:deriyi kesmeden önce ölçtüğümde "halaktu" derim, source:"خ ل ق,B001"}. Bu işin mantığı basittir. Bıçak deriye bir kez girdi mi yanlış kesik geri alınmaz. Tulumun su tutup tutmayacağı kesimden önceki ölçüde belli olur. Kelimenin aslı da bu yönde tarif edilir: {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhû et-takdîru'l-mustakîm, gloss:halkın aslı doğru ölçüdür, source:"خ ل ق,B001"}. Böylece ikinci ayetin ilk fiili, üçüncü ayetin {ar:قَدَّرَ, tr:kaddera, gloss:ölçüsünü koydu, source:87:3} fiilini daha baştan içinde taşır. Sure ikinci ayette yoğun söylediğini üçüncü ayette açar. Kur'an bu iki fiili başka yerlerde de art arda söyler: {ar:وَخَلَقَ كُلَّ شَىْءٍۢ فَقَدَّرَهُۥ تَقْدِيرًۭا, tr:ve halaka kulle şey'in fe-kaddarahû takdîrâ, gloss:her şeyi yarattı ve onu tam bir ölçüyle ölçtü, source:25:2}, {ar:إِنَّا كُلَّ شَىْءٍ خَلَقْنَٰهُ بِقَدَرٍۢ, tr:innâ kulle şey'in halaknâhu bi-kader, gloss:biz her şeyi bir ölçüyle yarattık, source:54:49}.

[¶6] Aynı fiilin öbür yüzü zanaatkârın elinde bulunmaz. Kelime {ar:ابتداع الشيء على مثال لم يسبق إليه, tr:ibtidâu'ş-şey'i alâ misâlin lem yusbak ileyh, gloss:bir şeyi daha önce kimsenin varmadığı bir örnekte ortaya koymak, source:"خ ل ق,B002"} diye de tarif edilir. Bu, hem hiçbir asıldan olmadan var etmeyi hem de bir şeyden başka bir şey çıkarmayı kapsar {source:"خ ل ق,B002"}. Deriyi ölçen usta bir kalıba bakar. Ayetin öznesi ise ölçüyü hiçbir kalıba bakmadan koyar. Fiil ustanın titizliğini alır, kalıba muhtaçlığını almaz.

[¶7] Türkçe bu kökten çok kelime almıştır: halk, mahlûk, hilkat. Ama "halk" bugün yalnızca insan topluluğu demektir. Yaratılmışların kalabalığı kalmış, onları ölçüp biçen el kelimeden çekilmiştir. Arapça kelime o eli hâlâ taşır.

[¶8] Ölçülen şey, ölçüldüğü işe yaraşır hale gelir. Araplar birine bir şeye uygun düştüğü için {ar:فلان خليق بكذا, tr:fulânun halîkun bi-keẕâ, gloss:falan şuna yaraşır, source:"خ ل ق,B005"} derlerdi. Bu söz {ar:كأنه مخلوق فيه ذلك, tr:keennehû mahlûkun fîhi ẕâlik, gloss:sanki o şey içine yaratılmış, source:"خ ل ق,B005"} diye açıklanırdı. Yani yaratılmış olmak, bir şeye yatkın olarak yapılmış olmaktır. Üçüncü ayet ölçünün ardından {ar:فَهَدَىٰ, tr:fe-hedâ, gloss:ve yol gösterdi, source:87:3} der. Ölçülen ve yöne çevrilen nesnenin, yani yontulan okun ve ucunun sahnesi o ayetin kelimeleriyle kurulur. Ölçünün bir başka yüzü de paydır. Araplar payı {ar:الخلاق النصيب لأنه قد قدر لكل أحد نصيبه, tr:el-halâku en-nasîbu li-ennehû kad kuddira li-kulli ehadin nasîbuh, gloss:halâk paydır, çünkü herkesin payı ölçülmüştür, source:"خ ل ق,B006"} diye anlatırdı. Kur'an hacdan sonra yalnız dünya için dua eden kişi hakkında {ar:وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ, tr:ve mâ lehû fi'l-âhireti min halâk, gloss:onun ahirette hiçbir payı yoktur, source:2:200} der. On altıncı ve on yedinci ayetteki dünya ile ahiret arasındaki seçim, bu ölçülmüş payın seçimi olarak oradan okunur.

## Eğriyi doğrultmak, eksiği tamamlamak

[¶9] سَوَّىٰ fiilinin en yakın anlamı bir şeyi düzeltip tam ve düzgün duruma getirmektir: {ar:سويت الشيء فاستوى, tr:sevvaytu'ş-şey'e fe'stevâ, gloss:onu düzelttim, o da düzeldi, source:"س و ي,B002"}. Bir eğrinin doğrulması için de {ar:استوى من اعوجاج, tr:istevâ min i'vicâc, gloss:eğrilikten doğruldu, source:"س و ي,B002"} denir. Böyle düzeltilmiş bir canlıya {ar:السوي الذي سوى الله خلقه لا دمامة فيه ولا داء, tr:es-seviyyu elleẕî sevvallâhu halkahû lâ demâmete fîhi ve lâ dâ', gloss:seviyy Allah'ın yaratılışını düzgün kıldığı kişidir, onda ne çirkinlik vardır ne hastalık, source:"س و ي,B002"} denir. Ölçü de şöyle verilir: {ar:السوي يقال فيما يصان عن الإفراط والتفريط, tr:es-seviyyu yukâlu fî mâ yusânu ani'l-ifrâti ve't-tefrît, gloss:seviyy aşırılıktan da eksiklikten de korunmuş olana denir, source:"س و ي,B002"}. Düzene koymak bu yüzden süslemek değildir. Fazlayı almak, eksiği tamamlamaktır. Kökün temeli bunu ilişki olarak kurar: {ar:أصل يدل على استقامة واعتدال بين شيئين, tr:aslun yedullu alâ istikâmetin ve'tidâlin beyne şey'eyn, gloss:iki şey arasında doğruluk ve denge gösteren kök, source:"س و ي,B001"}. Düzene konmuş şey tek başına düzgün değildir. Parçaları birbirine, kendisi de ölçüsüne denktir. Seksen ikinci surenin ikiliye eklediği {ar:فَعَدَلَكَ, tr:fe-adeleke, gloss:ve seni dengeledi, source:82:7} sözü bu denkliği ayrıca adlandırır.

[¶10] Türkçe de bu kökten kelimeler almıştır: seviye, tesviye, müsavi. Tesviye bugün toprağı düzlemek ya da metali eğeyle düzeltmek demektir. Bir yüzeyi düzleme anlamı kalmıştır. Ama Arapçadaki "hiçbir yeri eksik ya da fazla bırakmadan tamamlamak" anlamı Türkçeye geçmemiştir.

[¶11] Tamlığın bir gökyüzü örneği de vardır. Ayın on üçüncü gecesine {ar:ليلة السواء, tr:leyletu's-sevâ', gloss:dengeli gece, source:"س و ي,B012"} denirdi, çünkü {ar:وفيها يستوي القمر, tr:ve fîhâ yestevi'l-kamer, gloss:o gece ay dengeye gelir, source:"س و ي,B012"}. Ay bu dengeye bir gecede varmaz, ince bir hilalden gece gece varır. Fiil bu yönüyle bir olgunlaşmanın sonunu adlandırır.

[¶12] Kökün bir başka kullanımı tam tersini söyler. Bir şeyi atlayıp dışarıda bırakmak için de bu kökten bir fiil kullanılır, örnek cümlesi de dikkat çekicidir: {ar:أسوى فلان حرفا من كتاب الله أي أسقط وأغفل, tr:esvâ fulânun harfen min kitâbillâhi ey eskata ve ağfele, gloss:falan Allah'ın kitabından bir harfi atladı, yani düşürdü ve gözden kaçırdı, source:"س و ي,B011"}. Bu ayrı bir fiil kalıbıdır ve ayetteki fiil değildir. Yalnızca aynı kökten gelir. Yine de altıncı ve yedinci ayetin vaadi, {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız, sen de unutmayacaksın, source:87:6}, bu kullanımın tam karşısında durur. Hiçbir şeyi eksik bırakmadan düzene koyan, okuttuğundan tek harfin düşmemesini de üstlenir.

[¶13] Bu ayetin iki kökü bir noktada birbirine değer. خلق ailesinde pürüzsüzlük anlamı da vardır ve bu anlam سوى kökünün kelimesiyle tarif edilir. Yontulmuş bir ok gövdesi için {ar:سهم مخلق أملس مستو, tr:sehmun muhallakun emlesu mustevin, gloss:yontulmuş, pürüzsüz ve dosdoğru ok, source:"خ ل ق,B008"} denir. Bir ip ya da yay kirişi için de {ar:خلقت الحبل والوتر وغيرهما تخليقا إذا ملسته, tr:hallaktu'l-hable ve'l-vetera ve ğayrahumâ tahlîkan iẕâ mellestuh, gloss:ipi, kirişi ve benzerlerini pürüzsüzleştirdiğimde "hallaktu" derim, source:"خ ل ق,B008"} denir. Bu iki kök aynı kök değildir. Ama okun nasıl yapıldığı anlatılırken biri ötekini çağırır. Ok gövdesi önce ölçülüp kesilir, sonra pürüzü alınır, sonra doğrultulur. Gövdesi eğri bir ok hedefe gitmez, ne kadar güçlü atılırsa o kadar sapar. Ayetin iki fiili bu işin iki evresi gibi duyulur. Okun ucunu takıp onu hedefe çevirmek ise üçüncü ayetin fiillerine kalır.

## Bir damladan ölçülü bir insana

[¶14] Kur'an ayetimizin iki kelimesini, bağlacıyla birlikte, bir başka surede de aynen kullanır. Orada konu ana rahmidir. Allah önce {ar:أَيَحْسَبُ ٱلْإِنسَٰنُ أَن يُتْرَكَ سُدًى, tr:e-yahsebu'l-insânu en yutreke sudâ, gloss:insan başıboş bırakılacağını mı sanıyor, source:75:36} diye sorar, sonra insanın kökenini hatırlatır: {ar:أَلَمْ يَكُ نُطْفَةًۭ مِّن مَّنِىٍّۢ يُمْنَىٰ, tr:e-lem yeku nutfeten min meniyyin yumnâ, gloss:dökülen meniden bir damla değil miydi, source:75:37}, {ar:ثُمَّ كَانَ عَلَقَةًۭ فَخَلَقَ فَسَوَّىٰ, tr:ŝumme kâne alakaten fe-halaka fe-sevvâ, gloss:sonra bir alaka oldu; O da yarattı ve düzene koydu, source:75:38}. Bu kısa bölüm, bunu yapanın ölüleri diriltmeye gücü yetip yetmediğini soran ayetle biter {source:75:40}. Aynı surenin başında Allah, insanın kemiklerinin toplanmayacağını sanmasına {ar:بَلَىٰ قَٰدِرِينَ عَلَىٰٓ أَن نُّسَوِّىَ بَنَانَهُۥ, tr:belâ kâdirîne alâ en nusevviye benâneh, gloss:evet, onun parmak uçlarını bile düzene koymaya gücümüz yeter, source:75:4} diye cevap verir. Düzene koymak burada en ince ayrıntıya kadar iner ve ikinci kez yaratmanın adı olur.

[¶15] Arapça bu evreleri خلق kökünün kendisiyle de adlandırır. Biçimi belirmiş cenin için {ar:مضغة مخلقة أي تامة الخلق, tr:mudğatun muhallakatun ey tâmmetu'l-halk, gloss:yaratılışı tamamlanmış et parçası, source:"خ ل ق,B003"} denir. Biçimi belirmemiş olan için de {ar:غير مخلقة لم تصور, tr:ğayru muhallakatin lem tusavvar, gloss:henüz biçim almamış, source:"خ ل ق,B003"} denir. Kur'an bu ikisini yeniden dirilişten şüphe edenlere hitap ederken kullanır: {ar:ثُمَّ مِن مُّضْغَةٍۢ مُّخَلَّقَةٍۢ وَغَيْرِ مُخَلَّقَةٍۢ, tr:ŝumme min mudğatin muhallakatin ve ğayri muhallaka, gloss:sonra biçimlenmiş ve biçimlenmemiş bir et parçasından, source:22:5}. Boyu bosu yerinde bir adama da {ar:رجل خليق ومختلق أي تام الخلق معتدل, tr:raculun halîkun ve muhtelakun ey tâmmu'l-halki mu'tedil, gloss:yaratılışı tam ve dengeli adam, source:"خ ل ق,B003"} denirdi. Yani "yaratılmış" sıfatının kendisi tamlık ve denge demektir. Kur'an düzgün bir insan görüntüsünü de bu ayetin köküyle anlatır. Meryem ailesinden çekilip bir perde ardına geçtiğinde Allah ona ruhunu gönderir, ruh da ona {ar:بَشَرًۭا سَوِيًّۭا, tr:beşeran seviyyâ, gloss:kusursuz bir insan, source:19:17} biçiminde görünür. Meleklere insanı yaratacağını bildirdiğinde de Rab {ar:فَإِذَا سَوَّيْتُهُۥ وَنَفَخْتُ فِيهِ مِن رُّوحِى فَقَعُوا۟ لَهُۥ سَٰجِدِينَ, tr:fe-iẕâ sevveytuhû ve nefahtu fîhi min rûhî fe-kaû lehû sâcidîn, gloss:onu düzene koyup içine ruhumdan üflediğimde ona secdeye kapanın, source:15:29} der. Ruhun üflenmesi düzene koymayı bekler. Tamamlanmış kalıp, içine konacak olana hazırlanmıştır.

[¶16] Düzene konmak bir ömre de yayılır. Arapçada {ar:استوى الرجل إذا انتهى شبابه, tr:istevâ'r-raculu iẕe'ntehâ şebâbuh, gloss:adamın gençliği tamamlanınca "istevâ" denir, source:"س و ي,B005"}. Kur'an bunu, surenin son ayetinde sayfaları anılan Musa için söyler: {ar:وَلَمَّا بَلَغَ أَشُدَّهُۥ وَٱسْتَوَىٰٓ ءَاتَيْنَٰهُ حُكْمًۭا وَعِلْمًۭا, tr:ve lemmâ beleğa eşuddehû ve'stevâ âteynâhu hukmen ve ilmâ, gloss:olgunluk çağına ulaşıp kemale erince ona hüküm ve ilim verdik, source:28:14}. Rahimde başlayan düzen, bir delikanlının olgunluğunda tamamlanır ve ilim almaya hazır hale getirir.

[¶17] Düzene konan yalnız beden değildir. Arapça dış biçimi ve iç huyu aynı kökün iki kelimesiyle söyler. İç huya {ar:الخلق وهي السجية, tr:el-hulku ve hiye's-seciyye, gloss:huy, yaradılıştan gelen karakter, source:"خ ل ق,B004"} denir. Bir ayrım da yapılır: biri gözle görülen biçimlere, öteki basiretle sezilen güç ve huylara aittir {source:"خ ل ق,B004"}. Kur'an düzene koymayı ruha da uygular. Nefse ve onu düzene koyana yemin edildikten hemen sonra {ar:فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا, tr:fe-elhemehâ fucûrahâ ve takvâhâ, gloss:ona yoldan çıkışını da sakınmasını da ilham etti, source:91:8} denir. Sıra bizim surenin sırasıyla aynıdır: önce düzene koymak, sonra yön göstermek. Altıncı ayetin fiilinin ailesindeki rahim görüntüsü, yani rahmin yavrunun üzerine kapanması, o ayetin kelimesiyle bu bedene dair resme eklenir.

## Düz yürüyen ve dosdoğru yol

[¶18] سَوِيّ sıfatı Kur'an'da bir yürüyüşü de anlatır, ve orada üçüncü ayetin fiili hemen yanında durur. Allah rızkı kesse kimin vereceğini sorduktan sonra şöyle der: {ar:أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:e-fe-men yemşî mukibben alâ vechihî ehdâ em-men yemşî seviyyen alâ sırâtın mustekîm, gloss:yüzüstü kapanarak yürüyen mi daha doğru yoldadır, yoksa dosdoğru bir yolda dik yürüyen mi, source:67:22}. Burada düzene konmuş beden, yolunu bulan bedendir. Yüzü yere dönük olan önünü göremez, dik yürüyen görür. Kur'an'ın her namazda okunan duası bu yolu ister: {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdine's-sırâta'l-mustekîm, gloss:bizi dosdoğru yola ilet, source:1:6}. "Doğru" anlamındaki bu kelime, bu ayetin iki kökünün tanımında da geçer. خلق'in aslı {ar:التقدير المستقيم, tr:et-takdîru'l-mustakîm, gloss:doğru ölçü, source:"خ ل ق,B001"} diye verilmişti, سوى kökü de {ar:استقامة واعتدال, tr:istikâme ve i'tidâl, gloss:doğruluk ve denge, source:"س و ي,B001"} diye. Bu ortak kök değil, ortak bir tanım kelimesidir. Yine de Arapçanın kendisi, bu iki fiili tarif ederken Fatiha'nın yoluna ait kelimeye başvurur.

[¶19] Surenin son ayetinde adı geçen İbrahim de bu iki kelimeyi birlikte kullanır. İşitmeyen, görmeyen ve hiçbir işe yaramayan bir şeye neden taptığını babasına sorduktan sonra ona şöyle der: {ar:فَٱتَّبِعْنِىٓ أَهْدِكَ صِرَٰطًۭا سَوِيًّۭا, tr:fettebi'nî ehdike sırâtan seviyyâ, gloss:bana uy da seni düzgün bir yola ileteyim, source:19:43}. Başka bir surenin son ayetinde de bekleşen iki taraf için {ar:فَسَتَعْلَمُونَ مَنْ أَصْحَٰبُ ٱلصِّرَٰطِ ٱلسَّوِىِّ وَمَنِ ٱهْتَدَىٰ, tr:fe-se-ta'lemûne men ashâbu's-sırâti's-seviyyi ve meni'htedâ, gloss:düzgün yolun sahiplerinin ve doğru yolu bulanın kim olduğunu bileceksiniz, source:20:135} denir. İkinci ayetten üçüncü ayete geçiş, yani düzene koymaktan yol göstermeye geçiş, Kur'an'da defalarca tek bir cümlede birleşir. Düzgün yapılmış olan, düzgün bir yolda yürümek için yapılmıştır.

[¶20] Aynı kökün bir anlamı da ortadır: {ar:مكان سوى أي عدل ووسط, tr:mekânun suven ey adlun ve vasat, gloss:dengeli, ortada bir yer, source:"س و ي,B006"}. Ama bu kelime tek başına güvenlik vermez. Cennetteki bir kişi dünyadaki eski arkadaşını arar ve {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fettalea fe-raâhu fî sevâi'l-cahîm, gloss:baktı ve onu cehennemin tam ortasında gördü, source:37:55}. Denge kendi başına bir değer değildir. Neyin ortasında durulduğu önemlidir. Kolaylaşan, yana çekilen ve önden giden yolun sahnesi sekizinci, on birinci ve üçüncü ayetin kelimeleriyle kurulur.

## Bineğin sırtında tesbih

[¶21] سوى kökü, bu ayetteki biçimden farklı bir biçimde, bir binicinin hareketini de adlandırır: {ar:استوى على ظهر دابته أي علا واستقر, tr:istevâ alâ zahri dâbbetihî ey alâ ve'stekarr, gloss:hayvanının sırtına çıkıp yerleşti, source:"س و ي,B003"}. Deve sırtına konan dolgulu bir örtünün adı da bu ailedendir: {ar:السَّويّة كساء محشو بثمام ونحوه كالبرذعة, tr:es-seviyye kisâun mahşuvvun bi-ŝumâmin ve nahvihî ke'l-berẕaa, gloss:seviyye, içi kuru otla doldurulmuş, semere benzer bir örtüdür, source:"س و ي,B010"}. Bu örtü hörgücün çevresine sarılır {source:"س و ي,B010"}. Böylece binen kişi engebeli bir sırtta oturabileceği bir yer bulur. Bu kelimeler ayetin fiili değildir, aynı kökün başka kalıplarıdır. Ama Kur'an bu kalıbı tam da ayetimizinkine benzeyen bir cümle örgüsünün içine koyar.

[¶22] Orada konuşulanlar, gökleri ve yeri kimin yarattığı sorulunca "Güçlü ve Bilen" diyecek olanlardır {source:43:9}. Ardından bir dizi ilgi cümlesi gelir. Yeryüzünü beşik yapan ve {ar:وَجَعَلَ لَكُمْ فِيهَا سُبُلًۭا لَّعَلَّكُمْ تَهْتَدُونَ, tr:ve ceale lekum fîhâ subulen leallekum tehtedûn, gloss:yolunuzu bulasınız diye orada size yollar açan, source:43:10} odur. Gökten {ar:مَآءًۢ بِقَدَرٍۢ, tr:mâen bi-kader, gloss:ölçüyle bir su, source:43:11} indiren ve ölü bir beldeyi onunla dirilten de odur. Sonra şu gelir: {ar:وَٱلَّذِى خَلَقَ ٱلْأَزْوَٰجَ كُلَّهَا, tr:velleẕî halaka'l-ezvâce kullehâ, gloss:bütün çiftleri yaratan, source:43:12}. Bu yaratan size binilecek gemiler ve hayvanlar da vermiştir. Bu, ayetimizin kelimesi kelimesine aynı açılışıdır. Amaç da söylenir: {ar:لِتَسْتَوُۥا۟ عَلَىٰ ظُهُورِهِۦ ثُمَّ تَذْكُرُوا۟ نِعْمَةَ رَبِّكُمْ إِذَا ٱسْتَوَيْتُمْ عَلَيْهِ وَتَقُولُوا۟ سُبْحَٰنَ ٱلَّذِى سَخَّرَ لَنَا هَٰذَا, tr:li-testevû alâ zuhûrihî ŝumme teẕkurû ni'mete rabbikum iẕe'steveytum aleyhi ve tekûlû subhâne'lleẕî sahhara lenâ hâẕâ, gloss:sırtlarına kurulasınız, kurulduğunuzda Rabbinizin nimetini anasınız ve "Bunu bizim buyruğumuza veren arınmıştır" diyesiniz diye, source:43:13}.

[¶23] Sahne surenin açılışına çok yakındır. Orada da yol, ölçü, yaratma, toprağın canlanması ve "alleẕî" ile başlayan bir tesbih vardır. Bizim surede tesbih bir emirdir ve ilgi cümleleri onun gerekçesidir. Orada ise tesbih bineğin sırtında, binicinin yerleştiği anda söylenecek söz olarak verilir. Aynı kökün iki kalıbı bu iki sahneyi birbirine bağlar. Rab yaratılışı düzene koyar, insan da düzene konmuş bir sırtta dengesini bulur ve bunu kimin sağladığını anar. O bölüm de surenin son ayetlerindeki dönüşü önceden söyleyerek biter: {ar:وَإِنَّآ إِلَىٰ رَبِّنَا لَمُنقَلِبُونَ, tr:ve innâ ilâ rabbinâ le-munkalibûn, gloss:biz elbette Rabbimize döneceğiz, source:43:14}.

[¶24] Kök göğe çevrildiğinde de iki kalıp yan yana durur. Yerdekilerin hepsini insanlar için yarattığını söyleyen Allah için {ar:ثُمَّ ٱسْتَوَىٰٓ إِلَى ٱلسَّمَآءِ فَسَوَّىٰهُنَّ سَبْعَ سَمَٰوَٰتٍۢ, tr:ŝumme'stevâ ile's-semâi fe-sevvâhunne seb'a semâvât, gloss:sonra göğe yöneldi ve onları yedi gök olarak düzene koydu, source:2:29} denir. Göğe yönelmek için kullanılan kalıp {ar:استوى إلى السماء أي قصد, tr:istevâ ile's-semâi ey kasada, gloss:göğe yöneldi, yani onu amaç edindi, source:"س و ي,B004"} diye açıklanır. Ayetimizde kullanılan "düzene koymak" ise bu yönelişin ürünüdür.

## Düzlenen kaya, yıpranan giysi, yerle bir edilen yurt

[¶25] خلق kökünün pürüzsüzlük anlamı bir kayaya da ad verir: {ar:صخرة خلقاء ملساء, tr:sahratun halkâu melsâ', gloss:dümdüz, kaygan bir kaya, source:"خ ل ق,B008"}. Böyle bir kayanın yüzeyinden yağmur suyu akıp gider. Ama kayada bir oyuk varsa su orada kalır, ve Araplar bu oyuklara da aynı kökten ad verirdi: {ar:الخليقة نقر في صخرة يجتمع فيه ماء السماء, tr:el-halîkatu nakrun fî sahratin yectemiu fîhi mâu's-semâ', gloss:halîka, kayada gök suyunun toplandığı oyuktur, source:"خ ل ق,B011"}. Bunlar {ar:قلاتا تمسك ماء السحاب في صفاة خلقها الله فيها, tr:kılâten tumsiku mâe's-sehâbi fî safâtin halakahallâhu fîhâ, gloss:düz kayada Allah'ın yarattığı, bulut suyunu tutan çukurlar, source:"خ ل ق,B011"} diye anlatılır. Yeni kazılmış kuyuya da aynı ad verilir: {ar:الخليقة البئر ساعة تحفر, tr:el-halîkatu'l-bi'ru sâate tuhfer, gloss:halîka, kazıldığı anki kuyudur, source:"خ ل ق,B011"}. Yaratılan şey burada bir doluluk değil, tutan bir boşluktur. Bu boşluk akıp gidecek olanı alıkoyar. Selin götürdüğü döküntü ile yerde kalan faydanın sahnesi beşinci, dokuzuncu ve on yedinci ayetin kelimeleriyle kurulur. Bu ayetin kelimesi ona suyu tutan oyuğu katar.

[¶26] Aynı pürüzsüzlüğün bir de aşınma yüzü vardır. Eskiyen bir şey için {ar:أخلق الشيء وخلق إذا بلي, tr:ahleka'ş-şey'u ve haluka iẕâ beliye, gloss:bir şey yıpranınca "ahleka" ve "haluka" denir, source:"خ ل ق,B009"} denir. Bunun nasıl olduğu da anlatılır: {ar:إذا أخلق املاس وذهب زئبره, tr:iẕâ ahleka'mlâsse ve ẕehebe zi'biruh, gloss:eskiyince düzleşir ve tüyü gider, source:"خ ل ق,B009"}. Terk edilmiş bir yurdun izi için de {ar:رسم مخلولق إذا استوى بالأرض, tr:resmun muhlevlikun iẕe'stevâ bi'l-ard, gloss:iz, yerle bir olduğunda "muhlevlik" denir, source:"خ ل ق,B008"} denir. Bu tanımda سوى kökü yine geçer. Yontulmuş okun düzlüğü tamlıktır. Eskimiş giysinin ve silinmiş izin düzlüğü ise bitiştir. Arapça ikisini aynı pürüzsüzlük kelimesiyle söyler.

[¶27] Kur'an da سَوَّىٰ fiilini bu yönde kullanır, ayetimizdeki biçimin aynısıyla. Nefsin düzene konduğunu söyleyen surede Semud kavmi, Allah'ın elçisinin "Allah'ın dişi devesine ve onun su payına dokunmayın" uyarısını yalanlar ve deveyi keser. Sonuç şudur: {ar:فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا, tr:fe-demdeme aleyhim rabbuhum bi-ẕenbihim fe-sevvâhâ, gloss:Rableri günahları yüzünden onları ezip geçti ve yurtlarını yerle bir etti, source:91:14}. Aynı surede aynı fiil iki kez geçer, bir kez nefsi düzene koymak, bir kez bir kavmi düzlemek için. Bir başka yerde inkâr edenler hesap günü {ar:لَوْ تُسَوَّىٰ بِهِمُ ٱلْأَرْضُ, tr:lev tusevvâ bihimu'l-ard, gloss:keşke yer onlarla birlikte düzlense, source:4:42} diye diler. Ayetimizde fiil düz anlamında kurmak ve tamamlamaktır. Ama Kur'an'ın içinde bu fiil yıkıcı ucunu da taşır: düzene koyan, düzlemeye de güç yetirendir. Sure bu iki ucu dördüncü ve beşinci ayette kendisi gösterir. Çıkarılan otlak, kararmış bir çerçöpe döner. İkinci ayetin fiili ise o sahneye bir eşik koyar: yıpranmanın düzlüğü yalnızca bir kez düzene konmuş olanın başına gelebilir.

## Yaratan ile uyduran

[¶28] خلق kökünün söz için kullanılan bir anlamı da vardır ve o anlam iyi değildir: {ar:كل موضع استعمل الخلق في وصف الكلام فالمراد به الكذب, tr:kullu mevdıin ustu'mile'l-halku fî vasfi'l-kelâmi fe'l-murâdu bihi'l-keẕib, gloss:halk kelimesi sözü nitelemek için kullanıldığı her yerde yalan kastedilir, source:"خ ل ق,B007"}. Yalan uydurmanın nasıl bir iş olduğu da anlatılır: {ar:اختلاقه واختراعه وتقديره في النفس, tr:ihtilâkuhû ve'htirâuhû ve takdîruhû fi'n-nefs, gloss:onu uydurmak, icat etmek ve zihninde ölçüp biçmek, source:"خ ل ق,B007"}. Başkasına mal edilmiş bir şiire de {ar:قصيدة مخلوقة أي منحولة, tr:kasîdetun mahlûkatun ey menhûle, gloss:uydurma, sahibine ait olmayan kaside, source:"خ ل ق,B007"} denirdi. Yalancı da ölçer. Ama yalnız kendi içinde ölçer ve dışarıda karşılığı olmayan bir şey kurar. Bu, ayetteki fiilin taklididir.

[¶29] Kur'an bu iki kullanımı, surenin son ayetinde adı geçen İbrahim'in sözlerinde karşı karşıya getirir. İbrahim kavmine Allah'a kulluk edip ondan sakınmalarını söyler, sonra şöyle der: {ar:إِنَّمَا تَعْبُدُونَ مِن دُونِ ٱللَّهِ أَوْثَٰنًۭا وَتَخْلُقُونَ إِفْكًا, tr:innemâ ta'budûne min dûnillâhi evŝânen ve tahlukûne ifkâ, gloss:siz Allah'ı bırakıp yalnızca putlara tapıyor ve yalan uyduruyorsunuz, source:29:17}. Aynı İbrahim, kendisine düşman olan tapınılan şeylerin karşısına Âlemlerin Rabbini koyar ve O'nu ayetimizin kelimesiyle tanıtır: {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:elleẕî halakanî fe-huve yehdîn, gloss:beni yaratan, bana yol gösteren O'dur, source:26:78}. Bu cümle surenin ikinci ve üçüncü ayetinin özüdür ve bir peygamberin ağzından söylenir.

[¶30] Kur'an yaratmayı doğrudan bir ölçüt olarak da kullanır: {ar:أَفَمَن يَخْلُقُ كَمَن لَّا يَخْلُقُ ۗ أَفَلَا تَذَكَّرُونَ, tr:e-fe-men yahluku ke-men lâ yahluk, e-fe-lâ teẕekkerûn, gloss:yaratan, yaratmayan gibi midir; hiç düşünmez misiniz, source:16:17}. Tanrı edinilenler için de {ar:لَا يَخْلُقُونَ شَيْـًۭٔا وَهُمْ يُخْلَقُونَ, tr:lâ yahlukûne şey'en ve hum yuhlakûn, gloss:hiçbir şey yaratmazlar, kendileri yaratılırlar, source:16:20} denir. Kendi kavminin önde gelenleri tek Tanrı çağrısını duyunca "Tanrıları tek bir tanrı mı yaptı?" deyip birbirlerine tanrılarına bağlı kalmayı öğütlerler. Sonra da bu çağrı için {ar:إِنْ هَٰذَآ إِلَّا ٱخْتِلَٰقٌ, tr:in hâẕâ ille'htilâk, gloss:bu, uydurmadan başka bir şey değil, source:38:7} derler. Kelime ters yöne çevrilmiştir. Gerçekten yaratana çağıran söz "uydurma" diye suçlanır.

[¶31] Kur'an bir insanın ağzına bu fiili bir kez de olumlu biçimde koyar ve ölçüp biçme anlamını sınırıyla birlikte gösterir. İsa İsrailoğullarına gönderildiğinde {ar:أَنِّىٓ أَخْلُقُ لَكُم مِّنَ ٱلطِّينِ كَهَيْـَٔةِ ٱلطَّيْرِ فَأَنفُخُ فِيهِ فَيَكُونُ طَيْرًۢا بِإِذْنِ ٱللَّهِ, tr:ennî ahluku lekum mine't-tîni ke-hey'eti't-tayri fe-enfuhu fîhi fe-yekûnu tayran bi-iẕnillâh, gloss:size çamurdan kuş biçiminde bir şey ölçüp biçerim, içine üflerim, o da Allah'ın izniyle kuş olur, source:3:49} der. Biçimi veren eldir. Onu canlı kılan ise izindir. Tesbih emrinin anlamı bu karşıtlıkta belirginleşir. "Tesbih etmek" bir adı, ona yakıştırılan her ortaktan ve her uydurmadan ayrı tutmaktır. İkinci ayet bu ayrı tutmanın gerekçesini tek bir fiile yükler: ölçüsünü kendisi koyan, eksiğini kendisi tamamlayan ve bunu hiçbir kalıba bakmadan yapan, yalnızca O'dur.

===== _commentary/v16/out/87_2/DM.r13.images.r13.map3.nohft.tool.tool.tool/ledger.md =====
- memory: Turkish seviye/tesviye/müsavi derive from the root س و ي
- memory: fa marks sequence with no gap, thumma marks sequence with an interval
- not written: خ ل ق B010 perfume khalūq - has no bearing on shaping or the surah
- not written: خ ل ق B012 closed womb - this would distort the body theme with no support
- not written: س و ي B007 siwā "other", B008 aiming at someone's aim - no link to the ayah's act
- not written: س و ي B009 open level land, B013 wealth equal to one's head - nothing for a theme to rest on
- not written: س و ي B006 makānan suwan (Musa–Pharaoh meeting place) - it added Musa again without new weight
- not written: images.md Musa-fire and sorcerers scenes - this ayah's words do not take part in them

===== passages not cited (294) =====
## strong (this ayah's own list) (18)

- (7:11) [listed for 87:2] وَلَقَدْ خَلَقْنَٰكُمْ ثُمَّ صَوَّرْنَٰكُمْ ثُمَّ قُلْنَا لِلْمَلَٰٓئِكَةِ ٱسْجُدُوا۟ لِءَادَمَ فَسَجَدُوٓا۟ إِلَّآ إِبْلِيسَ لَمْ يَكُن مِّنَ ٱلسَّٰجِدِينَ
- (15:29) [listed for 87:2] [cited in ¶15] فَإِذَا سَوَّيْتُهُۥ وَنَفَخْتُ فِيهِ مِن رُّوحِى فَقَعُوا۟ لَهُۥ سَٰجِدِينَ
- (18:37) [listed for 87:2] [cited in ¶3] قَالَ لَهُۥ صَاحِبُهُۥ وَهُوَ يُحَاوِرُهُۥٓ أَكَفَرْتَ بِٱلَّذِى خَلَقَكَ مِن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ سَوَّىٰكَ رَجُلًۭا
- (20:50) [listed for 87:2] قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ
- (23:14) [listed for 87:2] ثُمَّ خَلَقْنَا ٱلنُّطْفَةَ عَلَقَةًۭ فَخَلَقْنَا ٱلْعَلَقَةَ مُضْغَةًۭ فَخَلَقْنَا ٱلْمُضْغَةَ عِظَٰمًۭا فَكَسَوْنَا ٱلْعِظَٰمَ لَحْمًۭا ثُمَّ أَنشَأْنَٰهُ خَلْقًا ءَاخَرَ ۚ فَتَبَارَكَ ٱللَّهُ أَحْسَنُ ٱلْخَٰلِقِينَ
- (25:2) [listed for 87:2] [cited in ¶5] ٱلَّذِى لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلَمْ يَتَّخِذْ وَلَدًۭا وَلَمْ يَكُن لَّهُۥ شَرِيكٌۭ فِى ٱلْمُلْكِ وَخَلَقَ كُلَّ شَىْءٍۢ فَقَدَّرَهُۥ تَقْدِيرًۭا
- (30:54) [listed for 87:2] ۞ ٱللَّهُ ٱلَّذِى خَلَقَكُم مِّن ضَعْفٍۢ ثُمَّ جَعَلَ مِنۢ بَعْدِ ضَعْفٍۢ قُوَّةًۭ ثُمَّ جَعَلَ مِنۢ بَعْدِ قُوَّةٍۢ ضَعْفًۭا وَشَيْبَةًۭ ۚ يَخْلُقُ مَا يَشَآءُ ۖ وَهُوَ ٱلْعَلِيمُ ٱلْقَدِيرُ
- (32:9) [listed for 87:2] ثُمَّ سَوَّىٰهُ وَنَفَخَ فِيهِ مِن رُّوحِهِۦ ۖ وَجَعَلَ لَكُمُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ ۚ قَلِيلًۭا مَّا تَشْكُرُونَ
- (38:72) [listed for 87:2] فَإِذَا سَوَّيْتُهُۥ وَنَفَخْتُ فِيهِ مِن رُّوحِى فَقَعُوا۟ لَهُۥ سَٰجِدِينَ
- (40:67) [listed for 87:2] هُوَ ٱلَّذِى خَلَقَكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ مِنْ عَلَقَةٍۢ ثُمَّ يُخْرِجُكُمْ طِفْلًۭا ثُمَّ لِتَبْلُغُوٓا۟ أَشُدَّكُمْ ثُمَّ لِتَكُونُوا۟ شُيُوخًۭا ۚ وَمِنكُم مَّن يُتَوَفَّىٰ مِن قَبْلُ ۖ وَلِتَبْلُغُوٓا۟ أَجَلًۭا مُّسَمًّۭى وَلَعَلَّكُمْ تَعْقِلُونَ
- (54:49) [listed for 87:2] [cited in ¶5] إِنَّا كُلَّ شَىْءٍ خَلَقْنَٰهُ بِقَدَرٍۢ
- (64:3) [listed for 87:2] خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ وَصَوَّرَكُمْ فَأَحْسَنَ صُوَرَكُمْ ۖ وَإِلَيْهِ ٱلْمَصِيرُ
- (75:38) [listed for 87:2] [cited in ¶14] ثُمَّ كَانَ عَلَقَةًۭ فَخَلَقَ فَسَوَّىٰ
- (76:28) [listed for 87:2] نَّحْنُ خَلَقْنَٰهُمْ وَشَدَدْنَآ أَسْرَهُمْ ۖ وَإِذَا شِئْنَا بَدَّلْنَآ أَمْثَٰلَهُمْ تَبْدِيلًا
- (80:19) [listed for 87:2] مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ
- (82:7) [listed for 87:2] [cited in ¶2, ¶9] ٱلَّذِى خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ
- (91:7) [listed for 87:2] [cited in ¶2] وَنَفْسٍۢ وَمَا سَوَّىٰهَا
- (95:4) [listed for 87:2] لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ

## medium (this ayah's own list) (56)

- (2:29) [listed for 87:2] [cited in ¶24] هُوَ ٱلَّذِى خَلَقَ لَكُم مَّا فِى ٱلْأَرْضِ جَمِيعًۭا ثُمَّ ٱسْتَوَىٰٓ إِلَى ٱلسَّمَآءِ فَسَوَّىٰهُنَّ سَبْعَ سَمَٰوَٰتٍۢ ۚ وَهُوَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (3:6) [listed for 87:2] هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (6:1) [listed for 87:2] ٱلْحَمْدُ لِلَّهِ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَجَعَلَ ٱلظُّلُمَٰتِ وَٱلنُّورَ ۖ ثُمَّ ٱلَّذِينَ كَفَرُوا۟ بِرَبِّهِمْ يَعْدِلُونَ
- (6:2) [listed for 87:2] هُوَ ٱلَّذِى خَلَقَكُم مِّن طِينٍۢ ثُمَّ قَضَىٰٓ أَجَلًۭا ۖ وَأَجَلٌۭ مُّسَمًّى عِندَهُۥ ۖ ثُمَّ أَنتُمْ تَمْتَرُونَ
- (7:54) [listed for 87:2] إِنَّ رَبَّكُمُ ٱللَّهُ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ يُغْشِى ٱلَّيْلَ ٱلنَّهَارَ يَطْلُبُهُۥ حَثِيثًۭا وَٱلشَّمْسَ وَٱلْقَمَرَ وَٱلنُّجُومَ مُسَخَّرَٰتٍۭ بِأَمْرِهِۦٓ ۗ أَلَا لَهُ ٱلْخَلْقُ وَٱلْأَمْرُ ۗ تَبَارَكَ ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
- (10:3) [listed for 87:2] إِنَّ رَبَّكُمُ ٱللَّهُ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ ۖ يُدَبِّرُ ٱلْأَمْرَ ۖ مَا مِن شَفِيعٍ إِلَّا مِنۢ بَعْدِ إِذْنِهِۦ ۚ ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ فَٱعْبُدُوهُ ۚ أَفَلَا تَذَكَّرُونَ
- (10:5) [listed for 87:2] هُوَ ٱلَّذِى جَعَلَ ٱلشَّمْسَ ضِيَآءًۭ وَٱلْقَمَرَ نُورًۭا وَقَدَّرَهُۥ مَنَازِلَ لِتَعْلَمُوا۟ عَدَدَ ٱلسِّنِينَ وَٱلْحِسَابَ ۚ مَا خَلَقَ ٱللَّهُ ذَٰلِكَ إِلَّا بِٱلْحَقِّ ۚ يُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَعْلَمُونَ
- (10:34) [listed for 87:2] قُلْ هَلْ مِن شُرَكَآئِكُم مَّن يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ ۚ قُلِ ٱللَّهُ يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ ۖ فَأَنَّىٰ تُؤْفَكُونَ
- (13:16) [listed for 87:2] قُلْ مَن رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ قُلِ ٱللَّهُ ۚ قُلْ أَفَٱتَّخَذْتُم مِّن دُونِهِۦٓ أَوْلِيَآءَ لَا يَمْلِكُونَ لِأَنفُسِهِمْ نَفْعًۭا وَلَا ضَرًّۭا ۚ قُلْ هَلْ يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ أَمْ هَلْ تَسْتَوِى ٱلظُّلُمَٰتُ وَٱلنُّورُ ۗ أَمْ جَعَلُوا۟ لِلَّهِ شُرَكَآءَ خَلَقُوا۟ كَخَلْقِهِۦ فَتَشَٰبَهَ ٱلْخَلْقُ عَلَيْهِمْ ۚ قُلِ ٱللَّهُ خَٰلِقُ كُلِّ شَىْءٍۢ وَهُوَ ٱلْوَٰحِدُ ٱلْقَهَّٰرُ
- (14:32) [listed for 87:2] ٱللَّهُ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ ۖ وَسَخَّرَ لَكُمُ ٱلْفُلْكَ لِتَجْرِىَ فِى ٱلْبَحْرِ بِأَمْرِهِۦ ۖ وَسَخَّرَ لَكُمُ ٱلْأَنْهَٰرَ
- (15:28) [listed for 87:2] وَإِذْ قَالَ رَبُّكَ لِلْمَلَٰٓئِكَةِ إِنِّى خَٰلِقٌۢ بَشَرًۭا مِّن صَلْصَٰلٍۢ مِّنْ حَمَإٍۢ مَّسْنُونٍۢ
- (19:10) [listed for 87:2] قَالَ رَبِّ ٱجْعَل لِّىٓ ءَايَةًۭ ۚ قَالَ ءَايَتُكَ أَلَّا تُكَلِّمَ ٱلنَّاسَ ثَلَٰثَ لَيَالٍۢ سَوِيًّۭا
- (19:17) [listed for 87:2] [cited in ¶15] فَٱتَّخَذَتْ مِن دُونِهِمْ حِجَابًۭا فَأَرْسَلْنَآ إِلَيْهَا رُوحَنَا فَتَمَثَّلَ لَهَا بَشَرًۭا سَوِيًّۭا
- (19:43) [listed for 87:2] [cited in ¶19] يَٰٓأَبَتِ إِنِّى قَدْ جَآءَنِى مِنَ ٱلْعِلْمِ مَا لَمْ يَأْتِكَ فَٱتَّبِعْنِىٓ أَهْدِكَ صِرَٰطًۭا سَوِيًّۭا
- (21:33) [listed for 87:2] وَهُوَ ٱلَّذِى خَلَقَ ٱلَّيْلَ وَٱلنَّهَارَ وَٱلشَّمْسَ وَٱلْقَمَرَ ۖ كُلٌّۭ فِى فَلَكٍۢ يَسْبَحُونَ
- (22:5) [listed for 87:2] [cited in ¶15] يَٰٓأَيُّهَا ٱلنَّاسُ إِن كُنتُمْ فِى رَيْبٍۢ مِّنَ ٱلْبَعْثِ فَإِنَّا خَلَقْنَٰكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ مِنْ عَلَقَةٍۢ ثُمَّ مِن مُّضْغَةٍۢ مُّخَلَّقَةٍۢ وَغَيْرِ مُخَلَّقَةٍۢ لِّنُبَيِّنَ لَكُمْ ۚ وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى ثُمَّ نُخْرِجُكُمْ طِفْلًۭا ثُمَّ لِتَبْلُغُوٓا۟ أَشُدَّكُمْ ۖ وَمِنكُم مَّن يُتَوَفَّىٰ وَمِنكُم مَّن يُرَدُّ إِلَىٰٓ أَرْذَلِ ٱلْعُمُرِ لِكَيْلَا يَعْلَمَ مِنۢ بَعْدِ عِلْمٍۢ شَيْـًۭٔا ۚ وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ مِن كُلِّ زَوْجٍۭ بَهِيجٍۢ
- (23:12) [listed for 87:2] وَلَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ مِن سُلَٰلَةٍۢ مِّن طِينٍۢ
- (24:45) [listed for 87:2] وَٱللَّهُ خَلَقَ كُلَّ دَآبَّةٍۢ مِّن مَّآءٍۢ ۖ فَمِنْهُم مَّن يَمْشِى عَلَىٰ بَطْنِهِۦ وَمِنْهُم مَّن يَمْشِى عَلَىٰ رِجْلَيْنِ وَمِنْهُم مَّن يَمْشِى عَلَىٰٓ أَرْبَعٍۢ ۚ يَخْلُقُ ٱللَّهُ مَا يَشَآءُ ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (25:54) [listed for 87:2] وَهُوَ ٱلَّذِى خَلَقَ مِنَ ٱلْمَآءِ بَشَرًۭا فَجَعَلَهُۥ نَسَبًۭا وَصِهْرًۭا ۗ وَكَانَ رَبُّكَ قَدِيرًۭا
- (25:59) [listed for 87:2] ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَمَا بَيْنَهُمَا فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ ۚ ٱلرَّحْمَٰنُ فَسْـَٔلْ بِهِۦ خَبِيرًۭا
- (26:78) [listed for 87:2] [cited in ¶29] ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ
- (29:19) [listed for 87:2] أَوَلَمْ يَرَوْا۟ كَيْفَ يُبْدِئُ ٱللَّهُ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥٓ ۚ إِنَّ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرٌۭ
- (29:44) [listed for 87:2] خَلَقَ ٱللَّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّلْمُؤْمِنِينَ
- (30:27) [listed for 87:2] وَهُوَ ٱلَّذِى يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ وَهُوَ أَهْوَنُ عَلَيْهِ ۚ وَلَهُ ٱلْمَثَلُ ٱلْأَعْلَىٰ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (30:30) [listed for 87:2] فَأَقِمْ وَجْهَكَ لِلدِّينِ حَنِيفًۭا ۚ فِطْرَتَ ٱللَّهِ ٱلَّتِى فَطَرَ ٱلنَّاسَ عَلَيْهَا ۚ لَا تَبْدِيلَ لِخَلْقِ ٱللَّهِ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (32:4) [listed for 87:2] ٱللَّهُ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَمَا بَيْنَهُمَا فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ ۖ مَا لَكُم مِّن دُونِهِۦ مِن وَلِىٍّۢ وَلَا شَفِيعٍ ۚ أَفَلَا تَتَذَكَّرُونَ
- (32:7) [listed for 87:2] ٱلَّذِىٓ أَحْسَنَ كُلَّ شَىْءٍ خَلَقَهُۥ ۖ وَبَدَأَ خَلْقَ ٱلْإِنسَٰنِ مِن طِينٍۢ
- (32:8) [listed for 87:2] ثُمَّ جَعَلَ نَسْلَهُۥ مِن سُلَٰلَةٍۢ مِّن مَّآءٍۢ مَّهِينٍۢ
- (35:11) [listed for 87:2] وَٱللَّهُ خَلَقَكُم مِّن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ جَعَلَكُمْ أَزْوَٰجًۭا ۚ وَمَا تَحْمِلُ مِنْ أُنثَىٰ وَلَا تَضَعُ إِلَّا بِعِلْمِهِۦ ۚ وَمَا يُعَمَّرُ مِن مُّعَمَّرٍۢ وَلَا يُنقَصُ مِنْ عُمُرِهِۦٓ إِلَّا فِى كِتَٰبٍ ۚ إِنَّ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرٌۭ
- (36:36) [listed for 87:2] سُبْحَٰنَ ٱلَّذِى خَلَقَ ٱلْأَزْوَٰجَ كُلَّهَا مِمَّا تُنۢبِتُ ٱلْأَرْضُ وَمِنْ أَنفُسِهِمْ وَمِمَّا لَا يَعْلَمُونَ
- (36:71) [listed for 87:2] أَوَلَمْ يَرَوْا۟ أَنَّا خَلَقْنَا لَهُم مِّمَّا عَمِلَتْ أَيْدِينَآ أَنْعَٰمًۭا فَهُمْ لَهَا مَٰلِكُونَ
- (36:77) [listed for 87:2] أَوَلَمْ يَرَ ٱلْإِنسَٰنُ أَنَّا خَلَقْنَٰهُ مِن نُّطْفَةٍۢ فَإِذَا هُوَ خَصِيمٌۭ مُّبِينٌۭ
- (38:71) [listed for 87:2] إِذْ قَالَ رَبُّكَ لِلْمَلَٰٓئِكَةِ إِنِّى خَٰلِقٌۢ بَشَرًۭا مِّن طِينٍۢ
- (39:6) [listed for 87:2] خَلَقَكُم مِّن نَّفْسٍۢ وَٰحِدَةٍۢ ثُمَّ جَعَلَ مِنْهَا زَوْجَهَا وَأَنزَلَ لَكُم مِّنَ ٱلْأَنْعَٰمِ ثَمَٰنِيَةَ أَزْوَٰجٍۢ ۚ يَخْلُقُكُمْ فِى بُطُونِ أُمَّهَٰتِكُمْ خَلْقًۭا مِّنۢ بَعْدِ خَلْقٍۢ فِى ظُلُمَٰتٍۢ ثَلَٰثٍۢ ۚ ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ لَهُ ٱلْمُلْكُ ۖ لَآ إِلَٰهَ إِلَّا هُوَ ۖ فَأَنَّىٰ تُصْرَفُونَ
- (40:64) [listed for 87:2] ٱللَّهُ ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ قَرَارًۭا وَٱلسَّمَآءَ بِنَآءًۭ وَصَوَّرَكُمْ فَأَحْسَنَ صُوَرَكُمْ وَرَزَقَكُم مِّنَ ٱلطَّيِّبَٰتِ ۚ ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ ۖ فَتَبَارَكَ ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
- (42:11) [listed for 87:2] فَاطِرُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ جَعَلَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَٰجًۭا وَمِنَ ٱلْأَنْعَٰمِ أَزْوَٰجًۭا ۖ يَذْرَؤُكُمْ فِيهِ ۚ لَيْسَ كَمِثْلِهِۦ شَىْءٌۭ ۖ وَهُوَ ٱلسَّمِيعُ ٱلْبَصِيرُ
- (51:49) [listed for 87:2] وَمِن كُلِّ شَىْءٍ خَلَقْنَا زَوْجَيْنِ لَعَلَّكُمْ تَذَكَّرُونَ
- (53:45) [listed for 87:2] وَأَنَّهُۥ خَلَقَ ٱلزَّوْجَيْنِ ٱلذَّكَرَ وَٱلْأُنثَىٰ
- (55:14) [listed for 87:2] خَلَقَ ٱلْإِنسَٰنَ مِن صَلْصَٰلٍۢ كَٱلْفَخَّارِ
- (59:24) [listed for 87:2] هُوَ ٱللَّهُ ٱلْخَٰلِقُ ٱلْبَارِئُ ٱلْمُصَوِّرُ ۖ لَهُ ٱلْأَسْمَآءُ ٱلْحُسْنَىٰ ۚ يُسَبِّحُ لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- (67:2) [listed for 87:2] ٱلَّذِى خَلَقَ ٱلْمَوْتَ وَٱلْحَيَوٰةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًۭا ۚ وَهُوَ ٱلْعَزِيزُ ٱلْغَفُورُ
- (67:3) [listed for 87:2] ٱلَّذِى خَلَقَ سَبْعَ سَمَٰوَٰتٍۢ طِبَاقًۭا ۖ مَّا تَرَىٰ فِى خَلْقِ ٱلرَّحْمَٰنِ مِن تَفَٰوُتٍۢ ۖ فَٱرْجِعِ ٱلْبَصَرَ هَلْ تَرَىٰ مِن فُطُورٍۢ
- (70:19) [listed for 87:2] ۞ إِنَّ ٱلْإِنسَٰنَ خُلِقَ هَلُوعًا
- (71:14) [listed for 87:2] وَقَدْ خَلَقَكُمْ أَطْوَارًا
- (75:4) [listed for 87:2] [cited in ¶14] بَلَىٰ قَٰدِرِينَ عَلَىٰٓ أَن نُّسَوِّىَ بَنَانَهُۥ
- (76:2) [listed for 87:2] إِنَّا خَلَقْنَا ٱلْإِنسَٰنَ مِن نُّطْفَةٍ أَمْشَاجٍۢ نَّبْتَلِيهِ فَجَعَلْنَٰهُ سَمِيعًۢا بَصِيرًا
- (77:20) [listed for 87:2] أَلَمْ نَخْلُقكُّم مِّن مَّآءٍۢ مَّهِينٍۢ
- (78:8) [listed for 87:2] وَخَلَقْنَٰكُمْ أَزْوَٰجًۭا
- (79:28) [listed for 87:2] [cited in ¶2] رَفَعَ سَمْكَهَا فَسَوَّىٰهَا
- (80:18) [listed for 87:2] مِنْ أَىِّ شَىْءٍ خَلَقَهُۥ
- (86:5) [listed for 87:2] فَلْيَنظُرِ ٱلْإِنسَٰنُ مِمَّ خُلِقَ
- (86:6) [listed for 87:2] خُلِقَ مِن مَّآءٍۢ دَافِقٍۢ
- (91:14) [listed for 87:2] [cited in ¶27] فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا
- (96:1) [listed for 87:2] ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ
- (96:2) [listed for 87:2] خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
- (113:2) [listed for 87:2] مِن شَرِّ مَا خَلَقَ

## named by the passage's own list as strong for this ayah (26)

- (13:8) [listed for 87:2] ٱللَّهُ يَعْلَمُ مَا تَحْمِلُ كُلُّ أُنثَىٰ وَمَا تَغِيضُ ٱلْأَرْحَامُ وَمَا تَزْدَادُ ۖ وَكُلُّ شَىْءٍ عِندَهُۥ بِمِقْدَارٍ
- (14:19) [listed for 87:2] أَلَمْ تَرَ أَنَّ ٱللَّهَ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۚ إِن يَشَأْ يُذْهِبْكُمْ وَيَأْتِ بِخَلْقٍۢ جَدِيدٍۢ
- (15:21) [listed for 87:2] وَإِن مِّن شَىْءٍ إِلَّا عِندَنَا خَزَآئِنُهُۥ وَمَا نُنَزِّلُهُۥٓ إِلَّا بِقَدَرٍۢ مَّعْلُومٍۢ
- (15:26) [listed for 87:2] وَلَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ مِن صَلْصَٰلٍۢ مِّنْ حَمَإٍۢ مَّسْنُونٍۢ
- (15:86) [listed for 87:2] إِنَّ رَبَّكَ هُوَ ٱلْخَلَّٰقُ ٱلْعَلِيمُ
- (17:84) [listed for 87:2] قُلْ كُلٌّۭ يَعْمَلُ عَلَىٰ شَاكِلَتِهِۦ فَرَبُّكُمْ أَعْلَمُ بِمَنْ هُوَ أَهْدَىٰ سَبِيلًۭا
- (23:17) [listed for 87:2] وَلَقَدْ خَلَقْنَا فَوْقَكُمْ سَبْعَ طَرَآئِقَ وَمَا كُنَّا عَنِ ٱلْخَلْقِ غَٰفِلِينَ
- (30:8) [listed for 87:2] أَوَلَمْ يَتَفَكَّرُوا۟ فِىٓ أَنفُسِهِم ۗ مَّا خَلَقَ ٱللَّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَمَا بَيْنَهُمَآ إِلَّا بِٱلْحَقِّ وَأَجَلٍۢ مُّسَمًّۭى ۗ وَإِنَّ كَثِيرًۭا مِّنَ ٱلنَّاسِ بِلِقَآئِ رَبِّهِمْ لَكَٰفِرُونَ
- (31:25) [listed for 87:2] وَلَئِن سَأَلْتَهُم مَّنْ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ لَيَقُولُنَّ ٱللَّهُ ۚ قُلِ ٱلْحَمْدُ لِلَّهِ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ
- (35:1) [listed for 87:2] ٱلْحَمْدُ لِلَّهِ فَاطِرِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ جَاعِلِ ٱلْمَلَٰٓئِكَةِ رُسُلًا أُو۟لِىٓ أَجْنِحَةٍۢ مَّثْنَىٰ وَثُلَٰثَ وَرُبَٰعَ ۚ يَزِيدُ فِى ٱلْخَلْقِ مَا يَشَآءُ ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (36:83) [listed for 87:2] فَسُبْحَٰنَ ٱلَّذِى بِيَدِهِۦ مَلَكُوتُ كُلِّ شَىْءٍۢ وَإِلَيْهِ تُرْجَعُونَ
- (37:11) [listed for 87:2] فَٱسْتَفْتِهِمْ أَهُمْ أَشَدُّ خَلْقًا أَم مَّنْ خَلَقْنَآ ۚ إِنَّا خَلَقْنَٰهُم مِّن طِينٍۢ لَّازِبٍۭ
- (43:9) [listed for 87:2] [cited in ¶22] وَلَئِن سَأَلْتَهُم مَّنْ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ لَيَقُولُنَّ خَلَقَهُنَّ ٱلْعَزِيزُ ٱلْعَلِيمُ
- (52:35) [listed for 87:2] أَمْ خُلِقُوا۟ مِنْ غَيْرِ شَىْءٍ أَمْ هُمُ ٱلْخَٰلِقُونَ
- (53:6) [listed for 87:2] ذُو مِرَّةٍۢ فَٱسْتَوَىٰ
- (55:3) [listed for 87:2] خَلَقَ ٱلْإِنسَٰنَ
- (55:7) [listed for 87:2] وَٱلسَّمَآءَ رَفَعَهَا وَوَضَعَ ٱلْمِيزَانَ
- (56:57) [listed for 87:2] نَحْنُ خَلَقْنَٰكُمْ فَلَوْلَا تُصَدِّقُونَ
- (57:22) [listed for 87:2] مَآ أَصَابَ مِن مُّصِيبَةٍۢ فِى ٱلْأَرْضِ وَلَا فِىٓ أَنفُسِكُمْ إِلَّا فِى كِتَٰبٍۢ مِّن قَبْلِ أَن نَّبْرَأَهَآ ۚ إِنَّ ذَٰلِكَ عَلَى ٱللَّهِ يَسِيرٌۭ
- (65:12) [listed for 87:2] ٱللَّهُ ٱلَّذِى خَلَقَ سَبْعَ سَمَٰوَٰتٍۢ وَمِنَ ٱلْأَرْضِ مِثْلَهُنَّ يَتَنَزَّلُ ٱلْأَمْرُ بَيْنَهُنَّ لِتَعْلَمُوٓا۟ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ وَأَنَّ ٱللَّهَ قَدْ أَحَاطَ بِكُلِّ شَىْءٍ عِلْمًۢا
- (70:39) [listed for 87:2] كَلَّآ ۖ إِنَّا خَلَقْنَٰهُم مِّمَّا يَعْلَمُونَ
- (74:11) [listed for 87:2] ذَرْنِى وَمَنْ خَلَقْتُ وَحِيدًۭا
- (75:37) [listed for 87:2] [cited in ¶14] أَلَمْ يَكُ نُطْفَةًۭ مِّن مَّنِىٍّۢ يُمْنَىٰ
- (77:23) [listed for 87:2] فَقَدَرْنَا فَنِعْمَ ٱلْقَٰدِرُونَ
- (82:8) [listed for 87:2] فِىٓ أَىِّ صُورَةٍۢ مَّا شَآءَ رَكَّبَكَ
- (88:17) [listed for 87:2] أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ

## named by the passage's own list as medium for this ayah (42)

- (2:21) [listed for 87:2] يَٰٓأَيُّهَا ٱلنَّاسُ ٱعْبُدُوا۟ رَبَّكُمُ ٱلَّذِى خَلَقَكُمْ وَٱلَّذِينَ مِن قَبْلِكُمْ لَعَلَّكُمْ تَتَّقُونَ
- (2:117) [listed for 87:2] بَدِيعُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ وَإِذَا قَضَىٰٓ أَمْرًۭا فَإِنَّمَا يَقُولُ لَهُۥ كُن فَيَكُونُ
- (3:59) [listed for 87:2] إِنَّ مَثَلَ عِيسَىٰ عِندَ ٱللَّهِ كَمَثَلِ ءَادَمَ ۖ خَلَقَهُۥ مِن تُرَابٍۢ ثُمَّ قَالَ لَهُۥ كُن فَيَكُونُ
- (6:98) [listed for 87:2] وَهُوَ ٱلَّذِىٓ أَنشَأَكُم مِّن نَّفْسٍۢ وَٰحِدَةٍۢ فَمُسْتَقَرٌّۭ وَمُسْتَوْدَعٌۭ ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَفْقَهُونَ
- (6:102) [listed for 87:2] ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ ۖ لَآ إِلَٰهَ إِلَّا هُوَ ۖ خَٰلِقُ كُلِّ شَىْءٍۢ فَٱعْبُدُوهُ ۚ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ وَكِيلٌۭ
- (7:185) [listed for 87:2] أَوَلَمْ يَنظُرُوا۟ فِى مَلَكُوتِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا خَلَقَ ٱللَّهُ مِن شَىْءٍۢ وَأَنْ عَسَىٰٓ أَن يَكُونَ قَدِ ٱقْتَرَبَ أَجَلُهُمْ ۖ فَبِأَىِّ حَدِيثٍۭ بَعْدَهُۥ يُؤْمِنُونَ
- (10:31) [listed for 87:2] قُلْ مَن يَرْزُقُكُم مِّنَ ٱلسَّمَآءِ وَٱلْأَرْضِ أَمَّن يَمْلِكُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَمَن يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ وَيُخْرِجُ ٱلْمَيِّتَ مِنَ ٱلْحَىِّ وَمَن يُدَبِّرُ ٱلْأَمْرَ ۚ فَسَيَقُولُونَ ٱللَّهُ ۚ فَقُلْ أَفَلَا تَتَّقُونَ
- (13:5) [listed for 87:2] ۞ وَإِن تَعْجَبْ فَعَجَبٌۭ قَوْلُهُمْ أَءِذَا كُنَّا تُرَٰبًا أَءِنَّا لَفِى خَلْقٍۢ جَدِيدٍ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ كَفَرُوا۟ بِرَبِّهِمْ ۖ وَأُو۟لَٰٓئِكَ ٱلْأَغْلَٰلُ فِىٓ أَعْنَاقِهِمْ ۖ وَأُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
- (16:17) [listed for 87:2] [cited in ¶30] أَفَمَن يَخْلُقُ كَمَن لَّا يَخْلُقُ ۗ أَفَلَا تَذَكَّرُونَ
- (16:20) [listed for 87:2] [cited in ¶30] وَٱلَّذِينَ يَدْعُونَ مِن دُونِ ٱللَّهِ لَا يَخْلُقُونَ شَيْـًۭٔا وَهُمْ يُخْلَقُونَ
- (17:61) [listed for 87:2] وَإِذْ قُلْنَا لِلْمَلَٰٓئِكَةِ ٱسْجُدُوا۟ لِءَادَمَ فَسَجَدُوٓا۟ إِلَّآ إِبْلِيسَ قَالَ ءَأَسْجُدُ لِمَنْ خَلَقْتَ طِينًۭا
- (19:67) [listed for 87:2] أَوَلَا يَذْكُرُ ٱلْإِنسَٰنُ أَنَّا خَلَقْنَٰهُ مِن قَبْلُ وَلَمْ يَكُ شَيْـًۭٔا
- (21:16) [listed for 87:2] وَمَا خَلَقْنَا ٱلسَّمَآءَ وَٱلْأَرْضَ وَمَا بَيْنَهُمَا لَٰعِبِينَ
- (23:13) [listed for 87:2] ثُمَّ جَعَلْنَٰهُ نُطْفَةًۭ فِى قَرَارٍۢ مَّكِينٍۢ
- (27:64) [listed for 87:2] أَمَّن يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ وَمَن يَرْزُقُكُم مِّنَ ٱلسَّمَآءِ وَٱلْأَرْضِ ۗ أَءِلَٰهٌۭ مَّعَ ٱللَّهِ ۚ قُلْ هَاتُوا۟ بُرْهَٰنَكُمْ إِن كُنتُمْ صَٰدِقِينَ
- (29:20) [listed for 87:2] قُلْ سِيرُوا۟ فِى ٱلْأَرْضِ فَٱنظُرُوا۟ كَيْفَ بَدَأَ ٱلْخَلْقَ ۚ ثُمَّ ٱللَّهُ يُنشِئُ ٱلنَّشْأَةَ ٱلْءَاخِرَةَ ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (31:28) [listed for 87:2] مَّا خَلْقُكُمْ وَلَا بَعْثُكُمْ إِلَّا كَنَفْسٍۢ وَٰحِدَةٍ ۗ إِنَّ ٱللَّهَ سَمِيعٌۢ بَصِيرٌ
- (35:16) [listed for 87:2] إِن يَشَأْ يُذْهِبْكُمْ وَيَأْتِ بِخَلْقٍۢ جَدِيدٍۢ
- (37:96) [listed for 87:2] وَٱللَّهُ خَلَقَكُمْ وَمَا تَعْمَلُونَ
- (39:67) [listed for 87:2] وَمَا قَدَرُوا۟ ٱللَّهَ حَقَّ قَدْرِهِۦ وَٱلْأَرْضُ جَمِيعًۭا قَبْضَتُهُۥ يَوْمَ ٱلْقِيَٰمَةِ وَٱلسَّمَٰوَٰتُ مَطْوِيَّٰتٌۢ بِيَمِينِهِۦ ۚ سُبْحَٰنَهُۥ وَتَعَٰلَىٰ عَمَّا يُشْرِكُونَ
- (40:57) [listed for 87:2] لَخَلْقُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ أَكْبَرُ مِنْ خَلْقِ ٱلنَّاسِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَعْلَمُونَ
- (41:9) [listed for 87:2] ۞ قُلْ أَئِنَّكُمْ لَتَكْفُرُونَ بِٱلَّذِى خَلَقَ ٱلْأَرْضَ فِى يَوْمَيْنِ وَتَجْعَلُونَ لَهُۥٓ أَندَادًۭا ۚ ذَٰلِكَ رَبُّ ٱلْعَٰلَمِينَ
- (42:29) [listed for 87:2] وَمِنْ ءَايَٰتِهِۦ خَلْقُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَثَّ فِيهِمَا مِن دَآبَّةٍۢ ۚ وَهُوَ عَلَىٰ جَمْعِهِمْ إِذَا يَشَآءُ قَدِيرٌۭ
- (43:87) [listed for 87:2] وَلَئِن سَأَلْتَهُم مَّنْ خَلَقَهُمْ لَيَقُولُنَّ ٱللَّهُ ۖ فَأَنَّىٰ يُؤْفَكُونَ
- (44:38) [listed for 87:2] وَمَا خَلَقْنَا ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَمَا بَيْنَهُمَا لَٰعِبِينَ
- (45:4) [listed for 87:2] وَفِى خَلْقِكُمْ وَمَا يَبُثُّ مِن دَآبَّةٍ ءَايَٰتٌۭ لِّقَوْمٍۢ يُوقِنُونَ
- (50:38) [listed for 87:2] وَلَقَدْ خَلَقْنَا ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَمَا بَيْنَهُمَا فِى سِتَّةِ أَيَّامٍۢ وَمَا مَسَّنَا مِن لُّغُوبٍۢ
- (53:47) [listed for 87:2] وَأَنَّ عَلَيْهِ ٱلنَّشْأَةَ ٱلْأُخْرَىٰ
- (56:35) [listed for 87:2] إِنَّآ أَنشَأْنَٰهُنَّ إِنشَآءًۭ
- (56:58) [listed for 87:2] أَفَرَءَيْتُم مَّا تُمْنُونَ
- (56:59) [listed for 87:2] ءَأَنتُمْ تَخْلُقُونَهُۥٓ أَمْ نَحْنُ ٱلْخَٰلِقُونَ
- (56:62) [listed for 87:2] وَلَقَدْ عَلِمْتُمُ ٱلنَّشْأَةَ ٱلْأُولَىٰ فَلَوْلَا تَذَكَّرُونَ
- (68:4) [listed for 87:2] وَإِنَّكَ لَعَلَىٰ خُلُقٍ عَظِيمٍۢ
- (71:15) [listed for 87:2] أَلَمْ تَرَوْا۟ كَيْفَ خَلَقَ ٱللَّهُ سَبْعَ سَمَٰوَٰتٍۢ طِبَاقًۭا
- (75:39) [listed for 87:2] فَجَعَلَ مِنْهُ ٱلزَّوْجَيْنِ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ
- (76:1) [listed for 87:2] هَلْ أَتَىٰ عَلَى ٱلْإِنسَٰنِ حِينٌۭ مِّنَ ٱلدَّهْرِ لَمْ يَكُن شَيْـًۭٔا مَّذْكُورًا
- (77:22) [listed for 87:2] إِلَىٰ قَدَرٍۢ مَّعْلُومٍۢ
- (79:2) [listed for 87:2] وَٱلنَّٰشِطَٰتِ نَشْطًۭا
- (84:19) [listed for 87:2] لَتَرْكَبُنَّ طَبَقًا عَن طَبَقٍۢ
- (85:13) [listed for 87:2] إِنَّهُۥ هُوَ يُبْدِئُ وَيُعِيدُ
- (89:8) [listed for 87:2] ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ
- (92:3) [listed for 87:2] وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ

## weak (this ayah's own list) (34)

- (2:228) [listed for 87:2] وَٱلْمُطَلَّقَٰتُ يَتَرَبَّصْنَ بِأَنفُسِهِنَّ ثَلَٰثَةَ قُرُوٓءٍۢ ۚ وَلَا يَحِلُّ لَهُنَّ أَن يَكْتُمْنَ مَا خَلَقَ ٱللَّهُ فِىٓ أَرْحَامِهِنَّ إِن كُنَّ يُؤْمِنَّ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۚ وَبُعُولَتُهُنَّ أَحَقُّ بِرَدِّهِنَّ فِى ذَٰلِكَ إِنْ أَرَادُوٓا۟ إِصْلَٰحًۭا ۚ وَلَهُنَّ مِثْلُ ٱلَّذِى عَلَيْهِنَّ بِٱلْمَعْرُوفِ ۚ وَلِلرِّجَالِ عَلَيْهِنَّ دَرَجَةٌۭ ۗ وَٱللَّهُ عَزِيزٌ حَكِيمٌ
- (3:190) [listed for 87:2] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلْأَلْبَٰبِ
- (4:1) [listed for 87:2] يَٰٓأَيُّهَا ٱلنَّاسُ ٱتَّقُوا۟ رَبَّكُمُ ٱلَّذِى خَلَقَكُم مِّن نَّفْسٍۢ وَٰحِدَةٍۢ وَخَلَقَ مِنْهَا زَوْجَهَا وَبَثَّ مِنْهُمَا رِجَالًۭا كَثِيرًۭا وَنِسَآءًۭ ۚ وَٱتَّقُوا۟ ٱللَّهَ ٱلَّذِى تَسَآءَلُونَ بِهِۦ وَٱلْأَرْحَامَ ۚ إِنَّ ٱللَّهَ كَانَ عَلَيْكُمْ رَقِيبًۭا
- (4:42) [listed for 87:2] [cited in ¶27] يَوْمَئِذٍۢ يَوَدُّ ٱلَّذِينَ كَفَرُوا۟ وَعَصَوُا۟ ٱلرَّسُولَ لَوْ تُسَوَّىٰ بِهِمُ ٱلْأَرْضُ وَلَا يَكْتُمُونَ ٱللَّهَ حَدِيثًۭا
- (5:17) [listed for 87:2] لَّقَدْ كَفَرَ ٱلَّذِينَ قَالُوٓا۟ إِنَّ ٱللَّهَ هُوَ ٱلْمَسِيحُ ٱبْنُ مَرْيَمَ ۚ قُلْ فَمَن يَمْلِكُ مِنَ ٱللَّهِ شَيْـًٔا إِنْ أَرَادَ أَن يُهْلِكَ ٱلْمَسِيحَ ٱبْنَ مَرْيَمَ وَأُمَّهُۥ وَمَن فِى ٱلْأَرْضِ جَمِيعًۭا ۗ وَلِلَّهِ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا بَيْنَهُمَا ۚ يَخْلُقُ مَا يَشَآءُ ۚ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (6:73) [listed for 87:2] وَهُوَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۖ وَيَوْمَ يَقُولُ كُن فَيَكُونُ ۚ قَوْلُهُ ٱلْحَقُّ ۚ وَلَهُ ٱلْمُلْكُ يَوْمَ يُنفَخُ فِى ٱلصُّورِ ۚ عَٰلِمُ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ ۚ وَهُوَ ٱلْحَكِيمُ ٱلْخَبِيرُ
- (7:191) [listed for 87:2] أَيُشْرِكُونَ مَا لَا يَخْلُقُ شَيْـًۭٔا وَهُمْ يُخْلَقُونَ
- (11:7) [listed for 87:2] وَهُوَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ فِى سِتَّةِ أَيَّامٍۢ وَكَانَ عَرْشُهُۥ عَلَى ٱلْمَآءِ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًۭا ۗ وَلَئِن قُلْتَ إِنَّكُم مَّبْعُوثُونَ مِنۢ بَعْدِ ٱلْمَوْتِ لَيَقُولَنَّ ٱلَّذِينَ كَفَرُوٓا۟ إِنْ هَٰذَآ إِلَّا سِحْرٌۭ مُّبِينٌۭ
- (16:4) [listed for 87:2] خَلَقَ ٱلْإِنسَٰنَ مِن نُّطْفَةٍۢ فَإِذَا هُوَ خَصِيمٌۭ مُّبِينٌۭ
- (16:75) [listed for 87:2] ۞ ضَرَبَ ٱللَّهُ مَثَلًا عَبْدًۭا مَّمْلُوكًۭا لَّا يَقْدِرُ عَلَىٰ شَىْءٍۢ وَمَن رَّزَقْنَٰهُ مِنَّا رِزْقًا حَسَنًۭا فَهُوَ يُنفِقُ مِنْهُ سِرًّۭا وَجَهْرًا ۖ هَلْ يَسْتَوُۥنَ ۚ ٱلْحَمْدُ لِلَّهِ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ
- (17:99) [listed for 87:2] ۞ أَوَلَمْ يَرَوْا۟ أَنَّ ٱللَّهَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ قَادِرٌ عَلَىٰٓ أَن يَخْلُقَ مِثْلَهُمْ وَجَعَلَ لَهُمْ أَجَلًۭا لَّا رَيْبَ فِيهِ فَأَبَى ٱلظَّٰلِمُونَ إِلَّا كُفُورًۭا
- (19:9) [listed for 87:2] قَالَ كَذَٰلِكَ قَالَ رَبُّكَ هُوَ عَلَىَّ هَيِّنٌۭ وَقَدْ خَلَقْتُكَ مِن قَبْلُ وَلَمْ تَكُ شَيْـًۭٔا
- (20:4) [listed for 87:2] تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى
- (23:28) [listed for 87:2] فَإِذَا ٱسْتَوَيْتَ أَنتَ وَمَن مَّعَكَ عَلَى ٱلْفُلْكِ فَقُلِ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى نَجَّىٰنَا مِنَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
- (26:137) [listed for 87:2] إِنْ هَٰذَآ إِلَّا خُلُقُ ٱلْأَوَّلِينَ
- (36:10) [listed for 87:2] وَسَوَآءٌ عَلَيْهِمْ ءَأَنذَرْتَهُمْ أَمْ لَمْ تُنذِرْهُمْ لَا يُؤْمِنُونَ
- (36:79) [listed for 87:2] قُلْ يُحْيِيهَا ٱلَّذِىٓ أَنشَأَهَآ أَوَّلَ مَرَّةٍۢ ۖ وَهُوَ بِكُلِّ خَلْقٍ عَلِيمٌ
- (36:81) [listed for 87:2] أَوَلَيْسَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِقَٰدِرٍ عَلَىٰٓ أَن يَخْلُقَ مِثْلَهُم ۚ بَلَىٰ وَهُوَ ٱلْخَلَّٰقُ ٱلْعَلِيمُ
- (37:55) [listed for 87:2] [cited in ¶20] فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ
- (38:76) [listed for 87:2] قَالَ أَنَا۠ خَيْرٌۭ مِّنْهُ ۖ خَلَقْتَنِى مِن نَّارٍۢ وَخَلَقْتَهُۥ مِن طِينٍۢ
- (39:29) [listed for 87:2] ضَرَبَ ٱللَّهُ مَثَلًۭا رَّجُلًۭا فِيهِ شُرَكَآءُ مُتَشَٰكِسُونَ وَرَجُلًۭا سَلَمًۭا لِّرَجُلٍ هَلْ يَسْتَوِيَانِ مَثَلًا ۚ ٱلْحَمْدُ لِلَّهِ ۚ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ
- (39:62) [listed for 87:2] ٱللَّهُ خَٰلِقُ كُلِّ شَىْءٍۢ ۖ وَهُوَ عَلَىٰ كُلِّ شَىْءٍۢ وَكِيلٌۭ
- (42:49) [listed for 87:2] لِّلَّهِ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ يَخْلُقُ مَا يَشَآءُ ۚ يَهَبُ لِمَن يَشَآءُ إِنَٰثًۭا وَيَهَبُ لِمَن يَشَآءُ ٱلذُّكُورَ
- (43:12) [listed for 87:2] [cited in ¶22] وَٱلَّذِى خَلَقَ ٱلْأَزْوَٰجَ كُلَّهَا وَجَعَلَ لَكُم مِّنَ ٱلْفُلْكِ وَٱلْأَنْعَٰمِ مَا تَرْكَبُونَ
- (43:27) [listed for 87:2] إِلَّا ٱلَّذِى فَطَرَنِى فَإِنَّهُۥ سَيَهْدِينِ
- (44:47) [listed for 87:2] خُذُوهُ فَٱعْتِلُوهُ إِلَىٰ سَوَآءِ ٱلْجَحِيمِ
- (46:33) [listed for 87:2] أَوَلَمْ يَرَوْا۟ أَنَّ ٱللَّهَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَلَمْ يَعْىَ بِخَلْقِهِنَّ بِقَٰدِرٍ عَلَىٰٓ أَن يُحْۦِىَ ٱلْمَوْتَىٰ ۚ بَلَىٰٓ إِنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (49:13) [listed for 87:2] يَٰٓأَيُّهَا ٱلنَّاسُ إِنَّا خَلَقْنَٰكُم مِّن ذَكَرٍۢ وَأُنثَىٰ وَجَعَلْنَٰكُمْ شُعُوبًۭا وَقَبَآئِلَ لِتَعَارَفُوٓا۟ ۚ إِنَّ أَكْرَمَكُمْ عِندَ ٱللَّهِ أَتْقَىٰكُمْ ۚ إِنَّ ٱللَّهَ عَلِيمٌ خَبِيرٌۭ
- (52:36) [listed for 87:2] أَمْ خَلَقُوا۟ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ ۚ بَل لَّا يُوقِنُونَ
- (57:4) [listed for 87:2] هُوَ ٱلَّذِى خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ فِى سِتَّةِ أَيَّامٍۢ ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ ۚ يَعْلَمُ مَا يَلِجُ فِى ٱلْأَرْضِ وَمَا يَخْرُجُ مِنْهَا وَمَا يَنزِلُ مِنَ ٱلسَّمَآءِ وَمَا يَعْرُجُ فِيهَا ۖ وَهُوَ مَعَكُمْ أَيْنَ مَا كُنتُمْ ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌۭ
- (60:1) [listed for 87:2] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَتَّخِذُوا۟ عَدُوِّى وَعَدُوَّكُمْ أَوْلِيَآءَ تُلْقُونَ إِلَيْهِم بِٱلْمَوَدَّةِ وَقَدْ كَفَرُوا۟ بِمَا جَآءَكُم مِّنَ ٱلْحَقِّ يُخْرِجُونَ ٱلرَّسُولَ وَإِيَّاكُمْ ۙ أَن تُؤْمِنُوا۟ بِٱللَّهِ رَبِّكُمْ إِن كُنتُمْ خَرَجْتُمْ جِهَٰدًۭا فِى سَبِيلِى وَٱبْتِغَآءَ مَرْضَاتِى ۚ تُسِرُّونَ إِلَيْهِم بِٱلْمَوَدَّةِ وَأَنَا۠ أَعْلَمُ بِمَآ أَخْفَيْتُمْ وَمَآ أَعْلَنتُمْ ۚ وَمَن يَفْعَلْهُ مِنكُمْ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
- (64:2) [listed for 87:2] هُوَ ٱلَّذِى خَلَقَكُمْ فَمِنكُمْ كَافِرٌۭ وَمِنكُم مُّؤْمِنٌۭ ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ
- (67:23) [listed for 87:2] قُلْ هُوَ ٱلَّذِىٓ أَنشَأَكُمْ وَجَعَلَ لَكُمُ ٱلسَّمْعَ وَٱلْأَبْصَٰرَ وَٱلْأَفْـِٔدَةَ ۖ قَلِيلًۭا مَّا تَشْكُرُونَ
- (90:4) [listed for 87:2] لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِى كَبَدٍ

## named by the passage's own list as weak for this ayah (16)

- (6:101) [listed for 87:2] بَدِيعُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ أَنَّىٰ يَكُونُ لَهُۥ وَلَدٌۭ وَلَمْ تَكُن لَّهُۥ صَٰحِبَةٌۭ ۖ وَخَلَقَ كُلَّ شَىْءٍۢ ۖ وَهُوَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
- (14:20) [listed for 87:2] وَمَا ذَٰلِكَ عَلَى ٱللَّهِ بِعَزِيزٍۢ
- (17:62) [listed for 87:2] قَالَ أَرَءَيْتَكَ هَٰذَا ٱلَّذِى كَرَّمْتَ عَلَىَّ لَئِنْ أَخَّرْتَنِ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ لَأَحْتَنِكَنَّ ذُرِّيَّتَهُۥٓ إِلَّا قَلِيلًۭا
- (18:51) [listed for 87:2] ۞ مَّآ أَشْهَدتُّهُمْ خَلْقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلَا خَلْقَ أَنفُسِهِمْ وَمَا كُنتُ مُتَّخِذَ ٱلْمُضِلِّينَ عَضُدًۭا
- (20:5) [listed for 87:2] ٱلرَّحْمَٰنُ عَلَى ٱلْعَرْشِ ٱسْتَوَىٰ
- (20:55) [listed for 87:2] ۞ مِنْهَا خَلَقْنَٰكُمْ وَفِيهَا نُعِيدُكُمْ وَمِنْهَا نُخْرِجُكُمْ تَارَةً أُخْرَىٰ
- (30:22) [listed for 87:2] وَمِنْ ءَايَٰتِهِۦ خَلْقُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفُ أَلْسِنَتِكُمْ وَأَلْوَٰنِكُمْ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّلْعَٰلِمِينَ
- (31:11) [listed for 87:2] هَٰذَا خَلْقُ ٱللَّهِ فَأَرُونِى مَاذَا خَلَقَ ٱلَّذِينَ مِن دُونِهِۦ ۚ بَلِ ٱلظَّٰلِمُونَ فِى ضَلَٰلٍۢ مُّبِينٍۢ
- (35:17) [listed for 87:2] وَمَا ذَٰلِكَ عَلَى ٱللَّهِ بِعَزِيزٍۢ
- (36:42) [listed for 87:2] وَخَلَقْنَا لَهُم مِّن مِّثْلِهِۦ مَا يَرْكَبُونَ
- (53:37) [listed for 87:2] وَإِبْرَٰهِيمَ ٱلَّذِى وَفَّىٰٓ
- (53:46) [listed for 87:2] مِن نُّطْفَةٍ إِذَا تُمْنَىٰ
- (74:19) [listed for 87:2] فَقُتِلَ كَيْفَ قَدَّرَ
- (78:3) [listed for 87:2] ٱلَّذِى هُمْ فِيهِ مُخْتَلِفُونَ
- (84:12) [listed for 87:2] وَيَصْلَىٰ سَعِيرًا
- (96:4) [listed for 87:2] ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ

## neighbours: within two ayat of a passage the commentary cites (102)

- (1:4) [next to 1:6] مَٰلِكِ يَوْمِ ٱلدِّينِ
- (1:5) [next to 1:6] إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- (1:7) [next to 1:6] صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ
- (2:27) [next to 2:29] ٱلَّذِينَ يَنقُضُونَ عَهْدَ ٱللَّهِ مِنۢ بَعْدِ مِيثَٰقِهِۦ وَيَقْطَعُونَ مَآ أَمَرَ ٱللَّهُ بِهِۦٓ أَن يُوصَلَ وَيُفْسِدُونَ فِى ٱلْأَرْضِ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
- (2:28) [next to 2:29] كَيْفَ تَكْفُرُونَ بِٱللَّهِ وَكُنتُمْ أَمْوَٰتًۭا فَأَحْيَٰكُمْ ۖ ثُمَّ يُمِيتُكُمْ ثُمَّ يُحْيِيكُمْ ثُمَّ إِلَيْهِ تُرْجَعُونَ
- (2:30) [next to 2:29] وَإِذْ قَالَ رَبُّكَ لِلْمَلَٰٓئِكَةِ إِنِّى جَاعِلٌۭ فِى ٱلْأَرْضِ خَلِيفَةًۭ ۖ قَالُوٓا۟ أَتَجْعَلُ فِيهَا مَن يُفْسِدُ فِيهَا وَيَسْفِكُ ٱلدِّمَآءَ وَنَحْنُ نُسَبِّحُ بِحَمْدِكَ وَنُقَدِّسُ لَكَ ۖ قَالَ إِنِّىٓ أَعْلَمُ مَا لَا تَعْلَمُونَ
- (2:31) [next to 2:29] وَعَلَّمَ ءَادَمَ ٱلْأَسْمَآءَ كُلَّهَا ثُمَّ عَرَضَهُمْ عَلَى ٱلْمَلَٰٓئِكَةِ فَقَالَ أَنۢبِـُٔونِى بِأَسْمَآءِ هَٰٓؤُلَآءِ إِن كُنتُمْ صَٰدِقِينَ
- (2:198) [next to 2:200] لَيْسَ عَلَيْكُمْ جُنَاحٌ أَن تَبْتَغُوا۟ فَضْلًۭا مِّن رَّبِّكُمْ ۚ فَإِذَآ أَفَضْتُم مِّنْ عَرَفَٰتٍۢ فَٱذْكُرُوا۟ ٱللَّهَ عِندَ ٱلْمَشْعَرِ ٱلْحَرَامِ ۖ وَٱذْكُرُوهُ كَمَا هَدَىٰكُمْ وَإِن كُنتُم مِّن قَبْلِهِۦ لَمِنَ ٱلضَّآلِّينَ
- (2:199) [next to 2:200] ثُمَّ أَفِيضُوا۟ مِنْ حَيْثُ أَفَاضَ ٱلنَّاسُ وَٱسْتَغْفِرُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ
- (2:201) [next to 2:200] وَمِنْهُم مَّن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ حَسَنَةًۭ وَقِنَا عَذَابَ ٱلنَّارِ
- (2:202) [next to 2:200] أُو۟لَٰٓئِكَ لَهُمْ نَصِيبٌۭ مِّمَّا كَسَبُوا۟ ۚ وَٱللَّهُ سَرِيعُ ٱلْحِسَابِ
- (3:47) [next to 3:49] قَالَتْ رَبِّ أَنَّىٰ يَكُونُ لِى وَلَدٌۭ وَلَمْ يَمْسَسْنِى بَشَرٌۭ ۖ قَالَ كَذَٰلِكِ ٱللَّهُ يَخْلُقُ مَا يَشَآءُ ۚ إِذَا قَضَىٰٓ أَمْرًۭا فَإِنَّمَا يَقُولُ لَهُۥ كُن فَيَكُونُ
- (3:48) [next to 3:49] وَيُعَلِّمُهُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَٱلتَّوْرَىٰةَ وَٱلْإِنجِيلَ
- (3:50) [next to 3:49] وَمُصَدِّقًۭا لِّمَا بَيْنَ يَدَىَّ مِنَ ٱلتَّوْرَىٰةِ وَلِأُحِلَّ لَكُم بَعْضَ ٱلَّذِى حُرِّمَ عَلَيْكُمْ ۚ وَجِئْتُكُم بِـَٔايَةٍۢ مِّن رَّبِّكُمْ فَٱتَّقُوا۟ ٱللَّهَ وَأَطِيعُونِ
- (3:51) [next to 3:49] إِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۗ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- (4:40) [next to 4:42] إِنَّ ٱللَّهَ لَا يَظْلِمُ مِثْقَالَ ذَرَّةٍۢ ۖ وَإِن تَكُ حَسَنَةًۭ يُضَٰعِفْهَا وَيُؤْتِ مِن لَّدُنْهُ أَجْرًا عَظِيمًۭا
- (4:41) [next to 4:42] فَكَيْفَ إِذَا جِئْنَا مِن كُلِّ أُمَّةٍۭ بِشَهِيدٍۢ وَجِئْنَا بِكَ عَلَىٰ هَٰٓؤُلَآءِ شَهِيدًۭا
- (4:43) [next to 4:42] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَقْرَبُوا۟ ٱلصَّلَوٰةَ وَأَنتُمْ سُكَٰرَىٰ حَتَّىٰ تَعْلَمُوا۟ مَا تَقُولُونَ وَلَا جُنُبًا إِلَّا عَابِرِى سَبِيلٍ حَتَّىٰ تَغْتَسِلُوا۟ ۚ وَإِن كُنتُم مَّرْضَىٰٓ أَوْ عَلَىٰ سَفَرٍ أَوْ جَآءَ أَحَدٌۭ مِّنكُم مِّنَ ٱلْغَآئِطِ أَوْ لَٰمَسْتُمُ ٱلنِّسَآءَ فَلَمْ تَجِدُوا۟ مَآءًۭ فَتَيَمَّمُوا۟ صَعِيدًۭا طَيِّبًۭا فَٱمْسَحُوا۟ بِوُجُوهِكُمْ وَأَيْدِيكُمْ ۗ إِنَّ ٱللَّهَ كَانَ عَفُوًّا غَفُورًا
- (4:44) [next to 4:42] أَلَمْ تَرَ إِلَى ٱلَّذِينَ أُوتُوا۟ نَصِيبًۭا مِّنَ ٱلْكِتَٰبِ يَشْتَرُونَ ٱلضَّلَٰلَةَ وَيُرِيدُونَ أَن تَضِلُّوا۟ ٱلسَّبِيلَ
- (15:27) [next to 15:29] وَٱلْجَآنَّ خَلَقْنَٰهُ مِن قَبْلُ مِن نَّارِ ٱلسَّمُومِ
- (15:30) [next to 15:29] فَسَجَدَ ٱلْمَلَٰٓئِكَةُ كُلُّهُمْ أَجْمَعُونَ
- (15:31) [next to 15:29] إِلَّآ إِبْلِيسَ أَبَىٰٓ أَن يَكُونَ مَعَ ٱلسَّٰجِدِينَ
- (16:15) [next to 16:17] وَأَلْقَىٰ فِى ٱلْأَرْضِ رَوَٰسِىَ أَن تَمِيدَ بِكُمْ وَأَنْهَٰرًۭا وَسُبُلًۭا لَّعَلَّكُمْ تَهْتَدُونَ
- (16:16) [next to 16:17] وَعَلَٰمَٰتٍۢ ۚ وَبِٱلنَّجْمِ هُمْ يَهْتَدُونَ
- (16:18) [next to 16:17] وَإِن تَعُدُّوا۟ نِعْمَةَ ٱللَّهِ لَا تُحْصُوهَآ ۗ إِنَّ ٱللَّهَ لَغَفُورٌۭ رَّحِيمٌۭ
- (16:19) [next to 16:17] وَٱللَّهُ يَعْلَمُ مَا تُسِرُّونَ وَمَا تُعْلِنُونَ
- (16:21) [next to 16:20] أَمْوَٰتٌ غَيْرُ أَحْيَآءٍۢ ۖ وَمَا يَشْعُرُونَ أَيَّانَ يُبْعَثُونَ
- (16:22) [next to 16:20] إِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ ۚ فَٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ قُلُوبُهُم مُّنكِرَةٌۭ وَهُم مُّسْتَكْبِرُونَ
- (18:35) [next to 18:37] وَدَخَلَ جَنَّتَهُۥ وَهُوَ ظَالِمٌۭ لِّنَفْسِهِۦ قَالَ مَآ أَظُنُّ أَن تَبِيدَ هَٰذِهِۦٓ أَبَدًۭا
- (18:36) [next to 18:37] وَمَآ أَظُنُّ ٱلسَّاعَةَ قَآئِمَةًۭ وَلَئِن رُّدِدتُّ إِلَىٰ رَبِّى لَأَجِدَنَّ خَيْرًۭا مِّنْهَا مُنقَلَبًۭا
- (18:38) [next to 18:37] لَّٰكِنَّا۠ هُوَ ٱللَّهُ رَبِّى وَلَآ أُشْرِكُ بِرَبِّىٓ أَحَدًۭا
- (18:39) [next to 18:37] وَلَوْلَآ إِذْ دَخَلْتَ جَنَّتَكَ قُلْتَ مَا شَآءَ ٱللَّهُ لَا قُوَّةَ إِلَّا بِٱللَّهِ ۚ إِن تَرَنِ أَنَا۠ أَقَلَّ مِنكَ مَالًۭا وَوَلَدًۭا
- (19:15) [next to 19:17] وَسَلَٰمٌ عَلَيْهِ يَوْمَ وُلِدَ وَيَوْمَ يَمُوتُ وَيَوْمَ يُبْعَثُ حَيًّۭا
- (19:16) [next to 19:17] وَٱذْكُرْ فِى ٱلْكِتَٰبِ مَرْيَمَ إِذِ ٱنتَبَذَتْ مِنْ أَهْلِهَا مَكَانًۭا شَرْقِيًّۭا
- (19:18) [next to 19:17] قَالَتْ إِنِّىٓ أَعُوذُ بِٱلرَّحْمَٰنِ مِنكَ إِن كُنتَ تَقِيًّۭا
- (19:19) [next to 19:17] قَالَ إِنَّمَآ أَنَا۠ رَسُولُ رَبِّكِ لِأَهَبَ لَكِ غُلَٰمًۭا زَكِيًّۭا
- (19:41) [next to 19:43] وَٱذْكُرْ فِى ٱلْكِتَٰبِ إِبْرَٰهِيمَ ۚ إِنَّهُۥ كَانَ صِدِّيقًۭا نَّبِيًّا
- (19:42) [next to 19:43] إِذْ قَالَ لِأَبِيهِ يَٰٓأَبَتِ لِمَ تَعْبُدُ مَا لَا يَسْمَعُ وَلَا يُبْصِرُ وَلَا يُغْنِى عَنكَ شَيْـًۭٔا
- (19:44) [next to 19:43] يَٰٓأَبَتِ لَا تَعْبُدِ ٱلشَّيْطَٰنَ ۖ إِنَّ ٱلشَّيْطَٰنَ كَانَ لِلرَّحْمَٰنِ عَصِيًّۭا
- (19:45) [next to 19:43] يَٰٓأَبَتِ إِنِّىٓ أَخَافُ أَن يَمَسَّكَ عَذَابٌۭ مِّنَ ٱلرَّحْمَٰنِ فَتَكُونَ لِلشَّيْطَٰنِ وَلِيًّۭا
- (20:133) [next to 20:135] وَقَالُوا۟ لَوْلَا يَأْتِينَا بِـَٔايَةٍۢ مِّن رَّبِّهِۦٓ ۚ أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ
- (20:134) [next to 20:135] وَلَوْ أَنَّآ أَهْلَكْنَٰهُم بِعَذَابٍۢ مِّن قَبْلِهِۦ لَقَالُوا۟ رَبَّنَا لَوْلَآ أَرْسَلْتَ إِلَيْنَا رَسُولًۭا فَنَتَّبِعَ ءَايَٰتِكَ مِن قَبْلِ أَن نَّذِلَّ وَنَخْزَىٰ
- (22:3) [next to 22:5] وَمِنَ ٱلنَّاسِ مَن يُجَٰدِلُ فِى ٱللَّهِ بِغَيْرِ عِلْمٍۢ وَيَتَّبِعُ كُلَّ شَيْطَٰنٍۢ مَّرِيدٍۢ
- (22:4) [next to 22:5] كُتِبَ عَلَيْهِ أَنَّهُۥ مَن تَوَلَّاهُ فَأَنَّهُۥ يُضِلُّهُۥ وَيَهْدِيهِ إِلَىٰ عَذَابِ ٱلسَّعِيرِ
- (22:6) [next to 22:5] ذَٰلِكَ بِأَنَّ ٱللَّهَ هُوَ ٱلْحَقُّ وَأَنَّهُۥ يُحْىِ ٱلْمَوْتَىٰ وَأَنَّهُۥ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
- (22:7) [next to 22:5] وَأَنَّ ٱلسَّاعَةَ ءَاتِيَةٌۭ لَّا رَيْبَ فِيهَا وَأَنَّ ٱللَّهَ يَبْعَثُ مَن فِى ٱلْقُبُورِ
- (25:0) [next to 25:2] بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- (25:1) [next to 25:2] تَبَارَكَ ٱلَّذِى نَزَّلَ ٱلْفُرْقَانَ عَلَىٰ عَبْدِهِۦ لِيَكُونَ لِلْعَٰلَمِينَ نَذِيرًا
- (25:3) [next to 25:2] وَٱتَّخَذُوا۟ مِن دُونِهِۦٓ ءَالِهَةًۭ لَّا يَخْلُقُونَ شَيْـًۭٔا وَهُمْ يُخْلَقُونَ وَلَا يَمْلِكُونَ لِأَنفُسِهِمْ ضَرًّۭا وَلَا نَفْعًۭا وَلَا يَمْلِكُونَ مَوْتًۭا وَلَا حَيَوٰةًۭ وَلَا نُشُورًۭا
- (25:4) [next to 25:2] وَقَالَ ٱلَّذِينَ كَفَرُوٓا۟ إِنْ هَٰذَآ إِلَّآ إِفْكٌ ٱفْتَرَىٰهُ وَأَعَانَهُۥ عَلَيْهِ قَوْمٌ ءَاخَرُونَ ۖ فَقَدْ جَآءُو ظُلْمًۭا وَزُورًۭا
- (26:76) [next to 26:78] أَنتُمْ وَءَابَآؤُكُمُ ٱلْأَقْدَمُونَ
- (26:77) [next to 26:78] فَإِنَّهُمْ عَدُوٌّۭ لِّىٓ إِلَّا رَبَّ ٱلْعَٰلَمِينَ
- (26:79) [next to 26:78] وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ
- (26:80) [next to 26:78] وَإِذَا مَرِضْتُ فَهُوَ يَشْفِينِ
- (28:12) [next to 28:14] ۞ وَحَرَّمْنَا عَلَيْهِ ٱلْمَرَاضِعَ مِن قَبْلُ فَقَالَتْ هَلْ أَدُلُّكُمْ عَلَىٰٓ أَهْلِ بَيْتٍۢ يَكْفُلُونَهُۥ لَكُمْ وَهُمْ لَهُۥ نَٰصِحُونَ
- (28:13) [next to 28:14] فَرَدَدْنَٰهُ إِلَىٰٓ أُمِّهِۦ كَىْ تَقَرَّ عَيْنُهَا وَلَا تَحْزَنَ وَلِتَعْلَمَ أَنَّ وَعْدَ ٱللَّهِ حَقٌّۭ وَلَٰكِنَّ أَكْثَرَهُمْ لَا يَعْلَمُونَ
- (28:15) [next to 28:14] وَدَخَلَ ٱلْمَدِينَةَ عَلَىٰ حِينِ غَفْلَةٍۢ مِّنْ أَهْلِهَا فَوَجَدَ فِيهَا رَجُلَيْنِ يَقْتَتِلَانِ هَٰذَا مِن شِيعَتِهِۦ وَهَٰذَا مِنْ عَدُوِّهِۦ ۖ فَٱسْتَغَٰثَهُ ٱلَّذِى مِن شِيعَتِهِۦ عَلَى ٱلَّذِى مِنْ عَدُوِّهِۦ فَوَكَزَهُۥ مُوسَىٰ فَقَضَىٰ عَلَيْهِ ۖ قَالَ هَٰذَا مِنْ عَمَلِ ٱلشَّيْطَٰنِ ۖ إِنَّهُۥ عَدُوٌّۭ مُّضِلٌّۭ مُّبِينٌۭ
- (28:16) [next to 28:14] قَالَ رَبِّ إِنِّى ظَلَمْتُ نَفْسِى فَٱغْفِرْ لِى فَغَفَرَ لَهُۥٓ ۚ إِنَّهُۥ هُوَ ٱلْغَفُورُ ٱلرَّحِيمُ
- (29:15) [next to 29:17] فَأَنجَيْنَٰهُ وَأَصْحَٰبَ ٱلسَّفِينَةِ وَجَعَلْنَٰهَآ ءَايَةًۭ لِّلْعَٰلَمِينَ
- (29:16) [next to 29:17] وَإِبْرَٰهِيمَ إِذْ قَالَ لِقَوْمِهِ ٱعْبُدُوا۟ ٱللَّهَ وَٱتَّقُوهُ ۖ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
- (29:18) [next to 29:17] وَإِن تُكَذِّبُوا۟ فَقَدْ كَذَّبَ أُمَمٌۭ مِّن قَبْلِكُمْ ۖ وَمَا عَلَى ٱلرَّسُولِ إِلَّا ٱلْبَلَٰغُ ٱلْمُبِينُ
- (37:53) [next to 37:55] أَءِذَا مِتْنَا وَكُنَّا تُرَابًۭا وَعِظَٰمًا أَءِنَّا لَمَدِينُونَ
- (37:54) [next to 37:55] قَالَ هَلْ أَنتُم مُّطَّلِعُونَ
- (37:56) [next to 37:55] قَالَ تَٱللَّهِ إِن كِدتَّ لَتُرْدِينِ
- (37:57) [next to 37:55] وَلَوْلَا نِعْمَةُ رَبِّى لَكُنتُ مِنَ ٱلْمُحْضَرِينَ
- (38:5) [next to 38:7] أَجَعَلَ ٱلْءَالِهَةَ إِلَٰهًۭا وَٰحِدًا ۖ إِنَّ هَٰذَا لَشَىْءٌ عُجَابٌۭ
- (38:6) [next to 38:7] وَٱنطَلَقَ ٱلْمَلَأُ مِنْهُمْ أَنِ ٱمْشُوا۟ وَٱصْبِرُوا۟ عَلَىٰٓ ءَالِهَتِكُمْ ۖ إِنَّ هَٰذَا لَشَىْءٌۭ يُرَادُ
- (38:8) [next to 38:7] أَءُنزِلَ عَلَيْهِ ٱلذِّكْرُ مِنۢ بَيْنِنَا ۚ بَلْ هُمْ فِى شَكٍّۢ مِّن ذِكْرِى ۖ بَل لَّمَّا يَذُوقُوا۟ عَذَابِ
- (38:9) [next to 38:7] أَمْ عِندَهُمْ خَزَآئِنُ رَحْمَةِ رَبِّكَ ٱلْعَزِيزِ ٱلْوَهَّابِ
- (43:7) [next to 43:9] وَمَا يَأْتِيهِم مِّن نَّبِىٍّ إِلَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ
- (43:8) [next to 43:9] فَأَهْلَكْنَآ أَشَدَّ مِنْهُم بَطْشًۭا وَمَضَىٰ مَثَلُ ٱلْأَوَّلِينَ
- (43:15) [next to 43:13] وَجَعَلُوا۟ لَهُۥ مِنْ عِبَادِهِۦ جُزْءًا ۚ إِنَّ ٱلْإِنسَٰنَ لَكَفُورٌۭ مُّبِينٌ
- (43:16) [next to 43:14] أَمِ ٱتَّخَذَ مِمَّا يَخْلُقُ بَنَاتٍۢ وَأَصْفَىٰكُم بِٱلْبَنِينَ
- (54:47) [next to 54:49] إِنَّ ٱلْمُجْرِمِينَ فِى ضَلَٰلٍۢ وَسُعُرٍۢ
- (54:48) [next to 54:49] يَوْمَ يُسْحَبُونَ فِى ٱلنَّارِ عَلَىٰ وُجُوهِهِمْ ذُوقُوا۟ مَسَّ سَقَرَ
- (54:50) [next to 54:49] وَمَآ أَمْرُنَآ إِلَّا وَٰحِدَةٌۭ كَلَمْحٍۭ بِٱلْبَصَرِ
- (54:51) [next to 54:49] وَلَقَدْ أَهْلَكْنَآ أَشْيَاعَكُمْ فَهَلْ مِن مُّدَّكِرٍۢ
- (67:20) [next to 67:22] أَمَّنْ هَٰذَا ٱلَّذِى هُوَ جُندٌۭ لَّكُمْ يَنصُرُكُم مِّن دُونِ ٱلرَّحْمَٰنِ ۚ إِنِ ٱلْكَٰفِرُونَ إِلَّا فِى غُرُورٍ
- (67:21) [next to 67:22] أَمَّنْ هَٰذَا ٱلَّذِى يَرْزُقُكُمْ إِنْ أَمْسَكَ رِزْقَهُۥ ۚ بَل لَّجُّوا۟ فِى عُتُوٍّۢ وَنُفُورٍ
- (67:24) [next to 67:22] قُلْ هُوَ ٱلَّذِى ذَرَأَكُمْ فِى ٱلْأَرْضِ وَإِلَيْهِ تُحْشَرُونَ
- (75:2) [next to 75:4] وَلَآ أُقْسِمُ بِٱلنَّفْسِ ٱللَّوَّامَةِ
- (75:3) [next to 75:4] أَيَحْسَبُ ٱلْإِنسَٰنُ أَلَّن نَّجْمَعَ عِظَامَهُۥ
- (75:5) [next to 75:4] بَلْ يُرِيدُ ٱلْإِنسَٰنُ لِيَفْجُرَ أَمَامَهُۥ
- (75:6) [next to 75:4] يَسْـَٔلُ أَيَّانَ يَوْمُ ٱلْقِيَٰمَةِ
- (75:34) [next to 75:36] أَوْلَىٰ لَكَ فَأَوْلَىٰ
- (75:35) [next to 75:36] ثُمَّ أَوْلَىٰ لَكَ فَأَوْلَىٰٓ
- (79:26) [next to 79:28] إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّمَن يَخْشَىٰٓ
- (79:27) [next to 79:28] ءَأَنتُمْ أَشَدُّ خَلْقًا أَمِ ٱلسَّمَآءُ ۚ بَنَىٰهَا
- (79:29) [next to 79:28] وَأَغْطَشَ لَيْلَهَا وَأَخْرَجَ ضُحَىٰهَا
- (79:30) [next to 79:28] وَٱلْأَرْضَ بَعْدَ ذَٰلِكَ دَحَىٰهَآ
- (79:32) [next to 79:31] وَٱلْجِبَالَ أَرْسَىٰهَا
- (79:33) [next to 79:31] مَتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ
- (82:5) [next to 82:7] عَلِمَتْ نَفْسٌۭ مَّا قَدَّمَتْ وَأَخَّرَتْ
- (82:6) [next to 82:7] يَٰٓأَيُّهَا ٱلْإِنسَٰنُ مَا غَرَّكَ بِرَبِّكَ ٱلْكَرِيمِ
- (82:9) [next to 82:7] كَلَّا بَلْ تُكَذِّبُونَ بِٱلدِّينِ
- (91:5) [next to 91:7] وَٱلسَّمَآءِ وَمَا بَنَىٰهَا
- (91:6) [next to 91:7] وَٱلْأَرْضِ وَمَا طَحَىٰهَا
- (91:9) [next to 91:7] قَدْ أَفْلَحَ مَن زَكَّىٰهَا
- (91:10) [next to 91:8] وَقَدْ خَابَ مَن دَسَّىٰهَا
- (91:12) [next to 91:14] إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا
- (91:13) [next to 91:14] فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا
- (91:15) [next to 91:14] وَلَا يَخَافُ عُقْبَٰهَا

