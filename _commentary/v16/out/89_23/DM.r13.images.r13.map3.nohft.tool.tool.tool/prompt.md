Focus: 89:23. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_23/D.r13/context.md =====
# 89:23 — focus

وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ

Anchor translation (canonical reading, reference only):

O gün cehennem getirilir. O gün insan hatırlar; fakat hatırlamanın ona ne yararı olur?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَجِا۟ىٓءَ | جَآءَ | ج ي ء | CONJ;V |
| 2 | يَوْمَئِذٍۭ | يَوْمَئِذ |  | T |
| 3 | بِجَهَنَّمَ | جَهَنَّم |  | P;PN |
| 4 | يَوْمَئِذٍ | يَوْمَئِذ |  | T |
| 5 | يَتَذَكَّرُ | تَذَكَّرَ | ذ ك ر | V |
| 6 | ٱلْإِنسَٰنُ | إِنسَٰن | ء ن س | DET;N |
| 7 | وَأَنَّىٰ | أَنَّىٰ | ء ن ي | CONJ;INTG |
| 8 | لَهُ |  |  | P;PRON |
| 9 | ٱلذِّكْرَىٰ | ذِكْرَىٰ | ذ ك ر | DET;N |


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
- 89:23 ◀ focus وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- 89:24 يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى
- 89:25 فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- 89:26 وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ
- 89:27 يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- 89:28 ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- 89:29 فَٱدْخُلِى فِى عِبَٰدِى
- 89:30 وَٱدْخُلِى جَنَّتِى


===== _commentary/v16/work/89_23/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ج ي ء (root_000281) — identity root of وَجِا۟ىٓءَ (w1)

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · geliş; varış · bir kez geliş veya geliş biçimi · sık sık iyilik getiren · iyi ki geldin
  جاء يجيء مجيئا (maqayis;mufradat)؛ جاء فلان يجيء جيئة إذا جاء مرة واحدة وجيئة حسنة (jamhara)؛ المجئ: الاتيان، جاء يجئ جيئة، وجئت مجيئا حسنا (sihah)؛ المجيء كالإتيان لكن المجيء أعم ويقال في الأعيان والمعاني ولمن قصد مكانا أو عملا أو زمانا (mufradat)
- **B002** gelip gitmede üstün gelmek [kalıp] — benimle sık gelme yarışına girdi, ben de onu geçtim
  جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ وجاءانى على فاعلنى فجئته أجيئه، أي غالبني بكثرة المجئ فغلبته (sihah)
