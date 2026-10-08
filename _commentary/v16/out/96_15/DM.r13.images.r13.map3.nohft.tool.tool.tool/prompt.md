Focus: 96:15. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/96_15/D.r13/context.md =====
# 96:15 — focus

كَلَّا لَئِن لَّمْ يَنتَهِ لَنَسْفَعًۢا بِٱلنَّاصِيَةِ

Anchor translation (canonical reading, reference only):

Hayır! Eğer vazgeçmezse onu perçeminden mutlaka sürükleyeceğiz.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | كَلَّا | كَلَّا |  | AVR |
| 2 | لَئِن | إِن |  | EMPH;COND |
| 3 | لَّمْ | لَم |  | NEG |
| 4 | يَنتَهِ | ٱنتَهَىٰ | ن ه ي | V |
| 5 | لَنَسْفَعًۢا | نَسْفَعًۢ | س ف ع | EMPH;V |
| 6 | بِٱلنَّاصِيَةِ | نَاصِيَة | ن ص ي | P;DET;N |


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
- 96:2 خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
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
- 96:15 ◀ focus كَلَّا لَئِن لَّمْ يَنتَهِ لَنَسْفَعًۢا بِٱلنَّاصِيَةِ
- 96:16 نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ
- 96:17 فَلْيَدْعُ نَادِيَهُۥ
- 96:18 سَنَدْعُ ٱلزَّبَانِيَةَ
- 96:19 كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩


===== _commentary/v16/work/96_15/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن ه ي (root_001560) — identity root of يَنتَهِ (w4)

- **B001** bir eylemi yasaklama, engelleme veya ondan geri durma — yasaklama ve engelleme · onu bundan alıkoyup bıraktırdı · ondan geri durdu · kötülükten birbirlerini alıkoydular · benliği tutkudan alıkoymak · kötülükten sık sık alıkoyan · onu bizden alıkoyacak kimse yok
  النهي خلاف الأمر (ayn;sihah)؛ النهي الزجر عن الشيء (mufradat)؛ نهيته عنه فانتهى عنك (maqayis;sihah)؛ وتناهوا عن المنكر أي نهى بعضهم بعضا (sihah)؛ ما تنهاه عنا ناهية أي ما تكفه عنا كافة (ayn)
- **B002** son noktaya varma veya bir şeyi hedefine ulaştırma — bitiş noktası ve son sınır · varış sınırı · son sınır · haberi ona ulaştırdı · oku ona ulaştırdı · ulaştırma ve bildirme · devenin burun bağının uç bölümü
  النهاية الغاية حيث ينتهي إليه الشيء وهو النهاء (ayn)؛ نهاية كل شيء غايته (maqayis)؛ أنهيت إليه الخبر بلغته إياه (maqayis;mufradat)؛ الإنهاء الإبلاغ وأنهيت إليه الخبر فانتهى وتناهى أي بلغ (sihah)؛ النهاية طرف العران الذي في أنف البعير (ayn)
- **B003** kötü davranışı önleyen akıl ve sağduyu — kötü davranışı önleyen sağduyu · kötü davranışı önleyen akıllar · onu durduracak aklı yok
  النهية العقل لأنه ينهى عن قبيح الفعل والجمع نهى (maqayis)؛ النهية العقول لأنها تنهى عن القبيح (sihah)؛ النهية العقل الناهي عن القبائح جمعها نهى (mufradat)
- **B004** akış sonunda suyun durulup biriktiği yer — suyun akıp toplandığı doğal gölcük · suyun akıp toplandığı doğal gölcük · su gölcükte durup sakinleşti · vadide sel sularının son bulup yayıldığı yer
  النهي والنهي الغدير لأن الماء ينتهي إليه (maqayis)؛ النهي الغدير حيث ينخرم السيل في الغدير (ayn)؛ تناهى الماء إذا وقف في الغدير وسكن (sihah)؛ تنهية الوادي حيث ينتهي إليه السيول (maqayis;mufradat)
- **B005** başkasını aratmayacak kadar yeterli [kalıp] — başkasını aratmayacak kadar yeterli adam · başkasını aratmayacak kadar yeterli adam · başkasını aratmayacak kadar yeterli adam · başkasını aratmayacak kadar yeterli kadın
  فلان ناهيك من رجل ونهيك كما يقال حسبك (maqayis)؛ هذا رجل ناهيك من رجل ونهيك من رجل ونهاك من رجل (sihah)؛ ناهيك من رجل كقولك حسبك (mufradat)
- **B006** semizliğin doruğuna ulaşmış deve [kalıp] — semizliğin doruğuna ulaşmış dişi deve · iri ve semiz kesimlik deve
  ناقة نهية تناهت سمنا (maqayis;mufradat)؛ جزور نهية أي ضخمة سمينة (sihah)
- **B007** sonuçtan bağımsız olarak ihtiyacı aramayı bırakma [kalıp] — ihtiyacı aramayı, bulsa da bulmasa da bıraktı
  طلب الحاجة حتى نهي عنها تركها ظفر بها أم لا (maqayis)؛ طلب الحاجة حتى نهى عنها أي تركها ظفر بها أو لم يظفر (sihah)؛ طلب الحاجة حتى نهي عنها أي انتهى عن طلبها ظفر بها أو لم يظفر (mufradat)
- **B008** günün veya suyun yükselmesi [kalıp] — günün yükselip öğleye yaklaşması · suyun yükselmesi
  نهاء النهار ارتفاعه (maqayis;mufradat)؛ نهاء النهار ارتفاعه قراب نصف النهار (ayn)؛ نهاء الماء بالضم ارتفاعه (sihah)
- **B009** şişe veya cam eşya için tartışmalı ad — 
  النهاء القوارير وليس كذلك عندنا (maqayis)؛ النهاء القوارير والزجاج (sihah)
- **B010** yaklaşık yüzlük miktar [kalıp] — yaklaşık yüz kişi veya öğelik miktar
  هم نهاء مائة ونهاء مائة أيضا أي قدر مائة (sihah)

## س ف ع (root_000713) — identity root of لَنَسْفَعًۢا (w5)

- **B001** başın ön saçından tutma — başın ön kısmındaki saçtan tutmak
  سفعت الفرس إذا أخذت بمقدم رأسه وهي ناصيته (maqayis)؛ سفعت بناصيته أي أخذت (sihah)؛ لنأخذن بها (tahdhib)؛ السفع الأخذ بسفعة الفرس أي سواد ناصيته (mufradat)
- **B002** kızıllık karışmış siyahlık — kızıllık karışmış siyahlık · kızıla çalan koyu renkli · koyu renkli dişi veya kadın · öfkeden yüzüne koyu bir renk çökmüş · yanakları koyu renkli kadın · koyu renkli veya kararmış olanlar · yer izlerinin çevreden ayrılan karalığı
  السفعة وهي السواد (maqayis)؛ السفعة بالضم سواد مشرب حمرة (sihah)؛ سفعاء الخدين امرأة سوداء (tahdhib)؛ باعتبار السواد قيل للأثافي سفع وبه سفعة غضب (mufradat)
- **B003** hafifçe kavurup ten rengini değiştirme — ateş onu hafifçe kavurup tenini kararttı · yakıcı sıcak rüzgar yüzünün rengini değiştirdi · kavurucu sıcak rüzgarlar
  سفعته النار والسموم إذا لفحته لفحا يسيرا فغيرت لون البشرة (sihah)؛ سفعته النار إذا لفحته لفحا يسيرا فسودت بشرته وسفعته السموم إذا لوحت بشرة الوجه (tahdhib)
- **B004** tokatlama veya vurma — kuş kanadıyla veya avına vurdu · başına değnekle vurdu · karşılıklı dövüşme ve tokatlaşma
  سفع الطائر ضريبته أي لطمه (maqayis)؛ سفع الطائر لطمه بجناحيه (sihah)؛ سفعته أي لطمته والمسافعة المضاربة (tahdhib)
- **B005** kovalamaca — kovalamaca ve peşinden gitme
  المسافعة كالمطاردة (sihah)
