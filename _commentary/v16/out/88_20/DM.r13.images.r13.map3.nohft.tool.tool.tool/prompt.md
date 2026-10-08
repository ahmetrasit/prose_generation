Focus: 88:20. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

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


===== _commentary/v16/work/88_20/D.r13/context.md =====
# 88:20 — focus

وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ

Anchor translation (canonical reading, reference only):

Ve yere, nasıl düzleştirildiğine?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَإِلَى | إِلَىٰ |  | CONJ;P |
| 2 | ٱلْأَرْضِ | أَرْض | ء ر ض | DET;N |
| 3 | كَيْفَ | كَيْف | ك ي ف | INTG |
| 4 | سُطِحَتْ | سُطِحَتْ | س ط ح | V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 88 — full text (context; no pericope)

- 88:1 هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ
- 88:2 وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ
- 88:3 عَامِلَةٌۭ نَّاصِبَةٌۭ
- 88:4 تَصْلَىٰ نَارًا حَامِيَةًۭ
- 88:5 تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ
- 88:6 لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ
- 88:7 لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ
- 88:8 وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ
- 88:9 لِّسَعْيِهَا رَاضِيَةٌۭ
- 88:10 فِى جَنَّةٍ عَالِيَةٍۢ
- 88:11 لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ
- 88:12 فِيهَا عَيْنٌۭ جَارِيَةٌۭ
- 88:13 فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ
- 88:14 وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ
- 88:15 وَنَمَارِقُ مَصْفُوفَةٌۭ
- 88:16 وَزَرَابِىُّ مَبْثُوثَةٌ
- 88:17 أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ
- 88:18 وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ
- 88:19 وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ
- 88:20 ◀ focus وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ
- 88:21 فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
- 88:22 لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- 88:23 إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- 88:24 فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- 88:25 إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 88:26 ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/work/88_20/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ء ر ض (root_000025) — identity root of ٱلْأَرْضِ (w2)

- **B001** yer ve yere bakan alt bölüm — yer, yeryüzü · yerler, ülkeler · bir şeyin yere bakan altı · hayvanın tırnağı veya ayaklarının altı
  كل شيء يسفل ويقابل السماء (maqayis)؛ الأرض التي نحن عليها (maqayis)؛ الأرض الجرم المقابل للسماء (mufradat)؛ كل ما سفل فهو أرض (sihah)؛ الأرض حافر الدابة (ayn)؛ أسفل قوائم الدابة (sihah)
- **B002** yumuşak ve verimli toprak — yumuşak, verimli ve bol bitkili toprak · yumuşak tabanlı geniş çayırlık · toprak verimlileşti · bitki iyice köklendi, çoğaldı veya biçilecek duruma geldi · toprakta kök salmış fidan · oğlak yer bitkisini yedi veya onunla semirdi
  أرض أريضة لينة طيبة (maqayis;ayn)؛ أرض أريضة أي زكية (sihah)؛ حسنة النبت (mufradat)؛ تأرض النبت إذا أمكن أن يجز (maqayis;sihah)؛ تأرض النبت تمكن على الأرض فكثر (mufradat)؛ تأرض الجدي إذا تناول نبت الأرض (mufradat)؛ جدي أريض أي سمين (sihah)
- **B003** iyiliğe yatkın ve layık [kalıp] — iyiliğe yatkın, layık ve alçak gönüllü kişi · bunu yapmaya en uygunları
  رجل أريض للخير أي خليق له شبه بالأرض الأريضة (maqayis)؛ رجل أريض أي متواضع خليق للخير (sihah)؛ هو آرضهم أن يفعل ذلك أي أخلقهم (sihah)
- **B004** yabancı kimse — yabancı kimse
  فلان ابن أرض أي غريب (maqayis)
- **B005** kalın yün veya kıl yaygı — kalın yün veya kıl yaygı
  الإراض بساط ضخم من وبر أو صوف (maqayis)؛ الإراض بالكسر بساط ضخم من صوف أو وبر (sihah)
- **B006** yere çökercesine ağırlaşıp oyalanmak — yere bağlı kalmak, ağırlaşıp oyalanmak
  تأرض فلان إذا لزم الأرض (maqayis)؛ فقام عجلان وما تأرضا أي ما تلبث (sihah)؛ التأرض أيضا التثاقل إلى الأرض (sihah)
- **B007** karşısına çıkıp kendini ortaya koymak — birinin karşısına çıkıp kendini ortaya koymak
  جاء فلان يتأرض إلي أي يتصدى ويتعرض (sihah)
- **B008** titreme veya ürperme — insanı tutan titreme veya ürperme · titreme ve sarsılma
  الأرض الرعدة (maqayis;ayn)؛ بفلان أرض أي رعدة (maqayis)؛ الأرْص النفضة والرعدة (sihah)
- **B009** soğuk algınlığı — soğuk algınlığı · soğuk algınlığına yakalanmış · soğuk algınlığına uğratmak
  الأرض الزكمة رجل مأروض أي مزكوم (maqayis)؛ الأرض الزكام وأرض فهو مأروض (ayn)؛ الأرض الزكام وقد آرضه الله إيراضا أي أزكمه فهو مأروض (sihah)
- **B010** odun yiyen küçük canlı — odun yiyen küçük canlı · odunu bu canlı yedi ve zarar verdi
  الأرضة دويبة بيضاء تشبه النمل تأكل الخشب (ayn)؛ الأرضة بالتحريك دويبة تأكل الخشب (sihah)؛ أرضت الخشبة تؤرض أرضا فهي مأروضة إذا أكلتها (sihah)؛ الأرضة الدودة التي تقع في الخشب من الأرض (mufradat)؛ أرضت الخشبة فهي مأروضة (mufradat)
- **B011** yaranın irinlenip bozulması [kalıp] — yara irinlenip kabardı ve bozuldu
  أرضت القرحة تأرض أرضا أي مجلت وفسدت بالمدة (sihah)