- **B003** suyun biriktiği çukur veya yer — suyun biriktiği yer veya büyük çukur · tuzlu ya da idrar karışmış kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره ويقال هي جيئة (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون، والموضع الذي يجتمع فيه الماء، والحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ جية من ماء أي ماء ناقع خبيث (tahdhib)
- **B004** bir şeyi getirmek veya hazır bulundurmak — sık sık iyilik getiren · bir şeyi getirmek veya hazır bulundurmak · onu getirmek
  أجأته، أي جئت به (sihah)؛ جاءه بكذا وأجاءه، وجاء بكذا: استحضره (mufradat)
- **B005** birini bir şeye zorlamak [kalıp] — onu belirli bir şeye zorlamak · seni buna gerek duyar duruma düşürmek
  أجأته إلى كذا بمعنى ألجأته واضطررته إليه (sihah)؛ أجاءها المخاض إلى جذع النخلة، قيل: ألجأها، وإنما هو معدى عن جاء (mufradat)
- **B006** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح، يقال: جاءت جائية الجراح (tahdhib)

## ج ي ء (root_000282) — identity root of وَجِا۟ىٓءَ (w1)

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · benimle sık gelme yarışına girdi, ben de onu geçtim · geliş; gelme
  جاء يجيء مجيئا (maqayis)؛ جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ الجيئة مصدر جاء (maqayis)؛ جاء فلان جيأة (tahdhib)
- **B002** suyun biriktiği yer veya çukur — kale çevresinde, alçak yerde veya büyük çukurda su birikme yeri · suların aktığı yer; kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون (tahdhib)؛ الجيأة الموضع الذي يجتمع فيه الماء (tahdhib)؛ الجيأة الحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ يقال له جية وجيأة وكل من كلام العرب (tahdhib)
- **B003** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح (tahdhib)؛ جاءت جائية الجراح (tahdhib)

## ذ ك ر (root_000516) — identity root of يَتَذَكَّرُ (w5)

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

## ء ن س (root_000059) — identity root of ٱلْإِنسَٰنُ (w6)

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

## ء ن ي (root_000063) — identity root of وَأَنَّىٰ (w7)

- **B001** ağırdan alma ve geciktirme — ağırbaşlılık ve acele etmeme · bir işte acele etmemek, bekleyip yumuşak davranmak · işlerde duraklayıp acele etmeme · bir şeyi geciktirmek, bekletmek ve yavaşlatmak · birini aceleye sürmemek, onun için beklemek · acele etmeyen, ağırbaşlı kişi · ağırbaşlı kadın veya kalkarken gevşek davranan kadın
  الأناة الحلم والفعل منه تأنى وتأيا (maqayis)؛ التأني (maqayis)؛ آنيت يعني أخرت المجيء وأبطأت (maqayis)؛ الإيناء بمعنى الإبطاء وآنيت الشيء أي أخرته (ayn)؛ آناه يؤنيه إيناء أي أخره وحبسه وأبطأه (sihah)؛ الأناة التؤدة وتأنيت تأخرت (mufradat)
- **B002** gecenin zaman bölümleri — gecenin zaman bölümleri · gecenin tek bir zaman bölümü · ara sıra, zaman zaman
  الإني والأنى ساعة من ساعات الليل والجمع آناء (maqayis;ayn)؛ وآناء الليل واحدها إني وهي الساعة من الليل (jamhara)؛ آناء الليل ساعاته (sihah;tahdhib;mufradat)
- **B003** zamanı gelip olgunluğa erişme — bir şeyin zamanı, olgunluğu veya erişme noktası · zamanı gelmek, olgunlaşmak ve erişmek · senin için zamanı gelmedi mi · yemeğin pişip olgunlaşmasını beklemek · ısısı doruğa varmış çok sıcak su · ısısı yükselmiş sıcak kaynak · olgunlaşmış ve erişmiş
  الإني إدراك الشيء (maqayis)؛ انتظرنا إنى الطعام أي إدراكه (maqayis;ayn)؛ ما أنى لك ولم يأن لك أي لم يحن (maqayis;ayn)؛ حميم آن قد انتهى حره وعين آنية (maqayis;ayn)؛ أنى الشيء يأنى إنى أي حان وأنى أيضا أدرك (sihah)؛ بلغ إناه من شدة الحر (mufradat)
- **B004** içine şey konan kap — içine bir şey konan kap · kaplar ve daha geniş çoğul biçimi
  الإناء ممدود من الآنية والأواني جمع جمع (maqayis)؛ الإناء معروف وجمعه آنية والأواني (sihah)؛ الإناء ما يوضع فيه الشيء وجمعه آنية (mufradat)
- **B005** nereden ve nasıl diye sorma sözü — nereden, hangi yönden, nasıl veya ne zaman · bu sana nereden ya da nasıl geldi · hangi yönden gelirsen, sana gelirim · nereye ya da nasıl yönelirse
  أنى معناها كيف ومن أين (ayn)؛ أنى معناه أين ومن أين ومن أي جهة وقد تكون بمعنى كيف (sihah)؛ أنى أداة لها معنيان متى ومن أين ويحتمل كيف (tahdhib)؛ أنى للبحث عن الحال والمكان (mufradat)

## ECHO ء و ن (root_000068) — for وَأَنَّىٰ (w7): withheld observed target; not identity

- **B001** yumuşak ve rahat davranma — yumuşak davrandı · rahatlık, dinginlik ve yumuşak davranma · yolculukta kendini yorma, rahat git · yumuşak ve rahat davrandın · rahat ve dingin adam · rahat ve dingin geceler
  كلمة واحدة تدل على الرفق (maqayis); آن يؤون أونا إذا رفق (maqayis); الأون: الدعة والسكينة والرفق (sihah); أن على نفسك أي ارفق في السير واتدع (maqayis;sihah); رجل آئن (maqayis); رجل آين أي رافه وادع (sihah); ليال أوائن روافه وآينات وادعات (sihah)
- **B002** yük yanı — yük kabının bir yanı; dengeli yük parçası · iki yanlı çıkın veya çift yanlı yük · eşeğin yiyip içince karnı ve iki yanı yük gibi doldu
  الأون: أحد جانبي الخرج (sihah); الأون: العدل (sihah); أون الحمار إذا أكل وشرب وامتلأ بطنه وامتدت خاصرتاه فصار مثل الأون (sihah)
- **B003** belirli zaman — belirli zaman · ayrı zamanlar, ara ara gelen vakitler · o işi ara sıra yapar ve ara sıra bırakır
  الأوان: الحين، والجمع آونة (sihah); فلان يصنع ذلك الأمر آونة إذا كان يصنعه مرارا ويدعه مرارا (sihah)
- **B004** büyük kemerli yapı bölümü — büyük kemerli yapı bölümü · büyük kemerli yapı bölümü; belirli saray örneğiyle de anılır · büyük kemerli yapı bölümü · büyük kemerli yapı bölümleri · büyük kemerli yapı bölümleri
  الأوان والإيوان: الصفة العظيمة كالأزج (sihah); إيوان كسرى (sihah); جمع الإوان أون وجمع الإيوان إيوانات وأواوين (sihah)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:23, and ## Buluşmalar) =====
## Saf saf gelenler

Yer dövülüp düzlendikten sonra bir topluluk gelir: {ar:وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا, tr:ve câe rabbuke ve'l-meleku saffen saffâ, gloss:Rabbin ve melekler saf saf geldiğinde, source:89:22}. Gelmek (mecî') genel bir fiildir: {ar:المجيء كالإتيان لكن المجيء أعم, tr:el-mecîu ke'l-ityân, lâkinne'l-mecîe a'amm, gloss:mecî' gelmek gibidir, ama ondan daha geniştir, source:"ج ي ء,B001"}. Melek kelimesi burada tekildir, ama bütün sınıfı kapsar: {ar:الملك من الملائكة واحد وجمع, tr:el-melek mine'l-melâike vâhidun ve cem', gloss:melek kelimesi hem tekil hem çoğul için kullanılır, source:"م ل ك,B009"}. Kur'an aynı tekili yerin ve dağların ezildiği sahnede de kullanır: {ar:وَٱلْمَلَكُ عَلَىٰٓ أَرْجَآئِهَا, tr:ve'l-meleku alâ ercâihâ, gloss:melekler de göğün kenarlarındadır, source:69:17}. Saf, bir şeyi düz bir çizgi üzerine dizmektir: {ar:الصف أن تجعل الشيء على خط مستو, tr:es-saffu en tec'ale'ş-şey'e alâ hattın mustevin, gloss:saf, bir şeyi düz bir çizgi üzerine dizmektir, source:"ص ف ف,B001"}. Durulan yer de bu kökten adlandırılır: {ar:المصف الموقف, tr:el-masaff el-mevkıf, gloss:masaff, durulan yerdir, source:"ص ف ف,B001"}. Kelimenin tekrarı bir dağıtım kalıbıdır. Arapça gelme fiilini tekrarlanan bir sayıyla aynı biçimde kurar: {ar:جاء القوم عشار عشار ومعشر معشر أي عشرة عشرة, tr:câe'l-kavmu uşâra uşâr, ve ma'şera ma'şer, ey aşeraten aşera, gloss:topluluk onar onar geldi, source:"ع ش ر,B005"}. Ayetteki tekrar da aynı şeyi söyler: saf ardından saf gelir. İkinci ayetteki "on" kelimesinin kökü bu kalıbı önceden taşır.

