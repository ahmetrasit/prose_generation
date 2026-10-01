Focus: 100:1. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/100_1/D.r13/context.md =====
# 100:1 — focus

وَٱلْعَٰدِيَٰتِ ضَبْحًۭا

Anchor translation (canonical reading, reference only):

Soluk soluğa koşanlara andolsun.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَٱلْعَٰدِيَٰتِ | عَٰدِيَٰت | ع د و | P;DET;N |
| 2 | ضَبْحًا | ضَبْح | ض ب ح | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 100 — full text (context; no pericope)

- 100:1 ◀ focus وَٱلْعَٰدِيَٰتِ ضَبْحًۭا
- 100:2 فَٱلْمُورِيَٰتِ قَدْحًۭا
- 100:3 فَٱلْمُغِيرَٰتِ صُبْحًۭا
- 100:4 فَأَثَرْنَ بِهِۦ نَقْعًۭا
- 100:5 فَوَسَطْنَ بِهِۦ جَمْعًا
- 100:6 إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌۭ
- 100:7 وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ
- 100:8 وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ
- 100:9 ۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ
- 100:10 وَحُصِّلَ مَا فِى ٱلصُّدُورِ
- 100:11 إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ


===== _commentary/v16/work/100_1/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ع د و (root_000993) — identity root of وَٱلْعَٰدِيَٰتِ (w1)

- **B001** hakkı aşan saldırganlık — uygun sınırı aşma · açık haksızlık ve saldırganlık · hakkı çiğneyerek sınırı aşma · sınırı aşan haksızlık · ona saldırıp malını alma ya da onu vurma · baskın yapan atlılar
  التعدي تجاوز ما ينبغي أن يقتصر عليه (maqayis;ayn)؛ العدوان الظلم الصراح (maqayis;sihah)؛ الاعتداء مجاوزة الحق (mufradat)؛ العادية الخيل المغيرة (ayn;sihah)
- **B002** yaya ya da atla koşma — yaya koşu ya da at koşusu · koşmak · atın iyi ve çok koşması
  العَدْو هو الحضر (maqayis;ayn;sihah)؛ يقال من عدو الفرس عدوان أي جيد العدو وكثيره (maqayis)؛ بالمشي فيقال له العدو (mufradat)
- **B003** düşmanlık ve düşman — düşman, dostun karşıtı · düşmanlar · düşmanlar · düşmanlık
  العَدُوّ ضد الولي والجمع الأعداء (sihah)؛ العداوة والمعاداة (sihah;mufradat)؛ يقال للواحد والاثنين والجمع عَدُوّ (maqayis)
- **B004** aşma, dışarıda bırakma ve öteye geçirme — belirtilen ögeyi kapsam dışında tutma · konuyu geçip başkasına yönelme · eylemin etkisini nesneye geçirme
  ما عدا زيدا أي ما جاوز زيدا (maqayis;ayn)؛ عدا فعل يستثنى به (sihah)؛ ما عدا كذا يستعمل في الاستثناء (mufradat)؛ عد عن هذا الأمر أي تجاوزه وخذ في غيره (maqayis)
- **B005** yetkiliden hakkını almasını isteme — yetkiliden yardım ve hakkını almasını isteme
  العَدْوى طلبك إلى وال أو قاض أن يعديك على من ظلمك (maqayis)؛ طلبك إلى وال ليعديك على من ظلمك (ayn;sihah)
- **B006** hastalığın bulaşması — hastalığın bulaşması · hastalığın birinden ötekine geçmesi
  العَدْوى ما يقال إنه يعدي من جرب أو داء (maqayis;ayn)؛ ما يعدي من جرب أو غيره ومجاوزته من صاحبه إلى غيره (sihah)
- **B007** işten alıkoyan uğraş veya engel — işten alıkoyan uğraş veya kötü olay · zamanın getirdiği engeller ve sıkıntılar · bir iş beni senden alıkoydu
  العادية شغل من أشغال الدهر يعدوك عن أمرك (maqayis;ayn)؛ عوادي الدهر عوائقه (sihah)؛ عدواء الشغل موانعه (sihah)
- **B008** iki avı peş peşe ele geçirme — iki avı peş peşe izleyip ele geçirme
  العِداء أن يعادي الفرس أو الكلب أو الصياد بين صيدين (maqayis)؛ العِداء الموالاة بين الصيدين (sihah)؛ فعادى عداء بين ثور ونعجة أي أعدى أحدهما إثر الآخر (mufradat)
- **B009** boyunca uzanan yan ve kıyı — bir şeyin eni ya da boyu boyunca uzanan yanı · ırmak kıyısı boyunca uzanan yan · vadinin yanı ve kıyısı
  العَداء طوار كل شيء (maqayis;sihah)؛ لزمت عداء النهر وطريق يأخذ عداء الجبل (maqayis)؛ العدوة جانب الوادي وحافته (sihah)؛ بالعدوة الدنيا أي الجانب المتجاوز للقرب (mufradat)
- **B010** sert, kuru ve engebeli yer — sert, kuru ve engebeli yer
  العَدْواء الأرض اليابسة الصلبة (maqayis)؛ العدواء المكان الذي لا يطمئن من قعد عليه (sihah)؛ مكان ذو عدواء أي غير متلائم الأجزاء (mufradat)
- **B011** develerin otladığı yaz yeşermesi — bahar geçince yeşeren ve develerin otladığı yaz bitkisi
  العَدَوِيّة من نبات الصيف بعد ذهاب الربيع يخضر فترعاه الإبل (maqayis)؛ العَدَوِيّة من نبات الصيف بعد ذهاب الربيع يخضر صغار الشجر فترعاه الإبل (sihah)
- **B012** eğrilik ve güçlük — eğrilik ve güçlük
  العَنْدَأْوَة التواء وعسر وهو من العداء (maqayis)

## ض ب ح (root_000901) — identity root of ضَبْحًا (w2)

- **B001** tilki sesi ve ona benzetilen sesler — tilki, gece kuşu ya da koşan atın özel sesini çıkarmak · tilki, gece kuşları ve kurt sesi ile yankı · bu özel sesi çıkaran · atlar koşarken ağızlarından veya soluklarından kişneme dışı ses çıkarmak
  صوت الثعلب وصوته الضباح (maqayis;jamhara;sihah;tahdhib;mufradat)؛ الهام تضبح والبوم والذئب والصدى (ayn;jamhara;tahdhib)؛ صوت أنفاس الخيل إذا عدون وليس بصهيل ولا حمحمة (ayn;sihah;tahdhib;mufradat)
