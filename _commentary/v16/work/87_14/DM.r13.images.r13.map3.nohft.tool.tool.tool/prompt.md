Focus: 87:14. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. No other command or tool is available.

===== _commentary/v16/prompts/r13/write.md =====
Write the Turkish reading of the focus Quranic ayah for a curious reader who
knows neither Arabic nor how lexical families work, and who already has the
plain meaning. Show what a translation cannot give: the supported latent
meanings and resonances of its words, heard through their attested senses, the
ayah's neighbours, its surah and the Quran. Work from the supplied evidence and
your own knowledge of Arabic and the Quran. This is your own
interpretation, not a catalogue: maps and readings by earlier readers are
proposals, and what their members reveal together is yours to find or correct.
A surprise is welcome when the evidence supports it. There is no length limit.

Themes lead; words serve them. First understand the ayah in its grammar and
situation. Then explore its words' attested senses within and across roots,
the chains they take part in, and Quran passages that share its words or stage
the same act, scene or stance without sharing a word; a partial finding may
gain its missing support from another. Let the themes emerge from what these
reveal together, not from the familiar reading. Write the reading as those
themes: a word, a family image or a Quran passage enters where it grounds,
expands, complicates or joins a theme, developed as far as that work needs.
Never list a family's senses for their own sake, but judge each attested sense
by what it does, not by the branch it is filed under. Where this ayah's words
take part in a surah chain, that chain can found a theme here even when
another ayah completes it, and so can a scene where two such chains meet.
Every image this ayah's own words take part in is developed here as far as the
word carries it: what the object is, how it works, what usage names it. The
scene it forms with other ayat's words belongs to the surah commentary; recall
it in a sentence, tied to the ayah whose words carry it, never as something
explained before.

Keep these guards:

- A family image is heard beside the word's meaning in this ayah, never in
  place of it; say so once, where the first one enters. Show where each
  image comes from: the word, the usage that carries the image, quoted in
  Arabic, then its work in the theme. Report usage as what speakers called
  or said, varying the grammar so that no formula recurs ("… denir",
  "Araplar … derlerdi"); never name a dictionary, and never make "the family"
  a speaker.
- Keep root identity, family images and your interpretive connections
  distinct. Same word, same root and analogy are different things; an echo
  root does not establish identity.
- Explain a concrete object or mechanism by its work before drawing its
  meaning; do not flatten it into a label.
- Never invent a sense, source, vowel, etymology, historical fact, citation or
  chronology.
- Where a key word lives in Turkish as a narrowed or shifted loanword, let the
  reader feel what the Turkish word no longer carries, once.
- When you use another Quran passage, assume the reader does not know it:
  give its speaker, its situation as the Quran itself tells it there and in
  the neighbouring ayat, and the wording the connection needs. Use no hadith, no exegetes' views and no
  report from outside the Quran (no occasion of revelation, no name the Quran
  does not give, no date): the Quran, the supplied dictionary and Arabic usage
  carry the reading.
- The prose never talks about its own sources or process and never hedges in
  the first person ("hafızadan", "bildiğim kadarıyla", "sözlük", the map, its
  chains, workflow language; branch IDs only in tag sources).
  A claim about Arabic that neither the supplied texts nor the Quran text can
  check goes in the ledger as memory.

Write continuous prose in `##` sections, one theme each, warm and direct:
explain, do not dramatize; no lists and no closing recap.

Every Arabic quotation (Quran or dictionary phrase) goes in the reader
tag, as normal prose, never in quotation marks or backticks, and every tag
ends with its source, so the reader can check it:
{ar:exact Arabic, tr:readable Turkish transliteration, gloss:Turkish meaning, source:…}
- a dictionary phrase or a branch's sense: source:"<root letters>,<branch id>",
  e.g. source:"ق و م,B016";
- a Quran quotation: source:<surah:ayah>, e.g. source:72:16, the one ayah that
  holds the quoted words, no ranges;
- Arabic from your own memory that is not in the supplied dictionary:
  source:"memory".
A branch's sense given in Turkish without its Arabic, and a Quran passage named
without quoting it, carry the source alone: {source:"ق و م,B016"},
{source:15:41}. Never write a Quran reference outside a tag; quote the
surah's own words in tags too, and name its ayat in words ("dördüncü ayet"). The gloss gives
the ayah's word by its meaning here, a family image by that image. Copy Quran
Arabic from the supplied text or the lookup.

