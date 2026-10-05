Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 17 of 18 ("Sunulan öğüt: korkanın aldığı, bedbahtın yanından geçtiği"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 17 (prose paragraphs numbered) =====
[¶65] Dokuzuncu ve on birinci ayet arasında bir öğüt sunulur, biri onu alır, biri onun yanından geçer: {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-ẕekkir in nefeati'ẕ-ẕikrâ, gloss:öğüt ver; eğer öğüt fayda verirse, source:87:9}, {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yeẕẕekkeru men yahşâ, gloss:içi titreyen öğüt alacaktır, source:87:10}, {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht ise ondan uzak duracaktır, source:87:11}. Öğüt, başkasına yönelen bir hatırlatmadır: {ar:الذكرى اسم للتذكير والتذكير مجاوز, tr:eẕ-ẕikrâ ismun li't-teẕkîr ve't-teẕkîru mucâviz, gloss:zikrâ hatırlatmanın adıdır ve hatırlatma başkasına geçen bir iştir, source:"ذ ك ر,B009"}. Fayda zararın zıddıdır: {ar:النفع ضد الضر, tr:en-nef'u diddu'd-darr, gloss:fayda zararın zıddıdır, source:"ن ف ع,B001"}. Onuncu ayetteki korku bilgiden doğar: {ar:الخشية خوف يشوبه تعظيم وأكثر ما يكون ذلك عن علم, tr:el-haşye havfun yeşûbuhû ta'zîmun ve ekŝeru mâ yekûnu ẕâlike an ilm, gloss:haşyet içine saygı karışmış bir korkudur ve çoğunlukla bilgiden doğar, source:"خ ش ي,B001"}. Bu tanım yedinci ayetteki "bilir" fiilinin kökünü içerir. Aynı fiil "bildim" anlamında da kullanılır: {ar:خشيت بأن من تبع الهدى معناه علمت, tr:haşîtu bi-enne men tebia'l-hudâ ma'nâhu alimtu, gloss:yol göstermeyi izleyenin hakkında haşîtu bildim anlamındadır, source:"خ ش ي,B002"}. Bu ifadede üçüncü ayetteki "yol gösterdi" fiilinin kökü de geçer. On birinci ayetteki kök uzaklıktır: {ar:الأصل الآخر البعد والجنابة, tr:el-aslu'l-âhar el-bu'du ve'l-cenâbe, gloss:öbür kök anlamı uzaklıktır, source:"ج ن ب,B003"}. Bu kök bir durumu da adlandırır: {ar:الجنب الذي يجامع أهله مشتق من هذا لأنه يبعد عن الصلاة والمسجد, tr:el-cunubu'lleẕî yucâmiu ehlehû muştakkun min hâẕâ li-ennehû yeb'udu ani's-salâti ve'l-mescid, gloss:cünüp bu kökten türemiştir çünkü namazdan ve mescitten uzak kalır, source:"ج ن ب,B004"}. Bedbahtlık da mutluluğun zıddıdır: {ar:الشقوة خلاف السعادة, tr:eş-şikve hilâfu's-seâde, gloss:şikve mutluluğun zıddıdır, source:"ش ق و,B001"}.

[¶66] Düz bir anlatım bu üç ayeti "bazıları kabul eder, bazıları reddeder" diye özetler. Kök aileleri iki tutumun işleyişini gösterir. Korku bilgiden gelir ve öğüdü alır. Bedbaht ise öğüde karşı çıkmaz, onu kendi yanında, uzakta tutar. Aynı kökün namazdan ve mescitten uzak kalmayı da adlandırması, bu uzak durmanın on beşinci ayetteki namazın da uzağında kalmak olduğunu duyurur. Bu son bağ dilin bir yankısıdır, ayetin kendi sözü değildir.

[¶67] Kur'an bu sahneyi Peygamber'in kendi durumu üzerinden kurar. Peygamber yüzünü ekşitip döner, çünkü yanına gözleri görmeyen bir adam gelmiştir. Ona şöyle denir: {ar:وَمَا يُدْرِيكَ لَعَلَّهُۥ يَزَّكَّىٰٓ, tr:ve mâ yudrîke leallehû yezzekkâ, gloss:ne bilirsin belki o arınacak, source:80:3}, {ar:أَوْ يَذَّكَّرُ فَتَنفَعَهُ ٱلذِّكْرَىٰٓ, tr:ev yeẕẕekkeru fe-tenfeahu'ẕ-ẕikrâ, gloss:ya da öğüt alacak da öğüt ona fayda verecek, source:80:4}. Adam için {ar:وَهُوَ يَخْشَىٰ, tr:ve huve yahşâ, gloss:o içi titreyerek gelmiştir, source:80:9} denir. Peygamber'e ise {ar:فَأَنتَ عَنْهُ تَلَهَّىٰ, tr:fe-ente anhu telehhâ, gloss:sen ise onunla ilgilenmiyorsun, source:80:10} denir. Bu birkaç ayette surenin dokuzuncu, onuncu ve on dördüncü ayetlerinin kelimeleri bir arada bulunur. Öğüdün faydası da şöyle söylenir: {ar:وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ, tr:ve ẕekkir fe-inne'ẕ-ẕikrâ tenfeu'l-mu'minîn, gloss:öğüt ver; çünkü öğüt müminlere fayda verir, source:51:55}. Öğütçünün sınırı da: {ar:فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ, tr:fe-ẕekkir innemâ ente muẕekkir, gloss:öğüt ver; sen yalnızca bir öğütçüsün, source:88:21}. Kime öğüt verileceği de: {ar:فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ, tr:fe-ẕekkir bi'l-kur'âni men yehâfu vaîd, gloss:tehdidimden korkana Kur'an ile öğüt ver, source:50:45}. Peygamber'e indirilen hitabın başı surenin dokuzuncu, onuncu ve on birinci ayetlerini birlikte verir: {ar:إِلَّا تَذْكِرَةًۭ لِّمَن يَخْشَىٰ, tr:illâ teẕkiraten li-men yahşâ, gloss:ancak içi titreyen için bir öğüt olarak indirdik, source:20:3}. Bu ayetten hemen önce ise Kur'an'ın Peygamber'in zahmet çekmesi için indirilmediği söylenir. Allah Musa ile Harun'u Firavun'a gönderirken {ar:فَقُولَا لَهُۥ قَوْلًۭا لَّيِّنًۭا لَّعَلَّهُۥ يَتَذَكَّرُ أَوْ يَخْشَىٰ, tr:fe-kûlâ lehû kavlen leyyinen leallehû yeteẕekkeru ev yahşâ, gloss:ona yumuşak bir söz söyleyin; belki öğüt alır ya da korkar, source:20:44} der. Başka bir anlatımda Musa'ya Firavun'a şöyle demesi söylenir: {ar:فَقُلْ هَل لَّكَ إِلَىٰٓ أَن تَزَكَّىٰ, tr:fe-kul hel leke ilâ en tezekkâ, gloss:arınmaya niyetin var mı de, source:79:18}, {ar:وَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ, tr:ve ehdiyeke ilâ rabbike fe-tahşâ, gloss:seni Rabbine götüreyim de içini bir korku kaplasın, source:79:19}. Firavun'a sunulan öğüt, arınma, yol gösterme ve korkuyu birlikte içerir. Firavun ise bu öğüdü reddeder. Bilgi ile korku arasındaki bağı Kur'an şöyle söyler: {ar:إِنَّمَا يَخْشَى ٱللَّهَ مِنْ عِبَادِهِ ٱلْعُلَمَٰٓؤُا۟, tr:innemâ yahşallâhe min ibâdihi'l-ulemâ, gloss:kulları içinde Allah'tan ancak bilenler korkar, source:35:28}. Uyarının kime yaradığını da söyler: {ar:إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ ۚ وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ, tr:innemâ tunẕiru'lleẕîne yahşevne rabbehum bi'l-ğaybi ve ekâmu's-salâh ve men tezekkâ fe-innemâ yetezekkâ li-nefsih, gloss:sen ancak Rablerinden görmeden korkan ve namazı kılanları uyarırsın; arınan kendisi için arınır, source:35:18}. Bu ayet surenin onuncu, on dördüncü ve on beşinci ayetlerini tek bir cümlede verir. Öğütten uzak durmanın sonucu da anlatılır: {ar:وَمَنْ أَعْرَضَ عَن ذِكْرِى فَإِنَّ لَهُۥ مَعِيشَةًۭ ضَنكًۭا, tr:ve men a'rada an ẕikrî fe-inne lehû maîşeten danka, gloss:kim beni anmaktan yüz çevirirse onun dar bir geçimi olur, source:20:124}. Bir başka yerde öğütten yüz çeviren {ar:إِلَّا مَن تَوَلَّىٰ وَكَفَرَ, tr:illâ men tevellâ ve kefer, gloss:yüz çevirip inkâr eden müstesna, source:88:23} diye anılır ve en büyük azaba çarptırılır.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (370) =====
## strong (268)

- (2:6) [terra: strong; basis: contrast+scene+theme] إِنَّ ٱلَّذِينَ كَفَرُوا۟ سَوَآءٌ عَلَيْهِمْ ءَأَنذَرْتَهُمْ أَمْ لَمْ تُنذِرْهُمْ لَا يُؤْمِنُونَ
  Unverified discovery rationale: terra: For entrenched disbelievers it is equal whether the Prophet warns or does not warn: they will not believe, a stark limit on benefit without cancelling his address.
- (2:102) [terra: strong (missing-ayat turn); basis: contrast+root+theme] وَٱتَّبَعُوا۟ مَا تَتْلُوا۟ ٱلشَّيَٰطِينُ عَلَىٰ مُلْكِ سُلَيْمَٰنَ ۖ وَمَا كَفَرَ سُلَيْمَٰنُ وَلَٰكِنَّ ٱلشَّيَٰطِينَ كَفَرُوا۟ يُعَلِّمُونَ ٱلنَّاسَ ٱلسِّحْرَ وَمَآ أُنزِلَ عَلَى ٱلْمَلَكَيْنِ بِبَابِلَ هَٰرُوتَ وَمَٰرُوتَ ۚ وَمَا يُعَلِّمَانِ مِنْ أَحَدٍ حَتَّىٰ يَقُولَآ إِنَّمَا نَحْنُ فِتْنَةٌۭ فَلَا تَكْفُرْ ۖ فَيَتَعَلَّمُونَ مِنْهُمَا مَا يُفَرِّقُونَ بِهِۦ بَيْنَ ٱلْمَرْءِ وَزَوْجِهِۦ ۚ وَمَا هُم بِضَآرِّينَ بِهِۦ مِنْ أَحَدٍ إِلَّا بِإِذْنِ ٱللَّهِ ۚ وَيَتَعَلَّمُونَ مَا يَضُرُّهُمْ وَلَا يَنفَعُهُمْ ۚ وَلَقَدْ عَلِمُوا۟ لَمَنِ ٱشْتَرَىٰهُ مَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ ۚ وَلَبِئْسَ مَا شَرَوْا۟ بِهِۦٓ أَنفُسَهُمْ ۚ لَوْ كَانُوا۟ يَعْلَمُونَ
  Unverified discovery rationale: terra: People learn from magic what harms them and does not benefit them, a reversal in which acquired knowledge yields harm rather than the fear and benefit of reminder.
- (2:206) [luna: strong; terra: strong; basis: contrast+scene+theme] وَإِذَا قِيلَ لَهُ ٱتَّقِ ٱللَّهَ أَخَذَتْهُ ٱلْعِزَّةُ بِٱلْإِثْمِ ۚ فَحَسْبُهُۥ جَهَنَّمُ ۚ وَلَبِئْسَ ٱلْمِهَادُ
  Unverified discovery rationale: luna: When told اِتَّقِ اللَّهَ, the hearer grows proud and sins; this is a specific rejection of admonition to fear, ending in Hell. | terra: When told “fear God,” pride carries the hearer further into sin and Hell suffices him; the offered call to fear produces the wretched response instead.
- (2:275) [terra: strong; basis: root+scene+theme] ٱلَّذِينَ يَأْكُلُونَ ٱلرِّبَوٰا۟ لَا يَقُومُونَ إِلَّا كَمَا يَقُومُ ٱلَّذِى يَتَخَبَّطُهُ ٱلشَّيْطَٰنُ مِنَ ٱلْمَسِّ ۚ ذَٰلِكَ بِأَنَّهُمْ قَالُوٓا۟ إِنَّمَا ٱلْبَيْعُ مِثْلُ ٱلرِّبَوٰا۟ ۗ وَأَحَلَّ ٱللَّهُ ٱلْبَيْعَ وَحَرَّمَ ٱلرِّبَوٰا۟ ۚ فَمَن جَآءَهُۥ مَوْعِظَةٌۭ مِّن رَّبِّهِۦ فَٱنتَهَىٰ فَلَهُۥ مَا سَلَفَ وَأَمْرُهُۥٓ إِلَى ٱللَّهِ ۖ وَمَنْ عَادَ فَأُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ ۖ هُمْ فِيهَا خَٰلِدُونَ
  Unverified discovery rationale: terra: Whoever receives an admonition from his Lord and desists may keep what is past, showing a reminder's benefit as an actual change of conduct.
- (3:138) [terra: strong; basis: root+theme] هَٰذَا بَيَانٌۭ لِّلنَّاسِ وَهُدًۭى وَمَوْعِظَةٌۭ لِّلْمُتَّقِينَ
  Unverified discovery rationale: terra: The revelation is guidance and admonition for the God-conscious, identifying receptive character rather than bare exposure as the ground of benefit.
- (4:43) [luna: strong; terra: strong; basis: root+scene] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تَقْرَبُوا۟ ٱلصَّلَوٰةَ وَأَنتُمْ سُكَٰرَىٰ حَتَّىٰ تَعْلَمُوا۟ مَا تَقُولُونَ وَلَا جُنُبًا إِلَّا عَابِرِى سَبِيلٍ حَتَّىٰ تَغْتَسِلُوا۟ ۚ وَإِن كُنتُم مَّرْضَىٰٓ أَوْ عَلَىٰ سَفَرٍ أَوْ جَآءَ أَحَدٌۭ مِّنكُم مِّنَ ٱلْغَآئِطِ أَوْ لَٰمَسْتُمُ ٱلنِّسَآءَ فَلَمْ تَجِدُوا۟ مَآءًۭ فَتَيَمَّمُوا۟ صَعِيدًۭا طَيِّبًۭا فَٱمْسَحُوا۟ بِوُجُوهِكُمْ وَأَيْدِيكُمْ ۗ إِنَّ ٱللَّهَ كَانَ عَفُوًّا غَفُورًا
  Unverified discovery rationale: luna: The source explicitly gives junub as a state derived from ج ن ب because one stays away from prayer; this ayah uses جُنُبًا and restricts approach to prayer until purification. | terra: The Quranic جُنُبًا is barred from approaching prayer until purification, the exact secondary dictionary sense used by the section to hear distance from prayer in يَتَجَنَّبُهَا.
- (4:63) [terra: strong; basis: root+speaker+theme] أُو۟لَٰٓئِكَ ٱلَّذِينَ يَعْلَمُ ٱللَّهُ مَا فِى قُلُوبِهِمْ فَأَعْرِضْ عَنْهُمْ وَعِظْهُمْ وَقُل لَّهُمْ فِىٓ أَنفُسِهِمْ قَوْلًۢا بَلِيغًۭا
  Unverified discovery rationale: terra: The Prophet must turn from the hypocrites yet admonish them and speak a word that reaches deeply into themselves, a Quranic realization of reminder as an act passing to another.
- (5:6) [luna: medium; terra: strong; basis: root+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا قُمْتُمْ إِلَى ٱلصَّلَوٰةِ فَٱغْسِلُوا۟ وُجُوهَكُمْ وَأَيْدِيَكُمْ إِلَى ٱلْمَرَافِقِ وَٱمْسَحُوا۟ بِرُءُوسِكُمْ وَأَرْجُلَكُمْ إِلَى ٱلْكَعْبَيْنِ ۚ وَإِن كُنتُمْ جُنُبًۭا فَٱطَّهَّرُوا۟ ۚ وَإِن كُنتُم مَّرْضَىٰٓ أَوْ عَلَىٰ سَفَرٍ أَوْ جَآءَ أَحَدٌۭ مِّنكُم مِّنَ ٱلْغَآئِطِ أَوْ لَٰمَسْتُمُ ٱلنِّسَآءَ فَلَمْ تَجِدُوا۟ مَآءًۭ فَتَيَمَّمُوا۟ صَعِيدًۭا طَيِّبًۭا فَٱمْسَحُوا۟ بِوُجُوهِكُمْ وَأَيْدِيكُم مِّنْهُ ۚ مَا يُرِيدُ ٱللَّهُ لِيَجْعَلَ عَلَيْكُم مِّنْ حَرَجٍۢ وَلَٰكِن يُرِيدُ لِيُطَهِّرَكُمْ وَلِيُتِمَّ نِعْمَتَهُۥ عَلَيْكُمْ لَعَلَّكُمْ تَشْكُرُونَ
  Unverified discovery rationale: luna: The source's dictionary form junub is used for a state requiring purification here; the ritual cleansing offers a concrete lexical echo of the source's link to prayer. | terra: The instruction وَإِن كُنتُمْ جُنُبًا فَٱطَّهَّرُوا۟ joins the named secondary root sense to purification before prayer, clarifying that this distance has a prescribed end.
- (5:83) [terra: strong; basis: scene+theme] وَإِذَا سَمِعُوا۟ مَآ أُنزِلَ إِلَى ٱلرَّسُولِ تَرَىٰٓ أَعْيُنَهُمْ تَفِيضُ مِنَ ٱلدَّمْعِ مِمَّا عَرَفُوا۟ مِنَ ٱلْحَقِّ ۖ يَقُولُونَ رَبَّنَآ ءَامَنَّا فَٱكْتُبْنَا مَعَ ٱلشَّٰهِدِينَ
  Unverified discovery rationale: terra: Those who recognize the truth in what reaches the Messenger overflow with tears and confess belief, another concrete passage from knowledge to receptive awe.
- (6:51) [luna: strong; terra: strong; basis: scene+speaker+theme] وَأَنذِرْ بِهِ ٱلَّذِينَ يَخَافُونَ أَن يُحْشَرُوٓا۟ إِلَىٰ رَبِّهِمْ ۙ لَيْسَ لَهُم مِّن دُونِهِۦ وَلِىٌّۭ وَلَا شَفِيعٌۭ لَّعَلَّهُمْ يَتَّقُونَ
  Unverified discovery rationale: luna: The Prophet is told to warn those who fear being gathered to their Lord, directly matching the source's fearful audience. | terra: The Prophet is told to warn by the Quran those who fear being gathered to their Lord, another direct restriction of effective warning to a fearful audience.
- (6:52) [luna: strong; basis: contrast+scene] وَلَا تَطْرُدِ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ مَا عَلَيْكَ مِنْ حِسَابِهِم مِّن شَىْءٍۢ وَمَا مِنْ حِسَابِكَ عَلَيْهِم مِّن شَىْءٍۢ فَتَطْرُدَهُمْ فَتَكُونَ مِنَ ٱلظَّٰلِمِينَ
  Unverified discovery rationale: luna: He must not drive away those who call on their Lord morning and evening; this echoes the blind, seeking visitor in 80 and the source's received reminder.
- (6:53) [luna: strong; basis: contrast+neighbour] وَكَذَٰلِكَ فَتَنَّا بَعْضَهُم بِبَعْضٍۢ لِّيَقُولُوٓا۟ أَهَٰٓؤُلَآءِ مَنَّ ٱللَّهُ عَلَيْهِم مِّنۢ بَيْنِنَآ ۗ أَلَيْسَ ٱللَّهُ بِأَعْلَمَ بِٱلشَّٰكِرِينَ
  Unverified discovery rationale: luna: The disbelievers question the worth of the humble believers in 6:52; this completes the status contrast that the source's 80 scene exposes.
- (6:68) [luna: strong; basis: contrast+scene] وَإِذَا رَأَيْتَ ٱلَّذِينَ يَخُوضُونَ فِىٓ ءَايَٰتِنَا فَأَعْرِضْ عَنْهُمْ حَتَّىٰ يَخُوضُوا۟ فِى حَدِيثٍ غَيْرِهِۦ ۚ وَإِمَّا يُنسِيَنَّكَ ٱلشَّيْطَٰنُ فَلَا تَقْعُدْ بَعْدَ ٱلذِّكْرَىٰ مَعَ ٱلْقَوْمِ ٱلظَّٰلِمِينَ
  Unverified discovery rationale: luna: When people mock God's signs, the Prophet must turn away until they change the subject; this is a concrete scene of disengaging from reminder.
- (6:69) [terra: strong; basis: root+theme] وَمَا عَلَى ٱلَّذِينَ يَتَّقُونَ مِنْ حِسَابِهِم مِّن شَىْءٍۢ وَلَٰكِن ذِكْرَىٰ لَعَلَّهُمْ يَتَّقُونَ
  Unverified discovery rationale: terra: Those who fear bear no guilt for the mockers' account, but they owe a reminder so that the latter may become wary; fear motivates transmitting a possibly beneficial warning.
- (6:70) [luna: strong; terra: strong; basis: root+scene+theme] وَذَرِ ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَعِبًۭا وَلَهْوًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ وَذَكِّرْ بِهِۦٓ أَن تُبْسَلَ نَفْسٌۢ بِمَا كَسَبَتْ لَيْسَ لَهَا مِن دُونِ ٱللَّهِ وَلِىٌّۭ وَلَا شَفِيعٌۭ وَإِن تَعْدِلْ كُلَّ عَدْلٍۢ لَّا يُؤْخَذْ مِنْهَآ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ أُبْسِلُوا۟ بِمَا كَسَبُوا۟ ۖ لَهُمْ شَرَابٌۭ مِّنْ حَمِيمٍۢ وَعَذَابٌ أَلِيمٌۢ بِمَا كَانُوا۟ يَكْفُرُونَ
  Unverified discovery rationale: luna: Those deluded by worldly life are to be reminded by the Qur'an lest they be left to their deeds, joining reminder with the source's worldly preference. | terra: The Prophet must leave those who trivialize religion yet continue to remind with the Quran lest a soul be ruined by what it earns, pairing distance with responsible admonition.
- (6:104) [luna: strong; terra: medium; basis: contrast+scene+speaker+theme] قَدْ جَآءَكُم بَصَآئِرُ مِن رَّبِّكُمْ ۖ فَمَنْ أَبْصَرَ فَلِنَفْسِهِۦ ۖ وَمَنْ عَمِىَ فَعَلَيْهَا ۚ وَمَآ أَنَا۠ عَلَيْكُم بِحَفِيظٍۢ
  Unverified discovery rationale: luna: The signs benefit the one who sees and harm the one who is blind, while the Prophet is no guardian; this concretizes the source's benefit/harm distinction and limited role. | terra: Insights have come from God; whoever sees benefits himself and whoever is blind bears it himself, while the Prophet is not their keeper—an analogue to the ʿAbasa correction.
- (7:164) [terra: strong; basis: scene+theme] وَإِذْ قَالَتْ أُمَّةٌۭ مِّنْهُمْ لِمَ تَعِظُونَ قَوْمًا ۙ ٱللَّهُ مُهْلِكُهُمْ أَوْ مُعَذِّبُهُمْ عَذَابًۭا شَدِيدًۭا ۖ قَالُوا۟ مَعْذِرَةً إِلَىٰ رَبِّكُمْ وَلَعَلَّهُمْ يَتَّقُونَ
  Unverified discovery rationale: terra: A group asks why admonish people destined for punishment; the answer, as an excuse before God and in hope they may fear, directly probes the section's conditional benefit.
