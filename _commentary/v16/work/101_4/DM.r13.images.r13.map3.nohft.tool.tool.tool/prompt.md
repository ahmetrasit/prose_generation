Focus: 101:4. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/101_4/D.r13/context.md =====
# 101:4 — focus

يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ

Anchor translation (canonical reading, reference only):

İnsanların etrafa saçılmış pervaneler gibi olacağı gün.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | يَوْمَ | يَوْم | ي و م | T |
| 2 | يَكُونُ | كَانَ | ك و ن | V |
| 3 | ٱلنَّاسُ | نَّاس | ن و س | DET;N |
| 4 | كَٱلْفَرَاشِ | فَرَاش | ف ر ش | P;DET;N |
| 5 | ٱلْمَبْثُوثِ | مَبْثُوث | ب ث ث | DET;ADJ |


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
- 101:4 ◀ focus يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ
- 101:5 وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ ٱلْمَنفُوشِ
- 101:6 فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ
- 101:7 فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ
- 101:8 وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ
- 101:9 فَأُمُّهُۥ هَاوِيَةٌۭ
- 101:10 وَمَآ أَدْرَىٰكَ مَا هِيَهْ
- 101:11 نَارٌ حَامِيَةٌۢ


===== _commentary/v16/work/101_4/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ي و م (root_001700) — identity root of يَوْمَ (w1)

- **B001** güneşin doğuşundan batışına kadarki gün — güneşin doğuşundan batışına kadarki gün · bu anlamdaki günlerin çoğulu · gün gün veya gündelik esasa göre yapılan işlem
  اليوم: الواحد من الأيام (maqayis)؛ اليوم مقداره من طلوع الشمس إلى غروبها (ayn;tahdhib)؛ اليوم معروف والجمع أيام (sihah)؛ اليوم يعبر به عن وقت طلوع الشمس إلى غروبها (mufradat)
- **B002** herhangi bir zaman dilimi; bağlama göre devir — herhangi bir zaman dilimi; bağlama göre devir · iki devri veya bollukla sıkıntı, cömertlikle savaş gibi iki karşıt hali
  مدة من الزمان أي مدة كانت (mufradat)؛ اليوم ها هنا بمعنى الدهر (tahdhib)؛ شر أيام دهرها (tahdhib)
- **B003** büyük olayın yaşandığı çetin gün veya olay — büyük olay, olayın gerçekleştiği kritik gün veya çetin gün · çok çetin gün veya savaş günü · bilinen günlerde gerçekleşmiş olaylar · çok çetin gün · kötülüğü insanlar üzerinde uzun süren çetin gün · kötülüğü insanlar üzerinde uzun süren çetin gün
  يستعيرونه في الأمر العظيم ويقولون نعم فلان في اليوم إذا نزل (maqayis)؛ اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت (ayn;tahdhib)؛ الشدة باليوم (sihah)؛ اليوم الشديد: يوم ذو أيام (ayn;tahdhib)؛ الأيام في معنى الوقائع (tahdhib)
- **B004** Tanrı'nın nimet ve ibret verici işleriyle anılan günler [kalıp] — Tanrı'nın nimet, bağışlama ve cezalandırma olaylarıyla anılan günleri
  وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب، وبالعفو عن آخرين (tahdhib)؛ جاءت الأيام بمعنى الوقائع والنعم (tahdhib)؛ أيامه: نعمه (tahdhib)؛ إضافة الأيام إلى الله تشريف لأمرها لما أفاض الله عليهم من نعمه فيها (mufradat)
- **B005** bağlamda işaret edilen o gün veya o sırada — o gün; o sırada
  يركب يوم مع إذ، فيقال: يومئذ؛ وربما يعرب ويبنى، وإذا بني فللإضافة إلى إذ (mufradat)

## ك و ن (root_001332) — identity root of يَكُونُ (w2)

- **B001** gerçekleşme, bulunma ve olma bildirimi — gerçekleşip ortaya çıkmak veya hazır bulunmak · geçmişte bir durumu bildirmek · oluş; gerçekleşme · olma, oluş · sonradan gerçekleşen iş · yüklemi pekiştiren ek söz · birini geliş kapsamı dışında tutan bağlı söz · var edip gerçekleşmesini sağlamak
  الكون الحدث يكون بين الناس ومصدر من كان يكون؛ الكينونة في مصدر كان؛ الكائنة الأمر الحادث (ayn); كان عبارة عما مضى من الزمان؛ حدوث الشيء ووقوعه؛ كان الأمر أي مذ خلق؛ تقع زائدة للتوكيد؛ لا يكون زيدا تعني الاستثناء؛ كونه فتكون أحدثه فحدث (sihah); أصل يدل على الإخبار عن حدوث شيء إما في زمان ماض أو زمان راهن؛ كان الشيء يكون كونا إذا وقع وحضر (maqayis)
- **B002** bulunma yeri ve konum değeri — bulunulan yer · yerler · konum, düzey veya bulunulan yer · birinin yanında güçlü konumu olan · yerleşmek veya güç kazanmak · birinin yanında şu yer veya düzeyde bulunmak
  المكان اشتقاقه من كان يكون؛ تمكن (ayn;maqayis); فلان مني مكان هذا؛ موضع العمامة (ayn); المكانة المنزلة؛ مكين عند فلان بين المكانة؛ المكان والمكانة الموضع؛ تمكن (sihah)
- **B003** birini güvenceyle üstlenme — başkası için güvence üstlenme · birini üstlenmek · birine güvence olmak
  الكيانة الكفالة؛ كنت على فلان أكون كونا أي تكفلت به؛ اكتنت به اكتيانا مثله (sihah); كنت على فلان أكون عليه إذا كفلت به؛ اكتنت أيضا اكتيانا (maqayis)
- **B004** boyun eğme — boyun eğme
  الاستكانة الخضوع (sihah)
- **B005** gençliğini anan yaşlı kişi — gençken şöyleydim diye anlatan yaşlı kişi
  يقال للرجل إذا شاخ كُنْتِيّ؛ كأنه نسب إلى قوله كُنْتُ في شبابي كذا وكذا (sihah)
- **B006** kötü durumda gece geçirme [kalıp] — geceyi kötü durumda geçirmek
  الكينة في قولهم بات فلان بكينة سوء أي بحال سوء فأصله الكون فعلة من الكون (maqayis)

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

## ف ر ش (root_001143) — identity root of كَٱلْفَرَاشِ (w4)

- **B001** yayıp düzleyerek hazırlama — sermek, yayıp düzlemek · işini ona bütünüyle açıp anlatmak · üzerinde yerleşmeye elverişli kılınmış yer · evin zeminini döşemek · geniş
  أصل صحيح يدل على تمهيد الشيء وبسطه؛ فرشت الفراش أفرشه (maqayis)؛ فرشت الفراش بسطته؛ فرشته أمري بسطته كله له (ayn)؛ فرشت الشيء بسطته؛ الفرش الفضاء الواسع؛ أكمة مفترشة الظهر إذا كانت دكاء (sihah)؛ فرشت زيدا بساطا؛ فرش فلان داره إذا بلطها؛ فرشته أمري أي بسطته كله (tahdhib)؛ الفرش بسط الثياب؛ جعل لكم الأرض فراشا أي ذللها (mufradat)؛ الفرشاط الواسع مما زيدت فيه الطاء والأصل فرش (maqayis_variant)
- **B002** serili yatak ve döşek — serili ev eşyası, döşek · oturmak için serilen örtü · ev veya kuş yuvası
  الفرش المفروش أيضا (maqayis)؛ المفرش شيء يكون مثل شاذكونه؛ المفرشة على الرحل (ayn)؛ الفراش واحد الفرش؛ الفرش المفروش من متاع البيت (sihah)؛ الفراش ما ينامان عليه؛ الفراش البيت؛ الفراش عش الطائر؛ المفرشة تكون على الرحل (tahdhib)؛ يقال للمفروش فرش وفراش؛ وفرش مرفوعة؛ فرش بطائنها من إستبرق (mufradat)
- **B003** evlilik bağı ve yatağı — eş veya evlilik birliğinin sahibi · çocuk evlilik birliğinin sahibine bağlanır · soylu kadınlarla evlenmiş · bir erkeğin birlikte olduğu cariye
  الولد للفراش؛ أراد به الزوج؛ الفراش في الحقيقة المرأة؛ كريم المفارش إذا تزوج كريم النساء (maqayis)؛ جارية فريش افترشها الرجل (ayn)؛ الفراش يكنى به عن المرأة؛ كريم المفارش إذا تزوج كرائم النساء؛ افترشه أي وطئه (sihah)؛ الفراش الزوج؛ الفراش المرأة؛ الولد للفراش معناه لمالك الفراش؛ جارية فريش قد افترشها الرجل؛ افترش كريمة بني فلان إذا تزوجها (tahdhib)؛ كني بالفراش عن كل واحد من الزوجين؛ الولد للفراش؛ كريم المفارش أي النساء (mufradat)
