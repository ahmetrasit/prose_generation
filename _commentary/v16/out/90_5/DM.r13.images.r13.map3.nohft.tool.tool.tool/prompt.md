Focus: 90:5. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/90_5/D.r13/context.md =====
# 90:5 — focus

أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ

Anchor translation (canonical reading, reference only):

Kimsenin ona güç yetiremeyeceğini mi sanıyor?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | أَيَحْسَبُ | حَسِبَ | ح س ب | INTG;V |
| 2 | أَن | أَن |  | SUB |
| 3 | لَّن | لَن |  | NEG |
| 4 | يَقْدِرَ | قَدَرَ | ق د ر | V |
| 5 | عَلَيْهِ | عَلَىٰ |  | P;PRON |
| 6 | أَحَدٌ | أَحَد | ء ح د | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 90 — full text (context; no pericope)

- 90:1 لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ
- 90:2 وَأَنتَ حِلٌّۢ بِهَٰذَا ٱلْبَلَدِ
- 90:3 وَوَالِدٍۢ وَمَا وَلَدَ
- 90:4 لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِى كَبَدٍ
- 90:5 ◀ focus أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ
- 90:6 يَقُولُ أَهْلَكْتُ مَالًۭا لُّبَدًا
- 90:7 أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ
- 90:8 أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ
- 90:9 وَلِسَانًۭا وَشَفَتَيْنِ
- 90:10 وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ
- 90:11 فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ
- 90:12 وَمَآ أَدْرَىٰكَ مَا ٱلْعَقَبَةُ
- 90:13 فَكُّ رَقَبَةٍ
- 90:14 أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ
- 90:15 يَتِيمًۭا ذَا مَقْرَبَةٍ
- 90:16 أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ
- 90:17 ثُمَّ كَانَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ وَتَوَاصَوْا۟ بِٱلصَّبْرِ وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ
- 90:18 أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ
- 90:19 وَٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا هُمْ أَصْحَٰبُ ٱلْمَشْـَٔمَةِ
- 90:20 عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ


===== _commentary/v16/work/90_5/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ح س ب (root_000318) — identity root of أَيَحْسَبُ (w1)

- **B001** sayarak nicelik belirleme — nesneyi saymak ve niceliğini çıkarmak · sayma ve nicelik belirleme işlemi · sayma işlemi · sayı yoluyla belirleme · belirli sayı düzeni ve zaman ölçüsü · ölçmeden, denetlemeden veya kısmadan; beklenenden fazla · sayıp değerlendiren ve gözeten
  الأول العد؛ الحساب عدك الأشياء؛ حسبت الحساب؛ حسبته إذا عددته؛ الحساب استعمال العدد؛ الشمس والقمر بحسبان
- **B002** öyle olduğunu sanmak — öyle sanmak ve zihnen öyle olduğuna hükmetmek · sanı ve kesin olmayan yargı
  الحسبان الظن؛ حسبت كذا في معنى ظننت؛ حسبته صالحا أي ظننته؛ حسبت الشيء ظننته؛ الحسبان أن يحكم لأحد النقيضين
- **B003** gereksinimi karşılayacak kadar yetmek — bu sana yeter; bununla yetin · Tanrı bize yeter · bu bana yetti · ona yetecek veya onu hoşnut edecek kadar vermek · yeterli ya da bol armağan · ölçmeden, denetlemeden veya kısmadan; beklenenden fazla · soyluluk ile yeterlik arasında iki türlü yorumlanan şiir sözü
  الأصل الثاني الكفاية؛ حسبك هذا أي كفاك؛ حسبي كذا أي يكفيني؛ أحسبني الشيء أي كفاني؛ حسبنا الله أي كافينا هو؛ عطاء حسابا أي كافيا
- **B004** atalardan gelen saygınlık ve iyi işler birikimi — atalardan gelen saygınlık ve övünülecek işler · soylu, saygın veya eli açık kişi · soyluluk ya da yeterlik diye yorumlanan şiir sözü
  الحسب الذي يعد من الإنسان؛ الحسب الشرف الثابت في الآباء؛ حسب الرجل مآثر آبائه وأجداده؛ ما يعده الإنسان من مفاخر آبائه؛ الحسب الفعال الحسن له ولآبائه
- **B005** Tanrı katında karşılığını beklemek — bir işi veya kaybı Tanrı katında değer hanesine yazıp karşılığını beklemek · Tanrı katında karşılık umularak yapılan iş
  احتسب فلان ابنه؛ احتسابك الأجر؛ احتسب فلان عند الله خيرا؛ احتسبت بكذا أجرا عند الله؛ احتسب ابنا له أي اعتد به عند الله؛ الحسبة فعل ما يحتسب به عند الله تعالى
- **B006** işi gözetme, kötü davranışı sorgulama ve kamusal denetim — kötü davranışından dolayı kınamak ve yaptığını sorgulamak · işi iyi çekip çevirmek ve gözetmek · kentte kamu düzenini ve davranışları gözeten görevli
  حسن الحسبة بالأمر إذا كان حسن التدبير؛ احتسب فلان على فلان أنكر عليه قبيحا عمله؛ احتسبت عليه كذا إذا أنكرته عليه؛ فلان محتسب البلد؛ حسن الحسبة في الأمر
- **B007** kısa ok veya yukarıdan gelen yıkıcı gönderim — kısa oklar veya atılan küçük nesneler · gökten gönderilen dolu, ateş, çekirge ya da yıkıcı şey
  الحسبان سهام صغار؛ حسبان من السماء بالبرد؛ حسبانا من السماء أي نارا تحرقها؛ حسبانا عذابا ولا أدري؛ الحسبان بالضم العذاب؛ أصاب الأرض حسبان أي جراد؛ الحسبان المرامي؛ نارا وعذابا
- **B008** yalıtık adlandırmalar — küçük yastık · deriden yapılmış veya baş altına konan yastık · birini yastığa oturtmak veya başına yastık koymak · yastıksız; bazı açıklamalarda ölü sargısına sarılmamış, gömülmemiş ya da onurlandırılmamış
  الحسبان جمع حسبانة وهي الوسادة الصغيرة؛ الحسبان سهام قصار؛ الحسبانة أيضا الوسادة الصغيرة؛ المحسبة وسادة من أدم؛ حسبته إذا وسدته؛ الحسبانة الوسادة الصغيرة
