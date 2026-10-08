Focus: 111:1. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/111_1/D.r13/context.md =====
# 111:1 — focus

تَبَّتْ يَدَآ أَبِى لَهَبٍۢ وَتَبَّ

Anchor translation (canonical reading, reference only):

Ebu Leheb'in iki eli yok olsun; kendisi de yok oldu.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | تَبَّتْ | تَبَّ | ت ب ب | V |
| 2 | يَدَآ | يَد | ي د ي | N |
| 3 | أَبِى | أَبٌ | ء ب و | N |
| 4 | لَهَبٍ | لَهَب | ل ه ب | N |
| 5 | وَتَبَّ | تَبَّ | ت ب ب | CONJ;V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 111 — full text (context; no pericope)

- 111:1 ◀ focus تَبَّتْ يَدَآ أَبِى لَهَبٍۢ وَتَبَّ
- 111:2 مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ
- 111:3 سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ
- 111:4 وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ
- 111:5 فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ


===== _commentary/v16/work/111_1/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ت ب ب (root_000172) — identity root of تَبَّتْ (w1)

- **B001** kayıp ve yok oluş — kayıp, yok oluş ve kaybın sürmesi · kayba uğradı veya yok oldu · elleri kayba uğradı; gücü boşa çıktı · ona yok oluş ve kayıp olsun · ona yok oluş diledim · kayba uğratma veya yok etme
  التباب الخسران (maqayis)؛ تبا للكافر أي هلاكا له (maqayis)؛ تبت يداه تبا وتبابا أي خسرت (jamhara)؛ التباب الخسران والهلاك (sihah)؛ تببوهم تتبيبا أي أهلكوهم (sihah)؛ التب الخسار وتبا لفلان على الدعاء (tahdhib)؛ وما زادوهم غير تتبيب أي تخسير (maqayis;tahdhib;mufradat)؛ التب والتباب الاستمرار في الخسران (mufradat)
- **B002** düzene girip süreklilik kazanma [kalıp] — iş hazır olup düzene girdi ve belli oldu · o şey onun için sürdü · açık, belirgin ve düzgün yol
  استتب الأمر إذا تهيأ (maqayis;sihah)؛ استتب أمر فلان إذا اطرد واستقام وتبين (tahdhib)؛ الطريق المستتب الواضح البين المستقيم (tahdhib)؛ استتب لفلان كذا أي استمر (mufradat)
- **B003** yaşlılık ve bedensel yıpranma — zayıf veya yaşlı adam · zayıf erkekler topluluğu · yaşlı kadın · sırtı yara olmuş eşek veya deve · yaşlandı
  رجل تاب ضعيف والجميع الإتباب؛ التابة الكبيرة ورجل تاب أي كبير؛ حمار تاب الظهر إذا دبر وجمل تاب كذلك؛ تبتب إذا شاخ
- **B004** kesmek — kesti
  تب إذا قطع

## ي د ي (root_001693) — identity root of يَدَآ (w2)

- **B001** el ve elin uğradığı bedensel durumlar — el · elinden vurmak · eli kökünden kesilmiş kimse · el ağrısı · eli tuzağa yakalanmış olmak
  اليَد الجارحة (mufradat)؛ اليد أصلها يدي وجمعها أيد ويدي (sihah)؛ يديت الرجل إذا ضربت يده (jamhara;sihah;tahdhib;mufradat)؛ رجل ميدي أي مقطوع اليد واليداء وجع اليد (tahdhib)
- **B002** güç, yeterlik ve güçlendirme — güç ve yeterlik · güç · güçlendirmek · buna gücüm yetmez
  اليد القوة وأيده أي قواه (sihah)؛ ما لي به يدان أي قوة (tahdhib;mufradat)؛ أولي الأيدي أي أولي القوة (tahdhib;mufradat)
- **B003** karşılıksız iyilik ve bağış — iyilik ve karşılıksız yarar · iyilikte bulunmak · satış, borç ya da karşılık olmadan vermek
  أيديت إلى الرجل يدا إذا أسديتها إليه (jamhara)؛ اليد النعمة والإحسان (sihah;tahdhib;mufradat)؛ أعطاه مالا عن ظهر يد تفضلا ليس من قرض ولا مكافأة (sihah;tahdhib)؛ يده مطلقة عبارة عن إيتاء النعيم (mufradat)
- **B004** elinde bulunma, sahiplik ve denetim [kalıp] — onun elinde, sahipliğinde ve denetiminde
  هذا الشيء في يدي أي في ملكي (sihah)؛ هذه الضيعة في يد فلان أي ملكه (tahdhib)؛ للحوز والملك يقال هذا في يد فلان (mufradat)
- **B005** egemenlik ve buyurma gücü — egemenlik ve buyurma gücü · rüzgarın yön verme gücü
  اليد السلطان (tahdhib)؛ اليد في هذا لفلان أي الأمر النافذ لفلان (tahdhib)؛ أيديكم فوق أيديهم (mufradat)؛ عن قهر وذل (tahdhib)
- **B006** boyun eğme, bağlılık ve güvence üstlenme — boyun eğme ve uyma · buyruğuna girdim · bunun için sana güvence veriyorum · bağlılıktan çıkmak
  عن يد أي عن ذلة واستسلام (sihah)؛ اليد الطاعة واليد الاستسلام (tahdhib)؛ هذه يدي لك (tahdhib)؛ يدي لك رهن بكذا أي ضمنت وكفلت (tahdhib)؛ خلع فلان يده عن الطاعة (tahdhib)
- **B007** elden ele verme, peşin ödeme ve iki fiyatlı satış — elden ele, doğrudan karşılık vererek · karşılığını elden vermek · elden ele verme · iki ayrı fiyatla
  ياديت فلانا جازيته يدا بيد (sihah)؛ أعطيته مياداة أي من يدي إلى يده (sihah)؛ عن يد نقدا عن ظهر يد ليس بنسيئة (sihah;tahdhib)؛ ابتعت الغنم باليدين أي بثمنين مختلفين (sihah;tahdhib)؛ باع غنمه اليدين أن يسلمها بيد ويأخذ ثمنها بيد (tahdhib)