- **B004** küçük veya yük taşımayan evcil hayvan — küçük, yük taşımayan veya kesimlik evcil hayvanlar
  الفرش من الأنعام الذي لا يصلح إلا للذبح والأكل (maqayis)؛ الفرش من النعم التي لا تصلح إلا للذبح وهي ما دون الحمولة؛ ومن الأنعام حمولة وفرشا (ayn)؛ الفرش صغار الإبل؛ حمولة وفرشا؛ يحتمل أن يكون مصدرا من فرشها الله أي بثها بثا (sihah)؛ الفرش الصغار؛ أجمع أهل اللغة على أن الفرش صغار الإبل وأن الغنم والبقر من الفرش (tahdhib)؛ الفرش ما يفرش من الأنعام أي يركب؛ حمولة وفرشا (mufradat)
- **B005** ışık çevresinde çırpınan küçük güve — ışığa veya ateşe uçan küçük güve · pervane gibi hafif adam
  الفراش هذا الذي يطير وسمي بذلك لخفته؛ الفراشة الرجل الخفيف (maqayis)؛ الفراش التي تطير طالبة للضوء؛ يقال للخفيف من الرجال فراشة (ayn)؛ الفراشة التي تطير وتهافت في السراج؛ أطيش من فراشة (sihah)؛ الفراش ما تراه كصغار البق يتهافت في النار؛ الفراش الذي يطير؛ الخفيف من الرجال فراشة (tahdhib)؛ الفراش طير معروف؛ كالفراش المبثوث (mufradat)
- **B006** yere yakın kanat çırpma — yere yakın kanatlarını açıp çırpmak
  تفرش الطائر إذا قرب من الأرض ورفرف بجناحه؛ فجاءت الحمرة تفرش (maqayis)؛ تفرش الطائر رفرف بجناحيه وبسطهما (sihah)؛ فرش الطائر تفريشا إذا جعل يرفرف على الشيء وهي الشرشرة والرفرفة (tahdhib)
- **B007** bedeni veya uzuvları yere yayma — toprağı veya örtüyü altına serip üzerine yatmak · kollarını yere serip üzerlerine dayanmak · yere devirip altına almak veya üzerine basmak · yolda ilerlemek · bacakları birbirinden ayırmak
  افترش السبع ذراعيه (maqayis)؛ افترش فلان ترابا أو ثوبا تحته؛ افترش الذئب ذراعيه ربض عليهما (ayn)؛ افترش الشيء أي انبسط؛ افترش ذراعيه بسطهما على الأرض؛ افترشه أي وطئه (sihah)؛ افتراش السبع أن يبسط ذراعيه؛ لقي فلان فلانا فافترشه إذا صرعه؛ افترش القوم الطريق إذا سلكوه (tahdhib)؛ الفرشحة أن يفرج الإنسان بين رجليه ويباعد إحداهما من الأخرى وهي من فرش وفسح (maqayis_variant)
- **B008** yayılmış ekin ve ince küçük dallar — yere yayılan veya en az üç yapraklı ekin · ağaç ve yakacağın ince küçük parçaları
  الفرش دق الحطب (maqayis)؛ الفرش من الشجر والحطب الدق الصغار (ayn)؛ الفرش الزرع إذا فرش؛ المفرش الزرع إذا انبسط (sihah)؛ الفرش الزرع الذي بثلاث ورقات أو أكثر؛ الفرش من الشجر والحطب الدق والصغار (tahdhib)
- **B009** ince su kalıntısı, kurumuş iz veya kabarcık — su çekilince kuruyup kabuklanan çamur · kapta veya yerde kalan az su · içecek veya ter yüzeyindeki küçük kabarcıklar
  الفراشة الماء على وجه الأرض قبيل نضوبه؛ الفراشة من الأرض الذي نضب عنه الماء فيبس وتقشر (maqayis)؛ فراش القاع والطين ما يبس بعد نضوب الماء؛ ما بقي في الحوض إلا فراشة من ماء (ayn)؛ الفراش ما يبس بعد الماء من الطين على وجه الأرض؛ فراش النبيذ الحبب وكذلك حبب العرق (sihah)؛ فراش القاع والطين ما يبس بعد نضوب الماء؛ الفراش أقل من الضحضاح؛ فراش المسيح كالجمان المحبب (tahdhib)؛ الفراشة الماء القليل في الإناء (mufradat)
- **B010** ince kemik veya metal levha — kafatasının ince kemik tabakaları veya dil altındaki et · ince kemik veya demir levha · kilit ve gemdeki ince metal parçalar · omuz başlarındaki çıkıntılar ve kaş kemiği
  فراش الرأس طرائق دقاق تلي القحف؛ الفراشة فراشة القفل (maqayis)؛ فراش اللسان لحمه تحته؛ فراش الرأس طرائق من القحف (ayn)؛ الفراشة كل عظم رقيق؛ فراش الرأس عظام رقاق تلي القحف؛ فراشة القفل ما ينشب فيه (sihah)؛ فراش اللسان اللحمة التي تحتها؛ فراش الرأس طرائق رقاق من القحف؛ كل رقيق من عظم أو حديد فهو فراشة؛ الفراش عظم الحاجب؛ فراشا الكتفين؛ فراشا اللجام الحديدتان (tahdhib)؛ به شبه فراشة القفل (mufradat)
- **B011** ince kemik tabakasına ulaşan yara — ince kafatası kemiğine ulaşan veya kemiği çatlatan yara · kemiğin içine giren delici yara
  شجة مفترشة ومفرشة تبلغ فراش القحف؛ طعنة فارشة مفرشة أي داخلة في العظم (ayn)؛ المفرشة الشجة التي تصدع العظم ولا تهشم (sihah)؛ المنقلة التي يخرج منها فراش العظام؛ ضربة فأطار فراش رأسه؛ طعنة فارشة مفرشة (tahdhib)
- **B012** dili serbest bırakma ve sözle kötüleme [kalıp] — dilini tutmadan istediği gibi konuşmak · arkadaşının ardından kötü konuşmak · dostlarına karşı açık ve cömert
  أفرش الرجل صاحبه إذا اغتابه وأساء القول؛ كأنه توطأه بكلام غير حسن؛ افترش الرجل لسانه إذا تكلم كيف شاء (maqayis)؛ افترش فلان لسانه يتكلم به ما شاء (ayn)؛ افترش لسانه إذا تكلم كيف شاء أي بسطه (sihah)؛ افترش فلان لسانه يتكلم كيف ما يشاء؛ فلان كريم متفرش لأصحابه إذا كان يفرش نفسه لهم (tahdhib)؛ أفرش الرجل صاحبه أي اغتابه وأساء القول فيه (mufradat)
- **B013** el çekme veya üzerinden kalkma [kalıp] — ondan el çekmedi, onu bırakmadı · ölüm üzerlerinden kalktı
  ما أفرش عنه أي ما أقلع (sihah)؛ أفرش عنهم الموت أي ارتفع؛ ضربه فما أفرش عنه حتى قتله أي أقلع عنه (tahdhib)؛ ما أفرش عنه أي ما أقلع عنه؛ تبعد عن قياس الباب وأظنها من باب الإبدال كأنه أفرج (maqayis)
- **B014** doğumdan yedi gün sonraki kısrak — doğumunun üzerinden yedi gün geçmiş tek tırnaklı dişi · kısrak bekledi
  مما شذ عن هذا الأصل الفريش من الخيل التي أتى لوضعها سبعة أيام (maqayis)؛ الفريش من الخيل التي أتى عليها من يوم وضعت سبعة أيام وبلغت أن يضربها الفحل (ayn)؛ كل ذات حافر فهي فريش بعد نتاجها بسبعة أيام (sihah)؛ أفرشت الفرس إذا استأنت؛ الفريش من الخيل التي أتى عليها بعد ولادتها سبعة أيام؛ الفريش من الحافر بمنزلة النفساء (tahdhib)
