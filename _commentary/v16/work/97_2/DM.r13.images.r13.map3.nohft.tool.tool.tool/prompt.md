Focus: 97:2. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/97_2/D.r13/context.md =====
# 97:2 — focus

وَمَآ أَدْرَىٰكَ مَا لَيْلَةُ ٱلْقَدْرِ

Anchor translation (canonical reading, reference only):

Ve Kadir Gecesi'nin ne olduğunu sana ne bildirdi?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَمَآ | مَا |  | CONJ;INTG |
| 2 | أَدْرَىٰكَ | أَدْرَىٰ | د ر ي | V;PRON |
| 3 | مَا | مَا |  | INTG |
| 4 | لَيْلَةُ | لَيْلَة | ل ي ل | N |
| 5 | ٱلْقَدْرِ | قَدْر | ق د ر | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 97 — full text (context; no pericope)

- 97:1 إِنَّآ أَنزَلْنَٰهُ فِى لَيْلَةِ ٱلْقَدْرِ
- 97:2 ◀ focus وَمَآ أَدْرَىٰكَ مَا لَيْلَةُ ٱلْقَدْرِ
- 97:3 لَيْلَةُ ٱلْقَدْرِ خَيْرٌۭ مِّنْ أَلْفِ شَهْرٍۢ
- 97:4 تَنَزَّلُ ٱلْمَلَٰٓئِكَةُ وَٱلرُّوحُ فِيهَا بِإِذْنِ رَبِّهِم مِّن كُلِّ أَمْرٍۢ
- 97:5 سَلَٰمٌ هِىَ حَتَّىٰ مَطْلَعِ ٱلْفَجْرِ


===== _commentary/v16/work/97_2/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## د ر ي (root_000473) — identity root of أَدْرَىٰكَ (w2)

- **B001** bir şeyi bilme, ustalıkla kavrama ve başkasına bildirme — bir şeyi bilmek veya ondan haberdar olmak · birine bildirmek, onun bilmesini sağlamak · bilgi ve kavrayış; özellikle düşünsel ustalıkla edinilen bilgi · bilmiyorum
  دريت الشيء والله أدرانيه (maqayis)؛ درى يدري درية ودريا ودريانا ودراية (ayn)؛ دريته ودريت به أي علمت به وأدريته أي أعلمته (sihah)؛ أتى فلان الأمر من غير درية أي من غير علم (tahdhib)؛ الدراية المعرفة المدركة بضرب من الحيل (mufradat)
- **B002** saldırı amacıyla bir yer ya da kişiyi seçmek [kalıp] — bir yeri baskın veya saldırı için seçmek
  أصلان أحدهما قصد الشيء واعتماده طلبا (maqayis)؛ ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة (maqayis)؛ ادرأوا فلانا كأنهم اعتمدوه بالغارة والغزو (ayn)؛ بني فلان ادروا مكانا كأنهم اعتمدوه بالغزو والغارة (sihah)
- **B003** avın yerini gözetleyip gizlenerek onu aldatmak ve atış fırsatı bulmak — avcının ardına saklandığı ve avı ürkütmeden yaklaştırdığı hayvan · avı gizlenip aldatarak atış menziline getirmek · hileyle kandırmak
  الدرية الدابة التي يستتر بها الذي يرمي الصيد (maqayis)؛ تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته (maqayis)؛ الدريئة ما تتستر به فترمي الصيد وتقول منه دريت الصيد (ayn)؛ الدرية غير مهموز دابة يستتر بها الصائد (sihah)؛ تدراه وادراه بمعنى أي ختله (sihah)؛ دريت فلانا أدريه دريا إذا ختلته (tahdhib)؛ الدرية البعير يستتر به من الوحش (tahdhib)؛ الدرية للناقة التي ينصبها الصائد ليأنس بها الصيد (mufradat)
- **B004** sivri uç ve bundan ad alan saç düzeltme aracı — sivri boynuz; saçı düzeltmeye yarayan sivri araç · saçı ayırıp düzeltmeye yarayan şiş biçimli araç · saçını tarayıp düzeltmek
  الأصل الآخر حدة تكون في الشيء (maqayis)؛ مدرى لأنه محدد (maqayis)؛ شاة مدراة حديدة القرنين (maqayis)؛ تدرت المرأة إذا سرحت شعرها (maqayis;sihah)؛ المدريين طبيا الشاة لأنهما إذا امتلئا تحدد طرفاهما (maqayis)؛ المدرى القرن والمدراة شيء كالمسلة (sihah)؛ المدرى لقرن الشاة واستعير المدرى لما يصلح به الشعر (mufradat)
- **B005** saplama ve atış alıştırma hedefi — üzerinde saplama alıştırması yapılan hedef
  الدريئة الحلقة التي يتعلم عليها الطعن (maqayis)؛ الدريئة من أدم وغيره يتعلم عليها الطعان (ayn)؛ الدريئة بالهمز الحلقة (ayn)؛ الدريئة مهموزة الحلقة التي يتعلم الرامي عليها (tahdhib)؛ الدرية لما يتعلم عليه الطعن (mufradat)
- **B006** insanlarla yumuşak ve incelikli geçinmek [kalıp] — insanlara karşı yumuşak ve uzlaştırıcı davranmak
  مداراة الناس تهمز ولا تهمز وهي المداجاة والملاينة (sihah)؛ دارأت الرجل مدارأة إذا اتقيته (tahdhib)؛ المدارأة المشاغبة والمخالفة (tahdhib)؛ المداراة في حسن الخلق والمعاشرة مع الناس (tahdhib)

## ل ي ل (root_001392) — identity root of لَيْلَةُ (w4)

- **B001** gündüzün karşıtı olan gece ve onun karanlığı — gündüzün karşıtı olan gece · gece karanlığı · tek bir gece · geceler · geceler · geceler · çok karanlık ve çetin gece · çok karanlık gece · uzun ya da şiddeti pekiştirilmiş gece · ayın en karanlık ve son gecesi
  الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)
- **B002** geceye girme ya da geceleyin iş görüp yol alma — geceye göre karşılıklı işlem yapma · geceye girmek · gece yol alan veya gece yolculuğuna dayanabilen kimse
  عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)
- **B003** bugüne göre belirlenen en yakın gece — bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece
  إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)
- **B004** bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı — bir kadın adı · şarap için kullanılan örtülü ad
  وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)

## ق د ر (root_001205) — identity root of ٱلْقَدْرِ (w5)

- **B001** bir şeyin ölçüsü ve eriştiği sınır — bir şeyin ölçüsü, niceliği ve sınırı · belirlenmiş ölçü, sınır veya süre
  مبلغ الشيء وكنهه ونهايته (maqayis)؛ القدر مبلغ الشيء؛ لكل شيء مقدار وأجل (ayn)؛ قدر الشيء مبلغه (sihah)؛ المقدار هو الهنداز؛ ينزل المطر بمقدار (tahdhib)؛ القدر والتقدير تبيين كمية الشيء (mufradat)
- **B002** Tanrı'nın varlıkları ölçülü biçimde hükme bağlaması — Tanrı'nın varlıklar için belirlediği ölçülü hüküm · Tanrısal belirlemeyi reddetmekle anılan topluluk · belirli işlere ayrılmış özel gece
  قضاء الله تعالى الأشياء على مبالغها ونهاياتها (maqayis)؛ القدر القضاء الموفق؛ قدره الله تقديرا (ayn;tahdhib)؛ ما يقدره الله عزوجل من القضاء (sihah)؛ يجعلها على مقدار مخصوص ووجه مخصوص حسبما اقتضت الحكمة (mufradat)
- **B003** bir şeyi yapmaya veya ona egemen olmaya elveren güç — bir işi yapmaya elveren güç ve yetkinlik · gücü yeten ve yapabilen · dilediğini gerçekleştirecek ölçüde güçlü · gücü olan veya güç edinmiş · varlıklı ve geniş olanaklı
  قدرة الله تعالى على خليقته؛ رجل ذو قدرة وذو مقدرة أي يسار (maqayis)؛ قدر على الشيء قدرة أي ملك فهو قادر (ayn;tahdhib)؛ الاقتدار على الشيء القدرة عليه؛ رجل ذو قدرة أي ذو يسار (sihah)؛ القدرة إذا وصف بها الإنسان فاسم لهيئة له بها يتمكن (mufradat)
