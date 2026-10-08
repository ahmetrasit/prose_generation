Focus: 98:7. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/98_7/D.r13/context.md =====
# 98:7 — focus

إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ

Anchor translation (canonical reading, reference only):

Kuşkusuz inanan ve iyi işler yapanlar, işte onlar yaratılmışların en iyileridir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | إِنَّ | إِنّ |  | ACC |
| 2 | ٱلَّذِينَ | ٱلَّذِى |  | REL |
| 3 | ءَامَنُوا۟ | ءَامَنَ | ء م ن | V;PRON |
| 4 | وَعَمِلُوا۟ | عَمِلَ | ع م ل | CONJ;V;PRON |
| 5 | ٱلصَّٰلِحَٰتِ | صَّٰلِحَٰت | ص ل ح | DET;N |
| 6 | أُو۟لَٰٓئِكَ | أُولَٰٓئِك |  | DEM |
| 7 | هُمْ |  |  | PRON |
| 8 | خَيْرُ | خَيْر | خ ي ر | N |
| 9 | ٱلْبَرِيَّةِ | بَرِيَّة | ب ر ء | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 98 — full text (context; no pericope)

- 98:1 لَمْ يَكُنِ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ مُنفَكِّينَ حَتَّىٰ تَأْتِيَهُمُ ٱلْبَيِّنَةُ
- 98:2 رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ
- 98:3 فِيهَا كُتُبٌۭ قَيِّمَةٌۭ
- 98:4 وَمَا تَفَرَّقَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ إِلَّا مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَةُ
- 98:5 وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ
- 98:6 إِنَّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ ۚ أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ
- 98:7 ◀ focus إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ
- 98:8 جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ


===== _commentary/v16/work/98_7/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ء م ن (root_000054) — identity root of ءَامَنُوا۟ (w3)

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ع م ل (root_001046) — identity root of وَعَمِلُوا۟ (w4)

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

## ص ل ح (root_000876) — identity root of ٱلصَّٰلِحَٰتِ (w5)

- **B001** iyi ve düzgün olma; düzeltme — iyilik, düzgünlük ve bozulmamışlık · iyi ve düzgün duruma gelmek · kendisi iyi ve düzgün olan kişi; iyi ve yararlı iş · işlerini düzelten veya başkasını iyi duruma getiren kimse · bozukluğu giderip iyi ve düzgün duruma getirme · hayvana iyi davranmak · iyilik ya da yarar sağlayan şey · iyi ve yararlı duruma getirmeye çalışma
  أصل واحد يدل على خلاف الفساد (maqayis)؛ الصلاح نقيض الطلاح ورجل صالح ومصلح وأصلحت إلى الدابة أحسنت إليها (ayn)؛ الصلاح ضد الطلاح وصلح الرجل صلاحا وصلوحا (jamhara)؛ الصلاح ضد الفساد والاصلاح نقيض الإفساد والمصلحة والاستصلاح (sihah)؛ الصلاح ضد الفساد مختصان في أكثر الاستعمال بالأفعال وإصلاح الله تعالى الإنسان (mufradat)
- **B002** barışma ve uzlaşma — barışma, uzlaşma ve aradaki soğukluğun giderilmesi · birbiriyle barışıp uzlaşmak
  والصلح تصالح القوم بينهم (ayn)؛ الصلاح بكسر الصاد المصالحة والاسم الصلح وقد اصطلحا وتصالحا واصالحا (sihah)؛ الصلح يختص بإزالة النفار بين الناس، يقال اصطلحوا وتصالحوا (mufradat)
- **B003** sana uygun olma [kalıp] — bu sana uygundur; bu sana uyar
  وهذا الشئ يصلح لك، أي هو من بابتك (sihah)
- **B004** kişi adı olan kök türevleri — bu kökten türemiş kişi adları; bunlardan biri bir peygamber adıdır
  وقد سمت العرب صالحا وصليحا ومصلحا (jamhara)؛ وصالح اسم للنبي عليه السلام (mufradat)
- **B005** bir kent ve bir nehir için özel adlar — belirli bir kentin özel adı · belirli bir nehrin özel adı
  إن مكة تسمى صلاحا (maqayis)؛ والصلح نهر بميسان (ayn)؛ وصلاح في وزن حذام وقطام وهو اسم مكة (jamhara)؛ وصلاح مثل قطام اسم مكة (sihah)

## خ ي ر (root_000452) — identity root of خَيْرُ (w8)

- **B001** arzulanan iyilik — iyilik; yarar veya üstünlük taşıyan olumlu şey
  فالخير خلاف الشر لأن كل أحد يميل إليه (maqayis)؛ الخير ضد الشر (jamhara;sihah)؛ الخير ما يرغب فيه الكل وضده الشر (mufradat)؛ يقابل به الشر مرة والضر مرة (mufradat)
