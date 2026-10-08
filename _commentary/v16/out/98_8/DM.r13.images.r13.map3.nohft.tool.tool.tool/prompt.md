Focus: 98:8. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/98_8/D.r13/context.md =====
# 98:8 — focus

جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ

Anchor translation (canonical reading, reference only):

Rableri katındaki karşılıkları, altlarından ırmaklar akan Adn bahçeleridir; orada sonsuza dek kalacaklardır. Allah onlardan hoşnut olmuştur, onlar da O'ndan hoşnut olmuşlardır. Bu, Rabbinden korkan kimse içindir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | جَزَآؤُهُمْ | جَزَآء | ج ز ي | N;PRON |
| 2 | عِندَ | عِند | ع ن د | LOC |
| 3 | رَبِّهِمْ | رَبّ | ر ب ب | N;PRON |
| 4 | جَنَّٰتُ | جَنَّة | ج ن ن | N |
| 5 | عَدْنٍ | عَدْن |  | PN |
| 6 | تَجْرِى | جَرَيْ | ج ر ي | V |
| 7 | مِن | مِن |  | P |
| 8 | تَحْتِهَا | تَحْت | ت ح ت | N;PRON |
| 9 | ٱلْأَنْهَٰرُ | نَهَر | ن ه ر | DET;N |
| 10 | خَٰلِدِينَ | خَٰلِد | خ ل د | N |
| 11 | فِيهَآ | فِى |  | P;PRON |
| 12 | أَبَدًا | أَبَدًا | ء ب د | T |
| 13 | رَّضِىَ | رَّضِىَ | ر ض و | V |
| 14 | ٱللَّهُ | ٱللَّه | ء ل ه | PN |
| 15 | عَنْهُمْ | عَن |  | P;PRON |
| 16 | وَرَضُوا۟ | رَّضِىَ | ر ض و | CONJ;V;PRON |
| 17 | عَنْهُ | عَن |  | P;PRON |
| 18 | ذَٰلِكَ | ذَٰلِك |  | DEM |
| 19 | لِمَنْ | مَن |  | P;REL |
| 20 | خَشِىَ | خَشِىَ | خ ش ي | V |
| 21 | رَبَّهُۥ | رَبّ | ر ب ب | N;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 98 — full text (context; no pericope)

- 98:1 لَمْ يَكُنِ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ مُنفَكِّينَ حَتَّىٰ تَأْتِيَهُمُ ٱلْبَيِّنَةُ
- 98:2 رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ
- 98:3 فِيهَا كُتُبٌۭ قَيِّمَةٌۭ
- 98:4 وَمَا تَفَرَّقَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ إِلَّا مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَةُ
- 98:5 وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ
- 98:6 إِنَّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ ۚ أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ
- 98:7 إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ
- 98:8 ◀ focus جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ


===== _commentary/v16/work/98_8/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ج ز ي (root_000244) — identity root of جَزَآؤُهُمْ (w1)

- **B001** iyiliğe ya da kötülüğe denk karşılık verme — birine yaptığını iyilikle ya da kötülükle karşılama · birine yaptığının karşılığını verme · yapılana verilen iyi ya da kötü karşılık · çok geçmeden öç alma karşılığı · iyi işlerin ve yerine getirilmesi gereken yükümlülüklerin karşılıkları
  جزى يجزي جزاء أي كافأ بالإحسان وبالإساءة (ayn)؛ جزيته بما صنع جزاء وجازيته (sihah)؛ الجزاء يكون ثوابا ويكون عقابا؛ جزيت فلانا بما صنع جزاء؛ جزاء العطاس؛ الجوازي معناها الجزاء (tahdhib)؛ الجزاء ما فيه الكفاية من المقابلة إن خيرا فخير وإن شرا فشر؛ جزيته بكذا وجازيته (mufradat)؛ مكافأته إياه؛ جزيت فلانا أجزيه جزاء وجازيته مجازاة (maqayis)
- **B002** yerini tutup yükümlülüğü karşılama — yeterlilik ve bir işi başkası adına yerine getirme · bu işi benim yerime görüp tamamlama · bir koyunun senin adına yükümlülüğü karşılaması · yeterli olan ve başkasının yerini tutan kimse · birinin alacağını ya da borcunu ödeme
  فلان ذو غناء وجزاء (ayn)؛ جزى عني هذا الأمر أي قضى؛ جزت عنك شاة؛ رجل جازيك أي حسبك (sihah)؛ الجزاء أيضا القضاء؛ لا تقضي فيه نفس عن نفس شيئا؛ جزيت فلانا حقه؛ جزيته قرضه؛ صدقتك جزت عنك؛ هذا رجل حسبك وناهيك وكافيك وجازيك (tahdhib)؛ الجزاء الغناء والكفاية؛ لا يجزي والد عن ولده؛ جازيك فلان أي كافيك (mufradat)؛ قيام الشيء مقام غيره؛ ينوب مناب كل أحد؛ جزى عني هذا الأمر يجزي كما تقول قضى يقضي (maqayis)
- **B003** alacağı talep etme — borcumu ondan isteme · alacağını isteyen veya borcun ödenmesini talep eden kimse
  تجازيت ديني تقاضيته (ayn)؛ تجازيت ديني على فلان إذا تقاضيته؛ المتجازي المتقاضي (sihah)؛ أمرت فلانا يتجازى ديني أي يتقاضاه؛ أهل المدينة يسمون المتقاضي المتجازي (tahdhib)؛ تجازيت ديني على فلان أي تقاضيته؛ أهل المدينة يسمون المتقاضي المتجازي (maqayis)
- **B004** koruma statüsüne bağlı tarihsel vergi — koruma statüsündeki topluluklardan alınan tarihsel vergi · koruma statüsüne bağlı tarihsel vergiler
  الجزية ما يؤخذ من أهل الذمة والجمع الجزى (sihah)؛ الجزية جزية الناس التي تؤخذ من أهل الذمة؛ الجزية الخراج المجعول على الذمي سميت جزية لأنها قضاء منه لما عليه (tahdhib)؛ الجزية ما يؤخذ من أهل الذمة وتسميتها بذلك للاجتزاء بها عن حقن دمهم (mufradat)
- **B005** karşılık vermede üstün gelme [kalıp] — karşılık verme yarışında ötekine üstün gelme
  جازيته فجزيته أي غلبته (sihah)

## ع ن د (root_001052) — identity root of عِندَ (w2)

- **B001** doğruyu bile bile geri çevirerek karşı koyma ve sınırı aşma — azıp sınırı aşmak ve doğruyu bile bile geri çevirmek · bildiği şeyi kabul etmeyi bile bile reddetme · birine karşı durup onunla boy ölçüşmek; kimi zaman onun yaptığının benzerini yapmak · zorbalık eden ve doğruya uymaktan yüz çeviren kimse · doğruyu kabul etmeyip karşı çıkan kimse · devenin yulara yüklenip onu yöneten kişiyi çekmesi
  أصل صحيح واحد يدل على مجاوزة وترك طريق الاستقامة (maqayis)؛ عند الرجل إذا طغى وعتا وجاوز قدره (maqayis;ayn)؛ المعاندة أن يعرف الرجل الشيء ويأبى أن يقبله (maqayis;ayn;tahdhib)؛ خالف ورد الحق وهو يعرفه (sihah)؛ العنيد المعرض عن طاعة الله تعالى (tahdhib)؛ استعند البعير إذا غلب قائده على الزمام (maqayis)؛ عاند البعير خطامه أي عارضه (tahdhib)
- **B002** ortak doğrultudan yana sapıp ayrı durma — yoldan ya da amaçlanan yönden sapıp uzaklaşmak · bir yana çekilip topluluğa karışmayan · tek başına yaşayıp insanlara karışmayan adam · sürünün bir yanında durup öteki develere karışmayan deve · canlılığı ve gücü yüzünden yoldan yana sapan dişi deve · düz doğrultudan yana sapmış yol · yan, taraf · sağa sola yönelen saplama vuruşu · öteki kura oklarından başka bir yönde çıkarak kazanan ok · dirseği göğüsten uzakta duran
  العنود من الإبل الذي لا يخالط الإبل إنما هو في ناحية (maqayis;ayn;tahdhib)؛ رجل عنود لا يخالط الناس (maqayis;ayn)؛ طريق عاند أي مائل (maqayis)؛ العند بالتحريك الجانب (sihah)؛ العاند البعير الذي يجور عن الطريق ويعدل عن القصد (sihah)؛ قدح عنود وهو الذي يخرج فائزا على غير وجهة سائر القداح (tahdhib)
- **B003** sıvının yana yönelerek veya kesilmeden akması [kalıp] — kanı fışkırıp bir türlü dinmeyen damar · kanın yana doğru akması · kanı yaralıdan uzağa doğru akan yara · kusmanın art arda sürüp kesilmemesi · bol yağmur taşıyan bulut
  العرق العاند الذي يتفجر منه الدم فلا يكاد يرقأ (maqayis)؛ عند العرق سال ولم يرقأ وهو عرق عاند (sihah)؛ أعند في قيئه إذا لم ينقطع (maqayis)؛ أعند الرجل في قيئه إذا أتبع بعضه بعضا (sihah;tahdhib)؛ عند الدم إذا سال في جانب (tahdhib)؛ سحابة عنود كثيرة المطر (tahdhib)
- **B004** yakınında veya birinin değerlendirmesinde bulunma — bir şeyin yer veya zaman bakımından yakınında · birinin görüşünde, değerlendirmesinde, gözünde veya katında
  عند فحضور الشيء ودنوه (sihah)؛ عند لفظ موضوع للقرب (mufradat)؛ يستعمل في المكان وفي الاعتقاد وفي الزلفى والمنزلة (mufradat)؛ عند حرف صفة يكون موضعا لغيره ولفظه نصب (tahdhib)؛ في التقريب شبه اللزق (tahdhib)؛ مال عن الناس كلهم إليه حتى قرب منه ولزق به (maqayis)
- **B005** başka seçenek, kaçınma payı veya çıkış yolu — başka bir seçenek, kaçınma payı veya çıkış yolu · bir işe ulaşma yolu ya da başka seçenek
  ما عنه عِنْدَد أي ما عنه ميل ولا حيدودة (maqayis)؛ مالي منه عِنْدَد ومُعْلَنْدَد أي بد (sihah;tahdhib)؛ العندد الحيلة (tahdhib)؛ ما وجدت إلى كذا معلنددا أي سبيلا (sihah)
- **B006** sözü dinleyeni almaya veya tutmaya yönelten buyruk — onu al; ona bağlı kal
  وقد يغرى بها تقول عندك زيدا أي خذه (sihah)؛ العرب تأمر من الصفات بعليك وعندك ودونك وإليك (tahdhib)

## ر ب ب (root_000532) — identity root of رَبِّهِمْ (w3)

- **B001** sahip olup yönetme — Tanrı; sahip, buyruğu geçen yönetici veya düzenleyici · bir şeyin sahibi · evin sahibi veya ev işlerini yöneten kadın · sahiplik, egemenlik ve yönetim yetkisi
  الرب: الله تبارك وتعالى؛ ورب كل شيء مالكه (jamhara); رب كل شئ: مالكه؛ وقد قالوه في الجاهلية للملك؛ رببت القوم: سستهم (sihah); يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح (tahdhib); الرب مصدر مستعار للفاعل؛ لا يقال الرب مطلقا إلا لله؛ رب الدار ورب الفرس (mufradat); فالرب المالك والخالق والصاحب؛ والله جل ثناؤه الرب (maqayis)
- **B002** adım adım yetiştirip tamamlama — yapılan iyiliği eksiksiz kılmak · mülkü gözetip iyileştirmek · çocuğunu yetiştirmek · bir şeyi aşama aşama olgunlaştırma · yetiştirme anlamındaki değişmeli söyleyiş
  رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها (jamhara); رب الضيعة أي أصلحها وأتمها؛ رب فلان ولده؛ رباه (sihah); رب الشيء أي أصلحه؛ رب فلان الصنيعة إذا أتمها وأصلحها (tahdhib); التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام؛ ربه ورباه ورببه (mufradat); رب فلان ضيعته إذا قام على إصلاحها؛ رببت الصبي أربه (maqayis); ربته تربيتا إذا رببه (maqayis-rbt)
- **B003** Tanrı bilgisiyle yetiştiren bilgin — Tanrı bilgisine sahip bilgin ve öğretici
  الرباني: المتأله العارف بالله تعالى (sihah); الرباني: العالم؛ العلماء بالحلال والحرام؛ حكماء علماء؛ العالم المعلم الذي يغذو الناس بصغار العلوم (tahdhib); الرباني... يرب العلم؛ يرب نفسه بالعلم؛ منسوب إلى الرب (mufradat); الربي العارف بالرب (maqayis)
- **B004** büyük insan topluluğu — büyük topluluk; on bin kişilik topluluk · tek birlik hâlinde birleşmiş beş kabile · insanları toplayan kişi veya toplanma yeri
  الربي: واحد الربيين، وهم الألوف من الناس؛ الرباب خمس قبائل تجمعوا (sihah); الربيون: الألوف؛ الربيون: الجماعات الكثيرة؛ الربة: عشرة آلاف؛ الربان: الجماعة (tahdhib); يجوز أن يضم الربرب إلى الباب الثالث لتجمعه (maqayis)