- **B012** doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu — görünmez varlıkların etkisine bağlanan, başını ve gövdesini istemsizce hareket ettiren kişi
  المأروض الذي به خبل من الجن وأهل الأرض وهو الذي يحرك رأسه وجسده على غير عمد (sihah)

## س ط ح (root_000703) — identity root of سُطِحَتْ (w4)

- **B001** düz üst yüzey ve yayarak düzleştirme — üstteki düz yüzey · bir şeyi yayıp uzatarak düzleştirmek · düzleştirme · çok basık burun · yayılıp uzamak ve genişlemek · yemeği kabın içine yayıp düzlemek
  أصل يدل على بسط الشيء ومده (maqayis)؛ السطح البسط (ayn)؛ سطح كل شيء أعلاه (jamhara)؛ السطح من كل شيء أعلاه؛ سطح الله الأرض سطحا بسطها؛ تسطيح القبر خلاف تسنيمه؛ أنف مسطح منبسط جدا؛ اسلنطح الشيء طال وعرض (sihah)؛ السطح ظهر البيت إذا كان مستويا (tahdhib)؛ السطح أعلى البيت؛ سطحت المكان جعلته في التسوية كسطح؛ سطحت الثريدة في القصعة بسطتها (mufradat)؛ اسلنطح الشيء إذا انبسط وعرض وإنما أصله سطح وزيدت فيه اللام والنون (maqayis-v)
- **B002** yere serme veya sırtüstü hareketsiz yatma — onları yere serdiler · yere serilmiş kişi veya ölü · adam sırtüstü uzanıp hareketsiz kaldı · bedensel engeli yüzünden yere yayılmış bir kahine verilen ad
  سطحوهم أي أضجعوهم على الأرض؛ السطيح المسطوح وهو القتيل (ayn;tahdhib)؛ انسطح الرجل إذا امتد على قفاه فلم يتحرك؛ سمي المنبسط على قفاه من الزمانة سطيحا (jamhara;maqayis)؛ السطيح المستلقي على قفاه من الزمانة (sihah)؛ سمي سطيح الكاهن لكونه منسطحا لزمانة (mufradat)
- **B003** örtüyü geren veya çardağı taşıyan sırık — çadırı geren direk · asma çardağını taşıyan enine kiriş
  المسطح عود من عيدان الخباء والفسطاط (ayn;tahdhib)؛ المسطح بكسر الميم عمود من أعمدة الخباء (jamhara;sihah)؛ المسطح عمود الخيمة الذي يجعل به لها سطحا (mufradat)؛ إنما سمي بذلك لأنه تمد الخيمة به مدا (maqayis)؛ الخشبة المعروضة تسمى المسطح (tahdhib)
- **B004** yayvan deri su kabı veya tek yanlı kap — iki deri parçasından yapılmış yayvan su tulumu · tek yanlı, yayvan kap
  المسطح والمسطحة شبه مطهرة ليست بمربعة؛ الكوز ذو الجنب الواحد مسطح (ayn;tahdhib)؛ السطيحة أديمان يتخذ منهما مزادة (jamhara)؛ السطيحة والسطيح المزادة (sihah)؛ السطيحة المزادة وإنما سميت بذلك لأنه إذا سقط انسطح (maqayis)؛ السطيحة من المزاد إذا كانت من جلدين (tahdhib)
- **B005** düz kurutma yeri, su toplayan kaya yüzü veya hasır — hurma kurutulan düz yer · suyun biriktiği geniş kaya yüzü · hurma yaprağından örülmüş hasır
  المسطح الموضع الذي يجفف ويبسط فيه التمر (jamhara;sihah;maqayis)؛ المسطح مكان مستو يجفف عليه التمر ويسمى الجرين (tahdhib)؛ المسطح الصفاة يحاط عليها بالحجارة فيجتمع فيها الماء (sihah)؛ صفيحة عريضة من الصخر يحوط عليه لماء السماء (tahdhib)؛ المسطح حصير يسف من خوص الدوم (tahdhib)
- **B006** yere yayılarak büyüyen bir ot — yere yayılarak büyüyen bir ot
  السطاح ضرب من النبت (jamhara)؛ السطاح نبت الواحد سطاحة (sihah)؛ السطاحة بقلة ترعاها الماشية ويغسل بورقها الرؤوس (tahdhib)؛ السطاح نبت من نبات الأرض وذلك أنه ينبسط على الأرض (maqayis)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:20, and ## Buluşmalar) =====
## Yüz: kurumuş toprak, yumuşamış toprak

İkinci ve sekizinci ayetler aynı iki kelimeyle başlar, "yüzler, o gün" der ve yalnızca bir sıfatta ayrılır. Birinci sıfat خاشعة'dır. Bu kelime alçalıp sinmeyi anlatır: {ar:أصل واحد يدل على التطامن, tr:aslun vâhidun yedullü ale't-tatâmün, gloss:alçalıp çökmeyi gösteren tek bir kök, source:"خ ش ع,B001"}. Araplar aynı kelimeyi toprak için de kullanır: {ar:بلدة خاشعة مغبرة, tr:beldetun hâşiatun muğberra, gloss:tozlu ve çökük bir yer, source:"خ ش ع,B002"}; {ar:إذا يبست الأرض ولم تمطر قيل قد خشعت, tr:izâ yebiseti'l-ardu ve lem tumtar kîle kad haşaat, gloss:yer kuruyup yağmur almayınca haşaat denir, source:"خ ش ع,B002"}; {ar:قف خاشع لاطئ بالأرض, tr:kuffun hâşiun lâtiun bi'l-ard, gloss:yere yapışmış alçak sırt, source:"خ ش ع,B002"}. Ayetin anlamı eğik ve ezik bir yüzdür. Yanında ise yağmur görmemiş, tozlanmış, yere yapışmış bir toprak duyulur.