- **B004** birinin geçim payını kısmak [kalıp] — onun geçim payını kıstı · onu darlığa sokarız
  من قدر عليه رزقه فمعناه قتر (maqayis)؛ قدر على عياله مثل قتر؛ قدر على الإنسان رزقه مثل قتر (sihah)؛ نضيق عليه؛ ضيق عليه (tahdhib)؛ قدرت عليه الشيء ضيقته؛ ومن قدر عليه رزقه أي ضيق عليه (mufradat)
- **B005** ölçüp biçerek tasarlamak ve hazırlamak — ölçüsünü belirleyip hazırladı · ayın gün sayısını hesaplayıp otuza tamamlayın · örgülü işi düzgün ve sağlam kurdu · o şey onun için hazır duruma geldi
  اقتدرت الشيء جعلته قدرا؛ قدرت الشيء أي هيأته (ayn)؛ فاقدروا له أي أتموا ثلاثين؛ تقدر له الشيء أي تهيأ (sihah)؛ التروية والتفكير في تسوية أمر وتهيئته؛ نظرت فيه ودبرته وقايسته؛ قدر في السرد أي أحكمه (tahdhib)؛ التقدير من الإنسان التفكر في الأمر؛ فكر وقدر؛ قدر في السرد أي أحكمه (mufradat)
- **B006** söz öbeğine göre ölçüye uygun, orta veya yapıca ölçülü olma [kalıp] — ölçüsüne uydu ve tam denk geldi · orta büyüklükte eyer · orta boylu adam · kısa boyunlu veya kısa adam · arka ayaklarını ön ayak izlerine basan at · yol alması kolay gece
  جاء على قدره؛ المقتدر الوسط؛ سرج قدر أي وسط (ayn)؛ بين أرضك وأرض فلان ليلة قادرة؛ الأقدر القصير؛ الأقدار من الخيل (sihah)؛ كل شيء مقتدر فهو الوسط؛ القدر من الرحال والسروج الوسط؛ الأقدر من الرجال القصير العنق؛ الأقدر من الخيل (maqayis;tahdhib)؛ الأقدر القصير العنق؛ فرس أقدر (mufradat)
- **B007** pişirme kabı ve ona bağlı yemek, pişirme işi ve görevli sözleri — et veya yemek pişirme tenceresi · tencerede pişmiş et veya yemek · pişmiş çorba suyu · topluluk tencerede yemek pişirdi · hayvanı kesip etini pişiren kasap veya aşçı
  القدر وهي معروفة؛ القدير اللحم يطبخ في القدر؛ القدار الجزار ويقال الطباخ (maqayis)؛ القدير ما طبخ من اللحم؛ مرق مقدور؛ القدار الطباخ (ayn)؛ القدير المطبوخ في القدر؛ القدار الجزار ويقال الطباخ (sihah)؛ القدر مؤنثة؛ قدرت القدر إذا طبخت قدرا؛ القدار الجزار (tahdhib)؛ القدر اسم لما يطبخ فيه اللحم؛ قدرت اللحم طبخته؛ القدار الذي ينحر ويقدر (mufradat)

## ECHO د ر ر (root_000469) — for أَدْرَىٰكَ (w2): withheld observed target; not identity

- **B001** bir kaynaktan bolca çıkma veya bol ürün verme — sütün memeden çıkıp akması · süt · bol sütlü dişi deve · bulutun yağmur boşaltması · bol yağmur getiren · gözünden yaş akması · damarların kanla dolması · Ne güzel iş ve iyilik! · İyiliği artmasın! · vergi gelirinin artması · pazarın canlanması · dişi keçilerin teke istemesi · sütün bolluğu veya akışı
  الدر در اللبن (maqayis;jamhara;sihah;tahdhib;mufradat)؛ در السحاب بالمطر ودرت السماء وسحابة مدرار (maqayis;jamhara;sihah;tahdhib;mufradat)؛ لله دره ولا در دره أي خيره أو عمله (maqayis;jamhara;sihah;tahdhib;mufradat)؛ در الخراج وحلوبة المسلمين وللسوق درة (maqayis;jamhara;sihah;tahdhib;mufradat)؛ استدرت المعزى إذا أرادت الفحل (maqayis;sihah;tahdhib;mufradat)
- **B002** hızlı, güçlü ve akıcı koşma — çok hızlı koşan binek hayvanı · atın hızlı ve rahat koşması · bacakta güçlü koşma yetisi · atın tırıs sırasında ön ayağını kaldırıp indirdiği yürüyüş biçimi
  الدرير من الدواب الشديد العدو السريعة (maqayis)؛ در الفرس دريرا إذا عدا عدوا شديدا سهلا (jamhara)؛ فرس درير أي سريع (sihah)؛ در الفرس درة فهو درير إذا أسرع في عدوه والإدرار في الخيل (tahdhib)
- **B003** gevşekçe sallanma veya tekrar tekrar gidip gelme — diş yuvaları; kimi kullanımda dil ucu · çocuğun bir şeyi ağzında çevirip çiğnemesi · sallanıp oynamak · dişleri dökülüp diş yuvaları görünmek · gereksiz yere gidip gelen kimse
  الدردر منابت أسنان الصبي ومن تدردرت اللحمة إذا اضطربت ودردر الصبي الشيء إذا لاكه (maqayis)؛ الدردر مغارز أسنان الصبي ودردر الصبي البسرة لاكها (sihah)؛ تدردر أي تمرمر وترجرج والدردر مغرز السن وطرف اللسان والدردرى الذي يذهب ويجيء في غير حاجة (tahdhib)
- **B004** doğrultu, yön veya karşı karşıya hizalanma — yolun doğrultusu veya güzergâhı · rüzgârın esiş yönü · tam karşında veya hizanda
  درر الريح مهبها ودرر الطريق قصده (maqayis)؛ هما على درر واحد ونحن على درر الطريق ودرر الريح مهبها (sihah)؛ فلان دررك أي قبالتك وعلى درر الطريق أي مدرجته وداري بدرر دارك أي بحذائها (tahdhib)
- **B005** iri inci; inci gibi beyaz ve parlak yıldız — iri inciler veya inci topluluğu · iri inci; tek bir inci · inci gibi beyaz ve parlak yıldız
  الدر كبار اللؤلؤ والكوكب الدري الثاقب المضيء (maqayis)؛ الدرة ما عظم من اللؤلؤ (jamhara)؛ الدرة اللؤلؤة والكوكب الدري الثاقب المضيء نسب إلى الدر لبياضه (sihah)؛ الدر العظام من اللؤلؤ والكوكب الدري الثاقب المضيء (tahdhib)
- **B006** özellikle yöneticinin kullandığı vurma değneği — özellikle yöneticinin kullandığı vurma değneği
  الدرة التي يضرب بها عربية معروفة (jamhara)؛ الدرة التي يضرب بها (sihah)؛ الدرة درة السلطان التي يضرب بها (tahdhib)
- **B007** ipliği sıkı bükmek için iği döndürme — ipliği sıkı bükmek için iği veya dönen parçasını çevirmek
  أدرت المرأة المغزل إذا فتلته فتلا شديدا فهي مدر والمغزل مدر (jamhara)؛ أدرت الغزالة درارتها إذا أدارتها لتستحكم قوة ما تغزله (tahdhib)
- **B008** gemiyi tehlikeye atan çalkantılı deniz girdabı — girdap; gemiyi tehlikeye atan çalkantılı deniz yeri
  الدردور الماء الذي يدور ويخاف فيه الغرق (sihah)؛ الدردور موضع من البحر يجيش ماؤه وقلما تسلم السفينة منه (tahdhib)

===== _commentary/v16/out/s097/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 97:2, and ## Buluşmalar) =====
## Gece, ay ve bin: bir gecenin tartılması

