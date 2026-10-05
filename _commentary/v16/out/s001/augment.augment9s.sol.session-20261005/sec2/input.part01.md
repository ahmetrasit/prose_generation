Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 2 of 14 ("Uysallaştırılmış olan: sahip, mülk ve kul"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 2 (prose paragraphs numbered) =====
[¶9] İkinci görüntü bir efendiyi ve onun sahip olduğu şeyleri gösterir: bir ev, bir at, bir köle. Bu sahnedeki işleyiş uysallaştırmadır. Yol çiğnenerek düzlenir, deve katranla sıvanıp uysallaştırılır, insan alçaltılıp hizmete sokulur. Bu üç durumun hepsini tek bir sıfat anlatır: "müzellel", yani boyun eğdirilmiş. Yol için {ar:الطريق المعبد وهو المسلوك المذلل, tr:et-tarîku'l-mu'abbed ve hüve'l-meslûku'l-müzellel, gloss:çiğnenmiş, uysallaştırılmış yol, source:"ع ب د,B005"} denir. Deve için {ar:البعير المعبد المهنوء بالقطران المذلل, tr:el-ba'îru'l-mu'abbedü'l-mehnû'ü bi'l-katrân el-müzellel, gloss:katranla sıvanmış, uysallaştırılmış deve, source:"ع ب د,B005"} denir. İnsan için de {ar:عبدت الرجل إذا ذللته وعبدت القوم اتخذتهم عبيدا, tr:abedtü'r-racüle izâ zelleltüh, gloss:adamı boyun eğdirdim; kavmi köle edindim, source:"ع ب د,B004"} denir.

[¶10] Sure bu sahnenin bütün rollerine ad verir. Birinci ayetteki {ar:ٱللَّهِ, tr:Allâh, gloss:Allah, source:1:1} adı, kulluk edilen olmakla anılır: {ar:فالإله الله تعالى لأنه معبود, tr:fe'l-ilâhu'llâhu teâlâ li-ennehû ma'bûd, gloss:ilah Allah'tır, çünkü kulluk edilendir, source:"ء ل ه,B001"}, {ar:لا يكون إلاها حتى يكون معبودا, tr:lâ yekûnü ilâhen hattâ yekûne ma'bûdâ, gloss:kulluk edilmedikçe ilah olmaz, source:"ء ل ه,B001"}. İkinci ayetteki {ar:رَبِّ, tr:rabbi, gloss:Rabbi, source:1:2} kelimesi itaat edilen efendidir: {ar:ويكون الرب: السيد المطاع, tr:ve yekûnü'r-rabbü es-seyyide'l-mutâ', gloss:Rab, itaat edilen efendidir, source:"ر ب ب,B001"}. Kelime ev ve at gibi somut şeylerin sahibini de anlatır: {ar:رب الدار ورب الفرس, tr:rabbü'd-dâr ve rabbü'l-feres, gloss:evin sahibi, atın sahibi, source:"ر ب ب,B001"}. Bir başka cümle, ikinci ayetin Rabbini dördüncü ayetin Mâlikine bağlar: {ar:ورب كل شيء مالكه, tr:ve rabbü kulli şey'in mâlikuh, gloss:her şeyin rabbi onun mâlikidir, source:"ر ب ب,B001"}. Dördüncü ayetteki "mâlik", elin tuttuğu şeyin sahibidir: {ar:الملك ما ملكت اليد من مال وخول, tr:el-milkü mâ meleketi'l-yedü min mâlin ve haval, gloss:mülk, elin sahip olduğu mal ve hizmetkârlardır, source:"م ل ك,B002"}. Mülk kelimesi alışılmış kullanımda köleler için özelleşir: {ar:المملوك يختص في التعارف بالرقيق من الأملاك, tr:el-memlûkü yahtassu fi't-teâruf bi'r-rakîk, gloss:memlûk, yaygın kullanımda mülkler arasından köleye özgü olur, source:"م ل ك,B002"}.

[¶11] Aynı ayetteki "dîn" kelimesi bu üç kökü tek cümlede birbirine bağlar: {ar:دانه دينا أي أذله واستعبده ودينته ملكته, tr:dânehû dînen, ezellehû vesta'bedeh, ve deyyentühû melektüh, gloss:onu boyun eğdirdi ve köle edindi; ona sahip oldum, source:"د ي ن,B004"}. Kul da bu kökten adlandırılır: {ar:العبد مدين كأنهما أذلهما العمل, tr:el-abdü medîn, gloss:köle medîndir, sanki iş onları alçaltmıştır, source:"د ي ن,B004"}. "Dîn" bu yüzden aynı zamanda itaattir: {ar:فالدين الطاعة, tr:fe'd-dînü't-tâ'a, gloss:din itaattir, source:"د ي ن,B001"}, {ar:الدين لله طاعته والتعبد له, tr:ed-dînü lillâhi tâ'atühû ve't-teabbüdü leh, gloss:Allah'a din, O'na itaat ve kulluktur, source:"د ي ن,B001"}. Böylece dördüncü ayet sahibi adlandırırken, kulun durumunu da aynı kelimelerin içinde taşır.

[¶12] Beşinci ayette konuşma değişir. İlk dört ayet sahipten "O" diye söz eder. Beşinci ayetle birlikte sahip olunan konuşmaya başlar ve sahibine doğrudan "sen" diye seslenir: {ar:إِيَّاكَ نَعْبُدُ, tr:iyyâke na'büdü, gloss:yalnız sana kulluk ederiz, source:1:5}. Kul, sahip olunan kişidir: {ar:العبد المملوك وجمعه عبيد, tr:el-abdü'l-memlûk, gloss:abd memlûktür, çoğulu abîddir, source:"ع ب د,B001"}. Bu ayetin kendisi itaat ve boyun eğmekle açıklanır: {ar:إياك نعبد إياك نطيع الطاعة التي نخضع معها, tr:iyyâke na'büdü: iyyâke nutî'u't-tâ'ate'lletî nahdau me'ahâ, gloss:yalnız sana kulluk ederiz, yani yalnız sana, içinde boyun eğdiğimiz bir itaatle itaat ederiz, source:"ع ب د,B003"}. Kulluk alçalmanın en ileri derecesidir: {ar:العبودية إظهار التذلل والعبادة غاية التذلل, tr:el-ubûdiyyetü izhâru't-tezellül ve'l-ibâdetü gâyetü't-tezellül, gloss:ubudiyet alçaklığı göstermektir, ibadet ise alçalmanın son noktasıdır, source:"ع ب د,B003"}.

[¶13] Bu görüntü, düz bir mealde kaybolan bir şeyi görünür kılar. "Kulluk ederiz" sözü yalnızca bir duygu anlatmaz, bir durumu da anlatır. Konuşan, bir sahibe ait olduğunu söyler ve bu aitliği kendi ağzıyla kabul eder. Bu aitlik kulun seçimiyle başlamaz: {ar:العبد الإنسان حرا أو رقيقا هو عبد الله, tr:el-abdü'l-insânü hurran ev rakîkan hüve abdu'llâh, gloss:insan, hür de olsa köle de olsa, Allah'ın kuludur, source:"ع ب د,B002"}. Bunun sebebi yaratılmış olmasıdır: {ar:عبد بالإيجاد وذلك ليس إلا لله, tr:abdün bi'l-îcâd, gloss:var edilmekle kul olmak; bu yalnız Allah içindir, source:"ع ب د,B002"}. Kur'an bunu açıkça söyler: {ar:إِن كُلُّ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ إِلَّآ ءَاتِى ٱلرَّحْمَٰنِ عَبْدًۭا, tr:in küllü men fi's-semâvâti ve'l-ardı illâ âti'r-rahmâni abdâ, gloss:göklerde ve yerde kim varsa Rahman'a ancak kul olarak gelecektir, source:19:93}. Beşinci ayetteki "na'büdü", yaratılışla zaten var olan bu aitliğin kulun kendi sesiyle kabul edilmesidir. Aynı ailede sahnenin öbür yüzü de vardır: {ar:المعبد المكرم والمعظم كأنه يعبد, tr:el-mu'abbedü'l-mükerramü ve'l-mu'azzam, gloss:mu'abbed, sanki kulluk ediliyormuş gibi ağırlanan ve yüceltilen kimsedir, source:"ع ب د,B006"}. Kulun boyun eğdiği yer, onu ağırlayan sahibin evidir.

[¶14] Kur'an'da bu sahne birçok yerde kurulur. Allah bir örnek verir: {ar:عَبْدًۭا مَّمْلُوكًۭا لَّا يَقْدِرُ عَلَىٰ شَىْءٍۢ, tr:abden memlûken lâ yakdiru alâ şey', gloss:hiçbir şeye gücü yetmeyen, sahip olunan bir köle, source:16:75}. Bu köle, kendisine güzel rızık verilip onu açıktan ve gizlice harcayan kişiyle karşılaştırılır ve örnek {ar:ٱلْحَمْدُ لِلَّهِ, tr:el-hamdü lillâh, gloss:hamd Allah'adır, source:16:75} sözüyle kapanır. Hayvanlar konusunda Allah sahipliği ve uysallaştırmayı birlikte anar: {ar:أَنْعَٰمًۭا فَهُمْ لَهَا مَٰلِكُونَ, tr:en'âmen fe-hüm lehâ mâlikûn, gloss:sahip oldukları hayvanlar, source:36:71}, {ar:وَذَلَّلْنَٰهَا لَهُمْ فَمِنْهَا رَكُوبُهُمْ, tr:ve zellelnâhâ lehüm fe-minhâ rakûbühüm, gloss:onları kendilerine boyun eğdirdik; kimine binerler, source:36:72}. Firavun'un sarayında bu sahnenin insan hali görülür. Firavun Musa'ya şöyle der: {ar:أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا, tr:e-lem nurabbike fînâ velîdâ, gloss:seni küçükken aramızda biz büyütmedik mi, source:26:18}. Musa şöyle cevap verir: {ar:وَتِلْكَ نِعْمَةٌۭ تَمُنُّهَا عَلَىَّ أَنْ عَبَّدتَّ بَنِىٓ إِسْرَٰٓءِيلَ, tr:ve tilke ni'metün temünnühâ aleyye en abbedte benî İsrâîl, gloss:başıma kaktığın o nimet, İsrailoğullarını köle edinmen midir, source:26:22}. "Abbedte", "abedtü'l-kavme ittehaztühüm abîden" cümlesindeki zorla köle edinmenin Kur'an'daki karşılığıdır. Yusuf, Mısırlı efendisinin evindeki kadına "rab" kelimesini bir insan için kullanır: {ar:إِنَّهُۥ رَبِّىٓ أَحْسَنَ مَثْوَاىَ, tr:innehû rabbî ahsene mesvây, gloss:o benim efendimdir, bana güzel bir yer verdi, source:12:23}. Kitap ehline yapılan çağrı ise insanlar arasındaki bu efendilik ilişkisini sınırlar: {ar:وَلَا يَتَّخِذَ بَعْضُنَا بَعْضًا أَرْبَابًۭا مِّن دُونِ ٱللَّهِ, tr:ve lâ yettehize ba'dunâ ba'dan erbâben min dûnillâh, gloss:Allah'ı bırakıp birbirimizi rabler edinmeyelim, source:3:64}. Zindandaki Yusuf, beşinci ayetin yapısını kurar: {ar:أَمَرَ أَلَّا تَعْبُدُوٓا۟ إِلَّآ إِيَّاهُ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ, tr:emera ellâ ta'büdû illâ iyyâh, zâlike'd-dînü'l-kayyim, gloss:yalnız O'na kulluk etmenizi emretti; dimdik din budur, source:12:40}. Burada "iyyâ", kulluk, din ve "kayyim" kökü tek cümlede bir araya gelir. Kur'an alçalmanın yalnızca kula ait olduğunu da söyler: {ar:وَلَمْ يَكُن لَّهُۥ وَلِىٌّۭ مِّنَ ٱلذُّلِّ, tr:ve lem yekün lehû veliyyün mine'z-züll, gloss:düşkünlükten ötürü bir yardımcıya da ihtiyacı olmadı, source:17:111}. Sahip hiçbir şekilde alçalmaz.

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

===== passages from the discovery list (267) =====
## strong (172)

- (2:21) [luna: strong; terra: strong (missing-ayat turn); basis: root+theme] يَٰٓأَيُّهَا ٱلنَّاسُ ٱعْبُدُوا۟ رَبَّكُمُ ٱلَّذِى خَلَقَكُمْ وَٱلَّذِينَ مِن قَبْلِكُمْ لَعَلَّكُمْ تَتَّقُونَ
  Unverified discovery rationale: luna: The source-section root ر ب ب appears in رَبَّكُمُ; the command to worship your Lord is grounded in His having created the people and those before them. | terra: “Worship your Lord” (ٱعْبُدُوا۟ رَبَّكُمُ) immediately identifies Him as the one who created people, joining Rabb, createdness, and service.
- (2:34) [luna: strong (missing-ayat turn); basis: scene+theme] وَإِذْ قُلْنَا لِلْمَلَٰٓئِكَةِ ٱسْجُدُوا۟ لِءَادَمَ فَسَجَدُوٓا۟ إِلَّآ إِبْلِيسَ أَبَىٰ وَٱسْتَكْبَرَ وَكَانَ مِنَ ٱلْكَٰفِرِينَ
  Unverified discovery rationale: luna: God commands the angels to prostrate to Adam; the honored human receives obeisance while remaining a creature under God's command, matching the section's honored-servant secondary sense.
- (2:49) [luna: strong; basis: neighbour+scene] وَإِذْ نَجَّيْنَٰكُم مِّنْ ءَالِ فِرْعَوْنَ يَسُومُونَكُمْ سُوٓءَ ٱلْعَذَابِ يُذَبِّحُونَ أَبْنَآءَكُمْ وَيَسْتَحْيُونَ نِسَآءَكُمْ ۚ وَفِى ذَٰلِكُم بَلَآءٌۭ مِّن رَّبِّكُمْ عَظِيمٌۭ
  Unverified discovery rationale: luna: Pharaoh's people slaughtered sons and spared women; this earlier telling supplies the oppression behind the enslavement scene.
- (2:83) [luna: strong; basis: root+speaker] وَإِذْ أَخَذْنَا مِيثَٰقَ بَنِىٓ إِسْرَٰٓءِيلَ لَا تَعْبُدُونَ إِلَّا ٱللَّهَ وَبِٱلْوَٰلِدَيْنِ إِحْسَانًۭا وَذِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَقُولُوا۟ لِلنَّاسِ حُسْنًۭا وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ ثُمَّ تَوَلَّيْتُمْ إِلَّا قَلِيلًۭا مِّنكُمْ وَأَنتُم مُّعْرِضُونَ
  Unverified discovery rationale: luna: The covenant commands Israel to worship none but Allah; this is a binding statement of the exclusive service voiced in 1:5.
- (2:107) [luna: strong; basis: root+theme] أَلَمْ تَعْلَمْ أَنَّ ٱللَّهَ لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۗ وَمَا لَكُم مِّن دُونِ ٱللَّهِ مِن وَلِىٍّۢ وَلَا نَصِيرٍ
  Unverified discovery rationale: luna: The source-section root م ل ك appears in مُّلْكُ السَّمَاوَاتِ وَالْأَرْضِ; sovereignty belongs to God alone, and no protector or helper exists besides Him.
- (2:116) [luna: strong; basis: root+theme] وَقَالُوا۟ ٱتَّخَذَ ٱللَّهُ وَلَدًۭا ۗ سُبْحَٰنَهُۥ ۖ بَل لَّهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۖ كُلٌّۭ لَّهُۥ قَٰنِتُونَ
  Unverified discovery rationale: luna: What is in the heavens and earth belongs to Allah, and all are devoutly obedient to Him; possession and service appear together.
- (2:133) [luna: strong; basis: speaker+theme] أَمْ كُنتُمْ شُهَدَآءَ إِذْ حَضَرَ يَعْقُوبَ ٱلْمَوْتُ إِذْ قَالَ لِبَنِيهِ مَا تَعْبُدُونَ مِنۢ بَعْدِى قَالُوا۟ نَعْبُدُ إِلَٰهَكَ وَإِلَٰهَ ءَابَآئِكَ إِبْرَٰهِۦمَ وَإِسْمَٰعِيلَ وَإِسْحَٰقَ إِلَٰهًۭا وَٰحِدًۭا وَنَحْنُ لَهُۥ مُسْلِمُونَ
  Unverified discovery rationale: luna: Jacob asks his sons whom they will worship after him; their answer names the one God of their fathers, presenting service as the creature's inherited allegiance.
- (2:156) [terra: strong; basis: speaker+theme] ٱلَّذِينَ إِذَآ أَصَٰبَتْهُم مُّصِيبَةٌۭ قَالُوٓا۟ إِنَّا لِلَّهِ وَإِنَّآ إِلَيْهِ رَٰجِعُونَ
  Unverified discovery rationale: terra: “Innā lillāhi wa innā ilayhi rājiʿūn” puts belonging to God and return to Him in the servants’ own voice.
- (2:186) [terra: strong (missing-ayat turn); basis: root+speaker+theme] وَإِذَا سَأَلَكَ عِبَادِى عَنِّى فَإِنِّى قَرِيبٌ ۖ أُجِيبُ دَعْوَةَ ٱلدَّاعِ إِذَا دَعَانِ ۖ فَلْيَسْتَجِيبُوا۟ لِى وَلْيُؤْمِنُوا۟ بِى لَعَلَّهُمْ يَرْشُدُونَ
  Unverified discovery rationale: terra: When “My servants” ask about God, He answers that He is near and responds to their call, supplying the direct reciprocal relation behind a servant’s appeal for help.
- (3:26) [luna: strong; terra: strong; basis: contrast+root+theme] قُلِ ٱللَّهُمَّ مَٰلِكَ ٱلْمُلْكِ تُؤْتِى ٱلْمُلْكَ مَن تَشَآءُ وَتَنزِعُ ٱلْمُلْكَ مِمَّن تَشَآءُ وَتُعِزُّ مَن تَشَآءُ وَتُذِلُّ مَن تَشَآءُ ۖ بِيَدِكَ ٱلْخَيْرُ ۖ إِنَّكَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: luna: The source-section's root م ل ك is widened by مَالِكَ الْمُلْكِ: God grants and removes human dominion, showing that human ownership is received and bounded. | terra: مَٰلِكَ ٱلْمُلْكِ gives and removes rule and both honors and abases; ownership here actively determines the high and low position developed by the image.
- (3:51) [luna: strong; terra: strong (missing-ayat turn); basis: root+speaker+theme] إِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۗ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
  Unverified discovery rationale: luna: Jesus says Allah is his Lord and the people's Lord, then commands them to worship Him; the human messenger remains a servant under the same Lord. | terra: Jesus says, “God is my Lord and your Lord, so worship Him,” a direct human voice refusing the Lord role while enjoining service.
- (3:64) [luna: strong; terra: contrast; basis: contrast+root+theme] [cited in ¶14] قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ تَعَالَوْا۟ إِلَىٰ كَلِمَةٍۢ سَوَآءٍۭ بَيْنَنَا وَبَيْنَكُمْ أَلَّا نَعْبُدَ إِلَّا ٱللَّهَ وَلَا نُشْرِكَ بِهِۦ شَيْـًۭٔا وَلَا يَتَّخِذَ بَعْضُنَا بَعْضًا أَرْبَابًۭا مِّن دُونِ ٱللَّهِ ۚ فَإِن تَوَلَّوْا۟ فَقُولُوا۟ ٱشْهَدُوا۟ بِأَنَّا مُسْلِمُونَ
  Unverified discovery rationale: luna: The source-section root ر ب ب appears in أَرْبَابًا; the call says not to take one another as lords apart from Allah, setting a boundary on human beings occupying the Lord's place. | terra: The call refuses taking one another as أَرْبَابًا besides God, directly limiting the human master relation the section traces in Rabb.
- (3:79) [luna: strong; terra: contrast; basis: contrast+root+theme] مَا كَانَ لِبَشَرٍ أَن يُؤْتِيَهُ ٱللَّهُ ٱلْكِتَٰبَ وَٱلْحُكْمَ وَٱلنُّبُوَّةَ ثُمَّ يَقُولَ لِلنَّاسِ كُونُوا۟ عِبَادًۭا لِّى مِن دُونِ ٱللَّهِ وَلَٰكِن كُونُوا۟ رَبَّٰنِيِّۦنَ بِمَا كُنتُمْ تُعَلِّمُونَ ٱلْكِتَٰبَ وَبِمَا كُنتُمْ تَدْرُسُونَ
  Unverified discovery rationale: luna: The source-section root ر ب ب appears in رَبَّانِيِّينَ, while the verse denies that a prophet would tell people to become his servants instead of God's; human teaching authority cannot claim worship. | terra: A recipient of revelation may not tell people, “be عِبَادًا لِّى”; even elevated human authority cannot turn people into its own servants.
- (3:80) [luna: strong; terra: contrast (missing-ayat turn); basis: contrast+neighbour+root] وَلَا يَأْمُرَكُمْ أَن تَتَّخِذُوا۟ ٱلْمَلَٰٓئِكَةَ وَٱلنَّبِيِّۦنَ أَرْبَابًا ۗ أَيَأْمُرُكُم بِٱلْكُفْرِ بَعْدَ إِذْ أَنتُم مُّسْلِمُونَ
  Unverified discovery rationale: luna: The source-section root ر ب ب appears in أَرْبَابًا; the verse explicitly says prophets and angels must not be taken as lords, marking the limit of human mastery. | terra: The revelation-bearer cannot command people to take angels or prophets as arbāb; this continues 3:79’s boundary against creatures claiming lordship.
- (3:83) [luna: strong; terra: strong; basis: contrast+root+theme] أَفَغَيْرَ دِينِ ٱللَّهِ يَبْغُونَ وَلَهُۥٓ أَسْلَمَ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ طَوْعًۭا وَكَرْهًۭا وَإِلَيْهِ يُرْجَعُونَ
  Unverified discovery rationale: luna: The verse says all in the heavens and earth submit to Allah willingly or unwillingly and return to Him, expressing the created servitude behind 19:93. | terra: All in heaven and earth submit to God willingly or unwillingly under His دِين, making the created servant’s belonging antecedent to a chosen verbal confession.
- (4:36) [luna: strong; terra: strong; basis: root+theme] ۞ وَٱعْبُدُوا۟ ٱللَّهَ وَلَا تُشْرِكُوا۟ بِهِۦ شَيْـًۭٔا ۖ وَبِٱلْوَٰلِدَيْنِ إِحْسَٰنًۭا وَبِذِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَٱلْجَارِ ذِى ٱلْقُرْبَىٰ وَٱلْجَارِ ٱلْجُنُبِ وَٱلصَّاحِبِ بِٱلْجَنۢبِ وَٱبْنِ ٱلسَّبِيلِ وَمَا مَلَكَتْ أَيْمَٰنُكُمْ ۗ إِنَّ ٱللَّهَ لَا يُحِبُّ مَن كَانَ مُخْتَالًۭا فَخُورًا
