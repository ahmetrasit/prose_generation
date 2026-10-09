Focus: 99:1. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/99_1/D.r13/context.md =====
# 99:1 — focus

إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا

Anchor translation (canonical reading, reference only):

Yer kendi sarsıntısıyla sarsıldığında,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | إِذَا | إِذَا |  | T |
| 2 | زُلْزِلَتِ | زُلْزِلُ | ز ل ز ل | V |
| 3 | ٱلْأَرْضُ | أَرْض | ء ر ض | DET;N |
| 4 | زِلْزَالَهَا | زِلْزَال | ز ل ز ل | N;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 99 — full text (context; no pericope)

- 99:1 ◀ focus إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا
- 99:2 وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا
- 99:3 وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا
- 99:4 يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا
- 99:5 بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا
- 99:6 يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ
- 99:7 فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
- 99:8 وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ


===== _commentary/v16/work/99_1/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ز ل ز ل (root_000638) — identity root of زُلْزِلَتِ (w2)

- **B001** sarsıntılı hareket — sarsıntı · yerin sarsılması
  الزلزلة: الاضطراب أخذ من زلزلت الأرض زلزالا
- **B002** çağın ağır sıkıntıları [kalıp] — çağın ağır sıkıntıları
  زلازل الدهر: شدائده
- **B003** berrak ve kolay içimli su [kalıp] — berrak ve kolay içimli su · berrak ve kolay içimli su
  ماء زلال وزلازل إذا كان ينساغ بلا كلفة من صفائه

## ء ر ض (root_000025) — identity root of ٱلْأَرْضُ (w3)

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

===== _commentary/v16/out/s099/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 99:1, and ## Buluşmalar) =====
## Sarsılan ve yükünü dışarı atan yer

Surenin ilk iki ayeti bir nesneyi ve onun nasıl çalıştığını gösterir. Nesne yerdir: üzerinde durduğumuz, göğün karşısında aşağıda kalan gövde {ar:الأرض التي نحن عليها, tr:el-arzu’lletî nahnu aleyhâ, gloss:üzerinde bulunduğumuz yer, source:"ء ر ض,B001"}. Önce sarsılır: {ar:إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا, tr:izâ zulziletil-arzu zilzâlehâ, gloss:yer kendi sarsıntısıyla sarsıldığında, source:99:1}. Zelzele, yatışmayan çalkantıdır {ar:الزلزلة: الاضطراب, tr:ez-zelzele: el-ıdtırâb, gloss:zelzele, çalkalanmadır, source:"ز ل ز ل,B001"}; kelimenin tanımı da tam bu iki kelimeyle verilir, yerin sarsılmasıyla. Fiilin ardından gelen "kendi sarsıntısı" sarsılmanın yere ait, ona göre ölçülmüş olduğunu söyler: yer, taşıyabileceği en büyük sarsıntıyla sarsılır.

Bu kelime ailelerinden gelen imgeler, kelimenin kendi ayetindeki anlamının yanında duyulur, onun yerine geçmez; aşağıdaki bütün bölümlerde böyle okunmalıdır.