- **B008** önünde ya da hemen öncesinde [kalıp] — önünde veya hemen öncesinde
  بين يدي الساعة أهوال أي قدامها (sihah)؛ بين يديك كذا لكل شيء أمامك (tahdhib)؛ يثور الرهج بين يدي المطر ويهيج السباب بين يدي القتال (tahdhib)
- **B009** kişinin kendi yaptığı iş ve doğurduğu sorumluluk [kalıp] — senin yaptığın, işlediğin ve kazandığın şey
  هذا ما قدمت يداك أي جنيته أنت (sihah)؛ ذلك بما كسبت يداك (tahdhib)؛ مما كتبت أيديهم فنسبته إلى أيديهم تنبيه على أنهم اختلقوه (mufradat)
- **B010** pişman olup hayıflanma [kalıp] — pişman olup hayıflanmak
  سقط في يديه وأسقط أي ندم (sihah)؛ اليد الندم ويقال سقط في يده إذا ندم (tahdhib)؛ ولما سقط في أيديهم أي ندموا (mufradat)
- **B011** yönlere dağılıp gitme ve izlenen yol [kalıp] — her yana dağılıp gitmek · deniz yolu
  ذهبوا أيدي سبا وأيادي سبا أي متفرقين (sihah)؛ اليد الطريق يقال أخذ فلان يد بحر إذا أخذ طريق البحر (tahdhib)؛ ذهب القوم أيدي سبا أي متفرقين في كل وجه (tahdhib)
- **B012** zaman boyunca, sonsuza dek [kalıp] — zaman boyunca, sonsuza dek
  لا أفعله يد الدهر أي أبدا (sihah)؛ يد الدهر مد زمانه (tahdhib)؛ شبه الدهر فجعل له يد في قولهم يد الدهر (mufradat)
- **B013** bir nesnenin tutacağı, ucu ya da uzantısı [kalıp] — nesnenin tutacağı, ucu, kolu veya uzantısı
  يد الثوب ما فضل منه إذا تعطفت به والتحفت (sihah)؛ يد الفأس مقبضها ويد القوس سيتها (tahdhib)؛ قميص قصير اليدين أي قصير الكمين (tahdhib)؛ يد المسند (mufradat)
- **B014** geniş, bol ve rahat [kalıp] — geniş ve rahat yaşam · bol ve geniş giysi
  عيش يدي واسع (jamhara)؛ ثوب يدي وأدي أي واسع (sihah)؛ ثوب يدي واسع (tahdhib)
- **B015** eli işe yatkın ve becerikli — eli işe yatkın, becerikli
  امرأة يدية أي صناع (sihah;mufradat)؛ رجل يدي (sihah;mufradat)؛ النسبة إلى يد يدي (tahdhib)
- **B016** birlik içinde destek ve koruma [kalıp] — başkalarına karşı tek güç olarak dayanışmak · onun destekçisi ve koruyucusu
  المسلمون يد على من سواهم أي كلمتهم ونصرتهم واحدة (tahdhib)؛ اليد الغياث واليد منع الظلم (tahdhib)؛ فلان يد فلان أي وليه وناصره (mufradat)؛ أنا يدك (mufradat)
- **B017** yemeye başlama buyruğu [kalıp] — ye, yemeğe başla
  اليد الأكل يقال ضع يدك أي كل (tahdhib)

## ء ب و (root_000007) — identity root of أَبِى (w3)

- **B001** babalık, besleyip yetiştirme ve oluşuma ya da iyileşmeye kaynaklık etme — baba · babalar, atalar ve baba yönünden onlara katılanlar · anne ile baba; bağlama göre baba ile amca veya dede · babalık veya baba soyu · birinin ya da bir topluluğun babası olmak · ebeveyn gibi besleyip büyütmek · birini baba edinmek · bir şeyin ortaya çıkmasına, düzelmesine veya görünür olmasına sebep olan kimse · konuklarla yakından ilgilenen kimse · savaşı kışkırtan kimse · bir kadının bekâretini bozan erkek
  يدل على التربية والغذو (maqayis)؛ أبوت الشيء آبوه أبوا إذا غذوته (maqayis)؛ فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده (ayn;tahdhib)؛ الأب أصله أبو (sihah)؛ الأب الوالد ويسمى كل من كان سببا في إيجاد شيء أو صلاحه أو ظهوره أبا (mufradat)
- **B002** babaya seslenme ve bağlama göre övgü ya da ağır yergi bildiren hitap kalıpları [kalıp] — babacığım diye seslenme · bağlama göre övgü ya da ağır sövgü bildiren hitap kalıbı · seni çekemeyenin babası olmasın anlamında onurlandırıcı hitap
  يا أبة افعل (sihah)؛ يا أبت ويا أبت لغتان (sihah)؛ لا أبا لك كأنه يمدحه (ayn)؛ لا أبا لك ولا أب لك مدح (sihah)؛ لا أبا لك ولا أب لك مدح ولا أم لك ذم (tahdhib)
- **B003** dağ keçisi idrarının kokusundan hastalanma — dağ keçisi idrarını koklayınca hastalanan dişi keçi · dağ keçisi idrarını koklayınca hastalanan erkek keçi
  عنز أبواء إذا أصابها وجع عن شم أبوال الأروى (maqayis)؛ عنز أبواء وتيس آبى إذا شم بول الأروى فمرض منه (sihah)

## ل ه ب (root_001379) — identity root of لَهَبٍ (w4)

- **B001** alev dili, ateşin tutuşması ve tutuşturulması — alev, ateş dili ve yanış · ateşten görünen alev · alevlenme ve yanma · ateşin yanması; alevsiz kor kızıllığı · ateş tutuştu ve alevlendi · ateşi tutuşturdu
  ارتفاع لسان النار (maqayis)؛ اللهب لهب النار (maqayis;jamhara;sihah)؛ اشتعال النار الذي قد خلص من الدخان (ayn;tahdhib)؛ التهبت النار وتلهبت وألهبتها (sihah;tahdhib)؛ اللهب اضطرام النار (mufradat)
