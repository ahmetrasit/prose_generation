Focus: 100:3. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/100_3/D.r13/context.md =====
# 100:3 — focus

فَٱلْمُغِيرَٰتِ صُبْحًۭا

Anchor translation (canonical reading, reference only):

Ardından sabah vakti baskın yapanlara,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَٱلْمُغِيرَٰتِ | مُغِيرَٰت | غ ي ر | CONJ;DET;N |
| 2 | صُبْحًا | صُبْح | ص ب ح | T |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 100 — full text (context; no pericope)

- 100:1 وَٱلْعَٰدِيَٰتِ ضَبْحًۭا
- 100:2 فَٱلْمُورِيَٰتِ قَدْحًۭا
- 100:3 ◀ focus فَٱلْمُغِيرَٰتِ صُبْحًۭا
- 100:4 فَأَثَرْنَ بِهِۦ نَقْعًۭا
- 100:5 فَوَسَطْنَ بِهِۦ جَمْعًا
- 100:6 إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌۭ
- 100:7 وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ
- 100:8 وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ
- 100:9 ۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ
- 100:10 وَحُصِّلَ مَا فِى ٱلصُّدُورِ
- 100:11 إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ


===== _commentary/v16/work/100_3/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## غ ي ر (root_001119) — identity root of فَٱلْمُغِيرَٰتِ (w1)

- **B001** yarar sağlayıp durumunu iyileştirme — aileyi geçindiren azık ve ihtiyaç payı · aileye geçimlik ve yarar sağlama · ailesine geçimlik sağladı ve yarar dokundurdu · ona yarar sağladı ve ihtiyacını giderdi · Tanrı onlara yağmur verip durumlarını iyileştirdi · yağmur toprağı suladı · sulanmış toprak · sulanmış toprak · yük takımlarını düzeltiyorlar · devesinin yükünü indirip durumunu düzeltti · hayvanı rahatlatmak için yük takımını düzenleyen kişi
  الغِيرة بالكسر: الميرة (sihah)؛ يميرهم وينفعهم (sihah)؛ غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم (maqayis)؛ سقاهم (sihah)؛ يصلحون الرحال (sihah)؛ حط عنه رحله وأصلح من شأنه (tahdhib)
- **B002** cana karşılık ceza yerine kabul edilen kan bedeli — bana kan bedelini ödedi · kan bedeli · cana karşılık ceza yerine kabul edilen kan bedeli
  غارني الرجل إذا وداك من الدية والاسم الغِيرة (sihah)؛ الدية فإنها تسمى الغير (maqayis)؛ تقبلوا الغيرا (maqayis;sihah)
- **B003** biçimini değiştirme veya yerine başkasını koyma — şeyi değiştirdi ve öncekinden farklı hale getirdi · biçimini değiştirme veya yerine başkasını koyma · durumundan ayrılıp farklı hale geldi · yanlış olanı doğru olanla değiştirip giderdi · onunla alışverişte karşılıklı değiş tokuş yaptı · yerine konan karşılık
  الاسم من قولك غيرت الشيء فتغير (sihah)؛ تغير فلان عن حاله (tahdhib)؛ تغيير صورة الشيء دون ذاته (mufradat)؛ تبديله بغيره (mufradat)؛ يدفعون ذلك المنكر بغيره من الحق (tahdhib)؛ قود فغير إلى الدية (maqayis)؛ غايرت الرجل أي عارضته بالبيع وبادلته والغيار البدال (sihah)
- **B004** eşini veya ailesini kıskanarak koruma duygusu — eşini veya ailesini kıskanarak koruma duygusu · eşini veya ailesini kıskanıp sakındı · eşine veya ailesine karşı kıskanç ve korumacı · eşine veya ailesine karşı kıskanç erkek · eşine veya ailesine karşı kıskanç kadın · eşine veya ailesine karşı çok kıskanç kişi · eşini veya ailesini kıskanarak koruma duygusunun bir başka söylenişi
  الغَيرة بالفتح مصدر قولك غار الرجل على أهله (sihah)؛ رجل غيور وغيران وامرأة غيور وغيرى (sihah)؛ غيرة الرجل على أهله (maqayis)؛ الغار لغة في الغيرة (maqayis)
