Focus: 96:2. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/96_2/D.r13/context.md =====
# 96:2 — focus

خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ

Anchor translation (canonical reading, reference only):

İnsanı bir kan pıhtısından yarattı.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | خَلَقَ | خَلَقَ | خ ل ق | V |
| 2 | ٱلْإِنسَٰنَ | إِنسَٰن | ء ن س | DET;N |
| 3 | مِنْ | مِن |  | P |
| 4 | عَلَقٍ | عَلَق | ع ل ق | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 96 — full text (context; no pericope)

- 96:1 ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ
- 96:2 ◀ focus خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
- 96:3 ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ
- 96:4 ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ
- 96:5 عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ
- 96:6 كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ
- 96:7 أَن رَّءَاهُ ٱسْتَغْنَىٰٓ
- 96:8 إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ
- 96:9 أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ
- 96:10 عَبْدًا إِذَا صَلَّىٰٓ
- 96:11 أَرَءَيْتَ إِن كَانَ عَلَى ٱلْهُدَىٰٓ
- 96:12 أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ
- 96:13 أَرَءَيْتَ إِن كَذَّبَ وَتَوَلَّىٰٓ
- 96:14 أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ
- 96:15 كَلَّا لَئِن لَّمْ يَنتَهِ لَنَسْفَعًۢا بِٱلنَّاصِيَةِ
- 96:16 نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ
- 96:17 فَلْيَدْعُ نَادِيَهُۥ
- 96:18 سَنَدْعُ ٱلزَّبَانِيَةَ
- 96:19 كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩


===== _commentary/v16/work/96_2/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## خ ل ق (root_000434) — identity root of خَلَقَ (w1)

- **B001** ölçüp sınırlarını belirleme — ölçüp sınırlarını belirlemek · ölçüp biçme
  أحدهما تقدير الشيء؛ خلقت الأديم للسقاء إذا قدرته (maqayis)؛ خلقت الأديم قدرته (ayn)؛ خلقت الشيء إذا قدرته (jamhara)؛ الخلق: التقدير؛ خلقت الأديم إذا قدرته قبل القطع (sihah)؛ الخلق في كلام العرب على ضربين... والآخر التقدير؛ خلقت الأديم إذا قدرته وقسته (tahdhib)؛ الخلق أصله: التقدير المستقيم (mufradat)
- **B002** var etme ve ortaya çıkarma — yaratmak, var etmek · yaratan, var eden · yaratan, var eden; özellikle Tanrı için kullanılan ad · yaratılanlar, insanlar · yaratılmış varlık ya da varlıklar topluluğu
  الخالق الصانع (ayn)؛ الخلق مصدر خلق الله الخلق يخلقهم خلقا (jamhara)؛ هم خليقة الله (sihah)؛ الخالق والخلاق؛ الخلق ابتداع الشيء على مثال لم يسبق إليه (tahdhib)؛ يستعمل في إبداع الشيء من غير أصل ولا احتذاء؛ ويستعمل في إيجاد الشيء من الشيء (mufradat)
- **B003** tam ve dengeli dış biçim — dış görünüş ve beden yapısı · beden yapısı tam ve dengeli · yapısı tamamlanmış ve ölçülü · biçimi belirmiş ve oluşumu tamamlanmış
  رجل مختلق تام الخلق؛ المختلق من كل شيء ما اعتدل (maqayis)؛ رجل خليق أي تم خلقه؛ المختلق من كل شيء ما اعتدل (ayn)؛ رجل خليق ومختلق أي تام الخلق معتدل؛ مضغة مخلقة أي تامة الخلق (sihah)؛ رجل خليق إذا تم خلقه؛ مخلقة قد بدا خلقها وغير مخلقة لم تصور (tahdhib)؛ خص الخلق بالهيئات والأشكال والصور المدركة بالبصر (mufradat)
- **B004** huy ve iç karakter — huy, iç karakter · doğal huy ve yaradılıştan eğilim · iyi huyluluk ve iyi geçim · insanlarla huyuna göre geçinmek · bir huyu edinmeye veya öyle görünmeye çalışmak
  الخلق وهي السجية (maqayis)؛ الخليقة الخلق والخليقة الطبيعة (ayn)؛ الخلق: خلق الإنسان الذي طبع عليه؛ حسن الخلق؛ كريم الخليقة (jamhara)؛ الخليقة: الطبيعة؛ الخلقة: الفطرة؛ الخلق والخلق: السجية (sihah)؛ الطبيعة والخليقة والسليقة بمعنى واحد؛ خالق الناس بخلق حسن أي عاشرهم؛ الخلق الدين؛ الخلق المروءة (tahdhib)؛ خص الخلق بالقوى والسجايا المدركة بالبصيرة (mufradat)
- **B005** bir şeye yaraşır ve uygun olma — yaraşır, uygun · bunu yapması ne kadar beklenir · iyiliğe veya o işe çok uygun
  فلان خليق بكذا وأخلق به؛ هو ممن يقدر فيه ذلك (maqayis)؛ مخلقة للخير أي جدير به؛ خليق له أي جدير به؛ ما أخلقه أي ما أشبهه (ayn)؛ فلان خليق بكذا أي جدير به؛ مخلقة لذلك أي مجدرة له (sihah)؛ خليق بذاك أي حري؛ أخلق به أن يفعل؛ مخلقة للخير (tahdhib)؛ فلان خليق بكذا أي كأنه مخلوق فيه ذلك (mufradat)
- **B006** iyilikten düşen pay — pay, özellikle iyilikten düşen pay · iyilikten veya öte dünyadaki karşılıktan payı yok
  الخلاق النصيب لأنه قد قدر لكل أحد نصيبه (maqayis)؛ الخلاق النصيب من الحظ الصالح؛ ليس له خلاق أي ليس له رغبة في الخير ولا في الآخرة (ayn)؛ لا خلاق له أي لا نصيب له في الخير؛ الخلاق النصيب (jamhara)؛ الخلاق: النصيب؛ لا خلاق له في الآخرة (sihah)؛ الخلاق النصيب من الحظ الصالح؛ النصيب من الخير؛ الخلاق الدين (tahdhib)؛ الخلاق ما اكتسبه الإنسان من الفضيلة بخلقه (mufradat)
- **B007** uydurup yalan üretme — söz uydurmak ve çarpıtmak · zihninde yalan kurup ortaya atmak · yanlış kişiye bağlanmış, uydurma · uydurma öyküler ve asılsız anlatılar
  الخلق خلق الكذب وهو اختلاقه واختراعه وتقديره في النفس؛ وتخلقون إفكا (maqayis)؛ الخلق الكذب (ayn)؛ اختلق فلان كلاما إذا زوره؛ وتخلقون إفكا (jamhara)؛ خلق الإفك واختلقه وتخلقه أي افتراه؛ قصيدة مخلوقة أي منحولة (sihah)؛ تقدرون كذبا؛ أحاديث الخلق وهي الخرافات من الأحاديث المفتعلة؛ اختلاق (tahdhib)؛ كل موضع استعمل الخلق في وصف الكلام فالمراد به الكذب؛ إن هذا إلا اختلاق (mufradat)
