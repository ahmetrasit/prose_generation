Focus: 89:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_6/D.r13/context.md =====
# 89:6 — focus

أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ

Anchor translation (canonical reading, reference only):

Rabbinin Âd'a ne yaptığını görmedin mi?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | أَلَمْ | لَم |  | INTG;NEG |
| 2 | تَرَ | رَءَا | ر ء ي | V |
| 3 | كَيْفَ | كَيْف | ك ي ف | INTG |
| 4 | فَعَلَ | فَعَلَ | ف ع ل | V |
| 5 | رَبُّكَ | رَبّ | ر ب ب | N;PRON |
| 6 | بِعَادٍ | عَاد2 | ع و د | P;PN |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 89 — full text (context; no pericope)

- 89:1 وَٱلْفَجْرِ
- 89:2 وَلَيَالٍ عَشْرٍۢ
- 89:3 وَٱلشَّفْعِ وَٱلْوَتْرِ
- 89:4 وَٱلَّيْلِ إِذَا يَسْرِ
- 89:5 هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ
- 89:6 ◀ focus أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ
- 89:7 إِرَمَ ذَاتِ ٱلْعِمَادِ
- 89:8 ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ
- 89:9 وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ
- 89:10 وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ
- 89:11 ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ
- 89:12 فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ
- 89:13 فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ
- 89:14 إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ
- 89:15 فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ
- 89:16 وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ
- 89:17 كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ
- 89:18 وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 89:19 وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا
- 89:20 وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
- 89:21 كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا
- 89:22 وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
- 89:23 وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- 89:24 يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى
- 89:25 فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- 89:26 وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ
- 89:27 يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- 89:28 ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- 89:29 فَٱدْخُلِى فِى عِبَٰدِى
- 89:30 وَٱدْخُلِى جَنَّتِى


===== _commentary/v16/work/89_6/D.r13/01_dictionary.md =====
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

## ع و د (root_001058) — identity root of بِعَادٍ (w6)

- **B001** geri dönme ve yeniden yapma — geri dönmek · geri dönüş; yeniden yönelme · bir şeyi yeniden yapmak veya yinelemek · bir şeyin yeniden yapılmasını istemek · önceki işe yeniden dönmek · aynı soruyu tekrar tekrar sormak · ateşi yeniden nüksetmek · önceden yenmişken yeniden sunulan yemek · sık sık dönen; geri dön buyruğu
  أصل يدل على تثنية في الأمر (maqayis)؛ بدأ ثم عاد (maqayis;ayn)؛ عاد إليه يعود عودة وعودا رجع (sihah)؛ العود الرجوع إلى الشيء بعد الانصراف عنه (mufradat)؛ استعدته الشيء فأعاده (sihah)؛ تعاود القوم في الحرب وغيرها (sihah)؛ عاودته الحمى وعاوده بالمسألة (sihah)؛ عواد بمعنى عد (sihah)؛ العوادة ما أعيد من الطعام (sihah)
- **B002** dönüş yeri ve son varış — son varış; dönüş zamanı veya yeri
  المعاد كل شيء إليه المصير (maqayis)؛ والآخرة معاد للناس (maqayis)؛ الحج معاد الحاج (ayn)؛ لرادك إلى معاد يعني مكة (ayn)؛ المعاد المصير والمرجع (sihah)؛ الآخرة معاد الخلق (sihah)؛ المعاد يقال للعود وللزمان الذي يعود فيه وقد يكون للمكان الذي يعود إليه (mufradat)
- **B003** tek söz söylememek — ne söze başlamak ne de karşılık vermek
  رأيت فلانا ما يبدئ وما يعيد أي ما يتكلم ببادية ولا عادية (ayn)؛ ما يبدئ وما يعيد أي ما يتكلم ببادئة ولا عائدة (maqayis)
- **B004** tekrarla alışkanlık ve yatkınlık kazanma — alışkanlık; tekrarla yerleşen davranış · alışmak; alışkanlık edinmek · ısrarla sürdüren; deneyimli · alıştığı için yapabilen · çiftleşmeye alışmış erkek hayvan
  العادة الدربة والتمادي في شيء حتى يصير له سجية (maqayis;ayn)؛ المواظب على الشيء المعاود (maqayis;ayn)؛ بطل معاود (maqayis;ayn)؛ العادة معروفة والجمع عاد وعادات (sihah)؛ عاده واعتاده وتعوده (sihah)؛ عود كلبه الصيد فتعوده (sihah)؛ فلان معيد لهذا الأمر أي مطيق له (sihah;ayn)؛ المعيد الفحل الذي قد ضرب في الإبل مرات (sihah)؛ العادة اسم لتكرير الفعل والانفعال حتى يصير ذلك سهلا (mufradat)
