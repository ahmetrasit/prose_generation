Focus: 98:3. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/98_3/D.r13/context.md =====
# 98:3 — focus

فِيهَا كُتُبٌۭ قَيِّمَةٌۭ

Anchor translation (canonical reading, reference only):

Onlarda dosdoğru yazılar vardır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فِيهَا | فِى |  | P;PRON |
| 2 | كُتُبٌ | كِتَٰب | ك ت ب | N |
| 3 | قَيِّمَةٌ | قَيِّمَة | ق و م | ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 98 — full text (context; no pericope)

- 98:1 لَمْ يَكُنِ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ مُنفَكِّينَ حَتَّىٰ تَأْتِيَهُمُ ٱلْبَيِّنَةُ
- 98:2 رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ
- 98:3 ◀ focus فِيهَا كُتُبٌۭ قَيِّمَةٌۭ
- 98:4 وَمَا تَفَرَّقَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ إِلَّا مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَةُ
- 98:5 وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ
- 98:6 إِنَّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ ۚ أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ
- 98:7 إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ
- 98:8 جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ


===== _commentary/v16/work/98_3/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ك ت ب (root_001283) — identity root of كُتُبٌ (w2)

- **B001** bir şeyi başka bir şeye katıp birleştirme — bir şeyi başka bir şeye katıp birleştirme · su tulumunu dikerek birleştirmek · katırın üreme organının dudaklarını halka veya kayışla birleştirmek · dişi devenin burun deliklerini iplikle dikmek veya bağlamak · dişi devenin memelerini bağlamak · su tulumunun ağzını bağıyla sıkıca kapatmak · kayışın iki yüzünü birleştiren boncuk · bir arada duran atlı veya askerî birlik · atların toplanması · askerleri birlik birlik düzenlemek
  أصل صحيح واحد يدل على جمع شيء إلى شيء (maqayis)؛ أصل الكتب ضمك الشيء إلى الشيء (jamhara)؛ ضم أديم إلى أديم بالخياطة (mufradat)؛ كتبت السقاء إذا خرزته (tahdhib)؛ كتبت البغلة إذا جمعت بين شفريها بحلقة (sihah;mufradat)؛ الكتيبة جماعة مستحيزة (sihah;tahdhib)
- **B002** yazma ve yazılı metin — kitabı yazmak veya kopyalamak · yazılı metin veya üzerinde yazı bulunan sayfa · yazma işi ve yazıcılık · kitabı yazmak veya kopyalamak · ona şiiri söyleyerek yazdırmak · birinden kendisi için bir şey yazmasını istemek · çocuğa yazmayı öğretmek · yazı öğretmeni veya yazı öğretilen yer · öğretim yerindeki çocuklar veya onların topluluğu
  الكتاب والكتابة يقال كتبت الكتاب أكتبه كتبا (maqayis)؛ وقد كتب الكتاب يكتبه كتبا إذا جمع حروفه (jamhara)؛ الكتاب معروف وقد كتبت كتبا وكتابا وكتابة (sihah)؛ كتبت الكتاب كتبا وكتابا فالكتاب اسم لما كتب مجموعا (tahdhib)؛ في التعارف ضم الحروف بعضها إلى بعض بالخط (mufradat)؛ أكتبني هذه القصيدة أي أملها علي (sihah)؛ استكتبه الشيء أي سأله أن يكتبه له (sihah;tahdhib)
- **B003** bağlayıcı olarak hükme bağlama ve belirleme — yükümlülük, hüküm veya yazgı · size zorunlu kılındı · Tanrı belirledi, karara bağladı veya zorunlu kıldı
  الكتاب وهو الفرض (maqayis)؛ يقال للحكم الكتاب (maqayis)؛ يقال للقدر الكتاب (maqayis)؛ الكتاب الفرض والحكم والقدر (sihah)؛ الكتاب يوضع موضع الفرض (tahdhib)؛ يعبر عن الإثبات والتقدير والإيجاب والفرض والعزم بالكتابة (mufradat)؛ يعبر بالكتابة عن القضاء الممضى (mufradat)
- **B004** adını sicile yazma veya bir gruba dâhil etme — pay veya geçim tahsisatı için kaydolma · adını pay kaydına veya yönetim siciline yazdırmak · bizi tanıklar topluluğuna kat
  الكتبة الاكتتاب في الفرض والرزق (ayn;tahdhib)؛ اكتتب فلان أي كتب اسمه في الفرض (ayn;tahdhib)؛ اكتتب الرجل إذا كتب نفسه في ديوان السلطان (sihah)؛ فاكتبنا مع الشاهدين أي اجعلنا في زمرتهم (mufradat)