- **B008** engebesiz ve düz olma — yüzeyini düzeltmek ve pürüzsüzleştirmek · engebesiz, düz ve yoğun · düz ve engebesiz kaya · alnın veya gözler arasının düz bölümü · yayılıp düzleşmek · düzeltilmiş ve yüzeyi engebesiz
  الأصل الثاني ملاسة الشيء؛ صخرة خلقاء أي ملساء؛ اخلولق السحاب استوى؛ رسم مخلولق إذا استوى بالأرض؛ السهم المصلح مخلق لأنه يصير أملس (maqayis)؛ الأخلق الأملس؛ صخرة خلقاء أي مصمتة؛ خليقاء الجبهة مستواها؛ خليقاء الغار الأعلى باطنه؛ اخلولق السحاب أي استوى (ayn)؛ خلقت الحبل والوتر وغيرهما تخليقا إذا ملسته؛ صخرة خلقاء ملساء؛ جبل أخلق؛ ضربه على خلقاء متنه (jamhara)؛ الأخلق الأملس المصمت؛ المخلق القدح إذا لين؛ صخرة خلقاء؛ اخلولق السحاب؛ اخلولق الرسم أي استوى بالأرض (sihah)؛ الأخلق الأملس من كل شيء؛ خليقاء الجبهة مستواها؛ خلقاء الغار الأعلى؛ سهم مخلق أملس مستو؛ الخلقة السحابة المستوية (tahdhib)
- **B009** kullanımdan yıpranıp eskime — kullanımdan yıpranıp tüyünü yitirmek · eski ve yıpranmış giysi · her yanı yıpranmış veya parçalanmış giysi · birine eski ve yıpranmış bir giysi vermek · istemekten yüzünü eskitmek
  أخلق الشيء وخلق إذا بلي؛ إذا أخلق املاس وذهب زئبره؛ ثوب خلق (maqayis)؛ خلق الثوب يخلق خلوقة أي بلي؛ أخلقني فلان ثوبه؛ ثوب أخلاق ممزق من جوانبه (ayn)؛ أخلق الثوب إخلاقا وخلق خلوقة وخلوقا فهو خلق؛ ثوب أخلاق (jamhara)؛ ملحفة خلق وثوب خلق أي بال؛ خلق الثوب أي بلى؛ أخلقته ثوبا إذا كسوته ثوبا خلقا؛ ثوب أخلاق (sihah)؛ خلق الثوب يخلق خلوقة وأخلق إخلاقا؛ أخلق فلان فلانا أي أعطاه ثوبا خلقا؛ ثوب أخلاق؛ جبة خلق (tahdhib)
- **B010** sürülen hoş koku karışımı — sürülen hoş koku karışımı · hoş koku karışımı sürmek veya sürünmek
  الخلوق معروف وهو الخلاق أيضا (maqayis)؛ الخلوق من الطيب؛ فعله التخليق والتخلق (ayn)؛ الخلوق ضرب من الطيب؛ خلقته أي طليته بالخلوق فتخلق به (sihah)؛ الخلوق من الطيب معروف؛ تخلقت المرأة بالخلوق وخلقت غيرها؛ خلق المسجد بالخلوق (tahdhib)
- **B011** su tutan kaya oyuğu veya yeni kuyu — su tutan kaya oyuğu veya yeni kuyu · yeni kazılmış kuyular
  الخلائق نقر في الصفا (ayn)؛ الخليقة نقر في صخرة يجتمع فيه ماء السماء (jamhara)؛ قلاتا تمسك ماء السحاب في صفاة خلقها الله فيها تسميها العرب الخلائق؛ دحلان خلقها الله في بطون الأرض؛ الخليقة البئر ساعة تحفر؛ الخلق الآبار الحديثات الحفر (tahdhib)
- **B012** kapalı üreme yolu — üreme yolu kapalı kadın
  امرأة خلقاء رتقاء لأنها مصمتة كالصفاة الخلقاء (ayn)؛ الخلق: المرأة الرتقاء (jamhara)؛ قيل للمرأة الرتقاء: خلقاء (sihah)؛ يقال للمرأة الرتقاء: خلقاء لأنها مصمتة كالصفاة الخلقاء (tahdhib)

## ء ن س (root_000059) — identity root of ٱلْإِنسَٰنَ (w2)

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

## ع ل ق (root_001039) — identity root of عَلَقٍ (w4)

- **B001** takılma ve bağlı kalma — bir şeye takılıp kalmak · bir şeyi başka bir şeye asmak · kapıyı yerine takıp kurmak · askı parçası veya kapı sürgüsü · kamçı, yay ya da kılıç askısı · kabı asmaya yarayan bağ · kolye ve küpe askı süsleri · göç imkanı kalmayacak biçimde yerleşmek · dikilen fidanın tutması · öldürülen kişinin kan sorumluluğunun birine yüklenmesi
  يناط الشيء بالشيء العالي (maqayis)؛ علق به إذا لزمه (maqayis)؛ علق بالشيء نشب به (ayn)؛ كل شيء علق به شيء فهو معلاقه (ayn;sihah;tahdhib)؛ تعليق الباب نصبه وتركيبه (ayn;tahdhib)؛ علق القربة الذي تشد به ثم تعلق (sihah;tahdhib)
- **B002** makara taşıyıcı su çekme düzeneği — makarayı taşıyan su çekme düzeneği
  العلق ما تعلق به البكرة من القامة (maqayis;ayn;sihah)؛ آلة البكرة (maqayis;sihah)؛ اسم جامع لجميع آلات الاستقاء بالبكرة (tahdhib)؛ الحبل المعلق بالبكرة (tahdhib)
- **B003** pıhtılaşmış kan ve kan emici su canlısı — koyu veya pıhtılaşmış kan · bir parça pıhtılaşmış kan · suda yaşayan kan emici sülük · boğazına sülük yapışmış kimse veya hayvan · su içerken boğazına sülük yapışmak
  العلق الدم الجامد والقطعة منه علقة (maqayis;ayn)؛ الدم الغليظ والقطعة منه علقة (sihah)؛ العلقة الدم الجامد الغليظ (tahdhib)؛ دويبة في الماء تجمع على علق (ayn;sihah)؛ أخذ العلق بحلقه (maqayis;ayn;tahdhib)
- **B004** kalbe yerleşen sevgi — kalbe yerleşen sevgi · bir kadına gönül vermek · kalıcı sevgi bağı · eşini seven ve ona bağlı kadın
  العلق الهوى (maqayis;sihah)؛ نظرة من ذي علق أي ذي هوى (maqayis;sihah)؛ علقت فلانة أي أحببتها (ayn)؛ علاقة الحب (sihah)؛ العلاقة الهوى اللازم للقلب (tahdhib)؛ العلوق من النساء المحبة لزوجها (maqayis;ayn)
- **B005** yapışkan ve ısrarlı çekişme — biriyle çatışıp çekişmek · kişiye bağlı dava veya çekişme · sert ve ısrarlı tartışmacı · tartışmada etkili dil · birine diliyle saldırmak
  علق فلان بفلان خاصمه (maqayis;ayn)؛ العلاقة الخصومة (maqayis)؛ علاقة الخصومة (sihah)؛ رجل معلاق إذا كان شديد الخصومة (maqayis;ayn;sihah;tahdhib)؛ الدعوى يقال لها علاقة (tahdhib)؛ علقه إذا تناوله بلسانه (tahdhib)