Sarsıntının işi ikinci ayette görünür: {ar:وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا, tr:ve ahracetil-arzu eskâlehâ, gloss:ve yer ağırlıklarını dışarı çıkardığında, source:99:2}. Çıkmak girmenin tersidir ve bir şeyin durduğu yerden, karargâhından belirmesidir {ar:خرج خروجا برز من مقره أو حاله, tr:harace hurûcen beraze min makarrihî ev hâlih, gloss:durduğu yerden ya da hâlinden çıkıp belirdi, source:"خ ر ج,B001"}; çıkarmak da çoğunlukla somut nesneler için söylenir {source:"خ ر ج,B002"}. Neyin çıktığını ise yerin ağırlıkları söyler: {ar:أثقال الأرض كنوزها وأجساد بني آدم, tr:eskâlul-arz künûzuhâ ve ecsâdu benî âdem, gloss:yerin ağırlıkları hazineleri ve Âdemoğullarının bedenleridir, source:"ث ق ل,B002"}. Aynı kelime yolcunun yüküne, ağırlığına da denir {source:"ث ق ل,B002"}. Yer bir kap gibi içinde ağır şeyler taşımıştır; sarsıntı onları yerinden oynatır, çıkarma onları içeriden dışarıya geçirir. Sahne, içi boşalmış ve içindekileri yüzeyine bırakmış bir yerle kapanır. Sade bir anlatım "kıyamet kopar, ölüler dirilir" der; ayetler ise ölülerin dirilişini yerin bir yükü indirmesi olarak, ağırlığın yer değiştirmesi olarak gösterir.

Yere yapışan ağırlık bu sahneye bir derinlik daha katar. Yer kelimesinden türeyen bir fiil yere yapışıp kalmayı anlatır {ar:التأرض أيضا التثاقل إلى الأرض, tr:et-teerruzu eyzan et-tesâkulu ilel-arz, gloss:yere yapışmak, yere doğru ağırlaşmaktır, source:"ء ر ض,B006"}; ağırlık kökü de yavaşlık, yere çöküş demektir {ar:المثقل البطيء والتثاقل من التباطؤ, tr:el-muskal el-batî’ ve’t-tesâkul minet-tebâtu’, gloss:ağırlaşmış olan yavaştır, ağırlaşmak ağırdan almaktır, source:"ث ق ل,B006"}. Kur’an bu ağırlaşmayı, sefere çağrılıp yerinden kıpırdamayan müminlere Allah’ın sorduğu soruda kullanır: {ar:مَا لَكُمْ إِذَا قِيلَ لَكُمُ ٱنفِرُوا۟ فِى سَبِيلِ ٱللَّهِ ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ, tr:mâ lekum izâ kîle lekumu’nfirû fî sebîlillâhi’ssâkaltum ilel-arz, gloss:size ne oluyor ki Allah yolunda sefere çıkın denince yere ağırlaşıp kaldınız, source:9:38}. Ayetlerini verdiği hâlde yere saplanan adam için de {ar:أَخْلَدَ إِلَى ٱلْأَرْضِ, tr:ahlede ilel-arz, gloss:yere saplanıp kaldı, source:7:176} denir. Surenin yeri bu yapışkan ağırlığı tutmuştur. Sarsıntı bunu tersine çevirir: aynı kelimenin bir kullanımı yerde oyalanmadan hızla kalkmayı anlatır {ar:فقام عجلان وما تأرضا, tr:fekâme acelâne ve mâ teerradâ, gloss:aceleyle kalktı, yerde oyalanmadı, source:"ء ر ض,B006"}. Bunu sağlayan, beşinci ayetteki vahyin hız anlamıdır {ar:الوحي السريع, tr:el-vahyu’s-serî’, gloss:vahy, hızlı olandır, source:"و ح ي,B006"}. Kur’an da emrin tek bir göz kırpması olduğunu söyler: {ar:وَمَآ أَمْرُنَآ إِلَّا وَٰحِدَةٌ كَلَمْحٍۭ بِٱلْبَصَرِ, tr:ve mâ emrunâ illâ vâhidetun kelemhın bil-basar, gloss:emrimiz bir tekten ibarettir, göz kırpması gibi, source:54:50}; diriliş günü de {ar:يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًا, tr:yevme teşakkakul-arzu anhum sirâan, gloss:yer üzerlerinden yarılır, hızla çıkarlar, source:50:44} diye anlatılır.

