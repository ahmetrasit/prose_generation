Focus: 101:11. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/101_11/D.r13/context.md =====
# 101:11 — focus

نَارٌ حَامِيَةٌۢ

Anchor translation (canonical reading, reference only):

Kızgın bir ateştir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | نَارٌ | نَار | ن و ر | N |
| 2 | حَامِيَةٌۢ | حَامِيَة | ح م ي | ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 101 — full text (context; no pericope)

- 101:1 ٱلْقَارِعَةُ
- 101:2 مَا ٱلْقَارِعَةُ
- 101:3 وَمَآ أَدْرَىٰكَ مَا ٱلْقَارِعَةُ
- 101:4 يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ
- 101:5 وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ ٱلْمَنفُوشِ
- 101:6 فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ
- 101:7 فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ
- 101:8 وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ
- 101:9 فَأُمُّهُۥ هَاوِيَةٌۭ
- 101:10 وَمَآ أَدْرَىٰكَ مَا هِيَهْ
- 101:11 ◀ focus نَارٌ حَامِيَةٌۢ


===== _commentary/v16/work/101_11/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن و ر (root_001564) — identity root of نَارٌ (w1)

- **B001** ışık ve aydınlatma — ışık, aydınlık · ışık vermek, aydınlanmak veya aydınlatmak · aydınlatma; günün ağarması
  النور الضياء والفعل نار وأنار ونورا وإنارة واستنار أي أضاء (ayn)؛ النور: الضياء؛ أنار الشئ واستنار بمعنى أي أضاء؛ التنوير: الإنارة؛ التنوير: الإسفار (sihah)؛ أصل صحيح يدل على إضاءة واضطراب وقلة ثبات؛ النور والنار سميا بذلك من طريقة الإضاءة (maqayis)
- **B002** yanan ateş ve ateşle yapılan hayvan damgası — yanan ateş · ateşler · devenin ateşle yapılmış damgası · hayvanın soyu damgasından belli olur
  النار مؤنثة وهي من الواو؛ الجمع نور ونيران (sihah)؛ ما نار هذه الناقة أي ما سمتها؛ نجارها نارها؛ سماتها (sihah)؛ النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة (maqayis)
- **B003** ateşi uzaktan görüp ona yönelmek [kalıp] — ateşe doğru yönelmek · ateşi uzaktan görüp seçmek
  تنورت نارا قصدت إليها (ayn)؛ تنورت النار من بعيد: تبصرتها (sihah)؛ تنورت النار تبصرتها (maqayis)
- **B004** ağaç çiçeği ve çiçeklenme — ağaç çiçeği · ağaç çiçekleri; tek bir ağaç çiçeği · ağaç çiçek açtı · ağacın çiçek açması
  النور نور الشجر؛ تنوير الشجرة إزهارها؛ النوار نور الشجر (ayn)؛ تنوير الشجرة: إزهارها؛ نورت الشجرة وأنارت أي أخرجت نورها؛ النوار نور الشجر (sihah)؛ ومنه النور نور الشجر ونواره؛ أنارت الشجرة أخرجت النور (maqayis)
- **B005** yol gösteren belirgin işaret ve yüksek yapı — yol gösteren belirgin işaret · arazinin sınırları ve belirgin işaretleri · yol gösteren, üstünde ışık bulunan veya çağrı yapılan yüksek yapı
  المنارة مفعلة من الإنارة؛ كانوا ينورون في الجاهلية ليهتدى ويقتدى بها؛ المنارة الشمعة ذات السراج؛ المنارة ما يوضع عليه للمسرجة؛ المنارة للمؤذن (ayn)؛ المنار: علم الطريق؛ ضرب المنار على طريقه ليهتدى بها؛ المنارة التي يؤذن عليها؛ المنارة ما يوضع فوقها السراج (sihah)؛ المنارة مفعلة من الاستنارة؛ منار الأرض حدودها وأعلامها سميت لبيانها وظهورها (maqayis)
- **B006** ürkmek, kaçınmak ve uzaklaştırmak — kötülükten veya erkeklerden uzak duran iffetli kadın · ürkek ve insandan kaçan ceylanlar · kuşku verici durumdan uzak duran kadınlar · eşinden ürküp kaçınan kısrak veya inek · bir şeyden ürküp uzaklaşmak · birini söz veya davranışla ürkütüp uzaklaştırmak · ürkme, kaçınma ve uzaklaşma
  امرأة نوار وهي العفيفة النافرة عن الشر والقبيح؛ التي تكره الرجال؛ بقرة نوار تنفر من الفحل؛ نرت فلانا أي أنفرته (ayn)؛ النور أيضا: النفر من الظباء؛ نسوة نور أي نفر من الربية؛ الواحدة نوار وهي الفرور؛ فرس وديق نوار؛ نرت من الشئ؛ نرت غيري أي نفرته (sihah)؛ امرأة نوار أي عفيفة تنور أي تنفر من القبيح؛ نارت نفرت؛ نرت فلانا نفرته؛ النوار النفار (maqayis)
- **B007** topluluklar arası düşmanlık ve kin — topluluklar arasında çıkan düşmanlık ve kin
  النائرة الكائنة تقع بين القوم (ayn)؛ بينهم نائرة أي عداوة وشحناء (sihah)
- **B008** göz boyası ve dövme için kullanılan duman karası — göz boyası veya dövme için kullanılan fitil ya da yağ dumanı karası · deriyi veya diş etini iğneleyip üzerine duman karası ya da göz boyası serpmek
  النؤور دخان الفتيلة يتخذ كحلا أو وشما (ayn)؛ النوور: النيلج، وهو دخان الشحم يعالج به الوشم؛ وقد نور ذراعه إذا غرزها بإبرة ثم ذر عليها النوور (sihah)؛ مما شذ عن هذا الأصل النؤور دخان الفتيلة يتخذ كحلا ووشما؛ نورت اللثة غرزتها بإبرة ثم جعلت في الغرز الإثمد (maqayis)
- **B009** bedene sürülen özel karışım ve onu sürünme — bedene sürülen özel karışım · özel karışımı bedenine sürmek
  النورة يطلى بها (ayn)؛ تنور الرجل: تطلى بالنورة (sihah)