- **B002** susuzluk ve susayana ya da kızgın zemine bağlı yakıcı sıcaklık — susuzluk · susuzluk ve susayana vuran sıcaklık · güneşte kızmış zeminin kavurucu sıcağı · susamış erkek · susamış kadın
  للعطشان لهبان (maqayis)؛ لهبان الحر في الرمضاء (ayn;tahdhib)؛ يستعمل اللهاب في النار والعطش جميعا (jamhara)؛ اللهبة العطش ورجل لهبان وامرأة لهبى (sihah;tahdhib)؛ اللهاب في الحر الذي ينال العطشان (mufradat)
- **B003** yükselen güçlü parıltı ve alevsi toz ya da duman — alev gibi yükselen parlak toz veya duman · ışığı yükselip güçlü biçimde parlayan her şey
  كل شيء ارتفع ضوؤه ولمع لمعانا شديدا (maqayis)؛ اللهب الغبار الساطع (maqayis;tahdhib)؛ يقال للدخان وللغبار لهب (mufradat)
- **B004** atın coşkun ve toz kaldıran şiddetli koşusu — at şiddetle ve coşkuyla koştu · şiddetle koşup toz kaldıran at · atın şiddetli koşusu ve atılışı
  فرس ملهب إذا أثار الغبار وله ألهوب (maqayis;tahdhib)؛ ألهب الفرس إذا عدا عدوا شديدا (jamhara)؛ ألهب الفرس إذا اضطرم جريه والاسم الألهوب (sihah)؛ فرس ملهب شديد العدو والألهوب العدو الشديد (mufradat)
- **B005** dağ yarığı, dağlar arası derin açıklık veya sarp dağ yüzü — 
  اللهب الشعب الصغير في الجبل (jamhara)؛ اللهب الفرجة والهواء يكون بين الجبلين (sihah)؛ اللهب وجه من الجبل كالحائط لا يستطاع ارتقاؤه (tahdhib)؛ اللهب مهواة ما بين كل جبلين (tahdhib)
- **B006** alevle ilişkili kişi, topluluk ve yer adları — alevle ilişkilendirilmiş bir künye · alevle ilişkilendirilmiş bir boy veya topluluk adı · bir yer adı · bir yer adı · bir kişi adı · bir kabile adı · bir vadi adı
  بنو لهب بطن من العرب (maqayis)؛ لَهاب موضع واللهباء موضع ولهبان اسم واللهبة قبيلة وبنو لهب قبيلة (jamhara)؛ كني أبو لهب به (sihah)؛ بنو لهب حي من العرب اللهبيون (tahdhib)؛ تبت يدا أبي لهب (mufradat)
- **B007** şimşeğin boşluksuz art arda çakması [kalıp] — şimşek arada boşluk bırakmadan art arda çaktı
  ألهب البرق إلهابا وإلهابه تداركه حتى لا يكون بين البرقتين فرجة (tahdhib)
- **B008** çarpıcı güzel kişi veya çok kıllı erkek — çarpıcı derecede güzel · çok kıllı erkek
  الملهب الرائع الجمال والملهب الكثير الشعر من الرجال (tahdhib)

## ECHO ء ي د (root_000071) — for يَدَآ (w2): withheld observed target; not identity

- **B001** güç ve güçlendirme — güçlü kıldı · güç
  أيده الله أي قواه الله (maqayis)؛ والسماء بنيناها بأيد فهذا معنى القوة (maqayis)؛ الأيد أي القوة الشديدة (mufradat)؛ يؤيد بنصره أي يكثر تأييده (mufradat)؛ له أيد ومنه قيل للأمر العظيم مؤيد (mufradat)
- **B002** koruyucu engel — bir şeyi koruyan engel
  الإياد كل حاجز الشيء يحفظه (maqayis)؛ إياد الشيء ما يقيه (mufradat)

===== _commentary/v16/out/s111/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 111:1, and ## Buluşmalar) =====
## Eller: toplayan, kazanan ve kaybeden