- **B009** deri veya tüyde karışık ak, kızıl ve koyu görünüm — derisi hastalıkla beyazlamış ya da tüyünde aklık, kızıllık ve koyuluk karışmış kişi veya deve · koyu zemin üstünde bozluk ya da kızıla çalan karalık
  الأحسب الذي ابيضت جلدته من داء؛ الأحسب من الناس والإبل وهو الأبرص؛ الحسبة غبرة في كدرة؛ الأحسب من الإبل فيه بياض وحمرة؛ الحسبة سواد يضرب إلى الحمرة
- **B010** yalıtık adlandırmalar — haberi sorup izini sürmek · birinin elinde ne olduğunu sınayıp öğrenmek
  بغير أن حسب المعطى أنه يعطيه؛ تحسبت الخبر أي استخبرت؛ احتسبت فلانا اختبرت ما عنده؛ يتحسب الأخبار أي يتحسسها ويطلبها

## ق د ر (root_001205) — identity root of يَقْدِرَ (w4)

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

## ء ح د (root_000017) — identity root of أَحَدٌ (w6)

- **B001** tek ve eşi olmayan olma — bir tane; tek ve eşsiz · yalnız bir, yalnız bir
  أحد فرع والأصل الواو وحد (maqayis); أحد بمعنى الواحد وهو أول العدد (sihah); قل هو الله أحد (sihah;mufradat); يستعمل مطلقا وصفا في وصف الله تعالى وأصله وحد (mufradat); أحد أحد (sihah)
- **B002** hiç kimse — olumsuzlukta hiç kimse
  لا أحد في الدار؛ ما في الدار أحد (sihah); أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا اثنان فصاعدا (mufradat); فما منكم من أحد عنه حاجزين (sihah;mufradat)
- **B003** bir sayısı, onlu kuruluşları ve on bire çıkarma — saymanın başlangıcındaki bir · on bir, on bir dişil biçimi ve yirmi bir · onları on bire çıkarmak
  أحد واثنان وأحد عشر وإحدى عشرة (sihah); الواحد المضموم إلى العشرات نحو أحد عشر وأحد وعشرين (mufradat); فأحدهن أي صيرهن أحد عشر (sihah)
- **B004** iki kişiden biri, ilk olan ve haftanın ilk günü — ikinizden biri · Pazar günü · Pazar günleri
  أن يستعمل مضافا أو مضافا إليه بمعنى الأول (mufradat); أما أحدكما (mufradat); يوم الأحد أي يوم الأول (mufradat); يوم الأحد يجمع على آحاد (sihah)
- **B005** tek başına kalma ve birer birer gelme — tek başına kalmak; işi yalnız üstlenmek · birer birer, ayrı ayrı
  ما استأحدت بهذا الأمر أي ما انفردت به (maqayis); استأحد الرجل انفرد (sihah); جاءوا آحاد أحاد (sihah)
- **B006** Medine'deki belirli bir dağın özel adı — Medine'deki dağın özel adı
  أحد جبل بالمدينة (sihah)

===== _commentary/v16/out/s090/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 90:5, and ## Buluşmalar) =====
## Harcanan mal: övünme, gösteriş ve hesap

