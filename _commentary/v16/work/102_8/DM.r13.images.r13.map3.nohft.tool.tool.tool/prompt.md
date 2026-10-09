Focus: 102:8. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/102_8/D.r13/context.md =====
# 102:8 — focus

ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ

Anchor translation (canonical reading, reference only):

Sonra o gün nimetler hakkında mutlaka sorgulanacaksınız.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ثُمَّ | ثُمّ |  | CONJ |
| 2 | لَتُسْـَٔلُنَّ | سَأَلَ | س ء ل | EMPH;V |
| 3 | يَوْمَئِذٍ | يَوْمَئِذ |  | T |
| 4 | عَنِ | عَن |  | P |
| 5 | ٱلنَّعِيمِ | نَعِيم | ن ع م | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 102 — full text (context; no pericope)

- 102:1 أَلْهَىٰكُمُ ٱلتَّكَاثُرُ
- 102:2 حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ
- 102:3 كَلَّا سَوْفَ تَعْلَمُونَ
- 102:4 ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ
- 102:5 كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ
- 102:6 لَتَرَوُنَّ ٱلْجَحِيمَ
- 102:7 ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ
- 102:8 ◀ focus ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ


===== _commentary/v16/work/102_8/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## س ء ل (root_000661) — identity root of لَتُسْـَٔلُنَّ (w2)

- **B001** bilgi sormak veya bir şey istemek — sormak; istemek · sorma; soru; istekte bulunma · soru veya istek konusu · çok soru soran kimse · sor; iste · sorular veya istek konuları · soran ya da isteyen kimse; yardım isteyen yoksul · ondan bir şeyi istemek · ona bir şey hakkında soru sormak · bir kişi hakkında soru sormak · ilk ses düşürülerek söylenen sormak biçimi
  سأل يسأل سؤالا ومسألة (maqayis;ayn)؛ سألته الشيء وسألته عن الشيء سؤالا ومسألة (sihah)؛ خرجنا نسأل عن فلان وبفلان (sihah)؛ رجل سؤلة كثير السؤال (maqayis;sihah)؛ الفقير يسمى سائلا (ayn)
- **B002** istenen şey — bir kimsenin istediği şey
  السؤل ما يسأله الإنسان (sihah)؛ السؤل يقارب الأمنية والسؤل فيما طلب (mufradat)
- **B003** birinin isteğini yerine getirmek — birinin isteğini veya gereksinimini karşılamak
  أسألته سؤلته ومسألته أي قضيت حاجته (sihah)
- **B004** birbirine soru sormak — birbirlerine soru sormak
  تساءلوا أي سأل بعضهم بعضا (sihah)

## ن ع م (root_001525) — identity root of ٱلنَّعِيمِ (w5)

- **B001** iyi yaşam durumu ve başkasına ulaştırılan iyilik — bağış, iyilik veya elverişli yaşam durumu · iyi durum ve esenlik · bolluk ve rahatlık · bol ve rahat yaşam · iyiliği başkasına ulaştırma
  أصل واحد يدل على ترفه وطيب عيش وصلاح (maqayis)؛ نعم ينعم نعمة فهو نعم ناعم (ayn;tahdhib)؛ النعمة اليد والصنيعة والمنة وما أنعم به عليك (sihah)؛ نعمة الله منه وعطاؤه (tahdhib)؛ النعمة الحالة الحسنة والإنعام إيصال الإحسان إلى الغير (mufradat)
- **B002** yumuşamak, rahat yaşamak veya rahat yaşatmak — yumuşamak · yumuşak; rahat yaşayan · rahat ve bolluk içinde yaşayan kadın · çocuklarını bolluk içinde yaşattı · rahat ve bolluk içindeki yaşam
  نعم الشيء صار ناعما لينا (sihah)؛ نعمة العيش حسنه وغضارته (tahdhib)؛ نعم فلان أولاده ترفهم (maqayis)؛ طعام ناعم وجارية ناعمة (mufradat)؛ فهو نعم ناعم بين المنعم (ayn)
- **B003** övgü ve beğeni bildirmek — ne güzel; övgü bildirir · bu ne güzel · öyleyse ne güzel, yerinde olur
  نعم ضد بئس (maqayis)؛ نعم وبئس فعلان ماضيان ... فنعم مدح وبئس ذم (sihah)؛ نعما ... المعنى نعم الشيء هي (tahdhib)؛ نعم كلمة تستعمل في المدح بإزاء بئس (mufradat)
- **B004** evet diyerek onaylamak veya söz vermek — evet; doğru; olur · ona evet dedi
  نعم جواب الواجب ضد لا (maqayis)؛ نعم عدة وتصديق وجواب الاستفهام (sihah)؛ نعم يكون تصديقا ويكون عدة (tahdhib)؛ نعم كلمة للإيجاب (mufradat)
- **B005** develer ve geniş anlamda otlayan evcil hayvanlar — develer; deve varlığı · deve, sığır ve koyun topluluğu
  النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم (maqayis)؛ النعم واحد الأنعام وهي المال الراعية وأكثر ما يقع هذا الاسم على الإبل (sihah)؛ النعم لم يريدوا بها إلا الإبل فإذا قالوا الأنعام أرادوا بها الإبل والبقر والغنم (tahdhib)؛ النعم مختص بالإبل وجمعه أنعام (mufradat)
- **B006** devekuşu — devekuşu; erkek veya dişi birey · devekuşu türü veya topluluğu
  النعامة معروفة لنعمة ريشها (maqayis)؛ النعامة من الطير يذكر ويؤنث والنعام اسم جنس (sihah)؛ النعام الظليم والنعامة الأنثى (tahdhib)؛ النعامة سميت تشبيها بالنعم في الخلقة (mufradat)
- **B007** devekuşuna benzetilerek ad verilen şeyler — devekuşuna benzetilen kuyu kirişi, gölgelik, beden bölümü veya yol · Ay'ın konak yerlerinden biri
  على معنى التشبيه النعامة وهي كالظلة تجعل على رءوس الجبل (maqayis)؛ النعامة الخشبة المعترضة على الزرنوقين والنعائم منزل من منازل القمر (sihah)؛ النعامة الخشبة المعترضة على الزرنوقين وابن النعامة عرق الرجل ومحجة الطريق (tahdhib)؛ النعامة المظلة في الجبل وعلى رأس البئر تشبيها بالنعامة في الهيئة والنعائم من منازل القمر (mufradat)
- **B008** bir topluluğun dağılıp gücünü yitirmesi [kalıp] — dağıldılar, ayrıldılar veya güçlerini yitirdiler · hızla yola koyulup gittiler · yenilip dağıldılar
  شالت نعامتهم إذا تفرقوا (maqayis)؛ للقوم إذا ارتحلوا أو تفرقوا قد شالت نعامتهم (sihah)؛ خفت نعامتهم أي استمر بهم السير وشالت نعامتهم إذا تفرقت كلمتهم أو ذهب عزهم (tahdhib)
- **B009** yumuşak esen nemli güney rüzgarı — yumuşak esen nemli güney rüzgarı
  النعامي الريح اللينة (maqayis)؛ النعامى ريح الجنوب لأنها أبل الرياح وأرطبها (sihah)؛ من أسماء الجنوب النعامى (tahdhib)؛ النعامى الريح الجنوب الناعمة الهبوب (mufradat)
- **B010** daha da artırmak veya ileri dereceye götürmek — artırdı; daha ileri götürdü · onu iyice ince öğüttü
  فعل كذا وأنعم أي زاد (sihah;mufradat)؛ أنعم أفضل وزاد وأنعما أي زادا على ذلك ودققت دواء فأنعمت دقه أي بالغت وزدت (tahdhib)
- **B011** bir yeri kendine uygun bulup orada kalmak [kalıp] — bir yere geldi, orayı uygun bulup kaldı
  أتيت أرض بني فلان فتنعمتني إذا وافقته (maqayis)؛ أتيت أرض فلان فتنعمتني إذا وافقته (sihah)؛ أتيت أرضا فنعمتني أي وافقتني وأقمت بها (tahdhib)
- **B012** birine yaya gitmek ve ayakları yürüyerek kullanmak [kalıp] — ona yaya gitti veya onu yürüyerek aradı · ayaklarını yürümekle eskitti; hafif yürüdü
  تنعمت زيدا طلبته كأنه أراد أعمل إليه نعامته وهي باطن قدمه (maqayis)؛ تنعمت فلانا أتيته على غير دابة وتنعم فلان قدميه أي ابتذلهما (tahdhib)؛ تنعم فلان إذا مشى مشيا خفيفا فمن النعمة (mufradat)
- **B013** birini göz sevinci saymak veya bunun için dua etmek [kalıp] — Tanrı seni gözlere sevinç kaynağı kılsın · göz sevinci ve hoşnutluğu
  نعم ونعمى عين ونعمة عين أي قرة عين (maqayis)؛ نعمة العين قرتها ونعم عين ونعام عين ونعامة عين ونعمة عين ونعمى عين كله بمعنى (sihah)؛ نعمك الله عينا ونعم الله بك عينا ونعمى عين ونعام عين (tahdhib)؛ نعم الله بك عينا ونعم ونعمة عين ونعمى عين ونَعام عين (mufradat)

## ECHO س ل ل (root_000736) — for لَتُسْـَٔلُنَّ (w2): withheld observed target; not identity

- **B001** nazikçe ve fark ettirmeden çekip çıkarma — bir şeyi çekip çıkarmak · kılıcı kınından çekmek · hamurdaki kılı ayıklayıp çıkarmak
  سللت الشيء أسله سلا (maqayis;sihah;tahdhib)؛ إخراجك الشعر من العجين (ayn;tahdhib)؛ سل الشيء من الشيء نزعه (mufradat)
- **B002** gizlice çalma — hırsızlık; gizli hırsızlık · gizli hırsızlık; ayrıca rüşvet · çalmak · hırsız
  السلة والإسلال السرقة (maqayis)؛ الإسلال السرقة الخفية (ayn;tahdhib)؛ الإسلال الرشوة والسرقة (sihah)؛ سل الشيء من البيت على سبيل السرقة (mufradat)
- **B003** kökenden çıkan yavru veya öz — oğul; çocuk · kız evlat · tay ve dişi tay · kökten ayrılan öz; üreme maddesi
  السليل الولد (maqayis;sihah;tahdhib)؛ السلالة ما استل منه والنطفة سلالة الإنسان (sihah;tahdhib;mufradat)؛ السليل والسليلة المهر والمهرة (ayn;tahdhib)
