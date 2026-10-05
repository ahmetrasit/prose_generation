Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 10 of 18 ("Yükseklik: yükselten ad ve alçak hayat"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 10 (prose paragraphs numbered) =====
[¶39] Sure yükseklikle açılır. "Ad" kelimesinin س م و kökündeki asıl anlamı yükselmektir: {ar:أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى, tr:aslu ismin sumuvvun ve huve mine'l-uluvvi li-ennehû tenvîhun ve delâletun ale'l-ma'nâ, gloss:ismin aslı sümüvdür ve yücelikten gelir; çünkü bir şeyi anıp yükseltir ve anlamı gösterir, source:"س م و,B005"}. {ar:الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى, tr:el-ismu mâ yu'rafu bihî ẕâtu'ş-şey'i ve asluhû sumuvvun bihî rufia ẕikru'l-musemmâ, gloss:isim bir şeyin kendisinin tanındığı şeydir; aslı sümüvdür; adlandırılanın anılışı onunla yükselir, source:"س م و,B005"}. Kök, ufukta beliren bir karaltıyı da anlatır: {ar:سما لي شخص ارتفع حتى استثبته, tr:semâ lî şahsun irtefea hattâ'steŝbettuh, gloss:bir karaltı yükseldi de onu iyice seçtim, source:"س م و,B002"}. Ufuktan ayrılan hilali de anlatır: {ar:سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا, tr:semâvetu'l-hilâli şahsuhû iẕe'rtefea ani'l-ufuki şey'en, gloss:hilalin semâvesi ufuktan biraz yükseldiğinde görünen biçimidir, source:"س م و,B002"}. "En yüce" kelimesinin kökü aynı yükseklikle tanımlanır: {ar:أصل واحد يدل على السمو والارتفاع, tr:aslun vâhidun yedullu ale's-sumuvvi ve'l-irtifâ, gloss:yücelik ve yükseklik bildiren tek köktür, source:"ع ل و,B001"}. "Gel" demek olan تعال de bu köktendir: {ar:تعال أصله أن يدعى الإنسان إلى مكان مرتفع, tr:teâle asluhû en yud'a'l-insânu ilâ mekânin murtefi', gloss:teâlin aslı insanın yüksek bir yere çağrılmasıdır, source:"ع ل و,B006"}. On beşinci ayetteki "anmak" fiilinin kökü de şerefi taşır: {ar:الذكر العلاء والشرف, tr:eẕ-ẕikru'l-alâu ve'ş-şeref, gloss:zikir yücelik ve şereftir, source:"ذ ك ر,B007"}. Birinci ayetin "ad", "en yüce" ve on beşinci ayetin "andı" kelimeleri böylece aynı yöne, yukarıya bakar.

[¶40] Tesbih bu yükseltmenin içeriğini verir: {ar:التسبيح وهو تنزيه الله من كل سوء, tr:et-tesbîh ve huve tenzîhullâhi min kulli sû', gloss:tesbih Allah'ı her kötülükten uzak tutmaktır, source:"س ب ح,B002"}. Aynı kökte ihtişam da vardır: {ar:سبحات وجه ربنا يعني جلاله وعظمته ونوره, tr:subuhâtu vechi rabbinâ ya'nî celâlehû ve azametehû ve nûrah, gloss:Rabbimizin yüzünün subuhâtı celali azameti ve nurudur, source:"س ب ح,B003"}. Bu ifade on ikinci ayetteki "ateş"in kökü olan nur kelimesini içerir. On ikinci ayetteki الكبرى'nın kökü Allah'ı yüceltme sözünü verir: {ar:التكبير يقال لتعظيم الله تعالى بقولهم الله أكبر, tr:et-tekbîr yukâlu li-ta'zîmillâhi teâlâ bi-kavlihimullâhu ekber, gloss:tekbir Allah'ı "Allah en büyüktür" diyerek yüceltmektir, source:"ك ب ر,B009"}. Aynı kök sahiplenilen büyüklüğü de verir: {ar:الكبر العظمة وكذلك الكبرياء, tr:el-kibr el-azametu ve keẕâlike'l-kibriyâ, gloss:kibir büyüklüktür; kibriyâ da öyle, source:"ك ب ر,B006"}. Yüksekliğin kendisi de bozulabilir: {ar:علا ملك في الأرض أي طغى وتعظم, tr:alâ melikun fi'l-ardi ey tağâ ve teazzama, gloss:bir hükümdar yeryüzünde yükseldi yani azdı ve büyüklük tasladı, source:"ع ل و,B003"}. Öbür uçta on altıncı ayetin الدنيا'sı durur. Bu kelime alçak olan ve daha az değerli olandır: {ar:يعبر بالأدنى تارة عن الأصغر وتارة عن الأول وتارة عن الأقرب, tr:yuabbaru bi'l-ednâ târaten ani'l-asğari ve târaten ani'l-evveli ve târaten ani'l-akrab, gloss:ednâ bazen daha küçük olanı bazen ilk olanı bazen en yakın olanı anlatır, source:"د ن و,B002"}. {ar:الدني من الرجال الضعيف الدون, tr:ed-deniyyu mine'r-ricâl ed-daîfu'd-dûn, gloss:insanların denîsi zayıf ve aşağı olandır, source:"د ن و,B003"}.

[¶41] Surenin iki ucunda bu iki kelime durur. Birinci ayet "en yüce" ile başlar, on altıncı ayet "en alçak" ya da "en yakın" olanla bir seçimi gösterir. Düz bir anlatımda bunlar yalnızca iki sıfattır. Kök aileleri ise onları bir eksenin iki ucu olarak duyurur. Adı anılan Rab yükseltilir. Tercih edilen hayat ise adı gereği alçak ve yakındır.

[¶42] Kur'an bu ekseni bir sahnede kurar. Musa'nın hikâyesini anlatan bölümde Firavun halkını toplayıp şöyle seslenir: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe-kâle ene rabbukumu'l-a'lâ, gloss:ben sizin en yüce rabbinizim dedi, source:79:24}. Bu, birinci ayetin iki kelimesinin bir yaratık tarafından sahiplenilmesidir, ve "yeryüzünde yükselip azmak" anlamının kendisidir. Aynı surede birkaç ayet sonra hüküm verilir: {ar:فَأَمَّا مَن طَغَىٰ, tr:fe-emmâ men tağâ, gloss:azana gelince, source:79:37}, {ar:وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:ve âŝera'l-hayâte'd-dunyâ, gloss:ve dünya hayatını tercih edene, source:79:38}. Yüksekliği sahiplenen ile yakın hayatı tercih eden aynı kişidir. Musa sihirbazlarla karşılaştığında içinde bir korku duyar ve Allah ona şöyle der: {ar:قُلْنَا لَا تَخَفْ إِنَّكَ أَنتَ ٱلْأَعْلَىٰ, tr:kulnâ lâ tehaf inneke ente'l-a'lâ, gloss:korkma; üstün olan sensin dedik, source:20:68}. Aynı sahnede iman eden sihirbazlar kendilerine {ar:فَأُو۟لَٰٓئِكَ لَهُمُ ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:fe-ulâike lehumu'd-derecâtu'l-ulâ, gloss:işte onlar için en yüce dereceler vardır, source:20:75} denir. Gökler için de {ar:تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى, tr:tenzîlen mimmen halaka'l-arda ve's-semâvâti'l-ulâ, gloss:yeri ve yüce gökleri yaratandan indirilmiştir, source:20:4} denir. Vahyin getiricisi için {ar:ذُو مِرَّةٍۢ فَٱسْتَوَىٰ, tr:ẕû mirretin fe'stevâ, gloss:güç sahibidir; doğrulup durdu, source:53:6} ve {ar:وَهُوَ بِٱلْأُفُقِ ٱلْأَعْلَىٰ, tr:ve huve bi'l-ufuki'l-a'lâ, gloss:o en yüksek ufuktaydı, source:53:7} denir. Ufukta yükselen bir karaltı, kökün kendi sahnesidir. Malını verip arınan kişinin amacı da şöyle anlatılır: {ar:إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ, tr:ille'btiğâe vechi rabbihi'l-a'lâ, gloss:yalnızca en yüce Rabbinin rızasını istemek için, source:92:20}. Adın yükseltilmesi bir mekânda da anlatılır: {ar:فِى بُيُوتٍ أَذِنَ ٱللَّهُ أَن تُرْفَعَ وَيُذْكَرَ فِيهَا ٱسْمُهُۥ يُسَبِّحُ لَهُۥ فِيهَا, tr:fî buyûtin eẕinallâhu en turfea ve yuẕkera fîhe'smuhû yusebbihu lehû fîhâ, gloss:Allah'ın yükseltilmesine ve içlerinde adının anılmasına izin verdiği evlerde onu tesbih ederler, source:24:36}. Bu tek ayet surenin birinci ve on beşinci ayetlerini, yani yükseltmeyi, adı, anmayı ve tesbihi bir arada tutar. Peygamber'e de {ar:وَرَفَعْنَا لَكَ ذِكْرَكَ, tr:ve rafa'nâ leke ẕikrak, gloss:senin anılışını yükselttik, source:94:4} denir. Allah'ın kendisi için ise {ar:فَتَعَٰلَى ٱللَّهُ ٱلْمَلِكُ ٱلْحَقُّ, tr:fe-teâlallâhu'l-meliku'l-hakk, gloss:gerçek hükümdar olan Allah yücedir, source:20:114} denir. Birinci ayetteki emrin bir benzeri başka bir yerde de geçer: {ar:فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ, tr:fe-sebbih bi'smi rabbike'l-azîm, gloss:büyük Rabbinin adıyla tesbih et, source:56:74}. Bir başka emir de okumayı, adı, Rabbi ve yaratmayı birleştirir: {ar:ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ, tr:ikra' bi'smi rabbike'lleẕî halak, gloss:yaratan Rabbinin adıyla oku, source:96:1}. Bu emirde surenin birinci, ikinci ve altıncı ayetlerinin kelimeleri bir aradadır.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (321) =====
## strong (217)