- **B005** bakımla kurulan üvey aile bağı — üvey oğul veya bakım altında yetişen erkek çocuk · üvey kız veya bakım altında yetişen kız çocuk · bakıcı kadın; evde sütü için beslenen dişi hayvan · çocuğun bakımını üstlenen üvey baba veya üvey anne
  الراب: زوج الأم؛ الرابة: امرأة الأب؛ ربيب الرجل: ابن امرأته من غيره؛ الربيبة: الحاضنة (sihah); الربيب: ابن امرأة الرجل من غيره؛ ربيبة الرجل: بنت امرأته من غيره؛ راب ورابة (tahdhib); الراب والرابة بأحد الزوجين إذا تولى تربية الولد؛ الربيب والربيبة بذلك الولد (mufradat); ربيب الرجل ابن امرأته؛ الراب الذي يقوم على أمر الربيب (maqayis)
- **B006** koyu öz veya yağ tortusu — koyu meyve özü veya yağ tortusu · koyu özle işlenmiş veya güçlendirilmiş · koyu meyve özüyle hazırlanmış yiyecekler
  رب السمن والزيت: ثفله الأسود؛ سقاء مربوب إذا أصلح بالرب (jamhara); الرب: الطلاء الخاثر؛ سقاء مربوب؛ المرببات الأنبجات (sihah); رب فلان نحيه إذا جعل فيه الرب ومتنه به؛ نحي مربوب (tahdhib); رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب (mufradat); هذا سقاء مربوب بالرب؛ الرب للعنب وغيره لأنه يرب به الشيء (maqayis)
- **B007** bir yerde kalıp sürme — bir yerde kalıp ayrılmamak · develerin sürekli kaldığı yer · bulut sürüp gitti · dişi deve erkeğe bağlandı · bir şeye yaklaşma
  رب بالمكان وأرب إذا أقام به (jamhara); مرب الإبل حيث لزمته؛ أربت الإبل؛ أربت الناقة؛ أربت الجنوب والسحابة أي دامت؛ الأرباب الدنو (sihah); أرب فلان بالمكان إذا أقام به فلم يبرحه؛ مرب الإبل أي حيث لزمته (tahdhib); أربت السحابة: دامت؛ أرب فلان بمكان كذا (mufradat); الأصل الآخر لزوم الشيء والإقامة عليه؛ أربت السحابة؛ الإرباب الدنو (maqayis)
- **B008** katmanlı asılı bulut kümesi — beyaz olabilen, katmanlı veya aşağıda asılı bulut
  الرباب: سحاب أبيض؛ الواحدة ربابة (sihah); الربابة: السحابة التي قد ركب بعضها بعضا؛ جمعها رباب (tahdhib); الرباب: السحاب، سمي بذلك لأنه يرب النبات (mufradat); سمي السحاب ربابا؛ السحاب المتعلق دون السحاب يكون أبيض ويكون أسود (maqayis)
- **B009** başlangıçtaki tazelik — yeni doğurmuş veya sütü için evde tutulan koyun · bir şeyin yeni ve taze dönemi · gençliğin ilk ve taze dönemi
  الربى: الشاة التي وضعت حديثا؛ قرب العهد بالولادة؛ بربانه أي بحدثانه وجدته وطراءته (sihah); الربى: أول الشباب؛ الربان من كل شيء: حدثانه؛ الشاة فهي ربى (tahdhib); الشاة الربي التي تحتبس في البيت للبن؛ التي وضعت حديثا (maqayis)
- **B010** kura oklarını toplayan kap — kura oklarını bir arada tutan deri veya bez kap
  الربابة: قطعة من أدم تجمع فيها القداح (jamhara); الربابة شبيهة بالكنانة تجمع فيها سهام الميسر؛ جماعة السهام (sihah); الربابة: جماعة السهام؛ الجلدة التي تجمع فيها السهام (tahdhib); لما يجمع فيه القدح ربابة (mufradat); الخرقة التي يجعل فيها القداح ربابة (maqayis)
- **B011** bağlayıcı söz ve güvence — tarafları birleştiren bağlayıcı söz veya sözleşme · sözleşmeye bağlı taraflar · bağlayıcı söz; söz gibi bağlayıcı vergi payı
  الربابة: العهد والمعاهدون أربة (jamhara); الربابة: العهد والميثاق؛ الأربة أهل الميثاق (sihah); الرباب: العهد؛ الرباب: العشور (tahdhib); العقد في موالاة الغير: الربابة (mufradat); الربابة وهو العهد؛ للمعاهدين أربة؛ الرباب العشور (maqayis)
- **B012** belirli bir yeşil bitki türü — belirli bir bitki, yumuşak ot veya küçük ağaç türü
  الربة: ضرب من الشجر أو النبت (jamhara); الربة بالكسر: ضرب من النبت، والجمع الربب (sihah); الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف (tahdhib)
- **B013** bol ve toplanmış su — çok miktarda su; bazen bol tatlı su
  الربب، بالفتح: الماء الكثير، ويقال العذب (sihah); الربب وهو الماء الكثير سمي بذلك لاجتماعه (maqayis)
- **B014** yaban sığırı sürüsü — yaban sığırı sürüsü; bazen sığır veya deve topluluğu
  الربرب: القطيع من بقر الوحش (sihah); الربرب: جماعة البقر، وكذلك الإبل (tahdhib); الربرب القطيع من بقر الوحش؛ يجوز أن يضم إلى الباب الثالث لتجمعه (maqayis)
- **B015** azlık bildiren ilgeç — belirsiz adla azlık bildiren ilgeç; nice az · eylem önünde bazen veya kimi zaman · azlık ilgecinin sonuna ses eklenmiş ağız biçimi · belirsiz öğe eklenmiş azlık ilgeci biçimi
  رب: كلمة؛ ربما؛ ربت في معنى رب (jamhara); رب حرف خافض؛ ربما؛ ربت؛ ربه رجلا (sihah); رب من حروف المعاني؛ رب للتقليل؛ ربما؛ ربتما؛ تزيد في رب هاء (tahdhib); رب لاستقلال الشيء، ولما يكون وقتا بعد وقت، نحو ربما (mufradat); رب فكلمة تستعمل في الكلام لتقليل الشيء؛ ولا يعرف لها اشتقاق (maqayis)
- **B016** gereksinim, sıkı düğüm veya iyilik — gereksinim · sıkıca bağlanmış düğüm · iyilik ve başkasına yarar sağlama
  الربى: الحاجة؛ الربى: الرابة؛ الربى: العقدة المحكمة؛ الربى: النعمة والإحسان (tahdhib)
- **B017** gemicilerin başı — gemicilerin başı, kaptan
  رباني: رئيس الملاحين (tahdhib)

## ج ن ن (root_000266) — identity root of جَنَّٰتُ (w4)

- **B001** örtme ve duyulardan gizleme — örtmek; gizleyecek bir örtü sağlamak; içinde saklamak · bir şeyin arkasına gizlenmek · insanı örten giysi veya örtü
  الجيم والنون أصل واحد وهو الستر والتستر (maqayis)؛ أصل الجن ستر الشيء عن الحاسة (mufradat)؛ استجن فلان إذا استتر بشيء (ayn;tahdhib)؛ أجننت الشيء في صدري أكننته (sihah)؛ ما علي جنان إلا ما ترى أي ثوب يواريني (sihah;tahdhib)
- **B002** gecenin karartıp örtmesi — gecenin kararıp üzerini örtmesi · gecenin koyu karanlığı ve nesneleri örtmesi
  جنان الليل سواده وستره الأشياء (maqayis)؛ أجنه الليل وجن عليه الليل إذا أظلم حتى يستره بظلمته (ayn)؛ جن عليه الليل يجن بالضم جنونا (sihah)؛ جن عليه الليل وأجنه الليل إذا أظلم حتى يستره بظلمته (tahdhib)؛ جنه الليل وأجنه وجن عليه (mufradat)
- **B003** zemini ağaçlarla örtülü bahçe — zemini ağaçlarla örtülü bahçe veya koruluk
  الجنة البستان (maqayis;sihah)؛ الجنة الحديقة وهي بستان ذات شجر ونزهة (ayn)؛ العرب تسمي النخيل جنة (sihah)؛ كل بستان ذي شجر يستر بأشجاره الأرض (mufradat)
- **B004** ölüm sonrası gizli nimetler yurdu — ölüm sonrası ödül ve gizli nimetler yurdu
  الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم (maqayis)؛ سميت الجنة إما تشبيها بالجنة في الأرض وإما لستره نعمها عنا (mufradat)
- **B005** gözle görülmeyen ruhani varlıklar topluluğu — gözle görülmeyen ruhani varlıklar · görünmeyen varlıkların atası veya bir bireyi · görünmeyen ruhani varlıkların topluluğu · görünmeyen ruhani varlıkların çok bulunduğu yer
  الجن سموا بذلك لأنهم متسترون عن أعين الخلق (maqayis)؛ الجن جماعة ولد الجان وجمعهم الجنة والجنان (ayn;tahdhib)؛ الجن خلاف الإنس والواحد جني (sihah)؛ الجنة جماعة الجن (mufradat)؛ أرض مجنة كثيرة الجن (ayn;sihah;tahdhib)
- **B006** aklı örten akıl yitimi — aklını yitirmek; aklını yitirmiş duruma getirmek · akıl yitimi; benlik ile akıl arasındaki engel · aklını yitirmiş gibi davranmak
  الجنة الجنون وذلك أنه يغطي العقل (maqayis)؛ المجنة الجنون وجن الرجل وأجنه الله فهو مجنون (ayn)؛ جن الرجل جنونا وأجنه الله فهو مجنون (sihah)؛ به جنون وجنة ومجنة (tahdhib)؛ الجنون حائل بين النفس والعقل (mufradat)
- **B007** ana rahmindeki doğmamış çocuk — ana rahmindeki doğmamış çocuk · rahminde çocuk taşımak; çocuğun rahimde saklı kalması
  الجنين الولد في بطن أمه (maqayis)؛ أجنت الحامل الجنين أي الولد في بطنها (ayn)؛ الجنين الولد ما دام في البطن (sihah)؛ الجنين الولد في الرحم (tahdhib)؛ الجنين الولد ما دام في بطن أمه (mufradat)
- **B008** koruyucu siper veya savaş donanımı — koruyucu örtü, siper veya savaş donanımı · kalkan
  المجن الترس وكل ما استتر به من السلاح فهو جنة (maqayis)؛ المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك (ayn)؛ الجنة ما استترت به من سلاح والجنة السترة والمجن الترس (sihah)؛ المجن الترس (tahdhib)؛ المجن والمجنة الترس الذي يجن صاحبه (mufradat)
- **B009** ölüyü örtüp gömme — ölüyü örtmek ve gömmek · gömüt; ölü örtüsü; gömülmüş kişi
  الجنين المقبور (maqayis)؛ الجنن القبر وقيل للكفن أيضا (ayn)؛ جننت الميت وأجننته أي واريته والجنن القبر (sihah)؛ جننته في القبر وأجننته والجنن القبر والجنن الكفن (tahdhib)؛ الجنين القبر (mufradat)
- **B010** duyulardan saklı yürek ve gizli yön — yürek veya yüreğin saklı iç yönü · gizli iş veya görünmeyen yön
  الجنان القلب (maqayis)؛ الجنان روع القلب (ayn;tahdhib)؛ أراد بالجن القلب (sihah)؛ الجنان القلب لكونه مستورا عن الحاسة (mufradat)؛ الجنان الأمر الخفي (tahdhib)
- **B011** bitkinin güçlenip boylanması ve sıklaşması — bitkinin güçlenmesi, boylanması, sıklaşması veya çiçek açması · uzun ağaç; bol otlu ve henüz otlanmamış arazi
  جن النبت جنونا إذا اشتد وخرج زهره (maqayis)؛ جن النبت جنونا أي طال والتف وخرج زهره ونخلة مجنونة أي طويلة (sihah)؛ للنبت الملتف الكثيف مجنون وجنت الرياض جنونا إذا اعتم نبتها (tahdhib)؛ جن التلاع والآفاق أي كثر عشبها (mufradat)
- **B012** yılan, özellikle beyaz bir tür — yılan, beyaz yılan veya belirli bir yılan türü
  الحية الذي يسمى الجان فهو تشبيه له بالواحد من الجان (maqayis)؛ الجان حية بيضاء (ayn)؛ الجان أيضا حية بيضاء (sihah)؛ الجان الحية وجمعها جوان (tahdhib)؛ الجان ضرب من الحيات (mufradat)
- **B013** halkın büyük kitlesi — insanların çoğunluğu veya halkın büyük kitlesi
  جنان الناس معظمهم ويسمى السواد (maqayis)؛ جنان الناس دهماؤهم (sihah)؛ جنانهم جماعتهم وسوادهم (tahdhib)
- **B014** bir şeyin ilk ve yeni dönemi — gençliğin, çocukluğun veya bir dönemin ilk başlangıcı
  كان ذلك في جن شبابه أي في أول شبابه (sihah)؛ كان ذلك في جن صباه أي في حداثته وكذلك جن كل شيء أول ابتدائه (tahdhib)
- **B015** uçuş sırasında çoğalan sinek vızıltısı — sineğin vızıltısının veya sesinin çoğalması · böcekse uçuş vızıltısının artması; bitkiyse sıklaşıp dolaşması
  جن الذباب أي كثر صوته (sihah)؛ جن الخازباز به جنونا يحتمل هذين الوجهين (sihah)؛ قيل هو ذباب وجنونه كثرة ترنمه في طيرانه وقيل هو نبت وجنون النبت التفافه (tahdhib)
- **B016** göğüs kemikleri ve kaburga uçları — göğüs kemikleri veya kaburgaların göğse yakın uçları
  الجناجن عظام الصدر (maqayis)؛ الجنجن والجناجن أطراف الأضلاع مما يلي الصدر وعظم القلب (ayn)؛ الجناجن عظام الصدر الواحد جنجن (sihah)
