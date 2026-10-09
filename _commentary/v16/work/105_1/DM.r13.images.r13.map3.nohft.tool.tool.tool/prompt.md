Focus: 105:1. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/105_1/D.r13/context.md =====
# 105:1 — focus

أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَٰبِ ٱلْفِيلِ

Anchor translation (canonical reading, reference only):

Rabbinin fil sahiplerine ne yaptığını görmedin mi?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | أَلَمْ | لَم |  | INTG;NEG |
| 2 | تَرَ | رَءَا | ر ء ي | V |
| 3 | كَيْفَ | كَيْف | ك ي ف | INTG |
| 4 | فَعَلَ | فَعَلَ | ف ع ل | V |
| 5 | رَبُّكَ | رَبّ | ر ب ب | N;PRON |
| 6 | بِأَصْحَٰبِ | أَصْحَٰب | ص ح ب | P;N |
| 7 | ٱلْفِيلِ | فِيل | ف ي ل | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 105 — full text (context; no pericope)

- 105:1 ◀ focus أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَٰبِ ٱلْفِيلِ
- 105:2 أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍۢ
- 105:3 وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ
- 105:4 تَرْمِيهِم بِحِجَارَةٍۢ مِّن سِجِّيلٍۢ
- 105:5 فَجَعَلَهُمْ كَعَصْفٍۢ مَّأْكُولٍۭ


===== _commentary/v16/work/105_1/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ر ء ي (root_000531) — identity root of تَرَ (w2)

- **B001** gözle ya da içsel kavrayışla görme — gözle ya da içsel kavrayışla görmek · görme, gözle algılama · kendi gözüyle görme · yeni ayı görebilmek için dikkatle bakmaya çalıştık
  نظر وإبصار بعين أو بصيرة (maqayis)؛ رأيت بعيني رؤية ورأيته رأي العين (ayn;tahdhib)؛ الرؤية بالعين (sihah)؛ الرؤية إدراك المرئي بالحاسة (mufradat)
- **B002** düşünüp bir görüşe varma — bilmek, sanmak veya öyle olduğuna inanmak · görüş, kanı veya değerlendirme · düşünüp taşınmak ve bir görüşe varmak · ağır ağır ve dikkatle düşünme · bir görüşe varmak için düşünme · adamın görüşünü sordu · onunla görüş alışverişinde bulundu · gözle gördüğünün gereğince öyle sandı
  الرأي ما يراه الإنسان في الأمر (maqayis)؛ الرأي رأي القلب (ayn;tahdhib)؛ بمعنى العلم تتعدى إلى مفعولين ورأى في الفقه رأيا (sihah)؛ الرأي اعتقاد النفس والروية والتروية التفكر (mufradat)؛ استرأيت الرجل في الرأي أي استشرته (tahdhib)
- **B003** uykuda görülen düş — uykuda görülen düş · uykuda görülen düşler
  الرؤيا معروفة والجمع رؤى (maqayis)؛ رأيت رؤيا حسنة (ayn)؛ رأى في منامه رؤيا وجمع الرؤيا رؤى (sihah)؛ لا تجمع الرؤيا وتجمع الرؤيا رؤى (tahdhib)؛ الرؤيا ما يرى في المنام (mufradat)
- **B004** karşı karşıya gelip görünür olma — topluluk birbirini gördü · görünmek üzere karşıma çıktı · birbirine bakar ve karşılıklı konumda
  تراءى القوم إذا رأى بعضهم بعضا (maqayis)؛ تراءى القوم رأى بعضهم بعضا وتراءى لي فلان (ayn)؛ قوم رئاء وبيوتهم رئاء وتراءى الجمعان (sihah)؛ تراءينا أي تلاقينا فرأيته ورآني وداري ترى دار فلان (tahdhib)؛ تراءا الجمعان أي تقاربا وتقابلا ومنازلهم رئاء (mufradat)
- **B005** başkaları görsün diye yapma — başkaları görsün diye yapma · işini başkalarına gösteriş için yaptı · gösteriş yapmaya zorlandı veya özendi
  وراءى فلان يرائي وفعل ذلك رئاء الناس وهو أن يفعل شيئا ليراه الناس (maqayis)؛ فلان مراء والاسم الرياء وفعل ذلك رياء وسمعة (sihah)؛ يرآءون الناس إذا أبصرهم الناس صلوا وإذا لم يروهم تركوا الصلاة (tahdhib)؛ فعل ذلك رئاء الناس أي مراءاة (mufradat)
- **B006** görünüş, belirti ve yansıtıcı yüzey — ayna · aynada yüzüne baktı · güzel ve parlak dış görünüş · göze güzel görünen durum veya donanım · yüzde beliren budalalık belirtisi
  الرئي ما رأت العين من حال حسنة والرواء حسن المنظر والمرآة معروفة (maqayis)؛ المرآة التي ينظر فيها والري ما أريت القوم من حسن الشارة والهيئة والرواء حسن المنظر (ayn)؛ المرآة التي ينظر فيها والمرآة المنظر الحسن والرواء حسن المنظر ورأوة الحمق (sihah)؛ الرئي المنظر والرواء حسن المنظر والمرآة التي ينظر فيها ورأوة أي نظرة ودمامة (tahdhib)؛ المرآة ما يرى فيه صورة الأشياء (mufradat)
- **B007** aybaşı sonu izi ve denetleme bezi — aybaşı sonrası hafif sarı, beyaz veya bulanık iz · aybaşı belirtisi olarak görülen iz
  الترئية والترية ما تراه الحائض من صفرة بعد دم حيض أو أمارات الحيض (maqayis)؛ الترية الخرقة التي تعرف بها المرأة حيضها من طهرها والماء الأصفر عند انقطاع الدم (jamhara)؛ الترية الشيء الخفي اليسير من الصفرة والكدرة (sihah)؛ الترية ما تراه المرأة من بقية حيضها من صفرة أو بياض (tahdhib)
- **B008** kişiye görünen görünmez yoldaş — kişiye alışıp onunla ilişki kuran görünmez varlık · görünmez yoldaşı ona göründü
  الرئي جني يتعرض للرجل يريه كهانة وطبا (ayn)؛ به رئي من الجن أي مس (sihah)؛ رئي من الجن وهو الذي يعتاد الإنسان من الجن وأرأى إذا صار له رئي من الجن (tahdhib)؛ مع فلان رئي من الجن (mufradat)
- **B009** akciğer ve ona gelen zarar — akciğer · akciğerine vurdu veya sapladı · akciğerinden yakındı
  الرئة موضع الريح والنفس وجمعها الرئات والرئين (ayn)؛ الرئة مهموزة وتجمع على رئين ورأيته أي أصبت رئته (sihah)؛ أرأى إذا اشتكى رئته (tahdhib)؛ الرئة العضو المنتشر عن القلب ورئته إذا ضربت رئته (mufradat)
- **B010** meme gelişmesiyle gebeliğin belli olması — dişi devenin gebeliği memesi gelişince belli oldu · dişi koyunun gebeliği memesi büyüyünce belli oldu
  أرأت الناقة إذا أرأى ضرعها أنها أقربت وأنزلت (ayn)؛ أرأت الشاة إذا عظم ضرعها قبل ولادها (sihah)؛ إذا استبان حمل الشاة وعظم ضرعها قيل أرأت (tahdhib)؛ أرأت الناقة إذا أظهرت الحمل حتى يرى صدق حملها (mufradat)
- **B011** görünür yere dikilen bayrak — dikili bayrak veya görünür işaret · bayrağı dikti
  الراية من رايات الأعلام (ayn)؛ الراية العلم لا تهمزها العرب وأصلها الهمز (tahdhib)؛ الراية العلامة المنصوبة للرؤية (mufradat)
- **B012** gösterip görmesini sağlama — bakması için aynayı ona tuttu · ona gösterip görmesini sağladı · ver, uzat · Tanrı onu düşmanını sevindirecek bir duruma düşürdü
  أرني يا فلان ثوبك لأراه وأرنا للمعاطاة (ayn)؛ أريته الشيء فرآه (sihah)؛ رأيت الرجل ترئية إذا أمسكت له المرآة لينظر فيها وأرى الله الناس بفلان (tahdhib)؛ أرنا وبما أراك الله أي بما علمك (mufradat)
- **B013** söyler misin, bir düşün — söyler misin, bir düşün · söyleyin bakalım, bir düşünün
  أرأيتك وأنت تقول أخبرني (tahdhib)؛ يجري أرأيت مجرى أخبرني وكل ذلك فيه معنى التنبيه (mufradat)

## ف ع ل (root_001167) — identity root of فَعَلَ (w4)

- **B001** bir şeyi yapıp etkileme — bir şeyi yapmak, ortaya çıkarmak veya üzerinde etki bırakmak · yapma işi, eylemin ad eylem biçimi · gerçekleşmiş işin veya eylemin adı · tek bir yapma olayı veya iyi ya da kötü iş · işlerin çoğulu · eylem adı olarak kullanılan biçim · bir etkinin altında değişmek veya ona uymak
  أصل صحيح يدل على إحداث شيء من عمل وغيره (maqayis)؛ فعل يفعل فعلا وفعلا فالفِعل المصدر والفِعل الاسم (ayn)؛ الفِعل بالفتح مصدر فعل يفعل والفِعل بالكسر الاسم (sihah)؛ فعلت الشيء فانفعل كسرته فانكسر (sihah)؛ فعل يفعل فعلا وفعلا فالمصدر مفتوح والاسم مكسور (tahdhib)
- **B002** iyi iş ve kişisel tutum — eli açıklık ve güzel davranış; ayrıca tek kişinin iyi ya da kötü işi
  الفَعال بفتح الفاء الكرم وما يفعل من حسن (maqayis)؛ الفَعال اسم للفعل الحسن مثل الجود والكرم ونحوه (ayn)؛ الفَعال بالفتح الكرم (sihah)؛ الفَعال فعل الواحد خاصة في الخير والشر (tahdhib)؛ الفَعال يكون في المدح والذم (tahdhib)
- **B003** el işçileri — işçiler, özellikle çamur ve kazı işlerinde çalışanlar · marangoz
  الفَعلة العملة وهم قوم يستعملون الطين والحفر وما يشبه ذلك من العمل (ayn)؛ الفَعلة قوم يعملون عمل الطين والحفر وما أشبه ذلك من العمل (tahdhib)؛ النجار يقال له فاعل (tahdhib)
