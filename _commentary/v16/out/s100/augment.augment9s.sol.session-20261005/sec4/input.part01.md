Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 100; below is its section 4 of 11 ("Toprağı altüst etmek"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md section 4 (prose paragraphs numbered) =====
[¶18] Dördüncü ayetin fiili tozu havaya kaldırmanın yanında toprağı ayakla eşelemeyi de anlatır: {ar:أثار الثور التراب إذا بحثه بقوائمه, tr:esâra's-sevru't-turâbe izâ behasehû bi-kavâimih, gloss:boğa toprağı ayaklarıyla eşeleyince "toprağı kaldırdı" denir, source:"ث و ر,B002"}. Aynı fiil toprağı sürmeyi de karşılar: {ar:أثرت الأرض إثارة, tr:esartu'l-arda isâraten, gloss:toprağı alt üst ettim, sürdüm, source:"ث و ر,B002"}. Kökün hayvanı da tarlayı süren öküzdür: {ar:والثور البقر الذي يثار به الأرض, tr:ve's-sevru'l-bakaru'llezî yusâru bihi'l-ard, gloss:"sevr", toprağın onunla sürüldüğü sığırdır, source:"ث و ر,B004"}. Kökün özü saklı duran bir şeyin fışkırmasıdır: {ar:أصل انبعاث الشيء, tr:aslu'nbi'âsi'ş-şey', gloss:bir şeyin harekete geçip fırlamasının aslı, source:"ث و ر,B001"}. Bu fışkırmanın örnekleri arasında çekirgeler de sayılır: {ar:وثار الجراد, tr:ve sâra'l-cerâd, gloss:çekirgeler havalandı, source:"ث و ر,B001"}. Toynaklar toprağa vurdukça yüzey dağılır, alttaki toprak üste çıkar ve havaya karışır.

[¶19] Dokuzuncu ayet aynı hareketi mezarlara taşır: {ar:أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ, tr:e-fe-lâ ya'lemu izâ bu'sira mâ fi'l-kubûr, gloss:bilmez mi ki kabirlerde olan şey altüst edilip çıkarıldığında, source:100:9}. "Bu'sira" ile dördüncü ayetin "eserne"si ayrı köklerdendir. Ama bu fiil Arapçada tam da dördüncü ayetin fiiliyle açıklanır: {ar:بعثر ما في القبور أثير وأخرج, tr:bu'sira mâ fi'l-kubûr: usîra ve uhrice, gloss:kabirlerdekiler "bu'sira" oldu, yani kaldırılıp çıkarıldı, source:"ب ع ث ر,B001"}. Bir başka açıklama, toprağın çevrilmesini daha da açık söyler: {ar:قلب ترابها وأثير ما فيها, tr:kulibe turâbuhâ ve usîra mâ fîhâ, gloss:toprağı ters çevrildi ve içindekiler kaldırıldı, source:"ب ع ث ر,B001"}. Kalıplaşmış bir söyleyiş bu altüst oluşun tam resmini çizer: {ar:بعثرت حوضي أي هدمته وجعلت أسفله أعلاه, tr:ba'sertu havdî, ey hedemtuhû ve ce'altu esfelehû a'lâh, gloss:havuzumu "ba'sere" ettim, yani yıktım, altını üstüne getirdim, source:"ب ع ث ر,B003"}. Bir yük de aynı biçimde dağıtılabilir: {ar:بعثر الرجل متاعه وبحثره إذا فرقه وبدده وقلب بعضه على بعض, tr:ba'sera'r-raculu metâ'ahû ve bahserahû izâ ferrakahû ve beddedehû ve kalebe ba'dahû alâ ba'd, gloss:adam eşyasını dağıtıp saçınca ve birbirine katınca "ba'sere" denir, source:"ب ع ث ر,B002"}. Kabir hem bir duraktır, {ar:القبر مقر الميت, tr:el-kabru makarru'l-meyyit, gloss:kabir, ölünün karar kıldığı yerdir, source:"ق ب ر,B001"}, hem de bir saklanma yeridir: {ar:أصل صحيح يدل على غموض في شيء وتطامن, tr:aslun sahîhun yedullu alâ gumûdın fî şey'in ve tatâmun, gloss:bir şeydeki kapalılığa ve çöküklüğe delalet eden sağlam bir kök, source:"ق ب ر,B002"}. Ayet "kabirlerdeki kimseler" demez, "kabirlerde olan şey" der. Bu "mâ" kelimesi kabirlerin içindekini, bir yüke ya da gömülü bir hazineye benzer biçimde, bir içerik olarak gösterir.

[¶20] İkinci ayetin kökü bu sahneye beklenmedik bir yerden katılır. Ateşi çıkaran kök, bir şeyi örtüp gizlemeyi de anlatır: {ar:واريت الشيء أي أخفيته وتوارى هو أي استتر, tr:vâraytu'ş-şey', ey ahfeytuh, ve tevârâ huve, ey isteter, gloss:"vâraytu", yani onu gizledim; "tevârâ", yani o gizlendi, source:"و ر ي,B005"}. Kur'an bu kökü ilk gömme sahnesinde kullanır. Kardeşini öldüren Âdem oğluna, Allah toprağı eşeleyen bir karga gönderir: {ar:فَبَعَثَ ٱللَّهُ غُرَابًا يَبْحَثُ فِى ٱلْأَرْضِ لِيُرِيَهُۥ كَيْفَ يُوَٰرِى سَوْءَةَ أَخِيهِ, tr:fe-be'asa'llâhu ğurâben yebhasu fi'l-ardı li-yuriyehû keyfe yuvârî sev'ete ahîh, gloss:Allah, kardeşinin cesedini nasıl örteceğini ona göstermek için toprağı eşeleyen bir karga gönderdi, source:5:31}. Karganın toprağı eşelemesi için kullanılan fiil ("yebhasu"), boğanın toprağı ayaklarıyla kaldırmasını anlatan söyleyişteki fiille ("behasehû") aynıdır. Gömmek, toprağı açıp sonra kapatmaktır. Dokuzuncu ayet bu işi tersine işletir: toprak yeniden açılır ve örtülen şey dışarı çıkar. Gizleyen ve ateşi çıkaran aynı kökün iki anlamı, böylece surenin başında ve sonunda iki ayrı yerde iş görür.

[¶21] Onuncu ayetin fiili de toprakla başlar: {ar:أصل التحصيل استخراج الذهب أو الفضة من الحجر أو من تراب المعدن, tr:aslu't-tahsîli istihrâcu'z-zehebi evi'l-fiddati mine'l-haceri ev min turâbi'l-ma'den, gloss:"tahsîl"in aslı, altını ya da gümüşü taştan veya maden toprağından çıkarmaktır, source:"ح ص ل,B002"}. Bu işi yapan kişinin de bir adı vardır: {ar:المحصلة المرأة التي تحصل تراب المعدن, tr:el-muhassılatu'l-mer'etu'lletî tuhassılu turâbe'l-ma'den, gloss:"muhassıla", maden toprağını ayıklayan kadındır, source:"ح ص ل,B002"}. Maden toprağı kazılır, yıkanır, elenir ve içindeki değerli metal ayrılır. Görüntünün sırası, sure ayetlerinin sırasıyla örtüşür: önce toprak kaldırılır, ardından içindeki değerli olan ayrılır.

[¶22] Kur'an bu sahneyi başka surelerde de kurar. Göğün yarılıp denizlerin taştığı anlatılırken şöyle denir: {ar:وَإِذَا ٱلْقُبُورُ بُعْثِرَتْ, tr:ve izâ'l-kubûru bu'siret, gloss:kabirler altüst edildiğinde, source:82:4}. Bunu hemen bilgi izler: {ar:عَلِمَتْ نَفْسٌ مَّا قَدَّمَتْ وَأَخَّرَتْ, tr:alimet nefsun mâ kaddemet ve ahharat, gloss:her can neyi öne sürüp neyi geride bıraktığını bilir, source:82:5}. Bizim surede aynı fiil "bilmez mi" sorusunun içinde geçer. Başka bir surede yer sarsılır ve {ar:وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا, tr:ve ahraceti'l-ardu eskâlehâ, gloss:yer ağırlıklarını dışarı çıkardı, source:99:2}. Bir başkasında yer uzatılır, {ar:وَأَلْقَتْ مَا فِيهَا وَتَخَلَّتْ, tr:ve elkat mâ fîhâ ve tehallet, gloss:içindekini atıp boşaldı, source:84:4}. Bu son ifadede de "mâ fîhâ", yani "içindeki" söz konusudur. Hac suresinde bu sahne açık bir hükümdür: {ar:وَأَنَّ ٱللَّهَ يَبْعَثُ مَن فِى ٱلْقُبُورِ, tr:ve enna'llâhe yeb'asu men fi'l-kubûr, gloss:ve Allah kabirlerdekileri diriltecektir, source:22:7}. Musa'nın Firavun'a söylediği sözlerin arasında toprağın üç işlevi tek ayette sayılır: {ar:مِنْهَا خَلَقْنَٰكُمْ وَفِيهَا نُعِيدُكُمْ وَمِنْهَا نُخْرِجُكُمْ تَارَةً أُخْرَىٰ, tr:minhâ halaknâkum ve fîhâ nu'îdukum ve minhâ nuhricukum târaten uhrâ, gloss:sizi ondan yarattık, sizi oraya döndüreceğiz ve sizi bir kez daha oradan çıkaracağız, source:20:55}. Kökün "havalanan çekirge" anlamı da diriliş sahnesinde Kur'an'ın kendi benzetmesiyle karşılanır: {ar:يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ كَأَنَّهُمْ جَرَادٌ مُّنتَشِرٌ, tr:yahrucûne mine'l-ecdâsi ke-ennehum cerâdun munteşir, gloss:kabirlerden yayılmış çekirgeler gibi çıkarlar, source:54:7}. Toprağı sürmek ise Kur'an'da dünyaya yapılan yatırımın ölçüsüdür. Eski kavimler hakkında {ar:وَأَثَارُوا۟ ٱلْأَرْضَ وَعَمَرُوهَآ أَكْثَرَ مِمَّا عَمَرُوهَا, tr:ve esârû'l-arda ve amerûhâ ekser mimmâ amerûhâ, gloss:toprağı sürdüler ve onu bunların imar ettiğinden daha çok imar ettiler, source:30:9} denir. İsrailoğullarından boğazlanması istenen inek de {ar:لَّا ذَلُولٌ تُثِيرُ ٱلْأَرْضَ, tr:lâ zelûlun tusîru'l-ard, gloss:toprağı sürmeye koşulmamış, source:2:71} diye tarif edilir.

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/ledger.md =====
- not developed: chain 7 (rain on the land) as its own section - merged into chain 6 as one image of kenûd
- not developed: chain 9 (shared pot) as its own section - merged into chain 8 as the counter-scene of the closed hand
- not developed: غ ي ر B001 "God's rain/provision" member in chains 6 and 7 - wrong root for al-mughīrāt, dropped
- not developed: ضبح as owl and echo calls (chain 4) - relies on pre-Islamic lore outside the Quran, dropped
- not developed: ربيون "great crowds" (chain 11) - too loose a link to rabb, dropped
- not developed: the map's meysir lore (chain 9) and its commentators remark (chain 6) - reports from outside the Quran, dropped
- memory: al-mughīrāt is the form IV participle of أغار "to raid", root غ و ر
- memory: غار يغير "to provide rain" is a separate verb and not the root of al-mughīrāt
- memory: the preposition عن in 38:32 can mean both "because of" and "away from"

===== passages from the discovery list (189) =====
## strong (61)

- (2:71) [luna: contrast; terra: strong; basis: contrast+root+scene] [cited in ¶22] قَالَ إِنَّهُۥ يَقُولُ إِنَّهَا بَقَرَةٌۭ لَّا ذَلُولٌۭ تُثِيرُ ٱلْأَرْضَ وَلَا تَسْقِى ٱلْحَرْثَ مُسَلَّمَةٌۭ لَّا شِيَةَ فِيهَا ۚ قَالُوا۟ ٱلْـَٰٔنَ جِئْتَ بِٱلْحَقِّ ۚ فَذَبَحُوهَا وَمَا كَادُوا۟ يَفْعَلُونَ
  Unverified discovery rationale: luna: The section’s ثور dictionary form explains the ox through plowing earth; this cow is explicitly “لَا ذَلُولٌ تُثِيرُ الْأَرْضَ,” not trained to plow it. The negation marks the boundary of the source’s plowing sense. | terra: لَّا ذَلُولٌ تُثِيرُ ٱلْأَرْضَ describes a cow not trained to plow, directly realizing the section's dictionary picture of the ox by which earth is stirred.
- (2:72) [terra: strong; basis: neighbour+theme] وَإِذْ قَتَلْتُمْ نَفْسًۭا فَٱدَّٰرَْٰٔتُمْ فِيهَا ۖ وَٱللَّهُ مُخْرِجٌۭ مَّا كُنتُمْ تَكْتُمُونَ
  Unverified discovery rationale: terra: After a concealed killing, وَٱللَّهُ مُخْرِجٌ مَّا كُنتُمْ تَكْتُمُونَ promises that God will bring out what was hidden; beside the plowing cow of 2:71, it joins soil-working, homicide, and disclosure as the section does.
- (2:73) [terra: strong; basis: neighbour+scene+theme] فَقُلْنَا ٱضْرِبُوهُ بِبَعْضِهَا ۚ كَذَٰلِكَ يُحْىِ ٱللَّهُ ٱلْمَوْتَىٰ وَيُرِيكُمْ ءَايَٰتِهِۦ لَعَلَّكُمْ تَعْقِلُونَ
  Unverified discovery rationale: terra: The slain person is made alive through the cow and كَذَٰلِكَ يُحْىِ ٱللَّهُ ٱلْمَوْتَى; it completes 2:71-72 by turning a disputed hidden corpse into evidence of resurrection.
- (2:267) [luna: medium (missing-ayat turn); terra: strong (missing-ayat turn); basis: scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَنفِقُوا۟ مِن طَيِّبَٰتِ مَا كَسَبْتُمْ وَمِمَّآ أَخْرَجْنَا لَكُم مِّنَ ٱلْأَرْضِ ۖ وَلَا تَيَمَّمُوا۟ ٱلْخَبِيثَ مِنْهُ تُنفِقُونَ وَلَسْتُم بِـَٔاخِذِيهِ إِلَّآ أَن تُغْمِضُوا۟ فِيهِ ۚ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ غَنِىٌّ حَمِيدٌ
  Unverified discovery rationale: luna: This ayah speaks of good things brought forth from earth and forbids choosing the bad for charity when one would not accept it except reluctantly. It parallels the section’s ore-sifting image through a concrete distinction between valued and inferior produce from earth. | terra: Believers are told to spend from good things and from what God has brought out of the earth, while refusing the bad; the ayah combines terrestrial extraction with discrimination between valuable and inferior material.
- (3:29) [terra: strong; basis: theme] قُلْ إِن تُخْفُوا۟ مَا فِى صُدُورِكُمْ أَوْ تُبْدُوهُ يَعْلَمْهُ ٱللَّهُ ۗ وَيَعْلَمُ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: terra: Whether people hide مَا فِى صُدُورِكُمْ or show it, Allah knows it; the ayah gives the concealment/disclosure polarity behind the section's chest-as-deposit image.
- (3:154) [terra: strong; basis: theme] ثُمَّ أَنزَلَ عَلَيْكُم مِّنۢ بَعْدِ ٱلْغَمِّ أَمَنَةًۭ نُّعَاسًۭا يَغْشَىٰ طَآئِفَةًۭ مِّنكُمْ ۖ وَطَآئِفَةٌۭ قَدْ أَهَمَّتْهُمْ أَنفُسُهُمْ يَظُنُّونَ بِٱللَّهِ غَيْرَ ٱلْحَقِّ ظَنَّ ٱلْجَٰهِلِيَّةِ ۖ يَقُولُونَ هَل لَّنَا مِنَ ٱلْأَمْرِ مِن شَىْءٍۢ ۗ قُلْ إِنَّ ٱلْأَمْرَ كُلَّهُۥ لِلَّهِ ۗ يُخْفُونَ فِىٓ أَنفُسِهِم مَّا لَا يُبْدُونَ لَكَ ۖ يَقُولُونَ لَوْ كَانَ لَنَا مِنَ ٱلْأَمْرِ شَىْءٌۭ مَّا قُتِلْنَا هَٰهُنَا ۗ قُل لَّوْ كُنتُمْ فِى بُيُوتِكُمْ لَبَرَزَ ٱلَّذِينَ كُتِبَ عَلَيْهِمُ ٱلْقَتْلُ إِلَىٰ مَضَاجِعِهِمْ ۖ وَلِيَبْتَلِىَ ٱللَّهُ مَا فِى صُدُورِكُمْ وَلِيُمَحِّصَ مَا فِى قُلُوبِكُمْ ۗ وَٱللَّهُ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: terra: لِيَبْتَلِىَ ٱللَّهُ مَا فِى صُدُورِكُمْ وَلِيُمَحِّصَ مَا فِى قُلُوبِكُمْ joins testing breast contents to purification, closely matching the section's image of processing mixed earth to isolate what is truly there.
- (4:42) [terra: strong; basis: contrast+scene+theme] يَوْمَئِذٍۢ يَوَدُّ ٱلَّذِينَ كَفَرُوا۟ وَعَصَوُا۟ ٱلرَّسُولَ لَوْ تُسَوَّىٰ بِهِمُ ٱلْأَرْضُ وَلَا يَكْتُمُونَ ٱللَّهَ حَدِيثًۭا
  Unverified discovery rationale: terra: The condemned wish the earth were levelled over them, yet لَا يَكْتُمُونَ ٱللَّهَ حَدِيثًا; imagined covering by earth cannot prevent disclosure, reversing burial's concealing function.
- (5:31) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶20] فَبَعَثَ ٱللَّهُ غُرَابًۭا يَبْحَثُ فِى ٱلْأَرْضِ لِيُرِيَهُۥ كَيْفَ يُوَٰرِى سَوْءَةَ أَخِيهِ ۚ قَالَ يَٰوَيْلَتَىٰٓ أَعَجَزْتُ أَنْ أَكُونَ مِثْلَ هَٰذَا ٱلْغُرَابِ فَأُوَٰرِىَ سَوْءَةَ أَخِى ۖ فَأَصْبَحَ مِنَ ٱلنَّٰدِمِينَ
  Unverified discovery rationale: luna: The section’s ثور dictionary form describes an ox stirring earth as it searches with its legs; here the raven “يَبْحَثُ فِي الْأَرْضِ” and teaches how to “يُوَارِيَ” the body. Burial opens earth and then covers what it holds, the inverse of the section’s graves opened. | terra: The crow يَبْحَثُ فِى ٱلْأَرْضِ scratches open the soil to teach how to يُوَارِى the brother's body; it supplies both the section's bull-like earth-scratching verb and the concealment branch of the fire-producing root, while burial reverses the grave-opening scene.
- (7:20) [luna: strong (missing-ayat turn); terra: strong; basis: contrast+root+scene+theme] فَوَسْوَسَ لَهُمَا ٱلشَّيْطَٰنُ لِيُبْدِىَ لَهُمَا مَا وُۥرِىَ عَنْهُمَا مِن سَوْءَٰتِهِمَا وَقَالَ مَا نَهَىٰكُمَا رَبُّكُمَا عَنْ هَٰذِهِ ٱلشَّجَرَةِ إِلَّآ أَن تَكُونَا مَلَكَيْنِ أَوْ تَكُونَا مِنَ ٱلْخَٰلِدِينَ
  Unverified discovery rationale: luna: The section explicitly names the concealment sense of its و ر ي root; this ayah uses “وُورِيَ” for what was covered from Adam and his wife. It adds bodily concealment to the section’s burial-and-uncovering image. | terra: The devil seeks لِيُبْدِىَ لَهُمَا مَا وُۥرِىَ عَنْهُمَا, bringing into view what had been concealed; the passive وُۥرِىَ realizes the section's named hiding sense and its reveal/conceal reversal.
- (7:25) [terra: strong; basis: scene+theme] قَالَ فِيهَا تَحْيَوْنَ وَفِيهَا تَمُوتُونَ وَمِنْهَا تُخْرَجُونَ
  Unverified discovery rationale: terra: فِيهَا تَمُوتُونَ ... وَمِنْهَا تُخْرَجُونَ locates death in earth and later emergence from it, the same closing and reopening of soil developed in the section.
- (7:57) [terra: strong; basis: scene+theme] وَهُوَ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۖ حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًۭا ثِقَالًۭا سُقْنَٰهُ لِبَلَدٍۢ مَّيِّتٍۢ فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ
  Unverified discovery rationale: terra: Rain brings produce out of a dead land and the ayah concludes كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ, explicitly making emergence from revived soil the model for bringing out the dead.
- (8:37) [terra: strong; basis: scene+theme] لِيَمِيزَ ٱللَّهُ ٱلْخَبِيثَ مِنَ ٱلطَّيِّبِ وَيَجْعَلَ ٱلْخَبِيثَ بَعْضَهُۥ عَلَىٰ بَعْضٍۢ فَيَرْكُمَهُۥ جَمِيعًۭا فَيَجْعَلَهُۥ فِى جَهَنَّمَ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
  Unverified discovery rationale: terra: God separates ٱلْخَبِيثَ مِنَ ٱلطَّيِّبِ and piles the bad بَعْضَهُۥ عَلَىٰ بَعْضٍ; the ayah combines the section's assay-like separation of value with its dictionary picture of mixed goods turned one over another.
- (9:64) [terra: strong; basis: theme] يَحْذَرُ ٱلْمُنَٰفِقُونَ أَن تُنَزَّلَ عَلَيْهِمْ سُورَةٌۭ تُنَبِّئُهُم بِمَا فِى قُلُوبِهِمْ ۚ قُلِ ٱسْتَهْزِءُوٓا۟ إِنَّ ٱللَّهَ مُخْرِجٌۭ مَّا تَحْذَرُونَ
  Unverified discovery rationale: terra: إِنَّ ٱللَّهَ مُخْرِجٌ مَّا تَحْذَرُونَ threatens to bring out what hypocrites fear will be exposed from their hearts, an explicit inner analogue to opening graves and extracting ore.
- (11:5) [luna: medium; terra: strong; basis: root+scene+theme] أَلَآ إِنَّهُمْ يَثْنُونَ صُدُورَهُمْ لِيَسْتَخْفُوا۟ مِنْهُ ۚ أَلَا حِينَ يَسْتَغْشُونَ ثِيَابَهُمْ يَعْلَمُ مَا يُسِرُّونَ وَمَا يُعْلِنُونَ ۚ إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ
  Unverified discovery rationale: luna: The people “يَثْنُونَ صُدُورَهُمْ لِيَسْتَخْفُوا مِنْهُ” fold their breasts to hide, while God knows what they conceal. This gives a bodily concealment image that the section’s chest contents later overturn. | terra: People fold their breasts and cover themselves to hide, yet God knows what they keep secret and disclose; bodily acts of covering fail to keep chest contents inaccessible.
- (11:82) [terra: strong; basis: contrast+scene] فَلَمَّا جَآءَ أَمْرُنَا جَعَلْنَا عَٰلِيَهَا سَافِلَهَا وَأَمْطَرْنَا عَلَيْهَا حِجَارَةًۭ مِّن سِجِّيلٍۢ مَّنضُودٍۢ