- **B017** içine girilip saklanılan yer — saklanılan yer; ayrıca kaynakta belirli bir eski pazar yerinin adı
  المجنة اسم موضع على أميال من مكة؛ كانت مجنة وذو المجاز وعكاظ أسواقا في الجاهلية؛ المجنة أيضا الموضع الذي يستتر فيه (sihah)

## ج ر ي (root_000240) — identity root of تَجْرِى (w6)

- **B001** bir yol boyunca akıp, koşup ya da ilerleyerek gitme — hızlı ilerleyiş ve kendi yatağında akış · aktı, koştu ya da yol aldı · suyun akışı · at koşusu · akıtmak ya da harekete geçirmek · akış, gidiş yolu ya da koşu yeri · denizde yol alan gemi · gökte yol alan güneş · suyu akan pınar · denizde yol alan gemiler · çeşitli koşu biçimleri olan at · kötücül ayartıcının sizi kendi işi doğrultusunda sürüklemesine ya da kendine aracı kılmasına izin vermeyin
  أصل واحد وهو انسياح الشيء (maqayis)؛ جرى الماء يجري جرية وجريا وجريانا (maqayis;sihah;mufradat)؛ الخيل تجري والرياح تجري والشمس تجري جريا (ayn;tahdhib)؛ الجارية السفينة والجارية الشمس (maqayis;sihah)
- **B002** alışılmış yol ve davranış düzeni — kişinin alışkanlık edindiği ve sürekli izlediği yol
  للعادة الإجريا (maqayis)؛ الإجريا طريقته التي يجري عليها من عادته (ayn)؛ الإجريا الجري والعادة مما تأخذ فيه (sihah)؛ الإجرياء الوجه الذي نأخذ فيه (tahdhib)؛ الإجريا العادة التي يجري عليها الإنسان (mufradat)
- **B003** başkası adına iş gören, haber götüren ya da güvence veren kimse — başkası adına iş gören, haber götüren ya da güvence veren kimse · başkası adına iş görecek birini tutmak · kötücül ayartıcının sizi kendi işi doğrultusunda sürüklemesine ya da kendine aracı kılmasına izin vermeyin
  الجري الوكيل (maqayis;tahdhib)؛ الجري الرسول (ayn;tahdhib;mufradat)؛ الجري الضامن (tahdhib)؛ استجريت أي اتخذت وكيلا (maqayis;sihah;tahdhib)؛ لا يستجرينكم الشيطان (maqayis;sihah;tahdhib;mufradat)
- **B004** genç kız ve ona bağlı genç kızlık çağı — genç kız ya da hizmette çalıştırılan genç kadın · genç kızlık çağı · genç kızlık durumu
  الجارية من النساء لأنها تستجرى في الخدمة (maqayis)؛ الجارية مصدرها الجراء (ayn)؛ جارية بينة الجراية والجراء (sihah;tahdhib)؛ أيام جرائها أي صباها (maqayis;ayn;sihah)
- **B005** kuş kursağı — 
  الجرية وهي الحوصلة أصلها قرية (maqayis)؛ الجرية مثل القرية هي الحوصلة (sihah)؛ الجرية والقرية والنوطة لحوصلة الطائر (tahdhib)؛ يقال للحوصلة جرية لأنها مجرى الطعام (mufradat)
- **B006** sürekli verilen geçimlik ya da kalıcı yarar — düzenli görev ödeneği · onun için sürekli verildi ya da sürüp gitti · ona sürekli olarak verdim · yararı süren bağış
  الجراية الجاري من الوظائف (sihah)؛ الأرزاق جارية والأعطيات دارة (tahdhib)؛ جرى عليه ذلك الشيء ودر له بمعنى دام له (tahdhib)؛ أجريت له كذا أي أدمت له (tahdhib)؛ صدقة جارية (tahdhib)
- **B007** birlikte ilerleyip birbirine ayak uydurma — yanında koşmak ya da ona ayak uydurmak · söyleşide ona ayak uydurmak ve karşılık vermek
  جاراه مجاراة وجراء أي جرى معه (sihah)؛ جاراه في الحديث وتجاروا فيه (sihah)
- **B008** senin yüzünden ya da senin için — senin yüzünden ya da senin için
  فعلت ذلك من جراك ومن جرائك أي من أجلك (sihah)

## ت ح ت (root_000177) — identity root of تَحْتِهَا (w8)

- **B001** alt konum — alt, altinda kalan yer
  تحت الشيء (maqayis)؛ تحت نقيض فوق (tahdhib)؛ تحت مقابل لفوق (mufradat)؛ يستعمل في المنفصل (mufradat)
- **B002** itibarsiz dusuk kimseler — dusuk ve itibarsiz kimseler
  التَّحوت الدون من الناس (maqayis)؛ الذين كانوا تحت أقدام الناس لا يؤبه لهم وهم السفل والأنذال (tahdhib)؛ الأراذل من الناس (mufradat)

## ن ه ر (root_001559) — identity root of ٱلْأَنْهَٰرُ (w9)

- **B001** bol su taşıyan doğal akarsu yatağı — taşkın suyun aktığı doğal akarsu yatağı · akarsu yatakları · akarsular veya akarsu yatakları · akarsu yatağı sağlam bir güzergah edindi · su aktı ve kendine bir yatak açtı · bol sulu veya geniş akarsu · suyun kazıp açtığı yatak yeri · kuyu kazısı suya ulaştı
  النهر مجرى الماء الفائض (mufradat)؛ النهر واحد الأنهار وجمعه أنهار ونهر (ayn;sihah;tahdhib;maqayis)؛ سمي النهر لأنه ينهر الأرض أي يشقها (maqayis)؛ استنهر النهر أخذ مجراه (ayn;tahdhib;maqayis)؛ نهر الماء أو أنهر الماء جرى (sihah;tahdhib;maqayis)؛ نهر نهر كثير الماء (sihah;tahdhib;maqayis;mufradat)؛ حفرت البئر حتى نهرت أي بلغت الماء (tahdhib)
- **B002** şafaktan gün batımına aydınlık gündüz — şafaktan güneş batımına kadar süren aydınlık gündüz · aydınlık gündüz süreleri · gündüz vaktinde baskın yapan kimse · gündüzün aydınlığına girdik
  النهار ضياء ما بين طلوع الفجر إلى غروب الشمس (ayn;tahdhib;maqayis)؛ النهار ضد الليل (sihah)؛ الوقت الذي ينتشر فيه الضوء (mufradat)؛ النهار اسم لكل يوم (tahdhib)؛ النهار يجمع على نهر (sihah;tahdhib;maqayis)؛ رجل نهر صاحب نهار (ayn;sihah;tahdhib;maqayis;mufradat)
- **B003** bir şeyi açma veya genişletme — genişlik veya aydınlıkla birlikte genişlik · kanı açıp serbest bırakarak akıttı · yaranın veya yarığın açıklığını genişletti · genişledi · evlerin önleri arasında atık bırakılan açık alan · bağırsağı çözüldü ve akarsu gibi boşaldı · tehlikeler; birleşik bir türetme olarak açıklanan biçim
  أصل صحيح يدل على تفتح شيء أو فتحه (maqayis)؛ أنهرت الدم فتحته وأرسلته (maqayis)؛ أنهرت الدم أي أسلته (sihah;mufradat)؛ أنهرت الطعنة وسعتها وأنهر فتقها (sihah;tahdhib)؛ نهر من نهر الفتق (maqayis)؛ استنهر الشيء اتسع (sihah)؛ المنهرة فضاء يكون بين أفنية القوم (maqayis;sihah;mufradat)؛ أنهر بطنه إذا جاء بطنه مثل مجيء النهر (tahdhib)؛ النهر السعة تشبيها بنهر الماء وفي ضياء وسعة (mufradat;sihah;tahdhib)
- **B004** sert sözle azarlayıp engelleme [kalıp] — onu sert sözle azarlayıp engelledi
  نهرت الرجل نهرا وانتهرته انتهارا زجرته بكلام عن شر (ayn)؛ نهره وانتهره أي زبره (sihah)؛ نهرته وانتهرته إذا استقبلته بكلام تزجره (tahdhib)؛ النهر والانتهار الزجر بمغالظة (mufradat)
- **B005** bazı kuşların yavrusu — türü aktarıma göre değişen bir kuş yavrusu
  النهار فرخ القطا والغطاط والعقاب ونحوه وثلاثة أنهرة (ayn)؛ النهار فرخ الحبارى (sihah;tahdhib;mufradat)؛ النهار فرخ بعض الطير مما لا يعرج على مثله ولا معنى له (maqayis)
- **B006** fırsat kollayıp gizlice kapma — fırsat kollayıp ani biçimde gizlice kapma
  النهر الدغرة وهي الخلسة (tahdhib)
- **B007** kişi, yer ve yıldızlara ait özel adlar — belirli bir topluluktan bir şairin adı · bir yer adı · sularının bolluğu nedeniyle iki yıldız için kullanılan ortak ad
  نهار بن توسعة اسم شاعر من تميم (sihah)؛ نهروان بلد (sihah)؛ العرب تسمي العواء والسماك الأنهرين لكثرة مائهما (tahdhib)
- **B008** bulut — bulut
  الناهُور السحاب (tahdhib)

## خ ل د (root_000429) — identity root of خَٰلِدِينَ (w10)

- **B001** kalıcı olma ve durumunu koruma — kalmak; varlığını sürdürmek · kalıcılık; bulunduğu durumda kalma · kalıcılık; kalıcı yaşam yurdu · sonsuz yaşam bahçesi · ölümden sonraki kalıcı yaşam yurdu · kalıcı kılmak; kalacağına hükmetmek · yaşlandığı halde saçına ak düşmeyen · ön kesici dişleri, yan kesici dişleri çıkana kadar düşmeyen hayvan · yıkıntılar yok olduktan sonra kalan ocak taşları ve kayalar
  أصل واحد يدل على الثبات والملازمة (maqayis)؛ الخلود البقاء فيها (ayn)؛ دوام البقاء (jamhara;sihah)؛ دار الخلود والخلد الآخرة والجنة (jamhara)؛ بقاؤه على الحالة التي هو عليها (mufradat)؛ مخلد إذا أبطأ عنه الشيب (maqayis;jamhara;sihah;mufradat)؛ خوالد للأثافي والحجارة لطول مكثها (ayn;sihah;mufradat)
- **B002** yönelip bağlanma, yapışma ya da ayrılmadan kalma [kalıp] — yere yapışmak veya ona bağlanmak · ona yönelmek ve ondan hoşnut olmak · o yerde kalmak · arkadaşının yanından ayrılmamak
  أخلد إلى الأرض إذا لصق بها (maqayis;jamhara)؛ أخلد إلى كذا أي ركن إليه ورضي به (ayn)؛ أخلدت إلى فلان أي ركنت إليه (sihah)؛ أخلد بالمكان أقام به وأخلد بصاحبه لزمه (sihah)؛ ركن إليها ظانا أنه يخلد فيها (mufradat)
- **B003** küpe; küpe veya bilezikle süslenmiş olma — küpe; bir tür kulak süsü
  ولدان مخلدون مقرطون (ayn;mufradat)؛ من الخلد والخلد جمع خلدة وهي القرط (maqayis)؛ مقرطون مشنفون (maqayis)؛ مسورون لغة يمانية (jamhara)
- **B004** akıl ve akla gelen düşünce — akıl; zihinde yer eden düşünce · aklıma geldi
  الخلد البال وسمي بذلك لأنه مستقر في القلب ثابت (maqayis)؛ ما يقع ذلك في خلدي (ayn)؛ وقع ذلك في خلدي أي في قلبي (jamhara)؛ وقع ذلك في خلدي أي في ورعي وقلبي (sihah)
- **B005** gözsüz faremsi küçük hayvan — gözleri olmayan, fareye veya sıçana benzeyen küçük hayvan
  الخلد ضرب من الجرذان عمي لم يخلق لها عيون (ayn)؛ الخلد دويبة تشبه الفأرة (jamhara)؛ ضرب من الجرذان أعمى (sihah)

## ء ب د (root_000004) — identity root of أَبَدًا (w12)

- **B001** sonsuz süre ve kalıcı kılma — sonsuz zaman, çok uzun süre · sonsuza dek, kesintisiz olarak · çağlar boyunca, sonsuza dek · bütün zaman boyunca · kalıcı kılma · sürekli kılınmış, devredilemez · sonsuza dek veya çok uzun süre kalmak
  طول المدة (maqayis)؛ الأبد الدهر (maqayis;sihah)؛ أبد الآبدين وأبد الدهر (tahdhib)؛ الأبد الدائم والتأبيد التخليد (sihah)؛ مدة الزمان الممتد (mufradat)؛ وقفا مؤبدا وتأبيدا (tahdhib)
- **B002** yabanıllaşıp insandan ürkme — devenin yabanıllaşması · hayvanın yabanıllaşıp insandan ürkmesi · yabani ve ürkek hayvanlar · yabani inek
  تأبد البعير توحش (maqayis;mufradat)؛ أوابد كأوابد الوحش (maqayis;tahdhib)؛ أبدت البهيمة أي توحشت (sihah)؛ توحشت ونفرت من الإنس (tahdhib)؛ الوحشيات (mufradat)
- **B003** terk edilip ıssızlaşmak [kalıp] — evin terk edilip ıssızlaşması ve yabani hayvanlara kalması
  تأبد المنزل خلا (maqayis)؛ تأبد المنزل أي أقفر وألفته الوحوش (sihah)؛ خلا منها أهلها خلفتهم الوحش بها قد تأبدت (tahdhib)
