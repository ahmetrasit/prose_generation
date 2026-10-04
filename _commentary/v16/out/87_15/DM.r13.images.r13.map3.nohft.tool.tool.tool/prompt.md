Focus: 87:15. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/87_15/D.r13/context.md =====
# 87:15 — focus

وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ

Anchor translation (canonical reading, reference only):

Ve Rabbinin adını andı, ardından namaz kıldı.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَذَكَرَ | ذَكَرَ | ذ ك ر | CONJ;V |
| 2 | ٱسْمَ | ٱسْم | س م و | N |
| 3 | رَبِّهِۦ | رَبّ | ر ب ب | N;PRON |
| 4 | فَصَلَّىٰ | صَلَّىٰ | ص ل و | CONJ;V |


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
- 87:13 ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- 87:14 قَدْ أَفْلَحَ مَن تَزَكَّىٰ
- 87:15 ◀ focus وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ
- 87:16 بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- 87:17 وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ
- 87:18 إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ
- 87:19 صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ


===== _commentary/v16/work/87_15/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ذ ك ر (root_000516) — identity root of وَذَكَرَ (w1)

- **B001** erkek cinsiyet ve erkek yavru doğurma — erkek · erkek üreme organı · erkeğin üreme organı çevresindeki organlar · erkekler veya erkeklik · erkek yavru doğurdu · çoğunlukla erkek yavru doğuran dişi · erkek yapılı kadın veya dişi deve · gebe için kolay doğum ve erkek çocuk dileği
  الذكر خلاف الأنثى (sihah;tahdhib;mufradat)؛ الذكورة والذكور والذكران جمع الذكر (ayn;tahdhib;mufradat)؛ أذكرت ولدت ذكرا والمذكار تلد الذكور (maqayis;ayn;sihah;tahdhib;mufradat)
- **B002** sert, keskin ve güçlü olma — demirin en sert ve kuru türü · keskin ve sağlam kılıç · kılıcın veya erkeğin keskinliği · kalın ve sert otlar · güçlü, yiğit ve onurlu adam · çetin ve korkutucu gün, yol veya felaket · şiddetli yağmur, sağlam söz veya güçlü şiir · tehlikeli, yalnız erkeklerin geçtiği veya sert ot bitiren ıssız ova
  سيف مذكر ذو ماء وذو ذكر صارم (maqayis;sihah;mufradat)؛ الذكر من الحديد أيبسه وأشده (ayn;sihah;tahdhib)؛ ذكور البقل ما غلظ منه (maqayis;sihah;tahdhib;mufradat)؛ رجل ذكر قوي شجاع ويوم وطريق وداهية ومطر ذكر للشدة (tahdhib)
- **B003** akılda tutma ve yeniden hatırlama — hatırladı veya aklında tuttu · aklında · hatırlama · ezberlemek için çalışma · belleği güçlü, yiğit veya iyi anılan adam
  ذكرت الشيء خلاف نسيته (maqayis;sihah)؛ الذكر الحفظ للشيء وهو مني على ذكر (ayn;tahdhib)؛ ذكر بالقلب والتذكر طلب ما فات (ayn;tahdhib;mufradat)
- **B004** bir şeyi sözle anma [kalıp] — sözle anma · insanların arkasından kusurlarını söyleme
  ثم حمل عليه الذكر باللسان (maqayis)؛ الذكر جري الشيء على لسانك (ayn;tahdhib)؛ ذكرته بلساني وبقلبي (sihah)؛ كل قول يقال له ذكر وذكر باللسان (mufradat)؛ يذكر الناس أي يغتابهم ويذكر عيوبهم (tahdhib)
- **B005** Tanrı'yı kulluk amacıyla anma — kulluk amacıyla anma, yakarış, övgü, şükretme ve itaat · Tanrı'yı kulluk, övgü ve yakarışla anma
  الذكر الصلاة والدعاء والثناء (ayn;tahdhib)؛ الذكر قراءة القرآن والتسبيح والدعاء والشكر والطاعة (tahdhib)؛ ولذكر الله أكبر واذكروا الله (mufradat)
- **B006** indirildiğine inanılan kutsal kitap — dinin ayrıntılarını bildiren kutsal kitap
  الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر (ayn;tahdhib)؛ القرآن والكتب المتقدمة والزبور من بعد الذكر (mufradat)
- **B007** onur, iyi ün ve saygınlık — onur, iyi ün ve övgü · belleği güçlü, yiğit veya iyi anılan adam
  الذكر العلاء والشرف (maqayis)؛ الذكر الشرف والصوت (ayn;tahdhib)؛ الذكر الصيت والثناء وذي الذكر أي ذي الشرف (sihah)؛ وإنه لذكر لك ولقومك أي شرف (mufradat)
- **B008** hakkı gösteren yazılı belge [kalıp] — hakkı gösteren yazılı belge · yazılı hak belgeleri
  ذكر الحق الصك وجمعه ذكور حقوق (ayn;tahdhib)؛ يقال ذكور حق (ayn;tahdhib)
- **B009** hatırlatma, hatırlamayı sağlayan araç ve sıkça anma — hatırlatma, öğüt alma veya sıkça anma · hatırlatıcı · hatırlatma · ona o şeyi hatırlattı
  الذكرى اسم للتذكير والتذكير مجاوز (ayn)؛ التذكرة ما تستذكر به الحاجة (sihah)؛ الذكرى بمعنى الذكر وبمعنى التذكير (tahdhib)؛ التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر (mufradat)

## س م و (root_000745) — identity root of ٱسْمَ (w2)

- **B001** fiziksel ya da toplumsal yükselme — yükselme, yücelme · yükselmek, yücelmek · bakışı yukarı yönelmek · toplumdaki yeri ve değeri yükselmiş olmak · gururla başını ve bakışını kaldırmak
  أصل يدل على العلو؛ سموت إذا علوت (maqayis)؛ سما الشيء يسمو سموا أي ارتفع (ayn)؛ السمو الارتفاع والعلو (sihah)؛ سما الشيء يسمو سموا وهو ارتفاعه، ويقال للحسيب والشريف قد سما (tahdhib)؛ أصله من السمو وهو الذي به رفع ذكر المسمى (mufradat)
- **B002** yükselerek uzaktan beliren görünüş — uzakta yükselip görünür olmak · bir şeyin yüksekte görünen gövdesi veya dış çizgisi · ayın ince yayının ufuktan yükselen görünüşü
  سما لي شخص ارتفع حتى استثبته؛ سماوة الهلال وكل شيء شخصه (maqayis)؛ سما لي شيء؛ سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا (ayn)؛ سما لي شخص؛ سماوة كل شيء شخصه (sihah)؛ سما لي شيء؛ سماوته أي شخصه؛ سماوة الهلال شخصه (tahdhib)؛ السماوة الشخص العالي؛ وسما لي شخص (mufradat)
- **B003** erkek devenin dişi deve sürüsüne atılıp aralarına girmesi [kalıp] — erkek devenin dişi deve sürüsüne atılıp aralarına girmesi
  سما الفحل سطا على شوله سماوة (maqayis)؛ سما الفحل إذا تطاول على شوله (ayn;tahdhib)؛ سما الفحل إذا سطا على شوله سماوة (sihah)؛ سما الفحل على الشول سماوة لتخلله إياها (mufradat)
- **B004** üstteki gök veya örtü ve buna bağlı üstten gelen ya da üstte bulunan şeyler — gök, tavan veya bir şeyin üst yanı · yağmur · bulut · yağmurla çıkan veya yerden yükselen bitki · atın sırtı veya üst yanı · evin tavanı · her şeyin en üst yanı
  العرب تسمى السحاب سماء والمطر سماء؛ السماء سقف البيت وكل عال مطل سماء؛ يسموا النبات سماء (maqayis)؛ السماء كل ما علاك فأظلك؛ السماء المطر؛ السماء ظهر الفرس؛ سماوة البيت سقفه (sihah)؛ السماء سقف كل شيء وكل بيت؛ السماء السحاب؛ السماء المطر (tahdhib)؛ سماء كل شيء أعلاه؛ سمي المطر سماء؛ سمي النبات سماء (mufradat)
- **B005** ad, adlandırma ve ad ya da nitelik bakımından denklik — bir şeyi tanıtan ad · birine bir ad vermek veya onu o adla çağırmak · bir adı edinmek ve o adla anılmak · aynı adı taşıyan kişi, adaş · aynı adı veya niteliği hak eden denk · varlıkları tanıtan tekli veya birleşik sözler ve anlamlar
  أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى (maqayis)؛ الاسم أصل تأسيسه السمو؛ سميت وأسميت وتسميت (ayn)؛ سميت فلانا زيدا؛ هذا سمي فلان؛ الاسم مشتق من سموت لأنه تنويه ورفعة (sihah)؛ الاسم مشتق من السمو وهو الرفعة؛ تنويها على الدلالة على المعنى (tahdhib)؛ الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى؛ سميا أي نظيرا له يستحق اسمه (mufradat)
- **B006** av için ıssız araziye çıkma ve buna bağlı avcı kullanımları — avlanmak için kır ve çöl arazisine çıkmak · avcılar · av hayvanını bulup avlamak üzere aramak · avcının sıcak zeminde beklerken giydiği koruyucu çorap
  خرج القوم للصيد في قفار الأرض وصحاريها قلت سموا وهم السماة أي الصيادون (ayn;tahdhib)؛ السماة الصيادون؛ سموا واستموا إذا خرجوا للصيد (sihah)؛ يستمي الوحش أي يطلبها؛ المسماة جورب الصياد (tahdhib)