- **B002** iyi ve seçkin olma — iyi ve üstün nitelikli · üstün, güzel veya seçkin olan · üstün veya seçkin kimse ya da şey · iyi ve erdemli kişiler · üstün, güzel veya seçilmiş olanlar
  رجل خير وامرأة خيرة فاضلة وقوم خيار وأخيار في صلاحها وامرأة خيرة في جمالها وميسمها (maqayis;ayn)؛ رجل خير إذا كان فيه خير ورجل خيار من قوم خيار وأخيار والأخيار خلاف الأشرار (jamhara)؛ الخيرات جمع خيرة وهي الفاضلة من كل شيء (sihah)؛ فيهن مختارات لا رذل فيهن والخير الفاضل المختص بالخير (mufradat)
- **B003** daha iyi olanı seçme — seçim veya seçim hakkı · seçim, seçilmiş şey veya seçim sonucu · daha iyi olanı arayıp seçme · seçmek veya üstün tutmak · Yaratıcıdan kişi için iyi sonucu dilemek · Yaratıcının kişi için iyi olanı seçip vermesi · iki şey arasında seçim hakkını ona bırakmak · seçimde üstün gelmek veya diğerini geçmek · seçen ya da seçilmiş olan
  الخيرة الخيار والاستخارة أن تسأل خير الأمرين لك ويقال خايرت فلانا فخرته وتقول اختر (maqayis)؛ خايرت فلانا فخرته والله يخير للعبد إذا استخاره وهذا وهذه وهؤلاء خيرتي وهو ما تختاره (ayn)؛ الخيار الاسم من الاختيار والخيرة من قولك خار الله لك والاختيار الاصطفياء والاستخارة الخيرة وخيرته بين الشيئين (sihah)؛ الاختيار طلب ما هو خير وفعله واستخار الله العبد فخار له وخايرت فلانا كذا فخرته (mufradat)
- **B004** mal, özellikle çok veya övülen bir yoldan edinilmiş servet — mal, özellikle çok veya iyi yoldan edinilmiş servet
  إن ترك خيرا أي مالا (sihah;mufradat)؛ لا يقال للمال خير حتى يكون كثيرا ومن مكان طيب (mufradat)؛ وإنه لحب الخير لشديد أي المال الكثير (mufradat)؛ ما كان مجموعا من المال من وجه محمود (mufradat)
- **B005** cömertlik ve armağan verme — cömertlik, armağan ve verme
  والخير الكرم (maqayis)؛ الخير الهبة (ayn)؛ رجل ذو خير إذا كان كثير الخير (jamhara)؛ الخير بالكسر الكرم (sihah)
- **B006** bir geçidi tıkayıp hayvanı yuvasından çıkarma [kalıp] — sırtlanı, yuvasının bir geçidini tıkayarak başka çıkıştan çıkarma · çöl sıçanını, yuvasının bir geçidini tıkayarak başka çıkıştan çıkarma
  استخاره الضبع وهو أن تجعل خشبة في ثقبة بيتها حتى تخرج من مكان إلى آخر (maqayis)؛ يستخير الضبع واليربوع إذا جعل في موضع النافقاء فخرج من القاصعاء (ayn)

## ب ر ء (root_000099) — identity root of ٱلْبَرِيَّةِ (w9)

- **B001** yaratıp var etme — Tanrı varlıkları yarattı ve ortaya çıkardı · yaratma anlamındaki ad · Tanrı için kullanılan yaratıcı nitelemesi · yaratılmış varlıklar topluluğu
  برأ الله الخلق يبرؤهم برءا (maqayis;ayn;sihah;tahdhib)؛ البارئ (maqayis;ayn;sihah;tahdhib;mufradat)؛ البرية الخلق (sihah;tahdhib;mufradat)
- **B002** ilişik kesip uzak durma — bir kimseden uzaklaşıp ilişiğini kesti · istenmeyen şeyden sakınıp uzak durdu · kusurdan ve istenmeyenden temiz olma · istenmeyen şeyden ayrılmış ve uzak duran · açık uyarı ve ilişik kesme bildirimi
  التباعد من الشيء ومزايلته (maqayis)؛ أصل البرء والبراء والتبري التقصي مما يكره مجاورته (mufradat)؛ برئت منك وبرئت من فلان وتبرأت (sihah;tahdhib;mufradat)؛ البراءة من العيب والمكروه (maqayis;ayn)؛ برآءة من الله ورسوله أي إعذار وإنذار (tahdhib)
- **B003** hastalıktan iyileşme — hastalıktan kurtulup iyileşti · hastalıktan kurtulup sağlığa dönme · hastalığından iyileşmiş · Tanrı hastalığını giderip iyileştirdi
  البرء السلامة من السقم (maqayis;ayn)؛ برأ من المرض برءا (jamhara;sihah;tahdhib)؛ أبرأه الله من مرضه إبراء (sihah;tahdhib)؛ برأت من المرض وبرئت من المرض (mufradat;tahdhib)
