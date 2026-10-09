Focus: 99:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/99_6/D.r13/context.md =====
# 99:6 — focus

يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ

Anchor translation (canonical reading, reference only):

O gün insanlar, yaptıkları kendilerine gösterilsin diye bölük bölük çıkarlar.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | يَوْمَئِذٍ | يَوْمَئِذ |  | T |
| 2 | يَصْدُرُ | يَصْدُرُ | ص د ر | V |
| 3 | ٱلنَّاسُ | نَّاس | ن و س | DET;N |
| 4 | أَشْتَاتًا | أَشْتَات | ش ت ت | N |
| 5 | لِّيُرَوْا۟ | أَرَيْ | ر ء ي | PRP;V;PRON |
| 6 | أَعْمَٰلَهُمْ | عَمَل | ع م ل | N;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 99 — full text (context; no pericope)

- 99:1 إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا
- 99:2 وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا
- 99:3 وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا
- 99:4 يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا
- 99:5 بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا
- 99:6 ◀ focus يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ
- 99:7 فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
- 99:8 وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ


===== _commentary/v16/work/99_6/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ص د ر (root_000849) — identity root of يَصْدُرُ (w2)

- **B001** göğüs bölgesi — göğüs · göğüsler · göğsün üstte çıkıntılı kesimi · göğsü örten kısa giysi · devenin göğsündeki damga · yükü sabitleyen göğüs bağı · göğsünden rahatsız olan kimse · birinin göğsüne bir şeyle vurmak · göğsü ağrımak · güçlü göğüslü aslan
  الصدر للإنسان والجمع صدور (maqayis)؛ الصدر الجارحة (mufradat)؛ الصدرة من الإنسان ما أشرف من أعلى صدره (ayn;sihah;tahdhib)؛ صدر فلان إذا وجع صدره (ayn;tahdhib)؛ المصدور الذي يشتكي صدره (maqayis;sihah)؛ الصدار ثوب يغطي الصدر (maqayis;ayn;tahdhib;mufradat)؛ الصدار سمة على صدر البعير (maqayis;sihah;mufradat)؛ المصدر الأسد (maqayis;ayn;sihah)
- **B002** ön, üst ya da başlangıç bölümü — ön, üst ya da başlangıç bölümü · mızrağın üst bölümü · işin başlangıcı · toplantının ön kısmı; kitabın veya sözün başlangıcı · okun ortasından ucuna uzanan ön bölümü · ön gövdesi kalın ok · göğsüyle öne çıkıp yarışı geçmek · kitaba giriş bölümü koymak · toplantının başköşesine oturmak
  الصدر أعلى مقدم كل شيء (ayn;tahdhib)؛ صدر القناة أعلاها (ayn;sihah;tahdhib;mufradat)؛ صدر الأمر أوله (ayn;tahdhib)؛ صدر كل شيء أوله (sihah)؛ صدر المجلس والكتاب والكلام (mufradat)؛ صدر السهم ما فوق نصفه إلى المراش (ayn;tahdhib)؛ صدر الفرس إذا جاء قد سبق بصدره (sihah;tahdhib;mufradat)
- **B003** geldiği yerden ayrılıp dönme — bir yerden ya da durumdan ayrılış · su başından, geldikten sonra ayrılmak · geri döndürmek · su başından dönüşü sağlayan yol
  صدر عن الماء وصدر عن البلاد (maqayis;sihah)؛ الصدر الانصراف عن الورد وعن كل أمر (ayn;tahdhib)؛ صدرت الإبل عن الماء (mufradat)؛ أصدرته فصدر أي رجعته فرجع (sihah)؛ طريق صادر يصدر بأهله عن الماء (ayn;sihah;tahdhib)
- **B004** eylem türetme temeli; çıkış yeri veya zamanı — eylemlerin türediği temel sözcük biçimi · çıkış yeri ya da zamanı
  المصدر أصل الكلمة الذي تصدر عنه الأفعال (ayn;tahdhib)؛ مصادر الأفعال (sihah)؛ المصدر في الحقيقة صدر عن الماء ولموضع المصدر ولزمانه (mufradat)
- **B005** para ödeme ve güvence yükümlülüğü koyma — birini belli bir parayı ödemek ve güvence altına almakla yükümlü kılmak · kendisine para ödeme ve güvence yükümlülüğü konmak
  صادره على كذا (sihah)؛ صودر فلان العامل على مال يؤديه أي فورق على مال ضمنه (tahdhib)
- **B006** bir şeyin bölümü ya da kümesi — bir şeyin bölümü ya da kümesi
  الصدر الطائفة من الشيء (sihah)

## ء ن س (root_000059) — identity root of ٱلنَّاسُ (w3)

- **B001** insan türü ve bu türden bir kişi — insanlar; insan topluluğu · insan; insan türü · insan topluluğunun bir üyesi; insana veya insanlara ait · insanlar; insan toplulukları · insanlar; halk · evde hiç kimse yok · belirli bir ağızda insan ve onun çoğulu
  الإنس خلاف الجن وسموا لظهورهم (maqayis;mufradat)؛ الإنس البشر والواحد إنسي والجمع أناسي (sihah)؛ الإنس جماعة الناس والأناسي جماع (tahdhib)
- **B002** görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma — bir şeyi görmek ve fark etmek · sesi işitmek · onda olgunluk belirtisi görmek ve bunu anlamak · ürken yabani hayvanın birini sezip çevreye bakınması · çevreye bakıp birinin olup olmadığını araştırmak
  آنست الشيء إذا رأيته وآنسته إذا سمعته (maqayis)؛ آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته (sihah)؛ آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه (tahdhib)؛ فإن آنستم منهم رشدا أي أبصرتم وآنست نارا (mufradat)