- **B005** başka olma, dışta bırakma veya olumsuzlama — başka, aynı olmayan veya aykırı · dışında, dışta bırakarak · değil, olmayan · doğru olmayan, yanlış · biri öteki olmayan iki şey · şeyler birbirinden farklılaştı
  هذا الشيء غير ذاك أي هو سواه وخلافه (maqayis)؛ غير بمعنى سوى (sihah;tahdhib)؛ يوصف بها ويستثنى (sihah)؛ يكون استثناء (tahdhib)؛ يكون غير اسما (tahdhib)؛ معنى غير معنى لا (tahdhib)؛ للنفي المجرد (mufradat)؛ بمعنى إلا (mufradat)؛ لنفي صورة من غير مادتها (mufradat)؛ متناولا لذات (mufradat)؛ الغيرين أعم من المختلفين (mufradat)؛ تغايرت الأشياء اختلف (sihah)

## ص ب ح (root_000839) — identity root of صُبْحًا (w2)

- **B001** günün ilk aydınlığı — tan ve günün ilk aydınlığı · günün başı, gecenin karşıtı olan erken gündüz · her günün ilk bölümü · günün ilk bölümüne girme ya da o an · günün ilk bölümüne varılan yer ya da o an
  الصباح نور النهار (maqayis)؛ الصبح والصباح أول النهار (mufradat)؛ الصبح الفجر والصباح نقيض المساء (sihah)؛ الصبح معروف والصبيحة من كل يوم أول النهار (jamhara)؛ صبحني فلان إذا أتاك صباحا والمصبح الموضع الذي يصبح فيه (ayn)
- **B002** günün başında gelmek — ona günün başında geldim ya da o bana günün başında geldi · onlara günün başında su getirdim · günün başına özgü esenlik sözü
  صبحني فلان إذا أتاك صباحا (ayn)؛ صبحته إذا أتيته صباحا وصبحته أي قلت له عم صباحا (sihah)؛ صبحتهم ماء كذا أتيتهم به صباحا (mufradat)
- **B003** günün başındaki içecek ve içme — günün başında içme ya da yeme; o vakitte içilen şey · ona günün başı içeceğini verdim · günün başında içti · günün başı içeceğini içmiş kimse · günün başı içeceğinin verildiği kap · günün başında içmek için kullanılan kadehler · günün başı içeceğinden önce oyalanılan şey
  لشرب الغداة الصبوح والمصابيح الأقداح التي يصطبح بها (maqayis)؛ الصبوح ما يشرب بالغداة وفعلك الاصطباح (ayn)؛ الصبوح الأكل والشرب في أول النهار وصبحت الإبل إذا سقيتها في أول النهار (jamhara)؛ الصبوح الشرب بالغداة وهو خلاف الغبوق (sihah)؛ الصبوح شرب الصباح يقال صبحته سقيته صبوحا والمصباح ما يسقى منه (mufradat)
- **B004** günün başında baskın — günün başındaki baskın günü · savaşta onlara günün başında atla vardık · tehlike anında söylenen yardım çağrısı
  يوم الصباح يوم الغارة (maqayis;sihah)؛ في الحرب صبحناهم أي غاديناهم بالخيل ونادوا يا صباحاه إذا استغاثوا (ayn)
- **B005** ışık veren lamba — lamba, kandil ya da lambalık · lambanın kendisi · onunla ışık yakmak ya da onu yakıt yapmak · gök cisimlerinin ışıkları
  سمي المصباح مصباحا لحمرته (maqayis)؛ الصباح السراج بعينه والمصباح المسرجة (jamhara)؛ المصباح السراج وقد استصبحت به إذا أسرجت والشمع مما يصطبح به أي يسرج به (sihah)؛ يقال للسراج مصباح والمصباح مقر السراج والمصابيح أعلام الكواكب (mufradat)
- **B006** kızılımsı parlak güzellik — kızıllıkla toprak rengi arası renk · kızılımsı ya da açık kestane renkte · güzel ve aydınlık yüzlü · saçtaki güçlü kızıllık · demir ve benzeri şeylerde parlaklık
  أصل واحد وهو لون من الألوان أصله الحمرة ووجه صبيح والصبح شدة حمرة في الشعر (maqayis)؛ الصبحة لون بين الحمرة والغبرة ورجل صبيح الوجه جميله (jamhara)؛ الصباحة الجمال ورجل أصبح وأسد أصبح بين الصبح والأصبح قريب من الأصهب (sihah)؛ الصبح شدة حمرة في الشعر وقيل صبح فلان أي وضؤ (mufradat)
