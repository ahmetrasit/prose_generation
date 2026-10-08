Focus: 89:24. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_24/D.r13/context.md =====
# 89:24 — focus

يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى

Anchor translation (canonical reading, reference only):

“Keşke hayatım için önceden bir şeyler yapsaydım!” der.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | يَقُولُ | قَالَ | ق و ل | V |
| 2 | يَٰلَيْتَنِى | لَيْت |  | VOC;ACC;PRON |
| 3 | قَدَّمْتُ | قَدَّمَ | ق د م | V;PRON |
| 4 | لِحَيَاتِى | حَيَوٰة | ح ي ي | P;N;PRON |


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
- 89:6 أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ
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
- 89:24 ◀ focus يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى
- 89:25 فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- 89:26 وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ
- 89:27 يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- 89:28 ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- 89:29 فَٱدْخُلِى فِى عِبَٰدِى
- 89:30 وَٱدْخُلِى جَنَّتِى


===== _commentary/v16/work/89_24/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق و ل (root_001272) — identity root of يَقُولُ (w1)

- **B001** söze dökme — sözü sesle dile getirmek · söylenmiş söz veya sözlü ifade · söylenmiş söz için kullanılan adlar
  القول من النطق (maqayis)؛ قال يقول قولا وقولة ومقالا ومقالة (sihah)؛ القول والقيل واحد (mufradat)؛ المركب من الحروف المبرز بالنطق (mufradat)؛ القيل من القول اسم (ayn)
- **B002** konuşma organı — konuşma organı olan dil
  المقول اللسان (maqayis;ayn;sihah)
- **B003** çok sözlü kişi — çok konuşan, dili güçlü kişi
  رجل قولة وقوال كثير القول (maqayis)؛ رجل تقوالة أي منطيق وقوال وقوالة أي كثير القول (ayn)؛ رجل مقول ومقوال وقولة وقوال وتقوالة أي لسن كثير القول (sihah)
- **B004** sözü geçen yönetici unvanı — sözü geçen yerel hükümdar unvanı · bu unvanın çoğul adları · bu unvanın kadın için kullanılan biçimi
  المقول بلغة أهل اليمن القيل وهم المقاولة والأقيال والأقوال والواحد القيل (ayn)؛ القيل ملك من ملوك حمير دون الملك الأعظم والمرأة قيلة (sihah)؛ كأنه الذي له قول أي ينفذ قوله (sihah)
- **B005** yalan söyleme veya isnat etme [kalıp] — olmayan bir şeyi söyledi · ona yalan isnat etti · bana söylemediğim şeyi yükledi
  تقول باطلا أي قال ما لم يكن (ayn)؛ قولتني ما لم أقل وأقولتني ما لم أقل أي ادعيته علي (sihah)؛ تقول عليه أي كذب عليه (sihah)
- **B006** sözü üzerine alma [kalıp] — iyi ya da kötü bir sözü kendi üzerine aldı
  اقتال قولا أي اجتر إلى نفسه قولا من خير أو شر (ayn)
- **B007** dolaşımdaki söz — hakkında iyi veya kötü söz yayıldı · insanlar arasında yayılmış söz · dedikodu ve çokça dönen laf
  انتشرت له قالة حسنة أو قبيحة في الناس (ayn)؛ القالة القول الفاشي في الناس (ayn)؛ كثر فيه القيل والقال (ayn)؛ كثرت قالة الناس (sihah)؛ كثر القيل والقال (sihah)
- **B008** oyun sopası — oyunda küçük parçaya vurulan tahta sopa
  القال الخشبة التي تضرب بها القلة (sihah)
- **B009** müzakere etme [kalıp] — bir iş hakkında karşılıklı görüştük
  قاولته في أمره وتقاولنا أي تفاوضنا (sihah)
- **B010** hükmünü dayatma [kalıp] — üzerinde hüküm yürüttü, tahakküm etti
  اقتال عليه تحكم (sihah)
- **B011** sanma işlevli söyleme — söyleme fiilini sanmak gibi kurmak
  العرب تجري تقول وحدها في الاستفهام مجرى تظن في العمل (sihah)؛ بنو سليم يجرون متصرف قلت في غير الاستفهام أيضا مجرى الظن (sihah)
- **B012** içte kalmış söz [kalıp] — içte tasarlanıp henüz söylenmemiş anlam
  المتصور في النفس قبل الإبراز باللفظ قول (mufradat)؛ في نفسي قول لم أظهره (mufradat)
- **B013** görüş benimseme [kalıp] — bir görüş veya mezhebi benimsedi
  للاعتقاد نحو فلان يقول بقول أبي حنيفة (mufradat)
- **B014** durumuyla belli etme [kalıp] — durumuyla yeter olduğunu belli etti
  للدلالة على الشيء نحو قول الشاعر امتلأ الحوض وقال قطني (mufradat)
- **B015** içten önemseme [kalıp] — bir şeye içten önem verdi
  للعناية الصادقة بالشيء كقولك فلان يقول بكذا (mufradat)
- **B016** teknik tanım [kalıp] — bir şeyin teknik tanımı
  يستعمله المنطقيون في معنى الحد فيقولون قول الجوهر كذا وقول العرض كذا أي حدهما (mufradat)
- **B017** içe doğan anlam — içe doğan anlamın söz diye adlandırılması
  في الإلهام فإن ذلك لم يكن بخطاب ورد عليه بل كان ذلك إلهاما فسماه قولا (mufradat)

## ق د م (root_001207) — identity root of قَدَّمْتُ (w3)

- **B001** ayak — ayak
  القدم ما يطأ عليه الإنسان (ayn;tahdhib)؛ القدم واحد الأقدام (sihah)؛ القدم قدم الرجل وجمعه أقدام (mufradat)؛ قدم الإنسان معروفة ولعلها سميت بذلك لأنها آلة للتقدم والسبق (maqayis)