Üçüncü ayet bu toprağın nasıl yorulduğunu gösterir: {ar:عَامِلَةٌۭ نَّاصِبَةٌۭ, tr:âmiletun nâsıba, gloss:çalışıp didinmiş ve bitkin, source:88:3}. Bitkinlik, ayakta durup çalışmaktan gelir: {ar:النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي, tr:en-nasabu'l-anâ ve ma'nâhu enne'l-insâne lâ yezâlü muntasiben hattâ yu'yî, gloss:yorgunluktur; insanın tükenene dek ayakta kalmasıdır, source:"ن ص ب,B004"}. Aynı kelime yüze çökmüş kederi de anlatır: {ar:الحزن إذا أثر فيه, tr:el-huznu izâ essera fîh, gloss:iz bırakan keder, source:"ن ص ب,B004"}. Beşinci ayette bu kurumuş yüz sulanır: {ar:تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:tuskâ min aynin âniye, gloss:kaynamış bir pınardan içirilir, source:88:5}. Sulamak, birine içecek vermektir: {ar:السقي والسقيا أن يعطيه ما يشرب, tr:es-sakyu ve's-sukyâ en yu'tıyehû mâ yeşrab, gloss:içecek vermek, source:"س ق ي,B001"}. Kuru toprağı diriltmesi gereken su burada yakan sudur. Toprağı canlandıran düzen tersine dönmüştür.

Kur'an kurumuş toprağın suyla dirilişini aynı kelimeyle anlatır. Allah ayetlerini sayarken şöyle der: {ar:تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:tera'l-arda hâşiaten fe-izâ enzelnâ aleyhe'l-mâe'htezzet ve rabet, gloss:yeri çökük görürsün; üstüne su indirince kıpırdar ve kabarır, source:41:39}. Aynı ayet hemen ardından {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39} der. Diriltilmekten şüphe edenlere de sahne aynı sözlerle kurulur: {ar:وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ, tr:ve tera'l-arda hâmideten, gloss:yeri kupkuru ve cansız görürsün, source:22:5}. Buradaki cansız toprak sıfatı, çökük toprağın tanımında geçen kelimedir: {ar:أرض خاشعة هامدة, tr:ardun hâşiatun hâmide, gloss:çökük ve cansız toprak, source:"خ ش ع,B002"}. Sağır edici çığlığın geldiği gün anlatılırken toz da yüzlere konar: {ar:فَإِذَا جَآءَتِ ٱلصَّآخَّةُ, tr:fe-izâ câeti's-sâhha, gloss:kulakları sağır eden geldiğinde, source:80:33}; {ar:وَوُجُوهٌۭ يَوْمَئِذٍ عَلَيْهَا غَبَرَةٌۭ, tr:ve vucûhun yevmeizin aleyhâ ğabera, gloss:o gün birtakım yüzlerin üstünde toz vardır, source:80:40}. Burada tozlu toprak ile tozlu yüz aynı resimde birleşir.

Altıncı ayetteki yiyecek, yüzün halini adında taşır. Yüzün eğikliği şöyle açıklanır: {ar:الخشوع الضراعة؛ إذا ضرع القلب خشعت الجوارح, tr:el-huşûu'd-darâa; izâ dara'a'l-kalbu haşaati'l-cevârih, gloss:huşu boyun eğmektir; kalp boyun eğince organlar da eğilir, source:"خ ش ع,B001"}. Bu açıklamadaki "boyun eğmek" kelimesi, yiyecek adı ضريع ile aynı köktendir: {ar:ضرع الرجل ضراعة إذا ذل, tr:dara'a'r-raculu darâaten izâ zell, gloss:adam alçalınca dara'a denir, source:"ض ر ع,B002"}. Aynı kök incelmiş bedeni de anlatır: {ar:لضارع الجسم أي نحيف ضعيف, tr:le-dâriu'l-cism ey nahîfun daîf, gloss:bedeni zayıf ve cılız, source:"ض ر ع,B003"}. Yiyecekle boyun eğme arasındaki bağ kök birliğinden gelir. Yüzün eğikliğine bağlanması ise kelimelerin açıklamasındandır.

Sekizinci ayette öteki sıfat gelir: {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ, tr:vucûhun yevmeizin nâime, gloss:o gün birtakım yüzler yumuşak ve mutlu, source:88:8}. Bu kelime yumuşamayı ve tazeliği anlatır: {ar:نعم الشيء صار ناعما لينا, tr:neime'ş-şey'u sâra nâimen leyyinâ, gloss:şey yumuşak ve esnek oldu, source:"ن ع م,B002"}; {ar:نعمة العيش حسنه وغضارته, tr:na'metü'l-ayşi husnühû ve ğadâratüh, gloss:yaşamın tazeliği ve güzelliği, source:"ن ع م,B002"}. Aynı kök rüzgârların en nemlisine de ad verir: {ar:النعامى ريح الجنوب لأنها أبل الرياح وأرطبها, tr:en-neâmâ rîhu'l-cenûb li-ennehâ eballü'r-riyâhi ve ertabuhâ, gloss:rüzgârların en ıslağı ve en nemlisi olan güney rüzgârı, source:"ن ع م,B009"}. Bu yüzün toprağında akan bir pınar vardır: {ar:العين الجارية النابعة من عيون الماء, tr:el-aynü'l-câriyetü'n-nâbiatü min uyûni'l-mâ', gloss:su gözelerinden kaynayıp akan pınar, source:"ع ي ن,B006"}. Dokuzuncu ayetteki hoşnutluk {ar:أصل واحد يدل على خلاف السخط, tr:aslun vâhidun yedullü alâ hılâfi's-saht, gloss:öfkenin karşıtını gösteren kök, source:"ر ض و,B001"} diye tanımlanır. On üçüncü ayetteki sedirler ise sevinçten adlandırılmıştır: {ar:السرير الذي يجلس عليه من السرور, tr:es-serîru'llezî yuclesu aleyhi mine's-surûr, gloss:üstüne oturulan sedir adını sevinçten alır, source:"س ر ر,B011"}; {ar:السرور أمر خال من الحزن, tr:es-surûru emrun hâlin mine'l-hazen, gloss:sevinç kederden boş bir haldir, source:"س ر ر,B010"}. Üçüncü ayetteki yorgunluk iz bırakan bir kederdi. Burada sedirin adı, kederden boş olan bir sevinçtir.