- **B004** her yıl doğuran dişi — her yıl doğuran dişi eşek, kısrak veya köle kadın
  الإبد ذات النتاج من المال كالأمة والفرس والأتان (maqayis)؛ الابد الولود من أمة أو أتان (sihah)؛ أتان إبد في كل عام تلد (tahdhib)
- **B005** yüzün lekelenip sertleşmesi [kalıp] — yüzün lekelenmesi, sertleşmesi veya öfkeden değişmesi
  تأبد وجهه كلف (maqayis)؛ تأبد وجه فلان توحش وقد فسر بغضب (mufradat)
- **B006** bir yerde kalıp ayrılmama — bir yerde kalıp oradan ayrılmamak · kış yaz aynı arazide kalan kuşlar
  أبد بالمكان أي أقام به (sihah)؛ أبدت بالمكان إذا أقمت به ولم تبرحه (tahdhib)؛ الطير المقيمة بأرض شتاءها وصيفها أوابد (tahdhib)
- **B007** uzun süre anılan olağanüstü olay — uzun süre anılan olağanüstü iş veya olay · unutulmayacak kadar sıra dışı bir iş yapmak
  الأبدة الفعلة تبقى على الأبد (maqayis)؛ جاء فلان بآبدة أي بداهية يبقى ذكرها على الأبد (sihah)
- **B008** yadırgatıcı söz veya başıboş uyak — yadırgatıcı, alışılmadık sözcük · şiirin başıboş veya aykırı uyakları
  الشوارد من القوافي أوابد (sihah)؛ الكلمة الوحشية آبدة وجمعه الأوابد (tahdhib)
- **B009** öfkelenmek veya birine öfkelenmek [kalıp] — adamın öfkelenmesi · ona öfkelenmek
  أبد الرجل غضب (sihah)؛ أبد إذا غضب عليه (tahdhib)؛ وقد فسر بغضب (mufradat)

## ر ض و (root_000569) — identity root of رَّضِىَ (w13)

- **B001** hoşnut olma ve kabul etme — hoşnut olmak; kabul etmek · hoşnut · kabul edilmiş; kendisinden hoşnut olunan · kendisinden hoşnut olunan kişi · hoşnutluk · onu kabul edip uygun buldu · onu seçip uygun buldu · ondan hoşnut oldu; onu kabul etti · hoşnutluk adı · beğenilen bir yaşayış · onu arkadaş olarak kabul etti · ondan hoşnut oldu; onu uygun buldu · beğenilen; kabul edilen · kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması · Tanrı'nın kulu buyruğa uyan ve yasaktan kaçınan biri olarak görmesi
  أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضا مقصور (ayn)؛ رضيت الشيء وارتضيته فهو مرضي ومرضو ورضيت عنه رضا (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو ورضا العبد عن الله ورضا الله عن العبد (mufradat)
- **B002** hoşnutluk; yoğun hoşnutluk — hoşnutluk; yoğun hoşnutluk · hoşnutluk
  الرضوان اسم موضوع من الرضا (ayn)؛ الرضوان الرضا وكذلك الرضوان بالضم والمرضاة مثله (sihah)؛ الرضوان الرضا الكثير (mufradat)
- **B003** karşılıklı hoşnutluk ve kabul — karşılıklı hoşnutluk · birbiriyle hoşnutlaşma · birbirlerinden hoşnut olduklarını karşılıklı gösterdiler
  المراضاة من اثنين (ayn)؛ مصدر راضيته رضاء ومراضاة (sihah;tahdhib)؛ إذا تراضوا بينهم أي أظهر كل واحد منهم الرضا بصاحبه ورضيه (mufradat)
- **B004** başkasını hoşnut etme veya hoşnutluğunu isteme — onu kendimden hoşnut ettim · onu hoşnut ettim · uğraşarak onu hoşnut ettim · ondan hoşnutluk göstermesini istedim; o da beni hoşnut etti
  أرضيته عني ورضيته بالتشديد أيضا فرضي وترضيته أرضيته بعد جهد واسترضيته فأرضاني (sihah)
- **B005** karşılıklı çekişmede üstün gelme — karşılıklı çekişmede ona üstün geldim
  قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه لأنه من الواو (sihah)
- **B006** söz dinleyen, seven veya güvence veren — söz dinleyen; seven; güvence veren
  الرضي المطيع والرضي المحب والرضي الضامن (tahdhib)
- **B007** bir dağ adı ve kadın adları — bir dağ adı; bir kadın adı · o dağın adına bağlılık bildiren biçim · bir kadın adı
  رضوى جبل (maqayis;ayn;sihah)؛ ومن أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)

## ء ل ه (root_000047) — identity root of ٱللَّهُ (w14)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## خ ش ي (root_000413) — identity root of خَشِىَ (w20)

- **B001** korku duyma — korku; özellikle saygı ve bilgiyle karışan korku · korkmak · korkan erkek · korkan kadın · ondan daha çok korku duydum · bu yer ötekinden daha çok korku verir · onu korkuttu
  الخشية الخوف والفعل خشي يخشى؛ هذا المكان أخشى من ذاك أي أفزعه (ayn)؛ خشي الرجل يخشى خشية أي خاف فهو خشيان والمرأة خشياء؛ كنت أشد خشية منه؛ هذا المكان أخشى أي أشد خوفا؛ خشاه تخشية أي خوفه (sihah)؛ الخشية الخوف والفعل خشي يخشى؛ هذا المكان أخشى من ذلك المكان؛ معناها من الآدميين الخوف (tahdhib)؛ الخشية خوف يشوبه تعظيم وأكثر ما يكون ذلك عن علم (mufradat)؛ يدل على خوف وذعر فالخشية الخوف ورجل خشيان؛ كنت أشد خشية منه؛ هذا المكان أخشى من ذلك أي أشد خوفا (maqayis)
- **B002** bilmek — bildim
  خشيت بأن من تبع الهدى معناه علمت (sihah)؛ فخشينا أي فعلمنا (tahdhib)؛ المجاز قولهم خشيت بمعنى علمت؛ أي علمت (maqayis)
- **B003** istememe ve hoşnutsuzluk [kalıp] — Tanrı'ya yüklenen kullanımda istememe ve hoşnutsuzluk
  فخشينا أن يرهقهما طغيانا وكفرا قال الأخفش معناه كرهنا (sihah)؛ فخشينا عن الله لأن الخشية من الله تعالى معناها الكراهة ومعناها من الآدميين الخوف (tahdhib)
- **B004** kuruyup sertleşmiş veya buruşup niteliğini yitirmiş olma — buruşmuş, düşük nitelikli hurma · hurma ağacı buruşmuş, düşük nitelikli meyve verdi · kuru et
  الخشي وهو اليابس؛ الخشو الحشف من التمر؛ خشت النخلة تخشو إذا أحشفت (sihah)؛ مما شذ عن الباب وقد يمكن الجمع بينهما على بعد الخشو التمر الحشف؛ خشت النخلة تخشو خشوا؛ الخشي من اللحم اليابس (maqayis)

## و ل ه (root_005296) — documented alternative for ٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ECHO ج ز ز (root_000242) — for جَزَآؤُهُمْ (w1): withheld observed target; not identity

- **B001** saç, yün veya bitkiyi kırkıp kesme — saçı, yünü veya bitkiyi kırkıp kesmek · kırkma aleti · yünü kırkılan koyunlar
  جززت الصوف جزا (maqayis); الجز جز الشعر والصوف وغيره (ayn); جززت البر والنخل والصوف أجزه جزا والمجز ما يجز به (sihah); الجز جز الشعر والصوف والحشيش ونحوه وقد جززت الكبش والنعجة (tahdhib)
- **B002** kesim ya da hasat vaktinin gelmesi — kırkım, hasat veya ürün toplama zamanı · ağaç ürününün, ekinin veya koyunun kesim ya da kırkım vaktinin gelmesi · topluluğun koyunlarını kırkma ya da ekinini biçme vaktinin gelmesi · ekinin biçilecek duruma gelmesi
  هذا زمن الجزاز والجزاز (maqayis); الجزاز كالحصاد يقع على الحين والأوان وأجز النخل مثل أحصد البر (ayn); هذا زمن الجزاز والجزاز أي زمن الحصاد وصرام النخل وأجز النخل والبر والغنم واستجز البر (sihah); الجزاز كالحصاد واقع على الحين والأوان وأجز النخل حان له أن يجز وأجز القوم إذا حان أن تجز غنمهم (tahdhib)
- **B003** yeni kırkılmış yün veya kesimden kalan parça — henüz kullanılmamış kırkılmış yün · bir koyundan bir yılda kırkılan yün · deri veya başka bir şey kesilince düşen ya da fazla kalan parça · bir tutam yün
  الجزيزة خصلة من صوف والجمع جزائز والجزازة ما سقط من الأديم (maqayis); الجزز الصوف الذي لم يستعمل بعد ما جز وصوف كل شاة جزة والجزاز ما فضل من الأديم (ayn); الجزة صوف شاة والجزازة ما سقط من الأديم والجزيزة خصلة من الصوف (sihah); الجزز الصوف الذي لم يستعمل بعدما جز وهذه جزة هذه الشاة والجزاز ما فضل من الأديم (tahdhib)
- **B004** asılan boyalı yün süsü veya süs boncuğu — deve üzerindeki yolcu bölmesine bağlanan veya asılan boyalı yün tutamları · deve üzerindeki yolcu bölmesine asılan boyalı yün tutamları · deve üzerindeki yolcu bölmesinden sarkan boyalı yün parçası · insanı süslemek için kullanılan bir boncuk türü
  الجزائر عهون تشد على الهوادج (ayn); الجزجزة وهي عهنة تعلق من الهودج (sihah); الجزاجز خصل العهن والصوف المصبوغة تعلق على هوادج الظعائن وهي الثكن والجزائز وقيل الجزيز ضرب من الخرز (tahdhib)
- **B005** hurmanın kuruması veya hurmadaki kuruluk — hurmanın kuruması · hurmanın kuruması · hurmadaki kuruluk veya kuruma durumu
  جز التمر يجز بالكسر جزوزا أي يبس وأجز مثله وتمر فيه جزوز (sihah); قد جز التمر إذا يبس يجز جزوزا وتمر فيه جزوز (tahdhib)
- **B006** rivayette bir çıkış yeri olarak anılan yer adı — rivayette bir çıkış yeri olarak anılan yer adı
  جزة اسم أرض يقال إن الدجال يخرج منها (ayn); جزة اسم أرض منها يخرج الدجال فيما روي (tahdhib)

## ECHO ر ب و (root_000537) — for رَبِّهِمْ (w3): withheld observed target; not identity

- **B001** artmak veya yükselmek — bir şey arttı veya yükseldi · toprak suyla kabarıp arttı · yükselen veya fazla köpük · olağandan daha şiddetli yakalayış · onun üzerine çıktı veya üstünde bulundu
  ربا الجرح والأرض والمال وكل شيء يربو إذا زاد (ayn)؛ ربا الشيء يربو ربوا إذا ارتفع (jamhara)؛ ربا الشيء يربو ربوا أي زاد (sihah;tahdhib)؛ ربت أي زادت، وزبدا رابيا، وأخذة رابية (tahdhib;mufradat)؛ أربى عليه أي أشرف عليه (mufradat)
- **B002** yükselmiş arazi — yükselmiş arazi · çevresinden yüksek yer · arazideki yükselti
  الرابية ما ارتفع من الأرض، والربوة لغات أرض مرتفعة (ayn)؛ الربو والربوة والرباوة واحد وهو العلو من الأرض (jamhara)؛ الرابية الربو وهو ما ارتفع من الأرض، وكذلك الربوة (sihah)؛ الرباوة والرابية والرباة كل ذلك ما ارتفع من الأرض (tahdhib)؛ ربوة وربوة وربوة ورباوة، وسميت الربوة رابية (mufradat)
- **B003** belirli işlem biçimleriyle sınırlı anapara fazlalığı — belirli alışveriş veya borç biçimlerinde anaparayı aşan fazlalık · işlemdeki anapara fazlalığının özel adı veya bir söyleyiş biçimi · mal bu işlemde fazlalıkla arttı · anaparaya fazlalık eklenen işleme girdi
  ربا المال يربو في الربا أي يزداد، والربا في كتاب الله حرام، والربية هي الربا خاصة (ayn)؛ الربا في البيع، والربية لغة في الربا (sihah)؛ الربا ربوان، فالحرام كل قرض يؤخذ به أكثر منه (tahdhib)؛ الربا الزيادة على رأس المال، لكن خص في الشرع بالزيادة على وجه دون وجه (mufradat)
- **B004** soluğu yükselip sıkışmak — yüksek ve sıkışık soluma · soluğu sıkıştı · at koşu ya da ürkme yüzünden şişip soluksuz kaldı · soluğu yükselip tıkanmış
  ربا فلان أي أصابه نفس في جوفه ودابة بها ربو (ayn)؛ أصابه ربو من مشي أو عدو إذا علت أنفاسه (jamhara)؛ الربو النفس العالي، وربا الفرس إذا انتفخ من عدو أو فزع (sihah)؛ أخذها الربو وهو البهر (tahdhib)؛ الربو الانبهار سمي بذلك تصورا لتصعده (mufradat)
- **B005** besleyip büyütmek ve yetişmek — onu besleyip büyüttü · onların arasında yetişti · çocuğu besleyip büyüttü, çocuk gelişti
  ربيته وتربيته أي غذوته (ayn)؛ ربوت في بني فلان وربيت أي نشأت فيهم، وربيته تربية وتربيته أي غذوته، هذا لكل ما ينمي كالولد والزرع (sihah)؛ ربيت الولد فربا من هذا (mufradat)