Output: the prose; then a line containing only
=== LEDGER ===
then, in plain English, one short line per item, a few words each:
- memory: <a claim about Arabic the texts cannot check>
- not written: <finding> - <why it could not found, reshape or join a theme>


===== _commentary/v16/prompts/r13/additions.md =====
No additions: write.md is the whole brief.


===== _commentary/v16/work/87_14/D.r13/context.md =====
# 87:14 — focus

قَدْ أَفْلَحَ مَن تَزَكَّىٰ

Anchor translation (canonical reading, reference only):

Arınan kişi gerçekten kurtuluşa ermiştir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | قَدْ | قَد |  | CERT |
| 2 | أَفْلَحَ | أَفْلَحَ | ف ل ح | V |
| 3 | مَن | مَن |  | REL |
| 4 | تَزَكَّىٰ | تَزَكَّىٰ | ز ك و | V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 87 — full text (context; no pericope)

- 87:1 سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى
- 87:2 ٱلَّذِى خَلَقَ فَسَوَّىٰ
- 87:3 وَٱلَّذِى قَدَّرَ فَهَدَىٰ
- 87:4 وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ
- 87:5 فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ
- 87:6 سَنُقْرِئُكَ فَلَا تَنسَىٰٓ
- 87:7 إِلَّا مَا شَآءَ ٱللَّهُ ۚ إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ
- 87:8 وَنُيَسِّرُكَ لِلْيُسْرَىٰ
- 87:9 فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ
- 87:10 سَيَذَّكَّرُ مَن يَخْشَىٰ
- 87:11 وَيَتَجَنَّبُهَا ٱلْأَشْقَى
- 87:12 ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ
- 87:13 ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- 87:14 ◀ focus قَدْ أَفْلَحَ مَن تَزَكَّىٰ
- 87:15 وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ
- 87:16 بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- 87:17 وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ
- 87:18 إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ
- 87:19 صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ


===== _commentary/v16/work/87_14/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ف ل ح (root_001175) — identity root of أَفْلَحَ (w2)

- **B001** yarmak veya kesip ayırmak — bir şeyi yarmak veya kesmek · toprağı sürmek üzere yarmak · toprağı sürmek üzere yarmak · demiri başka bir demirle yarmak veya kesmek · bir uzuvdaki yarıklar
  أصل يدل على شق (maqayis)؛ فلحت الأرض شققتها (maqayis;sihah;tahdhib)؛ فلحت الشيء إذا شققته أو قطعته (jamhara)؛ الحديد بالحديد يفلح أي يشق أو يقطع (maqayis;ayn;jamhara;sihah;tahdhib;mufradat)
- **B002** dudakta, özellikle alt dudakta yarık — dudaktaki yarık · alt dudağı yarık olan erkek · dudağında yarık bulunan kadın · dudaktaki yarığın kendisi
  الفلح الشق في الشفة (ayn;tahdhib)؛ الأفلح المشقوق الشفة السفلى (maqayis;jamhara;sihah;tahdhib)؛ امرأة فلحاء وعنترة الفلحاء لفلحة كانت به (maqayis;jamhara;sihah;tahdhib)
- **B003** çiftçi ve toprağı işleme işi — çiftçi, toprağı işleyen kimse · toprağı sürme ve çiftçilik işi
  سمي الأكار فلاحا لأنه يشق الأرض (maqayis;jamhara;sihah;tahdhib;mufradat)؛ الفلاحون الزراعون (ayn)؛ الفلاحة الحراثة أو صناعة الفلاح (jamhara;sihah;tahdhib)
- **B004** çiftçiye benzetilen ücretli taşıyıcı — çiftçiye benzetilerek adlandırılan ücretli taşıyıcı
  الفلاح المكاري وإنما قيل له فلاح تشبيها بالأكار (ayn;tahdhib)؛ وجعله ابن أحمر المكاري (jamhara)