- **B007** yarışma, övünerek boy ölçüşme ve karşı koyma — birbiriyle yarışmak ve karşı koymak · övünerek yarışma, boy ölçüşme ve karşı koyma · kimsenin kendisiyle yarışamadığı veya boy ölçüşemediği kişi
  فلان لا يسامى؛ تساموا أي تباروا؛ قد علا من ساماه (sihah)؛ معنى تساميها تباريها وتعارضها؛ المساماة المفاخرة (tahdhib)
- **B008** insanlar arasında yayılan iyi ün — insanlar arasında yayılan iyi ün veya iyi söz
  ذهب صيته في الناس وسماه، أي صوته في الخير لا في الشر (tahdhib)

## ر ب ب (root_000532) — identity root of رَبِّهِۦ (w3)

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

## ص ل و (root_000879) — identity root of فَصَلَّىٰ (w4)

- **B001** ateşin yakıcı sıcaklığına maruz kalma ve ateşle işleme — ateşe girip onun yakıcı sıcaklığını çekmek · ateşin yanında ısınmak · eti ateşte pişirmek · ateşte pişirilmiş · birini ateşe atıp yakmak · ateşi besleyen yakacak; ateşte pişirme · değneği ateşte yumuşatıp düzeltmek · bir işin güçlüğünü ve yorgunluğunu çekmek · onun sertliğine kimse yanaşamaz
  صليت العود بالنار (maqayis); اصطليت بالنار (maqayis;sihah); الصلا النار وصلى الكافر نارا (ayn); صليت اللحم شويته (ayn;sihah;tahdhib); الصلاء يقال للوقود وللشواء (mufradat); صلي بالأمر إذا قاسى حره وشدته (sihah;tahdhib)
- **B002** başkası için iyilik dileme; esirgeme, övme ve değer verme — başkası için iyilik ve esenlik dileme · biri için iyilik dilemek, onu övmek veya esirgenmesini istemek · Tanrı'nın esirgemesi, övmesi, bağışlaması ve değer vermesi · meleklerin bağışlanma ve iyilik dilemesi
  الصلاة وهي الدعاء (maqayis;sihah); صلوات الرسول للمسلمين دعاؤه لهم (ayn); الصلاة من الله تعالى الرحمة (maqayis;sihah;tahdhib); صلوات الله حسن ثنائه عليهم وقيل مغفرته لهم (ayn); صلاة الملائكة الاستغفار (ayn;tahdhib;mufradat); صلاة الله للمسلمين تزكيته إياهم (mufradat)
- **B003** ayakta durma, eğilme ve yere kapanma bölümleri olan kurallı tapınma — namaz · namazı bütün gerek ve koşullarını yerine getirerek kılmak
  الصلاة التي جاء بها الشرع من الركوع والسجود وسائر حدود الصلاة (maqayis); الصلاة واحدة الصلوات المفروضة (sihah); الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib); الصلاة التي هي العبادة المخصوصة أصلها الدعاء (mufradat); إقامة الصلاة (mufradat)
- **B004** yakalamak için kurulan tuzak — av için kurulan tuzak · avı veya başka hedefleri yakalayan tuzaklar · birini yıkıma düşürmek için gizlice düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis); المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد (ayn); المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib); صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة (tahdhib)
- **B005** sırtın ortası ve kuyruk kökünün iki yanı — sırtın orta bölümü veya kuyruk kökünün iki yanı · kuyruk kökünün iki yanı · doğum sırasında kuyruk kökü çevresinin açılması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn); كل أنثى إذا ولدت انفرج صلاها (ayn); الصلوين وهما مكتنفا الذنب من الناقة وغيرها (tahdhib); أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها وقرب نتاجها (tahdhib)
- **B006** yarışta birincinin hemen ardındaki ikinci — yarışta birincinin ardından gelen ikinci · yarışta liderin hemen ardından ikinci gelmek
  قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه (ayn); المصلى تالي السابق (sihah); السابق الأول والمصلي الثاني (tahdhib); يكون عند صلا الأول (tahdhib)
- **B007** tapınma yeri; kilise — Yahudilerin kiliseleri veya bir din topluluğunun tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn); الصلوات كنائس اليهود (tahdhib); قيل إنها مواضع صلوات الصابئين (tahdhib); يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B008** üzerinde dövme yapılan geniş taş — üzerinde malzeme dövülen geniş taş · dövme taşı
  الصلاية الفهر (sihah); الصلاءة بالهمز مثله (sihah); الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib); الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B009** iri başaklı, develerin otladığı bir bitki — iri başaklı, develerin otladığı bir bitki · bu bitkinin yetiştiği arazi
  الصليان نبت (ayn;tahdhib); له سنمة عظيمة كأنها رأس القصبة (ayn); له سبطة عظيمة كأنها رأس القصبة (tahdhib); تسميها العرب خبزة الإبل (ayn;tahdhib)

## و س م (root_001650) — documented alternative for ٱسْمَ: Kûfeli dilciler ve Sa‘leb; İbnü’l-Enbârî’nin aktarımı

- **B001** tanıtıcı fiziksel iz koyma, iz ve araç — bir şeyi tanıtıcı bir iz bırakarak işaretlemek · yakma veya kesme yoluyla bırakılmış tanıtıcı iz · tanınmayı sağlayan görünür işaret · üzerine tanıtıcı işaret konmuş · hayvan damgalamaya yarayan kızgın demir · kendine tanınacağı bir işaret edinmek · alt bölümü pirinçle süslenmiş zırh
  ووسمت الشيء وسما: أثرت فيه بسمة (maqayis;sihah)؛ الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي (ayn)؛ أثر كية، إما كية أو قطع في أذنه أو قرمة تكون علامة له (tahdhib)؛ الميسم المكواة أو الشيء الذي يوسم به الدواب (ayn;sihah;tahdhib)
- **B002** belirtiden karakter veya durum sezme — bir kimsede iyilik ya da kötülük belirtisi görüp niteliğini sezmek · duruma işaret eden belirtileri okuyup sonuç çıkaranlar · üzerinde iyilik ya da kötülük belirtisi bulunan
  الناظرين في السمة الدالة (maqayis)؛ توسمت فيه الخير والشر أي رأيت فيه أثرا (ayn)؛ فلان موسوم بالخير، وقد توسمت فيه الخير أي تفرست (sihah)؛ توسمت في فلان خيرا أي رأيت فيه أثرا منه، وتوسمت فيه الخير أي تفرست (tahdhib)
- **B003** toprağı bitkilendiren yılın ilk yağmuru — toprağı bitkilendiren yılın veya ilkbaharın ilk yağmuru · ilk yağmuru alıp etkisini taşıyan toprak · ilk yağmurun çıkardığı otu aramak
  الوسمى أول المطر لأنه يسم الأرض بالنبات (maqayis)؛ الوسمي أول مطر السنة يسم الأرض بالنبات، وأرض موسومة أصابها الوسمي (ayn)؛ الوسمي مطر الربيع الأول لأنه يسم الأرض بالنبات، والأرض موسومة (sihah)؛ سمي الوسمي من المطر وسميا لأنه يسم الأرض بالنبات فيصير فيها أثرا في أول السنة (tahdhib)
- **B004** belirlenmiş toplu buluşma zamanı ve yeri — kutsal ziyaret için belirlenmiş toplu buluşma zamanı ve yeri · eski Arap pazarlarının belirli toplanma zamanları ve yerleri · belirlenmiş toplu buluşmaya katılmak
  وسمى موسم الحاج موسما لأنه معلم يجتمع إليه الناس (maqayis)؛ موسم الحج موسما لأنه معلم يجتمع فيه وكذلك مواسم أسواق العرب (ayn;tahdhib)؛ موسم الحاج مجمعهم، سمي بذلك لأنه معلم يجتمع إليه (sihah)؛ وسم الناس: شهدوا الموسم (maqayis;sihah)
- **B005** kişide görünen yerleşik güzellik ve zarafet — güzellik; kişide görünen hoşluk · yüzü güzel ve hoş görünümlü · güzel ve hoş görünümlü kadın · üzerinde güzellik ve zarafet etkisi bulunan kadın · kişide görünen güzellik ve hoşluk · güzelleşmek ve hoş bir görünüş kazanmak · birini güzellikte geçmek
  فلانة ذات ميسم إذا كان عليها أثر الجمال، والوسامة الجمال (maqayis)؛ ذات ميسم وجمال وميسمها أثر الجمال فيها وهي وسيمة (ayn)؛ الميسم الجمال، وفلان وسيم أي حسن الوجه، ووسم الرجل وسامة ووساما (sihah)؛ فلانة لذات ميسم وميسمها أثر الجمال والعتق، والوسامة والميسم الحسن، والوسيم الثابت الحسن (tahdhib)
- **B006** yaprakları boya olarak kullanılan bitki — yaprakları boya olarak kullanılan bitki veya küçük ağaç
  الوسم والوسمة الواحدة شجرة ورقها خضاب (ayn;tahdhib)؛ الوسمة والعظلم يختضب به (sihah)

## ECHO ر ب و (root_000537) — for رَبِّهِۦ (w3): withheld observed target; not identity

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

## ECHO ص ل ي (root_000880) — for فَصَلَّىٰ (w4): withheld observed target; not identity