Yirminci ayette göz toprağın kendisine çevrilir. Arapçada iyi toprağın sıfatı yumuşaklıktır: {ar:أرض أريضة لينة طيبة, tr:ardun erîdatun leyyinatun tayyibe, gloss:yumuşak ve verimli toprak, source:"ء ر ض,B002"}. Bu, nâime'nin tanımındaki yumuşaklığın aynısıdır. Göğe verilen adlardan biri de bulut ve yağmurdur: {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tüsemmi's-sehâbe semâen ve'l-matara semâ', gloss:Araplar buluta da yağmura da gök der, source:"س م و,B004"}. Böylece göğe ve yere yöneltilen bakış, iki yüzün farkını da gösterir: yere su iner ya da inmez.

Kur'an iki yüzü başka yerlerde de aynı sözlerle karşı karşıya koyar. Güzel davrananlar için {ar:وَلَا يَرْهَقُ وُجُوهَهُمْ قَتَرٌۭ وَلَا ذِلَّةٌ, tr:ve lâ yerhaku vucûhehum katerun ve lâ zille, gloss:yüzlerini ne toz ne aşağılanma bürür, source:10:26} denir. İyilerin yüzü için {ar:تَعْرِفُ فِى وُجُوهِهِمْ نَضْرَةَ ٱلنَّعِيمِ, tr:ta'rifu fî vucûhihim nadrate'n-naîm, gloss:yüzlerinde nimetin tazeliğini tanırsın, source:83:24} denir. Burada nimet kelimesi nâime ile aynı köktendir. O günün yüzleri {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاضِرَةٌ, tr:vucûhun yevmeizin nâdıra, gloss:o gün birtakım yüzler taptaze, source:75:22} ve {ar:وَوُجُوهٌۭ يَوْمَئِذٍۭ بَاسِرَةٌۭ, tr:ve vucûhun yevmeizin bâsira, gloss:birtakım yüzler de asık, source:75:24} diye ikiye ayrılır. Sabredenlere verilen karşılık da surenin iki kelimesini bir arada söyler: {ar:وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا, tr:ve lakkâhum nadraten ve surûrâ, gloss:onlara tazelik ve sevinç kavuşturdu, source:76:11}. Üçüncü ayetteki yorgunluk bahçede ortadan kaldırılır. Pınarlı bahçelerdeki takva sahipleri için {ar:لَا يَمَسُّهُمْ فِيهَا نَصَبٌۭ, tr:lâ yemessuhum fîhâ nasab, gloss:orada onlara yorgunluk dokunmaz, source:15:48} denir. Bahçe halkı da aynı sözü kendisi söyler: {ar:لَا يَمَسُّنَا فِيهَا نَصَبٌۭ وَلَا يَمَسُّنَا فِيهَا لُغُوبٌۭ, tr:lâ yemessunâ fîhâ nasabun ve lâ yemessunâ fîhâ luğûb, gloss:burada bize ne yorgunluk dokunur ne bitkinlik, source:35:35}.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:2 خَٰشِعَةٌ خ ش ع B002; 88:3 نَّاصِبَةٌ ن ص ب B004; 88:5 تُسْقَىٰ س ق ي B001; 88:6 ضَرِيعٍ ض ر ع B002; 88:6 ضَرِيعٍ ض ر ع B003; 88:8 نَّاعِمَةٌ ن ع م B002; 88:8 نَّاعِمَةٌ ن ع م B009; 88:9 رَاضِيَةٌ ر ض و B001; 88:12 عَيْنٌ ع ي ن B006; 88:13 سُرُرٌ س ر ر B010; 88:13 سُرُرٌ س ر ر B011; 88:18 ٱلسَّمَآءِ س م و B004; 88:20 ٱلْأَرْضِ ء ر ض B002

## Alçalan ve yükselen

