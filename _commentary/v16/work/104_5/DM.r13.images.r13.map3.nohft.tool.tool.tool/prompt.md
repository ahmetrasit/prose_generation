Focus: 104:5. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/104_5/D.r13/context.md =====
# 104:5 — focus

وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ

Anchor translation (canonical reading, reference only):

Peki, Ezici'nin ne olduğunu sana ne bildirdi?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَمَآ | مَا |  | CONJ;INTG |
| 2 | أَدْرَىٰكَ | أَدْرَىٰ | د ر ي | V;PRON |
| 3 | مَا | مَا |  | INTG |
| 4 | ٱلْحُطَمَةُ | حُطَمَة | ح ط م | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 104 — full text (context; no pericope)

- 104:1 وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ
- 104:2 ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ
- 104:3 يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ
- 104:4 كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ
- 104:5 ◀ focus وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ
- 104:6 نَارُ ٱللَّهِ ٱلْمُوقَدَةُ
- 104:7 ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ
- 104:8 إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ
- 104:9 فِى عَمَدٍۢ مُّمَدَّدَةٍۭ


===== _commentary/v16/work/104_5/D.r13/01_dictionary.md =====
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

## ح ط م (root_000337) — identity root of ٱلْحُطَمَةُ (w4)

- **B001** kuru ya da sert şeyi kırıp ufalama ve bundan kalan kuru döküntü — kuru ya da sert bir şeyi kırıp parçalamak · kırılıp parçalanmış · kırıp parçalama · kuru şeylerin kırık döküntüsü
  حطمت الشيء حَطْما كسرته (maqayis;sihah;mufradat)؛ الحَطْم كسرك الشيء اليابس كالعظام ونحوها (ayn;tahdhib)؛ الحُطام ما تكسر من اليبس (sihah;tahdhib;mufradat)
- **B002** karşısına çıkanı parçalayan şiddetli ateş — karşısına çıkanı parçalayan şiddetli ateş
  سميت النار الحُطَمَة لحطمها ما تلقى (maqayis;sihah)؛ الحُطَمَة النار وقيل باب من جهنم (ayn)؛ للنار الشديدة حُطَمَة (tahdhib)؛ سميت الجحيم حُطَمَة (mufradat)
- **B003** insanı ve malı çökerten ağır kıtlık yılı — insanı ve malı çökerten ağır kuraklık yılı
  الحُطَمَة السنة الشديدة لأنها تحطم كل شيء (maqayis)؛ الحُطَمَة السنة الشديدة (ayn;tahdhib)؛ أصابتهم حُطَمَة أي سنة وجدب (sihah)
- **B004** sürüyü sertçe sürüp hayvanları birbirine ezen acımasız sürücü — hayvanları birbirine çarptıracak kadar sert süren acımasız sürücü · sürüsüne acımayan ve onu iyi otlatmayan çoban
  الحَطِم السواق يعنف يحطم بعض الإبل ببعض (maqayis)؛ رجل حَطِم وحُطَمَة إذا كان قليل الرحمة للماشية يهشم بعضها ببعض (sihah)؛ شر الرعاء الحُطَمَة (sihah;tahdhib)؛ سائق حَطِم يحطم الإبل لفرط سوقه (mufradat)
- **B005** yaşlılıkla çöküp güçten düşmek — yaşlılıktan veya zayıflıktan çökmüş at · hayvan yaşlanıp güçten düştü · yaş onu yaşlandırıp güçsüzleştirdi · yakınları arasında uzun süre yaşayıp iyice yaşlandı
  يقال للفرس إذا تهدم لطول عمره حَطِم (maqayis;sihah)؛ حطمت الدابة أي أسنت (sihah)؛ حطمته السن إذا أسن وضعف (sihah;tahdhib)؛ حطم فلانا أهله إذا كبر فيهم كأنهم صيروه شيخا محطوما (tahdhib)؛ فرس حَطِم إذا هزل أو أسن فضعف (tahdhib)
- **B006** karşısına çıkanı ezen kalabalık sürü veya aslanın mala saldırısı — karşısına çıkanı ve otu ezen kalabalık deve veya koyun sürüsü · aslanın mala saldırıp kırıp geçirmesi
  العكرة من الإبل حُطَمَة لأنها تحطم كل شيء تلقاه (maqayis;sihah)؛ للعكرة من الإبل حُطَمَة لحطمها الكلأ وكذلك الغنم إذا كثرت (tahdhib)؛ حُطَمَة الأسد في المال عيثه وفرسه (ayn;tahdhib)