- **B006** kötücül varlığa bağlanan zarar — kötücül bir varlıktan geldiğine inanılan dokunma, vuruş, kem göz veya delilik · böyle bir etkiyle delirmiş sayılan kişi · kem göz değmiş kadın
  به سفعة من الشيطان أي مس كأنه أخذ بناصيته (sihah)؛ سفعة أي ضربة منه والسفعة والشفعة الجنون والمسفوعة التي أصابتها العين (tahdhib)
- **B007** özellikle boyalı giysileri giyme — kadın giysilerini giydi; çoğunlukla boyalı giysiler için söylenir · kadının giysileri
  استفعت المرأة ثيابها إذا لبستها وأكثر ما يقال ذلك في الثياب المصبوغة (tahdhib)

## ن ص ي (root_001512) — identity root of بِٱلنَّاصِيَةِ (w6)

- **B001** alın saç çizgisi; buradan tutup çekme ve denetim altına alma — alındaki saç çizgisi ya da ön saçın çıktığı yer · birini ön saçından tutmak veya çekmek · karşılıklı olarak ön saçlarından tutup çekişmek · alındaki saç çizgisi için bölgesel bir söyleyiş · ön saçlardan tutma · onu denetimi altında tutan ve üzerinde söz sahibi olan
  الناصية قصاص الشعر (maqayis;ayn;sihah;mufradat)؛ الناصية منبت الشعر في مقدم الرأس (tahdhib)؛ نصوته قبضت على ناصيته ومددتها (maqayis;ayn;sihah;tahdhib;mufradat)؛ ناصيته أخذ كل واحد بناصية صاحبه (maqayis;ayn;tahdhib;mufradat)؛ آخذ بناصيتها أي متمكن منها (mufradat)
- **B002** saçı tarama, saçın uzaması ve ölünün ön saçını çekip uzatma — saçın uzaması · ölünün başı hazırlanırken ön saçını çekip uzatmak · kadının saçını tarayıp düzene sokması · saçını tarayıp düzene sokmak
  تنصت المرأة إذا رجلت شعرها (sihah;tahdhib)؛ أن تنصى أي تسرح شعرها (tahdhib)؛ انتصى الشعر طال (maqayis;sihah;mufradat)؛ تنصون ميتكم أي تمدون ناصيته (maqayis;sihah;tahdhib;mufradat)
- **B003** seçkin kesim, en iyiyi seçme ve önde gelme — bir topluluğun ya da şeyin en iyi kesimi; kimi bağlamda geride kalan bölüm · bir şeyin en iyisini seçip almak · insanların önde gelenleri ve seçkinleri · bir topluluğun en yüksek konumdaki kesiminden evlenmek · topluluğunun önderi ve en seçkin kişisi · önden gidenler
  النصية من القوم ومن كل شيء الخيار (maqayis;sihah)؛ انتصيت الشيء اخترته (maqayis;sihah)؛ نخبة الناس وخيارهم هم نصية انتصوا (ayn)؛ نواصي الناس أشرافهم والنصية الخيار الأشراف (sihah;tahdhib)؛ النصية البقية (sihah;tahdhib)؛ الأنصاء السابقون (tahdhib)؛ فلان ناصية قومه وفلان نصية قوم أي خيارهم (mufradat)؛ تنصيتهم إذا تزوجت في الذروة منهم والناصية (sihah)
- **B004** tazeyken değerli bir otlak bitkisi — tazeyken değerli bir otlak bitkisi · o bitkinin bir arazide çokça yetişmesi
  النصي نبات من أفضل المراعي (ayn;mufradat)؛ النصى نبت ما دام رطبا فإذا ابيض فهو الطريفة وإذا ضخم ويبس فهو الحلي (sihah)؛ النصي نبت معروف ما دام رطبا فإذا يبس فهو حلي (tahdhib)؛ أنصت الأرض أي كثر نصيها (sihah)
- **B005** bir çöl düzlüğünün başka bir çöl düzlüğüne bitişmesi — bir çöl düzlüğünün başka bir çöl düzlüğüne, onun önünü kavrar gibi bitişmesi
  مفازة تناصي أخرى كأنها تتصل بها كالقابضة على ناصيتها (maqayis)؛ مفازة تناصي مفازة إذا كانت الأولى متصلة بالأخرى (ayn)؛ فلاة تناصي فلاة أي تتصل بها (sihah;tahdhib)؛ تناصي أرض كذا وتواصيها أي تتصل بها (tahdhib)
- **B006** karında batıcı, huzursuz eden sancı — karında duyulan, kişiyi rahat duramaz hale getiren batıcı sancı
  أجد في بطني نصوا ووخزا (tahdhib)؛ النصو مثل المفس سمي نصوا لأنه ينصوك أي يزعجك عن القرار (tahdhib)؛ وجدت في بطني حصوا ونصوا وقبصا بمعنى واحد (tahdhib)

===== _commentary/v16/out/s096/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 96:15, and ## Buluşmalar) =====
## Ad, iz, işaret

