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
- (7:165) [terra: strong; basis: neighbour+scene+theme] فَلَمَّا نَسُوا۟ مَا ذُكِّرُوا۟ بِهِۦٓ أَنجَيْنَا ٱلَّذِينَ يَنْهَوْنَ عَنِ ٱلسُّوٓءِ وَأَخَذْنَا ٱلَّذِينَ ظَلَمُوا۟ بِعَذَابٍۭ بَـِٔيسٍۭ بِمَا كَانُوا۟ يَفْسُقُونَ
  Unverified discovery rationale: terra: When the warned people forget the admonition, God saves those forbidding evil and punishes the wrongdoers, resolving the question of whether offered reminder matters.
- (7:188) [terra: strong; basis: root+speaker+theme] قُل لَّآ أَمْلِكُ لِنَفْسِى نَفْعًۭا وَلَا ضَرًّا إِلَّا مَا شَآءَ ٱللَّهُ ۚ وَلَوْ كُنتُ أَعْلَمُ ٱلْغَيْبَ لَٱسْتَكْثَرْتُ مِنَ ٱلْخَيْرِ وَمَا مَسَّنِىَ ٱلسُّوٓءُ ۚ إِنْ أَنَا۠ إِلَّا نَذِيرٌۭ وَبَشِيرٌۭ لِّقَوْمٍۢ يُؤْمِنُونَ
  Unverified discovery rationale: terra: The Prophet must say he controls neither benefit nor harm even for himself and is only a warner and bearer of good news, sharply defining the reminder-bearer's limit.
- (7:204) [luna: strong (missing-ayat turn); basis: scene+speaker] وَإِذَا قُرِئَ ٱلْقُرْءَانُ فَٱسْتَمِعُوا۟ لَهُۥ وَأَنصِتُوا۟ لَعَلَّكُمْ تُرْحَمُونَ
  Unverified discovery rationale: luna: When the Qur'an is recited, people are told to listen and attend so they may receive mercy, specifying the accepting response contrasted in the source.
- (7:205) [luna: strong (missing-ayat turn); basis: root+scene] وَٱذْكُر رَّبَّكَ فِى نَفْسِكَ تَضَرُّعًۭا وَخِيفَةًۭ وَدُونَ ٱلْجَهْرِ مِنَ ٱلْقَوْلِ بِٱلْغُدُوِّ وَٱلْءَاصَالِ وَلَا تَكُن مِّنَ ٱلْغَٰفِلِينَ
  Unverified discovery rationale: luna: People are told to remember their Lord within themselves humbly and fearfully and not be heedless, joining the source's remembrance, fear, and avoidance themes.
- (8:2) [luna: strong; terra: strong; basis: root+scene+theme] إِنَّمَا ٱلْمُؤْمِنُونَ ٱلَّذِينَ إِذَا ذُكِرَ ٱللَّهُ وَجِلَتْ قُلُوبُهُمْ وَإِذَا تُلِيَتْ عَلَيْهِمْ ءَايَٰتُهُۥ زَادَتْهُمْ إِيمَٰنًۭا وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ
  Unverified discovery rationale: luna: When God is mentioned the believers' hearts tremble and recited signs increase faith, a concrete positive response to reminder through fear. | terra: True believers' hearts tremble when God is mentioned and their faith increases when His signs are recited; reminder has the benefit that fear opens them to receive.
- (8:20) [luna: strong; basis: scene+speaker] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ أَطِيعُوا۟ ٱللَّهَ وَرَسُولَهُۥ وَلَا تَوَلَّوْا۟ عَنْهُ وَأَنتُمْ تَسْمَعُونَ
  Unverified discovery rationale: luna: Believers are commanded not to turn away from the Messenger while hearing him, the same act of turning aside that the source marks in the avoider.
- (8:21) [luna: strong; basis: contrast+scene] وَلَا تَكُونُوا۟ كَٱلَّذِينَ قَالُوا۟ سَمِعْنَا وَهُمْ لَا يَسْمَعُونَ
  Unverified discovery rationale: luna: The people who say they hear but do not hear expose the difference between receiving a reminder and merely encountering it.
- (8:22) [luna: strong; basis: contrast+theme] ۞ إِنَّ شَرَّ ٱلدَّوَآبِّ عِندَ ٱللَّهِ ٱلصُّمُّ ٱلْبُكْمُ ٱلَّذِينَ لَا يَعْقِلُونَ
  Unverified discovery rationale: luna: The deaf and dumb who do not reason are called the worst creatures, a stark image of refusing what is heard.
- (8:23) [luna: strong; basis: contrast+scene] وَلَوْ عَلِمَ ٱللَّهُ فِيهِمْ خَيْرًۭا لَّأَسْمَعَهُمْ ۖ وَلَوْ أَسْمَعَهُمْ لَتَوَلَّوا۟ وَّهُم مُّعْرِضُونَ
  Unverified discovery rationale: luna: Even if made to hear, they would turn away; the verse directly describes the source's avoidant response.
- (8:24) [luna: strong; basis: contrast+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱسْتَجِيبُوا۟ لِلَّهِ وَلِلرَّسُولِ إِذَا دَعَاكُمْ لِمَا يُحْيِيكُمْ ۖ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ يَحُولُ بَيْنَ ٱلْمَرْءِ وَقَلْبِهِۦ وَأَنَّهُۥٓ إِلَيْهِ تُحْشَرُونَ
  Unverified discovery rationale: luna: God and the Messenger call believers to what gives life, a boundary against the deadened refusal in 8:21–23 and the source's fire scene.
- (9:122) [terra: strong; basis: scene+theme] ۞ وَمَا كَانَ ٱلْمُؤْمِنُونَ لِيَنفِرُوا۟ كَآفَّةًۭ ۚ فَلَوْلَا نَفَرَ مِن كُلِّ فِرْقَةٍۢ مِّنْهُمْ طَآئِفَةٌۭ لِّيَتَفَقَّهُوا۟ فِى ٱلدِّينِ وَلِيُنذِرُوا۟ قَوْمَهُمْ إِذَا رَجَعُوٓا۟ إِلَيْهِمْ لَعَلَّهُمْ يَحْذَرُونَ
  Unverified discovery rationale: terra: A group must gain deep religious knowledge and warn their people on returning so that they may become wary; knowledge is transmitted as fear-producing reminder.
- (9:124) [luna: medium (missing-ayat turn); terra: strong; basis: contrast+scene+theme] وَإِذَا مَآ أُنزِلَتْ سُورَةٌۭ فَمِنْهُم مَّن يَقُولُ أَيُّكُمْ زَادَتْهُ هَٰذِهِۦٓ إِيمَٰنًۭا ۚ فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ فَزَادَتْهُمْ إِيمَٰنًۭا وَهُمْ يَسْتَبْشِرُونَ
  Unverified discovery rationale: luna: When a surah is revealed, believers gain faith and rejoice; this depicts the positive response to revealed reminder that the source contrasts with avoidance. | terra: When a surah descends, believers gain faith and rejoice, showing the benefit of the same address in receptive hearts.
- (9:125) [luna: medium (missing-ayat turn); terra: strong; basis: contrast+neighbour+scene+theme] وَأَمَّا ٱلَّذِينَ فِى قُلُوبِهِم مَّرَضٌۭ فَزَادَتْهُمْ رِجْسًا إِلَىٰ رِجْسِهِمْ وَمَاتُوا۟ وَهُمْ كَٰفِرُونَ
  Unverified discovery rationale: luna: The same revelation adds impurity to those with diseased hearts, completing 9:124's divided responses to the message. | terra: Those with diseased hearts gain impurity upon impurity from that surah and die unbelieving, the opposed result of one offered revelation.
- (9:126) [terra: strong; basis: neighbour+root] أَوَلَا يَرَوْنَ أَنَّهُمْ يُفْتَنُونَ فِى كُلِّ عَامٍۢ مَّرَّةً أَوْ مَرَّتَيْنِ ثُمَّ لَا يَتُوبُونَ وَلَا هُمْ يَذَّكَّرُونَ
  Unverified discovery rationale: terra: Repeated testing still does not bring them to repentance or remembrance, identifying persistent nonreception despite renewed occasions.
- (10:12) [terra: strong; basis: root+scene+theme] وَإِذَا مَسَّ ٱلْإِنسَٰنَ ٱلضُّرُّ دَعَانَا لِجَنۢبِهِۦٓ أَوْ قَاعِدًا أَوْ قَآئِمًۭا فَلَمَّا كَشَفْنَا عَنْهُ ضُرَّهُۥ مَرَّ كَأَن لَّمْ يَدْعُنَآ إِلَىٰ ضُرٍّۢ مَّسَّهُۥ ۚ كَذَٰلِكَ زُيِّنَ لِلْمُسْرِفِينَ مَا كَانُوا۟ يَعْمَلُونَ
  Unverified discovery rationale: terra: Under harm a person calls God while lying on his side, then passes on when harm is removed as though he never called; the side-root and benefit–harm reversal expose forgetful reception.
- (10:49) [terra: strong; basis: root+speaker+theme] قُل لَّآ أَمْلِكُ لِنَفْسِى ضَرًّۭا وَلَا نَفْعًا إِلَّا مَا شَآءَ ٱللَّهُ ۗ لِكُلِّ أُمَّةٍ أَجَلٌ ۚ إِذَا جَآءَ أَجَلُهُمْ فَلَا يَسْتَـْٔخِرُونَ سَاعَةًۭ ۖ وَلَا يَسْتَقْدِمُونَ
  Unverified discovery rationale: terra: The Prophet likewise says he possesses neither harm nor benefit for himself except as God wills, preventing “the reminder benefits” from becoming a claim of prophetic control.
- (10:57) [luna: medium; terra: strong; basis: root+theme] يَٰٓأَيُّهَا ٱلنَّاسُ قَدْ جَآءَتْكُم مَّوْعِظَةٌۭ مِّن رَّبِّكُمْ وَشِفَآءٌۭ لِّمَا فِى ٱلصُّدُورِ وَهُدًۭى وَرَحْمَةٌۭ لِّلْمُؤْمِنِينَ
  Unverified discovery rationale: luna: A reminder from the Lord is described as healing for hearts, guidance, and mercy to believers, giving a specific account of how reminder benefits. | terra: The Quranic admonition is called healing, guidance, and mercy for believers, spelling out the concrete forms in which a reminder benefits.
- (10:101) [terra: strong; basis: contrast+theme] قُلِ ٱنظُرُوا۟ مَاذَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ وَمَا تُغْنِى ٱلْءَايَٰتُ وَٱلنُّذُرُ عَن قَوْمٍۢ لَّا يُؤْمِنُونَ
  Unverified discovery rationale: terra: Signs and warnings do not benefit a people unwilling to believe, distinguishing the offered warning from the inward condition that lets it work.
- (11:34) [terra: strong; basis: root+scene+theme] وَلَا يَنفَعُكُمْ نُصْحِىٓ إِنْ أَرَدتُّ أَنْ أَنصَحَ لَكُمْ إِن كَانَ ٱللَّهُ يُرِيدُ أَن يُغْوِيَكُمْ ۚ هُوَ رَبُّكُمْ وَإِلَيْهِ تُرْجَعُونَ
  Unverified discovery rationale: terra: Noah says his counsel will not benefit his people even if he wishes to counsel them when God wills their deviation; this is a direct boundary on a reminder's نَفْع.
- (11:105) [luna: strong; terra: strong; basis: contrast+root+theme] يَوْمَ يَأْتِ لَا تَكَلَّمُ نَفْسٌ إِلَّا بِإِذْنِهِۦ ۚ فَمِنْهُمْ شَقِىٌّۭ وَسَعِيدٌۭ
  Unverified discovery rationale: luna: The Day divides people into شَقِيٌّ and سَعِيدٌ, explicitly spelling out the misery/happiness opposition named in the source root gloss. | terra: The Last Day divides people explicitly into شَقِىٌّ وَسَعِيدٌ, confirming the section's dictionary opposition between wretchedness and happiness.
- (11:106) [luna: strong; terra: strong; basis: neighbour+root+scene] فَأَمَّا ٱلَّذِينَ شَقُوا۟ فَفِى ٱلنَّارِ لَهُمْ فِيهَا زَفِيرٌۭ وَشَهِيقٌ
  Unverified discovery rationale: luna: The wretched are placed in the Fire, carrying the source's al-ashqa from 87:11 into the consequence stated in 87:12. | terra: Those classed as wretched are in the Fire, joining the word's moral posture to the destination that follows 87:11.
- (11:107) [luna: strong; basis: neighbour+scene] خَٰلِدِينَ فِيهَا مَا دَامَتِ ٱلسَّمَٰوَٰتُ وَٱلْأَرْضُ إِلَّا مَا شَآءَ رَبُّكَ ۚ إِنَّ رَبَّكَ فَعَّالٌۭ لِّمَا يُرِيدُ
  Unverified discovery rationale: luna: The wretched remain in the Fire through the appointed duration; this completes 11:106's fate and recalls 87:13's condition in the Fire.
- (11:108) [luna: strong; terra: strong; basis: contrast+root+scene+theme] ۞ وَأَمَّا ٱلَّذِينَ سُعِدُوا۟ فَفِى ٱلْجَنَّةِ خَٰلِدِينَ فِيهَا مَا دَامَتِ ٱلسَّمَٰوَٰتُ وَٱلْأَرْضُ إِلَّا مَا شَآءَ رَبُّكَ ۖ عَطَآءً غَيْرَ مَجْذُوذٍۢ
  Unverified discovery rationale: luna: The happy are in the Garden without end, completing 11:105's contrast and echoing 87:17's better, abiding Hereafter. | terra: The happy are placed in the Garden, completing the Quranic opposite to the section's ٱلْأَشْقَى.
- (13:19) [terra: strong; basis: contrast+root+scene+theme] ۞ أَفَمَن يَعْلَمُ أَنَّمَآ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ ٱلْحَقُّ كَمَنْ هُوَ أَعْمَىٰٓ ۚ إِنَّمَا يَتَذَكَّرُ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
  Unverified discovery rationale: terra: One who knows the revelation is truth is contrasted with the blind, and only people of understanding remember; knowledge, sight, and remembrance converge around reception.
- (14:17) [luna: strong (missing-ayat turn); basis: contrast+scene] يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ وَيَأْتِيهِ ٱلْمَوْتُ مِن كُلِّ مَكَانٍۢ وَمَا هُوَ بِمَيِّتٍۢ ۖ وَمِن وَرَآئِهِۦ عَذَابٌ غَلِيظٌۭ
  Unverified discovery rationale: luna: The drinker's punishment brings death from every side but he does not die, a specific fire-scene parallel to 87:13's neither-death-nor-life condition.
- (14:35) [terra: strong; basis: contrast+root] وَإِذْ قَالَ إِبْرَٰهِيمُ رَبِّ ٱجْعَلْ هَٰذَا ٱلْبَلَدَ ءَامِنًۭا وَٱجْنُبْنِى وَبَنِىَّ أَن نَّعْبُدَ ٱلْأَصْنَامَ
  Unverified discovery rationale: terra: Abraham asks God to keep him and his sons away from idol worship; the distance-root marks protection when its object is false worship, reversing the wretched person's object.
- (14:52) [terra: strong; basis: root+theme] هَٰذَا بَلَٰغٌۭ لِّلنَّاسِ وَلِيُنذَرُوا۟ بِهِۦ وَلِيَعْلَمُوٓا۟ أَنَّمَا هُوَ إِلَٰهٌۭ وَٰحِدٌۭ وَلِيَذَّكَّرَ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
  Unverified discovery rationale: terra: The Quranic proclamation warns humanity so that they know God is one and so that people of understanding remember; warning produces knowledge and remembrance together.
- (16:36) [terra: strong; basis: contrast+root+scene] وَلَقَدْ بَعَثْنَا فِى كُلِّ أُمَّةٍۢ رَّسُولًا أَنِ ٱعْبُدُوا۟ ٱللَّهَ وَٱجْتَنِبُوا۟ ٱلطَّٰغُوتَ ۖ فَمِنْهُم مَّنْ هَدَى ٱللَّهُ وَمِنْهُم مَّنْ حَقَّتْ عَلَيْهِ ٱلضَّلَٰلَةُ ۚ فَسِيرُوا۟ فِى ٱلْأَرْضِ فَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ
  Unverified discovery rationale: terra: Every community receives a messenger saying to worship God and ٱجْتَنِبُوا۟ ٱلطَّاغُوتَ; the same avoidance root becomes right when directed at false gods rather than reminder.
- (16:82) [luna: strong (missing-ayat turn); terra: medium; basis: scene+speaker] فَإِن تَوَلَّوْا۟ فَإِنَّمَا عَلَيْكَ ٱلْبَلَٰغُ ٱلْمُبِينُ
  Unverified discovery rationale: luna: If people turn away, the Messenger's sole charge is clear delivery, a direct boundary on the reminder-giver's role in the source. | terra: If they turn away, only clear delivery rests upon the Messenger, preserving the reminder-bearer's task despite failed benefit.
- (16:90) [terra: strong (missing-ayat turn); basis: root+speaker+theme] ۞ إِنَّ ٱللَّهَ يَأْمُرُ بِٱلْعَدْلِ وَٱلْإِحْسَٰنِ وَإِيتَآئِ ذِى ٱلْقُرْبَىٰ وَيَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ وَٱلْبَغْىِ ۚ يَعِظُكُمْ لَعَلَّكُمْ تَذَكَّرُونَ
  Unverified discovery rationale: terra: After stating His commands, God says He admonishes the hearers so that they may remember; instruction crosses to another in order to produce remembrance.
- (17:18) [luna: strong; basis: contrast+theme] مَّن كَانَ يُرِيدُ ٱلْعَاجِلَةَ عَجَّلْنَا لَهُۥ فِيهَا مَا نَشَآءُ لِمَن نُّرِيدُ ثُمَّ جَعَلْنَا لَهُۥ جَهَنَّمَ يَصْلَىٰهَا مَذْمُومًۭا مَّدْحُورًۭا
  Unverified discovery rationale: luna: The one who desires only the immediate life is promised Hell, making the source's warning against preferring dunya concrete.
- (17:19) [luna: strong; basis: contrast+theme] وَمَنْ أَرَادَ ٱلْءَاخِرَةَ وَسَعَىٰ لَهَا سَعْيَهَا وَهُوَ مُؤْمِنٌۭ فَأُو۟لَٰٓئِكَ كَانَ سَعْيُهُم مَّشْكُورًۭا
  Unverified discovery rationale: luna: The believer who strives for the Hereafter receives recompense, completing 17:18's choice and 87:17's enduring alternative.
- (17:41) [terra: strong (missing-ayat turn); basis: contrast+root+scene] وَلَقَدْ صَرَّفْنَا فِى هَٰذَا ٱلْقُرْءَانِ لِيَذَّكَّرُوا۟ وَمَا يَزِيدُهُمْ إِلَّا نُفُورًۭا
  Unverified discovery rationale: terra: God has varied the Quran so that they may remember, yet this only increases their aversion, an exact case of reminder producing distance in unreceptive hearers.
- (17:45) [luna: strong; basis: contrast+scene] وَإِذَا قَرَأْتَ ٱلْقُرْءَانَ جَعَلْنَا بَيْنَكَ وَبَيْنَ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ حِجَابًۭا مَّسْتُورًۭا
  Unverified discovery rationale: luna: When the Qur'an is recited, a hidden barrier separates the Prophet from those who deny the Hereafter, a concrete image of distance from reminder.
- (17:46) [luna: strong; terra: contrast; basis: contrast+scene] وَجَعَلْنَا عَلَىٰ قُلُوبِهِمْ أَكِنَّةً أَن يَفْقَهُوهُ وَفِىٓ ءَاذَانِهِمْ وَقْرًۭا ۚ وَإِذَا ذَكَرْتَ رَبَّكَ فِى ٱلْقُرْءَانِ وَحْدَهُۥ وَلَّوْا۟ عَلَىٰٓ أَدْبَٰرِهِمْ نُفُورًۭا
  Unverified discovery rationale: luna: Their hearts have coverings and ears are stopped when the Lord alone is mentioned, explaining the barrier in 17:45 as refusal of remembrance. | terra: When the Prophet mentions his Lord alone in the Quran, the rejecters turn their backs in aversion; their motion contrasts with the blind seeker's approach.
- (17:82) [luna: strong (missing-ayat turn); basis: contrast+root+theme] وَنُنَزِّلُ مِنَ ٱلْقُرْءَانِ مَا هُوَ شِفَآءٌۭ وَرَحْمَةٌۭ لِّلْمُؤْمِنِينَ ۙ وَلَا يَزِيدُ ٱلظَّٰلِمِينَ إِلَّا خَسَارًۭا
  Unverified discovery rationale: luna: The Qur'an is healing and mercy for believers but increases wrongdoers only in loss, giving a specific account of reminder's benefit or harm according to reception.
- (17:83) [terra: strong; basis: root+scene+theme] وَإِذَآ أَنْعَمْنَا عَلَى ٱلْإِنسَٰنِ أَعْرَضَ وَنَـَٔا بِجَانِبِهِۦ ۖ وَإِذَا مَسَّهُ ٱلشَّرُّ كَانَ يَـُٔوسًۭا
  Unverified discovery rationale: terra: When favored, the human turns away and distances بِجَانِبِهِ, but when harm touches him he despairs; the root's “side/distance” sense meets the section's benefit–harm polarity.
- (17:107) [terra: strong; basis: scene+theme] قُلْ ءَامِنُوا۟ بِهِۦٓ أَوْ لَا تُؤْمِنُوٓا۟ ۚ إِنَّ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ مِن قَبْلِهِۦٓ إِذَا يُتْلَىٰ عَلَيْهِمْ يَخِرُّونَ لِلْأَذْقَانِ سُجَّدًۭا
  Unverified discovery rationale: terra: Those given knowledge before the Quran fall on their faces in prostration when it is recited, linking knowledge directly to receptive action.
- (17:108) [terra: strong; basis: neighbour+root] وَيَقُولُونَ سُبْحَٰنَ رَبِّنَآ إِن كَانَ وَعْدُ رَبِّنَا لَمَفْعُولًۭا
  Unverified discovery rationale: terra: They glorify their Lord and affirm His promise, showing the knowledgeable hearer's articulated response rather than mere exposure.
- (17:109) [terra: strong; basis: neighbour+scene+theme] وَيَخِرُّونَ لِلْأَذْقَانِ يَبْكُونَ وَيَزِيدُهُمْ خُشُوعًۭا ۩
  Unverified discovery rationale: terra: They fall weeping and the recitation increases their humility, completing the section's claim that informed fear receives reminder.
- (18:28) [luna: strong; basis: contrast+scene] وَٱصْبِرْ نَفْسَكَ مَعَ ٱلَّذِينَ يَدْعُونَ رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ وَلَا تَعْدُ عَيْنَاكَ عَنْهُمْ تُرِيدُ زِينَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُۥ عَن ذِكْرِنَا وَٱتَّبَعَ هَوَىٰهُ وَكَانَ أَمْرُهُۥ فُرُطًۭا
  Unverified discovery rationale: luna: The Prophet is told not to let his eyes pass beyond those invoking God while seeking the world's adornment; it closely parallels the warning against overlooking the fearful visitor in 80.
- (18:57) [luna: strong; terra: strong; basis: root+scene+theme] وَمَنْ أَظْلَمُ مِمَّن ذُكِّرَ بِـَٔايَٰتِ رَبِّهِۦ فَأَعْرَضَ عَنْهَا وَنَسِىَ مَا قَدَّمَتْ يَدَاهُ ۚ إِنَّا جَعَلْنَا عَلَىٰ قُلُوبِهِمْ أَكِنَّةً أَن يَفْقَهُوهُ وَفِىٓ ءَاذَانِهِمْ وَقْرًۭا ۖ وَإِن تَدْعُهُمْ إِلَى ٱلْهُدَىٰ فَلَن يَهْتَدُوٓا۟ إِذًا أَبَدًۭا
  Unverified discovery rationale: luna: The one reminded of God's signs turns away and forgets what he sent ahead, a direct instance of the source's avoided reminder. | terra: The one reminded of God's signs turns away and forgets what he has sent ahead; coverings and deafness explain why even a call to guidance will not reach him.
- (19:58) [terra: strong; basis: scene+theme] أُو۟لَٰٓئِكَ ٱلَّذِينَ أَنْعَمَ ٱللَّهُ عَلَيْهِم مِّنَ ٱلنَّبِيِّۦنَ مِن ذُرِّيَّةِ ءَادَمَ وَمِمَّنْ حَمَلْنَا مَعَ نُوحٍۢ وَمِن ذُرِّيَّةِ إِبْرَٰهِيمَ وَإِسْرَٰٓءِيلَ وَمِمَّنْ هَدَيْنَا وَٱجْتَبَيْنَآ ۚ إِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَٰتُ ٱلرَّحْمَٰنِ خَرُّوا۟ سُجَّدًۭا وَبُكِيًّۭا ۩
  Unverified discovery rationale: terra: When the Merciful's signs are recited, the guided prophets fall prostrate and weeping, the fullest bodily picture of address entering a fearful hearer.
- (19:59) [luna: strong; basis: contrast+scene] ۞ فَخَلَفَ مِنۢ بَعْدِهِمْ خَلْفٌ أَضَاعُوا۟ ٱلصَّلَوٰةَ وَٱتَّبَعُوا۟ ٱلشَّهَوَٰتِ ۖ فَسَوْفَ يَلْقَوْنَ غَيًّا
  Unverified discovery rationale: luna: Later generations neglect prayer and follow desires, a direct enactment of the source's lexical echo between avoidance and being far from prayer.
- (19:60) [luna: strong; basis: contrast+neighbour] إِلَّا مَن تَابَ وَءَامَنَ وَعَمِلَ صَٰلِحًۭا فَأُو۟لَٰٓئِكَ يَدْخُلُونَ ٱلْجَنَّةَ وَلَا يُظْلَمُونَ شَيْـًۭٔا
  Unverified discovery rationale: luna: Those who repent and do right enter the Garden, completing 19:59's neglected prayer and desire with a path back to success.
- (19:97) [terra: strong; basis: root+speaker+theme] فَإِنَّمَا يَسَّرْنَٰهُ بِلِسَانِكَ لِتُبَشِّرَ بِهِ ٱلْمُتَّقِينَ وَتُنذِرَ بِهِۦ قَوْمًۭا لُّدًّۭا
  Unverified discovery rationale: terra: The Quran is eased in the Prophet's tongue to give good news to the God-conscious and warn a fiercely contentious people, preserving both audiences of reminder.
- (20:2) [luna: strong; terra: contrast; basis: contrast+neighbour+root+speaker] مَآ أَنزَلْنَا عَلَيْكَ ٱلْقُرْءَانَ لِتَشْقَىٰٓ
  Unverified discovery rationale: luna: This says the Qur'an was not sent to distress the Prophet; it supplies the non-burdensome boundary immediately before 20:3's reminder for the fearful. | terra: The Quran was not sent to make the Prophet تَشْقَىٰ; the wretchedness-root applies here to the burden of delivery and protects the reminder-bearer from owning its reception.
- (20:3) [luna: strong; terra: strong; basis: root+scene+speaker] [cited in ¶67] إِلَّا تَذْكِرَةًۭ لِّمَن يَخْشَىٰ
  Unverified discovery rationale: luna: The Qur'an is a reminder for مَن يَخْشَىٰ, directly bringing together reminder and the fearful recipient as 87:9–10 do. | terra: The revelation is defined as تَذْكِرَةً for the one who fears, joining the section's offered reminder and receptive fear in one formula.
- (20:14) [luna: strong; basis: root+theme] إِنَّنِىٓ أَنَا ٱللَّهُ لَآ إِلَٰهَ إِلَّآ أَنَا۠ فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ
  Unverified discovery rationale: luna: God commands worship and prayer لِذِكْرِي, directly joining the source's remembrance of the Lord's name and prayer in 87:15.
- (20:44) [luna: strong; terra: strong; basis: root+scene+speaker+theme] [cited in ¶67] فَقُولَا لَهُۥ قَوْلًۭا لَّيِّنًۭا لَّعَلَّهُۥ يَتَذَكَّرُ أَوْ يَخْشَىٰ
  Unverified discovery rationale: luna: Moses and Aaron must speak gently to Pharaoh in hope that he remembers or fears, a direct parallel to offering reminder to a hearer who may respond. | terra: Moses and Aaron must address Pharaoh gently so that he may remember or fear; the two possible receptive acts of 87:10 are offered even to its emblematic rejecter.
- (20:47) [luna: strong (missing-ayat turn); basis: root+scene] فَأْتِيَاهُ فَقُولَآ إِنَّا رَسُولَا رَبِّكَ فَأَرْسِلْ مَعَنَا بَنِىٓ إِسْرَٰٓءِيلَ وَلَا تُعَذِّبْهُمْ ۖ قَدْ جِئْنَٰكَ بِـَٔايَةٍۢ مِّن رَّبِّكَ ۖ وَٱلسَّلَٰمُ عَلَىٰ مَنِ ٱتَّبَعَ ٱلْهُدَىٰٓ
  Unverified discovery rationale: luna: Moses and Aaron tell Pharaoh that peace is for whoever follows guidance, directly linking their invitation to the source's root ه د ي and Pharaoh's choice.
- (20:48) [luna: strong (missing-ayat turn); basis: contrast+scene] إِنَّا قَدْ أُوحِىَ إِلَيْنَآ أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ
  Unverified discovery rationale: luna: They tell Pharaoh that punishment is for whoever denies and turns away, completing their invitation in 20:47 with the very response the source assigns to its avoider.
- (20:74) [luna: strong; basis: contrast+scene] إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
  Unverified discovery rationale: luna: The criminal's Hell is described with لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, the exact fate named just after the source image in 87:13.
- (20:75) [luna: strong; basis: contrast+scene] وَمَن يَأْتِهِۦ مُؤْمِنًۭا قَدْ عَمِلَ ٱلصَّٰلِحَٰتِ فَأُو۟لَٰٓئِكَ لَهُمُ ٱلدَّرَجَٰتُ ٱلْعُلَىٰ
  Unverified discovery rationale: luna: The believer who does good receives high ranks, contrasting the wretched criminal of 20:74 and the source's successful purifier.
- (20:76) [luna: strong; basis: contrast+root] جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ
  Unverified discovery rationale: luna: The gardens are the reward of one who purifies himself, joining the source's 87:14 purification to its contrast with fire.
- (20:99) [terra: strong (missing-ayat turn); basis: neighbour+root] كَذَٰلِكَ نَقُصُّ عَلَيْكَ مِنْ أَنۢبَآءِ مَا قَدْ سَبَقَ ۚ وَقَدْ ءَاتَيْنَٰكَ مِن لَّدُنَّا ذِكْرًۭا
  Unverified discovery rationale: terra: God says the Prophet has been given a Reminder before warning in 20:100 about whoever turns from it; this ayah identifies what is being avoided.
- (20:100) [terra: strong; basis: root+scene+theme] مَّنْ أَعْرَضَ عَنْهُ فَإِنَّهُۥ يَحْمِلُ يَوْمَ ٱلْقِيَٰمَةِ وِزْرًا
  Unverified discovery rationale: terra: Whoever turns away from the Quranic reminder bears a burden on Resurrection, making refusal rather than lack of presentation decisive.
- (20:113) [terra: strong; basis: root+theme] وَكَذَٰلِكَ أَنزَلْنَٰهُ قُرْءَانًا عَرَبِيًّۭا وَصَرَّفْنَا فِيهِ مِنَ ٱلْوَعِيدِ لَعَلَّهُمْ يَتَّقُونَ أَوْ يُحْدِثُ لَهُمْ ذِكْرًۭا
  Unverified discovery rationale: terra: The Arabic Quran varies its warnings so that people may fear or it may produce remembrance in them, explicitly naming the two hoped-for effects of address.
- (20:123) [luna: strong; terra: strong; basis: contrast+root+theme] قَالَ ٱهْبِطَا مِنْهَا جَمِيعًۢا ۖ بَعْضُكُمْ لِبَعْضٍ عَدُوٌّۭ ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَنِ ٱتَّبَعَ هُدَاىَ فَلَا يَضِلُّ وَلَا يَشْقَىٰ
  Unverified discovery rationale: luna: Whoever follows God's guidance will neither go astray nor be wretched, the opposite of the source's al-ashqa who avoids the reminder; the verse also uses the ه د ي root in its source gloss. | terra: Whoever follows divine guidance will neither stray nor become wretched, directly opposing guided reception to شقاء.
- (20:124) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶67] وَمَنْ أَعْرَضَ عَن ذِكْرِى فَإِنَّ لَهُۥ مَعِيشَةًۭ ضَنكًۭا وَنَحْشُرُهُۥ يَوْمَ ٱلْقِيَٰمَةِ أَعْمَىٰ
  Unverified discovery rationale: luna: Whoever turns away from God's remembrance receives a constricted life, a direct statement of the consequence of the source's avoidance. | terra: Whoever turns away from God's remembrance receives a constricted life and blind resurrection, the developed consequence of keeping reminder distant.