Üçüncü ayet bir geceyi bin ayla karşılaştırır: {ar:لَيْلَةُ ٱلْقَدْرِ خَيْرٌۭ مِّنْ أَلْفِ شَهْرٍۢ, tr:leyletü'l-kadri hayrun min elfi şehr, gloss:Kadir gecesi bin aydan hayırlıdır, source:97:3}. Ayetin her kelimesi, ay hesabıyla zaman sayan Arapçanın sayma diline aittir. Gece, sayılan bir birimdir: {ar:ليل وليلة وليلات وليال, tr:leylün ve leyletün ve leylâtün ve leyâl, gloss:gece, bir gece, geceler, source:"ل ي ل,B001"}. Ay önce hilalin adıdır, sonra otuz günlük süreye ad olur: {ar:الشهر الهلال ثم سمي كل ثلاثين يوما باسم الهلال, tr:eş-şehru'l-hilâl, sümme summiye küllü selâsîne yevmen bi'smi'l-hilâl, gloss:şehr hilaldir; sonra her otuz güne hilalin adı verildi, source:"ش ه ر,B001"}. Bu süre, hilalin görünmesiyle bilinir: {ar:مدة مشهورة بإهلال الهلال, tr:müddetün meşhûretün bi-ihlâli'l-hilâl, gloss:hilalin doğmasıyla bilinen bir süre, source:"ش ه ر,B001"}. Ay kelimesi bir sayma kelimesidir: {ar:الشهر والأشهر عدد والشهور جماعة, tr:eş-şehru ve'l-eşhuru 'adedün ve'ş-şühûru cemâ'a, gloss:şehr ve eşhur sayıdır, şühûr topluluktur, source:"ش ه ر,B001"}. Bin belirli bir sayıdır ve bir toplamı bine çıkarmanın fiili de vardır: {ar:الألف العدد المخصوص, tr:el-elfu'l-'adedü'l-mahsûs, gloss:elf, belirli bir sayıdır, source:"ء ل ف,B001"}; {ar:آلفت الدراهم أي بلغت بها الألف, tr:âleftü'd-derâhime ey belağtü biha'l-elf, gloss:dirhemleri bine tamamladım, yani bine ulaştırdım, source:"ء ل ف,B001"}. Bu fiilin tarifinde geçen ulaşma kelimesi, kadrin tarifinde de geçer: {ar:قدر الشيء مبلغه, tr:kadru'ş-şey'i meblağuhû, gloss:bir şeyin kadri, vardığı miktardır, source:"ق د ر,B001"}; {ar:القدر والتقدير تبيين كمية الشيء, tr:el-kadru ve't-takdîru tebyînü kemmiyyeti'ş-şey', gloss:kadr ve takdir, bir şeyin miktarını ortaya koymaktır, source:"ق د ر,B001"}. Ayın sayımı da bu kökle yapılır: {ar:فاقدروا له أي أتموا ثلاثين, tr:fe'kdurû lehû ey etimmû selâsîn, gloss:"onun için takdir edin", yani otuza tamamlayın, source:"ق د ر,B005"}.

Bu dille okunduğunda üçüncü ayet bir toplamdır. Bin ayın her biri hilalden hilale kadar sayılan otuz gecedir, yani bin ay otuz bin kadar gece eder. Tek bir gece bunların hepsinden ağır basar. Kadr kelimesi ölçü ve miktar olduğu için gecenin kendi ölçüsü sayılan sürenin ölçüsünü aşar. Karşılaştırmayı taşıyan kelime hayırdır. Bu kelime her türün en seçkinini de anlatır: {ar:الخيرات جمع خيرة وهي الفاضلة من كل شيء, tr:el-hayrâtü cem'u hayretin ve hiye'l-fâdıletü min külli şey', gloss:hayrât, hayrenin çoğuludur; o da her şeyin en üstünüdür, source:"خ ي ر,B002"}. Seçmek de aynı köktendir: {ar:الاختيار طلب ما هو خير وفعله, tr:el-ihtiyâru talebü mâ hüve hayrun ve fi'lühû, gloss:ihtiyar, daha hayırlı olanı istemek ve onu yapmaktır, source:"خ ي ر,B003"}. Karşılaştırma bir seçimdir ve gece aylara tercih edilir. İndirmenin kökünden gelen menzile de rütbe demektir: {ar:المنزلة المرتبة, tr:el-menziletü'l-mertebe, gloss:menzile, mertebedir, source:"ن ز ل,B003"}.

Gece ile ay Arapçanın kendi sözünde birleşir: {ar:ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه, tr:leyletün leylâ eşeddü leyletin fi'ş-şehri zulmeten ve âhiru leyletin fîh, gloss:"leyletün leylâ", ayın en karanlık ve en son gecesidir, source:"ل ي ل,B001"}. Hilalin gizlendiği o karanlık gece, sayımın bittiği yerdir. "Bu gece" sözü de içinde bulunulan günün ardından gelen geceyi gösterir ve hilalin görüldüğü gece olarak anılır: {ar:هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه, tr:hâzihi'l-leyletü'lletî fi's-semâ'i akrabu'l-leyâlî min yevmike ve hiye'l-leyletü'lletî telîh, gloss:gökteki bu gece, gününe en yakın gecedir; onu izleyen gecedir, source:"ل ي ل,B003"}; {ar:الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار, tr:el-hilâlü fî hâzihi'l-leyleti'lletî fi's-semâ', ya'ni'l-leyleta'lletî tedhulühâ, yütekellemu bi-hâzâ fi'n-nehâr, gloss:hilal gökteki bu gecededir, yani gireceğin gecede; bu söz gündüz söylenir, source:"ل ي ل,B003"}. Sayımın sabit noktaları da aynı sözlerle anılır: {ar:الأمارة الموعد، والأمارة العلامة, tr:el-emâretü'l-mev'id, ve'l-emâretü'l-'alâme, gloss:emâre buluşma vaktidir, emâre işarettir, source:"ء م ر,B005"}. Doğuşlar da sayımın işaretleridir: {ar:طلعت الشمس؛ وكذلك طلع الفجر والنجم والقمر, tr:tala'ati'ş-şems; ve kezâlike tala'a'l-fecru ve'n-necmü ve'l-kamer, gloss:güneş doğdu; şafak, yıldız ve ay için de "doğdu" denir, source:"ط ل ع,B001"}.

Kur'an ay ve hesabı aynı kelimelerle kurar. Yûnus suresinde Allah {ar:وَٱلْقَمَرَ نُورًۭا وَقَدَّرَهُۥ مَنَازِلَ لِتَعْلَمُوا۟ عَدَدَ ٱلسِّنِينَ وَٱلْحِسَابَ, tr:ve'l-kamera nûran ve kaddarahû menâzile li-ta'lemû 'adede's-sinîne ve'l-hisâb, gloss:ayı bir ışık kıldı ve ona konaklar takdir etti ki yılların sayısını ve hesabı bilesiniz, source:10:5} der. Ölçünün kökü ile indirmenin kökü, ayın konaklarında yan yana gelir: menâzil, nezele kökündendir. Yâsîn suresinde gecenin, gündüz ondan sıyrılıp alınan bir işaret olduğu söylendikten sonra {source:36:37} şöyle denir: {ar:وَٱلْقَمَرَ قَدَّرْنَٰهُ مَنَازِلَ حَتَّىٰ عَادَ كَٱلْعُرْجُونِ ٱلْقَدِيمِ, tr:ve'l-kamera kaddernâhu menâzile hattâ 'âde ke'l-'urcûni'l-kadîm, gloss:aya da konaklar takdir ettik; sonunda eski hurma salkımının sapı gibi olur, source:36:39}. Orada da döngünün sonunu "hattâ" çizer. İsrâ suresi gece ile gündüzü sayım için iki işaret yapar: {ar:لِتَعْلَمُوا۟ عَدَدَ ٱلسِّنِينَ وَٱلْحِسَابَ, tr:li-ta'lemû 'adede's-sinîne ve'l-hisâb, gloss:yılların sayısını ve hesabı bilesiniz diye, source:17:12}. Bakara suresinde hilaller sorulur: {ar:يَسْـَٔلُونَكَ عَنِ ٱلْأَهِلَّةِ ۖ قُلْ هِىَ مَوَٰقِيتُ لِلنَّاسِ وَٱلْحَجِّ, tr:yes'elûneke 'ani'l-ehilleh, kul hiye mevâkîtü li'n-nâsi ve'l-hacc, gloss:sana hilalleri sorarlar; de ki: onlar insanlar ve hac için vakit ölçüleridir, source:2:189}. Tevbe suresi ayların sayısını Allah'ın kitabına bağlar: {ar:إِنَّ عِدَّةَ ٱلشُّهُورِ عِندَ ٱللَّهِ ٱثْنَا عَشَرَ شَهْرًۭا فِى كِتَٰبِ ٱللَّهِ, tr:inne 'iddete'ş-şühûri 'inda'llâhi'snâ 'aşera şehran fî kitâbi'llâh, gloss:Allah katında ayların sayısı, Allah'ın kitabında on iki aydır, source:9:36}. Oruç hükmünde Kur'an, indirişi bir aya yerleştirir ve sayının tamamlanmasını emreder: {ar:شَهْرُ رَمَضَانَ ٱلَّذِىٓ أُنزِلَ فِيهِ ٱلْقُرْءَانُ, tr:şehru ramadâne'llezî ünzile fîhi'l-Kur'ân, gloss:Kur'an'ın içinde indirildiği Ramazan ayı, source:2:185}; {ar:وَلِتُكْمِلُوا۟ ٱلْعِدَّةَ, tr:ve li-tükmilü'l-'iddeh, gloss:sayıyı tamamlamanız için, source:2:185}. Surenin ilk ayetindeki "içinde indirdik" sözü burada bir ayın içine yerleşir.

Kur'an başka yerlerde de kısa bir süreyi uzun bir sayımla karşılaştırır. Azabın acele istenmesine verilen cevapta {ar:وَإِنَّ يَوْمًا عِندَ رَبِّكَ كَأَلْفِ سَنَةٍۢ مِّمَّا تَعُدُّونَ, tr:ve inne yevmen 'inde rabbike ke-elfi senetin mimmâ te'uddûn, gloss:Rabbinin katında bir gün, sizin saydıklarınızdan bin yıl gibidir, source:22:47} denir. Secde suresinde emrin inip çıkışı ölçü kelimesiyle anlatılır: {ar:فِى يَوْمٍۢ كَانَ مِقْدَارُهُۥٓ أَلْفَ سَنَةٍۢ مِّمَّا تَعُدُّونَ, tr:fî yevmin kâne mikdâruhû elfe senetin mimmâ te'uddûn, gloss:ölçüsü sizin saydıklarınızdan bin yıl olan bir günde, source:32:5}. Me'âric suresinde melekler ile Ruh'un yükselişi için {ar:كَانَ مِقْدَارُهُۥ خَمْسِينَ أَلْفَ سَنَةٍۢ, tr:kâne mikdâruhû hamsîne elfe seneh, gloss:ölçüsü elli bin yıl olan, source:70:4} denir. Bu pasajlarda Rab katındaki tek bir süre insan sayımının binleriyle ölçülür. Kadir suresi aynı karşılaştırmayı tersinden kurar: insanın içinde yaşadığı tek bir gece, sayılmış bin aydan ağır gelir. Gece namazı pasajında Allah'ın geceyi ölçtüğü ve önceden gönderilen hayrın daha hayırlı bulunacağı söylenir: {ar:وَٱللَّهُ يُقَدِّرُ ٱلَّيْلَ وَٱلنَّهَارَ, tr:va'llâhu yukaddiru'l-leyle ve'n-nehâr, gloss:geceyi ve gündüzü Allah ölçer, source:73:20}; {ar:وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍۢ تَجِدُوهُ عِندَ ٱللَّهِ هُوَ خَيْرًۭا, tr:ve mâ tükaddimû li-enfüsiküm min hayrin tecidûhü 'inda'llâhi hüve hayrâ, gloss:kendiniz için önden gönderdiğiniz her hayrı Allah katında daha hayırlı olarak bulursunuz, source:73:20}. Ölçü, gece ve hayır orada da bir aradadır.