- **B005** iyilik içinde kalma, amaca ulaşma ve kurtuluş — iyilik içinde kalma, başarı ve kurtuluş · iyilik içinde kalma ve başarı · başarmak, amacına ulaşmak veya iyilik elde etmek · dilediğin biçimde yaşa · işinde başarı kazan ve onu kendi başına yürüt · kurtuluşa ve kalıcı iyiliğe yönel · iyilik elde eden başarılı kişi · dünya hayatında kalıcılık, varlık ve saygınlık elde etme · son bulmayan yaşam, yoksulluksuz varlık, aşağılanmayan saygınlık ve bilgisizlikten uzak bilgi · şafak öncesi öğünü ya da gece ibadetinin kazancını kaçırmaktan korkmak
  الأصل الثاني الفلاح البقاء والفوز (maqayis)؛ الفلاح والفلح البقاء في الخير (ayn;tahdhib)؛ الفلح والفلاح البقاء (jamhara)؛ الفلاح الفوز والنجاة والبقاء (sihah)؛ أفلح وأنجح إذا أدرك مطلوبه (jamhara)؛ استفلحي بأمرك أي فوزي أو اظفري بأمرك (maqayis;sihah;tahdhib)؛ الفلاح الظفر وإدراك بغية (mufradat)
- **B006** orucu sürdürmeye güç veren şafak öncesi öğün — şafak öncesi öğün · şafak öncesi öğünü ya da gece ibadetinin kazancını kaçırmaktan korkmak
  الفلاح السحور (maqayis;ayn;sihah;tahdhib)؛ سمي فلاحا لأن الإنسان تبقى معه قوته على الصوم (maqayis)؛ لأن به بقاء الصوم (sihah;tahdhib)؛ سمي السحور الفلاح (mufradat)
- **B007** alışverişi çekici gösterme; yalanla kandırma ve alaya alma — satış ve alışverişi satıcıya ve alıcıya çekici göstermek · satış ve alışverişi satıcıya ve alıcıya çekici göstermek · onları kandırıp gerçeğe aykırı söz söylemek · başkasını daha yüksek bedel vermeye kandırmak için kiracının bedeli artırması · kandırma ve alaya alma
  فلحت للقوم وبالقوم أفلح فلاحة وهو أن يزين البيع والشراء للبائع والمشتري (tahdhib)؛ فلحت بهم تفليحا إذا مكر بهم وقال لهم غير الحق (tahdhib)؛ الفلح النجس وهو زيادة المكتري ليزيد غيره فيغر به (tahdhib)؛ التفليح المكر والاستهزاء (tahdhib)

## ز ك و (root_000637) — identity root of تَزَكَّىٰ (w4)

- **B001** büyüyüp artma — büyümek, artmak ve verim kazanmak · büyüme ve artış · gelişmiş ve artışı belirgin · Tanrı onu büyütüp artırdı · ekin büyüyüp arttı · kişi bolluğa kavuşup rahat yaşadı
  أصل يدل على نماء وزيادة (maqayis)؛ زكا الزرع يزكو زكاء ازداد ونما وكل شيء ازداد ونما فهو يزكو زكاء (ayn)؛ زكا الزرع يزكو زكاء ممدود أي نما (sihah)؛ كل شيء يزداد ويسمن فهو يزكو زكاء (tahdhib)؛ أصل الزكاة النمو الحاصل عن بركة الله تعالى (mufradat)
- **B002** ahlaken arınıp düzgünleşme — arınmak ve düzgünleşmek · temiz, doğru ve kötülükten sakınan · arındırıp düzeltmek · arındırma, düzeltme ve iyiliklerle geliştirme · iç temizliği ve ahlaki düzgünlük · kendini övmek veya sözle temiz saymak · dinen uygun ve sonu zarar vermeyen yiyecek · temizlik ve düzgünlük
  الطهارة زكاة المال؛ زكاة لأنها طهارة (maqayis)؛ والزكاة الصلاح؛ رجل زكي تقي (ayn)؛ معناه صلاحا؛ ما صلح؛ أي يصلح (tahdhib)؛ بزكاء النفس وطهارتها؛ حلالا لا يستوخم عقباه (mufradat)
- **B003** yoksula verilmesi gereken mal payı — yoksullara verilmesi gereken mal payı · malının gereken payını ödemek · malından karşılıksız vermek
  زكاة المال (maqayis;ayn;sihah;tahdhib)؛ زكى ماله تزكية أي أدى عنه زكاته؛ وتزكى أي تصدق (sihah)؛ ما يخرج الإنسان من حق الله تعالى إلى الفقراء (mufradat)