- **B005** özgürlük bedelini ödemeye dayalı özgürleşme sözleşmesi — kölenin bedelini ödeyerek özgürlüğünü kazanma sözleşmesi · özgürlük bedeli sözleşmesinin tarafı olan köle; bağlama göre sahibi · köleyle özgürlük bedeli ödemesine dayalı sözleşme yapmak · kölenin özgürlüğünü satın almak için yaptığı sözleşme
  المكاتب العبد يكاتبه سيده على نفسه (maqayis)؛ المكاتب الذي يشتري نفسه ويكاتب عليها (jamhara)؛ المكاتب العبد يكاتب على نفسه بثمنه فإذا سعى وأداه عتق (sihah)؛ معنى الكتاب والمكاتبة أن يكاتب الرجل عبده أو أمته على مال ينجمه عليه (tahdhib)؛ كتابة العبد ابتياع نفسه من سيده بما يؤديه من كسبه (mufradat)

## ق و م (root_001273) — identity root of قَيِّمَةٌ (w3)

- **B001** erkekler topluluğu ve yakın çevresi — aslen erkeklerden oluşan topluluk · bir erkeğin yandaşları ve yakın soy çevresi · topluluklar; çoğulun çoğulu
  القوم الرجال دون النساء؛ قوم كل رجل شيعته وعشيرته (ayn;tahdhib)؛ القوم الرجال دون النساء؛ ربما دخل النساء فيه على سبيل التبع (sihah)؛ القوم جماعة الرجال في الأصل دون النساء؛ وفي عامة القرآن أريدوا به والنساء جميعا (mufradat)؛ القوم جمع امرئ ولا يكون ذلك إلا للرجال؛ وربما استعير في غيرهم (maqayis)
- **B002** ayağa kalkma ve dik durma — ayağa kalkmak veya dikilmek · bir kez ayağa kalkma; iki bölüm arasındaki ayakta duruş · kökleri üzerinde dikili kalmış
  القومة ما بين الركعتين من القيام؛ قمت قياما؛ منها هامد ومنها قائم (ayn;tahdhib)؛ قام الرجل قياما؛ القومة المرة الواحدة؛ قامت الدابة وقفت (sihah)؛ قيام بالشخص إما بتسخير أو اختيار؛ ساجدا وقائما؛ تركتموها قائمة على أصولها (mufradat)؛ قام قياما والقومة المرة الواحدة إذا انتصب (maqayis)
- **B003** bir işe kararlılıkla girişme [kalıp] — bu işi üstlenip kararlılıkla girişti
  قام بمعنى العزيمة؛ قام بهذا الأمر إذا اعتنقه؛ قيام عزم (maqayis)؛ القيام الذي هو العزم؛ إذا قمتم إلى الصلاة (mufradat)
- **B004** sürekli gözetip yönetme — işi gözeten, koruyan ve yürüten kişi · topluluğun işlerini yöneten kişi · her şeyi sürekli yöneten ve koruyan · onu taşıyamadı veya buna gücü yetmedi
  قيم القوم من يسوس أمرهم ويقومهم؛ القائم في الملك ونحوه الحافظ؛ القيوم (ayn)؛ قوام أهل بيته وقيام أهل بيته؛ الذي يقيم شأنهم؛ القيوم اسم من أسماء الله (sihah)؛ قيم القوم الذي يقومهم ويسوس أمرهم؛ القائم بالأمر؛ القيوم القائم على كل شيء (tahdhib)؛ قيام للشيء هو المراعاة للشيء والحفظ له؛ قوامين لله؛ القيوم القائم الحافظ لكل شيء (mufradat)؛ قام بهذا الأمر إذا اعتنقه؛ قوام الدين والحق أي به يقوم (maqayis)
- **B005** sürdürüp gereğini yerine getirme [kalıp] — bir şeyi sürdürmek, işler halde tutmak veya gereğini yerine getirmek · ibadetin ya da kitabın gereklerini eksiksiz uygulamak
  أقام الشيء أي أدامه؛ يقيمون الصلاة (sihah)؛ أقمت الشيء وقومته فقام بمعنى استقام؛ إقام الصلاة (tahdhib)؛ إقامة الشيء توفية حقه؛ تقيموا التوراة والإنجيل؛ أقيموا الصلاة؛ مقيم الصلاة (mufradat)
- **B006** bir yerde kalma ve kalınan yer — bir yerde yerleşip kalmak · ayak basılan veya kalınan yer ya da süre; oturum veya toplanmış topluluk
  أقمت بالمكان إقامة ومقاما؛ المقام موضع القدمين؛ المقام والمقامة الموضع الذي تقيم فيه (ayn;tahdhib)؛ المقامة الإقامة؛ المقامة المجلس والجماعة من الناس؛ المقام موضع القيام أو الإقامة (sihah)؛ المقام يكون مصدرا واسم مكان القيام وزمانه؛ المقامة الإقامة؛ لا مقام لكم أي لا مستقر لكم (mufradat)
- **B007** başkasının yerini ve işlevini alma [kalıp] — onun yerine geçti veya adına görev yaptı
  القيمة أصله الواو لأنه يقوم مقام الشيء (sihah)؛ قام فلان مقام فلان إذا ناب عنه؛ يقومان مقامهما (mufradat)؛ أصل القيمة الواو وأصله أنك تقيم هذا مكان ذاك (maqayis)