- **B003** yabancılık duymadan yakınlık ve rahatlık hissetme — yakınlık ve rahatlık; yabancılık duymama · birine alışıp onun yanında sevinmek · biriyle yakınlık kurmak ve onsuz kendini yalnız hissetmek · yakın arkadaş; rahatlık veren kişi veya şey · yakınlıktan ve söyleşiden hoşlanan genç kadın · insana alışık, saldırgan olmayan köpek · gece yolcusuna veya konaklayana güven veren ateş · sahibine güven veren bütün silahlar; zırh, miğfer, koruyucu örtü ve kalkan gibi savunma donanımları
  الأنس أنس الإنسان بالشيء إذا لم يستوحش منه (maqayis)؛ الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به (sihah)؛ أنست بفلان أي فرحت به والأنس والاستئناس هو التأنس وكلب أنوس نقيض العقور (tahdhib)؛ الأنس خلاف النفور ولكل ما يؤنس به (mufradat)
- **B004** insana dönük yan — bir şeyin insana bakan veya en yakın olan yanı · yayın okçuya bakan yüzü · hayvanın biniciye yakın olan yanı
  الإنسي الأيسر من كل شيء وقيل الأيمن وما أقبل منهما على الإنسان فهو إنسي وإنسي القوس ما أقبل عليك منها (sihah)؛ الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب ومن الإنسان الجانب الذي يلي الرجل الأخرى (tahdhib)؛ إنسي الدابة للجانب الذي يلي الراكب وإنسي القوس للجانب الذي يقبل على الرامي (mufradat)
- **B005** göz bebeğinde görülen küçük yansıma — göz bebeğinde görülen küçük görüntü veya yansıma · göz bebeklerinde görülen küçük görüntüler · parmak ucu; eldeki parmak ucunu anlatan kullanım
  إنسان العين صبيها الذي في السواد (maqayis)؛ إنسان العين المثال الذي يرى في السواد أي سواد العين (sihah)؛ الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة (tahdhib)
- **B006** belirli sözlerde kişinin kendisi veya seçilmiş yakını — kendin; kendi durumun nasıl · onun seçkin yakını ve sırdaşı · yakınım, içten dostum ve görüşme arkadaşım
  كيف ابن إنسك إذا سأله عن نفسه (maqayis)؛ كيف ابن إنسك يعني نفسه وفلان ابن إنس فلان أي صفيه وخاصته وهذا خدني وإنسي وخلصي وجلسي (sihah)؛ كيف ترى ابن إنسك إذا خاطبت الرجل عن نفسه وفلان ابن أنس فلان أي صفيه وأنيسه (tahdhib)؛ قيل ابن إنسك للنفس (mufradat)
- **B007** girişten önce izin ve kabul arama — 
  حتى تستأنسوا معناه حتى تستأذنوا وإنما هو حتى تسلموا وتستأنسوا السلام عليكم أأدخل (tahdhib)؛ حتى تستأنسوا أي تجدوا إيناسا (mufradat)

## ش ت ت (root_000775) — identity root of أَشْتَاتًا (w4)

- **B001** dağılma ve dağıtma — dağılmak; dağılma · dağıtmak, dağınık hale getirmek · topluluğum işimi dağıttı · şu şey gönlümü dağıttı · yayılıp dağılmak · dağılıp yayılmak · ayrı kişiler veya dağınık parçalar halinde · dağınıklık ve ayrılık · dağılmış, dağınık · dağınık bir iş veya durum · çeşitli, birbirinden farklı · aynı soydan olmayan insanlar
  أصل يدل على تفرق وتزيل (maqayis)؛ الشت مصدر الشيء الشتيت وهو المتفرق (ayn)؛ شت يشت شتاتا وهو التفرق (jamhara)؛ أمر شت أي متفرق (sihah)؛ يصدر الناس أشتاتا أي متفرقين (tahdhib)؛ الشت تفريق الشعب (mufradat)
- **B002** güzel ve aralıklı diş dizisi [kalıp] — dişleri güzel, düzgün ve aralıklı ağız
  ثغر شتيت مفلج حسن (maqayis)؛ ثغر شتيت مفلج حسن (ayn)؛ ثغر شتيت أي مفلج (sihah)
- **B003** iki şey arasındaki büyük uzaklık ve uyuşmazlık — ne kadar uzak ve farklılar · ikisi birbirinden ne kadar uzak ve farklı · aralarında ne büyük uzaklık ve ayrılık var
  شتان ما هما (maqayis;ayn;sihah;tahdhib;mufradat)؛ شتان ما بينهما (maqayis;sihah;mufradat)؛ تباعد ما بينهما (tahdhib)؛ ارتفاع الالتئام بينهما (mufradat)

## ر ء ي (root_000531) — identity root of لِّيُرَوْا۟ (w5)

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

## ع م ل (root_001046) — identity root of أَعْمَٰلَهُمْ (w6)

- **B001** bilerek yapılan iş veya eylem — bilerek yapılan iş veya eylem · iş yapan kimse · kendisi için çalışmak veya işe koyulmak · iş veya uğraş · işte kullanılan sığırlar · iyi ve kötü davranışlar
  أصل واحد صحيح وهو عام في كل فعل يفعل (maqayis); عمل عملا فهو عامل (ayn;sihah;tahdhib); كل فعل يكون من الحيوان بقصد (mufradat); الأعمال الصالحة والسيئة (mufradat)