- **B004** aradan sıyrılıp çıkma — dar yerden veya kalabalıktan sıyrılıp çıkma · aralarından çıkmak · topluluktan gizlice ayrılma
  الانسلال المضي والخروج من بين مضيق أو زحام (ayn;tahdhib)؛ انسل من بينهم أي خرج (sihah)؛ يتسللون منكم لواذا (tahdhib;mufradat)
- **B005** birbirine bağlı dizi — zincir; parçaların birbirine bağlanması · birbirine bağlı · bulut boyunca uzanan şimşek · birbirine eklenen kıvrımlı kum
  السلسلة اتصال الشيء بالشيء (maqayis)؛ شيء مسلسل متصل بعضه ببعض (sihah)؛ السلسلة معروفة وبرق ذو سلاسل ورمل ذو سلاسل (tahdhib)؛ ومنه السلسلة (mufradat)
- **B006** tatlı, duru ve kolay akan su — suyun boğazdan veya eğimden kolayca akması · tatlı, duru ve kolay içilen su · boğazdan kolay geçen duru şarap · kolay içilen, lezzetli ve hızlı akan kaynak suyu
  تسلسل الماء في الحلق إذا جرى وماء سلسل وسلسال (maqayis;sihah;tahdhib)؛ السلسل الماء العذب الصافي (ayn;tahdhib)؛ ماء سلسل متردد في مقره حتى صفا (mufradat)
- **B007** vadi içindeki su yolu veya çukur arazi — vadide dar su yolu; su toplayan alçak yer · vadi içindeki dar su yolları veya ağaçlı çukur yerler · geniş ve ağaçlı vadi
  السال مسيل في مضيق الوادي (maqayis;sihah;tahdhib)؛ السليل الوادي الواسع ينبت السلم والسمر (sihah;tahdhib)؛ السلان بطون من الأرض غامضة ذات شجر (tahdhib)
- **B008** tüberküloz — tüberküloz · tüberküloz · tüberküloz hastası
  السلال من المرض كأن لحمه قد سل (maqayis)؛ السل والسلال داء يأخذ الإنسان ويقتل (ayn)؛ السلال بالضم السل (sihah)؛ داء يهزل ويضني ويقتل (tahdhib)؛ مرض ينزع به اللحم والقوة (mufradat)
- **B009** atın yarıştaki güçlü ileri atılımı [kalıp] — atın yarışta ileri atılıp öne çıkması
  فرس شديد السلة وهي دفعته في سباقه (maqayis;sihah;tahdhib)؛ خرجت سلة هذا الفرس على سائر الخيل (ayn;tahdhib)
- **B010** çuvaldız — çuvaldız; iri dikiş iğnesi
  المسلة معروفة لأنها تسل الخيط سلا (maqayis)؛ المسلة المخيط وجمعه مسال (ayn)؛ المسلة واحدة المسال وهي الإبر العظام (sihah)
- **B011** sepet veya kapaklı kap — ekmek sepeti · kapaklı sepet veya kap
  سلة الخبز معروفة (sihah)؛ السلة السبذة المطبقة كالجؤنة (ayn;tahdhib)؛ سبذة الطين السلة (tahdhib)
- **B012** ince uzun şerit, lif veya uç — saçtan veya dokudan ince uzun şerit · hörgüçteki uzun şeritler veya burun içi doku parçaları · dilin ince ucu · uzun ve sivri diken · hurma dalından sıyrılmış ince parça
  السليلة عقبة أو عصبة أو لحمة شبه طرائق (ayn;tahdhib)؛ سليلة من شعر لما استل من ضريبته (sihah)؛ سلائل السنام طرائق طوال (tahdhib)؛ أسلة اللسان الطرف الرقيق (mufradat)؛ السلاءة من الشوك لأن فيها امتدادا (maqayis)
- **B013** biçime bağlı adlandırmalar — kumaşın giyilmekten incelmesi · kılıç yüzeyinin dalgalı parıltısı · çizgili süslü kumaş · eti azalıp bedeni oluklaşmış kişi
  تسلسل الثوب وتخلخل إذا لبس حتى رق؛ التسلسل بريق فرند السيف ودبيبه؛ ثوب ملسلس فيه وشي مخطط؛ المتسلسل الذي تخدد لحمه وقل
- **B014** dişleri düşmüş olma — dişleri düşmüş erkek, kadın veya koyun · yaşlılıktan dişleri düşmüş dişi deve
  السلة الناقة التي سقطت أسنانها؛ رجل سل وامرأة سلة وشاة سلة أي ساقطة الأسنان
- **B015** su teknesi destekleri arasındaki boşluk — su teknesinin dikili parçaları arasındaki boşluk
  السلة الفرجة بين نصائب الحوض

===== _commentary/v16/out/s102/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 102:8, and ## Buluşmalar) =====
## Sayılan şeyler: eş, çocuk, sürü, altın

Yarışın nesneleri de kelimelerin ailesinde adlandırılır. Oyalanma kelimesi kadın ve çocuk için dolaylı bir ad olarak kullanılır: {ar:وقد يكنى باللهو عن غيره، المرأة، الولد, tr:ve kad yükennâ bi'l-lehvi an gayrih el-mer'etü el-veled, gloss:lehv ile bazen başka şeyler kastedilir: kadın ve çocuk, source:"ل ه و,B002"}; {ar:يعبر عن كل ما به استمتاع باللهو، المرأة والولد, tr:yu'abbaru an külli mâ bihî istimtâun bi'l-lehv el-mer'etü ve'l-veled, gloss:kendisiyle zevk alınan her şey lehv diye anılır; kadın ve çocuk gibi, source:"ل ه و,B002"}; ve genel olarak {ar:اللهو ما شغلك من هوى أو طرب, tr:el-lehvü mâ şegaleke min heven ev tarab, gloss:lehv seni meşgul eden heves ya da coşkudur, source:"ل ه و,B002"}. Çokluk yarışı da iki şeyde yapılır, insan sayısında ve malda: {ar:التفاخر بكثرة العدد والمال, tr:et-tefâhurü bi-kesreti'l-adedi ve'l-mâl, gloss:sayı ve mal çokluğuyla övünmek, source:"ك ث ر,B002"}; malı çok olan adam da bu kökten adlandırılır: {ar:رجل مكثر كثير المال, tr:racülün müksirun kesîru'l-mâl, gloss:müksir adam; malı çok olan, source:"ك ث ر,B003"}.

Surenin son kelimesi bu nesnelerin bir kısmını kendi ailesinde taşır. {ar:ٱلنَّعِيمِ, tr:en-naîm, gloss:nimet; bolluk ve rahatlık, source:102:8} kelimesinin kökü develeri, içlerindeki iyilik ve nimet yüzünden adlandırır: {ar:النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم, tr:en-neamü'l-ibilü limâ fîhi mine'l-hayri ve'n-ni'meti ve'l-en'âmü'l-behâim, gloss:neam develerdir; içlerindeki hayır ve nimet yüzünden; en'âm ise hayvanlardır, source:"ن ع م,B005"}. Aynı kök çocukları bollukta büyütmeyi de adlandırır: {ar:نعم فلان أولاده ترفهم, tr:na''ame fülânun evlâdehû terrafehüm, gloss:filan çocuklarını bolluk içinde büyüttü, source:"ن ع م,B002"}. Yedinci ayetin {ar:عَيْنَ, tr:ayn, gloss:göz, source:102:7} kelimesi de hazır malı ve altını adlandırır: {ar:العين وهو المال العتيد الحاضر, tr:el-aynü ve hüve'l-mâlü'l-atîdü'l-hâdır, gloss:ayn hazır bulunan nakit maldır, source:"ع ي ن,B011"}; {ar:قيل للذهب: عين, tr:kîle li'z-zehebi ayn, gloss:altına ayn denmiştir, source:"ع ي ن,B011"}. Ayetlerde bu kelimeler "göz" ve "nimet" anlamındadır; ama ailelerinin bu dalları, birinci ayette sayılan sürülerin ve paranın surenin son kelimelerinin altında durduğunu duyurur: sayılan develer, hakkında sorulacak nimetin adını taşır.

Kur'an bu nesneleri tek bir listede toplar. Allah insanlara süslü gösterilen şeyleri sayar: {ar:زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ مِنَ ٱلنِّسَآءِ وَٱلْبَنِينَ وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ مِنَ ٱلذَّهَبِ وَٱلْفِضَّةِ وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ, tr:züyyine li'n-nâsi hubbü'ş-şehevâti mine'n-nisâi ve'l-benîne ve'l-kanâtîri'l-mukantarati mine'z-zehebi ve'l-fiddati ve'l-hayli'l-müsevvemeti ve'l-en'âmi ve'l-hars, gloss:kadınlara; oğullara; yığın yığın altına ve gümüşe; salma atlara; hayvanlara ve ekinlere duyulan arzuların sevgisi insanlara süslü gösterildi, source:3:14}. Kadınlar, oğullar, yığılmış altın ve sürüler: oyalanma ve çokluk kelimelerinin ailesinin adlandırdığı nesnelerin hepsi bu ayettedir, ve hayvanlar için kullanılan kelime nimet kelimesiyle aynı köktendir. Başka bir ayet surenin iki ilk kelimesini dünya hayatının tanımında birleştirir: {ar:ٱعْلَمُوٓا۟ أَنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌۭ وَلَهْوٌۭ وَزِينَةٌۭ وَتَفَاخُرٌۢ بَيْنَكُمْ وَتَكَاثُرٌۭ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ, tr:i'lemû ennema'l-hayâtü'd-dünyâ leibun ve lehvun ve zînetun ve tefâhurun beyneküm ve tekâsürun fi'l-emvâli ve'l-evlâd, gloss:bilin ki dünya hayatı bir oyun; bir oyalanma; bir süs; aranızda bir övünme ve mallarda ve evlatlarda bir çoğalma yarışıdır, source:57:20}. Aynı ayet bu hayatı, bitkisi inkârcıların hoşuna giden ama sonra sararıp kırıntı olan bir yağmura benzetir {source:57:20}. Burada tekâsürün nesnesi açıkça söylenir: mallar ve evlatlar. Müminlere yapılan uyarı da aynı ikiliyi alıkoyan şeyler olarak adlandırır {source:63:9}, ve başka bir ayette mal ve oğullar dünya hayatının süsü diye anılır: {ar:ٱلْمَالُ وَٱلْبَنُونَ زِينَةُ ٱلْحَيَوٰةِ ٱلدُّنْيَا, tr:el-mâlü ve'l-benûne zînetü'l-hayâti'd-dünyâ, gloss:mal ve oğullar dünya hayatının süsüdür, source:18:46}.

