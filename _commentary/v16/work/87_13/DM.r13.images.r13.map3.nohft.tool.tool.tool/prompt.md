Focus: 87:13. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. No other command or tool is available.

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


===== _commentary/v16/work/87_13/D.r13/context.md =====
# 87:13 — focus

ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ

Anchor translation (canonical reading, reference only):

Sonra orada ne ölecek ne de yaşayacaktır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ثُمَّ | ثُمّ |  | CONJ |
| 2 | لَا | لَا |  | NEG |
| 3 | يَمُوتُ | مَّاتَ | م و ت | V |
| 4 | فِيهَا | فِى |  | P;PRON |
| 5 | وَلَا | لَا |  | CONJ;NEG |
| 6 | يَحْيَىٰ | حَىَّ | ح ي ي | V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 87 — full text (context; no pericope)

- 87:1 سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى
- 87:2 ٱلَّذِى خَلَقَ فَسَوَّىٰ
- 87:3 وَٱلَّذِى قَدَّرَ فَهَدَىٰ
- 87:4 وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ
- 87:5 فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ
- 87:6 سَنُقْرِئُكَ فَلَا تَنسَىٰٓ
- 87:7 إِلَّا مَا شَآءَ ٱللَّهُ ۚ إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ
- 87:8 وَنُيَسِّرُكَ لِلْيُسْرَىٰ
- 87:9 فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ
- 87:10 سَيَذَّكَّرُ مَن يَخْشَىٰ
- 87:11 وَيَتَجَنَّبُهَا ٱلْأَشْقَى
- 87:12 ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ
- 87:13 ◀ focus ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- 87:14 قَدْ أَفْلَحَ مَن تَزَكَّىٰ
- 87:15 وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ
- 87:16 بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- 87:17 وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ
- 87:18 إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ
- 87:19 صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ


===== _commentary/v16/work/87_13/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## م و ت (root_001454) — identity root of يَمُوتُ (w3)

- **B001** yaşamın ve canlı gücünün sona ermesi — ölüm; yaşamın sona ermesi · öldü; yaşamdan ayrıldı · öldü; yaşamdan ayrıldı · yakında ölecek kimse · ölmüş veya ölecek kimse · kesin ve gerçek ölüm
  أصل صحيح يدل على ذهاب القوة من الشيء (maqayis)؛ الموت خلاف الحياة (maqayis;sihah)؛ الموت معروف مات يموت موتا (jamhara)؛ الموت خلق من خلق الله (tahdhib)؛ أنواع الموت بحسب أنواع الحياة (mufradat)
- **B002** öldürme veya pişirerek keskinliğini giderme — öldürdü; gücünü giderdi · pişirerek keskinliğini giderin · içki pişirilip keskinliği giderildi
  أميتوها طبخا (maqayis)؛ أميتت الخمر طبخت (maqayis)؛ أماته الله وموته شدد للمبالغة (sihah)
- **B003** cansız şey; işlenmemiş veya sahipsiz arazi — işlenmemiş arazi; canlı olmayan şey · cansız şey; sahipsiz ve kullanılmayan arazi
  الموتان الأرض لم تحي بعد بزرع ولا إصلاح وكذلك الموات (maqayis)؛ الموات ما لا روح فيه (sihah)؛ الموات الأرض التي لا مالك لها ولا ينتفع بها أحد (sihah)؛ الموتان أن يبيع المتاع وكل شيء غير ذي روح (tahdhib)
- **B004** insanlar veya hayvan varlığı içinde ölüm görülmesi — insanlarda veya hayvanlarda görülen ölüm · mal veya hayvan varlığı içindeki ölüm
  وقع في الناس موتان (maqayis)؛ الموتان بالضم موت يقع في الماشية (sihah)؛ وقع في المال موتان وموات وهو الموت (tahdhib)
- **B005** çocuğu ölmüş ebeveyn veya ana hayvan — yavrusu ölmüş ana hayvan veya çocuğu ölmüş kadın · oğlu veya oğulları öldü
  ناقة مميت ومميتة للتي يموت ولدها (maqayis)؛ أماتت الناقة إذا مات ولدها فهي مميت ومميتة (sihah)؛ وكذلك المرأة (sihah)؛ أمات فلان إذا مات له ابن أو بنون (sihah)
- **B006** zekâ ve anlayıştan yoksunluk — zekâsı ve anlayışı kıt kimse · ne kadar anlayışsız!
  رجل موتان الفؤاد وامرأة موتانة (maqayis)؛ رجل موتان الفؤاد وامرأة موتانة الفؤاد (sihah)؛ رجل موتان الفؤاد إذا كان غير ذكي ولا فهم (tahdhib)
- **B007** usulüne uygun kesilmeden ölen yenilebilir hayvan — usulüne uygun kesilmeden ölmüş yenilebilir hayvan
  الميتة ما مات مما يؤكل لحمه إذا ذكي (maqayis)؛ الميتة ما لم تلحقه الذكاة (sihah)
- **B008** bir kez ölme veya ölüm biçimi — ölüm biçimi veya hali · bir kez ölme
  الموتة الواحدة من الموت (maqayis)؛ الميتة حال من الموت حسنة أو قبيحة (maqayis)؛ مات فلان ميتة حسنة (sihah)؛ الميتة الحال من أحوال الموت (tahdhib)
- **B009** ardından ayılınan geçici delilik, nöbet veya baygınlık — ardından ayılınan delilik benzeri hal, nöbet veya baygınlık
  الموتة شبه الجنون يعترى الإنسان (maqayis)؛ الموتة جنس من الجنون والصرع يعتري الإنسان (sihah)؛ الموتة الجنون (tahdhib)؛ الموتة الذي يصرع من الجنون أو غيره ثم يفيق (tahdhib)؛ الموتة شبه الغشية (tahdhib)
- **B010** bir işe kendini bütünüyle verme; savaşta ölümü göze alma [kalıp] — işe kendini bütünüyle veren · savaşta ölümü göze alarak dövüşen · ölümü gönüllü karşıladı
  المستميت للأمر المسترسل له (maqayis;sihah)؛ المستميت المستقتل الذي لا يبالي في الحرب من الموت (sihah)؛ استمات الرجل إذا طاب نفسا بالموت (tahdhib)؛ المستميت الذي يقاتل على الموت (tahdhib)
