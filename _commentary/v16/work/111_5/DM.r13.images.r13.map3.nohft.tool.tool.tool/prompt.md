Focus: 111:5. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/111_5/D.r13/context.md =====
# 111:5 — focus

فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ

Anchor translation (canonical reading, reference only):

Boynunda liften bir ip vardır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فِى | فِى |  | P |
| 2 | جِيدِهَا | جِيد | ج ي د | N;PRON |
| 3 | حَبْلٌ | حَبْل | ح ب ل | N |
| 4 | مِّن | مِن |  | P |
| 5 | مَّسَدٍۭ | مَّسَد | م س د | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 111 — full text (context; no pericope)

- 111:1 تَبَّتْ يَدَآ أَبِى لَهَبٍۢ وَتَبَّ
- 111:2 مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ
- 111:3 سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ
- 111:4 وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ
- 111:5 ◀ focus فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ


===== _commentary/v16/work/111_5/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ج ي د (root_000284) — identity root of جِيدِهَا (w2)

- **B001** boyun; boynun önü, uzunluğu ve güzelliği — boyun veya boynun ön kısmı · boyun uzunluğu · boyunlar · uzun boyunlu veya güzel boyunlu erkek · uzun ya da güzel boyunlu kadın · güzel boyunlu kadın · boynu güzel kadın
  الجيم والياء والدال أصل واحد وهو العنق (maqayis)؛ الجيد مقدم العنق (ayn)؛ الجيد العنق (jamhara)؛ الجيد طول الجيد والجيداء الطويلة الجيد (maqayis)؛ رجل أجيد وامرأة جيداء حسنة الجيد إذا كانت طويلة العنق (jamhara)؛ امرأة جيدانة حسنة الجيد (ayn)

## ح ب ل (root_000291) — identity root of حَبْلٌ (w3)

- **B001** bağlama ve yedme ipi — ip veya yular · ağaca çıkma ipi · ip · ip gibi örülmüş ya da kıvrılmış saç
  الحبل الرسن (ayn;tahdhib)؛ الحبل معروف (jamhara;mufradat)؛ الحبل الرسن معروف والجمع حبال (maqayis)؛ الحابول الكر الذي يصعد به إلى النخل (jamhara;sihah)؛ المحبل الحبل (tahdhib)؛ محبل الشعر كأن كل قرن من قرون رأسه حبل (tahdhib)
- **B002** bağlayıcı söz ve güvence — söz, güvence ve bağlılık bağı · birinden koruma sözü almak · Tanrı'ya yönelten ve birlik sağlayan dayanak · Tanrı'dan ve insanlardan gelen söz ve güvence
  الحبل العهد والأمان والحبل التواصل (ayn)؛ الحبل العهد والحبل الأمان وأخذت بحبل من فلان أي عهدا وأمانا (jamhara)؛ الحبل العهد والأمان وهو مثل الجوار والحبل الوصال (sihah)؛ الحبل العهد والأمان والحبل التواصل والعهد والذمة (tahdhib)؛ استعير للوصل ولكل ما يتوصل به إلى شيء ويقال للعهد حبل (mufradat)؛ المحمول عليه الحبل وهو العهد ويريد الأمان وعهود الخفارة (maqayis)
- **B003** uzun kum sırtı — uzun ve yüksek kum sırtı
  الحبل الرمل الطويل الضخم (ayn)؛ يقال للرمل يستطيل حبل (sihah)؛ الحبل من الرمل المجتمع الكثير العالي والحبل رمل يستطيل ويمتد (tahdhib)؛ الحبل المستطيل من الرمل (mufradat)؛ الحبل القطعة من الرمل يستطيل (maqayis)
- **B004** ip biçimli damar veya bağ — omuz ile kol arasındaki sinir veya bağ · boyundaki ana damar · koldaki damar · yakınında, kolayca elinin altında · atın bacak damarları · atın veya başka bir binek hayvanının bileği
  حبل العاتق وصلة ما بين العاتق والمنكب وحبل الوريد عرق (ayn;tahdhib)؛ حبل الذراع معروف وهذا الأمر على حبل ذراعك أي ممكن لك (jamhara)؛ حبل الوريد عرق في العنق وحبل الذراع في اليد وهو على حبل ذراعك أي في القرب منك (sihah)؛ حبال الفرس عروق قوائمه والمحتبل رسغها (tahdhib)؛ شبه به من حيث الهيئة حبل الوريد وحبل العاتق (mufradat)؛ الحبل حبل العاتق ومحتبله أرساغه (maqayis)
- **B005** avı yakalayan ipli tuzak — avı tuzak kurarak yakalamak · avı ipli tuzakla yakalamak · ipli av tuzağı · av tuzağını kuran kişi · tuzağa yakalanmış av · ölüme götüren tuzaklar ve nedenler · kötülüğe sürükleyen ayartma tuzakları · ortalığın karışması veya her yandan korku gelmesi
  الحبل مصدر حبلت الصيد واحتبلته أي أخذته والحبالة المصيدة وحبائل الموت أسبابه (ayn)؛ الحبالة شرك الصائد والصيد محبول ومحتبل إذا وقع في الحبالة وأنا بين حابل ونابل (jamhara)؛ الحبالة التي يصاد بها والحابل الذي ينصب الحبالة والمحبول الوحشي الذي نشب في الحبالة واحتبله أي اصطاده بالحبالة واختلط الحابل بالنابل (sihah)؛ الحبل مصدر حبلت الصيد واحتبلته إذا نصبت له حبالة فنشب فيها والحبالة المصيدة وثار حابلهم على نابلهم (tahdhib)؛ الحبالة خصت بحبل الصائد والنساء حبائل الشيطان والمحتبل والحابل صاحب الحبالة (mufradat)؛ الحبالة حبالة الصائد واحتبل الصيد إذا صاده بالحبالة (maqayis)
- **B006** gebelik ve karındaki yavru — gebelik veya karındaki yavru · kadın gebe kaldı · gebe dişi · karındaki yavrunun ilerideki yavrusu · gebeliğin başladığı zaman veya yer · yavrunun rahimde yerleştiği bölüm
  حبلت المرأة حبلا فهي حبلى وحبل الحبلة ولد الولد الذي في البطن (ayn)؛ حبلت من الإنس وغيرهم وربما سمي ما في البطن بعينه حبلا والمحبل وقت الحبل وحبل الحبلة ما يكون في بطن الناقة التي هي في بطن أمها (jamhara)؛ الحبل الحمل وقد حبلت المرأة فهي حبلى وحبل الحبلة نتاج النتاج وولد الجنين وكان ذلك في محبل فلان أي في وقت حبل أمه به (sihah)؛ حبلت المرأة تحبل حبلا وهي حبلى وحبل الحبلة ولد الولد الذي في البطن والمحبل موضع الحبل (tahdhib)؛ الحبل وهو الحمل وذلك أن الأيام تمتد به (maqayis)؛ المهبل مستقر الولد من الرحم وهو من باب الإبدال وأصله محبل (maqayis)