- **B004** uydurup düzme — yalanı, düzme sözü veya anlatıyı uydurmak · sahibince ortaya atılmış veya önceki örneği olmadan yapılmış şey
  افتعل كذبا وزورا أي اختلق (sihah)؛ شعر مفتعل إذا ابتدعه قائله (tahdhib)؛ افتعل فلان حديثا إذا اخترقه (tahdhib)؛ يقال لكل شيء يسوى على غير مثال تقدمه مفتعل (tahdhib)
- **B005** karşılıklı eylem — eylem iki kişi arasında gerçekleştiğinde kullanılan ad
  الفِعال بكسر الفاء إذا كان الفعل بين الاثنين (tahdhib)؛ فإذا كان من فاعلين فهو فِعال (tahdhib)
- **B006** balta ya da keser sapı — balta sapı veya balta gözüne takılan ağaç parça; keser sapı
  يقولون الفَعال خشبة الفأس (maqayis)؛ الفَعال العود الذي يجعل في خرت الفأس يعمل به (tahdhib)؛ في نصاب القدوم سماه فَعالا (tahdhib)
- **B007** dil bilgisi tümleçleri — dil bilgisinde eyleme bağlanan öge türleri · eylemin yöneldiği veya etkilediği şey; nesne · eylemin yapılma amacı veya gerekçesi · yer, zaman veya durum bildirerek eyleme bağlanan öge · eylemin üzerinde gerçekleştiği alanı bildiren öge · doğrudan eylem adı; geçişli veya geçişsiz eylemle kullanılan tür
  المفعولات على وجوه في باب النحو (tahdhib)؛ فمفعول به (tahdhib)؛ ومفعول له (tahdhib)؛ ومفعول فيه (tahdhib)؛ ومفعول عليه (tahdhib)؛ ومفعول بلا صلة وهو المصدر (tahdhib)

## ر ب ب (root_000532) — identity root of رَبُّكَ (w5)

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

## ص ح ب (root_000844) — identity root of بِأَصْحَٰبِ (w6)

- **B001** süreğen eşlik ve yakın birliktelik — eşlik etmek veya birlikte bulunmak · sürekli eşlik eden kimse veya yoldaş · eşlik edenler topluluğu veya yoldaşlar · eşlik etme ve birlikte bulunma durumu · karşılıklı ve süreğen biçimde birlikte bulunma · bir şeyin sahibi veya o şeye sahip kişi · bir topluluğun ya da yöneticinin işini yürüten görevli · ey arkadaşım · iyi ve istekli biçimde arkadaşlık eden · yanında bir eşlikçisi bulunmak
  أصل واحد يدل على مقارنة شيء ومقاربته (maqayis)؛ الصاحب يجمع بالصحب والصحبان والصحبة والصحاب والأصحاب (ayn)؛ الصحب والصحاب والأصحاب والصحابة واحد (jamhara)؛ صحبه يصحبه صحبة وصحابة وجمع الصاحب صحب (sihah)؛ الصاحب الملازم إنسانا كان أو حيوانا أو مكانا أو زمانا (mufradat)؛ المصاحبة والاصطحاب أبلغ من الاجتماع (mufradat)؛ يقال للمالك للشيء هو صاحبه (mufradat)؛ وأصحب الرجل إذا كان ذا صاحب (ayn)
- **B002** eşlik eden koruma ve destek — Tanrı seni korusun · Tanrı onu korumasın · korunmak veya dinginlik ve destek görmek
  صحبك الله أي حفظك (ayn)؛ صحبه الله وأصحبه وصاحبه أي حفظه (jamhara)؛ لا يكون لهم من جهتنا ما يصحبهم من سكينة وروح وترفيق (mufradat)
- **B003** boyun eğip uyumlu duruma gelme — boyun eğmek ve güçlükten sonra uyumlu duruma gelmek · bir kimsenin ardından boyun eğerek gitmek
  أصحب فلان إذا انقاد (maqayis)؛ أصحبت الرجل إذا اتبعته منقادا (jamhara)؛ أصحب البعير والدابة إذا انقاد بعد صعوبة (sihah)؛ الإصحاب للشيء الانقياد له (mufradat)
- **B004** eşlikçi kılmak, yanında götürmek veya uygun düşmek — bir şeyi ona eşlikçi kılmak · kitabı veya başka bir şeyi yanına alıp götürmek · ona uygun düşmek ve onunla bağdaşmak
  كل شيء لاءم شيئا فقد استصحبه (maqayis;ayn;sihah)؛ أصحبته الشيء جعلته له صاحبا (sihah)؛ استصحبته الكتاب وغيره (sihah)؛ أصحب فلان فلانا جعل صاحبا له (mufradat)
- **B005** oğlunun büyüyüp babasına yoldaş olması — oğlu büyüyüp kendisine yoldaş olacak yaşa gelmek
  أصحب الرجل إذا بلغ ابنه (maqayis;sihah)؛ أصحب فلان إذا كبر ابنه فصار صاحبه (mufradat)
- **B006** kılı veya yünü üzerinde bırakılmış deri — kılı veya yünü üzerinde bırakılmış deri, post ya da tulum · hayvanı yüzerken kılı veya yünü deri üzerinde bırakmak
  الأديم إذا ترك عليه شعره مصحب (maqayis)؛ جلد مصحب إذا كان عليه شعره وصوفه (ayn)؛ صحبت المذبوح إذا سلخته وأبقيت على الجلد صوفا أو شعرا (jamhara)؛ أديم مصحب إذا دبغته وتركت عليه بعض الصوف أو الشعر (jamhara)؛ المصحب من الزقاق ما الشعر عليه (sihah)؛ أصحبته إذا تركت صوفه أو شعره عليه (sihah)؛ أديم مصحب أصحب الشعر الذي عليه ولم يجز عنه (mufradat)
- **B007** suyun yüzünü yosun kaplaması — suyun yüzü yosunla kaplanmak
  أصحب الماء إذا علاه الطحلب (maqayis;sihah)
- **B008** kızıla çalan açık toprak renginde eşek — kızıla çalan açık toprak renginde eşek
  حمار أصحب أي أصحر يضرب لونه إلى الحمرة (sihah)

## ف ي ل (root_001193) — identity root of ٱلْفِيلِ (w7)

- **B001** görüşün zayıflaması; görüşü zayıf ve sezgisinde yanılan kişi — görüşü zayıf kişi · görüşü zayıf, sezgisinde yanılan kişi · görüşü zayıflamak · birinin görüşünü zayıflatmak
  أصل يدل على استرخاء وضعف (maqayis)؛ رجل فَيِل الرأي (maqayis;sihah;mufradat)؛ رجل فال أي ضعيف الرأي مخطئ الفراسة (sihah;mufradat)؛ فال الرأي يفيل فيولة وفيل رأيه تفييلا (sihah)
- **B002** kalça çukuru üzerindeki et parçası ya da uyluktaki damar — kalça çukuru üzerindeki et parçası ya da uyluktaki damar · şiirde kalça çevresindeki et ya da damar için kullanılan biçim
  الفائل اللحم الذي على خربة الورك (maqayis;sihah)؛ يجعل الفائل عرقا (maqayis;sihah)؛ عرق في خربة الورك أو لحم عليها (mufradat)
- **B003** toprağa saklanan nesnenin yerini iki bölüm arasında bulma oyunu — toprağa saklanan nesnenin hangi bölümde olduğunu bulma oyunu
  مما شذ عن هذا الباب المفايلة لعبة (maqayis)؛ يخبئون الشيء في التراب ويقسمونه قسمين ويسألون في أيهما هو (maqayis)؛ المفايلة لعبة يخبئون شيئا في التراب ويقسمونه ويقولون في أيها هو (mufradat)
- **B004** uzun hortumlu iri memeli — uzun hortumlu iri memeli · uzun hortumlu iri memeliler · uzun hortumlu iri memeliler · uzun hortumlu iri memeliler · bu hayvanın bakıcısı veya sahibi
  الفيل معروف والجمع أفيال وفيول وفيلة (sihah)؛ صاحبه فيال (sihah)؛ الفيل معروف جمعه فيلة وفيول (mufradat)

## ECHO ر و ي (root_000615) — for تَرَ (w2): withheld observed target; not identity

- **B001** suya kanma ve susuzluğun giderilmesi — susuzluğu sona erinceye kadar su içmek · suya kanmak · suya kanmışlık; susuzluğun sona ermesi · suya kanmış, susuzluğu kalmamış · tatlı ve içeni iyice kandıran bol su · bol sulu pınar
  خلاف العطش (maqayis)؛ رويت من الماء ريا وارتويت وترويت (sihah)؛ روي فلان من الماء يروى ريا فهو ريان (tahdhib)؛ ماء رواء وروى (sihah;tahdhib;mufradat)؛ عين رية (sihah)
- **B002** başkaları için su çekip getirme — ailesine su getirip taşımak · topluluk için su çekmek · su çekmede kullanılan yük hayvanı veya su çeken kişi · su taşımaya yarayan büyük tulum · su taşıma işini meslek edinen kimse · hacıların sonraki günler için su tedarik ettiği gün
  رويت على أهلي أروي ريا (maqayis;sihah;tahdhib)؛ رويت القوم أرويهم إذا استقيت لهم (sihah;tahdhib)؛ الراوية البعير أو البغل أو الحمار الذي يستقى عليه (sihah)؛ الراوية هو البعير الذي يستقى عليه الماء والرجل المستقي أيضا راوية (tahdhib)؛ يوم التروية سمي به لأنهم يرتوون فيه من الماء (sihah;tahdhib)
- **B003** anlatı veya şiir aktarma — anlatıyı veya şiiri aktarmak · anlatı veya şiir aktaran kimse · çok sayıda şiir ya da anlatı aktaran kimse · birine şiiri tekrar ederek ezberletmek
  رويت الحديث والشعر رواية فأنا راو (sihah)؛ روى فلان حديثا وشعرا يرويه رواية فهو راو (tahdhib)؛ روى فلان فلانا شعرا إذا رواه له حتى حفظه للرواية عنه (tahdhib)؛ الذي يأتي القوم بعلم أو خبر فيرويه كأنه أتاهم بريهم من ذلك (maqayis)
