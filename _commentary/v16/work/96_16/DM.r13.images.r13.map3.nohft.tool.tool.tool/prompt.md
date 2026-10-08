Focus: 96:16. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/96_16/D.r13/context.md =====
# 96:16 — focus

نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ

Anchor translation (canonical reading, reference only):

Yalancı, günahkâr bir perçemden.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | نَاصِيَةٍ | نَاصِيَة | ن ص ي | N |
| 2 | كَٰذِبَةٍ | كَٰذِب | ك ذ ب | ADJ |
| 3 | خَاطِئَةٍ | خَاطِئَة | خ ط ء | ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 96 — full text (context; no pericope)

- 96:1 ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ
- 96:2 خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
- 96:3 ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ
- 96:4 ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ
- 96:5 عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ
- 96:6 كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ
- 96:7 أَن رَّءَاهُ ٱسْتَغْنَىٰٓ
- 96:8 إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ
- 96:9 أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ
- 96:10 عَبْدًا إِذَا صَلَّىٰٓ
- 96:11 أَرَءَيْتَ إِن كَانَ عَلَى ٱلْهُدَىٰٓ
- 96:12 أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ
- 96:13 أَرَءَيْتَ إِن كَذَّبَ وَتَوَلَّىٰٓ
- 96:14 أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ
- 96:15 كَلَّا لَئِن لَّمْ يَنتَهِ لَنَسْفَعًۢا بِٱلنَّاصِيَةِ
- 96:16 ◀ focus نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ
- 96:17 فَلْيَدْعُ نَادِيَهُۥ
- 96:18 سَنَدْعُ ٱلزَّبَانِيَةَ
- 96:19 كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩


===== _commentary/v16/work/96_16/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن ص ي (root_001512) — identity root of نَاصِيَةٍ (w1)

- **B001** alın saç çizgisi; buradan tutup çekme ve denetim altına alma — alındaki saç çizgisi ya da ön saçın çıktığı yer · birini ön saçından tutmak veya çekmek · karşılıklı olarak ön saçlarından tutup çekişmek · alındaki saç çizgisi için bölgesel bir söyleyiş · ön saçlardan tutma · onu denetimi altında tutan ve üzerinde söz sahibi olan
  الناصية قصاص الشعر (maqayis;ayn;sihah;mufradat)؛ الناصية منبت الشعر في مقدم الرأس (tahdhib)؛ نصوته قبضت على ناصيته ومددتها (maqayis;ayn;sihah;tahdhib;mufradat)؛ ناصيته أخذ كل واحد بناصية صاحبه (maqayis;ayn;tahdhib;mufradat)؛ آخذ بناصيتها أي متمكن منها (mufradat)
- **B002** saçı tarama, saçın uzaması ve ölünün ön saçını çekip uzatma — saçın uzaması · ölünün başı hazırlanırken ön saçını çekip uzatmak · kadının saçını tarayıp düzene sokması · saçını tarayıp düzene sokmak
  تنصت المرأة إذا رجلت شعرها (sihah;tahdhib)؛ أن تنصى أي تسرح شعرها (tahdhib)؛ انتصى الشعر طال (maqayis;sihah;mufradat)؛ تنصون ميتكم أي تمدون ناصيته (maqayis;sihah;tahdhib;mufradat)
- **B003** seçkin kesim, en iyiyi seçme ve önde gelme — bir topluluğun ya da şeyin en iyi kesimi; kimi bağlamda geride kalan bölüm · bir şeyin en iyisini seçip almak · insanların önde gelenleri ve seçkinleri · bir topluluğun en yüksek konumdaki kesiminden evlenmek · topluluğunun önderi ve en seçkin kişisi · önden gidenler
  النصية من القوم ومن كل شيء الخيار (maqayis;sihah)؛ انتصيت الشيء اخترته (maqayis;sihah)؛ نخبة الناس وخيارهم هم نصية انتصوا (ayn)؛ نواصي الناس أشرافهم والنصية الخيار الأشراف (sihah;tahdhib)؛ النصية البقية (sihah;tahdhib)؛ الأنصاء السابقون (tahdhib)؛ فلان ناصية قومه وفلان نصية قوم أي خيارهم (mufradat)؛ تنصيتهم إذا تزوجت في الذروة منهم والناصية (sihah)
- **B004** tazeyken değerli bir otlak bitkisi — tazeyken değerli bir otlak bitkisi · o bitkinin bir arazide çokça yetişmesi
  النصي نبات من أفضل المراعي (ayn;mufradat)؛ النصى نبت ما دام رطبا فإذا ابيض فهو الطريفة وإذا ضخم ويبس فهو الحلي (sihah)؛ النصي نبت معروف ما دام رطبا فإذا يبس فهو حلي (tahdhib)؛ أنصت الأرض أي كثر نصيها (sihah)
- **B005** bir çöl düzlüğünün başka bir çöl düzlüğüne bitişmesi — bir çöl düzlüğünün başka bir çöl düzlüğüne, onun önünü kavrar gibi bitişmesi
  مفازة تناصي أخرى كأنها تتصل بها كالقابضة على ناصيتها (maqayis)؛ مفازة تناصي مفازة إذا كانت الأولى متصلة بالأخرى (ayn)؛ فلاة تناصي فلاة أي تتصل بها (sihah;tahdhib)؛ تناصي أرض كذا وتواصيها أي تتصل بها (tahdhib)