Hud'un kavmine hatırlatması bu nesneleri hem nimetin hem gözün kökleriyle, hem de bilgi fiiliyle anar: {ar:وَٱتَّقُوا۟ ٱلَّذِىٓ أَمَدَّكُم بِمَا تَعْلَمُونَ, tr:ve'ttekû'llezî emeddeküm bimâ ta'lemûn, gloss:size bildiğiniz şeylerle yardım edenden sakının, source:26:132}; {ar:أَمَدَّكُم بِأَنْعَٰمٍۢ وَبَنِينَ, tr:emeddeküm bi-en'âmin ve benîn, gloss:size hayvanlar ve oğullarla yardım etti, source:26:133}; {ar:وَجَنَّٰتٍۢ وَعُيُونٍ, tr:ve cennâtin ve uyûn, gloss:bahçeler ve pınarlarla, source:26:134}. Hayvanlar nimet kelimesinin kökünden, pınarlar göz kelimesinin kökündendir, ve hepsi "bildiğiniz şeyler" diye anılır. Allah başka bir yerde mal ve oğullarla desteklenmenin bir iyilik yarışı sanılmasını sorgular: {ar:أَيَحْسَبُونَ أَنَّمَا نُمِدُّهُم بِهِۦ مِن مَّالٍۢ وَبَنِينَ, tr:e-yahsebûne ennemâ nümiddühüm bihî min mâlin ve benîn, gloss:onlara mal ve oğullardan verdiğimiz şeyi sanıyorlar mı, source:23:55} {ar:نُسَارِعُ لَهُمْ فِى ٱلْخَيْرَٰتِ ۚ بَل لَّا يَشْعُرُونَ, tr:nüsâriu lehüm fi'l-hayrât bel lâ yeş'urûn, gloss:onlara iyiliklerde koşturduğumuz; hayır; farkında değiller, source:23:56}. Sayılan şeyler bilginin yerini tutar ve söz "farkında değiller" ile kapanır. İbrahim'in duasında anılan günde ise bu nesneler işe yaramaz: {ar:يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ, tr:yevme lâ yenfeu mâlun ve lâ benûn, gloss:ne malın ne oğulların yarar sağladığı gün, source:26:88}.

Bu imge "çokluk" soyut kelimesinin altına somut nesneleri koyar: eşler, çocuklar, sürüler ve altın. Ve bu nesnelerin adları surenin sonunda, görmenin ve sorgunun kelimelerinde yeniden duyulur.

Kaynaklar: 102:1 أَلْهَىٰكُمُ ل ه و B002; 102:1 ٱلتَّكَاثُرُ ك ث ر B002; 102:1 ٱلتَّكَاثُرُ ك ث ر B003; 102:8 ٱلنَّعِيمِ ن ع م B005; 102:8 ٱلنَّعِيمِ ن ع م B002; 102:7 عَيْنَ ع ي ن B011

## Görülmek için sergilenen, sonra görmeye zorlanan

Çokluk yarışı bir övünmedir, {ar:التفاخر بكثرة العدد والمال, tr:et-tefâhurü bi-kesreti'l-adedi ve'l-mâl, gloss:sayı ve mal çokluğuyla övünmek, source:"ك ث ر,B002"}, ve övünme seyirci ister. Aynı kök insanın başkasının malıyla bile gösteriş yapabileceğini söyler: {ar:فلان يتكثر بمال غيره, tr:fülânun yetekesseru bi-mâli gayrih, gloss:filan başkasının malıyla çok görünmeye çalışır, source:"ك ث ر,B003"}. Bu kalıpta çokluk sahip olunan bir şey değil, gösterilen bir şeydir.

Görmek fiilinin ailesi seyirciyi sağlar. Bir şeyi insanlar görsün diye yapmak bu köktendir: {ar:وراءى فلان يرائي وفعل ذلك رئاء الناس وهو أن يفعل شيئا ليراه الناس, tr:ve râe fülânun yürâî ve feale zâlike riâe'n-nâsi ve hüve en yef'ale şey'en li-yerâhu'n-nâs, gloss:filan gösteriş yaptı; bunu insanlara gösteriş için yaptı; yani insanlar görsün diye bir şey yaptı, source:"ر ء ي,B005"}; {ar:فلان مراء والاسم الرياء وفعل ذلك رياء وسمعة, tr:fülânun mürâin ve'l-ismü'r-riyâü ve feale zâlike riyâen ve sum'a, gloss:filan gösterişçidir; adı riyadır; bunu görülmek ve duyulmak için yaptı, source:"ر ء ي,B005"}. İnsanlara gösterilen güzel kılık da bu köktendir: {ar:والري ما أريت القوم من حسن الشارة والهيئة والرواء حسن المنظر, tr:ve'r-riyyü mâ ereyte'l-kavme min husni'ş-şâreti ve'l-hey'eti ve'r-ruvâü husnü'l-manzar, gloss:riyy topluluğa gösterdiğin güzel kılık ve görünüştür; ruvâ güzel görünüştür, source:"ر ء ي,B006"}; {ar:الرئي ما رأت العين من حال حسنة والرواء حسن المنظر, tr:er-ri'yü mâ raeti'l-aynü min hâlin hasenetin ve'r-ruvâü husnü'l-manzar, gloss:ri'y gözün gördüğü güzel hâldir; ruvâ güzel görünüştür, source:"ر ء ي,B006"}. Nimet kelimesinin de bir anlamı yaşamın güzelliği ve tazeliğidir: {ar:نعمة العيش حسنه وغضارته, tr:na'metü'l-ayşi husnühû ve gadâratüh, gloss:yaşamın na'meti onun güzelliği ve tazeliğidir, source:"ن ع م,B002"}, yani sergilenebilen rahat bir hayat.

Altıncı ayette yön tersine döner. Görülmek için düzenleyenlere {ar:لَتَرَوُنَّ, tr:leteravünne, gloss:mutlaka göreceksiniz, source:102:6} denir, ve gördükleri şey bir gösteri değil cehennemdir. Fiil burada düz anlamıyla gözle görmedir: {ar:رأيت بعيني رؤية ورأيته رأي العين, tr:raeytü bi-aynî ru'yeten ve raeytühû ra'ye'l-ayn, gloss:kendi gözümle gördüm; onu göz görüşüyle gördüm, source:"ر ء ي,B001"}. Gösteren seyirci yerine konur. Bu imge ayetteki anlamı değiştirmez; aynı fiilin ailesinde "görülsün diye yapmak" bulunduğu için, görme vaadi gösteriş yarışının ters yüz edilmiş hâli olarak duyulur.

Kur'an bu ters yüz edilişi birkaç yerde sahneler. Ayetler okunduğunda inkâr edenler müminlere hangi topluluğun makamının daha iyi, meclisinin daha güzel olduğunu sorarlar {source:19:73}; Allah cevap verir: {ar:وَكَمْ أَهْلَكْنَا قَبْلَهُم مِّن قَرْنٍ هُمْ أَحْسَنُ أَثَٰثًۭا وَرِءْيًۭا, tr:ve kem ehleknâ kablehüm min karnin hüm ahsenü esâsen ve ri'yâ, gloss:onlardan önce eşyaca ve görünüşçe daha güzel nice nesli helak ettik, source:19:74}. Buradaki {ar:رِءْيًۭا, tr:ri'yen, gloss:görünüş, source:19:74} kelimesi, görülmek için sergilenen görünüşün adıdır ve görmek fiiliyle aynı köktendir. Karun kavminin karşısına süsüyle çıkar: {ar:فَخَرَجَ عَلَىٰ قَوْمِهِۦ فِى زِينَتِهِۦ, tr:fe-harace alâ kavmihî fî zînetih, gloss:süsü içinde kavminin karşısına çıktı, source:28:79}, ve dünya hayatını isteyenler aynı ayette "Keşke Karun'a verilenin bir benzeri bizim de olsaydı" derler; ardından {ar:فَخَسَفْنَا بِهِۦ وَبِدَارِهِ ٱلْأَرْضَ, tr:fe-hasefnâ bihî ve bi-dârihi'l-ard, gloss:onu da evini de yere geçirdik, source:28:81}. Sergilenen toprağın altına girer.

Allah müminleri de bu gösterişe karşı uyarır: {ar:وَلَا تَكُونُوا۟ كَٱلَّذِينَ خَرَجُوا۟ مِن دِيَٰرِهِم بَطَرًۭا وَرِئَآءَ ٱلنَّاسِ, tr:ve lâ tekûnû kellezîne harecû min diyârihim bataran ve riâe'n-nâs, gloss:yurtlarından şımarıkça ve insanlara gösteriş için çıkanlar gibi olmayın, source:8:47}. Kısa bir surede gösteriş en küçük yardımı esirgemeyle birlikte anılır: {ar:ٱلَّذِينَ هُمْ يُرَآءُونَ, tr:ellezîne hüm yürâûn, gloss:onlar ki gösteriş yaparlar, source:107:6} {ar:وَيَمْنَعُونَ ٱلْمَاعُونَ, tr:ve yemneûne'l-mâûn, gloss:ve ufak yardımı bile esirgerler, source:107:7}. Görülmek isteyen insan kendini de seyreder: Allah insanın azdığını söyler {source:96:6}, {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en raâhü'stağnâ, gloss:kendini yeterli gördüğü için, source:96:7}. Peygamber'e de inkârcıların malları ve evlatları karşısında hayranlığa kapılmaması söylenir: {ar:فَلَا تُعْجِبْكَ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُمْ, tr:fe-lâ tu'cibke emvâlühüm ve lâ evlâdühüm, gloss:onların malları ve evlatları seni hayran bırakmasın, source:9:55}; sergilenen çokluğun seyircisi olmak da reddedilir.

Bu imgenin kattığı, surenin ortasındaki görmenin bir karşılık olduğudur: birinci ayetteki çokluk başkalarına gösterilmek içindi; altıncı ve yedinci ayetlerde gösteren, kendisine gösterileni görmek zorunda kalır.

Kaynaklar: 102:1 ٱلتَّكَاثُرُ ك ث ر B002; 102:1 ٱلتَّكَاثُرُ ك ث ر B003; 102:6 لَتَرَوُنَّ ر ء ي B005; 102:6 لَتَرَوُنَّ ر ء ي B006; 102:8 ٱلنَّعِيمِ ن ع م B002; 102:6 لَتَرَوُنَّ ر ء ي B001

## Ziyaret, konak ve ağırlama

İkinci ayetin fiili düz anlamıyla ziyarettir: {ar:زرته أزوره زورا وزيارة وزوارة, tr:zürtühû ezûruhû zevran ve ziyâreten ve zivâre, gloss:onu ziyaret ettim, source:"ز و ر,B003"}; birine yönelmek, onu bilerek kastetmek: {ar:زرت فلانا تلقيته بزوري أو قصدت زوره, tr:zürtü fülânen telakkaytühû bi-zevrî ev kasadtü zevrah, gloss:filanı ziyaret ettim; onu göğsümle karşıladım ya da onun göğsüne yöneldim, source:"ز و ر,B003"}. Ziyaretin bir konuğu, bir ev sahibi ve konuğa gösterilen bir ikramı vardır: {ar:التزوير كرامة الزائر, tr:et-tezvîru kerâmetü'z-zâir, gloss:tezvîr ziyaretçiye gösterilen ikramdır, source:"ز و ر,B003"}. Ve ziyaretçi kalmaz; ziyaret, gidilip dönülen bir varıştır. Kabirleri "ziyaret ettiniz" demek, onları bir konak, geçilen bir yer olarak adlandırmaktır.

Konak da hazırdır: {ar:القبر مقر الميت, tr:el-kabru makarru'l-meyyit, gloss:kabir ölünün karar kıldığı yerdir, source:"ق ب ر,B001"}; {ar:أقبرته جعلت له مكانا يقبر فيه, tr:akbartühû cealtü lehû mekânen yukbaru fîh, gloss:ona gömüleceği bir yer yaptım, source:"ق ب ر,B001"}. Altıncı ayetin cehennemi de bir yerin adıdır: {ar:والجاحم المكان الشديد الحر وبه سميت الجحيم, tr:ve'l-câhimü'l-mekânü'ş-şedîdü'l-harri ve bihî sümmiyeti'l-cahîm, gloss:câhim çok sıcak yerdir; cahîm adını ondan almıştır, source:"ج ح م,B001"}. Sekizinci ayetin nimetinin kökü hoş bir yaşamı adlandırır, {ar:أصل واحد يدل على ترفه وطيب عيش وصلاح, tr:aslun vâhidun yedüllü alâ teraffuhin ve tîbi ayşin ve salâh, gloss:bolluğu ve hoş yaşamı ve iyiliği gösteren tek bir kök, source:"ن ع م,B001"}, ve bir kalıp ifadede bir yere varıp orayı kendine uygun bulmayı ve orada kalmayı anlatır: {ar:أتيت أرضا فنعمتني أي وافقتني وأقمت بها, tr:eteytü arden fe-neametnî ey vâfekatnî ve ekamtü bihâ, gloss:bir yere geldim ve orası bana hoş geldi; yani bana uydu ve orada kaldım, source:"ن ع م,B011"}; {ar:أتيت أرض بني فلان فتنعمتني إذا وافقته, tr:eteytü arda benî fülânin fe-tenaammetnî izâ vâfakatüh, gloss:filan oğullarının yurduna geldim ve orası bana uydu, source:"ن ع م,B011"}. Böylece surenin üç yeri, kabirler, cehennem ve nimet, bir yolculuğun durakları olarak duyulabilir: kabir geçilen konaktır, cehennem çok sıcak bir varış yeridir, nimet varılıp kalınan uygun bir yurttur. Bu bir yakıştırmadır; ayetlerde kelimeler kendi anlamlarındadır, ama ziyaret fiili bu durakları birbirine bağlar.

Kur'an varan konuğa sunulan ağırlamayı {ar:نُزُل, tr:nüzül, gloss:konuğa varışında sunulan ağırlama, source:"memory"} diye adlandırır ve bu kelimeyi tam da bu iki varış yeri için kullanır. Allah can boğaza dayandığında {source:56:83} ve başındakiler bakıp dururken {source:56:84} ölenin üç hâlini anlatır. Allah'a yakın olanlardansa {source:56:88}: {ar:فَرَوْحٌۭ وَرَيْحَانٌۭ وَجَنَّتُ نَعِيمٍۢ, tr:fe-revhun ve reyhânun ve cennetü naîm, gloss:ona rahatlık ve güzel koku ve nimet cenneti vardır, source:56:89}. Yalanlayan sapkınlardansa {source:56:92}: {ar:فَنُزُلٌۭ مِّنْ حَمِيمٍۢ, tr:fe-nüzülün min hamîm, gloss:kaynar sudan bir ağırlama, source:56:93} {ar:وَتَصْلِيَةُ جَحِيمٍ, tr:ve tasliyetü cahîm, gloss:ve cehenneme sokulmak, source:56:94}. Ve sahne şu sözle kapanır: {ar:إِنَّ هَٰذَا لَهُوَ حَقُّ ٱلْيَقِينِ, tr:inne hâzâ le-hüve hakku'l-yakîn, gloss:işte bu kesin bilginin ta kendisidir, source:56:95}. Nimet, cehennem, varan konuğa sunulan ağırlama ve yakîn: surenin son kelimelerinin hepsi bu kısa sahnededir ve hepsi ölüm anında açılır. Aynı surede sol tarafın halkı için hazırlanan yer de bir ağırlamanın tersidir: {ar:فِى سَمُومٍۢ وَحَمِيمٍۢ, tr:fî semûmin ve hamîm, gloss:kavurucu bir rüzgârda ve kaynar suda, source:56:42} {ar:وَظِلٍّۢ مِّن يَحْمُومٍۢ, tr:ve zıllin min yahmûm, gloss:ve kapkara dumandan bir gölgede, source:56:43} {ar:لَّا بَارِدٍۢ وَلَا كَرِيمٍ, tr:lâ bâridin ve lâ kerîm, gloss:ne serin ne cömert, source:56:44}. Gölge cömert değildir: ikram reddedilmiştir. Hemen ardından onların daha önce bolluk içinde yaşadıkları söylenir: {ar:إِنَّهُمْ كَانُوا۟ قَبْلَ ذَٰلِكَ مُتْرَفِينَ, tr:innehüm kânû kable zâlike mütrefîn, gloss:onlar bundan önce refah içinde şımarmışlardı, source:56:45}. Sekizinci ayetin sorusunun konusu olan rahatlık, burada reddedilen ikramın yanında anılır.

Cennet bahçelerini {source:37:43} anlattıktan sonra Allah sorar: {ar:أَذَٰلِكَ خَيْرٌۭ نُّزُلًا أَمْ شَجَرَةُ ٱلزَّقُّومِ, tr:e-zâlike hayrun nüzülen em şeceratü'z-zakkûm, gloss:ağırlama olarak bu mu daha iyi yoksa zakkum ağacı mı, source:37:62}; ve zakkumu tanımlar: {ar:إِنَّهَا شَجَرَةٌۭ تَخْرُجُ فِىٓ أَصْلِ ٱلْجَحِيمِ, tr:innehâ şeceratün tahrucü fî asli'l-cahîm, gloss:o cehennemin dibinde çıkan bir ağaçtır, source:37:64}. Başka bir yerde aynı kelime iki yöne de verilir: {ar:إِنَّآ أَعْتَدْنَا جَهَنَّمَ لِلْكَٰفِرِينَ نُزُلًۭا, tr:innâ a'tednâ cehenneme li'l-kâfirîne nüzülâ, gloss:biz cehennemi kâfirlere bir ağırlama olarak hazırladık, source:18:102}, ve iman edip iyi işler yapanlar için {ar:كَانَتْ لَهُمْ جَنَّٰتُ ٱلْفِرْدَوْسِ نُزُلًا, tr:kânet lehüm cennâtü'l-firdevsi nüzülâ, gloss:Firdevs cennetleri onlar için bir ağırlama oldu, source:18:107}.

Ziyaretçinin kalmadığı da Kur'an'da sahnelenir. Ölüm gelince insan geri dönmek ister: {ar:حَتَّىٰٓ إِذَا جَآءَ أَحَدَهُمُ ٱلْمَوْتُ قَالَ رَبِّ ٱرْجِعُونِ, tr:hattâ izâ câe ehadehümü'l-mevtü kâle rabbi'rciûn, gloss:sonunda onlardan birine ölüm gelince "Rabbim beni geri döndürün" der, source:23:99}; ve cevap: {ar:وَمِن وَرَآئِهِم بَرْزَخٌ إِلَىٰ يَوْمِ يُبْعَثُونَ, tr:ve min verâihim berzahun ilâ yevmi yüb'asûn, gloss:onların ötesinde diriltilecekleri güne kadar bir perde vardır, source:23:100}. "-e kadar" ölüme varır, ama oradaki kalış bir son değil bir bekleyiştir. Sûra üflendiğinde {source:36:51} ölüler {ar:قَالُوا۟ يَٰوَيْلَنَا مَنۢ بَعَثَنَا مِن مَّرْقَدِنَا, tr:kâlû yâ veylenâ men beasenâ min merkadinâ, gloss:"Vay hâlimize; bizi yattığımız yerden kim kaldırdı" derler, source:36:52}; ve {ar:يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًۭا, tr:yevme yahrucûne mine'l-ecdâsi sirâan, gloss:kabirlerden hızla çıktıkları gün, source:70:43}. Konak terk edilir. Bir sonraki varış yeri ise bir barınak diye adlandırılır: azgınlık edip dünya hayatını seçen için {source:79:38} {ar:فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ, tr:fe-inne'l-cahîme hiye'l-me'vâ, gloss:cehennem işte onun barınağıdır, source:79:39}.

Bu imgenin kattığı, ikinci ayetin fiil seçiminin taşıdığı geçicilik duygusudur: kabir bir yerleşme değil bir ziyarettir, ve ardından gelen iki yer, cehennem ve nimet, yolculuğun asıl varış noktalarıdır; her birinin kendi ağırlaması vardır.

Kaynaklar: 102:2 زُرْتُمُ ز و ر B003; 102:2 ٱلْمَقَابِرَ ق ب ر B001; 102:6 ٱلْجَحِيمَ ج ح م B001; 102:8 ٱلنَّعِيمِ ن ع م B011; 102:8 ٱلنَّعِيمِ ن ع م B001

## Alev alev bakan göz, gören ateş, serinleyen göz

Altıncı ayette görülen şeyin adı, kök ailesinde bir gözdür: {ar:الجحمة العين بلغة حمير وجحمتا الأسد عيناه بكل لغة والأجحم الشديد حمرة العين مع سعتها, tr:el-cahmetü'l-aynü bi-lugati Himyera ve cahmete'l-esedi aynâhü bi-külli lugatin ve'l-echamü'ş-şedîdü humrati'l-ayni ma'a se'atihâ, gloss:cahme Himyer dilinde gözdür; aslanın iki cahmesi her dilde onun gözleridir; echam gözü iri ve çok kırmızı olandır, source:"ج ح م,B003"}. Aslanın gözleri bu adı yanmalarından alır: {ar:جحمتا الأسد عيناه لتوقدهما, tr:cahmete'l-esedi aynâhü li-tevakkudihimâ, gloss:aslanın iki cahmesi gözleridir; tutuşmuş gibi parladıkları için, source:"ج ح م,B003"}. Fiil biçimi gözünü açıp dikmektir: {ar:جحم الرجل فتح عينيه كالشاخص وجحمني بعينيه تجحيما أحد إلي النظر والجحام داء يصيب الانسان فترم عيناه, tr:cehame'r-racülü fetaha ayneyhi ke'ş-şâhisi ve cahhamenî bi-ayneyhi techîmen ehadde ileyye'n-nazara ve'l-cuhâmü dâun yusîbü'l-insâne fe-terimü aynâh, gloss:adam gözlerini dikilmiş gibi açtı; bana gözlerini dikti; yani bana keskin baktı; cuhâm insanın gözlerini şişiren bir hastalıktır, source:"ج ح م,B003"}. Öfke dalı aynı yanmayı yüze taşır: {ar:جحم وجهه من شدة الغضب استعارة من جحمة النار وذلك من ثوران حرارة القلب, tr:cehime vechühû min şiddeti'l-gadabi isti'âratün min cahmeti'n-nâri ve zâlike min sevarâni harârati'l-kalb, gloss:yüzü öfkenin şiddetinden kızıştı; ateşin alevinden ödünçtür ve kalbin sıcaklığının kabarmasındandır, source:"ج ح م,B004"}. Ateşin parlaması ile görme fiili de bir ifadede birleşir: {ar:ورأيت جحمة النار أي توقدها, tr:ve raeytü cahmete'n-nâri ey tevakkudehâ, gloss:ateşin cahmesini gördüm; yani tutuşmasını, source:"ج ح م,B001"}. Ayette kelime ateşin adıdır; ama ailesi yanında duyulduğunda {ar:لَتَرَوُنَّ ٱلْجَحِيمَ, tr:leteravünne'l-cahîm, gloss:cehennemi mutlaka göreceksiniz, source:102:6} cümlesinde görülen şey, alev alev parlayan ve gözünü dikmiş bir bakış olarak da işitilir.

Görmenin karşılıklı biçimi de kökte vardır: {ar:تراءى القوم إذا رأى بعضهم بعضا, tr:terâe'l-kavmü izâ raâ ba'duhüm ba'dâ, gloss:topluluk birbirini gördü, source:"ر ء ي,B004"}; {ar:تراءينا أي تلاقينا فرأيته ورآني, tr:terâeynâ ey telâkaynâ fe-raeytühû ve raânî, gloss:birbirimizi gördük; yani karşılaştık; ben onu gördüm o da beni, source:"ر ء ي,B004"}. Kur'an ateşin onları gördüğünü söyler. Allah, Saati yalanlayanlar için alevli bir ateş hazırladığını söyledikten {source:25:11} sonra der ki: {ar:إِذَا رَأَتْهُم مِّن مَّكَانٍۭ بَعِيدٍۢ سَمِعُوا۟ لَهَا تَغَيُّظًۭا وَزَفِيرًۭا, tr:izâ raethüm min mekânin baîdin semiû lehâ tegayyuzan ve zefîrâ, gloss:onları uzak bir yerden gördüğünde onun öfkeyle kaynamasını ve uğultusunu işitirler, source:25:12}. Görme burada ateşten insana doğrudur, ve ateşin hâli öfkedir. Başka bir yerde Allah oraya atılanları anlatır: {ar:إِذَآ أُلْقُوا۟ فِيهَا سَمِعُوا۟ لَهَا شَهِيقًۭا وَهِىَ تَفُورُ, tr:izâ ülkû fîhâ semiû lehâ şehîkan ve hiye tefûr, gloss:oraya atıldıklarında onun hırıltısını işitirler; o kaynayıp durur, source:67:7} {ar:تَكَادُ تَمَيَّزُ مِنَ ٱلْغَيْظِ, tr:tekâdü temeyyezü mine'l-gayz, gloss:öfkeden neredeyse çatlayacak, source:67:8}. Öfkeden yüzü kızışan adamın imgesi burada ateşin kendisidir. Altıncı ayetteki fiil karşılıklı değildir; ama bu sahneler yanında duyulduğunda görme iki yönlüdür: onlar cehennemi görür, cehennem de onları.

Cehennemin görünür kılınışı da sahnelenir: büyük felaket geldiğinde {source:79:34} {ar:وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ, tr:ve burrizeti'l-cahîmü li-men yerâ, gloss:ve cehennem görenler için ortaya çıkarılır, source:79:36}; İbrahim'in duasında {ar:وَبُرِّزَتِ ٱلْجَحِيمُ لِلْغَاوِينَ, tr:ve burrizeti'l-cahîmü li'l-gâvîn, gloss:ve cehennem azgınlara gösterilir, source:26:91}; ve {ar:وَعَرَضْنَا جَهَنَّمَ يَوْمَئِذٍۢ لِّلْكَٰفِرِينَ عَرْضًا, tr:ve aradnâ cehenneme yevmeizin li'l-kâfirîne ardâ, gloss:o gün cehennemi kâfirlere açıkça sunarız, source:18:100}. Sonraki ayet o kâfirleri gözleri örtülü olanlar diye tanımlar: {ar:ٱلَّذِينَ كَانَتْ أَعْيُنُهُمْ فِى غِطَآءٍ عَن ذِكْرِى, tr:ellezîne kânet a'yünühüm fî gıtâin an zikrî, gloss:gözleri beni anmaktan bir örtü içinde olanlar, source:18:101}. Anmaya karşı örtülü olan göz, o gün kendisine sunulan cehennemi görür.

İnsanın gözü de bu sahnede dikilir. Allah zalimleri {ar:لِيَوْمٍۢ تَشْخَصُ فِيهِ ٱلْأَبْصَٰرُ, tr:li-yevmin teşhasu fîhi'l-ebsâr, gloss:gözlerin dikilip kaldığı bir güne, source:14:42} ertelediğini söyler; vaat yaklaştığında {ar:فَإِذَا هِىَ شَٰخِصَةٌ أَبْصَٰرُ ٱلَّذِينَ كَفَرُوا۟, tr:fe-izâ hiye şâhisatün ebsârü'llezîne keferû, gloss:bir de bakarsın ki inkâr edenlerin gözleri dikilip kalmıştır, source:21:97}, ve onlar {ar:يَٰوَيْلَنَا قَدْ كُنَّا فِى غَفْلَةٍۢ مِّنْ هَٰذَا, tr:yâ veylenâ kad künnâ fî gafletin min hâzâ, gloss:vay hâlimize; biz bundan gaflet içindeydik, source:21:97} derler. Ateşin kökündeki "dikilmiş gibi bakan göz", bu sahnede insanın gözüdür.

Yedinci ayetin {ar:عَيْنَ, tr:ayn, gloss:göz, source:102:7} kelimesi her görenin bakan gözüdür: {ar:العين الناظرة لكل ذي بصر, tr:el-aynü'n-nâziratü li-külli zî basar, gloss:ayn gören her canlının bakan gözüdür, source:"ع ي ن,B001"}. Aynı kelimenin bir kullanımı korumak ve gözetmektir: {ar:أنت على عيني، في الإكرام والحفظ جميعا, tr:ente alâ aynî fi'l-ikrâmi ve'l-hıfzı cemîan, gloss:sen gözümün üstündesin; hem ikram hem koruma anlamında, source:"ع ي ن,B003"}; {ar:بحيث نرى ونحفظ, tr:bi-haysü nerâ ve nahfazu, gloss:görüp koruduğumuz yerde, source:"ع ي ن,B003"}. Sekizinci ayetin nimeti de bir kalıp ifadede gözle birleşir: {ar:نعمة العين قرتها, tr:nu'metü'l-ayni kurratühâ, gloss:gözün nimeti onun serinliğidir, source:"ن ع م,B013"}; {ar:نعم ونعمى عين ونعمة عين أي قرة عين, tr:nu'mu ve nu'mâ aynin ve nu'metü aynin ey kurratü ayn, gloss:göz nimeti; yani göz serinliği, source:"ن ع م,B013"}. Arapçada sevinç gözün serinlemesi diye anlatılır: {ar:قرة العين, tr:kurratü'l-ayn, gloss:göz serinliği; göz aydınlığı, source:"memory"}. Altıncı ayetin alev alev parlayan gözünün karşısında, sekizinci ayetin nimeti serinlemiş bir gözün adını taşır.

Kur'an bu iki gözü aynı sahnede buluşturur. Cennet halkı birbirine dönüp soruşurken {source:37:50} içlerinden biri dünyadaki bir arkadaşını hatırlar; o arkadaş ölüp toprak olduktan sonra hesaba çekileceklerini inkâr ediyordu {source:37:53}. "Bakar mısınız" diye sorar {source:37:54}: {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fe'ttalea fe-raâhü fî sevâi'l-cahîm, gloss:yukarıdan baktı ve onu cehennemin ortasında gördü, source:37:55}; ve der ki: {ar:وَلَوْلَا نِعْمَةُ رَبِّى لَكُنتُ مِنَ ٱلْمُحْضَرِينَ, tr:ve levlâ ni'metü rabbî le-küntü mine'l-muhdarîn, gloss:Rabbimin nimeti olmasaydı ben de oraya getirilenlerden olurdum, source:37:57}. Cehennemi nimetin içinden görmek: altıncı ayetin görmesi ve sekizinci ayetin nimeti bu sahnede aynı kişinin gözündedir. Serinleyen göz başka iki yerde de anılır. Allah iman edenlerin ödülü için der ki: {ar:فَلَا تَعْلَمُ نَفْسٌۭ مَّآ أُخْفِىَ لَهُم مِّن قُرَّةِ أَعْيُنٍۢ, tr:fe-lâ ta'lemu nefsün mâ uhfiye lehüm min kurrati a'yün, gloss:hiçbir can onlar için gözleri serinletecek neyin saklandığını bilmez, source:32:17}: bilmek, saklılık ve serinleyen göz bir arada. Rahman'ın kulları da {ar:رَبَّنَا هَبْ لَنَا مِنْ أَزْوَٰجِنَا وَذُرِّيَّٰتِنَا قُرَّةَ أَعْيُنٍۢ, tr:rabbenâ heb lenâ min ezvâcinâ ve zürriyyâtinâ kurrate a'yün, gloss:Rabbimiz; bize eşlerimizden ve soyumuzdan göz serinliği bağışla, source:25:74} diye dua ederler: birinci ayette sayılan eşler ve çocuklar burada göz serinliği olarak istenir. Yüz de iki hâlde görünür: iyiler nimet içindedir {source:83:22}, tahtlar üstünde bakarlar {source:83:23}, ve {ar:تَعْرِفُ فِى وُجُوهِهِمْ نَضْرَةَ ٱلنَّعِيمِ, tr:ta'rifu fî vücûhihim nadrate'n-naîm, gloss:yüzlerinde nimetin parlaklığını tanırsın, source:83:24}. Başka bir surede o günün iki yüzü yan yana konur: {ar:وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ, tr:vücûhun yevmeizin hâşia, gloss:o gün bazı yüzler zelildir, source:88:2} ve {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ, tr:vücûhun yevmeizin nâime, gloss:o gün bazı yüzler nimet içinde yumuşaktır, source:88:8}; ikinci yüzün sıfatı nimet kelimesiyle aynı köktendir. Öfkeyle kızışan yüzün karşısında nimetle parlayan yüz durur.

Bu imgenin kattığı, surenin son üç ayetinin bir göz değişimini taşımasıdır: alev alev parlayan ve dikilen bir bakışın karşısına çıkmak, sonra onu kendi gözüyle görmek, sonra gözün serinliği olan nimetin sorulması.

Kaynaklar: 102:6 ٱلْجَحِيمَ ج ح م B003; 102:6 ٱلْجَحِيمَ ج ح م B004; 102:6 ٱلْجَحِيمَ ج ح م B001; 102:6 لَتَرَوُنَّ ر ء ي B004; 102:7 عَيْنَ ع ي ن B001; 102:7 عَيْنَ ع ي ن B003; 102:8 ٱلنَّعِيمِ ن ع م B013

## Kızgın ateş ve serin nimet

Altıncı ayetin cehennemi, kökünde sıcaklığın en şiddetli hâlidir: {ar:عظمها به الحرارة وشدتها والجاحم المكان الشديد الحر وبه سميت الجحيم, tr:uzmuhâ bihi'l-harâratü ve şiddetühâ ve'l-câhimü'l-mekânü'ş-şedîdü'l-harri ve bihî sümmiyeti'l-cahîm, gloss:kökün ana anlamı sıcaklık ve onun şiddetidir; câhim çok sıcak yerdir; cahîm adını ondan almıştır, source:"ج ح م,B001"}; {ar:الجحيم النار الشديدة التأجج والالتهاب, tr:el-cahîmü'n-nâru'ş-şedîdetü't-teeccüci ve'l-iltihâb, gloss:cahîm çok harlı ve alevli ateştir, source:"ج ح م,B001"}. Sekizinci ayetin nimeti ise kökünde yumuşaklık ve nemli bir rahatlıktır: {ar:نعم الشيء صار ناعما لينا, tr:neume'ş-şey'ü sâra nâimen leyyinâ, gloss:şey yumuşak ve narin oldu, source:"ن ع م,B002"}; {ar:نعمة العيش حسنه وغضارته, tr:na'metü'l-ayşi husnühû ve gadâratüh, gloss:yaşamın na'meti onun güzelliği ve tazeliğidir, source:"ن ع م,B002"}. Aynı kök, rüzgârların en ıslağı ve nemlisi olduğu için güney rüzgârını adlandırır: {ar:النعامى ريح الجنوب لأنها أبل الرياح وأرطبها, tr:en-neâmâ rîhu'l-cenûbi li-ennehâ eballü'r-riyâhi ve ertabuhâ, gloss:neâmâ güney rüzgârıdır; çünkü rüzgârların en ıslağı ve en nemlisidir, source:"ن ع م,B009"}; {ar:النعامي الريح اللينة, tr:en-neâmî er-rîhu'l-leyyine, gloss:neâmî yumuşak rüzgârdır, source:"ن ع م,B009"}. Bir dağın tepesine ya da kuyunun ağzına kurulan gölgeliği de devekuşuna benzediği için devekuşunun adıyla anar: {ar:على معنى التشبيه النعامة وهي كالظلة تجعل على رءوس الجبل, tr:alâ ma'na't-teşbîhi'n-neâmetü ve hiye ke'z-zulleti tüc'alü alâ ruûsi'l-cebel, gloss:benzetme yoluyla neâme; dağ başlarına kurulan bir gölgelik gibidir, source:"ن ع م,B007"}; {ar:النعامة المظلة في الجبل وعلى رأس البئر تشبيها بالنعامة في الهيئة, tr:en-neâmetü'l-mizalletü fi'l-cebeli ve alâ re'si'l-bi'ri teşbîhen bi'n-neâmeti fi'l-hey'e, gloss:neâme dağda ve kuyu başında kurulan gölgeliktir; görünüşte devekuşuna benzetilerek, source:"ن ع م,B007"}. Yedinci ayetin göz kelimesi akan pınarı da adlandırır: {ar:العين الجارية النابعة من عيون الماء, tr:el-aynü'l-câriyetü'n-nâbiatü min uyûni'l-mâ, gloss:ayn su kaynaklarından fışkırıp akan pınardır, source:"ع ي ن,B006"}; {ar:العين الينبوع الذي ينبع من الأرض ويجري, tr:el-aynü'l-yenbûu'llezî yenbeu mine'l-ardı ve yecrî, gloss:ayn yerden kaynayıp akan kaynaktır, source:"ع ي ن,B006"}. Bilmek kökünün ailesinde de suyla dolu bir kuyu vardır: {ar:العيلم الركية الكثيرة الماء, tr:el-aylemü'r-rakiyyetü'l-kesîratü'l-mâ, gloss:aylem suyu bol kuyudur, source:"ع ل م,B005"}; {ar:العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء, tr:el-aylemü yükâlü innehü'l-bahru ve yükâlü innehü'l-bi'ru'l-kesîratü'l-mâ, gloss:aylem için deniz denir; suyu bol kuyu da denir, source:"ع ل م,B005"}.

Bu dallar ayetlerin anlamı değildir; ama yanlarında duyulduklarında altıncı ayetten sekizinci ayete geçiş bir sıcaklıktan serinliğe geçiş olarak da işitilir: çukurdaki harlı ateşten nemli rüzgâra, kuyu başındaki gölgeye ve akan pınara. Sekizinci ayette sorulan nimet bu yumuşaklık ve serinliktir; ve soru ateş görüldükten sonra gelir.

Kur'an iki kelimeyi sabit bir çift olarak kullanır: {ar:إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍۢ, tr:inne'l-ebrâra le-fî naîm, gloss:iyiler elbette nimet içindedir, source:82:13} {ar:وَإِنَّ ٱلْفُجَّارَ لَفِى جَحِيمٍۢ, tr:ve inne'l-füccâra le-fî cahîm, gloss:günahkârlar da elbette cehennem içindedir, source:82:14}. Surenin altıncı ve sekizinci ayetlerinin iki kelimesi burada yan yana durur, ve hemen ardından günahkârların ondan uzak kalmayacağı söylenir {source:82:16}. Sağ tarafın halkı için {ar:وَظِلٍّۢ مَّمْدُودٍۢ, tr:ve zıllin memdûd, gloss:uzayıp giden bir gölge, source:56:30} ve {ar:وَمَآءٍۢ مَّسْكُوبٍۢ, tr:ve mâin meskûb, gloss:dökülüp akan su, source:56:31} vardır; sol tarafın halkı için ise kavurucu rüzgâr, kaynar su ve {ar:لَّا بَارِدٍۢ وَلَا كَرِيمٍ, tr:lâ bâridin ve lâ kerîm, gloss:ne serin ne cömert, source:56:44} bir gölge. Yalanlayanlara da {ar:ٱنطَلِقُوٓا۟ إِلَىٰ ظِلٍّۢ ذِى ثَلَٰثِ شُعَبٍۢ, tr:intalikû ilâ zıllin zî selâsi şuab, gloss:üç kollu bir gölgeye gidin, source:77:30} denir, ve o gölge {ar:لَّا ظَلِيلٍۢ وَلَا يُغْنِى مِنَ ٱللَّهَبِ, tr:lâ zalîlin ve lâ yuğnî mine'l-leheb, gloss:ne gölgelendirir ne de alevden korur, source:77:31}. Gölge vardır ama gölge değildir.

Pınar iki yanda da akar. O günün yüzlerini anlatan surede zelil yüzler {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4} ve {ar:تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:tuskâ min aynin âniye, gloss:kaynar bir pınardan içirilir, source:88:5}; nimetle yumuşamış yüzler ise yüce bir bahçededir {source:88:10} ve {ar:فِيهَا عَيْنٌۭ جَارِيَةٌۭ, tr:fîhâ aynun câriye, gloss:orada akan bir pınar vardır, source:88:12}. Pınar kelimesi yedinci ayetin göz kelimesidir; burada hem kaynar hem akar. Nimet içindeki iyilerin içeceği de bir pınardan karışır: {ar:وَمِزَاجُهُۥ مِن تَسْنِيمٍ, tr:ve mizâcuhû min tesnîm, gloss:karışımı Tesnîm'dendir, source:83:27} {ar:عَيْنًۭا يَشْرَبُ بِهَا ٱلْمُقَرَّبُونَ, tr:aynen yeşrabü bihe'l-mukarrabûn, gloss:yakın kılınanların içtiği bir pınar, source:83:28}. Ve ateşin halkı cennetin halkına seslenir: {ar:أَنْ أَفِيضُوا۟ عَلَيْنَا مِنَ ٱلْمَآءِ أَوْ مِمَّا رَزَقَكُمُ ٱللَّهُ, tr:en efîdû aleynâ mine'l-mâi ev mimmâ razakakümu'llâh, gloss:üzerimize biraz su ya da Allah'ın size verdiği rızıktan akıtın, source:7:50}. Sıcağın içinden serinlik istenir; cevap aynı ayette verilir: {ar:إِنَّ ٱللَّهَ حَرَّمَهُمَا عَلَى ٱلْكَٰفِرِينَ, tr:inna'llâhe harramehümâ ale'l-kâfirîn, gloss:Allah ikisini de kâfirlere haram kılmıştır, source:7:50}.

Bu imgenin kattığı, sekizinci ayetin nimetinin soyut bir "bolluk" değil, ateşin karşısında somut bir serinlik olarak duyulmasıdır: gölge, rüzgâr, su. Sorgu bu serinlik hakkındadır, ve onu soran sure az önce sıcaklığın en şiddetlisini göstermiştir.

Kaynaklar: 102:6 ٱلْجَحِيمَ ج ح م B001; 102:8 ٱلنَّعِيمِ ن ع م B002; 102:8 ٱلنَّعِيمِ ن ع م B009; 102:8 ٱلنَّعِيمِ ن ع م B007; 102:7 عَيْنَ ع ي ن B006; 102:3 تَعْلَمُونَ ع ل م B005; 102:5 عِلْمَ ع ل م B005

## Verilen, sayılan, sorulan

Surenin ilk kelimesinin ailesi bir bağışı da adlandırır. Değirmenin ağzına atılan avuç, bağışın adı olur: {ar:اللهوة ما يطرحه الطاحن في ثقبة الرحى بيده، وبذلك سمي العطاء لهوة, tr:el-lühvetü mâ yatrahuhu't-tâhinu fî sukbeti'r-rahâ bi-yedihî ve bi-zâlike sümmiye'l-atâü lühve, gloss:lühve değirmencinin eliyle değirmen deliğine attığıdır; bağışa da bu yüzden lühve denmiştir, source:"ل ه و,B003"}; {ar:واللهوة أيضا العطية, tr:ve'l-lühvetü eydan el-atiyye, gloss:lühve aynı zamanda armağandır, source:"ل ه و,B003"}. Çokluk kelimesinin ailesi bol iyiliği ve cömert kişiyi adlandırır: {ar:الكوثر الخير الكثير الذي أعطاه النبي, tr:el-kevserü'l-hayru'l-kesîru'llezî a'tâhü'n-nebiyy, gloss:kevser Peygamber'e verilen bol iyiliktir, source:"ك ث ر,B004"}; {ar:الكوثر الرجل الكثير العطاء والخير والسيد, tr:el-kevserü'r-racülü'l-kesîru'l-atâi ve'l-hayri ve's-seyyid, gloss:kevser çok veren ve iyiliği bol olan adamdır; efendidir, source:"ك ث ر,B004"}. Kur'an bu kelimeyi Peygamber'e verilen şey olarak anar: {ar:إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ, tr:innâ a'taynâke'l-kevser, gloss:biz sana kevseri verdik, source:108:1}. Surenin son kelimesi de bir verenin elinden konan şeydir: {ar:النعمة اليد والصنيعة والمنة وما أنعم به عليك, tr:en-ni'metü'l-yedü ve's-sanîatü ve'l-minnetü ve mâ un'ime bihî aleyk, gloss:nimet el; iyilik; lütuf ve sana bağışlanan şeydir, source:"ن ع م,B001"}; {ar:النعمة الحالة الحسنة والإنعام إيصال الإحسان إلى الغير, tr:en-ni'metü'l-hâletü'l-hasenetü ve'l-in'âmü îsâlü'l-ihsâni ile'l-gayr, gloss:nimet güzel hâldir; in'âm iyiliği başkasına ulaştırmaktır, source:"ن ع م,B001"}. Böylece sure, kelimelerinin aileleri içinde verilmiş olanla açılıp verilmiş olanla kapanır: birinci ayette çoğaltılan şey, sekizinci ayette bir verenin bağışı olarak adlandırılır.

Çokluk kökünün bir kalıp ifadesi zengin adamın yerini tersine çevirir: {ar:رجل مكثور عليه أي كثر من يطلب إليه معروفه, tr:racülün meksûrun aleyhi ey kesüre men yatlubu ileyhi ma'rûfeh, gloss:meksûrun aleyh adam; iyiliğini isteyenleri çoğalmış olan, source:"ك ث ر,B003"}; {ar:مكثور عليه إذا نفد ما عنده وكثرت عليه الحقوق, tr:meksûrun aleyhi izâ nefide mâ indehû ve kesürat aleyhi'l-hukûk, gloss:elindeki tükenip üzerindeki haklar çoğaldığında meksûrun aleyh denir, source:"ك ث ر,B003"}. Çokluğun sahibi, çokluğun kuşattığı kişi olur: istekliler çoğalır, eldeki tükenir, alacaklar birikir.

Sorma fiili de iki yönlüdür: {ar:سألته الشيء وسألته عن الشيء سؤالا ومسألة, tr:seeltühü'ş-şey'e ve seeltühû ani'ş-şey'i suâlen ve mes'ele, gloss:ondan bir şey istedim ve ona bir şey hakkında sordum, source:"س ء ل,B001"}. Sekizinci ayet ikinci yapıyı kullanır: {ar:عَنِ ٱلنَّعِيمِ, tr:ani'n-naîm, gloss:nimet hakkında, source:102:8}; bu bir isteme değil, alınmış olan şey hakkında bir sorgudur. Aynı kökte soran, çok soran ve yoksul da vardır: {ar:رجل سؤلة كثير السؤال, tr:racülün su'letün kesîru's-suâl, gloss:su'le adam; çok soran, source:"س ء ل,B001"}; {ar:الفقير يسمى سائلا, tr:el-fakîru yüsemmâ sâilâ, gloss:yoksula sâil denir, source:"س ء ل,B001"}. İsteğin karşılanması da aynı köktendir: {ar:أسألته سؤلته ومسألته أي قضيت حاجته, tr:es'eltühû su'letehû ve mes'eletehû ey kadaytü hâcetah, gloss:onun isteğini verdim; yani ihtiyacını karşıladım, source:"س ء ل,B003"}. Sorgu ancak bir şey verilmiş olduğu için yapılabilir; istenen önce verilmişti. Birinci ayetin çokluk sahibi sekizinci ayette sorgulananın yerine geçer: dünyada kendisinden istenen kişi, burada kendisine sorulan kişidir.

Yedinci ayetin göz kelimesinin bir anlamı da elde hazır duran ödemedir: {ar:عين غير دين أي مال حاضر, tr:aynun gayru deynin ey mâlun hâdır, gloss:veresiye değil peşin; yani hazır mal, source:"ع ي ن,B011"}. Ziyaret fiilinin ailesi de sözünü önceden düzenleyen adamı anlatır: {ar:الإنسان يزور كلاما أي يقومه قبل أن يتكلم به, tr:el-insânü yüzevviru kelâmen ey yükavvimühû kable en yetekelleme bih, gloss:insan sözü düzenler; yani söylemeden önce onu doğrultur, source:"ز و ر,B006"}. Bu imgeler ayetlerin anlamı değildir, yanlarında duyulur: kabirleri ziyaret eden cevabını içinde hazırlar; ama soru geldiğinde hesap peşindir, şeyin kendisi hazırdır.

Kur'an verme, sayma ve sormayı tek bir ayette toplar: {ar:وَءَاتَىٰكُم مِّن كُلِّ مَا سَأَلْتُمُوهُ ۚ وَإِن تَعُدُّوا۟ نِعْمَتَ ٱللَّهِ لَا تُحْصُوهَآ, tr:ve âtâküm min külli mâ seeltümûh ve in teuddû ni'meta'llâhi lâ tuhsûhâ, gloss:size istediğiniz her şeyden verdi; Allah'ın nimetini saymaya kalksanız sayamazsınız, source:14:34}. İstemek, verilmek, nimet ve saymak: surenin birinci ve sekizinci ayetleri arasındaki yol bu ayettedir. Sayma yarışı burada sayılamayan bir şeye çarpar; başka bir ayet aynı cümleyi tekrarlar {source:16:18}. Nimet, bilgi ve çokluk da bir ayette birleşir. Allah insanı anlatır: {ar:ثُمَّ إِذَا خَوَّلْنَٰهُ نِعْمَةًۭ مِّنَّا قَالَ إِنَّمَآ أُوتِيتُهُۥ عَلَىٰ عِلْمٍۭ ۚ بَلْ هِىَ فِتْنَةٌۭ وَلَٰكِنَّ أَكْثَرَهُمْ لَا يَعْلَمُونَ, tr:sümme izâ havvelnâhü ni'meten minnâ kâle innemâ ûtîtühû alâ ilm bel hiye fitnetün ve lâkinne ekserahüm lâ ya'lemûn, gloss:sonra ona katımızdan bir nimet verdiğimizde "Bu bana ancak bir bilgi sayesinde verildi" der; hayır; o bir sınavdır; ama çoğu bilmez, source:39:49}. Nimet bilgiye dayandırılır, ve ayet "çoğu bilmez" diye biter.

Sorgunun kendisi de sekizinci ayetin vurgulu biçimiyle tekrar eder: {ar:وَلَتُسْـَٔلُنَّ عَمَّا كُنتُمْ تَعْمَلُونَ, tr:ve le-tüs'elünne ammâ küntüm ta'melûn, gloss:yaptıklarınızdan mutlaka sorulacaksınız, source:16:93}; {ar:فَلَنَسْـَٔلَنَّ ٱلَّذِينَ أُرْسِلَ إِلَيْهِمْ وَلَنَسْـَٔلَنَّ ٱلْمُرْسَلِينَ, tr:fe-le-nes'elenne'llezîne ürsile ileyhim ve le-nes'elenne'l-mürselîn, gloss:kendilerine elçi gönderilenlere elbette soracağız ve elçilere de elbette soracağız, source:7:6}. Sorgu cehennemin yolunda da gelir. Allah zalimlerin toplanmasını {source:37:22} ve {ar:مِن دُونِ ٱللَّهِ فَٱهْدُوهُمْ إِلَىٰ صِرَٰطِ ٱلْجَحِيمِ, tr:min dûni'llâhi fehdûhüm ilâ sırâti'l-cahîm, gloss:Allah'tan başka taptıklarıyla birlikte onları cehennemin yoluna götürün, source:37:23} {ar:وَقِفُوهُمْ ۖ إِنَّهُم مَّسْـُٔولُونَ, tr:ve kıfûhüm innehüm mes'ûlûn, gloss:ve durdurun onları; çünkü onlar sorguya çekilecekler, source:37:24} diye emreder. Cehennem ve sorgu aynı sahnededir, ve birkaç ayet sonra onlar {ar:وَأَقْبَلَ بَعْضُهُمْ عَلَىٰ بَعْضٍۢ يَتَسَآءَلُونَ, tr:ve akbele ba'duhüm alâ ba'din yetesâelûn, gloss:birbirlerine dönüp soruşurlar, source:37:27}: sorma kökünün karşılıklı biçimi, {ar:تساءلوا أي سأل بعضهم بعضا, tr:tesâelû ey seele ba'duhüm ba'dâ, gloss:soruştular; yani birbirlerine sordular, source:"س ء ل,B004"}. Ateşin bekçileri de soru sorar: {ar:كُلَّمَآ أُلْقِىَ فِيهَا فَوْجٌۭ سَأَلَهُمْ خَزَنَتُهَآ أَلَمْ يَأْتِكُمْ نَذِيرٌۭ, tr:küllemâ ülkıye fîhâ fevcun seelehüm hazenetühâ elem ye'tiküm nezîr, gloss:oraya her topluluk atıldığında bekçileri onlara "Size bir uyarıcı gelmedi mi" diye sorar, source:67:8}. Bilmenin araçlarının kendileri de sorgulanır: {ar:إِنَّ ٱلسَّمْعَ وَٱلْبَصَرَ وَٱلْفُؤَادَ كُلُّ أُو۟لَٰٓئِكَ كَانَ عَنْهُ مَسْـُٔولًۭا, tr:inne's-sem'a ve'l-basara ve'l-fuâde küllü ülâike kâne anhü mes'ûlâ, gloss:kulak ve göz ve gönül; bunların her biri ondan sorumludur, source:17:36}. Beşinci ayetin kulak yakîni, yedinci ayetin gözü ve bilen kalp, sekizinci ayetin sorgusunun da konusudur.

Cehennemdekilere sorulan soru ve verdikleri cevap bu sorguyu sahneler: {ar:مَا سَلَكَكُمْ فِى سَقَرَ, tr:mâ selekeküm fî sekar, gloss:sizi Sekar'a ne soktu, source:74:42}. Namaz kılanlardan olmadıklarını {source:74:43}, {ar:وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ, tr:ve lem nekü nut'imü'l-miskîn, gloss:yoksulu da doyurmuyorduk, source:74:44}, {ar:وَكُنَّا نَخُوضُ مَعَ ٱلْخَآئِضِينَ, tr:ve künnâ nehûdu mea'l-hâidîn, gloss:dalıp gidenlerle birlikte biz de dalıp gidiyorduk, source:74:45}, din gününü yalanladıklarını {source:74:46} söylerler, {ar:حَتَّىٰٓ أَتَىٰنَا ٱلْيَقِينُ, tr:hattâ etâne'l-yakîn, gloss:sonunda bize yakîn geldi, source:74:47}. Sorgu verilenin paylaşılıp paylaşılmadığına uzanır; "dalıp gitmek" de başka bir kelimeyle oyalanmanın işleyişini anlatır. Malda bir hak vardır: {ar:وَٱلَّذِينَ فِىٓ أَمْوَٰلِهِمْ حَقٌّۭ مَّعْلُومٌۭ, tr:ve'llezîne fî emvâlihim hakkun ma'lûm, gloss:mallarında belirli bir hak bulunanlar, source:70:24} {ar:لِّلسَّآئِلِ وَٱلْمَحْرُومِ, tr:li's-sâili ve'l-mahrûm, gloss:isteyen ve yoksun kalan için, source:70:25}. Soran yoksul, sekizinci ayette sorgulananın karşısında durur: dünyada ondan istenmişti. Peygamber'e de {ar:وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ, tr:ve emme's-sâile fe-lâ tenher, gloss:isteyeni azarlama, source:93:10} {ar:وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ, tr:ve emmâ bi-ni'meti rabbike fe-haddis, gloss:Rabbinin nimetini anlat, source:93:11} denir: isteyen ve nimet yan yanadır.

Nimetin verilişi ve hesabın gelişi bir sahnede birleşir. Rabbi insanı sınayıp {ar:فَأَكْرَمَهُۥ وَنَعَّمَهُۥ, tr:fe-ekramehû ve na''amehû, gloss:ona ikram edip onu nimetlendirdiğinde, source:89:15} insan "Rabbim bana ikram etti" der. Allah ise yetime ikram etmediklerini {source:89:17}, yoksulu doyurmaya birbirlerini teşvik etmediklerini {source:89:18} ve {ar:وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا, tr:ve tühibbûne'l-mâle hubben cemmâ, gloss:malı aşırı bir sevgiyle seviyorsunuz, source:89:20} diye söyler; ardından cehennemin getirildiği ve insanın hatırladığı gün gelir {source:89:23}, ve insan {ar:يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى, tr:yekûlü yâ leytenî kaddemtü li-hayâtî, gloss:"Keşke hayatım için önceden bir şey gönderseydim" der, source:89:24}. Hesap kitabı da hiçbir şeyi bırakmaz: {ar:لَا يُغَادِرُ صَغِيرَةًۭ وَلَا كَبِيرَةً إِلَّآ أَحْصَىٰهَا ۚ وَوَجَدُوا۟ مَا عَمِلُوا۟ حَاضِرًۭا, tr:lâ yügâdiru sagîraten ve lâ kebîraten illâ ahsâhâ ve vecedû mâ amilû hâdırâ, gloss:küçük büyük hiçbir şey bırakmadan saymış; yaptıklarını hazır buldular, source:18:49}. "Hazır" kelimesi peşin ödemenin açıklamasındaki kelimedir. Ve sayma yön değiştirir: {ar:أَحْصَىٰهُ ٱللَّهُ وَنَسُوهُ, tr:ahsâhu'llâhü ve nesûh, gloss:Allah onu saydı; onlar ise unuttular, source:58:6}. İnsanlar çokluklarını saydı ve anmayı unuttu; Allah unuttuklarını saydı.

Bu imgenin kattığı, sekizinci ayetin sorgusunun birinci ayetin sayımına bir cevap olmasıdır: çoğaltılan şeyler bir verenin bağışıydı; onları sayan, şimdi onlar hakkında sorulan kişidir.

Kaynaklar: 102:1 أَلْهَىٰكُمُ ل ه و B003; 102:1 ٱلتَّكَاثُرُ ك ث ر B004; 102:1 ٱلتَّكَاثُرُ ك ث ر B003; 102:8 ٱلنَّعِيمِ ن ع م B001; 102:8 لَتُسْـَٔلُنَّ س ء ل B001; 102:8 لَتُسْـَٔلُنَّ س ء ل B003; 102:8 لَتُسْـَٔلُنَّ س ء ل B004; 102:7 عَيْنَ ع ي ن B011; 102:2 زُرْتُمُ ز و ر B006

## Buluşmalar

Birkaç Kur'an sahnesi bu imgelerden ikisini ya da daha fazlasını aynı anda taşır. Atların kaldırdığı tozla açılan ve mal sevgisinden kabirlere ve göğüslere uzanan sahne {source:100:10} sayı yarışını, gömülü olanın açılışını ve bilme merdivenini birlikte tutar: toz savaşın, saçılan kabirler ve ortaya dökülen göğüsler örtünün, "bilmez mi" sorusu da izden şeyin kendisine yükselen bilginin sahnesidir; ve hepsi "o gün" Rablerinin onlardan haberdar olmasıyla kapanır {source:100:11}. Ölüm anının sahnesi {source:56:95} ziyaretin konaklarını, serinlik ile sıcaklığı ve bilmenin üst basamağını bir arada tutar: nimet cenneti ve cehennem birer ağırlama olarak sunulur, ve hepsine kesin bilginin hakkı denir. Cennet halkından birinin cehennemin ortasındaki arkadaşını gördüğü sahne {source:37:55} göz imgesini sorgu imgesiyle birleştirir: sahne karşılıklı bir soruşmayla açılır {source:37:50}, cehennem nimetin içinden görülür, ve konuşan kurtuluşunu nimetin adıyla anar {source:37:57}. Mal toplayıp sayanın Hutame'ye atıldığı sahne {source:104:4} değirmen ağzını sayı yarışıyla birleştirir: sayılan yığın, kırıp parçalayan bir ateşe döner. Cehennemdekilere "sizi Sekar'a ne soktu" diye sorulan sahne {source:74:47} sorguyu bilme merdiveniyle birleştirir: sorguya verilen cevap ölümün adını yakîn koyar. Cehennemin kâfirlere sunulduğu sahne {source:18:101} göz imgesini oyalanmayla birleştirir: anmaya karşı örtülü gözler, o gün sunulanı görür. Ve cehennemin getirildiği gün {source:89:23} oyalanmayı hesapla birleştirir: oyalanmanın düşürdüğü anma, nimetin ve mal sevgisinin hesabıyla birlikte geri gelir.

Kelimelerin kendisinde de buluşmalar vardır. Oyalanmayı anlatan "meşgul etmek" fiili değirmenin yemini de anlatır; yüz çevirten oyalanma ile doymayan değirmen tek bir kelimenin iki yüzüdür, ve aynı kelimenin ailesi bağışı da adlandırdığı için değirmene atılan avuç, sonunda hakkında sorulacak bir armağandır. Yedinci ayetin göz kelimesi aynı anda yüz yüze gelmeyi, merdivenin tepesini, sayılan altını, akan pınarı ve peşin ödemeyi adlandırır; bu yüzden yedinci ayet imgelerin çoğunun düğümlendiği yerdir. Sekizinci ayetin nimet kelimesi sayılan develeri, varılıp kalınan yurdu, nemli rüzgârı, gözün serinliğini ve bir verenin bağışını taşır; sorgunun konusu birinci ayetin sayılan nesneleridir. Altıncı ayetin cehennemi çukurdaki doymayan ateş, savaşın en sıcak anı, alev alev bakan göz ve çok sıcak bir varış yeridir. İkinci ayetin iki kelimesi ise yol ile örtüyü birleştirir: ziyaret fiili sapmayı, ziyareti ve göğsü, kabir kelimesi konağı ve örtüyü taşır.

Bu buluşmalar surenin hareketini taşır. Birinci ayette insan bir şeyle tutulur, yüzünü kendisini ilgilendirenden çevirir, çokluğunu başkalarına karşı sayar ve gösterir; değirmen beslendikçe döner. İkinci ayette bu yol kabirlerde biter, ama kabir bir ziyarettir ve bir örtüdür: geçilen bir konak ve içindekini bir gün gösterecek bir kın. Üçüncü ayetten yedinci ayete kadar bilgi izden kesinliğe, kesinlikten göze yükselir; bu yükselişte gösteren seyirci olur, yüz çeviren yüz yüze getirilir, örtü kalkar ve görülen ateş de geri bakar. Sekizinci ayette sayılan şeyler bir verenin bağışı ve ateşin karşısındaki serinlik olarak adlandırılır, ve sayan, sorulan olur.