- **B004** enine boyuna düşünüp değerlendirme — enine boyuna düşünme; değerlendirme · bir mesele üzerinde düşünüp değerlendirmek
  الرَّوِيَّة التفكر في الأمر (sihah)؛ رويت في الأمر إذا نظرت فيه وفكرت (sihah)؛ روأت في الأمر وريأت فكرت (tahdhib)
- **B005** birinden beklenen ihtiyaç veya talep [kalıp] — birinden beklenen ihtiyaç veya talep
  لنا قبلك روية أي حاجة (sihah)؛ لنا عند فلان روية وأشكلة وهما الحاجة (tahdhib)
- **B006** geriye kalan bölüm veya miktar — borçtan ya da başka bir şeyden kalan miktar
  الرَّوِيَّة البقية من الدين ونحوه (sihah)؛ بقيت منه روية أي بقية مثل التلية (tahdhib)
- **B007** yük bağlama ipi — yükü veya su tulumlarını yük hayvanına bağlayan ip · yükü veya su tulumlarını özel iple hayvana bağlamak · su tulumlarını yük hayvanına bağlayan ip
  الرِّوَاء حبل يشد به المتاع على البعير (sihah)؛ رويته على الرجل إذا شددته على ظهر البعير (sihah)؛ الرِّوَاء الحبل الذي يروى به على الراوية إذا عكمت المزادتان (tahdhib)؛ يقال له المروى وجمعه مراوى (tahdhib)
- **B008** yapıya göre dolgunlaşma veya suya kavuşma [kalıp] — ipin lifleri kalınlaşıp bükümü sıkılaşmak · eklemler dengeli ve dolgun hale gelmek · sırtı semirip dolgunlaşmış at · kurak yere dikildikten sonra kökten sulanmak
  ارتوى الحبل غلظت قواه (sihah)؛ ارتوت مفاصل الرجل اعتدلت وغلظت (sihah)؛ ارتوت مفاصل الدابة إذا اعتدلت وغلظت (tahdhib)؛ فرس ريان الظهر إذا سمن متناه (tahdhib)؛ ارتوت النخلة إذا غرست في قفر ثم سقيت في أصلها (tahdhib)
- **B009** hoş ve güzel dış görünüş — hoş dış görünüş; görünen güzellik · kökeni tartışmalı bir görünüş güzelliği biçimi
  رجل له رُوَاء أي منظر (sihah)؛ من لم يهمز رئيا جعله من روي كأنه ريان من الحسن (mufradat)
- **B010** hoş koku — hoş koku; bir şeyin güzel kokusu
  طيبة الرِّيَا إذا كانت عطرة الجرم (tahdhib)؛ ريا كل شيء طيب رائحته (tahdhib)
- **B011** dişi dağ keçisi — dağ keçisi; özellikle dişisi, bazı kullanımlarda erkeği de · çok sayıda dağ keçisi; dağ keçileri topluluğu · kadın adı
  الإِرْوِيَّة الأنثى من الوعول (sihah)؛ أروى أيضا اسم امرأة (sihah)؛ الأُرْوِيَّة الأنثى من الوعول (tahdhib)؛ يقال للأنثى أروية وللذكر أروية (tahdhib)؛ لا تجمع بين الأروى والنعام (tahdhib)
- **B012** bayrak — bayrak; sancak
  الرَّايَة العلم (sihah)
- **B013** temel uyak harfi — şiir boyunca değişmeyen temel uyak harfi
  الرَّوِيّ حرف القافية (sihah)؛ قصيدتان على روي واحد (sihah)
- **B014** iri damlalı güçlü yağmur bulutu — iri damlalı, sert yağan yağmur bulutu
  الرَّوِيّ سحابة عظيمة القطر شديدة الوقع (sihah)
- **B015** topluluğun ağır yükümlülüklerini üstlenen ileri gelenler — topluluk adına kan bedeli ve ağır yükümlülükleri üstlenen ileri gelenler
  يقال لسادة القوم الروايا (tahdhib)؛ شبه السيد الذي تحمل الديات عن الحي بالبعير الراوية (tahdhib)؛ روايا الثقل حوامل ثقل الديات (tahdhib)

## ECHO ء ب و (root_000007) — for فَعَلَ (w4): withheld observed target; not identity

- **B001** babalık, besleyip yetiştirme ve oluşuma ya da iyileşmeye kaynaklık etme — baba · babalar, atalar ve baba yönünden onlara katılanlar · anne ile baba; bağlama göre baba ile amca veya dede · babalık veya baba soyu · birinin ya da bir topluluğun babası olmak · ebeveyn gibi besleyip büyütmek · birini baba edinmek · bir şeyin ortaya çıkmasına, düzelmesine veya görünür olmasına sebep olan kimse · konuklarla yakından ilgilenen kimse · savaşı kışkırtan kimse · bir kadının bekâretini bozan erkek
  يدل على التربية والغذو (maqayis)؛ أبوت الشيء آبوه أبوا إذا غذوته (maqayis)؛ فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده (ayn;tahdhib)؛ الأب أصله أبو (sihah)؛ الأب الوالد ويسمى كل من كان سببا في إيجاد شيء أو صلاحه أو ظهوره أبا (mufradat)
- **B002** babaya seslenme ve bağlama göre övgü ya da ağır yergi bildiren hitap kalıpları [kalıp] — babacığım diye seslenme · bağlama göre övgü ya da ağır sövgü bildiren hitap kalıbı · seni çekemeyenin babası olmasın anlamında onurlandırıcı hitap
  يا أبة افعل (sihah)؛ يا أبت ويا أبت لغتان (sihah)؛ لا أبا لك كأنه يمدحه (ayn)؛ لا أبا لك ولا أب لك مدح (sihah)؛ لا أبا لك ولا أب لك مدح ولا أم لك ذم (tahdhib)
- **B003** dağ keçisi idrarının kokusundan hastalanma — dağ keçisi idrarını koklayınca hastalanan dişi keçi · dağ keçisi idrarını koklayınca hastalanan erkek keçi
  عنز أبواء إذا أصابها وجع عن شم أبوال الأروى (maqayis)؛ عنز أبواء وتيس آبى إذا شم بول الأروى فمرض منه (sihah)

## ECHO ر ب و (root_000537) — for رَبُّكَ (w5): withheld observed target; not identity

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

===== _commentary/v16/out/s105/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 105:1, and ## Buluşmalar) =====
## Görmeye çağrı ve yanılan yargı

Sûre bir soruyla açılır ve bu soru okuru seyirci yerine koyar: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ, tr:elem tera keyfe feale rabbüke, gloss:Rabbinin ne yaptığını görmedin mi, source:105:1}. Olumsuz kurulmuş bu soru bir bilgi istemez, "evet" cevabını baştan varsayar; hitap edilen, olayı zaten bilen biri olarak konuşturulur. {ar:تَرَ, tr:tera, gloss:görürsün, source:105:1} fiilinin kökü önce gözün görmesidir, {ar:الرؤية بالعين, tr:er-ru'yetu bi'l-ayn, gloss:gözle görme, source:"ر ء ي,B001"}; ama iki nesne aldığında bilmek anlamına geçer, {ar:بمعنى العلم تتعدى إلى مفعولين, tr:bi-ma'ne'l-ilm teteaddâ ilâ mef'ûleyn, gloss:bilmek anlamında iki nesne alır, source:"ر ء ي,B002"}. Aynı kökten gelen "gördün mü?" sorusu ise bir dikkat çağrısıdır: {ar:يجري أرأيت مجرى أخبرني وكل ذلك فيه معنى التنبيه, tr:yecrî e-raeyte mecrâ ahbirnî ve küllü zâlike fîhi ma'ne't-tenbîh, gloss:"gördün mü" "bana haber ver" yerine geçer, hepsinde uyarma anlamı vardır, source:"ر ء ي,B013"}. Bu üç kat bir arada çalışır: olay bir sahne gibi göz önüne konur, gözle izlenmemiş olsa da gözle görülmüş kadar kesin bir bilgi sayılır ve dinleyenin dikkati ona çekilir. Kökün ettirgen biçimi bir adım daha atar: {ar:أريته الشيء فرآه, tr:ereytuhu'ş-şey'e fe-raâhu, gloss:ona şeyi gösterdim, o da gördü, source:"ر ء ي,B012"} ve {ar:وأرى الله الناس بفلان, tr:ve erallâhu'n-nâse bi-fulân, gloss:Allah insanlara falanca üzerinden (bir ibret) gösterdi, source:"ر ء ي,B012"}. Sûrede gösteren Rab, gösterilen ise filin sahipleridir; onlar bir sergi nesnesine dönüşür.

Bu sûrede kelimelerin kök ailesinden gelen imgeler, kelimenin kendi ayetindeki anlamının yerine geçmez, onun yanında duyulur: fil yine fildir, taş yine taştır; kök yalnızca arka planda ikinci bir ses verir. Bu ikinci ses burada şudur: sağlam görmeye çağrılan okurun karşısında, öbür tarafın kelimeleri yanılan görüşü taşır. {ar:ٱلْفِيلِ, tr:el-fîl, gloss:fil, source:105:1} kökünün bir dalı zayıf görüşü ve işaretleri yanlış okumayı adlandırır: {ar:رجل فَيِل الرأي, tr:raculun feyilu'r-ra'y, gloss:görüşü zayıf adam, source:"ف ي ل,B001"}, {ar:رجل فال أي ضعيف الرأي مخطئ الفراسة, tr:raculun fâl, ey daîfu'r-ra'y muhti'u'l-firâse, gloss:fâl adam, yani görüşü zayıf, sezgisi yanılan, source:"ف ي ل,B001"}. Bu ifadede "görüş" diye çevrilen kelime, {ar:تَرَ, tr:tera, gloss:görürsün, source:105:1} ile aynı köktendir. Böylece açılış ayetinin iki ucunda aynı kök iki zıt hâlde durur: okura "gör" denir, karşı tarafın adı ise görüşün çürüklüğünü fısıldar. Bu bir kök özdeşliği değil, bir aile imgesidir; fil kelimesi ayette yalnızca hayvanı söyler.