- **B015** deve bacağında ölçülü açıklık veya hörgüçsüzlük — deve bacağındaki az ve olumlu açıklık · bacağı dışa eğri dişi deve · hörgücü olmayan erkek deve
  جمل مفرش لا سنام له (maqayis)؛ الفرش في رجل البعير اتساع قليل وهو محمود؛ إذا كثر فهو العقل؛ أن لا يكون فيها انتصاب ولا إقعاد (sihah)؛ ناقة مفروشة الرجل إذا كان فيها انئطار وانحناء؛ الفرش مدح والعقل ذم؛ الفرش اتساع في رجل البعير (tahdhib)
- **B016** yalan söyleme — yalan; yalan söylemek
  الفرش الكذب؛ كم تفرش أي كم تكذب (tahdhib)

## ب ث ث (root_000083) — identity root of ٱلْمَبْثُوثِ (w5)

- **B001** dagitip yaymak — bir seyi dagitip yaymak veya aciga cikarmak · atlari saldiriya yaymak veya av kopeklerini ava salmak · yayilip dagilmak · cok ve daginik; yayilmis veya savrulmus · toplanmamis, etrafa sacilmis hurma · yiyecegi veya hurmayi alt ust edip birbirinin ustune atmak · yaratilmislari veya hayvanlari yeryuzune yayip cogaltmak
  تفريق الشيء وإظهاره؛ بثوا الخيل؛ بث الصياد كلابه؛ خلق الخلق وبثهم في الأرض؛ وزرابي مبثوثة؛ تمر بث؛ بثثت الطعام والتمر (maqayis)؛ بث الخيل؛ كل شيء فرقته؛ انبث الجراد؛ كالفراش المبثوث؛ تمر بث (jamhara)؛ فانبث أي انتشر؛ تمر بث؛ منثورا متفرقا؛ الغبار إذا هيجته (sihah)؛ تفريقك الأشياء؛ بثوا الخيل؛ بث الصياد كلابه؛ بثت البسط؛ مبثوثة كثيرة؛ غبارا منتشرا؛ وبث منهما رجالا كثيرا ونساء أي نشر وكثر (tahdhib)؛ التفريق وإثارة الشيء كبث الريح التراب؛ بثثته فانبث؛ وبث فيها؛ كالفراش المبثوث (mufradat)
- **B002** icindekini acip dile getirmek — haberi veya sozu yaymak, duyurmak · birine sirrini acmak ve onu haberdar etmek · insanin icinde tasidigi keder, gam veya sikinti · yoksullugunu ve duskunlugunu birine sikayet etmek · gizli bir kusur, sevgi veya isin durumunu yoklayip anlamaya calisma
  بثثت الحديث أي نشرته؛ البث من الحزن؛ يشتكى ويبث ويظهر؛ أبث فلان شقوره وفقوره؛ وأبثثتك مكتومي (maqayis)؛ بثثته سري وأبثثته؛ البث ما يجده الرجل في نفسه من كرب أو غم (jamhara)؛ بث الخبر وأبثه؛ نشره؛ أبثثتك سري؛ أظهرته لك؛ البث الحال والحزن؛ أظهرت لك بثي (sihah)؛ البث الحزن الذي تفضي به إلى صاحبك؛ أبثثت فلانا سري؛ أطلعته عليه؛ لا يولج الكف ليعلم البث (tahdhib)؛ بث النفس ما انطوت عليه من الغم والسر؛ غمي الذي أبثه عن كتمان (mufradat)
- **B003** arastirip aciga cikarmak [kalıp] — haberi yaymak veya tozu kaldirip savurmak · bir isi arastirip yoklamak veya aciga cikarmak
  بثبثت الخبر بثبثة نشرته؛ وكذلك الغبار إذا هيجته (sihah)؛ بثبثت الأمر إذا فتشت عنه وتخبرته؛ بثبثوه أي كشفوه؛ الأصل فيه بثثوه فأبدلوا (tahdhib)

===== _commentary/v16/out/s101/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 101:4, and ## Buluşmalar) =====
## Vuruş: sıkı olanın dağılması