İkinci ayetteki yüz başını eğmiştir: {ar:أصل واحد يدل على التطامن؛ تطامن وطأطا رأسه, tr:aslun vâhidun yedullü ale't-tatâmün; tetâmene ve ta'ta'e ra'sehû, gloss:alçalmayı gösteren kök; başını eğip indirdi, source:"خ ش ع,B001"}. Yemeğinin kökü de alçalmayı anlatır: {ar:ضرع الرجل ضراعة إذا ذل, tr:dara'a'r-raculu darâaten izâ zell, gloss:adam alçalınca dara'a denir, source:"ض ر ع,B002"}. Onuncu ayette ise bahçe yüksektedir: {ar:أصل واحد يدل على السمو والارتفاع, tr:aslun vâhidun yedullü ale's-sumuvvi ve'l-irtifâ', gloss:yükseliği ve yüksekte oluşu gösteren kök, source:"ع ل و,B001"}; {ar:العلاء فالرفعة, tr:el-alâu fe'r-rif'a, gloss:alâ yüksek mertebedir, source:"ع ل و,B002"}. On üçüncü ayette sedirler kaldırılmıştır. Kaldırılmak da aşağılanmanın karşıtıdır: {ar:الرفعة نقيض الذلة, tr:er-rif'atü nakîdu'z-zille, gloss:yükseklik aşağılanmanın zıddıdır, source:"ر ف ع,B002"}. On dördüncü ayetteki "konmuş" kelimesinin kökü insanın düşük konumunu da anlatır: {ar:رجل وضيع ضد الشريف والتواضع التذلل, tr:racülün vadîun zıddü'ş-şerîf ve't-tevâdu't-tezellül, gloss:vadî şerefli olanın zıddıdır; tevazu alçalmaktır, source:"و ض ع,B005"}. Bahçede alçak konulan şey insan değildir, hizmet eden kadehlerdir. İnsan yüksek sedirde oturur.

Aynı yükseklik ve alçaklık dünyada da göze gösterilir. Gök yüksekliktir: {ar:أصل يدل على العلو؛ سموت إذا علوت, tr:aslun yedullü ale'l-uluvv; semevtü izâ alevt, gloss:yükseliği gösteren kök; yükseldiğinde semevtü dersin, source:"س م و,B001"}. Yer ise aşağıda olandır: {ar:كل شيء يسفل ويقابل السماء, tr:küllü şey'in yesfülü ve yukâbilü's-semâ', gloss:aşağıda kalıp göğün karşısında duran her şey, source:"ء ر ض,B001"}. Yirmi dördüncü ayetteki azap "en büyük" olandır: {ar:أصل صحيح يدل على خلاف الصغر, tr:aslun sahîhun yedullü alâ hılâfi's-sığar, gloss:küçüklüğün karşıtını gösteren kök, source:"ك ب ر,B001"}. İki kökün öteki yüzü de duyulur. Yükseklik kökü kibirli büyüklenmeyi de anlatır: {ar:العلو فالعظمة والتجبر, tr:el-uluvvu fe'l-azametü ve't-tecebbür, gloss:ulüv büyüklenme ve zorbalıktır, source:"ع ل و,B003"}. "En büyük" kelimesinin kökü de kendini büyük görmeyi adlandırır: {ar:الكبر العظمة وكذلك الكبرياء, tr:el-kibru'l-azametü ve kezâlike'l-kibriyâ', gloss:kibir büyüklüktür; kibriya da öyledir, source:"ك ب ر,B006"}. Bu anlamlar ayetlerdeki anlamların yanında duyulur. Bahçedeki yükseklik verilmiş bir yüksekliktir. İnsanın kendi kendine verdiği yükseklik ise öteki yüzün yolunu açar ve onu "en büyük" azapla karşılaştırır.

Kur'an kıyameti bu iki hareketle adlandırır: {ar:إِذَا وَقَعَتِ ٱلْوَاقِعَةُ, tr:izâ vekaati'l-vâkıa, gloss:olacak olan olduğunda, source:56:1}; {ar:خَافِضَةٌۭ رَّافِعَةٌ, tr:hâfidatun râfia, gloss:alçaltan ve yükselten, source:56:3}. Dünyada da yükseltme Allah'ın işidir. Müminlere meclislerde yer açmaları ve kalkmaları söylendiğinde kalkmanın karşılığı şudur: {ar:يَرْفَعِ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ مِنكُمْ, tr:yerfaillâhullezîne âmenû minkum, gloss:Allah içinizden inananları yükseltir, source:58:11}. Ateşe sunulan zalimler ise {ar:خَٰشِعِينَ مِنَ ٱلذُّلِّ, tr:hâşiîne mine'z-zull, gloss:aşağılanmadan eğilmiş, source:42:45} diye anılır. O günün gözleri için de {ar:خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ, tr:hâşiaten ebsâruhum terhakuhum zille, gloss:gözleri eğik ve kendilerini aşağılanma bürümüş, source:70:44} denir. "En büyük azap" sözü Kur'an'da bir yerde daha geçer ve orada küçüğün karşısına konur: {ar:وَلَنُذِيقَنَّهُم مِّنَ ٱلْعَذَابِ ٱلْأَدْنَىٰ دُونَ ٱلْعَذَابِ ٱلْأَكْبَرِ لَعَلَّهُمْ يَرْجِعُونَ, tr:ve le-nuzîkannehum mine'l-azâbi'l-ednâ dûne'l-azâbi'l-ekberi leallehum yerciûn, gloss:belki dönerler diye onlara en büyük azaptan önce yakın azaptan tattıracağız, source:32:21}. Alt basamak bir uyarıdır, üst basamak sonun kendisidir. Önceki surede de ateş aynı ölçüyle anılır: {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasla'n-nâre'l-kübrâ, gloss:en büyük ateşe girecek olan, source:87:12}.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:6 ضَرِيعٍ ض ر ع B002; 88:10 عَالِيَةٍ ع ل و B001; 88:10 عَالِيَةٍ ع ل و B002; 88:10 عَالِيَةٍ ع ل و B003; 88:13 مَّرْفُوعَةٌ ر ف ع B002; 88:14 مَّوْضُوعَةٌ و ض ع B005; 88:18 ٱلسَّمَآءِ س م و B001; 88:20 ٱلْأَرْضِ ء ر ض B001; 88:24 ٱلْأَكْبَرَ ك ب ر B001; 88:24 ٱلْأَكْبَرَ ك ب ر B006

## Göz: yere atılan bakış ve serbest bakış