Kur’an bu sahneyi başka yerlerde de kurar. Gök yarıldığında {source:84:1} yer de uzatılır ve {ar:وَأَلْقَتْ مَا فِيهَا وَتَخَلَّتْ, tr:ve elkat mâ fîhâ ve tehallet, gloss:içindekini atar ve boşalır, source:84:4}; kaplar kabristanlar için {ar:وَإِذَا ٱلْقُبُورُ بُعْثِرَتْ, tr:ve izel-kubûru bu‘siret, gloss:kabirler altüst edildiğinde, source:82:4} denir ve nankör insana {ar:أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ, tr:efelâ ya‘lemu izâ bu‘sire mâ fil-kubûr, gloss:kabirlerdekiler altüst edilip çıkarıldığında bilmez mi, source:100:9} diye sorulur. Sarsıntının adı bu kökle Allah’ın insanlara hitabında geçer: {ar:إِنَّ زَلْزَلَةَ ٱلسَّاعَةِ شَىْءٌ عَظِيمٌ, tr:inne zelzeletes-sâati şey’un azîm, gloss:Saatin sarsıntısı büyük bir şeydir, source:22:1}. Yerin çalkalanması başka kelimelerle de söylenir {source:56:4}, {source:73:14}, {source:79:6}, {source:89:21}, {source:69:14}. Bedenlerin yerin içindeki yükler olduğunu dirilişi inkâr edenlere verilen cevap gösterir: {ar:قَدْ عَلِمْنَا مَا تَنقُصُ ٱلْأَرْضُ مِنْهُمْ, tr:kad alimnâ mâ tenkusul-arzu minhum, gloss:yerin onlardan neyi eksilttiğini biliyoruz, source:50:4}. Âdem ile eşine yeryüzüne inerken söylenen söz de yeri hem mesken hem çıkış yeri yapar: {ar:فِيهَا تَحْيَوْنَ وَفِيهَا تَمُوتُونَ وَمِنْهَا تُخْرَجُونَ, tr:fîhâ tahyevne ve fîhâ temûtûne ve minhâ tuhracûn, gloss:orada yaşarsınız, orada ölürsünüz ve oradan çıkarılırsınız, source:7:25}. Boşalan yerin son hâli de {ar:وَتَرَى ٱلْأَرْضَ بَارِزَةً, tr:ve teral-arda bârizeten, gloss:yeri çırılçıplak, ortada görürsün, source:18:47} sözüyle verilir.

Kaynaklar: 99:1 زُلْزِلَتِ ز ل ز ل B001; 99:1 زِلْزَالَهَا ز ل ز ل B001; 99:1 ٱلْأَرْضُ ء ر ض B001; 99:1 ٱلْأَرْضُ ء ر ض B006; 99:2 وَأَخْرَجَتِ خ ر ج B001; 99:2 وَأَخْرَجَتِ خ ر ج B002; 99:2 أَثْقَالَهَا ث ق ل B002; 99:2 أَثْقَالَهَا ث ق ل B006; 99:5 أَوْحَىٰ و ح ي B006

## Yükünü doğuran ağır beden

Aynı kelimeler ikinci bir sahne de kurar: içindekiyle ağırlaşan ve sonunda o yükü dışarı veren bir beden. Ağırlık kökü gebeliğin son ağırlığını adlandırır {ar:أثقلت المرأة فهي مثقل أي ثقل حملها في بطنها, tr:eskaletil-mer’etu fehiye muskil, ey sekule hamluhâ fî batnihâ, gloss:kadın ağırlaştı, yani karnındaki yükü ağırlaştı, source:"ث ق ل,B007"}. Çıkma kökü kendiliğinden dışarı itilen bir şişkinliği de anlatır {ar:الخراج ورم وقرح يخرج من ذاته, tr:el-hurâc veramun ve karhun yahrucu min zâtih, gloss:hurâc kendiliğinden çıkan şiş ve yaradır, source:"خ ر ج,B004"}, yer kelimesi de irinle şişen bir yarayı {ar:أرضت القرحة, tr:eridatil-karha, gloss:yara irinlendi, source:"ء ر ض,B011"}. Görme kökü ise taşınan yükün dışarıdan görünür hâle gelmesini adlandırır {ar:أرأت الناقة إذا أظهرت الحمل حتى يرى صدق حملها, tr:er’etin-nâka izâ azharatil-hamle hattâ yurâ sıdku hamlihâ, gloss:dişi deve gebeliğini belli etti, öyle ki gebeliğinin gerçek olduğu görülür, source:"ر ء ي,B010"}.