- **B004** hak veya borçtan salıverme — hakkımı sana bıraktım ve ondan çekildim · borç yükünden çıktı · kişiyi borç veya güvence yükünden salıverdi · onu üzerindeki haktan salıverdi · eş veya ortakla karşılıklı bağları çözerek ayrıldı
  برئت إليك من حقك (maqayis)؛ برئت من الديون (sihah)؛ أبرأت من الدين والضمان (maqayis;ayn)؛ أبرأته مما لي عليه وبرأته تبرئة (sihah)؛ بارأت المرأة صاحبها على المفارقة وبارأت شريكي (maqayis;sihah)؛ بارأت الرجل أي برئ إلي وبرئت إليه (ayn)
- **B005** boşluğu yoklayıp temizleme — boşluğu araştırıp güvenceye alma · satın alınan kadınla ilişki öncesi bekledi · elindeki şeyi yoklayıp arıttı · idrar sonrası organı temizleme
  الاستبراء أن يشتري الرجل جارية فلا يطأها حتى تحيض (maqayis;ayn)؛ استبرأت الجارية واستبرأت ما عندك (sihah)؛ الاستبراء إنقاء الذكر بعد البول (ayn)
- **B006** özel ay gecesi adı — ayın son gecesi için özel ad · ayın ilk gecesi için özel ad · istenmeyenden uzak sayılan uğurlu gün
  البراء آخر ليلة من الشهر (maqayis;tahdhib)؛ البراء أول ليلة من الشهر (sihah)؛ اليوم البراء السعد (maqayis)
- **B007** avcı gizlenme sığınağı — avcının gizlendiği sığınak veya örtülü yer · avcı gizlenme sığınakları
  برأة الصائد ناموسه وهي قترته والجمع برأ (maqayis)؛ البرأة بالهمز ناموس الصائد والجمع برأ (jamhara)؛ البرأة بالضم قترة الصائد والجمع برأ (sihah)

## ب ر ء (root_000100) — identity root of ٱلْبَرِيَّةِ (w9)

- **B001** yaratıp var etme — Tanrı varlıkları yarattı ve ortaya çıkardı · Tanrı için yaratıcı nitelemesi · yaratılmış varlıklar topluluğu
  برأ الله الخلق يبرؤهم برءا (maqayis;tahdhib)؛ البارئ الله جل ثناؤه (maqayis)؛ الله البارىء الذارىء (tahdhib)؛ البرية الخلق (tahdhib)
- **B002** ilişik kesip uzak durma — bir şeyden temiz, uzak ve kurtulmuş · muhataptan veya benimsenmeyen şeyden ilişik kesme bildirimi · açık uyarı ve ilişik kesme bildirimi · kusurdan ve istenmeyenden uzak olma
  التباعد من الشيء ومزايلته (maqayis)؛ البراءة من العيب والمكروه (maqayis)؛ برىء إذا تخلض وتنزه وتباعد (tahdhib)؛ برآءة من الله ورسوله أي إعذار وإنذار (tahdhib)؛ أنا براء منك (maqayis;tahdhib)
- **B003** hastalıktan iyileşme — hastalıktan kurtulup iyileşme · hastalıktan kurtulup iyileşti · Tanrı hastalığını giderip iyileştirdi
  البرء وهو السلامة من السقم (maqayis)؛ برئت وبرأت (maqayis)؛ برأت من المرض برءا وبرئت أبرأ برءا (tahdhib)؛ أبرأه الله من مرضه إبراء (tahdhib)
- **B004** hak bağını çözme [kalıp] — borç yükünden kurtuldu · hakkımı sana bırakıp ondan çekildim · borç ve güvence yükünü düşürdü · eşinden karşılıklı bağ çözerek ayrıldı
  برئت إليك من حقك (maqayis)؛ أبرأت من الدين والضمان (maqayis)؛ بارأت المرأة صاحبها على المفارقة وبارأت شريكي (maqayis)؛ برئت من الدين (tahdhib)؛ برئت إليك من فلان (tahdhib)
- **B005** ilişki öncesi boşluk yoklama — satın alınan kadınla ilişki öncesi bekleyip kuşkudan boşluğu sağlama
  الاستبراء أن يشتري الرجل جارية فلا يطأها حتى تحيض (maqayis)؛ برئت من الريبة التي تمنع المشتري من مباشرتها (maqayis)
- **B006** ayın son gecesi adı — ayın son gecesi için özel ad · istenmeyenden uzak sayılan uğurlu gün
  البراء آخر ليلة من الشهر (maqayis;tahdhib)؛ يبرأ فيها القمر من الشمس (tahdhib)؛ اليوم البراء السعد (maqayis)
- **B007** avcı gizlenme sığınağı — avcının gizlendiği sığınak veya örtülü yer · avcı gizlenme sığınakları
  برأة الصائد ناموسه وهي قترته والجمع برأ (maqayis)؛ قد زايل إليها كل أحد (maqayis)

===== _commentary/v16/out/s098/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 98:7, and ## Buluşmalar) =====
## Katkıyı ayıklamak: yıkamak, süzmek, saf olanı ayırmak