- **B010** bir işi karışık gösterip yanıltmak [kalıp] — bir işi birine karışık gösterip onu yanıltmak
  فلان ينور على فلان إذا شبه عليه أمرا؛ ليست الكلمة بعربية محضة؛ امرأة كانت تسمى نورة (ayn)
- **B011** açıkça seçilen veya belirgin biçimde çıkan şey — yolun belirgin oluğu · kumaşın belirgin işareti veya çizgisi · çift hayvanının boynundaki boyunduruk ve takımı · gücü başkasının iki katı olan adam
  النون والياء والراء كلمة تدل على وضوح شيء وبروزه؛ أخدود الطريق الواضح منه نير؛ نير الثوب علمه؛ النير الخشبة على عنق الفدان؛ ما ننكر أن يكون أصل هذا كله الواو فيرجع إلى ما ذكرناه في باب النور والنار (maqayis)

## ح م ي (root_000358) — identity root of حَامِيَةٌۢ (w2)

- **B001** ısınma ve ısıtma — ısındı, sıcaklığı arttı · demiri ateşte ısıttı · at koşudan ısınıp terledi · altın ve gümüşü ısıtma, bu işlemden iyi çıkma
  حمي الشيء يحمى حميا إذا سخن (ayn)؛ الحامية الحارة (ayn)؛ حمى النهار وحمي التنور أي اشتد حره (sihah)؛ أحميت الحديد في النار فهو محمى (sihah)؛ الحمي الحرارة المتولدة من الجواهر المحمية كالنار والشمس ومن القوة الحارة في البدن (mufradat)؛ حمي الفرس إذا عرق يحمى حميا وحمى الشد مثله (ayn;tahdhib)؛ هذا الذهب والفضة لحسن الحماء أي خرج من الحماء حسنا (ayn;tahdhib)
- **B002** koruma ve uzak tutma — onu korudu, yaklaşanı savdı · otlatmaya kapalı korunan yer · yeri korunan ve girilmez alan yaptı · hastaya zararlı yiyeceği yasakladı · hasta sakıncalı yiyeceklerden uzak durdu · insanlar ondan sakınıp uzak durdu · onu savundu ve korudu · yanındakileri ya da kendini koruyan kişi veya topluluk
  حميت القوم حماية وكل شيء دفعت عنه فقد حميته (ayn)؛ الحمى موضع فيه كلأ يحمى من الناس أن يرعى (ayn;tahdhib)؛ حميته حماية إذا دفعت عنه (sihah)؛ هذا شيء حمى أي محظور لا يقرب (sihah)؛ حميت المريض حمية منعته أكل ما يضره (ayn)؛ حاميت عنه محاماة وحماء (sihah)؛ تحاماه الناس أي توقوه واجتنبوه (sihah)؛ حمى أهله في القتال حماية (tahdhib)
- **B003** gücenme ve öfkelenme — onuruna yedirememe, gücenme ve öfke · ona öfkelendi · onurlu, aşağılanmayı kabul etmeyen
  حميت من هذا الشيء أحمى منه حمية أي أنفت أنفا وغضبا (ayn)؛ حميت عن كذا حمية ومحمية إذا أنفت منه وداخلك عار وأنفة (sihah)؛ حميت عليه غضبت (sihah)؛ حمى فلان أنفه يحميه حمية ومحمية (tahdhib)؛ عبر عن القوة الغضبية إذا ثارت وكثرت بالحمية (mufradat)
- **B004** kocanın yakınları — kocanın babası, erkek kardeşi ya da başka bir erkek yakını · kadının kocası tarafından gelen yakınları · kadının kayınvalidesi · kocanın erkek yakınıyla baş başa kalmak ölüm kadar tehlikelidir
  الحمو أبو الزوج وأخو الزوج وكل من ولي الزوج من ذي قرابته فهم أحماء المرأة وأم زوجها حماتها (ayn;tahdhib)؛ حماة المرأة أم زوجها (sihah;tahdhib)؛ كل شيء من قبل الزوج مثل الأب والأخ فهم الأحماء واحدهم حما (sihah)؛ الأحماء من قبل الزوج والأختان من قبل المرأة (tahdhib)؛ الحمو الموت (tahdhib)؛ أحماء المرأة كل من كان من قبل زوجها (mufradat)
- **B005** dokunulmaz sayılan damızlık erkek deve — binilmeyen, kırkılmayan ve otlaktan alıkonmayan damızlık erkek deve · damızlık geçmişi nedeniyle sırtı dokunulmaz sayılan erkek deve
  الحامي الفحل من الإبل الذي طال مكثه عندهم (sihah)؛ إذا لقح ولد ولده فقد حمى ظهره فلا يركب ولا يجز له وبر ولا يمنع من مرعى (sihah)؛ ولا حام قيل هو الفحل إذا ضرب عشرة أبطن كأن يقال حمى ظهره فلا يركب (mufradat)
- **B006** kara ve kötü kokulu balçık — kara ve kötü kokulu balçık · kara balçık, akarsu ya da kuyudan çıkarılan balçık · balçıklı pınar · kuyunun balçığını çıkardı
  الحمأ الطين الأسود المنتن (ayn)؛ يسمى الطين الذي نبث من النهر الحمأة (ayn)؛ عين حمئة أي ذات حمأة (ayn;mufradat)؛ الحمأة والحمأ طين أسود منتن (mufradat)؛ حمأت البئر أخرجت حمأتها وأحمأتها جعلت فيها حما (mufradat)
- **B007** sokucu hayvan zehrinin yakıcı etkisi — sokan ya da ısıran canlının zehri ve yakıcı etkisi · akrebin zehri ve verdiği zarar, iğnesi değil
  الحُمَة سم كل شيء يلدغ أو يلسع (ayn;tahdhib)؛ حمة العقرب سمها وضرها (sihah)؛ الحمة مخففة حرارة السم وليست كما تسمي العامة حمة العقرب إبرتها (jamhara)؛ هي فوعة السم أي حرارته وفورته (jamhara)؛ بسم العقرب الحمة والحمة (tahdhib)
- **B008** etkinin keskinliği ve şiddeti — içkinin ilk yükselişi, sıcaklığı ve içene yayılan etkisi · ağrının kabaran keskinliği · şeyin sertliği ve şiddeti
  الحميا بلوغ الخمر من شاربها (ayn)؛ حميا الكأس أول سورتها (sihah)؛ حموة الألم سورته (sihah)؛ حميا الكأس يعني سورتها (tahdhib)؛ الحميا دبيب الشراب (tahdhib)؛ حميا الشيء حدته وشدته (tahdhib)؛ حميا الكأس سورتها وحرارتها (mufradat)