- (20:126) [luna: strong; basis: contrast+scene] قَالَ كَذَٰلِكَ أَتَتْكَ ءَايَٰتُنَا فَنَسِيتَهَا ۖ وَكَذَٰلِكَ ٱلْيَوْمَ تُنسَىٰ
  Unverified discovery rationale: luna: God says His signs came but were disregarded, so the person is disregarded that Day; this names the consequence of refusing the reminder.
- (20:127) [luna: strong; basis: contrast+theme] وَكَذَٰلِكَ نَجْزِى مَنْ أَسْرَفَ وَلَمْ يُؤْمِنۢ بِـَٔايَٰتِ رَبِّهِۦ ۚ وَلَعَذَابُ ٱلْءَاخِرَةِ أَشَدُّ وَأَبْقَىٰٓ
  Unverified discovery rationale: luna: The afterlife punishment is more severe and more enduring than the worldly one, echoing 87:17's better and abiding Hereafter.
- (21:2) [terra: strong; basis: root+scene] مَا يَأْتِيهِم مِّن ذِكْرٍۢ مِّن رَّبِّهِم مُّحْدَثٍ إِلَّا ٱسْتَمَعُوهُ وَهُمْ يَلْعَبُونَ
  Unverified discovery rationale: terra: No renewed reminder comes from their Lord without their listening while at play; hearing without receptive attention is a specific way of letting it pass by.
- (21:10) [terra: strong (missing-ayat turn); basis: root+theme] لَقَدْ أَنزَلْنَآ إِلَيْكُمْ كِتَٰبًۭا فِيهِ ذِكْرُكُمْ ۖ أَفَلَا تَعْقِلُونَ
  Unverified discovery rationale: terra: God has sent a Book containing the addressees' reminder and asks whether they will reason, joining arriving reminder to the understanding needed to receive it.
- (21:24) [terra: strong (missing-ayat turn); basis: root+theme] أَمِ ٱتَّخَذُوا۟ مِن دُونِهِۦٓ ءَالِهَةًۭ ۖ قُلْ هَاتُوا۟ بُرْهَٰنَكُمْ ۖ هَٰذَا ذِكْرُ مَن مَّعِىَ وَذِكْرُ مَن قَبْلِى ۗ بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ ٱلْحَقَّ ۖ فَهُم مُّعْرِضُونَ
  Unverified discovery rationale: terra: Most of them do not know the truth and therefore turn away, directly linking deficient knowledge to the response opposite reverent fear.
- (21:42) [terra: strong (missing-ayat turn); basis: root+scene] قُلْ مَن يَكْلَؤُكُم بِٱلَّيْلِ وَٱلنَّهَارِ مِنَ ٱلرَّحْمَٰنِ ۗ بَلْ هُمْ عَن ذِكْرِ رَبِّهِم مُّعْرِضُونَ
  Unverified discovery rationale: terra: Although none can protect them from the Merciful, they turn away from their Lord's remembrance, naming the same object and posture as 87:11.
- (21:50) [terra: strong; basis: root+scene] وَهَٰذَا ذِكْرٌۭ مُّبَارَكٌ أَنزَلْنَٰهُ ۚ أَفَأَنتُمْ لَهُۥ مُنكِرُونَ
  Unverified discovery rationale: terra: “This is a blessed Reminder” is followed by the question whether they will deny it, holding the offered good and its possible rejection together.
- (22:12) [terra: strong (missing-ayat turn); basis: contrast+root] يَدْعُوا۟ مِن دُونِ ٱللَّهِ مَا لَا يَضُرُّهُۥ وَمَا لَا يَنفَعُهُۥ ۚ ذَٰلِكَ هُوَ ٱلضَّلَٰلُ ٱلْبَعِيدُ
  Unverified discovery rationale: terra: The misguided person invokes what can neither harm nor benefit, contrasting a falsely sought benefit with the reminder's real possible benefit.
- (22:13) [terra: strong (missing-ayat turn); basis: contrast+neighbour+root] يَدْعُوا۟ لَمَن ضَرُّهُۥٓ أَقْرَبُ مِن نَّفْعِهِۦ ۚ لَبِئْسَ ٱلْمَوْلَىٰ وَلَبِئْسَ ٱلْعَشِيرُ
  Unverified discovery rationale: terra: What he invokes is said to have harm nearer than benefit, exposing a wretched inversion of the benefit–harm distinction named in the section.
- (22:30) [terra: strong; basis: contrast+root] ذَٰلِكَ وَمَن يُعَظِّمْ حُرُمَٰتِ ٱللَّهِ فَهُوَ خَيْرٌۭ لَّهُۥ عِندَ رَبِّهِۦ ۗ وَأُحِلَّتْ لَكُمُ ٱلْأَنْعَٰمُ إِلَّا مَا يُتْلَىٰ عَلَيْكُمْ ۖ فَٱجْتَنِبُوا۟ ٱلرِّجْسَ مِنَ ٱلْأَوْثَٰنِ وَٱجْتَنِبُوا۟ قَوْلَ ٱلزُّورِ
  Unverified discovery rationale: terra: The command to avoid the filth of idols and false speech again shows that avoidance is morally defined by what one keeps distant.
- (22:35) [terra: strong; basis: root+scene+theme] ٱلَّذِينَ إِذَا ذُكِرَ ٱللَّهُ وَجِلَتْ قُلُوبُهُمْ وَٱلصَّٰبِرِينَ عَلَىٰ مَآ أَصَابَهُمْ وَٱلْمُقِيمِى ٱلصَّلَوٰةِ وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
  Unverified discovery rationale: terra: The humble are those whose hearts tremble when God is mentioned, who endure and establish prayer, joining receptive fear, remembrance, and prayer.
- (22:54) [terra: strong; basis: root+scene+theme] وَلِيَعْلَمَ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّكَ فَيُؤْمِنُوا۟ بِهِۦ فَتُخْبِتَ لَهُۥ قُلُوبُهُمْ ۗ وَإِنَّ ٱللَّهَ لَهَادِ ٱلَّذِينَ ءَامَنُوٓا۟ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
  Unverified discovery rationale: terra: Those given knowledge recognize revelation as truth, believe it, and their hearts humble to God; knowledge becomes the bridge from address to reverent reception.
- (23:57) [luna: strong; terra: strong; basis: root+theme] إِنَّ ٱلَّذِينَ هُم مِّنْ خَشْيَةِ رَبِّهِم مُّشْفِقُونَ
  Unverified discovery rationale: luna: Those who are apprehensive of their Lord's awe are identified as the first group in a portrait of receptive believers. | terra: Those who are apprehensive from خشية of their Lord begin a portrait of the people whose fear issues in responsive action.
- (23:58) [luna: strong; terra: strong; basis: neighbour+scene+theme] وَٱلَّذِينَ هُم بِـَٔايَٰتِ رَبِّهِمْ يُؤْمِنُونَ
  Unverified discovery rationale: luna: They believe in their Lord's signs, completing the receptive group introduced in 23:57 as a counterpart to those who avoid reminder. | terra: They believe in their Lord's signs, giving the direct receptive consequence of the fear named in 23:57.
- (23:59) [luna: strong; basis: contrast+neighbour] وَٱلَّذِينَ هُم بِرَبِّهِمْ لَا يُشْرِكُونَ
  Unverified discovery rationale: luna: They do not associate partners with their Lord, continuing the faithful response contrasted with refusal in the source.
- (23:60) [luna: strong; terra: strong; basis: neighbour+root+scene+theme] وَٱلَّذِينَ يُؤْتُونَ مَآ ءَاتَوا۟ وَّقُلُوبُهُمْ وَجِلَةٌ أَنَّهُمْ إِلَىٰ رَبِّهِمْ رَٰجِعُونَ
  Unverified discovery rationale: luna: They give while their hearts are fearful because they will return to their Lord, a direct form of fear that accompanies good action. | terra: They give what they give while their hearts remain fearful of return to their Lord, showing reverent fear joined to action rather than paralysis.
- (23:61) [luna: strong; terra: strong; basis: neighbour+scene+theme] أُو۟لَٰٓئِكَ يُسَٰرِعُونَ فِى ٱلْخَيْرَٰتِ وَهُمْ لَهَا سَٰبِقُونَ
  Unverified discovery rationale: luna: These believers hasten to good deeds, completing 23:57–60's portrait of fear and response. | terra: They hasten to good deeds and outstrip others in them, completing the active result of informed fear.
- (23:71) [terra: strong; basis: root+scene] وَلَوِ ٱتَّبَعَ ٱلْحَقُّ أَهْوَآءَهُمْ لَفَسَدَتِ ٱلسَّمَٰوَٰتُ وَٱلْأَرْضُ وَمَن فِيهِنَّ ۚ بَلْ أَتَيْنَٰهُم بِذِكْرِهِمْ فَهُمْ عَن ذِكْرِهِم مُّعْرِضُونَ
  Unverified discovery rationale: terra: God has brought them their Reminder, yet they turn away from it; arrival and self-imposed distance reproduce the section's two-sided action.
- (23:106) [terra: strong; basis: root+theme] قَالُوا۟ رَبَّنَا غَلَبَتْ عَلَيْنَا شِقْوَتُنَا وَكُنَّا قَوْمًۭا ضَآلِّينَ
  Unverified discovery rationale: terra: The condemned confess that their شِقْوَتُنَا overcame them and that they were astray, letting wretchedness name the condition behind failed reception.