İkinci ayetteki eğiklik önce gözdedir: {ar:الخشوع رميك ببصرك إلى الأرض, tr:el-huşûu remyüke bi-basarike ile'l-ard, gloss:huşu bakışını yere atmandır, source:"خ ش ع,B001"}; {ar:خشع ببصره إذا غضه, tr:haşaa bi-basarihî izâ ğaddah, gloss:gözünü indirdiğinde haşaa denir, source:"خ ش ع,B001"}. O gün yüz yukarı bakamaz, bakışı toprağa düşer. Kur'an bu bakışı birkaç sahnede gösterir. Mezarlardan çıkış için {ar:خُشَّعًا أَبْصَٰرُهُمْ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ, tr:huşşean ebsâruhum yahrucûne mine'l-ecdâs, gloss:gözleri eğik halde kabirlerden çıkarlar, source:54:7} denir. Sarsıntı günü için {ar:أَبْصَٰرُهَا خَٰشِعَةٌۭ, tr:ebsâruhâ hâşia, gloss:gözleri eğiktir, source:79:9} denir. Ateşe sunulan zalimler için ise eğiklik ile bakış bir arada anılır: {ar:يَنظُرُونَ مِن طَرْفٍ خَفِىٍّۢ, tr:yenzurûne min tarfin hafiyy, gloss:gizli bir göz ucuyla bakarlar, source:42:45}.

İki pınarın adı da gözdür: {ar:العين الناظرة لكل ذي بصر, tr:el-aynü'n-nâzıratü li-külli zî basar, gloss:gören her canlının bakan gözü, source:"ع ي ن,B001"}. Bu, ayetteki pınar anlamının yanında duyulur. On ikinci ayetteki pınarın suyu da göze açıktır: {ar:ماء معين أي ظاهر للعيون, tr:mâun maînun ey zâhirun li'l-uyûn, gloss:gözlere açık akan su, source:"ع ي ن,B006"}.

On yedinci ayet ise bugünün gözüne serbest bir bakış ister: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Bakmak düşünerek bakmak demektir: {ar:تأمل الشيء ومعاينته, tr:teemmülü'ş-şey'i ve muâyenetüh, gloss:bir şeyi düşünerek göz önünde tutmak, source:"ن ظ ر,B001"}; {ar:تقليب البصر والبصيرة لإدراك الشيء ورؤيته, tr:taklîbü'l-basari ve'l-basîreti li-idrâki'ş-şey'i ve ru'yetih, gloss:bir şeyi kavrayıp görmek için gözü ve gönül gözünü çevirmek, source:"ن ظ ر,B001"}. Bakmanın bir de boş kalan biçimi vardır: {ar:ينظرون إليك وهم لا يبصرون, tr:yenzurûne ileyke ve hum lâ yubsırûn, gloss:sana bakarlar ama görmezler, source:"ن ظ ر,B012"}. Ayetteki soru bu boşluğa karşı sorulur. Bakış dört yöne gönderilir: el altındaki deveye, yukarıya, karşıya ve aşağıya. Gök her yanıyla üstte olandır: {ar:السماء كل ما علاك فأظلك, tr:es-semâu küllü mâ alâke fe-ezallek, gloss:gök seni aşıp gölgeleyen her şeydir, source:"س م و,B004"}. Yer ise aşağıda kalıp göğün karşısında durandır. İkinci ayetteki bakış yere düşmüştü ve kalkamıyordu. On yedinci ayetten yirminci ayete kadar bakış her yöne serbestçe döner. Sure, o gün eğilecek gözün bugün henüz bakabildiğini hatırlatır.

Kur'an aynı soruyu başka yerlerde de sorar. Bir uyarıcıya ve toprak olduktan sonra diriltilmeye şaşanlara şöyle denir: {ar:أَفَلَمْ يَنظُرُوٓا۟ إِلَى ٱلسَّمَآءِ فَوْقَهُمْ كَيْفَ بَنَيْنَٰهَا, tr:e-fe-lem yenzurû ile's-semâi fevkahum keyfe beneynâhâ, gloss:üstlerindeki göğe bakmadılar mı onu nasıl kurduk, source:50:6}. Başka bir soru bakışı habere bağlar: {ar:أَوَلَمْ يَنظُرُوا۟ فِى مَلَكُوتِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:e-ve-lem yenzurû fî melekûti's-semâvâti ve'l-ard, gloss:göklerin ve yerin hükümranlığına bakmadılar mı, source:7:185}. Aynı ayet şöyle biter: {ar:فَبِأَىِّ حَدِيثٍۭ بَعْدَهُۥ يُؤْمِنُونَ, tr:fe-bi-eyyi hadîsin ba'dehû yu'minûn, gloss:bundan sonra hangi habere inanacaklar, source:7:185}. Dünyaya bakmak ile ilk ayetteki haber burada birleşir. Bakış diriltmeye de bağlanır: {ar:قُلْ سِيرُوا۟ فِى ٱلْأَرْضِ فَٱنظُرُوا۟ كَيْفَ بَدَأَ ٱلْخَلْقَ ۚ ثُمَّ ٱللَّهُ يُنشِئُ ٱلنَّشْأَةَ ٱلْءَاخِرَةَ, tr:kul sîrû fi'l-ardi fenzurû keyfe bedee'l-halka summallâhu yunşiu'n-neş'ete'l-âhira, gloss:de ki yeryüzünde gezin de yaratmayı nasıl başlattığına bakın; sonra Allah son yaratılışı yapacak, source:29:20}; {ar:فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ, tr:fenzur ilâ âsâri rahmetillâhi keyfe yuhyi'l-arda ba'de mevtihâ, gloss:Allah'ın rahmetinin izlerine bak; yeri ölümünden sonra nasıl diriltir, source:30:50}. Bahçede ise bakış yükseltilmiş yerlerden yapılır: {ar:عَلَى ٱلْأَرَآئِكِ يَنظُرُونَ, tr:ale'l-erâiki yenzurûn, gloss:koltuklar üstünde bakarlar, source:83:23}. Bakışın varacağı en uç yer de şudur: {ar:إِلَىٰ رَبِّهَا نَاظِرَةٌۭ, tr:ilâ rabbihâ nâzıra, gloss:Rablerine bakan, source:75:23}.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:5 عَيْنٍ ع ي ن B001; 88:12 عَيْنٌ ع ي ن B001; 88:12 عَيْنٌ ع ي ن B006; 88:17 يَنظُرُونَ ن ظ ر B001; 88:17 يَنظُرُونَ ن ظ ر B012; 88:18 ٱلسَّمَآءِ س م و B004; 88:20 ٱلْأَرْضِ ء ر ض B001

## Döşenen oda, döşenen dünya

On üçüncü ayetten on altıncıya kadar bir oda döşenir. Dört eşya vardır ve her birine yapılmış bir işi gösteren bir sıfat verilir: {ar:فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ, tr:fîhâ sururun merfûa, gloss:orada kaldırılmış sedirler, source:88:13}; {ar:وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ, tr:ve ekvâbun mevdûa, gloss:konmuş kadehler, source:88:14}; {ar:وَنَمَارِقُ مَصْفُوفَةٌۭ, tr:ve nemâriku masfûfe, gloss:sıra sıra dizilmiş yastıklar, source:88:15}; {ar:وَزَرَابِىُّ مَبْثُوثَةٌ, tr:ve zerâbiyyu mebsûse, gloss:serilmiş halılar, source:88:16}. Bunlar kaldırmak, koymak, dizmek ve sermektir. On yedinci ayetten yirminciye kadar ise dünya döşenir: dört nesne ve edilgen dört fiil gelir. Deve yaratılmış, gök kaldırılmış, dağlar dikilmiş, yer düzlenmiştir. Aynı el hareketleri hem bir odayı hem bir dünyayı kurar.

Kaldırmak iki listede de geçer. Tanımı koymayı da içinde taşır: {ar:الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها, tr:er-ref'u yukâlü fi'l-ecsâmi'l-mevdûati izâ a'leytehâ an makarrihâ, gloss:konmuş cisimleri yerlerinden yukarı aldığında ref' denir, source:"ر ف ع,B001"}. Yapı için de kullanılır: {ar:في البناء إذا طولته, tr:fi'l-binâi izâ tavveltehû, gloss:binada yükselttiğinde, source:"ر ف ع,B001"}. Gök, bir evin tavanı gibi kaldırılmıştır: {ar:السماء سقف البيت وكل عال مطل سماء, tr:es-semâu sakfu'l-beyt ve küllü âlin mutıllin semâ', gloss:sema evin tavanıdır; yüksekten bakan her şey semadır, source:"س م و,B004"}. Dağların fiili olan dikmek, kadehlerin fiili olan koymak üzerinden tanımlanır: {ar:نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر, tr:nasbu'ş-şey'i vad'uhû vad'an nâti'en ke-nasbi'r-rumhi ve'l-binâi ve'l-hacer, gloss:bir şeyi dikmek onu çıkıntılı biçimde koymaktır; mızrak bina ve taş dikmek gibi, source:"ن ص ب,B001"}. Dikmenin aslında doğruluk vardır: {ar:أصل صحيح يدل على إقامة شيء وإهداف في استواء, tr:aslun sahîhun yedullü alâ ikâmeti şey'in ve ihdâfin fi'stivâ', gloss:bir şeyi dikip düzgünce yükseltmeyi gösteren kök, source:"ن ص ب,B001"}. Dağlar yerin kazıklarıdır: {ar:اسم لكل وتد من أوتاد الأرض إذا عظم وطال, tr:ismun li-külli vetedin min evtâdi'l-ardi izâ azume ve tâl, gloss:yerin kazıklarından büyüyüp uzayan her birinin adı, source:"ج ب ل,B001"}. Yer de düz bir dam gibi yayılmıştır: {ar:سطح الله الأرض سطحا بسطها, tr:satahallâhu'l-arda sathan besatahâ, gloss:Allah yeri düzledi yani yaydı, source:"س ط ح,B001"}; {ar:السطح ظهر البيت إذا كان مستويا, tr:es-sathu zahru'l-beyti izâ kâne müsteviyen, gloss:satıh evin düz olan damıdır, source:"س ط ح,B001"}; {ar:سطحت المكان جعلته في التسوية كسطح, tr:satahtü'l-mekâne cealtühû fi't-tesviyeti ke-sath, gloss:yeri bir dam gibi düz yaptım, source:"س ط ح,B001"}. Aynı kök çadır direğine de ad verir: {ar:المسطح عمود الخيمة الذي يجعل به لها سطحا, tr:el-mistahu amûdü'l-hayme'llezî yüc'alu bihî lehâ sathan, gloss:çadıra düz bir üst veren direk, source:"س ط ح,B003"}. Bu anlam ayetin yanında duyulduğunda dünya bir çadıra benzer: yükseltilmiş bir tavanı, kazıkları ve serilmiş bir zemini vardır.

İki listeyi birbirine bağlayan kelimeler de vardır. Yastıkların dizildiği sıra düz bir çizgidir: {ar:الصف أن تجعل الشيء على خط مستو, tr:es-saffu en tec'ale'ş-şey'e alâ hattın müstevin, gloss:saf bir şeyi düz bir çizgiye koymaktır, source:"ص ف ف,B001"}. Aynı kelime düz arazi için de kullanılır: {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsafu'l-müstevî mine'l-ardi keennehû alâ saffin vâhid, gloss:tek bir saf üstündeymiş gibi düz yer, source:"ص ف ف,B005"}. Halıların serilmesini anlatan fiil, canlıların yere yayılmasını da anlatır: {ar:بثت البسط, tr:bussetil-busut, gloss:halılar serildi, source:"ب ث ث,B001"}; {ar:خلق الخلق وبثهم في الأرض, tr:halaka'l-halka ve besse-hum fi'l-ard, gloss:yaratılmışları yarattı ve yeryüzüne yaydı, source:"ب ث ث,B001"}. Bu ikinci cümlede on yedinci ayetteki yaratma ile yirminci ayetteki yer bir aradadır. Yerin kökü kalın bir halıya da ad verir: {ar:الإراض بساط ضخم من وبر أو صوف, tr:el-irâdu bisâtun dahmun min veberin ev sûf, gloss:deve tüyünden ya da yünden kalın bir yaygı, source:"ء ر ض,B005"}. Bu, on altıncı ayetteki halıların hemen yanında duyulur.

Yaratmak da bir ustanın ilk hareketidir: ölçmek. {ar:خلقت الأديم للسقاء إذا قدرته, tr:halaktü'l-edîme li's-sikâi izâ kaddertüh, gloss:deriyi tulum yapmak için ölçtüm, source:"خ ل ق,B001"}; {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhû et-takdîru'l-müstakîm, gloss:yaratmanın aslı doğru ölçüdür, source:"خ ل ق,B001"}. Aynı kök düzleştirmeyi de anlatır: {ar:صخرة خلقاء ملساء, tr:sahratun halkâu melsâ', gloss:dümdüz ve kaygan kaya, source:"خ ل ق,B008"}. Böylece dört fiilin dördü de ölçüye ve düzlüğe dayanır: doğru ölçü, düzgünce dikmek, dam gibi düzlemek ve aynı ölçünün sırası. Kur'an da yaratmayı düzenlemeyle birlikte söyler. Önceki sure {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî halaka fe-sevvâ, gloss:yaratıp düzenleyen, source:87:2} der. İnsana da şöyle seslenilir: {ar:ٱلَّذِى خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ, tr:ellezî halakake fe-sevvâke fe-adeleke, gloss:seni yaratıp düzenleyen ve dengeli kılan, source:82:7}.

Kur'an kaldırma ile koymayı yan yana koyar. Rahman nimetlerini sayarken şöyle der: {ar:وَٱلسَّمَآءَ رَفَعَهَا وَوَضَعَ ٱلْمِيزَانَ, tr:ve's-semâe rafeahâ ve vada'a'l-mîzân, gloss:göğü kaldırdı ve teraziyi koydu, source:55:7}; {ar:وَٱلْأَرْضَ وَضَعَهَا لِلْأَنَامِ, tr:ve'l-arda vada'ahâ li'l-enâm, gloss:yeri de yaratılmışlar için koydu, source:55:10}. Dirilişi inkâr edenlere sorulan soruda göğün yapısı şöyle anlatılır: {ar:رَفَعَ سَمْكَهَا فَسَوَّىٰهَا, tr:rafea semkehâ fe-sevvâhâ, gloss:tavanını yükseltip düzenledi, source:79:28}. Yerin döşenmesi de aynı resmi sürdürür: {ar:أَلَمْ نَجْعَلِ ٱلْأَرْضَ مِهَٰدًۭا, tr:e-lem nec'ali'l-arda mihâdâ, gloss:yeri bir döşek yapmadık mı, source:78:6}; {ar:وَٱلْجِبَالَ أَوْتَادًۭا, tr:ve'l-cibâle evtâdâ, gloss:dağları da kazıklar, source:78:7}; {ar:وَٱلْأَرْضَ فَرَشْنَٰهَا فَنِعْمَ ٱلْمَٰهِدُونَ, tr:ve'l-arda feraşnâhâ fe-ni'me'l-mâhidûn, gloss:yeri döşedik; ne güzel döşeyiciyiz, source:51:48}. Nuh da kavmine {ar:وَٱللَّهُ جَعَلَ لَكُمُ ٱلْأَرْضَ بِسَاطًۭا, tr:vallâhu ceale lekumu'l-arda bisâtâ, gloss:Allah yeri sizin için bir yaygı yaptı, source:71:19} der. Gök bir tavandır: {ar:وَجَعَلْنَا ٱلسَّمَآءَ سَقْفًۭا مَّحْفُوظًۭا ۖ وَهُمْ عَنْ ءَايَٰتِهَا مُعْرِضُونَ, tr:ve cealne's-semâe sakfen mahfûzan ve hum an âyâtihâ mu'ridûn, gloss:göğü korunmuş bir tavan yaptık; onlar ise onun işaretlerinden yüz çeviriyorlar, source:21:32}. Tur suresi de bir yemin olarak {ar:وَٱلسَّقْفِ ٱلْمَرْفُوعِ, tr:ve's-sakfi'l-merfû', gloss:yükseltilmiş tavana andolsun, source:52:5} der. Bu çadırın direği yoktur: {ar:ٱللَّهُ ٱلَّذِى رَفَعَ ٱلسَّمَٰوَٰتِ بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا, tr:Allâhullezî rafea's-semâvâti bi-ğayri amedin teravnehâ, gloss:gökleri görebileceğiniz direkler olmadan yükselten Allah, source:13:2}. Yayma fiili de iki yönde kullanılır: {ar:وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ, tr:ve besse fîhâ min külli dâbbe, gloss:orada her türlü canlıyı yaydı, source:31:10}. O gün ise yayılan insanlardır, halılar değil: {ar:يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ, tr:yevme yekûnu'n-nâsu ke'l-ferâşi'l-mebsûs, gloss:insanların saçılmış pervaneler gibi olacağı gün, source:101:4}. Bahçenin odası da başka yerlerde aynı kelimelerle döşenir: {ar:مُتَّكِـِٔينَ عَلَىٰ سُرُرٍۢ مَّصْفُوفَةٍۢ, tr:muttekiîne alâ sururin masfûfe, gloss:dizili sedirlere yaslanmış, source:52:20}; {ar:وَفُرُشٍۢ مَّرْفُوعَةٍ, tr:ve furuşin merfûa, gloss:yükseltilmiş döşekler, source:56:34}; {ar:إِخْوَٰنًا عَلَىٰ سُرُرٍۢ مُّتَقَٰبِلِينَ, tr:ihvânen alâ sururin mutekâbilîn, gloss:sedirler üstünde karşılıklı kardeşler olarak, source:15:47}.

Kaynaklar: 88:13 مَّرْفُوعَةٌ ر ف ع B001; 88:14 مَّوْضُوعَةٌ و ض ع B001; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:15 مَصْفُوفَةٌ ص ف ف B005; 88:16 مَبْثُوثَةٌ ب ث ث B001; 88:17 خُلِقَتْ خ ل ق B001; 88:17 خُلِقَتْ خ ل ق B008; 88:18 ٱلسَّمَآءِ س م و B004; 88:18 رُفِعَتْ ر ف ع B001; 88:19 نُصِبَتْ ن ص ب B001; 88:19 ٱلْجِبَالِ ج ب ل B001; 88:20 سُطِحَتْ س ط ح B001; 88:20 سُطِحَتْ س ط ح B003; 88:20 ٱلْأَرْضِ ء ر ض B005

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