Altıncı ayet bir sözdür. Adam konuşur: {ar:يَقُولُ, tr:yekûlu, gloss:der, source:90:6}. Sözün kökü dilden çıkan sesi bildirir: {ar:القول من النطق, tr:el-kavlu mine'n-nutk, gloss:kavl konuşmadandır, source:"ق و ل,B001"}. Aynı kök, insanlar arasında yayılan adı da bildirir: {ar:انتشرت له قالة حسنة أو قبيحة في الناس, tr:inteşeret lehû kâletun hasenetun ev kabîhatun fi'n-nâs, gloss:insanlar arasında onun hakkında iyi ya da kötü bir söz yayıldı, source:"ق و ل,B007"}. Övünme bu yayılmayı hedefler. Söylenen şey {ar:أَهْلَكْتُ مَالًۭا, tr:ehlektu mâlen, gloss:mal tükettim, source:90:6} sözüdür. Fiil bir şeyin yok olmasının bütün yollarını kapsar: {ar:الهلاك على أوجه افتقاد الشيء واستحالة وفساد والموت وبطلان الشيء وعدمه, tr:el-helâku alâ evcuh iftikâdu'ş-şey' ve'stihâle ve fesâd ve'l-mevt ve butlânu'ş-şey' ve ademuh, gloss:helak birkaç türlüdür: kaybolmak ve bozulmak ve ölüm ve bir şeyin boşa çıkıp yok olması, source:"ه ل ك,B001"}. Mal da edinilip tutulan şeydir: {ar:تمول الرجل اتخذ مالا, tr:temevvele'r-racul ittehaze mâlâ, gloss:adam mal edindi, source:"م و ل,B001"}. Bu kelimenin eski dünyasında mal çoğunlukla sürüdür: {ar:كانت أموال العرب أنعامهم, tr:kânet emvâlu'l-arabi en'âmehum, gloss:Arapların malları hayvanlarıydı, source:"م و ل,B001"}. Adamın övündüğü şey bir harcama değil, bir yok edişin sayımıdır. Hesabı tutulan yalnızca miktardır, nereye gittiği değil.

Yedinci ayet bu sözü bir soruyla karşılar: {ar:أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ, tr:e-yahsebu en lem yerahû ehad, gloss:onu hiç kimsenin görmediğini mi sanıyor, source:90:7}. "Görmek" fiilinin ailesinde gösteriş de vardır: {ar:وهو أن يفعل شيئا ليراه الناس, tr:ve huve en yef'ale şey'en li-yerâhu'n-nâs, gloss:insanlar görsün diye bir şey yapmaktır, source:"ر ء ي,B005"}. Sahnenin içindeki çelişki böylece görünür olur: harcamasının insanlarca görülmesini isteyen adam, kendisinin görülmediğini sanır. "Yahsebu" fiilinin kökü de aynı çifte işler. Bir yanda insanın sayılan şerefi vardır: {ar:الحسب الذي يعد من الإنسان, tr:el-hasebu'llezî yu'addu mine'l-insân, gloss:haseb insandan sayılıp dökülen şeydir, source:"ح س ب,B004"}. Bir başka söyleyiş de {ar:ما يعده الإنسان من مفاخر آبائه, tr:mâ yeudduhu'l-insânu min mefâhiri âbâih, gloss:insanın atalarının övünç konularından saydığı şeyler, source:"ح س ب,B004"}. Öbür yanda bunun tam tersi bir sayım vardır: {ar:احتسبت بكذا أجرا عند الله, tr:ihtesebtu bi-kezâ ecran indallâh, gloss:şunu Allah katında ecir olarak hesaba yazdım, source:"ح س ب,B005"}. Kaybedileni ya da verileni Allah'ın hesabına yazmak, övünmenin sayımının karşıtıdır. Ayetteki fiil ise ikisinin de yerine geçen sanıdır: {ar:الحسبان الظن, tr:el-husbânu'z-zann, gloss:husbân sanıdır, source:"ح س ب,B002"}. Kök bir de gökten inen ateşi adlandırır: {ar:حسبانا من السماء أي نارا تحرقها, tr:husbânen mine's-semâ ey nâran tuhrikuhâ, gloss:gökten bir husbân yani onu yakan bir ateş, source:"ح س ب,B007"}.

Sekizinci ve dokuzuncu ayetler insana verilen araçları sayar: {ar:وَلِسَانًۭا وَشَفَتَيْنِ, tr:ve lisânen ve şefeteyn, gloss:ve bir dil ve iki dudak, source:90:9}. Bu iki kelimenin ailesi de övgü dilini bilir: {ar:لسان الناس عليك ثناؤهم, tr:lisânu'n-nâsi aleyke senâuhum, gloss:insanların senin üzerine dili onların seni övmesidir, source:"ل س ن,B006"}. Bir başka söyleyiş de {ar:له في الناس شفة أي ثناء حسن, tr:lehû fi'n-nâsi şefe ey senâun hasen, gloss:onun insanlar arasında bir dudağı var yani güzel bir anılışı, source:"ش ف ه,B004"}. Övünen adamın istediği tam budur: insanların dilinde ve dudağında olmak. Ama dudağın ailesinde bir başka adam da vardır: {ar:رجل مشفوه إذا كثر سؤال الناس إياه حتى نفذ ما عنده, tr:raculun meşfûh izâ kesura suâlu'n-nâsi iyyâh hattâ nefize mâ indeh, gloss:insanlar ondan o kadar çok istedi ki elindeki tükendi, source:"ش ف ه,B003"}. Malın gerçekten tükenmesi de böyle olur: birçok ağız ister, el verir, elde bir şey kalmaz. Övünmenin "tükettim"i ile verenin tükenişi aynı kelimeyle söylenebilir, ama farklı iki sahnedir.

Kur'an bu sahneyi birçok kez kurar. Allah müminlere {ar:لَا تُبْطِلُوا۟ صَدَقَٰتِكُم بِٱلْمَنِّ وَٱلْأَذَىٰ كَٱلَّذِى يُنفِقُ مَالَهُۥ رِئَآءَ ٱلنَّاسِ, tr:lâ tubtılû sadakâtikum bi'l-menni ve'l-ezâ ke'llezî yunfiku mâlehû riâe'n-nâs, gloss:sadakalarınızı başa kakma ve eziyetle boşa çıkarmayın tıpkı malını insanlara gösteriş için harcayan gibi, source:2:264} der. Aynı ayetin sonunda bu harcayanlar için {ar:لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟, tr:lâ yakdirûne alâ şey'in mimmâ kesebû, gloss:kazandıklarından hiçbir şeye güç yetiremezler, source:2:264} denir. Gösteriş harcaması, beşinci ayetin "kadara" fiiliyle biter. Aynı figür başka bir yerde de görünür: {ar:وَٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ رِئَآءَ ٱلنَّاسِ, tr:vellezîne yunfikûne emvâlehum riâe'n-nâs, gloss:mallarını insanlara gösteriş için harcayanlar, source:4:38}. Yetimi iten ve yoksulun yemeğine teşvik etmeyen kişinin anlatıldığı surede de iki kusur yan yana gelir: {ar:ٱلَّذِينَ هُمْ يُرَآءُونَ, tr:ellezîne hum yurâûn, gloss:onlar gösteriş yaparlar, source:107:6} ve {ar:وَيَمْنَعُونَ ٱلْمَاعُونَ, tr:ve yemne'ûne'l-mâ'ûn, gloss:ve en küçük yardımı esirgerler, source:107:7}. Allah'ın kınadığı mal yığıcının sahnesinde de aynı iki fiil vardır: {ar:ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ, tr:ellezî ceme'a mâlen ve addedeh, gloss:mal toplayıp onu sayan, source:104:2} ve {ar:يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ, tr:yahsebu enne mâlehû ahledeh, gloss:malının onu ebedî kılacağını sanır, source:104:3}. Saymak ve sanmak yine yan yanadır.

İki adam misalinde, bağının sahibi bağına girer ve {ar:مَآ أَظُنُّ أَن تَبِيدَ هَٰذِهِۦٓ أَبَدًۭا, tr:mâ ezunnu en tebîde hâzihî ebedâ, gloss:bunun hiç yok olacağını sanmıyorum, source:18:35} der. Arkadaşı Rabbinin {ar:وَيُرْسِلَ عَلَيْهَا حُسْبَانًۭا مِّنَ ٱلسَّمَآءِ, tr:ve yursile aleyhâ husbânen mine's-semâ, gloss:ve onun üstüne gökten bir husbân göndermesini, source:18:40} umar. Sonunda bağ sahibi {ar:يُقَلِّبُ كَفَّيْهِ عَلَىٰ مَآ أَنفَقَ فِيهَا, tr:yukallibu keffeyhi alâ mâ enfeka fîhâ, gloss:oraya harcadıkları için ellerini ovuşturur, source:18:42} ve {ar:يَٰلَيْتَنِى لَمْ أُشْرِكْ بِرَبِّىٓ أَحَدًۭا, tr:yâ leytenî lem uşrik bi-rabbî ehadâ, gloss:keşke Rabbime kimseyi ortak koşmasaydım, source:18:42} der. Harcanan mal, sanı, gökten gelen ateş ve "ehad" kelimesi tek bir sahnede toplanır. Kitabı sol eline verilen adam da kendi sözüyle konuşur: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ, tr:mâ ağnâ annî mâliyeh, gloss:malım bana bir yarar sağlamadı, source:69:28} ve {ar:هَلَكَ عَنِّى سُلْطَٰنِيَهْ, tr:heleke annî sultâniyeh, gloss:gücüm benden yok olup gitti, source:69:29}. Altıncı ayette "tükettim" diyen fiil, o gün adamın kendisinden tükenen gücü anlatır. Kendisine hazineler verilen Karun da malı için {ar:إِنَّمَآ أُوتِيتُهُۥ عَلَىٰ عِلْمٍ عِندِىٓ, tr:innemâ ûtîtuhû alâ ilmin indî, gloss:bu bana ancak bendeki bir bilgi sayesinde verildi, source:28:78} der. Aynı ayet fiili bu kez Allah'ı özne yaparak kullanır: {ar:أَوَلَمْ يَعْلَمْ أَنَّ ٱللَّهَ قَدْ أَهْلَكَ مِن قَبْلِهِۦ, tr:e-ve lem ya'lem ennallâhe kad ehleke min kablih, gloss:Allah'ın ondan önce nicelerini helak ettiğini bilmiyor muydu, source:28:78}. Kendini görmek de bir tehlike olarak anılır: {ar:كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ, tr:kellâ inne'l-insâne le-yatğâ, gloss:hayır insan gerçekten azar, source:96:6} ve {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en reâhu'steğnâ, gloss:kendini yeterli gördüğünde, source:96:7}. Yığılmış malın sonu da açıkça söylenir: {ar:هَٰذَا مَا كَنَزْتُمْ لِأَنفُسِكُمْ فَذُوقُوا۟ مَا كُنتُمْ تَكْنِزُونَ, tr:hâzâ mâ kenaztum li-enfusikum fe-zûkû mâ kuntum teknizûn, gloss:işte kendiniz için biriktirdiğiniz bu; biriktirdiğinizi tadın, source:9:35}.

Karşıt söz de Kur'an'da vardır. Doyuranlar şöyle konuşur: {ar:إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءًۭ وَلَا شُكُورًا, tr:innemâ nut'imukum li-vechillâhi lâ nurîdu minkum cezâen ve lâ şukûrâ, gloss:sizi yalnızca Allah'ın yüzü için doyuruyoruz; sizden ne bir karşılık ne de bir teşekkür istiyoruz, source:76:9}. Malını veren sakınan kişi için de {ar:ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ, tr:ellezî yu'tî mâlehû yetezekkâ, gloss:arınmak için malını veren, source:92:18} ve {ar:إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ, tr:illebtiğâe vechi rabbihi'l-a'lâ, gloss:yalnızca yüce Rabbinin yüzünü arayarak, source:92:20} denir. Harcayıp başa kakmayanlar da şöyle anılır: {ar:ثُمَّ لَا يُتْبِعُونَ مَآ أَنفَقُوا۟ مَنًّۭا وَلَآ أَذًۭى, tr:summe lâ yutbi'ûne mâ enfekû mennen ve lâ ezâ, gloss:sonra harcadıklarının ardından ne başa kakma ne eziyet getirirler, source:2:262}. Dilin doğru övgüsü de vardır. İbrahim Rabbinden {ar:وَٱجْعَل لِّى لِسَانَ صِدْقٍۢ فِى ٱلْءَاخِرِينَ, tr:vec'al lî lisâne sıdkın fi'l-âhirîn, gloss:sonrakiler arasında benim için doğru bir dil kıl, source:26:84} diye ister. Övünen adam bu dili kendi sözüyle almaya çalışır, İbrahim ise onu Rabbinden ister.

Kaynaklar: 90:6 يَقُولُ ق و ل B001, B007; 90:6 أَهْلَكْتُ ه ل ك B001; 90:6 مَالًۭا م و ل B001; 90:6 لُّبَدًا ل ب د B002; 90:7 يَرَهُۥٓ ر ء ي B005; 90:5 أَيَحْسَبُ ح س ب B002, B004, B005, B007; 90:7 أَيَحْسَبُ ح س ب B002, B004, B005; 90:9 وَلِسَانًۭا ل س ن B006; 90:9 وَشَفَتَيْنِ ش ف ه B003, B004

## Ölçüp biçmek: yaratma, güç ve pay

Dördüncü ayetin fiili {ar:خَلَقْنَا, tr:halaknâ, gloss:yarattık, source:90:4}, Arapçada önce bir zanaat işidir: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme izâ kaddertuhû kable'l-kat', gloss:deriyi kesmeden önce ölçüp biçtiğimde onu halakttım, source:"خ ل ق,B001"}. Bir başka söyleyiş de {ar:خلقت الأديم للسقاء إذا قدرته, tr:halaktu'l-edîme li's-sikâ izâ kaddertuh, gloss:deriyi su tulumu için ölçtüm, source:"خ ل ق,B001"}. Usta deriyi serer, üstüne tulumun şeklini çizer, sonra keser. Kelimenin özü de böyle tanımlanır: {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhu't-takdîru'l-mustekîm, gloss:yaratmanın aslı doğru ölçüdür, source:"خ ل ق,B001"}. Aynı kökten gelen "halâk" kelimesi ise payı adlandırır: {ar:الخلاق النصيب لأنه قد قدر لكل أحد نصيبه, tr:el-halâku'n-nasîb li-ennehû kad kuddira li-kulli ehadin nasîbuh, gloss:halâk paydır çünkü herkese payı ölçülmüştür, source:"خ ل ق,B006"}. Bu tek tanımda surenin üç kelimesi buluşur: yaratma, beşinci ayetin "kadara"sı ve beşinci ile yedinci ayetlerin "ehad"ı. Sekizinci ayetin {ar:أَلَمْ نَجْعَل, tr:e-lem nec'al, gloss:yapmadık mı, source:90:8} fiili de aynı işe bağlanır: {ar:جعل خلق؛ خلقنا, tr:ce'ale haleka; halaknâ, gloss:ce'ale yarattı demektir; yarattık, source:"ج ع ل,B001"}. Gözler, dil ve dudaklar ölçülerek kesilmiş parçalardır.

Beşinci ayet adamın sanısını söyler: {ar:أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ, tr:e-yahsebu en len yakdira aleyhi ehad, gloss:kimsenin ona güç yetiremeyeceğini mi sanıyor, source:90:5}. "Kadara" önce güçtür: {ar:قدر على الشيء قدرة أي ملك فهو قادر, tr:kadara ale'ş-şey'i kudreten ey meleke fe-huve kâdir, gloss:bir şeye güç yetirdi yani ona sahip oldu, source:"ق د ر,B003"}. Ama kökün altında ölçü yatar: {ar:مبلغ الشيء وكنهه ونهايته, tr:mebleğu'ş-şey'i ve kunhuhû ve nihâyetuh, gloss:bir şeyin vardığı yer ve özü ve sınırı, source:"ق د ر,B001"}. Allah'ın takdiri de bu ölçüyle tanımlanır: {ar:قضاء الله تعالى الأشياء على مبالغها ونهاياتها, tr:kadâullâhi te'âle'l-eşyâe alâ mebâliğihâ ve nihâyâtihâ, gloss:Allah'ın şeyleri ulaşacakları ölçüye ve sınıra göre belirlemesi, source:"ق د ر,B002"}. Fiil "ona karşı" ile kurulduğunda bir de rızkı daraltmayı anlatır: {ar:ومن قدر عليه رزقه أي ضيق عليه, tr:ve men kudira aleyhi rizkuhû ey duyyika aleyh, gloss:rızkı ona ölçülü verilen yani daraltılan, source:"ق د ر,B004"}. İnsanın kendi kurduğu hesap da aynı kökle anılır: {ar:التقدير من الإنسان التفكر في الأمر؛ فكر وقدر, tr:et-takdîru mine'l-insâni't-tefekkuru fi'l-emr; fekkera ve kaddera, gloss:insanın takdiri iş üzerine düşünmesidir; düşündü ve ölçtü, source:"ق د ر,B005"}. Adam, kendisini ölçecek ya da kendisine bir sınır çizecek kimse bulunmadığını sanır. Oysa dördüncü ayetin fiili onun zaten ölçülüp biçildiğini söylemiştir. Düz bir anlatımın kaçırdığı şey budur: "kimse bana güç yetiremez" sanısı, deri gibi ölçülüp kesilmiş bir varlığın ağzından çıkar.

Birinci ayetin yemin fiili {ar:لَآ أُقْسِمُ, tr:lâ uksimu, gloss:yemin ederim ki, source:90:1} de bu işin içine girer. Kökü bölüp paylaştırmayı anlatır: {ar:تجزئة شيء والنصيب قسم, tr:tecziyetu şey' ve'n-nasîbu kısm, gloss:bir şeyi parçalara ayırmak ve pay kısımdır, source:"ق س م,B003"}. Kök insanın kendi işini tartmasını da anlatır ve bunu "kadara" ile tanımlar: {ar:هو يقسم أمره قسما أي يقدره وينظر فيه كيف يفعل, tr:huve yaksimu emrahû kasmen ey yukaddiruhû ve yenzuru fîhi keyfe yef'al, gloss:işini bölüp tartıyor yani onu ölçüyor ve nasıl yapacağına bakıyor, source:"ق س م,B006"}. Böylece birinci, dördüncü ve beşinci ayetler tek bir işlemde buluşur: ölçmek ve paylaştırmak. Sanı ile sayım arasındaki fark da aynı fiilde durur. Kök hem saymayı ({ar:الحساب عدك الأشياء, tr:el-hisâbu addukel-eşyâ, gloss:hesap şeyleri saymandır, source:"ح س ب,B001"}) hem sanmayı bildirir. Adam saymak yerine sanır. "Ehad" kelimesinin olumsuz cümledeki işi de açıktır: {ar:أحد في النفي لاستغراق جنس الناطقين, tr:ehadun fi'n-nefyi li'stiğrâki cinsi'n-nâtıkîn, gloss:olumsuzlukta ehad konuşan türün tamamını kapsar, source:"ء ح د,B002"}. "Hiç kimse" demektir. Ama aynı kelime Kur'an'da Allah'ın adıdır: {ar:قُلْ هُوَ ٱللَّهُ أَحَدٌ, tr:kul huvallâhu ehad, gloss:de ki O Allah birdir, source:112:1}. Adamın "kimse" diye yok saydığı yerde kelime, onu ölçmüş olan Bir'i duyurur. Aynı surede {ar:لَمْ يَلِدْ وَلَمْ يُولَدْ, tr:lem yelid ve lem yûled, gloss:doğurmadı ve doğurulmadı, source:112:3} sözü de vardır. Bu, üçüncü ayetin doğuran ve doğurulan üzerine yeminini Bir'in karşısına koyar.

Kur'an aynı kalıbı Zünnûn için kurar. Allah onun öfkeyle gidişini anlatırken {ar:فَظَنَّ أَن لَّن نَّقْدِرَ عَلَيْهِ, tr:fe-zanne en len nakdira aleyh, gloss:ona güç yetiremeyeceğimizi sandı, source:21:87} der. Sanı, "len" ve "aleyhi" aynı sıradadır. Ardından gelen şey ise bir çağrıdır: {ar:فَنَادَىٰ فِى ٱلظُّلُمَٰتِ, tr:fe-nâdâ fi'z-zulumât, gloss:karanlıklar içinde seslendi, source:21:87}. Sanıyı aşan şey Rabbe dönüştür. Önceki sure, sınanan insanın iki halini anlatır. İkincisi şöyledir: {ar:فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ, tr:fe-kadara aleyhi rizkahû fe-yekûlu rabbî ehânen, gloss:rızkını ona ölçülü verince Rabbim beni aşağıladı der, source:89:16}. Fiil aynıdır, insan yine konuşur. Yaratma, ölçme ve yol gösterme başka bir surede tek bir dizide gelir: {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî haleka fe-sevvâ, gloss:yaratıp düzene koyan, source:87:2} ve {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:vellezî kaddera fe-hedâ, gloss:ölçüp yol gösteren, source:87:3}. Bu, surenin dördüncü, beşinci ve onuncu ayetlerinin sırasıdır. Musa da Firavun'a Rabbini {ar:ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:ellezî a'tâ kulle şey'in halkahû summe hedâ, gloss:her şeye yaratılışını verip sonra yol gösteren, source:20:50} diye tanıtır. İnsanın yaratılışı da aynı iki fiille anlatılır: {ar:مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ, tr:min nutfetin halakahû fe-kadderah, gloss:onu bir damladan yarattı ve ölçüsünü verdi, source:80:19}. Kendi ölçüsünü kuran adamın sonu da aynı fiille söylenir. Kendisine uzayıp giden mal verilen adam için {ar:إِنَّهُۥ فَكَّرَ وَقَدَّرَ, tr:innehû fekkera ve kaddera, gloss:o düşündü ve ölçtü, source:74:18} ve {ar:فَقُتِلَ كَيْفَ قَدَّرَ, tr:fe-kutile keyfe kaddera, gloss:kahrolası nasıl ölçtü, source:74:19} denir. "E-yahsebu" sorusu insana başka yerlerde de yöneltilir: {ar:أَيَحْسَبُ ٱلْإِنسَٰنُ أَلَّن نَّجْمَعَ عِظَامَهُۥ, tr:e-yahsebu'l-insânu ellen necme'a izâmeh, gloss:insan kemiklerini toplamayacağımızı mı sanıyor, source:75:3} ve {ar:أَيَحْسَبُ ٱلْإِنسَٰنُ أَن يُتْرَكَ سُدًى, tr:e-yahsebu'l-insânu en yutrake sudâ, gloss:insan başıboş bırakılacağını mı sanıyor, source:75:36}. Burada da "len" kalıbı vardır, ve sanının konusu Allah'ın gücünün sınırıdır. Son gün "ehad" kelimesi tersine döner: {ar:فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ, tr:fe-yevme'izin lâ yu'azzibu azâbehû ehad, gloss:o gün O'nun azabı gibi kimse azap edemez, source:89:25} ve {ar:وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ, tr:ve lâ yûsiku vesâkahû ehad, gloss:O'nun bağlaması gibi kimse bağlayamaz, source:89:26}. "Kimse bana güç yetiremez" diyen sanının karşısında, "kimse O'nun gibi bağlayamaz" sözü durur.

Kaynaklar: 90:4 خَلَقْنَا خ ل ق B001, B006; 90:8 نَجْعَل ج ع ل B001; 90:5 يَقْدِرَ ق د ر B001, B002, B003, B004, B005; 90:1 أُقْسِمُ ق س م B003, B006; 90:5 أَيَحْسَبُ ح س ب B001, B002; 90:7 أَيَحْسَبُ ح س ب B001, B002; 90:5 أَحَدٌۭ ء ح د B001, B002; 90:7 أَحَدٌ ء ح د B001, B002

## Uzaktan görülen ateş

Sure ateşle biter: {ar:عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ, tr:aleyhim nârun mu'sade, gloss:üstlerine kapatılmış bir ateş vardır, source:90:20}. Ama ateşin kökü onu önce bir ışık yapar: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûru ve'n-nâru summiyâ bi-zâlike min tarîkati'l-idâe, gloss:nur ve nar aydınlatma yolundan ötürü bu adları aldı, source:"ن و ر,B001"}. Eskiden ateş yüksek yerlerde yol gösterilsin diye yakılırdı: {ar:كانوا ينورون في الجاهلية ليهتدى ويقتدى بها, tr:kânû yunevvirûne fi'l-câhiliyyeti li-yuhtedâ ve yuktedâ bihâ, gloss:cahiliyede onunla yol bulunsun ve ona uyulsun diye ateş yakarlardı, source:"ن و ر,B005"}. Yolun işareti de bu köktendir: {ar:المنار: علم الطريق, tr:el-menâr: alemu't-tarîk, gloss:menar yolun işaretidir, source:"ن و ر,B005"}. Bir başka söyleyiş de {ar:ضرب المنار على طريقه ليهتدى بها, tr:darabe'l-menâra alâ tarîkıhî li-yuhtedâ bihâ, gloss:yol bulunsun diye yolunun üstüne işaret dikti, source:"ن و ر,B005"}. Ateş uzaktan seçilir: {ar:تنورت النار من بعيد: تبصرتها, tr:tenevvertu'n-nâra min ba'îd: tebessartuhâ, gloss:ateşi uzaktan seçtim yani gözümle aradım, source:"ن و ر,B003"}. Dördüncü ayetin "insân" kelimesinin ailesi tam bu görüşü adlandırır: {ar:آنس من جانب يعني أبصر نارا, tr:ânese min cânib ya'nî ebsara nârâ, gloss:bir yandan ânese yani bir ateş gördü, source:"ء ن س,B002"}. Bir başka söyleyiş de {ar:فإن آنستم منهم رشدا أي أبصرتم وآنست نارا, tr:fe-in ânestum minhum ruşden ey ebsartum ve ânestu nârâ, gloss:onlarda olgunluk sezerseniz yani görürseniz; ve bir ateş sezdim, source:"ء ن س,B002"}. On altıncı ayetin kökü ateşi yanında dinlenilen bir şey olarak da bilir: {ar:السكن النار التي يسكن بها, tr:es-seken en-nâru'lletî yuskenu bihâ, gloss:seken yanında dinlenilen ateştir, source:"س ك ن,B004"}. Ateşin görüldüğü karanlık da on dokuzuncu ayetin köküyle anılır: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylu kâfirun li-ennehû setera bi-zulmetih, gloss:gece karanlığıyla örttüğü için kâfirdir, source:"ك ف ر,B002"}.