- **B001** ayakta durma, eğilme ve yere kapanmalı yükümlü tapınma — ayakta durma, eğilme ve yere kapanma bölümleri olan yükümlü tapınma
  الصلاة التي جاء بها الشرع من الركوع والسجود (maqayis)؛ الصلاة واحدة الصلوات المفروضة (sihah)؛ الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib)؛ الصلاة التي هي العبادة المخصوصة (mufradat)
- **B002** iyilik dileme; özneye göre esirgeme, övme veya aklama — iyilik dileme; özneye göre esirgeme, övme veya bağışlanma isteme · onun için iyilik dilemek, onu esirgemek ya da aklamak · Tanrı'nın kullarını esirgemesi, övmesi veya aklaması · göksel görevlilerin iyilik ve bağışlanma dilemesi · ölen kişi için iyilik dileme
  الصلاة وهي الدعاء (maqayis)؛ صلوات الرسول للمسلمين دعاؤه لهم وذكرهم (ayn)؛ الصلاة من الله تعالى الرحمة (sihah)؛ الصلاة من الملائكة دعاء واستغفار ومن الله سبحانه رحمة (tahdhib)؛ الصلاة الدعاء والتبريك والتمجيد (mufradat)
- **B003** ateşin veya benzer bir sıkıntının şiddetine uğramak; birini ateşe sokmak [kalıp] — ateşe girip yakıcı sıcağını çekmek · onu ateşe sokmak · ateşin başında ısınmak · bir işin ağır sıkıntısını çekmek · birinin kötülüğüne uğramak · onun sertliğini ve gücünü göze alamamak
  أحدهما النار وما أشبهها من الحمى (maqayis)؛ صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها (ayn)؛ صلي الرجل نارا إذا أدخلته النار (sihah)؛ من يصلى في النار أي يلزم النار (tahdhib)؛ صلي بالنار وبكذا أي بلي بها واصطلى بها (mufradat)
- **B004** ateş yakıtı; ateşte pişirme veya ısıyla düzeltme — ateşi tutuşturan ve başında ısınılan yakıt · ateşte pişirilmiş yiyecek · odun ya da ateş · eti ateşte pişirmek · ateşte pişmiş · değneği ateş üstünde döndürerek yumuşatıp doğrultmak · ateşin üstüne kurulan ocak taşları
  الصلاء ما يصطلى به وما يذكى به النار ويوقد (maqayis)؛ صليت اللحم صليا شويته (ayn;sihah;tahdhib)؛ صلى عصاه إذا أدارها على النار يثقفها (ayn;tahdhib)؛ الصلاء يقال للوقود وللشواء (mufradat)
- **B005** av yakalamak için kurulan kapan — av veya zararlı canlılar için kurulan kapanlar · av yakalamak için kurulan kapan · birini yok oluşa düşürecek bir düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis)؛ المصلاة أن تنصب شركا ونحوه (ayn)؛ المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib)
- **B006** sırtın ortası ve kuyruk dibinin iki yanı — sırtın ortası veya kuyruk dibi ile kuyruk sokumunun iki yanı · kuyruk dibinin iki yanı · doğumda kuyruk dibi bölgesinin açılması · devenin yavrusunun kuyruk dibi bölgesine inmesi ve doğumun yaklaşması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn)؛ انفرج صلاها (ayn)؛ الصلوين مكتنفا الذنب (tahdhib)؛ أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها (tahdhib)
- **B007** yarışta önderin hemen ardındaki ikinci at — yarışta önderin hemen ardındaki ikinci at · atın önder atın hemen ardından gelmesi
  أتى الفرس على أثر الفرس السابق قيل قد صلى وجاء مصليا (ayn)؛ المصلى تالي السابق (sihah)؛ السابق الأول والمصلي الثاني (tahdhib)
- **B008** tapınma yeri, özellikle Yahudi tapınağı — Yahudi tapınakları veya genel olarak tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn)؛ الصلوات كنائس اليهود (tahdhib)؛ يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B009** üzerinde madde dövülen geniş taş — üzerinde koku maddesi veya başka maddeler dövülen geniş taş · üzerinde madde dövülen geniş taş
  الصلاية الفهر (sihah)؛ الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib)؛ الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B010** iri başaklı deve yemi bitkisi — iri başaklı, develere yem olan bitki · bu iri başaklı bitkinin yetiştiği yer
  الصليان نبت على فعلان ويقال فعليان له سنمة عظيمة (ayn)؛ الصليان نبت له سبطة عظيمة (tahdhib)؛ تسميها العرب خبزة الإبل (ayn;tahdhib)

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 87:15, and ## Buluşmalar) =====
## Uzaktan görülen ateş