- **B006** karında batıcı, huzursuz eden sancı — karında duyulan, kişiyi rahat duramaz hale getiren batıcı sancı
  أجد في بطني نصوا ووخزا (tahdhib)؛ النصو مثل المفس سمي نصوا لأنه ينصوك أي يزعجك عن القرار (tahdhib)؛ وجدت في بطني حصوا ونصوا وقبصا بمعنى واحد (tahdhib)

## ك ذ ب (root_001290) — identity root of كَٰذِبَةٍ (w2)

- **B001** sözde veya davranışta doğruluğa aykırılık — sözde veya davranışta doğruluğa aykırılık; yalan · yalancı; çok yalan söyleyen kişi · uydurma söz; yalanlar · özürlere kaçınılmaz olarak yalan karışır
  الكذب خلاف الصدق (maqayis;jamhara); الكذاب لغة في الكذب (ayn); كذب كذبا فهو كاذب وكذاب وكذوب (sihah); يقال في المقال والفعال (mufradat)
- **B002** yalan sayma veya yalancı bulma — yalanlama; yalan sayma · birini yalancı saymak veya ona yalan söylediğini bildirmek · birini yalancı bulmak veya yalanını ortaya çıkarmak · seni yalancı saymıyorum
  كذبت فلانا نسبته إلى الكذب وأكذبته وجدته كاذبا (maqayis); كذبته جعلته كاذبا (ayn); كذبت بالحديث كذابا وتكذيبا (jamhara); أكذبت الرجل ألفيته كاذبا وكذبته إذا قلت له كذبت (sihah); كذبته نسبته إلى الكذب (mufradat)
- **B003** onu üstlen; sana düşer [kalıp] — şunu üstlen; sana düşer veya onu yapmalısın
  كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك (maqayis); كذب عليكم الحج أي وجب عليكم ودونكم الحج (ayn); كذب عليك كذا وكذا في معنى الإغراء (jamhara); كذب عليكم الحج أي وجب (sihah); كذب عليك الحج قيل معناه وجب فعليك به (mufradat)
- **B004** hamlede duraksamak; olumsuzda sonuna kadar ilerlemek [kalıp] — saldırıya geçti ama duraksadı veya korktu · saldırıya geçti ve vuruncaya kadar durmadı; korkmadı
  حمل فلان ثم كذب أي لم يصدق في الحملة (maqayis); حمل فلان على فلان فما كذب حتى طعن أو ضرب أي ما وقف (jamhara); حمل فلان فما كذب أي ما جبن (sihah); حمل فلان على قرنه فكذب (mufradat)
- **B005** gecikmeden yapmak [kalıp] — yapmakta gecikmedi; hemen yaptı
  ما كذب فلان أن فعل كذا أي ما لبث (maqayis;sihah)
- **B006** sütün kesilmesi veya beklenenden önce tükenmesi [kalıp] — dişi devenin sütü kesildi veya umulduğu kadar sürmedi
  كذب لبن الناقة ذهب وفيه نظر وقياسه صحيح (maqayis); كذب لبن الناقة أي ذهب (sihah); كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم (mufradat)
- **B007** koşup arkasına bakmak için durmak [kalıp] — yaban hayvanı bir mesafe koşup arkasına bakmak için durdu
  كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه (jamhara)
- **B008** iç benlik — iç benlik; kişinin kendisi
  الكذوب النفس (jamhara)
- **B009** dokuma bezemesi sanısı veren boyalı kumaş — dokuma bezemesi sanısı veren boyalı veya desenli kumaş
  الكذابة ثوب يصبغ بألوان الصبغ كأنه موشي (ayn); الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله (mufradat)

## خ ط ء (root_000420) — identity root of خَاطِئَةٍ (w3)

- **B001** istemeden doğruyu tutturamama — istemeden yapılan yanlış; doğruyu tutturamama · yanılmak; doğruyu tutturamamak · yanılmak; amaçlanan sonucu elde edememek · yanılmak; yanlış yapmak · doğruyu amaçlayıp yanılan kimse · yanlış yaptığını söylemek; yanlış bulmak · ıskalamak; değmemek · kötülük senden uzak olsun · çok yanılan da bazen doğruyu bulur
  أخطأ إذا لم يصب الصواب؛ الخطأ ما لم يتعمد؛ خطأته تخطئة (ayn)؛ الخطأ نقيض الصواب؛ المخطئ من أراد الصواب فصار إلى غيره؛ خطأته تخطئة وتخطيئا (sihah)؛ أخطأ إذا لم يصب الصواب؛ أخطأت لما صنعه خطأ غير عمد؛ خطىء عنك السوء إذا دعوا له أن يدفع عنه السوء (tahdhib)؛ الخطأ العدول عن الجهة؛ يقع منه خلاف ما يريد؛ أصاب الخطأ وأخطأ الصواب (mufradat)؛ الخطاء مجاوزة حد الصواب؛ أخطأ إذا تعدى الصواب (maqayis)