- **B008** düzgünlük, denge ve doğru yoldan sapmama — düzgün ve dengeli olmak; doğru yoldan ayrılmamak · düzgün, dengeli ve doğru
  رمح قويم ورجل قويم؛ القيمة الملة المستقيمة؛ إذا انقاد واستمرت طريقته فقد استقام (ayn)؛ الاستقامة الاعتدال؛ استقام له الأمر؛ قومت الشيء فهو قويم أي مستقيم؛ القوام العدل؛ دينا قيما (sihah)؛ الاستقامة على الطاعة؛ القيم هو المستقيم؛ أقوم كلاما أي أعدل كلاما (tahdhib)؛ الاستقامة في الطريق الذي يكون على خط مستو؛ استقامة الإنسان لزومه المنهج المستقيم؛ دينا قيما أي ثابتا (mufradat)
- **B009** ayakta tutan dayanak ve geçim temeli — bir şeyi ayakta tutan dayanak, düzen ve geçim temeli
  هذا الأمر لا قومية له أي لا قوام له؛ القوام من العيش ما يقيمك ويغنيك؛ القيام العماد؛ قوام كل شيء ما استقام به (ayn)؛ قوام الأمر نظامه وعماده؛ قوام الأمر ملاكه؛ جعل الله لكم قياما (sihah)؛ قوام الأمر وملاكه؛ تقيمكم فتقومون بها؛ قوام الجسم تمامه؛ قوام كل شيء ما استقام به (tahdhib)؛ القيام والقوام اسم لما يقوم به الشيء؛ جعلها مما يمسككم؛ قياما للناس أي قواما لهم يقوم به معاشهم ومعادهم (mufradat)؛ قوام الدين والحق أي به يقوم (maqayis)
- **B010** değer biçme ve belirlenen bedel — değer biçmeyle belirlenen bedel · malın değerini belirlemek veya ulaştığı bedeli bildirmek
  القيمة ثمن الشيء بالتقويم؛ تقاوموا فيما بينهم (ayn)؛ قومت السلعة؛ استقمت السلعة؛ القيمة واحدة القيم (sihah)؛ القيمة ثمن الشيء بالتقويم؛ تقاوموه فيما بينهم؛ استقمت المتاع أي قومته؛ قامت الأمة مائة دينار أي بلغت قيمتها (tahdhib)؛ تقويم السلعة بيان قيمتها (mufradat)؛ قومت الشيء تقويما؛ أصل القيمة الواو (maqayis)
- **B011** insanın boyu ve düzgün beden yapısı — insanın boyu ve beden uzunluğu · düzgün ve güzel boy; beden yapısı
  القامة مقدار قيام الرجل؛ قوام الجسم تمامه وطوله (ayn)؛ قوام الرجل قامته وحسن طوله؛ قامة الإنسان قده (sihah)؛ القامة قامة الرجل؛ حسن القامة والقمة والقومية؛ قوام الجسم تمامه (tahdhib)؛ تقويم الإنسان في أحسن تقويم؛ انتصاب القامة (mufradat)؛ القوام الطول الحسن؛ القومية القوام والقامة (maqayis)
- **B012** düzeneğin dik, taşıyıcı veya tutulan parçası — kuyu makarası veya ona bağlı donanım · kuyu başındaki insan biçimli yapı diye aktarılmış, fakat yanlış sayılmış yorum · kılıç sapı veya yatak, masa ve hayvanın dik duran parçası · çiftçinin elinde tuttuğu ahşap parça
  القامة مقدار قيام الرجل كهيئة الرجل يبنى على شفير بئر؛ قائم السيف مقبضه؛ قائمة السرير والخوان والدابة (ayn)؛ القامة البكرة بأداتها؛ قائم السيف وقائمته مقبضه؛ القائمة واحدة قوائم الدواب؛ المقوم الخشبة التي يمسكها الحراث (sihah)؛ القامة البكرة التي يستقى بها الماء؛ النعامة الخشبة المعترضة ثم تعلق القامة؛ قائم السيف مقبضه وما سوى ذلك فهو قائمة (tahdhib)؛ القامة البكرة بأداتها (maqayis)
- **B013** ölülerin diriltildiği ve insanların yargı için kalktığı gün — ölülerin diriltildiği ve insanların yargı için ayağa kalktığı son gün
  القيامة يوم البعث يقوم الخلق بين يدي القيوم (ayn)؛ يوم القيامة معروف (sihah)؛ القيامة يوم البعث يوم يقوم فيه الخلق بين يدي الحي القيوم (tahdhib)؛ القيامة عبارة عن قيام الساعة؛ يوم يقوم الناس لرب العالمين (mufradat)