- **B002** ön bacakları uzatarak koşma [kalıp] — at ön bacaklarını uzatarak yürümek veya koşmak · deve yürürken ön bacaklarını ileri uzatmak
  هو عدو فوق التقريب وأصله ضبع (maqayis)؛ ضبح الفرس وضبع إذا حرك ضبعيه في مشيه (jamhara)؛ ضبحت الخيل مثل ضبعت وهو السير (sihah;tahdhib)؛ مد الضبع في العدو والعدو الخفيف (mufradat)
- **B003** üst bölümünü ateşle yakma ve ateşten etkilenme — değneğin üst bölümünü ateşle yakma · değneğin üst bölümünden bir parçayı ateşte yakmak · ateşte yanmış, ateşten etkilenmiş veya ateşle doğrultulmuş · ateşle doğrultulmuş veya ateşin etkisi altında kalmış
  الضبح إحراق أعالي العود بالنار (maqayis;ayn;tahdhib;mufradat)؛ حجارة القداحة مضبوحة (maqayis;ayn;sihah;tahdhib)؛ كل شيء مسته النار فقد ضبحته (ayn)؛ قدح ضبيح ومضبوح إذا قوم بالنار (jamhara)
- **B004** siyaha doğru kararma — rengin hafifçe siyaha dönmesi · güneş rengini değiştirip koyulaştırdı
  الانضباح تغير اللون إلى السواد (maqayis)؛ انضبح لونه أي تغير إلى السواد قليلا (sihah)؛ ضبحته الشمس وضبته إذا غيرت لونه وكذلك النار (tahdhib)
- **B005** kül — kül
  الضبح الرماد (maqayis;sihah;tahdhib)

## ECHO ع د د (root_000989) — for وَٱلْعَٰدِيَٰتِ (w1): withheld observed target; not identity

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

## ECHO ع و د (root_001058) — for وَٱلْعَٰدِيَٰتِ (w1): withheld observed target; not identity

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

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 100:1, and ## Buluşmalar) =====
Burada sure 100 için istenen Türkçe yorum ve ardından kayıt bölümü yer alıyor. Kontrol betiği 100:1 ayeti için yalnızca on atıflık kısa bir listeyle çalıştırıldı, diğer on ayet ise tam listeyle denetlendi. Haritadaki 6 ile 7. zincirler, ayrıca 8 ile 9. zincirler tek görüntü olarak birleştirildi. Haritanın "mugîrât" için verdiği "yağmur ve erzak" anlamı geçerli sayılmadı, nedeni kayıtta yazılı.

## Koşan at: soluk, adım, inceltilmiş beden