- (24:37) [luna: strong; basis: root+scene] رِجَالٌۭ لَّا تُلْهِيهِمْ تِجَٰرَةٌۭ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَآءِ ٱلزَّكَوٰةِ ۙ يَخَافُونَ يَوْمًۭا تَتَقَلَّبُ فِيهِ ٱلْقُلُوبُ وَٱلْأَبْصَٰرُ
  Unverified discovery rationale: luna: Trade does not distract these people from God's ذكر, prayer, and fear of the Day, joining the source's remembered name, prayer, and worldly-life contrast.
- (24:52) [terra: strong; basis: root+theme] وَمَن يُطِعِ ٱللَّهَ وَرَسُولَهُۥ وَيَخْشَ ٱللَّهَ وَيَتَّقْهِ فَأُو۟لَٰٓئِكَ هُمُ ٱلْفَآئِزُونَ
  Unverified discovery rationale: terra: Obedience to God and His Messenger, fear of God, and God-consciousness are made the marks of the successful, connecting receptive fear to felicity rather than wretchedness.
- (24:54) [luna: strong (missing-ayat turn); basis: contrast+scene+speaker] قُلْ أَطِيعُوا۟ ٱللَّهَ وَأَطِيعُوا۟ ٱلرَّسُولَ ۖ فَإِن تَوَلَّوْا۟ فَإِنَّمَا عَلَيْهِ مَا حُمِّلَ وَعَلَيْكُم مَّا حُمِّلْتُمْ ۖ وَإِن تُطِيعُوهُ تَهْتَدُوا۟ ۚ وَمَا عَلَى ٱلرَّسُولِ إِلَّا ٱلْبَلَٰغُ ٱلْمُبِينُ
  Unverified discovery rationale: luna: If people turn away, their duty remains theirs and the Messenger's is clear conveyance; those who obey are guided, joining the source's avoider, receptive hearer, and preacher's boundary.
- (25:29) [terra: strong; basis: root+scene] لَّقَدْ أَضَلَّنِى عَنِ ٱلذِّكْرِ بَعْدَ إِذْ جَآءَنِى ۗ وَكَانَ ٱلشَّيْطَٰنُ لِلْإِنسَٰنِ خَذُولًۭا
  Unverified discovery rationale: terra: The false companion led the speaker away from the Reminder after it had reached him; this exactly stages reminder being held at a distance after presentation.
- (25:30) [luna: strong (missing-ayat turn); terra: strong; basis: neighbour+root+scene+speaker] وَقَالَ ٱلرَّسُولُ يَٰرَبِّ إِنَّ قَوْمِى ٱتَّخَذُوا۟ هَٰذَا ٱلْقُرْءَانَ مَهْجُورًۭا
  Unverified discovery rationale: luna: The Messenger complains that his people have treated the Qur'an as abandoned, an explicit form of the avoidant relation to reminder developed in the source. | terra: The Messenger complains that his people took this Quran as abandoned, giving the reminder-bearer's own account of collective avoidance.
- (25:60) [terra: strong (missing-ayat turn); basis: contrast+scene] وَإِذَا قِيلَ لَهُمُ ٱسْجُدُوا۟ لِلرَّحْمَٰنِ قَالُوا۟ وَمَا ٱلرَّحْمَٰنُ أَنَسْجُدُ لِمَا تَأْمُرُنَا وَزَادَهُمْ نُفُورًۭا ۩
  Unverified discovery rationale: terra: When commanded to prostrate to the Merciful, the rejecters challenge the name and the command increases their aversion, showing address converted into distance.
- (25:73) [terra: strong; basis: contrast+root+scene] وَٱلَّذِينَ إِذَا ذُكِّرُوا۟ بِـَٔايَٰتِ رَبِّهِمْ لَمْ يَخِرُّوا۟ عَلَيْهَا صُمًّۭا وَعُمْيَانًۭا
  Unverified discovery rationale: terra: The Merciful's servants, when reminded of their Lord's signs, do not fall upon them deaf and blind; bodily impairment becomes a metaphor for refusal, unlike the receptive blind man.
- (26:5) [terra: strong; basis: root+scene] وَمَا يَأْتِيهِم مِّن ذِكْرٍۢ مِّنَ ٱلرَّحْمَٰنِ مُحْدَثٍ إِلَّا كَانُوا۟ عَنْهُ مُعْرِضِينَ
  Unverified discovery rationale: terra: No renewed reminder comes from the Merciful without their turning away from it, an exact recurring formulation of 87:11's response.
- (26:136) [terra: strong; basis: contrast+scene+theme] قَالُوا۟ سَوَآءٌ عَلَيْنَآ أَوَعَظْتَ أَمْ لَمْ تَكُن مِّنَ ٱلْوَٰعِظِينَ
  Unverified discovery rationale: terra: Hud's people say admonition and its absence are the same to them, voicing the wretched hearer's deliberate insulation from reminder.
- (27:92) [terra: strong (missing-ayat turn); basis: scene+speaker+theme] وَأَنْ أَتْلُوَا۟ ٱلْقُرْءَانَ ۖ فَمَنِ ٱهْتَدَىٰ فَإِنَّمَا يَهْتَدِى لِنَفْسِهِۦ ۖ وَمَن ضَلَّ فَقُلْ إِنَّمَآ أَنَا۠ مِنَ ٱلْمُنذِرِينَ
  Unverified discovery rationale: terra: The Prophet is commanded to recite the Quran; whoever is guided benefits himself, while toward one who strays he is only a warner.
- (29:45) [luna: strong; terra: medium (missing-ayat turn); basis: root+theme] ٱتْلُ مَآ أُوحِىَ إِلَيْكَ مِنَ ٱلْكِتَٰبِ وَأَقِمِ ٱلصَّلَوٰةَ ۖ إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۗ وَلَذِكْرُ ٱللَّهِ أَكْبَرُ ۗ وَٱللَّهُ يَعْلَمُ مَا تَصْنَعُونَ
  Unverified discovery rationale: luna: The recited Book and prayer are joined to God's ذكر, the same relation made explicit by 87:15 in the source section's discussion. | terra: Prayer restrains indecency and God's remembrance is greater, affirming the section's developed intuition that remembrance and prayer belong together.
- (29:49) [terra: strong; basis: contrast+root+theme] بَلْ هُوَ ءَايَٰتٌۢ بَيِّنَٰتٌۭ فِى صُدُورِ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ ۚ وَمَا يَجْحَدُ بِـَٔايَٰتِنَآ إِلَّا ٱلظَّٰلِمُونَ
  Unverified discovery rationale: terra: The signs are clear in the breasts of those given knowledge, while only wrongdoers reject them; knowledge is presented as an inward lodging-place for reminder.
- (31:7) [terra: strong; basis: scene+theme] وَإِذَا تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا وَلَّىٰ مُسْتَكْبِرًۭا كَأَن لَّمْ يَسْمَعْهَا كَأَنَّ فِىٓ أُذُنَيْهِ وَقْرًۭا ۖ فَبَشِّرْهُ بِعَذَابٍ أَلِيمٍ
  Unverified discovery rationale: terra: When God's signs are recited, the arrogant hearer turns away as if he had not heard and had deafness in his ears, dramatizing reminder made useless by posture.
- (32:15) [luna: strong; terra: strong; basis: root+scene] إِنَّمَا يُؤْمِنُ بِـَٔايَٰتِنَا ٱلَّذِينَ إِذَا ذُكِّرُوا۟ بِهَا خَرُّوا۟ سُجَّدًۭا وَسَبَّحُوا۟ بِحَمْدِ رَبِّهِمْ وَهُمْ لَا يَسْتَكْبِرُونَ ۩
  Unverified discovery rationale: luna: Those reminded of God's signs fall in prostration and glorify Him without arrogance, showing the response opposite to avoidance. | terra: Believers in the signs fall prostrate and glorify when they are reminded of them, embodying the opposite movement from turning away.
- (32:16) [luna: strong; terra: medium; basis: contrast+neighbour+root+scene+theme] تَتَجَافَىٰ جُنُوبُهُمْ عَنِ ٱلْمَضَاجِعِ يَدْعُونَ رَبَّهُمْ خَوْفًۭا وَطَمَعًۭا وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
  Unverified discovery rationale: luna: Their sides withdraw from beds as they call their Lord in fear and hope, completing 32:15's humble response with worship and fear. | terra: The believers' جُنُوبُهُمْ forsake their beds as they call their Lord in fear and hope; the physical “sides” root is drawn toward prayer rather than used to keep reminder away.
- (32:22) [luna: strong; terra: strong; basis: root+scene] وَمَنْ أَظْلَمُ مِمَّن ذُكِّرَ بِـَٔايَٰتِ رَبِّهِۦ ثُمَّ أَعْرَضَ عَنْهَآ ۚ إِنَّا مِنَ ٱلْمُجْرِمِينَ مُنتَقِمُونَ
  Unverified discovery rationale: luna: It asks who is more unjust than one reminded of God's signs who then turns away, directly formulating the source's second response. | terra: The wrongdoer is reminded of his Lord's signs and then turns away from them, a compact statement of address followed by avoidance.
- (35:18) [luna: strong; terra: strong; basis: root+scene+speaker+theme] [cited in ¶67] وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ ۚ وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ ۗ إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ ۚ وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ ۚ وَإِلَى ٱللَّهِ ٱلْمَصِيرُ
  Unverified discovery rationale: luna: This ayah joins warning to those who fear their Lord unseen, establish prayer, and purify themselves; it gathers the source's 87:10, 14, and 15 links. | terra: Warning reaches those who fear their Lord unseen; the same ayah joins that fear to prayer and self-purification, unfolding the section's link forward to 87:14-15.
- (35:28) [luna: strong; terra: strong; basis: root+theme] [cited in ¶67] وَمِنَ ٱلنَّاسِ وَٱلدَّوَآبِّ وَٱلْأَنْعَٰمِ مُخْتَلِفٌ أَلْوَٰنُهُۥ كَذَٰلِكَ ۗ إِنَّمَا يَخْشَى ٱللَّهَ مِنْ عِبَادِهِ ٱلْعُلَمَٰٓؤُا۟ ۗ إِنَّ ٱللَّهَ عَزِيزٌ غَفُورٌ
  Unverified discovery rationale: luna: It says those with knowledge fear Allah, directly supporting the source's gloss that خشية usually arises from knowledge. | terra: Only the knowledgeable among God's servants truly يَخْشَى Him, stating directly the section's dictionary claim that reverent fear normally arises from knowledge.
- (35:36) [luna: strong; basis: contrast+scene] وَٱلَّذِينَ كَفَرُوا۟ لَهُمْ نَارُ جَهَنَّمَ لَا يُقْضَىٰ عَلَيْهِمْ فَيَمُوتُوا۟ وَلَا يُخَفَّفُ عَنْهُم مِّنْ عَذَابِهَا ۚ كَذَٰلِكَ نَجْزِى كُلَّ كَفُورٍۢ
  Unverified discovery rationale: luna: The unbelievers' fire is not ended by death and their punishment is not lightened, a close counterpart to the source's fire and no-life/no-death context.
- (35:37) [luna: strong; basis: root+scene] وَهُمْ يَصْطَرِخُونَ فِيهَا رَبَّنَآ أَخْرِجْنَا نَعْمَلْ صَٰلِحًا غَيْرَ ٱلَّذِى كُنَّا نَعْمَلُ ۚ أَوَلَمْ نُعَمِّرْكُم مَّا يَتَذَكَّرُ فِيهِ مَن تَذَكَّرَ وَجَآءَكُمُ ٱلنَّذِيرُ ۖ فَذُوقُوا۟ فَمَا لِلظَّٰلِمِينَ مِن نَّصِيرٍ
  Unverified discovery rationale: luna: The damned say that a warner came and that they had time to remember, directly tying the punishment to refusing the offered reminder.
- (36:10) [terra: strong; basis: contrast+scene+theme] وَسَوَآءٌ عَلَيْهِمْ ءَأَنذَرْتَهُمْ أَمْ لَمْ تُنذِرْهُمْ لَا يُؤْمِنُونَ
  Unverified discovery rationale: terra: Immediately before the fearful follower of 36:11, warning and not warning are equal for those who refuse belief, setting the two receptions side by side.
- (36:11) [luna: strong; terra: strong; basis: root+scene+speaker+theme] إِنَّمَا تُنذِرُ مَنِ ٱتَّبَعَ ٱلذِّكْرَ وَخَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ ۖ فَبَشِّرْهُ بِمَغْفِرَةٍۢ وَأَجْرٍۢ كَرِيمٍ
  Unverified discovery rationale: luna: The warning reaches one who follows the reminder and fears the Merciful unseen, a precise statement of the source's receptive audience. | terra: The Prophet can warn precisely the one who follows the Reminder and fears the Merciful unseen; fear is the disposition that lets the address arrive.
- (36:69) [terra: strong (missing-ayat turn); basis: root+speaker+theme] وَمَا عَلَّمْنَٰهُ ٱلشِّعْرَ وَمَا يَنۢبَغِى لَهُۥٓ ۚ إِنْ هُوَ إِلَّا ذِكْرٌۭ وَقُرْءَانٌۭ مُّبِينٌۭ
  Unverified discovery rationale: terra: The Prophet was not taught poetry; what he carries is remembrance and a clear recitation, defining the address he is commanded to transmit.
- (36:70) [terra: strong (missing-ayat turn); basis: neighbour+speaker+theme] لِّيُنذِرَ مَن كَانَ حَيًّۭا وَيَحِقَّ ٱلْقَوْلُ عَلَى ٱلْكَٰفِرِينَ
  Unverified discovery rationale: terra: That recitation warns whoever is alive and establishes the sentence against disbelievers, distinguishing a living receiver from one fixed in rejection.
- (37:13) [terra: strong (missing-ayat turn); basis: root+scene] وَإِذَا ذُكِّرُوا۟ لَا يَذْكُرُونَ
  Unverified discovery rationale: terra: When they are reminded, they do not remember, the shortest direct statement of the offered act failing to cross into its intended response.
- (39:9) [luna: strong; terra: strong; basis: contrast+root+scene+theme] أَمَّنْ هُوَ قَٰنِتٌ ءَانَآءَ ٱلَّيْلِ سَاجِدًۭا وَقَآئِمًۭا يَحْذَرُ ٱلْءَاخِرَةَ وَيَرْجُوا۟ رَحْمَةَ رَبِّهِۦ ۗ قُلْ هَلْ يَسْتَوِى ٱلَّذِينَ يَعْلَمُونَ وَٱلَّذِينَ لَا يَعْلَمُونَ ۗ إِنَّمَا يَتَذَكَّرُ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
  Unverified discovery rationale: luna: The one who stands in prayer fearing the Hereafter is set against the ignorant, joining the source's prayer, fear, and knowledge themes. | terra: The devout person fears the Hereafter, then the ayah contrasts those who know with those who do not and says only people of understanding remember.
- (39:17) [terra: strong; basis: contrast+root+scene] وَٱلَّذِينَ ٱجْتَنَبُوا۟ ٱلطَّٰغُوتَ أَن يَعْبُدُوهَا وَأَنَابُوٓا۟ إِلَى ٱللَّهِ لَهُمُ ٱلْبُشْرَىٰ ۚ فَبَشِّرْ عِبَادِ
  Unverified discovery rationale: terra: Those who يَجْتَنِبُوا۟ ٱلطَّاغُوتَ and turn to God receive good news, setting proper avoidance and receptive return against 87:11's misdirected avoidance.
- (39:18) [terra: strong; basis: neighbour+scene+theme] ٱلَّذِينَ يَسْتَمِعُونَ ٱلْقَوْلَ فَيَتَّبِعُونَ أَحْسَنَهُۥٓ ۚ أُو۟لَٰٓئِكَ ٱلَّذِينَ هَدَىٰهُمُ ٱللَّهُ ۖ وَأُو۟لَٰٓئِكَ هُمْ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
  Unverified discovery rationale: terra: These servants listen to speech and follow its best; God has guided them and they possess understanding, a full portrait of reminder being received through discernment.
- (39:22) [luna: strong; terra: strong; basis: contrast+root+scene] أَفَمَن شَرَحَ ٱللَّهُ صَدْرَهُۥ لِلْإِسْلَٰمِ فَهُوَ عَلَىٰ نُورٍۢ مِّن رَّبِّهِۦ ۚ فَوَيْلٌۭ لِّلْقَٰسِيَةِ قُلُوبُهُم مِّن ذِكْرِ ٱللَّهِ ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۢ مُّبِينٍ
  Unverified discovery rationale: luna: A heart opened to Islam and light is contrasted with hearts hardened against God's ذكر, directly portraying the source's two responses. | terra: Woe is pronounced upon hearts hardened against God's remembrance, the inward counterpart of the bodily distance in 87:11.
- (39:23) [luna: strong; terra: strong; basis: root+scene+theme] ٱللَّهُ نَزَّلَ أَحْسَنَ ٱلْحَدِيثِ كِتَٰبًۭا مُّتَشَٰبِهًۭا مَّثَانِىَ تَقْشَعِرُّ مِنْهُ جُلُودُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُمْ ثُمَّ تَلِينُ جُلُودُهُمْ وَقُلُوبُهُمْ إِلَىٰ ذِكْرِ ٱللَّهِ ۚ ذَٰلِكَ هُدَى ٱللَّهِ يَهْدِى بِهِۦ مَن يَشَآءُ ۚ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍ
  Unverified discovery rationale: luna: The revealed Qur'an makes the skins of those who fear their Lord shiver, then softens them to remembrance, a vivid scene of reminder received through fear. | terra: Those who fear their Lord first shiver at the best discourse and then soften in skin and heart toward God's remembrance; fear makes the reminder physically receivable.
- (39:24) [luna: strong; basis: contrast+scene] أَفَمَن يَتَّقِى بِوَجْهِهِۦ سُوٓءَ ٱلْعَذَابِ يَوْمَ ٱلْقِيَٰمَةِ ۚ وَقِيلَ لِلظَّٰلِمِينَ ذُوقُوا۟ مَا كُنتُمْ تَكْسِبُونَ
  Unverified discovery rationale: luna: The person shielding himself from the punishment with his face is asked whether he is like the secure; this makes the consequence of refusing reminder perceptible.
- (39:25) [luna: strong; basis: contrast+neighbour] كَذَّبَ ٱلَّذِينَ مِن قَبْلِهِمْ فَأَتَىٰهُمُ ٱلْعَذَابُ مِنْ حَيْثُ لَا يَشْعُرُونَ
  Unverified discovery rationale: luna: Earlier deniers were seized by punishment from where they did not expect, completing 39:24's image of exposure to punishment.
- (39:26) [luna: strong; basis: contrast+theme] فَأَذَاقَهُمُ ٱللَّهُ ٱلْخِزْىَ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَعَذَابُ ٱلْءَاخِرَةِ أَكْبَرُ ۚ لَوْ كَانُوا۟ يَعْلَمُونَ
  Unverified discovery rationale: luna: They taste humiliation in worldly life, while the afterlife punishment is greater, echoing the source's worldly/abiding contrast.
- (39:27) [terra: strong; basis: root+theme] وَلَقَدْ ضَرَبْنَا لِلنَّاسِ فِى هَٰذَا ٱلْقُرْءَانِ مِن كُلِّ مَثَلٍۢ لَّعَلَّهُمْ يَتَذَكَّرُونَ
  Unverified discovery rationale: terra: God sets out every kind of example in the Quran so that people may remember, describing varied presentation as service to reception.
- (39:28) [terra: strong; basis: neighbour+root+theme] قُرْءَانًا عَرَبِيًّا غَيْرَ ذِى عِوَجٍۢ لَّعَلَّهُمْ يَتَّقُونَ
  Unverified discovery rationale: terra: The Quran is Arabic and without crookedness so that they may fear, pairing clarity of address with the fear it seeks to form.
- (39:41) [luna: strong (missing-ayat turn); basis: speaker+theme] إِنَّآ أَنزَلْنَا عَلَيْكَ ٱلْكِتَٰبَ لِلنَّاسِ بِٱلْحَقِّ ۖ فَمَنِ ٱهْتَدَىٰ فَلِنَفْسِهِۦ ۖ وَمَن ضَلَّ فَإِنَّمَا يَضِلُّ عَلَيْهَا ۖ وَمَآ أَنتَ عَلَيْهِم بِوَكِيلٍ
  Unverified discovery rationale: luna: The one guided by the Book benefits himself and the one who strays harms himself, while the Prophet is no guardian over them; this joins the source's benefit/harm distinction to its limit on the reminder-giver.
- (39:45) [luna: strong; terra: strong; basis: contrast+root+scene] وَإِذَا ذُكِرَ ٱللَّهُ وَحْدَهُ ٱشْمَأَزَّتْ قُلُوبُ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ ۖ وَإِذَا ذُكِرَ ٱلَّذِينَ مِن دُونِهِۦٓ إِذَا هُمْ يَسْتَبْشِرُونَ
  Unverified discovery rationale: luna: When Allah alone is mentioned, those who deny the Hereafter recoil, a concrete negative response to remembrance opposite 87:15. | terra: Hearts that do not believe in the Hereafter recoil when God alone is mentioned, while other objects delight them; avoidance is exposed by its selective object.