- (2:31) [terra: strong; basis: root+theme] وَعَلَّمَ ءَادَمَ ٱلْأَسْمَآءَ كُلَّهَا ثُمَّ عَرَضَهُمْ عَلَى ٱلْمَلَٰٓئِكَةِ فَقَالَ أَنۢبِـُٔونِى بِأَسْمَآءِ هَٰٓؤُلَآءِ إِن كُنتُمْ صَٰدِقِينَ
  Unverified discovery rationale: terra: God teaches Adam ٱلْأَسْمَآءَ كُلَّهَا; names make the created things knowable, directly illustrating the dictionary account of a name as what identifies an essence.
- (2:33) [terra: strong; basis: neighbour+root+theme] قَالَ يَٰٓـَٔادَمُ أَنۢبِئْهُم بِأَسْمَآئِهِمْ ۖ فَلَمَّآ أَنۢبَأَهُم بِأَسْمَآئِهِمْ قَالَ أَلَمْ أَقُل لَّكُمْ إِنِّىٓ أَعْلَمُ غَيْبَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَأَعْلَمُ مَا تُبْدُونَ وَمَا كُنتُمْ تَكْتُمُونَ
  Unverified discovery rationale: terra: Adam discloses the beings' names while God declares knowledge of the heavens' and earth's unseen, linking naming as disclosure to what remains hidden.