Bu sahnede ikinci ayetin yeri ağır bir bedendir; {ar:أَثْقَالَهَا, tr:eskâlehâ, gloss:ağırlıkları, source:99:2} karnında taşıdığı yük, {ar:وَأَخْرَجَتِ, tr:ve ahracet, gloss:ve çıkardı, source:99:2} doğumdur. Yerin taşıdığı insan bedenleri olduğuna göre bu doğumdan çıkan da insanlardır. Birinci ayetin sarsıntısı doğumdan önceki sancı gibi durur. Sonda, yedinci ve sekizinci ayetin {ar:يَرَهُۥ, tr:yerahû, gloss:onu görür, source:99:7} fiili, taşınmış olanın görünür hâle gelmesini tamamlar. Bu imge dirilişe bir zorunluluk katar: dolan bir beden doğurmadan duramaz.

Kur’an "ağırlaştı" fiilini gebelik için kendisi kullanır. Tek bir nefisten yaratılan ilk çift anlatılırken {ar:فَلَمَّآ أَثْقَلَت دَّعَوَا ٱللَّهَ رَبَّهُمَا, tr:felemmâ eskalet deavallâhe rabbehumâ, gloss:ağırlaşınca ikisi Rableri Allah’a dua ettiler, source:7:189} denir. Saatin sarsıntısı ile doğum aynı sahnede durur: insanlara hitap eden ayetin devamında o gün {ar:وَتَضَعُ كُلُّ ذَاتِ حَمْلٍ حَمْلَهَا, tr:ve teda‘u kullu zâti hamlin hamlehâ, gloss:her gebe yükünü bırakır, source:22:2}. Dirilişten şüphe edenlere hitap eden ayet rahmi ve yeri yan yana koyar: {ar:ثُمَّ نُخْرِجُكُمْ طِفْلًا, tr:summe nuhricukum tıflen, gloss:sonra sizi bir çocuk olarak çıkarırız, source:22:5}. Doğum için de aynı fiil kullanılır: {ar:وَٱللَّهُ أَخْرَجَكُم مِّنۢ بُطُونِ أُمَّهَٰتِكُمْ, tr:vallâhu ahracekum min butûni ummehâtikum, gloss:Allah sizi annelerinizin karnından çıkardı, source:16:78}. Yer ise insanların hem geldiği hem yeniden çıkacağı yerdir; Musa’nın Firavun’a cevabının ardından {ar:وَمِنْهَا نُخْرِجُكُمْ تَارَةً أُخْرَىٰ, tr:ve minhâ nuhricukum târeten uhrâ, gloss:ve sizi bir kez daha ondan çıkaracağız, source:20:55} denir. Nuh da kavmine {ar:ثُمَّ يُعِيدُكُمْ فِيهَا وَيُخْرِجُكُمْ إِخْرَاجًا, tr:summe yuîdukum fîhâ ve yuhricukum ihrâcen, gloss:sonra sizi oraya döndürür ve sizi bir çıkarışla çıkarır, source:71:18} der.

Kaynaklar: 99:2 أَثْقَالَهَا ث ق ل B007; 99:2 أَثْقَالَهَا ث ق ل B002; 99:2 وَأَخْرَجَتِ خ ر ج B001; 99:2 وَأَخْرَجَتِ خ ر ج B004; 99:1 ٱلْأَرْضُ ء ر ض B011; 99:7 يَرَهُۥ ر ء ي B010