Surenin ilk kelimesi bir şeyi adıyla değil, yaptığı işle anar. {ar:ٱلْقَارِعَةُ, tr:el-kâria, gloss:vuran, çarpan, source:101:1} kelimesinin kökünde yatan iş, sert bir şeyin başka bir şeyin üstüne indirilmesidir: {ar:القرع ضرب شيء على شيء, tr:el-kar' darbu şey'in alâ şey', gloss:kar', bir şeyin bir şeye vurulmasıdır, source:"ق ر ع,B001"}. Binicinin hayvanını kamçıyla dürtmesi de aynı fiille söylenir: {ar:قرع راحلته أي ضربها بسوطه, tr:karaa râhilatehû, gloss:bineğini kamçısıyla vurdu, source:"ق ر ع,B001"}. Aynı kelime, insanların başına inen ağır belanın da adıdır: {ar:القارعة الشديدة من شدائد الدهر وهي الداهية, tr:el-kâria eş-şedîde min şedâidi'd-dehr, gloss:kâria, zamanın ağır sıkıntılarından biri, büyük felakettir, source:"ق ر ع,B005"}. Bir aile imgesi, kelimenin ayetteki anlamının yerine geçmez; o anlamın yanında duyulur. Burada kelimenin anlamı kıyamettir, duyulan imge ise bir darbenin inişi.

Bu darbe imgesini yalın bir açıklamadan ayıran şey, sonrasında olanlardır. Bir vuruş, sıkı ve bütün olan şeyi çözer; parçaları havaya kaldırır. Dördüncü ayet insanları {ar:ٱلْمَبْثُوثِ, tr:el-mebsûs, gloss:saçılmış, source:101:4} diye niteler. Bu kökün temel işi, rüzgârın toprağı kaldırıp dağıtması gibi bir dağıtmadır: {ar:التفريق وإثارة الشيء كبث الريح التراب, tr:et-tefrîk ve isâratu'ş-şey', gloss:ayırmak ve bir şeyi rüzgârın toprağı savurduğu gibi kaldırmak, source:"ب ث ث,B001"}; kışkırtılan toza da bu adla bakılır {source:"ب ث ث,B001"}. Beşinci ayetin dağları {ar:ٱلْمَنفُوشِ, tr:el-menfûş, gloss:didilmiş, atılmış, source:101:5} yündür. Yünün atılması da bir dövme işidir: {ar:نفش الصوف وهو أن يطرق حتى يتنفش, tr:nefşu's-sûf ve hüve en yutraka hattâ yetenaffeş, gloss:yünü atmak, kabarıp açılıncaya kadar onu dövmektir, source:"ن ف ش,B001"}. Yani dağların sonunu gösteren benzetme de darbelerle kurulmuştur. Yünü anlatan {ar:ٱلْعِهْنِ, tr:el-ıhn, gloss:boyalı yün, source:101:5} kelimesinin kökü, ayrıca kuvvetle kırılmış ama kopmamış, sarkıp kalmış bir dalı da adlandırır: {ar:أصل العاهن أن يتقصف القضيب من الشجرة ولا يبين منها فيبقى معلقا مسترخيا, tr:aslu'l-âhin en yetekassafe'l-kadîb, gloss:âhin, ağaçtan kırılıp ayrılmayan, asılı ve gevşek kalan daldır, source:"ع ه ن,B002"}. Sert bir biçim boyun eğmiş, ama yerinden kopmadan sallanıp kalmıştır.

Dokuzuncu ayetin {ar:هَاوِيَةٌ, tr:hâviye, gloss:düşülen derin çukur, source:101:9} kelimesinin kökü, darbenin öbür yarısını, vuran kolun inişini ve yukarıdan aşağı fırlatmayı da taşır: {ar:أهويت له بالسيف, tr:ehveytu lehû bi's-seyf, gloss:kılıcı ona doğru indirdim, source:"ه و ي,B003"}; {ar:أهويته إذا ألقيته من فوق, tr:ehveytuhû izâ elkaytuhû min fevk, gloss:onu yukarıdan attım, source:"ه و ي,B003"}. Böylece sure vuruştan saçılmaya, saçılmadan çukura atılışa doğru ilerler: önce iniş, sonra dağılma, en sonda hafif olanın aşağı fırlatılması.

Aynı kökler başa inen bir darbeyi de adlandırır. Kafatasının ince kemikleri {ar:فراش الرأس عظام رقاق تلي القحف, tr:ferâşu'r-re's izâmun rikâk, gloss:başın ferâşı, kafatasına bitişik ince kemiklerdir, source:"ف ر ش,B010"} diye anılır ve bir deyim, bu kemikleri uçuran vuruşu anlatır: {ar:ضربة فأطار فراش رأسه, tr:darbeten fe-etâra ferâşe re'sih, gloss:bir vuruş ki başının ince kemiklerini uçurdu, source:"ف ر ش,B011"}. Beynin zarına {ar:أم الرأس وهو الدماغ, tr:ummu'r-re's, gloss:başın anası, yani beyin, source:"ء م م,B003"} denir; ağzını açan yara için de {ar:هوت الطعنة إذا فتحت فاها, tr:hevet et-ta'ne, gloss:mızrak yarası ağzını açtı, source:"ه و ي,B007"} söylenir. Surenin kelimeleri bu dizilişte birbirini izler: birinci ayette vuruş, dördüncüde ferâş, dokuzuncuda ümm ve hâviye. Bu dizi bir aile imgesidir; ayetlerin anlamı kıyamet, insanlar, dağlar ve varılacak yerdir.

Kur'an bu darbeyi başka yerlerde de sahneler. Hâkka suresinde Allah, geçmiş kavimleri anlatırken {ar:كَذَّبَتْ ثَمُودُ وَعَادٌۢ بِٱلْقَارِعَةِ, tr:kezzebet Semûdu ve Âdun bi'l-kâria, gloss:Semûd ve Âd o çarpanı yalanladı, source:69:4} der; aynı surede yer ve dağlar kaldırılır ve {ar:فَدُكَّتَا دَكَّةًۭ وَٰحِدَةًۭ, tr:fe-dukketâ dekketen vâhide, gloss:bir tek çarpışla ezilip düzlendiler, source:69:14}. Ra'd suresinde Allah, inkâr edenler hakkında Peygamberine, onlara yaptıkları yüzünden {ar:قَارِعَةٌ أَوْ تَحُلُّ قَرِيبًۭا مِّن دَارِهِمْ, tr:kâriatun ev tehullu karîben min dârihim, gloss:bir çarpan, ya da yurtlarının yakınına inen bir bela, source:13:31} isabet etmeye devam edeceğini söyler; aynı ayet, Kur'an ile dağların yürütülmesini de anar. Vâkıa suresinde dağlar {ar:وَبُسَّتِ ٱلْجِبَالُ بَسًّۭا, tr:ve bussetil-cibâlu bessâ, gloss:dağlar ufalanıp un ufak edilir, source:56:5} ve {ar:فَكَانَتْ هَبَآءًۭ مُّنۢبَثًّۭا, tr:fe-kânet hebâen munbessâ, gloss:saçılmış toz olur, source:56:6}; buradaki "saçılmış", dördüncü ayetteki mebsûs ile aynı köktendir. Darbe ile dağılmanın arka arkaya gelişi, böylece Kur'an'ın kendi sahnesinde de görülür.

Kaynaklar: 101:1 ٱلْقَارِعَةُ ق ر ع B001; 101:1 ٱلْقَارِعَةُ ق ر ع B005; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:5 ٱلْمَنفُوشِ ن ف ش B001; 101:5 كَٱلْعِهْنِ ع ه ن B002; 101:9 هَاوِيَةٌ ه و ي B003; 101:4 كَٱلْفَرَاشِ ف ر ش B010; 101:4 كَٱلْفَرَاشِ ف ر ش B011; 101:9 فَأُمُّهُۥ ء م م B003; 101:9 هَاوِيَةٌ ه و ي B007

## Kapı çalınır, içeriden soru gelir

Aynı fiil kapının çalınmasını da anlatır: {ar:قرعت الباب أقرعه قرعا, tr:kara'tu'l-bâbe, gloss:kapıyı çaldım, source:"ق ر ع,B001"}. Kelime, evin önündeki açık alanın, yani vuruşun indiği yerin adıdır da: {ar:قارعة الدار ساحتها, tr:kâriatu'd-dâr sâhatuhâ, gloss:evin kâriası, onun avlusudur, source:"ق ر ع,B010"}. Bu imgeyle surenin ilk üç ayeti bir kapı sahnesi gibi işler. Önce vuruş gelir: tek kelime. Sonra içeriden bir ses sorar: {ar:مَا ٱلْقَارِعَةُ, tr:me'l-kâria, gloss:nedir o çarpan, source:101:2}. Ardından soru katlanır: {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْقَارِعَةُ, tr:ve mâ edrâke me'l-kâria, gloss:o çarpanın ne olduğunu sana ne bildirdi, source:101:3}. Kapıyı çalanın kim olduğu söylenmez; cevap bir isim olarak değil, dördüncü ve beşinci ayetlerdeki sahne olarak gelir.

"Bildirmek" fiilinin kökü, kişinin kendi çabasıyla vardığı bir bilgiyi anlatır: {ar:الدراية المعرفة المدركة بضرب من الحيل, tr:ed-dirâye el-ma'rifetu'l-mudreke, gloss:dirâye, bir tür çabayla ulaşılan bilgidir, source:"د ر ي,B001"}; aynı kökte bilmek ile bildirilmek yan yanadır: {ar:دريته ودريت به أي علمت به وأدريته أي أعلمته, tr:dereytuhû... ve edreytuhû, gloss:onu bildim; ona bildirdim, source:"د ر ي,B001"}. Üçüncü ayetteki soru, bu bilginin çabayla ulaşılamayacağını, ancak dışarıdan verilebileceğini hissettirir. Dördüncü ayetin mebsûs kelimesi bu imgeye bir anlam daha katar: aynı kök, haberin yayılmasını ve gizlinin açığa vurulmasını da adlandırır: {ar:أبثثتك سري؛ أظهرته لك, tr:ebsestuke sirrî, gloss:sırrımı sana açtım, source:"ب ث ث,B002"}. Sorunun cevabı, her şeyin açığa saçıldığı bir sahne olarak gelir.

Kelimenin bir anlamı daha, kapıyı çalmanın amacını gösterir: uyarı, onu dinleyeni geri döndürür; dinlemeyen için ise azardır. {ar:أقرعت إلى الحق إقراعا رجعت, tr:akra'tu ile'l-hakk, gloss:hakka döndüm, source:"ق ر ع,B006"}; {ar:فلان لا يقرع أي لا يرتدع, tr:fulânun lâ yukra', gloss:filan kişi uyarıdan geri durmaz, source:"ق ر ع,B006"}. Sure bir vuruşla açılır, çünkü vuruş içerideki kişiyi uyandırmak içindir.

Onuncu ayette aynı soru kalıbı geri döner, bu kez çukur için: {ar:وَمَآ أَدْرَىٰكَ مَا هِيَهْ, tr:ve mâ edrâke mâ hiyeh, gloss:onun ne olduğunu sana ne bildirdi, source:101:10}. Bu sefer cevap bekletilmez; on birinci ayet tek bir ifadeyle karşılık verir: {ar:نَارٌ حَامِيَةٌۢ, tr:nârun hâmiye, gloss:kızgın bir ateş, source:101:11}. Surenin başındaki soru bir sahneyle, sonundaki soru bir ateşle cevaplanır.

Kur'an bu soru kalıbını birçok yerde kullanır. Hâkka suresi aynı üç adımla açılır: {ar:ٱلْحَآقَّةُ, tr:el-hâkka, gloss:gerçekleşecek olan, source:69:1}, {ar:مَا ٱلْحَآقَّةُ, tr:me'l-hâkka, gloss:nedir o gerçekleşecek olan, source:69:2}, {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْحَآقَّةُ, tr:ve mâ edrâke me'l-hâkka, gloss:onun ne olduğunu sana ne bildirdi, source:69:3}; hemen ardından Semûd ile Âd'ın kâriayı yalanladığı anlatılır {source:69:4}. Hümeze suresinde Allah, kusur arayanın {ar:لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ, tr:le-yunbezenne fi'l-hutame, gloss:o mutlaka ezip kırana atılacak, source:104:4} olduğunu söyler, sonra sorar: {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ, tr:ve mâ edrâke me'l-hutame, gloss:ezip kıranın ne olduğunu sana ne bildirdi, source:104:5} ve cevap yine bir ateştir: {ar:نَارُ ٱللَّهِ ٱلْمُوقَدَةُ, tr:nâru'llâhi'l-mûkade, gloss:Allah'ın tutuşturulmuş ateşi, source:104:6}. Müddessir suresinde {ar:وَمَآ أَدْرَىٰكَ مَا سَقَرُ, tr:ve mâ edrâke mâ sekar, gloss:sekarın ne olduğunu sana ne bildirdi, source:74:27} sorusuna {ar:لَا تُبْقِى وَلَا تَذَرُ, tr:lâ tubkî ve lâ tezer, gloss:ne bırakır ne geri koyar, source:74:28} diye cevap verilir. İnfitâr suresinde soru iki kez sorulur, {ar:ثُمَّ مَآ أَدْرَىٰكَ مَا يَوْمُ ٱلدِّينِ, tr:summe mâ edrâke mâ yevmu'd-dîn, gloss:sonra, ceza gününün ne olduğunu sana ne bildirdi, source:82:18}, ve cevap {ar:يَوْمَ لَا تَمْلِكُ نَفْسٌۭ لِّنَفْسٍۢ شَيْـًۭٔا, tr:yevme lâ temliku nefsun li-nefsin şey'â, gloss:hiçbir canın bir başka can için hiçbir şeye güç yetiremediği gün, source:82:19} olur. Târık suresinde gece gelen yolcu da aynı soruyla anılır: {ar:وَمَآ أَدْرَىٰكَ مَا ٱلطَّارِقُ, tr:ve mâ edrâke me't-târık, gloss:gece gelenin ne olduğunu sana ne bildirdi, source:86:2}, cevap {ar:ٱلنَّجْمُ ٱلثَّاقِبُ, tr:en-necmu's-sâkıb, gloss:delip geçen yıldız, source:86:3}. Arapçada târık, gece kapıyı çalarak gelen kişidir {source:"memory"}; kökü kâriadan farklıdır, ama sahne aynı türden bir kapı vuruşudur.

Kaynaklar: 101:1 ٱلْقَارِعَةُ ق ر ع B001; 101:1 ٱلْقَارِعَةُ ق ر ع B010; 101:1 ٱلْقَارِعَةُ ق ر ع B006; 101:3 أَدْرَىٰكَ د ر ي B001; 101:10 أَدْرَىٰكَ د ر ي B001; 101:4 ٱلْمَبْثُوثِ ب ث ث B002

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

## Serilmiş yer ve kazıkları

Ferâş kelimesinin kökü, bir şeyi düzleyip sermek demektir: {ar:أصل صحيح يدل على تمهيد الشيء وبسطه, tr:aslun sahîh yedullu alâ temhîdi'ş-şey' ve bastih, gloss:bir şeyi düzleyip yaymayı gösteren sağlam bir kök, source:"ف ر ش,B001"}. Yeryüzü bu anlamda bir ferâştır, üzerinde yaşanmak için serilmiş bir döşek: {ar:جعل لكم الأرض فراشا أي ذللها, tr:ceale lekumu'l-arda firâşâ, gloss:yeri size döşek yaptı, yani onu boyun eğdirilmiş kıldı, source:"ف ر ش,B001"}. Aynı kök evin yaygısını, evi ve kuşun yuvasını da adlandırır: {ar:الفراش البيت؛ الفراش عش الطائر, tr:el-firâş el-beyt, gloss:firâş evdir; firâş kuşun yuvasıdır, source:"ف ر ش,B002"}. Mebsûs da aynı serme işinin bir parçasıdır: canlılar yeryüzüne yayılmıştır, halılar da zemine: {ar:خلق الخلق وبثهم في الأرض, tr:halaka'l-halka ve besse-hum fi'l-ard, gloss:yaratılmışları yarattı ve onları yeryüzüne yaydı, source:"ب ث ث,B001"}; {ar:بثت البسط, tr:bussetil-busut, gloss:yaygılar serildi, source:"ب ث ث,B001"}. Dağlar ise bu serili yerin kazıklarıdır {source:"ج ب ل,B001"}.

Kıyamet günü bu serme kelimeleri kendi bozuluşlarını taşır. Serili olan şey, yani ferâş, saçılmış bir pervane sürüsü olur; kazıklar, yani dağlar, atılmış yüne döner. Nefş kelimesi de bir yayılmayı anlatır, ama gevşemiş lif olarak: {ar:النفش نشر الصوف كالعهن المنفوش, tr:en-nefş neşru's-sûf, gloss:nefş, yünü atılmış ıhn gibi yaymaktır, source:"ن ف ش,B001"}. Kazık, kendisi yayılan bir şeye dönüşmüştür. Bu imge, surenin dördüncü ve beşinci ayetlerini bir çift olarak okutur: biri yaygıyı, öbürü onu tutan kazıkları anlatır; ikisi birlikte çözülür.

Kur'an bu yaratılış sahnesini birçok yerde anlatır. Bakara suresinde Allah, insanlara seslenirken {ar:ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ فِرَٰشًۭا, tr:ellezî ceale lekumu'l-arda firâşâ, gloss:yeri sizin için döşek yapan, source:2:22} der. Zâriyât suresinde {ar:وَٱلْأَرْضَ فَرَشْنَٰهَا فَنِعْمَ ٱلْمَٰهِدُونَ, tr:ve'l-arda feraşnâhâ fe-ni'me'l-mâhidûn, gloss:yeri biz serdik; ne güzel döşeyiciyiz, source:51:48}. Nebe' suresinde Allah, kıyamet gününü anlatmadan önce sorar: {ar:أَلَمْ نَجْعَلِ ٱلْأَرْضَ مِهَٰدًۭا, tr:e-lem nec'ali'l-arda mihâdâ, gloss:yeri bir beşik yapmadık mı, source:78:6}, {ar:وَٱلْجِبَالَ أَوْتَادًۭا, tr:ve'l-cibâle evtâdâ, gloss:ve dağları kazıklar, source:78:7}; aynı surede sonra dağlar yürütülür ve serap olur {source:78:20}. Gâşiye suresinde dağların nasıl dikildiğine {ar:وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ, tr:ve ile'l-cibâli keyfe nusibet, gloss:dağlara, nasıl dikildiklerine, source:88:19} ve yerin nasıl yayıldığına {ar:وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ, tr:ve ile'l-ardı keyfe sutihat, gloss:ve yere, nasıl düzlendiğine, source:88:20} bakılması istenir. Canlıların ilk yayılışı da aynı fiille anlatılır: {ar:وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ, tr:ve besse fîhâ min kulli dâbbe, gloss:ve orada her türlü canlıyı yaydı, source:2:164}; Nisâ suresinde Allah insanlara, onları tek bir candan yaratıp {ar:وَبَثَّ مِنْهُمَا رِجَالًۭا كَثِيرًۭا وَنِسَآءًۭ, tr:ve besse minhumâ ricâlen kesîran ve nisâ', gloss:ikisinden birçok erkek ve kadın yaydı, source:4:1} diye hatırlatır. İlk yayılış bir yerleşmedir; dördüncü ayetteki yayılış ise bir dağılıştır.

Kaynaklar: 101:4 كَٱلْفَرَاشِ ف ر ش B001; 101:4 كَٱلْفَرَاشِ ف ر ش B002; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:5 ٱلْجِبَالُ ج ب ل B001; 101:5 ٱلْمَنفُوشِ ن ف ش B001

## Çobansız sürü, seyrelen kalabalık

Menfûş kelimesinin kökü, yünün yanında bir sürü sahnesini de taşır: develerin ve koyunların geceleyin, çobansız, otlağa yayılması: {ar:نفشت الإبل والغنم أي رعت ليلا بلا راع ولا يكون النفش إلا بالليل, tr:nefeşeti'l-ibilu ve'l-ğanem, gloss:develer ve koyunlar geceleyin çobansız otladı; nefş ancak gece olur, source:"ن ف ش,B003"}; {ar:نفشت الإبل ترددت وانتشرت بلا راع, tr:nefeşeti'l-ibil, gloss:develer çobansız oraya buraya gidip yayıldı, source:"ن ف ش,B003"}. Ferâş kökü sürünün genç hayvanlarını ve yere yayılan ekini adlandırır: {ar:الفرش صغار الإبل, tr:el-ferş sığâru'l-ibil, gloss:ferş, küçük develerdir, source:"ف ر ش,B004"}; {ar:الفرش الزرع إذا فرش, tr:el-ferş ez-zer', gloss:ferş, yayıldığında ekindir, source:"ف ر ش,B008"}. Aynı açıklama, ferşi beşş ile, yani dördüncü ayetin iki kelimesini birbiriyle anlatır: {ar:يحتمل أن يكون مصدرا من فرشها الله أي بثها بثا, tr:ferşehâ'llâhu ey besse-hâ bessâ, gloss:Allah onları yaydı, yani saçıp dağıttı, source:"ف ر ش,B004"}. Kâria kökü ise otlakların sürülerce soyulup çıplak kalmasını ve ziyaretçisiz kalan avluyu anlatır: {ar:أصبحت الرياض قرعا قد جردتها المواشي, tr:asbahati'r-riyâdu kur'â, gloss:çayırlar hayvanların soyduğu çıplak yerler oldu, source:"ق ر ع,B008"}; {ar:قرع الفناء إذا خلا من الغاشية, tr:kari'a'l-finâ', gloss:avlu gelip gidenlerden boşaldı, source:"ق ر ع,B008"}. Hâviye kökü gecenin bir dilimini de adlandırır {source:"ه و ي,B006"}; sürünün başıboş kaldığı vakit.

İnsanların kendisi de bir topluluktur: {ar:الإنس جماعة الناس, tr:el-ins cemâ'atu'n-nâs, gloss:ins, insanların topluluğudur, source:"ء ن س,B001"}. Dağın kökü büyük bir insan kalabalığını da adlandırır: {ar:الجبل الجماعة العظيمة الكثيرة, tr:el-cibl el-cemâ'atu'l-azîme, gloss:cibl, büyük ve kalabalık topluluk, source:"ج ب ل,B002"}. Sekizinci ayetin fiili, bu kalabalığın seyrelmesini anlatır: {ar:خف القوم خفوفا أي قلوا وقد خفت زحمتهم, tr:haffe'l-kavmu hufûfen, gloss:topluluk azaldı, kalabalıkları hafifledi, source:"خ ف ف,B003"}; ve evlerinden hafifçe göçmelerini: {ar:خفوا عن منازلهم ارتحلوا منها في خفة, tr:haffû an menâzilihim, gloss:evlerinden hafifçe göçtüler, source:"خ ف ف,B002"}. Mebsûs bütün bunları tek kelimede toplar: {ar:كل شيء فرقته, tr:kullu şey'in ferraktehû, gloss:ayırıp dağıttığın her şey, source:"ب ث ث,B001"}. Bu aile imgesinde dördüncü ayetin insanları başıboş, gece dağılmış bir sürü gibidir; geride çıplak bir yer kalır.

Kur'an'da nefş fiili tam da bu sahnede geçer. Enbiyâ suresinde Allah, Dâvûd ile Süleymân'ın bir ekin hakkında hüküm verişini anlatır: {ar:إِذْ نَفَشَتْ فِيهِ غَنَمُ ٱلْقَوْمِ, tr:iz nefeşet fîhi ğanemu'l-kavm, gloss:o topluluğun koyunları geceleyin ona dağılıp otladığında, source:21:78}. En'âm suresinde Allah {ar:وَمِنَ ٱلْأَنْعَٰمِ حَمُولَةًۭ وَفَرْشًۭا, tr:ve mine'l-en'âmi hamûleten ve ferşâ, gloss:hayvanlardan yük taşıyanları ve küçükleri, source:6:142} yarattığını hatırlatır. Kalabalığın dağılışı da Kur'an'ın kıyamet sahnelerindedir: Zilzâl suresinde {ar:يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:yevmeizin yasduru'n-nâsu eştâten li-yurav a'mâlehum, gloss:o gün insanlar amellerini görmek için dağınık gruplar halinde çıkarlar, source:99:6}; Hac suresinde ise kıyametin sarsıntısında {ar:وَتَرَى ٱلنَّاسَ سُكَٰرَىٰ وَمَا هُم بِسُكَٰرَىٰ, tr:ve tere'n-nâse sukârâ ve mâ hum bi-sukârâ, gloss:insanları sarhoş görürsün, oysa sarhoş değillerdir, source:22:2}.

Kaynaklar: 101:5 ٱلْمَنفُوشِ ن ف ش B003; 101:4 كَٱلْفَرَاشِ ف ر ش B004; 101:4 كَٱلْفَرَاشِ ف ر ش B008; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:1 ٱلْقَارِعَةُ ق ر ع B008; 101:9 هَاوِيَةٌ ه و ي B006; 101:4 ٱلنَّاسُ ء ن س B001; 101:5 ٱلْجِبَالُ ج ب ل B002; 101:4 يَكُونُ ك و ن B001; 101:8 خَفَّتْ خ ف ف B003; 101:8 خَفَّتْ خ ف ف B002

## Terazi: ağır kefe, hafif kefe

Altıncı ve sekizinci ayetler iki kefeyi karşı karşıya koyar: {ar:فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ, tr:fe-emmâ men sekulet mevâzînuhû, gloss:tartıları ağır gelen kimseye gelince, source:101:6} ve {ar:وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ, tr:ve emmâ men haffet mevâzînuhû, gloss:tartıları hafif gelen kimseye gelince, source:101:8}. Tartmanın tanımı, bir şeyin ağırlığını benzeriyle karşılaştırmaktır: {ar:الوزن ثقل شيء بشيء مثله, tr:el-vezn siklu şey'in bi-şey'in mislih, gloss:vezn, bir şeyin ağırlığını benzeri olan bir şeyle ölçmektir, source:"و ز ن,B001"}. Ağır olan kefe aşağı iner: {ar:الثقل رجحان الثقيل, tr:es-sikal rüchânu's-sakîl, gloss:ağırlık, ağır olanın basıp inmesidir, source:"ث ق ل,B001"}. Miskal, benzerine karşı konan bilinen bir ağırlıktır {source:"ث ق ل,B004"}. Mîzân ise hem alet hem adalettir: {ar:الآلة التي يوزن بها الأشياء ميزان؛ الميزان العدل, tr:el-âletu elletî yûzenu bihe'l-eşyâ', gloss:şeylerin tartıldığı alet mîzândır; mîzân adalettir, source:"و ز ن,B002"}.

Bu imgenin düz anlatımın ötesinde gösterdiği şey, ağırlığın değer olmasıdır. Değerli ve korunan her şey ağır sayılır: {ar:كل شيء نفيس مصون ثقل, tr:kullu şey'in nefîsin masûnin sekal, gloss:değerli, korunan her şey sekaldir, source:"ث ق ل,B005"}; insanlar ve cinler "iki ağırlık" diye anılır: {ar:سمي الجن والإنس الثقلين, tr:summiye'l-cinnu ve'l-insu's-sekaleyn, gloss:cinler ve insanlar iki ağırlık diye adlandırıldı, source:"ث ق ل,B005"}. Yerin ağırlıkları, onun hazineleri ve Âdemoğullarının bedenleridir {source:"ث ق ل,B002"}. Hafiflik ise tersine değersizliktir: {ar:ما لفلان عندنا وزن أي قدر لخسته, tr:mâ li-fulânin indenâ vezn, gloss:filanın yanımızda bir ağırlığı yok, yani değeri yok, source:"و ز ن,B007"}. Hafif gelmek hem ağırlıkta hem halde hafifliktir, {ar:الخفة خفة الوزن وخفة الحال, tr:el-hiffe hiffetu'l-vezn ve hiffetu'l-hâl, gloss:hafiflik, ağırlığın ve halin hafifliğidir, source:"خ ف ف,B001"}, iyi amellerin azlığıdır {source:"خ ف ف,B003"}, akıl hafifliğidir, {ar:وخفة الرجل طيشه, tr:ve hiffetu'r-raculi tayşuh, gloss:adamın hafifliği onun savrukluğudur, source:"خ ف ف,B004"}, ve hafife alınmaktır: {ar:استخف به أهانه, tr:istehaffe bihî, gloss:onu hafife aldı, aşağıladı, source:"خ ف ف,B005"}. Hafif olan kolayca yerinden oynatılır ve peşe takılır: {ar:استخفه فلان إذا استجهله فحمله على اتباعه في غيه, tr:istehaffehû fulân, gloss:onu cahil yerine koydu ve sapkınlığında kendisine uymaya sürükledi, source:"خ ف ف,B004"}.

Surenin öbür kelimeleri bu teraziyi önceden kurar. Dördüncü ayetin pervanesi hafifliğinden dolayı bu adı almıştır: {ar:الفراش هذا الذي يطير وسمي بذلك لخفته؛ الفراشة الرجل الخفيف, tr:sumiye bi-zâlike li-hiffetih; el-ferâşe er-raculu'l-hafîf, gloss:pervane hafifliğinden ötürü böyle adlandırıldı; ferâşe hafif adamdır, source:"ف ر ش,B005"}; {ar:أطيش من فراشة, tr:etyaşu min ferâşe, gloss:pervaneden daha savruk, source:"ف ر ش,B005"}. Burada geçen savrukluk, sekizinci ayetin hafifliğini anlatan kelimenin ta kendisidir. Beşinci ayetin yünü içi boş liftir {source:"ن ف ش,B002"}; dağ ise iri, kalın gövdedir: {ar:ذو جبلة إذا كان غليظ الجسم, tr:zû cebeletin izâ kâne ğalîza'l-cism, gloss:iri gövdeli olan, source:"ج ب ل,B003"}. Yeryüzünün en ağır şeyi, en hafif şeye dönüşür. Dokuzuncu ayetin fiili hem hızlı bir düşüşü hem hızlı bir yükselişi anlatır: {ar:الهوي السريع إلى أسفل والهوي السريع إلى فوق, tr:el-huviyy es-serî' ilâ esfel ve'l-heviyy es-serî' ilâ fevk, gloss:aşağıya hızlı iniş ve yukarıya hızlı çıkış, source:"ه و ي,B002"}. Bir terazide hafif kefe yukarı kalkar; dokuzuncu ayette ise hafif kefenin sahibi aşağı düşer.

Kâria kelimesinin bir anlamı da ortaklar arasında paylaşılacak bir şey için kura çekmektir: {ar:أقرعت بين الشركاء في شيء يقتسمونه فاقترعوا عليه, tr:akra'tu beyne'ş-şurakâ', gloss:paylaşacakları bir şey için ortaklar arasında kura çektim, source:"ق ر ع,B004"}; {ar:الإقراع والمقارعة هي المساهمة, tr:el-ikrâ' ve'l-mukâra'a hiye'l-musâheme, gloss:kura çekmek, pay için ok atmaktır, source:"ق ر ع,B004"}. Bu adı taşıyan sureden sonra insanlar "fe-emmâ ... ve emmâ" ile iki paya ayrılır. Ama ayırma kura ile değil, iki şeyi karşı karşıya koyarak yapılır: {ar:وازنت بين الشيئين, tr:vâzentu beyne'ş-şey'eyn, gloss:iki şeyi tarttım, birbiriyle karşılaştırdım, source:"و ز ن,B003"}. Payı belirleyen tesadüf değil, ölçüdür. Kur'an'da kura çekilen iki sahne vardır: Sâffât suresinde Yûnus yüklü gemide {ar:فَسَاهَمَ فَكَانَ مِنَ ٱلْمُدْحَضِينَ, tr:fe-sâheme fe-kâne mine'l-mudhadîn, gloss:kura çekti ve kaybedenlerden oldu, source:37:141}; Âl-i İmrân suresinde Allah, Peygambere Meryem'in kimin himayesine gireceği için {ar:إِذْ يُلْقُونَ أَقْلَٰمَهُمْ أَيُّهُمْ يَكْفُلُ مَرْيَمَ, tr:iz yulkûne eklâmehum eyyuhum yekfulu Meryem, gloss:hangisinin Meryem'e bakacağı için kalemlerini atarlarken, source:3:44} orada olmadığını söyler.

Kur'an'da teraziyi açıkça kuran ayetler surenin kelimelerini aynen tekrarlar. A'râf suresinde Allah {ar:وَٱلْوَزْنُ يَوْمَئِذٍ ٱلْحَقُّ ۚ فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ, tr:ve'l-veznu yevmeizini'l-hakk, fe-men sekulet mevâzînuhû fe-ulâike humu'l-muflihûn, gloss:o gün tartı haktır; kimin tartıları ağır gelirse işte onlar kurtuluşa erenlerdir, source:7:8} ve {ar:وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُم, tr:ve men haffet mevâzînuhû fe-ulâike'llezîne hasirû enfusehum, gloss:kimin tartıları hafif gelirse, işte onlar kendilerini kaybedenlerdir, source:7:9} der. Mü'minûn suresi aynı çifti verir {source:23:102} ve hafif gelenlerin {ar:فِى جَهَنَّمَ خَٰلِدُونَ, tr:fî cehenneme hâlidûn, gloss:cehennemde ebedî kalıcıdırlar, source:23:103} olduğunu ekler. Enbiyâ suresinde Allah {ar:وَنَضَعُ ٱلْمَوَٰزِينَ ٱلْقِسْطَ لِيَوْمِ ٱلْقِيَٰمَةِ, tr:ve neda'u'l-mevâzîne'l-kıst li-yevmi'l-kıyâme, gloss:kıyamet günü için adalet terazilerini kurarız, source:21:47} der ve hardal tanesi ağırlığında bir şeyi bile getireceğini söyler. Kehf suresinde, ağırlıksızlığın değersizlik olduğu açıkça söylenir: {ar:فَلَا نُقِيمُ لَهُمْ يَوْمَ ٱلْقِيَٰمَةِ وَزْنًۭا, tr:fe-lâ nukîmu lehum yevme'l-kıyâmeti veznâ, gloss:kıyamet günü onlar için hiçbir tartı kurmayız, source:18:105}. Zilzâl suresinde yer {ar:وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا, tr:ve ahraceti'l-ardu eskâlehâ, gloss:yer ağırlıklarını dışarı çıkarır, source:99:2}, ve zerre ağırlığındaki her iyilik görülür: {ar:فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ, tr:fe-men ya'mel miskâle zerratin hayran yerah, gloss:kim zerre ağırlığında bir iyilik yaparsa onu görür, source:99:7}. Hafifliğin peşe takılmak olduğunu da Kur'an sahneler: Zuhruf suresinde Firavun {ar:فَٱسْتَخَفَّ قَوْمَهُۥ فَأَطَاعُوهُ, tr:fe'stehaffe kavmehû fe-etâûh, gloss:kavmini hafife aldı, onlar da ona uydular, source:43:54}; Rûm suresinde Allah Peygambere, kesin inanmayanların onu hafifletip yerinden oynatmamasını söyler {source:30:60}.

Kaynaklar: 101:6 ثَقُلَتْ ث ق ل B001; 101:6 ثَقُلَتْ ث ق ل B002; 101:6 ثَقُلَتْ ث ق ل B004; 101:6 ثَقُلَتْ ث ق ل B005; 101:6 مَوَٰزِينُهُۥ و ز ن B001; 101:6 مَوَٰزِينُهُۥ و ز ن B002; 101:6 مَوَٰزِينُهُۥ و ز ن B003; 101:8 مَوَٰزِينُهُۥ و ز ن B007; 101:8 خَفَّتْ خ ف ف B001; 101:8 خَفَّتْ خ ف ف B003; 101:8 خَفَّتْ خ ف ف B004; 101:8 خَفَّتْ خ ف ف B005; 101:4 كَٱلْفَرَاشِ ف ر ش B005; 101:5 ٱلْمَنفُوشِ ن ف ش B002; 101:5 ٱلْجِبَالُ ج ب ل B003; 101:9 هَاوِيَةٌ ه و ي B002; 101:1 ٱلْقَارِعَةُ ق ر ع B004

## Hoşnut yaşayış ve döşenmiş ev

Yedinci ayet, tartıları ağır geleni {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:o, hoşnut bir yaşayış içindedir, source:101:7} diye anlatır. Îşe, yaşamaktır: {ar:العيش الحياة, tr:el-ayş el-hayât, gloss:ayş, hayattır, source:"ع ي ش,B001"}. Bu iki kelime dilde zaten birlikte anılır ve aynı sırada tersleri de sayılır: {ar:عيشة صالحة وراضية وصدق وسوء وضنك, tr:îşetun sâliha ve râdiye ve sıdk ve sû' ve dank, gloss:iyi, hoşnut, gerçek, kötü ve dar yaşayış, source:"ع ي ش,B001"}. Ayş aynı zamanda insanın onunla yaşadığı ve içinde yaşadığı şeydir: {ar:المطعم والمشرب وما يكون به الحياة, tr:el-mat'am ve'l-meşrab, gloss:yemek, içecek ve hayatın onunla sürdüğü şey, source:"ع ي ش,B002"}; {ar:كل شيء يعاش به أو فيه فهو معاش, tr:kullu şey'in yu'âşu bihî ev fîh, gloss:onunla ya da içinde yaşanan her şey maâştır, source:"ع ي ش,B002"}. Râdiye, öfkenin karşıtıdır, {ar:أصل واحد يدل على خلاف السخط, tr:aslun vâhid yedullu alâ hılâfi's-suht, gloss:hoşnutsuzluğun zıddını gösteren tek kök, source:"ر ض و,B001"}; bol hoşnutluktur {source:"ر ض و,B002"} ve iki taraflıdır: {ar:المراضاة من اثنين, tr:el-murâdât mini'sneyn, gloss:karşılıklı hoşnutluk iki kişi arasındadır, source:"ر ض و,B003"}. Ayetin tuhaf görünen yapısı, yaşayışın kendisinin hoşnut olması, bu iki taraflılığı hissettirir: yaşayış hem hoşnut eder hem hoşnut olur.

Surenin öbür kelimeleri bu yaşayışın evini döşer. Ferâş, döşenmiş yataktır ve kelimenin örnekleri cennetin döşekleridir: {ar:يقال للمفروش فرش وفراش؛ وفرش مرفوعة؛ فرش بطائنها من إستبرق, tr:ve furuşin merfû'a, gloss:serilene ferş ve firâş denir; yükseltilmiş döşekler; astarları kalın ipekten döşekler, source:"ف ر ش,B002"}. Mebsûs, evin içine serilmiş halılardır: {ar:وزرابي مبثوثة, tr:ve zerâbiyyu mebsûse, gloss:ve serilmiş halılar, source:"ب ث ث,B001"}. Ihn kökü, hazır yemeği ve içeceği, bir yerde yerleşik kalmayı da adlandırır: {ar:العاهن الطعام الحاضر والشراب الحاضر, tr:el-âhin et-taâmu'l-hâdır, gloss:âhin, hazır yemek ve hazır içecektir, source:"ع ه ن,B001"}; {ar:عهن بالمكان أقام به, tr:ahene bi'l-mekân, gloss:o yerde kaldı, yerleşti, source:"ع ه ن,B001"}. Ümm kökü de nimeti, iyi hali anlatır: {ar:الإمة النعمة, tr:el-imme en-ni'me, gloss:imme, nimettir, source:"ء م م,B010"}. Bu aile imgesinde, dördüncü ve beşinci ayetlerde dağılmayı anlatan kelimeler, başka bir okumada yedinci ayetin evinin eşyalarıdır.

Kur'an yedinci ayetin sözlerini aynen başka bir sahnede tekrarlar. Hâkka suresinde, kitabı sağından verilen {ar:فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ, tr:fe-emmâ men ûtiye kitâbehû bi-yemînih, gloss:kitabı sağından verilene gelince, source:69:19} sevinçle kitabını gösterir ve {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:o hoşnut bir yaşayış içindedir, source:69:21}, {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüce bir bahçede, source:69:22}; meyveleri sarkmış, yakındır {source:69:23}. Aynı surede öbür taraf {ar:وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِشِمَالِهِۦ, tr:ve emmâ men ûtiye kitâbehû bi-şimâlih, gloss:kitabı solundan verilene gelince, source:69:25} diye açılır. Gâşiye suresinde yüzler {ar:لِّسَعْيِهَا رَاضِيَةٌۭ, tr:li-sa'yihâ râdiye, gloss:çabalarından hoşnuttur, source:88:9}, ve onların halıları serilidir: {ar:وَزَرَابِىُّ مَبْثُوثَةٌ, tr:ve zerâbiyyu mebsûse, gloss:ve serilmiş halılar, source:88:16}; mebsûs kelimesi burada dördüncü ayetteki ile aynı kalıptadır. Fecr suresinde huzura ermiş can {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irci'î ilâ rabbiki râdiyeten mardiyye, gloss:Rabbine hoşnut ve hoşnut olunmuş olarak dön, source:89:28} diye çağrılır; iki taraflı hoşnutluk burada iki kelimeyle söylenir. Hoşnut yaşayışın zıddı da Kur'an'dadır: Tâhâ suresinde Allah, zikrinden yüz çevirene {ar:فَإِنَّ لَهُۥ مَعِيشَةًۭ ضَنكًۭا, tr:fe-inne lehû maîşeten dankâ, gloss:onun için dar bir geçim vardır, source:20:124} olduğunu söyler.

Kaynaklar: 101:7 عِيشَةٍ ع ي ش B001; 101:7 عِيشَةٍ ع ي ش B002; 101:7 رَّاضِيَةٍ ر ض و B001; 101:7 رَّاضِيَةٍ ر ض و B002; 101:7 رَّاضِيَةٍ ر ض و B003; 101:4 كَٱلْفَرَاشِ ف ر ش B002; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:5 كَٱلْعِهْنِ ع ه ن B001; 101:9 فَأُمُّهُۥ ء م م B010

## Buluşmalar

İmgelerin ilk buluşma yeri dördüncü ve beşinci ayetlerdir. Bir darbe iner ve sıkı olanı dağıtır; bu dağılmanın iki yüzü vardır. Yünün atılması bir dövmedir {source:"ن ف ش,B001"}, dolayısıyla dağların yüne dönmesi, birinci ayetin vuruşunun eseridir. Aynı kelime, menfûş, geceleyin çobansız yayılan sürüyü de anlatır {source:"ن ف ش,B003"}; dağılan dağ ile dağılan sürü tek kelimede birleşir. Dördüncü ayetin ferâşı da hem serili yeri hem saçılan sürüyü taşır; bu iki anlamı bağlayan açıklama, ferşi beşş ile anlatır {source:"ف ر ش,B004"}. Yeryüzünü döşeyen serme işi ile kıyametteki saçılma aynı iki kelimeyle söylenir.

İkinci buluşma, pervane ile terazidir. Pervane hafifliğinden ötürü bu adı almıştır ve savruk adama ferâşe denir {source:"ف ر ش,B005"}; sekizinci ayetin hafifliği de akıl savrukluğudur {source:"خ ف ف,B004"}. Dördüncü ayetin pervane insanları, sekizinci ayetin tartıları hafif gelenleridir. Bu iki imge birlikte surenin hareketini taşır: hafif olan, ışığa doğru savrulur ve ateşe düşer. Pervanenin birbiri ardınca kandile düşüşü {source:"ف ر ش,B005"} ile topluluğun birbiri ardınca çukura düşüşü {source:"ه و ي,B002"} aynı hareketi verir; dokuzuncu ayetin ümm kelimesi hedefe yönelmeyi {source:"ء م م,B012"}, on birinci ayetin ateşi de o hedefin kendisini adlandırır. Böylece dördüncü ayetteki saçılma ile on birinci ayetteki ateş, surenin iki ucunda aynı sahnenin başı ve sonudur. Hâmiye kelimesinin insanların sakındığı korunmuş şeyi anlatan kolu {source:"ح م ي,B002"}, pervanenin yaptığının tersini gösterir.

Üçüncü buluşma, ana ile çukurdur ve bu ikisi yaşayışın karşısında durur. "Anası düştü" deyimi dokuzuncu ayetin iki kelimesini birlikte taşır {source:"ه و ي,B002"}; ümm kelimesinin toplayan, kendine katan anlamı {source:"ء م م,B002"} çukuru, düşeni içine alan yer yapar. Yedinci ayetin yaşayışı ise hayattır {source:"ع ي ش,B001"}; evladını yitirmiş ananın karşısında yaşayan biri. Nâziât suresinin iki sığınağı {source:79:39} {source:79:41} bu karşıtlığı Kur'an'ın kendi sözleriyle kurar.

Dördüncü buluşma çukur ile terazi, ve çukur ile dağlar arasındadır. Hâmiye kuyunun duvarını ören ağır taşlardır {source:"ح م ي,B011"}; içine düşen ise tartısı hafif gelendir. Dağlar en ağır, en kalın kütleydi {source:"ج ب ل,B003"} ve atılmış yünün içi boşluktur {source:"ن ف ش,B002"}; hâviyenin kökü de boşluktur {source:"ه و ي,B001"}. Kazıcıyı durduran kaya {source:"ج ب ل,B005"} yok olunca, çukurun dibi de yoktur. Terazide ağırlık değerse, dağların ağırlığının yüne dönmesi, kıyamet günü dünyanın ağır saydığı şeylerin ağırlıksızlaştığını, tek ağırlığın tartının kefesinde kaldığını gösterir.

Son buluşma, kapı ile ateş arasındadır. Surenin başındaki vuruş üç kez sorulur ve bir sahneyle cevaplanır; onuncu ayetteki soru ise hemen, kızgın bir ateşle cevaplanır. Hümeze suresi aynı soru ile aynı türden cevabı verir {source:104:5} {source:104:6}. Savaş günü imgesi de bu iki ucu birleştirir: başta kılıçların çarpışması {source:"ق ر ع,B002"}, sonda topluluk içinde patlak veren düşmanlık ve kızışan öfke {source:"ن و ر,B007"} {source:"ح م ي,B003"}. Böylece sure bir kapı vuruşuyla, bir uyarıyla açılır ve bir ateşle kapanır; aradaki her kelime, o vuruşun neyi dağıttığını, neyi tarttığını ve hafif olanı nereye düşürdüğünü gösterir.