İkinci ayette sayfalar arındırılmıştır; beşinci ayette kulluk edenlerden muhlis olmaları ve zekât vermeleri istenir; altıncı ve yedinci ayetler yaratılmışları iki uca ayırır. Bu kelimelerin altında somut işlemler vardır. Tahâret suyla yıkanmaktır: {ar:تطهرت بالماء, tr:tetahhartü bi'l-mâ', gloss:suyla temizlendim, source:"ط ه ر,B003"}; su kendisi temizdir ve temizler: {ar:الطهور الطاهر في نفسه المطهر لغيره, tr:et-tahûr et-tâhiru fî nefsihî el-mutahhiru li-gayrih, gloss:tahûr, kendisi temiz olan ve başkasını temizleyendir, source:"ط ه ر,B004"}. İhlâsın kökü katkıdan arınmış olandır: {ar:الخالص هو ما زال عنه شوبه بعد أن كان فيه, tr:el-hâlisu mâ zâle anhü şevbühû ba'de en kâne fîh, gloss:hâlis, içindeki karışım giderilmiş olandır, source:"خ ل ص,B001"}. İşlemin kendisi tereyağını süzmektir: {ar:خلاصة السمن ما ألقي فيه من تمر أو سويق ليخلص به, tr:hulâsatü's-semn, gloss:yağın hulâsası, arınsın diye içine atılan hurma ya da kavrulmuş undur, source:"خ ل ص,B008"}; dipte kalan tortunun da adı vardır: {ar:الثفل الذي يكون أسفل هو الخلوص, tr:es-süfl ellezî yekûnü esfel, gloss:dipteki tortu, source:"خ ل ص,B008"}. Yağ kaynatılır, içine hurma ya da un atılır, karışım dibe çöker, üstteki berrak kısım alınır. Surenin kendi ifadesi bu işlemle açıklanır: {ar:أخلصت لله ديني أمحضته, tr:ahlastü li'llâhi dînî emhadtühû, gloss:dinimi Allah'a halis kıldım, onu katışıksız yaptım, source:"خ ل ص,B005"}. {ar:مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:muhlisîne lehü'd-dîn, gloss:dini O'na has kılarak, source:98:5} sözünün arka planında, tortusundan ayrılmış berrak yağ duyulur.

