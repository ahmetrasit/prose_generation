Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 9 of 18 ("Ne ölü ne diri: kalan hayat"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 9 (prose paragraphs numbered) =====
[¶36] On üçüncü ayet ateşe gireni şöyle anlatır: {ar:ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:ŝumme lâ yemûtu fîhâ ve lâ yahyâ, gloss:sonra orada ne ölür ne yaşar, source:87:13}. Arapça iki uç arasındaki halleri ayrı ayrı adlandırır ve ayetin olumsuzladığı şeyi bu adlar belirginleştirir. Ölüm gücün bir şeyden çekilmesidir: {ar:أصل صحيح يدل على ذهاب القوة من الشيء, tr:aslun sahîhun yedullu alâ ẕehâbi'l-kuvveti mine'ş-şey', gloss:bir şeyden gücün gitmesini gösteren köktür, source:"م و ت,B001"}. Ayılınan bir baygınlık da bu kökle anılır: {ar:الموتة الذي يصرع من الجنون أو غيره ثم يفيق, tr:el-mûte elleẕî yusrau mine'l-cunûni ev ğayrihî ŝumme yufîk, gloss:mûte delilikten ya da başka bir şeyden yere yıkılıp sonra ayılmaktır, source:"م و ت,B009"}. Uyku da öyle: {ar:مات الرجل وهمد وهوم إذا نام, tr:mâte'r-raculu ve hemede ve hevveme iẕâ nâm, gloss:adam uyuduğunda mâte ve hemede denir, source:"م و ت,B012"}. Hayat ise fayda ve iyiliktir: {ar:ليس بفلان حياة أي ليس عنده نفع ولا خير, tr:leyse bi-fulânin hayâtun ey leyse indehû nef'un ve lâ hayr, gloss:falancada hayat yok yani onda ne fayda ne iyilik var, source:"ح ي ي,B013"}. Bu ifade dokuzuncu ayetteki "fayda" ve on yedinci ayetteki "hayırlı" kelimelerinin köklerini içerir. Diri bırakmak, sağ tutmak demektir: {ar:ويستحيون نساءكم أي يستبقونهن, tr:ve yestahyûne nisâekum ey yestebkûnehunn, gloss:kadınlarınızı diri bırakıyorlardı yani onları sağ tutuyorlardı, source:"ح ي ي,B006"}. Bu tanım "yaşamak" kökünü "kalmak" köküyle açıklar. Hakiki hayat da kalıcılıkla tanımlanır: {ar:الحيوان مقر الحياة وما له الحاسة وما له البقاء الأبدي, tr:el-hayevân makarru'l-hayâti ve mâ lehu'l-hâssetu ve mâ lehu'l-bekâu'l-ebediyy, gloss:hayevân hayatın yeri ve duyusu olan ve sonsuz kalıcılığı bulunandır, source:"ح ي ي,B003"}. Hayevân'ın, kayıtlı ikinci bir köke bağlanan bir anlamı da vardır: {ar:والحيوان ماء في الجنة لا يصيب شيئا إلا حي بإذن الله, tr:ve'l-hayevân mâun fi'l-cenneti lâ yusîbu şey'en illâ hayye bi-iẕnillâh, gloss:hayevân cennette bir sudur; dokunduğu her şey Allah'ın izniyle dirilir, source:"ح ي و,B003"}. Kalmak da yaşamak demektir: {ar:بقي الرجل زمانا طويلا أي عاش, tr:bakıye'r-raculu zemânen tavîlen ey âşe, gloss:adam uzun zaman kaldı yani yaşadı, source:"ب ق ي,B001"}. Ve yok olmaktan kurtarmaktır: {ar:العرب تقول للعدو إذا غلب البقية أي أبقوا علينا ولا تستأصلونا, tr:el-arabu tekûlu li'l-aduvvi iẕâ ğalebe el-bakıyye ey ebkû aleynâ ve lâ testa'sılûnâ, gloss:Araplar galip gelen düşmana bakıyye der yani bizi bırakın ve kökümüzü kazımayın, source:"ب ق ي,B003"}. Dünya ise yakın olduğu için bu adı alır: {ar:سميت الدنيا لدنوها, tr:summiyeti'd-dunyâ li-dunuvvihâ, gloss:dünyaya yakınlığından dolayı bu ad verilmiştir, source:"د ن و,B002"}.

[¶37] Bu adlar on üçüncü ayetteki olumsuzlamanın neyi dışarıda bıraktığını gösterir. Ateştekinin gücü tümüyle çekilmez. Ayılınan bir baygınlığı ya da bir uykusu yoktur. Ama hayatın tanımı olan fayda ve iyilik de onda yoktur. On altıncı ve on yedinci ayet ise hayat kelimesini iki yere böler: yakın olduğu için dünya diye anılan hayat ve kalıcı olan ahiret. Düz bir anlatım on üçüncü ayeti yalnızca bir azap tasviri olarak okur. Kök ailesi ise onu surenin sonundaki seçimin bir ucu olarak gösterir. Yakın hayatı kalıcı olana tercih edenin vardığı yer, ne hayatın ne de ölümün olduğu bir yerdir.

[¶38] Kur'an bu cümleyi kelimesi kelimesine başka bir sahnede, Musa'nın karşısındaki sihirbazların ağzından verir. Sihirbazlar secdeye kapanıp Harun'un ve Musa'nın Rabbine iman ettiklerini söyleyince Firavun onları el ve ayaklarını çaprazlama kesmekle tehdit eder ve şöyle der: {ar:وَلَتَعْلَمُنَّ أَيُّنَآ أَشَدُّ عَذَابًۭا وَأَبْقَىٰ, tr:ve le-ta'lemunne eyyunâ eşeddu azâben ve ebkâ, gloss:hangimizin azabının daha çetin ve daha kalıcı olduğunu bileceksiniz, source:20:71}. Firavun on yedinci ayetin "daha kalıcı" kelimesini kendi azabı için kullanır. Sihirbazlar ise ahiretin iki ucunu anlatır: {ar:إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:innehû men ye'ti rabbehû mucrimen fe-inne lehû cehenneme lâ yemûtu fîhâ ve lâ yahyâ, gloss:kim Rabbine suçlu olarak gelirse ona cehennem vardır; orada ne ölür ne yaşar, source:20:74}. Ötekiler için de bunun karşılığını söylerler: {ar:وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ, tr:ve ẕâlike cezâu men tezekkâ, gloss:bu arınanın karşılığıdır, source:20:76}. Bu birkaç ayette surenin on üçüncü ve on dördüncü ayetleri yan yana gelir. Başka bir yerde inatçı zorba için {ar:وَيَأْتِيهِ ٱلْمَوْتُ مِن كُلِّ مَكَانٍۢ وَمَا هُوَ بِمَيِّتٍۢ, tr:ve ye'tîhi'l-mevtu min kulli mekânin ve mâ huve bi-meyyit, gloss:ölüm ona her yerden gelir ama o ölmez, source:14:17} denir. Bir başka yerde inkâr edenler için {ar:لَا يُقْضَىٰ عَلَيْهِمْ فَيَمُوتُوا۟, tr:lâ yukdâ aleyhim fe-yemûtû, gloss:haklarında ölmeleri için hüküm verilmez, source:35:36} denir. Ateştekiler bekçiye seslenip Rablerinin işlerini bitirmesini isterler, cevap ise şudur: {ar:إِنَّكُم مَّٰكِثُونَ, tr:innekum mâkiŝûn, gloss:siz burada kalacaksınız, source:43:77}. Bu "kalmak" fiili, selin benzetmesinde faydalı suyun yerde kalmasını anlatan fiildir. Aynı fiil iki ayrı yerde iki ayrı türden kalıcılığı anlatır. Hayatın gerçeği için ise {ar:وَإِنَّ ٱلدَّارَ ٱلْءَاخِرَةَ لَهِىَ ٱلْحَيَوَانُ, tr:ve inne'd-dâre'l-âhirete le-hiye'l-hayevân, gloss:ahiret yurdu ise asıl hayatın kendisidir, source:29:64} denir. Gerçek hayatı kaçıran kişi o gün şöyle der: {ar:يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى, tr:yekûlu yâ leytenî kaddemtu li-hayâtî, gloss:keşke hayatım için önceden bir şey gönderseydim der, source:89:24}. Sahte bir kalıcılık da teklif edilir. Şeytan Adem'e {ar:هَلْ أَدُلُّكَ عَلَىٰ شَجَرَةِ ٱلْخُلْدِ وَمُلْكٍۢ لَّا يَبْلَىٰ, tr:hel edulluke alâ şeceratı'l-huldi ve mulkin lâ yeblâ, gloss:sana ölümsüzlük ağacını ve eskimeyen bir mülkü göstereyim mi, source:20:120} der. İbrahim ise ölümü ve hayatı Rabbine bağlar: {ar:وَٱلَّذِى يُمِيتُنِى ثُمَّ يُحْيِينِ, tr:velleẕî yumîtunî ŝumme yuhyîn, gloss:beni öldürecek sonra diriltecek olan O'dur, source:26:81}.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (246) =====
## strong (145)

- (2:28) [luna: medium (missing-ayat turn); terra: strong; basis: contrast+root+scene+theme] كَيْفَ تَكْفُرُونَ بِٱللَّهِ وَكُنتُمْ أَمْوَٰتًۭا فَأَحْيَٰكُمْ ۖ ثُمَّ يُمِيتُكُمْ ثُمَّ يُحْيِيكُمْ ثُمَّ إِلَيْهِ تُرْجَعُونَ
  Unverified discovery rationale: luna: The section's M-W-T and H-Y-Y roots name death and life as distinct endpoints; this verse recounts being dead, then given life, then dying and being raised again, a concrete sequence unlike the condemned state that reaches neither endpoint. | terra: Human beings were dead, were given life, will die, and will be revived, laying out the divinely ordered endpoints from which the Fire's inmate is suspended.
- (2:49) [luna: medium; terra: strong; basis: root+scene] وَإِذْ نَجَّيْنَٰكُم مِّنْ ءَالِ فِرْعَوْنَ يَسُومُونَكُمْ سُوٓءَ ٱلْعَذَابِ يُذَبِّحُونَ أَبْنَآءَكُمْ وَيَسْتَحْيُونَ نِسَآءَكُمْ ۚ وَفِى ذَٰلِكُم بَلَآءٌۭ مِّن رَّبِّكُمْ عَظِيمٌۭ
  Unverified discovery rationale: luna: The section's H-Y-Y gloss explains Pharaoh's “keeping your women alive” as sparing them; this verse recounts the same selective killing and preservation, giving the dictionary sense its Qur'anic scene. | terra: Pharaoh's people slaughter sons and يَسْتَحْيُونَ women, using life language in the source section's precise sense of sparing and keeping alive.
- (2:86) [luna: strong (missing-ayat turn); terra: strong; basis: contrast+root+scene+theme] أُو۟لَٰٓئِكَ ٱلَّذِينَ ٱشْتَرَوُا۟ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْءَاخِرَةِ ۖ فَلَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنصَرُونَ
  Unverified discovery rationale: luna: The section diagnoses preferring the near life over the afterlife; this verse says some have bought worldly life in exchange for the next and that their punishment will not be lightened, an exact choice-and-consequence parallel. | terra: Those who buy worldly life at the price of the Hereafter receive punishment that is not lightened, joining the wrong exchange to unrelieved torment.
- (2:96) [luna: medium; terra: strong; basis: root+theme] وَلَتَجِدَنَّهُمْ أَحْرَصَ ٱلنَّاسِ عَلَىٰ حَيَوٰةٍۢ وَمِنَ ٱلَّذِينَ أَشْرَكُوا۟ ۚ يَوَدُّ أَحَدُهُمْ لَوْ يُعَمَّرُ أَلْفَ سَنَةٍۢ وَمَا هُوَ بِمُزَحْزِحِهِۦ مِنَ ٱلْعَذَابِ أَن يُعَمَّرَ ۗ وَٱللَّهُ بَصِيرٌۢ بِمَا يَعْمَلُونَ
  Unverified discovery rationale: luna: The section's B-Q-Y note equates a long remaining time with living; this verse says some wish for a thousand years of life, yet such length would not remove them from punishment, distinguishing duration from true enduring life. | terra: A thousand years of life would not move the covetous person away from punishment, proving that mere duration is not the beneficial, lasting life of the section.
- (2:154) [luna: strong; terra: contrast; basis: contrast+root+scene+theme] وَلَا تَقُولُوا۟ لِمَن يُقْتَلُ فِى سَبِيلِ ٱللَّهِ أَمْوَٰتٌۢ ۚ بَلْ أَحْيَآءٌۭ وَلَٰكِن لَّا تَشْعُرُونَ
  Unverified discovery rationale: luna: The section distinguishes mere non-death from real, enduring life; here those killed in God's way are explicitly said not to be dead but alive with God, a sharp contrary state. | terra: Those killed in God's way must not be called dead but alive, distinguishing hidden, beneficial life from biological appearance.
- (2:164) [luna: medium; terra: strong; basis: root+scene+theme] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَٱلْفُلْكِ ٱلَّتِى تَجْرِى فِى ٱلْبَحْرِ بِمَا يَنفَعُ ٱلنَّاسَ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن مَّآءٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ وَتَصْرِيفِ ٱلرِّيَٰحِ وَٱلسَّحَابِ ٱلْمُسَخَّرِ بَيْنَ ٱلسَّمَآءِ وَٱلْأَرْضِ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
  Unverified discovery rationale: luna: The section's H-Y-W dictionary branch describes water reviving what it touches; this verse says rain revives the earth after its death, a natural scene that makes the water/life link visible. | terra: Water revives earth after its death and disperses living creatures, bringing the life root, water, and benefit into one sign.
- (2:167) [terra: strong (missing-ayat turn); basis: root+scene+speaker+theme] وَقَالَ ٱلَّذِينَ ٱتَّبَعُوا۟ لَوْ أَنَّ لَنَا كَرَّةًۭ فَنَتَبَرَّأَ مِنْهُمْ كَمَا تَبَرَّءُوا۟ مِنَّا ۗ كَذَٰلِكَ يُرِيهِمُ ٱللَّهُ أَعْمَٰلَهُمْ حَسَرَٰتٍ عَلَيْهِمْ ۖ وَمَا هُم بِخَٰرِجِينَ مِنَ ٱلنَّارِ
  Unverified discovery rationale: terra: The followers wish for a return to disown their leaders, but they will not emerge from the Fire, another concrete denial of an endpoint to punishment.
- (2:179) [luna: strong; basis: root+theme] وَلَكُمْ فِى ٱلْقِصَاصِ حَيَوٰةٌۭ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ لَعَلَّكُمْ تَتَّقُونَ
  Unverified discovery rationale: luna: The section's H-Y-Y dictionary sense of life as benefit fits “in retribution there is life” (في القصاص حياة): the verse names a social good that preserves life, not just biological duration.
- (2:255) [terra: strong (missing-ayat turn); basis: contrast+root+theme] ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْحَىُّ ٱلْقَيُّومُ ۚ لَا تَأْخُذُهُۥ سِنَةٌۭ وَلَا نَوْمٌۭ ۚ لَّهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ مَن ذَا ٱلَّذِى يَشْفَعُ عِندَهُۥٓ إِلَّا بِإِذْنِهِۦ ۚ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ وَلَا يُحِيطُونَ بِشَىْءٍۢ مِّنْ عِلْمِهِۦٓ إِلَّا بِمَا شَآءَ ۚ وَسِعَ كُرْسِيُّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ ۖ وَلَا يَـُٔودُهُۥ حِفْظُهُمَا ۚ وَهُوَ ٱلْعَلِىُّ ٱلْعَظِيمُ
  Unverified discovery rationale: terra: God is the Living, the Sustainer, whom neither drowsiness nor sleep overtakes; perfect life without sleep sharply contrasts the inmate's denied, restorative sleep and empty nondeath.
- (3:88) [terra: strong (missing-ayat turn); basis: root+scene+theme] خَٰلِدِينَ فِيهَا لَا يُخَفَّفُ عَنْهُمُ ٱلْعَذَابُ وَلَا هُمْ يُنظَرُونَ
  Unverified discovery rationale: terra: The condemned remain under the curse with punishment neither lightened nor delayed, specifying continued existence without relief.
- (3:145) [luna: medium (missing-ayat turn); terra: strong (missing-ayat turn); basis: root+speaker+theme] وَمَا كَانَ لِنَفْسٍ أَن تَمُوتَ إِلَّا بِإِذْنِ ٱللَّهِ كِتَٰبًۭا مُّؤَجَّلًۭا ۗ وَمَن يُرِدْ ثَوَابَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَن يُرِدْ ثَوَابَ ٱلْءَاخِرَةِ نُؤْتِهِۦ مِنْهَا ۚ وَسَنَجْزِى ٱلشَّٰكِرِينَ
  Unverified discovery rationale: luna: The section contrasts worldly life with the afterlife; this verse says one who seeks the reward of this world receives some of it, while one who seeks the reward of the afterlife receives it, making the chosen horizon explicit. | terra: The ayah separates whoever wants worldly reward from whoever wants the reward of the Hereafter, casting the section's preference as an actionable intention.
- (3:152) [terra: strong (missing-ayat turn); basis: speaker+theme] وَلَقَدْ صَدَقَكُمُ ٱللَّهُ وَعْدَهُۥٓ إِذْ تَحُسُّونَهُم بِإِذْنِهِۦ ۖ حَتَّىٰٓ إِذَا فَشِلْتُمْ وَتَنَٰزَعْتُمْ فِى ٱلْأَمْرِ وَعَصَيْتُم مِّنۢ بَعْدِ مَآ أَرَىٰكُم مَّا تُحِبُّونَ ۚ مِنكُم مَّن يُرِيدُ ٱلدُّنْيَا وَمِنكُم مَّن يُرِيدُ ٱلْءَاخِرَةَ ۚ ثُمَّ صَرَفَكُمْ عَنْهُمْ لِيَبْتَلِيَكُمْ ۖ وَلَقَدْ عَفَا عَنكُمْ ۗ وَٱللَّهُ ذُو فَضْلٍ عَلَى ٱلْمُؤْمِنِينَ
  Unverified discovery rationale: terra: At Uḥud some desired worldly gain and others desired the Hereafter, a concrete enactment of the preference diagnosed in 87:16.
- (3:169) [luna: strong; terra: contrast; basis: contrast+root+scene+theme] وَلَا تَحْسَبَنَّ ٱلَّذِينَ قُتِلُوا۟ فِى سَبِيلِ ٱللَّهِ أَمْوَٰتًۢا ۚ بَلْ أَحْيَآءٌ عِندَ رَبِّهِمْ يُرْزَقُونَ
  Unverified discovery rationale: luna: The section asks what counts as life beyond bodily survival; here the slain are alive with their Lord and provided for, unlike the torment that has neither death nor beneficial life. | terra: The slain are alive with their Lord and provided for, coupling true life with benefit and provision rather than mere continuance.
- (3:185) [terra: strong; basis: root+theme] كُلُّ نَفْسٍۢ ذَآئِقَةُ ٱلْمَوْتِ ۗ وَإِنَّمَا تُوَفَّوْنَ أُجُورَكُمْ يَوْمَ ٱلْقِيَٰمَةِ ۖ فَمَن زُحْزِحَ عَنِ ٱلنَّارِ وَأُدْخِلَ ٱلْجَنَّةَ فَقَدْ فَازَ ۗ وَمَا ٱلْحَيَوٰةُ ٱلدُّنْيَآ إِلَّا مَتَٰعُ ٱلْغُرُورِ
  Unverified discovery rationale: terra: Every soul tastes death, full recompense comes later, and worldly life is deceptive enjoyment; ordinary death and the near life's false value are held together.
- (4:56) [luna: medium; terra: strong; basis: root+scene+theme] إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا سَوْفَ نُصْلِيهِمْ نَارًۭا كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا لِيَذُوقُوا۟ ٱلْعَذَابَ ۗ إِنَّ ٱللَّهَ كَانَ عَزِيزًا حَكِيمًۭا
  Unverified discovery rationale: luna: The section says the fire's victim cannot die and so cannot leave the torment; here burned skin is replaced so the punishment can continue. That is a specific bodily mechanism for sustained torment, though the verse does not use the no-death formula. | terra: Burned skins are repeatedly replaced so punishment can continue to be tasted, a concrete mechanism for torment that neither benefits as life nor concludes in death.
- (4:74) [terra: strong (missing-ayat turn); basis: speaker+theme] ۞ فَلْيُقَٰتِلْ فِى سَبِيلِ ٱللَّهِ ٱلَّذِينَ يَشْرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا بِٱلْءَاخِرَةِ ۚ وَمَن يُقَٰتِلْ فِى سَبِيلِ ٱللَّهِ فَيُقْتَلْ أَوْ يَغْلِبْ فَسَوْفَ نُؤْتِيهِ أَجْرًا عَظِيمًۭا
  Unverified discovery rationale: terra: Those who exchange worldly life for the Hereafter are told to fight, presenting the saving inverse of preferring the nearer life.
- (4:77) [luna: medium; terra: strong (missing-ayat turn); basis: root+speaker+theme] أَلَمْ تَرَ إِلَى ٱلَّذِينَ قِيلَ لَهُمْ كُفُّوٓا۟ أَيْدِيَكُمْ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ فَلَمَّا كُتِبَ عَلَيْهِمُ ٱلْقِتَالُ إِذَا فَرِيقٌۭ مِّنْهُمْ يَخْشَوْنَ ٱلنَّاسَ كَخَشْيَةِ ٱللَّهِ أَوْ أَشَدَّ خَشْيَةًۭ ۚ وَقَالُوا۟ رَبَّنَا لِمَ كَتَبْتَ عَلَيْنَا ٱلْقِتَالَ لَوْلَآ أَخَّرْتَنَآ إِلَىٰٓ أَجَلٍۢ قَرِيبٍۢ ۗ قُلْ مَتَٰعُ ٱلدُّنْيَا قَلِيلٌۭ وَٱلْءَاخِرَةُ خَيْرٌۭ لِّمَنِ ٱتَّقَىٰ وَلَا تُظْلَمُونَ فَتِيلًا
  Unverified discovery rationale: luna: The section's selection is between near life and afterlife; this verse calls worldly enjoyment little and says the afterlife is better for the one who is mindful, specifying the measure behind that choice. | terra: Worldly enjoyment is declared little and the Hereafter better for the God-conscious, a close verbal counterpart to 87:16-17.