Bir şey, üzerine yükseltilen ya da içine bastırılan bir işaretle tanınır. Sure {ar:بِٱسْمِ, tr:bismi, gloss:adıyla, source:96:1} diye başlar. Ad kelimesinin kökü yüksekliktir: {ar:أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى, tr:aslu ismin sumuvvun ve huve mine'l-ʿuluvv, gloss:ismin aslı yükselmedir; çünkü anlamı ortaya çıkarır ve ona işaret eder, source:"س م و,B005"}. Kayıtlı bir başka türetmeye göre ise ad bir damgadır: {ar:ووسمت الشيء وسما: أثرت فيه بسمة, tr:ve vesemtu'ş-şey'e vesmen, gloss:bir şeye damga vurarak iz bıraktım, source:"و س م,B001"}. İlk anlamda ad, yükseğe kaldırılan bir işarettir; ikinci anlamda bir şeye bastırılan izdir. Kurân Rab'bin adını yükseklikle ve yaratmayla birlikte anar: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-aʿlâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1}, {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî halaka fe sevvâ, gloss:ki yarattı ve düzenledi, source:87:2}. Bu yapı surenin ilk ayetine çok yakındır. Adı anmak secdeye de bağlanır: {ar:وَٱذْكُرِ ٱسْمَ رَبِّكَ بُكْرَةً وَأَصِيلًا, tr:vezkuri'sme rabbike bukraten ve asîlâ, gloss:sabah akşam Rabbinin adını an, source:76:25}, {ar:وَمِنَ ٱلَّيْلِ فَٱسْجُدْ لَهُۥ, tr:ve mine'l-leyli fescud leh, gloss:gecenin bir kısmında O'na secde et, source:76:26}.

Öğretme kökü de işarettir: {ar:أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره, tr:aslun sahîhun vâhidun yedullu ʿalâ eserin bi'ş-şey', gloss:bir şeyi diğerlerinden ayıran bir ize delalet eden tek bir asıl, source:"ع ل م,B002"}. Bu kök sancağı ve kumaşın kenar nakışını da adlandırır: {ar:العلم الراية, tr:el-ʿalemu'r-râye, gloss:alem sancaktır, source:"ع ل م,B002"}. Görme kökü de bu sancağa varır: {ar:الراية العلامة المنصوبة للرؤية, tr:er-râyetu'l-ʿalâmetu'l-mensûbetu li'r-ru'ye, gloss:sancak, görülmek için dikilmiş işarettir, source:"ر ء ي,B011"}. On ikinci ayetteki {ar:أَمَرَ, tr:emera, gloss:emretti, source:96:12} fiilinin ailesinde yol işareti vardır: {ar:الأمارة العلامة، والأمار أمار الطريق معالمه, tr:el-emâretu'l-ʿalâme, gloss:emâre işarettir; emâr, yolun belirtileridir, source:"ء م ر,B005"}. Sekizinci ayetin dönüş kelimesinin ailesinde, yazının çizgilerinin tekrar tekrar mürekkeplenmesi bulunur: {ar:أن يعاد عليه السواد مرة بعد أخرى, tr:en yuʿâde ʿaleyhi's-sevâdu merraten baʿde uhrâ, gloss:üzerine siyahın tekrar tekrar geçirilmesi, source:"ر ج ع,B009"}.

Sure bu işaretleri yüze taşır. On beşinci ayetin {ar:لَنَسْفَعًۢا, tr:le nesfaʿan, gloss:mutlaka yakalarız, source:96:15} fiilinin ailesinde koyu bir leke vardır: {ar:السفعة بالضم سواد مشرب حمرة, tr:es-sufʿa sevâdun uşribe humra, gloss:sufʿa, kırmızıya çalan siyahlıktır, source:"س ف ع,B002"}. Son ayetin secdesinin ailesinde ise alındaki iz vardır: {ar:المسجد بالفتح جبهة الرجل حيث يصيبه ندب السجود, tr:el-mesced cebhetu'r-racul, gloss:mesced, adamın secde izinin düştüğü alnıdır, source:"س ج د,B003"}. Kurân iki tarafın da yüzüne iz koyar. Müminler için {ar:سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ, tr:sîmâhum fî vucûhihim min eseri's-sucûd, gloss:secde izinden belirtileri yüzlerindedir, source:48:29} denir. Çok yemin eden iftiracı için {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16} denir. Suçlular da yüzlerindeki işaretle tanınır: {ar:يُعْرَفُ ٱلْمُجْرِمُونَ بِسِيمَٰهُمْ فَيُؤْخَذُ بِٱلنَّوَٰصِى وَٱلْأَقْدَامِ, tr:yuʿrafu'l-mucrimûne bi sîmâhum fe yu'hazu bi'n-nevâsî ve'l-akdâm, gloss:suçlular belirtilerinden tanınır, perçemlerinden ve ayaklarından yakalanırlar, source:55:41}. Yazılı kayıt da işaretlenmiştir: {ar:كِتَٰبٌ مَّرْقُومٌ, tr:kitâbun merkûm, gloss:işaretlenmiş bir kitap, source:83:20}, {ar:يَشْهَدُهُ ٱلْمُقَرَّبُونَ, tr:yeşheduhu'l-mukarrabûn, gloss:ona yakınlaştırılanlar şahit olur, source:83:21}.

Böylece sure Rab'bin adıyla başlar, işaret koyan bir araçla öğretir ve iki işaretli alınla biter: biri yakalanıp karartılan alın, öteki secdenin iz bıraktığı alın.

Kaynaklar: 96:1 بِٱسْمِ س م و B005; 96:1 بِٱسْمِ و س م B001; 96:4 عَلَّمَ ع ل م B002; 96:7 رَّءَاهُ ر ء ي B011; 96:12 أَمَرَ ء م ر B005; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B009; 96:15 لَنَسْفَعًۢا س ف ع B002; 96:19 وَٱسْجُدْ س ج د B003

## Tutunmak ve kendini yeterli görmek

İnsan, tutunan bir şeyden yaratılmıştır. Alak kökü asılmayı ve yapışmayı adlandırır: {ar:يناط الشيء بالشيء العالي, tr:yunâtu'ş-şey'u bi'ş-şey'i'l-ʿâlî, gloss:bir şeyin yüksekteki bir şeye asılması, source:"ع ل ق,B001"}; {ar:علق بالشيء نشب به, tr:ʿalika bi'ş-şey'i neşibe bih, gloss:bir şeye takıldı, ona yapıştı, source:"ع ل ق,B001"}. Aynı kök suya yapışan sülüğü de adlandırır: {ar:دويبة في الماء تجمع على علق, tr:duveybetun fi'l-mâ', gloss:suda yaşayan küçük bir hayvan; çoğulu alaktır, source:"ع ل ق,B003"}. Ayrıca canı ayakta tutan en az lokmayı adlandırır: {ar:ما يأكل فلان إلا علقة أي ما يمسك نفسه, tr:mâ ye'kulu fulânun illâ ʿulka, gloss:falan ancak canını tutacak kadar yer, source:"ع ل ق,B006"}. İnsanın başlangıcı yüksekteki bir şeye asılı, tutunarak ve azla yaşayan bir şeydir.

Beşinci ayet bu eksik varlığa öğretilen şeyi anar: bilmediği şey ona verilir. Yedinci ayet sonra tersine döner: insan kendini {ar:ٱسْتَغْنَىٰٓ, tr:istagnâ, gloss:muhtaç olmayan, yeterli, source:96:7} görür. Kök ihtiyaçsızlığı adlandırır: {ar:عدم الحاجات وقلة الحاجات وكثرة القنيات, tr:ʿademu'l-hâcât ve killetu'l-hâcât ve kesretu'l-kunyât, gloss:ihtiyaçların olmaması, azlığı ve edinilmiş şeylerin çokluğu, source:"غ ن ي,B001"}. Aynı kök bir şeyin yetip yetmemesini de anlatır: {ar:ما يغني عنك هذا أي ما يجزئ وما ينفع, tr:mâ yugnî ʿanke hâzâ, gloss:bu sana yetmez, fayda vermez, source:"غ ن ي,B002"}. Kökte kendine bakışla yeterliliği tek figürde birleştiren bir kadın da vardır: {ar:الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي, tr:el-gâniye, gloss:gâniye, kocası ya da güzelliği sayesinde süs takmaya ihtiyaç duymayan kadındır, source:"غ ن ي,B005"}. Yedinci ayetteki "kendini görmek" ile "yeterli olmak" bu figürde bir araya gelir.

Kurân bu kelimeyi birkaç sahnede inkârla birleştirir: {ar:وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ, tr:ve emmâ men bahile ve'stagnâ, gloss:cimrilik eden ve kendini muhtaç görmeyene gelince, source:92:8}, {ar:وَكَذَّبَ بِٱلْحُسْنَىٰ, tr:ve kezzebe bi'l-husnâ, gloss:ve en güzeli yalanlayan, source:92:9}. Peygamber'e, kendini yeterli gören zengin kişiye yönelmesi hatırlatılır: {ar:أَمَّا مَنِ ٱسْتَغْنَىٰ, tr:emmâ meni'stagnâ, gloss:kendini muhtaç görmeyene gelince, source:80:5}, {ar:فَأَنتَ لَهُۥ تَصَدَّىٰ, tr:fe ente lehû tesaddâ, gloss:sen ona yöneliyorsun, source:80:6}. Gerçek yeterliliğin kime ait olduğu da söylenir. Elçilerini reddedenler için {ar:فَكَفَرُوا۟ وَتَوَلَّوا۟ وَّٱسْتَغْنَى ٱللَّهُ, tr:fe keferû ve tevellev vestagna'llâh, gloss:inkâr ettiler ve yüz çevirdiler, Allah da onlara ihtiyaç duymadı, source:64:6} denir. Tüm insanlara da {ar:أَنتُمُ ٱلْفُقَرَآءُ إِلَى ٱللَّهِ وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:entumu'l-fukarâ'u ila'llâh, va'llâhu huve'l-ganiyyu'l-hamîd, gloss:Allah'a muhtaç olanlar sizsiniz, ihtiyaçsız ve övülmeye layık olan Allah'tır, source:35:15} denir. Hesap gününde ise yeterlilik iddiası kendi ağzından çöker: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ, tr:mâ agnâ ʿannî mâliyeh, gloss:malım bana hiçbir yarar sağlamadı, source:69:28}.

Rab kelimesinin ailesinde ihtiyaç ile nimet tek kelimede birleşir: {ar:الربى: الحاجة؛ … الربى: النعمة والإحسان, tr:er-rubbâ: el-hâce … er-rubbâ: en-niʿmetu ve'l-ihsân, gloss:rubbâ ihtiyaçtır; rubbâ nimet ve iyiliktir da, source:"ر ب ب,B016"}. Üçüncü ayetteki en cömert sıfatı ihtiyacı gideren vericiyi anlatır: {ar:الكثير الخير الجواد المنعم المفضل, tr:el-kesîru'l-hayr el-cevâdu'l-munʿim, gloss:hayrı çok, cömert, nimet veren, lütfeden, source:"ك ر م,B001"}. Kurân insanın bu cömertliğe nasıl karşılık verdiğini anlatır: {ar:فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ, tr:fe ekramehû ve naʿʿamehû fe yekûlu rabbî ekramen, gloss:Rabbi ona ikram edip nimet verince "Rabbim bana ikram etti" der, source:89:15}. Hemen ardından rızkı daraltılınca {ar:فَيَقُولُ رَبِّىٓ أَهَٰنَنِ, tr:fe yekûlu rabbî ehânen, gloss:"Rabbim beni aşağıladı" der, source:89:16}. Kısacası insan, ikramı kendi değerinin kanıtı sayar.

On beşinci ayetteki {ar:يَنتَهِ, tr:yentehi, gloss:vazgeçer, source:96:15} fiilinin ailesinde "yeter" anlamı vardır: {ar:فلان ناهيك من رجل… كما يقال حسبك, tr:fulânun nâhîke min racul, gloss:falan sana yeter bir adamdır, "hasbuk" dendiği gibi, source:"ن ه ي,B005"}. Onuncu ayetin kulu ise kendine ait bir şeyi olmayandır: {ar:العبد وهو المملوك, tr:el-ʿabdu ve huve'l-memlûk, gloss:kul, sahip olunandır, source:"ع ب د,B001"}. Sekizinci ayetteki dönüş, yeterlilik iddiasını geçersiz kılar: asılı başlayan varlık, asıl olduğu yere döner.

Kaynaklar: 96:2 عَلَقٍ ع ل ق B001; 96:2 عَلَقٍ ع ل ق B003; 96:2 عَلَقٍ ع ل ق B006; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B001; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B002; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B005; 96:1 رَبِّكَ ر ب ب B016; 96:3 ٱلْأَكْرَمُ ك ر م B001; 96:15 يَنتَهِ ن ه ي B005; 96:10 عَبْدًا ع ب د B001

## Su: bulut, yağmur, taşkın ve gölet

Bu sahne suyun bütün yolculuğunu izler. Bulut yağmur getirir, ilk yağmur yeri bitkiyle işaretler, ardından ikinci yağmur gelir, yağmur döne döne yağar. Bazı yerler ise atlanır. Su bazen ölçüsünü aşar, taşar ve her şeyi sürükler, sonra yolunun sonundaki gölete varır ve orada durulur.

Üçüncü ayetteki en cömert sıfatının ailesinde yağmur getiren bulut ve verimli toprak vardır: {ar:كرم السحاب أتى بالغيث, tr:kerume's-sehâb, gloss:bulut cömert oldu, yani yağmur getirdi, source:"ك ر م,B002"}; {ar:أرض مكرمة للنبات, tr:ardun mekrame li'n-nebât, gloss:bitkiye cömert toprak, source:"ك ر م,B002"}. Rab kelimesinin ailesinde bitkileri büyüten bulut vardır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb, gloss:rabâb buluttur; bitkiyi büyüttüğü için böyle adlandırılmıştır, source:"ر ب ب,B008"}. Bu, rahimdeki cenini aşama aşama büyüten aynı terbiye işidir. Kayıtlı bir türetmeye göre ad kelimesinin ailesinde de yılın ilk yağmuru vardır: {ar:الوسمي أول مطر السنة يسم الأرض بالنبات, tr:el-vesmiyyu evvelu matari's-sene, gloss:vesmî, yeri bitkiyle işaretleyen yılın ilk yağmurudur, source:"و س م,B003"}. On üçüncü ayetteki {ar:وَتَوَلَّىٰٓ, tr:ve tevellâ, gloss:ve yüz çevirdi, source:96:13} fiilinin kökünde bu yağmuru izleyen yağmur bulunur: {ar:الولي المطر يجيء بعد الوسمي سمي بذلك لأنه يلي الوسمي, tr:el-veliyy el-matar yecî'u baʿde'l-vesmî, gloss:veliy, vesmîden sonra gelen yağmurdur; onu izlediği için böyle denir, source:"و ل ي,B010"}. Bu iki aile anlamı birer yankıdır; ayetlerdeki anlamlar "ad" ve "yüz çevirme"dir. Sekizinci ayetteki dönüş kelimesinin ailesinde ise dönüp duran yağmur vardır: {ar:الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث, tr:er-recʿu'l-gays, gloss:rec yağmurdur, çünkü yağar, sonra döner ve tekrar yağar, source:"ر ج ع,B006"}. Kurân göğe bu sıfatla yemin eder: {ar:وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ, tr:ve's-semâ'i zâti'r-recʿ, gloss:dönüp dönüp yağmur veren göğe andolsun, source:86:11}. On yedinci ayetin {ar:نَادِيَهُۥ, tr:nâdiyeh, gloss:meclisini, source:96:17} kelimesinin ailesinde nem ve cömertlik vardır: {ar:يعبر عن السخاء بالندى, tr:yuʿabbaru ʿani's-sehâ'i bi'n-nedâ, gloss:cömertlik "nem" ile ifade edilir, source:"ن د و,B004"}. On altıncı ayetin {ar:خَاطِئَةٍ, tr:hâti'e, gloss:günahkâr, source:96:16} kelimesinin ailesinde ise yağmurun atladığı toprak vardır: {ar:الخطيئة أرض يخطئها المطر ويصيب غيرها, tr:el-hatî'e ardun yuhti'uha'l-matar, gloss:hatîe, yağmurun ıskalayıp başka yere düştüğü topraktır, source:"خ ط ء,B003"}.

Kurân rahim ile yağmuru tek ayette birleştirir. Rahimdeki aşamalardan sonra {ar:وَتَرَى ٱلْأَرْضَ هَامِدَةً فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:ve tera'l-arda hâmideten fe izâ enzelnâ ʿaleyhe'l-mâ'e'htezzet ve rabet, gloss:yeri kupkuru görürsün; üzerine suyu indirince harekete geçer ve kabarır, source:22:5} denir. Bu ayet canlanmayı yaratılışla aynı kanıta bağlar. Dünya hayatı da yağmurla büyüyüp biçilen bir ekin olarak anlatılır: {ar:كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:keen lem tegne bi'l-ems, gloss:sanki dün orada hiç yokmuş gibi, source:10:24}. Bu ifadede, yedinci ayetin yeterlilik köküyle aynı kökten bir fiil, yerleşik yaşamın bir gecede silinmesini anlatır.

Su ölçüsünü de aşabilir. Altıncı ayetin azma fiili için {ar:طغى الماء خروجه عن المقدار, tr:tagâ'l-mâ' hurûcuhû ʿani'l-mikdâr, gloss:suyun azması ölçüsünden çıkmasıdır, source:"ط غ ي,B002"} ve {ar:طغا البحر والماء إذا علا كل شيء فاجترفه, tr:tagâ'l-bahru ve'l-mâ', gloss:deniz ve su her şeyin üstüne çıkıp onu sürükledi, source:"ط غ ي,B002"} denir. Kök genel olarak ölçüyü aşmaktır: {ar:كل شيء جاوز القدر فقد طغا, tr:kullu şey'in câveze'l-kadr fe kad tagâ, gloss:ölçüyü aşan her şey azmıştır, source:"ط غ ي,B001"}. Kurân bunu Nuh'un tufanı için kullanır: {ar:إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ, tr:innâ lemmâ tage'l-mâ'u hamelnâkum fi'l-câriye, gloss:su taştığında sizi akan gemide taşıdık, source:69:11}. Kuralı da teraziyle birlikte koyar: {ar:أَلَّا تَطْغَوْا۟ فِى ٱلْمِيزَانِ, tr:ellâ tatgav fi'l-mîzân, gloss:ölçüde aşırı gitmeyesiniz diye, source:55:8}. Böylece azma, yaratmanın ölçüsünün karşısına konur.

Taşkının sonu gölettir. On beşinci ayetin vazgeçme fiilinin ailesinde şu anlamlar bulunur: {ar:النهي والنهي الغدير لأن الماء ينتهي إليه, tr:en-nehy, el-gadîr, gloss:nehy göllenmiş sudur, çünkü su ona varıp durur, source:"ن ه ي,B004"}; {ar:تناهى الماء إذا وقف في الغدير وسكن, tr:tenâha'l-mâ', gloss:su gölette durup sakinleşti, source:"ن ه ي,B004"}. Dönüş kelimesinin ailesinde gölete de "rec" denir: {ar:سمي الغدير رجعا, tr:summiye'l-gadîru racʿan, gloss:gölete rec denmiştir, source:"ر ج ع,B006"}. Rab kelimesinin ailesinde de toplanmış bol su vardır: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabab el-mâ'u'l-kesîr, gloss:rabab, toplandığı için böyle denen bol sudur, source:"ر ب ب,B013"}. Böylece on beşinci ayetteki "vazgeçmezse" ifadesinin yanında, suyun durulduğu yerde durmaması da duyulur. Sekizinci ayet suyun varacağı yeri söyler. Kurân bunu ilahî adla birleştiren bir kardeş ayet içerir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Bu yapı sekizinci ayetle aynıdır; tek fark, dönüş yerine varış kökünün kullanılmasıdır.

Kaynaklar: 96:3 ٱلْأَكْرَمُ ك ر م B002; 96:1 رَبِّكَ ر ب ب B008; 96:1 بِٱسْمِ و س م B003; 96:13 وَتَوَلَّىٰٓ و ل ي B010; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B006; 96:17 نَادِيَهُۥ ن د و B004; 96:16 خَاطِئَةٍ خ ط ء B003; 96:6 لَيَطْغَىٰٓ ط غ ي B002; 96:6 لَيَطْغَىٰٓ ط غ ي B001; 96:15 يَنتَهِ ن ه ي B004; 96:8 رَبِّكَ ر ب ب B013

## Başın önü: perçem, alın ve yer

Bu sahne başın ön kısmında geçer. Saç çizgisinde perçem çıkar, altında alnın düz yüzü vardır. Azan adam bu kısmı yukarı kaldırır, bu kısımdan yakalanır ve derisi kararır. Kul ise aynı kısmı yere koyar.

On beşinci ve on altıncı ayetlerin {ar:ٱلنَّاصِيَةِ, tr:en-nâsiye, gloss:perçem, alnın üstündeki saç, source:96:15} kelimesi önce bir yeri adlandırır: {ar:الناصية منبت الشعر في مقدم الرأس, tr:en-nâsiyetu menbitu'ş-şaʿr fî mukaddemi'r-re's, gloss:nâsiye, başın önünde saçın bittiği yerdir, source:"ن ص ي,B001"}. Sonra bir tutuşu adlandırır: {ar:آخذ بناصيتها أي متمكن منها, tr:âhizun bi nâsiyetihâ, gloss:perçeminden tutan, yani ona tam hâkim olan, source:"ن ص ي,B001"}. On beşinci ayetin fiili bu tutuşun kendisidir: {ar:سفعت الفرس إذا أخذت بمقدم رأسه وهي ناصيته, tr:sefaʿtu'l-feres, gloss:atı başının önünden, yani perçeminden tuttum, source:"س ف ع,B001"}. Bu kalıp hem fiili hem perçemi tek cümlede birleştirir. Aynı fiil yüzün kararmasını da anlatır: {ar:سفعته النار والسموم إذا لفحته لفحا يسيرا فغيرت لون البشرة, tr:sefaʿathu'n-nâru ve's-semûm, gloss:ateş ya da kızgın rüzgâr onu hafifçe yalayıp deri rengini değiştirdi, source:"س ف ع,B003"}. Öfkeden kararan yüz için de {ar:به سفعة غضب, tr:bihî sufʿatu gadab, gloss:yüzünde öfke karası var, source:"س ف ع,B002"} denir. Kurân perçemden tutmayı her canlıya genelleştirir. Hud kavmine şöyle der: {ar:مَّا مِن دَآبَّةٍ إِلَّا هُوَ ءَاخِذٌۢ بِنَاصِيَتِهَآ, tr:mâ min dâbbetin illâ huve âhizun bi nâsiyetihâ, gloss:O'nun perçeminden tutmadığı hiçbir canlı yoktur, source:11:56}. Kurân bunu suçlular için de söyler: {ar:فَيُؤْخَذُ بِٱلنَّوَٰصِى وَٱلْأَقْدَامِ, tr:fe yu'hazu bi'n-nevâsî ve'l-akdâm, gloss:perçemlerinden ve ayaklarından tutulurlar, source:55:41}. Yüzün ateşte sürüklenmesi de anlatılır: {ar:يَوْمَ يُسْحَبُونَ فِى ٱلنَّارِ عَلَىٰ وُجُوهِهِمْ, tr:yevme yushabûne fi'n-nâri ʿalâ vucûhihim, gloss:ateşte yüzüstü sürüklenecekleri gün, source:54:48}. Cehennemin deriyi yakması da: {ar:لَوَّاحَةٌ لِّلْبَشَرِ, tr:levvâhatun li'l-beşer, gloss:deriyi kavurup karartan, source:74:29}.

Perçem aynı zamanda kavmin başıdır: {ar:فلان ناصية قومه, tr:fulânun nâsiyetu kavmih, gloss:falan kavminin perçemidir, yani önderidir, source:"ن ص ي,B003"}. Bu yüzden on altıncı ayetteki {ar:نَاصِيَةٍ كَٰذِبَةٍ خَاطِئَةٍ, tr:nâsiyetin kâzibetin hâti'e, gloss:yalancı, günahkâr bir perçem, source:96:16} ifadesinde hem adamın kendisi hem de on yedinci ayette çağırdığı meclisin başı duyulur. Sıfatlar perçeme yalan ve kasıtlı günah yükler: {ar:الخاطئ هو القاصد للذنب, tr:el-hâti'u huve'l-kâsidu li'z-zenb, gloss:hâti, günaha kasteden kişidir, source:"خ ط ء,B002"}.

Başın yükseltilmesi altıncı ayetin fiilinde de görülür: {ar:الطغية أعلى الجبل, tr:et-tugye aʿle'l-cebel, gloss:tugye dağın en yüksek yeridir, source:"ط غ ي,B005"}. Alnın düz yüzü de yaratma kökünden adlandırılır: {ar:خليقاء الجبهة مستواها, tr:halîkâ'u'l-cebhe, gloss:halîkâ, alnın düz yüzüdür, source:"خ ل ق,B008"}. Kurân başını en yükseğe kaldıranı Firavun'da gösterir: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe kâle ene rabbukumu'l-aʿlâ, gloss:"ben sizin en yüce rabbinizim" dedi, source:79:24}. Arkasından da {ar:فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ, tr:fe ehazehu'llâhu nekâle'l-âhirati ve'l-ûlâ, gloss:Allah onu ahiret ve dünya cezasıyla yakaladı, source:79:25} denir.

Son ayetin secde emri bu sahnenin karşı yüzüdür: {ar:سجد: خضع ومنه سجود الصلاة وهو وضع الجبهة على الأرض, tr:secede: hadaʿa, gloss:secde etti, yani boyun eğdi; namazdaki secde alnı yere koymaktır, source:"س ج د,B001"}; {ar:أسجد الرجل إذا طأطأ رأسه وانحنى, tr:escede'r-racul, gloss:adam başını eğip öne büküldü, source:"س ج د,B004"}. Yukarı kaldırılan ve yakalanıp karartılan alın ile yere konup secde izi taşıyan alın aynı organdır. Sure bu organı iki şekilde gösterir ve iki yol arasındaki farkı başın konumu üzerinden anlatır.

Kaynaklar: 96:15 ٱلنَّاصِيَةِ ن ص ي B001; 96:15 لَنَسْفَعًۢا س ف ع B001; 96:15 لَنَسْفَعًۢا س ف ع B002; 96:15 لَنَسْفَعًۢا س ف ع B003; 96:16 نَاصِيَةٍ ن ص ي B003; 96:16 خَاطِئَةٍ خ ط ء B002; 96:6 لَيَطْغَىٰٓ ط غ ي B005; 96:1 خَلَقَ خ ل ق B008; 96:19 وَٱسْجُدْ س ج د B001; 96:19 وَٱسْجُدْ س ج د B004

## Başından tutulan hayvan

Perçemden tutma sahnesi bir hayvanı da çağırır. Huysuz hayvan sağanı teper ya da insanlara direnir; perçeminden, burun ipinin ucundan tutulur. Dizgine uyan hayvan kolay yönetilir. Soylu at yakında tutulur ve değer görür.

On sekizinci ayetin {ar:ٱلزَّبَانِيَةَ, tr:ez-zebâniye, gloss:zebaniler, source:96:18} kelimesinin ailesinde, sağanı ya da yavrusunu ayağıyla iten deve vardır: {ar:ناقة زبون إذا زبنت حالبها أو ولدها عن ضرعها برجلها, tr:nâkatun zebûn, gloss:sağanı ya da yavrusunu ayağıyla memesinden iten deve, source:"ز ب ن,B001"}. Onuncu ayetin kul kelimesinin ailesinde iki zıt deve bulunur: {ar:بعير متعبد ومتأبد إذا امتنع على الناس صعوبة, tr:baʿîrun mutaʿabbid, gloss:insanlara direnen huysuz deve, source:"ع ب د,B011"} ve {ar:البعير المعبد المهنوء بالقطران المذلل, tr:el-baʿîru'l-muʿabbed, gloss:katranla bakılmış, alıştırılmış deve, source:"ع ب د,B005"}. On beşinci ayetin vazgeçme fiilinin ailesinde burun ipinin ucu vardır: {ar:النهاية طرف العران الذي في أنف البعير, tr:en-nihâye tarafu'l-ʿirân, gloss:nihâye, devenin burnundaki ipin ucudur, source:"ن ه ي,B002"}. Son ayetin {ar:تُطِعْهُ, tr:tutiʿhu, gloss:ona boyun eğme, source:96:19} fiilinin ailesinde de dizgine uyan at vardır: {ar:فرس طوع العنان, tr:ferasun tavʿu'l-ʿinân, gloss:dizgine uysal at, source:"ط و ع,B001"}.

Son ayetin {ar:وَٱقْتَرِب, tr:vakterib, gloss:ve yaklaş, source:96:19} emrinin ailesinde yakında tutulan at vardır: {ar:فرس مقربة وهي التي تدنى وتقرب ولا تترك أن ترود والمقربة المكرمة, tr:ferasun mukrabe … ve'l-mukrabetu'l-mukrame, gloss:mukrabe at, yakına alınıp otlamaya salınmayan attır; mukrabe, değer verilen demektir, source:"ق ر ب,B013"}. Bu ifade yakınlığı üçüncü ayetteki cömertlik köküyle birleştirir. Onuncu ayetin namaz fiilinin ailesinde de yarışta ikinci gelen at vardır: {ar:السابق الأول والمصلي الثاني, tr:es-sâbiku'l-evvel ve'l-musallî es-sânî, gloss:sâbık birincidir, musallî ikinci, source:"ص ل و,B006"}. İkinci atın başı öndekinin sağrısını izler. Kurân önde olanları yakınlıkla adlandırır: {ar:وَٱلسَّٰبِقُونَ ٱلسَّٰبِقُونَ, tr:ve's-sâbikûne's-sâbikûn, gloss:önde olanlar, önde olanlardır, source:56:10}, {ar:أُو۟لَٰٓئِكَ ٱلْمُقَرَّبُونَ, tr:ulâ'ike'l-mukarrabûn, gloss:onlar yakınlaştırılanlardır, source:56:11}. Atlar ile nankör insan da bir surede yan yana gelir: {ar:وَٱلْعَٰدِيَٰتِ ضَبْحًا, tr:ve'l-ʿâdiyâti dabhâ, gloss:soluk soluğa koşanlara andolsun, source:100:1}, {ar:إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌ, tr:inne'l-insâne li rabbihî le kenûd, gloss:insan Rabbine karşı gerçekten nankördür, source:100:6}.

Bu sahnede azmak, dizgine direnmektir: {ar:مجاوزة الحد في العصيان, tr:mucâvezetu'l-hadd fi'l-ʿisyân, gloss:isyanda sınırı aşmak, source:"ط غ ي,B001"}. Yasaklayan adam huysuz hayvan gibi perçeminden tutulur. Kul ise yakında tutulan, değer gören at gibi yaklaşmaya çağrılır. "Ona boyun eğme" emri, hangi elin dizgine sahip olduğu sorusunu sorar.

Kaynaklar: 96:18 ٱلزَّبَانِيَةَ ز ب ن B001; 96:10 عَبْدًا ع ب د B011; 96:10 عَبْدًا ع ب د B005; 96:15 يَنتَهِ ن ه ي B002; 96:19 تُطِعْهُ ط و ع B001; 96:19 وَٱقْتَرِب ق ر ب B013; 96:10 صَلَّىٰٓ ص ل و B006; 96:6 لَيَطْغَىٰٓ ط غ ي B001

## Ateş: namaz kılan ve yanan

Onuncu ayetin {ar:صَلَّىٰٓ, tr:sallâ, gloss:namaz kıldı, source:96:10} fiilinin kökü iki tarafı birden adlandırır. Bir anlamı namazdır: {ar:الصلاة التي جاء بها الشرع من الركوع والسجود, tr:es-salâtu'lletî câ'e bihe'ş-şerʿ, gloss:şeriatın getirdiği rükû ve secdeli namaz, source:"ص ل و,B003"}. Öteki anlamı ateşe girmek ve sıcağına katlanmaktır: {ar:الصلا النار وصلى الكافر نارا, tr:es-salâ en-nâr, ve saliye'l-kâfiru nârâ, gloss:salâ ateştir; kâfir ateşe girdi, source:"ص ل و,B001"}; {ar:صليت العود بالنار, tr:salaytu'l-ʿûde bi'n-nâr, gloss:değneği ateşte tutup düzelttim, source:"ص ل و,B001"}. Kurân bu ikiliği kendi eşleştirmeleriyle kurar. Ateşe kimin gireceğini söylerken surenin on üçüncü ayetindeki ifadeyi kullanır: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}, {ar:ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ, tr:ellezî kezzebe ve tevellâ, gloss:ki yalanladı ve yüz çevirdi, source:92:16}, {ar:وَسَيُجَنَّبُهَا ٱلْأَتْقَى, tr:ve seyucennebuhe'l-etkâ, gloss:en çok sakınan ise ondan uzak tutulacak, source:92:17}. Bu ayetlerde ateşe girmek, yalanlamak, yüz çevirmek ve sakınmak bir aradadır; bunlar surenin on ikinci ve on üçüncü ayetlerinin kelimeleridir. Ölüm anındaki inkârcı için de namaz yalanlamanın karşısına konur: {ar:فَلَا صَدَّقَ وَلَا صَلَّىٰ, tr:fe lâ saddeka ve lâ sallâ, gloss:ne doğruladı ne namaz kıldı, source:75:31}, {ar:وَلَٰكِن كَذَّبَ وَتَوَلَّىٰ, tr:ve lâkin kezzebe ve tevellâ, gloss:ama yalanladı ve yüz çevirdi, source:75:32}. Musa ile Harun da Firavun'a aynı ifadeyle seslenir: {ar:أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ, tr:enne'l-ʿazâbe ʿalâ men kezzebe ve tevellâ, gloss:azap yalanlayıp yüz çevirenedir, source:20:48}. Cehennemdekiler ise kendilerini oraya getiren şeyi şöyle söyler: {ar:قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ, tr:kâlû lem neku mine'l-musallîn, gloss:"namaz kılanlardan değildik" dediler, source:74:43}.

Yakalamak ve ateşe atmak bir başka sahnede art arda gelir: {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe gullûh, gloss:tutun onu, bağlayın, source:69:30}, {ar:ثُمَّ ٱلْجَحِيمَ صَلُّوهُ, tr:summe'l-cahîme sallûh, gloss:sonra cehenneme atın, source:69:31}. Bu, yeterliliğinin işe yaramadığını söyleyen adamın sahnesidir. Ateş kendisi de çağırır: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Böylece on yedinci ve on sekizinci ayetlerin çağrısı ateşin çağrısıyla buluşur.

On beşinci ayetin fiili bu sahnede yüzün yanıp kararmasıdır: {ar:سفعته النار إذا لفحته لفحا يسيرا فسودت بشرته, tr:sefaʿathu'n-nâr, gloss:ateş onu hafifçe yaladı ve derisini kararttı, source:"س ف ع,B003"}. Altıncı ayetin fiilinin ailesinde yıldırım azabı vardır: {ar:الطاغية الصاعقة ويعني صيحة العذاب, tr:et-tâgiye es-sâʿika, gloss:tâgiye yıldırımdır, yani azap çığlığı, source:"ط غ ي,B004"}. Azgın için varılacak yer de söylenir: {ar:فَأَمَّا مَن طَغَىٰ, tr:fe emmâ men tagâ, gloss:azana gelince, source:79:37}, {ar:فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ, tr:fe inne'l-cahîme hiye'l-me'vâ, gloss:barınağı cehennemdir, source:79:39}. On ikinci ayetin {ar:بِٱلتَّقْوَىٰٓ, tr:bi't-takvâ, gloss:sakınmayı, source:96:12} kelimesi ise bu ateşe karşı bir kalkandır: {ar:التقوى جعل النفس في وقاية مما يخاف, tr:et-takvâ caʿlu'n-nefsi fî vikâye, gloss:takva, nefsi korkulan şeyden bir korunak içine almaktır, source:"و ق ي,B002"}. Kurân bu kökü ateşle birlikte kullanır: {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًا, tr:kû enfusekum ve ehlîkum nârâ, gloss:kendinizi ve ailenizi ateşten koruyun, source:66:6}.

Bu sahne, surenin kul ile yasaklayan arasında kurduğu karşıtlığı tek bir kökte toplar. Kul namazla ateşten korunur; yasaklayan, yasakladığı fiilin öteki anlamıyla karşılaşır.

Kaynaklar: 96:10 صَلَّىٰٓ ص ل و B003; 96:10 صَلَّىٰٓ ص ل و B001; 96:15 لَنَسْفَعًۢا س ف ع B003; 96:6 لَيَطْغَىٰٓ ط غ ي B004; 96:12 بِٱلتَّقْوَىٰٓ و ق ي B002

## Tuzak ve av

Avcılar açık araziye çıkar, tuzak kurar; av ağa takılır. Yaban hayvanı bir süre koşar, sonra durup arkasına bakar. Bu sahnenin üyeleri surenin birçok kelimesine dağılmıştır. Onuncu ayetin namaz fiilinin ailesinde tuzak kurmak vardır: {ar:المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد, tr:el-maslât en tensibe şereken, gloss:maslât, bir şey düşsün de avlansın diye tuzak kurmaktır, source:"ص ل و,B004"}. Bu anlam mecaz olarak birinin yıkımına çalışmak için de kullanılır: {ar:صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة, tr:salaytu li fulân, gloss:falana tuzak kurdum, yani onu helake düşürmek için uğraştım, source:"ص ل و,B004"}. İkinci ayetin alak kökünde ağa takılan ceylan vardır: {ar:علق الظبي في الحبالة يعلق إذا نشق فيها, tr:ʿalika'z-zabyu fi'l-hibâle, gloss:ceylan ağa takıldı, source:"ع ل ق,B011"}. Birinci ayetin ad kelimesinin kökünde avcılar vardır: {ar:خرج القوم للصيد في قفار الأرض وصحاريها قلت سموا وهم السماة أي الصيادون, tr:semev, ve humu's-sumât, gloss:topluluk ıssız yerlere ava çıktığında "semev" denir; onlar sumâttır, yani avcılar, source:"س م و,B006"}. On beşinci ayetin fiilinin ailesinde kovalamaca ve yırtıcı kuşun vuruşu bulunur: {ar:المسافعة كالمطاردة, tr:el-musâfaʿa ke'l-mutârade, gloss:müsâfaa kovalamaca gibidir, source:"س ف ع,B005"}; {ar:سفع الطائر ضريبته أي لطمه, tr:sefaʿa't-tâ'iru darîbeteh, gloss:kuş avına vurdu, source:"س ف ع,B004"}. On üçüncü ayetin yalanlama fiilinin ailesinde de kaçan hayvan vardır: {ar:كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه, tr:kezebe'l-vahşiyy, gloss:yaban hayvanı bir koşu koşup sonra arkasına bakmak için durdu, source:"ك ذ ب,B007"}.

Sahnenin işleyişi tersine döner. Kulun namazına engel olmak isteyen adam bir avcı gibi davranır. Ama yakalanan odur: perçeminden tutulur, tıpkı ağa takılan av gibi. Kurân Peygamber'e karşı kurulan tuzağı ve tuzağın sahibine dönüşünü anlatır: {ar:وَإِذْ يَمْكُرُ بِكَ ٱلَّذِينَ كَفَرُوا۟ لِيُثْبِتُوكَ أَوْ يَقْتُلُوكَ أَوْ يُخْرِجُوكَ, tr:ve iz yemkuru bike'llezîne keferû li yusbitûke ev yaktulûke ev yuhricûk, gloss:inkâr edenler seni tutup bağlamak, öldürmek ya da çıkarmak için tuzak kuruyorlardı, source:8:30}, {ar:وَيَمْكُرُونَ وَيَمْكُرُ ٱللَّهُ, tr:ve yemkurûne ve yemkuru'llâh, gloss:onlar tuzak kuruyordu, Allah da tuzak kuruyordu, source:8:30}. Bu sahne, avcının av olduğu bir çevrilmeyi yasaklayanın sonuna bağlar.

Kaynaklar: 96:10 صَلَّىٰٓ ص ل و B004; 96:2 عَلَقٍ ع ل ق B011; 96:1 بِٱسْمِ س م و B006; 96:15 لَنَسْفَعًۢا س ف ع B005; 96:15 لَنَسْفَعًۢا س ف ع B004; 96:13 كَذَّبَ ك ذ ب B007; 96:15 ٱلنَّاصِيَةِ ن ص ي B001

## Yol: doğru yolda olmak, sapmak, dönmek, yaklaşmak

Bir yolcu yoldadır. Hedefi ıskalayabilir, yönünden sapabilir ya da sırtını dönüp kaçabilir. Sonunda herkes başladığı yere döner ve yolun bir varış noktası vardır. On birinci ayetin {ar:عَلَى ٱلْهُدَىٰٓ, tr:ʿale'l-hudâ, gloss:doğru yol üzerinde, source:96:11} ifadesi yolcuyu yolun üzerinde gösterir: {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytuhu't-tarîk, gloss:ona yolu ve evi gösterdim, yani tanıttım, source:"ه د ي,B001"}; {ar:الهداية دلالة بلطف, tr:el-hidâye delâletun bi lutf, gloss:hidayet, incelikle yol göstermektir, source:"ه د ي,B001"}. Kök sakin bir yürüyüşü de adlandırır: {ar:لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن, tr:lem yusriʿ isrâʿa'l-munhezim, gloss:bozguna uğrayan gibi koşmadı, sükûnet ve güzel bir yürüyüşle gitti, source:"ه د ي,B010"}. Kurân yolcuları karşılaştırır: {ar:أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ, tr:e fe men yemşî mukibben ʿalâ vechihî ehdâ em men yemşî seviyyen ʿalâ sırâtın mustakîm, gloss:yüzüstü kapanarak yürüyen mi daha doğru yoldadır, yoksa dosdoğru bir yolda dimdik yürüyen mi, source:67:22}. Bu ayette yüz, yolun karşısında bir yürüyüş biçimi olarak geçer; bu da perçem sahnesine yakındır.

On altıncı ayetin günahkâr kelimesi yönden sapmaktır: {ar:الخطأ العدول عن الجهة, tr:el-hata'u'l-ʿudûlu ʿani'l-cihe, gloss:hata yönden sapmaktır, source:"خ ط ء,B001"}. On üçüncü ayetin yüz çevirme fiili, bedenle ya da dinlememekle sırt dönmektir: {ar:التولي قد يكون بالجسم وقد يكون بترك الإصغاء والائتمار, tr:et-tevellî kad yekûnu bi'l-cism, gloss:yüz çevirmek bedenle de olur, dinlememek ve emre uymamakla da, source:"و ل ي,B007"}. Aynı kök kesintisiz yakınlığı da adlandırır: {ar:الولي القرب والدنو, tr:el-velyu'l-kurbu ve'd-dunuvv, gloss:vely yakınlık ve yaklaşmaktır, source:"و ل ي,B001"}. Böylece yüz çevirmek, yakınlığın tersine çevrilmiş halidir. Yalanlama fiilinin ailesinde saldırıda duraksamak da vardır: {ar:حمل فلان ثم كذب أي لم يصدق في الحملة, tr:hamele fulânun summe kezeb, gloss:falan saldırdı, sonra geri durdu, yani saldırısında sözünü tutmadı, source:"ك ذ ب,B004"}.

Sekizinci ayetin dönüşü başlangıca dönüştür: {ar:الرجوع العود إلى ما كان منه البدء, tr:er-rucûʿu'l-ʿavdu ilâ mâ kâne minhu'l-bed', gloss:dönüş, başlangıcın olduğu yere geri gelmektir, source:"ر ج ع,B001"}. Bu başlangıç, ilk iki ayetin yaratmasıdır. Kurân dönüşü yaratılışın başlangıcına bağlar: {ar:إِلَيْهِ مَرْجِعُكُمْ جَمِيعًا, tr:ileyhi merciʿukum cemîʿâ, gloss:hepinizin dönüşü O'nadır, source:10:4}, {ar:إِنَّهُۥ يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ, tr:innehû yebde'u'l-halka summe yuʿîduh, gloss:O yaratmayı başlatır, sonra onu geri getirir, source:10:4}; {ar:كَمَا بَدَأَكُمْ تَعُودُونَ, tr:kemâ bede'ekum teʿûdûn, gloss:sizi başlattığı gibi döneceksiniz, source:7:29}. İnsanın yolu da Rab'be doğru bir uğraş olarak tanımlanır: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًا فَمُلَٰقِيهِ, tr:yâ eyyuhe'l-insânu inneke kâdihun ilâ rabbike kedhan fe mulâkîh, gloss:ey insan, sen Rabbine doğru zahmetle çabalıyorsun ve O'na kavuşacaksın, source:84:6}. Dönmeyeceğini sanan kişi de anlatılır: {ar:إِنَّهُۥ ظَنَّ أَن لَّن يَحُورَ, tr:innehû zanne en len yahûr, gloss:o asla geri dönmeyeceğini sanmıştı, source:84:14}. Yedinci ayetin yeterlilik kökü bu sanıyı yere yerleşmekle de anlatır: {ar:غني القوم في دارهم أقاموا, tr:ganiye'l-kavmu fî dârihim, gloss:topluluk yurdunda yerleşip kaldı, source:"غ ن ي,B004"}. Dönüş kelimesinin ailesinde günahtan dönmek de vardır: {ar:يرجعون عن الذنب, tr:yarciʿûne ʿani'z-zenb, gloss:günahtan dönerler, source:"ر ج ع,B003"}. Bu, on beşinci ayetteki "vazgeçmezse" şartının açık bıraktığı yoldur.

Yolun bir son noktası vardır: {ar:النهاية الغاية حيث ينتهي إليه الشيء, tr:en-nihâyetu'l-gâye, gloss:nihâye, bir şeyin vardığı son noktadır, source:"ن ه ي,B002"}. Son ayetin emri ise yaklaşmaktır: {ar:القرب نقيض البعد والتقرب التدني إلى شيء والاقتراب الدنو, tr:el-kurbu nakîdu'l-buʿd, gloss:yakınlık uzaklığın zıddıdır; yaklaşmak bir şeye doğru alçalıp gelmektir, source:"ق ر ب,B001"}. On ikinci ayetin sakınma kökü yolda dikkatle yürüyen atı da adlandırır: {ar:فرس واق إذا كان يهاب المشي من وجع يجده في حافره, tr:ferasun vâk, gloss:toynağındaki ağrıdan ötürü yürümekten çekinen at, source:"و ق ي,B003"}. Sure böylece yolda olmayı, sapmayı, sırt dönmeyi ve sonunda yaklaşmayı tek bir yol üzerinde sıralar.

Kaynaklar: 96:11 ٱلْهُدَىٰٓ ه د ي B001; 96:11 ٱلْهُدَىٰٓ ه د ي B010; 96:16 خَاطِئَةٍ خ ط ء B001; 96:13 وَتَوَلَّىٰٓ و ل ي B007; 96:13 وَتَوَلَّىٰٓ و ل ي B001; 96:13 كَذَّبَ ك ذ ب B004; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B001; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B003; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B004; 96:15 يَنتَهِ ن ه ي B002; 96:19 وَٱقْتَرِب ق ر ب B001; 96:12 بِٱلتَّقْوَىٰٓ و ق ي B003

## Buluşmalar

İmgeler en açık şekilde baş sahnesinde buluşur. On beşinci ayetin fiili hem perçemden tutmak hem de yüzü karartmaktır. Böylece başın önü, avın yakalandığı yer, huysuz hayvanın tutulduğu yer ve ateşin yaladığı deri aynı noktada birleşir. Aynı alın son ayette yere konur ve secde izini taşır. İşaret imgesi buraya da uzanır: bir alın kararmış bir lekeyle işaretlenir, öteki secdenin iziyle. Kurân her iki tarafı da yüzlerindeki işaretle tanıtır: biri {ar:مِّنْ أَثَرِ ٱلسُّجُودِ, tr:min eseri's-sucûd, gloss:secdenin izinden, source:48:29}, öteki {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. Sure ad ile başlar ve iki işaretli alınla biter.

Göz ile yeterlilik imgeleri yedinci ayette buluşur. Kendini aynada gören adam ile süse ihtiyaç duymayan güzel kadın aynı kelime çiftinde birleşir: kendini görmek ve yeterli saymak. Su imgesi de buna bağlanır. Azan insan ölçüsünü aşan bir taşkın gibidir; on beşinci ayette durması istenir. Kökün göletteki duruluşu adlandırdığı hatırlanırsa, sekizinci ayet bu suyun nereye varacağını söyler. Kurân'ın varış ayeti bu iki imgeyi aynı yapıda birleştirir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Yol imgesi de bu dönüşe katılır, çünkü dönüş başlangıca dönmektir ve bu başlangıç rahimdeki ilk tutunuştur.

Rahim ile okuma, surenin ilk kelimesinde buluşur. Okumanın kökü hem rahmin bir şeyi toplayıp tutmasını hem de harflerin toplanmasını adlandırır. Pıhtıyı tutan kökle sözü toplayan kök aynıdır. İnsanın yaratılışı ve öğretilmesi bu yüzden aynı işin iki yüzü olarak duyulur. Kurân'daki benzer sıra da bunu destekler: Kurân'ı öğretmek, insanı yaratmak ve ona açıklamayı öğretmek. Okuma ile secde de buluşur: okuyucu aynı zamanda kulluk edendir ve sure, ilk emri okumak, son emri secde etmek olan bir eğri çizer. Kurân bu ikisini, okunduğunda secde edenler ile etmeyenler üzerinden birleştirir.

Ateş ile çağrı imgeleri onuncu, on yedinci ve on sekizinci ayetlerde buluşur. Namaz hem çağrıdır hem de kökü ateşe girmeyi adlandırır. Adam meclisini çağırır, Allah ateşe iten bekçileri çağırır ve kul yakın meclise çağrılır. Ateşin kendisinin de çağırdığı söylenir: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Bu yüz çevirme on üçüncü ayetin fiilidir.

İtaat ile hayvan imgeleri son ayette buluşur. Rab, itaat edilen efendidir; dizgine uyan at da itaatin bir figürüdür. Kul bu yüzden kendini rab ilan eden birine boyun eğmez, yakında tutulan ve değer gören at gibi yaklaşır. Yaratma ile uydurma da on altıncı ayette buluşur. Gerçek ölçüyle yaratan Rab'bin karşısında, yalanı içinde ölçen yalancı perçem durur.

Bu buluşmalar surenin hareketini taşır. Sure, rahimde toplanan ve tutunan bir varlıkla başlar; bu varlık sözü toplamayı ve kalemle yazmayı öğrenir. Sonra kendini aynada yeterli görür, taşkın su gibi ölçüsünü aşar, başını kaldırır ve namaz kılan kulu engellemeye çalışır. Dönüş ayeti ve Allah'ın görmesi bu yükselişin önüne bir sınır koyar. Yasaklayan perçeminden yakalanır, meclisi yerine bekçiler gelir. Kul ise yüz çevirmeden, başını yere koyarak, çağrılmış olduğu yakınlığa yürür.