- **B005** hasta veya yas ziyareti — hasta ziyareti · hasta ziyaretçileri · insanların ziyaret ettiği felaket veya yas hâli
  العيادة أن تعود مريضا (maqayis)؛ عدت المريض أعوده عيادة (sihah)؛ من العود عيادة المريض (mufradat)؛ الرجال عواد المريض والنساء عود (ayn)؛ فلان في معادة أي مصيبة يغشاه الناس (ayn)؛ لآل فلان معادة أي أمر يغشاهم الناس له (maqayis)
- **B006** kişiye dönen yarar ve iyilik — kişiye ulaşan yarar, şefkat veya bağış · bu senin için daha yararlı veya elverişlidir · iyilik yaptıktan sonra iyiliğini artırdı
  عاد فلان بمعروفه إذا أحسن ثم زاد (ayn)؛ العائدة وهو المعروف والصلة (maqayis)؛ ما أكثر عائدة فلان علينا (maqayis)؛ العائدة العطف والمنفعة (sihah)؛ هذا الشيء أعود عليك من كذا أي أنفع (sihah)؛ هذا الأمر أعود عليك أي أرفق بك (tahdhib)؛ العائدة اسم ما عاد به عليك المفضل من صلة أو فضل (tahdhib)؛ العائدة كل نفع يرجع إلى الإنسان (mufradat)
- **B007** yeniden gelen özel gün veya hâl — bayram; tekrarlanan toplanma veya sevinç günü · kişiye yeniden gelen kaygı, sevgi veya hâl · bayrama katılmak
  العيد ما يعتاد من خيال أو هم (maqayis)؛ العيد كل يوم مجمع (maqayis)؛ لأنه يعود كل عام (maqayis)؛ عيد قد مضى ذكره في محله لأن ذلك هو الأصل (maqayis-crossref)؛ العيد ما اعتادك من هم أو غيره (sihah)؛ العيد واحد الأعياد (sihah)؛ وقد عيدوا أي شهدوا العيد (sihah)؛ العيد ما يعاود مرة بعد أخرى (mufradat)؛ يستعمل العيد في كل يوم فيه مسرة (mufradat)
- **B008** gücü kalmış yaşlı deve — gücü kalmış yaşlı deve · yaşlı dişi deve veya koyun · ileri yaşa ulaşmak · savaşta yaşlı ve deneyimli kişilerden yardım al
  الجمل المسن فهو يسمى عودا (maqayis)؛ كأنه عاود الأسفار والرحل مرة بعد مرة (maqayis)؛ العود الجمل المسن وفيه سورة أي بقية (ayn)؛ العود المسن من الإبل (sihah)؛ زاحم بعود أو دع (sihah)؛ العود الجمل المسن الذي فيه بقية قوة (tahdhib)؛ عود الرجل تعويدا إذا أسن (tahdhib)؛ لا يقال عود إلا لبعير أو لشاة (tahdhib)؛ أنثى عودة (tahdhib)؛ البعير المسن اعتبارا بمعاودته السير والعمل (mufradat)
- **B009** eski yol ve köklü geçmiş — eski ve yeniden kullanılan yol · köklü saygınlık · eski akrabalık bağı
  العود الطريق القديم (ayn)؛ رحم عودة يعني قديمة (ayn)؛ السودد العود (maqayis)؛ الطريق القديم عود (maqayis)؛ العود الطريق القديم (sihah)؛ سودد عود أي قديم (sihah)؛ طريق عود إذا كان عاديا (tahdhib)؛ العود الطريق القديم الذي يعود إليه السفر (mufradat)
- **B010** tahta parçası, tütsülük odun veya telli çalgı — tahta parçası veya ince dal · tütsü için yakılan kokulu odun · telli müzik aleti
  الأصل الآخر فالعود وهو كل خشبة دقت (maqayis)؛ كل خشبة عود (maqayis)؛ العود الذي يتبخر به معروف (maqayis)؛ العود بالضم من الخشب واحد العيدان والأعواد (sihah)؛ العود الذي يضرب به (sihah)؛ العود الذي يتبخر به (sihah)؛ العود في الأصل الخشب الذي من شأنه أن يعود إذا قطع (mufradat)؛ خص بالمزهر المعروف وبالذي يتبخر به (mufradat)