- **B007** asma sürgünü ve bitkisel adlar — asma veya asma sürgünü · dikenli ağaçların meyvesi · bölgesel dilde fasulye · bu bitkiyi otlayan kertenkele
  الحبلة طاقة من قضبان الكرم والحبل نوع من الشجر مثل السمر (ayn)؛ الحبلة الكرم والأحبل الذي يسمى اللوبياء لغة يمانية (jamhara)؛ الحبلة ثمر العضاه والحبلة القضيب من الكرم وضب حابل يرعى الحبلة (sihah)؛ الكرمة حبلة والحبلة طاق من قضبان الكرم والحبلة ثمر السمر وثمر العضاه والأحبل اللوبياء (tahdhib)؛ الكرم يقال له حبلة وحبلة لأنه في نباته كالأرشية والحبلة ثمر العضاة (maqayis)
- **B008** kolyeye takılan süs parçası — kolyeye takılan süs parçası
  الحبلة ضرب يصاغ من الحلي (jamhara)؛ الحبلة أيضا حلى يجعل في القلائد وقلائد من حبلة وسلوس (sihah)؛ الحبلة حلي كان يجعل في القلائد في الجاهلية وقلائد من حبلة وسلوس (tahdhib)؛ الحبلة اسم لما يجعل في القلادة (mufradat)؛ الحبلة حلي يجعل في القلائد ولعله مشبه بثمره (maqayis)
- **B009** yer adı ve at yarışı başlangıç alanı — kaynaklarda adı verilen belirli bir yer · bir kentteki yarış alanının başlangıç bölümü · atların yarıştan önce beklediği başlangıç yeri
  الحبل موضع بالبصرة على شاطىء النهر (ayn)؛ الحبل موضع والحبل موقف خيل الحلبة قبل أن تطلق وبه سمي حبل البصرة (jamhara)؛ حبل موضع في شعر لبيد (tahdhib)
- **B010** biçime bağlı adlandırmalar — belirli bir topluluğa mensup · kaynaklarda adı verilen bir topluluk · bir erkek adı
  فلان الحبلي منسوب إلى حي من اليمن (ayn)؛ بنو الحبلى بطن من العرب (jamhara)؛ حبال اسم رجل (sihah)؛ الحبلي منسوب إلى حي من اليمن وبنو الحبلى من الأنصار وحبلوي وحبلي وحبلاوي (tahdhib)
- **B011** ağır bela — ağır bela veya çıkmaza düşüren olay · bilgili, uyanık ve keskin kavrayışlı adam
  الحبل الداهية والجمع حبول (jamhara)؛ الحبل بالكسر الداهية والجمع الحبول (sihah)؛ الحبل الرجل العالم الفطن الداهي والحبل الداهية وجمعه حبول (tahdhib)؛ الحبل بكسر الحاء وهي الداهية ووجهه أن الإنسان إذا دهي فكأنه قد حبل أي وقع في الحبالة (maqayis)
- **B012** yerinden kaçmayan cesur kişi — yerinde duran, kaçmayan cesur kişi; aslan · ölüm için kullanılan kalıplaşmış niteleme
  رجل حبيل براح إذا كان شجاعا ويسمى به الأسد أيضا (jamhara)؛ يقال للواقف مكانه كالأسد لا يفر حبيل براح (sihah)؛ يقال للموت حبيل براح (tahdhib)؛ للواقف مكانه لا يفر حبيل براح كأنه محبول وزعم ناس أن الأسد يقال له حبيل براح (maqayis)
- **B013** yalıtık adlandırmalar — geniş veya dar yaradılışlı · öfke, su veya içkiyle dolmuş · ağırlık · içecekten kaynaklanan karın şişliği
  واسع الحبل وضيق الحبل كضيق الخلق وواسع الخلق ورجل حبلان إذا امتلأ غيظا ورجل حبلان من الماء والشراب إذا امتلأ ريا والحبل الثقل والحبال انتفاخ البطن من الشراب والنبيذ ورجل حبلان وامرأة حبلانة وفلان حبلان على فلان أي غضبان وبه حبل أي غضب وغم (tahdhib)
- **B014** o sırada [kalıp] — o sırada, o vakit
  أتيته على حبالة ذاك أي على حين ذاك (tahdhib)
- **B015** yazılı kayıt; başka yoruma göre gebelik başlangıcı — yazılı kayıt; başka yoruma göre gebeliğin yeri veya başlangıcı
  المحبل الكتاب فمن كسر الباء عنى به الكتاب ومن لم يكسر الباء فإنه يريد وأمه حبلى (jamhara)؛ خط له ذلك في المحبل أي كتب له الموت حين حبلت به أمه والمحبل موضع الحبل (tahdhib)

## م س د (root_001422) — identity root of مَّسَدٍۭ (w5)

- **B001** bükülü lif veya ip; ipi ustaca bükme — hurma lifi veya yaprağından, deve tüyünden ya da derisinden yapılmış lif veya ip · ipi sağlam ve düzgün biçimde bükmek · bükülü lifsi malzemeden yapılmış ip · iyi bükülmüş ip
  أصل صحيح يدل على جدل شيء وطية (maqayis)؛ المسد ليف يتخذ من جريد النخل (maqayis;ayn;mufradat)؛ المسد حبل يتخذ من أوبار الإبل (maqayis;tahdhib)؛ حبل من ليف أو خوص وقد يكون من جلود الإبل أو من أوبارها (sihah;tahdhib)؛ مسدت الحبل أي أجدت فتله (sihah;tahdhib)
- **B002** ip gibi sıkı ve düzgün beden; eti sıkılaştırma — ip gibi sıkı, ince ve düzgün yapılı · beden yapısı güzel ve sıkı · üst etini sıkılaştırıp güçlendirmek
  امرأة ممسودة مجدولة الخلق كالحبل الممسود (maqayis;mufradat)؛ جارية ممسودة مطوية ممشوقة (ayn;tahdhib)؛ رجل ممسود أي مجدول الخلق (sihah;tahdhib)؛ يمسد أعلى لحمه ويأرمه أي يشده (sihah;tahdhib)