Sure bir el sahnesiyle açılır: {ar:تَبَّتْ يَدَآ أَبِى لَهَبٍۢ, tr:tebbet yedâ ebî leheb, gloss:Ebû Leheb'in iki eli kurudu, source:111:1}. İlk fiilin kökü bir kaybı adlandırır ve bu kaybı doğrudan ellere bağlayan bir kullanımı vardır: {ar:تبت يداه تبا وتبابا أي خسرت, tr:tebbet yedâhu tebben ve tebâben, ey hasirat, gloss:elleri kurudu, yani zarara uğradı, source:"ت ب ب,B001"}. Burada iflas önce bir organa, iki ele düşer. Aynı kökün masdarı bir beddua kalıbıdır, {ar:تبا لفلان, tr:tebben li-fulân, gloss:kahrolsun falanca, source:"ت ب ب,B001"}; bu yüzden açılış hem bir bildirim hem de bir lanet olarak işitilir. Kök kesmeyi de adlandırır {source:"ت ب ب,B004"}: kuruyan el aynı zamanda kesilen eldir. Hemen arkasından gelen {ar:وَتَبَّ, tr:ve tebbe, gloss:kendisi de kurudu, source:111:1} aynı fiili bu kez adamın kendisine yükler. Kökün bir başka tanımı, {ar:التب والتباب الاستمرار في الخسران, tr:et-tebbu ve't-tebâbu el-istimrâru fi'l-husrân, gloss:zararda kalıp sürmek, source:"ت ب ب,B001"}, ikinci fiilin işini gösterir: kayıp ellerden bütün kişiye geçer ve orada kalır.

Bu sure boyunca bir kelimenin kök ailesinden gelen imgeler, kelimenin ayetteki anlamının yerine değil yanında duyulur. Ayet iki eli söyler; elin kökünün taşıdığı öbür anlamlar bu elin arkasından işitilir. El vurulabilen, kesilebilen bir organdır: {ar:يديت الرجل إذا ضربت يده, tr:yedeytu'r-racule izâ darabtu yedehu, gloss:adamın eline vurdum, source:"ي د ي,B001"}. El güçtür: {ar:اليد القوة, tr:el-yedu el-kuvve, gloss:el, güçtür, source:"ي د ي,B002"}. Elde olan, sahip olunandır: {ar:هذا الشيء في يدي أي في ملكي, tr:hâze'ş-şey'u fî yedî, ey fî milkî, gloss:bu şey elimde, yani mülkümde, source:"ي د ي,B004"}. Ve el kazanılanın ve hesabı verilecek olanın faili olarak anılır: {ar:ذلك بما كسبت يداك, tr:zâlike bimâ kesebet yedâk, gloss:bu, ellerinin kazandığı yüzündendir, source:"ي د ي,B009"}. İkili sayı, yani "iki el", bu yüzden adamın kudretini, mülkünü ve kazancını birlikte tutar; kurutulan şey bütün bu tutuştur.

İkinci ayet ellerin ne tuttuğunu söyler ve onu boşa çıkarır: {ar:مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ, tr:mâ ağnâ anhu mâluhû ve mâ keseb, gloss:ne malı ona fayda verdi ne de kazandığı, source:111:2}. Fiil, bir şeyin birini karşılaması, ona yetmesi demektir: {ar:أغناني كذا وأغنى عنه كذا إذا كفاه, tr:ağnânî kezâ ve ağnâ anhu kezâ izâ kefâhu, gloss:şu bana yetti, şu ondan yana yetti, source:"غ ن ي,B002"}. Fakat aynı kök zenginliğin kendi adıdır, {ar:الغنى في المال, tr:el-ğınâ fi'l-mâl, gloss:zenginlik malda olur, source:"غ ن ي,B001"}. Böylece olumsuzlanan fiil zenginliğin kendi işini inkâr eder: malı onu zengin etmedi, ona yetmedi. Mal, eldeki birikmiş varlıktır; Arapların durumunda sürüdür: {ar:كانت أموال العرب أنعامهم, tr:kânet emvâlü'l-Arabi en'âmehum, gloss:Arapların malları hayvanlarıydı, source:"م و ل,B001"}. Kazanmak ise rızkı arayıp kendine çekmektir, {ar:الكسب طلب الرزق, tr:el-kesbu talebu'r-rızk, gloss:kazanç, rızık aramaktır, source:"ك س ب,B001"}. Ve bu kökün bir kullanımı daireyi kapatır: {ar:الكواسب الجوارح, tr:el-kevâsibu el-cevârih, gloss:kazananlar, uzuvlardır, source:"ك س ب,B003"}. Kazanan şey uzuvların kendisidir; ikinci ayetin kazancı birinci ayetin ellerine döner. Adam ellerini toplamak için uzattı; topladığı şey, aynı ellere düşen kaybın önüne geçmedi.

Kur'an el ile kazancı aynı kalıpta defalarca birleştirir: {ar:بِمَا كَسَبَتْ أَيْدِى ٱلنَّاسِ, tr:bimâ kesebet eydi'n-nâs, gloss:insanların ellerinin kazandığı yüzünden, source:30:41} ve {ar:فَبِمَا كَسَبَتْ أَيْدِيكُمْ, tr:febimâ kesebet eydîkum, gloss:ellerinizin kazandığı yüzünden, source:42:30}. Allah, kitabı kendi elleriyle yazıp "bu Allah katındandır" diyerek az bir bedele satanlar için el ile kazancı aynı lanetin altında toplar: {ar:فَوَيْلٌۭ لَّهُم مِّمَّا كَتَبَتْ أَيْدِيهِمْ وَوَيْلٌۭ لَّهُم مِّمَّا يَكْسِبُونَ, tr:fe-veylün lehum mimmâ ketebet eydîhim ve veylün lehum mimmâ yeksibûn, gloss:ellerinin yazdığından ötürü vay hâllerine, kazandıklarından ötürü vay hâllerine, source:2:79}. Allah hakkında bilgisiz tartışan ve insanları yoldan çıkarmak için böbürlenen kişiden söz eden pasaj {source:22:8}, ona dünyada rüsvaylık ve kıyamet günü yangın azabı tattırılacağını söyler {source:22:9} ve sonra ona şöyle denir: {ar:ذَٰلِكَ بِمَا قَدَّمَتْ يَدَاكَ, tr:zâlike bimâ kaddemet yedâk, gloss:bu, iki elinin önden gönderdiği yüzündendir, source:22:10}. Aynı ikili sayı uyarının gününde de geçer: {ar:يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ, tr:yevme yenzuru'l-mer'u mâ kaddemet yedâh, gloss:kişinin iki elinin önden gönderdiğine bakacağı gün, source:78:40}.

İkinci ayetin cümlesi Kur'an'da kaybedenin kendi ağzından da duyulur. Kitabı sol eline verilen kişi {source:69:25} şöyle der: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ, tr:mâ ağnâ annî mâliyeh, gloss:malım bana fayda vermedi, source:69:28}, ve hemen ardından {ar:هَلَكَ عَنِّى سُلْطَٰنِيَهْ, tr:heleke annî sultâniyeh, gloss:gücüm benden yok olup gitti, source:69:29}. Mal ile güç, yani surenin malı ile iki eli, orada da birlikte elden çıkar. Cimrilik edip kendini müstağni sanan kişiyi anlatan pasajda, {ar:وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ, tr:ve emmâ men bahile vestağnâ, gloss:cimrilik edip kendini yeterli sayana gelince, source:92:8}, kendini yeterli sayma fiili de aynı kökten gelir; birkaç ayet sonra surenin cümlesi neredeyse kelimesi kelimesine gelir: {ar:وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ, tr:ve mâ yuğnî anhu mâluhû izâ teraddâ, gloss:yuvarlanıp düştüğünde malı ona fayda vermez, source:92:11}. Kendini malıyla yeterli sayan, düştüğü anda malının ona yetmediğini görür. Helak edilmiş kavimler için aynı ikili sabit bir sıra hâlinde tekrarlanır, {ar:فَمَآ أَغْنَىٰ عَنْهُم مَّا كَانُوا۟ يَكْسِبُونَ, tr:fe-mâ ağnâ anhum mâ kânû yeksibûn, gloss:kazandıkları onlara fayda vermedi, source:15:84}; bir yerde de cehennemin önlerinde durduğu söylenerek: {ar:وَلَا يُغْنِى عَنْهُم مَّا كَسَبُوا۟ شَيْـًۭٔا, tr:ve lâ yuğnî anhum mâ kesebû şey'â, gloss:kazandıkları onlara hiçbir fayda vermez, source:45:10}. Fayda vermemek ile tebâb bir ayette birleşir; Allah helak edilen kentler için der ki ilahları onlara fayda vermedi ve {ar:وَمَا زَادُوهُمْ غَيْرَ تَتْبِيبٍۢ, tr:ve mâ zâdûhum ğayra tetbîb, gloss:onlara kayıptan başka bir şey katmadılar, source:11:101}. Kule yapılmasını buyuran Firavun'un {source:40:36} tasarısı da aynı kelimeyle biter: {ar:وَمَا كَيْدُ فِرْعَوْنَ إِلَّا فِى تَبَابٍۢ, tr:ve mâ keydu Fir'avne illâ fî tebâb, gloss:Firavun'un düzeni kayıptan başka bir yere varmadı, source:40:37}. İkinci ayetin reddettiği beklenti ise, mal toplayıp sayan dedikoducunun zannında açıkça söylenir: {ar:يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ, tr:yahsebu enne mâlehû ahledeh, gloss:malının kendisini ölümsüz kıldığını sanır, source:104:3}. Bağı yıkılan bahçe sahibinin sahnesi de el ile harcanan malı aynı jestte toplar: {ar:فَأَصْبَحَ يُقَلِّبُ كَفَّيْهِ عَلَىٰ مَآ أَنفَقَ فِيهَا, tr:fe-asbaha yukallibu keffeyhi alâ mâ enfeka fîhâ, gloss:oraya harcadıkları için avuçlarını ovuşturur oldu, source:18:42}. Ve ellere yöneltilmiş beddua kalıbı, Allah'ın elinin bağlı olduğunu söyleyenlere verilen cevapta aynı dilbilgisiyle geçer: {ar:غُلَّتْ أَيْدِيهِمْ وَلُعِنُوا۟, tr:ğullet eydîhim ve lu'inû, gloss:elleri bağlansın ve lanetlendiler, source:5:64}.