- **B002** önceden oluşmuş etki veya paye — öncül etki, iyilik veya saygın konum · önceden kazanılmış iyi paye · önceden işlenmiş kötülük · önder ve saygın kişi · hükümdar veya önder
  القدمة والقدم أيضا السابقة في الأمر وللكافرين قدم شر (ayn)؛ القدم أيضا السابقة في الأمر ولفلان قدم صدق أي أثرة حسنة (sihah)؛ قدم الصدق المنزلة الرفيعة والقدم السابقة وكل ما قدمت من خير والعمل الصالح واليد والمعروف والصنيعة والشرف القديم (tahdhib)؛ متقدم على فلان أي أشرف منه (mufradat)؛ لفلان قدم صدق أي شيء متقدم من أثر حسن والملك هو المقدم (maqayis)؛ رجل قدموس سيد وهو ذلك المعنى (maqayis-variant)
- **B003** eskilik ve önceden var olma — eskilik; sonradan oluşmama · eski; geçmiş zamana dayanan · eskiden; geçmiş zamanda · eski olan
  القدم مصدر القديم من كل شيء (ayn)؛ قدم الشيء فهو قديم والقدم خلاف الحدوث وقدما كان كذا (sihah)؛ القدم العتق مصدر القديم وقد قدم يقدم (tahdhib)؛ حديث وقديم والقدم وجود فيما مضى (mufradat)؛ القدم خلاف الحدوث وشيء قديم إذا كان زمانه سالفا (maqayis)؛ القدموس القديم وأصله من القدم (maqayis-variant)
- **B004** öne geçme, önde ilerleme veya erken davranma — öne geçmek; önde olmak · öne geçme ve ilerleme · ön taraf; önde · önüne geçmek; vaktinden önce davranmak · duraksamadan ileri gitmek
  قدم فلان قومه أي يكون أمامهم والقدم المضي أمام ويمضي قدما أي لا ينثني وقدام خلاف وراء والقدم ضد الأخر (ayn)؛ قدم أي تقدم وقدم بين يديه أي تقدم ومضى قدما لم يعرج ولم ينثن واستقدم وتقدم بمعنى ومقدم نقيض مؤخر (sihah)؛ القدم المضي وهو الإقدام وقدام خلاف وراء والقدم ضد أخر وقدم فلان فلانا إذا تقدمه ولا تقدموا معناه لا تتقدموا قبل الوقت (tahdhib)؛ به اعتبر التقدم والتأخر (mufradat)؛ أصل صحيح يدل على سبق وأصله مضى فلان قدما لم يعرج ولم ينثن ومقدمة الجيش أوله (maqayis)
- **B005** yolculuktan dönüş — yolculuktan dönmek; geri gelmek · yolculuktan dönüş; yolcunun geliş zamanı · yolculuktan dönenler
  القدوم الرجوع من السفر وقدم يقدم (ayn)؛ قدم من سفره قدوما ومقدما والقدام القادمون من سفر (sihah)؛ القدوم الإياب من السفر وقدم فلان من سفره يقدم قدوما (tahdhib)؛ من الباب قدم من سفره قدوما ويقال القدام القادمون من سفر (maqayis)
- **B006** cesaretle öne atılma ve gözüpeklik — gözüpeklik; cesaretle öne atılma · bir işe cesaretle girişmek · gözüpek, atılgan savaşçı · ileri! · gözüpek ve öne atılan kişi
  رجل قدم مقتحم للأشياء يتقدم الناس ويمضي في الحرب قدما (ayn)؛ أقدم على الأمر إقداما والإقدام الشجاعة وأقدم زجر للفرس والمقدام الكثير الإقدام على العدو (sihah)؛ أقدم على قرنه إقداما وقدما ومقدما إذا تقدم عليه بجرأة وضده الإحجام ورجل مقدام في الحرب جريء (tahdhib)؛ أقدم على الشيء إقداما وأقدم زجر للفرس ومضى القوم في الحرب اليقدمية (maqayis)
- **B007** ön bölüm veya ilk kesim — ordunun öncü birliği · gözün veya başın ön kısmı · alın önü ve perçem bölgesi · kuşun ön kanat telekleri · eyer takımının ön kısmı · deve veya ineğin öndeki iki meme başı · dağın öne çıkan burnu · yüzüstü düşmek
  مقدم العين ما يلي الأنف والمقدمة الناصية وما استقبلك من الجبهة والجبين وقادمة الرحل والقادمة الريشة التي تلي منكب الجناح (ayn)؛ قوادم الطير مقاديم ريشه وقيدوم الجبل أنف يتقدم منه وقيدوم كل شيء مقدمه وصدره ومقدمة الجيش أوله وقادمتا الناقة (sihah)؛ مقدمة الجيش الذين يتقدمون الجيش ومقدم العين ومقدم الرأس والمقدمة الناصية وقادمة الرحل وللناقة قادمان وقوادم ريش الطائر (tahdhib)؛ قادمة الرحل خلاف آخرته وقادمة من أطباء الناقة وقادم الإنسان رأسه وقوادم الطير ومقدمة الجيش أوله وقيدوم الجبل أنف يتقدم منه (maqayis)
- **B008** ahşap yontma keseri — ahşap yontma keseri
  القدوم مخفقة الحديدة التي ينحت بها الخشب (ayn)؛ القدوم التي ينحت بها مخففة ولا تقل قدوم بالتشديد (sihah)؛ القدوم التي ينحت بها وجمعها قدم واختتن إبراهيم بالقدوم قال قطعه بها (tahdhib)؛ مما شذ عن هذا الأصل القدوم الحديدة ينحت بها وهي معروفة (maqayis)
- **B009** belirli bir yer adı — belirli bir yer adı
  القدوم أيضا اسم موضع (sihah)؛ القدوم مكان (maqayis)
- **B010** bir işe yönelip onu amaçlamak [kalıp] — bir işe yönelip onu amaçlamak
  قدم فلان إلى أمر كذا أي قصد له ومنه وقدمنآ إلى ما عملوا قال الفراء والزجاج قدمنا عمدنا وقصدنا (tahdhib)