- **B009** bacağın içindeki kabarık kas parçası — bacağın içindeki kabarık et ya da kas parçası · atın bacağının eninde bulunan iki et parçası
  الحمأة لحمة منتبرة في باطن الساق (ayn)؛ الحماة عضلة الساق (sihah)؛ في ساق الفرس حماتان وهما اللحمتان اللتان في عرض الساق (sihah)؛ الحماة لحمة منتبرة في باطن الساق (tahdhib)؛ الحماتان اللحمتان اللتان في عرض الساق (tahdhib)
- **B010** toynağın iki yan kenarı — toynağın ortadaki bölümünün sağ ve solundaki iki parça · toynağın sağ ve sol yan kenarları
  الحاميتان ما عن يمين السنبك وشماله (sihah;tahdhib)؛ الحوامي وهي حروفها من عن يمين وشمال (tahdhib)
- **B011** kuyu duvarını ören ağır taşlar — kuyu duvarını örmekte kullanılan taş · kuyu örgüsünü sağlamlaştıran büyük ve ağır kayalar
  الحامية الحجارة يطوى بها البئر (ayn;tahdhib)؛ الحوامي عظام الحجارة وثقالها (tahdhib)؛ الحوامي صخر عظام تجعل في مآخير الطي (tahdhib)؛ حجارة الركية كلها حوام (tahdhib)
- **B012** kararıp kara bir görünüm alma — karardı, kara bir görünüm aldı · üst üste yığılmış kara bulut
  احمومى الشيء فهو محموم واحمومى الليل والسحاب وذلك من السواد (ayn)؛ احمومى الشيء فهو محموم يوصف به الأسود من نحو الليل والسحاب (tahdhib)؛ المحمومي من السحاب الأسود المتراكم (tahdhib)

===== _commentary/v16/out/s101/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 101:11, and ## Buluşmalar) =====
## Savaş günü

Araplar savaşlarına "gün" adını verirdi. Aynı kökte gün, olup biten olayın kendisidir: {ar:الأيام في معنى الوقائع, tr:el-eyyâm fî ma'ne'l-vekâi', gloss:günler, vakalar, çarpışmalar anlamında, source:"ي و م,B003"}. Bu tanım dördüncü ayetin fiilini de içine alır: {ar:اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت, tr:el-yevm: el-kevn, el-kâine, gloss:gün, olan şey, inip meydana gelen olaydır, source:"ي و م,B003"}. Fiilin kendi kökünde ise {ar:الكون الحدث يكون بين الناس, tr:el-kevnu el-hadesu yekûnu beyne'n-nâs, gloss:kevn, insanlar arasında olan olaydır, source:"ك و ن,B001"} denir. Dördüncü ayetin {ar:يَوْمَ يَكُونُ ٱلنَّاسُ, tr:yevme yekûnu'n-nâs, gloss:insanların ... olacağı gün, source:101:4} ifadesi, bu tanımın kelimelerini taşır.

Kâria kelimesinin bir kolu da kılıç çarpışmasıdır: {ar:المقارعة والقراع المضاربة بالسيف في الحرب, tr:el-mukâra'a ve'l-kırâ', gloss:savaşta kılıçla karşılıklı vuruşmak, source:"ق ر ع,B002"}. Surenin öbür kelimeleri, aynı meydanın birer parçasını adlandırır. Mebsûs atların akına dağıtılmasıdır: {ar:بثوا الخيل, tr:besse'l-hayl, gloss:atları yaydılar, source:"ب ث ث,B001"}. "Bildirmek" fiilinin bir kalıp kullanımı, bir yerin baskın hedefi olarak seçilmesini anlatır: {ar:ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة, tr:iddarâ benû fulân mekâne kezâ, gloss:filan oğulları falan yeri baskın için hedef aldı, source:"د ر ي,B002"}. Sekizinci ayetin "hafif geldi" fiili, obanın aceleyle göçmesini de anlatır: {ar:خف القوم إذا ارتحلوا مسرعين, tr:haffe'l-kavm, gloss:topluluk aceleyle göçtü, source:"خ ف ف,B002"}. On birinci ayetin ateşi, kabile içinde parlayan düşmanlığın da adıdır: {ar:النائرة الكائنة تقع بين القوم, tr:en-nâira el-kâine, gloss:nâira, topluluk arasında patlak veren olaydır, source:"ن و ر,B007"}; burada yine kâine kelimesi, yani gün ve olmak kelimelerinin kökü geçer. Hâmiye ise savaşta ailesini koruyanı {ar:حمى أهله في القتال حماية, tr:hamâ ehlehû fi'l-kıtâl, gloss:savaşta ailesini korudu, source:"ح م ي,B002"} ve öfkesi kızışan savaşçıyı {ar:حميت عليه غضبت, tr:hamîtu aleyh, gloss:ona öfkelendim, source:"ح م ي,B003"} anlatır.

Bu imge, düz bir anlatımın veremeyeceği bir şeyi duyurur: kıyamet uzak bir tarih değil, bir topluluğun başına gelen bir gündür, tıpkı tarihte anılan savaş günleri gibi. Kelimenin bir kalıp kullanımı da bunu Kur'an'a bağlar: {ar:وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب, tr:ve zekkirhum bi-eyyâmi'llâh, gloss:onlara Allah'ın günlerini hatırlat, yani Âd'a, Semûd'a ve başkalarına inen azabı, source:"ي و م,B004"}. İbrâhîm suresinde Allah, Mûsâ'yı kavmine gönderirken ona {ar:وَذَكِّرْهُم بِأَيَّىٰمِ ٱللَّهِ, tr:ve zekkirhum bi-eyyâmi'llâh, gloss:onlara Allah'ın günlerini hatırlat, source:14:5} diye emreder; birkaç ayet sonra Mûsâ, kavmine Nûh, Âd ve Semûd kavimlerinin haberini hatırlatır {source:14:9}. Hâkka suresinde ise kâriayı yalanlayanlar tam da bu iki kavimdir {source:69:4}: {ar:فَأَمَّا ثَمُودُ فَأُهْلِكُوا۟ بِٱلطَّاغِيَةِ, tr:fe-emmâ Semûdu fe-uhlikû bi't-tâğiye, gloss:Semûd, haddi aşan bir sarsıntıyla yok edildi, source:69:5}, {ar:وَأَمَّا عَادٌۭ فَأُهْلِكُوا۟ بِرِيحٍۢ صَرْصَرٍ عَاتِيَةٍۢ, tr:ve emmâ Âdun fe-uhlikû bi-rîhin sarsarin âtiye, gloss:Âd ise azgın, uğuldayan bir rüzgârla yok edildi, source:69:6}. Bu iki ayetin "fe-emmâ ... ve emmâ" kalıbı, Kâria suresinin altıncı ve sekizinci ayetlerinde tekrarlanır.