- **B007** kutsal yapının yağmur oluğu yanındaki belirli bölümü veya duvarı — kutsal yapının yağmur oluğu tarafındaki belirli bölüm veya onun duvarı
  الحَطِيم حجر مكة (ayn)؛ الحَطِيم الجدر يعني جدار حجر الكعبة (sihah)؛ الحَطِيم الذي فيه الميزاب وإنما سمي حطيما لأن البيت رفع وترك ذاك محطوما (tahdhib)؛ الحَطِيم وزمزم مكانان (mufradat)؛ الحَطِيم ممكن أن يكون من هذا وهو الحجر لكثرة من ينتابه كأنه يحطم (maqayis)
- **B008** aşırı yiyen kişi veya yiyeceği öğütüp sindiren şey — çok yiyen, obur kimse · yiyeceği öğüten diş veya sindiren organ
  رجل حُطَمَة للكثير الأكل (sihah;tahdhib)؛ قيل للأكول حُطَمَة تشبيها بالجحيم (mufradat)؛ يقال للجوارس حاطوم وهاضوم (tahdhib)
- **B009** dünyanın yok olup gidecek malı ve süsü — dünyanın geçici malı ve süsü
  حُطام الدنيا عرضها وأثرها وزينتها (tahdhib)؛ حُطام الدنيا كل ما فيها من مال يفنى ولا يبقى (tahdhib)

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

===== _commentary/v16/out/s104/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 104:5, and ## Buluşmalar) =====
## Aşağı atılan, yukarı çıkan ve hedefini bulan ateş

Surenin dikey bir sahnesi vardır ve bir avcının nişanı ile aynı hareketi paylaşır. Adam aşağı atılır; atma kökünün özü fırlatıp bırakmaktır {ar:أصل صحيح يدل على طرح وإلقاء, tr:aslün sahîhun yedüllü alâ tarhin ve ilkâ', gloss:atıp bırakmayı gösterir, source:"ن ب ذ,B001"}. Ateş ise yukarı çıkar. {ar:تَطَّلِعُ, tr:tattali'u, gloss:çıkıp vurur, üstüne tırmanır, source:104:7} fiilinin kökü güneşin ve yıldızın doğuşudur {ar:طلعت الشمس والكوكب طلوعا ومطلعا, tr:tala'ati'ş-şemsü ve'l-kevkeb, gloss:güneş ve yıldız doğdu, source:"ط ل ع,B001"}; görünmek ve belirmek {ar:أصل واحد صحيح يدل على ظهور وبروز, tr:aslün vâhidün sahîhun yedüllü alâ zuhûrin ve burûz, gloss:görünüp ortaya çıkmayı gösterir, source:"ط ل ع,B001"}. Bir dağın tepesine tırmanmak ve tepeden aşağıya bakılan yerin dehşeti de bu köktendir {ar:طلعت الجبل أي علوته, tr:tala'tü'l-cebele ey alevtüh, gloss:dağa çıktım, yani üstüne yükseldim, source:"ط ل ع,B006"}, {ar:هول المطلع, tr:hevlü'l-muttala', gloss:tepeden bakılan yerin dehşeti, source:"ط ل ع,B006"}. Bir kabı ağzına kadar doldurmak da {ar:قدح طلاع ممتلىء, tr:kadahun tılâ'un mümteli', gloss:ağzına kadar dolu kap, source:"ط ل ع,B007"}. Ayetteki yapı da önemlidir: fiil "alâ" edatıyla gelir ve Arapçada aynı yapı bir topluluğun üstüne baskın yapmak için kullanılır {ar:طلع علينا فلان يطلع طلوعا إذا هجم, tr:tala'a aleynâ fülânün izâ hecem, gloss:falan üstümüze çıkageldi, yani baskın yaptı, source:"ط ل ع,B002"}. Ateş doğan bir güneş gibi belirir, bir tırmanıcı gibi yükselir, bir baskıncı gibi üstlerine gelir ve kabı doldurur gibi yükselir. Ateşin kökünde de kararsızca kıpırdayan ışık vardır {ar:أصل صحيح يدل على إضاءة واضطراب وقلة ثبات, tr:aslün sahîhun yedüllü alâ idâetin ve ıdtırâbin ve kılleti sebât, gloss:aydınlanma, çalkalanma ve sabit durmamayı gösterir, source:"ن و ر,B001"}.