- (2:61) [luna: strong (missing-ayat turn); terra: contrast (missing-ayat turn); basis: contrast+root+theme] وَإِذْ قُلْتُمْ يَٰمُوسَىٰ لَن نَّصْبِرَ عَلَىٰ طَعَامٍۢ وَٰحِدٍۢ فَٱدْعُ لَنَا رَبَّكَ يُخْرِجْ لَنَا مِمَّا تُنۢبِتُ ٱلْأَرْضُ مِنۢ بَقْلِهَا وَقِثَّآئِهَا وَفُومِهَا وَعَدَسِهَا وَبَصَلِهَا ۖ قَالَ أَتَسْتَبْدِلُونَ ٱلَّذِى هُوَ أَدْنَىٰ بِٱلَّذِى هُوَ خَيْرٌ ۚ ٱهْبِطُوا۟ مِصْرًۭا فَإِنَّ لَكُم مَّا سَأَلْتُمْ ۗ وَضُرِبَتْ عَلَيْهِمُ ٱلذِّلَّةُ وَٱلْمَسْكَنَةُ وَبَآءُو بِغَضَبٍۢ مِّنَ ٱللَّهِ ۗ ذَٰلِكَ بِأَنَّهُمْ كَانُوا۟ يَكْفُرُونَ بِـَٔايَٰتِ ٱللَّهِ وَيَقْتُلُونَ ٱلنَّبِيِّۦنَ بِغَيْرِ ٱلْحَقِّ ۗ ذَٰلِكَ بِمَا عَصَوا۟ وَّكَانُوا۟ يَعْتَدُونَ
  Unverified discovery rationale: luna: The section’s d-n-w gloss includes what is low or lesser, and its central choice is the lower life over the better Hereafter; this verse uses “أدنى” for the inferior thing chosen in place of what is better, a concrete but worldly-food instance of that lower-for-better exchange. | terra: Moses asks whether the people would exchange what is lower for what is better, directly stating the value contrast carried by the section's discussion of أدنى.