- **B004** yakışmamak [kalıp] — ona yakışmamak veya durumuna uygun düşmemek
  أمر لا يزكو بفلان أي لا يليق به (maqayis;sihah)؛ وهذا الأمر لا يزكو أي لا يليق (ayn)؛ هذا الأمر لا يزكو بفلان أي لا يليق به (tahdhib)
- **B005** çift olma — çift veya iki öğeli · tek veya çift · avuçtaki çift mi tek mi · avuçtaki şey için tek-çift söylemek
  الزكا الزوج وهو الشفع (maqayis)؛ وزكا الشفع يقال خسا أو زكا (sihah)؛ العرب تقول للفرد خسا وللزوجين اثنين زكا؛ هو يخسي ويزكي إذا قبض على شيء في كفه وقال أزكا أم خسا (tahdhib)

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 87:14, and ## Buluşmalar) =====
## Yarılan tarla: büyüme ve hakkı verilen ürün

On dördüncü ayet {ar:قَدْ أَفْلَحَ مَن تَزَكَّىٰ, tr:kad eflaha men tezekkâ, gloss:arınan kurtuluşa ermiştir, source:87:14} der. Ayetin iki fiilinin aileleri bir tarla sahnesi kurar. فلح toprağı yarmaktır: {ar:فلحت الأرض شققتها, tr:felahtu'l-arda şakaktuhâ, gloss:toprağı sürdüm ve yardım, source:"ف ل ح,B001"}. Toprağı süren de bu adı alır: {ar:سمي الأكار فلاحا لأنه يشق الأرض, tr:sumiye'l-ekkâru fellâhan li-ennehû yeşukku'l-ard, gloss:çiftçiye toprağı yardığı için fellâh denmiştir, source:"ف ل ح,B003"}. Kökün başarı anlamı ise kalıcılık üzerinden tanımlanır: {ar:الفلاح والفلح البقاء في الخير, tr:el-felâhu ve'l-felahu el-bekâu fi'l-hayr, gloss:felâh iyilik içinde kalmaktır, source:"ف ل ح,B005"}. {ar:الفلاح الفوز والنجاة والبقاء, tr:el-felâh el-fevzu ve'n-necâtu ve'l-bekâ, gloss:felâh kazanmak kurtulmak ve kalıcı olmaktır, source:"ف ل ح,B005"}. Bu tanım on dördüncü ayeti, on yedinci ayetteki iki kelimeye, "hayırlı" ve "kalıcı" kelimelerine bağlar. زكا ekinin büyüyüp çoğalmasıdır: {ar:زكا الزرع يزكو زكاء ازداد ونما, tr:zekâ'z-zer'u yezkû zekâen izdâde ve nemâ, gloss:ekin artıp büyüdü, source:"ز ك و,B001"}. {ar:أصل الزكاة النمو الحاصل عن بركة الله تعالى, tr:aslu'z-zekâti en-nemuvvu'l-hâsılu an bereketi'llâh, gloss:zekâtın aslı Allah'ın bereketinden gelen büyümedir, source:"ز ك و,B001"}. Aynı kök üründen verilen payı da anlatır: {ar:زكى ماله تزكية أي أدى عنه زكاته؛ وتزكى أي تصدق, tr:zekkâ mâlehû tezkiyeten ey eddâ anhu zekâtehû ve tezekkâ ey tesaddaka, gloss:malının zekâtını verdi; tezekkâ sadaka verdi demektir, source:"ز ك و,B003"}. Bu pay geri kalanı temizler: {ar:الطهارة زكاة المال؛ زكاة لأنها طهارة, tr:et-tahâretu zekâtu'l-mâl zekâtun li-ennehâ tahâra, gloss:temizlik malın zekâtıdır; temizlik olduğu için zekât denmiştir, source:"ز ك و,B002"}.

Sahnenin öbür parçaları surenin başka kelimelerindedir. Dördüncü ayetin fiili hasılatın adını verir: {ar:الخرج والخراج ما يخرج من المال في السنة بقدر معلوم, tr:el-harcu ve'l-harâcu mâ yahrucu mine'l-mâli fi's-seneti bi-kaderin ma'lûm, gloss:harâc maldan her yıl bilinen bir ölçüyle çıkandır, source:"خ ر ج,B003"}. Bu tanım üçüncü ayetin kökünü de içerir. Rab, çiftliğe bakıp onu tamamlayandır: {ar:رب فلان ضيعته إذا قام على إصلاحها, tr:rabbe fulânun day'atehû iẕâ kâme alâ islâhihâ, gloss:falanca çiftliğinin bakımını üstlendi, source:"ر ب ب,B002"}. On yedinci ayetteki "kalıcı" kelimesinin ailesinde, hasılattan geriye kalan şey vardır: {ar:الباقي حاصل الخراج ونحوه, tr:el-bâkî hâsılu'l-harâci ve nahvih, gloss:bâkî hasılattan ve benzerinden kalan miktardır, source:"ب ق ي,B002"}.

