Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 12 of 14 ("Gözden kaybolmak: yolcuyu götüren yol ve toprakta yitip giden"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 12 (prose paragraphs numbered) =====
[¶59] Bir şeyin gözden kaybolmasının iki türü vardır. "Sırat" kelimesinin kökü, geçip giderken gözden kaybolmayı anlatır: {ar:أصل صحيح واحد يدل على غيبة في مر وذهاب؛ سرطت الطعام إذا بلعته لأنه إذا سرط غاب, tr:aslun sahîhun vâhidun yedüllü alâ gaybetin fî merrin ve zehâb; seratu't-taâme izâ bele'tüh, gloss:geçip giderken gözden kaybolmaya işaret eden bir köktür; yemeği yuttuğumda "seratu" derim, çünkü yutulan yemek kaybolur, source:"ص ر ط,B002"}. Yutulan lokma boğazdan geçer ve gider, fakat bedenin içinde varması gereken yere varır. Bir açıklamaya göre yol da bu adı aynı sebeple almıştır: {ar:لأن الذاهب فيه يغيب, tr:li-enne'z-zâhibe fîhi yegîb, gloss:çünkü yolda giden gözden kaybolur, source:"ص ر ط,B001"}. Yolcu yol boyunca ilerler ve bakanın gözünden çıkar, ama yolun bir yönü ve bir varış yeri vardır. Yedinci ayetin son kelimesi ise öbür türü anlatır: {ar:ضل الشيء إذا خفي وغاب؛ أئذا ضللنا في الأرض أي خفينا وغبنا, tr:dalle'ş-şey'ü izâ hafiye ve gâb, gloss:şey gizlenip kayboldu; "toprakta kaybolduğumuzda mı" sözü, gizlenip yok olduğumuzda demektir, source:"ض ل ل,B002"}. Bu kelimenin aslı kaybolmaktır: {ar:أصل الضلال الغيبوبة, tr:aslü'd-dalâli'l-gaybûbe, gloss:dalâlin aslı kaybolmaktır, source:"ض ل ل,B002"}. Ölü toprağa gömüldüğünde bu fiil kullanılır: {ar:أضل الميت إذا دفن, tr:udılle'l-meyyit, gloss:ölü gömüldü, source:"ض ل ل,B002"}. Suya karışan süt de böyle anılır: {ar:ضل اللبن في الماء ثم استهلك, tr:dalle'l-lebenü fi'l-mâ', gloss:süt suya karışıp kayboldu, source:"ض ل ل,B002"}. Kimsenin nereye gittiğini bilmediği kişi için de aynı söz söylenir: {ar:ذهب فلان ضلة إذا لم يدر أين ذهب, tr:zehebe fülânün dılleten, gloss:falanca gitti ve nereye gittiği bilinmedi, source:"ض ل ل,B003"}. Hafızadan silinen bir şey de bu kelimeyle anlatılır: {ar:أن تضل إحداهما أي تغيب عن حفظها أو يغيب حفظها عنها, tr:en tadılle ihdâhümâ, gloss:biri unutursa, yani olay hafızasından kaybolursa, source:"ض ل ل,B004"}.

[¶60] Bu iki tanım aynı fiili, "gâbe"yi kullanır. Yolcu yolda kaybolur, kaybolan şey de toprakta ya da suda kaybolur. Aradaki fark nereye gidildiğindedir. Altıncı ve yedinci ayetler bu iki kayboluşu karşı karşıya koyar. Sırat, yolcuyu gözden çıkarır, fakat bir yere ulaştırır. Dalâl ise kişiyi nereye gittiği bilinmeyecek şekilde yok eder. Düz bir meal "dosdoğru yol" ile "sapanlar"ı birbirinin zıddı sayar. Görüntü ise ikisinin de bir gidiş olduğunu, birinin varılacak yeri olduğunu, öbürünün olmadığını gösterir.

[¶61] Kur'an'da bu kayboluş birçok sahnede yer alır. Dirilişi inkâr edenler şöyle sorar: {ar:أَءِذَا ضَلَلْنَا فِى ٱلْأَرْضِ أَءِنَّا لَفِى خَلْقٍۢ جَدِيدٍۭ, tr:e-izâ dalelnâ fi'l-ardı e-innâ le-fî halkın cedîd, gloss:toprakta kaybolup gittiğimizde mi yeniden yaratılacağız, source:32:10}. Kur'an bu soruyu şöyle cevaplar: {ar:بَلْ هُم بِلِقَآءِ رَبِّهِمْ كَٰفِرُونَ, tr:bel hüm bi-likâi rabbihim kâfirûn, gloss:hayır, onlar Rablerine kavuşmayı inkâr ediyorlar, source:32:10}. Onlara göre toprakta kaybolmak bir son, Kur'an'a göre ise bir kavuşmanın yoludur. Hepsinin toplanacağı günde şirk koşanlara ortakları sorulur {source:6:22}. Uydurdukları şeyler o zaman kaybolup gider: {ar:وَضَلَّ عَنْهُم مَّا كَانُوا۟ يَفْتَرُونَ, tr:ve dalle anhüm mâ kânû yefterûn, gloss:uydurdukları şeyler onlardan kaybolup gitti, source:6:24}. Din gününde kimse gözden kaybolamaz: {ar:وَمَا هُمْ عَنْهَا بِغَآئِبِينَ, tr:ve mâ hüm anhâ bi-gâibîn, gloss:oradan uzaklaşıp kaybolamazlar, source:82:16}. Firavun Musa'ya geçmiş nesilleri sorar {source:20:51}. Musa şöyle cevap verir: {ar:عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى, tr:ilmühâ inde rabbî fî kitâb, lâ yadıllu rabbî ve lâ yensâ, gloss:onların bilgisi Rabbimin katında bir kitaptadır; Rabbim ne bir şeyi kaybeder ne de unutur, source:20:52}. Burada "dalle" fiili, unutmanın yanında, bir şeyin izini yitirmek anlamında kullanılır ve Rabden bu kayıp tamamen uzak tutulur. Yusuf'un kuyudaki kayboluşu ise varış yeri olan bir kayboluştur. Kardeşleri onu {ar:غَيَٰبَتِ ٱلْجُبِّ, tr:gayâbeti'l-cübb, gloss:kuyunun gözden ırak dibi, source:12:10} denilen yere atmak ister, fakat bu kaybolma onu bir yola, yolcuların eline ulaştırır. Gözü kapatılmış kimseler ise yolu bulmak için koşuşur: {ar:فَٱسْتَبَقُوا۟ ٱلصِّرَٰطَ فَأَنَّىٰ يُبْصِرُونَ, tr:festebeku's-sırâta fe-ennâ yübsırûn, gloss:yola doğru koşuşsalar da nasıl görebilirler, source:36:66}.

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

===== passages from the discovery list (294) =====
## strong (197)

- (2:28) [luna: strong; basis: contrast+scene+theme] كَيْفَ تَكْفُرُونَ بِٱللَّهِ وَكُنتُمْ أَمْوَٰتًۭا فَأَحْيَٰكُمْ ۖ ثُمَّ يُمِيتُكُمْ ثُمَّ يُحْيِيكُمْ ثُمَّ إِلَيْهِ تُرْجَعُونَ
  Unverified discovery rationale: luna: This verse describes people as dead, then given life, then dying and being revived before returning to God; it makes earthly disappearance one stage in a movement to a destination.
- (2:108) [luna: strong; terra: contrast; basis: contrast+root+scene] أَمْ تُرِيدُونَ أَن تَسْـَٔلُوا۟ رَسُولَكُمْ كَمَا سُئِلَ مُوسَىٰ مِن قَبْلُ ۗ وَمَن يَتَبَدَّلِ ٱلْكُفْرَ بِٱلْإِيمَٰنِ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
  Unverified discovery rationale: luna: The section’s named root ض ل ل is used with the way itself: whoever exchanges belief for disbelief has strayed from سَوَاءَ السَّبِيلِ, a direct instance of losing the route. | terra: Changing faith for disbelief makes a person ضَلَّ from the even way; this names the departure from a route whose straightness the source contrasts with loss.
- (2:259) [luna: strong (missing-ayat turn); terra: strong (missing-ayat turn); basis: contrast+scene+theme] أَوْ كَٱلَّذِى مَرَّ عَلَىٰ قَرْيَةٍۢ وَهِىَ خَاوِيَةٌ عَلَىٰ عُرُوشِهَا قَالَ أَنَّىٰ يُحْىِۦ هَٰذِهِ ٱللَّهُ بَعْدَ مَوْتِهَا ۖ فَأَمَاتَهُ ٱللَّهُ مِا۟ئَةَ عَامٍۢ ثُمَّ بَعَثَهُۥ ۖ قَالَ كَمْ لَبِثْتَ ۖ قَالَ لَبِثْتُ يَوْمًا أَوْ بَعْضَ يَوْمٍۢ ۖ قَالَ بَل لَّبِثْتَ مِا۟ئَةَ عَامٍۢ فَٱنظُرْ إِلَىٰ طَعَامِكَ وَشَرَابِكَ لَمْ يَتَسَنَّهْ ۖ وَٱنظُرْ إِلَىٰ حِمَارِكَ وَلِنَجْعَلَكَ ءَايَةًۭ لِّلنَّاسِ ۖ وَٱنظُرْ إِلَى ٱلْعِظَامِ كَيْفَ نُنشِزُهَا ثُمَّ نَكْسُوهَا لَحْمًۭا ۚ فَلَمَّا تَبَيَّنَ لَهُۥ قَالَ أَعْلَمُ أَنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: luna: A traveler sees a ruined town and asks how God will give it life after death; God makes him die for a hundred years and revives him, turning apparent disappearance into a demonstrated return. | terra: The man who passes a ruined town is made dead for a hundred years and then raised; his question about life after ruin makes vanished life a divinely reversible interval.
- (2:260) [terra: strong (missing-ayat turn); basis: scene+theme] وَإِذْ قَالَ إِبْرَٰهِۦمُ رَبِّ أَرِنِى كَيْفَ تُحْىِ ٱلْمَوْتَىٰ ۖ قَالَ أَوَلَمْ تُؤْمِن ۖ قَالَ بَلَىٰ وَلَٰكِن لِّيَطْمَئِنَّ قَلْبِى ۖ قَالَ فَخُذْ أَرْبَعَةًۭ مِّنَ ٱلطَّيْرِ فَصُرْهُنَّ إِلَيْكَ ثُمَّ ٱجْعَلْ عَلَىٰ كُلِّ جَبَلٍۢ مِّنْهُنَّ جُزْءًۭا ثُمَّ ٱدْعُهُنَّ يَأْتِينَكَ سَعْيًۭا ۚ وَٱعْلَمْ أَنَّ ٱللَّهَ عَزِيزٌ حَكِيمٌۭ
  Unverified discovery rationale: terra: Abraham's scattered bird-parts are called and come swiftly, a concrete scene in which what has been dispersed beyond ordinary sight returns to a summons.
- (2:282) [luna: strong; terra: strong; basis: root+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ ۚ وَلْيَكْتُب بَّيْنَكُمْ كَاتِبٌۢ بِٱلْعَدْلِ ۚ وَلَا يَأْبَ كَاتِبٌ أَن يَكْتُبَ كَمَا عَلَّمَهُ ٱللَّهُ ۚ فَلْيَكْتُبْ وَلْيُمْلِلِ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ وَلَا يَبْخَسْ مِنْهُ شَيْـًۭٔا ۚ فَإِن كَانَ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ سَفِيهًا أَوْ ضَعِيفًا أَوْ لَا يَسْتَطِيعُ أَن يُمِلَّ هُوَ فَلْيُمْلِلْ وَلِيُّهُۥ بِٱلْعَدْلِ ۚ وَٱسْتَشْهِدُوا۟ شَهِيدَيْنِ مِن رِّجَالِكُمْ ۖ فَإِن لَّمْ يَكُونَا رَجُلَيْنِ فَرَجُلٌۭ وَٱمْرَأَتَانِ مِمَّن تَرْضَوْنَ مِنَ ٱلشُّهَدَآءِ أَن تَضِلَّ إِحْدَىٰهُمَا فَتُذَكِّرَ إِحْدَىٰهُمَا ٱلْأُخْرَىٰ ۚ وَلَا يَأْبَ ٱلشُّهَدَآءُ إِذَا مَا دُعُوا۟ ۚ وَلَا تَسْـَٔمُوٓا۟ أَن تَكْتُبُوهُ صَغِيرًا أَوْ كَبِيرًا إِلَىٰٓ أَجَلِهِۦ ۚ ذَٰلِكُمْ أَقْسَطُ عِندَ ٱللَّهِ وَأَقْوَمُ لِلشَّهَٰدَةِ وَأَدْنَىٰٓ أَلَّا تَرْتَابُوٓا۟ ۖ إِلَّآ أَن تَكُونَ تِجَٰرَةً حَاضِرَةًۭ تُدِيرُونَهَا بَيْنَكُمْ فَلَيْسَ عَلَيْكُمْ جُنَاحٌ أَلَّا تَكْتُبُوهَا ۗ وَأَشْهِدُوٓا۟ إِذَا تَبَايَعْتُمْ ۚ وَلَا يُضَآرَّ كَاتِبٌۭ وَلَا شَهِيدٌۭ ۚ وَإِن تَفْعَلُوا۟ فَإِنَّهُۥ فُسُوقٌۢ بِكُمْ ۗ وَٱتَّقُوا۟ ٱللَّهَ ۖ وَيُعَلِّمُكُمُ ٱللَّهُ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ
  Unverified discovery rationale: luna: The section’s named root ض ل ل has a dictionary branch for an event disappearing from memory; here أَنْ تَضِلَّ إِحْدَاهُمَا is paired with the other woman reminding her, showing how a lost recollection is recovered. | terra: تَضِلَّ describes one witness's memory failing so the other can remind her, the source's explicit secondary sense of ضَلَل as something lost from remembrance.
- (4:44) [luna: strong; basis: root+scene] أَلَمْ تَرَ إِلَى ٱلَّذِينَ أُوتُوا۟ نَصِيبًۭا مِّنَ ٱلْكِتَٰبِ يَشْتَرُونَ ٱلضَّلَٰلَةَ وَيُرِيدُونَ أَن تَضِلُّوا۟ ٱلسَّبِيلَ
  Unverified discovery rationale: luna: The section’s named root ض ل ل appears in the wish that others lose the way; this verse says some People of the Book want believers to تَضِلُّوا السَّبِيلَ, making misdirection an intended diversion from a route.
- (4:88) [terra: strong (missing-ayat turn); basis: root+theme] ۞ فَمَا لَكُمْ فِى ٱلْمُنَٰفِقِينَ فِئَتَيْنِ وَٱللَّهُ أَرْكَسَهُم بِمَا كَسَبُوٓا۟ ۚ أَتُرِيدُونَ أَن تَهْدُوا۟ مَنْ أَضَلَّ ٱللَّهُ ۖ وَمَن يُضْلِلِ ٱللَّهُ فَلَن تَجِدَ لَهُۥ سَبِيلًۭا
  Unverified discovery rationale: terra: For one whom God leaves astray, no path can be found; the verse joins the source's loss-word to the failure to locate a route.
- (5:16) [luna: strong; terra: medium; basis: contrast+root+scene+theme] يَهْدِى بِهِ ٱللَّهُ مَنِ ٱتَّبَعَ رِضْوَٰنَهُۥ سُبُلَ ٱلسَّلَٰمِ وَيُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ بِإِذْنِهِۦ وَيَهْدِيهِمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
  Unverified discovery rationale: luna: The section’s named root ص ر ط depicts a route that takes a traveler somewhere; here guidance leads from darkness to light and to the straight path, specifying the change and destination of the journey. | terra: Through revelation God leads to paths of peace, brings people from darkness to light, and guides to a straight path; visibility and destination reinforce the source's image.
- (5:77) [luna: strong; terra: contrast; basis: contrast+root+scene] قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ لَا تَغْلُوا۟ فِى دِينِكُمْ غَيْرَ ٱلْحَقِّ وَلَا تَتَّبِعُوٓا۟ أَهْوَآءَ قَوْمٍۢ قَدْ ضَلُّوا۟ مِن قَبْلُ وَأَضَلُّوا۟ كَثِيرًۭا وَضَلُّوا۟ عَن سَوَآءِ ٱلسَّبِيلِ
  Unverified discovery rationale: luna: The section links ض ل ل to the traveler’s course; this verse describes people who strayed from the sound way and led many others astray, turning the path image into a chain of diverted travelers. | terra: People who went astray, led many astray, and strayed from the level way show ضَلَال as social misdirection that leaves the proper route.
- (6:22) [luna: strong; terra: strong; basis: neighbour+scene+theme] [cited in ¶61] وَيَوْمَ نَحْشُرُهُمْ جَمِيعًۭا ثُمَّ نَقُولُ لِلَّذِينَ أَشْرَكُوٓا۟ أَيْنَ شُرَكَآؤُكُمُ ٱلَّذِينَ كُنتُمْ تَزْعُمُونَ
  Unverified discovery rationale: luna: The section places the disappearance of false partners at the gathering; this verse stages that gathering and asks the associators where their claimed partners are. | terra: The gathering of all the associators supplies the judgment scene in which their claimed partners will prove absent in 6:24; none can disappear from that assembly.
- (6:23) [luna: strong; basis: neighbour+scene] ثُمَّ لَمْ تَكُن فِتْنَتُهُمْ إِلَّآ أَن قَالُوا۟ وَٱللَّهِ رَبِّنَا مَا كُنَّا مُشْرِكِينَ
  Unverified discovery rationale: luna: This verse gives the associators’ denial in the gathering scene begun in 6:22; 6:24 then says their fabricated claims have vanished, so this row contributes the denial immediately before that exposure.
- (6:24) [luna: strong; terra: strong; basis: contrast+root+scene+theme] [cited in ¶61] ٱنظُرْ كَيْفَ كَذَبُوا۟ عَلَىٰٓ أَنفُسِهِمْ ۚ وَضَلَّ عَنْهُم مَّا كَانُوا۟ يَفْتَرُونَ
  Unverified discovery rationale: luna: The section says fabricated partners disappear from their worshippers at the gathering; this verse states وَضَلَّ عَنْهُم مَا كَانُوا يَفْتَرُونَ, making the vanished claim itself the focus. | terra: Their inventions ضَلَّ عَنْهُمْ, vanish away from them at judgment, giving the source's loss-image a concrete eschatological scene.
- (6:39) [luna: strong (missing-ayat turn); terra: strong (missing-ayat turn); basis: contrast+root+scene+theme] وَٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِنَا صُمٌّۭ وَبُكْمٌۭ فِى ٱلظُّلُمَٰتِ ۗ مَن يَشَإِ ٱللَّهُ يُضْلِلْهُ وَمَن يَشَأْ يَجْعَلْهُ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
  Unverified discovery rationale: luna: This verse describes deaf and mute people in darkness, then contrasts those God leaves astray with those He places on a straight path; the lost and guided courses are explicit. | terra: Those who deny the signs are deaf and mute in darkness, while God may place another on a straight path; obscured perception and the road are explicitly paired.
- (6:59) [luna: strong (missing-ayat turn); terra: strong; basis: contrast+scene+theme] ۞ وَعِندَهُۥ مَفَاتِحُ ٱلْغَيْبِ لَا يَعْلَمُهَآ إِلَّا هُوَ ۚ وَيَعْلَمُ مَا فِى ٱلْبَرِّ وَٱلْبَحْرِ ۚ وَمَا تَسْقُطُ مِن وَرَقَةٍ إِلَّا يَعْلَمُهَا وَلَا حَبَّةٍۢ فِى ظُلُمَٰتِ ٱلْأَرْضِ وَلَا رَطْبٍۢ وَلَا يَابِسٍ إِلَّا فِى كِتَٰبٍۢ مُّبِينٍۢ
  Unverified discovery rationale: luna: The verse says no leaf falls without God knowing it and mentions a grain in earth’s darknesses kept in a clear record; it reverses the section’s image of something hidden as something lost. | terra: Leaves, grain in earth's darkness, and every moist or dry thing remain in a clear record; what is hidden in earth is never lost to the knower who does not يَضِلُّ or forget.
- (6:71) [luna: strong; terra: strong; basis: contrast+root+scene+theme] قُلْ أَنَدْعُوا۟ مِن دُونِ ٱللَّهِ مَا لَا يَنفَعُنَا وَلَا يَضُرُّنَا وَنُرَدُّ عَلَىٰٓ أَعْقَابِنَا بَعْدَ إِذْ هَدَىٰنَا ٱللَّهُ كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا ۗ قُلْ إِنَّ هُدَى ٱللَّهِ هُوَ ٱلْهُدَىٰ ۖ وَأُمِرْنَا لِنُسْلِمَ لِرَبِّ ٱلْعَٰلَمِينَ
  Unverified discovery rationale: luna: The section distinguishes a traveler who vanishes from view while following a route from someone lost without knowing where he is going; this verse pictures a حَيْرَان person in the land while companions call him toward guidance. | terra: The simile is a person bewildered on the earth after devils have lured him away, while companions call him back to guidance; it is the source's destinationless going versus a called route.
- (6:76) [terra: strong; basis: scene+theme] فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ رَءَا كَوْكَبًۭا ۖ قَالَ هَٰذَا رَبِّى ۖ فَلَمَّآ أَفَلَ قَالَ لَآ أُحِبُّ ٱلْءَافِلِينَ
  Unverified discovery rationale: terra: Abraham watches a star set and rejects what disappears; the visible vanishing of a supposed lord begins a scene whose next ayah joins guidance and ضَلَال.
- (6:77) [luna: strong; terra: strong; basis: contrast+root+scene+theme] فَلَمَّا رَءَا ٱلْقَمَرَ بَازِغًۭا قَالَ هَٰذَا رَبِّى ۖ فَلَمَّآ أَفَلَ قَالَ لَئِن لَّمْ يَهْدِنِى رَبِّى لَأَكُونَنَّ مِنَ ٱلْقَوْمِ ٱلضَّآلِّينَ