- **B002** işe koşmak veya kullanmak — onu çalıştırdı · onu kullandı veya çalıştırdı · ondan çalışmasını istedi · görüşünü, sözünü veya mızrağını kullandı · kerpici yapıda kullandı · zihnini işletip düşündü
  يستعمل غيره ويعمل رأيه أو كلامه أو رمحه؛ والبناء يستعمل اللبن (maqayis); أعمله غيره واستعمله بمعنى؛ واستعمله أيضا أي طلب إليه العمل (sihah); أعمل فلان ذهنه في كذا وكذا إذا دبره بفهمه (tahdhib)
- **B003** işe görevli kılma veya görev üstlenme — bağışları toplayan görevliler · bağış işi görevlisi · resmi bir işi üstlendi · birine iş görevi verme · bir kimseyi bir şehirde görevli kılmak
  العاملين عليها هم السعاة الذين يأخذون الصدقات (tahdhib); استعمل فلان إذا ولي عملا من أعمال السلطان (tahdhib); التعميل تولية العمل (sihah); العاملين عليها هم المتولون على الصدقة (mufradat)
- **B004** iş ücreti — iş karşılığı ücret veya pay · iş ücreti
  العمالة أجر ما عمل (maqayis); العمالة بالضم رزق العامل (sihah); العمالة رزق العامل (tahdhib); العملة والعمالة أجر العمل (tahdhib); العمالة أجرته (mufradat)
- **B005** karşılıklı işlem — karşılıklı işlem veya alışveriş ilişkisi · bir kimseyle alışveriş veya benzeri işlem yaptı
  المعاملة مصدر من قولك عاملته وأنا أعامله معاملة (maqayis); عاملت الرجل أعامله معاملة في المبايعة وغيرها (tahdhib)
- **B006** el işçileri — elleriyle çalışan işçi topluluğu
  العملة القوم يعملون بأيديهم ضروبا من العمل حفرا أو طيا أو نحوه (maqayis); العملة القوم الذين يعملون بأيديهم ضروبا من العمل في طين أو حفر أو غيره (tahdhib)
- **B007** zahmete girmek [kalıp] — kendini yorma · ihtiyacın için zahmete gireceğim · zahmet etme
  لا تتعمل في أمرك ذا كقولك لا تتعن (tahdhib); سوف أتعمل في حاجتك أي أتعنى (tahdhib); لا تعمل أي لا تتعن (tahdhib)
- **B008** işe yatkın ve dayanıklı — işe yatkın üstün dişi deve · işe nispet edilen dişi deve · işe yatkın adam · işe yatkın çalışkan adam · işe yatkın, güçlü ve üstün dişi deve
  اليعملة من الإبل اسم لها اشتق من العمل (maqayis); رجل عمل بكسر الميم أي مطبوع على العمل؛ ورجل عمول؛ اليعملة الناقة النجيبة المطبوعة على العمل (sihah); ناقة عملة بينة العمالة مثل اليعملة إذا كانت فارهة (tahdhib); اليعملة مشتقة من العمل (mufradat)
- **B009** mızrak ucunun alt bölümü — mızrağın sivri ucuna yakın ön gövde bölümü · mızrağın ucuna yakın gövde bölümü
  عامل الرمح وعاملته وهو ما دون الثعلب قليلا مما يلي السنان وهو صدره (maqayis); عامل الرمح ما يلي السنان وهو دون الثعلب (sihah); عامل الرمح صدره دون السنان ويجمع عوامل (tahdhib); عامل الرمح ما يلي السنان (mufradat)
- **B010** iş gören beden parçası [kalıp] — hayvanın ayakları · uzağı gören göz
  عوامل الدابة قوائمه واحدها عاملة (tahdhib); وترقبه بعاملة قذوف أي ترقبه بعين بعيدة النظر (tahdhib)
- **B011** işlek yol [kalıp] — işlek ve belirgin yol
  طريق معمل أي لحب مسلوك (sihah)
- **B012** yaya yolcular [kalıp] — yaya giden yolcular
  المسافرون إذا مشوا على أرجلهم يسمون بني العمل (tahdhib)

## ECHO ر و ي (root_000615) — for لِّيُرَوْا۟ (w5): withheld observed target; not identity

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

===== _commentary/v16/out/s099/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 99:6, and ## Buluşmalar) =====
## İçerinin çıkarılıp gösterilmesi

Sure boyunca içerdeki şeyler görünüre doğru hareket eder. Yerin ağırlıkları yer altındadır, hazineler göz önünden gömülüdür {source:"ث ق ل,B002"}. Çıkarmak, gizli olanı çekip almak, gömülü suyu yukarı çekmek gibidir {ar:الاستخراج كالاستنباط, tr:el-istihrâc kel-istinbât, gloss:çıkarıp almak, gizli suyu çekip çıkarmak gibidir, source:"خ ر ج,B002"}. Yerin haberleri işlerin içidir; anlatmak ise açığa çıkarmaktır {ar:الحدث الإبداء, tr:el-hadsu el-ibdâ’, gloss:açığa vurmak, source:"ح د ث,B006"}, hatta bir kılıcı cilalayıp donuk tabakasını gidermektir {ar:أحدث الرجل سيفه وحادثه إذا جلاه, tr:ahdeser-raculu seyfehû ve hâdesehû izâ celâh, gloss:kılıcını cilaladığında "ahdese" denir, source:"ح د ث,B007"}. Yer anlattıkça yüzeyi parlar ve altındaki görünür.