- **B014** karşılıklı direnip mücadele etme [kalıp] — ona karşı durup mücadele etmek; tarafların birbirine karşı koyması
  قاومته في كذا أي نازلته (ayn)؛ قاومه في المصارعة وغيرها؛ تقاوموا في الحرب أي قام بعضهم لبعض (sihah)؛ ما زلت أقاوم فلانا في هذا الأمر أي أنازله (tahdhib)
- **B015** tam ve denk ağırlıktaki para — ölçün ağırlığa tam denk gelen, ağır basmayan para
  دنانير قوم وقيم ودينار قائم أي مثقال سواء لا يرجح (ayn)؛ دنانير قوم وقيم ودينار قائم إذا كان مثقالا سواء لا يرجح (tahdhib)
- **B016** donup akmama veya yorulup ilerleyememe [kalıp] — su dondu veya akmaz halde kaldı · binek hayvanı durdu veya yorulup yürüyemedi
  قام الماء جمد؛ قامت الدابة وقفت (sihah)؛ قامت لفلان دابته إذا كلت أو عيت فلم تسر (tahdhib)
- **B017** güneşin tam tepede olduğu öğle ortası — güneşin ortada, günün iki yarısının dengede olduğu öğle vakti
  قام قائم الظهيرة إذا قامت الشمس وكاد الظل يعقل (ayn;tahdhib)؛ قام ميزان النهار إذا انتصف؛ قام ميزان النهار فاعتدل (tahdhib)
- **B018** pazarın canlanıp satışların artması [kalıp] — pazar canlandı ve mallar alıcı buldu
  قامت السوق نفقت (sihah)؛ قامت السوق إذا نفقت ونامت إذا كسدت (tahdhib)
- **B019** bir beden bölümünün kişiye ağrı vermesi [kalıp] — sırtım veya gözlerim ağrıdı
  قام بي ظهري أي أوجعني؛ قامت بي عيناي؛ كل ما أوجعك من جسدك فقد قام بك (tahdhib)
- **B020** koyunun bacaklarını tutan hastalık — koyunun bacaklarını tutup onu ayağa kaldıran hastalık
  القوام داء يأخذ الشاة في قوائمها تقوم منه (sihah)؛ أخذها قوام وهو داء يأخذها في قوائمها تقوم منه (tahdhib)
- **B021** göz bebeği sağlamken görme yetisinin kaybolması — göz bebeği sağlam kaldığı halde görmeyen göz
  عين قائمة ذهب بصرها والحدقة صحيحة (ayn)؛ العين القائمة أن يذهب بصرها والحدقة صحيحة (tahdhib)

===== _commentary/v16/out/s098/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 98:3, and ## Buluşmalar) =====
## Mühürlü yazı: getirilir, açılır, okunur