## ح ي ي (root_000383) — identity root of لِحَيَاتِى (w4)

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

## ح ي و (root_005544) — documented alternative for لِحَيَاتِى: Halîl b. Ahmed, el-Ayn; incelenmiş Furûk root_005544/B001 dalı

- **B001** yaşam ve canlı olma — 
  الحيوة كتبت بالواو؛ يقال حيي يحيا فهو حي؛ ولغة أخرى حي يحي والجميع حيوا (ayn)
- **B002** canlı varlık — 
  والحيوان كل ذي روح الواحد والجميع فيه سواء (ayn)
- **B003** cennette, değdiği her şeyi Tanrı'nın izniyle canlandıran su — 
  والحيوان ماء في الجنة لا يصيب شيئا إلا حي بإذن الله (ayn)
- **B004** yılan adının yaşam kökenli çözümlemesi — 
  والحَيَّة اشتقاقها من الحياة؛ هي في أصل البناء حيوة؛ ومن قال لصاحب الحَيّات حاي فهو فاعل من هذا البناء؛ ومن قال حواء على فعال فإنه يقول اشتقاق الحَيَّة من حَوَيْت لأنها تتحوى في التوائها (ayn)
- **B005** toprağı canlandıran bahar yağmuru — 
  والحَيَا مقصور حَيَا الربيع وهو ما تحيا به الأرض من الغيث (ayn)

## ECHO ق ل ل (root_001251) — for يَقُولُ (w1): withheld observed target; not identity

- **B001** azlık — az şey; azlık · azlık ve yetersizlik; yoksulluk ve düşüklük · az; az sayıda veya az miktarda · azalmak; az olmak · gözünde az göstermek · yoksullaşmak · az saymak; az görmek · hiç; ne azı ne çoğu · pek seyrek; hemen hemen hiç · yoksulluğa ve aşağılanmaya uğrasın · hiç malı olmamak · kendisi de ailesi de tanınmayan adam
  القل القليل؛ رماه الله بالقل والذل أي بالقلة والذلة (jamhara)؛ شيء قليل وجمعه قلل؛ قل الشيء يقل قلة؛ قلله في عينه؛ أقل افتقر؛ استقله عده قليلا (sihah)؛ قل الشيء يقل قلة فهو قليل وقلال؛ القل من الرجال الخسيس الدنيء؛ قليلة ولا كثيرة؛ قليلا ما يؤمنون؛ قاللت لفلان؛ تقاللت ما أعطاني (tahdhib)؛ القلة والكثرة يستعملان في الأعداد؛ يكنى بالقلة عن الذلة؛ يكنى بها تارة عن العزة؛ قليل يعبر به عن النفي (mufradat)
- **B002** bir şeyin tepesi veya başı — dağın tepesi; doruk · bir şeyin tepesi veya başı · insanın başı · sap ucunda topuzu bulunan kılıç
  القلة قلة الجبل وهي القطعة تستدير في أعلاه وهي القنة (jamhara)؛ القلة أعلى الجبل؛ قلة كل شيء أعلاه؛ رأس الإنسان قلة (sihah)؛ قلة كل شيء رأسه؛ قلة الجبل أعلاه؛ قبيعة السيف قلته؛ سيف مقلل (tahdhib)؛ قلة الجبل شعفه (mufradat)
- **B003** büyük küp — büyük küp; iri kap · belirli bir bölgenin iri küpleri · iki büyük küp veya bunların aldığı miktar
  القلة التي جاءت في الحديث مثل قلال هجر هي جرار عظام (jamhara)؛ القلة إناء للعرب كالجرة الكبيرة؛ قلال هجر شبيهة بالحباب (sihah)؛ قلتين يعني هذه الحباب العظام واحدتها قلة؛ قلال هجر؛ القلة منها تأخذ مزادة من الماء (tahdhib)؛ القلة ما أقله الإنسان من جرة وحب (mufradat)
- **B004** yük kaldırma, yükselme ve yola koyulma — küpü taşıyabilmek · bir şeyi taşımak; yüklenmek · ağır bulutları taşımak · uçuşa kalkmak; havalanmak · yüklenip yola çıkmak · yükselmek
  أقل الجرة أطاق حملها؛ استقلت السماء ارتفعت؛ استقل القوم مضوا وارتحلوا (sihah)؛ أقل الرجل الشيء واستقله إذا احتمله؛ استقل الطائر إذا نهض للطيران؛ استقل النبات أناف؛ استقل القوم إذا احتملوا ظاعنين؛ أقلت سحابا ثقالا أي حملت؛ قل إذا رفع وقل إذا علا (tahdhib)؛ أقلت سحابا ثقالا أي احتملته؛ أقللت كذا وجدته قليل المحمل (mufradat)
- **B005** korku veya öfkeden titreme — korku veya öfkeden doğan titreme · korku veya öfkeden titremeye tutulmak · öfkeden titremek
  القل الرعدة والانتفاض؛ أخذ فلانا القل إذا أخذته رعدة من فزع (jamhara)؛ القل بالكسر شبه الرعدة؛ أخذه قل من الغضب (sihah)؛ القل الرعدة؛ أخذه قل إذا أرعد من الغضب؛ إذا غضب قد استقل (tahdhib)
- **B006** oynatma ve kararsızca sallanma — sallanma, yerinde duramama ve hareket sesi · sallayıp oynatmak · sallanmak; yerinde duramamak · çevik; hızlı
  قلقل أي صوت وهو حكاية؛ قلقله قلقلة وقلقالا فتقلقل أي حركه فتحرك واضطرب (sihah)؛ القلقلة والتقلقل قلة الثبوت في المكان؛ يتقلقل في موضعه؛ القلق ألا يستقر الشيء في مكان واحد (tahdhib)؛ تقلقل الشيء إذا اضطرب؛ تقلقل المسمار؛ القلقلة حكاية صوت الحركة (mufradat)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:24, and ## Buluşmalar) =====
## Su: fışkıran, taşan, yukarıdan dökülen