Gelişin ritmi surenin önceki kelimelerinde de vardır. Üçüncü ayetteki tek kelimesinin kökünden birbiri ardınca gelmek anlamı türer: {ar:تترى من الوتر أي واحدا بعد واحد, tr:tetrâ mine'l-vetr, ey vâhiden ba'de vâhid, gloss:tetrâ vetr kökündendir, yani birbiri ardınca, source:"و ت ر,B004"}. Kur'an bu kelimeyi elçilerin ve onları yalanlayan ümmetlerin dizisi için kullanır: {ar:ثُمَّ أَرْسَلْنَا رُسُلَنَا تَتْرَا, tr:summe erselnâ rusulenâ tetrâ, gloss:sonra elçilerimizi birbiri ardınca gönderdik, source:23:44}. Aynı ayette yalanlayan ümmetler de birbirinin ardınca yok edilip söz konusu edilen hikâyelere dönüştürülür. Surenin altıncı ve onuncu ayetleri arasında anılan kavimler de böyle bir dizi oluşturur. İlk kelimenin kökü de bir topluluğun ansızın üstüne gelişini anlatır: {ar:انفجرت عليهم الدواهي إذا جاءهم الكثير منها بغتة, tr:infeceret aleyhimu'd-devâhî izâ câehumu'l-kesîru minhâ bağteten, gloss:felaketler birdenbire ve çok sayıda gelince "üstlerine boşandı" denir, source:"ف ج ر,B003"}. Dövme fiili de kalabalığın bir şeye yüklenmesini anlatır: {ar:تداك عليه القوم إذا ازدحموا عليه, tr:tedâkke aleyhi'l-kavmu izezdehamû aleyh, gloss:insanlar onun üstüne üşüştü, source:"د ك ك,B008"}.