Altıncı ayette yön insana döner: {ar:لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:li-yurav a‘mâlehum, gloss:amelleri kendilerine gösterilsin diye, source:99:6}. Fiil edilgendir: insanlar görmeye getirilir. Görme kökünün ettirgen kullanımı birine bir şeyi gösterip gördürmektir, birine ayna tutup bakmasını sağlamaktır {ar:رأيت الرجل ترئية إذا أمسكت له المرآة لينظر فيها, tr:ra’eytur-racule ter’iyeten izâ emsektu lehul-mir’âte li-yenzura fîhâ, gloss:adama bakması için ayna tuttuğumda "ra’eytuhu" derim, source:"ر ء ي,B012"}. Amel sahibinin önüne ayna gibi tutulur. Aynı kök, insanların görmesi için iş yapmayı da adlandırır {ar:أن يفعل شيئا ليراه الناس, tr:en yef‘ale şey’en li-yerâhun-nâs, gloss:bir şeyi insanlar görsün diye yapmak, source:"ر ء ي,B005"}; Kur’an münafıkları {ar:يُرَآءُونَ ٱلنَّاسَ, tr:yurâûnen-nâs, gloss:insanlara gösteriş yaparlar, source:4:142} diye anlatır. Surede yön tersine döner: herkes başkasına değil, kendi amelini görmeye getirilir. Yedinci ve sekizinci ayetin {ar:يَرَهُۥ, tr:yerahû, gloss:onu görür, source:99:8} fiili gözle ya da iç görüyle görmektir {ar:نظر وإبصار بعين أو بصيرة, tr:nazarun ve ibsârun bi-aynin ev basîra, gloss:gözle ya da basiretle bakış ve görüş, source:"ر ء ي,B001"}.

Sekizinci ayetin kötülük kelimesi de bu harekete katılır: aynı kök bir şeyi ortaya çıkarıp sergilemek anlamını taşır {ar:أشررت الشيء إذا أبرزته وأظهرته, tr:eşrartuş-şey’e izâ ebreztuhû ve azhartuh, gloss:bir şeyi ortaya çıkarıp gösterdiğimde "eşrartu" derim, source:"ش ر ر,B008"}, bir şeyi kurusun diye güneşe yaymak anlamını da {ar:الشر بسطك الشيء في الشمس, tr:eş-şerru bastukeş-şey’e fiş-şems, gloss:şerr, bir şeyi güneşe yaymandır, source:"ش ر ر,B002"}. Zerrenin kökü de güneşin doğuşunda yayılan ince ışığı adlandırır {ar:ذرت الشمس ذرورا إذا طلعت وهو ضوء لطيف منتشر, tr:zerratiş-şemsu zurûran izâ tala‘at ve huve dav’un latîfun munteşir, gloss:güneş doğup ince ışığını yaydı, source:"ذ ر ر,B004"}. Bu anlamlar kelimelerin ayetteki anlamını, iyilik ve kötülüğü, değiştirmez; yanlarında, en küçük kötülüğün bile güneşe serilmiş gibi açıkta olduğunu duyururlar. Gören de bu sahnededir: insan görünür olduğu için böyle adlandırılmıştır {ar:الإنس خلاف الجن وسموا لظهورهم, tr:el-insu hilâful-cinni ve summû li-zuhûrihim, gloss:ins cinnin karşıtıdır, görünür oldukları için böyle adlandırıldılar, source:"ء ن س,B001"}; göz bebeğinde görünen küçük suret {ar:إنسان العين المثال الذي يرى في السواد, tr:insânul-ayn el-misâlullezî yurâ fis-sevâd, gloss:göz bebeği, karalıkta görünen suret, source:"ء ن س,B005"} de aynı adı taşır; görmek ve duymak da bu köktendir {ar:آنست الشيء إذا رأيته وآنسته إذا سمعته, tr:ânestuş-şey’e izâ ra’eytuhû ve ânestuhû izâ semi‘tuh, gloss:bir şeyi gördüğümde ve duyduğumda "ânestu" derim, source:"ء ن س,B002"}. Üçüncü ayetin insanı sarsıntıyı görür, haberi duyar ve sonunda amelini görür.