Bu yükseliş bir hedefe yöneliktir. Beşinci ayetin {ar:أَدْرَىٰكَ, tr:edrâke, gloss:sana bildirdi, source:104:5} fiilinin kökü avcının ustalığını da taşır: avın yerini daha görmeden kollamak ve onu bir siper hayvanının ardından gizlice yaklaşarak aldatmak {ar:تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته, tr:tedarreytü's-sayde izâ nazartü eyne hüve ve lem erahü ba'd, gloss:avı henüz görmeden nerede olduğunu kolladım ve ona sinsice yaklaştım, source:"د ر ي,B003"}, {ar:الدرية الدابة التي يستتر بها الذي يرمي الصيد, tr:ed-dariyye ed-dâbbetü'lletî yesteteru bihe'llezî yermi's-sayd, gloss:avcının ardına saklandığı hayvan, source:"د ر ي,B003"}, nişan alıştırması yapılan halka {ar:الدريئة الحلقة التي يتعلم عليها الطعن, tr:ed-darî'e el-halkatü'lletî yute'allemu aleyhe't-ta'n, gloss:mızrak atmanın öğrenildiği halka, source:"د ر ي,B005"} ve bir yeri seçip baskın için ona yönelmek {ar:ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة, tr:iddarâ benû fülânin mekâne kezâ ey i'temedûhü bi-ğazvin ev ğâra, gloss:falan oğulları bir yeri seçip baskınla ona yöneldiler, source:"د ر ي,B002"}. Bu açıklamadaki "i'temedûhü", son ayetteki direklerin köküdür; o kökte kasten yönelmek de vardır {ar:العمد والتعمد خلاف السهو, tr:el-amd ve't-ta'ammüd hilâfü's-sehv, gloss:kasıt, yanılmanın zıddıdır, source:"ع م د,B001"}. İlk ayetin kökü güçlü atan yayı adlandırır {ar:قوس همزي شديدة الدفع للسهم, tr:kavsün hemezâ şedîdetü'd-def'i li's-sehm, gloss:oku güçlü iten yay, source:"ه م ز,B003"}; yedinci ayetin kökü düşmanı gözetlemek için önden gönderilen öncüleri {ar:الطليعة قوم يبعثون ليطلعوا طلع العدو, tr:et-talî'a kavmün yüb'asûne li-yattali'û tal'a'l-adüvv, gloss:düşmanın durumunu gözetlemek için gönderilen topluluk, source:"ط ل ع,B004"}; yüreklerin kökü avı kalbinden vurmayı {ar:فأدت الصيد إذا أصبت فؤاده, tr:fe'edtü's-sayde izâ esabtü fuâdeh, gloss:avı kalbinden vurdum, source:"ف ء د,B003"}. Aynı kökün bir dalı tersini de söyler: atıcının oku hedefin üstünden aşıp gider {ar:وأطلع الرامي أي جاز سهمه من فوق الغرض, tr:ve atla'a'r-râmî ey câze sehmühû min fevki'l-ğaraz, gloss:atıcı "atla'a" etti, yani oku hedefin üstünden geçti, source:"ط ل ع,B010"}. Surenin yükselişi aşmaz: {ar:عَلَى ٱلْأَفْـِٔدَةِ, tr:ale'l-ef'ide, gloss:yüreklerin üzerine, source:104:7} durur. Bunlar fiilin ayetteki anlamının yanında duyulan aile imgeleridir; ayetin kendisi ateşin yüreklere ulaştığını söyler.

Yükseliş, sekizinci ayette yukarıdan kapanan örtüyle biter: {ar:إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ, tr:innehâ aleyhim mü'sade, gloss:o, üzerlerine kapatılmıştır, source:104:8}; "aleyhim" yedinci ayetteki "alâ"yı tekrar eder. Kökün anlamı kapıyı kapatıp sıkıca örtmektir {ar:أوصدت الباب وآصدته أي أطبقته وأحكمته ومؤصدة مطبقة, tr:evsadtü'l-bâbe ve âsadtühû ey atbaktühû ve ahkemtüh, gloss:kapıyı kapadım, sıkıca örttüm; mü'sade üstü kapatılmış demektir, source:"و ص د,B001"}.

Kuran ateşe atılmayı ve ateşin onlara yönelişini başka yerlerde canlandırır. Furkan suresinde Allah {ar:إِذَا رَأَتْهُم مِّن مَّكَانٍۭ بَعِيدٍۢ سَمِعُوا۟ لَهَا تَغَيُّظًۭا وَزَفِيرًۭا, tr:izâ raethüm min mekânin ba'îdin semi'û lehâ teğayyuzan ve zefîrâ, gloss:onları uzaktan görünce, onun öfkeyle köpürüşünü ve uğultusunu duyarlar, source:25:12} der; ateş görür ve hedefine yönelir, ardından {ar:وَإِذَآ أُلْقُوا۟ مِنْهَا مَكَانًۭا ضَيِّقًۭا مُّقَرَّنِينَ دَعَوْا۟ هُنَالِكَ ثُبُورًۭا, tr:ve izâ ülkû minhâ mekânen dayyikan mukarranîne de'av hünâlike sübûrâ, gloss:bağlanmış olarak onun dar bir yerine atıldıklarında orada yok olmayı dilerler, source:25:13}. Mülk suresinde {ar:إِذَآ أُلْقُوا۟ فِيهَا سَمِعُوا۟ لَهَا شَهِيقًۭا وَهِىَ تَفُورُ, tr:izâ ülkû fîhâ semi'û lehâ şehîkan ve hiye tefûr, gloss:oraya atıldıklarında onun hırıltısını duyarlar, o kaynar, source:67:7}, {ar:تَكَادُ تَمَيَّزُ مِنَ ٱلْغَيْظِ, tr:tekâdü temeyyezü mine'l-ğayz, gloss:öfkeden neredeyse çatlayacaktır, source:67:8}. Yukarı yol kapalıdır: Hac suresinde {ar:كُلَّمَآ أَرَادُوٓا۟ أَن يَخْرُجُوا۟ مِنْهَا مِنْ غَمٍّ أُعِيدُوا۟ فِيهَا, tr:küllemâ erâdû en yahrucû minhâ min ğammin u'îdû fîhâ, gloss:kederden oradan çıkmak istedikçe oraya geri döndürülürler, source:22:22}, Secde suresinde de aynı söz {source:32:20}. Atılmanın kendisi Kasas suresinde Firavun ve ordusu için anlatılır: {ar:فَأَخَذْنَٰهُ وَجُنُودَهُۥ فَنَبَذْنَٰهُمْ فِى ٱلْيَمِّ, tr:fe-ehaznâhü ve cünûdehû fe-nebeznâhüm fi'l-yemm, gloss:onu ve ordularını yakalayıp denize attık, source:28:40}. Aynı surede Firavun yükselmeyi ve tutuşturmayı tek cümlede ister: {ar:فَأَوْقِدْ لِى يَٰهَٰمَٰنُ عَلَى ٱلطِّينِ فَٱجْعَل لِّى صَرْحًۭا لَّعَلِّىٓ أَطَّلِعُ إِلَىٰٓ إِلَٰهِ مُوسَىٰ, tr:fe-evkıd lî yâ Hâmânü ale't-tîni fec'al lî sarhan le'allî ettali'u ilâ ilâhi Mûsâ, gloss:Haman, benim için çamurun üstünde ateş yak, bana bir kule yap; belki Musa'nın ilahına çıkıp bakarım, source:28:38}. İnsanın yaktığı ateşle kurulan kule yukarı çıkmak içindir; bu surede ise tutuşturulmuş ateşin kendisi yükselir. Saffat suresinde cennetteki bir kişi dünyadaki arkadaşını arar: {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fettala'a fe-raâhü fî sevâi'l-cahîm, gloss:yukarıdan baktı ve onu cehennemin ortasında gördü, source:37:55}. Aynı fiil orada tepeden aşağı bakmaktır.

Kaynaklar: 104:4 لَيُنۢبَذَنَّ ن ب ذ B001; 104:7 تَطَّلِعُ ط ل ع B001; 104:7 تَطَّلِعُ ط ل ع B002; 104:7 تَطَّلِعُ ط ل ع B006; 104:7 تَطَّلِعُ ط ل ع B007; 104:7 تَطَّلِعُ ط ل ع B010; 104:7 تَطَّلِعُ ط ل ع B004; 104:6 نَارُ ن و ر B001; 104:5 أَدْرَىٰكَ د ر ي B003; 104:5 أَدْرَىٰكَ د ر ي B005; 104:5 أَدْرَىٰكَ د ر ي B002; 104:9 عَمَدٍ ع م د B001; 104:1 هُمَزَةٍ ه م ز B003; 104:7 ٱلْأَفْـِٔدَةِ ف ء د B003; 104:8 مُّؤْصَدَةٌۢ و ص د B001

## Sanmak, bilmemek, bilinmek

Sure bilginin üç konumundan geçer. Önce adam sanır: {ar:يَحْسَبُ, tr:yahsebü, gloss:sanıyor, source:104:3}, iki zıttan birine hüküm vermektir {ar:حسبت كذا في معنى ظننت, tr:hasibtü kezâ fî ma'nâ zanentü, gloss:"hasibtü" "zannettim" anlamındadır, source:"ح س ب,B002"}. Kökün bir dalı ise birinin içinde ne olduğunu yoklamaktır {ar:احتسبت فلانا اختبرت ما عنده, tr:ihtesebtü fülânen ihtebertü mâ indeh, gloss:falancanın içinde ne olduğunu sınadım, source:"ح س ب,B010"}. Adamın yapmadığı yoklama, sonunda ona yapılır.

Sonra dinleyiciye bilmediği söylenir: {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ, tr:ve mâ edrâke me'l-hutame, gloss:hutamenin ne olduğunu sana ne bildirdi, source:104:5}. Bu fiil bilmek ve bildirilmektir {ar:دريته ودريت به أي علمت به وأدريته أي أعلمته, tr:dereytühû ve dereytü bihî ey alimtü bih, ve edreytühû ey a'lemtüh, gloss:onu bildim; ona bildirdim, source:"د ر ي,B001"}, ve kökün örnek cümlesi bildireni Allah olarak anar {ar:دريت الشيء والله أدرانيه, tr:dereytü'ş-şey'e vallâhü edrânîh, gloss:şeyi bildim, onu bana Allah bildirdi, source:"د ر ي,B001"}. Altıncı ayet de cevabı Allah'a bağlar: {ar:نَارُ ٱللَّهِ ٱلْمُوقَدَةُ, tr:nârullâhi'l-mûkade, gloss:Allah'ın tutuşturulmuş ateşi, source:104:6}. Soru, insanın kendi bilgisiyle ulaşamayacağı bir şeyi gösterir ve cevabı yalnızca bildirilen bir bilgi olarak verir.

Son olarak ateş bilir. {ar:تَطَّلِعُ عَلَى, tr:tattali'u alâ, gloss:üzerine çıkar, source:104:7} yapısı Arapçada bir işin içyüzüne vakıf olmak için de kullanılır {ar:اطلعت على باطن أمره, tr:ittala'tü alâ bâtını emrih, gloss:işinin içyüzüne vakıf oldum, source:"ط ل ع,B003"}, {ar:أطلعني طلع هذا الأمر حتى علمته كله, tr:atla'anî tal'a hâze'l-emri hattâ alimtühû küllehû, gloss:bu işin içini bana gösterdi, hepsini öğrendim, source:"ط ل ع,B003"}. Ayetin anlamı ateşin yüreklere ulaşmasıdır; yanında, içi bilinen bir yüreğin sesi duyulur. Hesabını yapan adam kendi hesabını bilmiyordu; ateş, yürekte olanı bilir.

Kuran aynı sırayı başka surelerde de kurar. Müddessir suresinde Allah tek başına yarattığı ve {ar:وَجَعَلْتُ لَهُۥ مَالًۭا مَّمْدُودًۭا, tr:ve ce'altü lehû mâlen memdûdâ, gloss:ona uzayıp giden bir mal verdim, source:74:12} dediği adamı anlatır; sonra {ar:سَأُصْلِيهِ سَقَرَ, tr:se-uslîhi sekar, gloss:onu Sekar'a sokacağım, source:74:26}, {ar:وَمَآ أَدْرَىٰكَ مَا سَقَرُ, tr:ve mâ edrâke mâ sekar, gloss:Sekar'ın ne olduğunu sana ne bildirdi, source:74:27}, {ar:لَا تُبْقِى وَلَا تَذَرُ, tr:lâ tubkî ve lâ tezer, gloss:ne bırakır ne geri koyar, source:74:28}. Mal, "ne bildirdi" sorusu, ateş ve ardından bir sayı: bu surenin sırası oradadır. Karia suresinde aynı kalıp ateşe açılır: {ar:وَمَآ أَدْرَىٰكَ مَا هِيَهْ, tr:ve mâ edrâke mâ hiyeh, gloss:onun ne olduğunu sana ne bildirdi, source:101:10}, {ar:نَارٌ حَامِيَةٌۢ, tr:nârun hâmiye, gloss:kızgın bir ateş, source:101:11}. Hakka suresinde kitabı sol eline verilen kişi iki fiili, bilmeyi ve hesabı, tek feryatta söyler: {ar:يَٰلَيْتَنِى لَمْ أُوتَ كِتَٰبِيَهْ, tr:yâ leytenî lem ûte kitâbiyeh, gloss:keşke kitabım bana verilmeseydi, source:69:25}, {ar:وَلَمْ أَدْرِ مَا حِسَابِيَهْ, tr:ve lem edri mâ hisâbiyeh, gloss:ve hesabımın ne olduğunu bilmeseydim, source:69:26}. Aynı surede sağdan verilen ise {ar:إِنِّى ظَنَنتُ أَنِّى مُلَٰقٍ حِسَابِيَهْ, tr:innî zanentü ennî mülâkın hisâbiyeh, gloss:ben hesabıma kavuşacağımı zaten sanıyordum, source:69:20} der; doğru sanı, hesaba kavuşacağını bilen sanıdır. Beled suresinde de aynı sanı vardır: {ar:أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ, tr:e-yahsebü en len yakdira aleyhi ehad, gloss:kimsenin ona gücünün yetmeyeceğini mi sanıyor, source:90:5}, {ar:يَقُولُ أَهْلَكْتُ مَالًۭا لُّبَدًا, tr:yekûlü ehlektü mâlen lübedâ, gloss:yığın yığın mal harcadım diyor, source:90:6}, {ar:أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ, tr:e-yahsebü en lem yerahû ehad, gloss:onu kimsenin görmediğini mi sanıyor, source:90:7}. Görülmediğini sanan adam, içini bilen bir ateşle karşılaşır. Meryem suresinde mal ve evlat iddia eden kişiye sorulur: {ar:أَطَّلَعَ ٱلْغَيْبَ أَمِ ٱتَّخَذَ عِندَ ٱلرَّحْمَٰنِ عَهْدًۭا, tr:ettala'a'l-ğaybe emi'ttehaze inde'r-rahmâni ahdâ, gloss:gaybı mı gördü, yoksa Rahman katında bir söz mü aldı, source:19:78}. Gaybın içine bakamayan insanın karşısında, bu surede içini bilen bir ateş durur. Karun'un iddiası da bir bilgidir {source:28:78}; Tarık suresi ise gizlilerin sınanacağı günü anar: {ar:يَوْمَ تُبْلَى ٱلسَّرَآئِرُ, tr:yevme tüble's-serâir, gloss:gizlilerin sınandığı gün, source:86:9}.

Kaynaklar: 104:3 يَحْسَبُ ح س ب B002; 104:3 يَحْسَبُ ح س ب B010; 104:5 أَدْرَىٰكَ د ر ي B001; 104:7 تَطَّلِعُ ط ل ع B003

## Buluşmalar

İlk ayetteki iki kelime iki imgeyi aynı anda taşır: el ve dil. İtme ifadesi ile gıyap ve huzur ifadesi aynı iki kelimeyi birleştirir. Mümtehine suresindeki ayet, ellerin ve dillerin birlikte kötülükle uzatılmasını {source:60:2} söyleyerek bu ikisini tek sahnede toplar. Sıkan, iten, kusur arayan ve arkadan dürten kişi, ikinci ayette malın üstüne kapanan yumruğa dönüşür. Kökte o yumruğun sonu bukağıdır, ellerin boyna toplanması {source:"ج م ع,B008"}. Hakka suresinde malının işe yaramadığını söyleyen adam bukağılanır {source:69:30}. Toplayan el ile bağlanan el, aynı kökün iki ucudur.

Sayma ile yaslanma üçüncü ayetin bir tek fiilinde buluşur: "yahsebü" hem saymanın hem yeterliğin köküdür, kalıcılık fiili de sanarak yaslanmak diye açıklanır. Tevbe suresindeki {ar:خَٰلِدِينَ فِيهَا ۚ هِىَ حَسْبُهُمْ, tr:hâlidîne fîhâ, hiye hasbühüm, gloss:orada kalıcı olarak; o onlara yeter, source:9:68} sözü, adamın mala yüklediği iki şeyi, kalıcılığı ve yeterliği, ateşe verir. Aynı iki imge su sahnesiyle de buluşur: sayma kökündeki kesilmeyen su, adamın sandığı süreklilik; kırıcının kökündeki tükenen mal, bu sürekliliğin sonu. Kehf suresindeki bahçe sahibi bu yolu baştan sona yürür: bahçesinin arasından nehir akar, bahçenin yok olmayacağını sanır, sanma fiiliyle aynı kökten bir "husban" bahçeyi vurur ve avuçları boş kalır {source:18:40}. Hadid suresi aynı yolu mal çoğaltma yarışının benzetmesi yapar ve "hutam" ile bitirir {source:57:20}.

Kalıcılık ile ocak arasında bir buluşma daha vardır: kalıcılık kökünde "kalıcılar" diye anılan tek şey ocak taşlarıdır. Kendini kalıcı sanan adam, ateşin altında yıllarca kalan taşların adını taşıyan bir fiille konuşur. Kalıcılık kökünün bir dalı da kalbe gider: sanı, kalpte yerleşik olan gönüle düşer. Ocak ile yürek de iki kez birleşir: yürek tutuşmayla adlandırılır ve yüreklerin kökü ateş yakmanın fiiliyle açıklanır. Altıncı ve yedinci ayetler bu yüzden bir sıfat ile onun yerini ardı ardına söyler: tutuşturulmuş ateş, tutuşmayla adlanan yüreğe çıkar. Sanının oturduğu yer, ateşin vardığı yerdir.

Sürü ile kapalı yapı sekizinci ayetin kelimesinde buluşur: aynı kök mal için dağda yapılan taş ağılı ve üstü kapatılmış ateşi adlandırır. Sürüyü ağıla kapatan adam, kapatılmış bir ateşin içindedir. Sürü ile ateş damgada buluşur: devenin ateşi damgasıdır, Tevbe suresinde biriktirilen hazine kızdırılıp alınlara basılır {source:9:35}, Kalem suresinde mal ve oğullar sahibi hemmâz burnundan damgalanır {source:68:16}. Bu son ayet ilk imge ile sürüyü birbirine bağlar: iğneleyen dil, mal ve damga aynı adamdadır.

Yükselen ateş ile avcı, aynı kökün iki dalında buluşur: ateşin yükselişini anlatan fiil, okun hedefin üstünden aşmasını da adlandırır ve bu ateş aşmaz, yüreklerin üstünde durur. Avcının kolladığı yer yürektir; yüreklerin kökü avı kalbinden vurmaktır. Bilmek ile avcılık da beşinci ayetin fiilinde aynı köktür: görmeden kollamak ve bilmek. Sanan adam ile içini bilen ateş arasındaki mesafeyi, "ne bildirdi" sorusu kapatır ve cevabı Allah'ın ateşi olarak verir.

Surenin hareketi bu buluşmalarla taşınır. İlk iki ayette her şey adamın elindedir: sıkan, iten, toplayan, sayan bir el ve onu yaralayan bir dil. Üçüncü ayette bu el bir sanıya dayanır ve kalbe yerleşir. Dördüncü ayetten sonra yön tersine döner: el açılır ve atılan adamın kendisidir; topladığı malın adı kırıntı olur, saydığı sayı onu saymaz, dayandığı direkler onu tutar, sürüsünü kapattığı ağıl üzerine kapanır. Ateş aşağıdan yükselir ve sanının oturduğu yüreğe ulaşır. İlk ayetteki kuşatma kelimesinden son ayetteki direklere kadar sure, dışarıya uzanan bir elden içeriye kapanan bir yapıya doğru ilerler.