- (39:54) [terra: strong (missing-ayat turn); basis: scene+theme] وَأَنِيبُوٓا۟ إِلَىٰ رَبِّكُمْ وَأَسْلِمُوا۟ لَهُۥ مِن قَبْلِ أَن يَأْتِيَكُمُ ٱلْعَذَابُ ثُمَّ لَا تُنصَرُونَ
  Unverified discovery rationale: terra: Hearers are urged to turn back and submit before punishment comes, presenting timely reception as still open.
- (39:55) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] وَٱتَّبِعُوٓا۟ أَحْسَنَ مَآ أُنزِلَ إِلَيْكُم مِّن رَّبِّكُم مِّن قَبْلِ أَن يَأْتِيَكُمُ ٱلْعَذَابُ بَغْتَةًۭ وَأَنتُمْ لَا تَشْعُرُونَ
  Unverified discovery rationale: terra: They must follow the best of what was sent down before punishment arrives unexpectedly, specifying the action by which reminder benefits.
- (39:56) [luna: medium; terra: strong (missing-ayat turn); basis: neighbour+root+theme] أَن تَقُولَ نَفْسٌۭ يَٰحَسْرَتَىٰ عَلَىٰ مَا فَرَّطتُ فِى جَنۢبِ ٱللَّهِ وَإِن كُنتُ لَمِنَ ٱلسَّٰخِرِينَ
  Unverified discovery rationale: luna: The source's ج ن ب distance sense echoes فَرَّطتُ فِي جَنبِ اللَّهِ, regret for neglecting what is due to God; this is a plausible figurative link to keeping reminder at a distance. | terra: A soul will regret what it neglected concerning God and confess that it mocked, showing late knowledge of the reminder it kept distant.
- (39:57) [terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] أَوْ تَقُولَ لَوْ أَنَّ ٱللَّهَ هَدَىٰنِى لَكُنتُ مِنَ ٱلْمُتَّقِينَ
  Unverified discovery rationale: terra: The soul will claim that divine guidance would have made it God-conscious, directly opposing guidance and fear to its realized rejection.
- (39:58) [terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] أَوْ تَقُولَ حِينَ تَرَى ٱلْعَذَابَ لَوْ أَنَّ لِى كَرَّةًۭ فَأَكُونَ مِنَ ٱلْمُحْسِنِينَ
  Unverified discovery rationale: terra: At sight of punishment it asks for a return so that it may do good, another late wish for the beneficial response once the opportunity has passed.
- (41:4) [luna: strong; terra: strong; basis: scene+speaker+theme] بَشِيرًۭا وَنَذِيرًۭا فَأَعْرَضَ أَكْثَرُهُمْ فَهُمْ لَا يَسْمَعُونَ
  Unverified discovery rationale: luna: The Messenger brings good news and warning, while most people turn away and do not hear; this directly stages reminder and refusal. | terra: The Quran bears good news and warning, yet most turn away and do not listen, locating failure in the response to an intelligible address.
- (41:5) [luna: strong; terra: strong; basis: contrast+neighbour+scene] وَقَالُوا۟ قُلُوبُنَا فِىٓ أَكِنَّةٍۢ مِّمَّا تَدْعُونَآ إِلَيْهِ وَفِىٓ ءَاذَانِنَا وَقْرٌۭ وَمِنۢ بَيْنِنَا وَبَيْنِكَ حِجَابٌۭ فَٱعْمَلْ إِنَّنَا عَٰمِلُونَ
  Unverified discovery rationale: luna: The hearers claim their hearts are covered and their ears stopped, making their distance from the offered message explicit. | terra: The avoiders claim covered hearts, deaf ears, and a barrier between themselves and the Prophet, verbalizing the distance they maintain from reminder.
- (41:13) [luna: strong; basis: contrast+speaker] فَإِنْ أَعْرَضُوا۟ فَقُلْ أَنذَرْتُكُمْ صَٰعِقَةًۭ مِّثْلَ صَٰعِقَةِ عَادٍۢ وَثَمُودَ
  Unverified discovery rationale: luna: If the audience turns away, the Prophet must say he warned them of a thunderbolt like those of Aad and Thamud; this gives the rejecter's consequence.
- (41:26) [terra: strong; basis: contrast+scene] وَقَالَ ٱلَّذِينَ كَفَرُوا۟ لَا تَسْمَعُوا۟ لِهَٰذَا ٱلْقُرْءَانِ وَٱلْغَوْا۟ فِيهِ لَعَلَّكُمْ تَغْلِبُونَ
  Unverified discovery rationale: terra: Disbelievers command one another not to listen to the Quran and to drown it out, an active strategy for preventing reminder from crossing to them.
- (41:51) [terra: strong; basis: root+scene+theme] وَإِذَآ أَنْعَمْنَا عَلَى ٱلْإِنسَٰنِ أَعْرَضَ وَنَـَٔا بِجَانِبِهِۦ وَإِذَا مَسَّهُ ٱلشَّرُّ فَذُو دُعَآءٍ عَرِيضٍۢ
  Unverified discovery rationale: terra: When God favors a person he turns away and distances his side, while harm produces long supplication; benefit exposes the same self-distancing posture named in the section.
- (43:5) [terra: strong; basis: root+speaker+theme] أَفَنَضْرِبُ عَنكُمُ ٱلذِّكْرَ صَفْحًا أَن كُنتُمْ قَوْمًۭا مُّسْرِفِينَ
  Unverified discovery rationale: terra: God asks whether He should withhold the Reminder because the addressees are excessive, directly raising whether rejection should stop the act of reminding.
- (43:36) [luna: strong (missing-ayat turn); terra: strong; basis: root+scene+theme] وَمَن يَعْشُ عَن ذِكْرِ ٱلرَّحْمَٰنِ نُقَيِّضْ لَهُۥ شَيْطَٰنًۭا فَهُوَ لَهُۥ قَرِينٌۭ
  Unverified discovery rationale: luna: Whoever turns away from the remembrance of the Merciful is assigned a devil as companion, directly extending the source's image of keeping reminder at a distance. | terra: Whoever turns blindly away from the Merciful's remembrance is assigned a satanic companion, giving the section's distancing posture an inward consequence.
- (43:37) [luna: strong (missing-ayat turn); basis: neighbour+scene] وَإِنَّهُمْ لَيَصُدُّونَهُمْ عَنِ ٱلسَّبِيلِ وَيَحْسَبُونَ أَنَّهُم مُّهْتَدُونَ
  Unverified discovery rationale: luna: The devils turn their companions from the way while they think they are guided; this completes 43:36's consequence for turning from remembrance.
- (43:44) [terra: strong (missing-ayat turn); basis: root+theme] وَإِنَّهُۥ لَذِكْرٌۭ لَّكَ وَلِقَوْمِكَ ۖ وَسَوْفَ تُسْـَٔلُونَ
  Unverified discovery rationale: terra: The Quran is a reminder for the Prophet and his people for which they will be questioned, making reception a responsibility rather than passive exposure.
- (44:13) [terra: strong; basis: contrast+root+theme] أَنَّىٰ لَهُمُ ٱلذِّكْرَىٰ وَقَدْ جَآءَهُمْ رَسُولٌۭ مُّبِينٌۭ
  Unverified discovery rationale: terra: God asks how reminder can now avail them when a clarifying messenger had already come, another scene of benefit sought only after its proper moment.
- (44:14) [terra: strong; basis: contrast+neighbour+scene] ثُمَّ تَوَلَّوْا۟ عَنْهُ وَقَالُوا۟ مُعَلَّمٌۭ مَّجْنُونٌ
  Unverified discovery rationale: terra: They turned away from that messenger and called him instructed or mad, specifying the prior refusal that makes their late appeal empty.
- (44:58) [terra: strong; basis: root+speaker+theme] فَإِنَّمَا يَسَّرْنَٰهُ بِلِسَانِكَ لَعَلَّهُمْ يَتَذَكَّرُونَ
  Unverified discovery rationale: terra: God says He has made the Quran easy in the Prophet's tongue so that they may remember, linking the speaker's delivery to hoped-for reception.
- (45:8) [luna: strong; terra: strong; basis: contrast+scene+theme] يَسْمَعُ ءَايَٰتِ ٱللَّهِ تُتْلَىٰ عَلَيْهِ ثُمَّ يُصِرُّ مُسْتَكْبِرًۭا كَأَن لَّمْ يَسْمَعْهَا ۖ فَبَشِّرْهُ بِعَذَابٍ أَلِيمٍۢ
  Unverified discovery rationale: luna: The man hears God's signs recited but persists proudly as if he had not heard, a precise instance of keeping reminder at a distance. | terra: The sinner hears God's signs and then persists arrogantly as though he did not hear them, another exact form of letting reminder pass without entrance.
- (45:9) [luna: strong; terra: strong (missing-ayat turn); basis: contrast+scene] وَإِذَا عَلِمَ مِنْ ءَايَٰتِنَا شَيْـًٔا ٱتَّخَذَهَا هُزُوًا ۚ أُو۟لَٰٓئِكَ لَهُمْ عَذَابٌۭ مُّهِينٌۭ
  Unverified discovery rationale: luna: He takes the signs in mockery, and humiliating punishment is promised; this turns the refusal in 45:8 into consequence. | terra: When the arrogant hearer learns any of God's signs, he takes them in mockery, an active misuse of the knowledge that should have produced fear.
- (45:10) [luna: strong; basis: contrast+neighbour] مِّن وَرَآئِهِمْ جَهَنَّمُ ۖ وَلَا يُغْنِى عَنْهُم مَّا كَسَبُوا۟ شَيْـًۭٔا وَلَا مَا ٱتَّخَذُوا۟ مِن دُونِ ٱللَّهِ أَوْلِيَآءَ ۖ وَلَهُمْ عَذَابٌ عَظِيمٌ
  Unverified discovery rationale: luna: Hell awaits those described in 45:8–9, completing the refused signs' consequence and echoing the source's fire.
- (45:23) [luna: strong; basis: contrast+theme] أَفَرَءَيْتَ مَنِ ٱتَّخَذَ إِلَٰهَهُۥ هَوَىٰهُ وَأَضَلَّهُ ٱللَّهُ عَلَىٰ عِلْمٍۢ وَخَتَمَ عَلَىٰ سَمْعِهِۦ وَقَلْبِهِۦ وَجَعَلَ عَلَىٰ بَصَرِهِۦ غِشَٰوَةًۭ فَمَن يَهْدِيهِ مِنۢ بَعْدِ ٱللَّهِ ۚ أَفَلَا تَذَكَّرُونَ
  Unverified discovery rationale: luna: The one who makes desire his god is left astray despite knowledge and has hearing and heart sealed, a specific inward refusal of guidance.
- (45:24) [luna: strong; basis: contrast+theme] وَقَالُوا۟ مَا هِىَ إِلَّا حَيَاتُنَا ٱلدُّنْيَا نَمُوتُ وَنَحْيَا وَمَا يُهْلِكُنَآ إِلَّا ٱلدَّهْرُ ۚ وَمَا لَهُم بِذَٰلِكَ مِنْ عِلْمٍ ۖ إِنْ هُمْ إِلَّا يَظُنُّونَ
  Unverified discovery rationale: luna: They claim only worldly life exists and deny resurrection, the opposite of 87:17's better, abiding Hereafter.
- (47:16) [terra: strong; basis: contrast+scene+theme] وَمِنْهُم مَّن يَسْتَمِعُ إِلَيْكَ حَتَّىٰٓ إِذَا خَرَجُوا۟ مِنْ عِندِكَ قَالُوا۟ لِلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ مَاذَا قَالَ ءَانِفًا ۚ أُو۟لَٰٓئِكَ ٱلَّذِينَ طَبَعَ ٱللَّهُ عَلَىٰ قُلُوبِهِمْ وَٱتَّبَعُوٓا۟ أَهْوَآءَهُمْ
  Unverified discovery rationale: terra: Some listen to the Prophet but leave asking the knowledgeable what he just said; sealed hearts turn physical hearing into failed reception.
- (47:17) [terra: strong; basis: neighbour+scene+theme] وَٱلَّذِينَ ٱهْتَدَوْا۟ زَادَهُمْ هُدًۭى وَءَاتَىٰهُمْ تَقْوَىٰهُمْ
  Unverified discovery rationale: terra: Those already guided instead receive increased guidance and their God-consciousness, the beneficial reception paired with 47:16.
- (47:23) [terra: strong (missing-ayat turn); basis: scene+theme] أُو۟لَٰٓئِكَ ٱلَّذِينَ لَعَنَهُمُ ٱللَّهُ فَأَصَمَّهُمْ وَأَعْمَىٰٓ أَبْصَٰرَهُمْ
  Unverified discovery rationale: terra: Those who turn back are cursed, deafened, and blinded, so their withdrawal from obedience becomes an incapacity to receive address.
- (47:24) [terra: strong (missing-ayat turn); basis: neighbour+root+scene] أَفَلَا يَتَدَبَّرُونَ ٱلْقُرْءَانَ أَمْ عَلَىٰ قُلُوبٍ أَقْفَالُهَآ
  Unverified discovery rationale: terra: The question whether they ponder the Quran or have locks on their hearts locates failed reception behind an inwardly barred door.
- (50:45) [luna: strong; terra: strong; basis: root+scene+speaker+theme] [cited in ¶67] نَّحْنُ أَعْلَمُ بِمَا يَقُولُونَ ۖ وَمَآ أَنتَ عَلَيْهِم بِجَبَّارٍۢ ۖ فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ
  Unverified discovery rationale: luna: The Prophet is told to remind with the Qur'an whoever fears God's warning, joining the section's reminder, fearful recipient, and preacher's role. | terra: The command فَذَكِّرْ بِٱلْقُرْءَانِ targets whoever fears God's threat, matching both the section's speaker and its fear-defined hearer.
- (51:55) [luna: strong; terra: strong; basis: root+speaker+theme] [cited in ¶67] وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ
  Unverified discovery rationale: luna: The command to remind is followed by the claim that the reminder benefits believers, directly echoing the source section's ذ ك ر and ن ف ع. | terra: The same command to the Prophet, وَذَكِّرْ, is justified because the reminder benefits believers, making explicit who receives its good.
- (53:29) [luna: strong (missing-ayat turn); terra: strong; basis: contrast+root+scene+theme] فَأَعْرِضْ عَن مَّن تَوَلَّىٰ عَن ذِكْرِنَا وَلَمْ يُرِدْ إِلَّا ٱلْحَيَوٰةَ ٱلدُّنْيَا
  Unverified discovery rationale: luna: The command describes people who turn away from God's remembrance and desire only worldly life, a near-exact pairing of the source section's avoider with its surah's later worldly-life contrast. | terra: The Prophet must turn from whoever turns from God's remembrance and wants only the nearer life, joining avoidance of reminder to the preference named in 87:16.
- (53:30) [terra: strong; basis: neighbour+root+theme] ذَٰلِكَ مَبْلَغُهُم مِّنَ ٱلْعِلْمِ ۚ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ وَهُوَ أَعْلَمُ بِمَنِ ٱهْتَدَىٰ
  Unverified discovery rationale: terra: That preference is called the limit of their knowledge, while God knows who strays and who is guided; deficient knowledge explains deficient fear.
- (53:32) [terra: strong; basis: contrast+root] ٱلَّذِينَ يَجْتَنِبُونَ كَبَٰٓئِرَ ٱلْإِثْمِ وَٱلْفَوَٰحِشَ إِلَّا ٱللَّمَمَ ۚ إِنَّ رَبَّكَ وَٰسِعُ ٱلْمَغْفِرَةِ ۚ هُوَ أَعْلَمُ بِكُمْ إِذْ أَنشَأَكُم مِّنَ ٱلْأَرْضِ وَإِذْ أَنتُمْ أَجِنَّةٌۭ فِى بُطُونِ أُمَّهَٰتِكُمْ ۖ فَلَا تُزَكُّوٓا۟ أَنفُسَكُمْ ۖ هُوَ أَعْلَمُ بِمَنِ ٱتَّقَىٰٓ
  Unverified discovery rationale: terra: Those who avoid major sins and indecencies use the section's distance-root for salutary restraint, a boundary against treating all avoidance as wretched.
- (54:4) [terra: strong; basis: scene+theme] وَلَقَدْ جَآءَهُم مِّنَ ٱلْأَنۢبَآءِ مَا فِيهِ مُزْدَجَرٌ
  Unverified discovery rationale: terra: Reports containing deterrence have already reached the rejecters, establishing that their failure is not want of warning.
- (54:5) [terra: strong; basis: contrast+theme] حِكْمَةٌۢ بَٰلِغَةٌۭ ۖ فَمَا تُغْنِ ٱلنُّذُرُ
  Unverified discovery rationale: terra: Although consummate wisdom has reached them, the warnings do not avail; this states the negative case presupposed by “if the reminder benefits.”
- (54:6) [terra: strong; basis: neighbour+scene+speaker] فَتَوَلَّ عَنْهُمْ ۘ يَوْمَ يَدْعُ ٱلدَّاعِ إِلَىٰ شَىْءٍۢ نُّكُرٍ
  Unverified discovery rationale: terra: After warnings fail, the Prophet is told to turn away from them until the summoner calls to something terrible, marking the endpoint of unreceived reminder.
- (54:17) [luna: strong (missing-ayat turn); terra: strong; basis: root+theme] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
  Unverified discovery rationale: luna: The Qur'an is made easy for remembrance and the ayah asks who will take heed, echoing the source's beneficial reminder and the receptive listener. | terra: God has made the Quran easy for remembrance and asks whether anyone will remember, joining divine facilitation to the hearer's needed response.
- (54:22) [luna: strong (missing-ayat turn); terra: strong; basis: root+theme] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
  Unverified discovery rationale: luna: This repeated refrain again asks whether anyone will take heed after the account of Aad, making it a distinct recurrence of the source's reminder-and-response pattern. | terra: The repeated offer that the Quran is made easy for remembrance makes the question of an actual receiver recur after another warning narrative.
- (54:32) [luna: strong (missing-ayat turn); terra: strong; basis: root+theme] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
  Unverified discovery rationale: luna: The same refrain follows the account of Thamud, another distinct recurrence of the question whether a listener will receive the reminder. | terra: Again the Quran's ease for remembrance is paired with the open question of who will receive it, echoing 87:8-10.
- (54:40) [luna: strong (missing-ayat turn); terra: strong; basis: neighbour+root+theme] وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ فَهَلْ مِن مُّدَّكِرٍۢ
  Unverified discovery rationale: luna: This refrain follows the account of Lut's people and asks who will take heed; Pharaoh's people come next in 54:41–42, adding a parallel warning scene to the source's Pharaoh connection. | terra: The fourth refrain insists that facilitated reminder remains an offer requiring someone who remembers.
- (57:16) [luna: strong; terra: strong; basis: root+scene+theme] ۞ أَلَمْ يَأْنِ لِلَّذِينَ ءَامَنُوٓا۟ أَن تَخْشَعَ قُلُوبُهُمْ لِذِكْرِ ٱللَّهِ وَمَا نَزَلَ مِنَ ٱلْحَقِّ وَلَا يَكُونُوا۟ كَٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ مِن قَبْلُ فَطَالَ عَلَيْهِمُ ٱلْأَمَدُ فَقَسَتْ قُلُوبُهُمْ ۖ وَكَثِيرٌۭ مِّنْهُمْ فَٰسِقُونَ
  Unverified discovery rationale: luna: Believers' hearts are asked to humble to God's remembrance and revealed truth, contrasting receptivity with hardened distance from reminder. | terra: Believers are asked whether it is time for their hearts to humble to God's remembrance and revealed truth, treating reception as an inward softening that can be delayed.