Kur’an bu açığa çıkarışı birçok yerde sahneler. Kabirlerdekiyle göğüslerdeki birlikte çıkarılır: {ar:وَحُصِّلَ مَا فِى ٱلصُّدُورِ, tr:ve hussıle mâ fis-sudûr, gloss:göğüslerde olan ortaya dökülür, source:100:10}. Altıncı ayetin fiili göğüs kelimesiyle aynı köktendir {source:"ص د ر,B001"}; bu bir kök ortaklığıdır, aynı anlam değildir, ama bu ayetin yanında duyulur. Gizliler o gün sınanır {source:86:9}; {ar:يَوْمَئِذٍ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌ, tr:yevmeizin tu‘radûne lâ tahfâ minkum hâfiyeh, gloss:o gün arz olunursunuz, sizden hiçbir gizli kalmaz, source:69:18}. Çıkarma fiili kayıt için de kullanılır: {ar:وَنُخْرِجُ لَهُۥ يَوْمَ ٱلْقِيَٰمَةِ كِتَٰبًا يَلْقَىٰهُ مَنشُورًا, tr:ve nuhricu lehû yevmel-kıyâmeti kitâben yelkâhu menşûrâ, gloss:kıyamet günü onun için açılmış bulacağı bir kitap çıkarırız, source:17:13}; hemen ardından {ar:ٱقْرَأْ كِتَٰبَكَ, tr:ikra’ kitâbek, gloss:kitabını oku, source:17:14} denir. Sayfalar açılır {source:81:10}. Allah’ın uyarısında her nefis yaptığı iyiliği hazır bulur {ar:يَوْمَ تَجِدُ كُلُّ نَفْسٍ مَّا عَمِلَتْ مِنْ خَيْرٍ مُّحْضَرًا, tr:yevme tecidu kullu nefsin mâ amilet min hayrin muhdarâ, gloss:her nefsin yaptığı iyiliği hazır bulduğu gün, source:3:30}. Musa ve İbrahim’in sayfalarındaki söz surenin edilgen fiilini kullanır: {ar:وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ, tr:ve enne sa‘yehû sevfe yurâ, gloss:ve onun çabası görülecektir, source:53:40}. İnsana dirilişte {ar:فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌ, tr:fekeşefnâ anke gitâeke fe-basarukel-yevme hadîd, gloss:örtünü üzerinden kaldırdık, bugün gözün keskindir, source:50:22} denir; herkes ellerinin öne sürdüğüne bakar {source:78:40}. Ve o gün yer, Rabbinin nuruyla aydınlanır, kitap konur {ar:وَأَشْرَقَتِ ٱلْأَرْضُ بِنُورِ رَبِّهَا وَوُضِعَ ٱلْكِتَٰبُ, tr:ve eşrakatil-arzu bi-nûri rabbihâ ve vudi‘al-kitâb, gloss:yer Rabbinin nuruyla parladı ve kitap kondu, source:39:69}.

Kaynaklar: 99:2 أَثْقَالَهَا ث ق ل B002; 99:2 وَأَخْرَجَتِ خ ر ج B002; 99:4 أَخْبَارَهَا خ ب ر B001; 99:4 تُحَدِّثُ ح د ث B006; 99:4 تُحَدِّثُ ح د ث B007; 99:6 لِّيُرَوْا۟ ر ء ي B012; 99:6 لِّيُرَوْا۟ ر ء ي B005; 99:7 يَرَهُۥ ر ء ي B001; 99:8 شَرًّا ش ر ر B008; 99:8 شَرًّا ش ر ر B002; 99:7 ذَرَّةٍ ذ ر ر B004; 99:3 ٱلْإِنسَٰنُ ء ن س B001; 99:3 ٱلْإِنسَٰنُ ء ن س B005; 99:3 ٱلْإِنسَٰنُ ء ن س B002; 99:6 يَصْدُرُ ص د ر B001

## Sudan dönen kalabalık

Altıncı ayetin fiili çobanın fiilidir: {ar:يَوْمَئِذٍ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًا, tr:yevmeizin yasdurun-nâsu eştâtâ, gloss:o gün insanlar bölük bölük dönerler, source:99:6}. Sudur, sulak yere geldikten sonra oradan dönüp ayrılmaktır {ar:الصدر الانصراف عن الورد وعن كل أمر, tr:es-sadru el-insırâfu anil-virdi ve an kulli emr, gloss:sadr, suya gelişten ve her işten dönüp ayrılmaktır, source:"ص د ر,B003"}; develer sudan döner {ar:صدرت الإبل عن الماء, tr:saderatil-ibilu anil-mâ’, gloss:develer sudan döndü, source:"ص د ر,B003"}, yol da halkını sudan geri taşır {ar:طريق صادر يصدر بأهله عن الماء, tr:tarîkun sâdirun yasduru bi-ehlihî anil-mâ’, gloss:halkını sudan geri götüren yol, source:"ص د ر,B003"}. Aynı kök bir şeyin bir bölüğünü de adlandırır {ar:الصدر الطائفة من الشيء, tr:es-sadru et-tâifetu mineş-şey’, gloss:sadr, bir şeyden bir bölüktür, source:"ص د ر,B006"}. Bölük bölük kelimesi tam bu ayetle açıklanır {ar:يصدر الناس أشتاتا أي متفرقين, tr:yasdurun-nâsu eştâtan ey muteferrikîn, gloss:insanlar dağınık hâlde dönerler, source:"ش ت ت,B001"}; kök bir topluluğun dağılıp ayrılmasıdır {ar:الشت تفريق الشعب, tr:eş-şettu tefrîkuş-şa‘b, gloss:şett, bir topluluğu dağıtmaktır, source:"ش ت ت,B001"}. İnsanlar da önce tek bir kalabalıktır {ar:الإنس جماعة الناس, tr:el-insu cemâatun-nâs, gloss:ins insanların topluluğudur, source:"ء ن س,B001"}.

Sahne somuttur: sürülerin suya inmesi gibi bir yere toplanmış kalabalık oradan geri döner ve ayrı bölükler hâlinde yola koyulur. Ayetin iki ucu, hareketin çıkış noktasını ve varış yerini verir: dönüş ve {ar:لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:li-yurav a‘mâlehum, gloss:amelleri kendilerine gösterilsin diye, source:99:6}. Sade bir anlatım "insanlar dağılır" der; fiil ise dağılmanın bir toplanmanın ardından geldiğini ve bir yöne gittiğini duyurur. İkinci ayetin çıkması bu yürüyüşün ilk adımıdır {source:"خ ر ج,B001"}: yer bıraktığı anda kalabalık yola çıkar.

