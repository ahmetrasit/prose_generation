Focus: 107:1. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/OZTURK/_projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. No other command or tool is available.

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


===== _commentary/v16/work/107_1/D.r13/context.md =====
# 107:1 — focus

أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ

Anchor translation (canonical reading, reference only):

Dini yalanlayanı gördün mü?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | أَرَءَيْتَ | رَءَا | ر ء ي | INTG;V;PRON |
| 2 | ٱلَّذِى | ٱلَّذِى |  | REL |
| 3 | يُكَذِّبُ | كَذَّبَ | ك ذ ب | V |
| 4 | بِٱلدِّينِ | دِين | د ي ن | P;DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 107 — full text (context; no pericope)

- 107:1 ◀ focus أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ
- 107:2 فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ
- 107:3 وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 107:4 فَوَيْلٌۭ لِّلْمُصَلِّينَ
- 107:5 ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ
- 107:6 ٱلَّذِينَ هُمْ يُرَآءُونَ
- 107:7 وَيَمْنَعُونَ ٱلْمَاعُونَ


===== _commentary/v16/work/107_1/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ر ء ي (root_000531) — identity root of أَرَءَيْتَ (w1)

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

## ك ذ ب (root_001290) — identity root of يُكَذِّبُ (w3)

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

## د ي ن (root_000504) — identity root of بِٱلدِّينِ (w4)

- **B001** boyun eğerek uyma ve buna dayalı inanç düzeni — boyun eğme, kulluk ve inanç düzeni · ona boyun eğdi ve buyruğuna uydu · gerçek inanç yolu · hükümdarın buyruğu ya da yargısı
  أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل (maqayis)؛ فالدين الطاعة (maqayis;sihah)؛ الدين لله طاعته والتعبد له (tahdhib)؛ الدين كالملة اعتبارا بالطاعة والانقياد للشريعة (mufradat)
- **B002** yargılayıp hesap görerek karşılığını verme — hesap, yargı ve yapılanın karşılığı · hesap ve karşılık günü · hesaba çekilip karşılığı verilecek olanlar · yargılayan ve karşılığını veren · hükümdarın buyruğu ya da yargısı · kendini alçalttı ya da hesaba çekti
  يوم الدين أي يوم الحكم والحساب والجزاء (maqayis)؛ الدين الجزاء والمكافأة (sihah)؛ الدين الحساب ومنه مالك يوم الدين ومالك يوم الجزاء (tahdhib)؛ غير مدينين أي غير مجزيين (mufradat)
- **B003** borç alıp verme ve vadeli ödeme ilişkisi — borç ve vadeli ödeme yükümlülüğü · onunla borç alıp verme işlemi yaptı · ona ödünç verdi · ödünç aldı ve borçlandı · borçlu veya çok borçlanmış kişi · onu vadeli olarak sattım
  الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء (maqayis)؛ الدين واحد الديون وتداينوا تبايعوا بالدين (sihah)؛ دنت الرجل أقرضته وأدنت الرجل إذا أقرضته (tahdhib)؛ التداين والمداينة دفع الدين (mufradat)
- **B004** zorla alçaltıp egemenliği altına alma — onu alçalttı, boyunduruk altına aldı ve köleleştirdi · topluluğu alçalttım ve köleleştirdim · onu mülk edindim veya buyruğum altına aldım · köleleştirilmiş erkek · köleleştirilmiş kadın · kendini alçalttı ya da hesaba çekti · kalbini alçaltan şey; ayrıca alışkanlık, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz
  العبد مدين كأنهما أذلهما العمل ويا دين قلبك أي أذل (maqayis)؛ دانه دينا أي أذله واستعبده ودينته ملكته (sihah)؛ غير مدينين غير مملوكين ودنت القوم أدينهم إذا أذللتهم (tahdhib)؛ المدين والمدينة العبد والأمة (mufradat)
- **B005** alışılmış davranış ve öteden beri bilinen hal — alışkanlık, olağan iş ve öteden beri bilinen hal · kalbinin alışkanlığı; ayrıca alçaltma, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz
  العادة يقال لها دين (maqayis)؛ الدين بالكسر العادة والشأن (sihah)؛ الدين أيضا العادة (tahdhib)؛ الحال والأمر الذي تعهده (maqayis)
- **B006** kent — kent; yöneticilerin buyruğuna uyulan yer olarak açıklanan büyük yerleşim
  المدينة كأنها مفعلة سميت بذلك لأنها تقام فيها طاعة ذوي الأمر (maqayis)؛ ومنه سمى المصر مدينة (sihah)؛ جعل بعضهم المدينة من هذا الباب (mufradat)
- **B007** kişiyi sözüne ve vicdani sorumluluğuna göre değerlendirme — onu vicdani yükümlülüğüyle baş başa bıraktı · yargıda veya Tanrı'yla arasındaki konuda sözünü doğru kabul etti · yeminini kendi niyetine göre değerlendirdi
  دينت الرجل تديينا إذا وكلته إلى دينه (sihah)؛ دينت الرجل في القضاء وفيما بينه وبين الله أي صدقته (tahdhib)؛ دينت الحالف أي نويته فيما حلف وهو التديين (tahdhib)

## ECHO ر و ي (root_000615) — for أَرَءَيْتَ (w1): withheld observed target; not identity

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

===== _commentary/v16/out/s107/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 107:1, and ## Buluşmalar) =====
## Çağrılan bakış ve aranan bakış