- **B011** bağlayıcı eş sözünden ilgili davranışa dönüş — eş hakkındaki bağlayıcı sözden sonra ilgili davranışa dönmek
  ثم يعودون لما قالوا (mufradat)؛ عند أهل الظاهر هو أن يقول للمرأة ذلك ثانيا (mufradat)؛ عند أبي حنيفة العود في الظهار هو أن يجامعها (mufradat)؛ عند الشافعي هو إمساكها (mufradat)؛ يحمل على فعل ما حلف له أن لا يفعل (mufradat)
- **B012** biçime bağlı adlandırmalar — eski bir kavmin adı · eski; eski bir kavme bağlanan · erkek adı · bir kavme veya erkek deveye bağlanan soylu develer
  عاد قبيلة وهم قوم هود (sihah)؛ شيء عادي أي قديم كأنه منسوب إلى عاد (sihah)؛ عادياء اسم رجل (sihah)؛ العيدية نجائب منسوبة قالوا نسبت إلى عاد (maqayis)؛ العيدية إبل منسوبة إلى فحل يقال له عيد (mufradat)

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

## ECHO ع د د (root_000989) — for بِعَادٍ (w6): withheld observed target; not identity

- **B001** sayma, sayı ve sayıya göre bir topluluğa katma — bir şeyi sayıp miktarını belirlemek · sayı; sayılanın miktarı · sayıca çokluk · sayılmış veya sayıyla sınırlandırılmış · iyiler arasında sayılmak · az ya da çok sayıda topluluk · sayıları on bini aşmak
  عددت الشيء عدا أي أحصيته (maqayis;ayn;sihah;tahdhib)؛ العدد مقدار ما يعد (maqayis)؛ العديد الكثرة (maqayis;ayn;sihah;tahdhib)؛ فلان في عداد الصالحين (maqayis;ayn;sihah)؛ العدد آحاد مركبة (mufradat)
- **B002** gelecekteki bir iş için hazırlama ve hazır bulundurma — bir şeyi ilerideki iş için hazırlamak · ilerideki ihtiyaç için hazırlanmış mal, silah veya gereç · bir işe hazırlanmak ve donanmak
  أعددت الشيء إعدادا (maqayis)؛ أعددت الشيء هيأته (ayn)؛ العدة من السلاح ما اعتددته (jamhara)؛ أعده لأمر كذا هيأه له (sihah)؛ العدة ما أعد لأمر يحدث مثل الأهبة (tahdhib)؛ أعددت هذا لك أي جعلته بحيث تعده وتتناوله (mufradat)
- **B003** sayılı zaman dilimi ve bağlama bağlı bekleme ya da tamamlama süresi — kadının yeniden evlenmeden önce beklemesi gereken süre · kaçırılan günler kadar başka günlerde yerine getirmek · sayılı ve belirli günler
  عدة المرأة أيام قروئها (ayn)؛ عدة المرأة معروفة (jamhara)؛ عدة المرأة أيام أقرائها (sihah)؛ العدة عدة المرأة شهورا كانت أو أقراء أو وضع حمل (tahdhib)؛ فعدة من أيام أخر أي عليه أيام بعدد ما فاته (mufradat)؛ الأيام المعدودات أيام التشريق (sihah;tahdhib;mufradat)
- **B004** kaynağı kesilmeyen kalıcı su ve su yeri — eskiden beri var olan, tükenmeyen sürekli su · sürekli sular veya kalıcı su yerleri · köklü ve eski saygınlık
  العد مجتمع الماء وجمعه أعداد (maqayis;ayn)؛ العد من الماء القديم الذي لا ينتزح (jamhara)؛ العد بالكسر الماء الذي له مادة لا تنقطع (sihah)؛ الماء العد الدائم الذي لا انقطاع له (tahdhib)؛ ماء عد (mufradat)