Böylece surenin başındaki yol sahnesine bir ışık da düşer. "Necd" yol kendi başına yol gösterir {source:"ن ج د,B002"}, ve ateşin yakılma sebebi de yol göstermektir. İkisi aynı işi görür. Gece yolcusu tepedeki ateşi uzaktan görür ve ona doğru yürür. Yirminci ayetteki ateş ise yolun üstünde bir işaret değildir. Üstü kapatılmıştır, uzaktan görülmez, içindekilerin üstüne kapanır. Düz bir anlatımın veremeyeceği şey bu tersine dönüştür: yolda yol gösterecek olan ateş, yolu görmezden gelenlerin üstüne kapak olur. Beşinci ve yedinci ayetlerin "yahsebu"su da gökten inen bir yangını bilir: {ar:حسبانا من السماء أي نارا تحرقها, tr:husbânen mine's-semâ ey nâran tuhrikuhâ, gloss:gökten bir husbân yani onu yakan bir ateş, source:"ح س ب,B007"}. Sanının kökünde bile bir ateş vardır.

Kur'an'da bu ateşin en açık sahnesi Musa'nındır. Allah elçisine {ar:وَهَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ, tr:ve hel etâke hadîsu mûsâ, gloss:Musa'nın haberi sana geldi mi, source:20:9} diye sorar ve anlatır: {ar:إِذْ رَءَا نَارًۭا فَقَالَ لِأَهْلِهِ ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:iz reâ nâran fe-kâle li-ehlihi'mkusû innî ânestu nâran le'allî âtîkum minhâ bi-kabesin ev ecidu ale'n-nâri hudâ, gloss:hani bir ateş görmüştü de ailesine kalın, ben bir ateş seçtim; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösterici bulurum demişti, source:20:10}. Görmek, "ânestu" ve hidayet tek ayettedir: surenin yedinci, dördüncü ve onuncu ayetlerinin kökleri. Aynı sahne başka yerde ısınmayla da anlatılır: {ar:إِنِّىٓ ءَانَسْتُ نَارًۭا سَـَٔاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ ءَاتِيكُم بِشِهَابٍۢ قَبَسٍۢ لَّعَلَّكُمْ تَصْطَلُونَ, tr:innî ânestu nâran se-âtîkum minhâ bi-haberin ev âtîkum bi-şihâbin kabesin le'allekum tastalûn, gloss:ben bir ateş seçtim; size ondan bir haber ya da ısınasınız diye yanan bir kor getireceğim, source:27:7}. Üçüncü anlatım ateşin bir dağın yanında görüldüğünü söyler: {ar:ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا, tr:ânese min cânibi't-tûri nârâ, gloss:dağın yanından bir ateş seçti, source:28:29}. Ateşi yaratan da kendini anar: {ar:أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ, tr:e-fe-raeytumu'n-nâra'lletî tûrûn, gloss:yaktığınız ateşi gördünüz mü, source:56:71}. Ardından {ar:نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا, tr:nahnu ce'alnâhâ tezkiraten ve metâ'â, gloss:onu bir hatırlatma ve bir yararlanma kıldık, source:56:73} der. Ateş bir hatırlatmadır. Ama ışığı kaybetmenin sahnesi de anlatılır: {ar:مَثَلُهُمْ كَمَثَلِ ٱلَّذِى ٱسْتَوْقَدَ نَارًۭا فَلَمَّآ أَضَآءَتْ مَا حَوْلَهُۥ ذَهَبَ ٱللَّهُ بِنُورِهِمْ وَتَرَكَهُمْ فِى ظُلُمَٰتٍۢ لَّا يُبْصِرُونَ, tr:meseluhum ke-meseli'llezi'stevkade nâran fe-lemmâ edâet mâ havlehû zehebellâhu bi-nûrihim ve terakehum fî zulumâtin lâ yubsırûn, gloss:onların durumu ateş yakan kişinin durumu gibidir; ateş çevresini aydınlatınca Allah ışıklarını alıp götürdü ve onları görmez hâlde karanlıklarda bıraktı, source:2:17}. Mal yığanın ateşi ise kalplere kadar yükselir: {ar:ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ, tr:elletî tattali'u ale'l-ef'ide, gloss:yüreklerin üstüne çıkıp onları saran, source:104:7}. Ardından {ar:إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ, tr:innehâ aleyhim mu'sade, gloss:o onların üstüne kapatılmıştır, source:104:8} gelir. Bir başka ateş de yüz çevirip biriktireni çağırır: {ar:كَلَّآ ۖ إِنَّهَا لَظَىٰ, tr:kellâ innehâ lezâ, gloss:hayır, o alevli bir ateştir, source:70:15}, {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:ted'û men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17} ve {ar:وَجَمَعَ فَأَوْعَىٰٓ, tr:ve ceme'a fe-ev'â, gloss:ve toplayıp kaba koyup saklayanı, source:70:18}. İki çaba anlatıldıktan sonra da uyarı ateşledir: {ar:فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ, tr:fe-enzertukum nâran telezzâ, gloss:sizi alev alev yanan bir ateşle uyardım, source:92:14}. Bu ateşe yalnızca {ar:ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ, tr:ellezî kezzebe ve tevellâ, gloss:yalanlayıp yüz çeviren, source:92:16} girer. Kapanmışlığın son sözü de çıkışsızlıktır: {ar:وَمَا هُم بِخَٰرِجِينَ مِنَ ٱلنَّارِ, tr:ve mâ hum bi-hâricîne mine'n-nâr, gloss:onlar ateşten çıkacak değildir, source:2:167}.

Kaynaklar: 90:20 نَارٌۭ ن و ر B001, B003, B005; 90:20 مُّؤْصَدَةٌۢ و ص د B001; 90:4 ٱلْإِنسَٰنَ ء ن س B002; 90:7 يَرَهُۥٓ ر ء ي B001; 90:10 ٱلنَّجْدَيْنِ ن ج د B002; 90:10 وَهَدَيْنَٰهُ ه د ي B001; 90:16 مِسْكِينًۭا س ك ن B004; 90:19 كَفَرُوا۟ ك ف ر B002; 90:5 أَيَحْسَبُ ح س ب B007; 90:17 بِٱلصَّبْرِ ص ب ر B013

## Buluşmalar

Görüntülerin en sık buluştuğu sahne yoldur. Onuncu ayetteki "necd" yolu kendi kendine yol gösterir, ateşin kökü de yüksek yerde yol gösterilsin diye yakılan ateşi anlatır. Sırt ile işaret ateşi aynı işi görür: gece yolcusuna nereye çıkacağını göstermek. Musa'nın sahnesi bu iki görüntüyü tek bir ayette taşır: dağın yanında görülen ateş ve {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ev ecidu ale'n-nâri hudâ, gloss:ya da ateşin başında bir yol gösterici bulurum, source:20:10} umudu. Bu surede ise yolun sonundaki ateş bir işaret değildir, üstü kapatılmıştır. Yol sahnesiyle ateş sahnesi arasındaki fark, bir yolculuğun nasıl tersine döndüğünü gösterir. Atılmayan geçidin karşısında, içine dalınan bir ateş vardır: {ar:هَٰذَا فَوْجٌۭ مُّقْتَحِمٌۭ مَّعَكُمْ, tr:hâzâ fevcun muktehimun meakum, gloss:bu sizinle birlikte içeri dalan bir kalabalıktır, source:38:59}. Sabrın kökü de bu iki sahne arasında ikiye bölünür. Yokuşta kendini panikten tutan sabır vardır. Bir de kitabı gizleyenlerin {ar:فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ, tr:fe-mâ asberahum ale'n-nâr, gloss:ateşe karşı ne kadar dayanıklılar, source:2:175} sözündeki ateşe cüret vardır.

İkinci büyük buluşma boyunla kapak arasındadır. On üçüncü ayetin fiili Arapçada kapalıyı açmak olarak tanımlanır: {ar:فكاك الرهن وهو فتحه من الانغلاق, tr:fikâku'r-rahni ve huve fethuhû mine'l-inğılâk, gloss:rehnin fikâkı onu kapalılıktan açmaktır, source:"ف ك ك,B002"}. Yirminci ayetin fiili de kapamak olarak tanımlanır: {ar:أوصدت الباب أغلقته, tr:evsadtu'l-bâbe ağlaktuh, gloss:kapıyı kapattım yani kilitledim, source:"و ص د,B001"}. Sure açılan bir boyundan kapanan bir ateşe doğru ilerler, ve iki fiil birbirinin tam tersidir. Bu iki ucu Kur'an'da tek bir sahne birleştirir. Kitabı sol eline verilen adamın boynu bağlanır ve bunun sebebi yoksulun yemeğine teşvik etmemesidir: {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ taâmi'l-miskîn, gloss:ve yoksulun yemeğine teşvik etmiyordu, source:69:34}. Sol taraf, boyundaki halka ve doyurulmayan yoksul bir aradadır. Malının bir işe yaramadığını söyleyen ve gücünün yok olup gittiğini gören de aynı adamdır. Bu sahnede sağ ile sol, harcanan mal, kıtlık ve boyun görüntüleri aynı yerde durur. Altıncı ayetteki "tükettim" orada şu söze döner: {ar:هَلَكَ عَنِّى سُلْطَٰنِيَهْ, tr:heleke annî sultâniyeh, gloss:gücüm benden yok olup gitti, source:69:29}.

Üçüncü buluşma yeminle geçit arasındadır. Yeminin kefareti ayeti, surenin on üçüncü ve on dördüncü ayetlerini birlikte sayar. Yeminler düğümlenir, sonra on yoksul doyurulur ya da bir boyun çözülür. Birinci ayetin yemini, ikinci ayetin "hıll"i, geçidin iki işi, on sekizinci ayetin sağ eli ve on dokuzuncu ayetin örtme kökü, bir yeminin bağlanıp çözülmesinin bütün aşamalarını taşır. Kur'an'ın bahçe sahipleri ise yemini ters yönde kullanır: yoksulu dışarıda bırakmak için yemin ederler. Bu ikisinin karşı karşıya gelmesi, surenin açılış yemininin neye açıldığını gösterir. Bu yemin bir şehirle başlar, şehirdeki yoksulun ağzıyla devam eder.

Gözetleyen göz ile harcanan mal, gösteriş kelimesinde buluşur. Gösteriş için harcayan, insanların görmesini ister ama Allah'ın görmediğini sanır. Bu çelişki tek bir ayette sahnelenir: malını {ar:رِئَآءَ ٱلنَّاسِ, tr:riâe'n-nâs, gloss:insanlara gösteriş için, source:2:264} harcayanın emeği kayanın üstündeki toprak gibi yıkanır gider. Aynı misal yere yapışma görüntüsünü de taşır: toprak, kaya ve yağmurla çıplak kalan taş. Ölçme görüntüsü de aynı ayete girer: {ar:لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟, tr:lâ yakdirûne alâ şey'in mimmâ kesebû, gloss:kazandıklarından hiçbir şeye güç yetiremezler, source:2:264}. "Kimse bana güç yetiremez" sanısı, kendi kazancına güç yetirememekle biter. Ölçme ile yol da Kur'an'da tek bir dizide buluşur, ve bu dizi surenin sırasıdır: yaratan, ölçen, yol gösteren.

Soy ile kıtlık "yetim" kelimesinde buluşur. Babasından kopan çocuk, iyiliğin geç ulaştığı ve açlık gününde açlık çeken çocuktur. Dil bu ikisini tek bir örnekte birleştirir: {ar:يتيم ذو مسغبة أي ذو مجاعة, tr:yetîmun zû mesğabe ey zû mecâa, gloss:açlık sahibi yetim yani kıtlık içindeki yetim, source:"س غ ب,B001"}. Şehir ile kıtlık da kıtlık yılının tanımında buluşur: yıl bedevileri şehirlere atar. Kur'an'da doyurulan şehrin sahnesi de buradadır: {ar:ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ, tr:ellezî at'amehum min cû'in ve âmenehum min havf, gloss:onları açlıktan doyuran ve korkudan güvenliğe kavuşturan, source:106:4}. Yere yapışma ile geçit, yükselme ile saplanmanın aynı ayette karşı karşıya geldiği sahnede buluşur: ayetlerle yükseltilebilecekken yere saplanan adam. Bu da on dokuzuncu ayetin ayetleri inkâr edenlerine bağlanır.

Bütün bu görüntüler birlikte surenin hareketini taşır. Hareket yere oturmuş bir şehirde başlar. İnsan zorluğun ortasında yaratılmıştır. Malı keçeleşmiştir, kendini görülmez ve ölçülmez sanır. Ona gözler, dil ve dudaklar verilmiş, önüne görünen iki sırt konmuştur. İstenen şey yukarıya atılmaktır. Bu atılış da yere yapışmış olana eğilmek, bir boynun düğümünü çözmek ve aç bir ağza yemek koymaktır. Böyle atılanlar bitkiler gibi birbirine bitişir, aynı rahimden çıkmış gibi birbirine acır ve sağ tarafa yerleşir. Ayetleri örtenlerin üstü ise, yolda yol gösterebilecek bir ateşle kapatılır. Mağara sahnesindeki eşikte köpek ön ayaklarını uzatmış yatar: {ar:وَكَلْبُهُم بَٰسِطٌۭ ذِرَاعَيْهِ بِٱلْوَصِيدِ, tr:ve kelbuhum bâsitun zirâ'ayhi bi'l-vasîd, gloss:köpekleri iki ön ayağını eşiğe uzatmıştı, source:18:18}. Aynı ayette uyuyanlar sağa ve sola çevrilir. Yirminci ayetin kökü, sağ ve sol ile o eşiği orada tek bir sahnede bir araya getirir.