## Yerden bedene geçen sarsıntı

Sarsıntı yerde kalmaz. Yer kelimesi bir bedenin titremesini de adlandırır {ar:الأرض الرعدة, tr:el-arzu er-ri‘de, gloss:arz, titremedir, source:"ء ر ض,B008"}; birinde {ar:بفلان أرض, tr:bi-fulânin arz, gloss:falancada titreme var, source:"ء ر ض,B008"} denir. Aynı kelimeyle başını ve gövdesini istemeden sarsan kişi de anılır {ar:الذي يحرك رأسه وجسده على غير عمد, tr:ellezî yuharriku re’sehû ve ceseduhû alâ gayri amd, gloss:başını ve bedenini istemeden oynatan, source:"ء ر ض,B012"}. Zelzele kökü de zamanın sıkıntılarına uzanır {ar:زلازل الدهر: شدائده, tr:zelâzilud-dehr: şedâiduh, gloss:zamanın zelzeleleri onun sıkıntılarıdır, source:"ز ل ز ل,B002"}; dördüncü ayetin fiilinin kökü de başa inen olayı, felaketi adlandırır {ar:الحادثة النازلة العارضة, tr:el-hâdisetu en-nâziletu el-ârıda, gloss:hadise, inip gelen musibettir, source:"ح د ث,B005"}.

Bu imgede birinci ayetteki sarsıntı, yerin üstünde duranın bedenine geçen tek bir titremedir. Üçüncü ayet etkisini gösterir: {ar:وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا, tr:ve kâlel-insânu mâ lehâ, gloss:ve insan "ona ne oluyor" der, source:99:3}. Söz, konuşmanın dile gelmesidir {ar:القول من النطق, tr:el-kavlu minen-nutk, gloss:söz konuşmadandır, source:"ق و ل,B001"}; burada sarsılmış insanın ağzından çıkan kısa bir soru. Soru iki kelimedir ve cevabı yoktur; yer ayağının altında oynarken insan yalnızca "ona ne oluyor" diyebilir.

Kur’an sarsıntıyı insanlar için de kullanır. Saatin sarsıntısının ardından {ar:وَتَرَى ٱلنَّاسَ سُكَٰرَىٰ وَمَا هُم بِسُكَٰرَىٰ, tr:ve teran-nâse sukârâ ve mâ hum bisukârâ, gloss:insanları sarhoş görürsün, oysa sarhoş değillerdir, source:22:2}: yerin sarsıntısı insanların sendelemesinde görünür. Önceki toplulukları müminlere anlatan ayette {ar:وَزُلْزِلُوا۟ حَتَّىٰ يَقُولَ ٱلرَّسُولُ, tr:ve zulzilû hattâ yekûler-resûl, gloss:öyle sarsıldılar ki elçi şöyle dedi, source:2:214}; burada da sarsıntı bir sözle, bir çığlıkla biter. Kuşatma anlatılırken surenin aynı ikilisi insanlara uygulanır: {ar:وَزُلْزِلُوا۟ زِلْزَالًا شَدِيدًا, tr:ve zulzilû zilzâlen şedîdâ, gloss:ve şiddetli bir sarsıntıyla sarsıldılar, source:33:11}. Saatte insanın sorusu da aynı biçimdedir: {ar:يَقُولُ ٱلْإِنسَٰنُ يَوْمَئِذٍ أَيْنَ ٱلْمَفَرُّ, tr:yekûlul-insânu yevmeizin eynel-mefer, gloss:insan o gün "kaçacak yer nerede" der, source:75:10}; kabirlerinden kalkanlar da {ar:يَٰوَيْلَنَا مَنۢ بَعَثَنَا مِن مَّرْقَدِنَا, tr:yâ veylenâ men beasenâ min merkadinâ, gloss:vay bize, bizi yattığımız yerden kim kaldırdı, source:36:52} diye sorar.