- **B005** belirli zaman ve bilinen aralıklarla geri gelme — sokulma ağrısının belirli aralıklarla alevlenmesi · bana belirli zamanlarda yeniden baş göstermek · zaman, dönem veya en parlak çağ · yayın tekrarlanan titreşimi veya sesi · ayda bir gerçekleşen buluşma · dağıtım, yoklama veya geçici toplanma günü · belirli aralıklarla gelen akıl bulanıklığı
  العداد اهتياج وجع اللديغ (maqayis;ayn;sihah)؛ العداد الشيء الذي يأتيك لوقت (tahdhib)؛ عدان الشيء عهده وزمانه (mufradat)؛ كان ذلك في عدان شبابه (ayn;sihah;tahdhib)؛ عداد القوس أن تنبض بها ساعة بعد ساعة (maqayis)؛ عداد القوس صوتها (sihah;tahdhib)؛ يوم العداد يوم العطاء (maqayis;tahdhib)
- **B006** karşılıklı paydaşlık, pay ve denk sayılma — mal veya değer bakımından karşılıklı paydaş olmak · paylar, denkler veya mirastaki karşılıklı paydaşlar · onun dengi ve karşılığı
  هم يتعادون إذا اشتركوا فيما يعدد به بعضهم على بعض (ayn;tahdhib)؛ العدائد النظراء (tahdhib)؛ العدائد الحصص (tahdhib)؛ من يعاده في الميراث (sihah)؛ فلان عد فلان أي قرنه (tahdhib)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:6, and ## Buluşmalar) =====
## Gözetleme yeri ve bakan göz

Altıncı ayet dinleyenin gözünü olup bitene çevirir: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ, tr:e-lem tera keyfe feale rabbuke bi-Âd, gloss:Rabbinin Âd'a ne yaptığını görmedin mi, source:89:6}. Görmek, gözle ya da kalple bakmaktır: {ar:نظر وإبصار بعين أو بصيرة, tr:nazarun ve ibsârun bi-aynin ev basîra, gloss:gözle ya da basiretle bakıp görmek, source:"ر ء ي,B001"}. Aynı kalıp Fil sahiplerinin akıbetini anlatırken de kullanılır: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَٰبِ ٱلْفِيلِ, tr:e-lem tera keyfe feale rabbuke bi-ashâbi'l-fîl, gloss:Rabbinin fil sahiplerine ne yaptığını görmedin mi, source:105:1}. Dinleyen, bir olayın gözlemcisi yapılır.

Gözlenen şey yolda olan insanlardır. Dördüncü ayetin fiili gece yürüyenleri de adlandırır: {ar:السارية للقوم الذين يسرون بالليل, tr:es-sâriye li'l-kavmi'llezîne yesrûne bi'l-leyl, gloss:sâriye, gece yol alan topluluktur, source:"س ر ي,B001"}. Dokuzuncu ayetteki fiilin yanında ülkeleri boydan boya geçmek duyulur: {ar:جبت البلاد أجوبها وأجيبها واجتبتها إذا قطعتها, tr:cubtu'l-bilâde ecûbuhâ ve ecîbuhâ ve'ctebtuhâ izâ kata'tuhâ, gloss:ülkeleri boydan boya geçtim, source:"ج و ب,B002"}. On birinci ayette bu yolcular ülkelerde sınırı aşar: {ar:مجاوزة الحد في العصيان, tr:mucâvezetu'l-haddi fi'l-isyân, gloss:isyanda sınırı geçmek, source:"ط غ ي,B001"}. Ayetlerin anlamı kazmak ve azmaktır. Yanında yol alan, ülke aşan ve sınırı geçen yolcular duyulur.