- (59:18) [luna: strong; basis: speaker+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱتَّقُوا۟ ٱللَّهَ وَلْتَنظُرْ نَفْسٌۭ مَّا قَدَّمَتْ لِغَدٍۢ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ خَبِيرٌۢ بِمَا تَعْمَلُونَ
  Unverified discovery rationale: luna: Believers are told to fear Allah and consider what they sent ahead for tomorrow, linking fear to knowledge of the coming Day.
- (59:19) [luna: strong; basis: contrast+root] وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَسُوا۟ ٱللَّهَ فَأَنسَىٰهُمْ أَنفُسَهُمْ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلْفَٰسِقُونَ
  Unverified discovery rationale: luna: Those who forget Allah are made to forget themselves, a direct contrary to the source's reminder and remembrance theme.
- (59:21) [luna: strong; terra: contrast; basis: contrast+scene+theme] لَوْ أَنزَلْنَا هَٰذَا ٱلْقُرْءَانَ عَلَىٰ جَبَلٍۢ لَّرَأَيْتَهُۥ خَٰشِعًۭا مُّتَصَدِّعًۭا مِّنْ خَشْيَةِ ٱللَّهِ ۚ وَتِلْكَ ٱلْأَمْثَٰلُ نَضْرِبُهَا لِلنَّاسِ لَعَلَّهُمْ يَتَفَكَّرُونَ
  Unverified discovery rationale: luna: If the Qur'an descended on a mountain it would humble and split from fear of Allah; this vividly shows the knowledge-born awe named in the source. | terra: A mountain would humble and split from fear of God if this Quran descended upon it; its imagined reception exposes the human hardness that lets reminder pass.
- (62:9) [luna: strong; terra: medium (missing-ayat turn); basis: root+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا نُودِىَ لِلصَّلَوٰةِ مِن يَوْمِ ٱلْجُمُعَةِ فَٱسْعَوْا۟ إِلَىٰ ذِكْرِ ٱللَّهِ وَذَرُوا۟ ٱلْبَيْعَ ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: luna: At the call to Friday prayer, people must leave trade and hasten to remembrance, linking the source's prayer and remembrance against worldly distraction. | terra: At the call to Friday prayer believers must hasten to God's remembrance, directly placing movement toward remembrance inside movement toward prayer.
- (62:10) [luna: strong; basis: root+theme] فَإِذَا قُضِيَتِ ٱلصَّلَوٰةُ فَٱنتَشِرُوا۟ فِى ٱلْأَرْضِ وَٱبْتَغُوا۟ مِن فَضْلِ ٱللَّهِ وَٱذْكُرُوا۟ ٱللَّهَ كَثِيرًۭا لَّعَلَّكُمْ تُفْلِحُونَ
  Unverified discovery rationale: luna: After prayer, people may seek God's provision while remembering Him much, showing how worldly provision can coexist with the remembrance the source contrasts with preference for dunya.
- (62:11) [luna: strong; basis: contrast+scene] وَإِذَا رَأَوْا۟ تِجَٰرَةً أَوْ لَهْوًا ٱنفَضُّوٓا۟ إِلَيْهَا وَتَرَكُوكَ قَآئِمًۭا ۚ قُلْ مَا عِندَ ٱللَّهِ خَيْرٌۭ مِّنَ ٱللَّهْوِ وَمِنَ ٱلتِّجَٰرَةِ ۚ وَٱللَّهُ خَيْرُ ٱلرَّٰزِقِينَ
  Unverified discovery rationale: luna: The congregation disperses toward trade and amusement, leaving the Prophet standing; this concretely stages worldly distraction from reminder and prayer.
- (63:9) [luna: strong; terra: medium; basis: contrast+root+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُلْهِكُمْ أَمْوَٰلُكُمْ وَلَآ أَوْلَٰدُكُمْ عَن ذِكْرِ ٱللَّهِ ۚ وَمَن يَفْعَلْ ذَٰلِكَ فَأُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ
  Unverified discovery rationale: luna: Believers are warned not to let wealth and children distract them from remembrance of Allah; those who do so are losers, echoing 87:16's worldly preference. | terra: Believers are warned not to let wealth and children distract them from God's remembrance, for those who do are the losers; distance can arise through absorbed attention.
- (65:2) [terra: strong; basis: root+theme] فَإِذَا بَلَغْنَ أَجَلَهُنَّ فَأَمْسِكُوهُنَّ بِمَعْرُوفٍ أَوْ فَارِقُوهُنَّ بِمَعْرُوفٍۢ وَأَشْهِدُوا۟ ذَوَىْ عَدْلٍۢ مِّنكُمْ وَأَقِيمُوا۟ ٱلشَّهَٰدَةَ لِلَّهِ ۚ ذَٰلِكُمْ يُوعَظُ بِهِۦ مَن كَانَ يُؤْمِنُ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ ۚ وَمَن يَتَّقِ ٱللَّهَ يَجْعَل لَّهُۥ مَخْرَجًۭا
  Unverified discovery rationale: terra: The legal instruction is an admonition to one who believes in God and the Last Day, and the same ayah promises an exit to one who fears God; reminder and fear govern action.
- (65:10) [terra: strong; basis: root+speaker+theme] أَعَدَّ ٱللَّهُ لَهُمْ عَذَابًۭا شَدِيدًۭا ۖ فَٱتَّقُوا۟ ٱللَّهَ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ ٱلَّذِينَ ءَامَنُوا۟ ۚ قَدْ أَنزَلَ ٱللَّهُ إِلَيْكُمْ ذِكْرًۭا
  Unverified discovery rationale: terra: People of understanding who believe are told to fear God because He has sent them a Reminder, joining knowledge, fear, and the arrival of address.
- (65:11) [terra: strong; basis: neighbour+root+scene] رَّسُولًۭا يَتْلُوا۟ عَلَيْكُمْ ءَايَٰتِ ٱللَّهِ مُبَيِّنَٰتٍۢ لِّيُخْرِجَ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ ۚ وَمَن يُؤْمِنۢ بِٱللَّهِ وَيَعْمَلْ صَٰلِحًۭا يُدْخِلْهُ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ قَدْ أَحْسَنَ ٱللَّهُ لَهُۥ رِزْقًا
  Unverified discovery rationale: terra: The Reminder is embodied in a messenger reciting clear signs to bring believers from darkness into light, showing how reminder crosses to and benefits another.
- (67:9) [luna: strong; basis: contrast+scene] قَالُوا۟ بَلَىٰ قَدْ جَآءَنَا نَذِيرٌۭ فَكَذَّبْنَا وَقُلْنَا مَا نَزَّلَ ٱللَّهُ مِن شَىْءٍ إِنْ أَنتُمْ إِلَّا فِى ضَلَٰلٍۢ كَبِيرٍۢ
  Unverified discovery rationale: luna: The people in the Fire admit a warner came and they denied him, directly connecting refusal of warning with the source's wretched outcome.
- (67:10) [luna: strong; basis: neighbour+scene] وَقَالُوا۟ لَوْ كُنَّا نَسْمَعُ أَوْ نَعْقِلُ مَا كُنَّا فِىٓ أَصْحَٰبِ ٱلسَّعِيرِ
  Unverified discovery rationale: luna: They say that listening or reasoning would have kept them from the Blaze, completing the admission in 67:9 and the source's contrast of hearers.
- (67:11) [luna: strong; basis: contrast+neighbour] فَٱعْتَرَفُوا۟ بِذَنۢبِهِمْ فَسُحْقًۭا لِّأَصْحَٰبِ ٱلسَّعِيرِ
  Unverified discovery rationale: luna: They acknowledge their sin in the Fire, completing 67:9–10's rejected warning and its consequence.
- (67:12) [luna: strong; terra: medium; basis: contrast+root+theme] إِنَّ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ لَهُم مَّغْفِرَةٌۭ وَأَجْرٌۭ كَبِيرٌۭ
  Unverified discovery rationale: luna: Those who fear their Lord unseen receive forgiveness and great reward, the positive counterpart to the deniers in 67:9–11 and to the source's listener. | terra: Those who fear their Lord unseen receive forgiveness and great reward, confirming the ultimate felicity of the section's fear-defined hearer.
- (68:51) [terra: strong (missing-ayat turn); basis: contrast+root+scene] وَإِن يَكَادُ ٱلَّذِينَ كَفَرُوا۟ لَيُزْلِقُونَكَ بِأَبْصَٰرِهِمْ لَمَّا سَمِعُوا۟ ٱلذِّكْرَ وَيَقُولُونَ إِنَّهُۥ لَمَجْنُونٌۭ
  Unverified discovery rationale: terra: When disbelievers hear the Reminder, they nearly make the Prophet slip with their hostile looks and call him mad, an aggressive response to the same offered address.
- (68:52) [terra: strong (missing-ayat turn); basis: neighbour+root] وَمَا هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
  Unverified discovery rationale: terra: The passage answers that the revelation is nothing but a reminder to the worlds, preserving its identity despite the hearers' accusation.
- (69:12) [terra: strong; basis: root+scene+theme] لِنَجْعَلَهَا لَكُمْ تَذْكِرَةًۭ وَتَعِيَهَآ أُذُنٌۭ وَٰعِيَةٌۭ
  Unverified discovery rationale: terra: God makes the saving event a reminder and says a retaining ear may retain it, an anatomical image of reminder crossing to and lodging in a hearer.
- (69:48) [luna: strong (missing-ayat turn); basis: root+theme] وَإِنَّهُۥ لَتَذْكِرَةٌۭ لِّلْمُتَّقِينَ
  Unverified discovery rationale: luna: The Qur'an is called a reminder for the God-conscious, joining the source's reminder to the fearful, receptive audience.
- (71:5) [terra: strong (missing-ayat turn); basis: scene+speaker] قَالَ رَبِّ إِنِّى دَعَوْتُ قَوْمِى لَيْلًۭا وَنَهَارًۭا
  Unverified discovery rationale: terra: Noah says he called his people by night and day, establishing the persistence of the reminder-bearer toward a refusing audience.
- (71:6) [terra: strong (missing-ayat turn); basis: contrast+neighbour+scene] فَلَمْ يَزِدْهُمْ دُعَآءِىٓ إِلَّا فِرَارًۭا
  Unverified discovery rationale: terra: His calling only increases their flight, a bodily intensification of keeping the offered reminder distant.
- (71:7) [terra: strong (missing-ayat turn); basis: contrast+neighbour+scene] وَإِنِّى كُلَّمَا دَعَوْتُهُمْ لِتَغْفِرَ لَهُمْ جَعَلُوٓا۟ أَصَٰبِعَهُمْ فِىٓ ءَاذَانِهِمْ وَٱسْتَغْشَوْا۟ ثِيَابَهُمْ وَأَصَرُّوا۟ وَٱسْتَكْبَرُوا۟ ٱسْتِكْبَارًۭا
  Unverified discovery rationale: terra: They put fingers in ears, cover themselves, persist, and act arrogantly whenever called to forgiveness, detailing the mechanics of nonreception.
- (72:17) [terra: strong; basis: root+theme] لِّنَفْتِنَهُمْ فِيهِ ۚ وَمَن يُعْرِضْ عَن ذِكْرِ رَبِّهِۦ يَسْلُكْهُ عَذَابًۭا صَعَدًۭا
  Unverified discovery rationale: terra: Whoever turns away from his Lord's remembrance is driven into mounting punishment, connecting avoidance of reminder with the wretched end.
- (72:21) [luna: strong (missing-ayat turn); terra: strong; basis: root+speaker+theme] قُلْ إِنِّى لَآ أَمْلِكُ لَكُمْ ضَرًّۭا وَلَا رَشَدًۭا
  Unverified discovery rationale: luna: The Messenger says he cannot control harm or right guidance for his hearers, clarifying the source's contrast between offering a potentially beneficial reminder and controlling its effect. | terra: The Prophet says he controls neither harm nor right guidance for his hearers, a precise boundary on what the one who presents reminder can produce in another.
- (73:19) [luna: strong (missing-ayat turn); terra: medium; basis: root+scene+theme] إِنَّ هَٰذِهِۦ تَذْكِرَةٌۭ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ سَبِيلًا
  Unverified discovery rationale: luna: The passage calls itself a reminder and says whoever wills may take a way to the Lord, a direct formulation of reminder and response. | terra: The revelation is called a reminder, and whoever wills may take a path to his Lord; reminder is an offered route whose use belongs to the hearer.
- (74:42) [luna: strong (missing-ayat turn); terra: strong; basis: neighbour+scene] مَا سَلَكَكُمْ فِى سَقَرَ
  Unverified discovery rationale: luna: The people in Saqar are asked what brought them there; this opens the account in which the next ayah names abandoned prayer, the source's explicit lexical echo from ج ن ب. | terra: The people of the Garden ask what brought the condemned into Saqar, opening the account that soon culminates in turning from reminder.
- (74:43) [luna: strong (missing-ayat turn); terra: strong; basis: neighbour+root+scene+theme] قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ
  Unverified discovery rationale: luna: The people in Saqar say they were not among those who prayed, directly illustrating the source's stated echo between avoidance from ج ن ب and distance from prayer. | terra: Their first answer is that they were not among those who prayed, confirming the section's developed echo between avoiding reminder and distance from prayer.
- (74:46) [luna: strong (missing-ayat turn); terra: strong (missing-ayat turn); basis: contrast+neighbour+scene+theme] وَكُنَّا نُكَذِّبُ بِيَوْمِ ٱلدِّينِ
  Unverified discovery rationale: luna: They say they denied the Day of Judgment, a concrete form of rejecting the Hereafter against which the source's remembered, abiding Hereafter stands. | terra: The people of Saqar confess that they denied the Day of Judgment, supplying the lack of eschatological fear later named in 74:53.
- (74:47) [luna: strong (missing-ayat turn); basis: neighbour+scene] حَتَّىٰٓ أَتَىٰنَا ٱلْيَقِينُ
  Unverified discovery rationale: luna: They say certainty came to them, completing 74:46's denial with the arrival of death before their regret.
- (74:48) [luna: strong (missing-ayat turn); basis: contrast+theme] فَمَا تَنفَعُهُمْ شَفَٰعَةُ ٱلشَّٰفِعِينَ
  Unverified discovery rationale: luna: Intercession will not benefit them, extending the source's harm/benefit distinction into the fate of those in Saqar.
- (74:49) [luna: strong; terra: strong; basis: root+scene] فَمَا لَهُمْ عَنِ ٱلتَّذْكِرَةِ مُعْرِضِينَ
  Unverified discovery rationale: luna: The ayah asks why people turn away from the reminder, naming the same avoidant act described by the source's ج ن ب root. | terra: The question فَمَا لَهُمْ عَنِ ٱلتَّذْكِرَةِ مُعْرِضِينَ names the same inexplicable turning away from reminder.
- (74:50) [luna: strong; terra: strong; basis: neighbour+scene] كَأَنَّهُمْ حُمُرٌۭ مُّسْتَنفِرَةٌۭ
  Unverified discovery rationale: luna: The fleeing wild asses picture the people who turn away in 74:49; the image makes avoidance of reminder visible, while the source describes a quieter distancing. | terra: The avoiders are pictured as startled wild asses, giving bodily motion to the section's verb of keeping away.
- (74:51) [luna: strong; terra: strong; basis: neighbour+scene] فَرَّتْ مِن قَسْوَرَةٍۭ
  Unverified discovery rationale: luna: The asses flee from a lion, completing 74:50's image for the people turning away from reminder in 74:49. | terra: Their flight from a lion completes the simile: reminder is not refuted but fled from.
- (74:53) [luna: strong; terra: strong; basis: contrast+neighbour+root+theme] كَلَّا ۖ بَل لَّا يَخَافُونَ ٱلْءَاخِرَةَ
  Unverified discovery rationale: luna: The ayah says they do not fear the Hereafter, the precise contrary of the fear through which 87:10's listener receives the reminder. | terra: Their flight is traced to the fact that they do not fear the Hereafter, the direct negative of the fear that receives reminder in 87:10.
- (74:54) [luna: strong; terra: strong; basis: neighbour+root+theme] كَلَّآ إِنَّهُۥ تَذْكِرَةٌۭ
  Unverified discovery rationale: luna: إِنَّهُۥ تَذْكِرَةٌ calls the message a reminder, directly echoing the source root ذ ك ر. | terra: The passage corrects them with كَلَّا إِنَّهُۥ تَذْكِرَةٌ, insisting that what they flee is precisely a reminder.
- (74:55) [luna: strong; terra: strong; basis: neighbour+root+scene+speaker+theme] فَمَن شَآءَ ذَكَرَهُۥ
  Unverified discovery rationale: luna: Whoever wills may remember, spelling out the voluntary response contrasted in 87:10–11. | terra: Whoever wills may remember it, locating the decisive difference in reception rather than in whether reminder was offered.
- (74:56) [luna: strong; terra: strong; basis: neighbour+root+theme] وَمَا يَذْكُرُونَ إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ هُوَ أَهْلُ ٱلتَّقْوَىٰ وَأَهْلُ ٱلْمَغْفِرَةِ
  Unverified discovery rationale: luna: It says they remember only if God wills and names Him أهل التقوى; this holds together the source's voluntary response and fear/awe theme. | terra: Their remembering remains under God's will, and He is named worthy of fear, placing the hearer's choice inside the divine boundary around reminder and fear.
- (75:31) [terra: strong; basis: scene+theme] فَلَا صَدَّقَ وَلَا صَلَّىٰ
  Unverified discovery rationale: terra: The rejecter neither affirmed the truth nor prayed, coupling failed reception with the absence of prayer exactly as the section's root meditation does.
- (75:32) [terra: strong; basis: contrast+neighbour+scene] وَلَٰكِن كَذَّبَ وَتَوَلَّىٰ
  Unverified discovery rationale: terra: Instead he denied and turned away, naming the two-part posture behind his failure to pray.
- (76:29) [luna: strong (missing-ayat turn); terra: medium; basis: root+scene+theme] إِنَّ هَٰذِهِۦ تَذْكِرَةٌۭ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ سَبِيلًۭا
  Unverified discovery rationale: luna: This passage likewise calls itself a reminder and offers a way to the Lord to whoever wills, a repeated formulation of the source's voluntary reception. | terra: “This is a reminder” again opens a path to the Lord for whoever wills, a parallel formulation of offered and received guidance.
- (79:18) [luna: strong; terra: strong; basis: scene+speaker+theme] [cited in ¶67] فَقُلْ هَل لَّكَ إِلَىٰٓ أَن تَزَكَّىٰ
  Unverified discovery rationale: luna: Moses invites Pharaoh to purify himself, echoing both the possible purification in 80:3 and the success of 87:14. | terra: Moses offers Pharaoh purification as a question rather than compulsion, the first movement of the reminder offered to one who will reject it.
- (79:19) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶67] وَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ
  Unverified discovery rationale: luna: Moses offers guidance to the Lord so Pharaoh may fear; this joins the source's secondary خشية-as-knowing gloss to the root ه د ي named in that gloss. | terra: Moses offers to guide Pharaoh to his Lord so that he will fear; guidance is meant to produce the knowledgeable fear described in the section.
- (79:20) [luna: strong; terra: medium (missing-ayat turn); basis: neighbour+scene] فَأَرَىٰهُ ٱلْءَايَةَ ٱلْكُبْرَىٰ
  Unverified discovery rationale: luna: The great sign shown to Pharaoh is the message's concrete presentation; 79:21 then records his response, completing the invitation scene developed in the source. | terra: Moses shows Pharaoh the great sign before Pharaoh denies, so rejection follows both spoken invitation and visible evidence.
- (79:21) [luna: strong; terra: strong; basis: contrast+neighbour+scene] فَكَذَّبَ وَعَصَىٰ
  Unverified discovery rationale: luna: Pharaoh denies and disobeys after the sign, showing the refused response opposite the fearful hearer in 87:10. | terra: Pharaoh denies and disobeys after the offer, giving a concrete history of the wretched hearer's failed reception.
- (79:22) [luna: strong; terra: strong; basis: contrast+neighbour+scene] ثُمَّ أَدْبَرَ يَسْعَىٰ
  Unverified discovery rationale: luna: Pharaoh turns away and strives after refusing the sign, making the source's act of keeping the reminder at a distance explicit. | terra: He then turns away and strives, converting the section's distance from reminder into an enacted withdrawal.
- (79:23) [luna: strong; basis: neighbour+scene] فَحَشَرَ فَنَادَىٰ
  Unverified discovery rationale: luna: Pharaoh gathers his people and calls out; this continues his refusal in 79:21–22 and makes the audience to his counter-message visible.
- (79:24) [luna: strong; basis: contrast+scene] فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ
  Unverified discovery rationale: luna: Pharaoh claims to be their highest lord, the arrogant stance that answers Moses' invitation to turn toward the Lord in 79:19.
- (79:25) [luna: strong; terra: medium (missing-ayat turn); basis: neighbour+scene+theme] فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ
  Unverified discovery rationale: luna: The seizure is the consequence of Pharaoh's denial and turning away in 79:21–24, completing the refusal scene. | terra: God seizes Pharaoh in exemplary punishment for his rejection, making his failed reception into the lesson named in 79:26.
- (79:26) [luna: strong; terra: strong; basis: neighbour+root+speaker+theme] إِنَّ فِى ذَٰلِكَ لَعِبْرَةًۭ لِّمَن يَخْشَىٰٓ
  Unverified discovery rationale: luna: The account is called a lesson for one who fears, explicitly linking the Pharaoh episode to the source section's fearful recipient. | terra: Pharaoh's fate is itself an instructive sign for whoever fears, so even the rejecter's story becomes reminder for the receptive hearer.
- (79:37) [luna: strong; basis: contrast+theme] فَأَمَّا مَن طَغَىٰ
  Unverified discovery rationale: luna: The transgressor begins the path contrasted with the fearful recipient of reminder in the source section.
- (79:38) [luna: strong; basis: contrast+theme] وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
  Unverified discovery rationale: luna: Preferring the worldly life states the choice condemned by 87:16 and opposed to the abiding Hereafter.
- (79:39) [luna: strong; basis: contrast+scene] فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ
  Unverified discovery rationale: luna: Hell is the transgressor's refuge, completing the worldly preference in 79:38 and the fire for 87:11's al-ashqa.
- (79:40) [luna: strong; basis: contrast+root] وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ
  Unverified discovery rationale: luna: The one who fears standing before his Lord restrains desire, embodying the receptive fear and self-restraint contrasted with al-ashqa.
- (79:41) [luna: strong; basis: contrast+theme] فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ
  Unverified discovery rationale: luna: The Garden is the refuge for the one who fears and restrains himself, completing the contrast with 79:39 and 87:12–17.
- (79:45) [terra: strong; basis: speaker+theme] إِنَّمَآ أَنتَ مُنذِرُ مَن يَخْشَىٰهَا
  Unverified discovery rationale: terra: The Prophet is only the warner of whoever fears the Hour, matching the section's limit on his role and its fear-defined recipient.
- (80:1) [luna: strong; terra: contrast; basis: contrast+scene+speaker] عَبَسَ وَتَوَلَّىٰٓ
  Unverified discovery rationale: luna: The Prophet's frown and turning away open the scene the section uses to show that a receptive listener may be passed over. | terra: The Prophet frowns and turns away, briefly occupying the bodily posture later attributed to the wretched hearer; revelation corrects who deserves attention.
- (80:2) [luna: strong; terra: contrast; basis: contrast+neighbour+scene] أَن جَآءَهُ ٱلْأَعْمَىٰ
  Unverified discovery rationale: luna: This ayah identifies the blind man's arrival; it completes 80:1's turning-away scene that the section explicitly invokes. | terra: The cause is the blind man's arrival; his physical blindness will be opposed by inward fear and receptivity, while the sighted self-sufficient man remains unreceptive.
- (80:3) [luna: strong; terra: strong; basis: neighbour+root+scene] [cited in ¶67] وَمَا يُدْرِيكَ لَعَلَّهُۥ يَزَّكَّىٰٓ
  Unverified discovery rationale: luna: The question وَمَا يُدْرِيكَ introduces the possibility that the visitor will purify himself, echoing 87:14 and the section's connection between fear and knowledge. | terra: In the section's enacted scene, the Prophet cannot know whether the blind visitor may purify himself; this is the open possibility that makes reminder worthwhile in 80:4.
- (80:4) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶67] أَوْ يَذَّكَّرُ فَتَنفَعَهُ ٱلذِّكْرَىٰٓ
  Unverified discovery rationale: luna: The blind visitor may remember and the reminder may benefit him: this directly restages the source section's ذ ك ر and ن ف ع pairing. | terra: The section's reminder that may benefit is restaged exactly: the blind man may remember, and the reminder may benefit him.
- (80:8) [luna: strong; terra: strong; basis: neighbour+scene] وَأَمَّا مَن جَآءَكَ يَسْعَىٰ
  Unverified discovery rationale: luna: The one who comes striving is the same visitor whose approach the section contrasts with turning away from the reminder. | terra: The blind man actively comes striving, supplying the bodily approach that contrasts with the section's wretched person's keeping away.
- (80:9) [luna: strong; terra: strong; basis: neighbour+root+scene] [cited in ¶67] وَهُوَ يَخْشَىٰ
  Unverified discovery rationale: luna: The man who comes is described as وَهُوَ يَخْشَىٰ, matching the source section's one who receives the reminder through fear. | terra: The approaching man is وَهُوَ يَخْشَىٰ, the very fear that the section says receives reminder.
- (80:10) [luna: strong; terra: strong; basis: contrast+scene+speaker] [cited in ¶67] فَأَنتَ عَنْهُ تَلَهَّىٰ
  Unverified discovery rationale: luna: The Prophet is told he is distracted from the man; this is the same encounter's rejected attentiveness, set against 87:10's receiver. | terra: The Prophet is momentarily distracted from the fearful seeker; the warning turns the section's avoiding posture back upon its own appointed reminder.
- (80:11) [luna: strong; terra: strong; basis: neighbour+root+scene+theme] كَلَّآ إِنَّهَا تَذْكِرَةٌۭ
  Unverified discovery rationale: luna: إِنَّهَا تَذْكِرَةٌ calls the revelation a reminder, the same act named by the source root ذ ك ر. | terra: كَلَّا إِنَّهَا تَذْكِرَةٌ identifies the address itself as a reminder after correcting the mistaken allocation of attention.
- (80:12) [luna: strong; terra: strong; basis: neighbour+root+scene+speaker+theme] فَمَن شَآءَ ذَكَرَهُۥ
  Unverified discovery rationale: luna: فَمَن شَاءَ ذَكَرَهُ makes the listener's taking up the reminder a matter of response, as in 87:10–11. | terra: فَمَن شَاءَ ذَكَرَهُ makes reception the hearer's act, completing the scene in which reminder is offered but cannot be forced into another.
- (83:13) [terra: strong (missing-ayat turn); basis: contrast+scene] إِذَا تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا قَالَ أَسَٰطِيرُ ٱلْأَوَّلِينَ
  Unverified discovery rationale: terra: When God's signs are recited, the transgressor dismisses them as ancient tales, turning a present reminder into something he need not hear.
- (83:14) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] كَلَّا ۖ بَلْ ۜ رَانَ عَلَىٰ قُلُوبِهِم مَّا كَانُوا۟ يَكْسِبُونَ
  Unverified discovery rationale: terra: The denial is traced to rust over their hearts from what they earned, explaining the inward barrier that prevents reminder from benefiting.