Zekât da arınmadır: {ar:زكاة لأنها طهارة, tr:zekâtün li-ennehâ tahâra, gloss:zekâttır, çünkü bir temizliktir, source:"ز ك و,B002"}; bu tanım zekâtı ikinci ayetteki mutahhera kelimesinin köküne bağlar. Sayfaların lekeden arınması ile dinin karışımdan arınması aynı işlemin iki yüzüdür. Berîye kelimesinin kökü de kusurdan ve hastalıktan kurtulmayı anlatır: {ar:البراءة من العيب والمكروه, tr:el-berâetü mine'l-ayb, gloss:kusurdan ve hoşa gitmeyenden uzak olmak, source:"ب ر ء,B002"}; {ar:البرء السلامة من السقم, tr:el-bur'u es-selâmetü mine's-sekam, gloss:iyileşmek, hastalıktan kurtulmak, source:"ب ر ء,B003"}. Ayıklamanın iki ucu altıncı ve yedinci ayettedir. Hayr herkesin istediği, her şeyin seçkin kısmıdır: {ar:الخير ما يرغب فيه الكل وضده الشر, tr:el-hayru mâ yerğabu fîhi'l-küll, gloss:hayır, herkesin rağbet ettiği şeydir, karşıtı şerdir, source:"خ ي ر,B001"}; {ar:الخيرات جمع خيرة وهي الفاضلة من كل شيء, tr:el-hayrât, gloss:her şeyin en üstünü, source:"خ ي ر,B002"}. Şerr ise {ar:الشر الذي يرغب عنه الكل, tr:eş-şerru ellezî yerğabu anhü'l-küll, gloss:herkesin yüz çevirdiği şey, source:"ش ر ر,B001"}. {ar:شَرُّ ٱلْبَرِيَّةِ, tr:şerru'l-beriyye, gloss:yaratılmışların en kötüsü, source:98:6} ile {ar:خَيْرُ ٱلْبَرِيَّةِ, tr:hayru'l-beriyye, gloss:yaratılmışların en hayırlısı, source:98:7} böylece süzmenin iki ürünü olarak duyulur: alınıp saklanan berrak kısım ve dibe çöküp atılan tortu.

Kur'an bu işlemleri yan yana koyar. Tevbe suresinde Peygamber'e {ar:خُذْ مِنْ أَمْوَٰلِهِمْ صَدَقَةًۭ تُطَهِّرُهُمْ وَتُزَكِّيهِم بِهَا وَصَلِّ عَلَيْهِمْ, tr:huz min emvâlihim sadakaten tutahhiruhüm ve tüzekkîhim bihâ ve salli aleyhim, gloss:mallarından onları temizleyip arındıracak bir sadaka al ve onlar için dua et, source:9:103} denir; tahâret, zekât ve salât tek ayettedir. Nahl suresinde hayvanlardan çıkan süt, halisin tortudan ayrılmasını gösterir: {ar:مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:min beyni fersin ve demin lebenen hâlisan sâiğan li'ş-şâribîn, gloss:işkembedeki artıkla kan arasından, içenlere kolayca geçen halis bir süt, source:16:66}. Zümer suresinde Peygamber'e verilen emir surenin beşinci ayetine çok yakındır: {ar:فَٱعْبُدِ ٱللَّهَ مُخْلِصًۭا لَّهُ ٱلدِّينَ, tr:fa'budi'llâhe muhlisan lehü'd-dîn, gloss:dini yalnız O'na has kılarak Allah'a kulluk et, source:39:2}; ardından {ar:أَلَا لِلَّهِ ٱلدِّينُ ٱلْخَالِصُ, tr:elâ li'llâhi'd-dînü'l-hâlis, gloss:iyi bilin ki halis din Allah'ındır, source:39:3}. Nisâ suresi tövbe edenleri {ar:وَأَخْلَصُوا۟ دِينَهُمْ لِلَّهِ, tr:ve ahlasû dînehüm li'llâh, gloss:dinlerini Allah'a halis kıldılar, source:4:146} diye anar. Leyl suresinde arınmak için malını veren {ar:ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ, tr:ellezî yü'tî mâlehû yetezekkâ, gloss:arınmak için malını veren, source:92:18} anılır; Furkân suresinde gökten indirilen su {ar:مَآءًۭ طَهُورًۭا, tr:mâen tahûrâ, gloss:tertemiz ve temizleyici bir su, source:25:48} olarak Allah'ın ayetleri arasında sayılır.

Kaynaklar: 98:2 مُّطَهَّرَةً ط ه ر B003 B004; 98:5 مُخْلِصِينَ خ ل ص B001 B005 B008; 98:5 ٱلزَّكَوٰةَ ز ك و B002; 98:6 ٱلْبَرِيَّةِ ب ر ء B002 B003; 98:7 خَيْرُ خ ي ر B001 B002; 98:6 شَرُّ ش ر ر B001

## Hesap: borç, rehin, kefil, ödeme ve ibra

Din kelimesi itaattir; borç vermek ve almak da bu köktedir: {ar:الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء, tr:ed-deyn ve dâyentü fülânen, gloss:deyn; filanla alarak ya da vererek borç alışverişi yaptım, source:"د ي ن,B003"}; ve din karşılığın kendisidir: {ar:الدين الجزاء والمكافأة, tr:ed-dînü el-cezâü ve'l-mükâfee, gloss:din, karşılık ve bedeldir, source:"د ي ن,B002"}. Ceza da borcun ödenmesi ve tahsilidir: {ar:جزيت فلانا حقه؛ جزيته قرضه, tr:cezeytü fülânen hakkahû, gloss:filana hakkını ödedim; borcunu ödedim, source:"ج ز ي,B002"}; {ar:تجازيت ديني على فلان إذا تقاضيته, tr:tecâzeytü deynî alâ fülân, gloss:filandaki alacağımı tahsil ettim, source:"ج ز ي,B003"}. Bu son cümle ceza ile din köklerini birleştirir. Karşılığın ölçüsü de verilir: {ar:الجزاء ما فيه الكفاية من المقابلة إن خيرا فخير وإن شرا فشر, tr:el-cezâü mâ fîhi'l-kifâyetü mine'l-mukâbele, in hayran fe-hayr ve in şerran fe-şer, gloss:ceza, karşılıkta yeterli olandır: iyilikse iyilik, kötülükse kötülük, source:"ج ز ي,B001"}. Bu tanım altıncı ve yedinci ayetlerdeki şerr ve hayr kelimelerini sekizinci ayetteki {ar:جَزَآؤُهُمْ, tr:cezâühüm, gloss:karşılıkları, source:98:8} kelimesine bağlar.

Hesabın diğer parçaları surenin başka kelimelerinde durur. İnfikâkın kökü rehnin çözülmesidir: {ar:فك الرقبة تخليصها من إسار الرق وفك الرهن وفكاكه تخليصه من غلق الرهن, tr:fekkü'r-rakabeti tahlîsuhâ min isâri'r-rıkk ve fekkü'r-rehn, gloss:boynu çözmek onu kölelik bağından kurtarmak, rehni çözmek onu rehin kilidinden kurtarmaktır, source:"ف ك ك,B002"}; açıklamada kurtarmak için kullanılan tahlîs, muhlisîn kelimesinin köküdür. Berîye kelimesinin kökü borçtan aklanmaktır: {ar:برئت من الديون, tr:beri'tü mine'd-düyûn, gloss:borçlardan kurtuldum, source:"ب ر ء,B004"}. Tilâvetin kökü borcun kalanını ve alacağın devrini anlatır: {ar:التلية بقية الدين, tr:et-tuliyyetü bakıyyetü'd-deyn, gloss:tuliyye, borcun kalanıdır, source:"ت ل و,B003"}. Kitabın kökü, kölenin bedelini taksitle ödeyip özgürlüğünü satın aldığı sözleşmedir: {ar:المكاتب العبد يكاتب على نفسه بثمنه فإذا سعى وأداه عتق, tr:el-mükâteb, gloss:mükâteb, kendi bedeli üzerine yazılı anlaşma yapan köledir; çalışıp ödeyince özgür olur, source:"ك ت ب,B005"}. Kayyime bir şeyin biçilen değeridir: {ar:القيمة ثمن الشيء بالتقويم, tr:el-kıymetü semenü'ş-şey'i bi't-takvîm, gloss:kıymet, değer biçmeyle belirlenen bedel, source:"ق و م,B010"}. Surenin üç kelimesi kefili adlandırır: {ar:كنت على فلان أكون كونا أي تكفلت به, tr:küntü alâ fülân, gloss:filana kefil oldum, source:"ك و ن,B003"}; {ar:الجري الضامن, tr:el-cerî ed-dâmin, gloss:cerî, kefildir, source:"ج ر ي,B003"}; {ar:الرضي المطيع والرضي المحب والرضي الضامن, tr:er-radiyy, gloss:radî, itaat eden, seven ve kefil olandır, source:"ر ض و,B006"}.

Ödemenin ters yönü de vardır. Gelmek kökü haracı adlandırır ve ceza köküyle eşitlenir: {ar:الإتاوة الخراج أو الجزية يؤديه القوم إلى الملك, tr:el-itâve el-harâc evi'l-cizye, gloss:itâve, bir topluluğun hükümdara ödediği harac ya da cizye, source:"ء ت ي,B008"}. Cizye de üzerindekini ödemektir: {ar:الجزية … سميت جزية لأنها قضاء منه لما عليه, tr:el-cizye, gloss:cizye, üzerindeki borcu ödemesi olduğu için bu adı aldı, source:"ج ز ي,B004"}. Gönüllü verişin de bir adı vardır: {ar:إلا من أعطى في رسلها أي بطيب نفس منه, tr:illâ men a'tâ fî rislihâ, gloss:gönül hoşluğuyla veren hariç, source:"ر س ل,B010"}; hayr da hibe ve maldır: {ar:الخير الهبة, tr:el-hayru el-hibe, gloss:hayır, bağıştır, source:"خ ي ر,B005"}. Zekât, insanın Allah hakkı olarak fakirlere çıkardığıdır: {ar:ما يخرج الإنسان من حق الله تعالى إلى الفقراء, tr:mâ yuhricü'l-insânu min hakkı'llâh, gloss:insanın Allah hakkından fakirlere çıkardığı, source:"ز ك و,B003"}.

Bu kelimelerle sure bir hesap olarak duyulur. Dördüncü ayette kitap verilir; beşinci ayette verilenlerden din, yani borç bilinciyle sürdürülen bir itaat ve zekâtın verilmesi istenir; altıncı ve yedinci ayetlerde hayr ve şerr tartılır; sekizinci ayette ödeme yapılır ve hesap Rableri katında, {ar:عِندَ رَبِّهِمْ, tr:inde rabbihim, gloss:Rableri katında, source:98:8}, emanet gibi saklanır. Hesap karşılıklı bir hoşnutlukla kapanır: {ar:رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ, tr:radıya'llâhü anhüm ve radû anh, gloss:Allah onlardan razı olmuş, onlar da O'ndan razı olmuşlardır, source:98:8}; {ar:المراضاة من اثنين, tr:el-murâdâtü mine'sneyn, gloss:murâdât iki taraf arasında olur, source:"ر ض و,B003"}. Alışverişin sonunda iki tarafın birbirinden razı olması gibi.

Kur'an borcu, yazıyı ve ödemeyi açıkça birleştirir. Bakara suresinde müminlere {ar:إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ, tr:izâ tedâyentüm bi-deynin ilâ ecelin müsemmen fektübûh, gloss:belirli bir süreye kadar borçlandığınızda onu yazın, source:2:282} denir. Müddessir suresinde {ar:كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ رَهِينَةٌ, tr:küllü nefsin bimâ kesebet rehîne, gloss:her can kazandığına karşılık rehindir, source:74:38}; Beled suresinde sarp yokuş {ar:فَكُّ رَقَبَةٍ, tr:fekkü rakabe, gloss:bir boyun çözmek, source:90:13} diye açıklanır. Nûr suresinde özgürlük sözleşmesi yazıyla ve vermeyle kurulur: {ar:فَكَاتِبُوهُمْ إِنْ عَلِمْتُمْ فِيهِمْ خَيْرًۭا ۖ وَءَاتُوهُم مِّن مَّالِ ٱللَّهِ ٱلَّذِىٓ ءَاتَىٰكُمْ, tr:fe-kâtibûhüm in alimtüm fîhim hayrâ, ve âtûhüm min mâli'llâhi'llezî âtâküm, gloss:onlarda bir hayır görürseniz onlarla yazılı anlaşma yapın ve Allah'ın size verdiği maldan onlara verin, source:24:33}. Tevbe suresinde Allah müminlerden canlarını ve mallarını satın alır: {ar:بِأَنَّ لَهُمُ ٱلْجَنَّةَ, tr:bi-enne lehümü'l-cenne, gloss:karşılığında cennet onlarındır, source:9:111}. Karşılığın denkliği Nebe' suresinde {ar:جَزَآءًۭ وِفَاقًا, tr:cezâen vifâkâ, gloss:tam denk bir karşılık, source:78:26}, Rahmân suresinde iyilik için söylenir {source:55:60}. Lokmân suresinde o gün kimse kimsenin borcunu ödeyemez: {ar:وَٱخْشَوْا۟ يَوْمًۭا لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ, tr:vahşev yevmen lâ yeczî vâlidün an veledih, gloss:babanın evladı yerine ödeme yapamayacağı günden korkun, source:31:33}; sekizinci ayetin son kelimesindeki haşyet burada da vardır. Fâtiha'daki {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:mâliki yevmi'd-dîn, gloss:din gününün sahibi, source:1:4} ve Bakara suresindeki aynı uyarı {source:2:48} bu hesabın gününü adlandırır. Tevbe suresi müşriklere bir ibra ilanıyla açılır: {ar:بَرَآءَةٌۭ مِّنَ ٱللَّهِ وَرَسُولِهِۦٓ إِلَى ٱلَّذِينَ عَٰهَدتُّم مِّنَ ٱلْمُشْرِكِينَ, tr:berâetün mina'llâhi ve resûlihî ile'llezîne âhedtüm mine'l-müşrikîn, gloss:Allah'tan ve elçisinden, antlaşma yaptığınız müşriklere bir ilişik kesme, source:9:1}. Aynı surede kitap verilenlerin cizyesi {ar:حَتَّىٰ يُعْطُوا۟ ٱلْجِزْيَةَ عَن يَدٍۢ, tr:hattâ yu'tu'l-cizyete an yed, gloss:cizyeyi elden verinceye kadar, source:9:29} diye anılır; muhataplar surenin dördüncü ayetindeki ûtu'l-kitâb'dır. Gönüllü veriş de aynı surededir: sadakalar fakirlere, toplayıcılara, boyunların çözülmesine ve borçlulara verilir {source:9:60}; namazı kılıp zekâtı verenler ise {ar:فَإِخْوَٰنُكُمْ فِى ٱلدِّينِ, tr:fe-ihvânüküm fi'd-dîn, gloss:dinde kardeşlerinizdir, source:9:11}. Karşılıklı hoşnutluk Tevbe suresinde surenin sekizinci ayetinin sözleriyle tekrarlanır: {ar:رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ وَأَعَدَّ لَهُمْ جَنَّٰتٍۢ تَجْرِى تَحْتَهَا ٱلْأَنْهَٰرُ, tr:radıya'llâhü anhüm ve radû anhü ve eadde lehüm cennâtin tecrî tahtehe'l-enhâr, gloss:Allah onlardan razı olmuş, onlar da O'ndan razı olmuşlardır; onlara altlarından ırmaklar akan cennetler hazırlamıştır, source:9:100}; Mâide suresinde de Allah'ın kıyamet günü sözüyle {source:5:119}. Fecr suresinde huzura kavuşmuş cana {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdıyeten mardıyye, gloss:Rabbine razı edici ve razı olunmuş olarak dön, source:89:28} denir.

Kaynaklar: 98:5 ٱلدِّينَ د ي ن B002 B003; 98:8 جَزَآؤُهُمْ ج ز ي B001 B002 B003 B004; 98:1 مُنفَكِّينَ ف ك ك B002; 98:6 ٱلْبَرِيَّةِ ب ر ء B004; 98:2 يَتْلُوا۟ ت ل و B003; 98:1 ٱلْكِتَٰبِ ك ت ب B005; 98:5 ٱلْقَيِّمَةِ ق و م B010; 98:1 يَكُنِ ك و ن B003; 98:8 تَجْرِى ج ر ي B003; 98:8 رَّضِىَ ر ض و B003 B006; 98:5 وَيُؤْتُوا۟ ء ت ي B008; 98:2 رَسُولٌ ر س ل B010; 98:7 خَيْرُ خ ي ر B005; 98:5 ٱلزَّكَوٰةَ ز ك و B003

## Buluşmalar

En yoğun buluşma beşinci ayetteki salât kelimesindedir. Kökü bir yandan ateşte ısıtılıp düzeltilen çubuğu, {ar:صليت العود بالنار, tr:salleytü'l-ûde bi'n-nâr, gloss:çubuğu ateşte ısıtıp yumuşattım, source:"ص ل و,B001"}, öbür yandan ateşe girip yanan kâfiri, {ar:صلى الكافر نارا, tr:sale'l-kâfiru nârâ, gloss:kâfir ateşe girip yandı, source:"ص ل و,B001"}, adlandırır. Aynı ateş iki iş görür: eğri olanı doğrultur ya da yakar. Beşinci ayette ateş bir doğrultma aletidir; altıncı ayette inkâr edenlerin kaldığı yerdir. Doğrultma ile ocak sahneleri böylece tek bir kökün iki işlemi olarak birleşir ve surenin ikiye ayrılan yolunu taşır: kanıttan sonra doğrulup ayağa kalkanlar ve ateşte kalanlar. Aynı kök tuzağı da adlandırır; ama surede salât tuzaktan sıyrılmış olanların fiilidir.

Münfekkîn kelimesi üç sahneyi bir noktada tutar. Kökü tuzaktan kurtulan ceylanı, mührü açılan mektubu ve çözülen rehni anlatır. Birinci ayette bu kelime olumsuzdur: ip çözülmemiş, mühür açılmamış, rehin kurtarılmamıştır, ve bütün bunlar kanıtın gelişine bağlıdır. Rehnin çözülmesini anlatan cümlede infikâkın ve ihlâsın kökü yan yanadır, tuzaktan kurtulmayı anlatan cümlelerde de; bu yüzden birinci ayetteki çözülmeme ile beşinci ayetteki muhlisîn, hem avın hem borçlunun kurtuluşu olarak duyulur. Yazı ile kenet de aynı kelimede buluşur: mühürlü mektubun açılması ile iki çenenin ayrılması tek cümlede verilir ve dördüncü ayette açılan yazının ardından gelen ayrılık bunun devamıdır.

Teferruk kelimesi kenet ile yol sahnesini birleştirir. En'âm suresinde yan yollara uyunca insanların yoldan ayrı düşmesi {source:6:153}, hem çatallanan yolu hem bölünen topluluğu tek cümlede gösterir. Müşriklerin kökü ana yoldan ayrılan küçük patikaları adlandırdığı için dördüncü ayetteki ayrılık arka planda bir çatal noktasına, beşinci ayetteki hunefâ ise yan patikadan ana yola dönüşe dönüşür. Yol ile binek sahnesi müzellel kelimesinde birleşir: yürünmekle düzleşen yol ile katranla uysallaşan deve aynı kelimeyle anlatılır ve inde kelimesinin kökü ikisinin de tersini, yoldan sapan ve dizgini çeken deveyi verir. Doğrultma ile yol da kayyime kelimesinde birleşir: dik duran beden ile düz hat üzerindeki yol aynı kökle anlatılır; En'âm suresinde Peygamber'e söyletilen söz {source:6:161} yolu, kayyim olanı, hanifi ve müşrikleri tek ayette toplar.

Arındırma ile ekim zekâtta birleşir. Zekât hem bir temizliktir hem ekinin büyümesi ve hurmanın ürünüdür. Tâhâ suresinde surenin sekizinci ayetinin bahçesi tam olarak bu kelimeyle bağlanır: Adn cennetleri {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76}. Beşinci ayetteki zekât, sekizinci ayetteki bahçenin tohumu gibi durur. Arındırma ile hesap da hayr ve şerr kelimelerinde buluşur: süzmenin iki ürünü, karşılığın iki ölçüsüne dönüşür, iyiliğe iyilik ve kötülüğe kötülük.

Örtü ile ocak da kesişir: küfrün kökü üstü örtülmüş külü adlandırır. Örtü ile ekim ise aynı kelimede, tohumu örten çiftçide buluşur. Bakara suresindeki temsil {source:2:266} bu sahnelerin üçünü birden tutar: altından ırmaklar akan hurma bahçesi ve onu yakan ateşli kasırga. Altıncı ve sekizinci ayetler aynı sözü, hâlidîne fîhâ, ateş ve bahçe için kullanır; hulûdun kökü bir yandan ateşin içinde kalan ocak taşlarını, öbür yandan bir yerde yerleşip kalmayı adlandırır. Kalmanın iki yeri böylece aynı kelimede yan yana durur.

Bu buluşmalar surenin hareketini taşır. Birinci ayette bir şey kapalıdır: ilmek düğümlü, mühür kırılmamış, topluluk kendi hâlinde. Kanıt bir elçinin elinde, arındırılmış sayfalar olarak gelir ve okunur. Dördüncü ayette topluluk bu kanıtın ardından bölünür. Beşinci ayet çıkış yolunu tek cümlede verir: işaretli, düzleşmiş, dosdoğru bir yol; katkısından süzülmüş bir din; ateşte doğrultulan bir beden; tuzaktan sıyrılış; ürün veren bir ekin. Altıncı ve yedinci ayetler sonucu iki uca ayırır. Sekizinci ayet bir yerleşmeyle biter: Rableri katında, örtülü bir bahçede, ebedî bir kalış ve iki tarafın birbirinden razı olduğu kapanmış bir hesap.