- (2:152) [terra: strong (missing-ayat turn); basis: root+speaker] فَٱذْكُرُونِىٓ أَذْكُرْكُمْ وَٱشْكُرُوا۟ لِى وَلَا تَكْفُرُونِ
  Unverified discovery rationale: terra: “Remember Me and I will remember you” makes remembrance reciprocal divine acknowledgment rather than a mere utterance, supporting dhikr's honor-bearing sense.
- (2:185) [terra: strong; basis: root+theme] شَهْرُ رَمَضَانَ ٱلَّذِىٓ أُنزِلَ فِيهِ ٱلْقُرْءَانُ هُدًۭى لِّلنَّاسِ وَبَيِّنَٰتٍۢ مِّنَ ٱلْهُدَىٰ وَٱلْفُرْقَانِ ۚ فَمَن شَهِدَ مِنكُمُ ٱلشَّهْرَ فَلْيَصُمْهُ ۖ وَمَن كَانَ مَرِيضًا أَوْ عَلَىٰ سَفَرٍۢ فَعِدَّةٌۭ مِّنْ أَيَّامٍ أُخَرَ ۗ يُرِيدُ ٱللَّهُ بِكُمُ ٱلْيُسْرَ وَلَا يُرِيدُ بِكُمُ ٱلْعُسْرَ وَلِتُكْمِلُوا۟ ٱلْعِدَّةَ وَلِتُكَبِّرُوا۟ ٱللَّهَ عَلَىٰ مَا هَدَىٰكُمْ وَلَعَلَّكُمْ تَشْكُرُونَ
  Unverified discovery rationale: terra: وَلِتُكَبِّرُوا۟ ٱللَّهَ عَلَىٰ مَا هَدَىٰكُمْ makes magnifying God the response to His guidance, joining the section's greatness-language to the guidance of 87:3.