Sure bu hesabı ayet ayet kurar. Birinci ayet sayılacak birimi koyar: bir gece ve onun ölçüsü. İkinci ayet aynı adı tekrarlar ve gelecek geceyi gösteren bu sözle soruyu bir ölçüye yöneltir. Üçüncü ayet toplamı yapar: bir gece, bin ay, aradaki fark hayırla ifade edilir. Dördüncü ayetteki emir kelimesinin vakit ve işaret anlamı, hesabın sabit noktalarını hatırlatır. Beşinci ayet sayımı bir doğuşta durdurur. Gece, şafağın doğduğu anda tamamlanmış olur.

Kaynaklar: 97:1 لَيْلَةِ ل ي ل B001; 97:2 لَيْلَةُ ل ي ل B003; 97:3 شَهْرٍ ش ه ر B001; 97:3 أَلْفِ ء ل ف B001; 97:1 ٱلْقَدْرِ ق د ر B005; 97:1 ٱلْقَدْرِ ق د ر B001; 97:3 خَيْرٌۭ خ ي ر B002; 97:3 خَيْرٌۭ خ ي ر B003; 97:1 أَنزَلْنَٰهُ ن ز ل B003; 97:4 أَمْرٍ ء م ر B005; 97:5 مَطْلَعِ ط ل ع B001

## Örtülü olan ve görünüre çıkan