- **B011** ölmüş, deli veya alçakgönüllüymüş gibi davranma — gösteriş için aşırı alçakgönüllü görünen · canlıyken ölmüş gibi davrandı · deli veya alçakgönüllüymüş gibi davranan
  المتماوت من صفة الناسك المرائي (sihah)؛ المستميت الذي يتجان وليس بمجنون (tahdhib)؛ يتخاشع ويتواضع لهذا حتى يطعمه (tahdhib)؛ ضربته فتماوت إذا أرى أنه ميت وهو حي (tahdhib)؛ المتماوتون المراءون (tahdhib)
- **B012** rüzgârın dinmesi, kumaşın eskimesi veya insanın uyuması [kalıp] — rüzgâr dindi · kumaş eskidi ve yıprandı · adam uyudu ve hareketsizleşti
  الموت السكون (tahdhib)؛ ماتت الريح إذا سكنت (tahdhib)؛ مات الثوب ونام إذا بلي (tahdhib)؛ مات الرجل وهمد وهوم إذا نام (tahdhib)
- **B013** gerçeğe boyun eğme [kalıp] — adam gerçeğe boyun eğdi
  مات الرجل إذا خضع للحق (tahdhib)
- **B014** vurulmuş avın ölüp ölmediğini inceleme [kalıp] — avınızın ölüp ölmediğine bakın
  استميتوا صيدكم أي انظروا مات أم لا (tahdhib)؛ إذا أصيب فشك في موته (tahdhib)

## ح ي ي (root_000383) — identity root of يَحْيَىٰ (w6)

- **B001** canlı olma, sürüp gitme ve canlandırma — yaşam · canlı; ölmesi düşünülemeyen varlık · canlı oldu ya da canlı kaldı · canlandırdı ya da yeniden yaşama döndürdü · yaşam · bitmeyen gerçek yaşam · ateşi üfleyerek canlandırdı · çocuğu yaşatan besin
  خلاف الموت (maqayis); الحياة ضد الموت والحي ضد الميت (jamhara;sihah); يقال حيي يحيا فهو حي (ayn;tahdhib); الحياة تستعمل للقوة النامية والحساسة والعاقلة والأخروية والباري حي (mufradat)
- **B002** yağmurla gelen toprak canlılığı ve bolluk — toprağı canlandıran yağmur ve bolluk · toprağı bitkili ve verimli buldum · topluluk yağmura ve bol ota kavuştu · körpe ve canlı bitki
  يسمى المطر حيا لأن به حياة الأرض (maqayis); الحيا مقصور حيا الربيع وهو ما تحيا به الأرض من الغيث (ayn); أحيا القوم أي صاروا في الحيا وهو الخصب وأتيت الأرض فأحييتها أي وجدتها خصبة (sihah); الحي من النبات ما كان طريا يهتز والحيا الغيث (tahdhib); الحيا المطر لأنه يحيي الأرض بعد موتها (mufradat)
- **B003** canlı varlık veya bitmeyen gerçek yaşam — canlı varlık, özellikle duyup hareket eden varlık · bitmeyen gerçek yaşam
  الحيوان كل ذي روح (ayn); الحيوان خلاف الموتان (sihah); الحيوان اسم يقع على كل شيء حي وكل ذي روح حيوان (tahdhib); الحيوان مقر الحياة وما له الحاسة وما له البقاء الأبدي (mufradat)
- **B004** yılan ve yılanla ilgili adlandırmalar — yılan · erkek yılan · yılan bakıcısı · yılanlı toprak
  الحية معروف يقال حية ذكر وحية أنثى والحيوت ذكر الحيات (jamhara); الحية اشتقاقها من الحياة (ayn); الحية تكون للذكر والأنثى والحيوت ذكر الحيات (sihah); اشتقاق الحية من الحياة ومن قال حواء قال من حويت لأنها تتحوى (tahdhib)
- **B005** kötü olandan utanarak çekinme — utanma ve kötü davranıştan çekinme · ondan utandı ve çekindi · ondan utandı ya da konuşmasına karşılık vermedi
  الاستحياء الذي هو ضد الوقاحة واستحييت منه (maqayis); حييت عن فلان إذا استحييت عنه (jamhara); حييت منه أحيا استحييت واستحياه واستحيا منه من الحياء (sihah); الحياء من الاستحياء ورجل حيي واستحيا الرجل (tahdhib); الحياء انقباض النفس عن القبائح وتركه (mufradat)
- **B006** öldürmeyip sağ bırakma — kadınları sağ bırakıyor ve öldürmüyorlar
  ويستحيون نساءكم أي لا يستبقي (sihah); استحيوا شرخهم بمعنى استفعلوا من الحياة أي استبقوهم ولا تقتلوهم (tahdhib); ويستحيون نساءكم أي يستبقونهن (mufradat)
- **B007** esenlik, uzun ömür ve kalıcılık dileği — Tanrı sana yaşam, kalıcılık ve esenlik versin · karşılama ve esenlik dileği · yoruma göre bütün esenlik, kalıcılık ya da egemenlik Tanrı'nındır
  حياك الله أي ملكك الله والتحيات لله أي الملك لله (sihah); التحية ما يحيي به بعضهم بعضا وتحية الله السلام عليكم ورحمة الله وحياك الله أي أبقاك (tahdhib); التحية أن يقال حياك الله أي جعل لك حياة ثم يجعل دعاء (mufradat)
- **B008** egemenlik bildiren kalıplaşmış söz — egemenlik ve yönetme gücü · bütün egemenlik Tanrı'nındır
  التحية الملك وحياك الله أي ملكك الله (sihah); التحية الملك وأنشد يعني على ملكه والتحيات لله الألفاظ التي تدل على الملك (tahdhib)
- **B009** bir şeye gelmeye çağırma — haydi ibadete gel · haydi et suyuna ekmek yemeğine gel
  قولهم حي على الصلاة معناه هلم وأقبل والعرب تقول حي على الثريد وهو اسم لفعل الأمر (sihah)