- **B006** uyluk kökü ve iç yanlardaki iki çıkıntılı et parçası — uyluk kökü veya kasık eti · uyluk köklerinin iç yanlarındaki iki çıkıntılı et parçası
  الأربية أصل الفخذ، وهما أربيتان (sihah)؛ الأربيتان لحمتان ناتئتان في أصول الفخذين من باطن (mufradat)
- **B007** baba tarafından yakın hane halkının arasına gelmek [kalıp] — kendi topluluğundaki baba tarafından yakın hane halkının arasına geldi
  جاء فلان في أربية قومه، أي في أهل بيته من بني الأعمام ونحوهم، ولا تكون الأربية من غيرهم (sihah)

## ECHO ر ض ي (root_000570) — for رَّضِىَ (w13): withheld observed target; not identity

- **B001** hoşnut olup uygun bulma — hoşnut olmak; gönlüne uygun bulmak · hoşnut olan · beğenilmiş, uygun bulunmuş · kendisinden hoşnut olunan · uygun bulunmuş; eski kök yapısını koruyan biçim · kendisinden hoşnut olunan adam; eski kök yapısını koruyan söyleyiş · hoşnutluk; hoşnutsuzluğun karşıtı · hoşnutluğu bildiren uzatılmış ad biçimi · hoşnutluk; çok güçlü hoşnutluk · hoşnutluk bildiren ad · iki tarafın birbirini uygun bulması · birbirini uygun bulma ve karşılıklı anlaşma · şeyi beğenip uygun buldum · onu beğenip seçtim · ondan hoşnut oldum · onu arkadaş olarak uygun buldum · ondan ya da onunla olmaktan hoşnut oldum · beğenilen, hoşnutluk veren yaşayış · onu benden hoşnut ettim · onu hoşnut ettim · uğraştıktan sonra onu hoşnut ettim · onun gönlünü yapmaya çalıştım, sonunda benden hoşnut oldu · birbirlerini uygun bulup anlaştılar · kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması · Tanrı'nın kulunu buyruklarına uyar ve yasaklarından kaçınır görmesi · beğenilmiş, uygun bulunmuş
  أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضوان من الرضا (ayn)؛ الرضوان الرضا والمرضاة مثله ورضيت الشيء وارتضيته (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو والرضوان الرضا الكثير (mufradat)
- **B002** çekişmede alt etme — o benimle çekişti, ben de onu o işte yendim
  قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه (sihah)
- **B003** dağ ve kadın adı ailesi — bir dağın ve bir kadının adı · söz konusu dağla ilgili veya o dağdan olan · bir kadın adı
  رضوى جبل (maqayis;ayn)؛ رضوى جبل بالمدينة والنسبة إليه رضوى (sihah)؛ من أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)
- **B004** buyruğa uyan, seven veya güvence veren — buyruğa uyan, seven ya da güvence veren
  الرَّضِيّ المطيع؛ الرَّضِيّ المحب؛ الرَّضِيّ الضامن (tahdhib)

===== _commentary/v16/out/s098/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 98:8, and ## Buluşmalar) =====
## Sıra hâlinde atlar: önde giden, ardından gelen