- **B003** gece boyunca durmadan ve güçlüğe göğüs gererek yol alma — gece boyunca durmadan ve güçlüğe katlanarak yol alma
  المسد إدآب السير في الليل (ayn;sihah;tahdhib)؛ يكابد الليل عليها مسدا (ayn;tahdhib)؛ جعل الليث الدأب مسدا لأنه يمسد خلق من يدأب فيطويه ويضمره (tahdhib)
- **B004** yağ veya bal tulumu — yağ veya bal konan deri tulum
  المساد نحي السمن أو العسل (ayn)؛ المساد لغة في المساب وهو نحي السمن وسقاء العسل (sihah)؛ المساد نحي يجعل فيه سمن وعسل (tahdhib)
- **B005** demir mil — demirden yapılmış mil veya eksen
  المسد المحور إذا كان من حديد (ayn)
- **B006** siyah ince deri — siyah ince deri
  المساد الرق الأسود (tahdhib)
- **B007** saçın düzgün yapısı ve güzel görünüşü [kalıp] — saçın düzgün yapısı ve güzel görünüşü
  فلان أحسن مساد شعر من فلان يريد أحسن قوام شعر (tahdhib)

===== _commentary/v16/out/s111/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 111:5, and ## Buluşmalar) =====
## Ev ocağı ve soy: tersine dönen hane