- (84:21) [terra: strong (missing-ayat turn); basis: contrast+scene] وَإِذَا قُرِئَ عَلَيْهِمُ ٱلْقُرْءَانُ لَا يَسْجُدُونَ ۩
  Unverified discovery rationale: terra: When the Quran is recited to them they do not prostrate, a specific bodily nonresponse opposite the fearful hearers who fall down in receptivity.
- (84:22) [terra: strong (missing-ayat turn); basis: neighbour+scene] بَلِ ٱلَّذِينَ كَفَرُوا۟ يُكَذِّبُونَ
  Unverified discovery rationale: terra: The disbelievers instead deny, identifying the conviction beneath their refusal to bow to recitation.
- (88:21) [luna: strong; terra: strong; basis: root+scene+speaker+theme] [cited in ¶67] فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
  Unverified discovery rationale: luna: The Prophet's task is explicitly to remind; this states the limited role behind the source section's command فَذَكِّرْ. | terra: فَذَكِّرْ إِنَّمَا أَنتَ مُذَكِّرٌ repeats the command while delimiting the Prophet's task to presenting the reminder.
- (88:23) [luna: strong; terra: strong (missing-ayat turn); basis: contrast+neighbour+root+scene] [cited in ¶67] إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
  Unverified discovery rationale: luna: The one who turns back and disbelieves is a direct counterpart to the source section's al-ashqa who keeps the reminder at a distance. | terra: The person who turns away and disbelieves is the explicit exception to the hearer reached by the Prophet's reminder, restaging 87:11's avoidance.
- (88:24) [luna: strong; terra: strong (missing-ayat turn); basis: contrast+neighbour+scene+theme] فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
  Unverified discovery rationale: luna: This ayah gives the punishment for the turner in 88:23, completing the consequence of avoiding the reminder that 87:11–13 places nearby in its own surah. | terra: God then punishes that turner-away with the greatest punishment, completing the consequence of the rejected reminder.
- (89:23) [terra: strong; basis: contrast+root+theme] وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
  Unverified discovery rationale: terra: On the day Hell is brought, the human being finally remembers, but the ayah asks how remembrance can then benefit him; reception has come after its useful time.
- (91:9) [luna: strong; terra: contrast; basis: contrast+root+theme] قَدْ أَفْلَحَ مَن زَكَّىٰهَا
  Unverified discovery rationale: luna: قَدْ أَفْلَحَ مَن زَكَّاهَا directly echoes 87:14's success for the one who purifies himself. | terra: Success belongs to the one who purifies the soul, the positive outcome standing across from the most wretched rejecter later in the same passage.
- (91:10) [luna: strong; terra: contrast; basis: contrast+root+theme] وَقَدْ خَابَ مَن دَسَّىٰهَا
  Unverified discovery rationale: luna: The one who corrupts the soul fails, completing 91:9's purification contrast and clarifying the source's al-ashqa. | terra: Failure belongs to the one who corrupts or buries the soul, supplying the inward opposite to purification and receptivity.
- (91:12) [terra: strong; basis: root+scene] إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا
  Unverified discovery rationale: terra: Thamud's ٱلْأَشْقَى rises to act, another occurrence of the section's superlative embodied in a man who rejects a divine warning.
- (91:13) [terra: strong; basis: neighbour+scene+speaker] فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا
  Unverified discovery rationale: terra: God's messenger names the divine she-camel and her drink to the people, supplying the concrete warning that their most wretched member confronts.
- (91:14) [terra: strong; basis: contrast+neighbour+scene] فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا
  Unverified discovery rationale: terra: They deny the messenger and hamstring the camel, showing an openly violent form of the rejection whose quieter form is avoidance in 87:11.
- (92:5) [luna: strong; terra: strong; basis: contrast+root+scene] فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ
  Unverified discovery rationale: luna: The giver who fears God begins the positive path opposite the source's wretched avoider. | terra: The person who gives and fears begins the receptive side of a paired moral portrait closely matching 87:10.
- (92:6) [luna: strong; terra: strong; basis: neighbour+scene+theme] وَصَدَّقَ بِٱلْحُسْنَىٰ
  Unverified discovery rationale: luna: Belief in the best confirms the response begun in 92:5, supplying its faith commitment alongside fear. | terra: His affirmation of the best promise shows the assent that accompanies fear rather than the wretched person's denial.
- (92:7) [luna: strong; terra: strong; basis: neighbour+scene+theme] فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
  Unverified discovery rationale: luna: God eases this person's way toward ease, echoing 87:8 and showing the outcome of the receptive, God-fearing path. | terra: God eases this fearful believer toward ease, linking reception to the facilitation promised just before the section in 87:8.
- (92:8) [luna: strong; terra: strong; basis: contrast+scene] وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ
  Unverified discovery rationale: luna: The one who withholds and considers himself self-sufficient begins the negative path opposite 92:5 and the source's fearful listener. | terra: The opposing person is miserly and considers himself self-sufficient, the same self-sufficiency that misdirects attention in the ʿAbasa scene.
- (92:9) [luna: strong; terra: strong; basis: contrast+neighbour+scene+theme] وَكَذَّبَ بِٱلْحُسْنَىٰ
  Unverified discovery rationale: luna: He denies the best, explicitly showing the refusal paired with the source's one who avoids reminder. | terra: He denies the best promise, supplying the cognitive refusal behind avoidance.
- (92:10) [luna: strong; terra: strong; basis: contrast+neighbour+theme] فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
  Unverified discovery rationale: luna: The difficult way is made easy for the refuser of 92:8–9, completing the two paths set against each other. | terra: God eases him toward hardship, the opposed destination of the self-sufficient denier.