- (2:189) [luna: strong; terra: weak; basis: root+scene] ۞ يَسْـَٔلُونَكَ عَنِ ٱلْأَهِلَّةِ ۖ قُلْ هِىَ مَوَٰقِيتُ لِلنَّاسِ وَٱلْحَجِّ ۗ وَلَيْسَ ٱلْبِرُّ بِأَن تَأْتُوا۟ ٱلْبُيُوتَ مِن ظُهُورِهَا وَلَٰكِنَّ ٱلْبِرَّ مَنِ ٱتَّقَىٰ ۗ وَأْتُوا۟ ٱلْبُيُوتَ مِنْ أَبْوَٰبِهَا ۚ وَٱتَّقُوا۟ ٱللَّهَ لَعَلَّكُمْ تُفْلِحُونَ
  Unverified discovery rationale: luna: The section’s s-m-w dictionary branch calls the crescent’s visible form “سماوة الهلال” when it rises a little above the horizon; this verse asks about the new moons and identifies them as visible time-markers. | terra: The ayah treats crescent forms as time-signs; it activates the section's dictionary picture of the hilal becoming distinct above the horizon, though the ayah itself does not describe its rising.
- (2:201) [terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] وَمِنْهُم مَّن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ حَسَنَةًۭ وَقِنَا عَذَابَ ٱلنَّارِ
  Unverified discovery rationale: terra: The balanced prayer asks for good in both this world and the hereafter and protection from Fire, correcting the one-horizon request in 2:200.
- (2:253) [terra: strong (missing-ayat turn); basis: root+theme] ۞ تِلْكَ ٱلرُّسُلُ فَضَّلْنَا بَعْضَهُمْ عَلَىٰ بَعْضٍۢ ۘ مِّنْهُم مَّن كَلَّمَ ٱللَّهُ ۖ وَرَفَعَ بَعْضَهُمْ دَرَجَٰتٍۢ ۚ وَءَاتَيْنَا عِيسَى ٱبْنَ مَرْيَمَ ٱلْبَيِّنَٰتِ وَأَيَّدْنَٰهُ بِرُوحِ ٱلْقُدُسِ ۗ وَلَوْ شَآءَ ٱللَّهُ مَا ٱقْتَتَلَ ٱلَّذِينَ مِنۢ بَعْدِهِم مِّنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَٰتُ وَلَٰكِنِ ٱخْتَلَفُوا۟ فَمِنْهُم مَّنْ ءَامَنَ وَمِنْهُم مَّن كَفَرَ ۚ وَلَوْ شَآءَ ٱللَّهُ مَا ٱقْتَتَلُوا۟ وَلَٰكِنَّ ٱللَّهَ يَفْعَلُ مَا يُرِيدُ
  Unverified discovery rationale: terra: God favors some messengers over others and raises some in degrees, presenting rank as His grant even among honored servants.
- (2:255) [luna: medium; terra: strong; basis: root+theme] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْحَىُّ ٱلْقَيُّومُ ۚ لَا تَأْخُذُهُۥ سِنَةٌۭ وَلَا نَوْمٌۭ ۚ لَّهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ مَن ذَا ٱلَّذِى يَشْفَعُ عِندَهُۥٓ إِلَّا بِإِذْنِهِۦ ۚ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ وَلَا يُحِيطُونَ بِشَىْءٍۢ مِّنْ عِلْمِهِۦٓ إِلَّا بِمَا شَآءَ ۚ وَسِعَ كُرْسِيُّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ ۖ وَلَا يَـُٔودُهُۥ حِفْظُهُمَا ۚ وَهُوَ ٱلْعَلِىُّ ٱلْعَظِيمُ
  Unverified discovery rationale: luna: The section’s al-ʿulūw axis belongs to the Lord; this verse closes by naming God “العلي العظيم,” coupling divine highness and greatness rather than a ruler’s self-claim. | terra: The Throne encompasses heavens and earth and God is ٱلْعَلِىُّ ٱلْعَظِيمُ; cosmic rule joins true elevation to magnificence.