Sure, kim olduklarını adlarıyla değil, yalnızca yaptıklarıyla bildiren bir topluluk üzerine yeminle açılır: {ar:وَٱلْعَٰدِيَٰتِ ضَبْحًا, tr:ve'l-âdiyâti dabhâ, gloss:soluk soluğa koşanlara andolsun, source:100:1}. Surenin hiçbir yerinde "at" kelimesi geçmez. Hayvan koşusundan, soluğundan, taşa vuran ayağından ve kaldırdığı tozdan tanınır. Kur'an başka yerlerde de yemini böyle açar: işiyle tanımlanan dişil çoğul bir topluluk getirir ve her yeni hareketi "fe" ile bir öncekinin hemen ardına bağlar. Bir örnek {ar:وَٱلصَّٰٓفَّٰتِ صَفًّا, tr:ve's-sâffâti saffâ, gloss:saf saf dizilenlere andolsun, source:37:1} ile {ar:فَٱلزَّٰجِرَٰتِ زَجْرًا, tr:fe'z-zâcirâti zecrâ, gloss:derken sürüp önlerine katanlara, source:37:2} çiftidir. Bir başkası {ar:وَٱلْمُرْسَلَٰتِ عُرْفًا, tr:ve'l-murselâti urfâ, gloss:ardı ardına gönderilenlere andolsun, source:77:1} ile {ar:فَٱلْعَٰصِفَٰتِ عَصْفًا, tr:fe'l-âsıfâti asfâ, gloss:derken fırtına gibi esenlere, source:77:2} çiftidir. Bu surede "fe" bağları koşuyu, kıvılcımı, sabahı, tozu ve kalabalığın ortasını tek bir hareketin ardışık aşamaları olarak dizer. Aşağıda bir kelimenin akrabalarından gelen görüntüler, o kelimenin ayetteki anlamının yanında duyulan ikinci bir ses olarak okunur. Bu görüntüler o anlamın yerine geçmez.

Birinci ayetin ilk kelimesinin kökü, koşunun en hızlısını adlandırır: {ar:العَدْو هو الحضر, tr:el-advu huve'l-hudr, gloss:adv dörtnala koşmaktır, source:"ع د و,B002"}. İyi ve çok koşan ata da aynı kökten bir sıfat verilir: {ar:يقال من عدو الفرس عدوان أي جيد العدو وكثيره, tr:yukâlu min advi'l-ferasi advân, ey ceyyidu'l-advi ve kesîruh, gloss:atın koşusundan "advân" denir, yani iyi ve çok koşan, source:"ع د و,B002"}. Ardından gelen kelime bu koşunun sesidir: {ar:صوت أنفاس الخيل إذا عدون وليس بصهيل ولا حمحمة, tr:savtu enfâsi'l-hayli izâ adevne ve leyse bi-sahîlin ve lâ hamhame, gloss:atların koşarken çıkardığı soluk sesi; ne kişneme ne homurtu, source:"ض ب ح,B001"}. Kişneme, hayvanın kendi sesidir. Burada duyulan ise zorlanan göğüsten dışarı itilen nefestir, yani kelime bir çabayı kulağa duyurur. Aynı kelime bir adım biçimini de adlandırır: {ar:ضبح الفرس وضبع إذا حرك ضبعيه في مشيه, tr:dabaha'l-ferasu ve daba'a izâ harreke dab'ayhi fî meşyih, gloss:at yürürken ön kollarını ileri atıp oynatınca "dabaha" denir, source:"ض ب ح,B002"}. Bu, {ar:هو عدو فوق التقريب وأصله ضبع, tr:huve advun fevka't-takrîbi ve asluhû dab', gloss:tırıştan hızlı bir koşudur, aslı "dab'"dır, source:"ض ب ح,B002"}. Böylece tek kelimede hem ileri uzanan ön ayaklar görülür hem de göğüsten çıkan nefes işitilir.

İkinci ayetin {ar:قَدْحًا, tr:kadhâ, gloss:çakarak, source:100:2} kelimesi ateşi anlatır. Ama bu kökün kalıplaşmış bir söyleyişi atın bedenini de gösterir: {ar:قدح الفرس تقديحا إذا ضمر حتى يصير مثل القدح, tr:kaddaha'l-ferasu takdîhan izâ damura hattâ yasîra misle'l-kıdh, gloss:at, ok çubuğu gibi oluncaya dek inceltildiğinde "kaddaha" denir, source:"ق د ح,B008"}. Koşu için yetiştirilen at fazlasından arındırılır ve gövdesi bir ok çubuğu kadar inceltilir. Beşinci ayetin {ar:جَمْعًا, tr:cem'â, gloss:bir topluluğu, source:100:5} kelimesinin yanında da aynı kökten bir at deyimi duyulur: {ar:استجمع الفرس جريا, tr:isteceme'a'l-ferasu cerye, gloss:at bütün koşusunu tek bir atılışta topladı, source:"ج م ع,B010"}.

Atın kökleri, insanı anlatan ayetlerde de geri gelir. Altıncı ayetteki {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan, source:100:6} kelimesinin kökü, bineğin bir yanını adlandırır: {ar:إنسي الدابة للجانب الذي يلي الراكب, tr:insiyyu'd-dâbbeti li'l-cânibi'llezî yelî'r-râkib, gloss:hayvanın "insî" yanı, binicinin bulunduğu taraftır, source:"ء ن س,B004"}. Hayvanın bir yanı insana dönüktür ve insan onun sırtındadır. Yedinci ayetteki {ar:لَشَهِيدٌ, tr:le-şehîd, gloss:elbette tanıktır, source:100:7} kelimesinin kökünde ise atın koşusu kendi kendinin tanığıdır: {ar:الشاهد من جريه ما يشهد له على سبقه وجودته, tr:eş-şâhidu min caryihî mâ yeşhedu lehû alâ sebkıhî ve cevdetih, gloss:koşusunun "tanığı", öne geçtiğine ve iyi cins olduğuna tanıklık eden kısımdır, source:"ش ه د,B008"}. Sekizinci ayetteki {ar:لَشَدِيدٌ, tr:le-şedîd, gloss:pek düşkündür, source:100:8} kelimesinin kökü de koşunun adıdır: {ar:الشد العدو والفعل اشتد, tr:eş-şeddu'l-advu ve'l-fi'lu iştedde, gloss:"şedd" koşudur, fiili "iştedde"dir, source:"ش د د,B003"}. Bu söyleyiş "şedd"i birinci ayetin "adv"ıyla aynı tanımda birleştirir. Onuncu ayetin {ar:ٱلصُّدُورِ, tr:es-sudûr, gloss:göğüsler, source:100:10} kelimesinin kökünde de yarışı göğsüyle kazanan at vardır: {ar:صدر الفرس إذا جاء قد سبق بصدره, tr:sadera'l-ferasu izâ câe kad sebeka bi-sadrih, gloss:at göğsüyle öne geçerek gelince "sadera" denir, source:"ص د ر,B002"}.

Bu görüntü sureye bir karşılaştırma katar. At soluğunu, bacaklarını, inceltilmiş bedenini ve bütün koşusunu sahibinin işine verir. Koşusu öne geçtiğine tanıklık eder, yarışı göğsüyle kazanır. Hemen ardından insan gelir ve onun hakkında söylenen ilk şey, Rabbine karşı {ar:لَكَنُودٌ, tr:le-kenûd, gloss:pek nankördür, source:100:6} olmasıdır. Atın tanığı kendi lehinedir, insanın tanıklığı ise kendi nankörlüğü üzerinedir. Atın "şedd"i koşusudur, insanınki ise malı sevmesidir. Göğüs at için yarışın kazanıldığı yerdir, insan için ise içindekilerin ayıklanacağı yerdir.

Kur'an atları, sevilen malı ve Rab sözünü başka bir sahnede de bir araya getirir. Akşamüstü Süleyman'a soylu, çevik atlar sunulur: {ar:إِذْ عُرِضَ عَلَيْهِ بِٱلْعَشِىِّ ٱلصَّٰفِنَٰتُ ٱلْجِيَادُ, tr:iz uride aleyhi bi'l-aşiyyi's-sâfinâtu'l-ciyâd, gloss:akşamüstü ona durup bekleyen soylu atlar sunulduğunda, source:38:31}. Süleyman şöyle der: {ar:إِنِّىٓ أَحْبَبْتُ حُبَّ ٱلْخَيْرِ عَن ذِكْرِ رَبِّى, tr:innî ahbebtu hubbe'l-hayri an zikri rabbî, gloss:ben "hayır" sevgisini Rabbimin anılmasına bağlı olarak sevdim, source:38:32}. Arapçada "an" edatı hem "-den ötürü" hem "-den uzaklaşarak" anlamını taşıyabildiği için bu cümle iki yöne açıktır. Ama sözün devamı sabittir: {ar:حَتَّىٰ تَوَارَتْ بِٱلْحِجَابِ, tr:hattâ tevârat bi'l-hicâb, gloss:ta ki perdenin ardına gizleninceye dek, source:38:32}. Ardından {ar:رُدُّوهَا عَلَىَّ ۖ فَطَفِقَ مَسْحًا بِٱلسُّوقِ وَٱلْأَعْنَاقِ, tr:ruddûhâ aleyye, fe-tafika meshan bi's-sûkı ve'l-a'nâk, gloss:"Onları bana geri getirin" dedi ve bacaklarını, boyunlarını meshetmeye koyuldu, source:38:33}. Sekizinci ayetin "hubbu'l-hayr" ifadesi burada bir peygamberin ağzında, atlarla ve "Rabbim" sözüyle birlikte geçer. Bizim surede aynı ifade atların koşusundan hemen sonra, Rabbine nankör olan insanın bağlılığını adlandırır. Kur'an, insanlara süslü gösterilen sevgilerin listesine atları da koyar: {ar:زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ, tr:zuyyine li'n-nâsi hubbu'ş-şehevât, gloss:arzulanan şeylerin sevgisi insanlara süslü gösterildi, source:3:14}. O listede altın ve gümüş yığınlarının yanında {ar:وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ, tr:ve'l-hayli'l-musevveme, gloss:salma, damgalı atlar, source:3:14} de sayılır. Böylece at hem koşan bir hayvan hem de sevilen bir maldır. Surenin karşılaştırması bu iki yüzün arasında kurulur.

Kaynaklar: 100:1 ٱلْعَٰدِيَٰتِ ع د و B002; 100:1 ضَبْحًا ض ب ح B001; 100:1 ضَبْحًا ض ب ح B002; 100:2 قَدْحًا ق د ح B008; 100:5 جَمْعًا ج م ع B010; 100:6 ٱلْإِنسَٰنَ ء ن س B004; 100:7 لَشَهِيدٌ ش ه د B008; 100:8 لَشَدِيدٌ ش د د B003; 100:10 ٱلصُّدُورِ ص د ر B002; 37:1; 37:2; 77:1; 77:2; 38:31; 38:32; 38:33; 3:14

## Şafak baskını

Koşan atların yaptığı iş üçüncü ayette adını alır: {ar:فَٱلْمُغِيرَٰتِ صُبْحًا, tr:fe'l-muğîrâti subhâ, gloss:derken sabahleyin baskın yapanlara, source:100:3}. Kelime baskın fiilinden gelir: {ar:أغار على القوم, tr:eğâra ale'l-kavm, gloss:kavmin üzerine baskın yaptı, source:"memory"}. Birinci ayetin kelimesi zaten bu işle tanımlanır: {ar:العادية الخيل المغيرة, tr:el-âdiyetu'l-haylu'l-muğîra, gloss:"âdiye", baskın yapan atlardır, source:"ع د و,B001"}. Yani koşan at, tanımı gereği baskına koşan attır. Aynı kökte saldırının ahlaki adı da vardır: {ar:العدوان الظلم الصراح, tr:el-udvânu'z-zulmu's-surâh, gloss:"udvân" apaçık haksızlıktır, source:"ع د و,B001"}. Saldırının hedefi de bu köktendir: {ar:العَدُوّ ضد الولي والجمع الأعداء, tr:el-aduvvu ziddu'l-veliyyi ve'l-cem'u'l-a'dâ', gloss:düşman, dostun karşıtıdır; çoğulu "a'dâ"dır, source:"ع د و,B003"}.

Baskının işleyişi saatine bağlıdır. Baskıncılar geceyi yolda geçirir ve ilk ışıkta konağa varır. O saatte konaklayanlar ya uykudadır ya da yeni uyanmaktadır, silahlanacak vakitleri yoktur. Bu yüzden sabah, baskının kendi adı olmuştur: {ar:يوم الصباح يوم الغارة, tr:yevmu's-sabâhi yevmu'l-ğâra, gloss:"sabah günü", baskın günüdür, source:"ص ب ح,B004"}. Aynı kökten fiil ile baskına uğrayanların çığlığı da tek bir söyleyişte birleşir: {ar:في الحرب صبحناهم أي غاديناهم بالخيل ونادوا يا صباحاه إذا استغاثوا, tr:fi'l-harbi sabbahnâhum, ey ğâdeynâhum bi'l-hayl, ve nâdev yâ sabâhâh izâ isteğâsû, gloss:savaşta "onlara sabahladık" yani atlarla sabah erkenden üstlerine vardık denir; yardım isteyenler de "Vay sabah!" diye bağırır, source:"ص ب ح,B004"}. Kelimenin sade kullanımı da aynı yöndedir: {ar:صبحته إذا أتيته صباحا, tr:sabahtuhû izâ eteytuhû sabâhan, gloss:birine sabahleyin vardığında "onu sabahladım" denir, source:"ص ب ح,B002"}.

Dördüncü ayet baskının görüntüsünü verir: {ar:فَأَثَرْنَ بِهِۦ نَقْعًا, tr:fe-eserne bihî nak'â, gloss:derken orada toz kaldırdılar, source:100:4}. Fiil havalanan toza gider: {ar:ثار الغبار يثور ثورا وثورانا أي سطع, tr:sâra'l-ğubâru yesûru sevren ve sevarânen, ey sata'a, gloss:toz kalktı, yani yükselip yayıldı, source:"ث و ر,B001"}. Fiilin kökü birinin üstüne çullanmayı da adlandırır: {ar:ثار به الناس أي وثبوا عليه, tr:sâra bihi'n-nâsu, ey vesebû aleyh, gloss:insanlar onun üstüne atıldı, source:"ث و ر,B003"}. "Nak'", yükselen tozdur: {ar:النقع الغبار المرتفع, tr:en-nak'u'l-ğubâru'l-murtefi', gloss:"nak'" yükselen tozdur, source:"ن ق ع,B004"}. Aynı kelimenin yanında bir ses de duyulur: {ar:النقع رفع الصوت, tr:en-nak'u ref'u's-savt, gloss:"nak'" sesi yükseltmektir, source:"ن ق ع,B005"}. Bu ses kesintisiz sürer: {ar:نقع بصوته وأنقع صوته إذا تابعه, tr:neka'a bi-savtihî ve enka'a savtehû izâ tâbe'ah, gloss:sesini ardı ardına sürdürdüğünde "neka'a" denir, source:"ن ق ع,B005"}. Yükselen toz bulutunun yanında, baskına uğrayan konağın "Vay sabah!" çığlığı duyulur. Ayetteki "bihî" zamiri tozu az önce anılan o sabaha ve o hamleye bağlar. Toz, baskının anında ve yerinde kalkar.

Beşinci ayet hamlenin nerede bittiğini söyler: {ar:فَوَسَطْنَ بِهِۦ جَمْعًا, tr:fe-vasatne bihî cem'â, gloss:derken orada bir topluluğun ortasına daldılar, source:100:5}. Fiil, bir kalabalığın içine girip ortasında durmaktır: {ar:وسط فلان جماعة من الناس وهو يسطهم إذا صار في وسطهم, tr:vasata fulânun cemâ'aten mine'n-nâs, ve huve yesıtuhum, izâ sâra fî vasatihim, gloss:biri bir topluluğun ortasına vardığında "onları ortaladı" denir, source:"و س ط,B003"}. "Cem'" bir araya gelmiş insan topluluğudur: {ar:الجمع اسم لجماعة الناس, tr:el-cem'u ismun li-cemâ'ati'n-nâs, gloss:"cem'" insan topluluğunun adıdır, source:"ج م ع,B002"}. Bu topluluk çoğu zaman karışıktır: {ar:الجماع ما تجمع من أشابة الناس وأخلاطهم, tr:el-cimâ'u mâ tecemma'a min uşâbeti'n-nâsi ve ahlâtihim, gloss:"cimâ'", karışık, derme çatma bir halk kalabalığıdır, source:"ج م ع,B002"}. Hamle kalabalığın kenarında durmaz, toplanmış bir halkın tam merkezinde biter. Bu, kaçacak yerin kalmadığı anı gösterir. Sekizinci ayetin kelimesi bu sahneye yeniden döner: {ar:شد على العدو إذا حمل عليه, tr:şedde ale'l-aduvvi izâ hamele aleyh, gloss:düşmana saldırdığında "şedde" denir, source:"ش د د,B003"}. Baskının ardından gelen paylaşım da dördüncü ayetin kelimesinde durur: {ar:النقيعة ما نحر من النهب قبل القسم, tr:en-nakî'atu mâ nuhira mine'n-nehbi kable'l-kasm, gloss:"nakî'a", ganimet bölüşülmeden önce boğazlanan hayvandır, source:"ن ق ع,B003"}.

Düz bir anlatım, atların hızla koşup baskın yaptığını söylemekle yetinirdi. Kelimeler ise başka şeyleri de duyurur. Saldırının tanımında "apaçık haksızlık" vardır, baskının adı bir saattir, toz ve çığlık aynı kelimededir ve hamle kalabalığın ortasında biter. Bu ani, kaçışsız sabah surenin sonundaki güne bir ön hazırlıktır. Kur'an azabın gelişini de bir şafak baskını gibi anlatır. Azabı acele isteyenlere Allah önce {ar:أَفَبِعَذَابِنَا يَسْتَعْجِلُونَ, tr:e-fe-bi-azâbinâ yesta'cilûn, gloss:azabımızı mı acele istiyorlar, source:37:176} diye sorar, sonra şöyle der: {ar:فَإِذَا نَزَلَ بِسَاحَتِهِمْ فَسَآءَ صَبَاحُ ٱلْمُنذَرِينَ, tr:fe-izâ nezele bi-sâhatihim fe-sâe sabâhu'l-munzerîn, gloss:o, avlularına indiğinde, uyarılmışların sabahı ne kötüdür, source:37:177}. Azap yurdun avlusuna iner ve bunun vakti "sabah"tır. Lut'a gelen elçiler ona ailesiyle geceleyin yola çıkmasını söyler ve {ar:إِنَّ مَوْعِدَهُمُ ٱلصُّبْحُ ۚ أَلَيْسَ ٱلصُّبْحُ بِقَرِيبٍ, tr:inne mev'idehumu's-subh, e-leyse's-subhu bi-karîb, gloss:onların buluşma vakti sabahtır; sabah yakın değil mi, source:11:81} diye ekler. Hicr halkı için {ar:فَأَخَذَتْهُمُ ٱلصَّيْحَةُ مُصْبِحِينَ, tr:fe-ehazethumu's-sayhatu musbihîn, gloss:sabaha girerlerken onları o çığlık yakaladı, source:15:83} denir. Lut kavmi için aynı fiil kullanılır: {ar:وَلَقَدْ صَبَّحَهُم بُكْرَةً عَذَابٌ مُّسْتَقِرٌّ, tr:ve le-kad sabbahahum bukraten azâbun mustakır, gloss:andolsun, erkenden kalıcı bir azap onlara sabahladı, source:54:38}. Kur'an atlı akın görüntüsünü İblis'e verilen izinde de kullanır: {ar:وَأَجْلِبْ عَلَيْهِم بِخَيْلِكَ وَرَجِلِكَ, tr:ve eclib aleyhim bi-haylike ve recilik, gloss:atlılarınla ve yayalarınla üzerlerine yaygarayla yürü, source:17:64}. Müminlere verilen buyrukta ise atlar ile "düşman" kelimesi aynı ayette durur: {ar:وَمِن رِّبَاطِ ٱلْخَيْلِ تُرْهِبُونَ بِهِۦ عَدُوَّ ٱللَّهِ وَعَدُوَّكُمْ, tr:ve min ribâti'l-hayli turhibûne bihî aduvva'llâhi ve aduvvekum, gloss:bağlanıp hazır tutulan atlardan; onlarla Allah'ın düşmanını ve sizin düşmanınızı caydırırsınız, source:8:60}.

Kaynaklar: 100:1 ٱلْعَٰدِيَٰتِ ع د و B001; 100:1 ٱلْعَٰدِيَٰتِ ع د و B003; 100:3 فَٱلْمُغِيرَٰتِ غ و ر (memory); 100:3 صُبْحًا ص ب ح B004; 100:3 صُبْحًا ص ب ح B002; 100:4 فَأَثَرْنَ ث و ر B001; 100:4 فَأَثَرْنَ ث و ر B003; 100:4 نَقْعًا ن ق ع B004; 100:4 نَقْعًا ن ق ع B005; 100:4 نَقْعًا ن ق ع B003; 100:5 فَوَسَطْنَ و س ط B003; 100:5 جَمْعًا ج م ع B002; 100:8 لَشَدِيدٌ ش د د B003; 37:176; 37:177; 11:81; 15:83; 54:38; 17:64; 8:60

## Taştan ateş çakmak

İkinci ayet bir ateş yakma işlemini anlatır: {ar:فَٱلْمُورِيَٰتِ قَدْحًا, tr:fe'l-mûriyâti kadhâ, gloss:derken çakarak ateş çıkaranlara, source:100:2}. Ateş şöyle çakılır: bir demir parçası taşa sertçe vurulur, kopan kıvılcım tutuşmaya hazır bir maddeye düşer ve ateş doğar. İki kelime bu işlemin iki aletini tek bir tanımda birleştirir: {ar:المقدحة ما تقدح به النار والقداحة والقداح الحجر الذي يوري النار, tr:el-mikdahatu mâ tukdahu bihi'n-nâr, ve'l-kaddâhatu ve'l-kaddâhu'l-haceru'llezî yûri'n-nâr, gloss:"mikdaha" ateşin onunla çakıldığı alettir; "kaddâha" ve "kaddâh" ateş çıkaran taştır, source:"ق د ح,B001"}. Ayetin ilk kelimesinin kökü de ateşin dışarı çıkmasını anlatır: {ar:ورى الزند خرجت ناره, tr:verâ'z-zend, harecet nâruh, gloss:çakmak tutuştu, yani ateşi çıktı, source:"و ر ي,B002"}. Aynı kök sönmeye yüz tutmuş ateşi canlandırmayı da kapsar: {ar:أوريت النار إذا كانت خامدة فأججتها, tr:evraytu'n-nâra izâ kânet hâmideten fe-eccectehâ, gloss:sönük duran ateşi alevlendirdiğinde "evraytu" dersin, source:"و ر ي,B002"}. Surede bu aletler, koşan hayvanların taşlara çarpan ayaklarıdır. Hız taşla karşılaşınca kıvılcım çıkar.

Birinci ayetin kelimesi, anlamının yanında bu ateşin izlerini de taşır. Çakmak taşları "dabh" ile nitelenir: {ar:حجارة القداحة مضبوحة, tr:hicâratu'l-kaddâhati madbûha, gloss:çakmak taşları "madbûh"tur, yani yanıktır, source:"ض ب ح,B003"}. Kelime ateşle dağlanmayı da anlatır: {ar:الضبح إحراق أعالي العود بالنار, tr:ed-dabhu ihrâku a'âli'l-ûdi bi'n-nâr, gloss:"dabh", çubuğun ucunu ateşle yakmaktır, source:"ض ب ح,B003"}. Yanan şeyin rengi değişir: {ar:ضبحته الشمس وضبته إذا غيرت لونه وكذلك النار, tr:dabahathu'ş-şemsu ve dabbethu izâ ğayyerat levneh, ve kezâlike'n-nâr, gloss:güneş ya da ateş bir şeyin rengini değiştirince "onu dabh etti" denir, source:"ض ب ح,B004"}. Geriye kalan şey de aynı kelimeyle adlandırılır: {ar:الضبح الرماد, tr:ed-dabhu'r-ramâd, gloss:"dabh" küldür, source:"ض ب ح,B005"}. Böylece birinci ayetin soluğu, ikinci ayetin ateşinin hem kızgınlığını hem de külünü yanında taşır.

Sekizinci ayetin {ar:لِحُبِّ, tr:li-hubbi, gloss:sevgisine, source:100:8} kelimesinin ailesinde, atların çaktığı ateşin özel bir adı vardır: {ar:نار الحباحب ما أورت الخيل لا ينتفع به, tr:nâru'l-hubâhibi mâ evrati'l-haylu lâ yuntefe'u bih, gloss:"hubâhib ateşi", atların çıkardığı, hiçbir işe yaramayan ateştir, source:"ح ب ب,B011"}. Bu ateş havada uçuşan kıvılcımlardan ibarettir: {ar:ما اقتدحت من شرار النار في الهواء من تصادم الحجارة, tr:mâ'ktedahte min şerâri'n-nâri fi'l-hevâi min tesâdumi'l-hicâra, gloss:taşların çarpışmasıyla havaya çaktığın kıvılcımlar, source:"ح ب ب,B011"}. Buna karşılık üçüncü ayetin kelimesinin ailesinde süren ışık durur: {ar:المصباح السراج وقد استصبحت به إذا أسرجت, tr:el-misbâhu's-sirâc, ve kad istasbahtu bihî izâ esracte, gloss:"misbâh" kandildir; onu yaktığında "istasbahtu" dersin, source:"ص ب ح,B005"}. Günün ışığı da bu kökle anılır: {ar:الصباح نور النهار, tr:es-sabâhu nûru'n-nehâr, gloss:sabah, gündüzün ışığıdır, source:"ص ب ح,B001"}. İkinci ayetin kıvılcımı karanlıkta bir an parlar, üçüncü ayetin sabahı ise karanlığın yerini kalıcı olarak alan ışıktır. Sekizinci ayetteki sevginin yanında duyulan ateş ise atların çaktığı ama hiçbir şey aydınlatmayan kıvılcımdır.

Ateş insana da döner. Altıncı ayetteki insan kelimesinin kökü uzaktan bir ateş görmeyi anlatır: {ar:آنس من جانب يعني أبصر نارا, tr:ânese min cânib, ya'nî ebsara nâran, gloss:bir yandan "ânese", yani bir ateş gördü, source:"ء ن س,B002"}. Ateş çakmak, bir işi düşünüp tartmanın da adıdır: {ar:الإنسان يقتدح الأمر إذا نظر فيه ودبر, tr:el-insânu yaktedihu'l-emra izâ nazara fîhi ve debbera, gloss:insan bir işi inceleyip tartınca "o işi çakar", source:"ق د ح,B010"}. Çakmağın tutuşması, girişilen işin başarılmasıdır: {ar:لواري الزناد إذا رام أمرا أنجح فيه وأدرك ما طلب, tr:le-vâri'z-zinâd izâ râme emran encaha fîhi ve edreke mâ taleb, gloss:çakmağı tutuşan biri, bir işe girişince başarır ve istediğine ulaşır, source:"و ر ي,B003"}. Ama aynı çakmak yanlış taşa da vurulabilir: {ar:فلان يستوري زناد الضلالة, tr:fulânun yestevrî zinâde'd-dalâle, gloss:falanca sapıklığın çakmağından ateş çıkarmaya çalışıyor, source:"و ر ي,B009"}. Böylece görüntü, ikinci ayetin kıvılcımlarından insanın kendi aklını nasıl kullandığı sorusuna geçer: bu kıvılcım tutuşan bir iş mi olacak, boşa uçuşan bir ateş mi?

Kur'an aynı fiili, dirilişi inkâr edenlere yönelttiği sorularda kullanır. Ölüp toprak olduktan sonra diriltilmeyi uzak görenlere Allah ekin, su ve ateş üzerine sorular sorar: {ar:أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ, tr:e-fe-raeytumu'n-nâra'lletî tûrûn, gloss:çakıp çıkardığınız ateşi gördünüz mü, source:56:71}, {ar:ءَأَنتُمْ أَنشَأْتُمْ شَجَرَتَهَآ أَمْ نَحْنُ ٱلْمُنشِـُٔونَ, tr:e-entum enşe'tum şeceratehâ em nahnu'l-munşi'ûn, gloss:onun ağacını siz mi yarattınız, yoksa yaratan biz miyiz, source:56:72}. Cevap da ateşin ne olduğunu söyler: {ar:نَحْنُ جَعَلْنَٰهَا تَذْكِرَةً وَمَتَٰعًا لِّلْمُقْوِينَ, tr:nahnu ce'alnâhâ tezkireten ve metâ'an li'l-mukvîn, gloss:onu bir hatırlatma ve çölde konaklayanlar için bir geçim aracı yaptık, source:56:73}. Buradaki "tûrûn", ikinci ayetin "mûriyât"ıyla aynı kökten, aynı fiildir. Başka bir yerde de çürümüş kemikleri kimin dirilteceğini soran adama {ar:مَن يُحْىِ ٱلْعِظَٰمَ وَهِىَ رَمِيمٌ, tr:men yuhyi'l-izâme ve hiye ramîm, gloss:çürümüşken kemikleri kim diriltecek, source:36:78} ateşle cevap verilir: {ar:ٱلَّذِى جَعَلَ لَكُم مِّنَ ٱلشَّجَرِ ٱلْأَخْضَرِ نَارًا فَإِذَآ أَنتُم مِّنْهُ تُوقِدُونَ, tr:ellezî ce'ale lekum mine'ş-şeceri'l-ahdari nâran fe-izâ entum minhu tûkıdûn, gloss:size yeşil ağaçtan ateş çıkaran; siz de ondan yakıp duruyorsunuz, source:36:80}. İnsan kökünün "uzaktan ateş görmek" anlamı Musa'nın sahnesinde bütünüyle yaşanır. Ailesiyle yolculuk ederken Tur'un yanında bir ateş görür ve şöyle der: {ar:إِنِّىٓ ءَانَسْتُ نَارًا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِخَبَرٍ, tr:innî ânestu nâran le'allî âtîkum minhâ bi-haber, gloss:ben bir ateş gördüm; belki oradan size bir haber getiririm, source:28:29}. Bir başka anlatımda {ar:سَـَٔاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ ءَاتِيكُم بِشِهَابٍ قَبَسٍ, tr:se-âtîkum minhâ bi-haberin ev âtîkum bi-şihâbin kabes, gloss:oradan size bir haber ya da yanan bir kor getireceğim, source:27:7} der. Bir başkasında ise {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًى, tr:ev ecidu ale'n-nâri hudâ, gloss:ya da ateşin başında bir yol gösterici bulurum, source:20:10} der. Musa'nın sahnesinde uzaktan görülen ateş haber (haber, "h-b-r") ve yol göstericilikle sonuçlanır. Bu, surenin son kelimesi {ar:لَّخَبِيرٌ, tr:le-habîr, gloss:her şeyden haberdardır, source:100:11} ile aynı köktür.

Kaynaklar: 100:2 فَٱلْمُورِيَٰتِ و ر ي B002; 100:2 قَدْحًا ق د ح B001; 100:1 ضَبْحًا ض ب ح B003; 100:1 ضَبْحًا ض ب ح B004; 100:1 ضَبْحًا ض ب ح B005; 100:8 لِحُبِّ ح ب ب B011; 100:3 صُبْحًا ص ب ح B005; 100:3 صُبْحًا ص ب ح B001; 100:6 ٱلْإِنسَٰنَ ء ن س B002; 100:2 قَدْحًا ق د ح B010; 100:2 فَٱلْمُورِيَٰتِ و ر ي B003; 100:2 فَٱلْمُورِيَٰتِ و ر ي B009; 56:71; 56:72; 56:73; 36:78; 36:80; 28:29; 27:7; 20:10

## Buluşmalar

İlk buluşma, surenin açılış sahnesinde koşan at ile şafak baskını arasındadır. Koşanların tanımı zaten baskın yapanlardır: {ar:العادية الخيل المغيرة, tr:el-âdiyetu'l-haylu'l-muğîra, gloss:"âdiye", baskın yapan atlardır, source:"ع د و,B001"}. Sekizinci ayetin "şedd" kelimesi de iki görüntüyü aynı anda taşır. Bir yanda koşudur, öbür yanda düşmana saldırıdır: {ar:شد على العدو إذا حمل عليه, tr:şedde ale'l-aduvvi izâ hamele aleyh, gloss:düşmana saldırdığında "şedde" denir, source:"ش د د,B003"}. Aynı sahnede ateş görüntüsü de yer alır. Soluk soluğa koşan hayvanların ayakları taşlara çarparak kıvılcım çıkarır. Birinci ayetin kelimesi bir yandan bu soluğu, bir yandan da yanmış çakmak taşını adlandırır. Koşu, kıvılcım ve sabah tek bir hareketin ardışık parçalarıdır.

Surenin iki yarısını birbirine bağlayan asıl buluşma, dördüncü ayetin tozu ile dokuzuncu ayetin kabirleri arasındadır. Toynakların toprağı kaldırması ile kabirlerin altüst edilmesi aynı fiille açıklanır: "bu'sira", "usîra" demektir. Böylece surenin ilk yarısındaki sabah baskını, ikinci yarısındaki altüst oluşun bir ön provası olur. Kur'an da kabirlerden çıkışı bir koşu olarak anlatır: {ar:يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًا كَأَنَّهُمْ إِلَىٰ نُصُبٍ يُوفِضُونَ, tr:yevme yahrucûne mine'l-ecdâsi sirâ'an ke-ennehum ilâ nusubin yûfidûn, gloss:kabirlerden hızla çıkacakları, sanki dikili bir hedefe koşuyorlarmış gibi seğirtecekleri gün, source:70:43}. Bir başka yerde de {ar:يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًا, tr:yevme teşakkaku'l-ardu anhum sirâ'â, gloss:yerin yarılıp onların hızla çıktığı gün, source:50:44} denir. Surenin başında koşanlar atlardır. Sonunda ise koşanlar kabirlerden çıkan insanlardır. Bu insanların gittiği yer de beşinci ayetteki gibi bir topluluğun ortasıdır, ama bu kez bütün insanların toplandığı yerdir.

Ateş ile kabir de aynı kökte buluşur. İkinci ayetin "ateşi çıkarmak" fiili ile gömmenin "örtmek" fiili aynı köktendir. Kur'an ateşi dirilişe delil olarak da kullanır. Çakılan ateşe dair soru dirilişi inkâr edenlere sorulur. Yeşil ağaçtan çıkan ateş de çürümüş kemikleri kimin dirilteceğini soran kişiye verilen cevaptır. Tahtanın içinde gizli duran ateş çakılınca dışarı çıkar, toprağın içinde gizli duran insan da altüst edilince dışarı çıkar. Yağmur sahnesi de aynı yere varır. İyi toprak ile kıt ürün veren toprağı karşılaştıran ayetten hemen önce şöyle denir: {ar:كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:kezâlike nuhrici'l-mevtâ le'allekum tezekkerûn, gloss:ölüleri de böyle çıkarırız; belki düşünüp öğüt alırsınız, source:7:57}. Kenûd toprak bitki bitirmez. Ama sonunda kabirleri altüst edilecek olan da aynı topraktır.

Biriktirilen mal ile göğsün ayıklanması da bir sahnede buluşur. Onuncu ayetin fiilinin aslı, altını maden toprağından ayırmaktır. Biriktirenin malı ise toplanmış altın ve gümüştür. Kur'an bu iki şeyi ateşte birleştirir: {ar:وَٱلَّذِينَ يَكْنِزُونَ ٱلذَّهَبَ وَٱلْفِضَّةَ وَلَا يُنفِقُونَهَا فِى سَبِيلِ ٱللَّهِ, tr:ve'llezîne yeknizûne'z-zehebe ve'l-fiddate ve lâ yunfikûnehâ fî sebîli'llâh, gloss:altın ve gümüşü yığıp Allah yolunda harcamayanlar, source:9:34}; {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhuhum ve cunûbuhum ve zuhûruhum, gloss:o gün bunlar cehennem ateşinde kızdırılır ve alınları, yanları ve sırtları onlarla dağlanır, source:9:35}. Malın bağlılığı ile göğsün içindekinin çıkarılması da tek bir ayette bir aradadır: {ar:إِن يَسْـَٔلْكُمُوهَا فَيُحْفِكُمْ تَبْخَلُوا۟ وَيُخْرِجْ أَضْغَٰنَكُمْ, tr:in yes'elkumûhâ fe-yuhfikum tebhalû ve yuhric adğânekum, gloss:onları (mallarınızı) sizden isteyip ısrar etseydi cimrilik ederdiniz ve O da kinlerinizi dışarı çıkarırdı, source:47:37}. Sevgi kelimesinin "kalbin tanesi" anlamı da bu buluşmayı kelimenin içinden kurar. İnsanın şiddetle bağlandığı mal göğsün içindeki tanedir, harman savrulduğunda ayrılacak olan da odur. Beşinci ayetin kökü de aynı sahnede iki yönde işler. Mal toplayan, yumruğunu sıkan kişi sonunda toplanma gününde toplananlardan biri olur. Onuncu ayetin fiili de bir toplamadır.

Sabah baskını ile malı esirgeme de bir Kur'an sahnesinde birleşir. Bir bahçenin sahipleri ürünü sabahleyin devşireceklerine yemin ederler: {ar:إِذْ أَقْسَمُوا۟ لَيَصْرِمُنَّهَا مُصْبِحِينَ, tr:iz aksemû le-yasrimunnehâ musbihîn, gloss:onu sabaha girerken mutlaka devşireceklerine yemin ettiklerinde, source:68:17}. Onlar uyurken {ar:فَطَافَ عَلَيْهَا طَآئِفٌ مِّن رَّبِّكَ وَهُمْ نَآئِمُونَ, tr:fe-tâfe aleyhâ tâifun min rabbike ve hum nâimûn, gloss:onlar uykudayken Rabbinden bir bela bahçeyi sardı, source:68:19}. Bahçe {ar:فَأَصْبَحَتْ كَٱلصَّرِيمِ, tr:fe-asbahat ke's-sarîm, gloss:sabaha kapkara kesilmiş halde girdi, source:68:20}. Habersiz sahipler ise {ar:فَتَنَادَوْا۟ مُصْبِحِينَ, tr:fe-tenâdev musbihîn, gloss:sabaha girerken birbirlerine seslendiler, source:68:21}. Konuştukları şey şudur: {ar:أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌ, tr:en lâ yedhulennehe'l-yevme aleykum miskîn, gloss:bugün oraya hiçbir yoksul yanınıza girmesin, source:68:24}. Bu sahnede bir sabah seferi, yoksula kapanan bir el ve Rabbin cevabı vardır. Sabah baskını yapan, sonunda baskına uğrayan olur. Bizim surede de "yalnız yiyen" kenûd, "sabah" sözüyle başlayan bir surenin sonunda Rabbinin bilgisi karşısında durur.

Su başı ile toprağın altüst edilmesi aynı günün anlatımında buluşur. Yerin sarsıldığı ve ağırlıklarını dışarı attığı gün, insanların {ar:يَصْدُرُ, tr:yasduru, gloss:sudan döner gibi döner, source:99:6} günüdür. Fiil onuncu ayetin göğüs kelimesiyle aynı köktendir. Kabirden çıkış, gömülü olanın açılması ve sudan dönüş tek bir anda birleşir. İnsanlar amellerini görmek için bölük bölük döner.

Tanıklık ile Rab sözü ise yedinci ayetin iki okumasını bir araya getirir. Âdem oğullarının "Rabbiniz değil miyim" sorusuna "evet, tanık olduk" diye cevap verdiği sahnede, insan kendi Rabbine dair kendisi üzerine tanıktır. Bizim surede de aynı insan, Rabbine karşı nankörlüğü üzerine tanıktır. Birinci ayetin atının tanığı ise koşusudur ve onun öne geçtiğine tanıklık eder. Aynı kelime atta lehte, insanda aleyhte işler.

Bu buluşmalar surenin hareketini dışarıdan içeriye doğru taşır. Sure, gözle görülen ve kulakla işitilen şeylerle başlar: soluk, kıvılcım, sabah ışığı, toz ve kalabalık. Sonra göze görünmeyen bir yere, göğüsteki taneye ulaşır. Toynakların kaldırdığı toprak kabirlerin toprağına, baskının sabahı toplanma gününe, yağmurun beklendiği tarla kabirlerini açan yere dönüşür. Malın düğümü ve yumulmuş el de toplanıp ayıklanan bir göğse dönüşür. Bu yolun her aşamasında bilgi de derinleşir: önce hazır bulunan ve gören bir tanık vardır, sonra sorulan ama cevaplanmayan bir bilgi, en sonda da içini bilen bir Rab.