Yirmi üçüncü ayette cehennem getirilir: {ar:وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ, tr:ve cîe yevmeizin bi-cehennem, gloss:o gün cehennem getirildiğinde, source:89:23}. Bir şeyi getirmek onu hazır etmektir: {ar:وجاء بكذا: استحضره, tr:ve câe bi-kezâ: istahdarah, gloss:onu getirdi, yani hazır etti, source:"ج ي ء,B004"}. Uzakta sanılan şey göz önüne konur. Kur'an aynı edilgen fiili Sûr'dan sonraki sahnede kullanır: {ar:وَجِا۟ىٓءَ بِٱلنَّبِيِّۦنَ وَٱلشُّهَدَآءِ, tr:ve cîe bi'n-nebiyyîne ve'ş-şuhedâ', gloss:peygamberler ve şahitler getirildi, source:39:69}. Cehennemin ortaya çıkarılmasını da şöyle anlatır: {ar:وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ, tr:ve burrizeti'l-cahîmu li-men yerâ, gloss:cehennem gören herkes için ortaya çıkarılır, source:79:36}, {ar:وَبُرِّزَتِ ٱلْجَحِيمُ لِلْغَاوِينَ, tr:ve burrizeti'l-cahîmu li'l-ğâvîn, gloss:cehennem azgınlara gösterilir, source:26:91}. Her can da yanında bir sürücü ve bir şahitle gelir: {ar:وَجَآءَتْ كُلُّ نَفْسٍۢ مَّعَهَا سَآئِقٌۭ وَشَهِيدٌۭ, tr:ve câet kullu nefsin meahâ sâikun ve şehîd, gloss:her can yanında bir sürücü ve bir şahitle gelir, source:50:21}. Safın kendisi de başka sahnelerde vardır: {ar:يَوْمَ يَقُومُ ٱلرُّوحُ وَٱلْمَلَٰٓئِكَةُ صَفًّۭا, tr:yevme yekûmu'r-rûhu ve'l-melâiketu saffâ, gloss:Ruh ve meleklerin saf hâlinde durduğu gün, source:78:38}, {ar:وَٱلصَّٰٓفَّٰتِ صَفًّۭا, tr:ve's-sâffâti saffâ, gloss:saf saf dizilenlere andolsun, source:37:1}. İnsanlar da Rabbe saf hâlinde sunulur: {ar:وَعُرِضُوا۟ عَلَىٰ رَبِّكَ صَفًّۭا, tr:ve urıdû alâ rabbike saffâ, gloss:Rabbine saf hâlinde sunuldular, source:18:48}. Bu geliş inkârcıların beklediği şeyin gerçekleşmesidir: {ar:هَلْ يَنظُرُونَ إِلَّآ أَن يَأْتِيَهُمُ ٱللَّهُ فِى ظُلَلٍۢ مِّنَ ٱلْغَمَامِ وَٱلْمَلَٰٓئِكَةُ, tr:hel yenzurûne illâ en ye'tiyehumu'llâhu fî zulelin mine'l-ğamâmi ve'l-melâike, gloss:onlar Allah'ın ve meleklerin bulut gölgeleri içinde gelmesinden başka bir şey mi bekliyorlar, source:2:210}. Aynı bekleyiş başka bir ayette de dile getirilir {source:6:158}. Göğün bulutla yarıldığı ve meleklerin indirildiği gün de anlatılır {source:25:25}.

Kaynaklar: 89:1 ٱلْفَجْرِ ف ج ر B003; 89:2 عَشْرٍۢ ع ش ر B005; 89:3 ٱلْوَتْرِ و ت ر B004; 89:21 دَكًّۭا د ك ك B008; 89:22 وَجَآءَ ج ي ء B001; 89:22 وَٱلْمَلَكُ م ل ك B009; 89:22 صَفًّۭا ص ف ف B001; 89:23 وَجِا۟ىٓءَ ج ي ء B004

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