- **B007** günün başı uykusu — günün başında ya da gün aydınlanınca uyuma
  التصبح النوم بالغداة (maqayis;mufradat)؛ الصبحة النوم بالغداة (jamhara)؛ ينام الصبحة أي ينام حين يصبح (sihah)
- **B008** gün doğana dek çöken deve — çökülü yerinden gün başına kadar kalkmayan dişi deve · gün başına kadar çökülü kalan dişi develer
  المصباح الناقة تبرك في معرسها فلا تنبعث حتى تصبح (maqayis)؛ ناقة مصباح والجمع مصابيح وهي التي تصبح في مبركها (jamhara)؛ المصباح الناقة التي تصبح في مبركها ولا ترتعي حتى يرتفع النهار (sihah)؛ من الإبل ما يبرك فلا ينهض حتى يصبح (mufradat)
- **B009** gün başı zaman kalıbı [kalıp] — her günün başında, gelme veya görüşme zamanı olarak · beşinci günün başında · belirli bir gün başında görüşme ya da eylem zamanı
  أتيته أصبوحة كل يوم ولقيته ذا صبوح وأتانا لصبح خامسة وصبح خامسة (maqayis)؛ أتيته لصبح خامسة وصبح خامسة وأتيته أصبوحة كل يوم ولقيته صباحا وذا صباح (sihah)
- **B010** bir duruma gelmek — bir duruma geçti, o hale geldi
  الإصباح مصدر أصبح إصباحا مثل قولهم أمسى إمساء (jamhara)؛ أصبح فلان عالما أي صار (sihah)

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 100:3, and ## Buluşmalar) =====
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

## Sabah sulaması ve sudan dönüş

Üçüncü ayetin sabahının yanında, bir baskından çok daha sakin bir sabah işi daha duyulur: {ar:صبحت الإبل إذا سقيتها في أول النهار, tr:sabahtu'l-ibile izâ sekaytehâ fî evveli'n-nehâr, gloss:develeri günün başında suladığında "sabahtu'l-ibil" dersin, source:"ص ب ح,B003"}. Sabahleyin içilen şeyin de bir adı vardır: {ar:الصبوح ما يشرب بالغداة, tr:es-sabûhu mâ yuşrabu bi'l-ğadât, gloss:"sabûh", sabah erkenden içilendir, source:"ص ب ح,B003"}. Dördüncü ayetin kelimesinin ailesinde de durgun su vardır: {ar:نقع الماء في منقعه استقر, tr:neka'a'l-mâu fî menka'ihî isteqarra, gloss:su göletinde durdu, source:"ن ق ع,B001"}. Bu su susuzluğu giderir: {ar:ماء ناقع كأنه استقر قراره فكسر الغلة, tr:mâun nâki'un ke-ennehû isteqarra karâruhû fe-kesera'l-ğulle, gloss:"nâkı'" su, yerine oturup yanan susuzluğu kıran sudur, source:"ن ق ع,B002"}. Fiil de aynı anlamdadır: {ar:نقع الماء غلته إذا أروى عطشه, tr:neka'a'l-mâu ğulletehû izâ ervâ atașeh, gloss:su onun yanan susuzluğunu gidermiş, kandırmıştır, source:"ن ق ع,B002"}. Sekizinci ayetteki sevgi kelimesinin ailesinde ise kanana kadar içmek vardır: {ar:شربت الإبل حتى حببت, tr:şeribeti'l-ibilu hattâ habebet, gloss:develer kanıncaya dek içtiler, source:"ح ب ب,B006"}. Kanmanın da bir başlangıcı vardır: {ar:أول الري التحبب, tr:evvelu'r-riyyi't-tehabbub, gloss:kanmanın ilk aşaması "tehabbub"dur, source:"ح ب ب,B006"}. Onuncu ayetin göğüs kelimesinin ailesi bu sahneyi kapatır: {ar:الصدر الانصراف عن الورد وعن كل أمر, tr:es-sadru'l-insırâfu ani'l-virdi ve an kulli emr, gloss:"sadr", su başından ve her işten ayrılıp dönmektir, source:"ص د ر,B003"}. Kelime en sade haliyle {ar:صدرت الإبل عن الماء, tr:saderati'l-ibilu ani'l-mâ', gloss:develer sudan döndü, source:"ص د ر,B003"} cümlesinde görülür.

