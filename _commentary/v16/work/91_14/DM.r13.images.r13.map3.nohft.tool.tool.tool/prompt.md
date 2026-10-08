Focus: 91:14. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/91_14/D.r13/context.md =====
# 91:14 — focus

فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا

Anchor translation (canonical reading, reference only):

Onu yalanlayıp deveyi boğazladılar. Bunun üzerine Rableri, günahları yüzünden üzerlerine yıkım indirdi ve onları yerle bir etti.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَكَذَّبُوهُ | كَذَّبَ | ك ذ ب | REM;V;PRON |
| 2 | فَعَقَرُوهَا | عَقَرَ | ع ق ر | CONJ;V;PRON |
| 3 | فَدَمْدَمَ | دَمْدَمَ | د م د م | CAUS;V |
| 4 | عَلَيْهِمْ | عَلَىٰ |  | P;PRON |
| 5 | رَبُّهُم | رَبّ | ر ب ب | N;PRON |
| 6 | بِذَنۢبِهِمْ | ذَنب | ذ ن ب | P;N;PRON |
| 7 | فَسَوَّىٰهَا | سَوَّىٰ | س و ي | CONJ;V;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 91 — full text (context; no pericope)

- 91:1 وَٱلشَّمْسِ وَضُحَىٰهَا
- 91:2 وَٱلْقَمَرِ إِذَا تَلَىٰهَا
- 91:3 وَٱلنَّهَارِ إِذَا جَلَّىٰهَا
- 91:4 وَٱلَّيْلِ إِذَا يَغْشَىٰهَا
- 91:5 وَٱلسَّمَآءِ وَمَا بَنَىٰهَا
- 91:6 وَٱلْأَرْضِ وَمَا طَحَىٰهَا
- 91:7 وَنَفْسٍۢ وَمَا سَوَّىٰهَا
- 91:8 فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا
- 91:9 قَدْ أَفْلَحَ مَن زَكَّىٰهَا
- 91:10 وَقَدْ خَابَ مَن دَسَّىٰهَا
- 91:11 كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ
- 91:12 إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا
- 91:13 فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا
- 91:14 ◀ focus فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا
- 91:15 وَلَا يَخَافُ عُقْبَٰهَا


===== _commentary/v16/work/91_14/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ك ذ ب (root_001290) — identity root of فَكَذَّبُوهُ (w1)

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

## ع ق ر (root_001035) — identity root of فَعَقَرُوهَا (w2)

- **B001** yaralama ve bedeni zedeleme — yaralama, bedeni zedeleme · yaralı, yaralanmış · insanları yaralayan köpek ya da yırtıcı · sırtı korumayıp yaralayan eyer
  العقر كالجرح (maqayis;ayn)؛ عقره أي جرحه (sihah)؛ سرج معقر وكلب عقور (ayn;maqayis;mufradat)؛ لكل جارح أو عاقر من السباع كلب عقور (tahdhib)
- **B002** hayvanın bacaklarını kesip düşürme — atın bacaklarını kesip düşürmek · devenin arka ayak bağını kesmek, ardından kesmek · develeri bacaklarından kesme yarışı
  عقرت الفرس أي كسعت قوائمه بالسيف (maqayis)؛ عقرت الفرس كشفت قوائمه بالسيف (ayn)؛ عقر البعير كسف عرقوبه ثم جعل النحر عقرا (tahdhib)؛ عقرت البعير أو الفرس بالسيف (sihah)؛ عقرت البعير نحرته (mufradat)
- **B003** sırt hasarıyla ya da korkuyla hareketi kesilme — hayvanın sırtını eyerle yaralamak · beni uzun süre alıkoymak · korkudan donup kalma
  عقرت ظهر الدابة أدبرته (maqayis;ayn;sihah;tahdhib;mufradat)؛ عقرت بي أي أطلت حبسي (maqayis;sihah)؛ العقر داء يأخذ الإنسان عند الروع فلا يقدر أن يبرح وتسلمه رجلاه (maqayis)؛ عقر وبعل وهو مثل الدهش (tahdhib)
- **B004** üreme yetisinden yoksun olma — kısır, çocuk sahibi olamayan · doğurganlıkla ilişkilendirilen boncuk veya rahim hastalığı
  العاقر من النساء وهي التي لا تحمل (maqayis)؛ امرأة عاقر وبها عقر (ayn)؛ العاقر المرأة التي لا تحبل ورجل عاقر أيضا (sihah)؛ امرأة عاقر وقد عقر الرجل مثل المرأة (tahdhib)؛ رجل عاقر وامرأة عاقر لا تلد (mufradat)؛ العقرة خرزة تشدها المرأة لئلا تحبل (sihah;tahdhib)
- **B005** ardından benzeri gelmeyen son örnek — ardından benzeri gelmeyen son yumurta veya tek bağış
  بيضة العقر اسم لآخر بيضة تكون من الدجاجة فلا تبيض بعدها (maqayis)؛ بيضة العقر بيضة الديك (ayn;sihah;tahdhib)؛ بيضة العقر للعطية إذا كانت مرة واحدة (sihah)؛ المرة الأخيرة كانت بيضة العقر (tahdhib)؛ العقر آخر الولد وبيضة العقر كذلك (mufradat)
- **B006** cinsel ihlal karşılığı ödeme — kadına zorla veya yanılgılı ilişki nedeniyle ödenen bedel
  دية فرج المرأة عقر وذلك إذا غصبت (maqayis)؛ العقر دية فرج المرأة إذا غصبت (ayn)؛ العقر مهر المرأة إذا وطئت على شبهة (sihah)؛ العقر للمغتصبة من الإماء كمهر المثل (tahdhib)؛ عقر المرأة مهرها وجمعه أعقار (tahdhib)
- **B007** büyüme noktasını yok ederek gelişimi durdurma — hurma ağacının tepesini veya özünü kesmek · ön kanat tüyleri yeniden çıkmayan kuş
  النخلة تعقر يقطع رأسها فلا يخرج من ساقها شيء (maqayis;ayn)؛ عقرت النخلة إذا قطعت رأسها كله مع الجمار (sihah)؛ عقر النخلة أن يكشط ليفها عن قلبها ويستخرج جمارها (tahdhib)؛ عقرت النخل قطعته من أصله (mufradat)؛ طائر عقر وعاقر (ayn)
- **B008** bedeni veya bilgiyi güçlü biçimde etkileyen şey — ilaç kökleri veya şifalı bitkiler · develeri öldüren ot · bilgiyi yok eden unutma
  كلأ عقار أي يعقر الإبل ويقتلها (maqayis;tahdhib)؛ العقاقير أصول الأدوية واحدها عقار (sihah)؛ العقار والعقاقير كل نبت ينبت مما فيه شفاء (tahdhib)؛ عقرة العلم النسيان (maqayis;sihah;tahdhib)
- **B009** yükseltilmiş ses ve ona bağlı kişi adı — şarkıda, okumada veya ağlamada yükseltilen ses · bacağı kesilmiş veya öldürülmüş seçkin kişi
  رفع عقيرته إذا تغنى أو قرأ (maqayis)؛ عقيرة الرجل صوته إذا غنى أو قرأ أو بكى (ayn)؛ رفع فلان عقيرته أي صوته (sihah)؛ رفع فلان عقيرته يتغنى إذا رفع صوته بالغناء (tahdhib)؛ العقيرة هي الرجل المعقورة (maqayis)؛ ما رأيت كاليوم عقيرة وسط قوم (sihah;maqayis)
- **B010** kalıplaşmış bedensel zarar dileği — gerçekleşmesi amaçlanmayabilen kalıplaşmış kötü dilek · ona zarar gelsin
  عقرا له وجذعا (maqayis)؛ عقرى حلقى (ayn;sihah;tahdhib)؛ عقرها الله أي عقر جسدها (maqayis;tahdhib)؛ هذا على مذهب العرب في الدعاء على الشيء من غير إرادة لوقوعه (tahdhib)
- **B011** karşılıklı sözlü çekişme — karşılıklı övünme, sövüşme ve yergi
  المعاقرة المنافرة والسباب والهجاء (sihah)؛ المعاقرة الملاعنة (tahdhib)؛ عقرت الرجل إذا قلت له عقرى حلقى (maqayis)
- **B012** sarhoş edici içecek ve onu sürekli içme — çabuk sarhoş eden şarap · şarabı sürekli içmek
  العقار الخمر التي لا تلبث أن تسكر (ayn)؛ العقار بالضم الخمر (sihah)؛ العقار اسم للخمر (tahdhib)؛ معاقرة الخمر إدمان شربها (tahdhib;ayn;sihah)؛ عاقره إذا لازمه وداوم عليه (tahdhib;sihah)؛ العقار الخمر لكونه كالعاقر (mufradat)
- **B013** bir şeyin içteki kök ve dayanak bölümü — evin kök bölümü veya topluluğun yerleşim alanı · havuzun arka kısmı ve develerin durma yeri · ateşin közlerinin toplandığı orta bölüm
  العقر أصل كل شيء (maqayis;sihah;tahdhib)؛ عقر الحوض والدار وغيرهما أصلها (mufradat)؛ عقر الدار محلة القوم (maqayis;ayn)؛ عقر الحوض موقف الإبل إذا وردت (maqayis;ayn)؛ عقر النار مجتمع جمرها (maqayis;tahdhib;sihah)
- **B014** iki şey arasındaki açıklık — iki şey arasındaki açıklık
  كل فرجة بين شيئين فهو عقر وعقر (maqayis)؛ كل فرجة تكون بين شيئين هو عقر وعقر لغتان (ayn)؛ كل فرجة تكون بين شيئين فهو عقر وعقر لغتان (tahdhib)
- **B015** topluluğun sığındığı yüksek yapı — köy halkının sığındığı saray veya yüksek yapı
  العقر القصر الذي يكون معتمدا لأهل القرية يلجؤون إليه (maqayis;ayn;tahdhib)؛ العقر كل بناء مرتفع (maqayis;sihah)؛ وقيل للقصر عقرة (mufradat)
- **B016** kalıcı mülk ve korunan seçkin mal — arazi, tarım işletmesi, hurmalık veya ev · evin korunmuş değerli eşyası · bir şeyin en iyi ve seçkin parçası
  العقار ضيعة الرجل والجمع العقارات (maqayis;ayn)؛ العقار الأرض والضياع والنخل (sihah)؛ العقار وهو المنزل والأرض والضياع (tahdhib)؛ عقار البيت متاعه الحسن (tahdhib;sihah)؛ عقار كل شيء خياره (tahdhib)؛ العقار هو المتاع المصون (maqayis)
- **B017** bitki yetiştirmeyen büyük kumluk — bitki yetiştirmeyen büyük kumluk
  العاقر من الرمل ما لا ينبت شيئا (maqayis)؛ العاقر العظيم من الرمل (tahdhib)؛ العاقر من الرمال الرملة التي لا تنبت شيئا (tahdhib)؛ العاقر العظيم من الرمل لا ينبت شيئا (sihah)
- **B018** güneşi örten bulut parçası — güneşi örten veya saraya benzetilen bulut parçası
  العقر غيم ينشأ من قبل العين فيغشى عين الشمس (ayn;tahdhib)؛ العقر غيم ينشأ في عرض السماء (ayn)؛ العقر القطعة من الغمام (tahdhib)؛ ومما شبه بالعقر وهو القصر العقر غيم (maqayis)؛ بعضهم العقر في هذا البيت القصر (tahdhib)
- **B019** kırmızı ve gösterişli kumaş türü — kırmızı kumaş veya binek üstü bölme eşyası
  العقار أيضا ضرب من الثياب أحمر (sihah)؛ عقارا يظل الطير يخطف زهوه (sihah;tahdhib)؛ هو متاع البيت (tahdhib)؛ عقار البيت متاعه الحسن (tahdhib)
- **B020** akrep ve iğneleyici ya da sıkı yapılı olma — akrep · insanları iğneleyip incitmek · sıkı, toplu ve güçlü yapılı
  العقرب معروفة والباء فيه زائدة وإنما هو من العقر؛ يقال للذي يقرص الناس إنه لتدب عقاربه؛ دابة معقرب الخلق أي ملزز مجتمع شديد

## د م د م (root_000486) — identity root of فَدَمْدَمَ (w3)

- **B001** bütünüyle ortadan kaldırma — bütünüyle ortadan kaldırma
  الدَّمْدَمَة: الاستئصال

## ر ب ب (root_000532) — identity root of رَبُّهُم (w5)

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

## ذ ن ب (root_000521) — identity root of بِذَنۢبِهِمْ (w6)

- **B001** günah veya kötü sonuç doğuran suç — günah, suç veya kötü sonuç doğuran davranış · günah ya da suç işlemek
  الذنب والجرم (maqayis)؛ الذنب معروف أذنب يذنب إذنابا (jamhara)؛ الذنب الجرم وقد أذنب الرجل (sihah)؛ الذنب الإثم والمعصية (tahdhib)؛ يستعمل في كل فعل يستوخم عقباه (mufradat)