- (92:11) [luna: strong; terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
  Unverified discovery rationale: luna: His wealth cannot avail him when he falls, undercutting the worldly self-sufficiency opposed by the source's lasting hereafter. | terra: The self-sufficient denier's wealth will not avail him when he falls, exposing the false estimate of benefit that sustains his refusal.
- (92:12) [luna: strong; basis: root+theme] إِنَّ عَلَيْنَا لَلْهُدَىٰ
  Unverified discovery rationale: luna: إِنَّ عَلَيْنَا لَلْهُدَىٰ names guidance as God's charge, echoing the source's explicit ه د ي root link.
- (92:13) [luna: strong; basis: contrast+theme] وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
  Unverified discovery rationale: luna: The first life and the Hereafter belong to God, framing the source's contrast between preferred worldly life and the better, enduring one.
- (92:14) [luna: strong; terra: medium; basis: neighbour+scene+speaker] فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
  Unverified discovery rationale: luna: The warning of a blazing fire is the announced consequence of rejecting the path, as in the surrounding 87:11–13 context. | terra: God announces that He has warned of a blazing fire immediately before identifying its “most wretched” entrant, so punishment follows an offered warning.
- (92:15) [luna: strong; terra: strong; basis: contrast+root+scene] لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
  Unverified discovery rationale: luna: The word الْأَشْقَى names the one entering the fire, matching the source's word for the wretched avoider. | terra: The same superlative ٱلْأَشْقَى is the one who enters the blazing fire, carrying 87:11's identity directly into its consequence.
- (92:16) [luna: strong; terra: strong; basis: neighbour+root+scene+theme] ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
  Unverified discovery rationale: luna: The wretched one's defining acts are denial and turning away, explicitly aligning al-ashqa with the source's avoidance of reminder. | terra: This “most wretched” one is specified as the person who denied and turned away, explaining the avoidance of reminder as a settled response.
- (92:17) [luna: contrast; terra: strong; basis: contrast+root+scene] وَسَيُجَنَّبُهَا ٱلْأَتْقَى
  Unverified discovery rationale: luna: سَيُجَنَّبُهَا uses the source root ج ن ب for the God-fearing person kept away from the fire, reversing 87:11's wretched person who keeps away from reminder. | terra: وَسَيُجَنَّبُهَا ٱلْأَتْقَىٰ reverses 87:11 almost word for word: the God-conscious is kept away from the fire, while the wretched keeps away from reminder.
- (92:18) [luna: strong; terra: medium; basis: contrast+neighbour+root+scene+theme] ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
  Unverified discovery rationale: luna: The God-fearing man gives wealth to purify himself, echoing the purification of 87:14. | terra: The God-conscious person gives wealth seeking purification, extending the positive opposite of the denying, turning-away wretch.
- (92:19) [luna: strong; basis: contrast+theme] وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
  Unverified discovery rationale: luna: He gives without repaying a favor owed to anyone, making his action unlike worldly calculation and self-sufficiency.
- (92:20) [luna: strong; basis: speaker+theme] إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
  Unverified discovery rationale: luna: His giving seeks only his Lord's countenance, showing the motive behind the receptive, God-fearing path.
- (92:21) [luna: strong; basis: contrast+theme] وَلَسَوْفَ يَرْضَىٰ
  Unverified discovery rationale: luna: The giver will be satisfied, the good end set against the source's al-ashqa and its wretched consequence.
- (96:9) [terra: strong (missing-ayat turn); basis: contrast+scene] أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ
  Unverified discovery rationale: terra: The passage asks about one who forbids another, introducing a person who creates distance from worship for someone else.
- (96:10) [terra: strong (missing-ayat turn); basis: neighbour+scene+theme] عَبْدًا إِذَا صَلَّىٰٓ
  Unverified discovery rationale: terra: What he forbids is a servant's prayer, a concrete external counterpart to the section's echo of keeping oneself distant from prayer.
- (96:13) [terra: strong (missing-ayat turn); basis: contrast+neighbour+scene] أَرَءَيْتَ إِن كَذَّبَ وَتَوَلَّىٰٓ
  Unverified discovery rationale: terra: The forbidder is characterized as one who denies and turns away, the same posture that blocks reminder and prayer.

## medium (59)

- (3:191) [terra: medium (missing-ayat turn); basis: contrast+root+theme] ٱلَّذِينَ يَذْكُرُونَ ٱللَّهَ قِيَٰمًۭا وَقُعُودًۭا وَعَلَىٰ جُنُوبِهِمْ وَيَتَفَكَّرُونَ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ رَبَّنَا مَا خَلَقْتَ هَٰذَا بَٰطِلًۭا سُبْحَٰنَكَ فَقِنَا عَذَابَ ٱلنَّارِ
  Unverified discovery rationale: terra: People of understanding remember God standing, sitting, and on their sides; physical “side” does not keep remembrance distant for the receptive thinker.
- (3:193) [terra: medium; basis: scene+theme] رَّبَّنَآ إِنَّنَا سَمِعْنَا مُنَادِيًۭا يُنَادِى لِلْإِيمَٰنِ أَنْ ءَامِنُوا۟ بِرَبِّكُمْ فَـَٔامَنَّا ۚ رَبَّنَا فَٱغْفِرْ لَنَا ذُنُوبَنَا وَكَفِّرْ عَنَّا سَيِّـَٔاتِنَا وَتَوَفَّنَا مَعَ ٱلْأَبْرَارِ
  Unverified discovery rationale: terra: Believers say they heard a caller calling to faith and therefore believed; the transitive address reaches another and produces its intended response.
- (4:36) [luna: medium; terra: medium; basis: root] ۞ وَٱعْبُدُوا۟ ٱللَّهَ وَلَا تُشْرِكُوا۟ بِهِۦ شَيْـًۭٔا ۖ وَبِٱلْوَٰلِدَيْنِ إِحْسَٰنًۭا وَبِذِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَٱلْجَارِ ذِى ٱلْقُرْبَىٰ وَٱلْجَارِ ٱلْجُنُبِ وَٱلصَّاحِبِ بِٱلْجَنۢبِ وَٱبْنِ ٱلسَّبِيلِ وَمَا مَلَكَتْ أَيْمَٰنُكُمْ ۗ إِنَّ ٱللَّهَ لَا يُحِبُّ مَن كَانَ مُخْتَالًۭا فَخُورًا
  Unverified discovery rationale: luna: The source labels ج ن ب's other sense as distance; الْجَارِ الْجُنُبِ can denote a distant or unrelated neighbor, a lexical echo, though this is social proximity rather than avoiding a reminder. | terra: ٱلْجَارِ ٱلْجُنُبِ is the distant neighbor, directly preserving the dictionary root's distance sense and clarifying the spatial force heard in the section's avoidance verb.
- (6:54) [luna: medium; basis: neighbour+theme] وَإِذَا جَآءَكَ ٱلَّذِينَ يُؤْمِنُونَ بِـَٔايَٰتِنَا فَقُلْ سَلَٰمٌ عَلَيْكُمْ ۖ كَتَبَ رَبُّكُمْ عَلَىٰ نَفْسِهِ ٱلرَّحْمَةَ ۖ أَنَّهُۥ مَنْ عَمِلَ مِنكُمْ سُوٓءًۢا بِجَهَٰلَةٍۢ ثُمَّ تَابَ مِنۢ بَعْدِهِۦ وَأَصْلَحَ فَأَنَّهُۥ غَفُورٌۭ رَّحِيمٌۭ
  Unverified discovery rationale: luna: God's mercy is promised to those who repent after ignorance and set things right; this completes the humble audience contrast in 6:52–53.
- (6:90) [terra: medium (missing-ayat turn); basis: root+speaker] أُو۟لَٰٓئِكَ ٱلَّذِينَ هَدَى ٱللَّهُ ۖ فَبِهُدَىٰهُمُ ٱقْتَدِهْ ۗ قُل لَّآ أَسْـَٔلُكُمْ عَلَيْهِ أَجْرًا ۖ إِنْ هُوَ إِلَّا ذِكْرَىٰ لِلْعَٰلَمِينَ
  Unverified discovery rationale: terra: The Prophet follows earlier guidance without asking payment and says the message is only a reminder to the worlds, locating reminder in a continuous prophetic office.
- (7:2) [luna: medium; basis: scene+speaker] كِتَٰبٌ أُنزِلَ إِلَيْكَ فَلَا يَكُن فِى صَدْرِكَ حَرَجٌۭ مِّنْهُ لِتُنذِرَ بِهِۦ وَذِكْرَىٰ لِلْمُؤْمِنِينَ
  Unverified discovery rationale: luna: The Book is sent down so the Prophet may warn by it and as a reminder for believers, explicitly linking the messenger's role and reminder.
- (7:3) [luna: medium; basis: scene+speaker] ٱتَّبِعُوا۟ مَآ أُنزِلَ إِلَيْكُم مِّن رَّبِّكُمْ وَلَا تَتَّبِعُوا۟ مِن دُونِهِۦٓ أَوْلِيَآءَ ۗ قَلِيلًۭا مَّا تَذَكَّرُونَ
  Unverified discovery rationale: luna: People are told to follow what was sent down rather than other protectors and are said to remember little, a concrete reception choice.
- (7:51) [luna: medium; basis: contrast+theme] ٱلَّذِينَ ٱتَّخَذُوا۟ دِينَهُمْ لَهْوًۭا وَلَعِبًۭا وَغَرَّتْهُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا ۚ فَٱلْيَوْمَ نَنسَىٰهُمْ كَمَا نَسُوا۟ لِقَآءَ يَوْمِهِمْ هَٰذَا وَمَا كَانُوا۟ بِـَٔايَٰتِنَا يَجْحَدُونَ
  Unverified discovery rationale: luna: Those who made religion amusement and forgot the meeting of that Day face its punishment, joining forgotten reminder to the source's rejected Hereafter.
- (7:63) [luna: medium; basis: scene+speaker] أَوَعَجِبْتُمْ أَن جَآءَكُمْ ذِكْرٌۭ مِّن رَّبِّكُمْ عَلَىٰ رَجُلٍۢ مِّنكُمْ لِيُنذِرَكُمْ وَلِتَتَّقُوا۟ وَلَعَلَّكُمْ تُرْحَمُونَ
  Unverified discovery rationale: luna: Noah says a reminder from the Lord has come through a man to warn them so they may fear and receive mercy, a direct formulation of the source's scene.
- (7:64) [luna: medium; basis: contrast+scene] فَكَذَّبُوهُ فَأَنجَيْنَٰهُ وَٱلَّذِينَ مَعَهُۥ فِى ٱلْفُلْكِ وَأَغْرَقْنَا ٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِنَآ ۚ إِنَّهُمْ كَانُوا۟ قَوْمًا عَمِينَ
  Unverified discovery rationale: luna: Noah's people deny him, while he and those with him are saved and the deniers drowned; this makes the two responses consequential.
- (7:69) [luna: medium; basis: scene+speaker] أَوَعَجِبْتُمْ أَن جَآءَكُمْ ذِكْرٌۭ مِّن رَّبِّكُمْ عَلَىٰ رَجُلٍۢ مِّنكُمْ لِيُنذِرَكُمْ ۚ وَٱذْكُرُوٓا۟ إِذْ جَعَلَكُمْ خُلَفَآءَ مِنۢ بَعْدِ قَوْمِ نُوحٍۢ وَزَادَكُمْ فِى ٱلْخَلْقِ بَصْۜطَةًۭ ۖ فَٱذْكُرُوٓا۟ ءَالَآءَ ٱللَّهِ لَعَلَّكُمْ تُفْلِحُونَ
  Unverified discovery rationale: luna: Hud repeats that a reminder has come to warn his people and make them fear, a second direct instance of the message the source describes.
- (7:70) [luna: medium; basis: contrast+scene] قَالُوٓا۟ أَجِئْتَنَا لِنَعْبُدَ ٱللَّهَ وَحْدَهُۥ وَنَذَرَ مَا كَانَ يَعْبُدُ ءَابَآؤُنَا ۖ فَأْتِنَا بِمَا تَعِدُنَآ إِن كُنتَ مِنَ ٱلصَّٰدِقِينَ
  Unverified discovery rationale: luna: The people challenge Hud to bring the threatened punishment and reject worship of Allah alone, showing their response to the warning.
- (7:71) [luna: medium; basis: contrast+neighbour] قَالَ قَدْ وَقَعَ عَلَيْكُم مِّن رَّبِّكُمْ رِجْسٌۭ وَغَضَبٌ ۖ أَتُجَٰدِلُونَنِى فِىٓ أَسْمَآءٍۢ سَمَّيْتُمُوهَآ أَنتُمْ وَءَابَآؤُكُم مَّا نَزَّلَ ٱللَّهُ بِهَا مِن سُلْطَٰنٍۢ ۚ فَٱنتَظِرُوٓا۟ إِنِّى مَعَكُم مِّنَ ٱلْمُنتَظِرِينَ
  Unverified discovery rationale: luna: Hud announces anger and punishment after their refusal in 7:70, completing the rejection scene.
- (7:72) [luna: medium; basis: contrast+neighbour] فَأَنجَيْنَٰهُ وَٱلَّذِينَ مَعَهُۥ بِرَحْمَةٍۢ مِّنَّا وَقَطَعْنَا دَابِرَ ٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِنَا ۖ وَمَا كَانُوا۟ مُؤْمِنِينَ
  Unverified discovery rationale: luna: Hud and the believers are saved while those who denied God's signs are cut off, completing the choice set in 7:69–71.
- (7:201) [luna: medium; terra: medium; basis: root+scene+theme] إِنَّ ٱلَّذِينَ ٱتَّقَوْا۟ إِذَا مَسَّهُمْ طَٰٓئِفٌۭ مِّنَ ٱلشَّيْطَٰنِ تَذَكَّرُوا۟ فَإِذَا هُم مُّبْصِرُونَ
  Unverified discovery rationale: luna: When those who fear God are touched by Satan, they remember and see clearly, directly joining fear with taking up reminder. | terra: When a satanic suggestion touches the God-conscious, they remember and then see clearly; fear makes remembrance restore perception.
- (11:120) [terra: medium; basis: root+speaker+theme] وَكُلًّۭا نَّقُصُّ عَلَيْكَ مِنْ أَنۢبَآءِ ٱلرُّسُلِ مَا نُثَبِّتُ بِهِۦ فُؤَادَكَ ۚ وَجَآءَكَ فِى هَٰذِهِ ٱلْحَقُّ وَمَوْعِظَةٌۭ وَذِكْرَىٰ لِلْمُؤْمِنِينَ
  Unverified discovery rationale: terra: The messengers' histories steady the Prophet's heart and come as truth, admonition, and reminder for believers, so reminder benefits both bearer and hearer.
- (12:104) [terra: medium (missing-ayat turn); basis: root+speaker] وَمَا تَسْـَٔلُهُمْ عَلَيْهِ مِنْ أَجْرٍ ۚ إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
  Unverified discovery rationale: terra: The Prophet asks no payment for revelation, which is only a reminder to the worlds; the breadth and gratuity of delivery clarify his reminding stance.
- (13:21) [terra: medium (missing-ayat turn); basis: neighbour+root+theme] وَٱلَّذِينَ يَصِلُونَ مَآ أَمَرَ ٱللَّهُ بِهِۦٓ أَن يُوصَلَ وَيَخْشَوْنَ رَبَّهُمْ وَيَخَافُونَ سُوٓءَ ٱلْحِسَابِ
  Unverified discovery rationale: terra: The people of understanding fear their Lord and dread a bad accounting, continuing 13:19's link between knowing revelation and reverent response.
- (13:22) [terra: medium (missing-ayat turn); basis: neighbour+theme] وَٱلَّذِينَ صَبَرُوا۟ ٱبْتِغَآءَ وَجْهِ رَبِّهِمْ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَأَنفَقُوا۟ مِمَّا رَزَقْنَٰهُمْ سِرًّۭا وَعَلَانِيَةًۭ وَيَدْرَءُونَ بِٱلْحَسَنَةِ ٱلسَّيِّئَةَ أُو۟لَٰٓئِكَ لَهُمْ عُقْبَى ٱلدَّارِ
  Unverified discovery rationale: terra: They patiently seek God's face and establish prayer, giving the conduct produced by the informed fear of the preceding ayah.
- (13:40) [terra: medium; basis: speaker+theme] وَإِن مَّا نُرِيَنَّكَ بَعْضَ ٱلَّذِى نَعِدُهُمْ أَوْ نَتَوَفَّيَنَّكَ فَإِنَّمَا عَلَيْكَ ٱلْبَلَٰغُ وَعَلَيْنَا ٱلْحِسَابُ
  Unverified discovery rationale: terra: The Prophet's duty is only delivery while reckoning belongs to God, separating transmitted reminder from its final accounting.
- (16:125) [luna: medium; terra: medium; basis: root+scene+speaker+theme] ٱدْعُ إِلَىٰ سَبِيلِ رَبِّكَ بِٱلْحِكْمَةِ وَٱلْمَوْعِظَةِ ٱلْحَسَنَةِ ۖ وَجَٰدِلْهُم بِٱلَّتِى هِىَ أَحْسَنُ ۚ إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ ۖ وَهُوَ أَعْلَمُ بِٱلْمُهْتَدِينَ
  Unverified discovery rationale: luna: The Messenger is told to invite with wisdom and good instruction, specifying how the source's reminder is to be offered. | terra: Invitation by wisdom and good admonition describes how reminder should cross to another, while God alone knows who is guided or astray.
- (17:9) [luna: medium (missing-ayat turn); basis: root+scene] إِنَّ هَٰذَا ٱلْقُرْءَانَ يَهْدِى لِلَّتِى هِىَ أَقْوَمُ وَيُبَشِّرُ ٱلْمُؤْمِنِينَ ٱلَّذِينَ يَعْمَلُونَ ٱلصَّٰلِحَٰتِ أَنَّ لَهُمْ أَجْرًۭا كَبِيرًۭا
  Unverified discovery rationale: luna: The Qur'an guides to what is most upright and gives good news to believers, a concrete instance of the guidance root linked to the source's reminder.
- (17:10) [luna: medium (missing-ayat turn); basis: contrast+neighbour] وَأَنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ أَعْتَدْنَا لَهُمْ عَذَابًا أَلِيمًۭا
  Unverified discovery rationale: luna: Those who do not believe in the Hereafter face painful punishment, completing 17:9's contrast between the guided and those who reject the message.
- (20:43) [terra: medium (missing-ayat turn); basis: neighbour+scene] ٱذْهَبَآ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ
  Unverified discovery rationale: terra: Moses and Aaron are sent specifically to Pharaoh because he has transgressed, showing that even the likely rejecter remains an addressee of gentle reminder.
- (20:125) [luna: medium; basis: neighbour+scene] قَالَ رَبِّ لِمَ حَشَرْتَنِىٓ أَعْمَىٰ وَقَدْ كُنتُ بَصِيرًۭا
  Unverified discovery rationale: luna: The one who turned away from remembrance in 20:124 is raised blind and asks why, extending the consequence of refusing reminder.
- (21:45) [luna: medium (missing-ayat turn); basis: contrast+scene] قُلْ إِنَّمَآ أُنذِرُكُم بِٱلْوَحْىِ ۚ وَلَا يَسْمَعُ ٱلصُّمُّ ٱلدُّعَآءَ إِذَا مَا يُنذَرُونَ
  Unverified discovery rationale: luna: The Prophet says he warns by revelation, but the deaf do not hear when warned; this restates the source's distinction between offering reminder and having it received.
- (21:49) [terra: medium; basis: root+theme] ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَهُم مِّنَ ٱلسَّاعَةِ مُشْفِقُونَ
  Unverified discovery rationale: terra: Those who fear their Lord unseen and dread the Hour exemplify the reverent fear the section distinguishes from bare alarm.
- (21:66) [terra: medium (missing-ayat turn); basis: contrast+root] قَالَ أَفَتَعْبُدُونَ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُكُمْ شَيْـًۭٔا وَلَا يَضُرُّكُمْ
  Unverified discovery rationale: terra: Abraham asks whether his people worship objects that neither benefit nor harm them, using the pair to expose an address rejected for powerless substitutes.
- (23:109) [terra: medium (missing-ayat turn); basis: neighbour+root+scene] إِنَّهُۥ كَانَ فَرِيقٌۭ مِّنْ عِبَادِى يَقُولُونَ رَبَّنَآ ءَامَنَّا فَٱغْفِرْ لَنَا وَٱرْحَمْنَا وَأَنتَ خَيْرُ ٱلرَّٰحِمِينَ
  Unverified discovery rationale: terra: A group of God's servants confessed belief and prayed for mercy; their prayer is the receptive speech that the condemned mock before forgetting remembrance.
- (23:110) [terra: medium; basis: neighbour+root+scene] فَٱتَّخَذْتُمُوهُمْ سِخْرِيًّا حَتَّىٰٓ أَنسَوْكُمْ ذِكْرِى وَكُنتُم مِّنْهُمْ تَضْحَكُونَ
  Unverified discovery rationale: terra: The condemned mocked God's praying servants until that occupation made them forget His remembrance, a social mechanism by which the wretched lose the reminder.
- (23:111) [terra: medium (missing-ayat turn); basis: contrast+neighbour+theme] إِنِّى جَزَيْتُهُمُ ٱلْيَوْمَ بِمَا صَبَرُوٓا۟ أَنَّهُمْ هُمُ ٱلْفَآئِزُونَ
  Unverified discovery rationale: terra: God rewards those servants for patience and names them the successful, supplying felicity opposite the condemned speakers' wretchedness.
- (24:34) [terra: medium; basis: root+theme] وَلَقَدْ أَنزَلْنَآ إِلَيْكُمْ ءَايَٰتٍۢ مُّبَيِّنَٰتٍۢ وَمَثَلًۭا مِّنَ ٱلَّذِينَ خَلَوْا۟ مِن قَبْلِكُمْ وَمَوْعِظَةًۭ لِّلْمُتَّقِينَ
  Unverified discovery rationale: terra: Clear signs, exemplary history, and admonition are said to be for the God-conscious; the ayah identifies the disposition for which instruction bears fruit.
- (25:27) [terra: medium (missing-ayat turn); basis: neighbour+scene] وَيَوْمَ يَعَضُّ ٱلظَّالِمُ عَلَىٰ يَدَيْهِ يَقُولُ يَٰلَيْتَنِى ٱتَّخَذْتُ مَعَ ٱلرَّسُولِ سَبِيلًۭا
  Unverified discovery rationale: terra: The wrongdoer will wish he had taken a path with the Messenger, providing the missed approach behind being led away from reminder in 25:29.
- (25:28) [terra: medium (missing-ayat turn); basis: neighbour+scene] يَٰوَيْلَتَىٰ لَيْتَنِى لَمْ أَتَّخِذْ فُلَانًا خَلِيلًۭا
  Unverified discovery rationale: terra: He will regret choosing a particular friend, identifying the human agency through which the reminder was kept at a distance.
- (26:3) [terra: medium (missing-ayat turn); basis: speaker+theme] لَعَلَّكَ بَٰخِعٌۭ نَّفْسَكَ أَلَّا يَكُونُوا۟ مُؤْمِنِينَ
  Unverified discovery rationale: terra: The Prophet is warned that he may consume himself in grief because people do not believe, protecting the reminder-bearer from bearing the hearers' refusal.
- (33:39) [terra: medium; basis: root+speaker] ٱلَّذِينَ يُبَلِّغُونَ رِسَٰلَٰتِ ٱللَّهِ وَيَخْشَوْنَهُۥ وَلَا يَخْشَوْنَ أَحَدًا إِلَّا ٱللَّهَ ۗ وَكَفَىٰ بِٱللَّهِ حَسِيبًۭا
  Unverified discovery rationale: terra: Earlier messengers deliver God's messages and fear Him alone, locating reverent fear in the reminder-bearer as well as its recipient.
- (34:42) [terra: medium (missing-ayat turn); basis: root+theme] فَٱلْيَوْمَ لَا يَمْلِكُ بَعْضُكُمْ لِبَعْضٍۢ نَّفْعًۭا وَلَا ضَرًّۭا وَنَقُولُ لِلَّذِينَ ظَلَمُوا۟ ذُوقُوا۟ عَذَابَ ٱلنَّارِ ٱلَّتِى كُنتُم بِهَا تُكَذِّبُونَ
  Unverified discovery rationale: terra: On Judgment Day no person controls benefit or harm for another, placing the section's benefit–harm pair under God's final authority.
- (38:29) [terra: medium; basis: root+theme] كِتَٰبٌ أَنزَلْنَٰهُ إِلَيْكَ مُبَٰرَكٌۭ لِّيَدَّبَّرُوٓا۟ ءَايَٰتِهِۦ وَلِيَتَذَكَّرَ أُو۟لُوا۟ ٱلْأَلْبَٰبِ
  Unverified discovery rationale: terra: The blessed Book is sent for reflection on its signs and for people of understanding to remember, making thought the passage into remembrance.
- (38:87) [terra: medium (missing-ayat turn); basis: root+speaker] إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
  Unverified discovery rationale: terra: The Prophet is told that the Quran is only a reminder to the worlds, a concise statement of the address extending beyond one immediate hearer.
- (40:13) [terra: medium (missing-ayat turn); basis: root+theme] هُوَ ٱلَّذِى يُرِيكُمْ ءَايَٰتِهِۦ وَيُنَزِّلُ لَكُم مِّنَ ٱلسَّمَآءِ رِزْقًۭا ۚ وَمَا يَتَذَكَّرُ إِلَّا مَن يُنِيبُ
  Unverified discovery rationale: terra: God shows signs and sends provision, yet none remembers except the person who turns back to Him; return is the motion that receives reminder.
- (40:54) [terra: medium (missing-ayat turn); basis: root+theme] هُدًۭى وَذِكْرَىٰ لِأُو۟لِى ٱلْأَلْبَٰبِ
  Unverified discovery rationale: terra: Moses' scripture is described as guidance and reminder for people of understanding, again joining reception to knowledge.
- (41:44) [luna: medium (missing-ayat turn); terra: contrast; basis: contrast+scene+theme] وَلَوْ جَعَلْنَٰهُ قُرْءَانًا أَعْجَمِيًّۭا لَّقَالُوا۟ لَوْلَا فُصِّلَتْ ءَايَٰتُهُۥٓ ۖ ءَا۬عْجَمِىٌّۭ وَعَرَبِىٌّۭ ۗ قُلْ هُوَ لِلَّذِينَ ءَامَنُوا۟ هُدًۭى وَشِفَآءٌۭ ۖ وَٱلَّذِينَ لَا يُؤْمِنُونَ فِىٓ ءَاذَانِهِمْ وَقْرٌۭ وَهُوَ عَلَيْهِمْ عَمًى ۚ أُو۟لَٰٓئِكَ يُنَادَوْنَ مِن مَّكَانٍۭ بَعِيدٍۢ
  Unverified discovery rationale: luna: The Qur'an is guidance and healing for believers while unbelievers remain deaf and blind to it, a concrete split response to the same revealed warning. | terra: The Quran is guidance and healing for believers, but unbelievers experience deafness and blindness toward it, making one address beneficial or inaccessible according to reception.
- (42:48) [terra: medium; basis: scene+speaker+theme] فَإِنْ أَعْرَضُوا۟ فَمَآ أَرْسَلْنَٰكَ عَلَيْهِمْ حَفِيظًا ۖ إِنْ عَلَيْكَ إِلَّا ٱلْبَلَٰغُ ۗ وَإِنَّآ إِذَآ أَذَقْنَا ٱلْإِنسَٰنَ مِنَّا رَحْمَةًۭ فَرِحَ بِهَا ۖ وَإِن تُصِبْهُمْ سَيِّئَةٌۢ بِمَا قَدَّمَتْ أَيْدِيهِمْ فَإِنَّ ٱلْإِنسَٰنَ كَفُورٌۭ
  Unverified discovery rationale: terra: If people turn away, the Prophet was not sent as their keeper; his duty is delivery, a wider statement of the section's division between address and response.
- (46:29) [luna: medium; terra: medium; basis: scene+speaker+theme] وَإِذْ صَرَفْنَآ إِلَيْكَ نَفَرًۭا مِّنَ ٱلْجِنِّ يَسْتَمِعُونَ ٱلْقُرْءَانَ فَلَمَّا حَضَرُوهُ قَالُوٓا۟ أَنصِتُوا۟ ۖ فَلَمَّا قُضِىَ وَلَّوْا۟ إِلَىٰ قَوْمِهِم مُّنذِرِينَ
  Unverified discovery rationale: luna: A group of jinn listens to the recited Qur'an attentively, then returns to warn its people, a scene of reminder received and passed on. | terra: A group of jinn listens attentively to the Quran and then turns back to its people as warners, modeling reception that becomes transmitted reminder.
- (46:30) [luna: medium; terra: medium; basis: neighbour+root+theme] قَالُوا۟ يَٰقَوْمَنَآ إِنَّا سَمِعْنَا كِتَٰبًا أُنزِلَ مِنۢ بَعْدِ مُوسَىٰ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ يَهْدِىٓ إِلَى ٱلْحَقِّ وَإِلَىٰ طَرِيقٍۢ مُّسْتَقِيمٍۢ
  Unverified discovery rationale: luna: The jinn call the Qur'an a guide to truth, completing 46:29's listening with recognition of the message. | terra: They identify what they heard as a confirming scripture that guides to truth and a straight path, explaining the knowledge their warning carries.
- (46:31) [luna: medium; terra: medium; basis: neighbour+scene+speaker] يَٰقَوْمَنَآ أَجِيبُوا۟ دَاعِىَ ٱللَّهِ وَءَامِنُوا۟ بِهِۦ يَغْفِرْ لَكُم مِّن ذُنُوبِكُمْ وَيُجِرْكُم مِّنْ عَذَابٍ أَلِيمٍۢ
  Unverified discovery rationale: luna: They urge their people to answer God's caller and believe so their sins may be forgiven, an explicit invitation to receive warning. | terra: They urge their people to answer God's caller, extending the reminder from first hearers to a new audience.
- (46:32) [luna: medium; basis: contrast+neighbour] وَمَن لَّا يُجِبْ دَاعِىَ ٱللَّهِ فَلَيْسَ بِمُعْجِزٍۢ فِى ٱلْأَرْضِ وَلَيْسَ لَهُۥ مِن دُونِهِۦٓ أَوْلِيَآءُ ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۢ مُّبِينٍ
  Unverified discovery rationale: luna: Whoever does not answer God's caller cannot escape God, completing the invitation and contrasting its acceptance with refusal.
- (49:12) [terra: medium (missing-ayat turn); basis: contrast+root] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱجْتَنِبُوا۟ كَثِيرًۭا مِّنَ ٱلظَّنِّ إِنَّ بَعْضَ ٱلظَّنِّ إِثْمٌۭ ۖ وَلَا تَجَسَّسُوا۟ وَلَا يَغْتَب بَّعْضُكُم بَعْضًا ۚ أَيُحِبُّ أَحَدُكُمْ أَن يَأْكُلَ لَحْمَ أَخِيهِ مَيْتًۭا فَكَرِهْتُمُوهُ ۚ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ تَوَّابٌۭ رَّحِيمٌۭ
  Unverified discovery rationale: terra: The command to avoid much suspicion uses the section's avoidance root for a proper moral object, further defining the boundary exposed by 87:11's wrong object.
- (50:33) [terra: medium; basis: root+theme] مَّنْ خَشِىَ ٱلرَّحْمَٰنَ بِٱلْغَيْبِ وَجَآءَ بِقَلْبٍۢ مُّنِيبٍ
  Unverified discovery rationale: terra: The promised Garden is for one who feared the Merciful unseen and came with a returning heart, giving fear the directional movement opposite avoidance.
- (52:29) [terra: medium; basis: root+speaker] فَذَكِّرْ فَمَآ أَنتَ بِنِعْمَتِ رَبِّكَ بِكَاهِنٍۢ وَلَا مَجْنُونٍ
  Unverified discovery rationale: terra: The Prophet is told simply to continue reminding and reassured that God's grace has not made him a soothsayer or madman; rejection does not redefine his office.
- (64:12) [terra: medium; basis: scene+speaker] وَأَطِيعُوا۟ ٱللَّهَ وَأَطِيعُوا۟ ٱلرَّسُولَ ۚ فَإِن تَوَلَّيْتُمْ فَإِنَّمَا عَلَىٰ رَسُولِنَا ٱلْبَلَٰغُ ٱلْمُبِينُ
  Unverified discovery rationale: terra: Turning away does not enlarge the Messenger's responsibility beyond clear delivery, another boundary around reception.
- (74:52) [terra: medium (missing-ayat turn); basis: neighbour+scene] بَلْ يُرِيدُ كُلُّ ٱمْرِئٍۢ مِّنْهُمْ أَن يُؤْتَىٰ صُحُفًۭا مُّنَشَّرَةًۭ
  Unverified discovery rationale: terra: Each rejecter demands personally spread pages, replacing reception of the common reminder with a condition of his own making.
- (76:30) [luna: medium (missing-ayat turn); basis: neighbour+theme] وَمَا تَشَآءُونَ إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ إِنَّ ٱللَّهَ كَانَ عَلِيمًا حَكِيمًۭا
  Unverified discovery rationale: luna: The following ayah says human willing depends on God's will, completing 76:29's invitation to take the reminder's path.
- (79:17) [terra: medium (missing-ayat turn); basis: neighbour+scene+speaker] ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ
  Unverified discovery rationale: terra: Moses is commanded to go to the transgressing Pharaoh, identifying the receiver to whom purification and fear will be offered in the following ayat.
- (81:27) [terra: medium; basis: root+theme] إِنْ هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ
  Unverified discovery rationale: terra: The Quran is a reminder to all worlds, establishing the breadth of the offer before the next ayah specifies its willing receiver.
- (81:28) [terra: medium; basis: neighbour+scene] لِمَن شَآءَ مِنكُمْ أَن يَسْتَقِيمَ
  Unverified discovery rationale: terra: It addresses whoever among the hearers wills to take a straight course, distinguishing public presentation from actual uptake.
- (81:29) [terra: medium; basis: neighbour+theme] وَمَا تَشَآءُونَ إِلَّآ أَن يَشَآءَ ٱللَّهُ رَبُّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: terra: Human willing remains dependent on the will of the Lord of the worlds, supplying the divine boundary around reception.
- (88:22) [luna: contrast; terra: medium; basis: contrast+neighbour+speaker+theme] لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
  Unverified discovery rationale: luna: The Prophet is not a controller over his hearers; this boundary clarifies why the section distinguishes giving a reminder from forcing its acceptance. | terra: The Prophet is not a controller over the hearers, completing 88:21's definition of his role as reminder alone.
- (103:3) [terra: medium (missing-ayat turn); basis: scene+theme] إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَتَوَاصَوْا۟ بِٱلْحَقِّ وَتَوَاصَوْا۟ بِٱلصَّبْرِ
  Unverified discovery rationale: terra: Those saved from loss mutually counsel truth and patience, a reciprocal form of reminder passing from one person to another and being sustained in community.

## weak (2)

- (20:117) [terra: weak (missing-ayat turn); basis: root+theme] فَقُلْنَا يَٰٓـَٔادَمُ إِنَّ هَٰذَا عَدُوٌّۭ لَّكَ وَلِزَوْجِكَ فَلَا يُخْرِجَنَّكُمَا مِنَ ٱلْجَنَّةِ فَتَشْقَىٰٓ
  Unverified discovery rationale: terra: Adam is warned that expulsion from the Garden would make him تَشْقَىٰ; this uses the wretchedness root for worldly toil, a secondary sense distinct from 87:11's moral superlative.
- (28:11) [terra: weak; basis: root] وَقَالَتْ لِأُخْتِهِۦ قُصِّيهِ ۖ فَبَصُرَتْ بِهِۦ عَن جُنُبٍۢ وَهُمْ لَا يَشْعُرُونَ
  Unverified discovery rationale: terra: Moses' sister watches him عَن جُنُبٍ, “from a distance”; this is a specific but purely spatial occurrence of the root sense used interpretively for keeping reminder far away.

## contrast (17)

- (2:74) [terra: contrast; basis: contrast+scene+theme] ثُمَّ قَسَتْ قُلُوبُكُم مِّنۢ بَعْدِ ذَٰلِكَ فَهِىَ كَٱلْحِجَارَةِ أَوْ أَشَدُّ قَسْوَةًۭ ۚ وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ ۚ وَإِنَّ مِنْهَا لَمَا يَشَّقَّقُ فَيَخْرُجُ مِنْهُ ٱلْمَآءُ ۚ وَإِنَّ مِنْهَا لَمَا يَهْبِطُ مِنْ خَشْيَةِ ٱللَّهِ ۗ وَمَا ٱللَّهُ بِغَٰفِلٍ عَمَّا تَعْمَلُونَ
  Unverified discovery rationale: terra: Some stones fall from fear of God while the addressed hearts harden after signs, a material reversal of knowledgeable fear receiving reminder.
- (2:171) [terra: contrast; basis: contrast+scene+theme] وَمَثَلُ ٱلَّذِينَ كَفَرُوا۟ كَمَثَلِ ٱلَّذِى يَنْعِقُ بِمَا لَا يَسْمَعُ إِلَّا دُعَآءًۭ وَنِدَآءًۭ ۚ صُمٌّۢ بُكْمٌ عُمْىٌۭ فَهُمْ لَا يَعْقِلُونَ
  Unverified discovery rationale: terra: Disbelievers are likened to creatures hearing only a call without understanding—deaf, dumb, and blind—so sound reaches them while reminder does not.
- (4:31) [terra: contrast; basis: contrast+root] إِن تَجْتَنِبُوا۟ كَبَآئِرَ مَا تُنْهَوْنَ عَنْهُ نُكَفِّرْ عَنكُمْ سَيِّـَٔاتِكُمْ وَنُدْخِلْكُم مُّدْخَلًۭا كَرِيمًۭا
  Unverified discovery rationale: terra: Avoiding the major forbidden acts leads to sins being effaced, another boundary showing distance as obedience when directed at evil.
- (5:90) [terra: contrast; basis: contrast+root] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِنَّمَا ٱلْخَمْرُ وَٱلْمَيْسِرُ وَٱلْأَنصَابُ وَٱلْأَزْلَٰمُ رِجْسٌۭ مِّنْ عَمَلِ ٱلشَّيْطَٰنِ فَٱجْتَنِبُوهُ لَعَلَّكُمْ تُفْلِحُونَ
  Unverified discovery rationale: terra: The command فَٱجْتَنِبُوهُ directs avoidance toward intoxicants, gambling, idols, and divining arrows; the root itself is sound, while 87:11 exposes its wrong object.
- (22:46) [terra: contrast; basis: contrast+scene] أَفَلَمْ يَسِيرُوا۟ فِى ٱلْأَرْضِ فَتَكُونَ لَهُمْ قُلُوبٌۭ يَعْقِلُونَ بِهَآ أَوْ ءَاذَانٌۭ يَسْمَعُونَ بِهَا ۖ فَإِنَّهَا لَا تَعْمَى ٱلْأَبْصَٰرُ وَلَٰكِن تَعْمَى ٱلْقُلُوبُ ٱلَّتِى فِى ٱلصُّدُورِ
  Unverified discovery rationale: terra: The ayah says eyes do not go blind but hearts do, explaining why ʿAbasa's blind visitor can receive reminder while sighted people avoid it.
- (22:72) [terra: contrast (missing-ayat turn); basis: contrast+scene] وَإِذَا تُتْلَىٰ عَلَيْهِمْ ءَايَٰتُنَا بَيِّنَٰتٍۢ تَعْرِفُ فِى وُجُوهِ ٱلَّذِينَ كَفَرُوا۟ ٱلْمُنكَرَ ۖ يَكَادُونَ يَسْطُونَ بِٱلَّذِينَ يَتْلُونَ عَلَيْهِمْ ءَايَٰتِنَا ۗ قُلْ أَفَأُنَبِّئُكُم بِشَرٍّۢ مِّن ذَٰلِكُمُ ۗ ٱلنَّارُ وَعَدَهَا ٱللَّهُ ٱلَّذِينَ كَفَرُوا۟ ۖ وَبِئْسَ ٱلْمَصِيرُ
  Unverified discovery rationale: terra: Those who hear clear signs show denial in their faces and nearly attack the reciters; this active aggression marks a sharper refusal than simply keeping reminder distant.
- (35:19) [terra: contrast; basis: contrast+scene] وَمَا يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ
  Unverified discovery rationale: terra: The blind and the seeing are not equal; beside the ʿAbasa scene, this becomes a boundary between physical blindness and the inward sight that receives truth.
- (35:22) [terra: contrast; basis: contrast+neighbour+speaker] وَمَا يَسْتَوِى ٱلْأَحْيَآءُ وَلَا ٱلْأَمْوَٰتُ ۚ إِنَّ ٱللَّهَ يُسْمِعُ مَن يَشَآءُ ۖ وَمَآ أَنتَ بِمُسْمِعٍۢ مَّن فِى ٱلْقُبُورِ
  Unverified discovery rationale: terra: God makes whom He wills hear, while the Prophet cannot make those in graves hear; the reminder-bearer's voice does not control reception.
- (35:23) [terra: contrast; basis: contrast+neighbour+speaker] إِنْ أَنتَ إِلَّا نَذِيرٌ
  Unverified discovery rationale: terra: “You are only a warner” states the same limit as 88:21-22 after the hearing metaphor.
- (40:58) [terra: contrast; basis: contrast+root+scene] وَمَا يَسْتَوِى ٱلْأَعْمَىٰ وَٱلْبَصِيرُ وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَلَا ٱلْمُسِىٓءُ ۚ قَلِيلًۭا مَّا تَتَذَكَّرُونَ
  Unverified discovery rationale: terra: The blind and seeing, believer and evildoer, are not equal, yet little do people remember; remembrance is aligned with inward sight.
- (42:37) [terra: contrast; basis: contrast+root] وَٱلَّذِينَ يَجْتَنِبُونَ كَبَٰٓئِرَ ٱلْإِثْمِ وَٱلْفَوَٰحِشَ وَإِذَا مَا غَضِبُوا۟ هُمْ يَغْفِرُونَ
  Unverified discovery rationale: terra: Those who avoid major sins and indecencies are placed among the lasting recipients of divine provision, reversing the moral object of 87:11's avoidance.
- (80:5) [luna: contrast; terra: contrast; basis: contrast+neighbour+scene] أَمَّا مَنِ ٱسْتَغْنَىٰ
  Unverified discovery rationale: luna: The man who considers himself self-sufficient is contrasted with the fearful visitor who comes seeking reminder in 80:8–9. | terra: The self-sufficient man becomes the object of attention, even though self-sufficiency gives no sign that reminder will benefit him.
- (80:6) [luna: contrast; terra: contrast; basis: contrast+neighbour+scene+speaker] فَأَنتَ لَهُۥ تَصَدَّىٰ
  Unverified discovery rationale: luna: The Prophet is directed toward the self-sufficient man, completing the contrast with the fearful visitor in 80:8–10. | terra: The Prophet attends eagerly to the self-sufficient hearer, reversing the section's principle that fear marks the receptive audience.
- (80:7) [luna: contrast; terra: contrast; basis: contrast+neighbour+scene+speaker] وَمَا عَلَيْكَ أَلَّا يَزَّكَّىٰ
  Unverified discovery rationale: luna: The Prophet is not accountable if the self-sufficient man does not purify himself, contrasting worldly standing with receptive fear. | terra: The Prophet is not responsible if that man does not purify himself, drawing the boundary between transmitting reminder and producing its benefit.
- (91:11) [terra: contrast; basis: contrast+root+scene] كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ
  Unverified discovery rationale: terra: Thamud denies through transgression before its most wretched member rises, setting collective rejection behind the individual ٱلْأَشْقَى.
- (96:11) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+scene] أَرَءَيْتَ إِن كَانَ عَلَى ٱلْهُدَىٰٓ
  Unverified discovery rationale: terra: The forbidden praying servant may himself be upon guidance, reversing the forbidder's assumption about whom the divine address has benefited.