- **B002** bilerek işlenen günah — sorumluluk doğuran günah · günah; suç · günah işlemek · hesabı sorulan günah veya kötü eylem · günahı bilerek işleyen kimse; günahkâr · büyük günah · günahlar · ne büyük günah işledi!
  الخطء الذنب؛ خطئ يخطأ خطأ وخطأة؛ الخطيئة (sihah)؛ خطئت إذا أثمت؛ خاطئين أي آثمين؛ خطئت لما صنعه عمدا وهو الذنب؛ الخطيئة الذنب على عمد (tahdhib)؛ الخطأ التام المأخوذ به الإنسان؛ الخطيئة والسيئة يتقاربان؛ الخاطئ هو القاصد للذنب؛ الذنب العظيم (mufradat)؛ خطئ يخطأ إذا أذنب (maqayis)
- **B003** yağmurun atladığı arazi — yağmurun atladığı arazi · iki yağışlı arazi arasında yağışsız kalan yer · oraya yağmur yağmasın
  الخطيئة أرض يخطئها المطر ويصيب غيرها (ayn)؛ الأرض الخطيطة هي التي لم تمطر بين أرضين ممطورتين؛ من أخطأ كأن المطر أخطأها؛ خطأ الله نوءها (maqayis)

===== _commentary/v16/out/s096/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 96:16, and ## Buluşmalar) =====
## Su: bulut, yağmur, taşkın ve gölet

Bu sahne suyun bütün yolculuğunu izler. Bulut yağmur getirir, ilk yağmur yeri bitkiyle işaretler, ardından ikinci yağmur gelir, yağmur döne döne yağar. Bazı yerler ise atlanır. Su bazen ölçüsünü aşar, taşar ve her şeyi sürükler, sonra yolunun sonundaki gölete varır ve orada durulur.

Üçüncü ayetteki en cömert sıfatının ailesinde yağmur getiren bulut ve verimli toprak vardır: {ar:كرم السحاب أتى بالغيث, tr:kerume's-sehâb, gloss:bulut cömert oldu, yani yağmur getirdi, source:"ك ر م,B002"}; {ar:أرض مكرمة للنبات, tr:ardun mekrame li'n-nebât, gloss:bitkiye cömert toprak, source:"ك ر م,B002"}. Rab kelimesinin ailesinde bitkileri büyüten bulut vardır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb, gloss:rabâb buluttur; bitkiyi büyüttüğü için böyle adlandırılmıştır, source:"ر ب ب,B008"}. Bu, rahimdeki cenini aşama aşama büyüten aynı terbiye işidir. Kayıtlı bir türetmeye göre ad kelimesinin ailesinde de yılın ilk yağmuru vardır: {ar:الوسمي أول مطر السنة يسم الأرض بالنبات, tr:el-vesmiyyu evvelu matari's-sene, gloss:vesmî, yeri bitkiyle işaretleyen yılın ilk yağmurudur, source:"و س م,B003"}. On üçüncü ayetteki {ar:وَتَوَلَّىٰٓ, tr:ve tevellâ, gloss:ve yüz çevirdi, source:96:13} fiilinin kökünde bu yağmuru izleyen yağmur bulunur: {ar:الولي المطر يجيء بعد الوسمي سمي بذلك لأنه يلي الوسمي, tr:el-veliyy el-matar yecî'u baʿde'l-vesmî, gloss:veliy, vesmîden sonra gelen yağmurdur; onu izlediği için böyle denir, source:"و ل ي,B010"}. Bu iki aile anlamı birer yankıdır; ayetlerdeki anlamlar "ad" ve "yüz çevirme"dir. Sekizinci ayetteki dönüş kelimesinin ailesinde ise dönüp duran yağmur vardır: {ar:الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث, tr:er-recʿu'l-gays, gloss:rec yağmurdur, çünkü yağar, sonra döner ve tekrar yağar, source:"ر ج ع,B006"}. Kurân göğe bu sıfatla yemin eder: {ar:وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ, tr:ve's-semâ'i zâti'r-recʿ, gloss:dönüp dönüp yağmur veren göğe andolsun, source:86:11}. On yedinci ayetin {ar:نَادِيَهُۥ, tr:nâdiyeh, gloss:meclisini, source:96:17} kelimesinin ailesinde nem ve cömertlik vardır: {ar:يعبر عن السخاء بالندى, tr:yuʿabbaru ʿani's-sehâ'i bi'n-nedâ, gloss:cömertlik "nem" ile ifade edilir, source:"ن د و,B004"}. On altıncı ayetin {ar:خَاطِئَةٍ, tr:hâti'e, gloss:günahkâr, source:96:16} kelimesinin ailesinde ise yağmurun atladığı toprak vardır: {ar:الخطيئة أرض يخطئها المطر ويصيب غيرها, tr:el-hatî'e ardun yuhti'uha'l-matar, gloss:hatîe, yağmurun ıskalayıp başka yere düştüğü topraktır, source:"خ ط ء,B003"}.