Kaynaklar: 99:1 ٱلْأَرْضُ ء ر ض B008; 99:1 ٱلْأَرْضُ ء ر ض B012; 99:1 زِلْزَالَهَا ز ل ز ل B001; 99:1 زِلْزَالَهَا ز ل ز ل B002; 99:4 تُحَدِّثُ ح د ث B005; 99:3 وَقَالَ ق و ل B001

## Toprağın, bulutun ve suyun çıkardığı bitki

Kur’an dirilişi sürekli olarak yerden bitki çıkmasına benzetir: yağmur yağar, toprak kıpırdar ve kabarır, bitki çıkarılır, "işte siz de böyle çıkarılacaksınız". Surenin kelimeleri bu dizinin parçalarını kendi anlamlarında taşır. Yer, bitkinin kök saldığı yumuşak, verimli topraktır {ar:أرض أريضة لينة طيبة, tr:arzun erîdatun leyyinetun tayyibe, gloss:yumuşak, iyi, verimli toprak, source:"ء ر ض,B002"}. Çıkma kökü yerin bitkisini yer yer çıkarmasını {ar:أرض مخرجة نبتها في مكان دون مكان, tr:arzun muharracetun nebtuhâ fî mekânin dûne mekân, gloss:bitkisi bir yerde çıkıp bir yerde çıkmayan toprak, source:"خ ر ج,B007"}, ürünü {ar:الخراج الغلة, tr:el-harâcu el-galle, gloss:harac üründür, source:"خ ر ج,B003"} ve bulutun ilk belirişini {source:"خ ر ج,B005"} adlandırır. Haber kökü yağmur suyunu toplayan alçak, yumuşak toprağı {ar:الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء, tr:el-habrâ’ el-arzus-sehletul-munhafidatu yecteme‘u fîhâ mâus-semâ’, gloss:gök suyunun toplandığı alçak, düz toprak, source:"خ ب ر,B002"}, çiftçiyi ve yerden çıkanın bir kısmı karşılığında ortakçılığı {ar:المزارعة ببعض ما يخرج من الأرض, tr:el-muzâraa bi-ba‘dı mâ yahrucu minel-arz, gloss:yerden çıkanın bir kısmı karşılığında ortakçılık, source:"خ ب ر,B003"} ve körpe bitkiyi {source:"خ ب ر,B005"} adlandırır. Rab kökü üst üste binmiş bulutu, bitkiyi büyüttüğü için verilen adla anar {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb: es-sehâb, summiye bi-zâlike li-ennehû yerubbun-nebât, gloss:rabâb buluttur, bitkiyi büyüttüğü için böyle adlandırılmıştır, source:"ر ب ب,B008"}; terbiye de bir şeyi hâlden hâle tamamlanmaya kadar yetiştirmektir {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve huve inşâuş-şey’i hâlen fe-hâlen ilâ haddit-temâm, gloss:terbiye, bir şeyi hâlden hâle tamamına kadar geliştirmektir, source:"ر ب ب,B002"}; çok ve toplanmış su da bu köktendir {source:"ر ب ب,B013"}. Zerre kökü de toprağı yarıp çıkan filizi adlandırır {ar:ذر البقل إذا طلع من الأرض, tr:zerral-baklu izâ tala‘a minel-arz, gloss:sebze yerden baş verdiğinde "zerra" denir, source:"ذ ر ر,B004"}.

Bu imgede birinci ve ikinci ayetin yeri bir tarladır; çıkarması onun ürünüdür. Beşinci ayetteki Rab, kelimenin anlamında efendi ve sahiptir; yanında, bitkiyi aşama aşama büyüten bulutun adı da duyulur. Diriliş korkunç bir yıkım olduğu kadar tanıdık bir yetişmedir.