İlk kelimenin kökü, karanlıktan önce suyun yarılmasını anlatır: {ar:انفجر الماء انفجارا تفتح, tr:infecera'l-mâu'nficâran tefettah, gloss:su fışkırdı, önü açıldı, source:"ف ج ر,B001"}. Fışkırma şöyle tarif edilir: {ar:إذا انبعث سائلا, tr:ize'nbe'ase sâilen, gloss:akarak fırladığında, source:"ف ج ر,B001"}. Kaya ya da toprak bir noktada çatlar, içerideki su bastırarak dışarı fırlar ve akmaya başlar. Kur'an bu sahneyi taşın içinden kurar. İsrailoğullarına kalplerinin taştan da katı olduğu söylenirken bazı taşlardan ırmakların fışkırdığı hatırlatılır: {ar:وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ, tr:ve inne mine'l-hicârati lemâ yetefecceru minhu'l-enhâr, gloss:taşların öylesi var ki içinden ırmaklar fışkırır, source:2:74}. Nuh'un tufanında aynı fiil yeryüzünü kaynaklara çevirir ve su ölçüsü önceden belirlenmiş bir iş üzerinde buluşur: {ar:وَفَجَّرْنَا ٱلْأَرْضَ عُيُونًۭا فَٱلْتَقَى ٱلْمَآءُ عَلَىٰٓ أَمْرٍۢ قَدْ قُدِرَ, tr:ve feccernâ'l-arda uyûnen fe'lteka'l-mâu alâ emrin kad kudir, gloss:yeri kaynaklar hâlinde fışkırttık, su takdir edilmiş bir iş üzerinde buluştu, source:54:12}. Kıyamette denizler fışkırtılır: {ar:وَإِذَا ٱلْبِحَارُ فُجِّرَتْ, tr:ve ize'l-bihâru fuccirat, gloss:denizler fışkırtıldığında, source:82:3}. Mekke'de inkârcılar Peygamber'den, arasından ırmaklar fışkırttığı bir bahçe isterler {source:17:91}. Kur'an bu işi cennette Allah'ın kullarına verir: {ar:عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا, tr:aynen yeşrabu bihâ ibâdu'llâhi yufeccirûnehâ tefcîrâ, gloss:Allah'ın kullarının içtiği, dilediklerince fışkırttıkları bir kaynak, source:76:6}.

Aynı kök günahı da adlandırır: {ar:الانبعاث والتفتح في المعاصي فجورا, tr:el-inbi'âsu ve't-tefettuhu fi'l-me'âsî fucûrâ, gloss:günahlara atılmak ve açılmak, fücur, source:"ف ج ر,B004"}. Suyun önünü yarıp fırlaması ile insanın günaha açılıp atılması aynı kelimeyle söylenir. Bu yüzden surenin geçmiş kavimleri anlatan bölümü bir sel gibi duyulur.

Dokuzuncu ayette Semûd kayayı vadide oymuştur: {ar:بِٱلْوَادِ, tr:bi'l-vâd, gloss:vadide, source:89:9}. Vadi selin yoludur: {ar:كل مفرج بين جبال وآكام وتلال يكون مسلكا للسيل, tr:kullu mufracin beyne cibâlin ve âkâmin ve tilâlin yekûnu meslekan li's-seyl, gloss:dağlar, tepeler ve tümsekler arasında selin geçtiği her açıklık, source:"و د ي,B005"}. Kök akmayı adlandırır: {ar:ودى أي سال, tr:vedâ ey sâl, gloss:aktı, source:"و د ي,B001"}. Kaya evler suyun indiği yatağa kurulmuştur. Kur'an'ın sel benzetmesinde vadiler kendi ölçüleri kadar akar ve sel kabarık bir köpük taşır: {ar:فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا فَٱحْتَمَلَ ٱلسَّيْلُ زَبَدًۭا رَّابِيًۭا, tr:fe-sâlet evdiyetun bi-kaderihâ fahtemele's-seylu zebeden râbiyâ, gloss:vadiler ölçülerince aktı, sel kabarık bir köpük taşıdı, source:13:17}. Köpük gider, insanlara yarayan yerde kalır. Âd da vadilerine doğru gelen bulutu yağmur sanmıştır. Hûd'un Ahkâf'ta kavmini uyarmasıyla başlayan sahnede {source:46:21} bulutu görünce şöyle derler: {ar:قَالُوا۟ هَٰذَا عَارِضٌۭ مُّمْطِرُنَا ۚ بَلْ هُوَ مَا ٱسْتَعْجَلْتُم بِهِۦ ۖ رِيحٌۭ فِيهَا عَذَابٌ أَلِيمٌۭ, tr:kâlû hâzâ âridun mumtırunâ, bel huve me'sta'celtum bih, rîhun fîhâ azâbun elîm, gloss:"Bu bize yağmur getiren bir bulut" dediler. Hayır, o acele istediğiniz şeydir: içinde acı bir azap olan bir rüzgâr, source:46:24}.

On birinci ayetin fiili suyun taşmasıdır: {ar:ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ, tr:ellezîne tağav fi'l-bilâd, gloss:o ülkelerde azanlar, source:89:11}. Arapçada sel için {ar:طغى السيل إذا جاء بماء كثير, tr:tağa's-seylu izâ câe bi-mâin kesîr, gloss:sel bol suyla gelince "taştı" denir, source:"ط غ ي,B002"}, su için de {ar:طغى الماء خروجه عن المقدار, tr:tuğyânu'l-mâi hurûcuhû ani'l-mikdâr, gloss:suyun taşması ölçüsünden çıkmasıdır, source:"ط غ ي,B002"} denir. Ayette anlam azgınlıktır. Yanında ölçüsünden çıkan, yatağını aşan su duyulur. Kur'an kelimeyi tufan için doğrudan kullanır: {ar:إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ, tr:innâ lemmâ tağa'l-mâu hamelnâkum fi'l-câriye, gloss:su taştığında sizi akıp giden gemide taşıdık, source:69:11}. On ikinci ayet taşkının sonucunu verir: {ar:فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ, tr:fe-ekserû fîhe'l-fesâd, gloss:oralarda bozgunu çoğalttılar, source:89:12}. Çoğalmak {ar:الكثرة نماء العدد, tr:el-kesretu nemâu'l-aded, gloss:çokluk, sayının büyümesidir, source:"ك ث ر,B001"} demektir, bozulmak da {ar:الفساد خروج الشيء عن الاعتدال, tr:el-fesâdu hurûcu'ş-şey'i ani'l-i'tidâl, gloss:fesat, bir şeyin dengeden çıkmasıdır, source:"ف س د,B001"}. Hacim büyür ve şeyler dengelerinden çıkar. Bozgunun tarifindeki "çıkış" suyun ölçüden çıkışıyla aynı kelimedir. Kur'an'da bozgun karaya ve denize yayılır: {ar:ظَهَرَ ٱلْفَسَادُ فِى ٱلْبَرِّ وَٱلْبَحْرِ, tr:zahera'l-fesâdu fi'l-berri ve'l-bahr, gloss:karada ve denizde bozgun ortaya çıktı, source:30:41}. Salih de Semûd'a, Âd'dan sonra yerleştirildikleri yeryüzünde ovalardan saraylar edinip dağları ev diye oyduklarını hatırlatır ve sonra şöyle der: {ar:وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ, tr:ve lâ ta'sev fi'l-ardı mufsidîn, gloss:yeryüzünde bozguncular olarak dolaşmayın, source:7:74}.

