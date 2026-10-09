Focus: 114:2. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/114_2/D.r13/context.md =====
# 114:2 — focus

مَلِكِ ٱلنَّاسِ

Anchor translation (canonical reading, reference only):

İnsanların hükümdarına.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | مَلِكِ | مَلِك | م ل ك | N |
| 2 | ٱلنَّاسِ | نَّاس | ن و س | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 114 — full text (context; no pericope)

- 114:1 قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ
- 114:2 ◀ focus مَلِكِ ٱلنَّاسِ
- 114:3 إِلَٰهِ ٱلنَّاسِ
- 114:4 مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ
- 114:5 ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ
- 114:6 مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ


===== _commentary/v16/work/114_2/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## م ل ك (root_001444) — identity root of مَلِكِ (w1)

- **B001** güçlü ve tutarlı biçimde bir arada durma — hamuru sıkıca yoğurup kıvamlandırmak · sürgünü kabuğuyla kurutup sertleştirmek · kendini tutmak; dayanmak · bir şeyi ayakta tutan iç sağlamlık
  أصل صحيح يدل على قوة في الشيء وصحة (maqayis)؛ أملك عجينه قوي عجنه وشده (maqayis)؛ ملكت العجين إذا شددت عجنه (sihah)؛ ملك النبعة صلبها (sihah)؛ العجين إذا كان متماسكا متينا مملوك ومملك (tahdhib)؛ حائط ليس له ملاك أي تماسك (mufradat)
- **B002** sahiplik ve tasarruf yetkisi — bir şeye sahip olup onu tasarrufunda bulundurmak · mülkiyet; sahip olunan mal veya hak · kişinin elinin altında ve sahipliğinde bulunan şey · köleleştirilmiş kişi · köleleştirilmiş kişilere iyi davranma · özgür doğmuşken tutsak edilip köleleştirilen kişi · boşanma kararını eşin tasarrufuna bırakmak
  ملك الإنسان الشيء يملكه ملكا (maqayis)؛ الملك ما ملكت اليد من مال وخول (ayn;tahdhib)؛ ملكت الشيء أملكه ملكا (sihah)؛ وملكه المال والملك فهو مملك (sihah)؛ أملكت فلانة أمرها إذا جعل أمر طلاقها بيدها (tahdhib)؛ المملوك يختص في التعارف بالرقيق من الأملاك (mufradat)
- **B003** hükümdarlık ve kamusal egemenlik — hükümdar · hükümdar; egemen yönetici · hükümranlık; kamusal egemenlik · ilahi mutlak hükümranlık · hükümdarın yönetim alanı ve ülkesi · birini başlarına hükümdar yapmak
  والاسم الملك لأن يده فيه قوية صحيحة (maqayis)؛ الملك لله المالك المليك (ayn)؛ الملكوت ملك الله وملكوت الله سلطانه (ayn)؛ الملكوت من الملك (sihah)؛ المملكة سلطان الملك في رعيته (ayn;tahdhib)؛ له ملكوت العراق وعزه وسلطانه وملكه (tahdhib)؛ الملك هو المتصرف بالأمر والنهي في الجمهور (mufradat)؛ ملك القوم فلانا وأملكوه على أنفسهم أي صيروه ملكا (tahdhib)
- **B004** evlilik akdi kurma — evlilik akdi; evlendirme · kadınla evlenmek
  كنا في إملاك فلان أي أملكناه امرأته (maqayis)؛ الإملاك التزويج قد أملكوه وملكوه أي زوجوه (ayn)؛ ملكت المرأة تزوجتها (sihah)؛ أملكنا فلانا فلانة إذا زوجناه إياها (sihah)؛ شهدنا إملاك فلان وملاكه وملاكه (tahdhib)؛ الملاك التزويج وأملكوه زوجوه (mufradat)
- **B005** işi ayakta tutan temel dayanak [kalıp] — işin dayandığı temel unsur · kalp bedenin temel dayanağıdır
  ملاك الأمر ما يعتمد عليه (ayn)؛ القلب ملاك الجسد (ayn;sihah;mufradat)؛ هذا ملاك الأمر وملاكه أي صلاحه (tahdhib)
- **B006** yolun veya yerin orta ya da ana kesimi — yolun ortası veya ana kesimi · vadinin sınırı veya orta kesimi · yerleşimin ortası veya büyük kesimi
  ملك الطريق أيضا وسطه (sihah)؛ خل عن ملك الطريق وملك الوادي وملكه وملكه أي حده ووسطه (tahdhib)؛ الزم ملك الطريق أي وسطه (tahdhib)؛ أراد بالمملكة وسطها وملك الطريق معظمه ووسطه (tahdhib)
- **B007** işleri ve yaşamı sürdüren su kaynağı [kalıp] — işini yürütmesini sağlayan su · hiç suyu yok · sularımız geçimimizi ayakta tutar
  والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره (maqayis)؛ الماء ملك أمر أي يقوم به الأمر (sihah)؛ الماء ملك أمره (tahdhib)؛ الماء ملاك الأشياء يضرب للشيء الذي به كمال الأمر (tahdhib)؛ ماله ملك ولا نقر أي ما له ماء (tahdhib)؛ مياهنا ملوكنا ومات فلان عن ملوك كثيرة (tahdhib)
- **B008** hayvanlarda önden gidip yön veren unsur [kalıp] — arı topluluğunun önderi · bineğin ön ayakları ve yönlendirici kısmı · deve ve koyun sürüsünün öncüsü
  مليك النحل يعسوبها (sihah)؛ ملك الدابة قوائمها وهاديها (sihah;tahdhib)؛ جاءنا تقوده ملكه يعني قوائمه وهاديه (tahdhib)؛ ملك الإبل والشاء ما يتقدم ويتبعه سائره (mufradat)
- **B009** ilahi haberci varlık — 
  الملك واحد الملائكة إنما هو تخفيف الملأك والأصل مألك (ayn)؛ مألك من الألوك وهو الرسالة (ayn)؛ الملك من الملائكة واحد وجمع (sihah)؛ أصله مألك بتقديم الهمزة من الألوك وهي الرسالة (sihah)؛ الملك واحد الملائكة إنما هو تخفيف الملأك وهو مفعل من الألوك (tahdhib)

## ء ن س (root_000059) — identity root of ٱلنَّاسِ (w2)

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

