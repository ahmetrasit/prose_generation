Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 15 of 18 ("Koşan dizi: önde, ardında, sonda"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 15 (prose paragraphs numbered) =====
[¶58] On altıncı ve on yedinci ayetteki zaman kelimeleri, hareket halindeki bir at ya da deve dizisinde yer de bildirir. Birinci ayetteki tesbih fiilinin kökünde koşan at vardır: {ar:السابح من الخيل يمد يديه في الجري؛ النجوم تسبح في الفلك, tr:es-sâbihu mine'l-hayli yemuddu yedeyhi fi'l-cerî en-nucûmu tesbehu fi'l-felek, gloss:sâbih koşarken ön ayaklarını uzatan attır; yıldızlar yörüngelerinde yüzer, source:"س ب ح,B004"}. Kökün temel anlamı suda yüzmektir: {ar:سَبَحَ فِي ٱلْمَاءِ, tr:sebeha fi'l-mâ, gloss:suda yüzdü, source:"memory"}. Dizinin başında öncüler vardır: {ar:هوادي الخيل أعناقها أو أول رعيل, tr:hevâdi'l-hayli a'nâkuhâ ev evvelu racîl, gloss:atların hevâdîsi boyunlarıdır ya da ilk bölüktür, source:"ه د ي,B003"}. On beşinci ayetteki namaz kökü ikinci atı adlandırır: {ar:قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه, tr:kad sallâ ve câe musalliyen li-enne ra'sehû yetlu's-salâ'lleẕî beyne yedeyh, gloss:musallî olarak geldi çünkü başı öndekinin sağrısını izler, source:"ص ل و,B006"}. {ar:السابق الأول والمصلي الثاني, tr:es-sâbiku'l-evvel ve'l-musallî es-ŝânî, gloss:sâbık birinci musallî ikincidir, source:"ص ل و,B006"}. Sekizinci ayetin kökü düzgün adımı verir: {ar:دابة حسن التيسور أي حسن نقل القوائم, tr:dâbbetun hasenu't-teysûr ey hasenu nakli'l-kavâim, gloss:ayaklarını güzel atan hayvan, source:"ي س ر,B005"}. On altıncı ayetteki tercih kökü, öne koymaktır: {ar:له أصل تقديم الشيء, tr:lehû aslu takdîmi'ş-şey', gloss:bir şeyi öne koyma anlamında bir kökü vardır, source:"ء ث ر,B001"}. Ama aynı kök birinin izinden gitmek de demektir: {ar:جاء فلان على إثري وأثري وجاء في أثره وإثره, tr:câe fulânun alâ isrî ve eserî ve câe fî eserihî ve isrih, gloss:falanca peşimden geldi; onun izinden geldi, source:"ء ث ر,B004"}. Dünya yakın kıyıdır: {ar:العدوة الدنيا والعدوة القصوى, tr:el-udvetu'd-dunyâ ve'l-udvetu'l-kusvâ, gloss:yakın yamaç ve uzak yamaç, source:"د ن و,B002"}. Ahiret kökü topluluğun arkasında kalanları adlandırır: {ar:أخرى القوم أي من كان في آخرهم, tr:uhra'l-kavmi ey men kâne fî âhirihim, gloss:topluluğun uhrâsı en arkada olandır, source:"ء خ ر,B001"}. Semerin arka direği de bu köktendir: {ar:آخرة الرحل وقادمته ومؤخر الرحل ومقدمه, tr:âhiratu'r-rahli ve kâdimetuhû ve muahharu'r-rahli ve mukaddemuh, gloss:semerin arka ve ön direği, source:"ء خ ر,B003"}. On yedinci ayetteki "kalıcı" kelimesinin ailesinde koşusunun bir kısmını saklayan atlar vardır: {ar:المبقيات من الخيل التي تبقي بعض جريها تدخره, tr:el-mubkıyâtu mine'l-hayli elletî tubkî ba'da cerîhâ teddehıruh, gloss:mubkıyât koşusunun bir kısmını saklayıp biriktiren atlardır, source:"ب ق ي,B004"}. On sekizinci ayetin "ilk" kelimesi de dizinin önündeki deveyi verir: {ar:ناقة أولة وجمل أول إذا تقدما الإبل, tr:nâkatun evvelatun ve cemelun evvelu iẕâ tekaddeme'l-ibil, gloss:develerin önüne geçen dişi deve ve erkek deve, source:"ء و ل,B001"}.

[¶59] Bu dizi içinde on altıncı ve on yedinci ayet bir koşu olarak okunur. Öne koyduğunuz şey yakın olandır. Arkada gelen ise daha hayırlıdır ve daha uzun dayanır, tıpkı koşusunu sona saklayan at gibi. Düz bir anlatım yalnızca iki hayatı karşılaştırır. Bu sahne karşılaştırmaya bir zaman sırası ekler: ilk gelen yarışı kazanan değildir. On beşinci ayetteki "namaz kıldı" fiilinin ailesinde öncünün hemen ardından gelen ikinci at vardır. Bu, bir izleme hareketi olarak duyulur. Ama bu bağ kelimenin namaz anlamının yerine geçmez.

[¶60] Kur'an yemin ettiği koşucularla bir sureyi açar: {ar:وَٱلسَّٰبِحَٰتِ سَبْحًۭا, tr:ve's-sâbihâti sebhâ, gloss:yüzdükçe yüzenlere andolsun, source:79:3}. Bu, Firavun'un "en yüce rabbinizim" dediği ve dünya hayatını tercih edenin anıldığı suredir. Bir başka yerde öndekiler {ar:وَٱلسَّٰبِقُونَ ٱلسَّٰبِقُونَ, tr:ve's-sâbikûne's-sâbikûn, gloss:öne geçenler ise öne geçenlerdir, source:56:10} diye anılır. Yakın ve uzak yamaç, iki topluluğun karşılaştığı günün tasvirinde geçer: {ar:إِذْ أَنتُم بِٱلْعُدْوَةِ ٱلدُّنْيَا وَهُم بِٱلْعُدْوَةِ ٱلْقُصْوَىٰ, tr:iẕ entum bi'l-udveti'd-dunyâ ve hum bi'l-udveti'l-kusvâ, gloss:o gün siz yakın yamaçtaydınız onlar uzak yamaçtaydı, source:8:42}. On altıncı ayetin cümle yapısı başka bir yerde neredeyse aynen tekrarlanır. Orada "yakın" yerine "acele gelen" kelimesi kullanılır: {ar:كَلَّا بَلْ تُحِبُّونَ ٱلْعَاجِلَةَ, tr:kellâ bel tuhibbûne'l-âcile, gloss:hayır; siz acele geleni seviyorsunuz, source:75:20}, {ar:وَتَذَرُونَ ٱلْءَاخِرَةَ, tr:ve teẕerûne'l-âhira, gloss:ve sonra geleni bırakıyorsunuz, source:75:21}. Önce geleni tutup arkadan geleni bırakmak, bu dizideki yanlış sıralamadır.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (228) =====
## strong (126)

- (2:86) [luna: contrast; terra: strong; basis: contrast+root+theme] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْءَاخِرَةِ ۖ فَلَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنصَرُونَ
  Unverified discovery rationale: luna: The section’s preference root ء ث ر names choosing one thing ahead of another; this ayah says people “bought the life of this world for the Hereafter” (ٱشْتَرَوُا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْءَاخِرَةِ), spelling out the cost of the wrong order. | terra: ٱشْتَرَوُا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْـَٔاخِرَةِ treats the wrong ordering as an exchange of the later life for the near one.
- (2:110) [terra: strong (missing-ayat turn); basis: scene+theme] وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ ۚ وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍۢ تَجِدُوهُ عِندَ ٱللَّهِ ۗ إِنَّ ٱللَّهَ بِمَا تَعْمَلُونَ بَصِيرٌۭ
  Unverified discovery rationale: terra: Whatever good people send forward for themselves they will find with God, making present action an advance deposit at the later destination.
- (2:143) [terra: strong (missing-ayat turn); basis: contrast+root+scene] وَكَذَٰلِكَ جَعَلْنَٰكُمْ أُمَّةًۭ وَسَطًۭا لِّتَكُونُوا۟ شُهَدَآءَ عَلَى ٱلنَّاسِ وَيَكُونَ ٱلرَّسُولُ عَلَيْكُمْ شَهِيدًۭا ۗ وَمَا جَعَلْنَا ٱلْقِبْلَةَ ٱلَّتِى كُنتَ عَلَيْهَآ إِلَّا لِنَعْلَمَ مَن يَتَّبِعُ ٱلرَّسُولَ مِمَّن يَنقَلِبُ عَلَىٰ عَقِبَيْهِ ۚ وَإِن كَانَتْ لَكَبِيرَةً إِلَّا عَلَى ٱلَّذِينَ هَدَى ٱللَّهُ ۗ وَمَا كَانَ ٱللَّهُ لِيُضِيعَ إِيمَٰنَكُمْ ۚ إِنَّ ٱللَّهَ بِٱلنَّاسِ لَرَءُوفٌۭ رَّحِيمٌۭ
  Unverified discovery rationale: terra: The change of direction reveals who follows the Messenger and who turns back on his heels, a precise leader-and-follower test with reversal built into the bodily image.
- (2:148) [luna: strong; terra: strong; basis: root+scene+theme] وَلِكُلٍّۢ وِجْهَةٌ هُوَ مُوَلِّيهَا ۖ فَٱسْتَبِقُوا۟ ٱلْخَيْرَٰتِ ۚ أَيْنَ مَا تَكُونُوا۟ يَأْتِ بِكُمُ ٱللَّهُ جَمِيعًا ۚ إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ
  Unverified discovery rationale: luna: The section’s dictionary wording السَّابِقُ الأَوَّل evokes precedence; this ayah uses فَٱسْتَبِقُوا۟ ٱلْخَيْرَٰتِ, “race toward good things,” making that precedence an active pursuit of good. | terra: فَٱسْتَبِقُوا۟ ٱلْخَيْرَٰتِ makes differing directions converge in a race for good, giving the running image its proper object.
- (2:185) [terra: strong (missing-ayat turn); basis: root+theme] شَهْرُ رَمَضَانَ ٱلَّذِىٓ أُنزِلَ فِيهِ ٱلْقُرْءَانُ هُدًۭى لِّلنَّاسِ وَبَيِّنَٰتٍۢ مِّنَ ٱلْهُدَىٰ وَٱلْفُرْقَانِ ۚ فَمَن شَهِدَ مِنكُمُ ٱلشَّهْرَ فَلْيَصُمْهُ ۖ وَمَن كَانَ مَرِيضًا أَوْ عَلَىٰ سَفَرٍۢ فَعِدَّةٌۭ مِّنْ أَيَّامٍ أُخَرَ ۗ يُرِيدُ ٱللَّهُ بِكُمُ ٱلْيُسْرَ وَلَا يُرِيدُ بِكُمُ ٱلْعُسْرَ وَلِتُكْمِلُوا۟ ٱلْعِدَّةَ وَلِتُكَبِّرُوا۟ ٱللَّهَ عَلَىٰ مَا هَدَىٰكُمْ وَلَعَلَّكُمْ تَشْكُرُونَ
  Unverified discovery rationale: terra: God desires ease for people and does not desire hardship, stating the moral polarity behind being eased toward the easy course.
- (2:200) [luna: contrast (missing-ayat turn); terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] فَإِذَا قَضَيْتُم مَّنَٰسِكَكُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَذِكْرِكُمْ ءَابَآءَكُمْ أَوْ أَشَدَّ ذِكْرًۭا ۗ فَمِنَ ٱلنَّاسِ مَن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ
  Unverified discovery rationale: luna: This ayah describes one group asking only for worldly good and having no share in the Hereafter; 2:201 supplies the contrasting prayer for good in both lives, so this row gives the section’s wrong ordering a precise example. | terra: One class asks only for a worldly share and consequently has no share in the hereafter, making exclusive desire for the first stage determine the loss of the later one.
- (2:201) [luna: contrast (missing-ayat turn); terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] وَمِنْهُم مَّن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا حَسَنَةًۭ وَفِى ٱلْءَاخِرَةِ حَسَنَةًۭ وَقِنَا عَذَابَ ٱلنَّارِ
  Unverified discovery rationale: luna: In contrast to the world-only request of 2:200, this ayah asks for good in this world and the Hereafter and protection from the Fire, showing a rightly ordered desire that does not discard either life. | terra: The next class asks for good in both the world and the hereafter, establishing a boundary against reading the section's comparison as abandonment of every worldly good.
- (2:212) [terra: strong (missing-ayat turn); basis: contrast+scene+theme] زُيِّنَ لِلَّذِينَ كَفَرُوا۟ ٱلْحَيَوٰةُ ٱلدُّنْيَا وَيَسْخَرُونَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ ۘ وَٱلَّذِينَ ٱتَّقَوْا۟ فَوْقَهُمْ يَوْمَ ٱلْقِيَٰمَةِ ۗ وَٱللَّهُ يَرْزُقُ مَن يَشَآءُ بِغَيْرِ حِسَابٍۢ
  Unverified discovery rationale: terra: The near life is adorned for rejecters who mock believers, but the God-conscious will be above them on resurrection day; the final height reverses the visible worldly rank.
- (2:238) [terra: strong; basis: root+scene] حَٰفِظُوا۟ عَلَى ٱلصَّلَوَٰتِ وَٱلصَّلَوٰةِ ٱلْوُسْطَىٰ وَقُومُوا۟ لِلَّهِ قَٰنِتِينَ
  Unverified discovery rationale: terra: Guard all prayers and ٱلصَّلَوٰةِ ٱلْوُسْطَىٰ; one prayer is explicitly located within an ordered series, echoing the positional sense developed for the prayer root.
- (3:14) [luna: contrast; terra: strong; basis: contrast+scene+theme] زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ مِنَ ٱلنِّسَآءِ وَٱلْبَنِينَ وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ مِنَ ٱلذَّهَبِ وَٱلْفِضَّةِ وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ ۗ ذَٰلِكَ مَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱللَّهُ عِندَهُۥ حُسْنُ ٱلْمَـَٔابِ
  Unverified discovery rationale: luna: The section’s image uses a horse train to make worldly preference visible; this ayah lists branded horses among the attractions of worldly life, then contrasts that adornment with the better return with God. | terra: Branded horses are among the beautified desires of ٱلْحَيَوٰةِ ٱلدُّنْيَا, while the good return is with God; the horse image itself becomes part of the near-life test.
- (3:114) [luna: strong; basis: contrast+scene+theme] يُؤْمِنُونَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَيَأْمُرُونَ بِٱلْمَعْرُوفِ وَيَنْهَوْنَ عَنِ ٱلْمُنكَرِ وَيُسَٰرِعُونَ فِى ٱلْخَيْرَٰتِ وَأُو۟لَٰٓئِكَ مِنَ ٱلصَّٰلِحِينَ
  Unverified discovery rationale: luna: This ayah likewise says the righteous “hasten in good deeds” (يُسَٰرِعُونَ فِى ٱلْخَيْرَٰتِ); it is another concrete Qur’anic use of speed to reach good rather than favor the immediate life.
- (3:133) [luna: strong; terra: medium; basis: contrast+scene+theme] ۞ وَسَارِعُوٓا۟ إِلَىٰ مَغْفِرَةٍۢ مِّن رَّبِّكُمْ وَجَنَّةٍ عَرْضُهَا ٱلسَّمَٰوَٰتُ وَٱلْأَرْضُ أُعِدَّتْ لِلْمُتَّقِينَ
  Unverified discovery rationale: luna: Like the section’s reordering of what is worth reaching first, this ayah commands, “Race toward forgiveness” (وَسَارِعُوٓا۟ إِلَىٰ مَغْفِرَةٍ) and a Garden from the Lord. | terra: وَسَارِعُوٓا۟ إِلَىٰ مَغْفِرَةٍ directs speed toward forgiveness and the garden, a nonlexical race toward the enduring prize.
- (3:152) [terra: strong; basis: contrast+theme] وَلَقَدْ صَدَقَكُمُ ٱللَّهُ وَعْدَهُۥٓ إِذْ تَحُسُّونَهُم بِإِذْنِهِۦ ۖ حَتَّىٰٓ إِذَا فَشِلْتُمْ وَتَنَٰزَعْتُمْ فِى ٱلْأَمْرِ وَعَصَيْتُم مِّنۢ بَعْدِ مَآ أَرَىٰكُم مَّا تُحِبُّونَ ۚ مِنكُم مَّن يُرِيدُ ٱلدُّنْيَا وَمِنكُم مَّن يُرِيدُ ٱلْءَاخِرَةَ ۚ ثُمَّ صَرَفَكُمْ عَنْهُمْ لِيَبْتَلِيَكُمْ ۖ وَلَقَدْ عَفَا عَنكُمْ ۗ وَٱللَّهُ ذُو فَضْلٍ عَلَى ٱلْمُؤْمِنِينَ
  Unverified discovery rationale: terra: مِنكُم مَّن يُرِيدُ ٱلدُّنْيَا وَمِنكُم مَّن يُرِيدُ ٱلْـَٔاخِرَةَ divides one battle line by the two different goals its members put first.
- (4:77) [luna: contrast (missing-ayat turn); terra: strong; basis: contrast+root+theme] أَلَمْ تَرَ إِلَى ٱلَّذِينَ قِيلَ لَهُمْ كُفُّوٓا۟ أَيْدِيَكُمْ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ فَلَمَّا كُتِبَ عَلَيْهِمُ ٱلْقِتَالُ إِذَا فَرِيقٌۭ مِّنْهُمْ يَخْشَوْنَ ٱلنَّاسَ كَخَشْيَةِ ٱللَّهِ أَوْ أَشَدَّ خَشْيَةًۭ ۚ وَقَالُوا۟ رَبَّنَا لِمَ كَتَبْتَ عَلَيْنَا ٱلْقِتَالَ لَوْلَآ أَخَّرْتَنَآ إِلَىٰٓ أَجَلٍۢ قَرِيبٍۢ ۗ قُلْ مَتَٰعُ ٱلدُّنْيَا قَلِيلٌۭ وَٱلْءَاخِرَةُ خَيْرٌۭ لِّمَنِ ٱتَّقَىٰ وَلَا تُظْلَمُونَ فَتِيلًا
  Unverified discovery rationale: luna: The section says the later life is better and more lasting; this ayah calls the worldly enjoyment little and the Hereafter better for the God-fearing, directly adding duration and value to the comparison. | terra: مَتَـٰعُ ٱلدُّنْيَا قَلِيلٌ وَٱلْـَٔاخِرَةُ خَيْرٌ makes the near stage brief and the later stage better.
- (4:102) [luna: medium; terra: strong (missing-ayat turn); basis: root+scene+theme] وَإِذَا كُنتَ فِيهِمْ فَأَقَمْتَ لَهُمُ ٱلصَّلَوٰةَ فَلْتَقُمْ طَآئِفَةٌۭ مِّنْهُم مَّعَكَ وَلْيَأْخُذُوٓا۟ أَسْلِحَتَهُمْ فَإِذَا سَجَدُوا۟ فَلْيَكُونُوا۟ مِن وَرَآئِكُمْ وَلْتَأْتِ طَآئِفَةٌ أُخْرَىٰ لَمْ يُصَلُّوا۟ فَلْيُصَلُّوا۟ مَعَكَ وَلْيَأْخُذُوا۟ حِذْرَهُمْ وَأَسْلِحَتَهُمْ ۗ وَدَّ ٱلَّذِينَ كَفَرُوا۟ لَوْ تَغْفُلُونَ عَنْ أَسْلِحَتِكُمْ وَأَمْتِعَتِكُمْ فَيَمِيلُونَ عَلَيْكُم مَّيْلَةًۭ وَٰحِدَةًۭ ۚ وَلَا جُنَاحَ عَلَيْكُمْ إِن كَانَ بِكُمْ أَذًۭى مِّن مَّطَرٍ أَوْ كُنتُم مَّرْضَىٰٓ أَن تَضَعُوٓا۟ أَسْلِحَتَكُمْ ۖ وَخُذُوا۟ حِذْرَكُمْ ۗ إِنَّ ٱللَّهَ أَعَدَّ لِلْكَٰفِرِينَ عَذَابًۭا مُّهِينًۭا
  Unverified discovery rationale: luna: The section says the dictionary sense of ص ل و can name the second horse following the first but keeps the Qur’anic prayer sense; here prayer groups alternate, and the group that has prostrated is put behind the one still serving, uniting prayer with succession. | terra: The danger-prayer instructions place one troop in prayer with the Prophet, then bring forward another troop that has not yet prayed; صَلَاة is enacted as ordered companies following their leader.
- (4:134) [luna: contrast (missing-ayat turn); terra: strong (missing-ayat turn); basis: contrast+theme] مَّن كَانَ يُرِيدُ ثَوَابَ ٱلدُّنْيَا فَعِندَ ٱللَّهِ ثَوَابُ ٱلدُّنْيَا وَٱلْءَاخِرَةِ ۚ وَكَانَ ٱللَّهُ سَمِيعًۢا بَصِيرًۭا
  Unverified discovery rationale: luna: The section warns against preferring the nearer life over what lasts; this ayah supplies a boundary by saying that with God is the reward of this world and the Hereafter, so the choice of reward is not limited to the first life. | terra: Whoever wants worldly reward is reminded that both worldly and later reward are with God, relocating control of both stages from the chooser to their Lord.
- (5:48) [luna: strong; terra: strong; basis: root+scene+theme] وَأَنزَلْنَآ إِلَيْكَ ٱلْكِتَٰبَ بِٱلْحَقِّ مُصَدِّقًۭا لِّمَا بَيْنَ يَدَيْهِ مِنَ ٱلْكِتَٰبِ وَمُهَيْمِنًا عَلَيْهِ ۖ فَٱحْكُم بَيْنَهُم بِمَآ أَنزَلَ ٱللَّهُ ۖ وَلَا تَتَّبِعْ أَهْوَآءَهُمْ عَمَّا جَآءَكَ مِنَ ٱلْحَقِّ ۚ لِكُلٍّۢ جَعَلْنَا مِنكُمْ شِرْعَةًۭ وَمِنْهَاجًۭا ۚ وَلَوْ شَآءَ ٱللَّهُ لَجَعَلَكُمْ أُمَّةًۭ وَٰحِدَةًۭ وَلَٰكِن لِّيَبْلُوَكُمْ فِى مَآ ءَاتَىٰكُمْ ۖ فَٱسْتَبِقُوا۟ ٱلْخَيْرَٰتِ ۚ إِلَى ٱللَّهِ مَرْجِعُكُمْ جَمِيعًۭا فَيُنَبِّئُكُم بِمَا كُنتُمْ فِيهِ تَخْتَلِفُونَ
  Unverified discovery rationale: luna: This ayah repeats فَٱسْتَبِقُوا۟ ٱلْخَيْرَٰتِ, a race toward good, then says all return to God; it joins the section’s race order to its later destination. | terra: فَٱسْتَبِقُوا۟ ٱلْخَيْرَٰتِ again turns human difference into a race whose result is finally disclosed by God.