- **B002** kuyruk; bir şeyin arka ucu veya sonu — hayvan kuyruğu veya bir şeyin arka ucu · kuşun kuyruğu veya kuyruk kökü; at ve devede de kullanılan ad · bir şeyin sonu veya arka ucu · uzun kuyruklu at · başlığından kuyruk gibi bir parçayı aşağı sarkıtmak · çok öne geçip yakalanamaz olmak · geçmiş bir işin ardından gidip kaçırdığına hayıflanmak
  ذنب وهو مؤخر الدواب (maqayis)؛ ذنب الدابة معروف (jamhara)؛ ذنب الطائر وذناباه وذنب الفرس وذناباه (jamhara)؛ الذنب واحد الأذناب والذنابى ذنب الطائر (sihah)؛ ذنب كل شيء آخره (tahdhib)؛ ذنب الدابة وغيرها معروف (mufradat)
- **B003** ardından giden takipçiler — halkın aşağı görülen, geriden gelen takipçileri · birinin veya bir şeyin ardından gelen takipçi · sürünün kuyruğu yanında duran veya izini bırakmadan ardından giden kişi · takipçileriyle birlikte gelmek
  الأتباع الذنابي (maqayis)؛ أذناب الناس رذالهم (jamhara)؛ الذنابى الأتباع والذانب التابع (sihah)؛ ذنب الرجل أتباعه وأذناب القوم أتباع الرؤساء (tahdhib)؛ يعبر به عن المتأخر والرذل (mufradat)
- **B004** su yatağı ve vadinin son kesimi — yamaçlı dere yataklarındaki su akış yolları · vadinin veya nehrin sonu, suyunun ulaştığı yer · iki yamaçlı dere yatağı arasındaki su yolu · su yolu veya çayırlıktan dışarı akan küçük kanal
  المذانب مذانب التلاع وهي مسايل الماء فيها (maqayis)؛ ذنبة الوادي والنهر آخره وذِنابته (jamhara)؛ المذنب مسيل ماء وذنابة الوادي (sihah)؛ ذنب التلعة ومذنب النهر والمذنب كهيئة الجدول (tahdhib)؛ مذانب التلاع لمسائل مياهها (mufradat)
- **B005** hurmanın uçtan başlayarak kısmen olgunlaşması — bir ucundan olgunlaşmaya başlamış hurma · ham hurmanın kuyruk sayılan ucundan olgunlaşmaya başlaması · ucu olgunlaşmaya başlamış ham hurma
  المذنب من الرطب ما أرطب بعضه (maqayis)؛ ذنب البسر وأذنب إذا أرطب مما يلي أقماعه وهو التذنوب (jamhara)؛ التذنوب البسر الذي قد بدأ فيه الإرطاب من قبل ذنبه (sihah)؛ إذا بدت نكت من الإرطاب في البسر من قبل ذنبها قيل قد ذنبت فهي مذنبة (tahdhib)؛ المذنب ما أرطب من قبل ذنبه (mufradat)
- **B006** kişiye düşen pay veya nasip — pay veya nasip, özellikle azaptan düşen pay · eksik bir paya razı olmak
  الثالث كالحظ والنصيب (maqayis)؛ الذنوب في التنزيل هو النصيب (jamhara)؛ الذنوب النصيب (sihah)؛ تذهب به إلى النصيب والحظ (tahdhib)؛ استعير للنصيب (mufradat)
- **B007** kova; özellikle büyük, dolu veya kuyruk ipli olanı — büyük, dolu veya kuyruk ipi bulunan kova
  الذنوب الدلو (jamhara)؛ الذنوب الدلو الملأى ماء (sihah)؛ الذنوب الدلو العظيمة (tahdhib)؛ الدلو التي لها ذنب (mufradat)
- **B008** kepçe — kepçe veya büyük servis kaşığı
  المذانب أيضا المغارف والواحدة مذنب ومذنبة (jamhara)؛ المذنب المغرفة (sihah)؛ المذانب المغارف واحدها مذنبة (tahdhib)
- **B009** tilkikuyruğu da denen bir bitki — tilkikuyruğu da denen bilinen bir bitki
  الذنبان ضرب من النبت (jamhara)؛ الذنبان نبت (sihah)؛ الذنبان نبت معروف الواحدة ذنبانة وبعض العرب تسميه ذنب الثعلب (tahdhib)
- **B010** hayvanın kuyruğa bağlı özel davranışı — çekirgenin yumurtlamak için arka kısmını yere saplaması · kertenkelenin kuyruğu önde geri çıkması veya kuyruğuyla vurması · hayvanın kuyruğa bağlı çiftleşme veya vurma davranışı
  ذنب الجراد إذا غرز ليبيض (jamhara)؛ ذنب الضب إذا خرج بذنبه من جحره موليا (jamhara)؛ التذنيب للضباب والفراش إذا أرادت التعاظل والسفاد (tahdhib)؛ إنما يقال للضب مذنب إذا ضرب بذنبه (tahdhib)

## س و ي (root_000766) — identity root of فَسَوَّىٰهَا (w7)

- **B001** iki şeyi birbirine denk kılma veya denk sayma — bir şeyi ötekinin ölçüsüne ulaştırarak eşitlemek · iki şeyi ölçü, ağırlık, nicelik ya da nitelik bakımından eşitleme · bir işte aynı düzeyde ve eşit durumda · eş, benzer · ikisi de bir, ikisi eşit · özellikle, hele
  أصل يدل على استقامة واعتدال بين شيئين (maqayis)؛ لا يساوي كذا أي لا يعادله (maqayis;sihah;tahdhib)؛ المساواة والاستواء واحد (ayn)؛ السِيّ المثل من قولهم سِيّان أي مثلان (jamhara;maqayis;mufradat)؛ لا سِيّما أي لا مثل ما (maqayis)؛ هذا الثوب يساوي كذا (mufradat)
- **B002** kendi içinde düzgün ve tam duruma gelme — bir şeyi düzeltip düzgün ya da eksiksiz duruma getirmek · eğrilikten kurtulup doğrulmak · yapısı düzgün, eksiksiz ve sağlıklı · çocuklarımız ve hayvanlarımız iyi durumda · düz arazi
  سويت الشيء فاستوى (ayn;sihah)؛ استوى من اعوجاج (sihah;tahdhib)؛ السوي الذي سوى الله خلقه لا دمامة فيه ولا داء (ayn)؛ السوي فعيل في معنى مفتعل أي مستو (tahdhib)؛ السوي يقال فيما يصان عن الإفراط والتفريط (mufradat)؛ أولادنا وماشيتنا سوية صالحة (maqayis;tahdhib)
- **B003** üzerine çıkıp yerleşmek veya egemen olmak [kalıp] — bineğinin sırtına çıkıp yerleşmek · üzerine çıkmak ya da egemen olmak
  استوى على ظهر دابته أي علا واستقر (sihah)؛ استويت فوق الدابة وعلى ظهر الدابة أي علوته (tahdhib)؛ استوى أي استولى وظهر (sihah)؛ متى عدي بعلى اقتضى معنى الاستيلاء (mufradat)
- **B004** bir hedefe yönelip onu amaç edinmek [kalıp] — göğe yönelmek, ona varmak ya da ona yönelik işi düzenlemek
  استوى إلى السماء أي قصد (sihah)؛ استوى علي وإلي يشاتمني على معنى أقبل إلي وعلي (tahdhib)؛ ثم استوى إلى بلد معناه قصد بالاستواء إليه (tahdhib)؛ إذا عدي بإلى اقتضى معنى الانتهاء إليه إما بالذات أو بالتدبير (mufradat)
- **B005** gençlik olgunluğuna erişmek — gençliğinin sonuna erişip gücü ve kavrayışı olgunlaşmak
  استوى الرجل إذا انتهى شبابه (sihah)؛ بلغ أشده واستوى قيل بلغ الأربعين (tahdhib)؛ المستوي هو الذي تم شبابه (tahdhib)؛ فإذا استويت أنت (mufradat)
- **B006** iki yanın ortasında ve ikisine karşı yansız olma — orta; iki yana eşit ve yansız durum · iki yana eşit, ortada ve herkesçe bilinen yer · iki tarafın da hakkını gözeten ortak söz
  السواء ممدود وسط كل شيء (ayn)؛ مكانا سوى أي معلما قد علم القوم به (ayn;maqayis)؛ مكان سوى أي عدل ووسط (sihah)؛ السواء وسط الدار وغيرها (maqayis)؛ سواء بمعنى العدل والنصفة (tahdhib)؛ كلمة سواء أي عدل (tahdhib;mufradat)؛ في سواء الجحيم (maqayis;mufradat)
- **B007** başka ve ayrı olan — başka, öteki
  سوى مقصور إذا كان في موضع غير (ayn)؛ سواء الشيء غيره (sihah;tahdhib)؛ مررت برجل سواك أي غيرك (sihah)؛ هذا سوى ذلك أي غيره (maqayis)؛ يستعمل سوى وسواء بمعنى غير (mufradat)؛ عندي رجل سواك أي مكانك وبدلك (mufradat)
- **B008** birinin yöneldiği hedefe yönelmek [kalıp] — birinin tuttuğu yöne ya da hedefe yönelmek
  يقال قصدت سوى فلان كما يقال قصدت قصده (maqayis)؛ قصدت سوى فلان أي قصدت قصده (sihah)؛ فلأصرفن سوى حذيفة مدحتى (maqayis;sihah)؛ وقع المزار على سواهما أخطأهما (tahdhib)
- **B009** geniş ve açık arazi — geniş, açık ya da pürüzsüz arazi
  السِيّ الفضاء من الأرض الواسع (jamhara)؛ ومن الباب السِيّ الفضاء من الأرض (maqayis)؛ السِيّ موضع بالبادية أملس (ayn)؛ نزلنا في كلاء سِيّ وأنبط ماء سِيًّا أي كثيرا واسعا (tahdhib)
- **B010** devenin sırtına konan dolgulu binme örtüsü — devenin sırtına ya da hörgücü çevresine konan binme örtüsü
  السَّويّة قتب أعجمي للبعير والجميع السوايا (ayn;tahdhib)؛ السَّويّة كساء يلف ويجعل شبيها بالحوية يلقى على سنام البعير (jamhara)؛ السَّويّة كساء محشو بثمام ونحوه كالبرذعة (sihah)؛ كساء محشو بثمام أو ليف يجعل على ظهر البعير (tahdhib)
- **B011** atlayıp dışarıda bırakmak — atlamak, dışarıda bırakmak ve göz ardı etmek
  أسوى فلان حرفا من كتاب الله أي أسقط وأغفل (ayn)؛ أسويت الشيء أي تركته وأغفلته (sihah)؛ أسوى برزخا ثم رجع إليه (tahdhib)؛ أسوى يعني أسقط وأغفل (tahdhib)
- **B012** ayın on üçüncü gecesi — ayın dengeli göründüğü on üçüncü gece
  ليلة السواء ليلة ثلاث عشرة (sihah)؛ السواء ممدود ليلة ثلاث عشرة وفيها يستوي القمر (tahdhib)
- **B013** başına denk mal ve bolluk [kalıp] — başına denk sayılan mal miktarı ya da bolluk
  جاء فلان بسِيّ رأسه من المال أي ما يوازي رأسه (jamhara)؛ وقع فلان في سواء رأسه أي فيما ساوى رأسه من النعمة (tahdhib)؛ هو في سِيّ رأسه وسواء رأسه وهي النعمة (tahdhib)

## ECHO ر ب و (root_000537) — for رَبُّهُم (w5): withheld observed target; not identity

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

===== _commentary/v16/out/s091/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 91:14, and ## Buluşmalar) =====
## Gökte el değiştiren ışık: açılan ve örtülen yüz

Arapçada kelimelerin çoğu üç harfli bir kökten türer. Aynı kökten gelen kelimeler birbirinden çok farklı şeylere ad olabilir, ama aralarında ortak bir sahne taşırlar. Aşağıda bir kelimenin ailesinden getirilen her imge, o kelimenin ayetteki anlamının yanında duyulur. İmge bu anlamın yerine geçmez.