Kaynaklar: 111:1 تَبَّتْ ت ب ب B001; 111:1 تَبَّتْ ت ب ب B004; 111:1 وَتَبَّ ت ب ب B001; 111:1 يَدَآ ي د ي B001; 111:1 يَدَآ ي د ي B002; 111:1 يَدَآ ي د ي B004; 111:1 يَدَآ ي د ي B009; 111:2 أَغْنَىٰ غ ن ي B001; 111:2 أَغْنَىٰ غ ن ي B002; 111:2 مَالُهُۥ م و ل B001; 111:2 كَسَبَ ك س ب B001; 111:2 كَسَبَ ك س ب B003

## Alevin babası: ad ateşe dönüşür

Birinci ayet adamı alevden yapılmış bir künyeyle anar: {ar:أَبِى لَهَبٍۢ, tr:ebî leheb, gloss:alevin babası, source:111:1}. Kök bu adlandırmayı kendi içinde kaydeder, {ar:كني أبو لهب به, tr:kuniye Ebû Lehebin bihî, gloss:Ebû Leheb bununla künyelendi, source:"ل ه ب,B006"}, ve surenin kendi ifadesini bu anlamın altında anar: {ar:تبت يدا أبي لهب, tr:tebbet yedâ Ebî Leheb, gloss:Ebû Leheb'in iki eli kurudu, source:"ل ه ب,B006"}. Üçüncü ayet aynı kelimeyi bu kez ateşin niteliği olarak geri verir: {ar:سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ, tr:se-yaslâ nâran zâte leheb, gloss:alevli bir ateşe girip yanacak, source:111:3}. Adam "alevin babası"dır, ateş "alevin sahibi"; ad ile ateşin vasfı tek bir kelimeyi paylaşır ve künye, adamın varacağı yeri tarif eder hâle gelir.

"Baba" kelimesinin kökü bu sahneyi bir işleyişe çevirir. Baba yalnız doğuran değil, bir şeyi var eden, ayakta tutan, ortaya çıkarandır: {ar:الأب الوالد ويسمى كل من كان سببا في إيجاد شيء أو صلاحه أو ظهوره أبا, tr:el-ebu el-vâlid, ve yusemmâ kullu men kâne sebeben fî îcâdi şey'in ev salâhihî ev zuhûrihî eben, gloss:baba doğurandır; bir şeyin var olmasına, düzelmesine ya da ortaya çıkmasına sebep olan herkese de baba denir, source:"ء ب و,B001"}. Kök ayrıca beslemeyi adlandırır: {ar:أبوت الشيء آبوه أبوا إذا غذوته, tr:ebevtu'ş-şey'e âbûhu ebven izâ ğazevtuh, gloss:bir şeyi besledim, source:"ء ب و,B001"}. Alevin babası böylece alevi doğuran ve onu besleyendir; üçüncü ayette beslediği alevin içine girer.

Alev kökü, ışığın yükselip parlamasını da adlandırır: {ar:كل شيء ارتفع ضوؤه ولمع لمعانا شديدا, tr:kullu şey'in irtefea dav'uhû ve leme'a lem'ânen şedîden, gloss:ışığı yükselen ve şiddetle parlayan her şey, source:"ل ه ب,B003"}. Üçüncü ayette ise aynı kelime düpedüz ateşin dilidir: {ar:ارتفاع لسان النار, tr:irtifâu lisâni'n-nâr, gloss:ateş dilinin yükselmesi, source:"ل ه ب,B001"}. Ateş kelimesinin kökü de ışıkla aynıdır: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûru ve'n-nâru summiyâ bizâlike min tarîkati'l-idâe, gloss:nur da ateş de aydınlatma yönünden bu adı aldı, source:"ن و ر,B001"}. Addaki parlaklık ile sondaki yanış aynı aydınlanmanın iki yüzüdür. Kök bir de deve damgasını bilir; hayvanın soyu damgasından okunur: {ar:نجارها نارها, tr:nicâruhâ nâruhâ, gloss:soyu damgasıdır, source:"ن و ر,B002"}. Burada da adam kimliğini taşıyan bir ateş adıyla anılır ve o ad sonunu söyler. Kur'an, biriktirilip Allah yolunda harcanmayan altın ve gümüşten söz ederken {source:9:34} ateşi damga olarak da sahneler: {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhuhum, gloss:cehennem ateşinde kızdırılıp alınlarının onunla dağlanacağı gün, source:9:35}.

Üçüncü ayetin kuruluşu Kur'an'da bir başka ateşte de geçer. Hendek sahiplerinin sahnesi, tıpkı surenin açılışı gibi geçmiş zamanlı bir lanet fiiliyle başlar, {ar:قُتِلَ أَصْحَٰبُ ٱلْأُخْدُودِ, tr:kutile ashâbu'l-uhdûd, gloss:kahrolsun hendek sahipleri, source:85:4}, ve hemen ardından ateşi kendi maddesinin sahibi olarak anar: {ar:ٱلنَّارِ ذَاتِ ٱلْوَقُودِ, tr:en-nâri zâti'l-vekûd, gloss:yakıtı bol ateş, source:85:5}. Lanet fiili, sonra "sahibi" kelimesiyle nitelenen ateş: bu, birinci ve üçüncü ayetin sırasıdır. Alev kelimesi ile fayda vermeme fiili ise yalanlayanların gönderildiği üç kollu gölgenin tarifinde bir araya gelir {source:77:30}: {ar:لَّا ظَلِيلٍۢ وَلَا يُغْنِى مِنَ ٱللَّهَبِ, tr:lâ zalîlin ve lâ yuğnî mine'l-leheb, gloss:ne gölgelendirir ne de alevden korur, source:77:31}. İkinci ayette mal ona fayda vermedi; orada gölge alevden korumaz.

Kaynaklar: 111:1 أَبِى ء ب و B001; 111:1 لَهَبٍۢ ل ه ب B006; 111:1 لَهَبٍۢ ل ه ب B003; 111:3 لَهَبٍۢ ل ه ب B003; 111:3 لَهَبٍۢ ل ه ب B001; 111:3 نَارًۭا ن و ر B001; 111:3 نَارًۭا ن و ر B002

## Ev ocağı ve soy: tersine dönen hane

Bir ev; ailesi için kazanan bir erkek, bir eş, evlenmede ya da ev kurulurken verilen bir ziyafet, ev için toplanan odun ve et kızartılan, başında ısınılan bir ocakla döner. Surenin kelimeleri bu ev sahnesinin bütün parçalarını kökleriyle taşır. Kazanmak, ailesi için hayır kazanmaktır: {ar:فلان يكسب أهله خيرا, tr:fulânun yeksibu ehlehû hayran, gloss:falanca ailesine hayır kazandırır, source:"ك س ب,B002"}. Baba, besleyendir: {ar:فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده, tr:fulânun ye'bû hâze'l-yetîme ibâveten, ey yağzûhu kemâ yağzu'l-vâlidu veledeh, gloss:falanca bu yetime babalık eder, yani babanın çocuğunu beslediği gibi onu besler, source:"ء ب و,B001"}. Dördüncü ayetin ilk kelimesi eştir, {ar:هي امرأته, tr:hiye'mraetuh, gloss:o, onun karısıdır, source:"م ر ء,B001"}, ve kökü evin kuruluşundaki ziyafeti adlandırır: {ar:والمرء : الإطعام على بناء دار ، أو تزويج, tr:ve'l-mer'u el-it'âmu alâ binâi dârin ev tezvîc, gloss:mer', ev yapımında ya da evlenmede yemek vermektir, source:"م ر ء,B004"}. İkinci ayetin fiilinin kökü evliliği de adlandırır, {ar:الغنى التزويج, tr:el-ğınâ et-tezvîc, gloss:ğınâ, evlendirmedir, source:"غ ن ي,B006"}, ve kocasıyla yetinen kadını: {ar:الغانية المستغنية بزوجها عن الزينة, tr:el-ğâniye el-mustağniye bi-zevcihâ ani'z-zîne, gloss:ğâniye, kocası sayesinde süse ihtiyaç duymayan kadındır, source:"غ ن ي,B005"}. Odun kökü birisi için odun toplamayı bilir, {ar:حطبت فلانا إذا احتطبت له, tr:hatabtu fulânen izehtatabtu leh, gloss:falancaya odun topladım, source:"ح ط ب,B001"}, ve üçüncü ayetin fiili ocağın kendisidir: ısınılan ve kızartılan ateş {source:"ص ل ي,B004"}.

Surede bu ev bütünüyle tersine döner. Kazanan erkeğin kazancı kendine bile yetmez; ikinci ayetin fiili, kocası karısına yeten evliliğin kökünden gelir ama burada koca kendini bile karşılayamaz. Eş, kocasının içinde yanacağı ateşe odun taşır; ev ocağı Ateş olur. Bu ters çevrilmenin karşı sahnesi Kur'an'da Mûsâ'dadır. Süresini doldurup ailesiyle yola çıkan Mûsâ, Tûr'un yanında bir ateş görür ve ailesine şöyle der: {ar:لَعَلِّىٓ ءَاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ جَذْوَةٍۢ مِّنَ ٱلنَّارِ لَعَلَّكُمْ تَصْطَلُونَ, tr:lealî âtîkum minhâ bi-haberin ev cezvetin mine'n-nâri lealekum tastalûn, gloss:belki oradan size bir haber ya da bir ateş koru getiririm, belki ısınırsınız, source:28:29}; aynı söz başka bir yerde {ar:بِشِهَابٍۢ قَبَسٍۢ, tr:bi-şihâbin kabes, gloss:alınmış bir ateş parçasıyla, source:27:7} diye geçer {source:20:10}. Orada "ısınmak" fiili surenin "yanmak" fiiliyle aynı köktendir: bir koca ailesini ısıtmak için ateş getirir; burada bir eş, kocasının yanacağı ateşe odun taşır. Müminlere hitap eden ayet, insanın kendini ve ailesini yakıtı insanlar olan bir ateşten korumasını ister: {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا, tr:kû enfusekum ve ehlîkum nârâ, gloss:kendinizi ve ailenizi bir ateşten koruyun, source:66:6}. Kitabı arkasından verilen kişi için {source:84:10} yanmak, ailesi içindeki eski sevincin karşısına konur: {ar:وَيَصْلَىٰ سَعِيرًا إِنَّهُۥ كَانَ فِىٓ أَهْلِهِۦ مَسْرُورًا, tr:ve yaslâ seîran innehû kâne fî ehlihî mesrûrâ, gloss:alevli ateşe girer; çünkü o ailesi içinde sevinçliydi, source:84:12}. Allah'ın inkâr edenlere örnek verdiği Nûh'un ve Lût'un karılarında eş, fayda vermeme fiili ve Ateş bir araya gelir: {ar:فَلَمْ يُغْنِيَا عَنْهُمَا مِنَ ٱللَّهِ شَيْـًۭٔا وَقِيلَ ٱدْخُلَا ٱلنَّارَ مَعَ ٱلدَّٰخِلِينَ, tr:felem yuğniyâ anhumâ mina'llâhi şey'en ve kîle'dhulâ'n-nâra mea'd-dâhilîn, gloss:kocaları onlara Allah'a karşı hiçbir fayda vermedi ve onlara "girenlerle birlikte ateşe girin" denildi, source:66:10}. Hemen ardından Firavun'un karısı, kocasından ve onun işinden kurtarılmayı dileyen bir eş olarak gelir {source:66:11}: evlilik orada kaderi paylaştırmaz. Surede ise eş ve koca aynı ateşin iki ucundadır.

Dördüncü ve beşinci ayetin iki kelimesi bu evin bir başka parçasını, soyu da işitir. Taşımak, kökünde hamileliktir: {ar:حملت المرأة حبلت, tr:hamelet'il-mer'etu hebilet, gloss:kadın gebe kaldı, source:"ح م ل,B002"}, {ar:الحمل ما كان في بطن, tr:el-hamlu mâ kâne fî batn, gloss:haml, karında olandır, source:"ح م ل,B002"}. İp de kökünde aynı şeydir: {ar:الحبل الحمل وقد حبلت المرأة فهي حبلى, tr:el-habelu el-hamlu ve kad hebileti'l-mer'etu fe-hiye hublâ, gloss:habel gebeliktir; kadın gebe kaldı, o hâmiledir, source:"ح ب ل,B006"}. Bir tanım, iki kelimeyi birbiriyle açıklar ve gebeliğin ipe benzerliğini günlerin onunla uzamasında görür: {ar:الحبل وهو الحمل وذلك أن الأيام تمتد به, tr:el-habelu ve huve'l-hamlu ve zâlike enne'l-eyyâme temteddu bih, gloss:habel gebeliktir, çünkü günler onunla uzar, source:"ح ب ل,B006"}. Kadının iki ayetindeki iki kelime, onun taşıyacağı soyun kelimeleridir; oysa sahnede taşıdığı odun, boynundaki iptir. Birinci ayetin baba kelimesi bu soyun öbür ucunu tutar {source:"ء ب و,B001"}. Kur'an, ikinci ayetin cümlesini başka yerlerde malın yanına evladı koyarak kurar: {ar:مَن لَّمْ يَزِدْهُ مَالُهُۥ وَوَلَدُهُۥٓ إِلَّا خَسَارًۭا, tr:men lem yezidhu mâluhû ve veleduhû illâ hasârâ, gloss:malı ve evladı kendisine kayıptan başka bir şey katmayan, source:71:21}. Bu, Nûh'un kavminin kendisine isyan edip izledikleri önderlerden yakınmasıdır; "kayıp" kelimesi de tebâbın tanımında geçen kelimedir. İbrâhîm'in duasında o gün {ar:يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ, tr:yevme lâ yenfau mâlun ve lâ benûn, gloss:ne malın ne oğulların fayda vereceği gün, source:26:88} diye anılır. Mal ile evladın onlara fayda vermediği ve onların ateşin ehli olduğu ayette {source:58:17} ve yukarıda geçen ayette {source:3:10} bu ikili ikinci ve üçüncü ayetin sırasını kurar. Surede ikinci sırada "kazandığı" durur; o yerde evladı duymak bir okumadır, kelimenin söylediği değil. Suçlunun o gün kurtulmak için fidye olarak vermek isteyeceği şeyler de bu evin halkıdır: {ar:بِبَنِيهِ وَصَٰحِبَتِهِۦ وَأَخِيهِ, tr:bi-benîhi ve sâhibetihî ve ehîh, gloss:oğulları, eşi ve kardeşiyle, source:70:12}.

Kaynaklar: 111:1 أَبِى ء ب و B001; 111:2 كَسَبَ ك س ب B002; 111:2 أَغْنَىٰ غ ن ي B006; 111:2 أَغْنَىٰ غ ن ي B005; 111:3 سَيَصْلَىٰ ص ل ي B004; 111:4 وَٱمْرَأَتُهُۥ م ر ء B001; 111:4 وَٱمْرَأَتُهُۥ م ر ء B004; 111:4 ٱلْحَطَبِ ح ط ب B001; 111:4 حَمَّالَةَ ح م ل B002; 111:5 حَبْلٌۭ ح ب ل B006

## Sırttaki yük: yük hayvanı, yular, vebal

Sırtında odun, boynunda hurma lifinden bir ip: dördüncü ve beşinci ayetin kelimeleri kökleriyle bir yük hayvanı sahnesi kurar. Taşımanın temel yeri sırttır {source:"ح م ل,B001"}; aynı kök yük taşıyan develeri adlandırır: {ar:الحمولة الإبل تحمل عليها الأثقال, tr:el-hamûle el-ibilu tuhmelu aleyhe'l-eskâl, gloss:hamûle, üzerine ağırlık yüklenen develerdir, source:"ح م ل,B006"}. Kök zorlanarak taşımayı da bilir: {ar:تحاملت إذا تكلفت الشيء على مشقة, tr:tehâmeltu izâ tekellefte'ş-şey'e alâ meşakka, gloss:bir şeyi zahmetle üstlendim, source:"ح م ل,B007"}. Odun kökünden kuru diken otlayan dişi deve adını alır: {ar:ناقة محاطبة تأكل الشوك اليابس, tr:nâkatun muhâtıbe te'kulu'ş-şevke'l-yâbis, gloss:kuru diken yiyen dişi deve, source:"ح ط ب,B001"}. Beşinci ayetin ipi bir yulardır: {ar:الحبل الرسن, tr:el-hablu er-resen, gloss:ip, yulardır, source:"ح ب ل,B001"}. İpin maddesi de bu dünyadan gelir; mesed, deve yününden ya da hurma lifinden bükülmüş kaba iş ipidir: {ar:المسد حبل يتخذ من أوبار الإبل, tr:el-mesedu hablun yuttehazu min evbâri'l-ibil, gloss:mesed, deve yününden yapılan iptir, source:"م س د,B001"}, {ar:حبل من ليف أو خوص, tr:hablun min lîfin ev havs, gloss:lif ya da hurma yaprağından ip, source:"م س د,B001"}. Birinci ayetin fiili bile yük hayvanını bilir; sırtı yara olmuş eşek ya da deve onunla anılır: {ar:حمار تاب الظهر إذا دبر, tr:himârun tâbbu'z-zahri izâ debir, gloss:sırtı yağır olmuş eşek, source:"ت ب ب,B003"}.

Taşınan yük bir de vebaldir: {ar:من باء بالإثم يسمى حاملا للإثم, tr:men bâe bi'l-ismi yusemmâ hâmilen li'l-ism, gloss:günahı yüklenen kişiye günah taşıyan denir, source:"ح م ل,B003"}. Kur'an bu yükü sırta koyar. Allah ile karşılaşmayı yalanlayanlar, Saat ansızın geldiğinde hasretle bağırırken {ar:وَهُمْ يَحْمِلُونَ أَوْزَارَهُمْ عَلَىٰ ظُهُورِهِمْ, tr:ve hum yahmilûne evzârahum alâ zuhûrihim, gloss:onlar günah yüklerini sırtlarında taşırlar, source:6:31}; aynı ayet {ar:قَدْ خَسِرَ, tr:kad hasira, gloss:kaybetti, source:6:31} diye açılır, yani tebâbın tanımındaki kayıpla. Zikirden yüz çeviren kıyamet günü bir vebal taşır {source:20:100} ve {ar:وَسَآءَ لَهُمْ يَوْمَ ٱلْقِيَٰمَةِ حِمْلًۭا, tr:ve sâe lehum yevme'l-kıyâmeti himlâ, gloss:kıyamet günü onlar için ne kötü bir yüktür, source:20:101}. Başkalarını yoldan çıkaranlar kendi yükleriyle birlikte saptırdıklarının yükünü de taşır {source:16:25}: {ar:وَلَيَحْمِلُنَّ أَثْقَالَهُمْ وَأَثْقَالًۭا مَّعَ أَثْقَالِهِمْ, tr:ve le-yahmilunne eskâlehum ve eskâlen mea eskâlihim, gloss:kendi ağırlıklarını ve kendi ağırlıklarıyla birlikte başka ağırlıkları da mutlaka taşıyacaklar, source:29:13}. Yükün paylaşılmazlığı ise dişil bir yüklüyle söylenir: {ar:وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ, tr:ve in ted'u muskaletun ilâ himlihâ lâ yuhmel minhu şey'un ve lev kâne zâ kurbâ, gloss:yükü ağır bir kişi yüküne yardım için çağırsa, yakını bile olsa ondan hiçbir şey taşınmaz, source:35:18}. Kazanç ile yük bir ayette yan yana durur: {ar:وَلَا تَكْسِبُ كُلُّ نَفْسٍ إِلَّا عَلَيْهَا ۚ وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ, tr:ve lâ teksibu kullu nefsin illâ aleyhâ, ve lâ teziru vâziratun vizra uhrâ, gloss:her kişinin kazandığı yalnız kendi aleyhinedir; hiçbir yük taşıyan başkasının yükünü taşımaz, source:6:164}. Kadın sırtında yükünü taşır, kocası onun yükünü almaz, o da kocasınınkini.

Kaynaklar: 111:4 حَمَّالَةَ ح م ل B001; 111:4 حَمَّالَةَ ح م ل B006; 111:4 حَمَّالَةَ ح م ل B003; 111:4 حَمَّالَةَ ح م ل B007; 111:4 ٱلْحَطَبِ ح ط ب B001; 111:5 حَبْلٌۭ ح ب ل B001; 111:5 مَّسَدٍۭ م س د B001; 111:1 تَبَّتْ ت ب ب B003

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