On dördüncü ayet yolun üzerindeki yeri adlandırır: {ar:إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ, tr:inne rabbeke le-bi'l-mirsâd, gloss:Rabbin elbette gözetleme yerindedir, source:89:14}. Mirsâd hem yolun kendisidir, {ar:المرصاد الطريق, tr:el-mirsâd et-tarîk, gloss:mirsâd yoldur, source:"ر ص د,B003"}, hem de gözcünün beklediği yer: {ar:المرصاد المكان الذي يرصد به الراصد, tr:el-mirsâdu'l-mekânu'llezî yersudu bihi'r-râsıd, gloss:mirsâd, gözcünün gözetlediği yerdir, source:"ر ص د,B003"}. Gözcü bir şeyi kollayan kişidir: {ar:الراصد للشئ المراقب له, tr:er-râsıdu li'ş-şey'i el-murâkıbu leh, gloss:râsıd, bir şeyi gözetleyendir, source:"ر ص د,B001"}. Aynı kök yolda pusu kuran yılana da ad verir: {ar:يقال للحية التي ترصد المارة على الطريق رصيد, tr:yukâlu li'l-hayyeti'lletî tersudu'l-mârrate ale't-tarîki rasîd, gloss:yolda geçenleri kollayan yılana rasîd denir, source:"ر ص د,B001"}. Bu düzenin işleyişi şöyledir: gözcü kimseyi kovalamaz, yolun geçtiği yerde bekler. Her yolcu oradan geçmek zorundadır. Bir önceki ayetteki dökme fiili bu yılanın hareketini de anlatır: {ar:صبت الحية عليه إذا ارتفعت فانصبت عليه من فوق, tr:sabbeti'l-hayyetu aleyhi izertefeat fensabbet aleyhi min fevk, gloss:yılan kalkıp yukarıdan üstüne çullandı, source:"ص ب ب,B008"}. Surenin sıralaması da bu düzene uyar. Önce darbe iner, gözetleme yeri ancak sonra adlandırılır. Yolcular gözcünün varlığını vuruldukları anda öğrenir.

Kur'an aynı yeri başka sahnelerde de kurar. Kıyamet anlatılırken cehennem için {ar:إِنَّ جَهَنَّمَ كَانَتْ مِرْصَادًۭا, tr:inne cehenneme kânet mirsâdâ, gloss:cehennem bir gözetleme yeridir, source:78:21} denir. Antlaşmayı bozanlara karşı verilen emir şöyledir: {ar:وَٱقْعُدُوا۟ لَهُمْ كُلَّ مَرْصَدٍۢ, tr:vak'udû lehum kulle marsad, gloss:onlar için her gözetleme yerinde oturun, source:9:5}. İblis de Allah'a şöyle der: {ar:لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ, tr:le-ek'udenne lehum sırâtake'l-mustekîm, gloss:onlar için senin dosdoğru yolunun üstünde oturacağım, source:7:16}. Şuayb kavmine yollarda pusu kurmamalarını söyler: {ar:وَلَا تَقْعُدُوا۟ بِكُلِّ صِرَٰطٍۢ تُوعِدُونَ, tr:ve lâ tak'udû bi-kulli sırâtin tûidûn, gloss:tehdit ederek her yolun başında oturmayın, source:7:86}. Cinler gökte kendilerini bekleyen bir alev bulur: {ar:يَجِدْ لَهُۥ شِهَابًۭا رَّصَدًۭا, tr:yecid lehû şihâben rasadâ, gloss:kendisini gözetleyen bir alev bulur, source:72:9}. Allah elçisinin önüne ve arkasına gözcüler koyar {source:72:27}. İnsanın söylediği her sözün yanında da hazır bir gözcü vardır: {ar:مَّا يَلْفِظُ مِن قَوْلٍ إِلَّا لَدَيْهِ رَقِيبٌ عَتِيدٌۭ, tr:mâ yelfızu min kavlin illâ ledeyhi rakîbun atîd, gloss:ağzından çıkan her sözün yanında hazır bir gözcü vardır, source:50:18}.