Kurân rahim ile yağmuru tek ayette birleştirir. Rahimdeki aşamalardan sonra {ar:وَتَرَى ٱلْأَرْضَ هَامِدَةً فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:ve tera'l-arda hâmideten fe izâ enzelnâ ʿaleyhe'l-mâ'e'htezzet ve rabet, gloss:yeri kupkuru görürsün; üzerine suyu indirince harekete geçer ve kabarır, source:22:5} denir. Bu ayet canlanmayı yaratılışla aynı kanıta bağlar. Dünya hayatı da yağmurla büyüyüp biçilen bir ekin olarak anlatılır: {ar:كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:keen lem tegne bi'l-ems, gloss:sanki dün orada hiç yokmuş gibi, source:10:24}. Bu ifadede, yedinci ayetin yeterlilik köküyle aynı kökten bir fiil, yerleşik yaşamın bir gecede silinmesini anlatır.

Su ölçüsünü de aşabilir. Altıncı ayetin azma fiili için {ar:طغى الماء خروجه عن المقدار, tr:tagâ'l-mâ' hurûcuhû ʿani'l-mikdâr, gloss:suyun azması ölçüsünden çıkmasıdır, source:"ط غ ي,B002"} ve {ar:طغا البحر والماء إذا علا كل شيء فاجترفه, tr:tagâ'l-bahru ve'l-mâ', gloss:deniz ve su her şeyin üstüne çıkıp onu sürükledi, source:"ط غ ي,B002"} denir. Kök genel olarak ölçüyü aşmaktır: {ar:كل شيء جاوز القدر فقد طغا, tr:kullu şey'in câveze'l-kadr fe kad tagâ, gloss:ölçüyü aşan her şey azmıştır, source:"ط غ ي,B001"}. Kurân bunu Nuh'un tufanı için kullanır: {ar:إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ, tr:innâ lemmâ tage'l-mâ'u hamelnâkum fi'l-câriye, gloss:su taştığında sizi akan gemide taşıdık, source:69:11}. Kuralı da teraziyle birlikte koyar: {ar:أَلَّا تَطْغَوْا۟ فِى ٱلْمِيزَانِ, tr:ellâ tatgav fi'l-mîzân, gloss:ölçüde aşırı gitmeyesiniz diye, source:55:8}. Böylece azma, yaratmanın ölçüsünün karşısına konur.

Taşkının sonu gölettir. On beşinci ayetin vazgeçme fiilinin ailesinde şu anlamlar bulunur: {ar:النهي والنهي الغدير لأن الماء ينتهي إليه, tr:en-nehy, el-gadîr, gloss:nehy göllenmiş sudur, çünkü su ona varıp durur, source:"ن ه ي,B004"}; {ar:تناهى الماء إذا وقف في الغدير وسكن, tr:tenâha'l-mâ', gloss:su gölette durup sakinleşti, source:"ن ه ي,B004"}. Dönüş kelimesinin ailesinde gölete de "rec" denir: {ar:سمي الغدير رجعا, tr:summiye'l-gadîru racʿan, gloss:gölete rec denmiştir, source:"ر ج ع,B006"}. Rab kelimesinin ailesinde de toplanmış bol su vardır: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabab el-mâ'u'l-kesîr, gloss:rabab, toplandığı için böyle denen bol sudur, source:"ر ب ب,B013"}. Böylece on beşinci ayetteki "vazgeçmezse" ifadesinin yanında, suyun durulduğu yerde durmaması da duyulur. Sekizinci ayet suyun varacağı yeri söyler. Kurân bunu ilahî adla birleştiren bir kardeş ayet içerir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Bu yapı sekizinci ayetle aynıdır; tek fark, dönüş yerine varış kökünün kullanılmasıdır.

Kaynaklar: 96:3 ٱلْأَكْرَمُ ك ر م B002; 96:1 رَبِّكَ ر ب ب B008; 96:1 بِٱسْمِ و س م B003; 96:13 وَتَوَلَّىٰٓ و ل ي B010; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B006; 96:17 نَادِيَهُۥ ن د و B004; 96:16 خَاطِئَةٍ خ ط ء B003; 96:6 لَيَطْغَىٰٓ ط غ ي B002; 96:6 لَيَطْغَىٰٓ ط غ ي B001; 96:15 يَنتَهِ ن ه ي B004; 96:8 رَبِّكَ ر ب ب B013

## Başın önü: perçem, alın ve yer

Bu sahne başın ön kısmında geçer. Saç çizgisinde perçem çıkar, altında alnın düz yüzü vardır. Azan adam bu kısmı yukarı kaldırır, bu kısımdan yakalanır ve derisi kararır. Kul ise aynı kısmı yere koyar.

On beşinci ve on altıncı ayetlerin {ar:ٱلنَّاصِيَةِ, tr:en-nâsiye, gloss:perçem, alnın üstündeki saç, source:96:15} kelimesi önce bir yeri adlandırır: {ar:الناصية منبت الشعر في مقدم الرأس, tr:en-nâsiyetu menbitu'ş-şaʿr fî mukaddemi'r-re's, gloss:nâsiye, başın önünde saçın bittiği yerdir, source:"ن ص ي,B001"}. Sonra bir tutuşu adlandırır: {ar:آخذ بناصيتها أي متمكن منها, tr:âhizun bi nâsiyetihâ, gloss:perçeminden tutan, yani ona tam hâkim olan, source:"ن ص ي,B001"}. On beşinci ayetin fiili bu tutuşun kendisidir: {ar:سفعت الفرس إذا أخذت بمقدم رأسه وهي ناصيته, tr:sefaʿtu'l-feres, gloss:atı başının önünden, yani perçeminden tuttum, source:"س ف ع,B001"}. Bu kalıp hem fiili hem perçemi tek cümlede birleştirir. Aynı fiil yüzün kararmasını da anlatır: {ar:سفعته النار والسموم إذا لفحته لفحا يسيرا فغيرت لون البشرة, tr:sefaʿathu'n-nâru ve's-semûm, gloss:ateş ya da kızgın rüzgâr onu hafifçe yalayıp deri rengini değiştirdi, source:"س ف ع,B003"}. Öfkeden kararan yüz için de {ar:به سفعة غضب, tr:bihî sufʿatu gadab, gloss:yüzünde öfke karası var, source:"س ف ع,B002"} denir. Kurân perçemden tutmayı her canlıya genelleştirir. Hud kavmine şöyle der: {ar:مَّا مِن دَآبَّةٍ إِلَّا هُوَ ءَاخِذٌۢ بِنَاصِيَتِهَآ, tr:mâ min dâbbetin illâ huve âhizun bi nâsiyetihâ, gloss:O'nun perçeminden tutmadığı hiçbir canlı yoktur, source:11:56}. Kurân bunu suçlular için de söyler: {ar:فَيُؤْخَذُ بِٱلنَّوَٰصِى وَٱلْأَقْدَامِ, tr:fe yu'hazu bi'n-nevâsî ve'l-akdâm, gloss:perçemlerinden ve ayaklarından tutulurlar, source:55:41}. Yüzün ateşte sürüklenmesi de anlatılır: {ar:يَوْمَ يُسْحَبُونَ فِى ٱلنَّارِ عَلَىٰ وُجُوهِهِمْ, tr:yevme yushabûne fi'n-nâri ʿalâ vucûhihim, gloss:ateşte yüzüstü sürüklenecekleri gün, source:54:48}. Cehennemin deriyi yakması da: {ar:لَوَّاحَةٌ لِّلْبَشَرِ, tr:levvâhatun li'l-beşer, gloss:deriyi kavurup karartan, source:74:29}.

Perçem aynı zamanda kavmin başıdır: {ar:فلان ناصية قومه, tr:fulânun nâsiyetu kavmih, gloss:falan kavminin perçemidir, yani önderidir, source:"ن ص ي,B003"}. Bu yüzden on altıncı ayetteki {ar:نَاصِيَةٍ كَٰذِبَةٍ خَاطِئَةٍ, tr:nâsiyetin kâzibetin hâti'e, gloss:yalancı, günahkâr bir perçem, source:96:16} ifadesinde hem adamın kendisi hem de on yedinci ayette çağırdığı meclisin başı duyulur. Sıfatlar perçeme yalan ve kasıtlı günah yükler: {ar:الخاطئ هو القاصد للذنب, tr:el-hâti'u huve'l-kâsidu li'z-zenb, gloss:hâti, günaha kasteden kişidir, source:"خ ط ء,B002"}.

Başın yükseltilmesi altıncı ayetin fiilinde de görülür: {ar:الطغية أعلى الجبل, tr:et-tugye aʿle'l-cebel, gloss:tugye dağın en yüksek yeridir, source:"ط غ ي,B005"}. Alnın düz yüzü de yaratma kökünden adlandırılır: {ar:خليقاء الجبهة مستواها, tr:halîkâ'u'l-cebhe, gloss:halîkâ, alnın düz yüzüdür, source:"خ ل ق,B008"}. Kurân başını en yükseğe kaldıranı Firavun'da gösterir: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe kâle ene rabbukumu'l-aʿlâ, gloss:"ben sizin en yüce rabbinizim" dedi, source:79:24}. Arkasından da {ar:فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ, tr:fe ehazehu'llâhu nekâle'l-âhirati ve'l-ûlâ, gloss:Allah onu ahiret ve dünya cezasıyla yakaladı, source:79:25} denir.

Son ayetin secde emri bu sahnenin karşı yüzüdür: {ar:سجد: خضع ومنه سجود الصلاة وهو وضع الجبهة على الأرض, tr:secede: hadaʿa, gloss:secde etti, yani boyun eğdi; namazdaki secde alnı yere koymaktır, source:"س ج د,B001"}; {ar:أسجد الرجل إذا طأطأ رأسه وانحنى, tr:escede'r-racul, gloss:adam başını eğip öne büküldü, source:"س ج د,B004"}. Yukarı kaldırılan ve yakalanıp karartılan alın ile yere konup secde izi taşıyan alın aynı organdır. Sure bu organı iki şekilde gösterir ve iki yol arasındaki farkı başın konumu üzerinden anlatır.

Kaynaklar: 96:15 ٱلنَّاصِيَةِ ن ص ي B001; 96:15 لَنَسْفَعًۢا س ف ع B001; 96:15 لَنَسْفَعًۢا س ف ع B002; 96:15 لَنَسْفَعًۢا س ف ع B003; 96:16 نَاصِيَةٍ ن ص ي B003; 96:16 خَاطِئَةٍ خ ط ء B002; 96:6 لَيَطْغَىٰٓ ط غ ي B005; 96:1 خَلَقَ خ ل ق B008; 96:19 وَٱسْجُدْ س ج د B001; 96:19 وَٱسْجُدْ س ج د B004

## Yol: doğru yolda olmak, sapmak, dönmek, yaklaşmak

Bir yolcu yoldadır. Hedefi ıskalayabilir, yönünden sapabilir ya da sırtını dönüp kaçabilir. Sonunda herkes başladığı yere döner ve yolun bir varış noktası vardır. On birinci ayetin {ar:عَلَى ٱلْهُدَىٰٓ, tr:ʿale'l-hudâ, gloss:doğru yol üzerinde, source:96:11} ifadesi yolcuyu yolun üzerinde gösterir: {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytuhu't-tarîk, gloss:ona yolu ve evi gösterdim, yani tanıttım, source:"ه د ي,B001"}; {ar:الهداية دلالة بلطف, tr:el-hidâye delâletun bi lutf, gloss:hidayet, incelikle yol göstermektir, source:"ه د ي,B001"}. Kök sakin bir yürüyüşü de adlandırır: {ar:لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن, tr:lem yusriʿ isrâʿa'l-munhezim, gloss:bozguna uğrayan gibi koşmadı, sükûnet ve güzel bir yürüyüşle gitti, source:"ه د ي,B010"}. Kurân yolcuları karşılaştırır: {ar:أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ, tr:e fe men yemşî mukibben ʿalâ vechihî ehdâ em men yemşî seviyyen ʿalâ sırâtın mustakîm, gloss:yüzüstü kapanarak yürüyen mi daha doğru yoldadır, yoksa dosdoğru bir yolda dimdik yürüyen mi, source:67:22}. Bu ayette yüz, yolun karşısında bir yürüyüş biçimi olarak geçer; bu da perçem sahnesine yakındır.

On altıncı ayetin günahkâr kelimesi yönden sapmaktır: {ar:الخطأ العدول عن الجهة, tr:el-hata'u'l-ʿudûlu ʿani'l-cihe, gloss:hata yönden sapmaktır, source:"خ ط ء,B001"}. On üçüncü ayetin yüz çevirme fiili, bedenle ya da dinlememekle sırt dönmektir: {ar:التولي قد يكون بالجسم وقد يكون بترك الإصغاء والائتمار, tr:et-tevellî kad yekûnu bi'l-cism, gloss:yüz çevirmek bedenle de olur, dinlememek ve emre uymamakla da, source:"و ل ي,B007"}. Aynı kök kesintisiz yakınlığı da adlandırır: {ar:الولي القرب والدنو, tr:el-velyu'l-kurbu ve'd-dunuvv, gloss:vely yakınlık ve yaklaşmaktır, source:"و ل ي,B001"}. Böylece yüz çevirmek, yakınlığın tersine çevrilmiş halidir. Yalanlama fiilinin ailesinde saldırıda duraksamak da vardır: {ar:حمل فلان ثم كذب أي لم يصدق في الحملة, tr:hamele fulânun summe kezeb, gloss:falan saldırdı, sonra geri durdu, yani saldırısında sözünü tutmadı, source:"ك ذ ب,B004"}.

Sekizinci ayetin dönüşü başlangıca dönüştür: {ar:الرجوع العود إلى ما كان منه البدء, tr:er-rucûʿu'l-ʿavdu ilâ mâ kâne minhu'l-bed', gloss:dönüş, başlangıcın olduğu yere geri gelmektir, source:"ر ج ع,B001"}. Bu başlangıç, ilk iki ayetin yaratmasıdır. Kurân dönüşü yaratılışın başlangıcına bağlar: {ar:إِلَيْهِ مَرْجِعُكُمْ جَمِيعًا, tr:ileyhi merciʿukum cemîʿâ, gloss:hepinizin dönüşü O'nadır, source:10:4}, {ar:إِنَّهُۥ يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ, tr:innehû yebde'u'l-halka summe yuʿîduh, gloss:O yaratmayı başlatır, sonra onu geri getirir, source:10:4}; {ar:كَمَا بَدَأَكُمْ تَعُودُونَ, tr:kemâ bede'ekum teʿûdûn, gloss:sizi başlattığı gibi döneceksiniz, source:7:29}. İnsanın yolu da Rab'be doğru bir uğraş olarak tanımlanır: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًا فَمُلَٰقِيهِ, tr:yâ eyyuhe'l-insânu inneke kâdihun ilâ rabbike kedhan fe mulâkîh, gloss:ey insan, sen Rabbine doğru zahmetle çabalıyorsun ve O'na kavuşacaksın, source:84:6}. Dönmeyeceğini sanan kişi de anlatılır: {ar:إِنَّهُۥ ظَنَّ أَن لَّن يَحُورَ, tr:innehû zanne en len yahûr, gloss:o asla geri dönmeyeceğini sanmıştı, source:84:14}. Yedinci ayetin yeterlilik kökü bu sanıyı yere yerleşmekle de anlatır: {ar:غني القوم في دارهم أقاموا, tr:ganiye'l-kavmu fî dârihim, gloss:topluluk yurdunda yerleşip kaldı, source:"غ ن ي,B004"}. Dönüş kelimesinin ailesinde günahtan dönmek de vardır: {ar:يرجعون عن الذنب, tr:yarciʿûne ʿani'z-zenb, gloss:günahtan dönerler, source:"ر ج ع,B003"}. Bu, on beşinci ayetteki "vazgeçmezse" şartının açık bıraktığı yoldur.

Yolun bir son noktası vardır: {ar:النهاية الغاية حيث ينتهي إليه الشيء, tr:en-nihâyetu'l-gâye, gloss:nihâye, bir şeyin vardığı son noktadır, source:"ن ه ي,B002"}. Son ayetin emri ise yaklaşmaktır: {ar:القرب نقيض البعد والتقرب التدني إلى شيء والاقتراب الدنو, tr:el-kurbu nakîdu'l-buʿd, gloss:yakınlık uzaklığın zıddıdır; yaklaşmak bir şeye doğru alçalıp gelmektir, source:"ق ر ب,B001"}. On ikinci ayetin sakınma kökü yolda dikkatle yürüyen atı da adlandırır: {ar:فرس واق إذا كان يهاب المشي من وجع يجده في حافره, tr:ferasun vâk, gloss:toynağındaki ağrıdan ötürü yürümekten çekinen at, source:"و ق ي,B003"}. Sure böylece yolda olmayı, sapmayı, sırt dönmeyi ve sonunda yaklaşmayı tek bir yol üzerinde sıralar.

Kaynaklar: 96:11 ٱلْهُدَىٰٓ ه د ي B001; 96:11 ٱلْهُدَىٰٓ ه د ي B010; 96:16 خَاطِئَةٍ خ ط ء B001; 96:13 وَتَوَلَّىٰٓ و ل ي B007; 96:13 وَتَوَلَّىٰٓ و ل ي B001; 96:13 كَذَّبَ ك ذ ب B004; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B001; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B003; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B004; 96:15 يَنتَهِ ن ه ي B002; 96:19 وَٱقْتَرِب ق ر ب B001; 96:12 بِٱلتَّقْوَىٰٓ و ق ي B003

## Ölçerek yaratmak ve uydurmak

Yaratmak doğru ölçmektir. Aynı kök uydurmayı da adlandırır: {ar:الخلق خلق الكذب وهو اختلاقه واختراعه وتقديره في النفس, tr:el-halku halku'l-kezib, gloss:halk, yalanı uydurmak, icat etmek ve onu nefiste ölçüp biçmektir, source:"خ ل ق,B007"}. Bu tanım yaratma kökünü yalan köküyle birleştirir. Rab gerçeği ölçerek yaratır; yalancı ise yalanı içinde ölçüp biçer. Kurân bu anlamı İbrahim'in kavmine söylediği sözde kullanır: {ar:إِنَّمَا تَعْبُدُونَ مِن دُونِ ٱللَّهِ أَوْثَٰنًا وَتَخْلُقُونَ إِفْكًا, tr:innemâ taʿbudûne min dûni'llâhi evsânen ve tahlukûne ifkâ, gloss:siz Allah'ı bırakıp putlara tapıyor ve yalan uyduruyorsunuz, source:29:17}. Mekkeli ileri gelenler de vahyi bu kelimeyle niteler: {ar:إِنْ هَٰذَآ إِلَّا ٱخْتِلَٰقٌ, tr:in hâzâ ille'htilâk, gloss:bu bir uydurmadan başka bir şey değil, source:38:7}. Gerçek yaratıcının övgüsü de aynı kökle yapılır: {ar:فَتَبَارَكَ ٱللَّهُ أَحْسَنُ ٱلْخَٰلِقِينَ, tr:fe tebâreka'llâhu ahsenu'l-hâlikîn, gloss:yaratanların en güzeli Allah ne yücedir, source:23:14}.

On üçüncü ayetin yalanlama fiili ile on altıncı ayetin yalancı sıfatı aynı köktendir: {ar:الكذب خلاف الصدق, tr:el-kezibu hilâfu's-sidk, gloss:yalan doğruluğun zıddıdır, source:"ك ذ ب,B001"}. Kökte görünüşüyle yalan söyleyen bir kumaş da vardır: {ar:الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله, tr:el-kezzâbe sevbun yunkaşu bi levni sıbg, gloss:kezzâbe, boyayla nakışlı gibi gösterilen kumaştır; çünkü haliyle yalan söyler, source:"ك ذ ب,B009"}. Öğretme kökündeki gerçek dokuma kenarı bunun karşısında durur: {ar:علم الثوب ورقمه في أطرافه, tr:ʿalemu's-sevb, gloss:kumaşın alemi, kenarlarındaki dokuma nakışıdır, source:"ع ل م,B002"}. Kökte beklenenden önce kesilen süt de yer alır: {ar:كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم, tr:kezebe lebenu'n-nâka, gloss:devenin sütü bir süre süreceği sanıldığı halde kesildi, source:"ك ذ ب,B006"}. Görüntü ile sürekliliğin çatıştığı bir figürdür bu. Yedinci ayetin görme kökünde güzel görünüş de vardır: {ar:الرواء حسن المنظر, tr:er-ruvâ' husnu'l-manzar, gloss:ruvâ, görünüş güzelliğidir, source:"ر ء ي,B006"}.

On altıncı ayetin sıfatı kasıtlı günahı seçer: {ar:الخطأ ما لم يتعمد … الخطيئة الذنب على عمد, tr:el-hata'u mâ lem yutaʿammad … el-hatî'etu'z-zenbu ʿalâ ʿamd, gloss:hata kasıtsız olandır; hatîe kasıtlı günahtır, source:"خ ط ء,B002"}. Kurân bu kelimeyi helak edilmiş toplumlar için kullanır: {ar:وَجَآءَ فِرْعَوْنُ وَمَن قَبْلَهُۥ وَٱلْمُؤْتَفِكَٰتُ بِٱلْخَاطِئَةِ, tr:ve câ'e firʿavnu ve men kablehû ve'l-mu'tefikâtu bi'l-hâti'e, gloss:Firavun, ondan öncekiler ve altı üstüne getirilen şehirler o günahı işlediler, source:69:9}, {ar:فَأَخَذَهُمْ أَخْذَةً رَّابِيَةً, tr:fe ehazehum ahzeten râbiye, gloss:O da onları şiddetli bir yakalayışla yakaladı, source:69:10}. Günahın ardından gelen yakalama, on beşinci ayetteki perçemden yakalamayla aynı yapıdadır.

Bu sahne şunu gösterir: on altıncı ayetteki yalancı perçem, olmadığı bir şeyi iddia eden yüksek baştır, boyanmış ama dokunmamış bir kumaş gibidir. Gerçek ölçüyü yaratan Rab'bin karşısında, uydurma bir ölçüyle kendini yeterli görür.

Kaynaklar: 96:1 خَلَقَ خ ل ق B001; 96:1 خَلَقَ خ ل ق B007; 96:13 كَذَّبَ ك ذ ب B001; 96:16 كَٰذِبَةٍ ك ذ ب B009; 96:16 كَٰذِبَةٍ ك ذ ب B006; 96:4 عَلَّمَ ع ل م B002; 96:7 رَّءَاهُ ر ء ي B006; 96:16 خَاطِئَةٍ خ ط ء B002

## Buluşmalar

İmgeler en açık şekilde baş sahnesinde buluşur. On beşinci ayetin fiili hem perçemden tutmak hem de yüzü karartmaktır. Böylece başın önü, avın yakalandığı yer, huysuz hayvanın tutulduğu yer ve ateşin yaladığı deri aynı noktada birleşir. Aynı alın son ayette yere konur ve secde izini taşır. İşaret imgesi buraya da uzanır: bir alın kararmış bir lekeyle işaretlenir, öteki secdenin iziyle. Kurân her iki tarafı da yüzlerindeki işaretle tanıtır: biri {ar:مِّنْ أَثَرِ ٱلسُّجُودِ, tr:min eseri's-sucûd, gloss:secdenin izinden, source:48:29}, öteki {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. Sure ad ile başlar ve iki işaretli alınla biter.

Göz ile yeterlilik imgeleri yedinci ayette buluşur. Kendini aynada gören adam ile süse ihtiyaç duymayan güzel kadın aynı kelime çiftinde birleşir: kendini görmek ve yeterli saymak. Su imgesi de buna bağlanır. Azan insan ölçüsünü aşan bir taşkın gibidir; on beşinci ayette durması istenir. Kökün göletteki duruluşu adlandırdığı hatırlanırsa, sekizinci ayet bu suyun nereye varacağını söyler. Kurân'ın varış ayeti bu iki imgeyi aynı yapıda birleştirir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Yol imgesi de bu dönüşe katılır, çünkü dönüş başlangıca dönmektir ve bu başlangıç rahimdeki ilk tutunuştur.

Rahim ile okuma, surenin ilk kelimesinde buluşur. Okumanın kökü hem rahmin bir şeyi toplayıp tutmasını hem de harflerin toplanmasını adlandırır. Pıhtıyı tutan kökle sözü toplayan kök aynıdır. İnsanın yaratılışı ve öğretilmesi bu yüzden aynı işin iki yüzü olarak duyulur. Kurân'daki benzer sıra da bunu destekler: Kurân'ı öğretmek, insanı yaratmak ve ona açıklamayı öğretmek. Okuma ile secde de buluşur: okuyucu aynı zamanda kulluk edendir ve sure, ilk emri okumak, son emri secde etmek olan bir eğri çizer. Kurân bu ikisini, okunduğunda secde edenler ile etmeyenler üzerinden birleştirir.

Ateş ile çağrı imgeleri onuncu, on yedinci ve on sekizinci ayetlerde buluşur. Namaz hem çağrıdır hem de kökü ateşe girmeyi adlandırır. Adam meclisini çağırır, Allah ateşe iten bekçileri çağırır ve kul yakın meclise çağrılır. Ateşin kendisinin de çağırdığı söylenir: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Bu yüz çevirme on üçüncü ayetin fiilidir.

İtaat ile hayvan imgeleri son ayette buluşur. Rab, itaat edilen efendidir; dizgine uyan at da itaatin bir figürüdür. Kul bu yüzden kendini rab ilan eden birine boyun eğmez, yakında tutulan ve değer gören at gibi yaklaşır. Yaratma ile uydurma da on altıncı ayette buluşur. Gerçek ölçüyle yaratan Rab'bin karşısında, yalanı içinde ölçen yalancı perçem durur.

Bu buluşmalar surenin hareketini taşır. Sure, rahimde toplanan ve tutunan bir varlıkla başlar; bu varlık sözü toplamayı ve kalemle yazmayı öğrenir. Sonra kendini aynada yeterli görür, taşkın su gibi ölçüsünü aşar, başını kaldırır ve namaz kılan kulu engellemeye çalışır. Dönüş ayeti ve Allah'ın görmesi bu yükselişin önüne bir sınır koyar. Yasaklayan perçeminden yakalanır, meclisi yerine bekçiler gelir. Kul ise yüz çevirmeden, başını yere koyarak, çağrılmış olduğu yakınlığa yürür.