Surenin belgeleri elle tutulur nesnelerdir. Kitap kelimesinin kökü bir şeyi bir şeye eklemek, dikmektir: {ar:أصل الكتب ضمك الشيء إلى الشيء, tr:aslü'l-ketbi dammüke'ş-şey'e ile'ş-şey', gloss:ketbin aslı bir şeyi bir şeye katıp birleştirmendir, source:"ك ت ب,B001"}; {ar:كتبت السقاء إذا خرزته, tr:ketebtü's-sikâe izâ harraztühû, gloss:su tulumunu diktim, source:"ك ت ب,B001"}. Yazı, harflerin deri parçaları gibi birbirine dikilmesidir: {ar:في التعارف ضم الحروف بعضها إلى بعض بالخط, tr:fi't-teâruf dammü'l-hurûf, gloss:yaygın kullanımda harfleri yazıyla birbirine katmak, source:"ك ت ب,B002"}. Sayfa kelimesi açılıp serilmiş bir yüzeydir: {ar:الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها, tr:es-suhuf vâhidetühâ sahîfe, gloss:suhuf, tekili sahîfe; üzerine yazılan beyaz deri ya da parşömen parçası, source:"ص ح ف,B002"}. Bu yapraklar iki kapak arasında toplanınca mushaf olur: {ar:جعل جامعا للصحف المكتوبة بين الدفتين, tr:cuile câmian li's-suhufi'l-mektûbe beyne'd-deffeteyn, gloss:yazılı yaprakları iki kapak arasında toplayan kılındı, source:"ص ح ف,B003"}.

İlk ayetteki münfekkîn kelimesinin kökü bu nesneye de uzanır: {ar:فككت الشيء فانفك ككتاب مختوم تفك خاتمه, tr:fekektü'ş-şey'e fenfekke ke-kitâbin mahtûmin tefükkü hâtemehû, gloss:şeyi çözdüm, o da çözüldü; mühürlü bir mektubun mührünü açman gibi, source:"ف ك ك,B001"}. Bu açıklama infikâkın köküyle kitabı tek cümlede birleştirir. Birinci ayetin düz anlamı ayrılmamaktır; arka planında ise kapalı bir mektup ve mührün henüz kırılmamış olması duyulur. Mühürü açacak olan şey ayetin sonunda gelir: {ar:ٱلْبَيِّنَةُ, tr:el-beyyine, gloss:apaçık kanıt, source:98:1}; kök anlamı {ar:البيان الكشف عن الشيء, tr:el-beyânü el-keşfü ani'ş-şey', gloss:beyan, bir şeyi açığa çıkarmaktır, source:"ب ي ن,B005"}.

İkinci ayet bu kanıtı bir taşıyıcı ve bir eylem olarak gösterir: {ar:رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ, tr:resûlün mina'llâhi yetlû suhufen mutahhera, gloss:Allah'tan, tertemiz sayfaları okuyan bir elçi, source:98:2}. Resûl hem taşınan söz hem taşıyandır: {ar:الرسول يقال للقول المتحمل وتارة لمتحمل القول, tr:er-resûlü yukâlü li'l-kavli'l-mütehammel, gloss:resûl, yüklenilen söze de sözü yüklenene de denir, source:"ر س ل,B002"}; aynı kök acele etmeden okumayı da adlandırır: {ar:على رسلك أي اتئد فيه وترسل في قراءته, tr:alâ rislik, gloss:yavaş ol, okuyuşunda ağır ve tane tane git, source:"ر س ل,B004"}. Tilâvet ise izlemektir: {ar:تلاوة القرآن لأنه يتبع آية بعد آية, tr:tilâvetü'l-Kur'ân li-ennehû yetbau âyeten ba'de âye, gloss:Kur'an'ın tilâveti, ayetin ayeti izlemesindendir, source:"ت ل و,B002"}. Mühür açıldıktan sonra okuyan, satırları birbiri ardınca izler. Yapraklar {ar:مُّطَهَّرَةًۭ, tr:mutahhera, gloss:arındırılmış, source:98:2} olarak nitelenir: {ar:أصل واحد صحيح يدل على نقاء وزوال دنس, tr:aslün vâhidün yedüllü alâ nekâin ve zevâli denes, gloss:temizliğe ve kirin gitmesine delalet eden tek kök, source:"ط ه ر,B001"}; beyaz derinin üstünde leke yoktur. Üçüncü ayet açılan yaprakların içine bakar: {ar:فِيهَا كُتُبٌۭ قَيِّمَةٌۭ, tr:fîhâ kütübün kayyime, gloss:içlerinde dosdoğru yazılar vardır, source:98:3}; dikilip birleştirilmiş yazılar dimdik durur, {ar:قومت الشيء فهو قويم أي مستقيم, tr:kavvemtü'ş-şey'e fehüve kavîm, gloss:şeyi doğrulttum, o da düzgün, dosdoğru oldu, source:"ق و م,B008"}.

Dördüncü ayet aynı aktarımı alanların tarafından görür: {ar:ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ, tr:ellezîne ûtu'l-kitâb, gloss:kendilerine kitap verilenler, source:98:4}. Gelmek, getirmek ve vermek tek köktür: {ar:آتاه إيتاء أي أعطاه وآتاه أيضا أي أتى به, tr:âtâhu îtâen, gloss:ona verdi; ayrıca onu getirdi, source:"ء ت ي,B001"}. Birinci ayetteki ta'tiyehüm ("onlara gelinceye kadar") ile dördüncü ayetteki ûtû ("verildi") aynı hareketin iki ucudur; ayetin sonundaki {ar:جَآءَتْهُمُ ٱلْبَيِّنَةُ, tr:câet'hümü'l-beyyine, gloss:apaçık kanıt onlara geldi, source:98:4} de bu getirişi tekrarlar: {ar:جاء بكذا: استحضره, tr:câe bi-kezâ, gloss:onu getirip hazır etti, source:"ج ي ء,B004"}.

Kur'an bu nesneyi başka yerlerde de sahneler. Abese suresinde Allah zikri {ar:فِى صُحُفٍۢ مُّكَرَّمَةٍۢ, tr:fî suhufin mükerreme, gloss:değerli sayfalarda, source:80:13}, {ar:مَّرْفُوعَةٍۢ مُّطَهَّرَةٍۭ, tr:merfûatin mutahhera, gloss:yüceltilmiş, arındırılmış, source:80:14}, {ar:بِأَيْدِى سَفَرَةٍۢ, tr:bi-eydî sefera, gloss:yazıcıların ellerinde, source:80:15} diye anlatır; surenin ikinci ayetinin en yakın eşidir ve yaprakları tutan elleri de gösterir. Tâhâ suresinde inkârcılar "Rabbinden bize bir ayet getirmeli değil miydi" deyince cevap verilir: {ar:أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:e-ve lem te'tihim beyyinetü mâ fi's-suhufi'l-ûlâ, gloss:önceki sayfalarda olanın apaçık kanıtı onlara gelmedi mi, source:20:133}; gelmek, beyyine ve suhuf bir arada. Müddessir suresinde inkârcıların her biri sayfaların kendisine açılmış olarak teslim edilmesini ister: {ar:أَن يُؤْتَىٰ صُحُفًۭا مُّنَشَّرَةًۭ, tr:en yü'tâ suhufen müneşşera, gloss:kendisine açılıp serilmiş sayfalar verilmesini, source:74:52}. A'lâ suresi bu sayfaları adlarıyla anar: {ar:صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ, tr:suhufi İbrâhîme ve Mûsâ, gloss:İbrahim'in ve Musa'nın sayfaları, source:87:19}. Tûr suresi serilmiş parşömen üzerine yazılmış bir kitaba yemin eder {source:52:3}, Tekvîr suresi ise kıyamette sayfaların açılmasını haber verir: {ar:وَإِذَا ٱلصُّحُفُ نُشِرَتْ, tr:ve ize's-suhufu nüşirat, gloss:sayfalar açılıp serildiğinde, source:81:10}. Vâkıa suresi örtülü bir kitaptan ve temizliğin şartından söz eder: {ar:فِى كِتَٰبٍۢ مَّكْنُونٍۢ, tr:fî kitâbin meknûn, gloss:korunmuş, örtülü bir kitapta, source:56:78}, {ar:لَّا يَمَسُّهُۥٓ إِلَّا ٱلْمُطَهَّرُونَ, tr:lâ yemessühû ille'l-mutahharûn, gloss:ona ancak arındırılmışlar dokunur, source:56:79}. Okuyan elçi formülü Cuma suresinde aynen geçer: {ar:رَسُولًۭا مِّنْهُمْ يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِهِۦ وَيُزَكِّيهِمْ, tr:resûlen minhüm yetlû aleyhim âyâtihî ve yüzekkîhim, gloss:içlerinden, onlara ayetlerini okuyan ve onları arındıran bir elçi, source:62:2}; Bakara suresinde İbrahim aynı elçiyi dua ile ister {source:2:129}. Ankebût suresi ise okuyuşu elle yazmaktan ayırır: {ar:وَمَا كُنتَ تَتْلُوا۟ مِن قَبْلِهِۦ مِن كِتَٰبٍۢ وَلَا تَخُطُّهُۥ بِيَمِينِكَ, tr:ve mâ künte tetlû min kablihî min kitâbin ve lâ tehuttuhû bi-yemînik, gloss:bundan önce bir kitap okumuyordun, onu sağ elinle de yazmıyordun, source:29:48}. Müzzemmil suresindeki emir, {ar:وَرَتِّلِ ٱلْقُرْءَانَ تَرْتِيلًا, tr:ve rattili'l-Kur'âne tertîlâ, gloss:Kur'an'ı tane tane oku, source:73:4}, resûl kökündeki ağır okuyuşun yanına konabilir.

Kaynaklar: 98:1 مُنفَكِّينَ ف ك ك B001; 98:1 ٱلْكِتَٰبِ ك ت ب B001; 98:3 كُتُبٌ ك ت ب B002; 98:2 صُحُفًا ص ح ف B002 B003; 98:2 مُّطَهَّرَةً ط ه ر B001; 98:3 قَيِّمَةٌ ق و م B008; 98:2 يَتْلُوا۟ ت ل و B002; 98:2 رَسُولٌ ر س ل B002 B004; 98:1 تَأْتِيَهُمُ ء ت ي B001; 98:4 أُوتُوا۟ ء ت ي B001; 98:4 جَآءَتْهُمُ ج ي ء B004; 98:1 ٱلْبَيِّنَةُ ب ي ن B005

## Eğri olanın doğrultulması: ayak, ateş üstündeki çubuk, mızrak, ayakta duran beden

Hanif kelimesi bedensel bir eğrilikten başlar: {ar:الحنف اعوجاج في الرجل إلى داخل, tr:el-hanefü i'vicâcün fi'r-ricli ilâ dâhil, gloss:hanef, ayağın içe doğru eğri olmasıdır, source:"ح ن ف,B001"}. Kelime sonra bir meyle dönüşür: {ar:الحنيف المائل إلى الدين المستقيم, tr:el-hanîfü el-mâilü ile'd-dîni'l-müstakîm, gloss:hanif, dosdoğru dine meyledendir, source:"ح ن ف,B003"}. Bu tek tanım surenin üç kelimesini, hunefâ, dîn ve kayyime kelimelerinin kökünü, aynı cümlede toplar. Kayyime ve yükîmû ayağa kalkmaktan, dik durmaktan gelir: {ar:رمح قويم ورجل قويم, tr:rumhun kavîmün ve racülün kavîm, gloss:düz mızrak, düzgün adam, source:"ق و م,B008"}; {ar:أقمت الشيء وقومته فقام بمعنى استقام, tr:ekamtü'ş-şey'e ve kavvemtühû fekâme, gloss:şeyi doğrulttum, o da dikildi, yani dosdoğru oldu, source:"ق و م,B005"}. Kökün nesnelerdeki karşılığı da dik duran parçalardır: {ar:قائم السيف مقبضه؛ قائمة السرير والخوان والدابة, tr:kâimü's-seyf, kâimetü's-serîr, gloss:kılıcın kabzası; sedirin, sofranın ve hayvanın ayağı, source:"ق و م,B012"}.

Doğrultmanın aleti, salâtın kökünde durur: {ar:صليت العود بالنار, tr:salleytü'l-ûde bi'n-nâr, gloss:çubuğu ateşte ısıtıp yumuşattım, source:"ص ل و,B001"}. Eğri bir dal ateşe tutulur, ısındıkça yumuşar, el onu düz bir hatta tutar, soğuyunca düz bir sap olarak kalır. Namazın kendisi de bir beden düzenidir: {ar:الصلاة من المخلوقين القيام والركوع والسجود, tr:es-salâtü mine'l-mahlûkîn el-kıyâmü ve'r-rukûu ve's-sücûd, gloss:yaratılmışlardan salât, ayakta durmak, eğilmek ve secde etmektir, source:"ص ل و,B003"}. Üçüncü ve beşinci ayetler böylece bir doğrultma olarak duyulabilir. Üçüncü ayette yazılar {ar:قَيِّمَةٌۭ, tr:kayyime, gloss:dosdoğru, source:98:3}, eğrilik taşımayan düz bir mızrak gibidir. Beşinci ayette kulluk edenler {ar:حُنَفَآءَ, tr:hunefâ, gloss:hanifler olarak, source:98:5}, yani eğri ayaktan doğruya meyledenlerdir; {ar:وَيُقِيمُوا۟ ٱلصَّلَوٰةَ, tr:ve yükîmu's-salât, gloss:namazı kılsınlar, source:98:5} sözünde ikame, bir şeyi dikip ayakta tutmaktır ve salâtın kökü ateş üstündeki çubuğu taşır; ayet de bütünü {ar:دِينُ ٱلْقَيِّمَةِ, tr:dînü'l-kayyime, gloss:dosdoğru din, source:98:5} diye adlandırır. Kayyime kelimesi üçüncü ayette kitapların, beşinci ayette dinin niteliğidir; kitapların doğruluğu ile kulluk edenlerin doğrulması aynı kelimeyle bağlanır.

Kur'an kitabı aynı kelimeyle niteler. Kehf suresi Allah'a övgüyle açılır: {ar:ٱلْحَمْدُ لِلَّهِ ٱلَّذِىٓ أَنزَلَ عَلَىٰ عَبْدِهِ ٱلْكِتَٰبَ وَلَمْ يَجْعَل لَّهُۥ عِوَجَا, tr:el-hamdü li'llâhi'llezî enzele alâ abdihi'l-kitâbe ve lem yec'al lehû ivecâ, gloss:kuluna kitabı indiren ve onda hiçbir eğrilik kılmayan Allah'a hamd olsun, source:18:1}, ardından {ar:قَيِّمًۭا, tr:kayyimâ, gloss:dosdoğru, source:18:2}. Eğriliğin yokluğu ile kayyim olmak yan yana konmuştur. Zümer suresi Kur'an'ı {ar:غَيْرَ ذِى عِوَجٍۢ, tr:gayra zî ivec, gloss:eğriliği olmayan, source:39:28} diye niteler. Tîn suresinde insanın bedeni bu kökle anılır: {ar:لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ, tr:lekad halakne'l-insâne fî ahseni takvîm, gloss:andolsun, insanı en güzel biçimde, en düzgün duruşta yarattık, source:95:4}. Fetih suresinde Peygamber'in yanındakiler {ar:تَرَىٰهُمْ رُكَّعًۭا سُجَّدًۭا, tr:terâhüm rukkean succedâ, gloss:onları rükû ve secde ederken görürsün, source:48:29} diye anlatılır; aynı ayette benzetmeleri, gövdesi üstünde dikilen bir ekindir: {ar:فَٱسْتَغْلَظَ فَٱسْتَوَىٰ عَلَىٰ سُوقِهِۦ, tr:festağleza festevâ alâ sûkıh, gloss:kalınlaştı ve gövdesi üzerinde dimdik durdu, source:48:29}. Eğilen beden ile dimdik duran ekin aynı ayettedir.

Kaynaklar: 98:5 حُنَفَآءَ ح ن ف B001 B003; 98:3 قَيِّمَةٌ ق و م B008; 98:5 ٱلْقَيِّمَةِ ق و م B008; 98:5 وَيُقِيمُوا۟ ق و م B005; 98:5 وَيُقِيمُوا۟ ق و م B012; 98:5 ٱلصَّلَوٰةَ ص ل و B001 B003

## Buluşmalar

En yoğun buluşma beşinci ayetteki salât kelimesindedir. Kökü bir yandan ateşte ısıtılıp düzeltilen çubuğu, {ar:صليت العود بالنار, tr:salleytü'l-ûde bi'n-nâr, gloss:çubuğu ateşte ısıtıp yumuşattım, source:"ص ل و,B001"}, öbür yandan ateşe girip yanan kâfiri, {ar:صلى الكافر نارا, tr:sale'l-kâfiru nârâ, gloss:kâfir ateşe girip yandı, source:"ص ل و,B001"}, adlandırır. Aynı ateş iki iş görür: eğri olanı doğrultur ya da yakar. Beşinci ayette ateş bir doğrultma aletidir; altıncı ayette inkâr edenlerin kaldığı yerdir. Doğrultma ile ocak sahneleri böylece tek bir kökün iki işlemi olarak birleşir ve surenin ikiye ayrılan yolunu taşır: kanıttan sonra doğrulup ayağa kalkanlar ve ateşte kalanlar. Aynı kök tuzağı da adlandırır; ama surede salât tuzaktan sıyrılmış olanların fiilidir.

Münfekkîn kelimesi üç sahneyi bir noktada tutar. Kökü tuzaktan kurtulan ceylanı, mührü açılan mektubu ve çözülen rehni anlatır. Birinci ayette bu kelime olumsuzdur: ip çözülmemiş, mühür açılmamış, rehin kurtarılmamıştır, ve bütün bunlar kanıtın gelişine bağlıdır. Rehnin çözülmesini anlatan cümlede infikâkın ve ihlâsın kökü yan yanadır, tuzaktan kurtulmayı anlatan cümlelerde de; bu yüzden birinci ayetteki çözülmeme ile beşinci ayetteki muhlisîn, hem avın hem borçlunun kurtuluşu olarak duyulur. Yazı ile kenet de aynı kelimede buluşur: mühürlü mektubun açılması ile iki çenenin ayrılması tek cümlede verilir ve dördüncü ayette açılan yazının ardından gelen ayrılık bunun devamıdır.

Teferruk kelimesi kenet ile yol sahnesini birleştirir. En'âm suresinde yan yollara uyunca insanların yoldan ayrı düşmesi {source:6:153}, hem çatallanan yolu hem bölünen topluluğu tek cümlede gösterir. Müşriklerin kökü ana yoldan ayrılan küçük patikaları adlandırdığı için dördüncü ayetteki ayrılık arka planda bir çatal noktasına, beşinci ayetteki hunefâ ise yan patikadan ana yola dönüşe dönüşür. Yol ile binek sahnesi müzellel kelimesinde birleşir: yürünmekle düzleşen yol ile katranla uysallaşan deve aynı kelimeyle anlatılır ve inde kelimesinin kökü ikisinin de tersini, yoldan sapan ve dizgini çeken deveyi verir. Doğrultma ile yol da kayyime kelimesinde birleşir: dik duran beden ile düz hat üzerindeki yol aynı kökle anlatılır; En'âm suresinde Peygamber'e söyletilen söz {source:6:161} yolu, kayyim olanı, hanifi ve müşrikleri tek ayette toplar.

Arındırma ile ekim zekâtta birleşir. Zekât hem bir temizliktir hem ekinin büyümesi ve hurmanın ürünüdür. Tâhâ suresinde surenin sekizinci ayetinin bahçesi tam olarak bu kelimeyle bağlanır: Adn cennetleri {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76}. Beşinci ayetteki zekât, sekizinci ayetteki bahçenin tohumu gibi durur. Arındırma ile hesap da hayr ve şerr kelimelerinde buluşur: süzmenin iki ürünü, karşılığın iki ölçüsüne dönüşür, iyiliğe iyilik ve kötülüğe kötülük.

Örtü ile ocak da kesişir: küfrün kökü üstü örtülmüş külü adlandırır. Örtü ile ekim ise aynı kelimede, tohumu örten çiftçide buluşur. Bakara suresindeki temsil {source:2:266} bu sahnelerin üçünü birden tutar: altından ırmaklar akan hurma bahçesi ve onu yakan ateşli kasırga. Altıncı ve sekizinci ayetler aynı sözü, hâlidîne fîhâ, ateş ve bahçe için kullanır; hulûdun kökü bir yandan ateşin içinde kalan ocak taşlarını, öbür yandan bir yerde yerleşip kalmayı adlandırır. Kalmanın iki yeri böylece aynı kelimede yan yana durur.

Bu buluşmalar surenin hareketini taşır. Birinci ayette bir şey kapalıdır: ilmek düğümlü, mühür kırılmamış, topluluk kendi hâlinde. Kanıt bir elçinin elinde, arındırılmış sayfalar olarak gelir ve okunur. Dördüncü ayette topluluk bu kanıtın ardından bölünür. Beşinci ayet çıkış yolunu tek cümlede verir: işaretli, düzleşmiş, dosdoğru bir yol; katkısından süzülmüş bir din; ateşte doğrultulan bir beden; tuzaktan sıyrılış; ürün veren bir ekin. Altıncı ve yedinci ayetler sonucu iki uca ayırır. Sekizinci ayet bir yerleşmeyle biter: Rableri katında, örtülü bir bahçede, ebedî bir kalış ve iki tarafın birbirinden razı olduğu kapanmış bir hesap.