On üçüncü ayet taşkına yukarıdan karşılık verir: {ar:فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ, tr:fe-sabbe aleyhim rabbuke savte azâb, gloss:Rabbin de üzerlerine azap kamçısı yağdırdı, source:89:13}. Sabb, suyun fiilidir: {ar:صب الماء إراقته من أعلى, tr:sabbu'l-mâi irâkatuhû min a'lâ, gloss:suyu dökmek, onu yukarıdan akıtmaktır, source:"ص ب ب,B001"}. Vadiye inmek de bu fiille söylenir: {ar:صب في الوادي إذا انحدر فيه, tr:sabbe fi'l-vâdî izenhadera fîh, gloss:vadiye indi, oraya doğru aktı, source:"ص ب ب,B002"}. Aşağıda yatağını taşan suya yukarıdan dökülen bir şey karşılık verir. Dökülenin adı azaptır ve bu kelimenin harfleri tatlı suyu da adlandırır: {ar:العذب ضد الملح وكل مستسيغ من طعام أو شراب, tr:el-azbu diddu'l-milhi ve kullu mustesâğin min taâmin ev şarâb, gloss:azb, tuzlunun zıddıdır; boğazdan rahat geçen her yiyecek ve içecek, source:"ع ذ ب,B001"}. Âd'ın yağmur sandığı rüzgâr bu iki yüzü tek sahnede gösterir: beklenen tatlı su, gelen ise azaptır {source:46:24}.

Aynı su sahnesi surenin ikinci yarısında rahmet olarak döner. Kur'an insana yemeğine bakmasını söyler: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:suyu bol bol döktük, source:80:25}, {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:summe şekakne'l-arda şakkâ, gloss:sonra toprağı yardıkça yardık, source:80:26}. Fiil aynıdır, ama bu kez arkasından yarılan toprak ve biten yemek gelir. Surenin sınav sahnesindeki kelimeler bu yağmuru da taşır. İkram için {ar:كرم السحاب أتى بالغيث, tr:keruma's-sehâbu etâ bi'l-ğays, gloss:bulut cömert davrandı, yağmur getirdi, source:"ك ر م,B002"} denir. Rızık için {ar:وقد يسمى المطر رزقا, tr:ve kad yusemma'l-mataru rızkâ, gloss:yağmura da rızık denir, source:"ر ز ق,B003"} denir. Kur'an da şöyle der: {ar:وَفِى ٱلسَّمَآءِ رِزْقُكُمْ, tr:ve fi's-semâi rızkukum, gloss:rızkınız göktedir, source:51:22}. Ölçü için de {ar:ينزل المطر بمقدار, tr:yenzilu'l-mataru bi-mikdâr, gloss:yağmur ölçüyle iner, source:"ق د ر,B001"} denir. On altıncı ayette rızkın daraltılması, yağmurun ölçüyle inmesinin insanın gözünden görünen yüzüdür. Yirmi dördüncü ayetteki "hayatım" kelimesinin yanında yağmur duyulur: {ar:الحيا المطر لأنه يحيي الأرض بعد موتها, tr:el-hayâ el-mataru li-ennehû yuhyi'l-arda ba'de mevtihâ, gloss:hayâ yağmurdur, çünkü yeri ölümünden sonra diriltir, source:"ح ي ي,B002"}. Yirmi sekizinci ayetteki "dön" kelimesinin yanında da dökülüp yeniden gelen yağmur duyulur: {ar:الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث, tr:er-rec'u el-ğaysu ve huve'l-mataru li-ennehâ tuğîsu ve tasubbu summe terci'u fe-tuğîs, gloss:rec' yağmurdur, çünkü yağar, dökülür, sonra döner ve yine yağar, source:"ر ج ع,B006"}. Kur'an da göğe dönüşüyle yemin eder: {ar:وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ, tr:ve's-semâi zâti'r-rec', gloss:dönüp dönüp yağan göğe, source:86:11}. Ölü toprağa yağmur gönderilmesi, ölülerin çıkarılmasının örneğidir: {ar:كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:kezâlike nuhricu'l-mevtâ leallekum tezekkerûn, gloss:ölüleri de böyle çıkarırız; belki düşünüp hatırlarsınız, source:7:57}. Son kelime bu suyun ürününe varır: bahçeye ve bitkinin gürleşip çiçek açmasına: {ar:جن النبت جنونا إذا اشتد وخرج زهره, tr:cenne'n-nebtu cunûnen izeştedde ve harace zehruh, gloss:bitki gürleşip çiçeğini çıkarınca "cenne" denir, source:"ج ن ن,B011"}.