Kur’an üç imgeyi tek ayette birleştirir: rüzgârlar {ar:حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًا ثِقَالًا سُقْنَٰهُ لِبَلَدٍ مَّيِّتٍ فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ, tr:hattâ izâ ekallet sehâben sikâlen suknâhu li-beledin meyyitin fe-enzelnâ bihil-mâe fe-ahracnâ bihî min kullis-semerât, kezâlike nuhricul-mevtâ, gloss:ağır bulutları yüklendiklerinde onu ölü bir beldeye süreriz, oraya suyu indirir, onunla her türlü meyveyi çıkarırız; ölüleri de böyle çıkarırız, source:7:57}. Ağır bulut, çıkarılan meyve ve çıkarılan ölüler burada yan yanadır. Dirilişten şüphe edenlere gösterilen yer önce kupkurudur, su inince {ar:ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ, tr:ihtezzet ve rabet ve enbetet, gloss:titredi, kabardı ve bitirdi, source:22:5}; aynı söz Allah’ın ayetleri arasında da geçer ve {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰ, tr:innellezî ahyâhâ le-muhyil-mevtâ, gloss:onu dirilten elbette ölüleri de diriltir, source:41:39} sözüyle tamamlanır. Bulut sürülür ve yer diriltilir: {ar:كَذَٰلِكَ ٱلنُّشُورُ, tr:kezâliken-nuşûr, gloss:diriliş de böyledir, source:35:9}; dirilişi inkâr edenlere verilen cevapta {ar:كَذَٰلِكَ ٱلْخُرُوجُ, tr:kezâlikel-hurûc, gloss:çıkış da böyledir, source:50:11}; ve {ar:كَذَٰلِكَ تُخْرَجُونَ, tr:kezâlike tuhracûn, gloss:siz de böyle çıkarılırsınız, source:43:11}, {source:30:19}. Çıkarma fiili bitki için tekrar tekrar kullanılır {source:6:99}; yer de kendi suyunu ve otlağını verir {ar:أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا, tr:ahrace minhâ mâehâ ve mer‘âhâ, gloss:ondan suyunu ve otlağını çıkardı, source:79:31}; Rabbin övüldüğü surede de {ar:وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ, tr:vellezî ahracel-mer‘â, gloss:otlağı çıkaran, source:87:4} denir. Nuh da insanları yerin bitkisi olarak anar: {ar:وَٱللَّهُ أَنۢبَتَكُم مِّنَ ٱلْأَرْضِ نَبَاتًا, tr:vallâhu enbetekum minel-ardı nebâtâ, gloss:Allah sizi yerden bir bitki gibi bitirdi, source:71:17}.

Kaynaklar: 99:1 ٱلْأَرْضُ ء ر ض B002; 99:2 وَأَخْرَجَتِ خ ر ج B007; 99:2 وَأَخْرَجَتِ خ ر ج B003; 99:2 وَأَخْرَجَتِ خ ر ج B005; 99:4 أَخْبَارَهَا خ ب ر B002; 99:4 أَخْبَارَهَا خ ب ر B003; 99:4 أَخْبَارَهَا خ ب ر B005; 99:5 رَبَّكَ ر ب ب B008; 99:5 رَبَّكَ ر ب ب B002; 99:5 رَبَّكَ ر ب ب B013; 99:7 ذَرَّةٍ ذ ر ر B004

## Buluşmalar

Surenin hareketi bir yönden ötekine geçer: içeriden dışarıya, ağırdan hafife, büyükten küçüğe, sessizden konuşana, gizliden görünene. İmgeler bu hareketin farklı yüzlerini taşır ve birkaç sahnede üst üste biner.