- (96:12) [terra: contrast (missing-ayat turn); basis: contrast+neighbour+scene] أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ
  Unverified discovery rationale: terra: The praying servant may even command God-consciousness, so the person being kept from prayer is himself transmitting the fear-producing call.

## neighbours: within two ayat of a passage the section cites (24)

- (20:1) [next to 20:3] طه
- (20:4) [next to 20:3] تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى
- (20:5) [next to 20:3] ٱلرَّحْمَٰنُ عَلَى ٱلْعَرْشِ ٱسْتَوَىٰ
- (20:42) [next to 20:44] ٱذْهَبْ أَنتَ وَأَخُوكَ بِـَٔايَٰتِى وَلَا تَنِيَا فِى ذِكْرِى
- (20:45) [next to 20:44] قَالَا رَبَّنَآ إِنَّنَا نَخَافُ أَن يَفْرُطَ عَلَيْنَآ أَوْ أَن يَطْغَىٰ
- (20:46) [next to 20:44] قَالَ لَا تَخَافَآ ۖ إِنَّنِى مَعَكُمَآ أَسْمَعُ وَأَرَىٰ
- (20:122) [next to 20:124] ثُمَّ ٱجْتَبَٰهُ رَبُّهُۥ فَتَابَ عَلَيْهِ وَهَدَىٰ
- (35:16) [next to 35:18] إِن يَشَأْ يُذْهِبْكُمْ وَيَأْتِ بِخَلْقٍۢ جَدِيدٍۢ
- (35:17) [next to 35:18] وَمَا ذَٰلِكَ عَلَى ٱللَّهِ بِعَزِيزٍۢ
- (35:20) [next to 35:18] وَلَا ٱلظُّلُمَٰتُ وَلَا ٱلنُّورُ
- (35:26) [next to 35:28] ثُمَّ أَخَذْتُ ٱلَّذِينَ كَفَرُوا۟ ۖ فَكَيْفَ كَانَ نَكِيرِ
- (35:27) [next to 35:28] أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦ ثَمَرَٰتٍۢ مُّخْتَلِفًا أَلْوَٰنُهَا ۚ وَمِنَ ٱلْجِبَالِ جُدَدٌۢ بِيضٌۭ وَحُمْرٌۭ مُّخْتَلِفٌ أَلْوَٰنُهَا وَغَرَابِيبُ سُودٌۭ
- (35:29) [next to 35:28] إِنَّ ٱلَّذِينَ يَتْلُونَ كِتَٰبَ ٱللَّهِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَأَنفَقُوا۟ مِمَّا رَزَقْنَٰهُمْ سِرًّۭا وَعَلَانِيَةًۭ يَرْجُونَ تِجَٰرَةًۭ لَّن تَبُورَ
- (35:30) [next to 35:28] لِيُوَفِّيَهُمْ أُجُورَهُمْ وَيَزِيدَهُم مِّن فَضْلِهِۦٓ ۚ إِنَّهُۥ غَفُورٌۭ شَكُورٌۭ
- (50:43) [next to 50:45] إِنَّا نَحْنُ نُحْىِۦ وَنُمِيتُ وَإِلَيْنَا ٱلْمَصِيرُ
- (50:44) [next to 50:45] يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًۭا ۚ ذَٰلِكَ حَشْرٌ عَلَيْنَا يَسِيرٌۭ
- (51:53) [next to 51:55] أَتَوَاصَوْا۟ بِهِۦ ۚ بَلْ هُمْ قَوْمٌۭ طَاغُونَ
- (51:54) [next to 51:55] فَتَوَلَّ عَنْهُمْ فَمَآ أَنتَ بِمَلُومٍۢ
- (51:56) [next to 51:55] وَمَا خَلَقْتُ ٱلْجِنَّ وَٱلْإِنسَ إِلَّا لِيَعْبُدُونِ
- (51:57) [next to 51:55] مَآ أُرِيدُ مِنْهُم مِّن رِّزْقٍۢ وَمَآ أُرِيدُ أَن يُطْعِمُونِ
- (79:16) [next to 79:18] إِذْ نَادَىٰهُ رَبُّهُۥ بِٱلْوَادِ ٱلْمُقَدَّسِ طُوًى
- (88:19) [next to 88:21] وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ
- (88:20) [next to 88:21] وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ
- (88:25) [next to 88:23] إِنَّ إِلَيْنَآ إِيَابَهُمْ

===== Discovery accuracy findings (unverified; inspect canonical text) =====
{"surah": 87, "section": 17, "run_tag": "sol-session-20261005", "source_sha256": "5e9ef0a461cc99bfb9b4c0e1b4609dd85b292c96610df2a0bb8cfe5bd670daa3", "list_sha256": "ef7474a6f27909cddcd2b2812338b3602bcb2dae6929c5bd6a51307c46f21031", "models": {"luna": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec17/luna/run.log.json", "consolidation": {"mode": "separate-proposals-v1", "raw_proposal_rows": 33, "unique_additions": 33, "repeated_proposals": [], "turn1_sha256": "97f56d4cfbf406195cb35670642aac0502475709cee9a2cd8e65e62dadece578", "followup_sha256": "bd5035162363e856e6eaa1fdae04651c9ca7c3c385bac2c192d876b90205a03a", "proposal_file": "followup.tsv", "proposal_sha256": "bd5035162363e856e6eaa1fdae04651c9ca7c3c385bac2c192d876b90205a03a", "list_sha256": "f883a6340c5b01b7fec3b5c22b723e1a82208354bf28713c2f8369290a9f0efd", "policy": "First occurrence retained; no existing row or grade changed. Raw followup.tsv preserved."}, "validation_review": {"status": "unverified discovery notes; adjudicator must check canonical text", "agent_completion_notes": [], "policy": "Raw discoveries retained; quotation flags are review aids, not semantic verdicts."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec17/luna/list.tsv", "rows": 191, "schema_errors": [], "duplicates": {}, "arabic_findings": [{"line": 1, "ref": "80:4", "arabic": "ذ ك ر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 1, "ref": "80:4", "arabic": "ن ف ع", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 11, "ref": "80:11", "arabic": "ذ ك ر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 13, "ref": "51:55", "arabic": "ذ ك ر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 13, "ref": "51:55", "arabic": "ن ف ع", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 19, "ref": "20:3", "arabic": "مَن يَخْشَىٰ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": ["87:10"], "matching_ref_count": 1}, {"line": 23, "ref": "79:19", "arabic": "خشية", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 23, "ref": "79:19", "arabic": "ه د ي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 32, "ref": "35:28", "arabic": "خشية", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 41, "ref": "74:49", "arabic": "ج ن ب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 45, "ref": "74:54", "arabic": "ذ ك ر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 55, "ref": "92:12", "arabic": "ه د ي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 60, "ref": "92:17", "arabic": "ج ن ب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 72, "ref": "20:123", "arabic": "ه د ي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 81, "ref": "91:9", "arabic": "قَدْ أَفْلَحَ مَن زَكَّاهَا", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 102, "ref": "29:45", "arabic": "ذكر", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 125, "ref": "4:43", "arabic": "ج ن ب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 127, "ref": "4:36", "arabic": "ج ن ب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 128, "ref": "39:56", "arabic": "ج ن ب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 168, "ref": "20:47", "arabic": "ه د ي", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 170, "ref": "74:42", "arabic": "ج ن ب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 171, "ref": "74:43", "arabic": "ج ن ب", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}, "terra": {"run_log": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec17/terra/run.log.json", "consolidation": {"mode": "separate-proposals-v1", "raw_proposal_rows": 67, "unique_additions": 67, "repeated_proposals": [], "turn1_sha256": "b45703651739b535687b4f77165f1c0b8047f16dfb8d2fda7820af67398d160f", "followup_sha256": "b030714912d76936ddbc3ed566d5fd1553bfe28c5f4646446f491e0f792d40bd", "proposal_file": "followup.tsv", "proposal_sha256": "b030714912d76936ddbc3ed566d5fd1553bfe28c5f4646446f491e0f792d40bd", "list_sha256": "b57cec30710f46dda9195aeb529733ff64eecc5167187308e14ff4d36e693c68", "policy": "First occurrence retained; no existing row or grade changed. Raw followup.tsv preserved."}, "validation_review": {"status": "unverified discovery notes; adjudicator must check canonical text", "agent_completion_notes": [], "policy": "Raw discoveries retained; quotation flags are review aids, not semantic verdicts."}, "validation": {"file": "/Volumes/aro/projects/prose_generation/_commentary/v16/out/s087/discovery/sol-session-20261005/sec17/terra/list.tsv", "rows": 267, "schema_errors": [], "duplicates": {}, "arabic_findings": [{"line": 23, "ref": "11:34", "arabic": "نَفْع", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 35, "ref": "11:108", "arabic": "ٱلْأَشْقَى", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 36, "ref": "91:12", "arabic": "ٱلْأَشْقَى", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 53, "ref": "4:43", "arabic": "يَتَجَنَّبُهَا", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 56, "ref": "39:17", "arabic": "يَجْتَنِبُوا۟ ٱلطَّاغُوتَ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 145, "ref": "20:123", "arabic": "شقاء", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 147, "ref": "20:2", "arabic": "تَشْقَىٰ", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}, {"line": 166, "ref": "91:11", "arabic": "ٱلْأَشْقَى", "finding": "Arabic wording absent from cited ayah; review quotation/root/dictionary form", "matching_refs": [], "matching_ref_count": 0}], "limits": "Orthographic normalization only; roots, paraphrases and word segmentation require review. No semantic or relevance validation."}}}}