Surede suyun işleyişi bir ölçüye bağlanır. Ölçüsünde kalan su hayat verir, ölçüsünü aşan su süpürür. Âd, Semûd ve Firavun ölçüyü aşan taşkındır ve onlara yukarıdan azap dökülür. İnsana ölçülü rızık iner ve o, ölçünün kendisini aşağılanma sanır.

Kaynaklar: 89:1 وَٱلْفَجْرِ ف ج ر B001; 89:1 وَٱلْفَجْرِ ف ج ر B004; 89:9 بِٱلْوَادِ و د ي B001; 89:9 بِٱلْوَادِ و د ي B005; 89:11 طَغَوْا۟ ط غ ي B002; 89:12 فَأَكْثَرُوا۟ ك ث ر B001; 89:12 ٱلْفَسَادَ ف س د B001; 89:13 فَصَبَّ ص ب ب B001; 89:13 فَصَبَّ ص ب ب B002; 89:13 عَذَابٍ ع ذ ب B001; 89:15 فَأَكْرَمَهُۥ ك ر م B002; 89:16 فَقَدَرَ ق د ر B001; 89:16 رِزْقَهُۥ ر ز ق B003; 89:24 لِحَيَاتِى ح ي ي B002; 89:28 ٱرْجِعِىٓ ر ج ع B006; 89:30 جَنَّتِى ج ن ن B011

## Kan, yemin ve karşılık

