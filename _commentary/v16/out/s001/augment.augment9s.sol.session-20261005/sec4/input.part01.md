Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 4 of 14 ("Rahim ve terbiye: çocuğun evi ve onu kemale erdiren"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

Discovery rationales and accuracy flags are unverified. Judge each against canonical Arabic, including speaker, negation and ayah boundaries.

===== _commentary/v16/prompts/augment9s/augment.md =====
You are completing a finished Turkish commentary on the images of a surah,
written by another reader, with what the Quran itself says about it: the Quran
explaining the Quran. Below are one image section of that commentary, with its
prose paragraphs numbered [¶n] as in the whole commentary; the commentary's
ledger; and Quran passages from an image-based discovery list (two readers'
judgements of which ayat this image activates), each with its Arabic, its tier,
the bases given for it, and the paragraphs of the section that already cite it,
if any. A tier is that list's own judgement, not yours; the list is not
authoritative and may be incomplete.

Read the section first. Then judge every listed passage, one by one, against
every paragraph of the section: is it relevant to what that paragraph says? A passage is
relevant to a paragraph when it explains, completes, extends or contrasts
something the paragraph says, or names what the ayat the paragraph reads leave
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

Then go through the section paragraph by paragraph and ask your own
knowledge of the Quran, exhaustively, which ayat, in neither the list nor that
paragraph, are relevant to it in the same sense, and treat them the same way.
For each paragraph weigh at least: the other places of the key words and
constructions of the ayat it quotes; the other places where the image's scene,
object or act is staged, with or without a shared word; ayat that state the same thing in other
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
passage from your own knowledge that you weighed, marked "own". Paragraph
numbers are the ones shown: only this section's paragraphs may be served.
- <surah:ayah>: prose ¶n[, ref ¶m …] - <the mechanism in a few words>
- <surah:ayah>: ref ¶n[, ¶m …] - <the link in a few words>
- <surah:ayah>: context ¶n (in <surah:ayah>) - <quoted or named inside that prose addition>
- <surah:ayah>: conflict ¶n - <what it shows against the paragraph>
- <surah:ayah>: cited ¶n; ref ¶m | prose ¶m | nowhere else - <why, for a passage the commentary already cites>
- <surah:ayah>: not relevant - <reason in a few words>
- <surah:ayah> own: prose ¶n | ref ¶n | context ¶n (in <surah:ayah>) | conflict ¶n | not relevant - <…>

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 4 (prose paragraphs numbered) =====
[¶23] Birinci ayetteki iki sıfat {ar:ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:er-rahmâni'r-rahîm, gloss:merhameti bol olan, merhamet eden, source:1:1}, ana karnındaki rahimle aynı köktendir. Rahim, içinde çocuğun büyüdüğü bir evdir: {ar:الرحم بيت منبت الولد ووعاؤه في البطن, tr:er-rahimu beytü menbiti'l-veledi ve vi'âühû fi'l-batn, gloss:rahim, karındaki çocuğun bittiği yer olan ev ve onun kabıdır, source:"ر ح م,B003"}. Bu evin bedeli de vardır: {ar:الرحوم الناقة التي تشتكي رحمها بعد النتاج, tr:er-rahûmu'n-nâkatü'lletî teştekî rahimehâ ba'de'n-nitâc, gloss:rahûm, doğurduktan sonra rahminden acı çeken dişi devedir, source:"ر ح م,B004"}. Merhamet, bu yakınlıktan doğan bir incelik olarak tanımlanır, ama orada kalmaz, bir iyiliğe dönüşür: {ar:الرحمة رقة تقتضي الإحسان إلى المرحوم, tr:er-rahmetü rikkatün tektedi'l-ihsâne ile'l-merhûm, gloss:rahmet, merhamet edilene iyilik etmeyi gerektiren bir inceliktir, source:"ر ح م,B001"}. Bu iyilik özellikle zayıfa yönelir: {ar:ورحمة الضعيف والتعطف عليه, tr:ve rahmetü'd-da'îfi ve't-teattufu aleyh, gloss:zayıfa merhamet etmek ve ona şefkatle eğilmek, source:"ر ح م,B001"}. Akrabalık da aynı kelimeyle anılır, çünkü akrabalar tek bir rahimden çıkmıştır: {ar:استعير الرحم للقرابة لكونهم خارجين من رحم واحدة, tr:üstüîre'r-rahimu li'l-karâbe, gloss:rahim kelimesi akrabalık için ödünç alındı, çünkü akrabalar tek bir rahimden çıkmıştır, source:"ر ح م,B002"}.

[¶24] İkinci ayetteki "Rab" kelimesi rahimden sonraki aşamayı, yani büyütmeyi taşır: {ar:رب فلان ولده؛ رباه, tr:rabbe fülânün veledeh, gloss:falanca çocuğunu büyüttü, source:"ر ب ب,B002"}. Büyütmenin nasıl işlediği de tarif edilir: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiyetü, ve hüve inşâü'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi halden hale geçirerek tamamlanma sınırına kadar yetiştirmektir, source:"ر ب ب,B002"}. Çocuğu doğuranın dışında birinin büyütmesi de aynı köktendir: {ar:الراب والرابة بأحد الزوجين إذا تولى تربية الولد, tr:er-râbbü ve'r-râbbe, gloss:râb ve râbbe, eşlerden birinin çocuğunun terbiyesini üstlenen üvey ebeveyndir, source:"ر ب ب,B005"}, {ar:الربيبة: الحاضنة, tr:er-rabîbetü'l-hâdına, gloss:rabîbe, çocuğa bakan dadıdır, source:"ر ب ب,B005"}. Yeni doğurmuş koyun da bu köktendir: {ar:الشاة الربي التي تحتبس في البيت للبن, tr:eş-şâtü'r-rubbâ, gloss:rubbâ, sütü için evde alıkonan koyundur, source:"ر ب ب,B009"}. Büyütme öğretmeye de uzanır: {ar:العالم المعلم الذي يغذو الناس بصغار العلوم, tr:el-âlimü'l-muallimü'llezî yağzu'n-nâse bi-sığâri'l-ulûm, gloss:insanları önce bilginin küçük parçalarıyla besleyen öğretici âlim, source:"ر ب ب,B003"}. Bu cümle "Rab" ile ikinci ayetteki "âlemîn" kelimesinin kökünü yan yana getirir.

[¶25] Sure bu görüntüyü bir çerçeve içinde kurar. Birinci ayet rahimle açılır. İkinci ayet büyüten Rabbi anar. Üçüncü ayet, "âlemlerin Rabbi" sözünün hemen ardından iki sıfatı tekrar eder: {ar:ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:er-rahmâni'r-rahîm, gloss:merhameti bol olan, merhamet eden, source:1:3}. Böylece büyütme iki yandan rahimle sarılır. Düz bir meal "Rahman, Rahim" deyip geçer. Görüntü ise bu merhametin bir yer ve bir süre içinde işlediğini gösterir: Önce bir ev, sonra halden hale bir büyütme ve sonunda tamamlanma vardır. Altıncı ayet bu evin işlerini ayakta tutanı da hatırlatır: {ar:قوام أهل بيته وقيام أهل بيته؛ الذي يقيم شأنهم, tr:kıvâmü ehli beytihî, gloss:ev halkının işlerini ayakta tutan, source:"ق و م,B004"}. Yedinci ayetteki "en'amte" kelimesinin ailesinde rahat içinde büyütülen çocuklar vardır: {ar:نعم فلان أولاده ترفهم, tr:na''ame fülânün evlâdehû, gloss:falanca çocuklarını bolluk içinde büyüttü, source:"ن ع م,B002"}. Aynı ayetteki "gayr" kelimesinin ailesinde eve getirilen erzak ({ar:الغِيرة بالكسر: الميرة, tr:el-gıyretü bi'l-kesr: el-mîre, gloss:esreli gıyre erzaktır, source:"غ ي ر,B001"}) ve evi kıskançlıkla korumak ({ar:الغَيرة بالفتح مصدر قولك غار الرجل على أهله, tr:el-gayretü bi'l-feth, gloss:üstünlü gayre, adamın ailesini kıskanıp korumasıdır, source:"غ ي ر,B004"}) vardır. Bu iki kelime ayetteki "değil" anlamının yanında, bir evin beslenmesini ve korunmasını duyurur.

[¶26] Kur'an bu evi açıkça sahneler. Rahim, Allah'ın şekil verdiği yerdir: {ar:هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ, tr:hüvellezî yusavvirukum fi'l-erhâmi keyfe yeşâ', gloss:sizi rahimlerde dilediği gibi biçimlendiren O'dur, source:3:6}. Akrabalık bağı da Allah'ın adıyla birlikte anılır: {ar:وَٱتَّقُوا۟ ٱللَّهَ ٱلَّذِى تَسَآءَلُونَ بِهِۦ وَٱلْأَرْحَامَ, tr:vettekullâhellezî tesâelûne bihî ve'l-erhâm, gloss:adını anarak birbirinizden dilekte bulunduğunuz Allah'tan ve akrabalık bağlarından sakının, source:4:1}. Üvey çocuk da "rabîbe" kelimesiyle anılır: {ar:وَرَبَٰٓئِبُكُمُ ٱلَّٰتِى فِى حُجُورِكُم, tr:ve rabâibükümü'llâtî fî hucûriküm, gloss:kucağınızda büyüyen üvey kızlarınız, source:4:23}. Bu ailenin en yoğun sahnesi, Rabbin ana babayla ilgili hükmüdür: {ar:وَقَضَىٰ رَبُّكَ أَلَّا تَعْبُدُوٓا۟ إِلَّآ إِيَّاهُ وَبِٱلْوَٰلِدَيْنِ إِحْسَٰنًا, tr:ve kadâ rabbüke ellâ ta'büdû illâ iyyâhü ve bi'l-vâlideyni ihsânâ, gloss:Rabbin, yalnız O'na kulluk etmenizi ve ana babaya iyilik etmenizi hükmetti, source:17:23}. Ardından şu gelir: {ar:وَٱخْفِضْ لَهُمَا جَنَاحَ ٱلذُّلِّ مِنَ ٱلرَّحْمَةِ وَقُل رَّبِّ ٱرْحَمْهُمَا كَمَا رَبَّيَانِى صَغِيرًۭا, tr:vahfid lehümâ cenâha'z-zülli mine'r-rahmeti ve kul rabbi'rhamhümâ kemâ rabbeyânî sağîrâ, gloss:merhametten onlara alçakgönüllülük kanadını indir ve "Rabbim, onlar beni küçükken nasıl büyüttülerse sen de onlara öyle merhamet et" de, source:17:24}. Bu iki ayette "iyyâ" kelimesi, kulluk, alçalma, rahmet ve "rabbeyânî" kelimesindeki büyütme birlikte bulunur. Fâtiha'nın birinci, ikinci ve beşinci ayetlerinin kelimeleri burada bir ailenin içinde konuşur.

[¶27] Musa'nın çocukluğu da bu görüntüyü sahneler. Allah Musa'nın annesine vahyeder: {ar:أَنْ أَرْضِعِيهِ ۖ فَإِذَا خِفْتِ عَلَيْهِ فَأَلْقِيهِ فِى ٱلْيَمِّ, tr:en erdı'îh, fe-izâ hıfti aleyhi fe-elkîhi fi'l-yemm, gloss:onu emzir; onun için korkarsan onu suya bırak, source:28:7}. Çocuk rahimden ayrılır ve anne boşlukla kalır: {ar:وَأَصْبَحَ فُؤَادُ أُمِّ مُوسَىٰ فَٰرِغًا, tr:ve asbaha fuâdü ümmi Mûsâ fârigâ, gloss:Musa'nın annesinin yüreği bomboş kaldı, source:28:10}. Kız kardeşi bir ev önerir: {ar:هَلْ أَدُلُّكُمْ عَلَىٰٓ أَهْلِ بَيْتٍۢ يَكْفُلُونَهُۥ لَكُمْ, tr:hel edüllüküm alâ ehli beytin yekfulûnehû leküm, gloss:size onu sizin için büyütecek bir ev halkı göstereyim mi, source:28:12}. Sonunda çocuk annesine geri verilir: {ar:فَرَدَدْنَٰهُ إِلَىٰٓ أُمِّهِۦ كَىْ تَقَرَّ عَيْنُهَا, tr:fe-radednâhü ilâ ümmihî key tekarra aynühâ, gloss:gözü aydın olsun diye onu annesine geri verdik, source:28:13}. Allah aynı olayı Musa'ya anlatırken büyütmenin asıl gözetenini söyler: {ar:وَلِتُصْنَعَ عَلَىٰ عَيْنِىٓ, tr:ve li-tusna'a alâ aynî, gloss:gözümün önünde yetiştirilesin diye, source:20:39}. Firavun'un {ar:أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا, tr:e-lem nurabbike fînâ velîdâ, gloss:seni küçükken aramızda biz büyütmedik mi, source:26:18} sözü bu yüzden yarım bir iddiadır. Çocuğun asıl büyütülmesi annesinin göğsünde ve Rabbin gözü önünde olmuştur. Büyütme öğretmeye uzandığında Kur'an şunu söyler: {ar:وَلَٰكِن كُونُوا۟ رَبَّٰنِيِّۦنَ بِمَا كُنتُمْ تُعَلِّمُونَ ٱلْكِتَٰبَ, tr:ve lâkin kûnû rabbâniyyîne bimâ küntüm tu'allimûne'l-kitâb, gloss:kitabı öğretmenizden dolayı rabbâniler olun, source:3:79}. Rahman da bir öğretici olarak anılır: {ar:ٱلرَّحْمَٰنُ, tr:er-rahmân, gloss:Rahman, source:55:1}, {ar:عَلَّمَ ٱلْقُرْءَانَ, tr:allemel-kur'ân, gloss:Kur'an'ı öğretti, source:55:2}, {ar:خَلَقَ ٱلْإِنسَٰنَ, tr:halaka'l-insân, gloss:insanı yarattı, source:55:3}, {ar:عَلَّمَهُ ٱلْبَيَانَ, tr:allemehü'l-beyân, gloss:ona açıklamayı öğretti, source:55:4}.

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/ledger.md =====
- not developed: و ل ه members of ٱللَّهِ (road, womb, herd, well, passing) - alternative derivation, root identity not established
- not developed: hadith items in womb, herd and leaning chains - outside the Quran
- not developed: ن ع م B012 walking on soles - too remote
- not developed: ع و ن B005 strength matching age - adds nothing
- not developed: ق و م B012 ayn reading of qāma - recorded as wrong
- not developed: Debt and scale chain - merged into Day of reckoning
- not developed: Well-head chain - merged into Rain as water
- memory: dīn (kasra) vs dayn (fatha) are distinct words of one root
- memory: maghḍūb is a passive participle naming no agent; anʿamta names "you" as agent
- memory: fronted iyyāka marks exclusivity ("only you")
- memory: qāma also means "stopped dead" (beast), as well as "stood up"

===== passages from the discovery list (218) =====
## strong (137)

- (2:31) [luna: strong; basis: theme] وَعَلَّمَ ءَادَمَ ٱلْأَسْمَآءَ كُلَّهَا ثُمَّ عَرَضَهُمْ عَلَى ٱلْمَلَٰٓئِكَةِ فَقَالَ أَنۢبِـُٔونِى بِأَسْمَآءِ هَٰٓؤُلَآءِ إِن كُنتُمْ صَٰدِقِينَ
  Unverified discovery rationale: luna: The section's dictionary gloss calls the learned teacher one who feeds people small sciences; this ayah shows Allah teaching Adam the names, a foundational act of instruction.
- (2:83) [luna: strong (missing-ayat turn); basis: scene+theme] وَإِذْ أَخَذْنَا مِيثَٰقَ بَنِىٓ إِسْرَٰٓءِيلَ لَا تَعْبُدُونَ إِلَّا ٱللَّهَ وَبِٱلْوَٰلِدَيْنِ إِحْسَانًۭا وَذِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَقُولُوا۟ لِلنَّاسِ حُسْنًۭا وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ ثُمَّ تَوَلَّيْتُمْ إِلَّا قَلِيلًۭا مِّنكُمْ وَأَنتُم مُّعْرِضُونَ
  Unverified discovery rationale: luna: The section says mercy becomes good treatment, especially for the weak and kin; this ayah joins goodness to parents and relatives with care for orphans and the needy.
- (2:129) [luna: strong; basis: theme] رَبَّنَا وَٱبْعَثْ فِيهِمْ رَسُولًۭا مِّنْهُمْ يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِكَ وَيُعَلِّمُهُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَيُزَكِّيهِمْ ۚ إِنَّكَ أَنتَ ٱلْعَزِيزُ ٱلْحَكِيمُ
  Unverified discovery rationale: luna: The section extends upbringing into teaching; Abraham asks for a messenger who will recite signs and teach the Book and wisdom to his descendants.
- (2:177) [luna: strong (missing-ayat turn); terra: medium; basis: scene+theme] ۞ لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَلَٰكِنَّ ٱلْبِرَّ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَٱلْمَلَٰٓئِكَةِ وَٱلْكِتَٰبِ وَٱلنَّبِيِّۦنَ وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ وَٱبْنَ ٱلسَّبِيلِ وَٱلسَّآئِلِينَ وَفِى ٱلرِّقَابِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَٱلْمُوفُونَ بِعَهْدِهِمْ إِذَا عَٰهَدُوا۟ ۖ وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ وَحِينَ ٱلْبَأْسِ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
  Unverified discovery rationale: luna: The section connects kinship to practical care; this ayah includes spending on relatives, orphans, the needy, and the traveler among acts of righteousness. | terra: Righteousness gives cherished wealth to relatives, orphans, and the needy, specifying mercy as costly beneficence rather than feeling alone.
- (2:215) [luna: strong; terra: medium; basis: scene+theme] يَسْـَٔلُونَكَ مَاذَا يُنفِقُونَ ۖ قُلْ مَآ أَنفَقْتُم مِّنْ خَيْرٍۢ فَلِلْوَٰلِدَيْنِ وَٱلْأَقْرَبِينَ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَٱبْنِ ٱلسَّبِيلِ ۗ وَمَا تَفْعَلُوا۟ مِنْ خَيْرٍۢ فَإِنَّ ٱللَّهَ بِهِۦ عَلِيمٌۭ
  Unverified discovery rationale: luna: The section makes care for family and the vulnerable an expression of goodness; this ayah names parents, near relatives, orphans, and the needy as recipients of spending. | terra: When asked what to spend, the ayah names parents, near kin, orphans, and the needy; provision follows the family-and-weakness network of the section.
- (2:220) [luna: strong (missing-ayat turn); terra: strong; basis: scene+theme] فِى ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۗ وَيَسْـَٔلُونَكَ عَنِ ٱلْيَتَٰمَىٰ ۖ قُلْ إِصْلَاحٌۭ لَّهُمْ خَيْرٌۭ ۖ وَإِن تُخَالِطُوهُمْ فَإِخْوَٰنُكُمْ ۚ وَٱللَّهُ يَعْلَمُ ٱلْمُفْسِدَ مِنَ ٱلْمُصْلِحِ ۚ وَلَوْ شَآءَ ٱللَّهُ لَأَعْنَتَكُمْ ۚ إِنَّ ٱللَّهَ عَزِيزٌ حَكِيمٌۭ
  Unverified discovery rationale: luna: The section includes a child raised by someone other than a birth parent; this ayah says improving orphans' affairs is best and describes them as brothers when their lives are joined. | terra: “Improvement for them is best” makes orphan care an active good, and calling them brothers prevents guardianship from becoming exploitation.
- (2:233) [luna: strong; terra: strong; basis: scene+theme] ۞ وَٱلْوَٰلِدَٰتُ يُرْضِعْنَ أَوْلَٰدَهُنَّ حَوْلَيْنِ كَامِلَيْنِ ۖ لِمَنْ أَرَادَ أَن يُتِمَّ ٱلرَّضَاعَةَ ۚ وَعَلَى ٱلْمَوْلُودِ لَهُۥ رِزْقُهُنَّ وَكِسْوَتُهُنَّ بِٱلْمَعْرُوفِ ۚ لَا تُكَلَّفُ نَفْسٌ إِلَّا وُسْعَهَا ۚ لَا تُضَآرَّ وَٰلِدَةٌۢ بِوَلَدِهَا وَلَا مَوْلُودٌۭ لَّهُۥ بِوَلَدِهِۦ ۚ وَعَلَى ٱلْوَارِثِ مِثْلُ ذَٰلِكَ ۗ فَإِنْ أَرَادَا فِصَالًا عَن تَرَاضٍۢ مِّنْهُمَا وَتَشَاوُرٍۢ فَلَا جُنَاحَ عَلَيْهِمَا ۗ وَإِنْ أَرَدتُّمْ أَن تَسْتَرْضِعُوٓا۟ أَوْلَٰدَكُمْ فَلَا جُنَاحَ عَلَيْكُمْ إِذَا سَلَّمْتُم مَّآ ءَاتَيْتُم بِٱلْمَعْرُوفِ ۗ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ بِمَا تَعْمَلُونَ بَصِيرٌۭ
  Unverified discovery rationale: luna: The section moves from the womb into nurture at home; this ayah sets nursing and weaning, forbids harming either parent through the child, and assigns the child's father provision and clothing for the nursing mother. | terra: Mothers nurse for two complete years, while the father supplies food and clothing; it gives the section's house, duration, nourishment, and completion concrete legal form.
- (3:6) [luna: strong; terra: strong; basis: root+scene] [cited in ¶26] هُوَ ٱلَّذِى يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ كَيْفَ يَشَآءُ ۚ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
  Unverified discovery rationale: luna: The section makes the womb a house where the child is formed; this ayah says Allah shapes people in the wombs (ٱلْأَرْحَامِ), making that hidden home an act of divine formation. | terra: God fashions people “فِي الْأَرْحَامِ” as He wills, making the womb the place of divine formation described by the section.
- (3:35) [luna: strong; terra: strong; basis: root+scene] إِذْ قَالَتِ ٱمْرَأَتُ عِمْرَٰنَ رَبِّ إِنِّى نَذَرْتُ لَكَ مَا فِى بَطْنِى مُحَرَّرًۭا فَتَقَبَّلْ مِنِّىٓ ۖ إِنَّكَ أَنتَ ٱلسَّمِيعُ ٱلْعَلِيمُ
  Unverified discovery rationale: luna: The section treats the womb as a child's home; Mary's mother dedicates what is in her womb, making the unborn child the center of a household vow. | terra: The wife of ʿImran dedicates what is in her womb before birth, treating the unborn child as already held in a divine and familial trust.
- (3:36) [luna: strong; terra: strong; basis: scene+theme] فَلَمَّا وَضَعَتْهَا قَالَتْ رَبِّ إِنِّى وَضَعْتُهَآ أُنثَىٰ وَٱللَّهُ أَعْلَمُ بِمَا وَضَعَتْ وَلَيْسَ ٱلذَّكَرُ كَٱلْأُنثَىٰ ۖ وَإِنِّى سَمَّيْتُهَا مَرْيَمَ وَإِنِّىٓ أُعِيذُهَا بِكَ وَذُرِّيَّتَهَا مِنَ ٱلشَّيْطَٰنِ ٱلرَّجِيمِ
  Unverified discovery rationale: luna: The section moves from womb to the child's later life; this ayah records Mary's birth and her mother's naming her, carrying the image from gestation into family care. | terra: At Mary's birth her mother names her and seeks protection for her and her descendants, extending maternal care into prayerful safeguarding.
- (3:37) [luna: strong; terra: strong; basis: root+scene+theme] فَتَقَبَّلَهَا رَبُّهَا بِقَبُولٍ حَسَنٍۢ وَأَنۢبَتَهَا نَبَاتًا حَسَنًۭا وَكَفَّلَهَا زَكَرِيَّا ۖ كُلَّمَا دَخَلَ عَلَيْهَا زَكَرِيَّا ٱلْمِحْرَابَ وَجَدَ عِندَهَا رِزْقًۭا ۖ قَالَ يَٰمَرْيَمُ أَنَّىٰ لَكِ هَٰذَا ۖ قَالَتْ هُوَ مِنْ عِندِ ٱللَّهِ ۖ إِنَّ ٱللَّهَ يَرْزُقُ مَن يَشَآءُ بِغَيْرِ حِسَابٍ
  Unverified discovery rationale: luna: The section says a child can be raised by someone other than the one who gave birth; this ayah says Zakariyya took charge of Mary (كَفَّلَهَا زَكَرِيَّا) and that she grew under his care. | terra: Mary is accepted, made to grow a good growth, and placed in Zakariyya's care; this is Qur'anic tarbiya as gradual growth under a guardian.
- (3:79) [luna: strong; terra: strong; basis: root+theme] [cited in ¶27] مَا كَانَ لِبَشَرٍ أَن يُؤْتِيَهُ ٱللَّهُ ٱلْكِتَٰبَ وَٱلْحُكْمَ وَٱلنُّبُوَّةَ ثُمَّ يَقُولَ لِلنَّاسِ كُونُوا۟ عِبَادًۭا لِّى مِن دُونِ ٱللَّهِ وَلَٰكِن كُونُوا۟ رَبَّٰنِيِّۦنَ بِمَا كُنتُمْ تُعَلِّمُونَ ٱلْكِتَٰبَ وَبِمَا كُنتُمْ تَدْرُسُونَ