On ikinci ayet bedbahtı {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:elleẕî yasle'n-nâra'l-kubrâ, gloss:o en büyük ateşe girecek olan, source:87:12} diye tanıtır. "Ateş" kelimesi ışıkla aynı köktendir: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûru ve'n-nâru summiyâ bi-ẕâlike min tarîkati'l-idâe, gloss:nur da nâr da aydınlatma yönünden bu adı almıştır, source:"ن و ر,B001"}. Arapça bir ateşe varmanın birkaç yolunu ayrı ayrı adlandırır. Uzakta görülen ateşe yönelinir: {ar:تنورت نارا قصدت إليها, tr:tenevvertu nâran kasadtu ileyhâ, gloss:bir ateşe yöneldim, source:"ن و ر,B003"}, {ar:تنورت النار من بعيد: تبصرتها, tr:tenevvertu'n-nâra min baîd tebassartuhâ, gloss:ateşi uzaktan seçtim, source:"ن و ر,B003"}. Ateş yol işareti olarak yakılır: {ar:كانوا ينورون في الجاهلية ليهتدى ويقتدى بها, tr:kânû yunevvirûne fi'l-câhiliyyeti li-yuhtedâ ve yuktedâ bihâ, gloss:cahiliyede yol bulunsun ve izlensin diye ateş yakarlardı, source:"ن و ر,B005"}. Bu ifade üçüncü ayetteki "yol gösterdi" fiilinin kökünü içerir. Yol işaretinin adı da {ar:المنار: علم الطريق, tr:el-menâr alemu't-tarîk, gloss:menâr yolun işaretidir, source:"ن و ر,B005"} diye verilir ve yedinci ayetteki "bilir" fiilinin köküne bağlanır. Ateşte ısınılır: {ar:الصلاء ما يصطلى به وما يذكى به النار ويوقد, tr:es-salâu mâ yustalâ bihî ve mâ yuẕkâ bihi'n-nâru ve yûkad, gloss:salâ ısınılan ve ateşin tutuşturulduğu şeydir, source:"ص ل ي,B004"}. Ya da kişi ateşe sokulur ve yakıcılığına katlanır: {ar:صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها, tr:saliye'l-kâfiru nâran fe-huve yaslâhâ ey kâsâ harrahâ ve şiddetehâ, gloss:kâfir ateşe girdi yani sıcaklığına ve şiddetine katlandı, source:"ص ل ي,B003"}. Et de ateşte kızartılır: {ar:صليت اللحم صليا شويته, tr:saleytu'l-lahme salyen şeveytuh, gloss:eti ateşte kızarttım, source:"ص ل ي,B004"}. الكبرى ise {ar:كبر كل شيء عظمه, tr:kibru kulli şey'in izamuh, gloss:her şeyin kibri onun büyüklüğüdür, source:"ك ب ر,B001"}.

يصلى fiili ص ل ي kökündendir. On beşinci ayetteki فَصَلَّىٰ ise ص ل و kökündendir. Harfleri aynı kalıba oturur ama iki ayrı köktür, ve aralarındaki yakınlık bir yankıdır, kimlik değildir. Yine de sure bu yankıyı iki karşıt kişiye bölüştürür. Biri ateşe girer, öbürü Rabbinin adını anıp namaz kılar. Ateşe varmanın yolları arasındaki fark burada önem kazanır. Uzaktan görülüp yol bulmak için yönelinen ateş ile içine sokulup katlanılan ateş aynı nesnedir, ama ona giden kişinin işi farklıdır.

Kur'an bu farkı surenin son ayetinde anılan Musa'nın hikâyesinde sahneler. Musa bir ateş görür ve ailesine şöyle der: {ar:ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:imkuŝû innî ânestu nâran leallî âtîkum minhâ bi-kabesin ev ecidu ale'n-nâri hudâ, gloss:burada kalın; ben bir ateş gördüm; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösteren bulurum, source:20:10}. Başka bir anlatımda amacı ısınmaktır: {ar:لَّعَلَّكُمْ تَصْطَلُونَ, tr:leallekum tastalûn, gloss:belki ısınırsınız, source:27:7}. Bir başka anlatımda ateşi {ar:مِن جَانِبِ ٱلطُّورِ, tr:min cânibi't-tûr, gloss:Tur'un yanından, source:28:29} görür. Bu ifadede on birinci ayetteki kökün "yan" anlamı geçer. Ateşe vardığında kendisine seslenilir: {ar:أَنۢ بُورِكَ مَن فِى ٱلنَّارِ وَمَنْ حَوْلَهَا وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:en bûrike men fi'n-nâri ve men havlehâ ve subhânallâhi rabbi'l-âlemîn, gloss:ateşin içindeki ve çevresindeki kutlu kılındı; Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu seslenişte birinci ayetteki tesbih ateşin başında söylenir. Hikâyenin bir başka anlatımında ses ona şöyle der: {ar:وَأَنَا ٱخْتَرْتُكَ فَٱسْتَمِعْ لِمَا يُوحَىٰٓ, tr:ve ene'htertuke fe'stemi' li-mâ yûhâ, gloss:seni ben seçtim; vahyolunanı dinle, source:20:13}, ve sonra {ar:فَٱعْبُدْنِى وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:fa'budnî ve ekımi's-salâte li-ẕikrî, gloss:bana kulluk et ve beni anmak için namazı kıl, source:20:14}. Musa'nın ateşe yolculuğu namaz ve anma ile biter. Bu, surenin on beşinci ayetindeki kişinin yaptığı iştir. Kur'an insanların yaktığı küçük ateşi de anar: {ar:أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ, tr:e-fe-raeytumu'n-nâra'lletî tûrûn, gloss:yaktığınız ateşi gördünüz mü, source:56:71}. Hükmü de verir: {ar:نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا لِّلْمُقْوِينَ, tr:nahnu cealnâhâ teẕkiraten ve metâan li'l-mukvîn, gloss:onu bir hatırlatma ve çölde kalanlara bir geçimlik yaptık, source:56:73}. Küçük ateş bir öğüttür. Surenin dokuzuncu ayetindeki öğütten yüz çeviren ise on ikinci ayetteki büyük ateşe girer.

Ateşe sokulmanın işleyişini Kur'an kızartma diliyle anlatır: {ar:كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا, tr:kullemâ nadicet culûduhum beddelnâhum culûden ğayrahâ, gloss:derileri piştikçe onları başka derilerle değiştiririz, source:4:56}. Allah ayetlere sırt çeviren biri için {ar:سَأُصْلِيهِ سَقَرَ, tr:se-uslîhi sekar, gloss:onu Sekar'a sokacağım, source:74:26} der, ve o ateşin niteliği şudur: {ar:لَا تُبْقِى وَلَا تَذَرُ, tr:lâ tubkî ve lâ teẕer, gloss:ne bir şey bırakır ne de bir şeyi kendi haline koyar, source:74:28}. Bu ifadede on yedinci ayetteki "kalıcı" kelimesinin kökü olumsuz bir fiilde geçer. Sekar'dakilere oraya neden girdikleri sorulduğunda cevapları şudur: {ar:قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ, tr:kâlû lem neku mine'l-musallîn, gloss:namaz kılanlardan değildik dediler, source:74:43}. Bir başka surede ateş için surenin kendi kelimeleri kullanılır: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}, {ar:وَسَيُجَنَّبُهَا ٱلْأَتْقَى, tr:ve se-yucennebuhe'l-etkâ, gloss:en sakınan ondan uzak tutulacaktır, source:92:17}. Bu surede en bedbaht öğütten uzak durur. Orada ise en sakınan ateşten uzak tutulur. Aynı fiil yön değiştirir. Ateşin büyüklüğü başka yerlerde de anılır: {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4}. Bir başka yerde öğütten yüz çeviren için {ar:فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ, tr:fe-yuazzibuhullâhu'l-azâbe'l-ekber, gloss:Allah onu en büyük azapla cezalandırır, source:88:24} denir. Musa'ya ateşin başında gösterilen ise başka bir büyüklüktür: {ar:لِنُرِيَكَ مِنْ ءَايَٰتِنَا ٱلْكُبْرَى, tr:li-nuriyeke min âyâtine'l-kubrâ, gloss:sana en büyük ayetlerimizden göstermek için, source:20:23}.

Kaynaklar: 87:12 ٱلنَّارَ ن و ر B001; 87:12 ٱلنَّارَ ن و ر B003; 87:12 ٱلنَّارَ ن و ر B005; 87:12 يَصْلَى ص ل ي B004; 87:12 يَصْلَى ص ل ي B003; 87:12 ٱلْكُبْرَىٰ ك ب ر B001; 87:3 فَهَدَىٰ ه د ي B001; 87:15 فَصَلَّىٰ ص ل و B003

## Yükseklik: yükselten ad ve alçak hayat

Sure yükseklikle açılır. "Ad" kelimesinin س م و kökündeki asıl anlamı yükselmektir: {ar:أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى, tr:aslu ismin sumuvvun ve huve mine'l-uluvvi li-ennehû tenvîhun ve delâletun ale'l-ma'nâ, gloss:ismin aslı sümüvdür ve yücelikten gelir; çünkü bir şeyi anıp yükseltir ve anlamı gösterir, source:"س م و,B005"}. {ar:الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى, tr:el-ismu mâ yu'rafu bihî ẕâtu'ş-şey'i ve asluhû sumuvvun bihî rufia ẕikru'l-musemmâ, gloss:isim bir şeyin kendisinin tanındığı şeydir; aslı sümüvdür; adlandırılanın anılışı onunla yükselir, source:"س م و,B005"}. Kök, ufukta beliren bir karaltıyı da anlatır: {ar:سما لي شخص ارتفع حتى استثبته, tr:semâ lî şahsun irtefea hattâ'steŝbettuh, gloss:bir karaltı yükseldi de onu iyice seçtim, source:"س م و,B002"}. Ufuktan ayrılan hilali de anlatır: {ar:سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا, tr:semâvetu'l-hilâli şahsuhû iẕe'rtefea ani'l-ufuki şey'en, gloss:hilalin semâvesi ufuktan biraz yükseldiğinde görünen biçimidir, source:"س م و,B002"}. "En yüce" kelimesinin kökü aynı yükseklikle tanımlanır: {ar:أصل واحد يدل على السمو والارتفاع, tr:aslun vâhidun yedullu ale's-sumuvvi ve'l-irtifâ, gloss:yücelik ve yükseklik bildiren tek köktür, source:"ع ل و,B001"}. "Gel" demek olan تعال de bu köktendir: {ar:تعال أصله أن يدعى الإنسان إلى مكان مرتفع, tr:teâle asluhû en yud'a'l-insânu ilâ mekânin murtefi', gloss:teâlin aslı insanın yüksek bir yere çağrılmasıdır, source:"ع ل و,B006"}. On beşinci ayetteki "anmak" fiilinin kökü de şerefi taşır: {ar:الذكر العلاء والشرف, tr:eẕ-ẕikru'l-alâu ve'ş-şeref, gloss:zikir yücelik ve şereftir, source:"ذ ك ر,B007"}. Birinci ayetin "ad", "en yüce" ve on beşinci ayetin "andı" kelimeleri böylece aynı yöne, yukarıya bakar.

Tesbih bu yükseltmenin içeriğini verir: {ar:التسبيح وهو تنزيه الله من كل سوء, tr:et-tesbîh ve huve tenzîhullâhi min kulli sû', gloss:tesbih Allah'ı her kötülükten uzak tutmaktır, source:"س ب ح,B002"}. Aynı kökte ihtişam da vardır: {ar:سبحات وجه ربنا يعني جلاله وعظمته ونوره, tr:subuhâtu vechi rabbinâ ya'nî celâlehû ve azametehû ve nûrah, gloss:Rabbimizin yüzünün subuhâtı celali azameti ve nurudur, source:"س ب ح,B003"}. Bu ifade on ikinci ayetteki "ateş"in kökü olan nur kelimesini içerir. On ikinci ayetteki الكبرى'nın kökü Allah'ı yüceltme sözünü verir: {ar:التكبير يقال لتعظيم الله تعالى بقولهم الله أكبر, tr:et-tekbîr yukâlu li-ta'zîmillâhi teâlâ bi-kavlihimullâhu ekber, gloss:tekbir Allah'ı "Allah en büyüktür" diyerek yüceltmektir, source:"ك ب ر,B009"}. Aynı kök sahiplenilen büyüklüğü de verir: {ar:الكبر العظمة وكذلك الكبرياء, tr:el-kibr el-azametu ve keẕâlike'l-kibriyâ, gloss:kibir büyüklüktür; kibriyâ da öyle, source:"ك ب ر,B006"}. Yüksekliğin kendisi de bozulabilir: {ar:علا ملك في الأرض أي طغى وتعظم, tr:alâ melikun fi'l-ardi ey tağâ ve teazzama, gloss:bir hükümdar yeryüzünde yükseldi yani azdı ve büyüklük tasladı, source:"ع ل و,B003"}. Öbür uçta on altıncı ayetin الدنيا'sı durur. Bu kelime alçak olan ve daha az değerli olandır: {ar:يعبر بالأدنى تارة عن الأصغر وتارة عن الأول وتارة عن الأقرب, tr:yuabbaru bi'l-ednâ târaten ani'l-asğari ve târaten ani'l-evveli ve târaten ani'l-akrab, gloss:ednâ bazen daha küçük olanı bazen ilk olanı bazen en yakın olanı anlatır, source:"د ن و,B002"}. {ar:الدني من الرجال الضعيف الدون, tr:ed-deniyyu mine'r-ricâl ed-daîfu'd-dûn, gloss:insanların denîsi zayıf ve aşağı olandır, source:"د ن و,B003"}.

Surenin iki ucunda bu iki kelime durur. Birinci ayet "en yüce" ile başlar, on altıncı ayet "en alçak" ya da "en yakın" olanla bir seçimi gösterir. Düz bir anlatımda bunlar yalnızca iki sıfattır. Kök aileleri ise onları bir eksenin iki ucu olarak duyurur. Adı anılan Rab yükseltilir. Tercih edilen hayat ise adı gereği alçak ve yakındır.

Kur'an bu ekseni bir sahnede kurar. Musa'nın hikâyesini anlatan bölümde Firavun halkını toplayıp şöyle seslenir: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe-kâle ene rabbukumu'l-a'lâ, gloss:ben sizin en yüce rabbinizim dedi, source:79:24}. Bu, birinci ayetin iki kelimesinin bir yaratık tarafından sahiplenilmesidir, ve "yeryüzünde yükselip azmak" anlamının kendisidir. Aynı surede birkaç ayet sonra hüküm verilir: {ar:فَأَمَّا مَن طَغَىٰ, tr:fe-emmâ men tağâ, gloss:azana gelince, source:79:37}, {ar:وَءَاثَرَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:ve âŝera'l-hayâte'd-dunyâ, gloss:ve dünya hayatını tercih edene, source:79:38}. Yüksekliği sahiplenen ile yakın hayatı tercih eden aynı kişidir. Musa sihirbazlarla karşılaştığında içinde bir korku duyar ve Allah ona şöyle der: {ar:قُلْنَا لَا تَخَفْ إِنَّكَ أَنتَ ٱلْأَعْلَىٰ, tr:kulnâ lâ tehaf inneke ente'l-a'lâ, gloss:korkma; üstün olan sensin dedik, source:20:68}. Aynı sahnede iman eden sihirbazlar kendilerine {ar:فَأُو۟لَٰٓئِكَ لَهُمُ ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:fe-ulâike lehumu'd-derecâtu'l-ulâ, gloss:işte onlar için en yüce dereceler vardır, source:20:75} denir. Gökler için de {ar:تَنزِيلًۭا مِّمَّنْ خَلَقَ ٱلْأَرْضَ وَٱلسَّمَٰوَٰتِ ٱلْعُلَى, tr:tenzîlen mimmen halaka'l-arda ve's-semâvâti'l-ulâ, gloss:yeri ve yüce gökleri yaratandan indirilmiştir, source:20:4} denir. Vahyin getiricisi için {ar:ذُو مِرَّةٍۢ فَٱسْتَوَىٰ, tr:ẕû mirretin fe'stevâ, gloss:güç sahibidir; doğrulup durdu, source:53:6} ve {ar:وَهُوَ بِٱلْأُفُقِ ٱلْأَعْلَىٰ, tr:ve huve bi'l-ufuki'l-a'lâ, gloss:o en yüksek ufuktaydı, source:53:7} denir. Ufukta yükselen bir karaltı, kökün kendi sahnesidir. Malını verip arınan kişinin amacı da şöyle anlatılır: {ar:إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ, tr:ille'btiğâe vechi rabbihi'l-a'lâ, gloss:yalnızca en yüce Rabbinin rızasını istemek için, source:92:20}. Adın yükseltilmesi bir mekânda da anlatılır: {ar:فِى بُيُوتٍ أَذِنَ ٱللَّهُ أَن تُرْفَعَ وَيُذْكَرَ فِيهَا ٱسْمُهُۥ يُسَبِّحُ لَهُۥ فِيهَا, tr:fî buyûtin eẕinallâhu en turfea ve yuẕkera fîhe'smuhû yusebbihu lehû fîhâ, gloss:Allah'ın yükseltilmesine ve içlerinde adının anılmasına izin verdiği evlerde onu tesbih ederler, source:24:36}. Bu tek ayet surenin birinci ve on beşinci ayetlerini, yani yükseltmeyi, adı, anmayı ve tesbihi bir arada tutar. Peygamber'e de {ar:وَرَفَعْنَا لَكَ ذِكْرَكَ, tr:ve rafa'nâ leke ẕikrak, gloss:senin anılışını yükselttik, source:94:4} denir. Allah'ın kendisi için ise {ar:فَتَعَٰلَى ٱللَّهُ ٱلْمَلِكُ ٱلْحَقُّ, tr:fe-teâlallâhu'l-meliku'l-hakk, gloss:gerçek hükümdar olan Allah yücedir, source:20:114} denir. Birinci ayetteki emrin bir benzeri başka bir yerde de geçer: {ar:فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ, tr:fe-sebbih bi'smi rabbike'l-azîm, gloss:büyük Rabbinin adıyla tesbih et, source:56:74}. Bir başka emir de okumayı, adı, Rabbi ve yaratmayı birleştirir: {ar:ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ, tr:ikra' bi'smi rabbike'lleẕî halak, gloss:yaratan Rabbinin adıyla oku, source:96:1}. Bu emirde surenin birinci, ikinci ve altıncı ayetlerinin kelimeleri bir aradadır.

Kaynaklar: 87:1 ٱسْمَ س م و B005; 87:1 ٱسْمَ س م و B002; 87:1 ٱلْأَعْلَى ع ل و B001; 87:1 ٱلْأَعْلَى ع ل و B006; 87:1 ٱلْأَعْلَى ع ل و B003; 87:15 وَذَكَرَ ذ ك ر B007; 87:1 سَبِّحِ س ب ح B002; 87:1 سَبِّحِ س ب ح B003; 87:12 ٱلْكُبْرَىٰ ك ب ر B009; 87:12 ٱلْكُبْرَىٰ ك ب ر B006; 87:16 ٱلدُّنْيَا د ن و B002; 87:16 ٱلدُّنْيَا د ن و B003

## Tesbih, anma, namaz: sureyi açan ve kapayan iş

Birinci ayetin emri olan {ar:سَبِّحِ ٱسْمَ رَبِّكَ, tr:sebbihi'sme rabbik, gloss:Rabbinin adını tesbih et, source:87:1} on beşinci ayette bir kişinin yaptığı iş olarak geri döner: {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve ẕekera'sme rabbihî fe-sallâ, gloss:Rabbinin adını anıp namaz kıldı, source:87:15}. Arapça bu üç fiili, tesbihi, anmayı ve namazı, tek bir uygulama olarak ele alır. Tesbih nafile anma ve namazdır: {ar:السبحة التطوع من الذكر والصلاة, tr:es-subha et-tetavvuu mine'ẕ-ẕikri ve's-salât, gloss:subha nafile anma ve namazdır, source:"س ب ح,B001"}. {ar:التسبيح عاما في العبادات قولا كان أو فعلا أو نية, tr:et-tesbîhu âmmen fi'l-ibâdâti kavlen kâne ev fi'len ev niyye, gloss:tesbih söz iş ya da niyet olarak bütün ibadetler için genel bir addır, source:"س ب ح,B001"}. Anma namaz, dua ve övgüdür: {ar:الذكر الصلاة والدعاء والثناء, tr:eẕ-ẕikru's-salâtu ve'd-duâu ve's-senâ, gloss:zikir namaz dua ve övgüdür, source:"ذ ك ر,B005"}. Kur'an okumak da anmadır: {ar:الذكر قراءة القرآن والتسبيح والدعاء والشكر والطاعة, tr:eẕ-ẕikru kırâetu'l-kur'âni ve't-tesbîhu ve'd-duâu ve'ş-şukru ve't-tâa, gloss:zikir Kur'an okumak tesbih dua şükür ve itaattir, source:"ذ ك ر,B005"}. Bu tanım altıncı ayetteki "okutacağız" fiilinin kökünü de içerir. Anma dilde dolaşan addır: {ar:الذكر جري الشيء على لسانك, tr:eẕ-ẕikru cerayu'ş-şey'i alâ lisânik, gloss:zikir bir şeyin dilinde dolaşmasıdır, source:"ذ ك ر,B004"}. Namazın kendisi bir dizi harekettir: {ar:الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح, tr:es-salâtu mine'l-mahlûkîn el-kıyâmu ve'r-rukûu ve's-sucûdu ve'd-duâu ve't-tesbîh, gloss:yaratılmışlar için namaz kıyam rükû secde dua ve tesbihtir, source:"ص ل و,B003"}. Namaz dua da demektir: {ar:الصلاة وهي الدعاء, tr:es-salâtu ve hiye'd-duâ, gloss:salât duadır, source:"ص ل و,B002"}. Aynı kök, Allah'ın kullarına yönelişini de anlatır: {ar:صلاة الله للمسلمين تزكيته إياهم, tr:salâtullâhi li'l-muslimîne tezkiyetuhû iyyâhum, gloss:Allah'ın Müslümanlara salâtı onları arındırmasıdır, source:"ص ل و,B002"}. Bu tanım on beşinci ayeti on dördüncü ayete bağlar. Kişinin namazı ile Allah'ın arındırması aynı kökün iki yönüdür.

Namaz bedensel bir iştir ve kelimelerin aileleri bedeni gösterir. Tesbih kökü secde yerlerini adlandırır: {ar:السبحات مواضع السجود, tr:es-subuhât mevâdiu's-sucûd, gloss:subuhât secde yerleridir, source:"س ب ح,B003"}. Namaz kökü sırtın ortasını adlandırır: {ar:الصلا وسط الظهر لكل ذي أربع وللناس, tr:es-salâ vasatu'z-zahri li-kulli ẕî erbain ve li'n-nâs, gloss:salâ dört ayaklının ve insanın sırtının ortasıdır, source:"ص ل و,B005"}. Yedinci ayetteki "açık" kelimesinin kökü sesli kılınan namazı ve okumayı anlatır: {ar:جهر بكلامه وصلاته وقراءته, tr:cehera bi-kelâmihî ve salâtihî ve kırâetih, gloss:sözünü namazını ve okumasını açıktan yaptı, source:"ج ه ر,B001"}. Böylece sure ibadeti iki uçta kurar. Birinci ayette bir emir olarak başlar, on beşinci ayette bir insanın hareketleri olarak tamamlanır. Arada okuma, öğüt ve unutmama vardır. Bunların hepsi aynı uygulamanın parçalarıdır.

Kur'an bu üçlüyü sık sık birlikte sahneler. Yükseltilmiş evlerde adın anılıp tesbih edildiği ayetin hemen ardından şöyle denir: {ar:رِجَالٌۭ لَّا تُلْهِيهِمْ تِجَٰرَةٌۭ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَآءِ ٱلزَّكَوٰةِ, tr:ricâlun lâ tulhîhim ticâratun ve lâ bey'un an ẕikrillâhi ve ikâmi's-salâti ve îtâi'z-zekât, gloss:ne ticaretin ne alışverişin Allah'ı anmaktan namazı kılmaktan ve zekâtı vermekten alıkoymadığı adamlar, source:24:37}. Bu ayette surenin on dördüncü ve on beşinci ayetlerindeki üç kelime aynı sırayla bulunur. Musa ateşin başında {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14} emrini alır. Aynı konuşmada kardeşini yardımcı olarak isterken amacını şöyle söyler: {ar:كَىْ نُسَبِّحَكَ كَثِيرًۭا, tr:key nusebbihake keŝîrâ, gloss:seni çokça tesbih edelim diye, source:20:33}, {ar:وَنَذْكُرَكَ كَثِيرًا, tr:ve neẕkurake keŝîrâ, gloss:ve seni çokça analım diye, source:20:34}. Peygamber'e de {ar:وَسَبِّحْ بِحَمْدِ رَبِّكَ قَبْلَ طُلُوعِ ٱلشَّمْسِ وَقَبْلَ غُرُوبِهَا, tr:ve sebbih bi-hamdi rabbike kable tulûi'ş-şemsi ve kable ğurûbihâ, gloss:güneş doğmadan ve batmadan önce Rabbini överek tesbih et, source:20:130} denir. Müminlere cuma günü namaza çağrıldıklarında {ar:فَٱسْعَوْا۟ إِلَىٰ ذِكْرِ ٱللَّهِ, tr:fe's'av ilâ ẕikrillâh, gloss:Allah'ı anmaya koşun, source:62:9} denir. Namaz bitince de {ar:وَٱذْكُرُوا۟ ٱللَّهَ كَثِيرًۭا لَّعَلَّكُمْ تُفْلِحُونَ, tr:veẕkurullâhe keŝîran leallekum tuflihûn, gloss:Allah'ı çokça anın ki kurtuluşa eresiniz, source:62:10} denir. Bu emirde on beşinci ayetteki anma, on dördüncü ayetteki kurtuluşa bağlanır. Başka bir yerde namazın işi şöyle anlatılır: {ar:إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۗ وَلَذِكْرُ ٱللَّهِ أَكْبَرُ, tr:inne's-salâte tenhâ ani'l-fahşâi ve'l-munker ve le-ẕikrullâhi ekber, gloss:namaz hayâsızlıktan ve kötülükten alıkoyar; Allah'ı anmak ise elbette en büyüktür, source:29:45}. Bu ayette "en büyük" sıfatı anmaya verilir. Surede ise aynı kökten gelen "en büyük" sıfatı ateşe verilir. Namaz kılanlar arasında bile bir ayrım vardır: {ar:فَوَيْلٌۭ لِّلْمُصَلِّينَ, tr:fe-veylun li'l-musallîn, gloss:yazıklar olsun o namaz kılanlara, source:107:4}, {ar:ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ, tr:elleẕîne hum an salâtihim sâhûn, gloss:onlar ki namazlarından gafildirler, source:107:5}. Gaflet, altıncı ayetteki unutmanın bir türüdür.

Kaynaklar: 87:1 سَبِّحِ س ب ح B001; 87:1 سَبِّحِ س ب ح B003; 87:15 وَذَكَرَ ذ ك ر B005; 87:15 وَذَكَرَ ذ ك ر B004; 87:15 فَصَلَّىٰ ص ل و B003; 87:15 فَصَلَّىٰ ص ل و B002; 87:15 فَصَلَّىٰ ص ل و B005; 87:7 ٱلْجَهْرَ ج ه ر B001

## Açık ve gizli: ses ve örtüden çıkan

Yedinci ayetin sonu {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ, tr:innehû ya'lemu'l-cehra ve mâ yahfâ, gloss:O açığa vurulanı da gizli kalanı da bilir, source:87:7} der. Bu cümle iki ayrı sahnede duyulur. Birincisi sestir. جهر sesi yükseltmektir: {ar:جهر بالقول رفع به صوته, tr:cehera bi'l-kavli rafea bihî savtah, gloss:sözü açıktan söyledi yani sesini yükseltti, source:"ج ه ر,B001"}. {ar:الجهر ضد السر, tr:el-cehru diddu's-sirr, gloss:cehr gizlinin zıddıdır, source:"ج ه ر,B001"}. Bu kök tek bir harfin söylenişine kadar iner: {ar:سمي الحرف مجهورا لأنه أشبع الاعتماد في موضعه ومنع النفس أن يجري معه, tr:sumiye'l-harfu mechûran li-ennehû eşbea'l-i'timâde fî mevdiihî ve menea'n-nefese en yecriye meah, gloss:harfe mechûr denir çünkü çıkış yerine tam dayanır ve nefesin onunla akmasını engeller, source:"ج ه ر,B011"}. خفي sesi kısmaktır: {ar:أخفيت الصوت إخفاء ... والخافية ضد العلانية ولقيته خفيا أي سرا, tr:ahfeytu's-savte ihfâen ve'l-hâfiyetu diddu'l-alâniye ve lekîtuhû hafiyyen ey sirran, gloss:sesi kıstım; hâfiye açıklığın zıddıdır; onunla gizlice karşılaştım, source:"خ ف ي,B001"}. On beşinci ayetteki anma iki yerde yaşar: {ar:ذكرته بلساني وبقلبي, tr:ẕekertuhû bi-lisânî ve bi-kalbî, gloss:onu dilimle ve kalbimle andım, source:"ذ ك ر,B004"}. Okuma da ezberden yapılır: {ar:قرأت القرآن عن ظهر قلب أو نظرت فيه, tr:kara'tu'l-kur'âne an zahri kalbin ev nazartu fîh, gloss:Kur'an'ı ezberden ya da bakarak okudum, source:"ق ر ء,B002"}. Bilmek de söylenenin farkında olmaktır: {ar:ما علمت بخبرك أي ما شعرت به, tr:mâ alimtu bi-haberike ey mâ şaartu bih, gloss:haberini bilmedim yani farkına varmadım, source:"ع ل م,B001"}. Bu sahnede yedinci ayet, altıncı ayetteki okumanın iki halini, yüksek sesle ve içten okumayı birlikte kucaklar. Okutulan söz dilde de olsa kalpte de olsa bilinir.

İkinci sahne örtüden çıkmaktır. "Gizli" kökü, Arapçada zıt anlamları birlikte taşıyan kelimelerden biridir: {ar:خفيت الشيء بغير ألف إذا أظهرته, tr:hafeytu'ş-şey'e bi-ğayri elifin iẕâ azhartah, gloss:elifsiz hafeytu bir şeyi açığa çıkardım demektir, source:"خ ف ي,B003"}. {ar:استخفيت الشئ أي استخرجته, tr:istahfeytu'ş-şey'e ey istahrectuh, gloss:bir şeyi çıkardım, source:"خ ف ي,B003"}. Bu ikinci açıklama dördüncü ayetin "çıkarmak" kökünü kullanır, ki o kökün temel anlamı şudur: {ar:خرج خروجا برز من مقره أو حاله, tr:harace hurûcen beraze min makarrihî ev hâlih, gloss:yerinden ya da halinden dışarı belirdi, source:"خ ر ج,B001"}. Örtülü olanın somut örnekleri de vardır: {ar:الخوافي سعفات يلين قلب النخلة, tr:el-havâfî saafâtun yelîne kalbe'n-nahle, gloss:havâfî hurmanın göbeğine yakın dallardır, source:"خ ف ي,B002"}. {ar:الخوافي جمع خافية وهي ما دون القوادم من الريش, tr:el-havâfî cem'u hâfiye ve hiye mâ dûne'l-kavâdimi mine'r-rîş, gloss:havâfî kanadın ön tüylerinin altında kalan tüylerdir, source:"خ ف ي,B002"}. Öbür uçta açık olan vardır: {ar:كل شيء بدا فقد جهر, tr:kullu şey'in bedâ fe-kad cehera, gloss:ortaya çıkan her şey açığa çıkmıştır, source:"ج ه ر,B002"}, ve temizlenip suyu görünen kuyu bu kökle anılır. Açıklığın bir tersi de vardır: {ar:العين الجهراء التي لا تبصر في الشمس, tr:el-aynu'l-cehrâ elletî lâ tubsiru fi'ş-şems, gloss:cehrâ göz güneşte göremeyen gözdür, source:"ج ه ر,B004"}. Fazla ışık da bir örtü olabilir. Dördüncü ayetle birlikte okununca yedinci ayetin ikilisi sabit iki durum olmaktan çıkar ve bir harekete dönüşür: yağmurla topraktan ot çıkar, deliklerden fareler çıkar. Gizli olan, Rabbin bildiği ve dilediğinde açığa çıkardığı şeydir.

Kur'an bu iki sahneyi açıkça kurar. Peygamber'e indirilen hitabın başında şöyle denir: {ar:وَإِن تَجْهَرْ بِٱلْقَوْلِ فَإِنَّهُۥ يَعْلَمُ ٱلسِّرَّ وَأَخْفَى, tr:ve in techer bi'l-kavli fe-innehû ya'lemu's-sirra ve ahfâ, gloss:sözü yüksek sesle söylesen de O gizliyi ve daha gizlisini bilir, source:20:7}. Bu, Musa'nın ateşi gördüğü sahneye geçmeden önceki ayetlerdendir. Aynı hikâyede ateşin başında {ar:إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا, tr:inne's-sâate âtiyetun ekâdu uhfîhâ, gloss:o saat gelecektir; onu neredeyse gizli tutuyorum, source:20:15} denir. Sesin ölçüsü bir emirle verilir: {ar:وَلَا تَجْهَرْ بِصَلَاتِكَ وَلَا تُخَافِتْ بِهَا وَٱبْتَغِ بَيْنَ ذَٰلِكَ سَبِيلًۭا, tr:ve lâ techer bi-salâtike ve lâ tuhâfit bihâ vebteğı beyne ẕâlike sebîlâ, gloss:namazında sesini ne yükselt ne de kıs; ikisinin arasında bir yol tut, source:17:110}. Anmanın sesi de belirlenir: {ar:وَٱذْكُر رَّبَّكَ فِى نَفْسِكَ تَضَرُّعًۭا وَخِيفَةًۭ وَدُونَ ٱلْجَهْرِ مِنَ ٱلْقَوْلِ, tr:veẕkur rabbeke fî nefsike tedarruan ve hîfeten ve dûne'l-cehri mine'l-kavl, gloss:Rabbini içinden yalvararak ve korkarak ve yüksek olmayan bir sesle an, source:7:205}. Duanın sesi de: {ar:ٱدْعُوا۟ رَبَّكُمْ تَضَرُّعًۭا وَخُفْيَةً, tr:ud'û rabbekum tedarruan ve hufye, gloss:Rabbinize yalvararak ve gizlice dua edin, source:7:55}. Allah için {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ مِنَ ٱلْقَوْلِ وَيَعْلَمُ مَا تَكْتُمُونَ, tr:innehû ya'lemu'l-cehra mine'l-kavli ve ya'lemu mâ tektumûn, gloss:O sözün açığını da bilir gizlediğinizi de bilir, source:21:110} ve {ar:يَعْلَمُ سِرَّكُمْ وَجَهْرَكُمْ, tr:ya'lemu sirrakum ve cehrakum, gloss:gizlinizi de açığınızı da bilir, source:6:3} denir. Örtüden çıkarma sahnesini ise Süleyman'a haber getiren hüdhüd anlatır. Hüdhüd bir kavmin güneşe secde ettiğini, şeytanın onları yoldan çevirdiğini söyler ve şöyle ekler: {ar:أَلَّا يَسْجُدُوا۟ لِلَّهِ ٱلَّذِى يُخْرِجُ ٱلْخَبْءَ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَيَعْلَمُ مَا تُخْفُونَ وَمَا تُعْلِنُونَ, tr:ellâ yescudû lillâhi'lleẕî yuhricu'l-hab'e fi's-semâvâti ve'l-ardi ve ya'lemu mâ tuhfûne ve mâ tu'linûn, gloss:göklerde ve yerde saklı olanı çıkaran ve gizlediğinizi de açıkladığınızı da bilen Allah'a secde etmesinler diye, source:27:25}. Bu tek ayette dördüncü ayetteki "çıkarmak" ile yedinci ayetteki gizli ve açık bir arada bulunur.

Kaynaklar: 87:7 ٱلْجَهْرَ ج ه ر B001; 87:7 ٱلْجَهْرَ ج ه ر B011; 87:7 ٱلْجَهْرَ ج ه ر B002; 87:7 ٱلْجَهْرَ ج ه ر B004; 87:7 يَخْفَىٰ خ ف ي B001; 87:7 يَخْفَىٰ خ ف ي B003; 87:7 يَخْفَىٰ خ ف ي B002; 87:15 وَذَكَرَ ذ ك ر B004; 87:6 سَنُقْرِئُكَ ق ر ء B002; 87:7 يَعْلَمُ ع ل م B001; 87:4 أَخْرَجَ خ ر ج B001

## Koşan dizi: önde, ardında, sonda

On altıncı ve on yedinci ayetteki zaman kelimeleri, hareket halindeki bir at ya da deve dizisinde yer de bildirir. Birinci ayetteki tesbih fiilinin kökünde koşan at vardır: {ar:السابح من الخيل يمد يديه في الجري؛ النجوم تسبح في الفلك, tr:es-sâbihu mine'l-hayli yemuddu yedeyhi fi'l-cerî en-nucûmu tesbehu fi'l-felek, gloss:sâbih koşarken ön ayaklarını uzatan attır; yıldızlar yörüngelerinde yüzer, source:"س ب ح,B004"}. Kökün temel anlamı suda yüzmektir: {ar:سَبَحَ فِي ٱلْمَاءِ, tr:sebeha fi'l-mâ, gloss:suda yüzdü, source:"memory"}. Dizinin başında öncüler vardır: {ar:هوادي الخيل أعناقها أو أول رعيل, tr:hevâdi'l-hayli a'nâkuhâ ev evvelu racîl, gloss:atların hevâdîsi boyunlarıdır ya da ilk bölüktür, source:"ه د ي,B003"}. On beşinci ayetteki namaz kökü ikinci atı adlandırır: {ar:قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه, tr:kad sallâ ve câe musalliyen li-enne ra'sehû yetlu's-salâ'lleẕî beyne yedeyh, gloss:musallî olarak geldi çünkü başı öndekinin sağrısını izler, source:"ص ل و,B006"}. {ar:السابق الأول والمصلي الثاني, tr:es-sâbiku'l-evvel ve'l-musallî es-ŝânî, gloss:sâbık birinci musallî ikincidir, source:"ص ل و,B006"}. Sekizinci ayetin kökü düzgün adımı verir: {ar:دابة حسن التيسور أي حسن نقل القوائم, tr:dâbbetun hasenu't-teysûr ey hasenu nakli'l-kavâim, gloss:ayaklarını güzel atan hayvan, source:"ي س ر,B005"}. On altıncı ayetteki tercih kökü, öne koymaktır: {ar:له أصل تقديم الشيء, tr:lehû aslu takdîmi'ş-şey', gloss:bir şeyi öne koyma anlamında bir kökü vardır, source:"ء ث ر,B001"}. Ama aynı kök birinin izinden gitmek de demektir: {ar:جاء فلان على إثري وأثري وجاء في أثره وإثره, tr:câe fulânun alâ isrî ve eserî ve câe fî eserihî ve isrih, gloss:falanca peşimden geldi; onun izinden geldi, source:"ء ث ر,B004"}. Dünya yakın kıyıdır: {ar:العدوة الدنيا والعدوة القصوى, tr:el-udvetu'd-dunyâ ve'l-udvetu'l-kusvâ, gloss:yakın yamaç ve uzak yamaç, source:"د ن و,B002"}. Ahiret kökü topluluğun arkasında kalanları adlandırır: {ar:أخرى القوم أي من كان في آخرهم, tr:uhra'l-kavmi ey men kâne fî âhirihim, gloss:topluluğun uhrâsı en arkada olandır, source:"ء خ ر,B001"}. Semerin arka direği de bu köktendir: {ar:آخرة الرحل وقادمته ومؤخر الرحل ومقدمه, tr:âhiratu'r-rahli ve kâdimetuhû ve muahharu'r-rahli ve mukaddemuh, gloss:semerin arka ve ön direği, source:"ء خ ر,B003"}. On yedinci ayetteki "kalıcı" kelimesinin ailesinde koşusunun bir kısmını saklayan atlar vardır: {ar:المبقيات من الخيل التي تبقي بعض جريها تدخره, tr:el-mubkıyâtu mine'l-hayli elletî tubkî ba'da cerîhâ teddehıruh, gloss:mubkıyât koşusunun bir kısmını saklayıp biriktiren atlardır, source:"ب ق ي,B004"}. On sekizinci ayetin "ilk" kelimesi de dizinin önündeki deveyi verir: {ar:ناقة أولة وجمل أول إذا تقدما الإبل, tr:nâkatun evvelatun ve cemelun evvelu iẕâ tekaddeme'l-ibil, gloss:develerin önüne geçen dişi deve ve erkek deve, source:"ء و ل,B001"}.

Bu dizi içinde on altıncı ve on yedinci ayet bir koşu olarak okunur. Öne koyduğunuz şey yakın olandır. Arkada gelen ise daha hayırlıdır ve daha uzun dayanır, tıpkı koşusunu sona saklayan at gibi. Düz bir anlatım yalnızca iki hayatı karşılaştırır. Bu sahne karşılaştırmaya bir zaman sırası ekler: ilk gelen yarışı kazanan değildir. On beşinci ayetteki "namaz kıldı" fiilinin ailesinde öncünün hemen ardından gelen ikinci at vardır. Bu, bir izleme hareketi olarak duyulur. Ama bu bağ kelimenin namaz anlamının yerine geçmez.

Kur'an yemin ettiği koşucularla bir sureyi açar: {ar:وَٱلسَّٰبِحَٰتِ سَبْحًۭا, tr:ve's-sâbihâti sebhâ, gloss:yüzdükçe yüzenlere andolsun, source:79:3}. Bu, Firavun'un "en yüce rabbinizim" dediği ve dünya hayatını tercih edenin anıldığı suredir. Bir başka yerde öndekiler {ar:وَٱلسَّٰبِقُونَ ٱلسَّٰبِقُونَ, tr:ve's-sâbikûne's-sâbikûn, gloss:öne geçenler ise öne geçenlerdir, source:56:10} diye anılır. Yakın ve uzak yamaç, iki topluluğun karşılaştığı günün tasvirinde geçer: {ar:إِذْ أَنتُم بِٱلْعُدْوَةِ ٱلدُّنْيَا وَهُم بِٱلْعُدْوَةِ ٱلْقُصْوَىٰ, tr:iẕ entum bi'l-udveti'd-dunyâ ve hum bi'l-udveti'l-kusvâ, gloss:o gün siz yakın yamaçtaydınız onlar uzak yamaçtaydı, source:8:42}. On altıncı ayetin cümle yapısı başka bir yerde neredeyse aynen tekrarlanır. Orada "yakın" yerine "acele gelen" kelimesi kullanılır: {ar:كَلَّا بَلْ تُحِبُّونَ ٱلْعَاجِلَةَ, tr:kellâ bel tuhibbûne'l-âcile, gloss:hayır; siz acele geleni seviyorsunuz, source:75:20}, {ar:وَتَذَرُونَ ٱلْءَاخِرَةَ, tr:ve teẕerûne'l-âhira, gloss:ve sonra geleni bırakıyorsunuz, source:75:21}. Önce geleni tutup arkadan geleni bırakmak, bu dizideki yanlış sıralamadır.

Kaynaklar: 87:1 سَبِّحِ س ب ح B004; 87:3 فَهَدَىٰ ه د ي B003; 87:15 فَصَلَّىٰ ص ل و B006; 87:8 لِلْيُسْرَىٰ ي س ر B005; 87:16 تُؤْثِرُونَ ء ث ر B001; 87:16 تُؤْثِرُونَ ء ث ر B004; 87:16 ٱلدُّنْيَا د ن و B002; 87:17 وَٱلْءَاخِرَةُ ء خ ر B001; 87:17 وَٱلْءَاخِرَةُ ء خ ر B003; 87:17 أَبْقَىٰٓ ب ق ي B004; 87:18 ٱلْأُولَىٰ ء و ل B001

## Buluşmalar

İmgelerin çoğu, surenin son ayetinde adı geçen Musa'nın hikâyesinde buluşur. Musa uzakta bir ateş görür ve {ar:أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ecidu ale'n-nâri hudâ, gloss:ateşin başında bir yol gösteren bulurum, source:20:10} umuduyla ona yönelir. Uzaktan görülen ateşin sahnesi ile yol sahnesi burada aynı cümlededir. Ateşin başında önce seçim gelir: {ar:وَأَنَا ٱخْتَرْتُكَ, tr:ve ene'htertuk, gloss:seni ben seçtim, source:20:13}. Sonra namaz ve anma gelir: {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14}. Sonra gizli olan gelir: {ar:أَكَادُ أُخْفِيهَا, tr:ekâdu uhfîhâ, gloss:onu neredeyse gizli tutuyorum, source:20:15}. Başka bir anlatımda ateşin başında tesbih söylenir: {ar:وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve subhânallâhi rabbi'l-âlemîn, gloss:Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu sahnede surenin on ikinci ve on beşinci ayetleri arasındaki karşıtlık bir kişinin yolculuğunda çözülür. Aynı ateşe yaklaşan biri onun içine sokulmaz. Ateş ona yol, seçilmişlik, namaz ve anma verir. Surede bu iki son iki ayrı kişiye düşer: on ikinci ayetteki kişi ateşe girer, on beşinci ayetteki kişi namaz kılar. Kelimelerin harf benzerliği bu ayrılığı kulakta da duyurur.

İkinci büyük buluşma selin sahnesidir. Gökten inen suyun vadilerde {ar:بِقَدَرِهَا, tr:bi-kaderihâ, gloss:kendi ölçülerince, source:13:17} akması, ölçüp biçme sahnesini çağırır. Selin taşıdığı köpük, otlağın vardığı döküntüdür. İnsanların {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâr, gloss:ateşte üzerine yaktıkları şeyden, source:13:17} çıkan köpük ise ateşin sahnesine girer. Faydalı olanın yerde kalması da öğüdün ve kalıcılığın sahnesidir. Kurumuş otun tencerenin köpüğüyle aynı adı taşıması, bu iki köpüğün Arapçada zaten tek bir kelimede birleştiğini gösterir. Bu ayet surenin beşinci ayetinden on yedinci ayetine uzanan çizgiyi tek bir manzaraya sığdırır. Bir yanda giden döküntü, öbür yanda kalan fayda vardır.

Üçüncü buluşma, Musa'nın karşısındaki sihirbazların sahnesidir. Sihirbazlar secdeye kapanır. Firavun kendi azabının daha çetin ve {ar:وَأَبْقَىٰ, tr:ve ebkâ, gloss:ve daha kalıcı, source:20:71} olduğunu söyler. Sihirbazlar da onu {ar:لَن نُّؤْثِرَكَ, tr:len nu'ŝirak, gloss:seni asla tercih etmeyiz, source:20:72} diye reddeder, yalnızca {ar:هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:hâẕihi'l-hayâte'd-dunyâ, gloss:bu dünya hayatı, source:20:72} üzerinde hüküm verebileceğini söyler ve {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} der. Sonra suçlu için {ar:لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:lâ yemûtu fîhâ ve lâ yahyâ, gloss:orada ne ölür ne yaşar, source:20:74} der, iman edenler için {ar:ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:ed-derecâtu'l-ulâ, gloss:en yüce dereceler, source:20:75} der, ve hepsini {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76} sözüyle bağlar. Bu birkaç ayette seçim, kalıcı hayat, yükseklik ve yarılan tarlanın kelimeleri birlikte konuşur. Firavun'un "en yüce" iddiası da başka bir anlatımda bu sahneye eklenir. Surenin ikinci yarısı, on üçüncü ayetten on yedinci ayete kadar, neredeyse kelimesi kelimesine Musa'nın hikâyesindeki bir topluluğun ağzından gelmiştir. Son ayetin Musa'nın sayfalarını anması da bu yüzden önem taşır.

Dördüncü buluşma ot ile seçimdir. Dünya hayatının kuruyan ota benzetildiği ayetin hemen ardından kalıcı iyi işlerin daha hayırlı olduğu söylenir. Dünya hayatı başka bir yerde bir {ar:زَهْرَةَ, tr:zehrate, gloss:çiçek, source:20:131} olarak anılır, ve aynı ayet {ar:خَيْرٌۭ وَأَبْقَىٰ, tr:hayrun ve ebkâ, gloss:daha hayırlı ve daha kalıcı, source:20:131} diye biter. Otlağın sahnesi seçimin sahnesine bu yolla girer. Beşinci ayetteki ot ile on altıncı ayetteki tercih edilen hayat aynı nesnedir. Kalıcı olan ise ayıklanıp seçilen şeydir. Tarlanın sahnesi bu iki uç arasında bir yol açar. Kalıcı iyilik anlamına gelen kurtuluş kelimesi on dördüncü ayette, toprağı yaran çiftçinin kelimesiyle söylenir. Yabani ot kendi haline kalınca kurur ve selle gider. İşlenen toprağın ürünü ise büyür, hakkı verilir ve geriye kalan bir pay bırakır. Biri dünya tarlası, öbürü ahiret tarlasıdır.

Beşinci buluşma, yaratma fiillerinde zanaat ile bedenin birleşmesidir. İkinci ayetteki ikili hem yontulmuş oku hem de ceninin biçimlenmesini anlatır. Rahimden başlayan ayetin toprağın yağmurla titreşmesiyle bitmesi, beden ile otlağı da birbirine bağlar. Aynı aile, üçüncü ayetteki ölçmeyi pay ölçmeye de taşır, ve on altıncı ayetteki tercih bir pay seçimine döner. Değneği ateşte doğrultmanın fiili on ikinci ayetin fiilidir. Bu fiil aynı ateşin düzelten bir işi ile içine düşenin katlandığı bir işi olduğunu duyurur. Bu son bağ dilin yankısıdır, ayetin sözü değildir.

Bu buluşmalar surenin hareketini taşır. Sure tesbih emriyle ve yükseklikle açılır. Ölçen, yontan ve yol gösteren Rabbin işiyle devam eder. Yağmurun çıkardığı ve selin götürdüğü ot ile sona gelen bir ömür gösterir. Sonra sözün toplanıp unutulmamasına, sunulan öğüde ve öğüt karşısında ikiye ayrılan insanlara geçer. Biri ateşe girer ve ne ölü ne diri kalır. Öbürü arınır, Rabbinin adını anar ve namaz kılar, yani surenin başındaki emri yerine getirir. Ardından seçim gelir: yakın olan öne konmuştur, ama arkadan gelen daha hayırlı ve daha kalıcıdır. Sure, bu sözün ilk sayfalarda, ateşin başında namaz ve anma emrini alan Musa'nın ve Rabbinden kendisini puttan uzak tutmasını isteyen İbrahim'in sayfalarında yazılı olduğunu söyleyerek kapanır.