Surenin birkaç kelimesi bir kan davasının araçlarını taşır. Bu bir aile imgesidir. Surenin kendisi bir cinayet anlatmaz. Beşinci ayetteki kasem kelimesinin kökü öldürülmüş birinin yakınları arasında paylaştırılan yeminlere dayanır: {ar:اليمين فالقسم وأصل ذلك من القسامة وهي الأيمان تقسم على أولياء المقتول, tr:el-yemîn fe'l-kasem, ve aslu zâlike mine'l-kasâme, ve hiye'l-eymânu tuksemu alâ evliyâi'l-maktûl, gloss:yemine kasem denir; aslı kasâmedir, yani maktulün velileri arasında paylaştırılan yeminler, source:"ق س م,B004"}. Sahnede bir kişi öldürülmüştür ve yakınları hakkı aramak için yemini aralarında bölüşür. Üçüncü ayetteki vetr kelimesinin yanında ödenmemiş kan duyulur: {ar:الوتر الذحل, tr:el-vetru'z-zahl, gloss:vetr, alınmamış kan öcüdür, source:"و ت ر,B002"}, {ar:الموتور الذي قتل له قتيل, tr:el-mevtûru'llezî kutile lehû katîl, gloss:mevtûr, yakını öldürülmüş kişidir, source:"و ت ر,B002"}. Aynı kök hakkı eksiltmeyi de anlatır: {ar:وتره حقه أي نقصه, tr:veterahû hakkahû ey nekasah, gloss:hakkını eksiltti, source:"و ت ر,B003"}. Kur'an bu fiili Allah'ın kullara davranışı için kullanır: {ar:وَلَن يَتِرَكُمْ أَعْمَٰلَكُمْ, tr:ve len yetirakum a'mâlekum, gloss:amellerinizden hiçbir şeyi eksiltmeyecektir, source:47:35}. Dokuzuncu ayetteki vadi kelimesinin kökü diyeti de adlandırır: {ar:وديت القتيل أديه دية إذا أعطيت ديته, tr:vedeytu'l-katîle edîhi diyeten izâ a'taytu diyeteh, gloss:maktulün diyetini verdim, source:"و د ي,B002"}. Kur'an diyeti yanlışlıkla öldürme hükmünde anar: {ar:وَدِيَةٌۭ مُّسَلَّمَةٌ إِلَىٰٓ أَهْلِهِۦٓ, tr:ve diyetun musellemetun ilâ ehlih, gloss:ailesine teslim edilecek bir diyet, source:4:92}.

Sekizinci ayetteki misl kelimesinin kökü ibret olsun diye verilen cezayı da adlandırır: {ar:نقمة تنزل بالإنسان فيجعل مثالا يرتدع به غيره, tr:nikmetun tenzilu bi'l-insâni fe-yuc'alu misâlen yerteduu bihî ğayruh, gloss:insanın başına inen ve başkalarının ondan çekinmesi için örnek yapılan ceza, source:"م ث ل,B002"}. Kur'an inkârcıların iyilikten önce kötülüğü acele istediklerini söyler ve onlardan önce bu örnek cezaların geçtiğini hatırlatır: {ar:وَقَدْ خَلَتْ مِن قَبْلِهِمُ ٱلْمَثُلَٰتُ, tr:ve kad halet min kablihimu'l-mesulât, gloss:onlardan önce ibret olacak cezalar gelip geçti, source:13:6}. Âd, Semûd ve Firavun bu örneklerdir. On dördüncü ayetteki mirsâd kelimesi de karşılığın hazırda tutulmasını anlatır: {ar:أنا لك مرصد بإحسانك حتى أكافئك به, tr:ene leke mursıdun bi-ihsânike hattâ ukâfieke bih, gloss:iyiliğini sana karşılık verene kadar hazırda tutarım, source:"ر ص د,B002"}, {ar:وإرصاد الانسان في المكافأة والخير, tr:ve irsâdu'l-insâni fi'l-mukâfeeti ve'l-hayr, gloss:irsâd, karşılık ve iyilik için de kullanılır, source:"ر ص د,B002"}. Gözcünün beklediği şey bir hesaptır. Karşılık kaybolmaz, yerinde durur.

Yirmi dördüncü ayetteki "hayatım" kelimesinin yanında da kısasın verdiği hayat duyulur: {ar:ولكم في القصاص حياة أي يرتدع بالقصاص, tr:ve lekum fi'l-kısâsı hayâtun ey yurtedeu bi'l-kısâs, gloss:kısasta sizin için hayat vardır, yani insanlar kısas sayesinde kötülükten geri durur, source:"ح ي ي,B013"}. Kur'an'daki hüküm şöyledir: {ar:كُتِبَ عَلَيْكُمُ ٱلْقِصَاصُ فِى ٱلْقَتْلَى, tr:kutibe aleykumu'l-kısâsu fi'l-katlâ, gloss:öldürülenler hakkında size kısas yazıldı, source:2:178}, {ar:وَلَكُمْ فِى ٱلْقِصَاصِ حَيَوٰةٌۭ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ, tr:ve lekum fi'l-kısâsı hayâtun yâ uli'l-elbâb, gloss:ey akıl sahipleri, kısasta sizin için hayat vardır, source:2:179}. Haksız yere öldürülenin velisine yetki verilir, ama öldürmede aşırı gitmesi yasaklanır {source:17:33}. Bu hükümler akıl sahiplerine söylenir, sure de yeminini akıl sahibine yöneltmişti. Surenin dizisinde bu imge şöyle ilerler: önce yemin, sonra ibret olan kavimler, sonra karşılığı hazırda tutan Rab. Son olarak yirmi beşinci ayet hiçbir insan velinin yerine getiremeyeceği bir karşılığı haber verir.

Kaynaklar: 89:3 ٱلْوَتْرِ و ت ر B002; 89:3 ٱلْوَتْرِ و ت ر B003; 89:5 قَسَمٌۭ ق س م B004; 89:8 مِثْلُهَا م ث ل B002; 89:9 بِٱلْوَادِ و د ي B002; 89:14 لَبِٱلْمِرْصَادِ ر ص د B002; 89:24 لِحَيَاتِى ح ي ي B013

## Geç gelen hatırlama, nefes ve hayat

Getirilen cehennemle birlikte insan hatırlar: {ar:يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ, tr:yevmeizin yetezekkeru'l-insânu ve ennâ lehu'z-zikrâ, gloss:o gün insan hatırlar; ama bu hatırlama ona ne fayda verir, source:89:23}. Tezekkür, geçmiş olanın peşinden gitmektir: {ar:التذكر طلب ما فات, tr:et-tezekkuru talebu mâ fât, gloss:tezekkür, kaçırılmış olanı aramaktır, source:"ذ ك ر,B003"}. Hatırlamak geriye uzanan bir el gibidir, ama uzandığı şey artık geçmiştir. Ennâ kelimesi "nereden" ve "nasıl" diye sorar: {ar:أنى معناه أين ومن أين ومن أي جهة وقد تكون بمعنى كيف, tr:ennâ ma'nâhu eyne ve min eyne ve min eyyi cihetin, ve kad tekûnu bi-ma'nâ keyfe, gloss:ennâ "nerede, nereden, hangi yönden" demektir; "nasıl" anlamına da gelebilir, source:"ء ن ي,B005"}. Aynı harflerden gelen fiil ise vaktin gelip gelmediğini söyler: {ar:ما أنى لك ولم يأن لك أي لم يحن, tr:mâ enâ leke ve lem ye'ni leke ey lem yehin, gloss:senin için vakit gelmedi, source:"ء ن ي,B003"}. Kur'an bu fiili hatırlamayla aynı cümlede, müminlere bir uyarı olarak kullanır: {ar:أَلَمْ يَأْنِ لِلَّذِينَ ءَامَنُوٓا۟ أَن تَخْشَعَ قُلُوبُهُمْ لِذِكْرِ ٱللَّهِ, tr:e-lem ye'ni li'llezîne âmenû en tahşea kulûbuhum li-zikri'llâh, gloss:iman edenlerin kalplerinin Allah'ı anarak yumuşamasının vakti gelmedi mi, source:57:16}. Bu ayetin vakti hâlâ açıktır. Surenin ayetindeki vakit ise kapanmıştır. Kur'an aynı soruyu başka yerlerde de sorar: {ar:أَنَّىٰ لَهُمُ ٱلذِّكْرَىٰ وَقَدْ جَآءَهُمْ رَسُولٌۭ مُّبِينٌۭ, tr:ennâ lehumu'z-zikrâ ve kad câehum resûlun mubîn, gloss:apaçık bir elçi gelmişken onlara hatırlama nereden, source:44:13}, {ar:فَأَنَّىٰ لَهُمْ إِذَا جَآءَتْهُمْ ذِكْرَىٰهُمْ, tr:fe-ennâ lehum izâ câethum zikrâhum, gloss:o saat gelince hatırlamaları onlara ne fayda verir, source:47:18}. Uzanmanın mesafesini de gösterir: {ar:وَأَنَّىٰ لَهُمُ ٱلتَّنَاوُشُ مِن مَّكَانٍۭ بَعِيدٍۢ, tr:ve ennâ lehumu't-tenâvuşu min mekânin baîd, gloss:o uzak yerden uzanıp ona ulaşmaları nasıl mümkün olur, source:34:52}. Aynı ifade cehennemin gösterildiği bir sahnede de geçer: {ar:يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ, tr:yevme yetezekkeru'l-insânu mâ seâ, gloss:o gün insan çalışıp ettiklerini hatırlar, source:79:35}. Bu sahne de büyük felaketin gelmesiyle başlar {source:79:34}.

Hatırlayan insanın tek dileği önden göndermektir: {ar:يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى, tr:yekûlu yâ leytenî kaddemtu li-hayâtî, gloss:"Keşke hayatım için önceden bir şey gönderseydim" der, source:89:24}. Önden gönderilen şey varılacak yere önceden ulaştırılan azıktır: {ar:القدم السابقة وكل ما قدمت من خير والعمل الصالح, tr:el-kadem es-sâbika ve kullu mâ kaddemte min hayrin ve'l-amelu's-sâlih, gloss:kadem, önceden yapılmış iyilik, önden gönderdiğin her hayır ve salih ameldir, source:"ق د م,B002"}. Kur'an bu bakışı müminlere bir emir olarak verir: {ar:وَلْتَنظُرْ نَفْسٌۭ مَّا قَدَّمَتْ لِغَدٍۢ, tr:ve'l-tenzur nefsun mâ kaddemet li-ğad, gloss:her can yarın için önden ne gönderdiğine baksın, source:59:18}. Kıyamette de aynı bakış bir pişmanlığa döner: {ar:يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ وَيَقُولُ ٱلْكَافِرُ يَٰلَيْتَنِى كُنتُ تُرَٰبًۢا, tr:yevme yenzuru'l-mer'u mâ kaddemet yedâhu ve yekûlu'l-kâfiru yâ leytenî kuntu turâbâ, gloss:o gün kişi elleriyle önden gönderdiğine bakar, kâfir de "keşke toprak olsaydım" der, source:78:40}. Ayrıca bkz. {source:75:13}, {source:82:5}. Keşke sözü başka sahnelerde de vardır. Zalim ellerini ısırarak şöyle der: {ar:يَٰلَيْتَنِى ٱتَّخَذْتُ مَعَ ٱلرَّسُولِ سَبِيلًۭا, tr:yâ leytenî'ttehaztu mea'r-resûli sebîlâ, gloss:keşke elçiyle birlikte bir yol tutsaydım, source:25:27}. Kitabı sol eline verilen de şöyle der: {ar:يَٰلَيْتَنِى لَمْ أُوتَ كِتَٰبِيَهْ, tr:yâ leytenî lem ûte kitâbiyeh, gloss:keşke kitabım bana verilmeseydi, source:69:25}. Surede insanın üç sözü vardır: "bana ikram etti", "beni aşağıladı" ve "keşke". İlk ikisi sınavı yanlış okur, üçüncüsü bunu çok geç fark eder.

"Hayatım" kelimesi bu fark edişin içeriğidir. Hayat kelimesi büyümeden ahirete kadar geniş bir alanı kapsar: {ar:الحياة تستعمل للقوة النامية والحساسة والعاقلة والأخروية, tr:el-hayâtu tusta'melu li'l-kuvveti'n-nâmiyeti ve'l-hassâseti ve'l-âkıleti ve'l-uhreviyye, gloss:hayat, büyüyen, duyan, düşünen güç için ve ahiret hayatı için kullanılır, source:"ح ي ي,B001"}. Kur'an asıl hayatın hangisi olduğunu söyler: {ar:وَإِنَّ ٱلدَّارَ ٱلْءَاخِرَةَ لَهِىَ ٱلْحَيَوَانُ, tr:ve inne'd-dâra'l-âhirete le-hiye'l-hayevân, gloss:asıl hayat ahiret yurdudur, source:29:64}. İnsan bu kelimeyi "benim hayatım" diye ilk kez doğru yere koyar, ama o zaman da gönderilecek bir şeyi kalmamıştır. Ölüm anında geri gönderilip iyi iş yapmayı isteyen de "hayır" cevabını alır {source:23:100}.

