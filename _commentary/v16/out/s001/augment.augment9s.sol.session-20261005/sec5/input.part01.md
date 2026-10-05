Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 5 of 14 ("Tamamlanan nimet ve başa kakılan nimet"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 5 (prose paragraphs numbered) =====
[¶28] Bir iyilik bir el ile uzatılır: {ar:النعمة اليد والصنيعة والمنة وما أنعم به عليك, tr:en-ni'metü'l-yedü ve's-sanî'atü ve'l-minnetü ve mâ en'ame bihî aleyk, gloss:nimet el, iyilik, lütuf ve sana verilen şeydir, source:"ن ع م,B001"}. Nimet vermek, iyiliği başkasına ulaştırmaktır: {ar:النعمة الحالة الحسنة والإنعام إيصال الإحسان إلى الغير, tr:en-ni'metü'l-hâletü'l-hasene ve'l-in'âmü îsâlü'l-ihsâni ile'l-gayr, gloss:nimet güzel haldir; in'âm, iyiliği başkasına ulaştırmaktır, source:"ن ع م,B001"}. Aynı fiil bir işi sonuna kadar ve fazlasıyla yapmayı da anlatır: {ar:أنعم أفضل وزاد, tr:en'ame efdale ve zâd, gloss:en'ame, fazlasını verdi ve artırdı demektir, source:"ن ع م,B010"}. Bu kullanım günlük işlerde de görülür: {ar:دققت دواء فأنعمت دقه أي بالغت وزدت, tr:dekaktü devâen fe-en'amtü dakkahû, gloss:ilacı dövdüm ve iyice, sonuna kadar dövdüm, source:"ن ع م,B010"}. İkinci ayetteki "Rab" kelimesi iyiliği tamamlamayı anlatır: {ar:رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها, tr:rabbe'r-racülü'n-ni'mete yerubbühâ, gloss:adam nimeti tamamladı, source:"ر ب ب,B002"}, {ar:رب فلان الصنيعة إذا أتمها وأصلحها, tr:rabbe fülânüni's-sanî'ate, gloss:falanca iyiliğini tamamlayıp düzene koydu, source:"ر ب ب,B002"}. Nimetin kendisi de aynı köktendir: {ar:الربى: النعمة والإحسان, tr:er-rubbâ: en-ni'metü ve'l-ihsân, gloss:rubbâ nimet ve iyiliktir, source:"ر ب ب,B016"}.

[¶29] Alan kişinin cevabı hamddır. Hamd şükürden daha geniştir: {ar:الحمد أعم من الشكر, tr:el-hamdü eammü mine'ş-şükr, gloss:hamd şükürden daha kapsamlıdır, source:"ح م د,B001"}. Hamdın bir biçimi, verenin iyiliklerini başkalarının yanında saymaktır: {ar:أحمد إليك الله أي معك, tr:ahmedü ileyke'llâh, gloss:seninle birlikte Allah'a hamd ederim, source:"ح م د,B006"}, {ar:أشكر إليك أياديه ونعمه, tr:eşkürü ileyke eyâdîhi ve niamah, gloss:onun iyiliklerini ve nimetlerini sana anlatarak şükrederim, source:"ح م د,B006"}. Aynı kökte bunun tersi de vardır, iyiliği alanın başına kakmak: {ar:فلان يتحمد علي أي يمن, tr:fülânün yetehammedü aleyye, gloss:falanca bana iyiliğini başıma kakıyor, source:"ح م د,B005"}. Kendine harcadığını başkalarının yanında öne sürmek de böyle anılır: {ar:من أنفق ماله على نفسه فلا يتحمد به إلى الناس, tr:men enfeka mâlehû alâ nefsihî fe-lâ yetehammedü bihî ile'n-nâs, gloss:malını kendine harcayan, bunu insanlara karşı iyilik diye öne sürmesin, source:"ح م د,B005"}.

[¶30] Sure bu sahneyi dikkat çekici bir sırayla kurar. Birinci ayetteki merhamet iyiliğin kaynağıdır, çünkü rahmet iyilik etmeyi gerektiren bir inceliktir. İkinci ayet cevabı en başa koyar: {ar:ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:el-hamdü lillâhi rabbi'l-âlemîn, gloss:hamd âlemlerin Rabbi Allah'adır, source:1:2}. Hamd edilen burada iyiliği tamamlayan Rab olarak anılır. Nimetin kendisi ise ancak yedinci ayette adıyla geçer: {ar:أَنْعَمْتَ عَلَيْهِمْ, tr:en'amte aleyhim, gloss:onlara nimet verdin, source:1:7}. Teşekkür, sayılan iyilikten önce gelir. Düz bir meal "hamd" ile "nimet" arasındaki bu bağı göstermez. Görüntü ise iyiliğin elden ele geçişini gösterir: Bir el uzanır, iyilik sonuna kadar götürülür, alan da verenin iyiliklerini başkalarının yanında sayar. Yedinci ayetteki nimet ayrıca bir yol nimetidir. Kendilerine nimet verilenler, yolları istenen kişilerdir. Nimetin tamamlanması da o yolda yürümekle olur.

[¶31] Kur'an nimetin tamamlanmasını ile yola iletmeyi birçok yerde birlikte anar. Peygambere açık bir fetih verildiği bildirilir: {ar:إِنَّا فَتَحْنَا لَكَ فَتْحًۭا مُّبِينًۭا, tr:innâ fetahnâ leke fethan mübînâ, gloss:biz sana apaçık bir fetih verdik, source:48:1}. Bunun ardından şu gelir: {ar:وَيُتِمَّ نِعْمَتَهُۥ عَلَيْكَ وَيَهْدِيَكَ صِرَٰطًۭا مُّسْتَقِيمًۭا, tr:ve yütimme ni'metehû aleyke ve yehdiyeke sırâtan müstakîmâ, gloss:sana nimetini tamamlasın ve seni dosdoğru bir yola iletsin, source:48:2}. Burada Fâtiha'nın yedinci ve altıncı ayetleri tek cümlede birleşir. Kıblenin Mescid-i Haram'a çevrilmesi emredildiğinde de aynı ikili görülür: {ar:وَلِأُتِمَّ نِعْمَتِى عَلَيْكُمْ وَلَعَلَّكُمْ تَهْتَدُونَ, tr:ve li-ütimme ni'metî aleyküm ve lealleküm tehtedûn, gloss:size nimetimi tamamlayayım ve yolu bulasınız diye, source:2:150}. Bu ayette tamamlanan nimet yüzü bir eve döndürmekle birliktedir. Dinin kemale ermesi de aynı fiille söylenir: {ar:ٱلْيَوْمَ أَكْمَلْتُ لَكُمْ دِينَكُمْ وَأَتْمَمْتُ عَلَيْكُمْ نِعْمَتِى, tr:el-yevme ekmeltü leküm dîneküm ve etmemtü aleyküm ni'metî, gloss:bugün dininizi kemale erdirdim ve size nimetimi tamamladım, source:5:3}. Yakup oğlu Yusuf'a nimetin bir soy boyunca tamamlandığını anlatır: {ar:وَيُتِمُّ نِعْمَتَهُۥ عَلَيْكَ وَعَلَىٰٓ ءَالِ يَعْقُوبَ كَمَآ أَتَمَّهَا عَلَىٰٓ أَبَوَيْكَ مِن قَبْلُ, tr:ve yütimmü ni'metehû aleyke ve alâ âli Ya'kûbe kemâ etemmehâ alâ ebeveyke min kabl, gloss:daha önce iki atana tamamladığı gibi sana ve Yakup ailesine nimetini tamamlayacak, source:12:6}. Bu ayet, nimetin yedinci ayetteki "onlar" gibi bir topluluğa ait olduğunu gösterir. İbrahim'in cevabı da aynı sıradadır: {ar:شَاكِرًۭا لِّأَنْعُمِهِ ۚ ٱجْتَبَىٰهُ وَهَدَىٰهُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:şâkiran li-en'umih, ictebâhü ve hedâhü ilâ sırâtın müstakîm, gloss:onun nimetlerine şükrederdi; onu seçti ve dosdoğru bir yola iletti, source:16:121}. Nimeti başkalarının yanında anlatmak, Peygambere emredilen bir şeydir: {ar:وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ, tr:ve emmâ bi-ni'meti rabbike fe-haddis, gloss:Rabbinin nimetini ise anlat, source:93:11}. Kulluk da nimete verilen cevap olarak gösterilir: {ar:فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ, tr:fe'l-ya'büdû rabbe hâze'l-beyt, gloss:bu evin Rabbine kulluk etsinler, source:106:3}, {ar:ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ, tr:ellezî at'amehüm min cû'in ve âmenehüm min havf, gloss:onları açlıktan doyuran ve korkudan emin kılan, source:106:4}. Yolun sonunda hamd yeniden duyulur. Cennettekiler şöyle der: {ar:ٱلْحَمْدُ لِلَّهِ ٱلَّذِى هَدَىٰنَا لِهَٰذَا, tr:el-hamdü lillâhi'llezî hedânâ li-hâzâ, gloss:bizi buna ileten Allah'a hamd olsun, source:7:43}. Onların son sözü surenin ikinci ayetidir: {ar:وَءَاخِرُ دَعْوَىٰهُمْ أَنِ ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve âhiru da'vâhüm eni'l-hamdü lillâhi rabbi'l-âlemîn, gloss:dualarının sonu "hamd âlemlerin Rabbi Allah'adır" sözüdür, source:10:10}. Fâtiha'nın başta söylediği söz, yolun sonunda yeniden söylenir. Başa kakılan nimetin sahnesi ise Firavun'un sarayındadır. Firavun büyüttüğünü iddia eder, Musa da {ar:وَتِلْكَ نِعْمَةٌۭ تَمُنُّهَا عَلَىَّ, tr:ve tilke ni'metün temünnühâ aleyye, gloss:başıma kaktığın o nimet, source:26:22} diye cevap verir. Bu, "yetehammedü aleyye" sözünün sahnesidir.

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

===== passages from the discovery list (322) =====
## strong (243)

- (2:22) [luna: strong; basis: scene+theme] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ فِرَٰشًۭا وَٱلسَّمَآءَ بِنَآءًۭ وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ ۖ فَلَا تَجْعَلُوا۟ لِلَّهِ أَندَادًۭا وَأَنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: luna: Rain and crops are provided as sustenance, and people are told not to set up rivals to God; the ayah makes the giver behind received good explicit.
- (2:40) [luna: strong; terra: strong; basis: root+speaker+theme] يَٰبَنِىٓ إِسْرَٰٓءِيلَ ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ وَأَوْفُوا۟ بِعَهْدِىٓ أُوفِ بِعَهْدِكُمْ وَإِيَّٰىَ فَٱرْهَبُونِ
  Unverified discovery rationale: luna: The command to Israel to remember the favor bestowed on them directly matches the section's account of recounting a giver's good to its recipients. | terra: Israel is told to remember God's favor and fulfill His covenant, making recollection of a benefit answerable in conduct.
- (2:47) [luna: strong; basis: root+speaker+theme] يَٰبَنِىٓ إِسْرَٰٓءِيلَ ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ وَأَنِّى فَضَّلْتُكُمْ عَلَى ٱلْعَٰلَمِينَ
  Unverified discovery rationale: luna: This repeated command to remember God's favor to Israel addresses the receiving people as a group, matching the section's plural “those You favored.”
- (2:57) [luna: strong; terra: strong; basis: scene+theme] وَظَلَّلْنَا عَلَيْكُمُ ٱلْغَمَامَ وَأَنزَلْنَا عَلَيْكُمُ ٱلْمَنَّ وَٱلسَّلْوَىٰ ۖ كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ ۖ وَمَا ظَلَمُونَا وَلَٰكِن كَانُوٓا۟ أَنفُسَهُمْ يَظْلِمُونَ
  Unverified discovery rationale: luna: The section pictures a good delivered from a giver to recipients; here cloud shade, manna, and quail are provided to Israel, with the command to eat good things. | terra: Cloud shade, manna, and quails are given as good things for Israel to eat; the scene gives food directly to a people who must receive it rightly.
- (2:122) [luna: strong; basis: root+speaker+theme] يَٰبَنِىٓ إِسْرَٰٓءِيلَ ٱذْكُرُوا۟ نِعْمَتِىَ ٱلَّتِىٓ أَنْعَمْتُ عَلَيْكُمْ وَأَنِّى فَضَّلْتُكُمْ عَلَى ٱلْعَٰلَمِينَ
  Unverified discovery rationale: luna: This ayah again tells Israel to remember the favor bestowed on them; its direct act of communal recollection matches the section's recounting of good.
- (2:144) [terra: strong; basis: neighbour+scene] قَدْ نَرَىٰ تَقَلُّبَ وَجْهِكَ فِى ٱلسَّمَآءِ ۖ فَلَنُوَلِّيَنَّكَ قِبْلَةًۭ تَرْضَىٰهَا ۚ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ ۗ وَإِنَّ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ لَيَعْلَمُونَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّهِمْ ۗ وَمَا ٱللَّهُ بِغَٰفِلٍ عَمَّا يَعْمَلُونَ
  Unverified discovery rationale: terra: The command to turn toward the Sacred Mosque supplies the changed direction whose completion of favor and guidance are announced in 2:150.
- (2:150) [luna: strong; terra: strong; basis: root+scene+theme] [cited in ¶31] وَمِنْ حَيْثُ خَرَجْتَ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَحَيْثُ مَا كُنتُمْ فَوَلُّوا۟ وُجُوهَكُمْ شَطْرَهُۥ لِئَلَّا يَكُونَ لِلنَّاسِ عَلَيْكُمْ حُجَّةٌ إِلَّا ٱلَّذِينَ ظَلَمُوا۟ مِنْهُمْ فَلَا تَخْشَوْهُمْ وَٱخْشَوْنِى وَلِأُتِمَّ نِعْمَتِى عَلَيْكُمْ وَلَعَلَّكُمْ تَهْتَدُونَ
  Unverified discovery rationale: luna: The section's wording “complete the favor” and its path image meet in لِأُتِمَّ نِعْمَتِي and لَعَلَّكُمْ تَهْتَدُونَ; the immediate scene is facing the Sacred Mosque. | terra: The section explicitly pairs this qiblah verse with 48:2: completing God's favor upon the community is stated together with their being guided.
- (2:172) [luna: strong; terra: strong; basis: scene+speaker+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُلُوا۟ مِن طَيِّبَٰتِ مَا رَزَقْنَٰكُمْ وَٱشْكُرُوا۟ لِلَّهِ إِن كُنتُمْ إِيَّاهُ تَعْبُدُونَ
  Unverified discovery rationale: luna: This command to eat good provision and thank God for it makes explicit the recipient's response to a provider, as the section links favor and hamd. | terra: Those given good provisions are commanded to eat and give thanks to God, a direct provision-to-response scene.
- (2:177) [luna: strong (missing-ayat turn); basis: scene+theme] ۞ لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَلَٰكِنَّ ٱلْبِرَّ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْءَاخِرِ وَٱلْمَلَٰٓئِكَةِ وَٱلْكِتَٰبِ وَٱلنَّبِيِّۦنَ وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ وَٱبْنَ ٱلسَّبِيلِ وَٱلسَّآئِلِينَ وَفِى ٱلرِّقَابِ وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ وَٱلْمُوفُونَ بِعَهْدِهِمْ إِذَا عَٰهَدُوا۟ ۖ وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ وَحِينَ ٱلْبَأْسِ ۗ أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ
  Unverified discovery rationale: luna: Righteousness includes giving beloved wealth to relatives, orphans, the needy, and travelers; the ayah makes beneficence to recipients part of the path.
- (2:185) [luna: strong; terra: strong; basis: scene+speaker+theme] شَهْرُ رَمَضَانَ ٱلَّذِىٓ أُنزِلَ فِيهِ ٱلْقُرْءَانُ هُدًۭى لِّلنَّاسِ وَبَيِّنَٰتٍۢ مِّنَ ٱلْهُدَىٰ وَٱلْفُرْقَانِ ۚ فَمَن شَهِدَ مِنكُمُ ٱلشَّهْرَ فَلْيَصُمْهُ ۖ وَمَن كَانَ مَرِيضًا أَوْ عَلَىٰ سَفَرٍۢ فَعِدَّةٌۭ مِّنْ أَيَّامٍ أُخَرَ ۗ يُرِيدُ ٱللَّهُ بِكُمُ ٱلْيُسْرَ وَلَا يُرِيدُ بِكُمُ ٱلْعُسْرَ وَلِتُكْمِلُوا۟ ٱلْعِدَّةَ وَلِتُكَبِّرُوا۟ ٱللَّهَ عَلَىٰ مَا هَدَىٰكُمْ وَلَعَلَّكُمْ تَشْكُرُونَ
  Unverified discovery rationale: luna: The section joins a completed gift, guidance, and a grateful response; this fasting passage says to complete the number, glorify God for guiding you, and be grateful. | terra: Completing the counted days is joined to magnifying God for His guidance and being grateful, a ritual-scale parallel to completed favor and praise.
- (2:231) [luna: strong; terra: strong; basis: root+theme] وَإِذَا طَلَّقْتُمُ ٱلنِّسَآءَ فَبَلَغْنَ أَجَلَهُنَّ فَأَمْسِكُوهُنَّ بِمَعْرُوفٍ أَوْ سَرِّحُوهُنَّ بِمَعْرُوفٍۢ ۚ وَلَا تُمْسِكُوهُنَّ ضِرَارًۭا لِّتَعْتَدُوا۟ ۚ وَمَن يَفْعَلْ ذَٰلِكَ فَقَدْ ظَلَمَ نَفْسَهُۥ ۚ وَلَا تَتَّخِذُوٓا۟ ءَايَٰتِ ٱللَّهِ هُزُوًۭا ۚ وَٱذْكُرُوا۟ نِعْمَتَ ٱللَّهِ عَلَيْكُمْ وَمَآ أَنزَلَ عَلَيْكُم مِّنَ ٱلْكِتَٰبِ وَٱلْحِكْمَةِ يَعِظُكُم بِهِۦ ۚ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ بِكُلِّ شَىْءٍ عَلِيمٌۭ
  Unverified discovery rationale: luna: The section presents the giver's good as something remembered; this ayah explicitly tells people to remember God's favor and the Book and wisdom sent down to them. | terra: Believers are told to remember God's favor and the Book and wisdom sent down to admonish them, treating teaching itself as received good.
- (2:243) [luna: strong; terra: strong (missing-ayat turn); basis: contrast+scene+theme] ۞ أَلَمْ تَرَ إِلَى ٱلَّذِينَ خَرَجُوا۟ مِن دِيَٰرِهِمْ وَهُمْ أُلُوفٌ حَذَرَ ٱلْمَوْتِ فَقَالَ لَهُمُ ٱللَّهُ مُوتُوا۟ ثُمَّ أَحْيَٰهُمْ ۚ إِنَّ ٱللَّهَ لَذُو فَضْلٍ عَلَى ٱلنَّاسِ وَلَٰكِنَّ أَكْثَرَ ٱلنَّاسِ لَا يَشْكُرُونَ
  Unverified discovery rationale: luna: After God restored life to a people who had fled death, this ayah says God has favor over people but most are ungrateful; it joins a delivered good to its denied response. | terra: After God causes the fleeing multitude to die and restores them to life, the ayah calls Him full of bounty toward people while most do not give thanks; revived life is a concrete favor with a failed response.
- (2:261) [luna: strong (missing-ayat turn); basis: scene+theme] مَّثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ فِى سَبِيلِ ٱللَّهِ كَمَثَلِ حَبَّةٍ أَنۢبَتَتْ سَبْعَ سَنَابِلَ فِى كُلِّ سُنۢبُلَةٍۢ مِّا۟ئَةُ حَبَّةٍۢ ۗ وَٱللَّهُ يُضَٰعِفُ لِمَن يَشَآءُ ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌ
  Unverified discovery rationale: luna: The parable of a grain yielding seven ears, each with many grains, depicts charity multiplied by God; it connects the section's giving of good with increase beyond the initial gift.
- (2:262) [luna: strong; terra: contrast; basis: contrast+root+scene+theme] ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ فِى سَبِيلِ ٱللَّهِ ثُمَّ لَا يُتْبِعُونَ مَآ أَنفَقُوا۟ مَنًّۭا وَلَآ أَذًۭى ۙ لَّهُمْ أَجْرُهُمْ عِندَ رَبِّهِمْ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
  Unverified discovery rationale: luna: The section contrasts recounting a giver's good with reproaching its recipient; this ayah says charity is emptied by مَنًّا or injury, and promises reward without fear to those who refrain. | terra: Those who give wealth and do not follow it with mann or injury keep their reward. It is the Qur'anic boundary against the section's head-claimed favor.
- (2:263) [luna: strong (missing-ayat turn); terra: contrast; basis: contrast+neighbour+root+scene] ۞ قَوْلٌۭ مَّعْرُوفٌۭ وَمَغْفِرَةٌ خَيْرٌۭ مِّن صَدَقَةٍۢ يَتْبَعُهَآ أَذًۭى ۗ وَٱللَّهُ غَنِىٌّ حَلِيمٌۭ