İlk buluşma yerin boşalmasıyla doğumdur. İkinci ayetin iki kelimesi, {ar:وَأَخْرَجَتِ, tr:ve ahracet, gloss:ve çıkardı, source:99:2} ile {ar:أَثْقَالَهَا, tr:eskâlehâ, gloss:ağırlıkları, source:99:2}, hem gömülü yükü atan yeri hem doğuran bedeni anlatır. Kur’an bu iki sahneyi aynı ayetlerde tutar: Saatin sarsıntısı {source:22:1} ve her gebenin yükünü bırakması {source:22:2}; rahimden çocuğu çıkarmak ve suyla titreyip kabaran toprak {source:22:5}. Aynı ayet bitki imgesini de içerir; böylece boşalan yer, doğuran beden ve filiz veren tarla tek bir dirilişin üç görünüşü olur. Ağır bulutlarla meyveyi ve ölüleri çıkaran ayet {source:7:57} ağırlık imgesini de bu sahneye bağlar.

İkinci buluşma boşalan yerle konuşan yerdir. İnşikak suresinde sıra surenin sırasıyla aynıdır: yer içindekini atar ve boşalır {source:84:4}, sonra Rabbine kulak verir {source:84:5}. İkinci ayette yer yükünü çıkarır, beşinci ayette Rabbinin vahyini alır. Arada üçüncü ayetin sarsılmış insanı vardır: sarsıntı bedenine geçmiş, ağzından {ar:مَا لَهَا, tr:mâ lehâ, gloss:ona ne oluyor, source:99:3} sorusu çıkmıştır. Bu soru, sarsıntı imgesini konuşma imgesine bağlar; çünkü yer ona cevap verecektir. Suçluların kitabın önündeki sorusu {source:18:49} aynı biçimdedir ve ardından yaptıklarını hazır bulurlar: soru, haber ve görme bir sahnede toplanır.

Üçüncü buluşma konuşmayla göstermedir. Dördüncü ayette yerin anlattığı haber, işin içyüzüdür; anlatmak açığa vurmak, kılıcı parlatmaktır. Yerin içindekilerini çıkarması ile haberlerini anlatması aynı işlemdir: içeride olanın dışarı verilmesi. Kur’an bu iki çıkarışı yan yana koyar: kabirlerdeki altüst edilir ve göğüslerdeki ortaya dökülür {source:100:9}, {source:100:10}; kıyamet günü kitap çıkarılır ve açılmış bulunur {source:17:13}.

Dördüncü buluşma altıncı ayetin kendisidir. Sudan dönen kalabalık bir yöne yürür ve ayet varış yerini söyler: {ar:لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:li-yurav a‘mâlehum, gloss:amelleri kendilerine gösterilsin diye, source:99:6}. Yolun sonunda tutulan ayna vardır. Aynı kalabalık bölüklere serpilir ve zerre imgesi başlar; bölükler arasındaki uzaklık da iki payın imgesini açar. Bir kelime, {ar:أَشْتَاتًا, tr:eştâtâ, gloss:bölük bölük, source:99:6}, üç imgeyi birden taşır: sudan dönüş, serpilme ve ak ile kara kadar uzak iki pay.

Son buluşma zerrede olur. {ar:ذَرَّةٍ, tr:zerratin, gloss:zerre, source:99:8} hem serpilmenin en küçük birimidir hem terazideki en küçük ağırlık; kötülük sözünün yanında ateşten kopan kıvılcım, toprağı yarıp çıkan filiz ve güneşte yayılan ince ışık da duyulur. Ağırlık kökü burada çemberi kapatır: sure yerin bütün ağırlıklarıyla açılmış, aynı kökten bir miskalle biter. Lokman’ın oğluna söylediği söz {source:31:16} bu iki ucu birleştirir: yerin içinde gizli bir küçük ağırlık getirilir ve sözü {ar:إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌ, tr:innallâhe latîfun habîr, gloss:Allah en ince şeyi bilen, her şeyden haberdardır, source:31:16} diye biter. Haber kökü burada da durur: yerin anlattığı haberler, her şeyden haberdar olanın bildiğidir. Yer ağırlıklarını verir, haberlerini anlatır; insan da tek tek, en küçük ağırlığına kadar amelini görür.