Surenin ilk dört ayeti dört ayrı şeye yemin ediyor gibi görünür: güneş, ay, gündüz, gece. Oysa dört ayetin de sonundaki "-hâ" zamiri hep aynı yere döner, yani güneşe. Birinci ayet güneşi kendi ışığıyla anar: {ar:وَٱلشَّمْسِ وَضُحَىٰهَا, tr:ve'ş-şemsi ve duhâhâ, gloss:güneşe ve kuşluğuna andolsun, source:91:1}. Güneş hem bir disktir hem de o diskten yayılan aydınlık: {ar:الشمس يقال للقرصة وللضوء المنتشر عنها, tr:eş-şemsu yukâlu li'l-kursati ve li'd-dav'i'l-munteşiri anhâ, gloss:güneş hem diske hem de ondan yayılan ışığa denir, source:"ش م س,B001"}. Kuşluk da o ışığın açılıp yayılmasıdır: {ar:الضحى انبساط الشمس وامتداد النهار, tr:ed-duhâ inbisâtu'ş-şemsi ve'mtidâdu'n-nehâr, gloss:kuşluk, güneşin yayılması ve gündüzün uzamasıdır, source:"ض ح و,B001"}. Bu yayılma ölçülü basamaklarla sayılır: {ar:ضحوة النهار بعد طلوع الشمس ثم بعده الضحى ثم بعده الضحاء, tr:dahvetu'n-nehâri ba'de tulû'i'ş-şems, summe ba'dehu'd-duhâ, summe ba'dehu'd-dahâ', gloss:güneş doğduktan sonra önce dahve, sonra duhâ, sonra dahâ gelir, source:"ض ح و,B001"}. Kısacası ilk ayette güneş kendi aydınlığını yayan bir kaynak olarak durur.

İkinci ayet ayı kendi ışığıyla değil, sırasıyla tanımlar: {ar:وَٱلْقَمَرِ إِذَا تَلَىٰهَا, tr:ve'l-kameri izâ telâhâ, gloss:onu izlediğinde aya andolsun, source:91:2}. Fiil bir peşinden gelmeyi anlatır: {ar:تلاه تبعه متابعة, tr:telâhu tebi'ahu mutâba'aten, gloss:onu izledi, ardı sıra peşinden gitti, source:"ت ل و,B001"}. Üçüncü ayette ilişki ters döner: {ar:وَٱلنَّهَارِ إِذَا جَلَّىٰهَا, tr:ve'n-nehâri izâ cellâhâ, gloss:onu açığa çıkardığında gündüze andolsun, source:91:3}. Gündüz, güneşin ışığından başka bir şey değildir: {ar:النهار ضياء ما بين طلوع الفجر إلى غروب الشمس, tr:en-nehâru diyâun mâ beyne tulû'i'l-fecri ilâ gurûbi'ş-şems, gloss:gündüz, tan yerinin ağarmasından güneşin batışına kadarki aydınlıktır, source:"ن ه ر,B002"}. Yine de güneşi görünür kılan, güneşten gelen bu aydınlıktır. Fiilin kökü örtünün kalkıp şeyin ortaya çıkmasını anlatır: {ar:انكشاف الشيء وبروزه, tr:inkişâfu'ş-şey'i ve burûzuhu, gloss:bir şeyin örtüsünün açılması ve ortaya çıkması, source:"ج ل و,B001"}. Arap dili bu ayeti de tam böyle okur: {ar:والنهار إذا جلاها إذا بين الشمس, tr:ve'n-nehâri izâ cellâhâ: izâ beyyene'ş-şemse, gloss:"gündüz onu açığa çıkardığında", yani güneşi belirgin kıldığında, source:"ج ل و,B007"}. Dördüncü ayette gece aynı yüzü kapatır: {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰهَا, tr:ve'l-leyli izâ yağşâhâ, gloss:onu örttüğünde geceye andolsun, source:91:4}. Kökün işi bir şeyi başka bir şeyle kaplamaktır: {ar:أصل صحيح يدل على تغطية شيء بشيء, tr:aslun sahîhun yedullu alâ tağtiyeti şey'in bi-şey', gloss:bir şeyin başka bir şeyle örtülmesini gösteren sağlam bir kök, source:"غ ش و,B001"}.

Düz bir anlatım "güneşe, aya, gündüze ve geceye andolsun" der ve geçer. Fiiller ise tek bir yüzün dört türlü ele alındığını gösterir: yayılır, izlenir, açılır, örtülür. Kur'an bu düzeni başka yerlerde de sahneler. Yâsîn Suresi'nde Allah işaretlerini sayarken hiçbir cismin sırasını bozmadığını söyler: {ar:لَا ٱلشَّمْسُ يَنۢبَغِى لَهَآ أَن تُدْرِكَ ٱلْقَمَرَ وَلَا ٱلَّيْلُ سَابِقُ ٱلنَّهَارِ, tr:le'ş-şemsu yenbağî lehâ en tudrike'l-kamera ve le'l-leylu sâbiku'n-nehâr, gloss:ne güneşin aya yetişmesi yaraşır ne de gece gündüzü geçebilir, source:36:40}. Göklerle yeri altı günde yaratan Rabbi anlatan ayette örtme işi bir kovalamacaya dönüşür: {ar:يُغْشِى ٱلَّيْلَ ٱلنَّهَارَ يَطْلُبُهُۥ حَثِيثًۭا, tr:yuğşi'l-leyle'n-nehâra yatlubuhu hasîsâ, gloss:geceyi, onu hızla kovalayan gündüzün üstüne örter, source:7:54}. Hemen ardından gelen sure aynı çifti iki yeminle açar: {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰ, tr:ve'l-leyli izâ yağşâ, gloss:örttüğünde geceye andolsun, source:92:1} ve {ar:وَٱلنَّهَارِ إِذَا تَجَلَّىٰ, tr:ve'n-nehâri izâ tecellâ, gloss:açılıp parladığında gündüze andolsun, source:92:2}. Nâziât Suresi'nde Allah, dirilişi inkâr edenlere yaratılmalarının mı daha zor olduğunu, yoksa göğün mü olduğunu sorar. Orada kuşluk, gecenin içinden çıkarılan bir şey gibi anlatılır: {ar:وَأَغْطَشَ لَيْلَهَا وَأَخْرَجَ ضُحَىٰهَا, tr:ve ağtaşe leylehâ ve ahrace duhâhâ, gloss:gecesini karanlık kıldı, kuşluğunu çıkardı, source:79:29}.

Bu gök sahnesi dördüncü ayette bitmez. Surenin sonraki kelimeleri aynı gökten anlamlar taşır. Yedinci ayetteki "nefs" kelimesinin kökü sabahın nefes almasını da adlandırır: {ar:تنفس الصبح أي تبلج وتنفس النهار إذا زاد, tr:teneffese's-subhu ey teballece, ve teneffese'n-nehâru izâ zâde, gloss:sabah nefes aldı, yani ağardı; gündüz nefes aldı, yani uzadı, source:"ن ف س,B009"}. Kur'an aynı fiili bir yeminde kullanır: {ar:وَٱلصُّبْحِ إِذَا تَنَفَّسَ, tr:ve's-subhi izâ teneffes, gloss:nefes aldığında sabaha andolsun, source:81:18}. Yine yedinci ayetteki "sevvâhâ" fiilinin ailesinde ayın tamamlandığı gece vardır: {ar:السواء ممدود ليلة ثلاث عشرة وفيها يستوي القمر, tr:es-sevâ'u memdûdun, leyletu selâse aşrate ve fîhâ yestevi'l-kamer, gloss:sevâ', ayın on üçüncü gecesidir; o gece ay dolgunlaşır, source:"س و ي,B012"}. Kur'an da dolunaya yemin eder: {ar:وَٱلْقَمَرِ إِذَا ٱتَّسَقَ, tr:ve'l-kameri izâ't-tesak, gloss:dolunay olduğunda aya andolsun, source:84:18}. Altıncı ayetteki "tahâhâ" fiili de yükselmiş, ışığı yayılmış ayı adlandırır: {ar:القمر الطاحي أي المرتفع والطاحي أيضا المنبسط, tr:el-kameru't-tâhî, eyi'l-murtefi', ve't-tâhî eyzan el-munbesit, gloss:tâhî ay, yükselmiş ay demektir; tâhî yayılmış anlamına da gelir, source:"ط ح و,B008"}. Sekizinci ayetteki "fucûr" kelimesinin kökü şafağın adıdır: {ar:الفجر حمرة الشمس في سواد الليل وهما فجران, tr:el-fecru humretu'ş-şemsi fî sevâdi'l-leyl, ve humâ fecrân, gloss:fecr, gecenin karasındaki güneş kızıllığıdır; iki fecr vardır, source:"ف ج ر,B002"}. Şafak bu adı geceyi yardığı için alır: {ar:قيل للصبح فجر لكونه فجر الليل, tr:kîle li's-subhi fecrun li-kevnihî fecera'l-leyl, gloss:sabaha fecr denmesi, geceyi yarmış olmasındandır, source:"ف ج ر,B002"}. Kur'an Allah'ı bu yarışın sahibi olarak anar: {ar:فَالِقُ ٱلْإِصْبَاحِ, tr:fâliku'l-isbâh, gloss:sabahı yarıp çıkaran, source:6:96}. On beşinci ayetteki "ukbâhâ" kelimesinin ailesinde ise gece ile gündüzün nöbetleşmesi vardır: {ar:الليل والنهار يتعاقبان, tr:el-leylu ve'n-nehâru yeteâkabân, gloss:gece ile gündüz birbirini izler, source:"ع ق ب,B005"}. Kur'an bu nöbeti şöyle anlatır: {ar:جَعَلَ ٱلَّيْلَ وَٱلنَّهَارَ خِلْفَةًۭ, tr:ce'ale'l-leyle ve'n-nehâra hilfeten, gloss:geceyi ve gündüzü birbirinin ardınca gelen kıldı, source:25:62}. Böylece sure, gökte başlayan nöbetin sözcükleri içinde ilerler ve yine bir "ardınca gelme" kelimesiyle kapanır.