Bakmanın bir de insanın içindeki yüzü vardır. On beşinci ve yirmi üçüncü ayetlerdeki "insan" kelimesi göz bebeğindeki küçük sureti de adlandırır: {ar:إنسان العين المثال الذي يرى في السواد, tr:insânu'l-ayn el-misâlu'llezî yurâ fi's-sevâd, gloss:gözün insanı, gözbebeğinin karasında görünen küçük surettir, source:"ء ن س,B005"}. Bu tanımda misal ve görmek kelimeleri birlikte geçer. Sekizinci ayetin kökü sureti, {ar:التمثال الصورة, tr:et-timsâl es-sûra, gloss:timsal, surettir, source:"م ث ل,B008"}, ve görülerek alınan dersi de adlandırır: {ar:يكون المثل بمعنى العبرة, tr:yekûnu'l-meselu bi-ma'ne'l-ibra, gloss:mesel, ibret anlamına da gelir, source:"م ث ل,B011"}. Beşinci ayetin hicr kökü gözün çevresine de ad verir: {ar:ومحجر العين ما يدور بها, tr:ve mahcaru'l-ayni mâ yedûru bihâ, gloss:gözün mahceri, onu çevreleyen yerdir, source:"ح ج ر,B006"}. Üçüncü ayetteki çift kelimesi de bir tek şeyi iki gören gözü adlandırır: {ar:عين شافعة تنظر نظرين, tr:aynun şâfiatun tenzuru nazarayn, gloss:şâfia göz, iki bakışla bakan gözdür, source:"ش ف ع,B006"}. Sure insana Âd'ı, Semûd'u ve Firavun'u göstermiştir. İnsan ise hemen ardından kendi hâline bakar ve tek bir sınavı iki ayrı hüküm olarak okur: bolluğa ikram, darlığa aşağılanma der. Kur'an bu bakışın kendini nasıl gördüğünü söyler {source:96:7}. Âd'a da kulaklar, gözler ve gönüller verilmişti, ama onlara bir yararı olmadı: {ar:فَمَآ أَغْنَىٰ عَنْهُمْ سَمْعُهُمْ وَلَآ أَبْصَٰرُهُمْ, tr:fe-mâ ağnâ anhum sem'uhum ve lâ ebsâruhum, gloss:ne kulakları ne gözleri onlara bir yarar sağladı, source:46:26}. Kıyamet günü örtü kalkar: {ar:فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ, tr:fe-keşefnâ anke ğitâeke fe-basaruke'l-yevme hadîd, gloss:örtünü üstünden kaldırdık, bugün gözün keskindir, source:50:22}.

Kaynaklar: 89:3 ٱلشَّفْعِ ش ف ع B006; 89:4 يَسْرِ س ر ي B001; 89:5 حِجْرٍ ح ج ر B006; 89:6 تَرَ ر ء ي B001; 89:8 مِثْلُهَا م ث ل B008; 89:8 مِثْلُهَا م ث ل B011; 89:9 جَابُوا۟ ج و ب B002; 89:11 طَغَوْا۟ ط غ ي B001; 89:13 فَصَبَّ ص ب ب B008; 89:14 لَبِٱلْمِرْصَادِ ر ص د B001; 89:14 لَبِٱلْمِرْصَادِ ر ص د B003; 89:15 ٱلْإِنسَٰنُ ء ن س B005

## Yol, binek ve dönüş

Surenin kelimeleri bir yolculuğun aşamalarını sırayla taşır. Dördüncü ayette gece yürüyüşü başlar: {ar:السرى سير الليل, tr:es-surâ seyru'l-leyl, gloss:gece yürüyüşü, source:"س ر ي,B001"}. Kur'an bu kökü kul ve gece kelimeleriyle aynı cümlede kullanır: {ar:سُبْحَٰنَ ٱلَّذِىٓ أَسْرَىٰ بِعَبْدِهِۦ لَيْلًۭا, tr:subhâna'llezî esrâ bi-abdihî leylen, gloss:kulunu geceleyin yürüten Allah'ı tesbih ederim, source:17:1}. Dokuzuncu ayetteki fiilin yanında ülke ülke dolaşan yolcu duyulur: {ar:رجل جواب إذا كان قطاعا للبلاد, tr:raculun cevvâbun izâ kâne kattâan li'l-bilâd, gloss:cevvâb, ülkeleri durmadan aşan adamdır, source:"ج و ب,B002"}. On beşinci ve on altıncı ayetlerdeki sınav fiilinin yanında da yolun bineği yıpratması duyulur: {ar:ناقة بلو سفر أبلاها السفر, tr:nâkatun ilvu seferin eblâhe's-sefer, gloss:yolculuğun yıprattığı dişi deve, source:"ب ل و,B001"}. Elbisenin eskimesi de aynı köktendir: {ar:بلي الثوب يبلى بلى وبلاء, tr:beliye's-sevbu yeblâ bilen ve belâ', gloss:elbise eskidi, yıprandı, source:"ب ل و,B001"}. Ayette anlam sınamaktır. Yanında kullanıldıkça yıpranan, yürüdükçe tükenen bir binek duyulur. Sınavın, insanın kendisine ait sandığı şeyi aşındırdığı da duyulur.

Yolculuğun karşısında yere yapışmak vardır. Yirminci ayetteki sevgi kelimesi bir şeye yapışıp kalmakla açıklanır: {ar:الحب والمحبة اشتقاقه من أحبه إذا لزمه, tr:el-hubbu ve'l-mahabbe iştikâkuhû min ehabbehû izâ lezimeh, gloss:sevgi kelimesi bir şeye yapışıp ondan ayrılmamaktan türer, source:"ح ب ب,B002"}. Aynı fiil inatla yerinden kalkmayan deveyi de anlatır: {ar:أحب البعير إذا حرن ولزم مكانه, tr:ehabbe'l-baîru izâ harana ve lezime mekâneh, gloss:deve inat edip yerinden kalkmayınca "ehabbe" denir, source:"ح ب ب,B005"}. Malı yapışarak seven insan çöküp kalmış bir bineğe benzer. Sekizinci ve on birinci ayetlerdeki "ülkeler" kelimesi de yerleşip kalmayı taşır: {ar:بلد بالمكان أقام به فهو بالد, tr:belede bi'l-mekâni ekâme bih, gloss:bir yerde kalıp yerleşti, source:"ب ل د,B009"}, {ar:بلد الرجل بالأرض إذا لزق بها, tr:belede'r-raculu bi'l-ardı izâ leziga bihâ, gloss:adam yere yapıştı, source:"ب ل د,B010"}. Devenin göğsünü yere koyup çökmesi de aynı köktendir: {ar:وضعت الناقة بلدتها بالأرض إذا بركت, tr:vedaati'n-nâkatu beldetehâ bi'l-ardı izâ berakat, gloss:deve göğsünü yere koyup çöktü, source:"ب ل د,B002"}. Yirmi birinci ayetteki yer kelimesinin kökü yere ağırlaşmayı da söyler: {ar:التأرض أيضا التثاقل إلى الأرض, tr:et-teerrudu eydan et-tesâkulu ile'l-ard, gloss:teerrud, yere doğru ağırlaşmaktır, source:"ء ر ض,B006"}. Onuncu ayetteki kazık ayağı yere çakar, yirmi altıncı ayetteki bağ ise bağlar. Kur'an bu ağırlığı bir çağrı sahnesinde adlandırır. Allah yolunda harekete geçmeye çağrılan müminlere şöyle seslenir: {ar:ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ ۚ أَرَضِيتُم بِٱلْحَيَوٰةِ ٱلدُّنْيَا مِنَ ٱلْءَاخِرَةِ, tr:issâkaltum ile'l-ard, e-radîtum bi'l-hayâti'd-dunyâ mine'l-âhira, gloss:yere çakılıp kaldınız; dünya hayatına ahiretten daha mı razı oldunuz, source:9:38}. Yer, razı olmak ve hayat: surenin sonundaki kelimeler burada ters yönde dizilmiştir. Ayetlerine rağmen yere saplanıp kalan adam da şöyle anlatılır: {ar:وَلَٰكِنَّهُۥٓ أَخْلَدَ إِلَى ٱلْأَرْضِ وَٱتَّبَعَ هَوَىٰهُ, tr:ve lâkinnehû ahlede ile'l-ardı ve'ttebea hevâh, gloss:ama o yere saplanıp kaldı ve hevesine uydu, source:7:176}.

Yolun sonu dönüştür. Altıncı ayette adı geçen Âd, Arapçada dönüş anlamındaki kökün altında sayılır: {ar:عاد قبيلة وهم قوم هود, tr:Âd kabîle, ve hum kavmu Hûd, gloss:Âd bir kabiledir, Hûd'un kavmidir, source:"ع و د,B012"}. Aynı kök varılacak yeri de adlandırır: {ar:المعاد المصير والمرجع, tr:el-meâd el-masîru ve'l-merci', gloss:meâd, varılacak ve dönülecek yerdir, source:"ع و د,B002"}. Âd bir özel addır ve bu anlamı taşımaz, yalnız harfleri dönüşü çağrıştırır. Kur'an Peygamber'e dönüş yerini vaat eder: {ar:لَرَآدُّكَ إِلَىٰ مَعَادٍۢ, tr:le-râdduke ilâ meâd, gloss:seni elbette dönüş yerine döndürecektir, source:28:85}. Yirmi yedinci ayet yolcuyu durulmuş olarak karşılar: {ar:يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ, tr:yâ eyyetuhe'n-nefsu'l-mutmainne, gloss:ey huzura kavuşmuş can, source:89:27}. Huzur, sarsıntıdan sonra gelen dinginliktir: {ar:الطمأنينة والاطمئنان السكون بعد الانزعاج, tr:et-tume'nîne ve'l-itmi'nân es-sukûnu ba'de'l-inzi'âc, gloss:itminan, sarsıntıdan sonraki dinginliktir, source:"ط م ء ن,B001"}. Kur'an bu dinginliğin kaynağını da söyler: {ar:أَلَا بِذِكْرِ ٱللَّهِ تَطْمَئِنُّ ٱلْقُلُوبُ, tr:elâ bi-zikri'llâhi tatmainnu'l-kulûb, gloss:bilin ki kalpler ancak Allah'ı anmakla huzura kavuşur, source:13:28}. Yirmi sekizinci ayetteki çağrı şöyledir: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ, tr:irciî ilâ rabbiki, gloss:Rabbine dön, source:89:28}. Dönmek, başlanılan yere geri gitmektir: {ar:الرجوع العود إلى ما كان منه البدء, tr:er-rucûu'l-avdu ilâ mâ kâne minhu'l-bed', gloss:rücû, başlangıç noktasına dönmektir, source:"ر ج ع,B001"}. Aynı kök, bir yolculuktan ötekine geri gönderilen yorgun hayvanı da adlandırır: {ar:الرجيع من الدواب ما رجعته من سفر إلى سفر وهو الكال, tr:er-recî' mine'd-devâbbi mâ raca'tehû min seferin ilâ sefer, ve huve'l-kâll, gloss:recî', bir yolculuktan ötekine döndürülen yorgun hayvandır, source:"ر ج ع,B014"}. Çağrılan can ise yeni bir yola gönderilmez. Yolun bittiği yere döndürülür. Kur'an insanın bütün çabasını bu yöne bağlar: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًۭا فَمُلَٰقِيهِ, tr:yâ eyyuhe'l-insânu inneke kâdihun ilâ rabbike kedhan fe-mulâkîh, gloss:ey insan, sen Rabbine doğru zahmetle çabalıyorsun ve O'na kavuşacaksın, source:84:6}. Varılacak yer de bir yerleşmedir: {ar:إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمُسْتَقَرُّ, tr:ilâ rabbike yevmeizini'l-mustekarr, gloss:o gün varılıp karar kılınacak yer Rabbinin huzurudur, source:75:12}. Azan insana da aynı söz söylenir: {ar:إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ, tr:inne ilâ rabbike'r-ruc'â, gloss:dönüş Rabbinedir, source:96:8}. Sınanıp musibete uğrayanların sözü de dönüşle biter: {ar:إِنَّا لِلَّهِ وَإِنَّآ إِلَيْهِ رَٰجِعُونَ, tr:innâ li'llâhi ve innâ ileyhi râciûn, gloss:biz Allah'a aitiz ve O'na döneceğiz, source:2:156}. Yorgun binek imgesi ile dönüş çağrısı burada aynı insanda birleşir. Dönüşün tersi de Kur'an'dadır. Ölüm gelince inkârcı geri gönderilmeyi ister: {ar:رَبِّ ٱرْجِعُونِ, tr:rabbi'rciûn, gloss:Rabbim, beni geri gönderin, source:23:99}. Cevap ise surenin iki kez kullandığı kelimedir: {ar:كَلَّآ ۚ إِنَّهَا كَلِمَةٌ هُوَ قَآئِلُهَا, tr:kellâ, innehâ kelimetun huve kâiluhâ, gloss:hayır, bu yalnızca onun söylediği bir sözdür, source:23:100}. Yolun en son aşaması giriştir: {ar:فَٱدْخُلِى فِى عِبَٰدِى, tr:fedhulî fî ibâdî, gloss:kullarımın arasına gir, source:89:29}. Kur'an bu girişi kapılar açılırken bölük bölük sürülen bir kafile olarak da gösterir: {ar:وَسِيقَ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ إِلَى ٱلْجَنَّةِ زُمَرًا, tr:ve sîka'llezîne'ttekav rabbehum ile'l-cenneti zumerâ, gloss:Rablerinden sakınanlar bölük bölük cennete sürülür, source:39:73}.

Kaynaklar: 89:4 يَسْرِ س ر ي B001; 89:6 بِعَادٍ ع و د B002; 89:6 بِعَادٍ ع و د B012; 89:8 ٱلْبِلَٰدِ ب ل د B002; 89:8 ٱلْبِلَٰدِ ب ل د B009; 89:11 ٱلْبِلَٰدِ ب ل د B010; 89:9 جَابُوا۟ ج و ب B002; 89:15 ٱبْتَلَىٰهُ ب ل و B001; 89:20 وَتُحِبُّونَ ح ب ب B002; 89:20 وَتُحِبُّونَ ح ب ب B005; 89:21 ٱلْأَرْضُ ء ر ض B006; 89:27 ٱلْمُطْمَئِنَّةُ ط م ء ن B001; 89:28 ٱرْجِعِىٓ ر ج ع B001; 89:28 ٱرْجِعِىٓ ر ج ع B014; 89:29 فَٱدْخُلِى د خ ل B001

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