Bu pişman sesin hemen ardından başka bir canla konuşulur. Nefs kelimesinin kökü nefesin içeriden dışarı çıkmasıdır: {ar:التنفس خروج النسيم من الجوف, tr:et-teneffusu hurûcu'n-nesîmi mine'l-cevf, gloss:teneffüs, havanın içeriden dışarı çıkmasıdır, source:"ن ف س,B001"}. Can da bedeni yaşatan şeydir: {ar:النفس الروح الذي به حياة الجسد, tr:en-nefsu'r-rûhu'llezî bihî hayâtu'l-ced, gloss:nefs, bedenin onunla yaşadığı ruhtur, source:"ن ف س,B011"}. Nefes çıkar ve geri döner. Kur'an canın alınışını ve geri bırakılışını uykuda ve ölümde gösterir: {ar:ٱللَّهُ يَتَوَفَّى ٱلْأَنفُسَ حِينَ مَوْتِهَا وَٱلَّتِى لَمْ تَمُتْ فِى مَنَامِهَا, tr:Allâhu yeteveffe'l-enfuse hîne mevtihâ ve'lletî lem temut fî menâmihâ, gloss:Allah canları ölümleri sırasında, ölmeyenleri de uykularında alır, source:39:42}. Zalimlere ölüm anında melekler ellerini uzatıp şöyle der: {ar:أَخْرِجُوٓا۟ أَنفُسَكُمُ, tr:ahricû enfusekum, gloss:canlarınızı çıkarın, source:6:93}. Aynı ayette karşılık da adlandırılır: {ar:ٱلْيَوْمَ تُجْزَوْنَ عَذَابَ ٱلْهُونِ, tr:el-yevme tuczevne azâbe'l-hûn, gloss:bugün aşağılayıcı bir azapla cezalandırılacaksınız, source:6:93}. Can köprücük kemiklerine dayandığında da yön Rabbe doğrudur {ar:كَلَّآ إِذَا بَلَغَتِ ٱلتَّرَاقِىَ, tr:kellâ izâ beleğati't-terâkıy, gloss:hayır, can köprücük kemiklerine dayandığında, source:75:26}, {ar:إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمَسَاقُ, tr:ilâ rabbike yevmeizini'l-mesâk, gloss:o gün sürülüş Rabbinedir, source:75:30}. Surenin sonundaki can ise ne zorla çıkarılır ne de sürülür. Ona seslenilir ve dönmesi söylenir. Kur'an canın başka hâllerini de anar: kötülüğü emreden can {source:12:53} ve kendini kınayan can {source:75:2}. Bu surede seslenilen ise o çalkantılardan sonra durulmuş olandır.

Kaynaklar: 89:23 يَتَذَكَّرُ ذ ك ر B003; 89:23 وَأَنَّىٰ ء ن ي B003; 89:23 وَأَنَّىٰ ء ن ي B005; 89:24 قَدَّمْتُ ق د م B002; 89:24 لِحَيَاتِى ح ي ي B001; 89:27 ٱلنَّفْسُ ن ف س B001; 89:27 ٱلنَّفْسُ ن ف س B011

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