Suya iniş ile sudan dönüş, Arapçada iki ayrı fiille anlatılan bir çifttir. Sürü suya gelir, durgun suyun başında kanana kadar içer, sonra döner. Dönüş anı, kimin ne kadar içtiğinin belli olduğu andır. Onuncu ayetin "sudûr" kelimesi anlam olarak göğüslerdir. Ama kelimenin yanında bu dönüş de duyulur: su başında içilen içilmiştir ve şimdi herkes aldığıyla geri döner. Dördüncü ayetin kelimesinin bir deyimi, çok su başı görmüş bir kişiyi tarif eder ve onun bilgisini surenin son kelimesinin fiiliyle anlatır: {ar:إن فلانا لشراب بأنقع يضرب مثلا للرجل الذي قد جرب الأمور وعرفها ومارسها حتى خبرها, tr:inne fulânen le-şerrâbun bi-enku', yudrabu meselen li'r-raculi'llezî kad cerrabe'l-umûra ve arafehâ ve mârasehâ hattâ haberahâ, gloss:"falanca çok göletten içmiştir" sözü, işleri denemiş, tanımış ve onlarla uğraşıp sonunda iç yüzlerini öğrenmiş adam için atasözü olarak söylenir, source:"ن ق ع,B008"}.

Kur'an aynı fiili gerçek bir su başında kullanır. Musa Medyen suyuna vardığında sürülerini sulayan bir kalabalık bulur, onların gerisinde de hayvanlarını geri tutan iki kadın görür. Ne istediklerini sorduğunda kadınlar şöyle der: {ar:لَا نَسْقِى حَتَّىٰ يُصْدِرَ ٱلرِّعَآءُ ۖ وَأَبُونَا شَيْخٌ كَبِيرٌ, tr:lâ neskî hattâ yusdira'r-ri'â', ve ebûnâ şeyhun kebîr, gloss:çobanlar sürülerini sudan çekip götürmedikçe biz sulayamayız; babamız da çok yaşlı biridir, source:28:23}. Aynı kök, yerin altüst edildiği günün anlatımında da geçer. Yer sarsılır, ağırlıklarını dışarı atar, haberlerini anlatır ve sonra {ar:يَوْمَئِذٍ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًا لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:yevme'izin yasduru'n-nâsu eştâten li-yurav a'mâlehum, gloss:o gün insanlar amelleri kendilerine gösterilsin diye bölük bölük dönüp gelirler, source:99:6}. "Yasduru" fiili, sudan dönen sürünün fiili ile göğüs kelimesiyle aynı köktendir. İnsanlar, yeryüzünün bir su başı gibi bırakıldığı o günde, içtiklerini görmeye döner.

Kaynaklar: 100:3 صُبْحًا ص ب ح B003; 100:4 نَقْعًا ن ق ع B001; 100:4 نَقْعًا ن ق ع B002; 100:4 نَقْعًا ن ق ع B008; 100:8 لِحُبِّ ح ب ب B006; 100:10 ٱلصُّدُورِ ص د ر B003; 28:23; 99:6

## Buluşmalar

İlk buluşma, surenin açılış sahnesinde koşan at ile şafak baskını arasındadır. Koşanların tanımı zaten baskın yapanlardır: {ar:العادية الخيل المغيرة, tr:el-âdiyetu'l-haylu'l-muğîra, gloss:"âdiye", baskın yapan atlardır, source:"ع د و,B001"}. Sekizinci ayetin "şedd" kelimesi de iki görüntüyü aynı anda taşır. Bir yanda koşudur, öbür yanda düşmana saldırıdır: {ar:شد على العدو إذا حمل عليه, tr:şedde ale'l-aduvvi izâ hamele aleyh, gloss:düşmana saldırdığında "şedde" denir, source:"ش د د,B003"}. Aynı sahnede ateş görüntüsü de yer alır. Soluk soluğa koşan hayvanların ayakları taşlara çarparak kıvılcım çıkarır. Birinci ayetin kelimesi bir yandan bu soluğu, bir yandan da yanmış çakmak taşını adlandırır. Koşu, kıvılcım ve sabah tek bir hareketin ardışık parçalarıdır.

Surenin iki yarısını birbirine bağlayan asıl buluşma, dördüncü ayetin tozu ile dokuzuncu ayetin kabirleri arasındadır. Toynakların toprağı kaldırması ile kabirlerin altüst edilmesi aynı fiille açıklanır: "bu'sira", "usîra" demektir. Böylece surenin ilk yarısındaki sabah baskını, ikinci yarısındaki altüst oluşun bir ön provası olur. Kur'an da kabirlerden çıkışı bir koşu olarak anlatır: {ar:يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًا كَأَنَّهُمْ إِلَىٰ نُصُبٍ يُوفِضُونَ, tr:yevme yahrucûne mine'l-ecdâsi sirâ'an ke-ennehum ilâ nusubin yûfidûn, gloss:kabirlerden hızla çıkacakları, sanki dikili bir hedefe koşuyorlarmış gibi seğirtecekleri gün, source:70:43}. Bir başka yerde de {ar:يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًا, tr:yevme teşakkaku'l-ardu anhum sirâ'â, gloss:yerin yarılıp onların hızla çıktığı gün, source:50:44} denir. Surenin başında koşanlar atlardır. Sonunda ise koşanlar kabirlerden çıkan insanlardır. Bu insanların gittiği yer de beşinci ayetteki gibi bir topluluğun ortasıdır, ama bu kez bütün insanların toplandığı yerdir.

Ateş ile kabir de aynı kökte buluşur. İkinci ayetin "ateşi çıkarmak" fiili ile gömmenin "örtmek" fiili aynı köktendir. Kur'an ateşi dirilişe delil olarak da kullanır. Çakılan ateşe dair soru dirilişi inkâr edenlere sorulur. Yeşil ağaçtan çıkan ateş de çürümüş kemikleri kimin dirilteceğini soran kişiye verilen cevaptır. Tahtanın içinde gizli duran ateş çakılınca dışarı çıkar, toprağın içinde gizli duran insan da altüst edilince dışarı çıkar. Yağmur sahnesi de aynı yere varır. İyi toprak ile kıt ürün veren toprağı karşılaştıran ayetten hemen önce şöyle denir: {ar:كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:kezâlike nuhrici'l-mevtâ le'allekum tezekkerûn, gloss:ölüleri de böyle çıkarırız; belki düşünüp öğüt alırsınız, source:7:57}. Kenûd toprak bitki bitirmez. Ama sonunda kabirleri altüst edilecek olan da aynı topraktır.

Biriktirilen mal ile göğsün ayıklanması da bir sahnede buluşur. Onuncu ayetin fiilinin aslı, altını maden toprağından ayırmaktır. Biriktirenin malı ise toplanmış altın ve gümüştür. Kur'an bu iki şeyi ateşte birleştirir: {ar:وَٱلَّذِينَ يَكْنِزُونَ ٱلذَّهَبَ وَٱلْفِضَّةَ وَلَا يُنفِقُونَهَا فِى سَبِيلِ ٱللَّهِ, tr:ve'llezîne yeknizûne'z-zehebe ve'l-fiddate ve lâ yunfikûnehâ fî sebîli'llâh, gloss:altın ve gümüşü yığıp Allah yolunda harcamayanlar, source:9:34}; {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhuhum ve cunûbuhum ve zuhûruhum, gloss:o gün bunlar cehennem ateşinde kızdırılır ve alınları, yanları ve sırtları onlarla dağlanır, source:9:35}. Malın bağlılığı ile göğsün içindekinin çıkarılması da tek bir ayette bir aradadır: {ar:إِن يَسْـَٔلْكُمُوهَا فَيُحْفِكُمْ تَبْخَلُوا۟ وَيُخْرِجْ أَضْغَٰنَكُمْ, tr:in yes'elkumûhâ fe-yuhfikum tebhalû ve yuhric adğânekum, gloss:onları (mallarınızı) sizden isteyip ısrar etseydi cimrilik ederdiniz ve O da kinlerinizi dışarı çıkarırdı, source:47:37}. Sevgi kelimesinin "kalbin tanesi" anlamı da bu buluşmayı kelimenin içinden kurar. İnsanın şiddetle bağlandığı mal göğsün içindeki tanedir, harman savrulduğunda ayrılacak olan da odur. Beşinci ayetin kökü de aynı sahnede iki yönde işler. Mal toplayan, yumruğunu sıkan kişi sonunda toplanma gününde toplananlardan biri olur. Onuncu ayetin fiili de bir toplamadır.

Sabah baskını ile malı esirgeme de bir Kur'an sahnesinde birleşir. Bir bahçenin sahipleri ürünü sabahleyin devşireceklerine yemin ederler: {ar:إِذْ أَقْسَمُوا۟ لَيَصْرِمُنَّهَا مُصْبِحِينَ, tr:iz aksemû le-yasrimunnehâ musbihîn, gloss:onu sabaha girerken mutlaka devşireceklerine yemin ettiklerinde, source:68:17}. Onlar uyurken {ar:فَطَافَ عَلَيْهَا طَآئِفٌ مِّن رَّبِّكَ وَهُمْ نَآئِمُونَ, tr:fe-tâfe aleyhâ tâifun min rabbike ve hum nâimûn, gloss:onlar uykudayken Rabbinden bir bela bahçeyi sardı, source:68:19}. Bahçe {ar:فَأَصْبَحَتْ كَٱلصَّرِيمِ, tr:fe-asbahat ke's-sarîm, gloss:sabaha kapkara kesilmiş halde girdi, source:68:20}. Habersiz sahipler ise {ar:فَتَنَادَوْا۟ مُصْبِحِينَ, tr:fe-tenâdev musbihîn, gloss:sabaha girerken birbirlerine seslendiler, source:68:21}. Konuştukları şey şudur: {ar:أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌ, tr:en lâ yedhulennehe'l-yevme aleykum miskîn, gloss:bugün oraya hiçbir yoksul yanınıza girmesin, source:68:24}. Bu sahnede bir sabah seferi, yoksula kapanan bir el ve Rabbin cevabı vardır. Sabah baskını yapan, sonunda baskına uğrayan olur. Bizim surede de "yalnız yiyen" kenûd, "sabah" sözüyle başlayan bir surenin sonunda Rabbinin bilgisi karşısında durur.

Su başı ile toprağın altüst edilmesi aynı günün anlatımında buluşur. Yerin sarsıldığı ve ağırlıklarını dışarı attığı gün, insanların {ar:يَصْدُرُ, tr:yasduru, gloss:sudan döner gibi döner, source:99:6} günüdür. Fiil onuncu ayetin göğüs kelimesiyle aynı köktendir. Kabirden çıkış, gömülü olanın açılması ve sudan dönüş tek bir anda birleşir. İnsanlar amellerini görmek için bölük bölük döner.

Tanıklık ile Rab sözü ise yedinci ayetin iki okumasını bir araya getirir. Âdem oğullarının "Rabbiniz değil miyim" sorusuna "evet, tanık olduk" diye cevap verdiği sahnede, insan kendi Rabbine dair kendisi üzerine tanıktır. Bizim surede de aynı insan, Rabbine karşı nankörlüğü üzerine tanıktır. Birinci ayetin atının tanığı ise koşusudur ve onun öne geçtiğine tanıklık eder. Aynı kelime atta lehte, insanda aleyhte işler.

Bu buluşmalar surenin hareketini dışarıdan içeriye doğru taşır. Sure, gözle görülen ve kulakla işitilen şeylerle başlar: soluk, kıvılcım, sabah ışığı, toz ve kalabalık. Sonra göze görünmeyen bir yere, göğüsteki taneye ulaşır. Toynakların kaldırdığı toprak kabirlerin toprağına, baskının sabahı toplanma gününe, yağmurun beklendiği tarla kabirlerini açan yere dönüşür. Malın düğümü ve yumulmuş el de toplanıp ayıklanan bir göğse dönüşür. Bu yolun her aşamasında bilgi de derinleşir: önce hazır bulunan ve gören bir tanık vardır, sonra sorulan ama cevaplanmayan bir bilgi, en sonda da içini bilen bir Rab.