Kaynaklar: 101:1 ٱلْقَارِعَةُ ق ر ع B002; 101:4 يَوْمَ ي و م B003; 101:4 يَوْمَ ي و م B004; 101:4 يَكُونُ ك و ن B001; 101:5 وَتَكُونُ ك و ن B001; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:3 أَدْرَىٰكَ د ر ي B002; 101:10 أَدْرَىٰكَ د ر ي B002; 101:8 خَفَّتْ خ ف ف B002; 101:11 نَارٌ ن و ر B007; 101:11 حَامِيَةٌ ح م ي B002; 101:11 حَامِيَةٌ ح م ي B003

## Işığa düşen pervaneler

Dördüncü ayetin benzetmesi {ar:كَٱلْفَرَاشِ ٱلْمَبْثُوثِ, tr:ke'l-ferâşi'l-mebsûs, gloss:saçılmış pervaneler gibi, source:101:4} ifadesidir. Ferâş, ışığı arayarak uçan, sonunda kandile ya da ateşe düşen küçük kanatlı böcektir: {ar:الفراش التي تطير طالبة للضوء, tr:el-ferâş elletî tatîru tâlibeten li'd-dav', gloss:ferâş, ışığı arayarak uçan böceklerdir, source:"ف ر ش,B005"}; {ar:الفراشة التي تطير وتهافت في السراج, tr:el-ferâşe elletî tatîru ve tehâfetu fi's-sirâc, gloss:uçup kandile üşüşerek düşen pervane, source:"ف ر ش,B005"}; {ar:الفراش ما تراه كصغار البق يتهافت في النار, tr:yetehâfetu fi'n-nâr, gloss:küçük sinekler gibi ateşe üşüşüp düşenler, source:"ف ر ش,B005"}. Aynı kök, yere yakın kanat çırpışı da anlatır: {ar:تفرش الطائر إذا قرب من الأرض ورفرف بجناحه, tr:teferreşe't-tâir, gloss:kuş yere yaklaşıp kanat çırptı, source:"ف ر ش,B006"}. Mebsûs, sürünün dağılmasıdır; aynı fiil çekirgelerin yayılması için de kullanılır: {ar:انبث الجراد, tr:inbesse'l-cerâd, gloss:çekirgeler yayıldı, source:"ب ث ث,B001"}.