- **B006** yaşamı sürdürecek az besin — hayvanın yetindiği kıt otlak · yaşamı sürdürecek az yiyecek · devenin ağzıyla koparıp yediği ot · meyveleri ağzıyla alıp yemek · hayvana asılan yem veya ağaca sarılan bitki · devenin otladığı bir bitki · azla yetinen, seçerek yaşayan gibi değildir
  العلاق الذي يجتزىء به الماشية من الكلأ (maqayis)؛ ما يأكل فلان إلا علقة أي ما يمسك نفسه (maqayis)؛ كل شيء يتبلغ به فهو علقة (ayn;sihah)؛ العلقة من الطعام القليل الذي يتبلغ به (tahdhib)؛ العلوق ما تعلقه الإبل أي ترعاه (maqayis;ayn;sihah;tahdhib)؛ تعلق من ثمار الجنة أي تناول بأفواهها (sihah;tahdhib)
- **B007** elden çıkarılmaya kıyılmayan değerli şey — elden çıkarılmaya kıyılmayan değerli şey · özenle sakınılan değerli şey · değerli sayılan bir içki veya hurma içkisi
  هذا علق من الأعلاق للشيء النفيس (maqayis)؛ علق مضنة ومضنة (maqayis;sihah;tahdhib)؛ العلق المال الذي يكرم عليك تضن به (ayn)؛ العلق بالكسر النفيس من كل شيء (sihah)؛ يقال للشراب عليق (ayn;tahdhib)
- **B008** evlilikte askıda bırakılmış kadın — evlilikte askıda bırakılmış kadın · konuşursa boşanır, susarsa askıda kalır
  كالمعلقة هي التي لا تكون أيما ولا ذات بعل (maqayis)؛ المعلقة من النساء التي فقد زوجها (sihah)؛ امرأة معلقة إذا لم ينفق عليها زوجها ولم يطلقها فهي لا أيم ولا ذات بعل (tahdhib)؛ إن أنطق أطلق وإن أسكت أعلق (maqayis)
- **B009** döllenmenin tutup gebeliğin başlaması — kadının gebe kalması · döllenmesi tutmuş dişi veya erkek üreme sıvısı
  علقت المرأة حبلت (maqayis;sihah)؛ العلوق التي قد علقت لقاحا (ayn)؛ علقت وعقدت على الماء (tahdhib)؛ العلوق ماء الفحل (tahdhib)
- **B010** yavruyu benimsemeyip sütünü esirgeyen deve — yavruyu benimsemeyip sütünü esirgeyen deve · yavruyu benimsemeyen veya süt vermeyen develer · başkasının çocuğunu emziren kadın
  العلوق الناقة التي تأبى أن ترأم ولدها (maqayis)؛ من النوق التي تألف الفحل ولا ترأم البو (ayn)؛ المرأة إذا أرضعت ولد غيرها يقال لها علوق (ayn)؛ العلوق والمعالق الناقة تعطف على غير ولدها فلا ترأمه (sihah)؛ ناقة علوق إذا رئمت بأنفها ومنعت درتها (tahdhib)
- **B011** avın tuzağa takılıp yakalanması — ceylanın veya avın tuzağa takılması · avcının tuzağına av düşmesi
  علق الظبي في الحبالة يعلق إذا نشق فيها (maqayis)؛ أعلق الحابل إذا وقع في حبالته الصيد (maqayis)؛ علق الظبي في الحبالة (sihah)؛ أعلقت فأدرك أي علق الصيد في حبالتك (sihah)
- **B012** biçime bağlı adlandırmalar — sülüğü kan emmesi için bedene yerleştirme · çocuğun boğazındaki hastalıklı bölgeyi parmakla tedavi etme
  أعلقت الأم من عذرة الصبي بيدها (maqayis)؛ الإعلاق إرسال العلق على الموضع ليمص الدم (sihah)؛ الإعلاق أيضا الدغر (sihah)؛ معالجة عذرة الصبي ورفعها بالإصبع (tahdhib)؛ غمز حلق الصبي المعذور (tahdhib)
- **B013** sahibi adına erzak getirmeye gönderilen yük hayvanı — sahibi adına erzak getirmeye gönderilen yük hayvanı
  العليقة الدابة تدفع إلى الرجل ليمتار عليها لصاحبها (maqayis)؛ البعير يوجهه الرجل مع قوم يمتارون (sihah)؛ الناقة يعطيها الرجل القوم يمتارون (tahdhib)
- **B014** insanın peşini bırakmayan ağır bela — kişinin başına gelen büyük bela · insanı yakalayıp bırakmayan ölüm · belalar, ölümler veya insanı bağlayan uğraşlar
  جاء فلان بعلق فلق أي بداهية (maqayis;sihah;tahdhib)؛ أعلق وأفلق (maqayis;tahdhib)؛ المنية علوق (maqayis;sihah;tahdhib)؛ العلق الدواهي والمنايا والأشغال (tahdhib)
- **B015** bele kadar inen küçük üst giysisi — bele veya göbeğe kadar inen küçük üst giysisi
  العلقة قميص يكون إلى السرة (maqayis)؛ ثوب صغير وهو أول ثوب يتخذ للصبي (sihah)؛ العلقة الإتب (tahdhib)؛ الصدرة تلبسها الجارية (tahdhib)
- **B016** bir eylemi yapmaya koyulmak — belirtilen eylemi yapmaya koyulmak
  علق يفعل كذا كأنه يتعلق بالأمر الذي يريده (maqayis)؛ علق فلان يفعل كذا أي طنق وصار (ayn)؛ علق يفعل كذا مثل طفق (sihah)؛ علق فلان يفعل كذا كقولك طفق يفعل كذا (tahdhib)؛ يقال أحبه واعتاده (sihah)

===== _commentary/v16/out/s096/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 96:2, and ## Buluşmalar) =====
## Rahimde toplanan, tutunan, biçim alan

Bu surenin kelimelerinin çoğu, ayetteki anlamlarının yanında aynı kök ailesinin başka bir sahnesini de duyurur. Bu aile imgesi kelimenin ayetteki anlamının yerine geçmez; onun yanında işitilir. Aşağıdaki her bölüm bu yan sahneleri ayetin kendi anlamına dayanarak okur.