Kur’an fiilin asıl sahnesini Musa’nın Medyen suyunda anlatır. Musa suya varınca orada su veren bir topluluk bulur ve iki kadın ona {ar:لَا نَسْقِى حَتَّىٰ يُصْدِرَ ٱلرِّعَآءُ, tr:lâ neskî hattâ yusdirar-riâ’, gloss:çobanlar sürülerini sudan çevirmeden biz sulamayız, source:28:23} der; suya varış ve sudan dönüş aynı ayettedir. Su imgesi kıyamete de taşınır: Firavun kavminin önüne düşer {ar:فَأَوْرَدَهُمُ ٱلنَّارَ وَبِئْسَ ٱلْوِرْدُ ٱلْمَوْرُودُ, tr:fe-evradehumun-nâr, ve bi’sel-virdul-mevrûd, gloss:onları ateşe sudan içirmeye götürdü, varılan ne kötü bir sulak yer, source:11:98}; suçlular cehenneme suya sürülür gibi sürülür {ar:وَنَسُوقُ ٱلْمُجْرِمِينَ إِلَىٰ جَهَنَّمَ وِرْدًا, tr:ve nesûkul-mucrimîne ilâ cehenneme virdâ, gloss:suçluları cehenneme susuz sürü gibi süreriz, source:19:86}. Kalabalığın çıkışı da başka ayetlerde görünür: {ar:يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ كَأَنَّهُمْ جَرَادٌ مُّنتَشِرٌ, tr:yahrucûne minel-ecdâsi keennehum cerâdun munteşir, gloss:kabirlerden yayılmış çekirgeler gibi çıkarlar, source:54:7}; {ar:يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًا كَأَنَّهُمْ إِلَىٰ نُصُبٍ يُوفِضُونَ, tr:yevme yahrucûne minel-ecdâsi sirâan keennehum ilâ nusubin yûfidûn, gloss:kabirlerden hızla, dikili bir işarete koşar gibi çıktıkları gün, source:70:43}; {ar:فَإِذَا هُم مِّنَ ٱلْأَجْدَاثِ إِلَىٰ رَبِّهِمْ يَنسِلُونَ, tr:fe-izâ hum minel-ecdâsi ilâ rabbihim yensilûn, gloss:bir de bakarsın kabirlerden Rablerine akın ederler, source:36:51}. Kalabalık tek tek kişilere kadar ayrılır: {ar:وَكُلُّهُمْ ءَاتِيهِ يَوْمَ ٱلْقِيَٰمَةِ فَرْدًا, tr:ve kulluhum âtîhi yevmel-kıyâmeti ferdâ, gloss:hepsi kıyamet günü O’na tek başına gelir, source:19:95}; ölülere de {ar:وَلَقَدْ جِئْتُمُونَا فُرَٰدَىٰ, tr:ve lekad ci’tumûnâ furâdâ, gloss:bize teker teker geldiniz, source:6:94} denir. Saatin günü {ar:يَوْمَئِذٍ يَتَفَرَّقُونَ, tr:yevmeizin yeteferrakûn, gloss:o gün ayrılırlar, source:30:14} ve {ar:يَوْمَئِذٍ يَصَّدَّعُونَ, tr:yevmeizin yassadda‘ûn, gloss:o gün bölünürler, source:30:43} sözleriyle de anlatılır; bölüklerin varış yerleri ise {ar:وَسِيقَ ٱلَّذِينَ كَفَرُوٓا۟ إِلَىٰ جَهَنَّمَ زُمَرًا, tr:ve sîkallezîne keferû ilâ cehenneme zumerâ, gloss:inkâr edenler cehenneme bölük bölük sürüldü, source:39:71} ve {ar:وَسِيقَ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ إِلَى ٱلْجَنَّةِ زُمَرًا, tr:ve sîkallezînettekav rabbehum ilel-cenneti zumerâ, gloss:Rablerinden sakınanlar cennete bölük bölük sürüldü, source:39:73} ayetlerinde gösterilir.

Kaynaklar: 99:6 يَصْدُرُ ص د ر B003; 99:6 يَصْدُرُ ص د ر B006; 99:6 أَشْتَاتًا ش ت ت B001; 99:6 ٱلنَّاسُ ء ن س B001; 99:2 وَأَخْرَجَتِ خ ر ج B001

## Serpilen zerre ve sıçrayan kıvılcım

Zerre kökünün işlemi serpmektir: tahılı, tuzu ya da ilacı dağıtarak saçmak {ar:ذررت الحب والدواء والملح أذره ذرا فرقته, tr:zerartul-habbe ved-devâe vel-milha ezurruhû zerran ferraktuh, gloss:taneyi, ilacı, tuzu serptim, yani dağıttım, source:"ذ ر ر,B002"}. Zerre de karıncaların en küçüğüdür, dağınık bir sürünün tek bir bireyi {ar:الذر صغار النمل الواحدة ذرة, tr:ez-zerru sıgârun-nemli, el-vâhidetu zerra, gloss:zerr küçük karıncalardır, tekili zerredir, source:"ذ ر ر,B001"}; aynı kökten ince bir tozun adı gelir {source:"ذ ر ر,B003"}. Altıncı ayetin bölükleri de bir topluluğun parçalara ayrılmasıdır {ar:شت يشت شتاتا وهو التفرق, tr:şette yeşittu şetâten ve huvet-teferruk, gloss:dağıldı, dağılmak, source:"ش ت ت,B001"}. Bu üç kelime tek bir imge kurar: bir kütle birimlere serpilir ve birim küçülür, insan bölüklerinden yedinci ve sekizinci ayette tartılan {ar:ذَرَّةٍ, tr:zerratin, gloss:zerre, source:99:7} ölçüsüne kadar.