===== _commentary/v16/out/s114/images.r13.map3.nochannels.hftbundle.tool.tool/images.md (only the images that cite 114:2, and ## Buluşmalar) =====
## Göğüs ve içinde saklanan

Beşinci ayet fısıltının yerini adlandırır: {ar:فِى صُدُورِ ٱلنَّاسِ, tr:fî sudûri'n-nâs, gloss:insanların göğüslerinde, source:114:5}. Göğüs bedenin bir odasıdır, önü yükselen bir kafestir: {ar:الصدرة من الإنسان ما أشرف من أعلى صدره, tr:es-sudretu mine'l-insâni mâ eşrafe min a'lâ sadrih, gloss:insanın sudresi göğsünün üstünde yükselen kısmıdır, source:"ص د ر,B001"}. Altıncı ayetin {ar:ٱلْجِنَّةِ, tr:el-cinne, gloss:cinler, source:114:6} kelimesinin kökü bu odanın parçalarını da adlandırır: {ar:الجناجن عظام الصدر, tr:el-cenâcin izâmu's-sadr, gloss:cenâcin göğüs kemikleridir, source:"ج ن ن,B016"}. Odanın içindeki kalp de aynı kökten, gizli olduğu için adını alır: {ar:الجنان القلب لكونه مستورا عن الحاسة, tr:el-cenânu'l-kalbu li-kevnihî mestûran ani'l-hâsse, gloss:cenân kalptir, duyudan örtülü olduğu için, source:"ج ن ن,B010"}. Ve kök bir şeyi göğüste saklamayı söyler: {ar:أجننت الشيء في صدري أكننته, tr:ecnentu'ş-şey'e fî sadrî ekenentuh, gloss:o şeyi göğsümde gizledim, source:"ج ن ن,B001"}. Böylece saldıranın adı ile saldırının yapıldığı odanın kemikleri ve içindeki kalp aynı köke bağlanır: örtülü olan, örtülü bir odaya girer.

Fısıltı tam bu odaya yerleştirilir: {ar:وسوس إلي ووسوس في صدري, tr:vesvese ileyye ve vesvese fî sadrî, gloss:bana fısıldadı, göğsümde fısıldadı, source:"و س و س,B001"}. Ve fısıltı, kişinin kendi kendine konuşmasına benzer: {ar:الوسوسة حديث النفس, tr:el-vesvesetu hadîsu'n-nefs, gloss:vesvese nefsin kendi kendine konuşmasıdır, source:"و س و س,B001"}. İnsan kökü de kendine döner: {ar:كيف ابن إنسك يعني نفسه, tr:keyfe'bnu insik, gloss:"insinin oğlu nasıl" yani kendisi nasıl, source:"ء ن س,B006"}. Bu yüzden fısıltı dışarıdan gelen bir ses gibi değil, kişinin kendi sesi gibi duyulur; tehlikeyi görünmez kılan budur. İkinci ayetin {ar:مَلِكِ, tr:melik, gloss:hükümdar, source:114:2} kelimesinin kökü kalbi bedenin dayanağı sayar: {ar:القلب ملاك الجسد, tr:el-kalbu milâku'l-ced, gloss:kalp bedenin ayakta tutanıdır, source:"م ل ك,B005"}. Fısıltı bedeni ayakta tutan noktaya gider. İlk ayetin {ar:قُلْ, tr:kul, gloss:de, source:114:1} kelimesinin kökü de içte tutulan sözü bilir: {ar:في نفسي قول لم أظهره, tr:fî nefsî kavlun lem uzhirh, gloss:içimde açığa vurmadığım bir söz var, source:"ق و ل,B012"}. Göğüs iki sözün de yeridir: emredilen sığınma sözü oradan çıkar, fısıltı oraya girer.

İnsan kökü bir eve girmeden önce izin istemeyi de adlandırır {source:"ء ن س,B007"}. Kuran bunu emreder: {ar:لَا تَدْخُلُوا۟ بُيُوتًا غَيْرَ بُيُوتِكُمْ حَتَّىٰ تَسْتَأْنِسُوا۟ وَتُسَلِّمُوا۟ عَلَىٰٓ أَهْلِهَا, tr:lâ tedhulû buyûten gayra buyûtikum hattâ teste'nisû ve tusellimû alâ ehlihâ, gloss:kendi evlerinizden başka evlere, izin alıp halkına selam vermeden girmeyin, source:24:27}. Fısıldayan bu kuralın tersini yapar: göğüs odasına izin almadan girer.

Kuran göğsün içini bilen yakınlığı aynı fiille gösterir: {ar:وَنَعْلَمُ مَا تُوَسْوِسُ بِهِۦ نَفْسُهُۥ ۖ وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ, tr:ve na'lemu mâ tuvesvisu bihî nefsuh, ve nahnu akrabu ileyhi min habli'l-verîd, gloss:nefsinin ona ne fısıldadığını biliriz; biz ona şah damarından daha yakınız, source:50:16}. Fısıltının girdiği yerden daha derinde bir yakınlık vardır; sığınılan Rab bu yakınlıktadır. Göğsünü saklamak için bükenler de anlatılır: {ar:يَثْنُونَ صُدُورَهُمْ لِيَسْتَخْفُوا۟ مِنْهُ, tr:yesnûne sudûrahum li-yestahfû minh, gloss:ondan gizlenmek için göğüslerini bükerler, source:11:5}; elbiselerine bürünseler de {ar:إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ, tr:innehû alîmun bi-zâti's-sudûr, gloss:o göğüslerin özünü bilir, source:11:5}. Sözlükteki "göğüste gizlemek" fiilinin kardeşi Kuran'da da göğüslere söylenir: {ar:وَرَبُّكَ يَعْلَمُ مَا تُكِنُّ صُدُورُهُمْ, tr:ve rabbuke ya'lemu mâ tukinnu sudûruhum, gloss:Rabbin göğüslerinin gizlediğini bilir, source:28:69}. Kalp göğsün içindedir: {ar:ٱلْقُلُوبُ ٱلَّتِى فِى ٱلصُّدُورِ, tr:el-kulûbu'lletî fi's-sudûr, gloss:göğüslerdeki kalpler, source:22:46}. Göğüste oturan bir şeye karşı ilaç da sığınmadır: {ar:إِن فِى صُدُورِهِمْ إِلَّا كِبْرٌۭ مَّا هُم بِبَٰلِغِيهِ ۚ فَٱسْتَعِذْ بِٱللَّهِ, tr:in fî sudûrihim illâ kibrun mâ hum bi-bâliğîh, festeiz billâh, gloss:göğüslerinde yalnızca ulaşamayacakları bir büyüklenme var; Allah'a sığın, source:40:56}. Sonunda göğüslerdekinin hepsi dışarı çıkarılır: {ar:وَحُصِّلَ مَا فِى ٱلصُّدُورِ, tr:ve hussile mâ fi's-sudûr, gloss:göğüslerde olan ortaya dökülür, source:100:10}. Göğüs, Kuran'ın açıp genişlettiği bir oda olarak da görünür: {ar:رَبِّ ٱشْرَحْ لِى صَدْرِى, tr:rabbi'şrah lî sadrî, gloss:Rabbim, göğsümü aç, source:20:25}.

Kaynaklar: 114:5 صُدُورِ ص د ر B001; 114:6 ٱلْجِنَّةِ ج ن ن B016; 114:6 ٱلْجِنَّةِ ج ن ن B010; 114:6 ٱلْجِنَّةِ ج ن ن B001; 114:5 يُوَسْوِسُ و س و س B001; 114:2 مَلِكِ م ل ك B005; 114:5 ٱلنَّاسِ ء ن س B006; 114:1 قُلْ ق و ل B012; 114:5 ٱلنَّاسِ ء ن س B007

## Rab, Melik, İlah ve onların küçük sahipleri

İlk üç ayet aynı nesnenin üzerine üç unvan koyar: {ar:بِرَبِّ ٱلنَّاسِ, tr:bi-rabbi'n-nâs, gloss:insanların Rabbine, source:114:1}, {ar:مَلِكِ ٱلنَّاسِ, tr:meliki'n-nâs, gloss:insanların hükümdarına, source:114:2}, {ar:إِلَٰهِ ٱلنَّاسِ, tr:ilâhi'n-nâs, gloss:insanların ilahına, source:114:3}. "İnsanlar" üç kez değişmeden kalır, unvan değişir. Her unvanın kökü daha küçük ya da sahte sahipleri de kapsar. Rab her şeyin sahibidir ve krallara da söylenmiştir: {ar:رب كل شئ: مالكه؛ وقد قالوه في الجاهلية للملك, tr:rabbu kulli şey' mâlikuh; ve kad kâlûhu fi'l-câhiliyyeti li'l-melik, gloss:her şeyin rabbi onun sahibidir; cahiliyede bunu krala da söylerlerdi, source:"ر ب ب,B001"}; ev rabbi, at rabbi denir, ama kayıtsız "Rab" yalnız Allah içindir {source:"ر ب ب,B001"}. Melik, buyruk ve yasakla tasarruf edendir, {ar:الملك هو المتصرف بالأمر والنهي في الجمهور, tr:el-meliku huve'l-mutasarrifu bi'l-emri ve'n-nehyi fi'l-cumhûr, gloss:melik topluluk içinde emir ve yasakla tasarruf edendir, source:"م ل ك,B003"}; ama insanlar kendilerine de kral yapar: {ar:ملك القوم فلانا وأملكوه على أنفسهم أي صيروه ملكا, tr:mellek'el-kavmu fulânen, gloss:topluluk birini kendilerine kral yaptı, source:"م ل ك,B003"}. Elin sahip olduğu mal da aynı köktendir {source:"م ل ك,B002"}. İlah her tapılandır: {ar:إله اسما لكل معبود, tr:ilâh ismen li-kulli ma'bûd, gloss:ilah her tapılanın adıdır, source:"ء ل ه,B001"}; putlar ve güneş dahil. Sonra belirlilik takısıyla Yaratıcıya özgü kılınır {source:"ء ل ه,B002"}. Surenin ilk kelimesi bile bu sahnede bir küçük kral taşır: {ar:القيل ملك من ملوك حمير دون الملك الأعظم, tr:el-kayl melikun min mulûki himyer dûne'l-meliki'l-a'zam, gloss:kayl, Himyer krallarından en büyük kralın altındaki bir kraldır, source:"ق و ل,B004"}, adını sözünün geçmesinden alır {source:"ق و ل,B004"}.

Sahne bir talipler sarayıdır: sahipler, küçük krallar, putlar ve güneş unvanları küçük ölçüde taşır; üç unvanı birden ve mutlak olarak taşıyan, insanların tek Rabbi, Meliki ve İlahıdır. Üç unvanın üst üste gelmesi, bu taliplerin her birinin bir yere kadar kabul edilebileceği ihtimalini kapatır. Kötülük kökü de bu sahnede yer alır: {ar:ألقى عليه شراشره إذا ألقى عليه نفسه حرصا ومحبة, tr:elkâ aleyhi şerâşirahû izâ elkâ aleyhi nefsehû hırsan ve mahabbe, gloss:hırs ve sevgiyle kendini bütünüyle ona attı, source:"ش ر ر,B007"}. Bütün benliği tek bir nesneye atmak, tapınmanın istediği şeydir; sahte talibin istediği de budur.

Kuran sahte talipleri adlandırır. Firavun: {ar:أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:ene rabbukumu'l-a'lâ, gloss:ben sizin en yüce rabbinizim, source:79:24}; ve {ar:مَا عَلِمْتُ لَكُم مِّنْ إِلَٰهٍ غَيْرِى, tr:mâ alimtu lekum min ilâhin gayrî, gloss:sizin için benden başka bir ilah bilmiyorum, source:28:38}. Yusuf zindanda: {ar:ءَأَرْبَابٌۭ مُّتَفَرِّقُونَ خَيْرٌ أَمِ ٱللَّهُ ٱلْوَٰحِدُ ٱلْقَهَّارُ, tr:e-erbâbun muteferrikûne hayrun emi'llâhu'l-vâhidu'l-kahhâr, gloss:dağınık rabler mi daha iyi, yoksa tek ve kahhar Allah mı, source:12:39}. İnsanlar din bilginlerini rab edinir {source:9:31}; kitap ehline çağrı birbirini rab edinmemektir {source:3:64}. Hevesini ilah edinen de vardır {source:25:43}. Allah'ın mülk verdiği biri İbrahim'le Rabbi hakkında tartışır ve güneşle susturulur {source:2:258}. Fısıldayan da sahte bir krallık sunar: {ar:عَلَىٰ شَجَرَةِ ٱلْخُلْدِ وَمُلْكٍۢ لَّا يَبْلَىٰ, tr:alâ şecerati'l-huldi ve mulkin lâ yeblâ, gloss:ölümsüzlük ağacına ve eskimeyen bir mülke, source:20:120}, ve {ar:إِلَّآ أَن تَكُونَا مَلَكَيْنِ, tr:illâ en tekûnâ melekeyn, gloss:ancak iki melek olmayasınız diye, source:7:20}. Hükümdarın tebaası üzerindeki gücünün adı sultandır {source:"م ل ك,B003"}, ve fısıldayana bu güç inananlar üzerinde verilmez: {ar:إِنَّهُۥ لَيْسَ لَهُۥ سُلْطَٰنٌ عَلَى ٱلَّذِينَ ءَامَنُوا۟ وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ, tr:innehû leyse lehû sultânun ale'llezîne âmenû ve alâ rabbihim yetevekkelûn, gloss:onun inananlar ve Rablerine dayananlar üzerinde gücü yoktur, source:16:99}; gücü ancak onu dost edinenler üzerindedir {source:16:100}. Allah İblis'e: {ar:إِنَّ عِبَادِى لَيْسَ لَكَ عَلَيْهِمْ سُلْطَٰنٌۭ ۚ وَكَفَىٰ بِرَبِّكَ وَكِيلًۭا, tr:inne ibâdî leyse leke aleyhim sultân, ve kefâ bi-rabbike vekîlâ, gloss:kullarım üzerinde senin gücün yoktur; vekil olarak Rabbin yeter, source:17:65}. Fısıldayan tapınma da ister ve bu yasaklanır: {ar:أَلَمْ أَعْهَدْ إِلَيْكُمْ يَٰبَنِىٓ ءَادَمَ أَن لَّا تَعْبُدُوا۟ ٱلشَّيْطَٰنَ, tr:e-lem a'hed ileykum yâ benî âdeme en lâ ta'budu'ş-şeytân, gloss:Ey Âdemoğulları, size şeytana tapmayın diye ahit vermedim mi, source:36:60}. Gerçek unvanlar ise yerinde durur: {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:mâliki yevmi'd-dîn, gloss:din gününün sahibi, source:1:4}, {ar:فَتَعَٰلَى ٱللَّهُ ٱلْمَلِكُ ٱلْحَقُّ ۖ لَآ إِلَٰهَ إِلَّا هُوَ رَبُّ ٱلْعَرْشِ ٱلْكَرِيمِ, tr:fe-teâla'llâhu'l-meliku'l-hakk, lâ ilâhe illâ hû, rabbu'l-arşi'l-kerîm, gloss:gerçek hükümdar Allah yücedir; ondan başka ilah yoktur, şerefli arşın Rabbidir, source:23:116}; ve sonunda {ar:لِّمَنِ ٱلْمُلْكُ ٱلْيَوْمَ ۖ لِلَّهِ ٱلْوَٰحِدِ ٱلْقَهَّارِ, tr:li-meni'l-mulku'l-yevm, li'llâhi'l-vâhidi'l-kahhâr, gloss:bugün mülk kimin? Tek ve kahhar Allah'ın, source:40:16}.

Kaynaklar: 114:1 بِرَبِّ ر ب ب B001; 114:2 مَلِكِ م ل ك B003; 114:2 مَلِكِ م ل ك B002; 114:1 قُلْ ق و ل B004; 114:3 إِلَٰهِ ء ل ه B001; 114:3 إِلَٰهِ ء ل ه B002; 114:4 شَرِّ ش ر ر B007

## Bir arada tutmak ve parçalamak

{ar:مَلِكِ, tr:melik, gloss:hükümdar, source:114:2} kelimesinin kökü sağlamlıktan başlar: sıkıca yoğrulmuş hamur, {ar:ملكت العجين إذا شددت عجنه, tr:melektu'l-acîne izâ şedettu acneh, gloss:hamuru sıkıca yoğurdum, source:"م ل ك,B001"}; bir arada duran duvar, {ar:حائط ليس له ملاك أي تماسك, tr:hâitun leyse lehû milâk, gloss:tutarlılığı olmayan duvar, source:"م ل ك,B001"}; ve krallık, elin tuttuğunda güçlü olmasından: {ar:والاسم الملك لأن يده فيه قوية صحيحة, tr:ve'l-ismu'l-mulk li-enne yedehû fîhi kaviyyetun sahîha, gloss:mülk denir, çünkü eli onun üzerinde güçlü ve sağlamdır, source:"م ل ك,B003"}. {ar:بِرَبِّ, tr:bi-rabbi, gloss:Rabbine, source:114:1} kelimesinin kökü toplar: kumar oklarını bir arada tutan kese {source:"ر ب ب,B010"}; binlerce insan ve tek olmak için toplanmış beş kabile, {ar:الربي: واحد الربيين، وهم الألوف من الناس؛ الرباب خمس قبائل تجمعوا, tr:er-ribbî vâhidu'r-ribbiyyîn, ve humu'l-ulûfu mine'n-nâs, gloss:ribbî, binlerce insan demek olan ribbiyyûn'un tekilidir; rabâb, bir araya gelmiş beş kabiledir, source:"ر ب ب,B004"}; sıkı düğüm {source:"ر ب ب,B016"}; tarafları bağlayan ahit, {ar:الربابة: العهد والميثاق, tr:er-ribâbe el-ahdu ve'l-mîsâk, gloss:ribâbe ahit ve sözleşmedir, source:"ر ب ب,B011"}; toplandığı için adını alan bol su {source:"ر ب ب,B013"}. Beş kez tekrar eden {ar:ٱلنَّاسِ, tr:en-nâs, gloss:insanlar, source:114:1} de bir topluluktur {source:"ء ن س,B001"}. Altıncı ayetin kökü ise halkın kalabalık yığınını adlandırır, ki orada tek tek kişiler kaybolur: {ar:جنان الناس معظمهم ويسمى السواد, tr:cenânu'n-nâsi mu'zamuhum ve yusemma's-sevâd, gloss:insanların cenânı onların büyük kısmıdır, karaltı da denir, source:"ج ن ن,B013"}.

Buna karşı kötülük kökü parçalar: {ar:شرشرة الشيء تشقيقه وتقطيعه, tr:şerşeretu'ş-şey'i teşkîkuhû ve takti'uh, gloss:bir şeyin şerşeresi onu yarıp parçalamaktır, source:"ش ر ر,B004"}; ve çekişmeyi adlandırır {source:"ش ر ر,B011"}. Sure şu süreci duyurur: çok olan bir bağlayıcı tarafından tek tutulur ya da parçalanır. İnsanlar birlikte anıldıkları üç ayette tek bir Rabbe, tek bir Meliğe, tek bir İlaha bağlıdır; fısıldayan bu bağı içeriden çözer.

Kuran'da sığınmanın sözlükteki açıklaması olan tutunmak fiili topluluğa emredilir: {ar:وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا وَلَا تَفَرَّقُوا۟, tr:va'tesımû bi-habli'llâhi cemîan ve lâ teferrakû, gloss:hep birlikte Allah'ın ipine tutunun, dağılmayın, source:3:103}, ve aynı ayette {ar:فَأَلَّفَ بَيْنَ قُلُوبِكُمْ, tr:fe-ellefe beyne kulûbikum, gloss:kalplerinizi birleştirdi, source:3:103}. Şeytanın amacı tersidir: {ar:إِنَّمَا يُرِيدُ ٱلشَّيْطَٰنُ أَن يُوقِعَ بَيْنَكُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ فِى ٱلْخَمْرِ وَٱلْمَيْسِرِ, tr:innemâ yurîdu'ş-şeytânu en yûkia beynekumu'l-adâvete ve'l-bağdâe fi'l-hamri ve'l-meysir, gloss:şeytan içki ve kumarla aranıza düşmanlık ve kin sokmak ister, source:5:91}; kesenin bir arada tuttuğu kumar okları, bölen bir oyun olur. Toplanmış binler peygamberlerin yanında çarpışır: {ar:قَٰتَلَ مَعَهُۥ رِبِّيُّونَ كَثِيرٌۭ فَمَا وَهَنُوا۟, tr:kâtele meahû ribbiyyûne kesîrun fe-mâ vehenû, gloss:onunla birlikte pek çok ribbî savaştı ve gevşemediler, source:3:146}. Çok ilah, dünyanın parçalanmasıdır: {ar:لَوْ كَانَ فِيهِمَآ ءَالِهَةٌ إِلَّا ٱللَّهُ لَفَسَدَتَا, tr:lev kâne fîhimâ âlihetun illa'llâhu le-fesedetâ, gloss:yerde ve gökte Allah'tan başka ilahlar olsaydı ikisi de bozulurdu, source:21:22}; {ar:إِذًۭا لَّذَهَبَ كُلُّ إِلَٰهٍۭ بِمَا خَلَقَ, tr:izen le-zehebe kullu ilâhin bimâ halak, gloss:o zaman her ilah kendi yarattığını alıp giderdi, source:23:91}. Bağlayan ahit ise Rab sorusuyla kurulur: {ar:أَلَسْتُ بِرَبِّكُمْ ۖ قَالُوا۟ بَلَىٰ, tr:e-lestu bi-rabbikum, kâlû belâ, gloss:ben sizin Rabbiniz değil miyim? Evet, dediler, source:7:172}. Şeytan buna karşı yemin eder {source:7:21}. İkiz surede düğümlere üfleyenler anılır {source:113:4}; Rab kökünün sıkı düğümü bunun karşısında durur.

Kaynaklar: 114:2 مَلِكِ م ل ك B001; 114:2 مَلِكِ م ل ك B003; 114:1 بِرَبِّ ر ب ب B010; 114:1 بِرَبِّ ر ب ب B004; 114:1 بِرَبِّ ر ب ب B016; 114:1 بِرَبِّ ر ب ب B011; 114:1 بِرَبِّ ر ب ب B013; 114:1–6 ٱلنَّاسِ ء ن س B001; 114:6 ٱلْجِنَّةِ ج ن ن B013; 114:4 شَرِّ ش ر ر B004; 114:4 شَرِّ ش ر ر B011

## Gece, saklanan yıldızlar, güneş ve karanlıkta görülen ateş

{ar:ٱلْخَنَّاسِ, tr:el-hannâs, gloss:sinip çekilen, source:114:4} kökü yürüyen, gündüz güneş ışığı onları örtünce gizlenen ve batan gezegenleri adlandırır: {ar:الخنس الكواكب الخمسة التي تجري وتخنس في مجراها حتى يخفى ضوء الشمس وخنوسها اختفاؤها بالنهار, tr:el-hunnesu'l-kevâkibu'l-hamsetu'lletî tecrî ve tahnisu fî mecrâhâ, gloss:hunnes, akan ve akışında gizlenen beş yıldızdır; gizlenmeleri gündüz kaybolmalarıdır, source:"خ ن س,B002"}. Altıncı ayetin kökü gecenin her şeyi örtmesini söyler: {ar:أجنه الليل وجن عليه الليل إذا أظلم حتى يستره بظلمته, tr:ecennehu'l-leylu ve cenne aleyhi'l-leyl, gloss:gece onu örttü; karanlığıyla örtecek kadar karardı, source:"ج ن ن,B002"}. Üçüncü ayetin kökü güneşi adlandırır, çünkü ona tapılmıştır: {ar:والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها, tr:ve'l-ilâhetu'ş-şems, summiyet bi-zâlike li-enne kavmen kânû ya'budûnehâ, gloss:ilâhe güneştir; bir topluluk ona taptığı için böyle denmiştir, source:"ء ل ه,B001"}. Kötülük kökü güneşe sermeyi {source:"ش ر ر,B002"} ve ateşten uçan kıvılcımı adlandırır: {ar:الشرر ما تطاير من النار, tr:eş-şereru mâ tetâyera mine'n-nâr, gloss:şerer ateşten uçuşandır, source:"ش ر ر,B003"}. İnsan kökü ateşi uzaktan görmeyi, {ar:آنس من جانب يعني أبصر نارا, tr:ânese min cânib, gloss:bir yandan ateş gördü, source:"ء ن س,B002"}, ve gözbebeğinin karasında görünen küçük sureti adlandırır: {ar:إنسان العين المثال الذي يرى في السواد, tr:insânu'l-ayn el-misâlu'lledî yurâ fi's-sevâd, gloss:gözün insanı, gözün karasında görünen surettir, source:"ء ن س,B005"}. İnsan kökü kişiye eşlik eden her şeyi de bilir {source:"ء ن س,B003"}. Rab kökü yerinden ayrılmayanı {source:"ر ب ب,B007"}, Melik kökü de Allah'ın melekûtunu söyler {source:"م ل ك,B003"}.

Sahne şudur: gece her şeyi örter; gezegenler görünür, akar, gizlenir ve döner; bir zamanlar tapılan güneş doğar; bir ateş görülür, kıvılcımlar uçar; bir göz bakar; ve batan ışıklar arasında hangisinin Rab olduğu sorulur. Surenin üç unvanı bu soruya cevaptır: batmayan.

Kuran bu sahneyi İbrahim'in gecesinde kurar. Önce putlar ilah olarak anılır {source:6:74}, sonra {ar:وَكَذَٰلِكَ نُرِىٓ إِبْرَٰهِيمَ مَلَكُوتَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:ve kezâlike nurî ibrâhîme melekûte's-semâvâti ve'l-ard, gloss:böylece İbrahim'e göklerin ve yerin melekûtunu gösteriyorduk, source:6:75}, ve: {ar:فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ رَءَا كَوْكَبًۭا ۖ قَالَ هَٰذَا رَبِّى ۖ فَلَمَّآ أَفَلَ قَالَ لَآ أُحِبُّ ٱلْءَافِلِينَ, tr:fe-lemmâ cenne aleyhi'l-leylu raâ kevkeben, kâle hâzâ rabbî, fe-lemmâ efele kâle lâ uhibbu'l-âfilîn, gloss:gece onu örtünce bir yıldız gördü, "bu benim Rabbim" dedi; batınca "batanları sevmem" dedi, source:6:76}. Güneşte aynı tekrarlanır: {ar:فَلَمَّا رَءَا ٱلشَّمْسَ بَازِغَةًۭ قَالَ هَٰذَا رَبِّى هَٰذَآ أَكْبَرُ, tr:fe-lemmâ raa'ş-şemse bâzigaten kâle hâzâ rabbî hâzâ ekber, gloss:güneşi doğarken görünce "bu benim Rabbim, bu daha büyük" dedi, source:6:78}; o da batar, ve İbrahim yüzünü gökleri ve yeri yaratana çevirir {source:6:79}. Örten gece (cenne), bir yıldız, batmak ve Rab sorusu tek pasajdadır. Kuran güneşe secdeyi yasaklar {source:41:37}, ve Sebe halkının güneşe tapmasını şeytanın süslemesine bağlar: {ar:يَسْجُدُونَ لِلشَّمْسِ مِن دُونِ ٱللَّهِ وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ, tr:yescudûne li'ş-şemsi min dûni'llâhi ve zeyyene lehumu'ş-şeytânu a'mâlehum, gloss:Allah'ı bırakıp güneşe secde ediyorlar; şeytan onlara işlerini süslemiş, source:27:24}. Yıldızlar şeytanlara karşı bekçidir: {ar:وَحِفْظًۭا مِّن كُلِّ شَيْطَٰنٍۢ مَّارِدٍۢ, tr:ve hifzan min kulli şeytânin mârid, gloss:ve her inatçı şeytana karşı koruma, source:37:7}; kulak hırsızını {ar:شِهَابٌۭ ثَاقِبٌۭ, tr:şihâbun sâkıb, gloss:delip geçen bir alev, source:37:10} izler. Cinler de bunu anlatır {source:72:9}. Karanlıkta görülen ateş Musa'nındır: {ar:إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:innî ânestu nâran lealli âtîkum minhâ bi-kabesin ev ecidu ale'n-nâri hudâ, gloss:ben bir ateş gördüm; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösteren bulurum, source:20:10}. Kıvılcım ise cehennemin ateşinde büyür {source:77:32}. Sure-kardeşindeki oluk da gecedir: yemin {ar:وَٱلَّيْلِ إِذَا عَسْعَسَ, tr:ve'l-leyli izâ as'as, gloss:kararmaya başlayan geceye, source:81:17} ile sürer.

Kaynaklar: 114:4 ٱلْخَنَّاسِ خ ن س B002; 114:6 ٱلْجِنَّةِ ج ن ن B002; 114:3 إِلَٰهِ ء ل ه B001; 114:4 شَرِّ ش ر ر B002; 114:4 شَرِّ ش ر ر B003; 114:1–6 ٱلنَّاسِ ء ن س B002; 114:1–6 ٱلنَّاسِ ء ن س B005; 114:1–6 ٱلنَّاسِ ء ن س B003; 114:1 بِرَبِّ ر ب ب B007; 114:2 مَلِكِ م ل ك B003

## At ve binici

Surenin beş kelimesi atın bir parçasını ya da koşusunu adlandırır. Binici hayvana insî yandan biner ve sağar: {ar:إنسي الدابة للجانب الذي يلي الراكب, tr:insiyyu'd-dâbbe li'l-cânibi'llezî yeli'r-râkib, gloss:hayvanın insîsi biniciye bakan yanıdır, source:"ء ن س,B004"}. Atın bacakları ve boynu onu yönetendir, onun "milk"idir: {ar:ملك الدابة قوائمها وهاديها, tr:milku'd-dâbbe kavâimuhâ ve hâdîhâ, gloss:hayvanın milki ayakları ve boynudur, source:"م ل ك,B008"}. Boynunda gerdanlığın asıldığı girdap sığınma kökündendir: {ar:معوذ الفرس موضع القلادة ودائرة المعوذ تستحب, tr:muavvizu'l-feresi mevdiu'l-kılâde, gloss:atın muavvizi gerdanlığın yeridir; o yerdeki girdap beğenilir, source:"ع و ذ,B005"}. Yeni doğurmuş kısraklar da ûz arasındadır {source:"ع و ذ,B003"}. Hannâs kökünden bir at da vardır: {ar:فرس خنوس وهو الذي يعدل وهو مستقيم في حضره ذات اليمين وذات الشمال, tr:ferasun hanûs, ve huvellezî ya'dilu ve huve mustakîmun fî hudrihî zâte'l-yemîni ve zâte'ş-şimâl, gloss:hanûs at, dörtnala düz koşarken sağa sola sapandır, source:"خ ن س,B005"}. Ve at yarışı göğüsle kazanır: {ar:صدر الفرس إذا جاء قد سبق بصدره, tr:sadera'l-feresu izâ câe kad sebeka bi-sadrih, gloss:at göğsüyle önde gelince "sadera" denir, source:"ص د ر,B002"}.

Fısıldayan, düz bir koşunun içindeki sapmadır: at yolundan çıkmaz ama sağa sola kayar. Sığınma, gerdanlığın asıldığı yerde takılır. Göğüs, yarışı kazanan uçtur; fısıltı tam oraya yerleşir.

Kuran'da İblis'in yaklaşımı aynı iki yönü adlandırır: {ar:وَعَنْ أَيْمَٰنِهِمْ وَعَن شَمَآئِلِهِمْ, tr:ve an eymânihim ve an şemâilihim, gloss:sağlarından ve sollarından, source:7:17}. Şeytana atlılar verilir {source:17:64}. Allah koşan atlara yemin eder: {ar:وَٱلْعَٰدِيَٰتِ ضَبْحًۭا, tr:ve'l-âdiyâti dabhâ, gloss:soluk soluğa koşanlara, source:100:1}, {ar:فَٱلْمُورِيَٰتِ قَدْحًۭا, tr:fe'l-mûriyâti kadhâ, gloss:nallarıyla kıvılcım çıkaranlara, source:100:2}; ve aynı sure göğüslerdekinin ortaya dökülmesiyle biter {source:100:10}.

Kaynaklar: 114:1–6 ٱلنَّاسِ ء ن س B004; 114:2 مَلِكِ م ل ك B008; 114:1 أَعُوذُ ع و ذ B005; 114:4 ٱلْخَنَّاسِ خ ن س B005; 114:5 صُدُورِ ص د ر B002; 114:1 أَعُوذُ ع و ذ B003

## Suya giden yol ve dönüş

{ar:مَلِكِ, tr:melik, gloss:hükümdar, source:114:2} kökü yolun ortasını, {ar:الزم ملك الطريق أي وسطه, tr:ilzem milke't-tarîk ey vesatah, gloss:yolun milkine, yani ortasına sarıl, source:"م ل ك,B006"}; sürünün takip ettiği öndeki hayvanı {source:"م ل ك,B008"}; ve yolcunun yanında taşıdığı, onu ayakta tutan suyu adlandırır: {ar:والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره, tr:ve'l-melku'l-mâu yekûnu mea'l-musâfir, gloss:melk yolcunun yanındaki sudur, çünkü yanında olunca işini elinde tutar, source:"م ل ك,B007"}. {ar:صُدُورِ, tr:sudûr, gloss:göğüsler, source:114:5} kökü sudan dönmeyi, {ar:الصدر الانصراف عن الورد وعن كل أمر, tr:es-sadaru'l-insirâfu ani'l-virdi ve an kulli emr, gloss:sader sudan ve her işten geri dönmektir, source:"ص د ر,B003"}; halkını sudan geri getiren yolu, {ar:طريق صادر يصدر بأهله عن الماء, tr:tarîkun sâdirun yasduru bi-ehlihî ani'l-mâ, gloss:halkını sudan geri getiren dönüş yolu, source:"ص د ر,B003"}; ve dönüşün yerini ve zamanını adlandırır {source:"ص د ر,B004"}. Rab kökü develerin durduğu yeri bilir {source:"ر ب ب,B007"}. Hannâs kökü topluluktan gizlice sıyrılanı bilir {source:"خ ن س,B001"}.

Sahne şudur: bir sürü önderinin ardından yolun ortasından suya gider, içer ve dönüş yolundan geri gelir; biri topluluktan gizlice ayrılır. Beşinci ayetteki çoğul aynı zamanda "dönüşler" diye de duyulur: göğüsler, insanın her işten döndüğü yerdir. Fısıldayan yolun ortasından ayırmaya çalışır.

Kuran bu sahneyi Musa'nın Medyen yolunda kurar: {ar:عَسَىٰ رَبِّىٓ أَن يَهْدِيَنِى سَوَآءَ ٱلسَّبِيلِ, tr:asâ rabbî en yehdiyenî sevâe's-sebîl, gloss:umarım Rabbim bana yolun ortasını gösterir, source:28:22}; suya varınca {ar:وَجَدَ عَلَيْهِ أُمَّةًۭ مِّنَ ٱلنَّاسِ يَسْقُونَ, tr:vecede aleyhi ummeten mine'n-nâsi yeskûn, gloss:başında su içiren bir insan topluluğu buldu, source:28:23}, ve kadınlar {ar:لَا نَسْقِى حَتَّىٰ يُصْدِرَ ٱلرِّعَآءُ, tr:lâneskî hattâ yusdira'r-riâ, gloss:çobanlar sürülerini sudan geri çevirmedikçe biz su veremeyiz, source:28:23} der. Sonunda: {ar:رَبِّ إِنِّى لِمَآ أَنزَلْتَ إِلَىَّ مِنْ خَيْرٍۢ فَقِيرٌۭ, tr:rabbi innî limâ enzelte ileyye min hayrin fakîr, gloss:Rabbim, bana indireceğin her hayra muhtacım, source:28:24}. Yol, su, insanlar, sudan dönüş ve Rab bir pasajdadır. Surenin iki kelimesi tek cümlede de durur: {ar:يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:yevmeizin yasduru'n-nâsu eştâten li-yurav a'mâlehum, gloss:o gün insanlar amelleri kendilerine gösterilmek üzere dağınık halde dönerler, source:99:6}. Yolun ortasında pusuya yatan İblis'tir {source:7:16}; yoldaş şeytanlar yoldan alıkoyar: {ar:وَإِنَّهُمْ لَيَصُدُّونَهُمْ عَنِ ٱلسَّبِيلِ وَيَحْسَبُونَ أَنَّهُم مُّهْتَدُونَ, tr:ve innehum le-yesuddûnehum ani's-sebîli ve yahsebûne ennehum muhtedûn, gloss:onları yoldan alıkoyarlar, onlar da doğru yolda olduklarını sanırlar, source:43:37}. Topluluğundan koparılan da anlatılır: {ar:كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا, tr:kellezi'steh'vethu'ş-şeyâtînu fi'l-ardı hayrâne lehû ashâbun yed'ûnehû ile'l-hude'tinâ, gloss:şeytanların yerde ayartıp şaşkın bıraktığı, arkadaşlarının "bize gel" diye doğru yola çağırdığı kişi gibi, source:6:71}. Yolun kendisi adlandırılır: {ar:هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ, tr:hâzâ sırâtun mustakîm, gloss:bu dosdoğru bir yoldur, source:36:61}.

Kaynaklar: 114:2 مَلِكِ م ل ك B006; 114:2 مَلِكِ م ل ك B008; 114:2 مَلِكِ م ل ك B007; 114:5 صُدُورِ ص د ر B003; 114:5 صُدُورِ ص د ر B004; 114:1 بِرَبِّ ر ب ب B007; 114:4 ٱلْخَنَّاسِ خ ن س B001

## Yüzün çevresindeki sürü ve kıvılcım

{ar:شَرِّ, tr:şerr, gloss:kötülük, source:114:4} kökü sivrisineğe benzeyen, insanın yüzünü kaplayan ama ısırmayan bir böceği adlandırır: {ar:الشران شبيه بالبعوض يغشى وجه الإنسان ولا يعض وربما سموه الأذى, tr:eş-şirrân şebîhun bi'l-baûd yağşâ vechu'l-insâni ve lâ yeuddu ve rubbemâ semmevhu'l-ezâ, gloss:şirrân sivrisineğe benzer, insanın yüzünü kaplar, ısırmaz; ona bazen "eza" derler, source:"ش ر ر,B009"}. Kök ateşten uçuşan kıvılcımı da bilir {source:"ش ر ر,B003"}. Altıncı ayetin kökü uçarken vızıltısı artan sinekleri adlandırır: {ar:جن الذباب أي كثر صوته, tr:cenne'z-zubâb ey kesura savtuh, gloss:sinek "cenne" etti, yani sesi çoğaldı, source:"ج ن ن,B015"}. Fısıltı da hafif bir hışırtıdır {source:"و س و س,B002"}. Melik kökü arıların beyini bilir: {ar:مليك النحل يعسوبها, tr:melîku'n-nahli ya'sûbuhâ, gloss:arıların meliki onların beyidir, source:"م ل ك,B008"}.

Sahne şudur: küçük şeyler yüzün çevresinde dolaşır; onu kaplar, vızıldar, parlar, hışırdar ve ısırmaz. Fısıltı bu boyda bir zarardır: yer kaplar, örter, ama yaralamaz. Kişiyi meşgul eden ama kendiliğinden yaralayamayan bir şey olduğu için ona karşı sığınmak yeterlidir.

Kuran bu ölçüyü açıkça verir: {ar:إِنَّمَا ٱلنَّجْوَىٰ مِنَ ٱلشَّيْطَٰنِ لِيَحْزُنَ ٱلَّذِينَ ءَامَنُوا۟ وَلَيْسَ بِضَآرِّهِمْ شَيْـًٔا إِلَّا بِإِذْنِ ٱللَّهِ, tr:innema'n-necvâ mine'ş-şeytâni li-yahzune'llezîne âmenû ve leyse bi-dârrihim şey'en illâ bi-izni'llâh, gloss:gizli konuşma, inananları üzmek için şeytandandır; ama Allah'ın izni olmadan onlara hiçbir zarar veremez, source:58:10}. Ezanın zarar sayılmayan ölçüsü de geçer: {ar:لَن يَضُرُّوكُمْ إِلَّآ أَذًۭى, tr:len yedurrûkum illâ ezâ, gloss:size eziyetten başka zarar veremezler, source:3:111}. Sözlükteki böceğin adı "eza", Kuran'daki ifadede de zararın altındaki rahatsızlıktır.

Kaynaklar: 114:4 شَرِّ ش ر ر B009; 114:4 شَرِّ ش ر ر B003; 114:6 ٱلْجِنَّةِ ج ن ن B015; 114:4 ٱلْوَسْوَاسِ و س و س B002; 114:2 مَلِكِ م ل ك B008

## Buluşmalar

İlk buluşma göğüstedir. Örten kök göğsün içinde çalışır: {ar:أجننت الشيء في صدري أكننته, tr:ecnentu'ş-şey'e fî sadrî, gloss:o şeyi göğsümde gizledim, source:"ج ن ن,B001"}. Görünen ve örtülü imgesi ile göğüs imgesi burada tek sahne olur: görünen insanların içinde, kemik kafesin altında, gizli kalp vardır; örtülü olan, örtülü odaya girer. Kuran'ın göğüslerini bükerek saklananları {source:11:5} da bu sahneye aittir: ne kadar örtünseler de göğüslerin özü bilinir. Sığınma imgesindeki bütün dış örtüler (göğüs giysisi, zırh, kalkan) bu odanın dışında kalır; içerdeki fısıltıya karşı yalnız söylenen söz işler.

İkinci buluşma sözdedir. Sözlük, söylenen sözü "telaffuzla dışarı çıkarılan" diye tanımlarken kullandığı fiili {source:"ق و ل,B001"} kötülük kökünün "ortaya çıkarmak" anlamında da kullanır {source:"ش ر ر,B008"}. Sure böylece iki çıkarma arasında kurulur: sığınma sözü içten dışa çıkar, fısıltının amacı ise örtülüyü açığa çıkarmaktır {source:7:20}. Söz ile çekilme de buluşur: {ar:الشيطان يوسوس فإذا ذكر الله خنس, tr:eş-şeytânu yuvesvisu fe-izâ zukira'llâhu hanes, gloss:şeytan fısıldar, Allah anılınca çekilir, source:"خ ن س,B001"}. "De" emri bu anmayı dile getirir; "sinip çekilen" sıfatı onun sonucunu adlandırır. Söz ile sığınma okunan muskada birleşir {source:"ع و ذ,B002"}: emredilen cümle, dilde taşınan korunaktır.

Üçüncü buluşma gece ile çekilmededir. Hannâs kökü hem geri çekilmeyi hem gündüz gizlenip yörüngesinde dönen yıldızları adlandırır; Kuran onlara yemin eden pasajda deliliği ve şeytan sözünü reddeder {source:81:15}. İbrahim'in gecesinde batanlara karşı {source:6:76} Rab kökünün "yerinden ayrılmayan" anlamı {source:"ر ب ب,B007"} durur. Fısıldayan gidip gelir; Rab batmaz.

Dördüncü buluşma unvanlar ile sığınmadadır: {ar:عاذ فلان بربه, tr:âze fulânun bi-rabbih, gloss:Rabbine sığındı, source:"ع و ذ,B001"}. Fiil ile unvan tek ifadede durur. Ana ve yavru imgesi bu bağa sıcaklık verir: aynı iki kök yeni doğurmuş anneyi adlandırır, ve Kuran'da bir anne yeni doğan kızını Rabbine sığındırır, Rab da onu bir bitki gibi büyütür {source:3:37}. Bağlama imgesi aynı sığınmayı topluluğa genişletir: sığınmanın açıklaması olan tutunmak {source:3:103} bütün insanları tek ipte toplar; kötülük kökü ise parçalar.

Surenin hareketi bu buluşmalarla taşınır. İlk üç ayet aynı insanları üç unvan altında, bir arada ve görünür olarak toplar; dördüncü ayet görünmeyen ve gidip gelen bir fısıltıyı adlandırır; beşinci ayet onu en içteki odaya, göğse yerleştirir; altıncı ayet kaynağını hem örtülülere hem görünenlere açar. Sığınma sözü bu yolun tersinden ilerler: içten dışa, dilde söylenir, ve yerinden ayrılmayan bir Rabbe tutunur.