İkinci ayetin {ar:تَضْلِيلٍ, tr:tadlîl, gloss:saptırılma, yolunu kaybettirme, source:105:2} kelimesinin kökü yolda kaybolmanın yanında bir işte doğruyu bulamamayı da adlandırır: {ar:ضل في الأمر إذا لم يهتد له, tr:dalle fi'l-emr izâ lem yehtedi leh, gloss:bir işin yolunu bulamadığında "o işte saptı" denir, source:"ض ل ل,B001"}. Üçüncü ayetin kuşları, {ar:طَيْرًا, tr:tayran, gloss:kuşlar, source:105:3}, Arapçada fal bakılan şeydir: {ar:تطير من الشيء فاشتقاقه من الطير, tr:tetayyera mine'ş-şey', fe'ştikâkuhu mine't-tayr, gloss:bir şeyden uğursuzluk çıkardı; türeyişi kuştandır, source:"ط ي ر,B003"}, {ar:الطائر من الزجر في التشؤم والتسعد, tr:et-tâ'ir mine'z-zecr fi't-teşe'üm ve't-tese'ud, gloss:kuş, uğur ve uğursuzluk için okunan işarettir, source:"ط ي ر,B003"}. Burada kuşlar bir şeyin habercisi değildir; okunacak işaret olmaktan çıkıp doğrudan vurucunun kendisi olurlar. Dördüncü ayetin fiili {ar:تَرْمِيهِم, tr:termîhim, gloss:onları atıyordu, source:105:4} kökünde isabet etmeyen tahmini de taşır: {ar:رمى فلان يرمي إذا ظن ظنا غير مصيب, tr:ramâ fulânun yermî izâ zanne zannen gayra musîb, gloss:isabetsiz bir zanda bulunduğunda "attı" denir, source:"ر م ي,B009"}. Ayetteki atış ise hedefini bulur. Taşlar, {ar:بِحِجَارَةٍ, tr:bi-hicâratin, gloss:taşlarla, source:105:4}, aklı da adlandıran bir köktendir: {ar:العقل يسمى حجرا لأنه يمنع من إتيان ما لا ينبغي, tr:el-aklu yusemmâ hicran li-ennehû yemneu min ityâni mâ lâ yenbagî, gloss:akla "hicr" denir, çünkü yakışmayanı yapmaktan alıkoyar, source:"ح ج ر,B002"}. Kendilerini alıkoyacak "hicr"i olmayanlara, aynı kökün öbür anlamı, taş, iner.

Kur'an bu bağı kendisi sahneler. Fecr sûresinde Allah yeminlerini sıraladıktan sonra sorar: {ar:هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ, tr:hel fî zâlike kasemun li-zî hicr, gloss:bunda akıl sahibi için bir yemin var mı, source:89:5}; hemen ardından gelen ayet bu sûrenin açılış kalıbının aynısıdır: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ, tr:elem tera keyfe feale rabbüke bi-âd, gloss:Rabbinin Âd'a ne yaptığını görmedin mi, source:89:6}. Orada sahne Âd'dan Semûd'a ve Firavun'a uzanır ve {ar:فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ, tr:fe-sabbe aleyhim rabbüke sevta azâb, gloss:Rabbin üzerlerine bir azap kamçısı döktü, source:89:13} ile kapanır. "Hicr sahibi" ile "görmedin mi" yan yana durur: görmeye çağrılan, aklı olandır. İbrahim sûresinde Allah, yıkılmış zalimlerin yurtlarında oturanlara {ar:وَتَبَيَّنَ لَكُمْ كَيْفَ فَعَلْنَا بِهِمْ, tr:ve tebeyyene leküm keyfe fealnâ bihim, gloss:onlara ne yaptığımız size apaçık belli olmuştu, source:14:45} der; aynı "nasıl yaptı" burada açıkça görülmüş bir bilgi olarak geri gelir. En'âm sûresinde inkârcılara {ar:أَلَمْ يَرَوْا۟ كَمْ أَهْلَكْنَا مِن قَبْلِهِم, tr:elem yerav kem ehleknâ min kablihim, gloss:kendilerinden önce nice nesli helak ettiğimizi görmediler mi, source:6:6} denir; görmek yine tarihin bilgisi demektir.

Yanlış görmenin sahneleri de Kur'an'dadır. Âd kavmi vadilerine yönelen bulutu görür ve yanılır: {ar:قَالُوا۟ هَٰذَا عَارِضٌۭ مُّمْطِرُنَا, tr:kâlû hâzâ âridun mumtirunâ, gloss:"bu bize yağmur getirecek bir bulut" dediler, source:46:24}; ayetin devamı onun bir azap rüzgârı olduğunu söyler, sonraki ayet de sonucu gösterir: {ar:فَأَصْبَحُوا۟ لَا يُرَىٰٓ إِلَّا مَسَٰكِنُهُمْ, tr:fe-asbahû lâ yurâ illâ mesâkinuhum, gloss:sabaha yalnızca evleri görünür hâlde çıktılar, source:46:25}. Tûr sûresinde inkârcılar için {ar:وَإِن يَرَوْا۟ كِسْفًۭا مِّنَ ٱلسَّمَآءِ سَاقِطًۭا يَقُولُوا۟ سَحَابٌۭ مَّرْكُومٌۭ, tr:ve in yerav kisfen mine's-semâ'i sâkitan yekûlû sehâbun merkûm, gloss:gökten düşen bir parça görseler "üst üste yığılmış bulut" derler, source:52:44} denir. Firavun'un ailesi başlarına gelen kötülüğü {ar:يَطَّيَّرُوا۟ بِمُوسَىٰ وَمَن مَّعَهُۥٓ, tr:yettayyerû bi-mûsâ ve men meah, gloss:Musa'dan ve beraberindekilerden uğursuzluk çıkarırlar, source:7:131} ve Allah cevap verir: {ar:أَلَآ إِنَّمَا طَٰٓئِرُهُمْ عِندَ ٱللَّهِ, tr:elâ innemâ tâ'iruhum indallâh, gloss:bilin ki onların "kuşu" Allah katındadır, source:7:131}. Kuş falının düzeltildiği yer burasıdır: işaret insanın elinde değil, Allah katındadır. Mülk sûresinde inkârcılara {ar:أَوَلَمْ يَرَوْا۟ إِلَى ٱلطَّيْرِ فَوْقَهُمْ صَٰٓفَّٰتٍۢ وَيَقْبِضْنَ, tr:e-ve lem yerav ile't-tayri fevkahum sâffâtin ve yakbidn, gloss:üstlerinde kanat açıp kapayan kuşları görmediler mi, source:67:19} denir ve Nûr sûresinde aynı tekil hitap kuşları gösterir: {ar:أَلَمْ تَرَ أَنَّ ٱللَّهَ يُسَبِّحُ لَهُۥ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱلطَّيْرُ صَٰٓفَّٰتٍۢ, tr:elem tera ennallâhe yusebbihu lehû men fi's-semâvâti ve'l-ardi ve't-tayru sâffât, gloss:göklerde ve yerde olanların ve kanat çırpan kuşların Allah'ı tesbih ettiğini görmedin mi, source:24:41}. Bu sûrede kuşa bakmak bir kehanet değil, Rabbin işini görmektir.