Düz bir anlatım on dördüncü ayeti "arınan kurtuldu" diye özetler. Tarla sahnesi bu cümleye bir işleyiş ekler: toprak yarılır, ekin büyür, büyüyen üründen bir pay verilir, verilen pay geri kalanı temizler, ve bu büyüme iyilik içinde kalıcı olur. Böylece tarla, beşinci ayetteki yabani otlağın karşısına geçer. Aynı toprakta biri kuruyup selle gider, öbürü işlenir, verimi alınır ve hakkı ödenir.

Kur'an bu tarlayı açıkça sahneler. Allah insandan yemeğine bakmasını ister: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:biz suyu bol bol döktük, source:80:25}, {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:ŝumme şakakne'l-arda şakkâ, gloss:sonra toprağı yardıkça yardık, source:80:26}. Yarmak fiili tarlanın sürülmesini de verir. Başka bir yerde Allah sorar: {ar:أَفَرَءَيْتُم مَّا تَحْرُثُونَ, tr:e-fe-raeytum mâ tahruŝûn, gloss:ektiğinizi gördünüz mü, source:56:63}. Ardından {ar:لَوْ نَشَآءُ لَجَعَلْنَٰهُ حُطَٰمًۭا, tr:lev neşâu le-cealnâhu hutâmâ, gloss:dileseydik onu çer çöp yapardık, source:56:65} diye ekler. Tarla da otlağın kaderine düşebilir. Ayrım ekimin hangi tarlaya yapıldığındadır: {ar:مَن كَانَ يُرِيدُ حَرْثَ ٱلْءَاخِرَةِ نَزِدْ لَهُۥ فِى حَرْثِهِۦ ۖ وَمَن كَانَ يُرِيدُ حَرْثَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِن نَّصِيبٍ, tr:men kâne yurîdu harŝe'l-âhireti nezid lehû fî harŝih ve men kâne yurîdu harŝe'd-dunyâ nu'tihî minhâ ve mâ lehû fi'l-âhireti min nasîb, gloss:ahiret tarlasını isteyenin tarlasını artırırız; dünya tarlasını isteyene ondan veririz ama onun ahirette payı yoktur, source:42:20}. Bu ayet, on altıncı ve on yedinci ayetteki karşıtlığı tarlanın diliyle söyler. Ürünün hakkı için {ar:وَءَاتُوا۟ حَقَّهُۥ يَوْمَ حَصَادِهِۦ, tr:ve âtû hakkahû yevme hasâdih, gloss:hasat günü hakkını verin, source:6:141} denir. Malını veren kişi için {ar:ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ, tr:elleẕî yu'tî mâlehû yetezekkâ, gloss:arınmak için malını veren, source:92:18} denir. Can üzerine yemin edilen ayetlerde iki ayrı son yan yana konur: {ar:قَدْ أَفْلَحَ مَن زَكَّىٰهَا, tr:kad eflaha men zekkâhâ, gloss:onu arıtan kurtuluşa erdi, source:91:9}, {ar:وَقَدْ خَابَ مَن دَسَّىٰهَا, tr:ve kad hâbe men dessâhâ, gloss:onu gömüp örten ise hüsrana uğradı, source:91:10}. Tarlanın dilinde arıtmanın karşıtı, tohumu toprağın altında boğmaktır. Peygamber'in arkadaşları ise bir ekine benzetilir: {ar:كَزَرْعٍ أَخْرَجَ شَطْـَٔهُۥ فَـَٔازَرَهُۥ فَٱسْتَغْلَظَ فَٱسْتَوَىٰ عَلَىٰ سُوقِهِۦ, tr:ke-zer'in ahrace şat'ehû fe-âzerahû fe'steğleza fe'stevâ alâ sûkıh, gloss:filizini çıkaran sonra onu güçlendiren sonra kalınlaşıp sapları üzerinde doğrulan bir ekin gibi, source:48:29}. Bu ayet, surenin dördüncü ayetindeki "çıkardı" fiilini ve ikinci ayetindeki "düzene koydu" fiilinin kökünü, kurumayan bir ekinde buluşturur. Bir başka yerde kurtuluşa erenler sayılırken {ar:قَدْ أَفْلَحَ ٱلْمُؤْمِنُونَ, tr:kad eflaha'l-mu'minûn, gloss:müminler kurtuluşa ermiştir, source:23:1} denir ve onlar arasında {ar:وَٱلَّذِينَ هُمْ لِلزَّكَوٰةِ فَٰعِلُونَ, tr:velleẕîne hum li'z-zekâti fâilûn, gloss:zekâtı yerine getirenler, source:23:4} anılır. Musa'nın karşısındaki sihirbazlar da sözlerini cennet bahçelerini anarak bitirir: {ar:وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ, tr:ve ẕâlike cezâu men tezekkâ, gloss:bu arınanın karşılığıdır, source:20:76}.

Kaynaklar: 87:14 أَفْلَحَ ف ل ح B001; 87:14 أَفْلَحَ ف ل ح B003; 87:14 أَفْلَحَ ف ل ح B005; 87:14 تَزَكَّىٰ ز ك و B001; 87:14 تَزَكَّىٰ ز ك و B003; 87:14 تَزَكَّىٰ ز ك و B002; 87:4 أَخْرَجَ خ ر ج B003; 87:1 رَبِّ ر ب ب B002; 87:17 أَبْقَىٰٓ ب ق ي B002

## Buluşmalar

İmgelerin çoğu, surenin son ayetinde adı geçen Musa'nın hikâyesinde buluşur. Musa uzakta bir ateş görür ve {ar:أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ecidu ale'n-nâri hudâ, gloss:ateşin başında bir yol gösteren bulurum, source:20:10} umuduyla ona yönelir. Uzaktan görülen ateşin sahnesi ile yol sahnesi burada aynı cümlededir. Ateşin başında önce seçim gelir: {ar:وَأَنَا ٱخْتَرْتُكَ, tr:ve ene'htertuk, gloss:seni ben seçtim, source:20:13}. Sonra namaz ve anma gelir: {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14}. Sonra gizli olan gelir: {ar:أَكَادُ أُخْفِيهَا, tr:ekâdu uhfîhâ, gloss:onu neredeyse gizli tutuyorum, source:20:15}. Başka bir anlatımda ateşin başında tesbih söylenir: {ar:وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve subhânallâhi rabbi'l-âlemîn, gloss:Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu sahnede surenin on ikinci ve on beşinci ayetleri arasındaki karşıtlık bir kişinin yolculuğunda çözülür. Aynı ateşe yaklaşan biri onun içine sokulmaz. Ateş ona yol, seçilmişlik, namaz ve anma verir. Surede bu iki son iki ayrı kişiye düşer: on ikinci ayetteki kişi ateşe girer, on beşinci ayetteki kişi namaz kılar. Kelimelerin harf benzerliği bu ayrılığı kulakta da duyurur.

İkinci büyük buluşma selin sahnesidir. Gökten inen suyun vadilerde {ar:بِقَدَرِهَا, tr:bi-kaderihâ, gloss:kendi ölçülerince, source:13:17} akması, ölçüp biçme sahnesini çağırır. Selin taşıdığı köpük, otlağın vardığı döküntüdür. İnsanların {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâr, gloss:ateşte üzerine yaktıkları şeyden, source:13:17} çıkan köpük ise ateşin sahnesine girer. Faydalı olanın yerde kalması da öğüdün ve kalıcılığın sahnesidir. Kurumuş otun tencerenin köpüğüyle aynı adı taşıması, bu iki köpüğün Arapçada zaten tek bir kelimede birleştiğini gösterir. Bu ayet surenin beşinci ayetinden on yedinci ayetine uzanan çizgiyi tek bir manzaraya sığdırır. Bir yanda giden döküntü, öbür yanda kalan fayda vardır.

Üçüncü buluşma, Musa'nın karşısındaki sihirbazların sahnesidir. Sihirbazlar secdeye kapanır. Firavun kendi azabının daha çetin ve {ar:وَأَبْقَىٰ, tr:ve ebkâ, gloss:ve daha kalıcı, source:20:71} olduğunu söyler. Sihirbazlar da onu {ar:لَن نُّؤْثِرَكَ, tr:len nu'ŝirak, gloss:seni asla tercih etmeyiz, source:20:72} diye reddeder, yalnızca {ar:هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:hâẕihi'l-hayâte'd-dunyâ, gloss:bu dünya hayatı, source:20:72} üzerinde hüküm verebileceğini söyler ve {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} der. Sonra suçlu için {ar:لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:lâ yemûtu fîhâ ve lâ yahyâ, gloss:orada ne ölür ne yaşar, source:20:74} der, iman edenler için {ar:ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:ed-derecâtu'l-ulâ, gloss:en yüce dereceler, source:20:75} der, ve hepsini {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76} sözüyle bağlar. Bu birkaç ayette seçim, kalıcı hayat, yükseklik ve yarılan tarlanın kelimeleri birlikte konuşur. Firavun'un "en yüce" iddiası da başka bir anlatımda bu sahneye eklenir. Surenin ikinci yarısı, on üçüncü ayetten on yedinci ayete kadar, neredeyse kelimesi kelimesine Musa'nın hikâyesindeki bir topluluğun ağzından gelmiştir. Son ayetin Musa'nın sayfalarını anması da bu yüzden önem taşır.

Dördüncü buluşma ot ile seçimdir. Dünya hayatının kuruyan ota benzetildiği ayetin hemen ardından kalıcı iyi işlerin daha hayırlı olduğu söylenir. Dünya hayatı başka bir yerde bir {ar:زَهْرَةَ, tr:zehrate, gloss:çiçek, source:20:131} olarak anılır, ve aynı ayet {ar:خَيْرٌۭ وَأَبْقَىٰ, tr:hayrun ve ebkâ, gloss:daha hayırlı ve daha kalıcı, source:20:131} diye biter. Otlağın sahnesi seçimin sahnesine bu yolla girer. Beşinci ayetteki ot ile on altıncı ayetteki tercih edilen hayat aynı nesnedir. Kalıcı olan ise ayıklanıp seçilen şeydir. Tarlanın sahnesi bu iki uç arasında bir yol açar. Kalıcı iyilik anlamına gelen kurtuluş kelimesi on dördüncü ayette, toprağı yaran çiftçinin kelimesiyle söylenir. Yabani ot kendi haline kalınca kurur ve selle gider. İşlenen toprağın ürünü ise büyür, hakkı verilir ve geriye kalan bir pay bırakır. Biri dünya tarlası, öbürü ahiret tarlasıdır.

Beşinci buluşma, yaratma fiillerinde zanaat ile bedenin birleşmesidir. İkinci ayetteki ikili hem yontulmuş oku hem de ceninin biçimlenmesini anlatır. Rahimden başlayan ayetin toprağın yağmurla titreşmesiyle bitmesi, beden ile otlağı da birbirine bağlar. Aynı aile, üçüncü ayetteki ölçmeyi pay ölçmeye de taşır, ve on altıncı ayetteki tercih bir pay seçimine döner. Değneği ateşte doğrultmanın fiili on ikinci ayetin fiilidir. Bu fiil aynı ateşin düzelten bir işi ile içine düşenin katlandığı bir işi olduğunu duyurur. Bu son bağ dilin yankısıdır, ayetin sözü değildir.

Bu buluşmalar surenin hareketini taşır. Sure tesbih emriyle ve yükseklikle açılır. Ölçen, yontan ve yol gösteren Rabbin işiyle devam eder. Yağmurun çıkardığı ve selin götürdüğü ot ile sona gelen bir ömür gösterir. Sonra sözün toplanıp unutulmamasına, sunulan öğüde ve öğüt karşısında ikiye ayrılan insanlara geçer. Biri ateşe girer ve ne ölü ne diri kalır. Öbürü arınır, Rabbinin adını anar ve namaz kılar, yani surenin başındaki emri yerine getirir. Ardından seçim gelir: yakın olan öne konmuştur, ama arkadan gelen daha hayırlı ve daha kalıcıdır. Sure, bu sözün ilk sayfalarda, ateşin başında namaz ve anma emrini alan Musa'nın ve Rabbinden kendisini puttan uzak tutmasını isteyen İbrahim'in sayfalarında yazılı olduğunu söyleyerek kapanır.