Sure bir bakma emriyle açılır: {ar:أَرَءَيْتَ, tr:eraeyte, gloss:gördün mü?, source:107:1}. Sözcük "görmek" fiilinden gelir. Ama bu kalıpta görüp görmediğini sormaz; dinleyicinin dikkatini bir yere çeker ve ondan bir cevap bekler. Arapçada bu kalıp için {ar:يجري أرأيت مجرى أخبرني وكل ذلك فيه معنى التنبيه, tr:yecrî eraeyte mecrâ ahbirnî ve küllü zâlike fîhi ma‘ne't-tenbîh, gloss:"gördün mü?" "bana haber ver" yerine kullanılır ve hepsinde uyarı anlamı vardır, source:"ر ء ي,B013"} denir. Dinleyiciye bir adam gösterilir ve gördüğünü söylemesi istenir. Kökün temel tanımı bu bakışın ne kadar derine indiğini de belirler: {ar:نظر وإبصار بعين أو بصيرة, tr:nazar ve ibsâr bi-aynin ev basîra, gloss:gözle ya da iç görüyle bakıp görmek, source:"ر ء ي,B001"}. Dinleyiciden adamın kılığına değil, ne olduğuna bakması istenmektedir.

Sure aynı kökten bir kelimeyle kapanır: {ar:ٱلَّذِينَ هُمْ يُرَآءُونَ, tr:ellezîne hum yurâûn, gloss:onlar ki gösteriş yaparlar, source:107:6}. Fiilin bu kalıbı iki tarafı birbirine bağlar. Kök, aynı alandan {ar:تراءى القوم إذا رأى بعضهم بعضا, tr:terâe'l-kavmu izâ raâ ba‘duhum ba‘dâ, gloss:topluluk birbirini gördüğünde "terâe" denir, source:"ر ء ي,B004"} anlamını da verir. Gösteriş yapan kişi insanların ona baktığını gözler, insanlar da onun yaptığına bakar. Yapılan işin tanımı da açıktır: {ar:وفعل ذلك رئاء الناس وهو أن يفعل شيئا ليراه الناس, tr:ve fe‘ale zâlike riâe'n-nâs ve huve en yef‘ale şey'en li-yerâhu'n-nâs, gloss:bunu insanlara göstermek için yaptı; yani bir şeyi insanlar görsün diye yapmak, source:"ر ء ي,B005"}. Kök bu işin aletini de adlandırır: {ar:المرآة ما يرى فيه صورة الأشياء, tr:el-mir'âtu mâ yurâ fîhi sûratu'l-eşyâ, gloss:ayna, eşyanın görüntüsünün içinde görüldüğü şeydir, source:"ر ء ي,B006"}. Bir fiil, aynayı başkasının önüne tutmayı anlatır: {ar:رأيت الرجل ترئية إذا أمسكت له المرآة لينظر فيها, tr:ra’eytu'r-racule ter’iyeten izâ emsekte lehu'l-mir'âte li-yanzura fîhâ, gloss:adama bakması için ayna tuttuğunda "ra’eytu'r-racul" dersin, source:"ر ء ي,B012"}. Ayna bir görüntü verir ama derinliği yoktur; arkasında, gösterdiği şeyden hiçbir şey bulunmaz. Gösteriş yapan kişi de işini bir ayna gibi insanların önüne tutar. Onların orada gördüğü {ar:الري ما أريت القوم من حسن الشارة والهيئة, tr:er-riyyu mâ eryte'l-kavme min husni'ş-şâreti ve'l-hey'e, gloss:topluluğa gösterdiğin güzel kılık ve duruş, source:"ر ء ي,B006"} olur.

Bu imgeler ve aşağıdaki bütün aile imgeleri, kelimenin ayetteki anlamının yerine geçmez; o anlamın yanında duyulur. Altıncı ayetteki fiil "gösteriş yaparlar" demektir. Ayna o anlamın işleyişini görünür kılar.

Bir açıklama "gösteriş yapıyorlar" der ve geçer. Surenin çerçevesi ise iki bakışı karşı karşıya koyar. Bir yanda Allah'ın dinleyiciye emrettiği bakış vardır; bu bakış adamın ne olduğuna kadar iner. Öbür yanda bu adamların peşinde koştuğu bakış vardır; o, yüzeyde kalır. Dinleyici gerçek seyircinin yerine konur, adamların aradığı seyirciler ise çerçevenin dışında kalır.

Sure ilerledikçe bakış yönlendirilir. Birinci ayet bakmayı emreder. İkinci ayet bir işaretle cevap verir: {ar:فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ, tr:fe-zâlike'llezî yedu‘‘u'l-yetîm, gloss:işte o, yetimi itip kakandır, source:107:2}. "Gördün mü?" sorusunun cevabı bir delil değildir; bir eli gösteren parmaktır. İnkâr bir hareketin içinde görünür hâle gelir. Üçüncü ayet görülmesi mümkün olmayan bir şeyi ekler: yapılmayan bir teşvik. Kimsenin yokluğunu fark etmediği bir sözdür bu. Dördüncü ve beşinci ayetler en göz önünde olan işe, namaza gelir. Altıncı ayet o işin kimin gözü için yapıldığını söyler. Kökün bir kolu bu ikisini tek cümlede birleştirir: {ar:يرآءون الناس إذا أبصرهم الناس صلوا وإذا لم يروهم تركوا الصلاة, tr:yurâûne'n-nâs, izâ ebsarahumu'n-nâsu sallev ve izâ lem yerevhum terakü's-salâh, gloss:insanlara gösteriş yaparlar; insanlar onları görürse namaz kılarlar, görmezlerse namazı bırakırlar, source:"ر ء ي,B005"}. Böyle bir namaz ancak bakan göz varken vardır. Yedinci ayet bu yüzden ters yönde biter. Esirgenen şey küçüktür ve kimsenin görmediği bir yerde esirgenir.

Kuran aynı açılışı başka bir yerde, yine namazın karşısında kurar. Alak suresinde Allah Peygamber'e seslenir: {ar:أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ, tr:eraeyte'llezî yenhâ, gloss:gördün mü o engelleyeni, source:96:9}, {ar:عَبْدًا إِذَا صَلَّىٰٓ, tr:abden izâ sallâ, gloss:namaz kıldığında bir kulu, source:96:10}. Biraz sonra soru, bu surenin ilk ayetindeki fiile döner: {ar:أَرَءَيْتَ إِن كَذَّبَ وَتَوَلَّىٰٓ, tr:eraeyte in kezzebe ve tevellâ, gloss:gördün mü, ya yalanladıysa ve yüz çevirdiyse, source:96:13}. Sahne gerçek görenin adıyla kapanır: {ar:أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ, tr:elem ya‘lem bi-enna'llâhe yerâ, gloss:bilmedi mi ki Allah görüyor, source:96:14}. Aynı surenin başında insanın taşkınlığı da bir bakışla başlar. Bu kez insan aynayı kendine tutmuştur: {ar:كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ, tr:kellâ inne'l-insâne le-yatğâ, gloss:hayır, insan gerçekten azar, source:96:6}, {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en raâhu'staġnâ, gloss:kendini kimseye muhtaç değil gördüğü için, source:96:7}. Şuarâ suresinde Allah Peygamber'e kendisine dayanmasını söyler ve namazdaki kulun asıl seyircisini adlandırır: {ar:ٱلَّذِى يَرَىٰكَ حِينَ تَقُومُ, tr:ellezî yerâke hîne tekûm, gloss:kalktığın zaman seni gören, source:26:218}, {ar:وَتَقَلُّبَكَ فِى ٱلسَّٰجِدِينَ, tr:ve tekallübeke fi's-sâcidîn, gloss:secde edenler arasında dönüp duruşunu da, source:26:219}. Nisâ suresinde Allah münafıkları anlatırken aynı fiili namazın içine yerleştirir: {ar:وَإِذَا قَامُوٓا۟ إِلَى ٱلصَّلَوٰةِ قَامُوا۟ كُسَالَىٰ يُرَآءُونَ ٱلنَّاسَ, tr:ve izâ kâmû ile's-salâti kâmû küsâlâ yurâûne'n-nâs, gloss:namaza kalktıklarında üşenerek kalkarlar, insanlara gösteriş yaparlar, source:4:142}. Aynı surede gösteriş verme işine de geçer. Hemen önceki ayette cimrileri anlattıktan sonra, malını {ar:وَٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ رِئَآءَ ٱلنَّاسِ, tr:ve'llezîne yünfikûne emvâlehum riâe'n-nâs, gloss:mallarını insanlara gösteriş için harcayanlar, source:4:38} diye anar. Karşı resim İnsan suresindedir. Allah iyileri anlatırken onların, doyurdukları kişilere şöyle dediklerini aktarır: {ar:إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءًۭ وَلَا شُكُورًا, tr:innemâ nut‘imukum li-vechi'llâh, lâ nurîdu minkum cezâen ve lâ şükûrâ, gloss:sizi yalnızca Allah'ın yüzü için doyuruyoruz, sizden ne karşılık ne teşekkür istiyoruz, source:76:9}. Burada yemek verilir, ama bakış insanların yüzünden çevrilmiştir. Leyl suresi verenin içini aynı biçimde çizer: {ar:وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ, tr:ve mâ li-ehadin indehû min ni‘metin tüczâ, gloss:onun yanında kimsenin karşılığı ödenecek bir iyiliği yoktur, source:92:19}, {ar:إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ, tr:ille'btiġâe vechi rabbihi'l-a‘lâ, gloss:yalnızca yüce Rabbinin yüzünü dileyerek, source:92:20}.

Kaynaklar: 107:1 أَرَءَيْتَ ر ء ي B013; 107:1 أَرَءَيْتَ ر ء ي B001; 107:6 يُرَآءُونَ ر ء ي B005; 107:6 يُرَآءُونَ ر ء ي B004; 107:6 يُرَآءُونَ ر ء ي B006; 107:6 يُرَآءُونَ ر ء ي B012

## Yalan söyleyen kumaş ve yarıda kalan koşu

Birinci ayetin fiili {ar:يُكَذِّبُ, tr:yükezzibu, gloss:yalanlar, source:107:1}, doğruluğun karşıtı olan bir kökten gelir: {ar:الكذب خلاف الصدق, tr:el-kezibu hılâfu's-sıdk, gloss:yalan, doğruluğun karşıtıdır, source:"ك ذ ب,B001"}. Bu yalanın yalnız sözle sınırlı olmadığı da belirtilir: {ar:يقال في المقال والفعال, tr:yukâlu fi'l-makâli ve'l-fi‘âl, gloss:hem söz hem fiil için söylenir, source:"ك ذ ب,B001"}. Kök bunu bir eşyayla gösterir: {ar:الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله, tr:el-kezzâbetu sevbun yunkaşu bi-levni sıbġin ke-ennehû muvaşşâ, ve zâlike li-ennehû yekzibu bi-hâlih, gloss:"kezzâbe", boyayla desen basılan ve işlemeliymiş gibi görünen kumaştır; böyle denir çünkü hâliyle yalan söyler, source:"ك ذ ب,B009"}. Kumaşın işleyişi şöyledir: Desen ipliğin içine dokunmamış, yüzeye boyanmıştır. Göz orada ilmek okur, ama ilmek yoktur. Kumaş bir şey söylemez; yalanı kendi hâliyle söyler.

Aynı kök bir de yarıda kalan hareketleri adlandırır. Bunlar kalıplaşmış deyimlerdir ve bir başlangıcın verdiği sözü devamın tutmamasını anlatır. Hücum eden biri için {ar:حمل فلان ثم كذب أي لم يصدق في الحملة, tr:hamele fulânun summe kezebe, ey lem yasduk fi'l-hamle, gloss:filan saldırdı sonra "kezebe", yani hücumunda sadık kalmadı, source:"ك ذ ب,B004"} denir. Dişi deve için {ar:كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم, tr:kezebe lebenu'n-nâka izâ zunne en yedûme müdde fe-lem yedum, gloss:bir süre sürmesi beklenen deve sütü sürmeyince "sütü yalan söyledi" denir, source:"ك ذ ب,B006"} denir. Yabani hayvan için {ar:كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه, tr:kezebe'l-vahşiyyu izâ cerâ şavtan summe vekafe li-yanzura mâ verâeh, gloss:yabani hayvan bir koşu koşup ardına bakmak için durduğunda "kezebe" denir, source:"ك ذ ب,B007"} denir. Kökün karşı yüzü de aynı deyimlerdedir: {ar:حمل فلان على فلان فما كذب حتى طعن أو ضرب أي ما وقف, tr:hamele fulânun alâ fulânin fe-mâ kezebe hattâ ta‘ane ev darabe, ey mâ vekaf, gloss:filan filana saldırdı ve mızrağı saplayana ya da vurana kadar durmadı, source:"ك ذ ب,B004"}; {ar:ما كذب فلان أن فعل كذا أي ما لبث, tr:mâ kezebe fulânun en fe‘ale kezâ, ey mâ lebis, gloss:filan şunu yapmakta gecikmedi, source:"ك ذ ب,B005"}. Surenin açılışındaki öteki kök, aynı hayvanın doğru söyleyen hâlini verir: {ar:أرأت الناقة إذا أظهرت الحمل حتى يرى صدق حملها, tr:er'eti'n-nâka izâ azhareti'l-hamle hattâ yurâ sıdku hamlihâ, gloss:dişi deve gebeliğini belli ettiğinde, gebeliğinin doğruluğu görülsün diye "er'et" denir, source:"ر ء ي,B010"}. Böylece birinci ayetin iki fiilinde birer dişi deve vardır. Birinin sütü yalan söyler, ötekinin karnı doğruyu gösterir.

Ayetin söylediği "dini yalanlayan"dır. Bu imge o anlamın yanında şunu duyurur: yalanlama yalnızca ağızdan çıkan bir cümle değildir. Yüzeyi içini, başlangıcı devamını tutmayan bir hayatın biçimidir. Sure bu adamla tartışmaz. Kumaştaki boya gibi, sütü kesilen deve gibi ortaya kendi hâliyle çıkan işlerini gösterir. İnkâr edilen şeyin kökü de bu boyanın tam karşılığını taşır: {ar:دينت الحالف أي نويته فيما حلف, tr:dayyentü'l-hâlif, ey neveytühû fîmâ halef, gloss:yemin edeni niyetine bıraktım, yani yemininde onu niyetine göre tuttum, source:"د ي ن,B007"}; {ar:دينت الرجل تديينا إذا وكلته إلى دينه, tr:dayyentü'r-racule tedyînen izâ vekeltehû ilâ dînih, gloss:adamı kendi dinine havale ettiğinde, source:"د ي ن,B007"}. Bu sözler bir insanın yüzeyine göre değil, içindeki niyete göre tutulmasını anlatır. Yalanlanan din, boyanın altına bakan hükümdür.

İkinci ayetin başındaki {ar:فَ, tr:fe, gloss:işte, demek ki, source:107:2} edatı itip kakmayı yalanlamanın sonucu ve görünür belgesi yapar. Dördüncü ve beşinci ayetlerde boyanın üzerine basıldığı desen ortaya çıkar. Kökün bir kolu namazı görünen parçalarıyla sayar: {ar:الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح, tr:es-salâtu mine'l-mahlûkîn el-kıyâmu ve'r-rükû‘u ve's-sücûdu ve'd-du‘âu ve't-tesbîh, gloss:yaratılmışlardan namaz; kıyam, rükû, secde, dua ve tesbihtir, source:"ص ل و,B003"}. Bu parçalar yerindedir. Ama ayet, namazda bir şeyi unutmaktan söz etmez. O durum ayrıca adlandırılır: {ar:سها الرجل في صلاته إذا غفل عن شيء منها, tr:sehe'r-racülu fî salâtihî izâ ġafele an şey'in minhâ, gloss:adam namazında bir parçasından gafil kaldığında "namazında yanıldı" denir, source:"س ه و,B001"}. Ayet ise şöyle der: {ar:عَن صَلَاتِهِمْ سَاهُونَ, tr:an salâtihim sâhûn, gloss:namazlarından gafildirler, source:107:5}. "An" edatı içeride değil, uzakta olmayı bildirir. Mü'minûn suresi içerideki hâli aynı kalıpla verir: {ar:ٱلَّذِينَ هُمْ فِى صَلَاتِهِمْ خَٰشِعُونَ, tr:ellezîne hum fî salâtihim hâşi‘ûn, gloss:onlar ki namazlarında saygıyla eğilmişlerdir, source:23:2}. Bu surenin adamları namazı kılarken namazın dışındadır, tıpkı ipliğe girmemiş boya gibi. Altıncı ayet yüzeyin adını koyar: {ar:الرواء حسن المنظر, tr:er-ruvâu husnü'l-manzar, gloss:"ruvâ", güzel görünüştür, source:"ر ء ي,B006"}. Aynı ayet koşunun biçimini de verir: göz çekilince namaz bırakılır {source:"ر ء ي,B005"}. Yabani hayvanın durup ardına bakması gibi bu namaz da yolda durup seyirciye bakar. Yetimin kökü de bu yavaşlayan adımı bilir: {ar:في سيره يتم أي إبطاء, tr:fî seyrihî yutmun, ey ibtâ’, gloss:yürüyüşünde ağırlık, yani gecikme var, source:"ي ت م,B004"}.

Kuran yüzeyle altı arasındaki bu ayrılığı birkaç sahnede kurar. Bakara suresinde Allah mü'minlere sadakalarını başa kakarak ve incitmeyle boşa çıkarmamalarını söyler. Gösteriş için harcayanı bir kayaya benzetir: {ar:فَمَثَلُهُۥ كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا, tr:fe-meseluhû ke-meseli safvânin aleyhi turâbun fe-esâbehû vâbilun fe-terakehû saldâ, gloss:onun durumu, üstünde biraz toprak bulunan düz bir kayaya benzer; sağanak vurunca onu çıplak bırakır, source:2:264}. Toprak, tohumun tutacağı bir yer gibi görünür. Yağmur gelince altındaki taş ortaya çıkar. Münâfikûn suresinde Allah Peygamber'e münafıkların görünüşünü anlatır: {ar:وَإِذَا رَأَيْتَهُمْ تُعْجِبُكَ أَجْسَامُهُمْ, tr:ve izâ raeytehum tu‘cibuke ecsâmuhum, gloss:onları gördüğünde gövdeleri hoşuna gider, source:63:4}. Hemen ardından bu gövdeleri {ar:كَأَنَّهُمْ خُشُبٌۭ مُّسَنَّدَةٌۭ, tr:ke-ennehum huşubun musennede, gloss:sanki dayatılmış kütüklerdir, source:63:4} diye niteler. Kütükler ayakta durur, ama kendi içlerinden değil, arkalarındaki desteğe yaslanarak. Bakara suresi iyiliği görünen bir duruştan ayırarak başlar: {ar:لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ, tr:leyse'l-birra en tuvellû vucûhekum kıbele'l-meşrıkı ve'l-maġrib, gloss:iyilik yüzlerinizi doğuya ve batıya çevirmeniz değildir, source:2:177}. Sonra malı yetimlere ve yoksullara vermeyi, namazı ve zekâtı sayar ve bunları yapanları kökün karşıtıyla adlandırır: {ar:أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟, tr:ülâike'llezîne sadakû, gloss:işte doğru olanlar onlardır, source:2:177}. Yarıda kalan verme Necm suresinde bir "gördün mü" ile gösterilir. Allah Peygamber'e sorar: {ar:أَفَرَءَيْتَ ٱلَّذِى تَوَلَّىٰ, tr:e-fe-raeyte'llezî tevellâ, gloss:yüz çevireni gördün mü, source:53:33}, {ar:وَأَعْطَىٰ قَلِيلًۭا وَأَكْدَىٰٓ, tr:ve a‘tâ kalîlen ve ekdâ, gloss:azıcık verdi, sonra kesti, source:53:34}. Yolunu tutan namaz ise Meâric suresinde iki kez adlandırılır: {ar:ٱلَّذِينَ هُمْ عَلَىٰ صَلَاتِهِمْ دَآئِمُونَ, tr:ellezîne hum alâ salâtihim dâimûn, gloss:onlar ki namazlarını sürdürürler, source:70:23}, {ar:وَٱلَّذِينَ هُمْ عَلَىٰ صَلَاتِهِمْ يُحَافِظُونَ, tr:ve'llezîne hum alâ salâtihim yuhâfizûn, gloss:onlar ki namazlarını korurlar, source:70:34}. Beyyine suresi boyasız kumaşı tarif eder: namaz ve zekât, dini yalnızca Allah'a ayırmanın içinde emredilmiştir: {ar:مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:muhlisîne lehu'd-dîn, gloss:dini yalnız O'na özgü kılarak, source:98:5}.

Kaynaklar: 107:1 يُكَذِّبُ ك ذ ب B001; 107:1 يُكَذِّبُ ك ذ ب B009; 107:1 يُكَذِّبُ ك ذ ب B004; 107:1 يُكَذِّبُ ك ذ ب B005; 107:1 يُكَذِّبُ ك ذ ب B006; 107:1 يُكَذِّبُ ك ذ ب B007; 107:1 أَرَءَيْتَ ر ء ي B010; 107:1 بِٱلدِّينِ د ي ن B007; 107:2 ٱلْيَتِيمَ ي ت م B004; 107:5 صَلَاتِهِمْ ص ل و B003; 107:5 سَاهُونَ س ه و B001; 107:6 يُرَآءُونَ ر ء ي B006; 107:6 يُرَآءُونَ ر ء ي B005

## Borç, hesap ve boyun eğiş

Birinci ayetin nesnesi bir alacak verecek ilişkisi kurar: {ar:بِٱلدِّينِ, tr:bi'd-dîn, gloss:dini, hesap ve karşılık gününü, source:107:1}. Kök hesabın görülüp ödenmesini adlandırır: {ar:يوم الدين أي يوم الحكم والحساب والجزاء, tr:yevmü'd-dîn, ey yevmü'l-hukmi ve'l-hisâbi ve'l-cezâ’, gloss:din günü; hüküm, hesap ve karşılık günü, source:"د ي ن,B002"}; {ar:الدين الجزاء والمكافأة, tr:ed-dînu'l-cezâu ve'l-mükâfee, gloss:din karşılık ve ödemedir, source:"د ي ن,B002"}. İnsanlar arasındaki borcu da adlandırır: {ar:داينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء, tr:dâyentü fülânen izâ âmeltehû deynen, immâ ahzen ve immâ i‘tâ’, gloss:biriyle borç alarak ya da vererek iş gördüğünde "dâyentü" dersin, source:"د ي ن,B003"}; {ar:دنت الرجل أقرضته, tr:dintü'r-racüle akradtüh, gloss:adama borç verdim, source:"د ي ن,B003"}. Bütün bunların altında bir boyun eğiş vardır: {ar:أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل, tr:aslun vâhidun ileyhi yerci‘u furû‘uhû küllühâ, ve huve cinsun mine'l-inkıyâdi ve'z-züll, gloss:bütün kollarının döndüğü tek bir asıl vardır; o da bir tür boyun eğiş ve alçalıştır, source:"د ي ن,B001"}; {ar:فالدين الطاعة, tr:fe'd-dînu't-tâ‘a, gloss:din itaattir, source:"د ي ن,B001"}. Fiil ise bu hesabı getireni yalancı saymaktır: {ar:كذبت فلانا نسبته إلى الكذب, tr:kezzebtü fülânen nesebtühû ile'l-kezib, gloss:filanı yalanladım, yani onu yalana nispet ettim, source:"ك ذ ب,B002"}. Yalanlayanın kendi fiilinin içinde, kalıplaşmış bir deyim olarak, tam tersi bir söz de durur: {ar:كذب عليكم الحج أي وجب, tr:kezebe aleykumu'l-hacc, ey vecebe, gloss:hac size borç oldu, yani üzerinize vacip oldu, source:"ك ذ ب,B003"}; {ar:كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك, tr:kezebe aleyke kezâ, bi-ma‘ne'l-iġrâ’, ey aleyke bih, ev kad vecebe aleyk, gloss:"kezebe aleyke" şunu yapmaya teşvik anlamındadır; yani ona sarıl ya da o sana vacip oldu, source:"ك ذ ب,B003"}. Borcu yalanlamak için kullanılan fiil, kendi içinde "bu senin üzerine borçtur" sözünü saklar.

Surenin son kelimesi de aynı hesabın içine girer: {ar:الماعون في الجاهلية كل منفعة وعطية وفي الإسلام الطاعة والزكاة, tr:el-mâ‘ûnu fi'l-câhiliyye küllü menfe‘atin ve atıyye, ve fi'l-islâmi't-tâ‘atu ve'z-zekât, gloss:mâûn cahiliyede her türlü yarar ve bağıştı, İslâm'da itaat ve zekâttır, source:"م ع ن,B005"}; {ar:الماعون الطاعة, tr:el-mâ‘ûnu't-tâ‘a, gloss:mâûn itaattir, source:"م ع ن,B005"}; {ar:الماعون يفسر بالزكاة والصدقة, tr:el-mâ‘ûnu yufesseru bi'z-zekâti ve's-sadaka, gloss:mâûn zekât ve sadaka diye açıklanır, source:"م ع ن,B005"}. Bir hakkın karşısında yapılabilecek iki şey aynı fiilde durur: {ar:أمعن بحقي ذهب به, tr:em‘ane bi-hakkî, zehebe bih, gloss:hakkımı alıp götürdü, source:"م ع ن,B004"}; {ar:أمعن لي بحقي إذا أقر به وانقاد, tr:em‘ane lî bi-hakkî izâ akarra bihî ve'nkâd, gloss:hakkımı tanıyıp boyun eğdiğinde "em‘ane lî bi-hakkî" denir, source:"م ع ن,B004"}. Bu son tanımdaki boyun eğiş, dinin kökünü tanımlayan boyun eğişle aynı kelimedir. Böylece surenin ilk nesnesi ile son nesnesi itaatte buluşur. Esirgemek de vermenin tersi olarak bu hesaba yazılır: {ar:ضد العطية, tr:ziddu'l-atıyye, gloss:bağışın karşıtı, source:"م ن ع,B001"}.

Sahne iki taraf arasında tutulan bir hesap defteridir. Borç alınır ve verilir, bir gün hesap kapatılıp ödenir. Birinci ayet, defteri getireni yalancı sayan adamı gösterir. İkinci ve üçüncü ayetlerde defterin satırları açılır: Yetimin hakkı kapıdan itilir, yoksulun payı hiç anılmaz. Yedinci ayetteki küçük borç da ödenmez. Hesabı inkâr eden, sonunda en ucuz borcunu da inkâr eder. Kuran sure boyunca bu hesabı açık tutar. İnfitâr suresinde Allah insana seslenir: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ مَا غَرَّكَ بِرَبِّكَ ٱلْكَرِيمِ, tr:yâ eyyühe'l-insânu mâ ġarraka bi-rabbike'l-kerîm, gloss:ey insan, seni cömert Rabbine karşı ne aldattı, source:82:6}. Birkaç ayet sonra bu surenin ifadesi aynen geçer: {ar:كَلَّا بَلْ تُكَذِّبُونَ بِٱلدِّينِ, tr:kellâ bel tükezzibûne bi'd-dîn, gloss:hayır, siz dini yalanlıyorsunuz, source:82:9}. Hesabın sahibi Fâtiha'da adlandırılır: {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:mâliki yevmi'd-dîn, gloss:din gününün sahibi, source:1:4}. Meâric suresi bu sureyi madde madde tersine çevirir. İnsan hırslı yaratılmıştır {ar:إِنَّ ٱلْإِنسَٰنَ خُلِقَ هَلُوعًا, tr:inne'l-insâne hulika helû‘â, gloss:insan hırslı yaratıldı, source:70:19}. Hayra dokunulunca {ar:وَإِذَا مَسَّهُ ٱلْخَيْرُ مَنُوعًا, tr:ve izâ messehu'l-hayru menû‘â, gloss:ona bir hayır dokununca esirgeyendir, source:70:21}. Ardından istisna gelir: {ar:إِلَّا ٱلْمُصَلِّينَ, tr:ille'l-musallîn, gloss:namaz kılanlar hariç, source:70:22}. Bunlar namazlarını sürdürenlerdir {source:70:23}. Mallarında bir hak bulunur: {ar:وَٱلَّذِينَ فِىٓ أَمْوَٰلِهِمْ حَقٌّۭ مَّعْلُومٌۭ, tr:ve'llezîne fî emvâlihim hakkun ma‘lûm, gloss:mallarında belirli bir hak bulunanlar, source:70:24}, {ar:لِّلسَّآئِلِ وَٱلْمَحْرُومِ, tr:li's-sâili ve'l-mahrûm, gloss:isteyen ve yoksun kalan için, source:70:25}. Ve {ar:وَٱلَّذِينَ يُصَدِّقُونَ بِيَوْمِ ٱلدِّينِ, tr:ve'llezîne yusaddikûne bi-yevmi'd-dîn, gloss:din gününü doğrulayanlar, source:70:26}. Esirgemek, namaz kılanlar, sürdürülen namaz, maldaki hak ve dini doğrulamak: Bu surede dağılan her parça orada yerine oturur. Fussilet suresinde Peygamber'e şunu söylemesi emredilir: "Ben de sizin gibi bir insanım." Aynı ayet şöyle biter: {ar:وَوَيْلٌۭ لِّلْمُشْرِكِينَ, tr:ve veylun li'l-müşrikîn, gloss:vay hâline ortak koşanların, source:41:6}. Ortak koşanlar {ar:ٱلَّذِينَ لَا يُؤْتُونَ ٱلزَّكَوٰةَ وَهُم بِٱلْءَاخِرَةِ هُمْ كَٰفِرُونَ, tr:ellezîne lâ yü'tûne'z-zekâte ve hum bi'l-âhireti hum kâfirûn, gloss:zekâtı vermeyenler ve ahireti inkâr edenlerdir, source:41:7}. İsrâ suresi yoksulun payını hak diye anar: {ar:وَءَاتِ ذَا ٱلْقُرْبَىٰ حَقَّهُۥ وَٱلْمِسْكِينَ وَٱبْنَ ٱلسَّبِيلِ, tr:ve âti ze'l-kurbâ hakkahû ve'l-miskîne ve'bne's-sebîl, gloss:yakına hakkını ver, yoksula ve yolda kalmışa da, source:17:26}. Zâriyât suresi de aynısını yapar: {ar:وَفِىٓ أَمْوَٰلِهِمْ حَقٌّۭ لِّلسَّآئِلِ وَٱلْمَحْرُومِ, tr:ve fî emvâlihim hakkun li's-sâili ve'l-mahrûm, gloss:mallarında isteyen ve yoksun kalan için bir hak vardı, source:51:19}.

Kaynaklar: 107:1 بِٱلدِّينِ د ي ن B002; 107:1 بِٱلدِّينِ د ي ن B003; 107:1 بِٱلدِّينِ د ي ن B001; 107:1 يُكَذِّبُ ك ذ ب B002; 107:1 يُكَذِّبُ ك ذ ب B003; 107:7 ٱلْمَاعُونَ م ع ن B005; 107:7 ٱلْمَاعُونَ م ع ن B004; 107:7 وَيَمْنَعُونَ م ن ع B001

## Buluşmalar

Görme imgesi ile gözden kaçma imgesi tek bir cümlede buluşur: Suhâ yıldızı {ar:خفي جدا فيسهى عن رؤيته, tr:hafiyyun ciddâ fe-yushâ an ru'yetih, gloss:pek gizlidir, onu görmekten gaflet edilir, source:"س ه و,B005"}. Surenin beşinci ayetindeki kökle altıncı ayetindeki kök bu cümlede yan yana durur. Gözden kaçırmak ile göze görünmek tek bir görme alanının iki ucudur. Adamlar sönük olanı, yani yetimi, yoksulu ve kendi namazlarındaki kalbi atlar. Kendilerinin ise atlanmamasını isterler. Alak suresindeki sahne bu buluşmaya namazı ve yarıda kalan yolu ekler. Bir "gördün mü" ile açılır, namaz kılan bir kulu engelleyeni gösterir, onun yalanlayıp yüz çevirdiğini söyler ve görenin Allah olduğunu hatırlatarak kapanır {source:96:9} {source:96:13} {source:96:14}. Burada bakış imgesi ile yalanın yüzey ve yol imgesi birbirinin içindedir. İnsanların gözü için kılınan namaz, gözü hiç ayrılmayan birinin önünde kılınmaktadır.

İtiş ile ateş Tûr suresinde tek harekette birleşir. Yetimi iten, ateşe itilir {source:52:13}, ve ona yalanladığı ateşin bu olduğu söylenir {source:52:14}. Böylece birinci ve ikinci ayetin iki fiili, yalanlamak ve itmek, dördüncü ayetin ateşini taşıyan kökle bir araya gelir. Hâkka suresinde ateş fiili ile teşvik etmeme aynı kişinin hesabında yan yana yazılır {source:69:31} {source:69:34}. Bu kez evin ocağı ile zayıfın üstündeki eller birbirine bağlanır. Teşvik edilmeyen yemek, pişirilmeyen ocağın karşılığında ateşe katlanmaya dönüşür.

Bütün imgeleri tek bir ağızdan dile getiren sahne Müddessir suresindedir. Cennet halkı suçlulara sorar: {ar:مَا سَلَكَكُمْ فِى سَقَرَ, tr:mâ selekekum fî sakar, gloss:sizi Sakar'a ne soktu, source:74:42}. Cevap bu surenin kelime dizisini ateşin içinden verir: {ar:قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ, tr:kâlû lem neku mine'l-musallîn, gloss:dediler ki: namaz kılanlardan değildik, source:74:43}, {ar:وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ, tr:ve lem neku nut‘imu'l-miskîn, gloss:yoksulu doyurmazdık, source:74:44}, {ar:وَكُنَّا نَخُوضُ مَعَ ٱلْخَآئِضِينَ, tr:ve künnâ nehûdu ma‘a'l-hâidîn, gloss:dalıp gidenlerle birlikte biz de dalardık, source:74:45}, {ar:وَكُنَّا نُكَذِّبُ بِيَوْمِ ٱلدِّينِ, tr:ve künnâ nükezzibu bi-yevmi'd-dîn, gloss:din gününü yalanlardık, source:74:46}. Namaz, doyurmak, gaflete dalmak ve hesabı yalanlamak burada tek bir itirafta toplanır ve bu itiraf ateşin içinden yapılır. Bu suredeki boş namaz, kapalı kap, gözden kaçırılan yoksul ve inkâr edilen hesap, orada bir hikâyenin sırası olarak geri döner.

Ev, su ve borç imgeleri tek bir kelimede, mâûnda buluşur. Aynı ad tencereyi ve kovayı {source:"م ع ن,B005"}, vadiden akan suyu {source:"م ع ن,B001"} ve itaatle zekâtı {source:"م ع ن,B005"} taşır. Rafta duran kap, yataktan akan su ve ödenmesi gereken pay tek bir şeyin üç görünüşüdür. Barındırma fiili de bu buluşmayı Kuran'da iki kez kurar. Yetim için {source:93:6}, Meryem oğlu ve annesi için kullanılır; ikincisinde barınak yerleşme ile akan suyun bir arada olduğu yerdir {source:23:50}. İtişin kökü de evle ellerin buluştuğu yerdir. Aynı harfler bir adamın küçük çocuklarını {source:"د ع ع,B009"}, sarsılarak doldurulan tabağı {source:"د ع ع,B002"} ve kapıdan kovan itişi {source:"د ع ع,B001"} taşır. Esirgemenin kökü de eli sıkı adamı {source:"م ن ع,B001"} ve babasız çocuğun yitirdiği koruyucu halkayı {source:"م ن ع,B003"} birlikte taşır.

Borç imgesi ile dışa dönük namaz imgesi Meâric suresinde birlikte sahnelenir. Esirgeyen insan, namazını sürdürenler, malındaki bilinen hak ve din gününü doğrulamak aynı dizide yer alır {source:70:21} {source:70:24} {source:70:26}. Tevbe suresindeki döngüde de pay, dua ve huzur birbirine bağlanır {source:9:103}. Bu sure, aynı halkaların çözülmüş hâlidir.

Surenin hareketi bu buluşmalarla taşınır. Sure bir bakış emriyle ve yalanlanan bir hesapla başlar. Bakışı önce bir evin kapısına götürür: Yetimi iten el, yoksulun yemeği için açılmayan ağız. Sonra namaz yerine geçer ve orada ateşi de taşıyan bir ada beddua düşer. Ardından seyircinin gözüne, en sonunda yeniden evin rafındaki küçük kaplara döner. Bir uçta "gördün mü" ile gösteriş vardır, yani bakış ve bakılmak. Öbür uçta din ile mâûn vardır, yani hesap ve küçük borç. İki uç da itaatte buluşur. Ortadaki ad, namaz kılanlar, hem halkayı kuracak ibadeti hem de halka kopunca gelen ateşi kökünde taşır.