Kur'an aynı zamanda belirleyici gücün görünmediğini de söyler. Ahzâb sûresinde Allah mü'minlere, üzerlerine ordular geldiği günü hatırlatır: {ar:فَأَرْسَلْنَا عَلَيْهِمْ رِيحًۭا وَجُنُودًۭا لَّمْ تَرَوْهَا, tr:fe-erselnâ aleyhim rîhan ve cunûden lem teravhâ, gloss:üzerlerine bir rüzgâr ve sizin görmediğiniz ordular gönderdik, source:33:9}. Bu sûrede ise ordu görünür kılınır: kuşlar vardır, taşlar vardır, ve okura "görmedin mi" denir. Aynı kalıp başka ilahi işlerin üzerine de kurulur: {ar:أَلَمْ تَرَ إِلَىٰ رَبِّكَ كَيْفَ مَدَّ ٱلظِّلَّ, tr:elem tera ilâ rabbike keyfe medde'z-zıll, gloss:Rabbinin gölgeyi nasıl uzattığını görmedin mi, source:25:45}; Nuh da kavmine {ar:أَلَمْ تَرَوْا۟ كَيْفَ خَلَقَ ٱللَّهُ سَبْعَ سَمَٰوَٰتٍۢ طِبَاقًۭا, tr:elem teravâ keyfe halakallâhu seb'a semâvâtin tıbâkâ, gloss:Allah'ın yedi göğü kat kat nasıl yarattığını görmediniz mi, source:71:15} der. İki sûre sonra aynı kökün dikkat çağrısı yeniden açılır: {ar:أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ, tr:e-raeyte'llezî yukezzibu bi'd-dîn, gloss:dini yalanlayanı gördün mü, source:107:1}.

Kaynaklar: 105:1 تَرَ ر ء ي B001; 105:1 تَرَ ر ء ي B002; 105:1 تَرَ ر ء ي B013; 105:1 تَرَ ر ء ي B012; 105:1 ٱلْفِيلِ ف ي ل B001; 105:2 تَضْلِيلٍ ض ل ل B001; 105:3 طَيْرًا ط ي ر B003; 105:4 تَرْمِيهِم ر م ي B009; 105:4 بِحِجَارَةٍ ح ج ر B002

## Rab ve filin sahipleri

İlk ayet iki tür sahipliği karşı karşıya koyar. {ar:رَبُّكَ, tr:rabbüke, gloss:senin Rabbin, source:105:1} kelimesinin kökü malikliği, itaat edilen efendiliği ve onarıp düzene koymayı bir arada taşır: {ar:يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح, tr:yekûnu'r-rabbu'l-mâlik, ve yekûnu'r-rabbu's-seyyidu'l-mutâ', ve yekûnu'r-rabbu'l-muslih, gloss:Rab malik olur, itaat edilen efendi olur, düzelten olur, source:"ر ب ب,B001"}. Kullanımdaki örnekler bir evin ve bir binek hayvanının sahibidir: {ar:رب الدار ورب الفرس, tr:rabbu'd-dâr ve rabbu'l-feres, gloss:evin sahibi, atın sahibi, source:"ر ب ب,B001"}. Kökün öbür dalı sahip olduğunu besleyip tamamlayanı anlatır: {ar:رب الشيء أي أصلحه؛ رب فلان الصنيعة إذا أتمها وأصلحها, tr:rabbe'ş-şey', ey aslahahû; rabbe fulânun es-sanîate izâ etemmehâ ve aslahahâ, gloss:bir şeyi "rabb etti", yani düzeltti; bir iyiliği tamamlayıp güzelleştirdi, source:"ر ب ب,B002"}. Kelimeye bağlanan "senin" eki, hitap edilenin bu bakımın altında olduğunu söyler.

Karşı tarafın adı ise {ar:بِأَصْحَٰبِ ٱلْفِيلِ, tr:bi-ashâbi'l-fîl, gloss:fil sahiplerine, source:105:1} olarak konur. {ar:أَصْحَٰبِ, tr:ashâb, gloss:sahipler, arkadaşlar, source:105:1} kökü sürekli bir bağlılığı, ayrılmayan yoldaşlığı ve sahipliği anlatır: {ar:الصاحب الملازم إنسانا كان أو حيوانا أو مكانا أو زمانا, tr:es-sâhibu'l-mulâzimu insânen kâne ev hayevânen ev mekânen ev zamânâ, gloss:sâhib, insan, hayvan, yer ya da zaman olsun, bir şeye yapışık olandır, source:"ص ح ب,B001"}, {ar:يقال للمالك للشيء هو صاحبه, tr:yukâlu li'l-mâliki li'ş-şey' huve sâhibuh, gloss:bir şeyin malikine onun sâhibi denir, source:"ص ح ب,B001"}. Bu topluluk ne bir kavim adıyla ne bir yer adıyla anılır; tanımı yanlarında tuttukları hayvandır. Arapça filin bakıcısına ayrı bir ad bile verir: {ar:الفيل معروف والجمع أفيال وفيول وفيلة؛ صاحبه فيال, tr:el-fîlu ma'rûf, ve'l-cem'u efyâl ve fuyûl ve fiyele; sâhibuhû feyyâl, gloss:fil bilinir, çoğulu efyâl, fuyûl, fiyele; bakıcısına feyyâl denir, source:"ف ي ل,B004"}. Sahne böylece iki sahibi karşılaştırır: hitap edilenin Rabbi, ve bir hayvanın sahipleri. Kökün bir başka dalı ise korunarak eşlik edilmeyi anlatır: {ar:صحبك الله أي حفظك, tr:sahibekallâh, ey hafizak, gloss:"Allah sana yoldaş olsun", yani seni korusun, source:"ص ح ب,B002"}. Filin "sahipleri" kendi hayvanlarına yoldaştır; onlara Allah'ın koruyan yoldaşlığından söz edilmez.

Kur'an bu "sahip" kelimesini Allah'ın koruması altındaki bir yoldaşlık için de kullanır. Tevbe sûresinde, inkârcıların çıkardığı iki kişiden biri mağarada {ar:إِذْ يَقُولُ لِصَٰحِبِهِۦ لَا تَحْزَنْ إِنَّ ٱللَّهَ مَعَنَا, tr:iz yekûlu li-sâhibihî lâ tahzen innallâhe meanâ, gloss:yoldaşına "üzülme, Allah bizimle" diyordu, source:9:40} der ve aynı ayet Allah'ın onu {ar:بِجُنُودٍۢ لَّمْ تَرَوْهَا, tr:bi-cunûdin lem teravhâ, gloss:sizin görmediğiniz ordularla, source:9:40} desteklediğini söyler. Orada sâhib Allah'ın beraberliği içindedir; burada ashâb bir filin yanındadır.

{ar:رَبُّكَ, tr:rabbüke, gloss:senin Rabbin, source:105:1} kelimesi, mushafta hemen ardından gelen sûrede bir yere bağlanır: {ar:فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ, tr:felya'budû rabbe hâze'l-beyt, gloss:öyleyse bu Evin Rabbine ibadet etsinler, source:106:3}, {ar:ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ, tr:ellezî at'amehum min cû'in ve âmenehum min havf, gloss:onları açlıktan doyuran, korkudan emin kılan, source:106:4}. Bu sûre filin sahiplerinin neyi hedeflediğini söylemez; ama iki sûrenin yan yana durması, "rab" kelimesinin "evin sahibi" kullanımını ve korkudan emin kılmayı aynı okumaya taşır. Kur'an Evin bu korunmuşluğunu başka yerlerde açıkça söyler: {ar:وَمَن دَخَلَهُۥ كَانَ ءَامِنًۭا, tr:ve men dehalehû kâne âminâ, gloss:oraya giren emin olur, source:3:97}, insanlar için konan ilk ev hakkında, {ar:إِنَّ أَوَّلَ بَيْتٍۢ وُضِعَ لِلنَّاسِ لَلَّذِى بِبَكَّةَ مُبَارَكًۭا, tr:inne evvele beytin vudia li'n-nâsi lellezî bi-bekkete mubârakâ, gloss:insanlar için konan ilk ev, Bekke'deki o mübarek evdir, source:3:96}. Ankebût sûresinde ise yine bir görme sorusuyla gelir: {ar:أَوَلَمْ يَرَوْا۟ أَنَّا جَعَلْنَا حَرَمًا ءَامِنًۭا وَيُتَخَطَّفُ ٱلنَّاسُ مِنْ حَوْلِهِمْ, tr:e-ve lem yerav ennâ cealnâ haramen âminen ve yutehattafu'n-nâsu min havlihim, gloss:çevrelerinde insanlar kapılıp götürülürken bizim güvenli bir harem kıldığımızı görmediler mi, source:29:67}. Hac sûresi ise orada yalnızca kötülüğe niyet etmeyi bile cezalandırır: {ar:وَمَن يُرِدْ فِيهِ بِإِلْحَادٍۭ بِظُلْمٍۢ نُّذِقْهُ مِنْ عَذَابٍ أَلِيمٍۢ, tr:ve men yurid fîhi bi-ilhâdin bi-zulmin nuzıkhu min azâbin elîm, gloss:orada zulümle sapkınlığa niyet edene acı bir azap tattırırız, source:22:25}.

Kaynaklar: 105:1 رَبُّكَ ر ب ب B001; 105:1 رَبُّكَ ر ب ب B002; 105:1 بِأَصْحَٰبِ ص ح ب B001; 105:1 بِأَصْحَٰبِ ص ح ب B002; 105:1 ٱلْفِيلِ ف ي ل B004

## Emekle kurulan düzen, yoldan çıkarılması ve iki "kılma"