Açma ve örtme işi gökte kalmaz. Kuşluk kelimesinin kendisi de açıkta durmayı anlatır: {ar:ضحا الطريق إذا بدا وظهر, tr:dahâ't-tarîku izâ bedâ ve zahara, gloss:yol göründüğünde ve ortaya çıktığında "dahâ" denir, source:"ض ح و,B002"}; {ar:فعل ذلك ضاحية أي ظاهرا بينا, tr:fe'ale zâlike dâhiyeten, ey zâhiren beyyinen, gloss:bunu dâhiye olarak yaptı, yani açıkça, göz önünde yaptı, source:"ض ح و,B002"}. Gecenin örtüsü de kalbe taşınır: {ar:الغشاوة ما غشي القلب من رين الطبع, tr:el-ğışâvetu mâ ğaşiye'l-kalbe min rayni't-tab', gloss:ğışâve, kalbi kaplayan mühür pasıdır, source:"غ ش و,B001"}. Kur'an inkârcılar için aynı kelimeyi kullanır: {ar:وَعَلَىٰٓ أَبْصَٰرِهِمْ غِشَٰوَةٌۭ, tr:ve alâ ebsârihim ğışâvetun, gloss:gözlerinin üstünde bir perde vardır, source:2:7}.

Sekizinci ayette bu iki iş nefsin içine yerleşir: {ar:فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا, tr:fe-elhemehâ fucûrahâ ve takvâhâ, gloss:ona hem yoldan çıkışını hem korunuşunu ilham etti, source:91:8}. Fucûr, şafağın geceyi yardığı kökten gelir. Ama burada yarılan şey karanlık değil, bir perdedir: {ar:الفجور شق ستر الديانة, tr:el-fucûru şakku sitri'd-diyâne, gloss:fucûr, din perdesini yırtmaktır, source:"ف ج ر,B004"}. Gökte yarılma ışık getirir; nefiste ise koruyucu örtüyü parçalar. Takvâ bunun karşısında yerinde tutulan bir örtüdür: {ar:كل ما وقى شيئا فهو وقاء له ووقاية, tr:kullu mâ vakâ şey'en fe-huve vikâun lehu ve vikâye, gloss:bir şeyi koruyan her şey onun için vikâ ve vikâyedir, source:"و ق ي,B001"}. Kökün en somut örneği, dış örtü ile saç arasında duran ince bezdir: {ar:وقاية المرأة وهي الخرقة التي بين جلبابها وشعرها, tr:vikâyetu'l-mer'e, ve hiye'l-hırkatu'lletî beyne cilbâbihâ ve şa'rihâ, gloss:kadının vikâyesi, cilbabı ile saçı arasındaki bez parçasıdır, source:"و ق ي,B001"}. Böylece surede iki tür örtü ve iki tür açılış belirir. Gecenin örtüsü düzenin parçasıdır, takvânın örtüsü korur. Gündüzün açması gösterir, fucûrun açması yırtar.

Dokuzuncu ve onuncu ayetler bu çifti nefsin kaderine bağlar: {ar:قَدْ أَفْلَحَ مَن زَكَّىٰهَا, tr:kad efleha men zekkâhâ, gloss:onu arındırıp büyüten kurtuluşa ermiştir, source:91:9}; {ar:وَقَدْ خَابَ مَن دَسَّىٰهَا, tr:ve kad hâbe men dessâhâ, gloss:onu gömüp gizleyen eli boş kalmıştır, source:91:10}. İkinci fiil gizlemektir: {ar:دساها أي أخفاها, tr:dessâhâ, ey ahfâhâ, gloss:dessâhâ, onu gizledi demektir, source:"د س و,B001"}. Gizleme burada kişinin kendine yöneliktir: {ar:دس فلان نفسه إذا أخفاها وأخملها, tr:dessâ fulânun nefsehu izâ ahfâhâ ve ahmelehâ, gloss:biri kendini gizleyip adını sönük bıraktığında bu fiil kullanılır, source:"د س و,B001"}. Fiil açıkça büyütmenin karşıtı olarak tanımlanır: {ar:وهو نقيض زكا يزكو زكاء وزكاة وهو داس لا زاك, tr:ve huve nakîdu zekâ yezkû zekâen ve zekâten, ve huve dâsin lâ zâk, gloss:bu, "zekâ" fiilinin zıddıdır; o kişi büyüyen değil, gizlenendir, source:"د س و,B002"}. Arap dilinde bu fiil, harflerden biri dönüşmüş bir "dessese" olarak da açıklanır: {ar:دسّسها, tr:dessesehâ, gloss:onu gömdü, toprağa itip gizledi, source:"memory"}. Bu, iki kökün aynı olduğunu göstermez. Yalnızca bir türeyiş yolunu gösterir. Kur'an, iki harfli bu ikinci kökün fiilini bir saklanma sahnesinde kullanır. Allah, kendisine kız çocuğu müjdelenen ve yüzü kararan bir babayı anlatır. Bu adam halktan gizlenir, {ar:يَتَوَٰرَىٰ مِنَ ٱلْقَوْمِ, tr:yetevârâ mine'l-kavm, gloss:halktan saklanır, source:16:59}, ve kendine sorar: {ar:أَمْ يَدُسُّهُۥ فِى ٱلتُّرَابِ, tr:em yedussuhû fi't-turâb, gloss:yoksa onu toprağa mı gömsün, source:16:59}. Kişinin kendini saklaması ile başkasını toprağa itmesi orada tek bir sahnede birleşir. Onuncu ayetteki nefis de böylece güneşin tersine götürülür: açıktan kuytuya, görünürden gömülüye.

Semûd'a gelince açılan şey bir işaret, kapanan şey de bir azaptır. Allah, Semûd'a verdiği dişi deveyi gözleri açan bir işaret olarak anar: {ar:وَءَاتَيْنَا ثَمُودَ ٱلنَّاقَةَ مُبْصِرَةًۭ, tr:ve âteynâ Semûde'n-nâkate mubsıraten, gloss:Semûd'a göz açan bir işaret olarak dişi deveyi verdik, source:17:59}. Onlar ise gündüzün değil gecenin tarafını seçtiler: {ar:فَٱسْتَحَبُّوا۟ ٱلْعَمَىٰ عَلَى ٱلْهُدَىٰ, tr:fe'stehabbu'l-amâ ale'l-hudâ, gloss:körlüğü doğru yola tercih ettiler, source:41:17}. Gecenin fiili bir halkın üstüne serilen cezanın da fiilidir: {ar:غاشية من عذاب الله أي عقوبة مجللة تعمهم, tr:ğâşiyetun min azâbi'llâh, ey ukûbetun mucellilatun teummuhum, gloss:Allah'ın azabından bir ğâşiye, yani onları baştan başa kaplayıp hepsini saran bir ceza, source:"غ ش و,B002"}. Kur'an kendini güvende sananlara aynı kelimeyle seslenir: {ar:أَن تَأْتِيَهُمْ غَٰشِيَةٌۭ مِّنْ عَذَابِ ٱللَّهِ, tr:en te'tiyehum ğâşiyetun min azâbi'llâh, gloss:Allah'ın azabından onları kaplayacak bir şeyin gelmesinden, source:12:107}. Necm Suresi'nde Allah helak ettiği toplulukları sayar: {ar:وَثَمُودَا۟ فَمَآ أَبْقَىٰ, tr:ve Semûde fe-mâ ebkâ, gloss:Semûd'u da geride hiçbir şey bırakmadı, source:53:51}. Aynı dizinin sonunda tersyüz edilmiş şehir için yine örtme fiili gelir: {ar:فَغَشَّىٰهَا مَا غَشَّىٰ, tr:fe-ğaşşâhâ mâ ğaşşâ, gloss:onu örten örttü, source:53:54}. On dördüncü ayetteki "demdeme aleyhim" sözü dilde yok etmeyi anlatır: {ar:الدَّمْدَمَة: الاستئصال, tr:ed-demdeme: el-isti'sâl, gloss:demdeme, kökünden kazımaktır, source:"د م د م,B001"}. Arap dili aynı fiili "üstlerine kapattı" diye de açıklar: {ar:أطبق عليهم, tr:etbaka aleyhim, gloss:üstlerine kapandı, source:"memory"}. Suçun fiili bile örtü taşır. Devenin ayaklarını kesmek anlamındaki "akr" kelimesi, güneşin gözünü örten bir bulutun da adıdır: {ar:العقر غيم ينشأ من قبل العين فيغشى عين الشمس, tr:el-ukru ğaymun yenşe'u min kıbeli'l-ayn, fe-yağşâ ayne'ş-şems, gloss:ukr, ufkun bir yönünden yükselip güneşin gözünü örten buluttur, source:"ع ق ر,B018"}.

Kaynaklar: 91:1 ٱلشَّمْسِ ش م س B001; 91:1 ضُحَىٰهَا ض ح و B001; 91:1 ضُحَىٰهَا ض ح و B002; 91:2 تَلَىٰهَا ت ل و B001; 91:3 ٱلنَّهَارِ ن ه ر B002; 91:3 جَلَّىٰهَا ج ل و B001; 91:3 جَلَّىٰهَا ج ل و B007; 91:4 يَغْشَىٰهَا غ ش و B001; 91:4 يَغْشَىٰهَا غ ش و B002; 91:6 طَحَىٰهَا ط ح و B008; 91:7 نَفْسٍۢ ن ف س B009; 91:7 سَوَّىٰهَا س و ي B012; 91:8 فُجُورَهَا ف ج ر B002; 91:8 فُجُورَهَا ف ج ر B004; 91:8 تَقْوَىٰهَا و ق ي B001; 91:10 دَسَّىٰهَا د س و B001; 91:10 دَسَّىٰهَا د س و B002; 91:14 فَدَمْدَمَ د م د م B001; 91:14 فَعَقَرُوهَا ع ق ر B018; 91:15 عُقْبَٰهَا ع ق ب B005

## Düzlenen: dengelenmiş nefis, yere serilen kavim

Aynı fiil surede iki kez geçer. Yedinci ayette "sevvâhâ" bir nefsi düzgün bir biçime getirir. On dördüncü ayette "fe-sevvâhâ" bir kavmi yerle bir eder: {ar:فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا, tr:fe-kezzebûhu fe-akarûhâ fe-demdeme aleyhim rabbuhum bi-zenbihim fe-sevvâhâ, gloss:onu yalanladılar ve deveyi ayaklarından kestiler; Rableri de günahları yüzünden üstlerine yıkım indirdi ve onu dümdüz etti, source:91:14}. Kökün bir kolu geniş, düz araziyi adlandırır: {ar:السِيّ الفضاء من الأرض الواسع, tr:es-siyyu'l-fadâu mine'l-ardi'l-vâsi', gloss:siyy, geniş, açık düzlüktür, source:"س و ي,B009"}. Bir başka kolu ise eşitliği: {ar:السِيّ المثل من قولهم سِيّان أي مثلان, tr:es-siyyu'l-mislu, min kavlihim siyyân, ey meslân, gloss:siyy, denk demektir; "siyyân", yani iki eş sözünden, source:"س و ي,B001"}. Birinci anlamda kavim düz bir yer gibi serilir. İkincisinde hiçbiri ayrı tutulmaz, hepsi bir olur.

Altıncı ayetteki yayılmış yer, bu düzlenmenin önceden kurulmuş biçimidir. "Tahâ" fiili yaymanın yanında vurulup yere uzanmayı da anlatır: {ar:ضربه ضربة طحا منها أي امتد, tr:darabehû darbeten tahâ minhâ, ey imtedde, gloss:ona bir darbe vurdu, adam o darbeyle yere serildi, yani boylu boyunca uzandı, source:"ط ح و,B006"}. Yere yapışıp kalan bir deve de bu fiille anılır: {ar:وطحى البعير إلى الأرض أي لزق بها, tr:ve tahâ'l-ba'îru ile'l-ard, ey lezika bihâ, gloss:deve yere tahâ etti, yani yere yapıştı, source:"ط ح و,B006"}. Fiil helak olmayı da adlandırır: {ar:طحا إذا هلك, tr:tahâ izâ heleke, gloss:helak olduğunda "tahâ" denir, source:"ط ح و,B007"}. Yerin kendi kökünde ise yere doğru ağırlaşıp çökmek vardır: {ar:التأرض أيضا التثاقل إلى الأرض, tr:et-te'arrudu eyzan et-tesâkulu ile'l-ard, gloss:te'arrud, yere doğru ağırlaşıp çökmek anlamına da gelir, source:"ء ر ض,B006"}. Arada iki devirme olur. Birincisi devenindir: {ar:عقرت الفرس أي كسعت قوائمه بالسيف, tr:akartu'l-ferese, ey kese'tu kavâimehû bi's-seyf, gloss:atı akr ettim, yani ayaklarını kılıçla biçtim, source:"ع ق ر,B002"}. İkincisi kavmindir ve kökten kazımadır: {ar:الدَّمْدَمَة: الاستئصال, tr:ed-demdeme: el-isti'sâl, gloss:demdeme, kökünden kazımaktır, source:"د م د م,B001"}.

Kur'an bu düzlenmeyi Semûd için yerinde gösterir. Salih kavmine şunu hatırlatır: {ar:تَتَّخِذُونَ مِن سُهُولِهَا قُصُورًۭا وَتَنْحِتُونَ ٱلْجِبَالَ بُيُوتًۭا, tr:tettehızûne min suhûlihâ kusûran ve tenhitûne'l-cibâle buyûtâ, gloss:ovalarında saraylar ediniyor, dağları oyup evler yapıyorsunuz, source:7:74}. Bina kökü bu sarayları da adlandırır: {ar:بنى فلان بيتا من البنيان وبنى قصورا, tr:benâ fulânun beyten mine'l-bunyân ve benâ kusûran, gloss:falan bina olarak bir ev kurdu, saraylar kurdu, source:"ب ن ي,B001"}. "Tahâ" kökü de bu ovaların adıdır: {ar:والطحا المنبسط من الأرض, tr:ve't-tahâ el-munbesitu mine'l-ard, gloss:tahâ, yerin yayvan düzlüğüdür, source:"ط ح و,B001"}. Suçun fiili "akr", bir köyün sığındığı yüksek binanın da adıdır: {ar:العقر القصر الذي يكون معتمدا لأهل القرية يلجؤون إليه, tr:el-ukru'l-kasru'llezî yekûnu mu'temeden li-ehli'l-karye, yelce'ûne ileyh, gloss:ukr, köy halkının dayandığı ve sığındığı saraydır, source:"ع ق ر,B015"}. Daha genel olarak da: {ar:العقر كل بناء مرتفع, tr:el-ukru kullu binâin murtefi', gloss:ukr, yükseltilmiş her yapıdır, source:"ع ق ر,B015"}. Yurdun ortası da bu kökle anılır: {ar:عقر الدار محلة القوم, tr:ukru'd-dâri mahalletu'l-kavm, gloss:yurdun ortası, kavmin oturduğu yerdir, source:"ع ق ر,B013"}. Kur'an, Semûd'un kayaları oyan bir halk olduğunu söyler: {ar:وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ, tr:ve Semûde'llezîne câbu's-sahra bi'l-vâd, gloss:vadide kayaları oyan Semûd, source:89:9}. Hicr halkı da bu evlerde kendini güvende sanmıştır: {ar:وَكَانُوا۟ يَنْحِتُونَ مِنَ ٱلْجِبَالِ بُيُوتًا ءَامِنِينَ, tr:ve kânû yenhitûne mine'l-cibâli buyûten âminîn, gloss:dağlardan güven içinde evler oyuyorlardı, source:15:82}.

Bu yapıların sonu düzlenmedir. Allah Semûd'un hikâyesini şöyle bitirir: {ar:فَأَصْبَحُوا۟ فِى دَارِهِمْ جَٰثِمِينَ, tr:fe-asbahû fî dârihim câsimîn, gloss:yurtlarında diz üstü çökmüş halde sabahladılar, source:7:78}; {ar:كَأَن لَّمْ يَغْنَوْا۟ فِيهَآ, tr:ke-en lem yağnev fîhâ, gloss:sanki orada hiç oturmamışlardı, source:11:68}. Bir başka anlatımda kuru ot gibi ezilirler: {ar:فَكَانُوا۟ كَهَشِيمِ ٱلْمُحْتَظِرِ, tr:fe-kânû ke-heşîmi'l-muhtezır, gloss:ağıl yapanın çiğnenmiş kuru otu gibi oldular, source:54:31}. Bir yerde de ayağa kalkamazlar: {ar:فَمَا ٱسْتَطَٰعُوا۟ مِن قِيَامٍۢ, tr:fe-mâ'steta'û min kıyâm, gloss:ayağa kalkmaya güçleri yetmedi, source:51:45}. Evleri boş kalır, yıkılır: {ar:فَتِلْكَ بُيُوتُهُمْ خَاوِيَةًۢ بِمَا ظَلَمُوٓا۟, tr:fe-tilke buyûtuhum hâviyeten bimâ zalemû, gloss:işte zulümleri yüzünden çökmüş, boş kalmış evleri, source:27:52}. Kur'an düzlemeyi dağlar için de sahneler. Kıyamette dağlar savrulur ve yer şöyle olur: {ar:فَيَذَرُهَا قَاعًۭا صَفْصَفًۭا, tr:fe-yezeruhâ kâ'an safsafâ, gloss:onları dümdüz bir alan olarak bırakır, source:20:106}; {ar:لَّا تَرَىٰ فِيهَا عِوَجًۭا وَلَآ أَمْتًۭا, tr:lâ terâ fîhâ ivecen ve lâ emtâ, gloss:orada ne bir eğrilik ne bir tümsek görürsün, source:20:107}. Aynı gün inkârcılar kendi üstlerine düzlenmeyi isterler: {ar:لَوْ تُسَوَّىٰ بِهِمُ ٱلْأَرْضُ, tr:lev tusevvâ bihimu'l-ard, gloss:keşke yer üstlerine düzlenseydi, source:4:42}. Fiil burada sevvâ fiilinin kendisidir.

Fiilin iki yüzü aynı kudrete aittir. Diriltmeyi inkâr edene Allah şunu söyler: {ar:بَلَىٰ قَٰدِرِينَ عَلَىٰٓ أَن نُّسَوِّىَ بَنَانَهُۥ, tr:belâ kâdirîne alâ en nusevviye benâneh, gloss:evet, parmak uçlarını bile yeniden düzenlemeye gücümüz yeter, source:75:4}. Ufacık bir şekli inceden inceye işleyen fiil, bir kavmi yere serer. Düz bir anlatım yalnızca "yok etti" der. Fiilin tekrarı ise yedinci ayetteki biçim verme ile on dördüncü ayetteki dümdüz etmeyi aynı elin iki işi olarak yan yana koyar. Ovaya saray, dağa ev kuran kavim, yaydığı yer kadar düz kalır.

Kaynaklar: 91:7 سَوَّىٰهَا س و ي B002; 91:14 فَسَوَّىٰهَا س و ي B009; 91:14 فَسَوَّىٰهَا س و ي B001; 91:6 طَحَىٰهَا ط ح و B001; 91:6 طَحَىٰهَا ط ح و B006; 91:6 طَحَىٰهَا ط ح و B007; 91:6 ٱلْأَرْضِ ء ر ض B006; 91:5 بَنَىٰهَا ب ن ي B001; 91:14 فَعَقَرُوهَا ع ق ر B002; 91:14 فَعَقَرُوهَا ع ق ر B013; 91:14 فَعَقَرُوهَا ع ق ر B015; 91:14 فَدَمْدَمَ د م د م B001

## Tarla: yarılan, sulanan, büyüyen toprak ve hiçbir şey bitirmeyen kum

Altıncı ayette yayılan yerin ailesinde verimli toprak vardır. Bu toprak dokuzuncu ayetin fiiliyle anılır: {ar:أرض أريضة أي زكية, tr:ardun erîdatun, ey zekiyye, gloss:erîde bir toprak, yani bereketle büyüyen toprak, source:"ء ر ض,B002"}. Bitkinin toprakta kök salıp çoğalması da yerin kökünden bir fiildir: {ar:تأرض النبت تمكن على الأرض فكثر, tr:te'arrada'n-nebtu: temekkene ale'l-ardı fe-kesura, gloss:bitki yere tutundu ve çoğaldı, source:"ء ر ض,B002"}. "Tahâ" fiili de toprağın yüzüne yayılmış bitkiyi anlatır: {ar:والبقلة المطحية النابتة على وجه الأرض قد افترشتها, tr:ve'l-baklatu'l-mathiyyetu en-nâbitetu alâ vechi'l-ard, kad efteraşethâ, gloss:yerin yüzünde biten ve onu döşek gibi kaplayan yayvan sebze, source:"ط ح و,B006"}. Göğün adı ise yağmurun da bitkinin de adıdır: {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tusemmi's-sehâbe semâen ve'l-matara semâ', gloss:Araplar buluta da yağmura da semâ der, source:"س م و,B004"}; {ar:سمي النبات سماء, tr:summiye'n-nebâtu semâ', gloss:bitkiye de semâ denmiştir, source:"س م و,B004"}. Bu adlarla beşinci ve altıncı ayetlerdeki ev bir tarlaya dönüşür. Tavandan su iner, döşeme yeşerir.

Tarlanın işlemesi suyun yolunu açmakla başlar. Üçüncü ayetteki gündüz kelimesi, toprağı yaran ırmakla aynı köktendir: {ar:سمي النهر لأنه ينهر الأرض أي يشقها, tr:summiye'n-nehru li-ennehû yenheru'l-ard, ey yeşukkuhâ, gloss:ırmağa nehr denmesi, toprağı yarmasındandır, source:"ن ه ر,B001"}. Sekizinci ayetteki fucûrun kökü suyun açıldığı yeri adlandırır: {ar:الفجرة موضع تفتح الماء, tr:el-fecretu mevdı'u tefettuhi'l-mâ', gloss:fecre, suyun açılıp aktığı yerdir, source:"ف ج ر,B001"}. Dokuzuncu ayetteki "efleha" fiili saban işidir: {ar:فلحت الأرض شققتها, tr:felahtu'l-arda: şakaktuhâ, gloss:toprağı sürdüm, yani yardım, source:"ف ل ح,B001"}. Çiftçinin adı da buradan gelir: {ar:سمي الأكار فلاحا لأنه يشق الأرض, tr:summiye'l-ekkâru fellâhan li-ennehû yeşukku'l-ard, gloss:çiftçiye fellâh denmesi, toprağı yarmasındandır, source:"ف ل ح,B003"}. Aynı ayetteki "zekkâhâ" ekinin büyümesidir: {ar:زكا الزرع يزكو زكاء ممدود أي نما, tr:zekâ'z-zer'u yezkû zekâen, ey nemâ, gloss:ekin zekâ etti, yani büyüdü, source:"ز ك و,B001"}; {ar:أصل الزكاة النمو الحاصل عن بركة الله تعالى, tr:aslu'z-zekâti'n-nemuvvu'l-hâsılu an bereketi'llâhi teâlâ, gloss:zekâtın aslı, Allah'ın bereketinden gelen büyümedir, source:"ز ك و,B001"}. On üçüncü ayetteki "sukyâ" bir tarlanın sudaki payıdır: {ar:كم سقى أرضك أي حظها من الشرب, tr:kem sakyu ardık, ey hazzuhâ mine'ş-şirb, gloss:toprağının sakyı ne kadar, yani su payı ne kadar, source:"س ق ي,B003"}. On dördüncü ayetteki "zenb" kelimesinin ailesinde yamaçlardaki su yolları vardır: {ar:المذانب مذانب التلاع وهي مسايل الماء فيها, tr:el-mezânibu mezânibu't-tilâ', ve hiye mesâyilu'l-mâi fîhâ, gloss:mezânib, yamaçlardaki su yataklarıdır, source:"ذ ن ب,B004"}. Aynı ayetteki "Rab" kelimesinin ailesinde ise bitkiyi besleyen bulut vardır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb: es-sehâb, summiye bi-zâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur; bitkiyi beslediği için bu adı almıştır, source:"ر ب ب,B008"}. Kökün temel işi de budur: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi adım adım olgunluğa erdirmektir, source:"ر ب ب,B002"}.

Tarlanın tersi de surenin kelimelerinde durur. Onuncu ayetteki fiil, Arap dilinin açıkladığı türeyişle "dessese"ye götürür: toprağa itip gömmek. Kur'an'daki karşılığı, yukarıda anılan, toprağa gömme sahnesidir: {ar:أَمْ يَدُسُّهُۥ فِى ٱلتُّرَابِ, tr:em yedussuhû fi't-turâb, gloss:yoksa onu toprağa mı gömsün, source:16:59}. Çok derine itilen tohum filizlenmez. Fiil de büyümenin tam zıddı olarak tanımlanır: {ar:وهو نقيض زكا يزكو زكاء وزكاة وهو داس لا زاك, tr:ve huve nakîdu zekâ yezkû zekâen ve zekâten, ve huve dâsin lâ zâk, gloss:bu, büyümenin zıddıdır; o gömen biridir, büyüten değil, source:"د س و,B002"}. On dördüncü ayetteki suç fiili "akr", hiçbir şey bitirmeyen kumun adıdır: {ar:العاقر من الرمل ما لا ينبت شيئا, tr:el-âkiru mine'r-ramli mâ lâ yunbitu şey'â, gloss:âkir kum, hiçbir şey bitirmeyen kumdur, source:"ع ق ر,B017"}. Aynı fiil hurmanın büyüme noktasını kesip atmayı da anlatır: {ar:عقرت النخلة إذا قطعت رأسها كله مع الجمار, tr:ukırati'n-nahletu izâ kutı'a ra'suhâ kulluhû ma'a'l-cumâr, gloss:hurmanın başı, özüyle birlikte tümden kesilince "ukırat" denir, source:"ع ق ر,B007"}.

Kur'an bu tarlayı açıkça sahneler. Abese Suresi'nde Allah insana yemeğine bakmasını söyler: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:fe'l-yenzuri'l-insânu ilâ taâmih, gloss:insan yemeğine bir baksın, source:80:24}. Ardından üç adım sayılır: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:suyu bol bol döktük, source:80:25}; {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:summe şakakne'l-arda şakkâ, gloss:sonra toprağı yardıkça yardık, source:80:26}; {ar:فَأَنۢبَتْنَا فِيهَا حَبًّۭا, tr:fe-enbetnâ fîhâ habbâ, gloss:orada tane bitirdik, source:80:27}. Dökmek, yarmak, bitirmek: dokuzuncu ayetteki sürme ve büyümenin adımları bunlardır. Nûh kavmine insanın kendisini bir bitki gibi anlatır: {ar:وَٱللَّهُ أَنۢبَتَكُم مِّنَ ٱلْأَرْضِ نَبَاتًۭا, tr:va'llâhu enbetekum mine'l-ardı nebâtâ, gloss:Allah sizi yerden bir bitki gibi bitirdi, source:71:17}. Bu yüzden nefsin büyütülmesi bir tarlanın büyümesiyle aynı işi görür. Kur'an iki toprağı yan yana koyar: {ar:وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ, tr:ve'l-beledu't-tayyibu yahrucu nebâtuhû bi-izni rabbih, gloss:iyi toprağın bitkisi Rabbinin izniyle çıkar, source:7:58}; {ar:وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًۭا, tr:ve'llezî habuse lâ yahrucu illâ nekidâ, gloss:kötü topraktan ise ancak cılız bir şey çıkar, source:7:58}. Mallarını harcayanlar için de iki örnek verir. Biri tepedeki bahçedir: {ar:كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ, tr:ke-meseli cennetin bi-rabvetin esâbehâ vâbilun fe-âtet ukulehâ dı'feyn, gloss:tepedeki bir bahçe gibi; sağanak ona isabet edince ürününü iki kat verir, source:2:265}. Öteki üzerinde biraz toprak olan kayadır: {ar:كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا, tr:ke-meseli safvânin aleyhi turâbun fe-esâbehû vâbilun fe-terakehû saldâ, gloss:üstünde toprak bulunan düz bir kaya gibi; sağanak onu çıplak bırakır, source:2:264}. Aynı yağmur bir yerde büyütür, öteki yerde altındaki kayayı ortaya çıkarır.

Semûd da bir tarla halkıdır. Salih onlara bunu hatırlatır: {ar:هُوَ أَنشَأَكُم مِّنَ ٱلْأَرْضِ وَٱسْتَعْمَرَكُمْ فِيهَا, tr:huve enşeekum mine'l-ardı ve'ste'marakum fîhâ, gloss:sizi yerden O yetiştirdi ve sizi orada imar ettirdi, source:11:61}. Onlar bahçelerin ve kaynakların içindedir: {ar:فِى جَنَّٰتٍۢ وَعُيُونٍۢ, tr:fî cennâtin ve uyûn, gloss:bahçeler ve pınarlar içinde, source:26:147}; {ar:وَزُرُوعٍۢ وَنَخْلٍۢ طَلْعُهَا هَضِيمٌۭ, tr:ve zurû'in ve nahlin tal'uhâ hedîm, gloss:ekinler ve tomurcukları yumuşacık hurmalar içinde, source:26:148}. Hurmalık içinde yaşayan bir kavmin suç fiili, hurmanın başını kesip atan fiille aynıdır. Kur'an büyümenin karşılığını da su yollarıyla anlatır: {ar:وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ, tr:ve zâlike cezâu men tezekkâ, gloss:işte bu, arınıp büyüyenin karşılığıdır, source:20:76}. Bu söz, Firavun'un tehdidi karşısında iman eden sihirbazların ağzındadır ve altından ırmaklar akan bahçeleri anlatır. Kalbin taşa dönmesi bile bu dille anlatılır: {ar:وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ, tr:ve inne mine'l-hicârati lemâ yetefecceru minhu'l-enhâr, gloss:taşların öylesi vardır ki içinden ırmaklar fışkırır, source:2:74}. Bu sözler İsrailoğullarına, kalpleri bu taşlardan da katı olduğu için söylenir. Düz bir anlatım dokuzuncu ve onuncu ayeti "nefsini arındıran" ve "nefsini kirleten" diye geçer. Fiillerin ailesi ise iki tarlayı gösterir: biri sürülmüş, sulanmış ve yeşermiş; öbürü gömülmüş ya da kum.

Kaynaklar: 91:3 ٱلنَّهَارِ ن ه ر B001; 91:5 ٱلسَّمَآءِ س م و B004; 91:6 ٱلْأَرْضِ ء ر ض B002; 91:6 طَحَىٰهَا ط ح و B006; 91:8 فُجُورَهَا ف ج ر B001; 91:9 أَفْلَحَ ف ل ح B001; 91:9 أَفْلَحَ ف ل ح B003; 91:9 زَكَّىٰهَا ز ك و B001; 91:10 دَسَّىٰهَا د س و B002; 91:13 وَسُقْيَٰهَا س ق ي B003; 91:14 بِذَنۢبِهِمْ ذ ن ب B004; 91:14 رَبُّهُم ر ب ب B002; 91:14 رَبُّهُم ر ب ب B008; 91:14 فَعَقَرُوهَا ع ق ر B007; 91:14 فَعَقَرُوهَا ع ق ر B017

## Yutulan, içilen, payına düşen

Sekizinci ayetteki "elhemehâ" fiilinin ailesinde yutmak vardır: {ar:لهمت الشيء وقلما يقال إلا التهمت وهو ابتلاعه بمرة, tr:lehimtu'ş-şey'e, ve kallemâ yukâlu illâ iltehemtu, ve huve'btilâ'uhû bi-merre, gloss:bir şeyi lehimtu, ya da daha çok denildiği gibi iltehemtu: onu bir lokmada yuttum, source:"ل ه م,B001"}. Bunun en somut örneği emzikteki yavrudur: {ar:التهم الفصيل ما في ضرع أمه استوفاه, tr:iltehemel-fasîlu mâ fî dar'ı ummihî: istevfâh, gloss:sütten kesilmemiş yavru, annesinin memesindekini sonuna kadar emip tüketti, source:"ل ه م,B001"}. İlham bu yutuşun içe dönük biçimidir: {ar:الإلهام كأنه شيء ألقى في الروع فالتهمه, tr:el-ilhâmu ke-ennehû şey'un ulkıye fi'r-rav' fe'ltehemeh, gloss:ilham, gönle atılan ve gönlün yutuverdiği bir şey gibidir, source:"ل ه م,B002"}. Bu atış Allah'tan gelir: {ar:الإلهام إلقاء الشيء في الروع ويختص بما كان من جهة الله تعالى, tr:el-ilhâmu ilkâu'ş-şey'i fi'r-rav', ve yahtessu bimâ kâne min cihetillâhi teâlâ, gloss:ilham, bir şeyin gönle atılmasıdır ve Allah tarafından gelene mahsustur, source:"ل ه م,B002"}. Böylece ayet nefse iki lokma verir: fucûrunu ve takvâsını. Nefis ikisini de kendi içine alır.

Yedinci ayetteki "nefs" kelimesi de içmeye yakındır. Kök bir yudumu adlandırır: {ar:كرع في الإناء نفسا أو نفسين, tr:kera'a fi'l-inâi nefesen ev nefeseyn, gloss:kaptan bir ya da iki yudum içti, source:"ن ف س,B006"}. Suyun kendisini de: {ar:يقال للماء نفس ولأن قوام النفس به, tr:yukâlu li'l-mâi nefs, ve li-enne kıvâme'n-nefsi bih, gloss:suya da nefs denir, çünkü nefsin ayakta durması onunladır, source:"ن ف س,B008"}. Bu ses, nefsin bir kap gibi su aldığını duyurur.

On üçüncü ayette içilecek olan, devenin suyudur: {ar:فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا, tr:fe-kâle lehum rasûlu'llâhi nâkata'llâhi ve sukyâhâ, gloss:Allah'ın elçisi onlara dedi ki: Allah'ın dişi devesi ve onun su içmesi, source:91:13}. "Nâkata" ve "sukyâhâ" kelimelerindeki nasb hali Arapçada bir uyarıyı bildirir: bunlara dokunmayın, bunlardan sakının. Kur'an'daki diğer anlatım bu uyarıyı açıkça söyler. Salih'in sözüdür: {ar:هَٰذِهِۦ نَاقَةُ ٱللَّهِ لَكُمْ ءَايَةًۭ ۖ فَذَرُوهَا تَأْكُلْ فِىٓ أَرْضِ ٱللَّهِ ۖ وَلَا تَمَسُّوهَا بِسُوٓءٍۢ, tr:hâzihî nâkatu'llâhi lekum âyeten, fe-zerûhâ te'kul fî ardı'llâhi ve lâ temessûhâ bi-sû', gloss:işte bu, size bir işaret olarak Allah'ın devesi; bırakın Allah'ın yerinde otlasın ve ona kötülükle dokunmayın, source:7:73}. Sukyâ bir içirmedir: {ar:السقي والسقيا أن يعطيه ما يشرب, tr:es-sakyu ve's-sukyâ en yu'tıyehû mâ yeşrab, gloss:sakyi ve sukyâ, birine içecek bir şey vermektir, source:"س ق ي,B001"}. Kök, dilediği gibi alabileceği bir pay ayırmayı da anlatır: {ar:الإسقاء أن يجعل له ذلك حتى يتناوله كيف شاء, tr:el-iskâu en yec'ale lehû zâlike hattâ yetenâvelehû keyfe şâ', gloss:iskâ, ona bunu ayırmaktır ki istediği gibi alsın, source:"س ق ي,B002"}. Kur'an bu payı günlere böler. Salih Semûd'a şöyle der: {ar:هَٰذِهِۦ نَاقَةٌۭ لَّهَا شِرْبٌۭ وَلَكُمْ شِرْبُ يَوْمٍۢ مَّعْلُومٍۢ, tr:hâzihî nâkatun lehâ şirbun ve lekum şirbu yevmin ma'lûm, gloss:işte bir dişi deve; belli bir günde su içme hakkı onun, belli bir günde de sizin, source:26:155}. Allah'ın Salih'e verdiği talimatta da aynı bölüşüm vardır: {ar:وَنَبِّئْهُمْ أَنَّ ٱلْمَآءَ قِسْمَةٌۢ بَيْنَهُمْ ۖ كُلُّ شِرْبٍۢ مُّحْتَضَرٌۭ, tr:ve nebbi'hum enne'l-mâe kısmetun beynehum, kullu şirbin muhtadar, gloss:onlara suyun aralarında paylaştırıldığını haber ver; her içiş payına sahibi gelir, source:54:28}. Benzer bir paylaştırma Mûsâ kavminde de vardır. Taştan su fışkırır ve herkes kendi içme yerini bilir: {ar:فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ, tr:fe'nfecerat minhu'snetâ aşrate aynâ, kad alime kullu unâsin meşrabehum, gloss:ondan on iki pınar fışkırdı; her topluluk kendi içme yerini bildi, source:2:60}. Elçinin adı bile bu sahnede süt gibi akan bir bolluğu çağırır: {ar:الرسل اللبن الكثير المتتابع الدر, tr:er-reslu'l-lebenu'l-kesîru'l-mutetâbi'u'd-dirr, gloss:resl, ardı ardınca akan bol süttür, source:"ر س ل,B006"}.

Devenin payını çiğneyen kavim kendi payını alır. On dördüncü ayetteki "zenb" kelimesinin kökü, ağzına kadar dolu bir kovayı adlandırır: {ar:الذنوب الدلو الملأى ماء, tr:ez-zenûbu'd-delvu'l-mel'â mâen, gloss:zenûb, suyla dolu kovadır, source:"ذ ن ب,B007"}. Bu kova bir hisse anlamına da gelir: {ar:الذنوب في التنزيل هو النصيب, tr:ez-zenûbu fi't-tenzîli huve'n-nasîb, gloss:Kur'an'da zenûb, paydır, source:"ذ ن ب,B006"}. Kur'an bu kelimeyi zalimlerin cezası için kullanır: {ar:فَإِنَّ لِلَّذِينَ ظَلَمُوا۟ ذَنُوبًۭا مِّثْلَ ذَنُوبِ أَصْحَٰبِهِمْ, tr:fe-inne li'llezîne zalemû zenûben misle zenûbi ashâbihim, gloss:zulmedenlerin, öncekilerin payı gibi bir kova payı vardır, source:51:59}. Bu söz, Semûd'un da anıldığı helak edilmiş kavimler dizisinin hemen ardından gelir. Kova ile günah aynı kökten gelir. Düz bir anlatım "günahları yüzünden" der ve geçer. Kelimenin ailesi ise ölçüyü gösterir: devenin içme payını engelleyenler, kendi kovalarının tam payını alırlar.

Kaynaklar: 91:7 نَفْسٍۢ ن ف س B006; 91:7 نَفْسٍۢ ن ف س B008; 91:8 فَأَلْهَمَهَا ل ه م B001; 91:8 فَأَلْهَمَهَا ل ه م B002; 91:13 رَسُولُ ر س ل B006; 91:13 وَسُقْيَٰهَا س ق ي B001; 91:13 وَسُقْيَٰهَا س ق ي B002; 91:14 بِذَنۢبِهِمْ ذ ن ب B006; 91:14 بِذَنۢبِهِمْ ذ ن ب B007

## Dişi devenin bedeni

Surenin birçok kelimesi bir dişi deveyle uğraşmanın dilinden gelir. Merkezde devenin kendisi durur: {ar:ناقة ونوق, tr:nâkatun ve nûk, gloss:nâka, dişi deve; çoğulu nûk, source:"ن و ق,B002"}. On ikinci ayetin fiili de deve sürmenin dilindendir: {ar:بعثت الناقة إذا أثرتها, tr:ba'astu'n-nâkate izâ eseartuhâ, gloss:dişi deveyi kaldırdığımda "ba'astu" derim, source:"ب ع ث,B001"}. İşin tamamı şöyle anlatılır: {ar:بعثت البعير فانبعث إذا حللت عقاله وأرسلته لو كان باركا فأثرته, tr:ba'astu'l-ba'îra fe'nbe'ase izâ halaltu ıkâlehû ve erseltuh, ev kâne bârikan fe-esertuh, gloss:deveyi kaldırdım, o da kalktı; yani köstekini çözüp saldım ya da çökmüşse ayağa kaldırdım, source:"ب ع ث,B001"}. Deve sürücüsünün fiilinde iki taraf vardır: biri kaldırır, deve kalkar. On ikinci ayette ise kaldıran yoktur, yalnızca kalkan vardır. Köstekten kurtulan, en bedbaht adamdır ve kalkışı devenin üstüne yönelir.

İkinci ayetteki fiil, devenin ardından yürüyen yavruyu adlandırır: {ar:تلو الناقة ولدها الذي يتلوها, tr:tilvu'n-nâkati veleduhe'llezî yetlûhâ, gloss:devenin tilvu, onu izleyen yavrusudur, source:"ت ل و,B006"}. Ay güneşi, yavrunun anasını izlediği gibi izler. Elçinin adının kökü de devenin yürüyüşünü anlatır: {ar:ناقة رسلة لينة المفاصل, tr:nâkatun resletun leyyinetu'l-mefâsıl, gloss:resle deve, eklemleri yumuşak devedir, source:"ر س ل,B003"}; {ar:ناقة رسلة سهلة السير وإبل مراسيل منبعثة انبعاثا سهلا, tr:nâkatun resletun sehletu's-seyr, ve ibilun merâsîlu munbe'isetun inbi'âsen sehlen, gloss:resle deve, yürüyüşü kolay devedir; merâsîl develer, kolayca harekete geçen develerdir, source:"ر س ل,B003"}. Sekizinci ayetteki fiil memedeki yavruyu taşır, on üçüncü ayetteki kelime devenin suyunu. Bu sahne yukarıdaki iki imgede gösterildi.

On dördüncü ayette devenin bedenine yönelen fiil gelir. Bu fiil eşek arısı sokması gibi bir dokunuş değildir; ayağı biçmektir: {ar:عقر البعير كسف عرقوبه ثم جعل النحر عقرا, tr:akru'l-ba'îri kesfu urkûbih, summe cu'ile'n-nahru akran, gloss:deveyi akr etmek, topuk kirişini kesmektir; sonra boğazlamaya da akr denmiştir, source:"ع ق ر,B002"}. Kesilen kirişin adı on beşinci ayetteki kelimenin kökündendir: {ar:العرقوب عقب موتر خلف الكعبين والراء زائدة, tr:el-urkûbu akabun mûterun halfe'l-ka'beyn, ve'r-râu zâide, gloss:urkûb, iki aşık kemiğinin arkasında gerilmiş bir kiriştir; içindeki "r" harfi fazladan gelmiştir, source:"ع ق ب,B001"}; {ar:العقب العصب الذي تعمل منه الأوتار, tr:el-akabu'l-asabu'llezî tu'melu minhu'l-evtâr, gloss:akab, yay kirişlerinin yapıldığı sinirdir, source:"ع ق ب,B001"}. Topuğun kendisi de aynı köktendir: {ar:العقب مؤخر القدم, tr:el-akibu mu'ahharu'l-kadem, gloss:akib, ayağın arka ucudur, source:"ع ق ب,B002"}. On dördüncü ayetteki günah kelimesinin kökü de hayvanın arka tarafını adlandırır: {ar:ذنب وهو مؤخر الدواب, tr:zenebun, ve huve mu'ahharu'd-devâbb, gloss:zeneb, hayvanların arka ucudur, kuyruğudur, source:"ذ ن ب,B002"}. Ayakları biçen kılıç tam bu arka tarafa iner.

Kur'an devenin hikâyesini birkaç yerde anlatır. Allah Salih'e şöyle der: {ar:إِنَّا مُرْسِلُوا۟ ٱلنَّاقَةِ فِتْنَةًۭ لَّهُمْ فَٱرْتَقِبْهُمْ وَٱصْطَبِرْ, tr:innâ mursilu'n-nâkati fitneten lehum fe'rtakıbhum ve'stabir, gloss:onları sınamak için dişi deveyi gönderiyoruz; sen onları gözle ve sabret, source:54:27}. Burada deve "gönderilir", ve fiil elçinin adının köküyle kurulur. Ardından o tek adam bıçağa uzanır: {ar:فَنَادَوْا۟ صَاحِبَهُمْ فَتَعَاطَىٰ فَعَقَرَ, tr:fe-nâdev sâhibehum fe-teâtâ fe-akar, gloss:arkadaşlarını çağırdılar; o da eline aldı ve ayaklarını biçti, source:54:29}. Salih'in uyarısında devenin otlama hakkı da vardır, dokunma yasağı da: {ar:هَٰذِهِۦ نَاقَةُ ٱللَّهِ لَكُمْ ءَايَةًۭ ۖ فَذَرُوهَا تَأْكُلْ فِىٓ أَرْضِ ٱللَّهِ ۖ وَلَا تَمَسُّوهَا بِسُوٓءٍۢ, tr:hâzihî nâkatu'llâhi lekum âyeten, fe-zerûhâ te'kul fî ardı'llâhi ve lâ temessûhâ bi-sû', gloss:bu, size bir işaret olarak Allah'ın devesi; bırakın Allah'ın yerinde otlasın, ona kötülükle dokunmayın, source:7:73}. Şuarâ Suresi'nde ise devirmenin hemen ardından pişmanlık gelir: {ar:فَعَقَرُوهَا فَأَصْبَحُوا۟ نَٰدِمِينَ, tr:fe-akarûhâ fe-asbahû nâdimîn, gloss:ayaklarını biçtiler ve pişman oldular, source:26:157}. Düz bir anlatım "deveyi öldürdüler" der. Fiil ise işin yerini gösterir: önce topuğa, sonra yere yapılan bir iş. Kelimelerin dağılımı da bir sıra gösterir. Kaldırılan, izlenen, rahat yürüyen ve sulanan bir deve, sonunda arkasından biçilir. Bu ardından gelen kelimeler, son ayette suçun ardından gelecek olanı haber verir.

Kaynaklar: 91:2 تَلَىٰهَا ت ل و B006; 91:8 فَأَلْهَمَهَا ل ه م B001; 91:12 ٱنۢبَعَثَ ب ع ث B001; 91:13 نَاقَةَ ن و ق B002; 91:13 رَسُولُ ر س ل B003; 91:13 وَسُقْيَٰهَا س ق ي B001; 91:14 فَعَقَرُوهَا ع ق ر B002; 91:14 بِذَنۢبِهِمْ ذ ن ب B002; 91:15 عُقْبَٰهَا ع ق ب B001; 91:15 عُقْبَٰهَا ع ق ب B002

## Gönderilen ve peşine düşülen

Surenin başında doğru bir izleme vardır: ay güneşi izler. İzleme fiilinin bir kolu, vahyedilmiş kitabı izlemeyi anlatır: {ar:التلاوة تختص باتباع كتب الله المنزلة تارة بالقراءة وتارة بالارتسام, tr:et-tilâvetu tahtessu bi'ttibâ'i kutubi'llâhi'l-munzele, târeten bi'l-kırâe ve târeten bi'l-irtisâm, gloss:tilâvet, Allah'ın indirdiği kitapları izlemeye mahsustur; bazen okuyarak, bazen izine uyarak, source:"ت ل و,B002"}. İkinci ayetteki ayın işi, on üçüncü ayette elçinin getirdiği sözü izlemenin ölçüsü olur.

Elçinin adının kökü, salıvermeyi ve uzanmayı anlatır: {ar:أصل واحد يدل على الانبعاث والامتداد, tr:aslun vâhidun yedullu ale'l-inbi'âsi ve'l-imtidâd, gloss:harekete geçmeyi ve uzanmayı gösteren tek bir kök, source:"ر س ل,B001"}; {ar:الإرسال يقابل الإمساك, tr:el-irsâlu yukâbilu'l-imsâk, gloss:irsâl, tutmanın karşıtıdır, source:"ر س ل,B001"}. Elçi taşıdığı sözün adıyla da anılır: {ar:الرسول يقال للقول المتحمل وتارة لمتحمل القول والرسالة, tr:er-rasûlu yukâlu li'l-kavli'l-mutehammel, ve târeten li-mutehammili'l-kavli ve'r-risâle, gloss:resûl, taşınan söze de, sözü ve mesajı taşıyana da denir, source:"ر س ل,B002"}. Gönderme fiili ile on ikinci ayetin fiili aynı aileye bağlanır: {ar:ولقد بعثنا في كل أمة رسولا نحو أرسلنا رسلنا, tr:ve le-kad ba'asnâ fî kulli ummetin rasûlen, nahvu erselnâ rusulenâ, gloss:"her ümmete bir elçi ba'as ettik" sözü, "elçilerimizi irsâl ettik" gibidir, source:"ب ع ث,B002"}. Kur'an'daki karşılığı bir ayette göndermeyi, inkârı ve sonucu birlikte toplar: {ar:وَلَقَدْ بَعَثْنَا فِى كُلِّ أُمَّةٍۢ رَّسُولًا, tr:ve le-kad ba'asnâ fî kulli ummetin rasûlen, gloss:andolsun, her ümmete bir elçi gönderdik, source:16:36}. Aynı ayet şöyle biter: {ar:فَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ, tr:fe'nzurû keyfe kâne âkıbetu'l-mukezzibîn, gloss:yalanlayanların sonunun nasıl olduğuna bakın, source:16:36}. On ikinci ayette ise fiil, göndereni olmayan bir kalkış biçiminde gelir. Allah'ın göndermesine karşılık bir adam kendini gönderir.

Bu adam kavmin başındadır ve kavmin en bedbahtıdır: {ar:الشقوة خلاف السعادة, tr:eş-şikvetu hılâfu's-seâde, gloss:şikve, mutluluğun karşıtıdır, source:"ش ق و,B001"}. Kavim de onun peşine düşer. On dördüncü ayetteki "zenb" kelimesinin bir kolu bu izleyenlerin adıdır: {ar:ذنب الرجل أتباعه وأذناب القوم أتباع الرؤساء, tr:zenebu'r-raculi etbâ'uh, ve ezenâbu'l-kavmi etbâ'u'r-ruesâ', gloss:adamın kuyruğu, ona uyanlardır; kavmin kuyrukları, reislere uyanlardır, source:"ذ ن ب,B003"}. On beşinci ayetteki kelimenin kökü de birinin izinden gelmeyi anlatır: {ar:العاقب الذي يجيء في أثر صاحبه, tr:el-âkıbu'llezî yecîu fî eseri sâhibih, gloss:âkıb, arkadaşının izinden gelendir, source:"ع ق ب,B005"}. İzlenmesi gereken elçi ise yalanlanır: {ar:كذبته نسبته إلى الكذب, tr:kezzebtuhû: nesebtuhû ile'l-kezib, gloss:onu yalanladım, yani ona yalan isnat ettim, source:"ك ذ ب,B002"}. Kavmin elçiye cevabı söze karşı söz olarak gelir. Elçi "ve kâle", "dedi ki" diye konuşur: {ar:القول من النطق, tr:el-kavlu mine'n-nutk, gloss:kavl, konuşmadan gelir, source:"ق و ل,B001"}.

Kur'an Semûd'un bu reddini kendi sözleriyle aktarır. Bir insanı izlemeyi küçümserler: {ar:أَبَشَرًۭا مِّنَّا وَٰحِدًۭا نَّتَّبِعُهُۥٓ, tr:e beşeren minnâ vâhiden nettebi'uh, gloss:aramızdan tek bir insana mı uyacağız, source:54:24}. Ve onu yalancılıkla suçlarlar: {ar:بَلْ هُوَ كَذَّابٌ أَشِرٌۭ, tr:bel huve kezzâbun eşir, gloss:hayır, o şımarık bir yalancıdır, source:54:25}. Aynı sure, tek bir adamın ardına düşüldüğü sahneyle sürer: {ar:فَنَادَوْا۟ صَاحِبَهُمْ فَتَعَاطَىٰ فَعَقَرَ, tr:fe-nâdev sâhibehum fe-teâtâ fe-akar, gloss:arkadaşlarını çağırdılar; o da eline aldı ve ayaklarını biçti, source:54:29}. Elçiye uymayı reddedenler, kendi seçtikleri adamı izler. A'râf Suresi'nde de büyüklenen ileri gelenler müminlere sorar: {ar:أَتَعْلَمُونَ أَنَّ صَٰلِحًۭا مُّرْسَلٌۭ مِّن رَّبِّهِۦ, tr:e ta'lemûne enne Sâlihan murselun min rabbih, gloss:Salih'in Rabbi tarafından gönderildiğini mi biliyorsunuz, source:7:75}. Deveyi biçtikten sonra da alay ederler: {ar:إِن كُنتَ مِنَ ٱلْمُرْسَلِينَ, tr:in kunte mine'l-murselîn, gloss:eğer gönderilenlerdensen, source:7:77}. Şuarâ Suresi'nde de anlatım bir yalanlamayla açılır: {ar:كَذَّبَتْ ثَمُودُ ٱلْمُرْسَلِينَ, tr:kezzebet Semûdu'l-murselîn, gloss:Semûd gönderilenleri yalanladı, source:26:141}. Salih'in kendini tanıtması da şudur: {ar:إِنِّى لَكُمْ رَسُولٌ أَمِينٌۭ, tr:innî lekum rasûlun emîn, gloss:ben size gönderilmiş güvenilir bir elçiyim, source:26:143}. Neml Suresi bu izleyiciliğin içindeki bir çekirdekten bahseder: {ar:وَكَانَ فِى ٱلْمَدِينَةِ تِسْعَةُ رَهْطٍۢ, tr:ve kâne fi'l-medîneti tis'atu rahtin, gloss:şehirde dokuz kişilik bir çete vardı, source:27:48}. Elçinin son sözü, taşıdığı yükü teslim ettiğidir: {ar:لَقَدْ أَبْلَغْتُكُمْ رِسَالَةَ رَبِّى, tr:le-kad eblağtukum risâlete rabbî, gloss:Rabbimin mesajını size ulaştırdım, source:7:79}. Düz bir anlatım "yalanladılar" der. Bu imge ise iki izleme hattı çizer: biri gökte ve doğru, ay güneşin ardından gider; öteki yerde ve yanlış, kavim kendi en bedbahtının ardından gider. Birinde sıra korunur, ötekinde başa geçen, peşindekileri yıkıma götürür.

Kaynaklar: 91:2 تَلَىٰهَا ت ل و B001; 91:2 تَلَىٰهَا ت ل و B002; 91:11 كَذَّبَتْ ك ذ ب B002; 91:12 ٱنۢبَعَثَ ب ع ث B002; 91:12 أَشْقَىٰهَا ش ق و B001; 91:13 فَقَالَ ق و ل B001; 91:13 رَسُولُ ر س ل B001; 91:13 رَسُولُ ر س ل B002; 91:14 فَكَذَّبُوهُ ك ذ ب B002; 91:14 بِذَنۢبِهِمْ ذ ن ب B003; 91:15 عُقْبَٰهَا ع ق ب B005

## Suç ve topuğundaki

On dördüncü ve on beşinci ayetler bir bedenin arka ucunda kapanır. "Zenb" ile "ukbâ" ayrı köklerden gelir, ama ikisi de bir şeyin son ucunu adlandırır. Zenb kuyruktur: {ar:ذنب كل شيء آخره, tr:zenebu kulli şey'in âhiruh, gloss:her şeyin zenebi, onun son ucudur, source:"ذ ن ب,B002"}. Ukbâ da sondur: {ar:عاقبة كل شيء آخره والعقبى جزاء الأمر, tr:âkıbetu kulli şey'in âhiruh, ve'l-ukbâ cezâu'l-emr, gloss:her şeyin âkıbeti onun sonudur; ukbâ da bir işin karşılığıdır, source:"ع ق ب,B006"}. Günah, sonucuyla tanımlanır: {ar:يستعمل في كل فعل يستوخم عقباه, tr:yusta'melu fî kulli fi'lin yustevhamu ukbâh, gloss:sonu ağır gelen, sindirilemeyen her iş için kullanılır, source:"ذ ن ب,B001"}. Ceza da günahın ardından gelen ikinci şey olarak adını alır: {ar:سميت عقوبة لأنها تكون آخرا وثاني الذنب, tr:summiyet ukûbeten li-ennehâ tekûnu âhiran ve sâniye'z-zenb, gloss:cezaya ukûbe denmesi, en sonda ve günahın ikincisi olarak gelmesindendir, source:"ع ق ب,B007"}. İki kök tek bir cümlede de buluşur: {ar:العقاب العقوبة وقد عاقبته بذنبه, tr:el-ıkâbu'l-ukûbe, ve kad âkabtuhû bi-zenbih, gloss:ıkâb cezadır; onu günahıyla cezalandırdım, source:"ع ق ب,B007"}. Bu, on dördüncü ayetin "bi-zenbihim" sözüyle on beşinci ayetin "ukbâhâ" sözünün dilde birbirine bağlı iki parça olduğunu gösterir.

Suçu cezalandıran, malın sahibidir. On dördüncü ayet Rab der: {ar:رب كل شئ: مالكه, tr:rabbu kulli şey': mâlikuh, gloss:her şeyin rabbi, onun sahibidir, source:"ر ب ب,B001"}. On üçüncü ayette deve "Allah'ın devesi" diye anılmıştı. Sahibinin malına el uzatılmış, sahibi de karşılığı vermiştir. Gecenin fiili bu karşılığın biçimini verir: {ar:غاشية من عذاب الله أي عقوبة مجللة تعمهم, tr:ğâşiyetun min azâbi'llâh, ey ukûbetun mucellilatun teummuhum, gloss:Allah'ın azabından bir ğâşiye, yani onları baştan başa saran bir ceza, source:"غ ش و,B002"}. Ceza, on beşinci ayetin kökünden, gecenin örtüsüyle gelir.

On beşinci ayet sonucu hiç kimsenin geri çeviremeyeceğini söyler: {ar:وَلَا يَخَافُ عُقْبَٰهَا, tr:ve lâ yehâfu ukbâhâ, gloss:o, bunun sonundan korkmaz, source:91:15}. Ayetin öznesi, bir önceki ayetin öznesi olan Rabdir. Korku, bir işaretten zarar beklemektir: {ar:الخوف توقع مكروه عن أمارة مظنونة أو معلومة, tr:el-havfu tevakku'u mekrûhin an emâratin maznûnetin ev ma'lûme, gloss:korku, sanılan ya da bilinen bir işaretten hoşa gitmeyen bir şey beklemektir, source:"خ و ف,B001"}. Ama Allah'ın korkutması bir uyarıdır, kendisi korkmaz: {ar:التخويف من الله تعالى هو الحث على التحرز, tr:et-tahvîfu mina'llâhi teâlâ huve'l-hassu ale't-teharruz, gloss:Allah'ın korkutması, sakınmaya teşviktir, source:"خ و ف,B002"}. Kur'an deveyi tam olarak böyle bir korkutma olarak anar: {ar:وَمَا نُرْسِلُ بِٱلْءَايَٰتِ إِلَّا تَخْوِيفًۭا, tr:ve mâ nursilu bi'l-âyâti illâ tahvîfâ, gloss:işaretleri ancak korkutmak için göndeririz, source:17:59}. "Ukbâ" kökünün bir kolu, bir hükmün ardına düşüp hak arayanı adlandırır: {ar:المعقب الذي يتتبع عقب إنسان في طلب حق, tr:el-mu'akkıbu'llezî yetetebba'u akibe insânin fî talebi hakk, gloss:mu'akkıb, hak istemek için birinin topuğu ardınca izleyendir, source:"ع ق ب,B008"}; {ar:لا معقب لحكمه أي لا راد لقضائه, tr:lâ mu'akkıbe li-hukmih, ey lâ râdde li-kadâih, gloss:hükmünün ardına düşen yoktur, yani kararını geri çevirecek yoktur, source:"ع ق ب,B008"}. Kur'an bu sözü kendi diliyle söyler: {ar:وَٱللَّهُ يَحْكُمُ لَا مُعَقِّبَ لِحُكْمِهِۦ, tr:va'llâhu yahkumu lâ mu'akkibe li-hukmih, gloss:Allah hükmeder; O'nun hükmünün ardına düşüp onu bozacak yoktur, source:13:41}. Bir başka yerde aynı gerçeği şöyle söyler: {ar:لَا يُسْـَٔلُ عَمَّا يَفْعَلُ وَهُمْ يُسْـَٔلُونَ, tr:lâ yus'elu ammâ yef'alu ve hum yus'elûn, gloss:O yaptığından sorgulanmaz, onlar sorgulanır, source:21:23}.

Kur'an Semûd'un sonunu bu iki kelimeyle anlatır. Neml Suresi'nde dokuz kişilik çetenin tuzağı şöyle biter: {ar:فَٱنظُرْ كَيْفَ كَانَ عَٰقِبَةُ مَكْرِهِمْ أَنَّا دَمَّرْنَٰهُمْ وَقَوْمَهُمْ أَجْمَعِينَ, tr:fe'nzur keyfe kâne âkıbetu mekrihim, ennâ demmernâhum ve kavmehum ecma'în, gloss:tuzaklarının sonunun nasıl olduğuna bak: onları da kavimlerini de topyekûn yok ettik, source:27:51}. Ankebût Suresi'nde helak edilen kavimler toplu olarak anılır: {ar:فَكُلًّا أَخَذْنَا بِذَنۢبِهِۦ, tr:fe-kullen ehaznâ bi-zenbih, gloss:hepsini kendi günahıyla yakaladık, source:29:40}. Enfâl Suresi'nde de aynı bağ kurulur: {ar:فَأَهْلَكْنَٰهُم بِذُنُوبِهِمْ, tr:fe-ehleknâhum bi-zunûbihim, gloss:onları günahları yüzünden helak ettik, source:8:54}. Devenin biçilmesinden sonra Salih'in sözü, sonucu bir süreye bağlar: {ar:فَعَقَرُوهَا فَقَالَ تَمَتَّعُوا۟ فِى دَارِكُمْ ثَلَٰثَةَ أَيَّامٍۢ, tr:fe-akarûhâ fe-kâle temetta'û fî dârikum selâsete eyyâm, gloss:onu biçtiler; Salih de dedi ki: yurdunuzda üç gün daha yaşayın, source:11:65}; {ar:ذَٰلِكَ وَعْدٌ غَيْرُ مَكْذُوبٍۢ, tr:zâlike va'dun ğayru mekzûb, gloss:bu, yalanlanamayacak bir sözdür, source:11:65}. Yalanlayarak işe başlayan kavim, yalanlanamayan bir sözle karşılaşır.

Dokuzuncu ayet bu dilin öbür yüzünü taşır. Arınıp büyüyenin işi de sonucuyla tanımlanır, ama tersinden: {ar:حلالا لا يستوخم عقباه, tr:helâlen lâ yustevhamu ukbâh, gloss:helâl, yani sonu ağır gelmeyen, source:"ز ك و,B002"}. Günah sindirilemeyen bir sondur, arınmanın sonu ise kolay sindirilir. Düz bir anlatım son ayeti bir ek söz gibi okur. Bu imge ise onu surenin bedenine bağlar: suç arkada durur, karşılığı da onun ardından gelir ve ardından bir şey gelmeyen tek şey hükmün kendisidir.

Kaynaklar: 91:4 يَغْشَىٰهَا غ ش و B002; 91:9 زَكَّىٰهَا ز ك و B002; 91:14 رَبُّهُم ر ب ب B001; 91:14 بِذَنۢبِهِمْ ذ ن ب B001; 91:14 بِذَنۢبِهِمْ ذ ن ب B002; 91:15 يَخَافُ خ و ف B001; 91:15 يَخَافُ خ و ف B002; 91:15 عُقْبَٰهَا ع ق ب B006; 91:15 عُقْبَٰهَا ع ق ب B007; 91:15 عُقْبَٰهَا ع ق ب B008

## Buluşmalar

İlk buluşma sekizinci ayette olur. "Fucûr" kelimesi aynı kökten üç sahneyi bir arada tutar: geceyi yaran şafağı, bentten fırlayan suyu ve din perdesini yırtmayı. Gökte yarılma ışık getirir, nefiste ise koruyucu örtüyü yırtar ve bir taşkın başlatır. Takvâ aynı ayette hem bir örtüdür hem de bir settir. Tek bir kelime bu iki imgeyi birlikte taşır: örten ve alıkoyan. Böylece surenin başındaki düzenli nöbet nefsin içine taşınır. Gece güneşin üstünü sırası gelince örter ve sırası gelince açılır. Nefis ise ya kendi örtüsünü yerinde tutar ya da onu yırtıp taşar.

İkinci buluşma on ikinci ayetteki "inbe'ase" fiilindedir. Bu fiil üç imgeyi birden toplar. Fucûru tanımlayan atılıştır, deveyi köstekinden çözüp kaldırmanın sonucudur ve Allah'ın elçi gönderişinin eşi olan bir fiildir. Deve sürücüsünün dilinde biri kaldırır, deve kalkar. Bu ayette ise kaldıran yoktur. Adam kendi kendine, köstekinden kurtulmuş bir hayvan gibi kalkar ve Allah'ın gönderdiği deveye yönelir. Elçi gönderilmiştir, deve gönderilmiştir. Taşkın olan ise kendini gönderir.

Üçüncü buluşma, on dördüncü ayetten on beşinciye geçen bedenin arka ucudur. "Akr" topuk kirişini keser. O kirişin adı on beşinci ayetteki "ukbâ" kelimesinin kökündendir. Günahın adı olan "zenb" de hayvanın arka ucunun adıdır. Devenin imgesi ile suçun ardından gelen sonucun imgesi böylece aynı noktada birleşir. Kavim devenin arkasına vurur; karşılık da onların "arkalarından", yani günahlarının ardından gelir. Kova ile günahın aynı kökten gelmesi bunu ölçüye bağlar. Devenin su payını çiğneyenler kendi kova paylarını alırlar.

Dördüncü buluşma "sevvâ" fiilindedir. Bu fiil göğün ve nefsin bitirilişini Semûd'un yerle bir edilişine bağlar. Altıncı ayetteki yayılmış yer bu iki ucun arasında durur. Kavim ovaya saray kurmuştu. Yayılan yere kurulan sarayları yayılmış bir yer gibi dümdüz olur. Gökten yağan su, sürülen toprak ve büyüyen ekin bu yere bağlıdır. Hurmanın başını kesmeyi ve hiçbir şey bitirmeyen kumu anlatan "akr" fiili, kavmin tarlasını bir çorak yere çevirir.

Bu buluşmalar birlikte surenin hareketini taşır. Sure, her cismin yerini bildiği bir gökle başlar: ışık yayılır, ay onu izler, gündüz açar, gece örter. Ardından gök ve yerden bir ev kurulur ve aynı el nefsi bu evin üçüncü yapısı olarak düzenler. Nefse iki lokma yutturulur: hem yırtan ve taşan hem de örten ve alıkoyan. Dokuzuncu ve onuncu ayetler bu iki lokmanın sonucunu iki tarla gibi gösterir: biri sürülmüş ve büyümüş, öbürü gömülmüş. Semûd ise yanlış yolu seçer. Sınırı aşar, kendi en bedbahtının ardına düşer, gönderilen deveyi arkasından biçer. Karşılık gece gibi üstlerine kapanır ve evleri ile birlikte onları yayılmış bir yer gibi dümdüz eder. Sure, gece ile gündüzün nöbetleşmesini de adlandıran bir kelimeyle kapanır. Ama bu son nöbette, hükmün ardından gelecek ve onu geri çevirecek hiçbir şey yoktur.