Bir ev; ailesi için kazanan bir erkek, bir eş, evlenmede ya da ev kurulurken verilen bir ziyafet, ev için toplanan odun ve et kızartılan, başında ısınılan bir ocakla döner. Surenin kelimeleri bu ev sahnesinin bütün parçalarını kökleriyle taşır. Kazanmak, ailesi için hayır kazanmaktır: {ar:فلان يكسب أهله خيرا, tr:fulânun yeksibu ehlehû hayran, gloss:falanca ailesine hayır kazandırır, source:"ك س ب,B002"}. Baba, besleyendir: {ar:فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده, tr:fulânun ye'bû hâze'l-yetîme ibâveten, ey yağzûhu kemâ yağzu'l-vâlidu veledeh, gloss:falanca bu yetime babalık eder, yani babanın çocuğunu beslediği gibi onu besler, source:"ء ب و,B001"}. Dördüncü ayetin ilk kelimesi eştir, {ar:هي امرأته, tr:hiye'mraetuh, gloss:o, onun karısıdır, source:"م ر ء,B001"}, ve kökü evin kuruluşundaki ziyafeti adlandırır: {ar:والمرء : الإطعام على بناء دار ، أو تزويج, tr:ve'l-mer'u el-it'âmu alâ binâi dârin ev tezvîc, gloss:mer', ev yapımında ya da evlenmede yemek vermektir, source:"م ر ء,B004"}. İkinci ayetin fiilinin kökü evliliği de adlandırır, {ar:الغنى التزويج, tr:el-ğınâ et-tezvîc, gloss:ğınâ, evlendirmedir, source:"غ ن ي,B006"}, ve kocasıyla yetinen kadını: {ar:الغانية المستغنية بزوجها عن الزينة, tr:el-ğâniye el-mustağniye bi-zevcihâ ani'z-zîne, gloss:ğâniye, kocası sayesinde süse ihtiyaç duymayan kadındır, source:"غ ن ي,B005"}. Odun kökü birisi için odun toplamayı bilir, {ar:حطبت فلانا إذا احتطبت له, tr:hatabtu fulânen izehtatabtu leh, gloss:falancaya odun topladım, source:"ح ط ب,B001"}, ve üçüncü ayetin fiili ocağın kendisidir: ısınılan ve kızartılan ateş {source:"ص ل ي,B004"}.

Surede bu ev bütünüyle tersine döner. Kazanan erkeğin kazancı kendine bile yetmez; ikinci ayetin fiili, kocası karısına yeten evliliğin kökünden gelir ama burada koca kendini bile karşılayamaz. Eş, kocasının içinde yanacağı ateşe odun taşır; ev ocağı Ateş olur. Bu ters çevrilmenin karşı sahnesi Kur'an'da Mûsâ'dadır. Süresini doldurup ailesiyle yola çıkan Mûsâ, Tûr'un yanında bir ateş görür ve ailesine şöyle der: {ar:لَعَلِّىٓ ءَاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ جَذْوَةٍۢ مِّنَ ٱلنَّارِ لَعَلَّكُمْ تَصْطَلُونَ, tr:lealî âtîkum minhâ bi-haberin ev cezvetin mine'n-nâri lealekum tastalûn, gloss:belki oradan size bir haber ya da bir ateş koru getiririm, belki ısınırsınız, source:28:29}; aynı söz başka bir yerde {ar:بِشِهَابٍۢ قَبَسٍۢ, tr:bi-şihâbin kabes, gloss:alınmış bir ateş parçasıyla, source:27:7} diye geçer {source:20:10}. Orada "ısınmak" fiili surenin "yanmak" fiiliyle aynı köktendir: bir koca ailesini ısıtmak için ateş getirir; burada bir eş, kocasının yanacağı ateşe odun taşır. Müminlere hitap eden ayet, insanın kendini ve ailesini yakıtı insanlar olan bir ateşten korumasını ister: {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا, tr:kû enfusekum ve ehlîkum nârâ, gloss:kendinizi ve ailenizi bir ateşten koruyun, source:66:6}. Kitabı arkasından verilen kişi için {source:84:10} yanmak, ailesi içindeki eski sevincin karşısına konur: {ar:وَيَصْلَىٰ سَعِيرًا إِنَّهُۥ كَانَ فِىٓ أَهْلِهِۦ مَسْرُورًا, tr:ve yaslâ seîran innehû kâne fî ehlihî mesrûrâ, gloss:alevli ateşe girer; çünkü o ailesi içinde sevinçliydi, source:84:12}. Allah'ın inkâr edenlere örnek verdiği Nûh'un ve Lût'un karılarında eş, fayda vermeme fiili ve Ateş bir araya gelir: {ar:فَلَمْ يُغْنِيَا عَنْهُمَا مِنَ ٱللَّهِ شَيْـًۭٔا وَقِيلَ ٱدْخُلَا ٱلنَّارَ مَعَ ٱلدَّٰخِلِينَ, tr:felem yuğniyâ anhumâ mina'llâhi şey'en ve kîle'dhulâ'n-nâra mea'd-dâhilîn, gloss:kocaları onlara Allah'a karşı hiçbir fayda vermedi ve onlara "girenlerle birlikte ateşe girin" denildi, source:66:10}. Hemen ardından Firavun'un karısı, kocasından ve onun işinden kurtarılmayı dileyen bir eş olarak gelir {source:66:11}: evlilik orada kaderi paylaştırmaz. Surede ise eş ve koca aynı ateşin iki ucundadır.

Dördüncü ve beşinci ayetin iki kelimesi bu evin bir başka parçasını, soyu da işitir. Taşımak, kökünde hamileliktir: {ar:حملت المرأة حبلت, tr:hamelet'il-mer'etu hebilet, gloss:kadın gebe kaldı, source:"ح م ل,B002"}, {ar:الحمل ما كان في بطن, tr:el-hamlu mâ kâne fî batn, gloss:haml, karında olandır, source:"ح م ل,B002"}. İp de kökünde aynı şeydir: {ar:الحبل الحمل وقد حبلت المرأة فهي حبلى, tr:el-habelu el-hamlu ve kad hebileti'l-mer'etu fe-hiye hublâ, gloss:habel gebeliktir; kadın gebe kaldı, o hâmiledir, source:"ح ب ل,B006"}. Bir tanım, iki kelimeyi birbiriyle açıklar ve gebeliğin ipe benzerliğini günlerin onunla uzamasında görür: {ar:الحبل وهو الحمل وذلك أن الأيام تمتد به, tr:el-habelu ve huve'l-hamlu ve zâlike enne'l-eyyâme temteddu bih, gloss:habel gebeliktir, çünkü günler onunla uzar, source:"ح ب ل,B006"}. Kadının iki ayetindeki iki kelime, onun taşıyacağı soyun kelimeleridir; oysa sahnede taşıdığı odun, boynundaki iptir. Birinci ayetin baba kelimesi bu soyun öbür ucunu tutar {source:"ء ب و,B001"}. Kur'an, ikinci ayetin cümlesini başka yerlerde malın yanına evladı koyarak kurar: {ar:مَن لَّمْ يَزِدْهُ مَالُهُۥ وَوَلَدُهُۥٓ إِلَّا خَسَارًۭا, tr:men lem yezidhu mâluhû ve veleduhû illâ hasârâ, gloss:malı ve evladı kendisine kayıptan başka bir şey katmayan, source:71:21}. Bu, Nûh'un kavminin kendisine isyan edip izledikleri önderlerden yakınmasıdır; "kayıp" kelimesi de tebâbın tanımında geçen kelimedir. İbrâhîm'in duasında o gün {ar:يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ, tr:yevme lâ yenfau mâlun ve lâ benûn, gloss:ne malın ne oğulların fayda vereceği gün, source:26:88} diye anılır. Mal ile evladın onlara fayda vermediği ve onların ateşin ehli olduğu ayette {source:58:17} ve yukarıda geçen ayette {source:3:10} bu ikili ikinci ve üçüncü ayetin sırasını kurar. Surede ikinci sırada "kazandığı" durur; o yerde evladı duymak bir okumadır, kelimenin söylediği değil. Suçlunun o gün kurtulmak için fidye olarak vermek isteyeceği şeyler de bu evin halkıdır: {ar:بِبَنِيهِ وَصَٰحِبَتِهِۦ وَأَخِيهِ, tr:bi-benîhi ve sâhibetihî ve ehîh, gloss:oğulları, eşi ve kardeşiyle, source:70:12}.

Kaynaklar: 111:1 أَبِى ء ب و B001; 111:2 كَسَبَ ك س ب B002; 111:2 أَغْنَىٰ غ ن ي B006; 111:2 أَغْنَىٰ غ ن ي B005; 111:3 سَيَصْلَىٰ ص ل ي B004; 111:4 وَٱمْرَأَتُهُۥ م ر ء B001; 111:4 وَٱمْرَأَتُهُۥ م ر ء B004; 111:4 ٱلْحَطَبِ ح ط ب B001; 111:4 حَمَّالَةَ ح م ل B002; 111:5 حَبْلٌۭ ح ب ل B006

## Sırttaki yük: yük hayvanı, yular, vebal

Sırtında odun, boynunda hurma lifinden bir ip: dördüncü ve beşinci ayetin kelimeleri kökleriyle bir yük hayvanı sahnesi kurar. Taşımanın temel yeri sırttır {source:"ح م ل,B001"}; aynı kök yük taşıyan develeri adlandırır: {ar:الحمولة الإبل تحمل عليها الأثقال, tr:el-hamûle el-ibilu tuhmelu aleyhe'l-eskâl, gloss:hamûle, üzerine ağırlık yüklenen develerdir, source:"ح م ل,B006"}. Kök zorlanarak taşımayı da bilir: {ar:تحاملت إذا تكلفت الشيء على مشقة, tr:tehâmeltu izâ tekellefte'ş-şey'e alâ meşakka, gloss:bir şeyi zahmetle üstlendim, source:"ح م ل,B007"}. Odun kökünden kuru diken otlayan dişi deve adını alır: {ar:ناقة محاطبة تأكل الشوك اليابس, tr:nâkatun muhâtıbe te'kulu'ş-şevke'l-yâbis, gloss:kuru diken yiyen dişi deve, source:"ح ط ب,B001"}. Beşinci ayetin ipi bir yulardır: {ar:الحبل الرسن, tr:el-hablu er-resen, gloss:ip, yulardır, source:"ح ب ل,B001"}. İpin maddesi de bu dünyadan gelir; mesed, deve yününden ya da hurma lifinden bükülmüş kaba iş ipidir: {ar:المسد حبل يتخذ من أوبار الإبل, tr:el-mesedu hablun yuttehazu min evbâri'l-ibil, gloss:mesed, deve yününden yapılan iptir, source:"م س د,B001"}, {ar:حبل من ليف أو خوص, tr:hablun min lîfin ev havs, gloss:lif ya da hurma yaprağından ip, source:"م س د,B001"}. Birinci ayetin fiili bile yük hayvanını bilir; sırtı yara olmuş eşek ya da deve onunla anılır: {ar:حمار تاب الظهر إذا دبر, tr:himârun tâbbu'z-zahri izâ debir, gloss:sırtı yağır olmuş eşek, source:"ت ب ب,B003"}.

Taşınan yük bir de vebaldir: {ar:من باء بالإثم يسمى حاملا للإثم, tr:men bâe bi'l-ismi yusemmâ hâmilen li'l-ism, gloss:günahı yüklenen kişiye günah taşıyan denir, source:"ح م ل,B003"}. Kur'an bu yükü sırta koyar. Allah ile karşılaşmayı yalanlayanlar, Saat ansızın geldiğinde hasretle bağırırken {ar:وَهُمْ يَحْمِلُونَ أَوْزَارَهُمْ عَلَىٰ ظُهُورِهِمْ, tr:ve hum yahmilûne evzârahum alâ zuhûrihim, gloss:onlar günah yüklerini sırtlarında taşırlar, source:6:31}; aynı ayet {ar:قَدْ خَسِرَ, tr:kad hasira, gloss:kaybetti, source:6:31} diye açılır, yani tebâbın tanımındaki kayıpla. Zikirden yüz çeviren kıyamet günü bir vebal taşır {source:20:100} ve {ar:وَسَآءَ لَهُمْ يَوْمَ ٱلْقِيَٰمَةِ حِمْلًۭا, tr:ve sâe lehum yevme'l-kıyâmeti himlâ, gloss:kıyamet günü onlar için ne kötü bir yüktür, source:20:101}. Başkalarını yoldan çıkaranlar kendi yükleriyle birlikte saptırdıklarının yükünü de taşır {source:16:25}: {ar:وَلَيَحْمِلُنَّ أَثْقَالَهُمْ وَأَثْقَالًۭا مَّعَ أَثْقَالِهِمْ, tr:ve le-yahmilunne eskâlehum ve eskâlen mea eskâlihim, gloss:kendi ağırlıklarını ve kendi ağırlıklarıyla birlikte başka ağırlıkları da mutlaka taşıyacaklar, source:29:13}. Yükün paylaşılmazlığı ise dişil bir yüklüyle söylenir: {ar:وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ, tr:ve in ted'u muskaletun ilâ himlihâ lâ yuhmel minhu şey'un ve lev kâne zâ kurbâ, gloss:yükü ağır bir kişi yüküne yardım için çağırsa, yakını bile olsa ondan hiçbir şey taşınmaz, source:35:18}. Kazanç ile yük bir ayette yan yana durur: {ar:وَلَا تَكْسِبُ كُلُّ نَفْسٍ إِلَّا عَلَيْهَا ۚ وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ, tr:ve lâ teksibu kullu nefsin illâ aleyhâ, ve lâ teziru vâziratun vizra uhrâ, gloss:her kişinin kazandığı yalnız kendi aleyhinedir; hiçbir yük taşıyan başkasının yükünü taşımaz, source:6:164}. Kadın sırtında yükünü taşır, kocası onun yükünü almaz, o da kocasınınkini.

Kaynaklar: 111:4 حَمَّالَةَ ح م ل B001; 111:4 حَمَّالَةَ ح م ل B006; 111:4 حَمَّالَةَ ح م ل B003; 111:4 حَمَّالَةَ ح م ل B007; 111:4 ٱلْحَطَبِ ح ط ب B001; 111:5 حَبْلٌۭ ح ب ل B001; 111:5 مَّسَدٍۭ م س د B001; 111:1 تَبَّتْ ت ب ب B003

## Boyundaki ip: gerdanlıktan tasmaya

Beşinci ayet ipi boynun belirli bir yerine koyar: {ar:فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ, tr:fî cîdihâ hablun min mesed, gloss:boynunda bükülmüş liften bir ip, source:111:5}. Cîd, boynun ön yüzüdür, {ar:الجيد مقدم العنق, tr:el-cîdu mukaddemu'l-unuk, gloss:cîd, boynun önüdür, source:"ج ي د,B001"}, ve övgüyle anılan, uzunluğu ve güzelliği söylenen boyundur: {ar:امرأة جيداء حسنة الجيد إذا كانت طويلة العنق, tr:imraetun caydâu haseneti'l-cîdi izâ kânet tavîlete'l-unuk, gloss:boynu uzun olan kadına "güzel boyunlu" denir, source:"ج ي د,B001"}. Bu, gerdanlığın takıldığı yerdir. İp kökü de gerdanlıktaki bir süs taşını adlandırır: {ar:الحبلة حلي يجعل في القلائد, tr:el-hablatu huliyyun yuc'alu fi'l-kalâid, gloss:habla, gerdanlıklara takılan bir süstür, source:"ح ب ل,B008"}. Süsün kelimesi burada kaba bir ip olarak görünür. Kocası ya da güzelliği sayesinde süse ihtiyaç duymayan kadının adı ikinci ayetin fiilinin kökündendir {source:"غ ن ي,B005"}; surede süse ihtiyaç duymaması gereken boyun bir ip taşır.

Mesed sıkı bükülmüş iptir: {ar:مسدت الحبل أي أجدت فتله, tr:mesedtu'l-habl, ey eceddu fetlehu, gloss:ipi mesedledim, yani iyice büktüm, source:"م س د,B001"}. Aynı kök, sıkı yapılı bir kadının bedenini de bu iple anar: {ar:امرأة ممسودة مجدولة الخلق كالحبل الممسود, tr:imraetun memsûdetun meclûdetu'l-halki ke'l-habli'l-memsûd, gloss:bükülmüş ip gibi sıkı yapılı kadın, source:"م س د,B002"}. Kadın ile boynundaki ip tek bir kelimeyi paylaşır. Kök demirden bir mili de bilir: {ar:المسد المحور إذا كان من حديد, tr:el-mesedu el-mihveru izâ kâne min hadîd, gloss:mesed, demirden olduğunda mil, source:"م س د,B005"}. Kelime liften demire uzanır. İpin boyunda yaptığı iş de kökte kayıtlıdır: yular hayvanı yerinde tutar ve götürür {source:"ح ب ل,B001"}, ve bağlanmış gibi yerinden ayrılamayan kişi ipin adıyla anılır, ölüm de bu adı alır: {ar:للواقف مكانه لا يفر حبيل براح كأنه محبول, tr:li'l-vâkıfi mekânehû lâ yefirru habîlu berâh, keennehû mahbûl, gloss:yerinde durup kaçmayana "habîlu berâh" denir, sanki bağlanmıştır, source:"ح ب ل,B012"}. İpin altında boynun kendi ipi vardır: {ar:حبل الوريد عرق في العنق, tr:hablu'l-verîd ırkun fi'l-unuk, gloss:şah damarı boyundaki bir damardır, source:"ح ب ل,B004"}. Kur'an bu ipi Allah'ın yakınlığının ölçüsü yapar: {ar:وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ, tr:ve nahnu akrabu ileyhi min habli'l-verîd, gloss:biz ona şah damarından daha yakınız, source:50:16}.

Kur'an'da boyuna konan şey, insanın sahip olduğunun ya da yaptığının boyuna dönüşmüş hâlidir. Cimriler için: {ar:سَيُطَوَّقُونَ مَا بَخِلُوا۟ بِهِۦ يَوْمَ ٱلْقِيَٰمَةِ, tr:se-yutavvakûne mâ bahilû bihî yevme'l-kıyâme, gloss:cimrilik ettikleri şey kıyamet günü boyunlarına dolanacak, source:3:180}; esirgenen mal bir boyun halkası olur ve gelecek eki üçüncü ayetin fiilindekiyle aynıdır. Allah'ın talimatı eli boyna bağlar: {ar:وَلَا تَجْعَلْ يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:ve lâ tec'al yedeke mağlûleten ilâ unukik, gloss:elini boynuna bağlı kılma, source:17:29}. Her insanın payı boynuna bağlanır: {ar:وَكُلَّ إِنسَٰنٍ أَلْزَمْنَٰهُ طَٰٓئِرَهُۥ فِى عُنُقِهِۦ, tr:ve kulle insânin elzemnâhu tâirahû fî unukıh, gloss:her insanın amelini boynuna bağladık, source:17:13}. Yeniden dirilişi inkâr edenler hakkında {ar:وَأُو۟لَٰٓئِكَ ٱلْأَغْلَٰلُ فِىٓ أَعْنَاقِهِمْ, tr:ve ulâike'l-ağlâlu fî a'nâkıhim, gloss:işte boyunlarında halkalar olanlar onlardır, source:13:5} denir; halka çeneye kadar çıkar ve başı yukarı kaldırır {source:36:8}. Sürüklenme sahnesi halka ile zinciri birlikte gösterir: {ar:إِذِ ٱلْأَغْلَٰلُ فِىٓ أَعْنَٰقِهِمْ وَٱلسَّلَٰسِلُ يُسْحَبُونَ, tr:izi'l-ağlâlu fî a'nâkıhim ve's-selâsilu yushabûn, gloss:boyunlarında halkalar ve zincirlerle sürüklenirken, source:40:71}. Kitabı sol eline verilen kişinin sahnesinde {source:69:25} bağlama ile yakma aynı sırada gelir: {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe-ğullûh, gloss:tutun onu, boynuna halka geçirin, source:69:30}, {ar:ثُمَّ ٱلْجَحِيمَ صَلُّوهُ, tr:summe'l-cahîme sallûh, gloss:sonra onu cehenneme sokup yakın, source:69:31}, {ar:ثُمَّ فِى سِلْسِلَةٍۢ ذَرْعُهَا سَبْعُونَ ذِرَاعًۭا فَٱسْلُكُوهُ, tr:summe fî silsiletin zer'uhâ seb'ûne zirâan feslukûh, gloss:sonra onu yetmiş arşınlık bir zincire geçirin, source:69:32}. Ateş ile bağın yan yana durduğu öbür yerler de vardır: {ar:سَلَٰسِلَا۟ وَأَغْلَٰلًۭا وَسَعِيرًا, tr:selâsile ve ağlâlen ve seîrâ, gloss:zincirler, halkalar ve alevli ateş, source:76:4}; {ar:إِنَّ لَدَيْنَآ أَنكَالًۭا وَجَحِيمًۭا, tr:inne ledeynâ enkâlen ve cahîmâ, gloss:bizim katımızda ağır bukağılar ve cehennem var, source:73:12}. Surede de ateş üçüncü ayette, ip beşinci ayettedir. Boynun karşı sahnesi de Kur'an'dadır: sarp yokuşun ilk adımı {ar:فَكُّ رَقَبَةٍ, tr:fekku rakabe, gloss:bir boynu çözmek, source:90:13}.

Kaynaklar: 111:5 جِيدِهَا ج ي د B001; 111:5 حَبْلٌۭ ح ب ل B008; 111:5 حَبْلٌۭ ح ب ل B001; 111:5 حَبْلٌۭ ح ب ل B012; 111:5 حَبْلٌۭ ح ب ل B004; 111:5 مَّسَدٍۭ م س د B001; 111:5 مَّسَدٍۭ م س د B002; 111:5 مَّسَدٍۭ م س د B005; 111:2 أَغْنَىٰ غ ن ي B005

## Tuzak: kurulan ve kurana dönen

İp kökü avcının tuzağını da adlandırır: {ar:الحبل مصدر حبلت الصيد واحتبلته أي أخذته والحبالة المصيدة وحبائل الموت أسبابه, tr:el-hablu masdaru habeltu's-sayde vehtebeltuh, ey ehaztuh, ve'l-hibâletu el-misyede, ve habâilu'l-mevti esbâbuh, gloss:habl, avı iple yakaladım fiilinin masdarıdır; hibâle tuzaktır; ölümün ipleri onun sebepleridir, source:"ح ب ل,B005"}. Tuzağa düşen hayvanın da adı vardır: {ar:المحبول الوحشي الذي نشب في الحبالة, tr:el-mahbûl el-vahşiyyu'llezî neşibe fi'l-hibâle, gloss:mahbûl, tuzağa takılan yaban hayvanıdır, source:"ح ب ل,B005"}. Felaket de bu sahneyle açıklanır: {ar:الحبل بكسر الحاء وهي الداهية ووجهه أن الإنسان إذا دهي فكأنه قد حبل أي وقع في الحبالة, tr:el-hiblu ve hiye'd-dâhiye, ve vechuhû enne'l-insâne izâ duhiye fe-keennehû kad hubile, ey vekaa fi'l-hibâle, gloss:hibl felakettir; çünkü insan felakete uğradığında sanki iple yakalanmış, yani tuzağa düşmüştür, source:"ح ب ل,B011"}. Üçüncü ayetin fiilinin kökü de tuzak kurmayı bilir: {ar:المصلاة أن تنصب شركا ونحوه, tr:el-maslât en tensibe şereken ve nahveh, gloss:maslât, bir kapan ya da benzerini kurmaktır, source:"ص ل ي,B005"}, {ar:مصالي هي الأشراك واحدتها مصلاة, tr:mesâlî hiye'l-eşrâk, vâhidetuhâ maslât, gloss:mesâlî kapanlardır, tekili maslâttır, source:"ص ل ي,B005"}. Böylece surenin son iki kelimesinde, boyundaki ip ile yakılma fiilinde, birer tuzak sesi vardır. Birinci ayetin fiili de birilerinin başkalarını helak etmesini söyleyebilir: {ar:تببوهم تتبيبا أي أهلكوهم, tr:tebbebûhum tetbîben, ey ehlekûhum, gloss:onları helak ettiler, source:"ت ب ب,B001"}.

Bu sesler birlikte bir işleyiş gösterir: kurulan tuzak sonunda kurana kapanır, ip boyna geçer, felaket bir yakalanma olarak gelir. Kur'an bu işleyişi açıkça söyler: {ar:وَلَا يَحِيقُ ٱلْمَكْرُ ٱلسَّيِّئُ إِلَّا بِأَهْلِهِۦ, tr:ve lâ yahîku'l-mekru's-seyyiu illâ bi-ehlih, gloss:kötü düzen ancak sahibini kuşatır, source:35:43}. Zayıf bırakılanların büyüklenenlere sitemi de gece ve gündüz kurulan düzeni boyundaki halkalara bağlar: {ar:بَلْ مَكْرُ ٱلَّيْلِ وَٱلنَّهَارِ, tr:bel mekru'l-leyli ve'n-nehâr, gloss:hayır, gece gündüz kurduğunuz düzendi, source:34:33}; aynı ayet {ar:وَجَعَلْنَا ٱلْأَغْلَٰلَ فِىٓ أَعْنَاقِ ٱلَّذِينَ كَفَرُوا۟, tr:ve cealne'l-ağlâle fî a'nâkı'llezîne keferû, gloss:inkâr edenlerin boyunlarına halkalar geçirdik, source:34:33} diye biter.

Kaynaklar: 111:5 حَبْلٌۭ ح ب ل B005; 111:5 حَبْلٌۭ ح ب ل B011; 111:3 سَيَصْلَىٰ ص ل ي B005; 111:1 تَبَّتْ ت ب ب B001

## Bağ ve koruma: el ve ip

İp, kökünde ahit, güven ve bağlılıktır: {ar:الحبل العهد والأمان وهو مثل الجوار والحبل الوصال, tr:el-hablu el-ahdu ve'l-emân, ve huve mislu'l-civâr, ve'l-hablu el-visâl, gloss:habl ahit ve güvencedir, himaye gibidir; habl bağlılıktır, source:"ح ب ل,B002"}. Bir şeye ulaştıran her şeyin adı olarak da ödünç alınır: {ar:استعير للوصل ولكل ما يتوصل به إلى شيء, tr:usteîra li'l-vasli ve li-kulli mâ yutevassalu bihî ilâ şey', gloss:bağlantı ve bir şeye kendisiyle ulaşılan her şey için ödünç alındı, source:"ح ب ل,B002"}. El de koruyan ve arka çıkandır: {ar:فلان يد فلان أي وليه وناصره, tr:fulânun yedu fulân, ey veliyyuhû ve nâsıruh, gloss:falanca falancanın elidir, yani dostu ve yardımcısı, source:"ي د ي,B016"}; {ar:اليد الغياث واليد منع الظلم, tr:el-yedu el-ğıyâs, ve'l-yedu men'u'z-zulm, gloss:el yardıma koşmaktır, el zulmü engellemektir, source:"ي د ي,B016"}. El verilir ve geri çekilir: {ar:هذه يدي لك, tr:hâzihî yedî lek, gloss:işte elim senin, source:"ي د ي,B006"}; {ar:خلع فلان يده عن الطاعة, tr:hale'a fulânun yedehû ani't-tâa, gloss:falanca elini itaatten çekti, source:"ي د ي,B006"}. Birinci ayetin fiili kesmektir {source:"ت ب ب,B004"}. Surenin ilk kelimesi elleri keser ve kurutur, son kelimesi bir iptir. Korumanın eli ile güvenin ipi surede yalnızca kurumuş el ve boyun bağı olarak vardır. İpe gücünü veren büküm {source:"م س د,B001"} burada bir boynu bağlamaya harcanır.

Kur'an ipi kurtuluşun aracı olarak, hem de ateşin karşısında gösterir: {ar:وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا, tr:va'tasımû bi-habli'llâhi cemîan, gloss:hep birlikte Allah'ın ipine sımsıkı tutunun, source:3:103}; aynı ayet, birbirine düşman olanların kalplerinin birleştirildiğini ve {ar:وَكُنتُمْ عَلَىٰ شَفَا حُفْرَةٍۢ مِّنَ ٱلنَّارِ فَأَنقَذَكُم مِّنْهَا, tr:ve kuntum alâ şefâ hufretin mine'n-nâri fe-enkazekum minhâ, gloss:bir ateş çukurunun kıyısındaydınız, sizi oradan kurtardı, source:3:103} diye biter. Orada ip düşmanlığı bağlılığa çevirir ve ateşten çeker; surede ip boyna dolanır ve ateş önündedir. Bir başka ayette ip açıkça himayedir: {ar:إِلَّا بِحَبْلٍۢ مِّنَ ٱللَّهِ وَحَبْلٍۢ مِّنَ ٱلنَّاسِ, tr:illâ bi-hablin mina'llâhi ve hablin mine'n-nâs, gloss:ancak Allah'tan bir iple ve insanlardan bir iple, source:3:112}. Verilen el de Kur'an'da bir ahit sahnesidir: {ar:يَدُ ٱللَّهِ فَوْقَ أَيْدِيهِمْ ۚ فَمَن نَّكَثَ فَإِنَّمَا يَنكُثُ عَلَىٰ نَفْسِهِۦ, tr:yedu'llâhi fevka eydîhim, fe-men nekese fe-innemâ yenkusu alâ nefsih, gloss:Allah'ın eli onların ellerinin üstündedir; kim bozarsa kendi aleyhine bozar, source:48:10}. Bükülmüş bir şeyi çözmek de ahit bozmanın mecazıdır: {ar:وَلَا تَكُونُوا۟ كَٱلَّتِى نَقَضَتْ غَزْلَهَا مِنۢ بَعْدِ قُوَّةٍ أَنكَٰثًۭا, tr:ve lâ tekûnû kelletî nakadat ğazlehâ min ba'di kuvvetin enkâsâ, gloss:ipliğini sağlamca büktükten sonra çözüp lime lime eden kadın gibi olmayın, source:16:92}. Birleştirilmesi emredileni kesmek, kaybedenlerin işidir: {ar:وَيَقْطَعُونَ مَآ أَمَرَ ٱللَّهُ بِهِۦٓ أَن يُوصَلَ, tr:ve yakta'ûne mâ emera'llâhu bihî en yûsal, gloss:Allah'ın birleştirilmesini emrettiğini keserler, source:2:27}; o ayet {ar:أُو۟لَٰٓئِكَ هُمُ ٱلْخَٰسِرُونَ, tr:ulâike humu'l-hâsirûn, gloss:işte onlar kaybedenlerdir, source:2:27} diye biter ve bir başka yerde aynı kesişin karşılığı lanettir {source:13:25}. Akrabalık bağlarını kesmek de bu kesişin bir adıdır: {ar:وَتُقَطِّعُوٓا۟ أَرْحَامَكُمْ, tr:ve tukattı'û erhâmekum, gloss:akrabalık bağlarınızı kesersiniz, source:47:22}.

Kaynaklar: 111:5 حَبْلٌۭ ح ب ل B002; 111:1 يَدَآ ي د ي B016; 111:1 يَدَآ ي د ي B006; 111:1 تَبَّتْ ت ب ب B004; 111:5 مَّسَدٍۭ م س د B001

## Buluşmalar

İlk buluşma birinci ayetin kendisindedir: kuruyan eller, alevle adlandırılmış adama aittir. Alev kökünün surenin ifadesini kendi adlandırma anlamının altında anması {source:"ل ه ب,B006"} iki imgeyi tek bir tamlamada tutar: kaybeden eller ile ateşe giden ad aynı kişinin iki yüzüdür. Elin kaybı ile ateş, ikinci ve üçüncü ayetin sırasında birleşir. Kur'an bu sırayı başka bir surede aynı kelimelerle kurar: önce {ar:وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ, tr:ve mâ yuğnî anhu mâluhû izâ teraddâ, gloss:yuvarlanıp düştüğünde malı ona fayda vermez, source:92:11}, birkaç ayet sonra {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona ancak en bedbaht olan girer, source:92:15}. Fayda vermeme fiili ile alev kelimesi de bir ayette yan yanadır {source:77:31}.

Alev ile yakıt, adın içinde buluşur. Baba kökü besleyeni adlandırır {source:"ء ب و,B001"}, odun ise yakmak için hazırlanan şeydir {source:"ح ط ب,B001"}. Alevin babası alevi besleyen olarak birinci ayette durur, alevin yakıtı dördüncü ayette sırtta taşınır, ve ikisi üçüncü ayetin ateşinde birleşir. Aynı ateş ev ocağıyla da buluşur: yakma fiilinin kökü hem ısınılan ocağı hem Ateşi adlandırır {source:"ص ل ي,B004"}. Mûsâ'nın ailesine getirdiği ateşte {ar:لَعَلَّكُمْ تَصْطَلُونَ, tr:lealekum tastalûn, gloss:belki ısınırsınız, source:27:7} ile surenin {ar:سَيَصْلَىٰ, tr:se-yaslâ, gloss:yanacak, source:111:3} kelimesi aynı kökün iki ucudur. Odun bir de söz odunudur: yakıt olarak taşınan ile laf olarak taşınan aynı kelimedir, ve laf insanlar arasında ateşin kökünden adını alan bir düşmanlık tutuşturur {source:"ن و ر,B007"}. Mal toplayan dedikoducunun tutuşturulmuş ateşe atıldığı sahne {source:104:6} ve savaş için yakılan ateşler {source:5:64} bu iki odunu tek sahnede tutar.

Sırttaki yük ile boyundaki ip, beşinci ayetin ipinde birleşir: yular yük hayvanının boyun ipidir {source:"ح ب ل,B001"}, mesed de deve yününden bükülen iptir {source:"م س د,B001"}. Sırtına yük vurulmuş bir hayvanın boynunda yular vardır; kadının sırtında odun, boynunda ip vardır. Kur'an yük ile süsü bir ayette birleştirir: buzağı olayında İsrailoğulları {ar:حُمِّلْنَآ أَوْزَارًۭا مِّن زِينَةِ ٱلْقَوْمِ, tr:hummilnâ evzâren min zîneti'l-kavm, gloss:kavmin süs eşyasından yükler yüklendik, source:20:87} derler. Süs yük olur; surede gerdanlığın yeri ip taşır. Kazanç ile yük de bir ayette buluşur {source:6:164}: birinci ve ikinci ayetin kazanan elleri ile dördüncü ayetin taşıyan sırtı, kişinin kazandığının kendi yükü oluşunun iki yarısıdır.

El ile boyun, birinci ve beşinci ayet arasında buluşur. Elin boyna bağlanmasını yasaklayan talimat {source:17:29} ve esirgenen malın boyun halkasına dönüşmesi {source:3:180}, surenin iki ucunu tek bir bedende birleştirir: kazanan el ile bağlanan boyun. İp kendi içinde üç sahneyi birden tutar: boyundaki halka, avcının tuzağı ve kesilen bağ. Gece gündüz kurulan düzenin boyunlardaki halkalarla bittiği ayet {source:34:33} halka ile tuzağı, Allah'ın ipine tutunmayı ateş çukurunun kıyısına koyan ayet {source:3:103} bağ ile ateşi birleştirir. Bükümün ipe verdiği güç, birinde birleştirmeye, ötekinde bir boynu bağlamaya gider.

Surenin hareketi bedenin üzerinden ilerler: birinci ayette eller, ikinci ayette ellerin tuttuğu mal ve kazanç, üçüncü ayette bütün bedenin girdiği ateş, dördüncü ayette sırt, beşinci ayette boyun. Adamın kazanan elleri ile kadının taşıyan sırtı aynı ateşe çalışır; biri kazandığının kendisine yetmediğini görür, öteki taşıdığı odunun yandığı yere bağlanır. İlk kelime ellere düşen bir kayıp ve bir kesiştir, son kelime boyna geçen bükülmüş bir ip; arada, adın içinde daha baştan yanan alev durur.