Benzetmenin açık anlamı, insanların dağınık, şaşkın ve sayısız oluşudur. Bu yüzeyin yanında, kelimenin içinden bir sahne duyulur: bir ateş vardır, sürü ona doğru uçar ve içine düşer. Surenin son kelimesi de nârdır, ateş. Ateşin kökü ışıkla birdir ve bu kök, aynı anda parlaklığı ve titrek, kararsız hareketi anlatır: {ar:النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة, tr:en-nûr ve'n-nâr, gloss:nur ve nar bu adı ışık saçtıkları ve titrek, hızlı hareketli oldukları için aldılar, source:"ن و ر,B002"}. Pervanenin çırpınışı ile alevin titreyişi aynı harekettir. Aynı kökte uzaktan görülen ateşe yönelmek de vardır: {ar:تنورت نارا قصدت إليها, tr:tenevvertu nâran, gloss:bir ateşe yöneldim, source:"ن و ر,B003"}.

Surenin kelimeleri bu yolculuğun adımlarını sırayla verir. Dördüncü ayetin {ar:ٱلنَّاسُ, tr:en-nâs, gloss:insanlar, source:101:4} kelimesi, uzaktan bir ateşi fark etmek anlamındaki fiille birlikte anılan kökle ilişkilendirilir: {ar:آنس من جانب يعني أبصر نارا, tr:ânese min cânib, gloss:bir yandan bir ateş gördü, source:"ء ن س,B002"}. Dokuzuncu ayetin {ar:فَأُمُّهُۥ, tr:fe-ummuhû, gloss:onun anası, source:101:9} kelimesinin kökü, bir hedefe doğru yönelmeyi de anlatır: {ar:الأم القصد المستقيم وهو التوجه نحو مقصود, tr:el-emm el-kasdu'l-mustakîm, gloss:emm, bir hedefe doğru dosdoğru yönelmektir, source:"ء م م,B012"}. Hâviye kelimesinin kökü, bir topluluğun birbiri ardınca çukura düşüşünü anlatır: {ar:تهاوى القوم في المهواة سقط بعضهم في إثر بعض, tr:tehâve'l-kavmu fi'l-mehvât, gloss:topluluk çukura birbiri ardınca düştü, source:"ه و ي,B002"}; pervanelerin birer birer kandile düşüşü gibi. On birinci ayetin hâmiyesi ise sürünün vardığı yerin sıcaklığıdır: {ar:حمي الشيء يحمى حميا إذا سخن, tr:hamiye'ş-şey', gloss:şey ısındı, source:"ح م ي,B001"}. Işık, sürü, yöneliş, düşüş ve sıcaklık tek bir sahnede birleşir. Ateşin kökü bunun tersini de adlandırır, ürküp kaçmayı: {ar:النوار النفار, tr:en-nevâr en-nifâr, gloss:nevâr, ürküp kaçmaktır, source:"ن و ر,B006"}. Bir canlının ateş karşısında yapması gereken budur; pervanenin yaptığı ise tam tersidir.

Aynı türden bir cezbetme sahnesi avcılıkta da vardır. "Bildirmek" fiilinin kökü, avcının avı alıştırmak için diktiği deveyi adlandırır: {ar:الدرية للناقة التي ينصبها الصائد ليأنس بها الصيد, tr:ed-diriyye, gloss:dirye, avın alışması için avcının diktiği dişi devedir, source:"د ر ي,B003"}; avcı onun arkasına saklanır ve görünmeden yaklaşır: {ar:تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته, tr:tedarreytu's-sayd... ve dereytuhû hateltuh, gloss:avın nerede olduğuna baktım, henüz görmeden; ve onu pusuyla avladım, source:"د ر ي,B003"}. Aynı kökte mızrak talimi için dikilen halka da hedef olarak anılır {source:"د ر ي,B005"}. İnsanların kökü burada iki karşıt hali verir: ürkmeyen, alışmış hal, {ar:الأنس أنس الإنسان بالشيء إذا لم يستوحش منه, tr:el-uns, gloss:üns, insanın bir şeye ürkmeden alışmasıdır, source:"ء ن س,B003"}, ve bir şeyden kuşkulanınca etrafa bakınmak, {ar:الاستئناس النظر وأحس بما رابه, tr:el-isti'nâs, gloss:bakınmak ve kuşkulandığı şeyi sezmek, source:"ء ن س,B002"}. Mebsûs, avcının köpeklerini salmasıdır, {ar:بث الصياد كلابه, tr:bessa's-sayyâdu kilâbeh, gloss:avcı köpeklerini saldı, source:"ب ث ث,B001"}, hâviye ise kartalın avına pike yapması: {ar:هوت العقاب إذا انقضت فإذا أراغته قيل أهوت له إهواء, tr:hevet el-ukâb, gloss:kartal pike yaptı; avını kollayınca ona daldı denir, source:"ه و ي,B003"}. Işık pervaneyi nasıl çekiyorsa, tuzak da avı öyle alıştırır. Üçüncü ve onuncu ayetteki "sana ne bildirdi" sorusu, bu aile imgesinde görünmeden yaklaşanın kökünde durur.

Kur'an'da ateşe yönelen insan sahnesi, bu imgenin tersini gösterir. Tâhâ suresinde Mûsâ, ailesiyle yolculuk ederken bir ateş görür: {ar:إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:innî ânestu nâran le'allî âtîkum minhâ bi-kabesin ev ecidu ale'n-nâri hudâ, gloss:ben bir ateş gördüm; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösterici bulurum, source:20:10}. Kasas suresi aynı sahneyi {ar:ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا, tr:ânese min cânibi't-Tûri nârâ, gloss:Tûr tarafından bir ateş gördü, source:28:29} diye anlatır; Neml suresinde Mûsâ ateşten bir haber ya da ısınmak için bir kor getirmeyi umar {source:27:7}. Mûsâ'nın vardığı ateş yol gösterir; pervanenin vardığı ateş yakar. Bakara suresinde Allah, münafıkları ateş yakan birine benzetir: {ar:كَمَثَلِ ٱلَّذِى ٱسْتَوْقَدَ نَارًۭا فَلَمَّآ أَضَآءَتْ مَا حَوْلَهُۥ ذَهَبَ ٱللَّهُ بِنُورِهِمْ, tr:ke-meseli'llezi'stevkade nâran fe-lemmâ edâet mâ havlehû zeheba'llâhu bi-nûrihim, gloss:ateş yakan biri gibi; ateş çevresini aydınlatınca Allah onların ışığını götürdü, source:2:17}; ışık ile ateşin aynı kökten oluşu orada da sahnenin kendisidir. Kamer suresinde Allah, insanların kabirlerden çıkışını {ar:كَأَنَّهُمْ جَرَادٌۭ مُّنتَشِرٌۭ, tr:ke-ennehum cerâdun munteşir, gloss:yayılmış çekirgeler gibi, source:54:7} diye anlatır; Meâric suresinde ise {ar:كَأَنَّهُمْ إِلَىٰ نُصُبٍۢ يُوفِضُونَ, tr:ke-ennehum ilâ nusubin yûfidûn, gloss:sanki dikili bir hedefe koşuşuyorlarmış gibi, source:70:43}. Hedefe koşan, birbiri ardınca düşen sürü, dördüncü ve dokuzuncu ayetlerin aile imgesinde de duyulur.

Kaynaklar: 101:4 كَٱلْفَرَاشِ ف ر ش B005; 101:4 كَٱلْفَرَاشِ ف ر ش B006; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:4 ٱلنَّاسُ ء ن س B002; 101:4 ٱلنَّاسُ ء ن س B003; 101:9 فَأُمُّهُۥ ء م م B012; 101:9 هَاوِيَةٌ ه و ي B002; 101:9 هَاوِيَةٌ ه و ي B003; 101:11 نَارٌ ن و ر B002; 101:11 نَارٌ ن و ر B003; 101:11 نَارٌ ن و ر B006; 101:11 حَامِيَةٌ ح م ي B001; 101:3 أَدْرَىٰكَ د ر ي B003; 101:3 أَدْرَىٰكَ د ر ي B005; 101:10 أَدْرَىٰكَ د ر ي B003

## Anası: dipsiz çukur

Dokuzuncu ayet, tartıları hafif gelene bir ana verir: {ar:فَأُمُّهُۥ هَاوِيَةٌۭ, tr:fe-ummuhû hâviye, gloss:onun anası hâviyedir, source:101:9}. Ayetin anlamı, onun sığınağının ve varacağı yerin hâviye olduğudur. Ümm, besleyen ve büyütendir: {ar:فلانة تؤم فلانا أي تغذوه وتربيه, tr:fulânetun teummu fulânâ, gloss:filan kadın filanı besler ve büyütür, source:"ء م م,B001"}. Ümm aynı zamanda yanındakileri kendine toplayan her şeydir: {ar:كل شيء يضم إليه ما سواه مما يليه فإن العرب تسمى ذلك الشيء أما, tr:kullu şey'in yedummu ileyhi mâ sivâh, gloss:yanındakileri kendine katan her şeye Araplar ümm der, source:"ء م م,B002"}; {ar:كل شيء انضمت إليه أشياء فهو أم, tr:kullu şey'in indammet ileyhi eşyâ', gloss:başka şeylerin kendisine katıldığı her şey ümmdür, source:"ء م م,B002"}. Bir şeyin varlığının, büyümesinin ya da başlangıcının kaynağı olan her şey de böyle adlandırılır {source:"ء م م,B002"}.

Hâviye, dibine erişilemeyen her uçurumdur: {ar:الهاوية كل مهواة لا يدرك قعرها والهوة كل وهدة معمقة, tr:el-hâviye kullu mehvâtin lâ yudraku ka'ruhâ, gloss:hâviye, dibine erişilemeyen her çukurdur; huvve, derinleştirilmiş her çukurdur, source:"ه و ي,B002"}; düşmek, yukarıdan aşağı yuvarlanmaktır: {ar:هوى الشيء يهوي إذا خر من علو إلى سفل, tr:heve'ş-şey'u yehvî, gloss:şey yukarıdan aşağıya düştü, source:"ه و ي,B002"}. Kökün temelinde boşluk ile düşüş birdir: {ar:أصل صحيح يدل على خلو وسقوط, tr:aslun sahîh yedullu alâ hulüvvin ve sukût, gloss:boşluk ve düşüşü gösteren sağlam bir kök, source:"ه و ي,B001"}. Gökle yer arasındaki hava da, boş bir kalp de bu kökle anılır: {ar:الهَواء ما بين السماء والأرض وكل خال هواء, tr:el-hevâ' mâ beyne's-semâi ve'l-ard, gloss:hevâ, gökle yer arasındaki şeydir; her boş şey hevâdır, source:"ه و ي,B001"}; {ar:قلبه هَواء, tr:kalbuhû hevâ', gloss:kalbi bomboş, source:"ه و ي,B001"}. Düşmek ölmektir de: {ar:هوى فلان أي مات, tr:hevâ fulân, gloss:filan düştü, yani öldü, source:"ه و ي,B002"}; hâviye, cehennemin adlarından biridir {source:"ه و ي,B002"}.

Ümm ile hâviyeyi bir araya getiren bir deyim vardır: {ar:هوت أمه فهي هاوية أي ثاكلة, tr:hevet ummuhû fe-hiye hâviye, gloss:anası düştü, yani evladını yitirdi; o, hâviyedir, source:"ه و ي,B002"}. Arapçada bu söz bir beddua olarak kullanılır, "anası ağlasın" gibi {source:"memory"}. Böylece ayet iki sahneyi birden taşır. Biri: anası evladını yitirmiştir, çünkü o ölmüştür. Öbürü: çukur onun anasıdır ve bir ananın çocuğunu bağrına basması gibi onu içine alır. Çukur besleyen değil yutan bir anadır; toplayan ama bırakmayan. Karşısında yedinci ayetin adamı durur, onun bir hayatı, bir yaşayışı vardır {source:"ع ي ش,B001"}. Hayat ile evladını yitirmiş ana, ayetlerin karşıtlığını aile imgesinde de kurar.

Çukurun bir dibi yoktur. Dağın kökü, kazanların kayaya varıp durduğu anı adlandıran bir deyim taşır: {ar:أجبل القوم إذا حفروا فبلغوا المكان الصلب, tr:ecbele'l-kavm, gloss:topluluk kazdı ve sert yere vardı, source:"ج ب ل,B005"}. Dipsiz çukur bunun tersidir: duracak bir kaya yoktur, çünkü dağlar da yün olmuştur. On birinci ayetin hâmiyesi, bir kuyunun duvarını ören ağır taşları da adlandırır: {ar:الحامية الحجارة يطوى بها البئر, tr:el-hâmiye el-hıcâre yutvâ bihe'l-bi'r, gloss:hâmiye, kuyunun onlarla örüldüğü taşlardır, source:"ح م ي,B011"}; {ar:الحوامي عظام الحجارة وثقالها, tr:el-havâmî izâmu'l-hıcâre ve sikâluhâ, gloss:havâmî, taşların iri ve ağır olanlarıdır, source:"ح م ي,B011"}. Bu aile imgesinde çukurun duvarları ağır taştır, içine düşen ise hafif olandır.

Kur'an'da düşüş ve boşluk, bu kökün sahneleridir. Hac suresinde Allah, ona ortak koşanı {ar:فَكَأَنَّمَا خَرَّ مِنَ ٱلسَّمَآءِ فَتَخْطَفُهُ ٱلطَّيْرُ أَوْ تَهْوِى بِهِ ٱلرِّيحُ فِى مَكَانٍۢ سَحِيقٍۢ, tr:fe-ke-ennemâ harra mine's-semâi fe-tahtafuhu't-tayru ev tehvî bihi'r-rîhu fî mekânin sehîk, gloss:sanki gökten düşmüş, kuşlar onu kapıyor ya da rüzgâr onu uzak bir yere savuruyor, source:22:31} diye anlatır. İbrâhîm suresinde zalimler gözlerin donup kaldığı günde {source:14:42} anlatılır: {ar:وَأَفْـِٔدَتُهُمْ هَوَآءٌۭ, tr:ve ef'idetuhum hevâ', gloss:kalpleri bomboştur, source:14:43}. Tâhâ suresinde Allah İsrâiloğullarına {ar:وَمَن يَحْلِلْ عَلَيْهِ غَضَبِى فَقَدْ هَوَىٰ, tr:ve men yahlil aleyhi ğadabî fe-kad hevâ, gloss:kime gazabım inerse o düşmüştür, source:20:81} der; Necm suresinde altüst edilen kentler için {ar:وَٱلْمُؤْتَفِكَةَ أَهْوَىٰ, tr:ve'l-mu'tefikete ehvâ, gloss:altüst olanı da düşürdü, source:53:53} söylenir. Tevbe suresindeki sahne başka bir kökle kurulur ama aynı düşüşü gösterir: bina, çökecek bir yarın kenarına kurulmuştur, {ar:فَٱنْهَارَ بِهِۦ فِى نَارِ جَهَنَّمَ, tr:fe'nhâra bihî fî nâri cehennem, gloss:onunla birlikte cehennem ateşine yıkılıp gitti, source:9:109}. Kâf suresinde dipsizlik bir konuşmaya dönüşür: {ar:يَوْمَ نَقُولُ لِجَهَنَّمَ هَلِ ٱمْتَلَأْتِ وَتَقُولُ هَلْ مِن مَّزِيدٍۢ, tr:yevme nekûlu li-cehenneme heli'mtele'ti ve tekûlu hel min mezîd, gloss:o gün cehenneme "doldun mu" deriz, o da "daha var mı" der, source:50:30}. Nâziât suresinde Allah insanları ayırır, her birine bir sığınak verir: {ar:فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ, tr:fe-inne'l-cahîme hiye'l-me'vâ, gloss:işte cehennem, sığınak odur, source:79:39} ve {ar:فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ, tr:fe-inne'l-cennete hiye'l-me'vâ, gloss:işte cennet, sığınak odur, source:79:41}; ikisinin arasında, cennete gidenin nefsini {ar:وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ, tr:ve nehe'n-nefse ani'l-hevâ, gloss:ve nefsini hevadan alıkoydu, source:79:40} diye anılması, hâviye ile aynı kökü taşır.

O gün insan anası da elinden bırakır. Hac suresinde kıyametin sarsıntısında {ar:تَذْهَلُ كُلُّ مُرْضِعَةٍ عَمَّآ أَرْضَعَتْ, tr:tezhelu kullu murdı'atin ammâ erda'at, gloss:her emziren, emzirdiğini unutur, source:22:2}; Abese suresinde, kulakları sağır eden ses geldiğinde {source:80:33}, {ar:يَوْمَ يَفِرُّ ٱلْمَرْءُ مِنْ أَخِيهِ, tr:yevme yefirru'l-mer'u min ahîh, gloss:kişinin kardeşinden kaçtığı gün, source:80:34}, {ar:وَأُمِّهِۦ وَأَبِيهِ, tr:ve ummihî ve ebîh, gloss:anasından ve babasından, source:80:35}. Mü'minûn suresi bunu, terazi ayetlerinin hemen öncesinde söyler: {ar:فَلَآ أَنسَابَ بَيْنَهُمْ يَوْمَئِذٍۢ وَلَا يَتَسَآءَلُونَ, tr:fe-lâ ensâbe beynehum yevmeizin ve lâ yetesâelûn, gloss:o gün aralarında soy bağı kalmaz, birbirlerini de sormazlar, source:23:101}. Gerçek ana çocuğunu bırakınca, geriye o kişiyi kucaklayan tek ana olarak çukur kalır.

Kaynaklar: 101:9 فَأُمُّهُۥ ء م م B001; 101:9 فَأُمُّهُۥ ء م م B002; 101:9 هَاوِيَةٌ ه و ي B001; 101:9 هَاوِيَةٌ ه و ي B002; 101:7 عِيشَةٍ ع ي ش B001; 101:5 ٱلْجِبَالُ ج ب ل B005; 101:11 حَامِيَةٌ ح م ي B011

## Son kertesine dek kızdırılmış ateş

Son ayet iki kelimedir: {ar:نَارٌ حَامِيَةٌۢ, tr:nârun hâmiye, gloss:kızgın bir ateş, source:101:11}. Nâr, parlayan ve kıpırdayan bir ışıktır: {ar:أصل صحيح يدل على إضاءة واضطراب وقلة ثبات, tr:aslun sahîh yedullu alâ idâetin ve'dtırâbin ve killeti sebât, gloss:ışık saçmayı, kıpırdanmayı ve az durmayı gösteren sağlam bir kök, source:"ن و ر,B001"}; yanan ateş de odur {source:"ن و ر,B002"}. Hâmiye ise bir şeyin sonuna kadar ısıtılmasıdır: demirin ateşte kızdırılması, {ar:أحميت الحديد في النار فهو محمى, tr:ahmeytu'l-hadîde fi'n-nâr, gloss:demiri ateşte kızdırdım, artık o kızgındır, source:"ح م ي,B001"}, fırının en kızgın hali, {ar:حمى النهار وحمي التنور أي اشتد حره, tr:hamiye'n-nehâr ve hamiye't-tennûr, gloss:gün ısındı, tandır kızdı, yani sıcaklığı şiddetlendi, source:"ح م ي,B001"}. Bu sıcaklığın kaynağı olarak ateşin kendisi gösterilir: {ar:الحمي الحرارة المتولدة من الجواهر المحمية كالنار والشمس, tr:el-hamy el-harâratu'l-mutevellide, gloss:hamy, ateş ve güneş gibi kızdırılmış cevherlerden doğan sıcaklıktır, source:"ح م ي,B001"}.

Hâmiye sıfatı, ateşi tek bir anla değil bir süreçle anlatır: ateş zaten sıcaktır, ama bu ateş sıcaklığın sonuna kadar götürülmüştür. Aynı kök öfkenin kabarmasını da anlatır: {ar:عبر عن القوة الغضبية إذا ثارت وكثرت بالحمية, tr:ubbire ani'l-kuvveti'l-ğadabiyye, gloss:öfke gücü kabarıp çoğaldığında hamiyyet diye anlatıldı, source:"ح م ي,B003"}; bir şeyin en keskin, en şiddetli hali de bu köktendir: {ar:حميا الشيء حدته وشدته, tr:humeyyâ'ş-şey', gloss:bir şeyin humeyyâsı, onun keskinliği ve şiddetidir, source:"ح م ي,B008"}. Kökün öbür yönü tersine gider: kimsenin yaklaşamadığı korunmuş şey, {ar:هذا شيء حمى أي محظور لا يقرب, tr:hâzâ şey'un himâ, gloss:bu korunmuş bir şeydir, yasaktır, yaklaşılmaz, source:"ح م ي,B002"}, ve insanların sakındığı şey: {ar:تحاماه الناس أي توقوه واجتنبوه, tr:tehâmâhu'n-nâs, gloss:insanlar ondan sakındı ve uzak durdu, source:"ح م ي,B002"}. Bu son deyimde surenin dördüncü ayetindeki kelime, en-nâs, geçer; insanlar burada ateşten uzak durur, dördüncü ayette ise pervane gibi ona doğru uçarlar.

Kur'an aynı iki kelimeyi başka bir surede de kullanır. Gâşiye suresi {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsu'l-ğâşiye, gloss:her şeyi saran olayın haberi sana geldi mi, source:88:1} diye açılır; o gün bazı yüzler {ar:وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ, tr:vucûhun yevmeizin hâşia, gloss:o gün bazı yüzler zelildir, source:88:2}, {ar:عَامِلَةٌۭ نَّاصِبَةٌۭ, tr:âmiletun nâsıbe, gloss:çalışmış, yorgun düşmüş, source:88:3}, ve {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girerler, source:88:4}. Tevbe suresinde Allah, altını ve gümüşü yığıp harcamayanlara, o hazinenin {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhuhum ve cunûbuhum ve zuhûruhum, gloss:o gün cehennem ateşinde kızdırılıp onlarla alınları, yanları ve sırtları dağlanır, source:9:35} günü haber verir; demirin ateşte kızdırılması burada aynı fiille sahnelenir. Mülk suresinde içine atılanlar ateşin {ar:سَمِعُوا۟ لَهَا شَهِيقًۭا وَهِىَ تَفُورُ, tr:semiû lehâ şehîkan ve hiye tefûr, gloss:onun soluyuşunu işitirler, o kaynar, source:67:7} sesini işitir ve ateş {ar:تَكَادُ تَمَيَّزُ مِنَ ٱلْغَيْظِ, tr:tekâdu temeyyezu mine'l-ğayz, gloss:öfkesinden neredeyse çatlar, source:67:8}; kökün öfke kolu, burada ateşin kendi öfkesi olarak görünür. Furkân suresinde ateş inkârcıları uzaktan görür ve onlar onun öfkeli kükreyişini işitir {source:25:12}. Hümeze suresinin ateşi {ar:ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ, tr:elletî tattali'u ale'l-ef'ide, gloss:yüreklerin üstüne çıkıp onları saran, source:104:7} ateştir ve {ar:إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ, tr:innehâ aleyhim mû'sada, gloss:o, üstlerine kapatılmıştır, source:104:8}.

Kaynaklar: 101:11 نَارٌ ن و ر B001; 101:11 نَارٌ ن و ر B002; 101:11 حَامِيَةٌ ح م ي B001; 101:11 حَامِيَةٌ ح م ي B002; 101:11 حَامِيَةٌ ح م ي B003; 101:11 حَامِيَةٌ ح م ي B008

## Buluşmalar

İmgelerin ilk buluşma yeri dördüncü ve beşinci ayetlerdir. Bir darbe iner ve sıkı olanı dağıtır; bu dağılmanın iki yüzü vardır. Yünün atılması bir dövmedir {source:"ن ف ش,B001"}, dolayısıyla dağların yüne dönmesi, birinci ayetin vuruşunun eseridir. Aynı kelime, menfûş, geceleyin çobansız yayılan sürüyü de anlatır {source:"ن ف ش,B003"}; dağılan dağ ile dağılan sürü tek kelimede birleşir. Dördüncü ayetin ferâşı da hem serili yeri hem saçılan sürüyü taşır; bu iki anlamı bağlayan açıklama, ferşi beşş ile anlatır {source:"ف ر ش,B004"}. Yeryüzünü döşeyen serme işi ile kıyametteki saçılma aynı iki kelimeyle söylenir.

İkinci buluşma, pervane ile terazidir. Pervane hafifliğinden ötürü bu adı almıştır ve savruk adama ferâşe denir {source:"ف ر ش,B005"}; sekizinci ayetin hafifliği de akıl savrukluğudur {source:"خ ف ف,B004"}. Dördüncü ayetin pervane insanları, sekizinci ayetin tartıları hafif gelenleridir. Bu iki imge birlikte surenin hareketini taşır: hafif olan, ışığa doğru savrulur ve ateşe düşer. Pervanenin birbiri ardınca kandile düşüşü {source:"ف ر ش,B005"} ile topluluğun birbiri ardınca çukura düşüşü {source:"ه و ي,B002"} aynı hareketi verir; dokuzuncu ayetin ümm kelimesi hedefe yönelmeyi {source:"ء م م,B012"}, on birinci ayetin ateşi de o hedefin kendisini adlandırır. Böylece dördüncü ayetteki saçılma ile on birinci ayetteki ateş, surenin iki ucunda aynı sahnenin başı ve sonudur. Hâmiye kelimesinin insanların sakındığı korunmuş şeyi anlatan kolu {source:"ح م ي,B002"}, pervanenin yaptığının tersini gösterir.

Üçüncü buluşma, ana ile çukurdur ve bu ikisi yaşayışın karşısında durur. "Anası düştü" deyimi dokuzuncu ayetin iki kelimesini birlikte taşır {source:"ه و ي,B002"}; ümm kelimesinin toplayan, kendine katan anlamı {source:"ء م م,B002"} çukuru, düşeni içine alan yer yapar. Yedinci ayetin yaşayışı ise hayattır {source:"ع ي ش,B001"}; evladını yitirmiş ananın karşısında yaşayan biri. Nâziât suresinin iki sığınağı {source:79:39} {source:79:41} bu karşıtlığı Kur'an'ın kendi sözleriyle kurar.

Dördüncü buluşma çukur ile terazi, ve çukur ile dağlar arasındadır. Hâmiye kuyunun duvarını ören ağır taşlardır {source:"ح م ي,B011"}; içine düşen ise tartısı hafif gelendir. Dağlar en ağır, en kalın kütleydi {source:"ج ب ل,B003"} ve atılmış yünün içi boşluktur {source:"ن ف ش,B002"}; hâviyenin kökü de boşluktur {source:"ه و ي,B001"}. Kazıcıyı durduran kaya {source:"ج ب ل,B005"} yok olunca, çukurun dibi de yoktur. Terazide ağırlık değerse, dağların ağırlığının yüne dönmesi, kıyamet günü dünyanın ağır saydığı şeylerin ağırlıksızlaştığını, tek ağırlığın tartının kefesinde kaldığını gösterir.

Son buluşma, kapı ile ateş arasındadır. Surenin başındaki vuruş üç kez sorulur ve bir sahneyle cevaplanır; onuncu ayetteki soru ise hemen, kızgın bir ateşle cevaplanır. Hümeze suresi aynı soru ile aynı türden cevabı verir {source:104:5} {source:104:6}. Savaş günü imgesi de bu iki ucu birleştirir: başta kılıçların çarpışması {source:"ق ر ع,B002"}, sonda topluluk içinde patlak veren düşmanlık ve kızışan öfke {source:"ن و ر,B007"} {source:"ح م ي,B003"}. Böylece sure bir kapı vuruşuyla, bir uyarıyla açılır ve bir ateşle kapanır; aradaki her kelime, o vuruşun neyi dağıttığını, neyi tarttığını ve hafif olanı nereye düşürdüğünü gösterir.