- (3:14) [luna: strong; terra: contrast (missing-ayat turn); basis: contrast+root+theme] زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ مِنَ ٱلنِّسَآءِ وَٱلْبَنِينَ وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ مِنَ ٱلذَّهَبِ وَٱلْفِضَّةِ وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ ۗ ذَٰلِكَ مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلْمَـَٔابِ
  Unverified discovery rationale: luna: The section presents the worldly life as a preferred, lesser good; this verse names the attractions that beautify it, calls them worldly enjoyment, and contrasts them with the good return with God. | terra: Desired possessions are presented as the adornment of worldly life, while the beautiful return is with God; attraction and destination are placed on different levels.
- (3:15) [terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] ۞ قُلْ أَؤُنَبِّئُكُم بِخَيْرٍۢ مِّن ذَٰلِكُمْ ۚ لِلَّذِينَ ٱتَّقَوْا۟ عِندَ رَبِّهِمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا وَأَزْوَٰجٌۭ مُّطَهَّرَةٌۭ وَرِضْوَٰنٌۭ مِّنَ ٱللَّهِ ۗ وَٱللَّهُ بَصِيرٌۢ بِٱلْعِبَادِ
  Unverified discovery rationale: terra: The Prophet is told to announce what is better than worldly adornment: lasting gardens, purified spouses, and God's approval.
- (3:26) [terra: strong; basis: contrast+theme] قُلِ ٱللَّهُمَّ مَٰلِكَ ٱلْمُلْكِ تُؤْتِى ٱلْمُلْكَ مَن تَشَآءُ وَتَنزِعُ ٱلْمُلْكَ مِمَّن تَشَآءُ وَتُعِزُّ مَن تَشَآءُ وَتُذِلُّ مَن تَشَآءُ ۖ بِيَدِكَ ٱلْخَيْرُ ۖ إِنَّكَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: terra: God gives and removes rule and grants honor or humiliation as He wills; the two-direction movement denies rulers ownership of their height.
- (3:41) [terra: strong; basis: root+speaker] قَالَ رَبِّ ٱجْعَل لِّىٓ ءَايَةًۭ ۖ قَالَ ءَايَتُكَ أَلَّا تُكَلِّمَ ٱلنَّاسَ ثَلَٰثَةَ أَيَّامٍ إِلَّا رَمْزًۭا ۗ وَٱذْكُر رَّبَّكَ كَثِيرًۭا وَسَبِّحْ بِٱلْعَشِىِّ وَٱلْإِبْكَٰرِ
  Unverified discovery rationale: terra: Remembering the Lord much and glorifying Him morning and evening places dhikr and tasbih in one divine instruction.
- (3:55) [terra: strong (missing-ayat turn); basis: root+theme] إِذْ قَالَ ٱللَّهُ يَٰعِيسَىٰٓ إِنِّى مُتَوَفِّيكَ وَرَافِعُكَ إِلَىَّ وَمُطَهِّرُكَ مِنَ ٱلَّذِينَ كَفَرُوا۟ وَجَاعِلُ ٱلَّذِينَ ٱتَّبَعُوكَ فَوْقَ ٱلَّذِينَ كَفَرُوٓا۟ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ ۖ ثُمَّ إِلَىَّ مَرْجِعُكُمْ فَأَحْكُمُ بَيْنَكُمْ فِيمَا كُنتُمْ فِيهِ تَخْتَلِفُونَ
  Unverified discovery rationale: terra: God tells Jesus that He will raise him to Himself and purify him from the disbelievers, joining elevation to divine action and purification.
- (3:64) [luna: medium; terra: strong; basis: root+speaker+theme] قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ تَعَالَوْا۟ إِلَىٰ كَلِمَةٍۢ سَوَآءٍۭ بَيْنَنَا وَبَيْنَكُمْ أَلَّا نَعْبُدَ إِلَّا ٱللَّهَ وَلَا نُشْرِكَ بِهِۦ شَيْـًۭٔا وَلَا يَتَّخِذَ بَعْضُنَا بَعْضًا أَرْبَابًۭا مِّن دُونِ ٱللَّهِ ۚ فَإِن تَوَلَّوْا۟ فَقُولُوا۟ ٱشْهَدُوا۟ بِأَنَّا مُسْلِمُونَ