- **B010** ortak soylu topluluk veya boylar birliği — soy topluluğu ya da boy · aynı soydan gelen bir topluluk
  الحي حي من العرب وبنو حي بطن من العرب (jamhara); الحي واحد أحياء العرب (sihah); الحي الواحد من أحياء العرب يقع على بني أب كثروا أم قلوا وعلى شعب يجمع القبائل (tahdhib)
- **B011** dişi canlının üreme organı veya döl yatağı — dişi insan ya da hayvanın üreme organı veya döl yatağı
  حياء الناقة وهو فرجها يمكن أن يكون من هذا (maqayis); الحياء أيضا رحم الناقة والجمع أحيية (sihah); الحي فرج المرأة وحياء الشاة والناقة والمرأة ممدود (tahdhib)
- **B012** yüz — yüz
  المحيا الوجه (sihah)
- **B013** yarar, iyilik ve yok olmaktan koruma — yarar, iyilik ve yok olmaktan koruma · çocuğu yaşatan besin
  في القصاص حياة أي منفعة وليس بفلان حياة أي ليس عنده نفع ولا خير (tahdhib); ولكم في القصاص حياة أي يرتدع بالقصاص ومن أحياها أي من نجاها من الهلاك (mufradat)
- **B014** yaşamla ilişkilendirilen erkek kişi adları — yaşamla ilişkilendirilen erkek kişi adları
  حيي اسم رجل (jamhara); حيوة اسم رجل (sihah); حيوة اسم رجل بسكون الياء (tahdhib); اسمه يحيى نبه أنه سماه بذلك من حيث إنه لم تمته الذنوب (mufradat)

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 87:13, and ## Buluşmalar) =====
## Gökten otlağa: bulut, ilk yağmur ve kararan ot

Surenin ilk beş ayeti bir bitkinin bütün ömrünü kısa tutarak anlatır. Dördüncü ayet {ar:وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ, tr:velleẕî ahrace'l-mer'â, gloss:otlağı çıkaran O'dur, source:87:4} der, beşinci ayet ise {ar:فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ, tr:fe-ce'alehû ğuŝâen ahvâ, gloss:sonra onu kapkara bir sel döküntüsüne çevirdi, source:87:5} diye biter. İki ayet arasında otu topraktan çıkaran şeyin, yani yağmurun adı geçmez. Bu eksik halkayı surenin başka kelimelerinin aileleri tamamlar. Burada ve sonraki bölümlerde, bir kelimenin kök ailesinden gelen görüntü kelimenin kendi ayetindeki anlamının yanında duyulur, hiçbir zaman onun yerine geçmez. Birinci ayetteki "ad" yine addır, "Rab" yine Rab'dir. Aile görüntüsü, bu anlamın arkasında Arapçayı bilen kulağa ayrıca ulaşan sahnedir.