İlk sahne bir rahimdir. Kan rahimde toplanır, rahim onun üzerine kapanır, toplanan şey tutunur ve gebelik kalıcı olur. Sonra biçim belirir, ardından doğum yaklaşır. Gebelik bazen de biçim belli olmadan düşer. Surenin ilk emri olan {ar:ٱقْرَأْ, tr:ikra, gloss:oku, source:96:1} kelimesinin kökü, okumanın yanında dişinin rahminde bir şey taşımasını da adlandırır: {ar:ما قرأت الناقة سلى قط … لم تحمل علقة أي دما ولا جنينا, tr:mâ kara'eti'n-nâkatu selan katt … lem tahmil ʿalakaten ey demen ve lâ cenînen, gloss:dişi deve hiç yavru zarı taşımadı … yani hiç kan pıhtısı ya da cenin taşımadı, source:"ق ر ء,B004"}. Bu söz okumanın kökünü, ikinci ayetin {ar:عَلَقٍ, tr:alak, gloss:tutunan pıhtı, source:96:2} kelimesiyle aynı cümlede birleştirir. Aynı kök, rahmin temizlik ve kanama dönemlerini de adlandırır: {ar:القرء الحيض والقرء أيضا الطهر, tr:el-kur'u'l-hayzu ve'l-kur'u eyzan et-tuhr, gloss:kur' hem âdet hem temizlik dönemidir, source:"ق ر ء,B003"}. Kurân bu kelimeyi tam bu anlamda kullanır ve hemen arkasından rahimde yaratılanı anar. Boşanmış kadınlar {ar:ثَلَٰثَةَ قُرُوٓءٍ, tr:selâsete kurû', gloss:üç dönem, source:2:228} bekler ve {ar:مَا خَلَقَ ٱللَّهُ فِىٓ أَرْحَامِهِنَّ, tr:mâ halaka'llâhu fî erhâmihinn, gloss:Allah'ın rahimlerinde yarattığını, source:2:228} gizlemezler. Böylece okumanın kökü ile yaratmanın fiili aynı ayette rahimde buluşur.

İkinci ayet bu sahnenin başlangıcını adlandırır. Alak hem donmuş kan parçasıdır, {ar:العلق الدم الجامد والقطعة منه علقة, tr:el-ʿalaku'd-demu'l-câmid, gloss:alak donmuş kandır, bir parçasına alaka denir, source:"ع ل ق,B003"}, hem de gebeliğin tutunmasıdır, {ar:علقت المرأة حبلت, tr:ʿalikati'l-mer'e: hebilet, gloss:kadın tutundu, yani gebe kaldı, source:"ع ل ق,B009"}. Birinci ve ikinci ayetlerdeki {ar:خَلَقَ, tr:halaka, gloss:yarattı, source:96:2} fiilinin ailesinde biçimi belirmiş cenin vardır: {ar:مخلقة قد بدا خلقها وغير مخلقة لم تصور, tr:muhallaka kad bedâ halkuhâ ve gayru muhallaka lem tusavver, gloss:biçimlenmiş, yani yaratılışı belirmiş; biçimlenmemiş, yani henüz şekil verilmemiş, source:"خ ل ق,B003"}. Kurân bu aşamaları yeniden diriliş için kanıt olarak sayar. Allah insanlara, dirilişten şüphe ediyorlarsa, onları {ar:مِنْ عَلَقَةٍ ثُمَّ مِن مُّضْغَةٍ مُّخَلَّقَةٍ وَغَيْرِ مُخَلَّقَةٍ, tr:min ʿalakatin summe min mudgatin muhallakatin ve gayri muhallaka, gloss:bir pıhtıdan, sonra biçimlenmiş ve biçimlenmemiş bir çiğnemlik etten, source:22:5} yarattığını söyler ve ekler: {ar:وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ, tr:ve nukirru fi'l-erhâmi mâ neşâ', gloss:dilediğimizi rahimlerde durdururuz, source:22:5}. Başka bir yerde aşamalar birbirine yaratma fiiliyle bağlanır: {ar:فَخَلَقْنَا ٱلْعَلَقَةَ مُضْغَةً, tr:fe halaknâ'l-ʿalakate mudga, gloss:pıhtıyı bir çiğnemlik et olarak yarattık, source:23:14}. Dirilişi inkâr eden insana da aynı soru sorulur: {ar:ثُمَّ كَانَ عَلَقَةً فَخَلَقَ فَسَوَّىٰ, tr:summe kâne ʿalakaten fe halaka fe sevvâ, gloss:sonra bir pıhtı oldu, O da yarattı ve düzenledi, source:75:38}. Biçimi verenin kim olduğu da açıkça söylenir: {ar:يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ, tr:yusavvirukum fi'l-erhâm, gloss:sizi rahimlerde biçimlendirir, source:3:6}.