Tilâvetin kökündeki izleme, Arapçada bir yarış alanında da görülür: {ar:جاءت الخيل تتاليا أي متتابعة, tr:câeti'l-haylü tetâliyen, gloss:atlar birbiri ardınca geldi, source:"ت ل و,B001"}. Atlar ardışık bölükler hâlinde de gelir ve bu, resûl kökünün sözüdür: {ar:جاءت الخيل أرسالا قطيعا قطيعا, tr:câeti'l-haylü ersâlen, gloss:atlar bölük bölük geldi, source:"ر س ل,B005"}. Yarışta ikinci gelen atın adı ise namaz kelimesinin kökünden gelir: {ar:قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه, tr:kad sallâ ve câe musalliyen, gloss:ikinci geldi, çünkü başı önündeki atın sağrısını izliyordu, source:"ص ل و,B006"}; kısaca {ar:المصلى تالي السابق, tr:el-musallî tâli's-sâbık, gloss:musallî, öndekinin ardından gelendir, source:"ص ل و,B006"}. Burada tilâvetin kökü ile salâtın kökü tek cümlede birleşir: ikinci at başını birincinin sağrısına dayayarak onun izini sürer.

Bu sahne ikinci ayetteki {ar:يَتْلُوا۟, tr:yetlû, gloss:okuyor, source:98:2} kelimesine bir hareket verir: okuyuş, satırın satırı izlemesidir, tıpkı atın atı izlemesi gibi. Beşinci ayetteki {ar:وَيُقِيمُوا۟ ٱلصَّلَوٰةَ, tr:ve yükîmu's-salât, gloss:namazı kılsınlar, source:98:5} emri de arka planda bu izleme duygusunu taşır: önde gideni takip eden konum. Yarışın bir de bitiş çizgisi vardır ve bu ad gelmek kökündendir: {ar:الميتاء والميداء آخر الغاية حيث ينتهي إليه جري الخيل, tr:el-mîtâ' ve'l-mîdâ', gloss:mîtâ, atların koşusunun sona erdiği son hedef, source:"ء ت ي,B010"}. Bu tanım, birinci ayetteki ta'tiyehüm ile sekizinci ayetteki {ar:تَجْرِى, tr:tecrî, gloss:akar, source:98:8} kelimelerinin köklerini tek cümlede toplar; koşu fiilinin kendisi de atlar için kullanılır: {ar:الخيل تجري والرياح تجري, tr:el-haylü tecrî, gloss:atlar koşar, rüzgârlar eser, source:"ج ر ي,B001"}. Surenin sekizinci ayetinde akan şey nehirlerdir; atların koşusu yalnızca kökün arka planında duyulur.

Kur'an elçilerin ardışıklığını aynı izleme diliyle anlatır: {ar:ثُمَّ أَرْسَلْنَا رُسُلَنَا تَتْرَا, tr:sümme erselnâ rusulenâ tetrâ, gloss:sonra elçilerimizi birbiri ardınca gönderdik, source:23:44}; aynı ayette {ar:فَأَتْبَعْنَا بَعْضَهُم بَعْضًۭا, tr:fe-etba'nâ ba'dahum ba'dâ, gloss:onların bir kısmını bir kısmının ardından getirdik, source:23:44}. Mürselât suresi ardışık gönderilenlere yemin ederek açılır {source:77:1}, Sâffât suresi de okuyanlara: {ar:فَٱلتَّٰلِيَٰتِ ذِكْرًا, tr:fe't-tâliyâti zikrâ, gloss:zikri okuyanlara andolsun, source:37:3}. Vâkıa suresi kıyamette insanları sınıflarken öne geçenleri ayrı anar: {ar:وَٱلسَّٰبِقُونَ ٱلسَّٰبِقُونَ, tr:ve's-sâbikûne's-sâbikûn, gloss:öne geçenler, öne geçenlerdir, source:56:10}.

Kaynaklar: 98:2 يَتْلُوا۟ ت ل و B001; 98:2 رَسُولٌ ر س ل B005; 98:5 ٱلصَّلَوٰةَ ص ل و B006; 98:1 تَأْتِيَهُمُ ء ت ي B010; 98:8 تَجْرِى ج ر ي B001

## Yol ve binek: çiğnenmiş yol, işaret taşı, çatal, yumuşatılmış deve

Dördüncü ve beşinci ayetlerin birçok kelimesi bir güzergâhın parçalarını adlandırır. İbadet kelimesinin kökü çok yürünmekle düzleşmiş yoldur: {ar:الطريق المعبد وهو المسلوك المذلل, tr:et-tarîku'l-muabbed, gloss:muabbed yol, çok yürünmüş, ayak altında yumuşamış yoldur, source:"ع ب د,B005"}. Aynı kök, katranla sıvanıp uysallaştırılmış deveyi de adlandırır: {ar:البعير المعبد المهنوء بالقطران المذلل, tr:el-ba'îru'l-muabbed, gloss:katranla sıvanmış, yumuşatılmış deve, source:"ع ب د,B003"}; yol için de deve için de aynı kelime, müzellel, kullanılır. Kökün insana dönük anlamı da budur: {ar:العبودية إظهار التذلل والعبادة غاية التذلل, tr:el-ubûdiyyetü izhâru't-tezellül, gloss:kulluk boyun eğişi göstermek, ibadet boyun eğişin en ileri derecesidir, source:"ع ب د,B003"}. Din kelimesi de bu boyun eğişin bir türü olarak tanımlanır: {ar:جنس من الانقياد والذل, tr:cinsün mine'l-inkıyâdi ve'z-zül, gloss:bir tür itaat ve alçalış, source:"د ي ن,B001"}. Beşinci ayetin {ar:لِيَعْبُدُوا۟ ٱللَّهَ, tr:li-ya'budu'llâh, gloss:Allah'a kulluk etsinler diye, source:98:5} ifadesi arka planda hem çiğnenip düzleşen yolu hem dizgine uyan deveyi taşır.

Yolun üzerinde işaretler vardır. Emir kelimesinin kökü, çölde yolu gösteren küçük taş yığınlarını adlandırır: {ar:الأمر بالتحريك جمع أمرة وهي العلم الصغير من أعلام المفاوز من الحجارة, tr:el-emeru cem'u emera, gloss:emer, emara'nın çoğulu; çöllerdeki işaretlerden taştan küçük bir alamet, source:"ء م ر,B005"}. Ayetin {ar:وَمَآ أُمِرُوٓا۟, tr:ve mâ umirû, gloss:onlara emredilmedi, source:98:5} sözü, düz anlamında bir buyruktur; arka planında yolcunun gözünü diktiği taş işaretler duyulur. Yol bir noktada çatallanır: {ar:فرق له الطريق أي اتجه له طريقان, tr:feraka lehü't-tarîk, gloss:yol önünde ikiye ayrıldı, source:"ف ر ق,B006"}; dördüncü ayetteki teferruk bu çatal noktasında durur. Müşriklerin kökü yolun ana gövdesinden ayrılan küçük patikaları adlandırır: {ar:أم الطريق معظمه وبنياته أشراك صغار, tr:ümmü't-tarîki mu'zamuhû ve büneyyâtühû eşrâkün sıgâr, gloss:yolun anası ana gövdesidir, ondan ayrılan küçük yollar ise küçük şeraklardır, source:"ش ر ك,B005"}. Hanif kelimesi doğruya meyletmektir: {ar:الحنف ميل عن الضلال إلى الاستقامة, tr:el-hanefü meylün ani'd-dalâli ile'l-istikâme, gloss:hanef, sapkınlıktan doğruluğa meyletmektir, source:"ح ن ف,B003"}; {ar:حُنَفَآءَ, tr:hunefâ, gloss:hanifler olarak, source:98:5} yan patikadan dönüp ana yola sapanlardır. Ayetin sonu yolun kendisini adlandırır: {ar:وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ, tr:ve zâlike dînü'l-kayyime, gloss:işte dosdoğru din budur, source:98:5}; {ar:الاستقامة في الطريق الذي يكون على خط مستو, tr:el-istikâmetü fi't-tarîki'llezî yekûnü alâ hattin müstevin, gloss:istikamet, düz bir hat üzerindeki yolda olmaktır, source:"ق و م,B008"}. Beşinci ayet, yolun neredeyse bütün parçalarını tek cümlede toplar.

Altıncı ayetteki ateş kelimesinin kökü bile yolda bir işarettir: {ar:المنار: علم الطريق, tr:el-menâr alemü't-tarîk, gloss:menar, yolun işaretidir, source:"ن و ر,B005"}; insanlar yolu bulmak için ateş yakardı: {ar:كانوا ينورون في الجاهلية ليهتدى ويقتدى بها, tr:kânû yünevvirûn, gloss:yol bulunsun ve izlensin diye ateş yakarlardı, source:"ن و ر,B005"}. Surede ise ateş yolun sonunda düşülen yerdir. Yolun ters yönü sekizinci ayetteki bir kelimede saklıdır: {ar:عِندَ, tr:inde, gloss:yanında, source:98:8} kelimesinin kökü yoldan sapan deveyi ve dizgini çekip kaçanı anlatır: {ar:العاند البعير الذي يجور عن الطريق ويعدل عن القصد, tr:el-âniüd, gloss:yoldan sapıp hedeften dönen deve, source:"ع ن د,B002"}; {ar:استعند البعير إذا غلب قائده على الزمام, tr:ista'nede'l-ba'îr, gloss:deve dizginde yedeğindekine galip geldi, source:"ع ن د,B001"}. İnsana dönük anlamı bilerek reddetmektir: {ar:المعاندة أن يعرف الرجل الشيء ويأبى أن يقبله, tr:el-muâneda, gloss:inat, bir şeyi bilip kabul etmekten kaçınmaktır, source:"ع ن د,B001"}. Sekizinci ayetteki inde rabbihim varılan yerdir, sapma değil; ama kökün arka planı dördüncü ayetteki ayrılığa bir ad verir: kanıt geldikten, yol işaretlenip düzleştikten sonra dizgini çekip kaçmak.

Kur'an yolu bu parçalarla sahneler. En'âm suresindeki öğütte yol ve yan patikalar ve ayrı düşüş bir aradadır: {ar:وَأَنَّ هَٰذَا صِرَٰطِى مُسْتَقِيمًۭا فَٱتَّبِعُوهُ ۖ وَلَا تَتَّبِعُوا۟ ٱلسُّبُلَ فَتَفَرَّقَ بِكُمْ عَن سَبِيلِهِۦ, tr:ve enne hâzâ sırâtî müstakîmen fettebiûh, ve lâ tettebiu's-sübüle feteferraka biküm an sebîlih, gloss:bu benim dosdoğru yolumdur, ona uyun; başka yollara uymayın, sizi O'nun yolundan ayırıp dağıtır, source:6:153}. Aynı surede Peygamber'e şöyle demesi söylenir: {ar:هَدَىٰنِى رَبِّىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ دِينًۭا قِيَمًۭا مِّلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا ۚ وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ, tr:hedânî rabbî ilâ sırâtin müstakîmin dînen kıyemen millete İbrâhîme hanîfâ, ve mâ kâne mine'l-müşrikîn, gloss:Rabbim beni dosdoğru bir yola, dimdik bir dine, hanif İbrahim'in milletine iletti; o müşriklerden değildi, source:6:161}; yol, kayyim, hanif ve müşrik tek ayettedir. İbrahim'in kendi sözü de yön çevirmedir: {ar:إِنِّى وَجَّهْتُ وَجْهِىَ لِلَّذِى فَطَرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ حَنِيفًۭا, tr:innî veccehtü vechiye li'llezî fatara's-semâvâti ve'l-arda hanîfâ, gloss:ben yüzümü gökleri ve yeri yaratana hanif olarak çevirdim, source:6:79}. Âl-i İmrân ve Nahl sureleri İbrahim'i aynı karşıtlıkla anar: {ar:وَلَٰكِن كَانَ حَنِيفًۭا مُّسْلِمًۭا وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ, tr:ve lâkin kâne hanîfen müslimen ve mâ kâne mine'l-müşrikîn, gloss:o hanif bir müslümandı, müşriklerden değildi, source:3:67}; {source:16:120}. Rûm suresinde emir yüzü dine doğrultmaktır: {ar:فَأَقِمْ وَجْهَكَ لِلدِّينِ حَنِيفًۭا, tr:fe-ekım vecheke li'd-dîni hanîfâ, gloss:yüzünü hanif olarak dine doğrult, source:30:30}, ayet {ar:ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ, tr:zâlike'd-dînü'l-kayyim, gloss:dosdoğru din budur, source:30:30} diye biter. Nahl suresinde yolun doğrusu ve sapanı Allah'ın nimetleri arasında sayılır: {ar:وَعَلَى ٱللَّهِ قَصْدُ ٱلسَّبِيلِ وَمِنْهَا جَآئِرٌۭ, tr:ve ala'llâhi kasdü's-sebîli ve minhâ câir, gloss:yolun doğrusunu göstermek Allah'a aittir, yollardan sapan da vardır, source:16:9}; biraz sonra yol işaretleri anılır {source:16:16}. Gece yolculuğunda Musa bir ateş görür ve onda yol bulmayı umar: {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ev ecidü ale'n-nâri hüdâ, gloss:ya da ateşin başında bir yol gösteren bulurum, source:20:10}. Uysallaştırma da bir nimettir: Yâsîn suresinde hayvanlar için {ar:وَذَلَّلْنَٰهَا لَهُمْ فَمِنْهَا رَكُوبُهُمْ, tr:ve zellelnâhâ lehüm fe-minhâ rakûbühüm, gloss:onları kendilerine boyun eğdirdik, bir kısmı binekleridir, source:36:72} denir; Mülk suresinde yer {ar:ذَلُولًۭا, tr:zelûlâ, gloss:boyun eğen, yürünmeye elverişli, source:67:15} kılınmıştır. Ters yüzü Kâf suresinde, cehenneme atılma emrindedir: {ar:أَلْقِيَا فِى جَهَنَّمَ كُلَّ كَفَّارٍ عَنِيدٍۢ, tr:elkıyâ fî cehenneme külle keffârin anîd, gloss:her inatçı nankörü cehenneme atın, source:50:24}; küfür ve inat kökleri bir arada. Tevbe suresi ise beşinci ayetin sözünü kitap ehli için tekrarlar: {ar:وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوٓا۟ إِلَٰهًۭا وَٰحِدًۭا, tr:ve mâ umirû illâ li-ya'budû ilâhen vâhidâ, gloss:onlara ancak tek bir ilaha kulluk etmeleri emredilmişti, source:9:31}.

Kaynaklar: 98:5 لِيَعْبُدُوا۟ ع ب د B003 B005; 98:5 ٱلدِّينَ د ي ن B001; 98:5 أُمِرُوٓا۟ ء م ر B005; 98:4 تَفَرَّقَ ف ر ق B006; 98:1 وَٱلْمُشْرِكِينَ ش ر ك B005; 98:5 حُنَفَآءَ ح ن ف B003; 98:5 ٱلْقَيِّمَةِ ق و م B008; 98:6 نَارِ ن و ر B005; 98:8 عِندَ ع ن د B001 B002

## Örten ve örtülen: tohum, su, bahçe

Surenin ilk eyleyenleri ve son mekânı aynı kök imgesini paylaşır: örtmek. Küfrün kökü {ar:كل شيء غطى شيئا فقد كفره, tr:küllü şey'in gattâ şey'en fekad keferahû, gloss:bir şeyi örten her şey onu kefr etmiştir, source:"ك ف ر,B001"} diye tanımlanır; inanç anlamı da buradan gelir: {ar:الكفر ضد الإيمان سمى لأنه تغطية الحق, tr:el-küfrü ziddü'l-îmân, gloss:küfür imanın karşıtıdır; hakkı örtmek olduğu için bu adı aldı, source:"ك ف ر,B003"}. Gece de bir örtücüdür: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylü kâfir, gloss:gece kâfirdir, çünkü karanlığıyla örter, source:"ك ف ر,B002"}. Cennet kelimesinin kökü de örtmektir ve aynı geceyi taşır: {ar:الجيم والنون أصل واحد وهو الستر والتستر, tr:el-cîm ve'n-nûn aslün vâhid, gloss:cim ve nun tek bir köktür, örtmek ve örtünmektir, source:"ج ن ن,B001"}; {ar:جن عليه الليل وأجنه الليل إذا أظلم حتى يستره بظلمته, tr:cenne aleyhi'l-leyl, gloss:gece onun üstüne karardı, karanlığıyla onu örttü, source:"ج ن ن,B002"}. Her iki kök kabri de adlandırır: {ar:الكفر أيضا القبر, tr:el-kefru eyden el-kabr, gloss:kefr kabir anlamına da gelir, source:"ك ف ر,B012"}; {ar:جننت الميت وأجننته أي واريته والجنن القبر, tr:cenentü'l-meyyit, gloss:ölüyü gömdüm; cenen kabirdir, source:"ج ن ن,B009"}.

Bu örtme bir tarlada somutlaşır. Küfrün kökü, tohumu toprakla örten çiftçiyi adlandırır: {ar:الكافر الزارع لأنه يغطي البذر بالتراب, tr:el-kâfiru ez-zâri', gloss:kâfir, ekincidir, çünkü tohumu toprakla örter, source:"ك ف ر,B008"}; hurma tomurcuğunu saran kını da: {ar:الكافور الطلع ووعاء طلع النخل, tr:el-kâfûr et-tal', gloss:kâfûr, hurmanın tomurcuğu ve onu saran kın, source:"ك ف ر,B010"}. Toprağa su getirilir: {ar:الأتي الجدول يؤتيه الرجل إلى أرضه, tr:el-etiyyü el-cedvel, gloss:etî, adamın toprağına getirdiği arktır, source:"ء ت ي,B004"}; bu, dördüncü ayetteki ûtû kelimesinin köküdür. Ekin büyür: {ar:زكا الزرع يزكو زكاء ازداد ونما, tr:zekâ'z-zer'u yezkû zekâen, gloss:ekin arttı ve büyüdü, source:"ز ك و,B001"}. Hurma ürün verir ve bu ürünün tanımı surenin iki kelimesini birden içerir: {ar:إتاء النخلة ريعها وزكاؤها وكثرة ثمارها, tr:itâu'n-nahleti rîuhâ ve zekâuhâ, gloss:hurmanın itâsı, getirisi, büyümesi ve meyvesinin bolluğudur, source:"ء ت ي,B007"}. Beşinci ayetteki {ar:وَيُؤْتُوا۟ ٱلزَّكَوٰةَ, tr:ve yü'tu'z-zekât, gloss:zekâtı versinler, source:98:5} sözü, düz anlamıyla bir vermedir; arka planında hurmanın büyüyüp ürününü vermesi duyulur. Emir kelimesinin kökü de artışı anlatır: {ar:الأمر النماء والبركة, tr:el-emeru en-nemâu ve'l-bereke, gloss:emer, büyüme ve bereket, source:"ء م ر,B004"}.

Sekizinci ayet bu ekimi tamamlar: {ar:جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ, tr:cennâtü adnin tecrî min tahtihe'l-enhâr, gloss:altlarından ırmaklar akan Adn cennetleri, source:98:8}. Cennet ağaçlarıyla toprağı örten bahçedir: {ar:كل بستان ذي شجر يستر بأشجاره الأرض, tr:küllü bustânin zî şecer, gloss:ağaçlarıyla toprağı örten her bahçe, source:"ج ن ن,B003"}; Araplar hurmalığa da cennet der: {ar:العرب تسمي النخيل جنة, tr:el-arabü tüsemmi'n-nahîle cenneten, gloss:Araplar hurma ağaçlarına cennet der, source:"ج ن ن,B003"}. Irmak toprağı yararak akar: {ar:سمي النهر لأنه ينهر الأرض أي يشقها, tr:sümmiye'n-nehru li-ennehû yenheru'l-ard, gloss:nehir, toprağı yardığı için bu adı aldı, source:"ن ه ر,B001"}. Su aşağıda, bahçe yukarıdadır. Rab kelimesinin kökü bitkiyi besleyen bulutu ve bir şeyi adım adım olgunluğa erdirmeyi de anlatır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb, gloss:rabâb buluttur, bitkiyi beslediği için bu adı aldı, source:"ر ب ب,B008"}; {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, gloss:terbiye, bir şeyi hâlden hâle olgunluk sınırına kadar geliştirmektir, source:"ر ب ب,B002"}. Ödülün kendisi de örtülüdür: {ar:الجنة… ثواب مستور عنهم اليوم, tr:el-cenne sevâbün mestûr, gloss:cennet, bugün onlardan örtülü olan karşılıktır, source:"ج ن ن,B004"}. Aynı ayetin son kelimesinin kökü ise kurumuş hurmayı da adlandırır: {ar:الخشو الحشف من التمر, tr:el-haşvü el-haşefü mine't-temr, gloss:haşv, hurmanın kurusu, işe yaramazı, source:"خ ش ي,B004"}; ayetin düz anlamı ise rabbinden korkmaktır.

Sure böylece örtenlerle açılır ve örtülü bahçeyle kapanır. Birinci ayetteki örtü hakkı gizler; sekizinci ayetteki örtü ödülü saklar ve gölge verir. Arka planda tohumu örten çiftçi ile ağaçlarıyla toprağı örten bahçe arasında bir süreç duyulur: örtülen tohum, getirilen su, büyüyen ekin, ürün veren hurma ve altından ırmak akan bahçe.

Kur'an bu imgeleri başka yerlerde açıkça sahneler. Hadîd suresinde dünya hayatının temsilinde {ar:كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ, tr:ke-meseli gaysin a'cebe'l-küffâra nebâtüh, gloss:bitkisi ekincileri hayran bırakan bir yağmur gibi, source:57:20} denir; burada küffâr ekincilerdir ve ekin sonra sararıp çer çöp olur. Fetih suresinde ekin {ar:يُعْجِبُ ٱلزُّرَّاعَ لِيَغِيظَ بِهِمُ ٱلْكُفَّارَ, tr:yu'cibü'z-zürrâa li-yağîza bihimü'l-küffâr, gloss:ekincileri hayran bırakır, onlarla kâfirleri öfkelendirir, source:48:29}; ayet surenin yedinci ayetinin sözüyle biter: {ar:وَعَدَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ, tr:ve aded'llâhü'llezîne âmenû ve amilu's-sâlihât, gloss:Allah iman edip salih ameller işleyenlere vaat etti, source:48:29}. Kehf suresindeki iki adam temsilinde {ar:كِلْتَا ٱلْجَنَّتَيْنِ ءَاتَتْ أُكُلَهَا, tr:kilte'l-cenneteyni âtet ukülehâ, gloss:iki bahçe de ürününü verdi, source:18:33} denir, aynı ayette aralarından bir ırmak fışkırtılır; itâ fiili ürün için kullanılmıştır. Bakara suresinde infak edenlerin temsili de {ar:فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ, tr:fe-âtet ukülehâ dı'feyn, gloss:ürününü iki kat verdi, source:2:265} der; İbrâhîm suresinde güzel ağaç {ar:تُؤْتِىٓ أُكُلَهَا كُلَّ حِينٍۭ بِإِذْنِ رَبِّهَا, tr:tü'tî ukülehâ külle hînin bi-izni rabbihâ, gloss:Rabbinin izniyle her zaman ürününü verir, source:14:25}. Bakara suresinin bir başka temsili surenin bahçesini ve ateşini tek sahnede toplar: {ar:جَنَّةٌۭ مِّن نَّخِيلٍۢ وَأَعْنَابٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ, tr:cennetün min nahîlin ve a'nâbin tecrî min tahtihe'l-enhâr, gloss:altından ırmaklar akan hurma ve üzüm bahçesi, source:2:266}, sonra {ar:فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ, tr:fe-esâbehâ i'sârun fîhi nârun fahtarakat, gloss:ona içinde ateş bulunan bir kasırga isabet etti ve yandı, source:2:266}. Tâhâ suresinde Firavun'un iman eden sihirbazları, surenin sekizinci ayetini zekâtın köküne bağlayan sözü söyler: {ar:جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ, tr:cennâtü adnin tecrî min tahtihe'l-enhâru hâlidîne fîhâ, ve zâlike cezâu men tezekkâ, gloss:altlarından ırmaklar akan, içinde temelli kalacakları Adn cennetleri; bu, arınanın karşılığıdır, source:20:76}. Örtünün geceye bakan yüzü İbrahim'in gecesindedir: {ar:فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ رَءَا كَوْكَبًۭا, tr:felemmâ cenne aleyhi'l-leylü raâ kevkebâ, gloss:gece üstüne çöküp onu örtünce bir yıldız gördü, source:6:76}. Gizli ödül Secde suresinde de karşılık adıyla anılır: {ar:فَلَا تَعْلَمُ نَفْسٌۭ مَّآ أُخْفِىَ لَهُم مِّن قُرَّةِ أَعْيُنٍۢ جَزَآءًۢ بِمَا كَانُوا۟ يَعْمَلُونَ, tr:felâ ta'lemü nefsün mâ uhfiye lehüm min kurrati a'yün, cezâen bimâ kânû ya'melûn, gloss:yaptıklarına karşılık olarak onlar için gizlenmiş göz aydınlığını hiç kimse bilmez, source:32:17}. İnsan suresinde iyilerin içtiği kâfûr da aynı kökün bahçedeki yüzüdür: {ar:يَشْرَبُونَ مِن كَأْسٍۢ كَانَ مِزَاجُهَا كَافُورًا, tr:yeşrabûne min ke'sin kâne mizâcühâ kâfûrâ, gloss:katkısı kâfur olan bir kadehten içerler, source:76:5}.

Kaynaklar: 98:1 كَفَرُوا۟ ك ف ر B001 B002 B003 B008 B010 B012; 98:8 جَنَّٰتُ ج ن ن B001 B002 B003 B004 B009; 98:4 أُوتُوا۟ ء ت ي B004; 98:5 وَيُؤْتُوا۟ ء ت ي B007; 98:5 ٱلزَّكَوٰةَ ز ك و B001; 98:5 أُمِرُوٓا۟ ء م ر B004; 98:8 ٱلْأَنْهَٰرُ ن ه ر B001; 98:8 رَبِّهِمْ ر ب ب B002 B008; 98:8 خَشِىَ خ ش ي B004

## Yerinde kalmak ve ayrılmamak

Sure, süren bir hâlle açılır: lem yekün ... münfekkîn, "ayrılıp geri kalmıyorlardı". {ar:لا ينفك يفعل ذلك بمعنى لا يزال, tr:lâ yenfekkü yef'alü zâlik, gloss:onu yapmaktan geri kalmaz, yani yapmayı sürdürür, source:"ف ك ك,B003"}. Sure süren bir yurtla kapanır: {ar:جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ, tr:cezâühüm inde rabbihim cennâtü adn, gloss:Rableri katındaki karşılıkları Adn cennetleridir, source:98:8} ve {ar:خَٰلِدِينَ فِيهَآ أَبَدًۭا, tr:hâlidîne fîhâ ebedâ, gloss:orada ebedî olarak kalacaklar, source:98:8}. Sekizinci ayetin birçok kökü bir yerde kalıp ondan ayrılmamak için aynı kullanımı paylaşır. Hulûd sebat ve bağlılıktır: {ar:أصل واحد يدل على الثبات والملازمة, tr:aslün vâhidün yedüllü ale's-sebâti ve'l-mülâzeme, gloss:sabit kalmaya ve ayrılmamaya delalet eden tek kök, source:"خ ل د,B001"}; {ar:أخلد بالمكان أقام به, tr:ahlede bi'l-mekân, gloss:o yerde kaldı, source:"خ ل د,B002"}. Ebed için de aynısı söylenir: {ar:أبدت بالمكان إذا أقمت به ولم تبرحه, tr:ebedtü bi'l-mekân, gloss:o yerde kaldım ve ondan ayrılmadım, source:"ء ب د,B006"}. Rab kelimesinin kökü de: {ar:أرب فلان بالمكان إذا أقام به فلم يبرحه, tr:erabbe fülânün bi'l-mekân, gloss:filan o yerde kaldı ve ondan ayrılmadı, source:"ر ب ب,B007"}. Adn kelimesinin kökü için Arapçada {ar:عدن بالمكان أقام به, tr:adene bi'l-mekân, gloss:o yerde yerleşip kaldı, source:"memory"} denir; aynı kökten gelen {ar:المعدن, tr:el-ma'din, gloss:bir şeyin kaynağı, çıktığı yer, source:"memory"} kelimesi de vardır. Beşinci ayetteki yükîmû fiilinin aynı kalıbı bir yerde ikamet etmeyi anlatır: {ar:أقمت بالمكان إقامة ومقاما, tr:ekamtü bi'l-mekân, gloss:o yerde ikamet ettim, source:"ق و م,B006"}. İnde yakınlıktır: {ar:عند لفظ موضوع للقرب, tr:inde lafzun mevdûun li'l-kurb, gloss:inde yakınlık için konmuş bir sözdür, source:"ع ن د,B004"}. Birinci ayetteki ehl kelimesi ise içinde sahipleri bulunan evi ve "hoş geldin" sözünü taşır: {ar:منزل آهل أي به أهله, tr:menzilün âhil, gloss:içinde ahalisi olan ev, source:"ء ه ل,B004"}; {ar:مرحبا وأهلا أي أتيت سعة وأتيت أهلا فاستأنس ولا تستوحش, tr:merhaben ve ehlen, gloss:genişliğe ve aileye geldin, ısın, yabancılık çekme, source:"ء ه ل,B005"}.

Bu kökler surenin hareketini bir yerleşme olarak duyurur. Birinci ayette bir topluluk kendi hâlinde sürüp gider; dördüncü ayette ayrılır ve aralarına mesafe girer; altıncı ve sekizinci ayetlerde aynı hâlidîne fîhâ iki farklı yere bağlanır: ateş ve bahçe. Ebed kelimesinin kökü ters yüzü de taşır: {ar:تأبد المنزل أي أقفر وألفته الوحوش, tr:teebbede'l-menzil, gloss:konak ıssızlaştı, yabani hayvanlar ona alıştı, source:"ء ب د,B003"}; {ar:تأبد البعير توحش, tr:teebbede'l-ba'îr, gloss:deve yabanileşti, source:"ء ب د,B002"}. İçinde ahalisi olan ev ile yabani hayvanlara kalmış ıssız konak aynı kökün iki ucudur; sekizinci ayetteki ebedâ, ahalisi içinde, Rableri katında sürüp giden bir oturuşu söyler.

Kur'an bu yerleşmeyi başka yerlerde de anlatır. Kehf suresinde iman edip salih amel işleyenler için firdevs cennetleri bir konuk ağırlaması olarak hazırlanır {source:18:107} ve oradakiler {ar:خَٰلِدِينَ فِيهَا لَا يَبْغُونَ عَنْهَا حِوَلًۭا, tr:hâlidîne fîhâ lâ yebğûne anhâ hivelâ, gloss:orada temelli kalırlar, oradan ayrılmak istemezler, source:18:108}. Fâtır suresinde Adn cennetlerine girenler {source:35:33} şöyle der: {ar:ٱلَّذِىٓ أَحَلَّنَا دَارَ ٱلْمُقَامَةِ مِن فَضْلِهِۦ, tr:ellezî ehallenâ dâra'l-mukâmeti min fadlih, gloss:lütfuyla bizi kalınacak yurda yerleştiren, source:35:35}; mukâme, yükîmû fiilinin köküdür. Duhân suresinde takva sahipleri {ar:فِى مَقَامٍ أَمِينٍۢ, tr:fî makâmin emîn, gloss:güvenli bir makamdadır, source:44:51}; Kamer suresinde {ar:فِى مَقْعَدِ صِدْقٍ عِندَ مَلِيكٍۢ مُّقْتَدِرٍۭ, tr:fî mak'adi sıdkın inde melîkin muktedir, gloss:güçlü bir hükümdarın yanında doğruluk oturağında, source:54:55}. Tevbe suresinde Allah müminlere {ar:وَمَسَٰكِنَ طَيِّبَةًۭ فِى جَنَّٰتِ عَدْنٍۢ, tr:ve mesâkine tayyibeten fî cennâti adn, gloss:Adn cennetlerinde güzel meskenler, source:9:72} vaat eder. Kâf suresinde cennet yakına getirilir: {ar:وَأُزْلِفَتِ ٱلْجَنَّةُ لِلْمُتَّقِينَ غَيْرَ بَعِيدٍۢ, tr:ve ü'zlifeti'l-cennetü li'l-müttekîne gayra ba'îd, gloss:cennet takva sahiplerine yaklaştırılır, uzak değildir, source:50:31}; dördüncü ayetteki uzaklığın tersidir. Yanlış bir kalış da vardır: A'râf suresinde ayetlerden yüz çeviren adam için {ar:وَلَٰكِنَّهُۥٓ أَخْلَدَ إِلَى ٱلْأَرْضِ, tr:ve lâkinnehû ahlede ile'l-ard, gloss:ama o yere yapışıp kaldı, source:7:176} denir. Muhammed suresi ise iki kalışı karşı karşıya koyar: ırmaklı cennet {ar:كَمَنْ هُوَ خَٰلِدٌۭ فِى ٱلنَّارِ, tr:ke-men hüve hâlidün fi'n-nâr, gloss:ateşte temelli kalan kimse gibi midir, source:47:15}.

Kaynaklar: 98:1 مُنفَكِّينَ ف ك ك B003; 98:5 وَيُقِيمُوا۟ ق و م B006; 98:6 خَٰلِدِينَ خ ل د B001; 98:8 خَٰلِدِينَ خ ل د B001 B002; 98:8 أَبَدًا ء ب د B002 B003 B006; 98:8 رَبِّهِمْ ر ب ب B007; 98:8 عَدْنٍ (memory); 98:8 عِندَ ع ن د B004; 98:1 أَهْلِ ء ه ل B004 B005

## Hesap: borç, rehin, kefil, ödeme ve ibra

Din kelimesi itaattir; borç vermek ve almak da bu köktedir: {ar:الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء, tr:ed-deyn ve dâyentü fülânen, gloss:deyn; filanla alarak ya da vererek borç alışverişi yaptım, source:"د ي ن,B003"}; ve din karşılığın kendisidir: {ar:الدين الجزاء والمكافأة, tr:ed-dînü el-cezâü ve'l-mükâfee, gloss:din, karşılık ve bedeldir, source:"د ي ن,B002"}. Ceza da borcun ödenmesi ve tahsilidir: {ar:جزيت فلانا حقه؛ جزيته قرضه, tr:cezeytü fülânen hakkahû, gloss:filana hakkını ödedim; borcunu ödedim, source:"ج ز ي,B002"}; {ar:تجازيت ديني على فلان إذا تقاضيته, tr:tecâzeytü deynî alâ fülân, gloss:filandaki alacağımı tahsil ettim, source:"ج ز ي,B003"}. Bu son cümle ceza ile din köklerini birleştirir. Karşılığın ölçüsü de verilir: {ar:الجزاء ما فيه الكفاية من المقابلة إن خيرا فخير وإن شرا فشر, tr:el-cezâü mâ fîhi'l-kifâyetü mine'l-mukâbele, in hayran fe-hayr ve in şerran fe-şer, gloss:ceza, karşılıkta yeterli olandır: iyilikse iyilik, kötülükse kötülük, source:"ج ز ي,B001"}. Bu tanım altıncı ve yedinci ayetlerdeki şerr ve hayr kelimelerini sekizinci ayetteki {ar:جَزَآؤُهُمْ, tr:cezâühüm, gloss:karşılıkları, source:98:8} kelimesine bağlar.

Hesabın diğer parçaları surenin başka kelimelerinde durur. İnfikâkın kökü rehnin çözülmesidir: {ar:فك الرقبة تخليصها من إسار الرق وفك الرهن وفكاكه تخليصه من غلق الرهن, tr:fekkü'r-rakabeti tahlîsuhâ min isâri'r-rıkk ve fekkü'r-rehn, gloss:boynu çözmek onu kölelik bağından kurtarmak, rehni çözmek onu rehin kilidinden kurtarmaktır, source:"ف ك ك,B002"}; açıklamada kurtarmak için kullanılan tahlîs, muhlisîn kelimesinin köküdür. Berîye kelimesinin kökü borçtan aklanmaktır: {ar:برئت من الديون, tr:beri'tü mine'd-düyûn, gloss:borçlardan kurtuldum, source:"ب ر ء,B004"}. Tilâvetin kökü borcun kalanını ve alacağın devrini anlatır: {ar:التلية بقية الدين, tr:et-tuliyyetü bakıyyetü'd-deyn, gloss:tuliyye, borcun kalanıdır, source:"ت ل و,B003"}. Kitabın kökü, kölenin bedelini taksitle ödeyip özgürlüğünü satın aldığı sözleşmedir: {ar:المكاتب العبد يكاتب على نفسه بثمنه فإذا سعى وأداه عتق, tr:el-mükâteb, gloss:mükâteb, kendi bedeli üzerine yazılı anlaşma yapan köledir; çalışıp ödeyince özgür olur, source:"ك ت ب,B005"}. Kayyime bir şeyin biçilen değeridir: {ar:القيمة ثمن الشيء بالتقويم, tr:el-kıymetü semenü'ş-şey'i bi't-takvîm, gloss:kıymet, değer biçmeyle belirlenen bedel, source:"ق و م,B010"}. Surenin üç kelimesi kefili adlandırır: {ar:كنت على فلان أكون كونا أي تكفلت به, tr:küntü alâ fülân, gloss:filana kefil oldum, source:"ك و ن,B003"}; {ar:الجري الضامن, tr:el-cerî ed-dâmin, gloss:cerî, kefildir, source:"ج ر ي,B003"}; {ar:الرضي المطيع والرضي المحب والرضي الضامن, tr:er-radiyy, gloss:radî, itaat eden, seven ve kefil olandır, source:"ر ض و,B006"}.

Ödemenin ters yönü de vardır. Gelmek kökü haracı adlandırır ve ceza köküyle eşitlenir: {ar:الإتاوة الخراج أو الجزية يؤديه القوم إلى الملك, tr:el-itâve el-harâc evi'l-cizye, gloss:itâve, bir topluluğun hükümdara ödediği harac ya da cizye, source:"ء ت ي,B008"}. Cizye de üzerindekini ödemektir: {ar:الجزية … سميت جزية لأنها قضاء منه لما عليه, tr:el-cizye, gloss:cizye, üzerindeki borcu ödemesi olduğu için bu adı aldı, source:"ج ز ي,B004"}. Gönüllü verişin de bir adı vardır: {ar:إلا من أعطى في رسلها أي بطيب نفس منه, tr:illâ men a'tâ fî rislihâ, gloss:gönül hoşluğuyla veren hariç, source:"ر س ل,B010"}; hayr da hibe ve maldır: {ar:الخير الهبة, tr:el-hayru el-hibe, gloss:hayır, bağıştır, source:"خ ي ر,B005"}. Zekât, insanın Allah hakkı olarak fakirlere çıkardığıdır: {ar:ما يخرج الإنسان من حق الله تعالى إلى الفقراء, tr:mâ yuhricü'l-insânu min hakkı'llâh, gloss:insanın Allah hakkından fakirlere çıkardığı, source:"ز ك و,B003"}.

Bu kelimelerle sure bir hesap olarak duyulur. Dördüncü ayette kitap verilir; beşinci ayette verilenlerden din, yani borç bilinciyle sürdürülen bir itaat ve zekâtın verilmesi istenir; altıncı ve yedinci ayetlerde hayr ve şerr tartılır; sekizinci ayette ödeme yapılır ve hesap Rableri katında, {ar:عِندَ رَبِّهِمْ, tr:inde rabbihim, gloss:Rableri katında, source:98:8}, emanet gibi saklanır. Hesap karşılıklı bir hoşnutlukla kapanır: {ar:رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ, tr:radıya'llâhü anhüm ve radû anh, gloss:Allah onlardan razı olmuş, onlar da O'ndan razı olmuşlardır, source:98:8}; {ar:المراضاة من اثنين, tr:el-murâdâtü mine'sneyn, gloss:murâdât iki taraf arasında olur, source:"ر ض و,B003"}. Alışverişin sonunda iki tarafın birbirinden razı olması gibi.

Kur'an borcu, yazıyı ve ödemeyi açıkça birleştirir. Bakara suresinde müminlere {ar:إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ, tr:izâ tedâyentüm bi-deynin ilâ ecelin müsemmen fektübûh, gloss:belirli bir süreye kadar borçlandığınızda onu yazın, source:2:282} denir. Müddessir suresinde {ar:كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ رَهِينَةٌ, tr:küllü nefsin bimâ kesebet rehîne, gloss:her can kazandığına karşılık rehindir, source:74:38}; Beled suresinde sarp yokuş {ar:فَكُّ رَقَبَةٍ, tr:fekkü rakabe, gloss:bir boyun çözmek, source:90:13} diye açıklanır. Nûr suresinde özgürlük sözleşmesi yazıyla ve vermeyle kurulur: {ar:فَكَاتِبُوهُمْ إِنْ عَلِمْتُمْ فِيهِمْ خَيْرًۭا ۖ وَءَاتُوهُم مِّن مَّالِ ٱللَّهِ ٱلَّذِىٓ ءَاتَىٰكُمْ, tr:fe-kâtibûhüm in alimtüm fîhim hayrâ, ve âtûhüm min mâli'llâhi'llezî âtâküm, gloss:onlarda bir hayır görürseniz onlarla yazılı anlaşma yapın ve Allah'ın size verdiği maldan onlara verin, source:24:33}. Tevbe suresinde Allah müminlerden canlarını ve mallarını satın alır: {ar:بِأَنَّ لَهُمُ ٱلْجَنَّةَ, tr:bi-enne lehümü'l-cenne, gloss:karşılığında cennet onlarındır, source:9:111}. Karşılığın denkliği Nebe' suresinde {ar:جَزَآءًۭ وِفَاقًا, tr:cezâen vifâkâ, gloss:tam denk bir karşılık, source:78:26}, Rahmân suresinde iyilik için söylenir {source:55:60}. Lokmân suresinde o gün kimse kimsenin borcunu ödeyemez: {ar:وَٱخْشَوْا۟ يَوْمًۭا لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ, tr:vahşev yevmen lâ yeczî vâlidün an veledih, gloss:babanın evladı yerine ödeme yapamayacağı günden korkun, source:31:33}; sekizinci ayetin son kelimesindeki haşyet burada da vardır. Fâtiha'daki {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:mâliki yevmi'd-dîn, gloss:din gününün sahibi, source:1:4} ve Bakara suresindeki aynı uyarı {source:2:48} bu hesabın gününü adlandırır. Tevbe suresi müşriklere bir ibra ilanıyla açılır: {ar:بَرَآءَةٌۭ مِّنَ ٱللَّهِ وَرَسُولِهِۦٓ إِلَى ٱلَّذِينَ عَٰهَدتُّم مِّنَ ٱلْمُشْرِكِينَ, tr:berâetün mina'llâhi ve resûlihî ile'llezîne âhedtüm mine'l-müşrikîn, gloss:Allah'tan ve elçisinden, antlaşma yaptığınız müşriklere bir ilişik kesme, source:9:1}. Aynı surede kitap verilenlerin cizyesi {ar:حَتَّىٰ يُعْطُوا۟ ٱلْجِزْيَةَ عَن يَدٍۢ, tr:hattâ yu'tu'l-cizyete an yed, gloss:cizyeyi elden verinceye kadar, source:9:29} diye anılır; muhataplar surenin dördüncü ayetindeki ûtu'l-kitâb'dır. Gönüllü veriş de aynı surededir: sadakalar fakirlere, toplayıcılara, boyunların çözülmesine ve borçlulara verilir {source:9:60}; namazı kılıp zekâtı verenler ise {ar:فَإِخْوَٰنُكُمْ فِى ٱلدِّينِ, tr:fe-ihvânüküm fi'd-dîn, gloss:dinde kardeşlerinizdir, source:9:11}. Karşılıklı hoşnutluk Tevbe suresinde surenin sekizinci ayetinin sözleriyle tekrarlanır: {ar:رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ وَأَعَدَّ لَهُمْ جَنَّٰتٍۢ تَجْرِى تَحْتَهَا ٱلْأَنْهَٰرُ, tr:radıya'llâhü anhüm ve radû anhü ve eadde lehüm cennâtin tecrî tahtehe'l-enhâr, gloss:Allah onlardan razı olmuş, onlar da O'ndan razı olmuşlardır; onlara altlarından ırmaklar akan cennetler hazırlamıştır, source:9:100}; Mâide suresinde de Allah'ın kıyamet günü sözüyle {source:5:119}. Fecr suresinde huzura kavuşmuş cana {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdıyeten mardıyye, gloss:Rabbine razı edici ve razı olunmuş olarak dön, source:89:28} denir.

Kaynaklar: 98:5 ٱلدِّينَ د ي ن B002 B003; 98:8 جَزَآؤُهُمْ ج ز ي B001 B002 B003 B004; 98:1 مُنفَكِّينَ ف ك ك B002; 98:6 ٱلْبَرِيَّةِ ب ر ء B004; 98:2 يَتْلُوا۟ ت ل و B003; 98:1 ٱلْكِتَٰبِ ك ت ب B005; 98:5 ٱلْقَيِّمَةِ ق و م B010; 98:1 يَكُنِ ك و ن B003; 98:8 تَجْرِى ج ر ي B003; 98:8 رَّضِىَ ر ض و B003 B006; 98:5 وَيُؤْتُوا۟ ء ت ي B008; 98:2 رَسُولٌ ر س ل B010; 98:7 خَيْرُ خ ي ر B005; 98:5 ٱلزَّكَوٰةَ ز ك و B003

## Buluşmalar

En yoğun buluşma beşinci ayetteki salât kelimesindedir. Kökü bir yandan ateşte ısıtılıp düzeltilen çubuğu, {ar:صليت العود بالنار, tr:salleytü'l-ûde bi'n-nâr, gloss:çubuğu ateşte ısıtıp yumuşattım, source:"ص ل و,B001"}, öbür yandan ateşe girip yanan kâfiri, {ar:صلى الكافر نارا, tr:sale'l-kâfiru nârâ, gloss:kâfir ateşe girip yandı, source:"ص ل و,B001"}, adlandırır. Aynı ateş iki iş görür: eğri olanı doğrultur ya da yakar. Beşinci ayette ateş bir doğrultma aletidir; altıncı ayette inkâr edenlerin kaldığı yerdir. Doğrultma ile ocak sahneleri böylece tek bir kökün iki işlemi olarak birleşir ve surenin ikiye ayrılan yolunu taşır: kanıttan sonra doğrulup ayağa kalkanlar ve ateşte kalanlar. Aynı kök tuzağı da adlandırır; ama surede salât tuzaktan sıyrılmış olanların fiilidir.

Münfekkîn kelimesi üç sahneyi bir noktada tutar. Kökü tuzaktan kurtulan ceylanı, mührü açılan mektubu ve çözülen rehni anlatır. Birinci ayette bu kelime olumsuzdur: ip çözülmemiş, mühür açılmamış, rehin kurtarılmamıştır, ve bütün bunlar kanıtın gelişine bağlıdır. Rehnin çözülmesini anlatan cümlede infikâkın ve ihlâsın kökü yan yanadır, tuzaktan kurtulmayı anlatan cümlelerde de; bu yüzden birinci ayetteki çözülmeme ile beşinci ayetteki muhlisîn, hem avın hem borçlunun kurtuluşu olarak duyulur. Yazı ile kenet de aynı kelimede buluşur: mühürlü mektubun açılması ile iki çenenin ayrılması tek cümlede verilir ve dördüncü ayette açılan yazının ardından gelen ayrılık bunun devamıdır.

Teferruk kelimesi kenet ile yol sahnesini birleştirir. En'âm suresinde yan yollara uyunca insanların yoldan ayrı düşmesi {source:6:153}, hem çatallanan yolu hem bölünen topluluğu tek cümlede gösterir. Müşriklerin kökü ana yoldan ayrılan küçük patikaları adlandırdığı için dördüncü ayetteki ayrılık arka planda bir çatal noktasına, beşinci ayetteki hunefâ ise yan patikadan ana yola dönüşe dönüşür. Yol ile binek sahnesi müzellel kelimesinde birleşir: yürünmekle düzleşen yol ile katranla uysallaşan deve aynı kelimeyle anlatılır ve inde kelimesinin kökü ikisinin de tersini, yoldan sapan ve dizgini çeken deveyi verir. Doğrultma ile yol da kayyime kelimesinde birleşir: dik duran beden ile düz hat üzerindeki yol aynı kökle anlatılır; En'âm suresinde Peygamber'e söyletilen söz {source:6:161} yolu, kayyim olanı, hanifi ve müşrikleri tek ayette toplar.

Arındırma ile ekim zekâtta birleşir. Zekât hem bir temizliktir hem ekinin büyümesi ve hurmanın ürünüdür. Tâhâ suresinde surenin sekizinci ayetinin bahçesi tam olarak bu kelimeyle bağlanır: Adn cennetleri {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76}. Beşinci ayetteki zekât, sekizinci ayetteki bahçenin tohumu gibi durur. Arındırma ile hesap da hayr ve şerr kelimelerinde buluşur: süzmenin iki ürünü, karşılığın iki ölçüsüne dönüşür, iyiliğe iyilik ve kötülüğe kötülük.

Örtü ile ocak da kesişir: küfrün kökü üstü örtülmüş külü adlandırır. Örtü ile ekim ise aynı kelimede, tohumu örten çiftçide buluşur. Bakara suresindeki temsil {source:2:266} bu sahnelerin üçünü birden tutar: altından ırmaklar akan hurma bahçesi ve onu yakan ateşli kasırga. Altıncı ve sekizinci ayetler aynı sözü, hâlidîne fîhâ, ateş ve bahçe için kullanır; hulûdun kökü bir yandan ateşin içinde kalan ocak taşlarını, öbür yandan bir yerde yerleşip kalmayı adlandırır. Kalmanın iki yeri böylece aynı kelimede yan yana durur.

Bu buluşmalar surenin hareketini taşır. Birinci ayette bir şey kapalıdır: ilmek düğümlü, mühür kırılmamış, topluluk kendi hâlinde. Kanıt bir elçinin elinde, arındırılmış sayfalar olarak gelir ve okunur. Dördüncü ayette topluluk bu kanıtın ardından bölünür. Beşinci ayet çıkış yolunu tek cümlede verir: işaretli, düzleşmiş, dosdoğru bir yol; katkısından süzülmüş bir din; ateşte doğrultulan bir beden; tuzaktan sıyrılış; ürün veren bir ekin. Altıncı ve yedinci ayetler sonucu iki uca ayırır. Sekizinci ayet bir yerleşmeyle biter: Rableri katında, örtülü bir bahçede, ebedî bir kalış ve iki tarafın birbirinden razı olduğu kapanmış bir hesap.