İkinci ayet bir soru sorar: {ar:وَمَآ أَدْرَىٰكَ مَا لَيْلَةُ ٱلْقَدْرِ, tr:ve mâ edrâke mâ leyletü'l-kadr, gloss:Kadir gecesinin ne olduğunu sana ne bildirdi, source:97:2}. Kök, bilmeyi ve Allah'ın bildirmesini birlikte taşır: {ar:دريت الشيء والله أدرانيه, tr:dereytü'ş-şey'e va'llâhu edrânîh, gloss:o şeyi bildim, onu bana Allah bildirdi, source:"د ر ي,B001"}. Soru, bilgiyi kimin verdiğini sorar. Bu kökten gelen bilgi bir tür ustalıkla elde edilir: {ar:الدراية المعرفة المدركة بضرب من الحيل, tr:ed-dirâyetü'l-ma'rifetü'l-müdrekeü bi-darbin mine'l-hiyel, gloss:dirâyet, bir çeşit ustalık ve hileyle ulaşılan bilgidir, source:"د ر ي,B001"}. Soru, bu gecenin insanın kendi çabasıyla çözülemeyeceğini söyler. Aynı ailenin başka bir kolu avcılığı anlatır: {ar:تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته, tr:tedereytü's-sayde izâ nazartü eyne hüve ve lem terahü ba'd, ve dereytühû hateltühû, gloss:avın nerede olduğuna, henüz görmeden bakındığımda "tedereytü" derim; "dereytühû", onu sinsice yakaladım demektir, source:"د ر ي,B003"}; {ar:الدرية الدابة التي يستتر بها الذي يرمي الصيد, tr:ed-diriyyetü'd-dâbbetü'lletî yesteteru bihe'llezî yermi's-sayd, gloss:diriyye, avcının arkasına saklandığı hayvandır, source:"د ر ي,B003"}. Avcı hayvanın arkasına gizlenir ve henüz görmediği avı gözetler. Bu imge sorunun yanında duyulur: gece, avcının ustalığının göremediği bir şeydir.

Kur'an bu soru kalıbını başka şeyler için de kullanır, ve çoğu zaman ardından bilgiyi kendisi verir. Beled suresinde {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْعَقَبَةُ, tr:ve mâ edrâke me'l-'akabe, gloss:o sarp yokuşun ne olduğunu sana ne bildirdi, source:90:12} diye sorar ve hemen cevap verir: {ar:فَكُّ رَقَبَةٍ, tr:fekkü rakabe, gloss:bir boynu esaretten kurtarmak, source:90:13}. Müddessir suresinde {ar:وَمَآ أَدْرَىٰكَ مَا سَقَرُ, tr:ve mâ edrâke mâ sakar, gloss:Sakar'ın ne olduğunu sana ne bildirdi, source:74:27} sorusunun ardından {ar:لَا تُبْقِى وَلَا تَذَرُ, tr:lâ tübkî ve lâ tezer, gloss:ne bırakır ne geride koyar, source:74:28} gelir. Kâria suresinde {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْقَارِعَةُ, tr:ve mâ edrâke me'l-kâri'a, gloss:o kapıyı çalanın ne olduğunu sana ne bildirdi, source:101:3} sorusunun ardından {ar:يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ, tr:yevme yekûnü'n-nâsü ke'l-ferâşi'l-mebsûs, gloss:insanların dağılmış pervaneler gibi olacağı gün, source:101:4} gelir. Aynı kalıp İnfitâr suresinde iki kez tekrarlanır: {ar:وَمَآ أَدْرَىٰكَ مَا يَوْمُ ٱلدِّينِ, tr:ve mâ edrâke mâ yevmü'd-dîn, gloss:din gününün ne olduğunu sana ne bildirdi, source:82:17}; {ar:ثُمَّ مَآ أَدْرَىٰكَ مَا يَوْمُ ٱلدِّينِ, tr:sümme mâ edrâke mâ yevmü'd-dîn, gloss:sonra, din gününün ne olduğunu sana ne bildirdi, source:82:18}. Hâkka suresi de {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْحَآقَّةُ, tr:ve mâ edrâke me'l-hâkka, gloss:o gerçekleşecek olanın ne olduğunu sana ne bildirdi, source:69:3} diye sorar. Kadir suresinde de cevap hemen gelir: üçüncü, dördüncü ve beşinci ayetler gecenin ne olduğunu söyler. Sorunun "sana ne bildirdi" dediği bilgiyi sure kendisi verir. Bildiren, surenin ilk ayetinde "biz" diye konuşandır. Şûrâ suresi bunu açıkça söyler: emirden bir ruh vahyedilmeden önce elçi bilmiyordu: {ar:مَا كُنتَ تَدْرِى مَا ٱلْكِتَٰبُ وَلَا ٱلْإِيمَٰنُ, tr:mâ künte tedrî me'l-kitâbü ve le'l-îmân, gloss:kitap nedir, iman nedir bilmiyordun, source:42:52}.

Gece de bu sahnede örtüdür. {ar:ظلام الليل, tr:zalâmü'l-leyl, gloss:gecenin karanlığı, source:"ل ي ل,B001"} sözü örten karanlığı anlatır. Kur'an da geceyi bir giysi yapar: {ar:وَجَعَلْنَا ٱلَّيْلَ لِبَاسًۭا, tr:ve ce'alne'l-leyle libâsâ, gloss:geceyi bir örtü kıldık, source:78:10}. Dördüncü ayetteki izin kelimesi bilgiyi de taşır: {ar:بإذن الله أي بعلمه, tr:bi-izni'llâhi ey bi-'ilmih, gloss:Allah'ın izniyle, yani bilgisiyle, source:"ء ذ ن,B004"}. Bu kökün bir kolu doğrudan bildirmektir: {ar:الأصل الآخر العلم والإعلام؛ آذنني فلان أعلمني, tr:el-aslü'l-âharu'l-'ilmü ve'l-i'lâm; âzenenî fülânun a'lemenî, gloss:öbür asıl bilmek ve bildirmektir; "falan bana âzene", yani bana bildirdi, source:"ء ذ ن,B003"}; {ar:المؤذن كل من يعلم بشيء نداء, tr:el-mü'ezzinü küllü men yu'limu bi-şey'in nidâ'en, gloss:müezzin, bir şeyi seslenerek bildiren herkestir, source:"ء ذ ن,B003"}. İkinci ayet dinleyicinin bilmediğini söyler, dördüncü ayet ise inişin bilgiyle ve izinle olduğunu bildirir. Kur'an indirmeyi ve bilgiyi Nisâ suresinde birleştirir: {ar:أَنزَلَهُۥ بِعِلْمِهِۦ ۖ وَٱلْمَلَٰٓئِكَةُ يَشْهَدُونَ, tr:enzelehû bi-'ilmih, ve'l-melâiketü yeşhedûn, gloss:onu kendi bilgisiyle indirdi; melekler de şahitlik eder, source:4:166}. Cin suresinin sonunda gaybı bilen, gaybını kimseye göstermez {ar:عَٰلِمُ ٱلْغَيْبِ فَلَا يُظْهِرُ عَلَىٰ غَيْبِهِۦٓ أَحَدًا, tr:'âlimü'l-gaybi fe-lâ yuzhiru 'alâ gaybihî ehadâ, gloss:gaybı bilen O'dur; gaybını kimseye açmaz, source:72:26}, ancak razı olduğu bir elçi bunun dışındadır {ar:إِلَّا مَنِ ٱرْتَضَىٰ مِن رَّسُولٍۢ, tr:illâ meni'rtedâ min rasûl, gloss:razı olduğu bir elçi dışında, source:72:27}.

Ay kelimesinin ailesi açıklığı da taşır: {ar:الشهرة وضوح الأمر, tr:eş-şühretü vudûhu'l-emr, gloss:şöhret, bir işin açık olmasıdır, source:"ش ه ر,B002"}. Üçüncü ayetteki "ay", hilalle herkesin bildiği açık bir süredir. Gecenin değeri ise o açık sayımdan çıkarılamaz, ona üstün gelir. Sahnenin sonu bir görünür olmadır: matla' kelimesinin kökü {ar:ظهور وبروز, tr:zuhûrun ve burûz, gloss:görünme ve ortaya çıkma, source:"ط ل ع,B001"} anlamındadır. Aynı aile bir işin içine bakmayı da anlatır: {ar:اطلعت على باطن أمره, tr:ittala'tü 'alâ bâtını emrih, gloss:işinin içyüzüne vâkıf oldum, source:"ط ل ع,B003"}. Başını dışarı çıkarmak: {ar:أطلع فلان رأسه أظهره, tr:atla'a fülânun re'sehû ezharahû, gloss:falan başını çıkardı, yani gösterdi, source:"ط ل ع,B003"}. Bir görünüp bir gizlenmek: {ar:امرأة طلعة قبعة تظهر رأسها مرة وتستر أخرى, tr:imra'etün tula'atün kube'a, tuzhiru re'sehâ merraten ve testuru uhrâ, gloss:"tula'a kube'a" kadın, başını bir gösterip bir saklayandır, source:"ط ل ع,B008"}.

Ayetler sırayla bu imgeyi kurar. Birinci ayet gizli bir şey söyler: indirilenin adı yoktur ve indiriş karanlık bir zamana bırakılır. İkinci ayet bu gizliliği bir soru hâline getirir. Üçüncü ayet açık bir sayımla, yani ayla, gizli bir değeri karşılaştırır. Dördüncü ayet inişin bilgi ve izinle olduğunu söyler. Beşinci ayet örtüyü bir doğuşla, yani görünür olmayla kapatır.

Kaynaklar: 97:2 أَدْرَىٰكَ د ر ي B001; 97:2 أَدْرَىٰكَ د ر ي B003; 97:1 لَيْلَةِ ل ي ل B001; 97:4 بِإِذْنِ ء ذ ن B004; 97:4 بِإِذْنِ ء ذ ن B003; 97:3 شَهْرٍ ش ه ر B002; 97:5 مَطْلَعِ ط ل ع B001; 97:5 مَطْلَعِ ط ل ع B003; 97:5 مَطْلَعِ ط ل ع B008

## Geceleyin bir kavmin üstüne inen kalabalık: baskın değil esenlik

Dördüncü ayetin melekleri bir kalabalık olarak gelir. Melek kelimesi hem tekil hem çoğul olabilir: {ar:الملك من الملائكة واحد وجمع, tr:el-melekü mine'l-melâiketi vâhidün ve cem', gloss:meleklerden "melek" sözü hem tek hem çoğuldur, source:"م ل ك,B009"}. "Her" kelimesi tek bir sözde çokluğu tutar: {ar:كل لفظه واحد ومعناه جمع, tr:küllün lafzuhû vâhidun ve ma'nâhü cem', gloss:"kull"ün sözü tek, anlamı çoğuldur, source:"ك ل ل,B003"}. Aynı kökten bir kelime de bölükleri anlatır: {ar:الكلاكل من الجماعات كالكراكر من الخيل, tr:el-kelâkilü mine'l-cemâ'âti ke'l-kerâkiri mine'l-hayl, gloss:kelâkil, at sürüleri gibi insan bölükleridir, source:"ك ل ل,B009"}. Bir önceki ayetteki bin kelimesinin bir topluluğu bin kişiye tamamlamayı anlatan fiili vardır: {ar:آلفت القوم صيرتهم ألفا, tr:âleftü'l-kavme sayyartühüm elfâ, gloss:topluluğu bine tamamladım, source:"ء ل ف,B001"}; {ar:الألف عدد والجمع ألوف وآلاف, tr:el-elfü 'adedün ve'l-cem'u ülûfün ve âlâf, gloss:bin bir sayıdır, çoğulu ülûf ve âlâf, source:"ء ل ف,B001"}. Rab kelimesinin kökü de binlerce kişiyi anlatır: {ar:الربي: واحد الربيين، وهم الألوف من الناس, tr:er-ribbiyyü vâhidü'r-ribbiyyîn, ve hümü'l-ülûfü mine'n-nâs, gloss:ribbî, ribbiyyûnun tekilidir; onlar binlerce insandır, source:"ر ب ب,B004"}; {ar:الربيون: الألوف؛ الربيون: الجماعات الكثيرة؛ الربة: عشرة آلاف, tr:er-ribbiyyûn: el-ülûf; er-ribbiyyûn: el-cemâ'âtü'l-kesîre; er-ribbetü: 'aşeretü âlâf, gloss:ribbiyyûn binlerdir, kalabalık topluluklardır; ribbe on bindir, source:"ر ب ب,B004"}. Doğuşun kökü de yeryüzünü dolduracak kadar bir miktarı anlatır: {ar:طلاع الأرض ملؤها حتى يطالع أعلى الأرض؛ طلاع الأرض ما طلعت عليه الشمس, tr:tılâ'u'l-ardı mil'uhâ hattâ yütâli'a a'le'l-ard; tılâ'u'l-ardı mâ tala'at 'aleyhi'ş-şems, gloss:tılâ'u'l-ard, yerin en üstüne erişecek kadar yerin doluşudur; güneşin üzerine doğduğu her yerdir, source:"ط ل ع,B007"}. Bu kelimelerin yanında gece, gökten yere kadar, binlerle sayılan ve sayıyı aşan bir kalabalıkla dolar.

Kur'an melekleri tam da böyle, binlerce ve "indirilmiş" olarak sahneler. Elçi, savaştan önce müminlere şöyle der: {ar:أَلَن يَكْفِيَكُمْ أَن يُمِدَّكُمْ رَبُّكُم بِثَلَٰثَةِ ءَالَٰفٍۢ مِّنَ ٱلْمَلَٰٓئِكَةِ مُنزَلِينَ, tr:e-len yekfiyeküm en yümiddeküm rabbüküm bi-selâseti âlâfin mine'l-melâiketi münzelîn, gloss:Rabbinizin size indirilmiş üç bin melekle yardım etmesi yetmez mi, source:3:124}. Ardından {ar:يُمْدِدْكُمْ رَبُّكُم بِخَمْسَةِ ءَالَٰفٍۢ مِّنَ ٱلْمَلَٰٓئِكَةِ مُسَوِّمِينَ, tr:yümdidküm rabbüküm bi-hamseti âlâfin mine'l-melâiketi müsevvimîn, gloss:Rabbiniz size nişanlı beş bin melekle yardım eder, source:3:125} der. Rab, bin, melek ve inmek orada tek satırda bir aradadır. Enfâl suresinde müminlerin yardım çağrısına cevap verilir: {ar:أَنِّى مُمِدُّكُم بِأَلْفٍۢ مِّنَ ٱلْمَلَٰٓئِكَةِ مُرْدِفِينَ, tr:ennî mümiddüküm bi-elfin mine'l-melâiketi mürdifîn, gloss:size birbiri ardınca gelen bin melekle yardım edeceğim, source:8:9}. Âl-i İmrân suresi ribbiyyûn kelimesini kullanır: {ar:وَكَأَيِّن مِّن نَّبِىٍّۢ قَٰتَلَ مَعَهُۥ رِبِّيُّونَ كَثِيرٌۭ, tr:ve ke-eyyin min nebiyyin kâtele me'ahû ribbiyyûne kesîr, gloss:nice peygamber vardır ki onunla birlikte pek çok kalabalık savaştı, source:3:146}.

Bu kalabalığın gece bir kavmin üzerine inmesi, Arapçada başka bir sahneyi de çağırır. Bir kuvvet gece yol alır, bir topluluğun yurduna iner ve ilk ışıkta vurur. Surenin kelime ailelerinde bu sahnenin her parçası vardır. İnmek kökü, bir kavmin üzerine inen ağır felaketi anlatır: {ar:النازلة الشديدة من شدائد الدهر تنزل بالقوم وجمعها النوازل, tr:en-nâziletü'ş-şedîdetü min şedâ'idi'd-dehri tenzilü bi'l-kavm ve cem'uhe'n-nevâzil, gloss:nâzile, zamanın sıkıntılarından bir kavmin üzerine inen ağır bir felakettir; çoğulu nevâzil, source:"ن ز ل,B006"}. Savaşmak için iki tarafın binekten inmesini anlatır: {ar:النزال المنازلة في الحرب أن ينزلا معا فيقتتلا, tr:en-nizâlü'l-münâzeletü fi'l-harbi en yenzilâ me'an fe-yaktetilâ, gloss:nizâl, savaşta iki tarafın birlikte inip çarpışmasıdır, source:"ن ز ل,B007"}. Bir savaş çağrısı da bu köktendir: {ar:نزال أي انزلوا للحرب, tr:nezâli ey inzilû li'l-harb, gloss:"nezâli", yani savaşmak için inin, source:"ن ز ل,B007"}. Fecr kökü, ansızın bastıran kalabalığı ve felaketleri anlatır: {ar:انفجر عليهم القوم وانفجرت عليهم الدواهي إذا جاءهم الكثير منها بغتة, tr:infecera 'aleyhimü'l-kavmü ve'nfeceret 'aleyhimü'd-devâhî izâ câ'ehümü'l-kesîru minhâ bağteten, gloss:topluluk onların üstüne patladı, felaketler üzerlerine patladı; yani çoğu ansızın geldi, source:"ف ج ر,B003"}. Doğuş kökü saldırarak görünmeyi anlatır: {ar:طلع علينا فلان يطلع طلوعا إذا هجم, tr:tala'a 'aleynâ fülânun yatlu'u tulû'an izâ hecem, gloss:falan üstümüze çıkageldi, yani saldırdı, source:"ط ل ع,B002"}. Ordunun öncü gözcüsünü de bu kök adlandırır: {ar:طليعة الجيش من يبعث ليطلع طلع العدو, tr:talî'atü'l-ceyşi men yüb'asü li-yettali'a tal'a'l-'aduvv, gloss:ordunun talîası, düşmanın durumunu öğrenmek için gönderilendir, source:"ط ل ع,B004"}. Yüksek bir yerden aşağı bakmanın dehşeti de bu köktendir: {ar:هول المطلع, tr:hevlü'l-muttala', gloss:bakılan yerin dehşeti, source:"ط ل ع,B006"}. Bilmek kökünde, baskın için bir yer seçmek de vardır: {ar:ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة, tr:iddarâ benû fülânin mekâne kezâ ey i'temedûhü bi-ğazvin ev ğâra, gloss:falan oğulları falan yeri gözlerine kestirdi, yani oraya akın ya da baskın için yöneldi, source:"د ر ي,B002"}. Gece yürüyüşüne herkesin dayanamadığı da gece kökünde söylenir: {ar:لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل, tr:lestü bi-leyliyyin ve lâkinnî neharun ey esîru bi'n-nehâri ve lâ utîku sure'l-leyl, gloss:ben gece adamı değil gündüz adamıyım, yani gündüz yürürüm, gece yürüyüşüne dayanamam, source:"ل ي ل,B002"}. Ay kökü kılıç çekmeyi de anlatır: {ar:شهر سيفه إذا انتضاه فرفعه على الناس, tr:şehera seyfehû izâ'ntedâhü fe-refe'ahû 'ale'n-nâs, gloss:kılıcını çekip insanlara karşı kaldırdığında "şehera seyfehû" denir, source:"ش ه ر,B003"}.

Bütün bunların karşısında surenin kelimesi selâmdır. Bu kelime zarardan uzak kalmayı anlatır: {ar:السلامة أن يسلم الإنسان من العاهة والأذى, tr:es-selâmetü en yeslema'l-insânü mine'l-'âheti ve'l-ezâ, gloss:selâmet, insanın sakatlıktan ve eziyetten uzak kalmasıdır, source:"س ل م,B001"}. Savaşın karşıtı olan barışı da anlatır: {ar:السلم ضد الحرب, tr:es-silmü ziddü'l-harb, gloss:silm, savaşın karşıtıdır, source:"س ل م,B004"}; {ar:السلم الصلح والتسالم التصالح والمسالمة المصالحة, tr:es-silmü's-sulhu ve't-tesâlümü't-tesâlühu ve'l-müsâlemetü'l-musâlaha, gloss:silm barıştır; tesâlüm ve müsâleme barışmaktır, source:"س ل م,B004"}. Hayır da şerrin karşıtıdır: {ar:الخير ضد الشر, tr:el-hayru ziddü'ş-şerr, gloss:hayır şerrin karşıtıdır, source:"خ ي ر,B001"}. O gece inen şey bir nâzilenin tersidir. Bir kalabalık gece iner, bir kavmin yurduna yerleşir ve baskın saati olan şafağa kadar orada kalır, ama getirdiği esenliktir.

Kur'an aynı sahnenin karanlık yüzünü açıkça sahneler. Sâffât suresinde, azabı acele isteyenler için {ar:أَفَبِعَذَابِنَا يَسْتَعْجِلُونَ, tr:e-fe-bi-'azâbinâ yesta'cilûn, gloss:azabımızı mı acele istiyorlar, source:37:176} denir, ardından {ar:فَإِذَا نَزَلَ بِسَاحَتِهِمْ فَسَآءَ صَبَاحُ ٱلْمُنذَرِينَ, tr:fe-izâ nezele bi-sâhatihim fe-sâ'e sabâhu'l-münzerîn, gloss:o, yurtlarının avlusuna indiğinde, uyarılanların sabahı ne kötü olur, source:37:177}. İnmek ve sabah orada baskının iki parçasıdır. Âdiyât suresi, soluyarak koşanlara yemin ederek açılır {ar:وَٱلْعَٰدِيَٰتِ ضَبْحًۭا, tr:ve'l-'âdiyâti dabhâ, gloss:soluyarak koşanlara andolsun, source:100:1} ve sabah baskınını anlatır: {ar:فَٱلْمُغِيرَٰتِ صُبْحًۭا, tr:fe'l-muğîrâti subhâ, gloss:sabahleyin baskın yapanlara, source:100:3}; {ar:فَأَثَرْنَ بِهِۦ نَقْعًۭا, tr:fe-eserne bihî nak'â, gloss:orada toz kaldıranlara, source:100:4}. Hûd suresinde İbrahim'e selamla gelen elçiler {source:11:69} Lût'a şöyle der: {ar:يَٰلُوطُ إِنَّا رُسُلُ رَبِّكَ, tr:yâ Lûtu innâ rusulü rabbik, gloss:ey Lût, biz Rabbinin elçileriyiz, source:11:81}; {ar:فَأَسْرِ بِأَهْلِكَ بِقِطْعٍۢ مِّنَ ٱلَّيْلِ, tr:fe-esri bi-ehlike bi-kıt'ın mine'l-leyl, gloss:gecenin bir bölümünde aileni yola çıkar, source:11:81}; {ar:إِنَّ مَوْعِدَهُمُ ٱلصُّبْحُ ۚ أَلَيْسَ ٱلصُّبْحُ بِقَرِيبٍۢ, tr:inne mev'idehümü's-subh, e-leyse's-subhu bi-karîb, gloss:onların buluşma vakti sabahtır; sabah yakın değil mi, source:11:81}. Hicr suresi aynı olayda verilen hükmü emir kelimesiyle söyler: {ar:وَقَضَيْنَآ إِلَيْهِ ذَٰلِكَ ٱلْأَمْرَ أَنَّ دَابِرَ هَٰٓؤُلَآءِ مَقْطُوعٌۭ مُّصْبِحِينَ, tr:ve kadaynâ ileyhi zâlike'l-emra enne dâbira hâ'ülâ'i maktû'un musbihîn, gloss:ona şu emri bildirdik: bunların kökü sabaha erdiklerinde kesilecektir, source:15:66}. Kur'an meleklerin inişinin inkârcılar için mühlet bırakmadığını da söyler: {ar:مَا نُنَزِّلُ ٱلْمَلَٰٓئِكَةَ إِلَّا بِٱلْحَقِّ وَمَا كَانُوٓا۟ إِذًۭا مُّنظَرِينَ, tr:mâ nünezzilü'l-melâikete illâ bi'l-hakkı ve mâ kânû izen münzarîn, gloss:melekleri ancak hak ile indiririz, o zaman da onlara mühlet verilmez, source:15:8}; {ar:وَلَوْ أَنزَلْنَا مَلَكًۭا لَّقُضِىَ ٱلْأَمْرُ ثُمَّ لَا يُنظَرُونَ, tr:ve lev enzelnâ meleken le-kudıye'l-emru sümme lâ yünzarûn, gloss:bir melek indirseydik iş bitirilirdi, sonra onlara mühlet verilmezdi, source:6:8}; {ar:يَوْمَ يَرَوْنَ ٱلْمَلَٰٓئِكَةَ لَا بُشْرَىٰ يَوْمَئِذٍۢ لِّلْمُجْرِمِينَ, tr:yevme yeravne'l-melâikete lâ büşrâ yevme'izin li'l-mücrimîn, gloss:melekleri görecekleri gün suçlulara o gün hiçbir müjde yoktur, source:25:22}; {ar:وَٱلْمَلَٰٓئِكَةُ وَقُضِىَ ٱلْأَمْرُ, tr:ve'l-melâiketü ve kudıye'l-emr, gloss:melekler de gelir ve iş bitirilir, source:2:210}. Bu pasajlarda melekler ve emir bir kavmin üzerine iner ve sonuç yıkımdır. Kadir suresinde ise aynı iniş, aynı emir ve aynı sabah, esenlikle anılır.

Kur'an savaştan önceki bir geceyi de bir güven gecesi olarak anlatır. Bin meleğin vaat edildiği yerde {source:8:9}, hemen ardından şöyle denir: {ar:إِذْ يُغَشِّيكُمُ ٱلنُّعَاسَ أَمَنَةًۭ مِّنْهُ وَيُنَزِّلُ عَلَيْكُم مِّنَ ٱلسَّمَآءِ مَآءًۭ, tr:iz yuğaşşîkümü'n-nu'âse emeneten minhü ve yünezzilü 'aleyküm mine's-semâ'i mâ'â, gloss:hani O'ndan bir güven olarak sizi uyuklama sarıyor ve gökten üzerinize su indiriyordu, source:8:11}. Âl-i İmrân suresinde de sıkıntıdan sonra bir güven indirilir ve emrin hepsinin Allah'a ait olduğu söylenir: {ar:ثُمَّ أَنزَلَ عَلَيْكُم مِّنۢ بَعْدِ ٱلْغَمِّ أَمَنَةًۭ نُّعَاسًۭا, tr:sümme enzele 'aleyküm min ba'di'l-ğammi emeneten nu'âsâ, gloss:sonra kederin ardından üzerinize bir güven, bir uyuklama indirdi, source:3:154}; {ar:قُلْ إِنَّ ٱلْأَمْرَ كُلَّهُۥ لِلَّهِ, tr:kul inne'l-emra küllehû li'llâh, gloss:de ki: emrin hepsi Allah'ındır, source:3:154}. Savaş hükmünde barışa yönelme emredilir: {ar:وَإِن جَنَحُوا۟ لِلسَّلْمِ فَٱجْنَحْ لَهَا, tr:ve in cenahû li's-selmi fe'cnah lehâ, gloss:barışa yanaşırlarsa sen de ona yanaş, source:8:61}. Haram ayda savaşmak büyük sayılır: {ar:يَسْـَٔلُونَكَ عَنِ ٱلشَّهْرِ ٱلْحَرَامِ قِتَالٍۢ فِيهِ ۖ قُلْ قِتَالٌۭ فِيهِ كَبِيرٌۭ, tr:yes'elûneke 'ani'ş-şehri'l-harâmi kıtâlin fîh, kul kıtâlün fîhi kebîr, gloss:sana haram ayı, onda savaşmayı sorarlar; de ki: onda savaşmak büyük bir iştir, source:2:217}. Ayların sayısının verildiği yerde dört ay haram kılınır: {ar:مِنْهَآ أَرْبَعَةٌ حُرُمٌۭ ۚ ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ ۚ فَلَا تَظْلِمُوا۟ فِيهِنَّ أَنفُسَكُمْ, tr:minhâ erbe'atün hurum, zâlike'd-dînü'l-kayyim, fe-lâ tazlimû fîhinne enfüseküm, gloss:onlardan dördü haramdır; dosdoğru din budur; o aylarda kendinize zulmetmeyin, source:9:36}. Kılıç çekmeyi de anlatan ay kelimesi, Kur'an'da kılıcın kınında kaldığı zamanları da sayar. Rahman'ın kulları da düşmanca söze selamla karşılık verir: {ar:وَإِذَا خَاطَبَهُمُ ٱلْجَٰهِلُونَ قَالُوا۟ سَلَٰمًۭا, tr:ve izâ hâtabehümü'l-câhilûne kâlû selâmâ, gloss:cahiller onlara laf attığında "selam" derler, source:25:63}.

Sure bu sahneyi ayet ayet kurar. Birinci ayet bir gece söyler; gece yürüyüşünün sözü onun yanında duyulur. İkinci ayetin bilgi fiili, ailesinde baskın için yer seçmeyi taşır, ama soru burada bir bilgiyi sorar. Üçüncü ayet bini sayar. Bu sayı, binlerce kişilik bir topluluğun sözünü ve şerrin karşıtı olan hayrı da duyurur. Dördüncü ayette kalabalık iner. Melekler çoğuldur, "her" çokluğu tek sözde tutar, inenlerin Rabbinin kökü binleri anar. İnmek fiili, ailesinde felaketi ve çarpışmayı taşır. Beşinci ayet sahneyi çözer: şafak, baskının saatidir, doğuş saldırının ve gözcünün kelimesidir, fecr ansızın patlayan felaketin kelimesidir. Ama yüklem selâmdır. Gelen kalabalık zarar değil, esenlik getirir.

Kaynaklar: 97:4 ٱلْمَلَٰٓئِكَةُ م ل ك B009; 97:4 كُلِّ ك ل ل B003; 97:4 كُلِّ ك ل ل B009; 97:3 أَلْفِ ء ل ف B001; 97:4 رَبِّهِم ر ب ب B004; 97:5 مَطْلَعِ ط ل ع B007; 97:4 تَنَزَّلُ ن ز ل B006; 97:4 تَنَزَّلُ ن ز ل B007; 97:5 ٱلْفَجْرِ ف ج ر B003; 97:5 مَطْلَعِ ط ل ع B002; 97:5 مَطْلَعِ ط ل ع B004; 97:5 مَطْلَعِ ط ل ع B006; 97:2 أَدْرَىٰكَ د ر ي B002; 97:1 لَيْلَةِ ل ي ل B002; 97:3 شَهْرٍۢ ش ه ر B003; 97:5 سَلَٰمٌ س ل م B001; 97:5 سَلَٰمٌ س ل م B004; 97:3 خَيْرٌۭ خ ي ر B001

## Buluşmalar

İniş ile ölçü, Kur'an'ın hazineler sahnesinde tek bir sahnede buluşur: {ar:وَمَا نُنَزِّلُهُۥٓ إِلَّا بِقَدَرٍۢ مَّعْلُومٍۢ, tr:ve mâ nünezzilühû illâ bi-kaderin ma'lûm, gloss:onu ancak bilinen bir ölçüyle indiririz, source:15:21}. Yukarıdan aşağıya inen çizgi ölçülmüş paylar taşır. Duhân suresi aynı buluşmayı surenin kendi kelimeleriyle kurar: bir gecede indiriş, o gecede her işin ayrılması {source:44:4}. Yağmur sahnesi de bu buluşmanın içindedir. Arapçadaki "yağmur bir ölçüyle iner" sözü iki imgeyi tek cümlede birleştirir. Ra'd suresinde vadilerin "kendi ölçülerince" akması {source:13:17}, inen şeyin her yere kendi kabı kadar dağıldığını gösterir. Kamer suresindeki tufan ayeti {source:54:12} fışkırmayı, emri ve ölçüyü tek ayette toplar. Böylece iniş, ölçü ve fışkıran su tek bir hareketin üç anı olur.

İniş ile emir, Meryem suresinde inenlerin kendi sözünde buluşur: {ar:وَمَا نَتَنَزَّلُ إِلَّا بِأَمْرِ رَبِّكَ, tr:ve mâ netenezzelü illâ bi-emri rabbik, gloss:biz ancak Rabbinin emriyle ineriz, source:19:64}. Talâk suresinde de emrin kendisi iner {source:65:12}. Emir ile ölçü, işini yerine ulaştıran ve her şeye bir ölçü koyan Allah'ı anlatan ayette buluşur {source:65:3}. Ölçü ile hesap, ayın konakları sahnesinde buluşur. Orada ölçmek fiili ile inmek kökünden gelen konaklar yan yana durur {source:10:5}, {source:36:39}. En'âm suresinde sabahın yarılması, gecenin dinlenme kılınması ve güneşle ayın hesap için konması, "takdir" sözüyle kapanır {source:6:96}. Bu ayet şafak, hesap, ölçü ve dinlenme imgelerini tek bir cümlede taşır.

İzin kelimesi emir zinciri ile konuk sahnesini birleştirir. Rabbin izni, kapıcının girme izniyle aynı kelimedir. Nûr suresinde eve giriş için izin ve selam birlikte istenir {source:24:27}, {source:24:28}. İbrâhîm suresi bu buluşmayı Kadir suresinin kelimeleriyle kurar: {ar:بِإِذْنِ رَبِّهِمْ ۖ تَحِيَّتُهُمْ فِيهَا سَلَٰمٌ, tr:bi-izni rabbihim, tahiyyetühüm fîhâ selâm, gloss:Rablerinin izniyle; oradaki selamlaşmaları selamdır, source:14:23}. Selâm kelimesi de üç imgenin buluştuğu yerdir. Emir zincirinde emre teslim olmaktır, konuk sahnesinde varışın selamıdır, kalabalığın inişi sahnesinde ise baskının karşıtı olan zarar görmemek ve barıştır. Ağıl sahnesinde de gece boyunca korunmaktır. Beşinci ayetin ilk kelimesi bu dört sahnenin hepsine birden cevap verir.

Konuk sahnesi ile baskın sahnesi Hûd suresinde aynı elçilerde buluşur. Elçiler İbrahim'in kapısına selamla gelirler ve önlerine yemek konur {source:11:69}. Aynı elçiler Lût'a gece yola çıkmasını söyler ve hükmün sabah olduğunu bildirir {source:11:81}. Bir kavmin üzerine inen elçiler ya bir müjde ve selam getirir ya da sabahleyin bir yıkım. Fussilet suresinde inen melekler korkuyu kaldırır ve bir konukluk ikramı getirir {source:41:30}, {source:41:32}. Sâffât suresinde ise inen şeyin ardından uyarılanların kötü sabahı gelir {source:37:177}. Kadir suresi bu iki olasılık arasında yerini açıkça söyler. Gece iner, kalabalık iner, sabah gelir, ve yüklem selâmdır. Kalabalığın binleri de konuk sahnesine bağlanır. Âl-i İmrân suresinde indirilmiş binlerce melek {source:3:124}, savaş gecesinin güven uykusuyla aynı pasajlarda yer alır {source:8:9}, {source:8:11}.

İniş ile şafak, dikey çizginin iki ucudur. Me'âric suresinde melekler ve Ruh yükselir {source:70:4}. Secde suresinde emir iner ve yükselir {source:32:5}. Kadir suresinde iniş karanlığa doğru, doğuş ise karanlığın içinden dışarı doğrudur. Fecr kelimesi bu dönüşün işleyişini verir: gece yukarıdan doldurulur ve sonunda içeriden yarılır. Örtü imgesi de aynı noktada şafakla buluşur. Kur'an'ın giysi kıldığı gece {source:78:10} örter, doğuş kelimesi ise görünmeyi ve başını çıkarmayı anlatır. İkinci ayetin sorusu böylece beşinci ayetin doğuşunda bir görünür olmaya varır. Fecr kökü şafak imgesini bolluk imgesine de bağlar. Aynı kök geceyi yaran ışığı, taşı yaran suyu ve hayırla taşan cömertliği anlatır, fücur ise bunların tersidir. Üçüncü ayetin hayrı ile beşinci ayetin fecri bu kökte birbirine değer. Tekvîr suresindeki yeminlerde gecenin çekilmesi ve sabahın nefes alması {source:81:17}, {source:81:18}, değerli bir elçinin sözüne bağlanır {source:81:19}. Şafak imgesi orada dinlenme imgesiyle ve inen sözle aynı anda durur.

Surenin hareketi bu buluşmalarla taşınır. Birinci ayet yukarıdan tek bir indiriş yapar ve onu ölçünün adını taşıyan bir geceye bırakır. İkinci ayet o geceyi bilginin dışında bir şey olarak örter. Üçüncü ayet onu ay hesabıyla tartar ve tek gecenin hayrını sayılmış binlerin üstüne koyar. Dördüncü ayet gecenin içini doldurur: izinle, Rabbin elçileriyle, Ruh ile, her işten bir payla, konuk gibi ve kalabalık gibi inen bir akışla. Beşinci ayet bu dolu geceye tek bir yüklem verir ve onu karanlığın yarıldığı, ışığın ve ekinin çıktığı bir doğuşa kadar uzatır. İniş imgeleri birinci ve dördüncü ayetlerde, tartı ve örtü imgeleri ikinci ve üçüncü ayetlerde, karşılama, koruma ve çıkış imgeleri beşinci ayette yoğunlaşır. Surenin söylediği şey bir gecenin anlamıdır, imgeler de bu anlamı yukarıdan aşağıya ve karanlıktan aydınlığa uzanan tek bir hareket olarak gösterir.