Surenin üçüncü ve sekizinci ayetlerinde de geçen {ar:رَبِّكَ, tr:rabbike, gloss:Rabbin, source:96:1} kelimesinin ailesi bu sahneye bir işleyiş ekler: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye: inşâu'ş-şey'i hâlen fe hâlen ilâ haddi't-temâm, gloss:bir şeyi hal hal, tamamlanacağı sınıra kadar geliştirmek, source:"ر ب ب,B002"}. Yaratan Rab, pıhtıyı aşama aşama tamamlanmaya götürendir. Beşinci ayetin {ar:مَا لَمْ يَعْلَمْ, tr:mâ lem yaʿlem, gloss:bilmediğini, source:96:5} ifadesi bu doğuma bağlanır, çünkü doğan insan hiçbir şey bilmez: {ar:أَخْرَجَكُم مِّنۢ بُطُونِ أُمَّهَٰتِكُمْ لَا تَعْلَمُونَ شَيْـًٔا, tr:ahraceküm min butûni ummehâtikum lâ taʿlemûne şey'â, gloss:sizi annelerinizin karınlarından hiçbir şey bilmez halde çıkardı, source:16:78}. Sekizinci ayetin {ar:ٱلرُّجْعَىٰٓ, tr:er-ruc'â, gloss:dönüş, source:96:8} kelimesinin ailesinde ise sahnenin tersi vardır: {ar:إذا ألقت الناقة حملها قبل أن يستبين خلقه قيل قد رجعت, tr:izâ elkati'n-nâkatu hamlehâ kable en yestebîne halkuhû kîle kad racaʿat, gloss:dişi deve yükünü biçimi belli olmadan düşürünce "döndü" denir, source:"ر ج ع,B013"}. Bu kalıp ifade dönüşü ve biçimi tek cümlede birleştirir. Kurân yaratılış ile geri döndürmeyi bir sahnede birlikte anlatır. İnsan {ar:يَخْرُجُ مِنۢ بَيْنِ ٱلصُّلْبِ وَٱلتَّرَآئِبِ, tr:yahrucu min beyni's-sulbi ve't-terâ'ib, gloss:bel ile göğüs kemikleri arasından çıkan, source:86:7} bir sudan yaratılmıştır ve {ar:إِنَّهُۥ عَلَىٰ رَجْعِهِۦ لَقَادِرٌ, tr:innehû ʿalâ rac'ihî le kâdir, gloss:O onu geri döndürmeye elbette gücü yetendir, source:86:8}. Surenin sonundaki iki kelimenin ailesinde doğumun yaklaşması da vardır: onuncu ayetin fiili için {ar:أصلت الناقة … إذا وقع ولدها في صلاها وقرب نتاجها, tr:aslati'n-nâka … izâ vakaʿa veleduhâ fî salâhâ, gloss:dişi devenin yavrusu sağrısına indi ve doğumu yaklaştı, source:"ص ل و,B005"}, son ayetin emri için {ar:أقربت المرأة إذا قرب ولادها, tr:akrabeti'l-mer'e, gloss:kadının doğumu yaklaştı, source:"ق ر ب,B012"}. Bu iki aile anlamı uzak birer yankıdır, ama kuruluşları ortadadır.

Bu sahne, insanın düz bir anlatımla verilemeyecek bir yanını gösterir: okunması emredilen kişi, kendisi de toplanmış, tutunmuş ve biçimlendirilmiş bir varlıktır. Surenin dönüş ayeti, rahimden çıkan hayatı tekrar başladığı yere bağlar.

Kaynaklar: 96:1 ٱقْرَأْ ق ر ء B004; 96:1 ٱقْرَأْ ق ر ء B003; 96:2 عَلَقٍ ع ل ق B003; 96:2 عَلَقٍ ع ل ق B009; 96:1 خَلَقَ خ ل ق B003; 96:1 رَبِّكَ ر ب ب B002; 96:5 يَعْلَمْ ع ل م B001; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B013; 96:10 صَلَّىٰٓ ص ل و B005; 96:19 وَٱقْتَرِب ق ر ب B012

## Yontulan kamış, düzeltilen ok, kaygan kaya

Bu bölümdeki sahne sert malzeme üzerinde çalışan bir zanaatkârın sahnesidir. Zanaatkâr önce ölçer, sonra keser, yontar ve düzeltir. Birinci ve ikinci ayetlerdeki yaratma fiilinin kökü bu ilk adımı adlandırır: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme izâ kaddertuhû kable'l-katʿ, gloss:deriyi kesmeden önce ölçtüğümde onu "halk" ettim, source:"خ ل ق,B001"}; {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhu't-takdîru'l-mustakîm, gloss:halkın aslı doğru ölçmektir, source:"خ ل ق,B001"}. Kurân yaratmayı ölçmeyle yan yana koyar: {ar:مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ, tr:min nutfetin halakahû fe kaddarahû, gloss:onu bir damladan yarattı ve ölçüsünü verdi, source:80:19}.

Dördüncü ayetin kalemi, yontma işinden adını alır: {ar:أصل القلم القص من الشيء الصلب كالظفر وكعب الرمح والقصب, tr:aslu'l-kalemi'l-kassu mine'ş-şey'i's-sulb, gloss:kalemin aslı, tırnak, mızrak boğumu ve kamış gibi sert bir şeyden kesip almaktır, source:"ق ل م,B001"}; {ar:إنما سمي قلما لأنه قلم مرة بعد مرة, tr:innemâ summiye kalemen li ennehû kulime merraten baʿde merra, gloss:kalem denmesi, tekrar tekrar yontulduğu içindir, source:"ق ل م,B003"}. Öğreten Rab'bin aracı, defalarca yontulmuş bir kamıştır.

Yaratma kökü düzeltmeyi de adlandırır: {ar:السهم المصلح مخلق لأنه يصير أملس, tr:es-sehmu'l-muslahu muhallak, gloss:düzeltilmiş ok "muhallak"tır, çünkü pürüzsüz hale gelir, source:"خ ل ق,B008"}; {ar:المخلق القدح إذا لين, tr:el-muhallaku'l-kıdhu izâ luyyin, gloss:muhallak, yumuşatılmış kura okudur, source:"خ ل ق,B008"}. Kalem kökü de aynı nesneye varır: {ar:الأقلام ها هنا القداح جعلوا عليها علامات على جهة القرعة, tr:el-aklâmu hâhunâ el-kıdâh, gloss:buradaki kalemler, üzerine kura için işaret konmuş oklardır, source:"ق ل م,B004"}. Kurân bu nesneyi Meryem'in bakımı sahnesinde anar. Allah Peygamber'e, kendisinin orada olmadığı bir anı bildirir: {ar:إِذْ يُلْقُونَ أَقْلَٰمَهُمْ أَيُّهُمْ يَكْفُلُ مَرْيَمَ, tr:iz yulkûne aklâmehum eyyuhum yekfulu Meryem, gloss:Meryem'i hangisi üstlenecek diye kalemlerini atarlarken, source:3:44}. Cahiliye kura oklarıyla kısmet aramak ise yasaklanır: {ar:وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ ذَٰلِكُمْ فِسْقٌ, tr:ve en testaksimû bi'l-ezlâm, zâlikum fisk, gloss:fal oklarıyla pay aramanız da haram kılındı; bu yoldan çıkmaktır, source:5:3}. Bu okların toplandığı torbanın adı da rab kökündendir: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر, tr:er-rabâbe, gloss:rabâbe, kumar oklarının toplandığı sadağa benzer bir torbadır, source:"ر ب ب,B010"}.

Pürüzsüzleştirme sahnesinin bir de kaya hali vardır. Yaratma kökü kaygan kayayı adlandırır: {ar:صخرة خلقاء أي ملساء, tr:sahratun halkâ', gloss:halkâ kaya, yani kaygan kaya, source:"خ ل ق,B008"}. Altıncı ayetin {ar:لَيَطْغَىٰٓ, tr:le yatgâ, gloss:azar, source:96:6} fiilinin kökü de aynı kayayı adlandırır: {ar:الطغية الصفاة الملساء, tr:et-tugye es-safâtu'l-melsâ', gloss:tugye, kaygan kaya düzlüğüdür, source:"ط غ ي,B005"}. Kartalın pençesi bu kayada tutunamaz. Bu kayanın oyuklarında yağmur suyu birikir: {ar:الخليقة نقر في صخرة يجتمع فيه ماء السماء, tr:el-halîka nakrun fî sahra, gloss:halîka, kayada gök suyunun biriktiği oyuktur, source:"خ ل ق,B011"}. Böylece aynı kök hem ustaca işlenmiş nesneyi hem de üzerine tutunulamayan kayayı adlandırır. Azan insan, yontulup düzeltilmiş olduğunu unutup kendini hiçbir şeyin tutamadığı kaygan bir doruk sanır.

Kaynaklar: 96:1 خَلَقَ خ ل ق B001; 96:4 ٱلْقَلَمِ ق ل م B001; 96:4 ٱلْقَلَمِ ق ل م B003; 96:1 خَلَقَ خ ل ق B008; 96:4 ٱلْقَلَمِ ق ل م B004; 96:1 رَبِّكَ ر ب ب B010; 96:6 لَيَطْغَىٰٓ ط غ ي B005; 96:2 خَلَقَ خ ل ق B011

## Göz bebeğindeki insan, ayna ve bakış

Surede üç kez geçen {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan, source:96:2} kelimesinin ailesinde, göz bebeğinin karasında görülen küçük suret de vardır: {ar:إنسان العين المثال الذي يرى في السواد أي سواد العين, tr:insânu'l-ʿayn el-misâlu'llezî yurâ fi's-sevâd, gloss:gözün insanı, göz karasında görülen surettir, source:"ء ن س,B005"}. Aynı kök görerek fark etmeyi de anlatır: {ar:آنسته أبصرته, tr:ânestuhû: ebsartuhû, gloss:onu fark ettim, yani gördüm, source:"ء ن س,B002"}.

Yedinci ayette insan kendini görür: {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en ra'âhu'stagnâ, gloss:kendini yeterli gördüğü için, source:96:7}. Fiilin öznesi de nesnesi de aynı kişidir. Görme kökünün ailesinde ayna vardır: {ar:المرآة ما يرى فيه صورة الأشياء, tr:el-mir'âtu mâ yurâ fîhi sûretu'l-eşyâ', gloss:ayna, içinde şeylerin suretinin görüldüğü şeydir, source:"ر ء ي,B006"}; {ar:رأيت الرجل ترئية إذا أمسكت له المرآة لينظر فيها, tr:ra'eytu'r-racule terʾiyeten, gloss:adama bakması için ayna tuttum, source:"ر ء ي,B012"}. Bu ayette görmek aynı zamanda bir yargıdır: {ar:الرأي اعتقاد النفس, tr:er-ra'yu'ʿtikâdu'n-nefs, gloss:re'y, nefsin kanaatidir, source:"ر ء ي,B002"}. İnsan kendine bakar ve gördüğü suretten yeterli olduğu yargısını çıkarır.

Sure dinleyene üç kez seslenir: {ar:أَرَءَيْتَ, tr:e ra'eyte, gloss:gördün mü, source:96:9}. Bu kalıp hem "bana haber ver" anlamına gelir hem de uyarır: {ar:يجري أرأيت مجرى أخبرني وكل ذلك فيه معنى التنبيه, tr:yecrî e ra'eyte mecrâ ahbirnî, gloss:"gördün mü" "bana haber ver" yerine geçer ve hepsinde uyarı anlamı vardır, source:"ر ء ي,B013"}. On dördüncü ayet ise bu bakışların hepsini çevreleyen bakışı söyler: {ar:أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ, tr:e lem yaʿlem bi ennallâhe yerâ, gloss:Allah'ın gördüğünü bilmedi mi, source:96:14}. Burada bilmek bir şeyi gerçekte olduğu gibi kavramaktır: {ar:إدراك الشيء بحقيقته, tr:idrâku'ş-şey'i bi hakîkatih, gloss:bir şeyi hakikatiyle kavramak, source:"ع ل م,B001"}. Kurân aynı çerçeveyi bir başka yerde kurar: {ar:أَفَرَءَيْتَ ٱلَّذِى تَوَلَّىٰ, tr:e fe ra'eyte'llezî tevellâ, gloss:yüz çevireni gördün mü, source:53:33}, {ar:أَعِندَهُۥ عِلْمُ ٱلْغَيْبِ فَهُوَ يَرَىٰٓ, tr:e ʿindehû ʿilmu'l-gaybi fe huve yerâ, gloss:yanında gaybın bilgisi var da o mu görüyor, source:53:35}. Yüz çevirme, bilme ve görme burada da birlikte gelir. Malını harcamakla övünen insana da aynı soru sorulur: {ar:أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ, tr:e yahsebu en lem yerahû ehad, gloss:onu kimsenin görmediğini mi sanıyor, source:90:7}. Geri dönmeyeceğini sanan için de {ar:بَلَىٰٓ إِنَّ رَبَّهُۥ كَانَ بِهِۦ بَصِيرًا, tr:belâ inne rabbehû kâne bihî basîrâ, gloss:hayır, Rabbi onu hep görüyordu, source:84:15} denir. Namaz kılan kulun görülmesi ise Peygamber'e bir teselli olarak söylenir: {ar:ٱلَّذِى يَرَىٰكَ حِينَ تَقُومُ, tr:ellezî yerâke hîne tekûm, gloss:kalktığında seni gören, source:26:218}, {ar:وَتَقَلُّبَكَ فِى ٱلسَّٰجِدِينَ, tr:ve tekallubeke fi's-sâcidîn, gloss:secde edenler arasında dönüp durmanı da, source:26:219}.

Görme kökü bunun tersini de içerir. Görülmek için yapılan iş: {ar:يرآءون الناس إذا أبصرهم الناس صلوا, tr:yurâ'ûne'n-nâs, gloss:insanlara gösteriş yaparlar; insanlar onları görünce namaz kılarlar, source:"ر ء ي,B005"}. Kurân bunu namaz kılanlar için söyler: {ar:فَوَيْلٌ لِّلْمُصَلِّينَ, tr:fe veylun li'l-musallîn, gloss:yazık o namaz kılanlara, source:107:4}, {ar:ٱلَّذِينَ هُمْ يُرَآءُونَ, tr:ellezîne hum yurâ'ûn, gloss:ki onlar gösteriş yaparlar, source:107:6}. Surenin kulu ise Allah'ın görmesi altında namaz kılar. Son ayetteki secdenin kökü de bir bakış biçimini adlandırır: {ar:أصل السجود إدامة النظر في إطراق إلى الأرض, tr:aslu's-sucûd idâmetu'n-nazar fî itrâk, gloss:secdenin aslı, gözü yere indirerek uzun uzun bakmaktır, source:"س ج د,B005"}. Secdeden kaçınanların gözü ise bunun tersidir: {ar:وَيُدْعَوْنَ إِلَى ٱلسُّجُودِ فَلَا يَسْتَطِيعُونَ, tr:ve yudʿavne ile's-sucûdi fe lâ yestatîʿûn, gloss:secdeye çağrılırlar ama güç yetiremezler, source:68:42}, {ar:خَٰشِعَةً أَبْصَٰرُهُمْ, tr:hâşiʿaten ebsâruhum, gloss:gözleri yere eğik halde, source:68:43}.

Bakış bu sırayla ilerler: önce kendini aynada yeterli görmek, sonra dinleyenin bakmaya çağrılması, sonra Allah'ın görmesi ve en sonunda yere indirilen göz. Bir düz anlatım bunu yalnızca bir uyarı olarak verir; bu sahne bakışın yön değiştirmesini gösterir.

Kaynaklar: 96:2 ٱلْإِنسَٰنَ ء ن س B005; 96:2 ٱلْإِنسَٰنَ ء ن س B002; 96:7 رَّءَاهُ ر ء ي B006; 96:7 رَّءَاهُ ر ء ي B012; 96:7 رَّءَاهُ ر ء ي B002; 96:9 أَرَءَيْتَ ر ء ي B013; 96:14 يَرَىٰ ر ء ي B001; 96:14 يَعْلَم ع ل م B001; 96:7 رَّءَاهُ ر ء ي B005; 96:19 وَٱسْجُدْ س ج د B005

## Tutunmak ve kendini yeterli görmek

İnsan, tutunan bir şeyden yaratılmıştır. Alak kökü asılmayı ve yapışmayı adlandırır: {ar:يناط الشيء بالشيء العالي, tr:yunâtu'ş-şey'u bi'ş-şey'i'l-ʿâlî, gloss:bir şeyin yüksekteki bir şeye asılması, source:"ع ل ق,B001"}; {ar:علق بالشيء نشب به, tr:ʿalika bi'ş-şey'i neşibe bih, gloss:bir şeye takıldı, ona yapıştı, source:"ع ل ق,B001"}. Aynı kök suya yapışan sülüğü de adlandırır: {ar:دويبة في الماء تجمع على علق, tr:duveybetun fi'l-mâ', gloss:suda yaşayan küçük bir hayvan; çoğulu alaktır, source:"ع ل ق,B003"}. Ayrıca canı ayakta tutan en az lokmayı adlandırır: {ar:ما يأكل فلان إلا علقة أي ما يمسك نفسه, tr:mâ ye'kulu fulânun illâ ʿulka, gloss:falan ancak canını tutacak kadar yer, source:"ع ل ق,B006"}. İnsanın başlangıcı yüksekteki bir şeye asılı, tutunarak ve azla yaşayan bir şeydir.

Beşinci ayet bu eksik varlığa öğretilen şeyi anar: bilmediği şey ona verilir. Yedinci ayet sonra tersine döner: insan kendini {ar:ٱسْتَغْنَىٰٓ, tr:istagnâ, gloss:muhtaç olmayan, yeterli, source:96:7} görür. Kök ihtiyaçsızlığı adlandırır: {ar:عدم الحاجات وقلة الحاجات وكثرة القنيات, tr:ʿademu'l-hâcât ve killetu'l-hâcât ve kesretu'l-kunyât, gloss:ihtiyaçların olmaması, azlığı ve edinilmiş şeylerin çokluğu, source:"غ ن ي,B001"}. Aynı kök bir şeyin yetip yetmemesini de anlatır: {ar:ما يغني عنك هذا أي ما يجزئ وما ينفع, tr:mâ yugnî ʿanke hâzâ, gloss:bu sana yetmez, fayda vermez, source:"غ ن ي,B002"}. Kökte kendine bakışla yeterliliği tek figürde birleştiren bir kadın da vardır: {ar:الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي, tr:el-gâniye, gloss:gâniye, kocası ya da güzelliği sayesinde süs takmaya ihtiyaç duymayan kadındır, source:"غ ن ي,B005"}. Yedinci ayetteki "kendini görmek" ile "yeterli olmak" bu figürde bir araya gelir.

Kurân bu kelimeyi birkaç sahnede inkârla birleştirir: {ar:وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ, tr:ve emmâ men bahile ve'stagnâ, gloss:cimrilik eden ve kendini muhtaç görmeyene gelince, source:92:8}, {ar:وَكَذَّبَ بِٱلْحُسْنَىٰ, tr:ve kezzebe bi'l-husnâ, gloss:ve en güzeli yalanlayan, source:92:9}. Peygamber'e, kendini yeterli gören zengin kişiye yönelmesi hatırlatılır: {ar:أَمَّا مَنِ ٱسْتَغْنَىٰ, tr:emmâ meni'stagnâ, gloss:kendini muhtaç görmeyene gelince, source:80:5}, {ar:فَأَنتَ لَهُۥ تَصَدَّىٰ, tr:fe ente lehû tesaddâ, gloss:sen ona yöneliyorsun, source:80:6}. Gerçek yeterliliğin kime ait olduğu da söylenir. Elçilerini reddedenler için {ar:فَكَفَرُوا۟ وَتَوَلَّوا۟ وَّٱسْتَغْنَى ٱللَّهُ, tr:fe keferû ve tevellev vestagna'llâh, gloss:inkâr ettiler ve yüz çevirdiler, Allah da onlara ihtiyaç duymadı, source:64:6} denir. Tüm insanlara da {ar:أَنتُمُ ٱلْفُقَرَآءُ إِلَى ٱللَّهِ وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:entumu'l-fukarâ'u ila'llâh, va'llâhu huve'l-ganiyyu'l-hamîd, gloss:Allah'a muhtaç olanlar sizsiniz, ihtiyaçsız ve övülmeye layık olan Allah'tır, source:35:15} denir. Hesap gününde ise yeterlilik iddiası kendi ağzından çöker: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ, tr:mâ agnâ ʿannî mâliyeh, gloss:malım bana hiçbir yarar sağlamadı, source:69:28}.

Rab kelimesinin ailesinde ihtiyaç ile nimet tek kelimede birleşir: {ar:الربى: الحاجة؛ … الربى: النعمة والإحسان, tr:er-rubbâ: el-hâce … er-rubbâ: en-niʿmetu ve'l-ihsân, gloss:rubbâ ihtiyaçtır; rubbâ nimet ve iyiliktir da, source:"ر ب ب,B016"}. Üçüncü ayetteki en cömert sıfatı ihtiyacı gideren vericiyi anlatır: {ar:الكثير الخير الجواد المنعم المفضل, tr:el-kesîru'l-hayr el-cevâdu'l-munʿim, gloss:hayrı çok, cömert, nimet veren, lütfeden, source:"ك ر م,B001"}. Kurân insanın bu cömertliğe nasıl karşılık verdiğini anlatır: {ar:فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ, tr:fe ekramehû ve naʿʿamehû fe yekûlu rabbî ekramen, gloss:Rabbi ona ikram edip nimet verince "Rabbim bana ikram etti" der, source:89:15}. Hemen ardından rızkı daraltılınca {ar:فَيَقُولُ رَبِّىٓ أَهَٰنَنِ, tr:fe yekûlu rabbî ehânen, gloss:"Rabbim beni aşağıladı" der, source:89:16}. Kısacası insan, ikramı kendi değerinin kanıtı sayar.

On beşinci ayetteki {ar:يَنتَهِ, tr:yentehi, gloss:vazgeçer, source:96:15} fiilinin ailesinde "yeter" anlamı vardır: {ar:فلان ناهيك من رجل… كما يقال حسبك, tr:fulânun nâhîke min racul, gloss:falan sana yeter bir adamdır, "hasbuk" dendiği gibi, source:"ن ه ي,B005"}. Onuncu ayetin kulu ise kendine ait bir şeyi olmayandır: {ar:العبد وهو المملوك, tr:el-ʿabdu ve huve'l-memlûk, gloss:kul, sahip olunandır, source:"ع ب د,B001"}. Sekizinci ayetteki dönüş, yeterlilik iddiasını geçersiz kılar: asılı başlayan varlık, asıl olduğu yere döner.

Kaynaklar: 96:2 عَلَقٍ ع ل ق B001; 96:2 عَلَقٍ ع ل ق B003; 96:2 عَلَقٍ ع ل ق B006; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B001; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B002; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B005; 96:1 رَبِّكَ ر ب ب B016; 96:3 ٱلْأَكْرَمُ ك ر م B001; 96:15 يَنتَهِ ن ه ي B005; 96:10 عَبْدًا ع ب د B001

## Tuzak ve av

Avcılar açık araziye çıkar, tuzak kurar; av ağa takılır. Yaban hayvanı bir süre koşar, sonra durup arkasına bakar. Bu sahnenin üyeleri surenin birçok kelimesine dağılmıştır. Onuncu ayetin namaz fiilinin ailesinde tuzak kurmak vardır: {ar:المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد, tr:el-maslât en tensibe şereken, gloss:maslât, bir şey düşsün de avlansın diye tuzak kurmaktır, source:"ص ل و,B004"}. Bu anlam mecaz olarak birinin yıkımına çalışmak için de kullanılır: {ar:صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة, tr:salaytu li fulân, gloss:falana tuzak kurdum, yani onu helake düşürmek için uğraştım, source:"ص ل و,B004"}. İkinci ayetin alak kökünde ağa takılan ceylan vardır: {ar:علق الظبي في الحبالة يعلق إذا نشق فيها, tr:ʿalika'z-zabyu fi'l-hibâle, gloss:ceylan ağa takıldı, source:"ع ل ق,B011"}. Birinci ayetin ad kelimesinin kökünde avcılar vardır: {ar:خرج القوم للصيد في قفار الأرض وصحاريها قلت سموا وهم السماة أي الصيادون, tr:semev, ve humu's-sumât, gloss:topluluk ıssız yerlere ava çıktığında "semev" denir; onlar sumâttır, yani avcılar, source:"س م و,B006"}. On beşinci ayetin fiilinin ailesinde kovalamaca ve yırtıcı kuşun vuruşu bulunur: {ar:المسافعة كالمطاردة, tr:el-musâfaʿa ke'l-mutârade, gloss:müsâfaa kovalamaca gibidir, source:"س ف ع,B005"}; {ar:سفع الطائر ضريبته أي لطمه, tr:sefaʿa't-tâ'iru darîbeteh, gloss:kuş avına vurdu, source:"س ف ع,B004"}. On üçüncü ayetin yalanlama fiilinin ailesinde de kaçan hayvan vardır: {ar:كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه, tr:kezebe'l-vahşiyy, gloss:yaban hayvanı bir koşu koşup sonra arkasına bakmak için durdu, source:"ك ذ ب,B007"}.

Sahnenin işleyişi tersine döner. Kulun namazına engel olmak isteyen adam bir avcı gibi davranır. Ama yakalanan odur: perçeminden tutulur, tıpkı ağa takılan av gibi. Kurân Peygamber'e karşı kurulan tuzağı ve tuzağın sahibine dönüşünü anlatır: {ar:وَإِذْ يَمْكُرُ بِكَ ٱلَّذِينَ كَفَرُوا۟ لِيُثْبِتُوكَ أَوْ يَقْتُلُوكَ أَوْ يُخْرِجُوكَ, tr:ve iz yemkuru bike'llezîne keferû li yusbitûke ev yaktulûke ev yuhricûk, gloss:inkâr edenler seni tutup bağlamak, öldürmek ya da çıkarmak için tuzak kuruyorlardı, source:8:30}, {ar:وَيَمْكُرُونَ وَيَمْكُرُ ٱللَّهُ, tr:ve yemkurûne ve yemkuru'llâh, gloss:onlar tuzak kuruyordu, Allah da tuzak kuruyordu, source:8:30}. Bu sahne, avcının av olduğu bir çevrilmeyi yasaklayanın sonuna bağlar.

Kaynaklar: 96:10 صَلَّىٰٓ ص ل و B004; 96:2 عَلَقٍ ع ل ق B011; 96:1 بِٱسْمِ س م و B006; 96:15 لَنَسْفَعًۢا س ف ع B005; 96:15 لَنَسْفَعًۢا س ف ع B004; 96:13 كَذَّبَ ك ذ ب B007; 96:15 ٱلنَّاصِيَةِ ن ص ي B001

## Buluşmalar

İmgeler en açık şekilde baş sahnesinde buluşur. On beşinci ayetin fiili hem perçemden tutmak hem de yüzü karartmaktır. Böylece başın önü, avın yakalandığı yer, huysuz hayvanın tutulduğu yer ve ateşin yaladığı deri aynı noktada birleşir. Aynı alın son ayette yere konur ve secde izini taşır. İşaret imgesi buraya da uzanır: bir alın kararmış bir lekeyle işaretlenir, öteki secdenin iziyle. Kurân her iki tarafı da yüzlerindeki işaretle tanıtır: biri {ar:مِّنْ أَثَرِ ٱلسُّجُودِ, tr:min eseri's-sucûd, gloss:secdenin izinden, source:48:29}, öteki {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. Sure ad ile başlar ve iki işaretli alınla biter.

Göz ile yeterlilik imgeleri yedinci ayette buluşur. Kendini aynada gören adam ile süse ihtiyaç duymayan güzel kadın aynı kelime çiftinde birleşir: kendini görmek ve yeterli saymak. Su imgesi de buna bağlanır. Azan insan ölçüsünü aşan bir taşkın gibidir; on beşinci ayette durması istenir. Kökün göletteki duruluşu adlandırdığı hatırlanırsa, sekizinci ayet bu suyun nereye varacağını söyler. Kurân'ın varış ayeti bu iki imgeyi aynı yapıda birleştirir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Yol imgesi de bu dönüşe katılır, çünkü dönüş başlangıca dönmektir ve bu başlangıç rahimdeki ilk tutunuştur.

Rahim ile okuma, surenin ilk kelimesinde buluşur. Okumanın kökü hem rahmin bir şeyi toplayıp tutmasını hem de harflerin toplanmasını adlandırır. Pıhtıyı tutan kökle sözü toplayan kök aynıdır. İnsanın yaratılışı ve öğretilmesi bu yüzden aynı işin iki yüzü olarak duyulur. Kurân'daki benzer sıra da bunu destekler: Kurân'ı öğretmek, insanı yaratmak ve ona açıklamayı öğretmek. Okuma ile secde de buluşur: okuyucu aynı zamanda kulluk edendir ve sure, ilk emri okumak, son emri secde etmek olan bir eğri çizer. Kurân bu ikisini, okunduğunda secde edenler ile etmeyenler üzerinden birleştirir.

Ateş ile çağrı imgeleri onuncu, on yedinci ve on sekizinci ayetlerde buluşur. Namaz hem çağrıdır hem de kökü ateşe girmeyi adlandırır. Adam meclisini çağırır, Allah ateşe iten bekçileri çağırır ve kul yakın meclise çağrılır. Ateşin kendisinin de çağırdığı söylenir: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Bu yüz çevirme on üçüncü ayetin fiilidir.

İtaat ile hayvan imgeleri son ayette buluşur. Rab, itaat edilen efendidir; dizgine uyan at da itaatin bir figürüdür. Kul bu yüzden kendini rab ilan eden birine boyun eğmez, yakında tutulan ve değer gören at gibi yaklaşır. Yaratma ile uydurma da on altıncı ayette buluşur. Gerçek ölçüyle yaratan Rab'bin karşısında, yalanı içinde ölçen yalancı perçem durur.

Bu buluşmalar surenin hareketini taşır. Sure, rahimde toplanan ve tutunan bir varlıkla başlar; bu varlık sözü toplamayı ve kalemle yazmayı öğrenir. Sonra kendini aynada yeterli görür, taşkın su gibi ölçüsünü aşar, başını kaldırır ve namaz kılan kulu engellemeye çalışır. Dönüş ayeti ve Allah'ın görmesi bu yükselişin önüne bir sınır koyar. Yasaklayan perçeminden yakalanır, meclisi yerine bekçiler gelir. Kul ise yüz çevirmeden, başını yere koyarak, çağrılmış olduğu yakınlığa yürür.