Sekizinci ayette bu birime bir kıvılcım eklenir. Kötülük kelimesinin kökü ateşten sıçrayan kıvılcımı adlandırır {ar:الشرر ما تطاير من النار الواحدة شررة, tr:eş-şerer mâ tetâyera minen-nâr, el-vâhidetu şerera, gloss:şerer ateşten uçuşandır, tekili şereredir, source:"ش ر ر,B003"}. Bu bir kök ortaklığıdır; ayetteki kelime kötülük demektir. Ama {ar:مِثْقَالَ ذَرَّةٍ شَرًّا, tr:miskâle zerratin şerran, gloss:zerre ağırlığınca kötülük, source:99:8} sözünde kıvılcım da duyulur: en küçük kötülük, ateşten kopup uçan en küçük parça gibidir. Kur’an ateşin kıvılcımını ters ölçekte gösterir; inkâr edenlere anlatılan ateş {ar:إِنَّهَا تَرْمِى بِشَرَرٍ كَٱلْقَصْرِ, tr:innehâ termî bi-şererin kel-kasr, gloss:o, saray gibi kıvılcımlar atar, source:77:32}. Zerre büyüklüğündeki kötülükle saray büyüklüğündeki kıvılcım aynı kökte buluşur.

Kur’an insanları da dağınık bir sürü gibi gösterir: yayılmış çekirgeler {source:54:7} ve {ar:يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ, tr:yevme yekûnun-nâsu kel-ferâşil-mebsûs, gloss:insanların saçılmış pervaneler gibi olacağı gün, source:101:4}. Sarsılan yerin ardından dağlar da toza döner: {ar:فَكَانَتْ هَبَآءً مُّنۢبَثًّا, tr:fekânet hebâen munbessâ, gloss:saçılmış toz oldu, source:56:6}. En küçük canlıların sürüsü bir sahnede konuşur da: Süleyman’ın ordusu yaklaşırken bir karınca {ar:يَٰٓأَيُّهَا ٱلنَّمْلُ ٱدْخُلُوا۟ مَسَٰكِنَكُمْ, tr:yâ eyyuhen-neml udhulû mesâkinekum, gloss:ey karıncalar, yuvalarınıza girin, source:27:18} der.

Kaynaklar: 99:7 ذَرَّةٍ ذ ر ر B002; 99:7 ذَرَّةٍ ذ ر ر B001; 99:7 ذَرَّةٍ ذ ر ر B003; 99:6 أَشْتَاتًا ش ت ت B001; 99:8 شَرًّا ش ر ر B003; 99:8 ذَرَّةٍ ذ ر ر B001

## Ak ile kara kadar uzak iki pay

Bölük bölük kelimesi yalnızca dağılmak değildir. Aynı kökten iki şey arasındaki büyük mesafe söylenir {ar:شتان ما بينهما, tr:şettâne mâ beynehumâ, gloss:ikisinin arası ne kadar uzak, source:"ش ت ت,B003"}, ikisi arasındaki bağın kalkması {ar:ارتفاع الالتئام بينهما, tr:irtifâul-iltiâmi beynehumâ, gloss:aralarındaki kaynaşmanın kalkması, source:"ش ت ت,B003"}. İyilik ve kötülük de birbirinin karşıtıdır {ar:الشر نقيض الخير, tr:eş-şerru nakîdul-hayr, gloss:şer hayrın zıddıdır, source:"ش ر ر,B001"}. Çıkma kökü ise iki renkli bir yüzeyi adlandırır {ar:الخرج لونان بين سواد وبياض, tr:el-harac levnâni beyne sevâdin ve beyâd, gloss:harac karayla ak arasında iki renktir, source:"خ ر ج,B007"}. Altıncı ayetin kalabalığı surenin son iki ayetine ayrılır: biri {ar:خَيْرًا يَرَهُۥ, tr:hayran yerahû, gloss:iyilik, onu görür, source:99:7}, öbürü {ar:شَرًّا يَرَهُۥ, tr:şerran yerahû, gloss:kötülük, onu görür, source:99:8}. İki ayet aynı kelimelerle kurulur, yalnızca son kelimeden önceki ad değişir; bu eşitlik iki payın arasındaki uzaklığı daha keskin gösterir.

Kur’an bu ayrılışı renkle gösterir: {ar:يَوْمَ تَبْيَضُّ وُجُوهٌ وَتَسْوَدُّ وُجُوهٌ, tr:yevme tebyaddu vucûhun ve tesveddu vucûh, gloss:kimi yüzlerin ağarıp kimi yüzlerin karardığı gün, source:3:106}; {ar:وُجُوهٌ يَوْمَئِذٍ مُّسْفِرَةٌ, tr:vucûhun yevmeizin musfira, gloss:o gün parlayan yüzler var, source:80:38} ve {ar:وَوُجُوهٌ يَوْمَئِذٍ عَلَيْهَا غَبَرَةٌ, tr:ve vucûhun yevmeizin aleyhâ gabera, gloss:ve o gün üzerinde toz olan yüzler var, source:80:40}. Saatin günü insanlar ayrılır {source:30:14}, ardından {ar:فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ, tr:fe-emmallezîne âmenû ve amilus-sâlihât, gloss:iman edip salih amel işleyenlere gelince, source:30:15} ve {ar:وَأَمَّا ٱلَّذِينَ كَفَرُوا۟, tr:ve emmallezîne keferû, gloss:inkâr edenlere gelince, source:30:16} gelir: kalabalık amellere göre ikiye ayrılır. Toplanma günü {ar:فَرِيقٌ فِى ٱلْجَنَّةِ وَفَرِيقٌ فِى ٱلسَّعِيرِ, tr:ferîkun fil-cenneti ve ferîkun fis-saîr, gloss:bir bölük cennette, bir bölük alevli ateşte, source:42:7}. Aynı kök çabaların ayrılığı için de kullanılır: {ar:إِنَّ سَعْيَكُمْ لَشَتَّىٰ, tr:inne sa‘yekum le-şettâ, gloss:çabalarınız elbette çeşit çeşittir, source:92:4}. Kitap da iki payı ayırır: sağından verilen {source:69:19} ve solundan verilen {source:69:25}.