Birinci ayet {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:yüce Rabbinin adını tesbih et, source:87:1} der. "Ad" anlamındaki اسم kelimesi س م و kökündendir ve bu kök gökyüzünü de verir. Araplar için {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tusemmi's-sehâbe semâen ve'l-matara semâen, gloss:Araplar buluta da yağmura da semâ der, source:"س م و,B004"}, ve aynı ad yağmurun bitirdiği ota da verilir: {ar:يسموا النبات سماء, tr:yusemmû'n-nebâte semâen, gloss:bitkiye de semâ derler, source:"س م و,B004"}. Ölçüt basittir: {ar:السماء كل ما علاك فأظلك, tr:es-semâu kullu mâ alâke fe-ezalleke, gloss:semâ senin üstüne çıkıp sana gölge salan her şeydir, source:"س م و,B004"}. Tek bir kök böylece başın üstündeki örtüden buluta, buluttan yağmura, yağmurdan topraktan çıkan ota kadar uzanan bütün dikey sütunu kapsar. "Rab" kelimesinin ailesi bu sütunun içinde belirli bir bulutu gösterir: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb sumiye bi-ẕâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur; bitkiyi besleyip büyüttüğü için bu adı almıştır, source:"ر ب ب,B008"}. Bu, ötekilerin altında sarkan alçak buluttur: {ar:السحاب المتعلق دون السحاب, tr:es-sehâbu'l-muteallaku dûne's-sehâb, gloss:bulutların altında asılı duran bulut, source:"ر ب ب,B008"}. Aynı kök bulutun bir yerde durup gitmemesini de söyler: {ar:أربت السحابة: دامت, tr:erabbeti's-sehâbe dâmet, gloss:bulut durdu ve sürdü, source:"ر ب ب,B007"}. Aynı kalıp güney rüzgârı için de kullanılır: {ar:أربت الجنوب والسحابة أي دامت, tr:erabbeti'l-cenûbu ve's-sehâbe ey dâmet, gloss:güney rüzgârı da bulut da sürdü, source:"ر ب ب,B007"}. Bulutu süren bu rüzgârın adı olan cenûb, on birinci ayetteki يَتَجَنَّبُهَا kelimesiyle aynı köktendir: {ar:الجنوب ريح تجيء عن يمين القبلة, tr:el-cenûbu rîhun tecîu an yemîni'l-kıble, gloss:cenûb kıblenin sağ yanından gelen rüzgârdır, source:"ج ن ب,B006"}.

Bulut ilk belirdiğinde Arapça ona dördüncü ayetin fiilinden bir ad verir: {ar:الخروج السحاب أول ما يبدأ, tr:el-hurûc es-sehâbu evvele mâ yebdeu, gloss:hurûc bulutun ilk belirişidir, source:"خ ر ج,B005"}. Bulutun kenarlarında zayıf bir şimşek çakar. Bunu anlatan fiil, yedinci ayetteki يَخْفَىٰ ile aynı köktendir: {ar:خفا البرق يخفو خفوا ويخفى خفيا إذا لمع لمعا ضعيفا معترضا في نواحى الغيم, tr:hafe'l-berku yahfû hufuvven ve yahfî hafyen iẕâ leme'a lem'an daîfen mu'teridan fî nevâhi'l-ğaym, gloss:şimşek bulutun kenarlarında yan yan zayıfça parladığında hafâ denir, source:"خ ف ي,B004"}. Bu ışığı bütün gece gözleyen kişiyi ise on yedinci ayetteki أَبْقَىٰٓ kelimesinin kökü anlatır: {ar:بات فلان يبقي البرق أي ينظر إليه من أين يلمع, tr:bâte fulânun yubkı'l-berka ey yenzuru ileyhi min eyne yelma', gloss:falanca şimşeğin nereden çakacağına bakarak geceyi geçirdi, source:"ب ق ي,B005"}. Sonunda yağmur gelir ve adını verdiği hayattan alır: {ar:يسمى المطر حيا لأن به حياة الأرض, tr:yusemme'l-mataru hayâen li-enne bihî hayâte'l-ard, gloss:yağmura hayâ denir çünkü yerin hayatı onunladır, source:"ح ي ي,B002"}. On üçüncü ayetteki يَحْيَىٰ fiili ve on altıncı ayetteki ٱلْحَيَوٰةَ kelimesi bu köktendir. Yağmur yuvalarındaki fareleri de dışarı sürer. Bu sürüş yine "gizli" kökünden bir fiille söylenir, açıklaması da dördüncü ayetin fiiliyle yapılır: {ar:وخفا المطر الفأر من حجرتهن أخرجهن, tr:ve hafe'l-mataru'l-fe'ra min hucurâtihinne ahracehunne, gloss:yağmur fareleri deliklerinden çıkardı, source:"خ ف ي,B003"}.

اسم kelimesi için Arapçada kayıtlı ikinci bir türetme vardır. Bu türetme kelimeyi "damga" anlamındaki وسم köküne bağlar. Bu, kök kimliği değil, kayıtlı bir alternatiftir. Ama bu yoldan da aynı sahneye varılır, çünkü yılın ilk yağmurunun adı bu köktendir: {ar:سمي الوسمي من المطر وسميا لأنه يسم الأرض بالنبات فيصير فيها أثرا في أول السنة, tr:sumiye'l-vesmiyyu mine'l-matari vesmiyyen li-ennehû yesimu'l-arda bi'n-nebâti fe-yasîru fîhâ eseran fî evveli's-sene, gloss:ilk yağmura vesmî denir çünkü yeri bitkiyle damgalar ve yılın başında yerde bir iz olur, source:"و س م,B003"}. Yağmur toprağa yeşil bir iz basar.

Dördüncü ayetin fiili أخرج, somut bir şeyin bulunduğu yerden dışarı alınmasıdır: {ar:الإخراج أكثر ما يقال في الأعيان, tr:el-ihrâcu ekŝeru mâ yukâlu fi'l-a'yân, gloss:ihrâc çoğunlukla somut şeyler için söylenir, source:"خ ر ج,B002"}. Ot gerçekten topraktan çekilip çıkarılan bir şeydir. Aynı kökün ailesi ilk çıkışın görünüşünü de verir: {ar:أرض مخرجة نبتها في مكان دون مكان, tr:ardun muhrecetun nebtuhâ fî mekânin dûne mekân, gloss:otu bir yerde bitip başka yerde bitmeyen toprak, source:"خ ر ج,B007"}. İlk yeşil, toprağa yama yama düşer. Aynı ailede bir renk adı da vardır: {ar:الأخرج لون سواده أكثر من بياضه, tr:el-ahrecu levnun sevâduhû ekŝeru min beyâdih, gloss:karası akından çok olan renk, source:"خ ر ج,B007"}. المرعى ise tek kelimede otu, otlağın yerini ve otlamanın kendisini birlikte taşır: {ar:المرعى الرعي والموضع والمصدر, tr:el-mer'â er-ra'yu ve'l-mevdiu ve'l-masdar, gloss:mer'â hem ot hem yer hem otlamadır, source:"ر ع ي,B001"}.

Beşinci ayetteki جعل, bir şeyi bir halden başka bir hale çevirmektir: {ar:جعل صير, tr:ce'ale sayyera, gloss:ce'ale bir şeyi başka bir hale soktu demektir, source:"ج ع ل,B002"}. Otun çevrildiği şey olan غثاء, otun sonunu üç adımda anlatır: ot kurur, tadını yitirir, sel onu yığıp götürür. {ar:غثا السيل المرتع إذا جمع بعضه إلى بعض وأذهب حلاوته, tr:ğaŝe's-seylu'l-merte'a iẕâ ceme'a ba'dahû ilâ ba'din ve eẕhebe halâvetehû, gloss:sel otlağı üst üste yığıp tadını giderdiğinde ğaŝâ denir, source:"غ ث و,B002"}. Ot bu noktada {ar:يابسا بعد خضرته, tr:yâbisen ba'de hudratihî, gloss:yeşilliğinden sonra kurumuş olarak, source:"غ ث و,B002"} kalır. غثاء de {ar:الغثاء ما جاء به السيل من نبات قد يبس, tr:el-ğuŝâu mâ câe bihi's-seylu min nebâtin kad yebise, gloss:ğuŝâ selin getirdiği kurumuş bitkidir, source:"غ ث و,B001"}. Ardından gelen أحوى bir renktir: {ar:الأحوى الأسود من الخضرة, tr:el-ahvâ el-esvedu mine'l-hudra, gloss:ahvâ yeşilden kararmış olandır, source:"ح و ي,B006"}. Bir deve için de {ar:بعير أحوى إذا خالط خضرته سواد وصفرة, tr:baîrun ahvâ iẕâ hâlata hudratehû sevâdun ve sufra, gloss:yeşiline kara ve sarı karışmış deveye ahvâ denir, source:"ح و ي,B006"}. Rengin adı {ar:حُوَّة, tr:huvve, gloss:yeşile çalan koyu renk, source:"memory"} kelimesidir. Ayette kelime غثاء'nın sıfatı olarak durur. Ama tanımı hem gür yeşilin koyuluğunu hem de çürüyen otun kararmasını kapsar. Bu yüzden tek kelime otun iki ucunu, taze koyuluğu ve kapkara döküntüyü yan yana tutar. Kur'an gür yeşilin koyuluğunu başka bir yerde tek kelimeyle, cennet bahçeleri için verir: {ar:مُدْهَآمَّتَانِ, tr:müdhâmmetân, gloss:yeşillikten koyu kara görünen iki bahçe, source:55:64}.

Bu sahne surenin geri kalanında karşılık bulur. On üçüncü ayetteki "yaşamak" fiilinin ailesi diri otu {ar:الحي من النبات ما كان طريا يهتز, tr:el-hayyu mine'n-nebâti mâ kâne tariyyen yehtezzu, gloss:bitkinin dirisi taze olup titreşenidir, source:"ح ي ي,B002"} diye tanımlar. "Ölmek" fiilinin ailesi de {ar:الموتان الأرض لم تحي بعد بزرع ولا إصلاح, tr:el-mevtân el-ardu lem tuhye ba'du bi-zer'in ve lâ islâh, gloss:mevtân ekinle ya da bakımla henüz diriltilmemiş topraktır, source:"م و ت,B003"}. Otun yolculuğu böylece ölü topraktan titreşen yeşile, oradan kuru döküntüye uzanır. On üçüncü ayetin ateşteki adam için söylediği şey ise bu uçlardan hiçbirinde olmamaktır. "Rab" kelimesinin ailesinde bu yolculuğun karşısında duran bir bitki adı da vardır: {ar:اسم لعدة من النبات لا تهيج في الصيف, tr:ismun li-iddetin mine'n-nebâti lâ tehîcu fi's-sayf, gloss:yazın sararıp kurumayan birkaç bitkinin adı, source:"ر ب ب,B012"}. Kur'an dünya hayatı benzetmesinde tam da bu "sararıp kurumak" fiilini kullanır. Rab adının ailesindeki sararmayan ot bu sayede otlağın kaderinin karşısına konabilir. Bu bağı dil değil, okuma kurar.

Kur'an bu yolculuğu kendi sözleriyle sahneler. Allah kendini, rüzgârları rahmetinin önünde müjdeci olarak gönderen ve ağır bulutları ölü bir beldeye süren olarak anlatır, sonra şöyle der: {ar:فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:fe-enzelnâ bihi'l-mâe fe-ahracnâ bihî min kulli'ŝ-ŝemerât keẕâlike nuhrici'l-mevtâ leallekum teẕekkerûn, gloss:oraya suyu indirdik ve onunla her türlü üründen çıkardık; ölüleri de böyle çıkarırız; belki düşünüp hatırlarsınız, source:7:57}. Çıkarmak fiili burada hem bitkiye hem ölülere, sonunda da hatırlamaya bağlanır. Sure de dördüncü ayetteki çıkarmadan dokuzuncu ayetteki hatırlatmaya aynı yolla uzanır. Hemen sonraki ayet, iyi toprağın bitkisini {ar:بِإِذْنِ رَبِّهِۦ, tr:bi-izni rabbih, gloss:Rabbinin izniyle, source:7:58} çıkardığını söyler. Başka bir yerde Allah gökten bereketli su indirip onunla ölü bir beldeyi dirilttiğini anlatır ve {ar:كَذَٰلِكَ ٱلْخُرُوجُ, tr:keẕâlike'l-hurûc, gloss:çıkış da böyledir, source:50:11} der. Firavun Musa'ya {ar:فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:fe-men rabbukumâ yâ mûsâ, gloss:ikinizin Rabbi kimdir ey Musa, source:20:49} diye sorduğunda Musa'nın cevabı bu surenin ilk ayetlerindeki sırayı izler: {ar:رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:rabbunelleẕî a'tâ kulle şey'in halkahû ŝumme hedâ, gloss:Rabbimiz her şeye yaratılışını veren sonra yol gösterendir, source:20:50}. Birkaç ayet sonra gökten su indirilir ve {ar:فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ, tr:fe-ahracnâ bihî ezvâcen min nebâtin şettâ, gloss:onunla çeşit çeşit bitkiden çiftler çıkardık, source:20:53}. Surenin son ayetinde sayfaları anılan Musa, Rabbini tanıtırken aynı yaratma, yol gösterme ve çıkarma sırasını kullanır. Bir başka yerde yeryüzü için {ar:أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا, tr:ahrace minhâ mâehâ ve mer'âhâ, gloss:ondan suyunu ve otlağını çıkardı, source:79:31} denir.

Kur'an otun ikinci yarısını, yani kuruyup savrulmasını, dünya hayatının benzetmesi yapar. İki bahçe sahibinin hikâyesinden sonra Allah Peygamber'e şöyle der: {ar:وَٱضْرِبْ لَهُم مَّثَلَ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ, tr:vadrib lehum meŝele'l-hayâti'd-dunyâ ke-mâin enzelnâhu mine's-semâ, gloss:onlara dünya hayatının örneğini ver; gökten indirdiğimiz bir su gibidir, source:18:45}. Yerin bitkisi o suyla karışır, sonra {ar:هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ, tr:heşîmen teẕrûhu'r-riyâh, gloss:rüzgârların savurduğu kuru çöp, source:18:45} olur. Hemen sonraki ayet karşı kefeyi koyar: {ar:وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا, tr:ve'l-bâkıyâtu's-sâlihâtu hayrun inde rabbike sevâben, gloss:kalıcı iyi işler ise Rabbinin katında karşılık bakımından daha hayırlıdır, source:18:46}. Bu iki ayet, beşinci ayetteki döküntüyü on altıncı ve on yedinci ayetteki "dünya hayatı" ile "daha hayırlı ve daha kalıcı" ayrımına bağlayan köprüyü Kur'an'ın kendi ağzından kurar. Aynı benzetme başka bir yerde şu sözlerle gelir: {ar:ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا, tr:ŝumme yehîcu fe-terâhu musferran ŝumme yekûnu hutâmâ, gloss:sonra kurur da onu sapsarı görürsün sonra çer çöp olur, source:57:20}. Bir başka yerde aynı süreç {ar:ثُمَّ يَجْعَلُهُۥ حُطَٰمًا ۚ إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ, tr:ŝumme yec'aluhû hutâmâ inne fî ẕâlike le-ẕikrâ, gloss:sonra onu çer çöpe çevirir; bunda elbette bir öğüt vardır, source:39:21} sözleriyle anlatılır. Bu cümle beşinci ayetteki "çevirdi" fiilini ve dokuzuncu ayetteki "öğüt" kelimesini bir arada tutar. Başka bir yerde yeryüzü süslenir, sahipleri ona güç yetirdiklerini sanır, sonra buyruk gelir: {ar:فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:fe-ce'alnâhâ hasîden ke-en lem teğne bi'l-ems, gloss:onu dün hiç yokmuş gibi biçilmiş hale getirdik, source:10:24}. Kelimenin kendisi de Kur'an'da bir topluluk için kullanılır. Bir önceki kavimden sonra yaratılan bir neslin hikâyesinde, onları yakalayan çığlığın ardından şöyle denir: {ar:فَجَعَلْنَٰهُمْ غُثَآءًۭ, tr:fe-ce'alnâhum ğuŝâen, gloss:onları sel döküntüsüne çevirdik, source:23:41}. Fiil de kelime de aynıdır, ama burada ot yerine insanlar vardır.

Kaynaklar: 87:1 ٱسْمَ س م و B004; 87:1 ٱسْمَ و س م B003; 87:1 رَبِّ ر ب ب B008; 87:1 رَبِّ ر ب ب B007; 87:1 رَبِّ ر ب ب B012; 87:11 يَتَجَنَّبُهَا ج ن ب B006; 87:4 أَخْرَجَ خ ر ج B005; 87:4 أَخْرَجَ خ ر ج B002; 87:4 أَخْرَجَ خ ر ج B007; 87:4 ٱلْمَرْعَىٰ ر ع ي B001; 87:5 فَجَعَلَهُۥ ج ع ل B002; 87:5 غُثَآءً غ ث و B002; 87:5 غُثَآءً غ ث و B001; 87:5 أَحْوَىٰ ح و ي B006; 87:7 يَخْفَىٰ خ ف ي B004; 87:7 يَخْفَىٰ خ ف ي B003; 87:17 أَبْقَىٰٓ ب ق ي B005; 87:13 يَحْيَىٰ ح ي ي B002; 87:13 يَمُوتُ م و ت B003

## Ne ölü ne diri: kalan hayat

On üçüncü ayet ateşe gireni şöyle anlatır: {ar:ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:ŝumme lâ yemûtu fîhâ ve lâ yahyâ, gloss:sonra orada ne ölür ne yaşar, source:87:13}. Arapça iki uç arasındaki halleri ayrı ayrı adlandırır ve ayetin olumsuzladığı şeyi bu adlar belirginleştirir. Ölüm gücün bir şeyden çekilmesidir: {ar:أصل صحيح يدل على ذهاب القوة من الشيء, tr:aslun sahîhun yedullu alâ ẕehâbi'l-kuvveti mine'ş-şey', gloss:bir şeyden gücün gitmesini gösteren köktür, source:"م و ت,B001"}. Ayılınan bir baygınlık da bu kökle anılır: {ar:الموتة الذي يصرع من الجنون أو غيره ثم يفيق, tr:el-mûte elleẕî yusrau mine'l-cunûni ev ğayrihî ŝumme yufîk, gloss:mûte delilikten ya da başka bir şeyden yere yıkılıp sonra ayılmaktır, source:"م و ت,B009"}. Uyku da öyle: {ar:مات الرجل وهمد وهوم إذا نام, tr:mâte'r-raculu ve hemede ve hevveme iẕâ nâm, gloss:adam uyuduğunda mâte ve hemede denir, source:"م و ت,B012"}. Hayat ise fayda ve iyiliktir: {ar:ليس بفلان حياة أي ليس عنده نفع ولا خير, tr:leyse bi-fulânin hayâtun ey leyse indehû nef'un ve lâ hayr, gloss:falancada hayat yok yani onda ne fayda ne iyilik var, source:"ح ي ي,B013"}. Bu ifade dokuzuncu ayetteki "fayda" ve on yedinci ayetteki "hayırlı" kelimelerinin köklerini içerir. Diri bırakmak, sağ tutmak demektir: {ar:ويستحيون نساءكم أي يستبقونهن, tr:ve yestahyûne nisâekum ey yestebkûnehunn, gloss:kadınlarınızı diri bırakıyorlardı yani onları sağ tutuyorlardı, source:"ح ي ي,B006"}. Bu tanım "yaşamak" kökünü "kalmak" köküyle açıklar. Hakiki hayat da kalıcılıkla tanımlanır: {ar:الحيوان مقر الحياة وما له الحاسة وما له البقاء الأبدي, tr:el-hayevân makarru'l-hayâti ve mâ lehu'l-hâssetu ve mâ lehu'l-bekâu'l-ebediyy, gloss:hayevân hayatın yeri ve duyusu olan ve sonsuz kalıcılığı bulunandır, source:"ح ي ي,B003"}. Hayevân'ın, kayıtlı ikinci bir köke bağlanan bir anlamı da vardır: {ar:والحيوان ماء في الجنة لا يصيب شيئا إلا حي بإذن الله, tr:ve'l-hayevân mâun fi'l-cenneti lâ yusîbu şey'en illâ hayye bi-iẕnillâh, gloss:hayevân cennette bir sudur; dokunduğu her şey Allah'ın izniyle dirilir, source:"ح ي و,B003"}. Kalmak da yaşamak demektir: {ar:بقي الرجل زمانا طويلا أي عاش, tr:bakıye'r-raculu zemânen tavîlen ey âşe, gloss:adam uzun zaman kaldı yani yaşadı, source:"ب ق ي,B001"}. Ve yok olmaktan kurtarmaktır: {ar:العرب تقول للعدو إذا غلب البقية أي أبقوا علينا ولا تستأصلونا, tr:el-arabu tekûlu li'l-aduvvi iẕâ ğalebe el-bakıyye ey ebkû aleynâ ve lâ testa'sılûnâ, gloss:Araplar galip gelen düşmana bakıyye der yani bizi bırakın ve kökümüzü kazımayın, source:"ب ق ي,B003"}. Dünya ise yakın olduğu için bu adı alır: {ar:سميت الدنيا لدنوها, tr:summiyeti'd-dunyâ li-dunuvvihâ, gloss:dünyaya yakınlığından dolayı bu ad verilmiştir, source:"د ن و,B002"}.

Bu adlar on üçüncü ayetteki olumsuzlamanın neyi dışarıda bıraktığını gösterir. Ateştekinin gücü tümüyle çekilmez. Ayılınan bir baygınlığı ya da bir uykusu yoktur. Ama hayatın tanımı olan fayda ve iyilik de onda yoktur. On altıncı ve on yedinci ayet ise hayat kelimesini iki yere böler: yakın olduğu için dünya diye anılan hayat ve kalıcı olan ahiret. Düz bir anlatım on üçüncü ayeti yalnızca bir azap tasviri olarak okur. Kök ailesi ise onu surenin sonundaki seçimin bir ucu olarak gösterir. Yakın hayatı kalıcı olana tercih edenin vardığı yer, ne hayatın ne de ölümün olduğu bir yerdir.

Kur'an bu cümleyi kelimesi kelimesine başka bir sahnede, Musa'nın karşısındaki sihirbazların ağzından verir. Sihirbazlar secdeye kapanıp Harun'un ve Musa'nın Rabbine iman ettiklerini söyleyince Firavun onları el ve ayaklarını çaprazlama kesmekle tehdit eder ve şöyle der: {ar:وَلَتَعْلَمُنَّ أَيُّنَآ أَشَدُّ عَذَابًۭا وَأَبْقَىٰ, tr:ve le-ta'lemunne eyyunâ eşeddu azâben ve ebkâ, gloss:hangimizin azabının daha çetin ve daha kalıcı olduğunu bileceksiniz, source:20:71}. Firavun on yedinci ayetin "daha kalıcı" kelimesini kendi azabı için kullanır. Sihirbazlar ise ahiretin iki ucunu anlatır: {ar:إِنَّهُۥ مَن يَأْتِ رَبَّهُۥ مُجْرِمًۭا فَإِنَّ لَهُۥ جَهَنَّمَ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:innehû men ye'ti rabbehû mucrimen fe-inne lehû cehenneme lâ yemûtu fîhâ ve lâ yahyâ, gloss:kim Rabbine suçlu olarak gelirse ona cehennem vardır; orada ne ölür ne yaşar, source:20:74}. Ötekiler için de bunun karşılığını söylerler: {ar:وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ, tr:ve ẕâlike cezâu men tezekkâ, gloss:bu arınanın karşılığıdır, source:20:76}. Bu birkaç ayette surenin on üçüncü ve on dördüncü ayetleri yan yana gelir. Başka bir yerde inatçı zorba için {ar:وَيَأْتِيهِ ٱلْمَوْتُ مِن كُلِّ مَكَانٍۢ وَمَا هُوَ بِمَيِّتٍۢ, tr:ve ye'tîhi'l-mevtu min kulli mekânin ve mâ huve bi-meyyit, gloss:ölüm ona her yerden gelir ama o ölmez, source:14:17} denir. Bir başka yerde inkâr edenler için {ar:لَا يُقْضَىٰ عَلَيْهِمْ فَيَمُوتُوا۟, tr:lâ yukdâ aleyhim fe-yemûtû, gloss:haklarında ölmeleri için hüküm verilmez, source:35:36} denir. Ateştekiler bekçiye seslenip Rablerinin işlerini bitirmesini isterler, cevap ise şudur: {ar:إِنَّكُم مَّٰكِثُونَ, tr:innekum mâkiŝûn, gloss:siz burada kalacaksınız, source:43:77}. Bu "kalmak" fiili, selin benzetmesinde faydalı suyun yerde kalmasını anlatan fiildir. Aynı fiil iki ayrı yerde iki ayrı türden kalıcılığı anlatır. Hayatın gerçeği için ise {ar:وَإِنَّ ٱلدَّارَ ٱلْءَاخِرَةَ لَهِىَ ٱلْحَيَوَانُ, tr:ve inne'd-dâre'l-âhirete le-hiye'l-hayevân, gloss:ahiret yurdu ise asıl hayatın kendisidir, source:29:64} denir. Gerçek hayatı kaçıran kişi o gün şöyle der: {ar:يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى, tr:yekûlu yâ leytenî kaddemtu li-hayâtî, gloss:keşke hayatım için önceden bir şey gönderseydim der, source:89:24}. Sahte bir kalıcılık da teklif edilir. Şeytan Adem'e {ar:هَلْ أَدُلُّكَ عَلَىٰ شَجَرَةِ ٱلْخُلْدِ وَمُلْكٍۢ لَّا يَبْلَىٰ, tr:hel edulluke alâ şeceratı'l-huldi ve mulkin lâ yeblâ, gloss:sana ölümsüzlük ağacını ve eskimeyen bir mülkü göstereyim mi, source:20:120} der. İbrahim ise ölümü ve hayatı Rabbine bağlar: {ar:وَٱلَّذِى يُمِيتُنِى ثُمَّ يُحْيِينِ, tr:velleẕî yumîtunî ŝumme yuhyîn, gloss:beni öldürecek sonra diriltecek olan O'dur, source:26:81}.

Kaynaklar: 87:13 يَمُوتُ م و ت B001; 87:13 يَمُوتُ م و ت B009; 87:13 يَمُوتُ م و ت B012; 87:13 يَحْيَىٰ ح ي ي B013; 87:13 يَحْيَىٰ ح ي ي B006; 87:16 ٱلْحَيَوٰةَ ح ي ي B003; 87:16 ٱلْحَيَوٰةَ ح ي و B003; 87:17 أَبْقَىٰٓ ب ق ي B001; 87:17 أَبْقَىٰٓ ب ق ي B003; 87:16 ٱلدُّنْيَا د ن و B002

## Buluşmalar

İmgelerin çoğu, surenin son ayetinde adı geçen Musa'nın hikâyesinde buluşur. Musa uzakta bir ateş görür ve {ar:أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ecidu ale'n-nâri hudâ, gloss:ateşin başında bir yol gösteren bulurum, source:20:10} umuduyla ona yönelir. Uzaktan görülen ateşin sahnesi ile yol sahnesi burada aynı cümlededir. Ateşin başında önce seçim gelir: {ar:وَأَنَا ٱخْتَرْتُكَ, tr:ve ene'htertuk, gloss:seni ben seçtim, source:20:13}. Sonra namaz ve anma gelir: {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14}. Sonra gizli olan gelir: {ar:أَكَادُ أُخْفِيهَا, tr:ekâdu uhfîhâ, gloss:onu neredeyse gizli tutuyorum, source:20:15}. Başka bir anlatımda ateşin başında tesbih söylenir: {ar:وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve subhânallâhi rabbi'l-âlemîn, gloss:Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu sahnede surenin on ikinci ve on beşinci ayetleri arasındaki karşıtlık bir kişinin yolculuğunda çözülür. Aynı ateşe yaklaşan biri onun içine sokulmaz. Ateş ona yol, seçilmişlik, namaz ve anma verir. Surede bu iki son iki ayrı kişiye düşer: on ikinci ayetteki kişi ateşe girer, on beşinci ayetteki kişi namaz kılar. Kelimelerin harf benzerliği bu ayrılığı kulakta da duyurur.

İkinci büyük buluşma selin sahnesidir. Gökten inen suyun vadilerde {ar:بِقَدَرِهَا, tr:bi-kaderihâ, gloss:kendi ölçülerince, source:13:17} akması, ölçüp biçme sahnesini çağırır. Selin taşıdığı köpük, otlağın vardığı döküntüdür. İnsanların {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâr, gloss:ateşte üzerine yaktıkları şeyden, source:13:17} çıkan köpük ise ateşin sahnesine girer. Faydalı olanın yerde kalması da öğüdün ve kalıcılığın sahnesidir. Kurumuş otun tencerenin köpüğüyle aynı adı taşıması, bu iki köpüğün Arapçada zaten tek bir kelimede birleştiğini gösterir. Bu ayet surenin beşinci ayetinden on yedinci ayetine uzanan çizgiyi tek bir manzaraya sığdırır. Bir yanda giden döküntü, öbür yanda kalan fayda vardır.

Üçüncü buluşma, Musa'nın karşısındaki sihirbazların sahnesidir. Sihirbazlar secdeye kapanır. Firavun kendi azabının daha çetin ve {ar:وَأَبْقَىٰ, tr:ve ebkâ, gloss:ve daha kalıcı, source:20:71} olduğunu söyler. Sihirbazlar da onu {ar:لَن نُّؤْثِرَكَ, tr:len nu'ŝirak, gloss:seni asla tercih etmeyiz, source:20:72} diye reddeder, yalnızca {ar:هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:hâẕihi'l-hayâte'd-dunyâ, gloss:bu dünya hayatı, source:20:72} üzerinde hüküm verebileceğini söyler ve {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} der. Sonra suçlu için {ar:لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:lâ yemûtu fîhâ ve lâ yahyâ, gloss:orada ne ölür ne yaşar, source:20:74} der, iman edenler için {ar:ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:ed-derecâtu'l-ulâ, gloss:en yüce dereceler, source:20:75} der, ve hepsini {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76} sözüyle bağlar. Bu birkaç ayette seçim, kalıcı hayat, yükseklik ve yarılan tarlanın kelimeleri birlikte konuşur. Firavun'un "en yüce" iddiası da başka bir anlatımda bu sahneye eklenir. Surenin ikinci yarısı, on üçüncü ayetten on yedinci ayete kadar, neredeyse kelimesi kelimesine Musa'nın hikâyesindeki bir topluluğun ağzından gelmiştir. Son ayetin Musa'nın sayfalarını anması da bu yüzden önem taşır.

Dördüncü buluşma ot ile seçimdir. Dünya hayatının kuruyan ota benzetildiği ayetin hemen ardından kalıcı iyi işlerin daha hayırlı olduğu söylenir. Dünya hayatı başka bir yerde bir {ar:زَهْرَةَ, tr:zehrate, gloss:çiçek, source:20:131} olarak anılır, ve aynı ayet {ar:خَيْرٌۭ وَأَبْقَىٰ, tr:hayrun ve ebkâ, gloss:daha hayırlı ve daha kalıcı, source:20:131} diye biter. Otlağın sahnesi seçimin sahnesine bu yolla girer. Beşinci ayetteki ot ile on altıncı ayetteki tercih edilen hayat aynı nesnedir. Kalıcı olan ise ayıklanıp seçilen şeydir. Tarlanın sahnesi bu iki uç arasında bir yol açar. Kalıcı iyilik anlamına gelen kurtuluş kelimesi on dördüncü ayette, toprağı yaran çiftçinin kelimesiyle söylenir. Yabani ot kendi haline kalınca kurur ve selle gider. İşlenen toprağın ürünü ise büyür, hakkı verilir ve geriye kalan bir pay bırakır. Biri dünya tarlası, öbürü ahiret tarlasıdır.

Beşinci buluşma, yaratma fiillerinde zanaat ile bedenin birleşmesidir. İkinci ayetteki ikili hem yontulmuş oku hem de ceninin biçimlenmesini anlatır. Rahimden başlayan ayetin toprağın yağmurla titreşmesiyle bitmesi, beden ile otlağı da birbirine bağlar. Aynı aile, üçüncü ayetteki ölçmeyi pay ölçmeye de taşır, ve on altıncı ayetteki tercih bir pay seçimine döner. Değneği ateşte doğrultmanın fiili on ikinci ayetin fiilidir. Bu fiil aynı ateşin düzelten bir işi ile içine düşenin katlandığı bir işi olduğunu duyurur. Bu son bağ dilin yankısıdır, ayetin sözü değildir.

Bu buluşmalar surenin hareketini taşır. Sure tesbih emriyle ve yükseklikle açılır. Ölçen, yontan ve yol gösteren Rabbin işiyle devam eder. Yağmurun çıkardığı ve selin götürdüğü ot ile sona gelen bir ömür gösterir. Sonra sözün toplanıp unutulmamasına, sunulan öğüde ve öğüt karşısında ikiye ayrılan insanlara geçer. Biri ateşe girer ve ne ölü ne diri kalır. Öbürü arınır, Rabbinin adını anar ve namaz kılar, yani surenin başındaki emri yerine getirir. Ardından seçim gelir: yakın olan öne konmuştur, ama arkadan gelen daha hayırlı ve daha kalıcıdır. Sure, bu sözün ilk sayfalarda, ateşin başında namaz ve anma emrini alan Musa'nın ve Rabbinden kendisini puttan uzak tutmasını isteyen İbrahim'in sayfalarında yazılı olduğunu söyleyerek kapanır.