Sûrenin iskeleti bir yapış ve iki kılmadır. {ar:فَعَلَ, tr:feale, gloss:yaptı, source:105:1} nasıl yapıldığı sorulan işi açar; {ar:يَجْعَلْ, tr:yec'al, gloss:kılmak, source:105:2} ve {ar:فَجَعَلَهُمْ, tr:fe-cealehum, gloss:onları ... kıldı, source:105:5} bu soruyu cevaplayan iki dönüştürmedir. Arada gönderme ve atma durur. Yapmak fiilinin kökü bir şeyi meydana getirmektir: {ar:أصل صحيح يدل على إحداث شيء من عمل وغيره, tr:aslun sahîhun yedullu alâ ihdâsi şey'in min amelin ve gayrih, gloss:bir işle ya da başka yolla bir şeyi meydana getirmeyi gösteren sağlam bir köktür, source:"ف ع ل,B001"}. Kılmak ise bir şeyi bir hâle sokmaktır: {ar:جعل صير, tr:ceale: sayyera, gloss:"ceale", "dönüştürdü" demektir, source:"ج ع ل,B002"}, {ar:جعله الله نبيا أي صيره, tr:cealehullâhu nebiyyen, ey sayyerah, gloss:Allah onu peygamber kıldı, yani o hâle getirdi, source:"ج ع ل,B002"}, ve yapıp ortaya koymaktır: {ar:جعلت الشيء صنعته, tr:cealtu'ş-şey'e: sana'tuh, gloss:şeyi "kıldım", yani yaptım, source:"ج ع ل,B001"}.

Bu iki kılmanın ilkinin nesnesi onların düzenidir: {ar:أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍ, tr:elem yec'al keydehum fî tadlîl, gloss:onların düzenini boşa çıkarmadı mı, source:105:2}. {ar:كَيْدَهُمْ, tr:keydehum, gloss:onların tuzağı, düzeni, source:105:2} kökü önce bir şey üzerinde güçle uğraşmaktır: {ar:يدل على معالجة لشيء بشدة, tr:yedullu alâ muâlecetin li-şey'in bi-şidde, gloss:bir şeyle sertçe uğraşmayı gösterir, source:"ك ي د,B001"}, {ar:كل شيء تعالجه فأنت تكيده, tr:küllu şey'in tuâlicuhû fe-ente tekîduh, gloss:uğraştığın her şeyi "keyd" edersin, source:"ك ي د,B001"}. Sonra bu emek gizli bir düzene, zarar vermeye kurulmuş bir hileye dönüşür: {ar:الكيد المكر وكاده يكيده كيدا ومكيدة, tr:el-keydu'l-mekr, ve kâdehû yekîduhû keyden ve mekîde, gloss:keyd, gizli tuzaktır, source:"ك ي د,B002"}, {ar:الكيد ضرب من الاحتيال, tr:el-keydu darbun mine'l-ihtiyâl, gloss:keyd bir tür hiledir, source:"ك ي د,B002"}, {ar:لأريدن بها سوءا, tr:le-urîdenne bihâ sû'â, gloss:ona mutlaka kötülük kastedeceğim, source:"ك ي د,B002"}. Kelime böylece bir yolculuğun emeğini ve onun bir hedefe kurulmuş kastını birlikte taşır.

İlk "kılma" bu emeği {ar:تَضْلِيلٍ, tr:tadlîl, gloss:saptırılma, source:105:2} içine yerleştirir. Kelime, birini ya da bir şeyi yoldan çıkarma eylemini anlatan bir mastardır; düzen kendiliğinden sapmaz, saptırılır. Kökün ilk resmi doğru yoldan ayrılmaktır: {ar:كل جائر عن القصد ضال, tr:küllu câ'irin ani'l-kasdi dâll, gloss:hedefe giden yoldan sapan herkes "dâll"dır, source:"ض ل ل,B001"}, {ar:ضل في الأرض إذا لم يهتد للسبيل, tr:dalle fi'l-ard izâ lem yehtedi li's-sebîl, gloss:yolu bulamadığında "yeryüzünde saptı" denir, source:"ض ل ل,B001"}. İkinci resim gidilen yeri bulamamaktır ve kullanımın kendi örneği bir mescit ile bir evdir: {ar:ضللت المسجد والدار إذا لم تهتد لهما, tr:daleltu'l-mescide ve'd-dâr izâ lem tehtedi lehumâ, gloss:mescide ve eve yolunu bulamadığında "onları kaybettim" dersin, source:"ض ل ل,B003"}; yanında sahibinin elinden kaçıp giden hayvan durur: {ar:أضل بعيره إذا أفلت فذهب, tr:edalle baîrahû izâ efleta fe-zeheb, gloss:devesi elinden kurtulup gidince "devesini kaybetti" denir, source:"ض ل ل,B003"}. Üçüncü resim gözden kaybolup erimektir: {ar:ضل اللبن في الماء ثم استهلك, tr:dalle'l-leben fi'l-mâ'i summe'stuhlik, gloss:süt suyun içinde kayboldu, sonra tükendi, source:"ض ل ل,B002"}, {ar:أضل الميت إذا دفن, tr:udille'l-meyyit izâ dufin, gloss:ölü gömülünce "kaybettirildi" denir, source:"ض ل ل,B002"}. Düzenin akıbeti bu üç adımda yürür: hedefe kurulmuş bir emek yoldan çıkarılır, hedefini bulamaz, sonunda suya karışan süt gibi iz bırakmadan erir. Dördüncü ayetin fiil kökü yola çıkmayı ve niyet edilen yönü de taşır: {ar:رمى الرجل إذا سافر, tr:ramâ'r-racul izâ sâfer, gloss:adam yolculuğa çıkınca "attı" denir, source:"ر م ي,B007"}, {ar:أين ترمي أي جهة تنوي, tr:eyne termî, ey cihetin tenvî, gloss:"nereye atıyorsun", yani hangi yöne niyetlisin, source:"ر م ي,B007"}. Yolculuğun yönünü söyleyen kök, sûrede kuşların onları "atmasında" geri döner.

İkinci kılma ise insanların kendisini nesne alır: {ar:فَجَعَلَهُمْ كَعَصْفٍۢ مَّأْكُولٍۭ, tr:fe-cealehum ke-asfin me'kûl, gloss:onları yenmiş ekin yaprağı gibi kıldı, source:105:5}. İlk kılma onların yaptığı şeyi, ikincisi onları kendilerini dönüştürür. Onların "keyd"i, yani bir şeye güçle uğraşmaları, sûrenin sonunda Onun yapışının nesnesi olarak kalır.

Kur'an bu ilişkiyi defalarca kurar. Mü'min sûresinde Firavun'un meclisi, Musa'ya inananların oğullarını öldürmeyi emreder ve ayet şu hükümle kapanır: {ar:وَمَا كَيْدُ ٱلْكَٰفِرِينَ إِلَّا فِى ضَلَٰلٍۢ, tr:ve mâ keydu'l-kâfirîne illâ fî dalâl, gloss:kâfirlerin düzeni boşa gitmekten başka bir şey değildir, source:40:25}; keyd ve dalâl bu sûredeki gibi tek cümlede durur. Aynı sûrede Firavun göğün yollarına çıkmak ister ve hüküm aynı kalıpla verilir: {ar:وَمَا كَيْدُ فِرْعَوْنَ إِلَّا فِى تَبَابٍۢ, tr:ve mâ keydu fir'avne illâ fî tebâb, gloss:Firavun'un düzeni yıkımdan başka bir şeye varmaz, source:40:37}. Yusuf sûresinde Yusuf, kendisine kurulan tuzağın ortaya çıkışından sonra şöyle der: {ar:وَأَنَّ ٱللَّهَ لَا يَهْدِى كَيْدَ ٱلْخَآئِنِينَ, tr:ve ennallâhe lâ yehdî keyde'l-hâ'inîn, gloss:Allah hainlerin düzenini hedefine ulaştırmaz, source:12:52}; burada keyd'in yolunu bulmaması, "doğru yola iletmek" fiiliyle söylenir, sûrenin tadlîl'inin tam karşılığıdır. Daha önce de Rab onu kurulan tuzaktan çevirmişti: {ar:فَٱسْتَجَابَ لَهُۥ رَبُّهُۥ فَصَرَفَ عَنْهُ كَيْدَهُنَّ, tr:festecâbe lehû rabbuhû fe-sarafe anhu keydehunn, gloss:Rabbi duasını kabul etti ve onların tuzağını ondan çevirdi, source:12:34}. İbrahim'i yakmak isteyen kavim için Kur'an keyd'e karşı bir "kılma" koyar: {ar:وَأَرَادُوا۟ بِهِۦ كَيْدًۭا فَجَعَلْنَٰهُمُ ٱلْأَخْسَرِينَ, tr:ve erâdû bihî keyden fe-cealnâhumu'l-ahserîn, gloss:ona bir tuzak kurmak istediler, biz de onları en çok kaybedenler kıldık, source:21:70}, ve Sâffât sûresinde {ar:فَأَرَادُوا۟ بِهِۦ كَيْدًۭا فَجَعَلْنَٰهُمُ ٱلْأَسْفَلِينَ, tr:fe-erâdû bihî keyden fe-cealnâhumu'l-esfelîn, gloss:ona tuzak kurmak istediler, biz de onları en alçaklar kıldık, source:37:98}. Enfâl sûresi bunu bir ilahi sıfata bağlar: {ar:وَأَنَّ ٱللَّهَ مُوهِنُ كَيْدِ ٱلْكَٰفِرِينَ, tr:ve ennallâhe mûhinu keydi'l-kâfirîn, gloss:Allah kâfirlerin düzenini zayıflatandır, source:8:18}. Tûr sûresi keyd kuranları keyd'in nesnesi yapar: {ar:أَمْ يُرِيدُونَ كَيْدًۭا ۖ فَٱلَّذِينَ كَفَرُوا۟ هُمُ ٱلْمَكِيدُونَ, tr:em yurîdûne keydâ, fellezîne keferû humu'l-mekîdûn, gloss:yoksa bir tuzak mı kurmak istiyorlar? Asıl tuzağa düşürülenler inkâr edenlerdir, source:52:42}; birkaç ayet sonra {ar:يَوْمَ لَا يُغْنِى عَنْهُمْ كَيْدُهُمْ شَيْـًۭٔا, tr:yevme lâ yugnî anhum keyduhum şey'â, gloss:tuzaklarının kendilerine hiçbir yarar sağlamayacağı gün, source:52:46} gelir. Târık sûresinde iki keyd yüz yüze konur: {ar:إِنَّهُمْ يَكِيدُونَ كَيْدًۭا, tr:innehum yekîdûne keydâ, gloss:onlar bir tuzak kuruyorlar, source:86:15}, {ar:وَأَكِيدُ كَيْدًۭا, tr:ve ekîdu keydâ, gloss:ben de bir düzen kuruyorum, source:86:16}; A'râf sûresinde Allah {ar:إِنَّ كَيْدِى مَتِينٌ, tr:inne keydî metîn, gloss:benim düzenim sağlamdır, source:7:183} der. Yapma fiilinin Allah'a ait olduğu da açıkça söylenir: {ar:فَعَّالٌۭ لِّمَا يُرِيدُ, tr:fe''âlun limâ yurîd, gloss:dilediğini yapandır, source:85:16}. İbrahim sûresi ise sapmayı ve rüzgârı bir benzetmede birleştirir: {ar:أَعْمَٰلُهُمْ كَرَمَادٍ ٱشْتَدَّتْ بِهِ ٱلرِّيحُ فِى يَوْمٍ عَاصِفٍۢ, tr:a'mâluhum ke-ramâdin işteddet bihi'r-rîhu fî yevmin âsıf, gloss:yaptıkları, fırtınalı bir günde rüzgârın savurduğu kül gibidir, source:14:18}, ve aynı ayet {ar:ذَٰلِكَ هُوَ ٱلضَّلَٰلُ ٱلْبَعِيدُ, tr:zâlike huve'd-dalâlu'l-baîd, gloss:işte uzak sapkınlık budur, source:14:18} diye biter. Secde sûresinde inkârcılar dalâl kökünü yerin içinde kaybolmak anlamında kullanır: {ar:أَءِذَا ضَلَلْنَا فِى ٱلْأَرْضِ, tr:e-izâ dalelnâ fi'l-ard, gloss:biz yerin içinde kaybolup gittiğimizde mi, source:32:10}.

Kaynaklar: 105:1 فَعَلَ ف ع ل B001; 105:2 يَجْعَلْ ج ع ل B002; 105:5 فَجَعَلَهُمْ ج ع ل B001; 105:5 فَجَعَلَهُمْ ج ع ل B002; 105:2 كَيْدَهُمْ ك ي د B001; 105:2 كَيْدَهُمْ ك ي د B002; 105:2 تَضْلِيلٍ ض ل ل B001; 105:2 تَضْلِيلٍ ض ل ل B003; 105:2 تَضْلِيلٍ ض ل ل B002; 105:4 تَرْمِيهِم ر م ي B007

## Av ve avcı: ağırın hafif tarafından vurulması

Dördüncü ayetin fiili bir atıştır: {ar:تَرْمِيهِم بِحِجَارَةٍۢ مِّن سِجِّيلٍۢ, tr:termîhim bi-hicâratin min siccîl, gloss:onlara siccîlden taşlar atıyorlardı, source:105:4}. Fiil dişil kurulmuştur ve öznesi kuşlardır; kuşlar atandır, onlar atılandır. Atmanın kökü nesnelerini kendisi sayar: ok ve taş. {ar:الرمي يقال في الأعيان كالسهم والحجر, tr:er-ramyu yukâlu fi'l-a'yân ke's-sehmi ve'l-hacer, gloss:atmak, ok ve taş gibi somut şeyler için söylenir, source:"ر م ي,B001"}. Kök ava çıkmayı da anlatır: {ar:خرجت أرتمي إذا رميت القنص, tr:haractu ertemî izâ rameytu'l-kanas, gloss:av vurmaya çıktığımda "atmaya çıktım" derim, source:"ر م ي,B001"}, ve atılan her şey bir avdır: {ar:الرمية الصيد الذي يرمى, tr:er-ramiyyetu's-saydu'llezî yurmâ, gloss:"ramiyye", vurulan avdır, source:"ر م ي,B003"}; okun yuvarlak ucuna da bu kökten ad verilir: {ar:المرماة نصل السهم المدور, tr:el-mirmâtu naslu's-sehmi'l-mudevver, gloss:"mirmât", okun yuvarlak temreni, source:"ر م ي,B003"}. Fiile bağlanan "onları" zamiri, filin sahiplerini bu "ramiyye"nin, yani vurulan avın yerine koyar. Göndermenin kökü bile kısa bir oku adlandırır: {ar:المرسال سهم قصير, tr:el-mirsâlu sehmun kasîr, gloss:"mirsâl", kısa bir oktur, source:"ر س ل,B011"}. Taşlar da sert birer mermidir: {ar:الحجر الجوهر الصلب المعروف وجمعه أحجار وحجارة, tr:el-haceru'l-cevheru's-sulbu'l-ma'rûf, ve cem'uhû ahcâr ve hicâra, gloss:taş bilinen sert maddedir, çoğulu ahcâr ve hicâra, source:"ح ج ر,B003"}.

Bu avın tuhaflığı rollerin yer değiştirmesidir. Kuşlar normalde avlanandır; burada avcıdırlar. Hayvanların en irisi ve onun sahipleri ise vurulan avdır. Avın sonu son ayettedir: {ar:مَّأْكُولٍۭ, tr:me'kûl, gloss:yenmiş, source:105:5} kökü, bir yırtıcının yediği avı da adlandırır: {ar:أكيل الذئب الشاة وغيرها؛ أكيلة الأسد فريسته, tr:ekîlu'z-zi'bi'ş-şâtu ve gayruhâ; ekîletu'l-esedi ferîsetuh, gloss:kurdun "ekîl"i yediği koyun ve benzeridir; aslanın "ekîle"si avıdır, source:"ء ك ل,B007"}. Sahne şöyle akar: avcılar salınır, taşlar ok gibi atılır, ordu vurulan av olur ve yenmiş av olarak kalır. Kur'an yırtıcının yediği hayvanı haram kılınanlar arasında sayar, {ar:وَمَآ أَكَلَ ٱلسَّبُعُ, tr:ve mâ ekele's-sebu', gloss:ve yırtıcı hayvanın yediği, source:5:3}; Yusuf'un kardeşleri de babalarına onu kurdun yediğini söyler, {ar:فَأَكَلَهُ ٱلذِّئْبُ, tr:fe-ekelehu'z-zi'b, gloss:onu kurt yedi, source:12:17}. Bu sahnede "yenmiş" olan, bir avın sonudur.

Avın içinde ağır ile hafifin yer değiştirmesi de vardır. Fil en iri hayvandır, {ar:الفيل معروف, tr:el-fîlu ma'rûf, gloss:fil bilinir, source:"ف ي ل,B004"}; ama kökünün temel anlamı gevşeklik ve zayıflıktır: {ar:أصل يدل على استرخاء وضعف, tr:aslun yedullu ale'stirhâ'in ve da'f, gloss:gevşeklik ve zayıflık gösteren bir köktür, source:"ف ي ل,B001"}. En güçlü hayvanın adının altında güçsüzlük yatar. Kuşlar hafif ve hızlıdır: {ar:لكل من خف قد طار وكل سرعة, tr:li-külli men haffe kad târ, ve küllu sur'a, gloss:hafifleyen her şeye "uçtu" denir, her hıza da, source:"ط ي ر,B001"}. Ama bu hafif sürülerin adı ağırlığı ve yenmeyi taşıyan bir köktendir: {ar:أبل الرجل إذا غلب وامتنع والأبلة الثقل, tr:ebile'r-racul izâ galebe ve'mtena', ve'l-ubletu's-sikal, gloss:adam galip gelip direnince "ebile" denir; "uble" ağırlıktır, source:"ء ب ل,B004"}. Taşlar serttir ve siccîl şiddetle açıklanır: {ar:وقالوا السجيل الشديد, tr:ve kâlû es-siccîlu'ş-şedîd, gloss:siccîl, şiddetli olandır dediler, source:"س ج ل,B005"}, {ar:تأويله كثيرة شديدة, tr:te'vîluhû kesîratun şedîde, gloss:anlamı: çok ve şiddetli, source:"س ج ل,B005"}. Son kelime {ar:كَعَصْفٍ, tr:ke-asf, gloss:ekin yaprağı gibi, source:105:5} ise hafiflik ve hızın kökündendir: {ar:أصل واحد صحيح يدل على خفة وسرعة, tr:aslun vâhidun sahîhun yedullu alâ hıffetin ve sur'a, gloss:hafiflik ve hız gösteren sağlam tek bir köktür, source:"ع ص ف,B003"}. Ağır olan hafif olanca vurulur; sert taşlar hafif kuşlardan iner ve en kütleli olan sonunda ağırlığı olmayan bir yaprağa döner.

Kur'an gücün korumadığı kavimleri anlatırken bu tersine dönüşü öne çıkarır. Mü'min sûresinde Allah önceki kavimler için {ar:كَانُوا۟ هُمْ أَشَدَّ مِنْهُمْ قُوَّةًۭ وَءَاثَارًۭا فِى ٱلْأَرْضِ فَأَخَذَهُمُ ٱللَّهُ بِذُنُوبِهِمْ, tr:kânû hum eşedde minhum kuvveten ve âsâran fi'l-ard, fe-ehazehumullâhu bi-zunûbihim, gloss:onlar bunlardan daha güçlü ve yeryüzünde daha çok iz bırakmışlardı, Allah onları günahları yüzünden yakaladı, source:40:21} der. Fussilet sûresinde Âd kavmi {ar:وَقَالُوا۟ مَنْ أَشَدُّ مِنَّا قُوَّةً, tr:ve kâlû men eşeddu minnâ kuvveh, gloss:"bizden daha güçlü kim var" dediler, source:41:15} ve cevap bir göndermedir: {ar:فَأَرْسَلْنَا عَلَيْهِمْ رِيحًۭا صَرْصَرًۭا, tr:fe-erselnâ aleyhim rîhan sarsarâ, gloss:üzerlerine dondurucu, uğultulu bir rüzgâr gönderdik, source:41:16}. Atmanın gerçek sahibi de Enfâl sûresinde açıkça söylenir; Allah elçisine {ar:وَمَا رَمَيْتَ إِذْ رَمَيْتَ وَلَٰكِنَّ ٱللَّهَ رَمَىٰ, tr:ve mâ rameyte iz rameyte ve lâkinnallâhe ramâ, gloss:attığın zaman sen atmadın, Allah attı, source:8:17} der. Orada görünen atıcı bir insandır, burada kuşlardır; atışın sahibi iki yerde de Odur.

Kaynaklar: 105:4 تَرْمِيهِم ر م ي B001; 105:4 تَرْمِيهِم ر م ي B003; 105:3 وَأَرْسَلَ ر س ل B011; 105:4 بِحِجَارَةٍ ح ج ر B003; 105:5 مَّأْكُولٍۭ ء ك ل B007; 105:1 ٱلْفِيلِ ف ي ل B004; 105:1 ٱلْفِيلِ ف ي ل B001; 105:3 طَيْرًا ط ي ر B001; 105:3 أَبَابِيلَ ء ب ل B004; 105:4 سِجِّيلٍ س ج ل B005; 105:5 كَعَصْفٍ ع ص ف B003

## Ekin, saman ve yenmiş olan

Son ayet bir tarlada biter: {ar:فَجَعَلَهُمْ كَعَصْفٍۢ مَّأْكُولٍۭ, tr:fe-cealehum ke-asfin me'kûl, gloss:onları yenmiş ekin yaprağı gibi kıldı, source:105:5}. {ar:عَصْفٍ, tr:asf, gloss:ekin yaprağı, kabuk, source:105:5}, tanenin üzerindeki kabuk ve sapın kuruyup ufalanan yapraklarıdır: {ar:العصف ما على الحب من قشور التبن, tr:el-asfu mâ ale'l-habbi min kuşûri't-tibn, gloss:asf, tanenin üzerindeki saman kabuklarıdır, source:"ع ص ف,B001"}, {ar:ما على ساق الزرع من الورق الذي يبس فتفتت, tr:mâ alâ sâkı'z-zer'i mine'l-varaki'llezî yebise fe-tefettet, gloss:ekinin sapı üzerinde kuruyup ufalanan yapraklar, source:"ع ص ف,B001"}, {ar:العصف والعصيفة الذي يعصف من الزرع وحطام النبت المتكسر, tr:el-asfu ve'l-asîfetu'llezî yu'safu mine'z-zer', ve hutâmu'n-nebti'l-mutekessir, gloss:asf ve asîfe, ekinden koparılan ve kırılmış bitki döküntüsüdür, source:"ع ص ف,B001"}. Kökün rüzgârı da bu döküntüyü üretir: {ar:عاصفة ومعصفة تكسر الشيء فتجعله كعصف وعصفت بهم الريح تشبيها بذلك, tr:âsıfa ve mu'sıfa tekseru'ş-şey'e fe-tec'aluhû ke-asf, ve asafet bihimu'r-rîhu teşbîhen bi-zâlik, gloss:âsıfa ve mu'sıfa şeyi kırıp asf gibi yapar; "rüzgâr onları asf etti" sözü buna benzetmedir, source:"ع ص ف,B004"}. {ar:فَجَعَلَهُمْ, tr:fe-cealehum, gloss:onları kıldı, source:105:5} bu hâle sokmaktır, {ar:جعل صير, tr:ceale: sayyera, gloss:"ceale", "dönüştürdü" demektir, source:"ج ع ل,B002"}. Sûrenin ilk fiili de buraya bağlanır: yapmanın kullanımdaki örneği kırmaktır, {ar:فعلت الشيء فانفعل كسرته فانكسر, tr:faaltu'ş-şey'e fe'nfeal, kesertuhû fe'nkeser, gloss:şeyi yaptım, o da yapıldı; kırdım, o da kırıldı, source:"ف ع ل,B001"}. Birinci ayette sorulan "yapış", beşinci ayette sonucu görünen bir kırmadır.

{ar:مَّأْكُولٍۭ, tr:me'kûl, gloss:yenmiş, source:105:5} sahnenin son adımını verir. Kelime önce yenmiş olandır, {ar:الأكل تناول المطعم, tr:el-eklu tenâvulu'l-mat'am, gloss:yemek, yiyeceği almaktır, source:"ء ك ل,B001"}. Ekinin ürünü de bu kökten adlanır, {ar:أكل الشجرة ثمرها؛ الأكل ثمر النخل والشجر, tr:uklu'ş-şecerati semeruhâ; el-uklu semeru'n-nahli ve'ş-şecer, gloss:ağacın "ukl"ü meyvesidir; ukl, hurma ve ağaç meyvesidir, source:"ء ك ل,B002"}; ürün alındığında geriye kabuk kalır. Kök bir şeyin içten çürümesini, kurt yemesini de anlatır: {ar:والأكال أن يتأكل عود أو شيء؛ تأكل كذا فسد؛ في جسدي إكلة من الأكال, tr:ve'l-ukâlu en yete'ekkele ûdun ev şey'; te'ekkele kezâ: fesed; fî cesedî ikletun mine'l-ukâl, gloss:"ukâl", bir dalın ya da şeyin kurtlanıp yenmesidir; "te'ekkele" bozuldu demektir; "bedenimde yenik var", source:"ء ك ل,B006"}. Süreç şudur: yetişmiş bir ekin, ürünü alınmış, geriye kabuk ve kuru yaprak kalmış, rüzgârla kırılmış ve içten yenmiş. Bir ordu bu hâle getirilir. "Gibi" edatı bunun bir benzetme olduğunu açıkça söyler; ayet onları ekinin kendisi değil, ekinin artığı gibi gösterir.

Kur'an bu artığı bitkinin bir parçası olarak sayar: {ar:وَٱلْحَبُّ ذُو ٱلْعَصْفِ وَٱلرَّيْحَانُ, tr:ve'l-habbu zu'l-asfi ve'r-reyhân, gloss:kabuklu taneler ve güzel kokulu bitkiler, source:55:12}. Zümer sûresi bu sûrenin bütün yayını tek ayette taşır: aynı "görmedin mi" ile açılır, ekini çıkarır ve "kılma" ile kırıntıya çevirir: {ar:أَلَمْ تَرَ أَنَّ ٱللَّهَ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ, tr:elem tera ennallâhe enzele mine's-semâ'i mâ', gloss:Allah'ın gökten su indirdiğini görmedin mi, source:39:21}, ve aynı ayette {ar:ثُمَّ يُخْرِجُ بِهِۦ زَرْعًۭا مُّخْتَلِفًا أَلْوَٰنُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَجْعَلُهُۥ حُطَٰمًا, tr:summe yuhricu bihî zer'an muhtelifen elvânuh, summe yehîcu fe-terâhu musferran, summe yec'aluhû hutâmâ, gloss:sonra onunla renkleri çeşitli ekin çıkarır, sonra ekin kurur, onu sararmış görürsün, sonra onu kırıntı hâline getirir, source:39:21}. Vâkıa sûresinde Allah ekinciye {ar:لَوْ نَشَآءُ لَجَعَلْنَٰهُ حُطَٰمًۭا, tr:lev neşâ'u le-cealnâhu hutâmâ, gloss:dileseydik onu kırıntıya çevirirdik, source:56:65} der; A'lâ sûresinde {ar:فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ, tr:fe-cealehû gusâ'en ahvâ, gloss:sonra onu kapkara bir çerçöp yaptı, source:87:5}; Kehf sûresinde dünya hayatı, {ar:فَأَصْبَحَ هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ, tr:fe-asbaha heşîmen tezrûhu'r-riyâh, gloss:sonunda rüzgârların savurduğu kuru çöp oldu, source:18:45} diye biten bir benzetmedir. Yûnus sûresinde aynı benzetme bir "kılma" ile kapanır: {ar:فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:fe-cealnâhâ hasîden ke-en lem tagne bi'l-ems, gloss:onu sanki dün hiç yokmuş gibi biçilmiş kıldık, source:10:24}. Helak edilen kavimler için de aynı dil kullanılır: {ar:حَتَّىٰ جَعَلْنَٰهُمْ حَصِيدًا خَٰمِدِينَ, tr:hattâ cealnâhum hasîden hâmidîn, gloss:sonunda onları biçilmiş, sönmüş kıldık, source:21:15}, {ar:فَجَعَلْنَٰهُمْ غُثَآءًۭ, tr:fe-cealnâhum gusâ', gloss:onları çerçöp kıldık, source:23:41}, Semûd için {ar:فَكَانُوا۟ كَهَشِيمِ ٱلْمُحْتَظِرِ, tr:fe-kânû ke-heşîmi'l-muhtazır, gloss:ağıl yapanın kuru çalı çırpısı gibi oldular, source:54:31}. Âl-i İmrân sûresindeki benzetmede rüzgâr ekini vurur: {ar:كَمَثَلِ رِيحٍۢ فِيهَا صِرٌّ أَصَابَتْ حَرْثَ قَوْمٍۢ ظَلَمُوٓا۟ أَنفُسَهُمْ فَأَهْلَكَتْهُ, tr:ke-meseli rîhin fîhâ sırrun esâbet harse kavmin zalemû enfusehum fe-ehleketh, gloss:kendilerine zulmeden bir kavmin ekinine çarpıp onu yok eden, içinde dondurucu soğuk bulunan bir rüzgâr gibi, source:3:117}. Enbiyâ sûresinde İbrahim putları kırar ve fiil bu sûrenin son ayetindeki biçimin aynısıdır: {ar:فَجَعَلَهُمْ جُذَٰذًا, tr:fe-cealehum cuzâzâ, gloss:onları paramparça etti, source:21:58}. Sebe' sûresinde ise "yemek" içten çürütmedir: Süleyman'ın ölümünü onlara {ar:إِلَّا دَآبَّةُ ٱلْأَرْضِ تَأْكُلُ مِنسَأَتَهُۥ, tr:illâ dâbbetu'l-ardi te'kulu minse'eteh, gloss:asasını yiyen bir yer kurdundan başkası göstermedi, source:34:14}. Hâkka sûresinin sorusu da bu sonu tamamlar: {ar:فَهَلْ تَرَىٰ لَهُم مِّنۢ بَاقِيَةٍۢ, tr:fe-hel terâ lehum min bâkiyeh, gloss:onlardan geriye kalan bir şey görüyor musun, source:69:8}.

Kaynaklar: 105:5 كَعَصْفٍ ع ص ف B001; 105:5 كَعَصْفٍ ع ص ف B004; 105:5 فَجَعَلَهُمْ ج ع ل B002; 105:1 فَعَلَ ف ع ل B001; 105:5 مَّأْكُولٍۭ ء ك ل B001; 105:5 مَّأْكُولٍۭ ء ك ل B002; 105:5 مَّأْكُولٍۭ ء ك ل B006

## Buluşmalar

Sûrenin hareketi, açılıştaki görme çağrısı ile sondaki kırılmış ekin arasında kurulur ve imgeler bu yolda birbirine geçer. Görmenin imgesi ile düzenin imgesi aynı kökte buluşur: yolunu kaybetmeyi anlatan kök, bir işte doğruyu bulamamayı da anlatır. İkinci ayetteki düzen, hem bir yolda saptırılan bir yürüyüş hem de sağlıklı görmeyen bir aklın yanılmasıdır; okura "gör" denirken karşı tarafın düzeni "yolunu bulamaz". Fecr sûresinin "hicr sahibi" ile "Rabbinin ne yaptığını görmedin mi" sorusunu yan yana koyması, bu karşılaşmanın sahnesidir: akıl anlamındaki "hicr" ile taşın kökü aynıdır ve aklı olmayanlara taş iner.

Salınan sürüler, av ve fırtına tek bir sahnede durur. Göndermenin kökü hem otlağa salınan sürüleri hem gönderilen rüzgârları hem kısa bir oku adlandırır; üçüncü ayetin tek fiili, kuşların bölük bölük gelişini, rüzgârın esişini ve okun atılışını birlikte taşır. Atmanın kökü de iki yüzlüdür: ok ve taşla ava atmak ve iri damlalı bulutun yağması. Dördüncü ayetteki kuşlar, bir avcı gibi atar ve bir bulut gibi yağdırır. Mürselât sûresinin "gönderilenler" ile "şiddetle esenler"i ardışık koyması, göndermenin fırtınaya dönüşümünü sahneler; bu sûrede de gönderilen kuşlarla başlayan iş "asf" kelimesiyle biter.

Fırtına ile yazılmış taşlar siccîl kelimesinde buluşur. Kelime hem "salıverdiğim" hem "onlar için yazılmış olan" diye açıklanır: taşlar hem bir buluttan boşalan kovanın dökülüşü gibi iner hem de kimin için olduklarını taşır. Hûd ve Zâriyât sûrelerinin taş yağmuru, bu iki yüzü bir arada gösterir: yağdırılan siccîl taşları "Rabbinin katında işaretlenmiş"tir.

Savaş ile fırtına da siccîl'in kökünde birleşir: savaşın dönüşümlü talihi, su çekerken sırayla dökülen kovadan gelir. Fil sûresinde kova yalnızca bir tarafa, onların üzerine dökülür; fırtınanın boşalan kovası, savaşın sıra beklemeyen kovasıdır. Savaş ile ekin de "asf"ın kökünde buluşur: savaş bir kavmi silip götürür, rüzgâr şeyi kırıp asf gibi yapar ve rüzgârın insanları silip götürmesi bu kırılmaya benzetilerek söylenir.

Av ile ekin "yenmiş" kelimesinde iki ayrı sona ayrılır: yırtıcının yediği av ve ürünü alınıp içi yenmiş ekin. Ekin ile ateş de kuru yaprakta buluşur: kuruyup ufalanan yaprak, ateşin ilk yediği şeydir. Ağır ile hafifin yer değiştirmesi bu sahnelerin hepsinden geçer: en iri hayvan, en hafif kanatlıların avıdır ve sonunda en hafif şeye, ağırlığı olmayan bir yaprağa döner.

Bütün bu imgeleri birinci ve beşinci ayetler arasındaki fiiller bağlar. Rabbin "yapışı", kullanımdaki örneğiyle bir kırmadır; ilk "kılma" onların düzenini sapmaya, ikinci "kılma" onların kendilerini kırılmış ekine çevirir. Zümer sûresi bu yayı tek bir ayette gösterir: "görmedin mi" ile açılır, bir ekin çıkarır, sararmasını gösterir ve "onu kırıntı kılar". Fil sûresi aynı yayı bir topluluğun üzerine kurar: okur görmeye çağrılır, onların emeği yoldan çıkarılır, gökten bölük bölük salınan avcılar yazılmış taşlarını yağdırır ve sonunda geriye, ürünü yenmiş bir ekinin rüzgârla kırılmış yaprağı kalır.