Kaynaklar: 99:6 أَشْتَاتًا ش ت ت B003; 99:6 أَشْتَاتًا ش ت ت B001; 99:7 خَيْرًا خ ي ر B001; 99:8 شَرًّا ش ر ر B001; 99:2 وَأَخْرَجَتِ خ ر ج B007

## Buluşmalar

Surenin hareketi bir yönden ötekine geçer: içeriden dışarıya, ağırdan hafife, büyükten küçüğe, sessizden konuşana, gizliden görünene. İmgeler bu hareketin farklı yüzlerini taşır ve birkaç sahnede üst üste biner.

İlk buluşma yerin boşalmasıyla doğumdur. İkinci ayetin iki kelimesi, {ar:وَأَخْرَجَتِ, tr:ve ahracet, gloss:ve çıkardı, source:99:2} ile {ar:أَثْقَالَهَا, tr:eskâlehâ, gloss:ağırlıkları, source:99:2}, hem gömülü yükü atan yeri hem doğuran bedeni anlatır. Kur’an bu iki sahneyi aynı ayetlerde tutar: Saatin sarsıntısı {source:22:1} ve her gebenin yükünü bırakması {source:22:2}; rahimden çocuğu çıkarmak ve suyla titreyip kabaran toprak {source:22:5}. Aynı ayet bitki imgesini de içerir; böylece boşalan yer, doğuran beden ve filiz veren tarla tek bir dirilişin üç görünüşü olur. Ağır bulutlarla meyveyi ve ölüleri çıkaran ayet {source:7:57} ağırlık imgesini de bu sahneye bağlar.

İkinci buluşma boşalan yerle konuşan yerdir. İnşikak suresinde sıra surenin sırasıyla aynıdır: yer içindekini atar ve boşalır {source:84:4}, sonra Rabbine kulak verir {source:84:5}. İkinci ayette yer yükünü çıkarır, beşinci ayette Rabbinin vahyini alır. Arada üçüncü ayetin sarsılmış insanı vardır: sarsıntı bedenine geçmiş, ağzından {ar:مَا لَهَا, tr:mâ lehâ, gloss:ona ne oluyor, source:99:3} sorusu çıkmıştır. Bu soru, sarsıntı imgesini konuşma imgesine bağlar; çünkü yer ona cevap verecektir. Suçluların kitabın önündeki sorusu {source:18:49} aynı biçimdedir ve ardından yaptıklarını hazır bulurlar: soru, haber ve görme bir sahnede toplanır.

Üçüncü buluşma konuşmayla göstermedir. Dördüncü ayette yerin anlattığı haber, işin içyüzüdür; anlatmak açığa vurmak, kılıcı parlatmaktır. Yerin içindekilerini çıkarması ile haberlerini anlatması aynı işlemdir: içeride olanın dışarı verilmesi. Kur’an bu iki çıkarışı yan yana koyar: kabirlerdeki altüst edilir ve göğüslerdeki ortaya dökülür {source:100:9}, {source:100:10}; kıyamet günü kitap çıkarılır ve açılmış bulunur {source:17:13}.

Dördüncü buluşma altıncı ayetin kendisidir. Sudan dönen kalabalık bir yöne yürür ve ayet varış yerini söyler: {ar:لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:li-yurav a‘mâlehum, gloss:amelleri kendilerine gösterilsin diye, source:99:6}. Yolun sonunda tutulan ayna vardır. Aynı kalabalık bölüklere serpilir ve zerre imgesi başlar; bölükler arasındaki uzaklık da iki payın imgesini açar. Bir kelime, {ar:أَشْتَاتًا, tr:eştâtâ, gloss:bölük bölük, source:99:6}, üç imgeyi birden taşır: sudan dönüş, serpilme ve ak ile kara kadar uzak iki pay.

Son buluşma zerrede olur. {ar:ذَرَّةٍ, tr:zerratin, gloss:zerre, source:99:8} hem serpilmenin en küçük birimidir hem terazideki en küçük ağırlık; kötülük sözünün yanında ateşten kopan kıvılcım, toprağı yarıp çıkan filiz ve güneşte yayılan ince ışık da duyulur. Ağırlık kökü burada çemberi kapatır: sure yerin bütün ağırlıklarıyla açılmış, aynı kökten bir miskalle biter. Lokman’ın oğluna söylediği söz {source:31:16} bu iki ucu birleştirir: yerin içinde gizli bir küçük ağırlık getirilir ve sözü {ar:إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌ, tr:innallâhe latîfun habîr, gloss:Allah en ince şeyi bilen, her şeyden haberdardır, source:31:16} diye biter. Haber kökü burada da durur: yerin anlattığı haberler, her şeyden haberdar olanın bildiğidir. Yer ağırlıklarını verir, haberlerini anlatır; insan da tek tek, en küçük ağırlığına kadar amelini görür.

