Focus: 105:3. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/105_3/D.r13/context.md =====
# 105:3 — focus

وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ

Anchor translation (canonical reading, reference only):

Ve üzerlerine sürü sürü kuşlar gönderdi.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَأَرْسَلَ | أَرْسَلَ | ر س ل | CONJ;V |
| 2 | عَلَيْهِمْ | عَلَىٰ |  | P;PRON |
| 3 | طَيْرًا | طَيْر | ط ي ر | N |
| 4 | أَبَابِيلَ | أَبَابِيل | ء ب ل | ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 105 — full text (context; no pericope)

- 105:1 أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَٰبِ ٱلْفِيلِ
- 105:2 أَلَمْ يَجْعَلْ كَيْدَهُمْ فِى تَضْلِيلٍۢ
- 105:3 ◀ focus وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ
- 105:4 تَرْمِيهِم بِحِجَارَةٍۢ مِّن سِجِّيلٍۢ
- 105:5 فَجَعَلَهُمْ كَعَصْفٍۢ مَّأْكُولٍۭ


===== _commentary/v16/work/105_3/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ر س ل (root_000563) — identity root of وَأَرْسَلَ (w1)

- **B001** bir şeyi gönderme veya serbest bırakma — göndermek veya salıvermek · gönderme, yöneltme veya serbest bırakma · gönderilmiş rüzgarlar veya görevlendirilmiş melekler
  أصل واحد يدل على الانبعاث والامتداد (maqayis)؛ أرسلت فلانا في رسالة والمرسلات الرياح ويقال الملائكة (sihah)؛ إرسال الله أنبياءه وإرسال الشياطين تخليتهم وإياهم (tahdhib)؛ الإرسال يقابل الإمساك (mufradat)
- **B002** haber taşıyıcısı veya taşınan haber — elçi veya haberci · taşınan ileti veya haber · ileti veya taşınan haber · iletiler veya taşınan haberler · elçiler veya haberciler
  الرسول معروف (maqayis)؛ الرسول بمعنى الرسالة والرسائل جمع الرسالة (ayn)؛ أرسلت فلانا في رسالة فهو مرسل ورسول والرسول أيضا الرسالة (sihah)؛ الرسول معناه الذي يتابع أخبار الذي بعثه (tahdhib)؛ الرسول يقال للقول المتحمل وتارة لمتحمل القول والرسالة (mufradat)
- **B003** harekette veya uzanışta yumuşak akıcılık — rahat ve yumuşak ilerleyiş · rahat yürüyen, bacakları ve eklemleri yumuşak dişi deve · rahat yürüyen deve · düz ve salık saç · saçın düzleşip salık duruma gelmesi · hızlı veya rahatça ilerleyen deve sürüleri · uzun ya da yumuşak ve rahat hareketli bacaklar
  فالرسل السير السهل وناقة رسلة لينة المفاصل وشعر رسل (maqayis)؛ ناقة رسلة القوائم سلسة لينة المفاصل (ayn)؛ شعر رسل وبعير رسل وناقة رسلة وإبل مراسيل (sihah)؛ الرسل الذي فيه لين واسترخاء وناقة مرسال رسلة القوائم (tahdhib)؛ ناقة رسلة سهلة السير وإبل مراسيل منبعثة انبعاثا سهلا (mufradat)
- **B004** acele etmeden ölçülü ilerleme — Acele etme; yavaş ve sakin ol · işte veya konuşmada sakin, ağırbaşlı ve temkinli davranma · metni acele etmeden açık seçik okuma
  على رسلك أي على هينتك (maqayis)؛ تكلم على رسلك والترسل في الأمر والمنطق كالتمهل والتوقر والتثبت (ayn)؛ على رسلك أي اتئد فيه وترسل في قراءته (sihah)؛ الترسل من الرسل في الأمور والمنطق كالتمهل والتوقر والتثبت والترسيل التحقيق بلا عجلة (tahdhib)؛ على رسلك إذا أمرته بالرفق (mufradat)
- **B005** peş peşe gelen topluluklar — deve, koyun veya başka varlıklardan oluşan sürü · gruplar halinde, birbirinin ardından
  الرسل ما أرسل من الغنم إلى الرعي وجاء القوم أرسالا يتبع بعضهم بعضا (maqayis)؛ الرسل القطيع من كل شيء وجمعه أرسال (ayn)؛ الرسل القطيع من الإبل والغنم وجاءت الخيل أرسالا قطيعا قطيعا (sihah)؛ جاءت الإبل أرسالا رسل بعد رسل والرسل قطيع من الإبل (tahdhib)؛ جاءوا أرسالا أي متتابعين (mufradat)
- **B006** bol ve sürekli gelen süt — süt; özellikle bol ve sürekli gelen süt · hayvanlarından süt elde eder duruma gelmek
  الرِّسل اللبن لأنه يترسل من الضرع (maqayis)؛ والرسل اللبن (ayn)؛ والرسل أيضا اللبن وقد أرسل القوم أي صار لهم اللبن (sihah)؛ كثر الرسل العام أي كثر اللبن (tahdhib)؛ الرسل اللبن الكثير المتتابع الدر (mufradat)
- **B007** ısınıp güvenerek açılma — birine veya bir şeye ısınıp güvenmek · sana güvenip yanında rahat davranan kimse
  استرسلت إلى الشيء إذا انبعثت نفسك إليه وأنست (maqayis)؛ الاسترسال إلى شيء كالاستئناس والطمأنينة (ayn)؛ استرسل إليه أي انبسط واستأنس (sihah)؛ الاسترسال إلى الإنسان كالاستئناس والطمأنينة (tahdhib)
- **B008** karşılıklı iletişim ve eşlik — karşılıklı haberleşmek veya birbirine ayak uydurmak · atışmada veya başka bir uğraşta eşlik eden kişi · şarkıda veya işte bir öncekinin ardından giden eşlikçi
  رسيل الرجل الذي يقف معه في نضال أو غيره (maqayis)؛ راسله مراسلة فهو مراسل ورسيل الرجل الذي يراسله في نضال أو غيره (sihah)؛ العرب تسمي المراسل في الغناء والعمل المتالي (tahdhib)
- **B009** taliplerin haber gönderdiği dul veya ayrılmak üzere olan kadın [kalıp] — eşi ölmüş, boşanmış veya ayrılmak üzere olduğu için taliplerin haber gönderdiği kadın
  المرأة المراسل التي مات بعلها فالخطاب يراسلونها (maqayis)؛ امرأة مراسل كان لها زوج والخطاب يراسلونها الخطبة (ayn)؛ امرأة مراسل يموت زوجها أو أحست منه أنه يريد تطليقها (sihah)؛ امرأة مراسل وهي التي مات عنها زوجها أو طلقها (tahdhib)
- **B010** rahatlık ve gönül hoşluğuyla verme [kalıp] — sıkıntısında ve rahatlığında; gönül hoşluğuyla verirken
  النجدة الشدة والرسل الرخاء (maqayis)؛ في نجدتها ورسلها يريد الشدة والرخاء (sihah)؛ إلا من أعطى في رسلها أي بطيب نفس منه (tahdhib)
- **B011** özel adlandırma kümesi — kısa ok · iki damar · belirli bir topluluğun damızlık erkek devesi · aktarım zinciri kesintili söz · boncuklu kolye · başını henüz örtmeyen küçük kız
  الراسلان عرقان (maqayis)؛ المرسال سهم قصير (sihah)؛ هذا رسيل بني فلان أي فحل إبلهم وحديث مرسل والمرسلة القلادة وجارية رسل (tahdhib)

## ط ي ر (root_000962) — identity root of طَيْرًا (w3)

- **B001** kanatlı canlı ve uçuş — kuşlar; kuş türünden kanatlı canlı · kuş; havada uçan kanatlı canlı · kuşlar · uçmak; uçmuşçasına hızlanmak · uçma, uçuş · uçurmak, uçmaya yöneltmek · hızlı at · kuş desenli dokuma veya giysi · kuşu bol arazi
  الطير جمع طائر (maqayis;sihah;mufradat); الطائر كل ذي جناح يسبح في الهواء (mufradat); الطيران مصدر طار يطير (ayn;sihah); لكل من خف قد طار وكل سرعة (maqayis); فرس مطار للسريع وحديد الفؤاد (mufradat;ayn); المطير من البرود والثياب ما صور فيه صور الطيور (ayn); أرض مطارة كثيرة الطير (sihah)
- **B002** dağılıp yayılma — dağılmak, ayrılıp gitmek · ışığı ufka yayılmış tan · her yana yayılmış kötülük · havaya yayılmış toz · uzayıp dağılan saç · uzayıp yayılmış hörgüç ucu
  تطاير الشيء تفرق (maqayis;sihah); التطاير التفرق والذهاب (ayn); فجر مستطير إذا انتشر ضوؤه في الأفق (ayn); فجر مستطير أي فاش وغبار مستطار (mufradat); خذ ما طار من شعر رأسك أي ما انتشر (mufradat;sihah)
- **B003** belirtiyi uğur ya da uğursuzluk sayma — bir şeyi uğurlu ya da uğursuz saymak · uğursuzluk çıkarma; kötü sayılan belirti · kişiye yüklenen işi veya uğursuz payı · kuş hareketinden uğur ya da uğursuzluk çıkarma · uğursuzluk çıkarmayı reddeden söz · seni uğursuz saydık; ayrıca kaçırdık ya da kurtardık diye de açıklanır
  تطير من الشيء فاشتقاقه من الطير (maqayis); الطيرة مصدر قولك اطيرت أي تطيرت (ayn); الطائر من الزجر في التشؤم والتسعد (ayn); طائر الإنسان عمله الذي قلده (ayn;sihah); ألا إنما طائرهم عند الله أي شؤمهم (mufradat); كل إنسان ألزمناه طائره في عنقه أي عمله (mufradat)
- **B004** ağzı geniş kuyu [kalıp] — ağzı geniş kuyu · geniş ağızlı kuyu çukuru
  بئر مطارة إذا كانت واسعة الفم (maqayis); بئر مطارة واسعة الفم (sihah); جفر مطار (maqayis;sihah)
- **B005** öfkeli taşkınlık ve ölçüsüz atılganlık — öfke ve öfkeli taşkınlık · hafif ve düşünmeden davranan · taşkınlığının ve düşüncesizliğinin yanları · coşmuş, saldırgan köpek · yürekli, atılgan ve hızlı at
  الطيرة الغضب وسمي كذا لأنه يستطار له الإنسان (maqayis); في فلان طيرة وطيرورة أي خفة وطيش (sihah); ازجر أحناء طيرك أي جوانب خفتك وطيشك (sihah); كلب مستطير كما يقال للفحل هائج (ayn); فرس مستطار أي حديد الفؤاد ماض طيار (ayn); فرس مطار للسريع ولحديد الفؤاد (mufradat)
- **B006** kuşun durgunluğuyla anlatılan heybet veya bolluk [kalıp] — heybetten çıt çıkarmadan durmak · bolluk ve iyilik içinde olmak
  كأن على رؤوسهم الطير إذا سكنوا من هيبة (sihah); في الخصب وكثرة الخير قولهم في شيء لا يطير غرابه (sihah)

## ء ب ل (root_000006) — identity root of أَبَابِيلَ (w4)

- **B001** deve topluluğu, sahipliği ve bakım ustalığı — develer; tekili aynı kökten olmayan topluluk adı · çok sayıda ya da elde tutulan toplu develer · deve sahibi veya deve bakımında usta kimse · deve ve koyun bakımını iyi bilmek · develerin yanında durmamak ya da bakımlarını sürdürmemek
  الإبل معروفة ورجل آبل ومال مؤبل (maqayis)؛ الإبل لا واحد لها وإبل مؤبلة ورجل إبلي وأبل الرجل اتخذ إبلا (sihah)؛ إبل مؤبلة كثيرة وأبل الرجل إذا كثرت إبله وتأبل فلان إبلا (tahdhib)؛ الإبل يقع على البعران الكثيرة وأبل الرجل كثرت إبله ورجل آبل وأبل (mufradat)
- **B002** yaş otla yetinip sudan uzak durma — develerin veya yaban hayvanlarının yaş otla yetinip su içmemesi · suya gerek duymadan bulunduğu yerde kalan hayvan · yaş otla yetinip su içmeyen develer veya yaban hayvanları · erkeğin kadına yaklaşmaktan kaçınması
  بعير آبل في موضع لا يبرح يجتزئ عن الماء وتأبل الرجل عن المرأة (maqayis)؛ أبلت الإبل والوحش اجتزأت بالرطب عن الماء وأبل الرجل عن امرأته (sihah)؛ أبلت الوحش إذا جزأت بالرطب عن الماء وإبل أوابل قد جزأت (tahdhib)؛ أبل الوحشي اجتزأ عن الماء وتأبل الرجل عن امرأته (mufradat)
- **B003** ayrı ayrı veya art arda gelen topluluklar — ayrı kümeler halinde veya birbiri ardınca gelen topluluklar
  طيرا أبابيل أي يتبع بعضها بعضا (maqayis)؛ جاءت إبلك أبابيل أي فرقا وطير أبابيل (sihah)؛ طيرا أبابيل جماعات وقيل يتبع بعضها بعضا إبيلا إبيلا (tahdhib)؛ طيرا أبابيل أي متفرقة كقطعات إبل (mufradat)
- **B004** ağırlık, yükümlülük veya ayıp — ağırlık, ağır gelme, yükümlülük veya kınanma · üstün gelip direnmek · bunda senin için bir ayıp yok · giderilecek ihtiyaç veya öç
  أبل الرجل إذا غلب وامتنع والأبلة الثقل وذهبت أبلته (maqayis)؛ الأبلة الوخامة والثقل من الطعام وذهبت أبلته (sihah)؛ ما عليك فيه أبلة ولا أبنة أي لا عيب وخرجت من أبلته أي من تبعته ومذمته (tahdhib)
- **B005** yakacak odun demeti — yakacak odun demeti · sıkıntı üstüne sıkıntı
  الإبالة الحزمة من الحطب (maqayis)؛ الإبالة الحزمة من الحطب وضغث على إبالة (sihah)؛ ضغث على إبالة (tahdhib)؛ الإبالة الحزمة من الحطب (mufradat)
- **B006** Hristiyan manastır din görevlisi — Hristiyan manastır görevlisi, üst düzey din görevlisi veya çan çalan görevli
  الأبيل من رؤوس النصارى وهو الأبيلى (maqayis)؛ الأبيل الذي يضرب بالناقوس (jamhara)؛ الأبيل راهب النصارى (sihah)؛ الأبيل الراهب الرئيس وهم الأبيلون (tahdhib)
- **B007** iri bir hurma parçası — iri bir hurma parçası
  الأبلة الفدرة من التمر (maqayis)؛ الأُبُلَّة الفدرة من التمر (sihah)؛ الأبلة الفدرة من التمر (tahdhib)
- **B008** Basra yakınındaki kent ve ayrı bir yer adı — Basra yakınındaki kent · bir yer adı
  أبلى موضع (maqayis)؛ الأبلة مدينة إلى جنب البصرة (sihah)؛ الأبلة لأبلة البصرة (tahdhib)
- **B009** kendi boyuyla birlikte gelmek [kalıp] — kendi boyunun içinde, onlarla birlikte
  جاء فلان في أبلته وإبالته أي في قبيلته (tahdhib)
- **B010** öleni övgüyle anmak veya ardından üzülmek [kalıp] — öleni ölümünden sonra övgüyle anmak · ölen kişinin ardından üzülmek
  تأبل على الميت حزن عليه وأبلت الميت مثل أبنت (maqayis)؛ أبنت الميت تأبينا وأبلته تأبيلا إذا أثنيت عليه بعد وفاته (tahdhib)

===== _commentary/v16/out/s105/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 105:3, and ## Buluşmalar) =====
## Görmeye çağrı ve yanılan yargı

Sûre bir soruyla açılır ve bu soru okuru seyirci yerine koyar: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ, tr:elem tera keyfe feale rabbüke, gloss:Rabbinin ne yaptığını görmedin mi, source:105:1}. Olumsuz kurulmuş bu soru bir bilgi istemez, "evet" cevabını baştan varsayar; hitap edilen, olayı zaten bilen biri olarak konuşturulur. {ar:تَرَ, tr:tera, gloss:görürsün, source:105:1} fiilinin kökü önce gözün görmesidir, {ar:الرؤية بالعين, tr:er-ru'yetu bi'l-ayn, gloss:gözle görme, source:"ر ء ي,B001"}; ama iki nesne aldığında bilmek anlamına geçer, {ar:بمعنى العلم تتعدى إلى مفعولين, tr:bi-ma'ne'l-ilm teteaddâ ilâ mef'ûleyn, gloss:bilmek anlamında iki nesne alır, source:"ر ء ي,B002"}. Aynı kökten gelen "gördün mü?" sorusu ise bir dikkat çağrısıdır: {ar:يجري أرأيت مجرى أخبرني وكل ذلك فيه معنى التنبيه, tr:yecrî e-raeyte mecrâ ahbirnî ve küllü zâlike fîhi ma'ne't-tenbîh, gloss:"gördün mü" "bana haber ver" yerine geçer, hepsinde uyarma anlamı vardır, source:"ر ء ي,B013"}. Bu üç kat bir arada çalışır: olay bir sahne gibi göz önüne konur, gözle izlenmemiş olsa da gözle görülmüş kadar kesin bir bilgi sayılır ve dinleyenin dikkati ona çekilir. Kökün ettirgen biçimi bir adım daha atar: {ar:أريته الشيء فرآه, tr:ereytuhu'ş-şey'e fe-raâhu, gloss:ona şeyi gösterdim, o da gördü, source:"ر ء ي,B012"} ve {ar:وأرى الله الناس بفلان, tr:ve erallâhu'n-nâse bi-fulân, gloss:Allah insanlara falanca üzerinden (bir ibret) gösterdi, source:"ر ء ي,B012"}. Sûrede gösteren Rab, gösterilen ise filin sahipleridir; onlar bir sergi nesnesine dönüşür.

Bu sûrede kelimelerin kök ailesinden gelen imgeler, kelimenin kendi ayetindeki anlamının yerine geçmez, onun yanında duyulur: fil yine fildir, taş yine taştır; kök yalnızca arka planda ikinci bir ses verir. Bu ikinci ses burada şudur: sağlam görmeye çağrılan okurun karşısında, öbür tarafın kelimeleri yanılan görüşü taşır. {ar:ٱلْفِيلِ, tr:el-fîl, gloss:fil, source:105:1} kökünün bir dalı zayıf görüşü ve işaretleri yanlış okumayı adlandırır: {ar:رجل فَيِل الرأي, tr:raculun feyilu'r-ra'y, gloss:görüşü zayıf adam, source:"ف ي ل,B001"}, {ar:رجل فال أي ضعيف الرأي مخطئ الفراسة, tr:raculun fâl, ey daîfu'r-ra'y muhti'u'l-firâse, gloss:fâl adam, yani görüşü zayıf, sezgisi yanılan, source:"ف ي ل,B001"}. Bu ifadede "görüş" diye çevrilen kelime, {ar:تَرَ, tr:tera, gloss:görürsün, source:105:1} ile aynı köktendir. Böylece açılış ayetinin iki ucunda aynı kök iki zıt hâlde durur: okura "gör" denir, karşı tarafın adı ise görüşün çürüklüğünü fısıldar. Bu bir kök özdeşliği değil, bir aile imgesidir; fil kelimesi ayette yalnızca hayvanı söyler.

İkinci ayetin {ar:تَضْلِيلٍ, tr:tadlîl, gloss:saptırılma, yolunu kaybettirme, source:105:2} kelimesinin kökü yolda kaybolmanın yanında bir işte doğruyu bulamamayı da adlandırır: {ar:ضل في الأمر إذا لم يهتد له, tr:dalle fi'l-emr izâ lem yehtedi leh, gloss:bir işin yolunu bulamadığında "o işte saptı" denir, source:"ض ل ل,B001"}. Üçüncü ayetin kuşları, {ar:طَيْرًا, tr:tayran, gloss:kuşlar, source:105:3}, Arapçada fal bakılan şeydir: {ar:تطير من الشيء فاشتقاقه من الطير, tr:tetayyera mine'ş-şey', fe'ştikâkuhu mine't-tayr, gloss:bir şeyden uğursuzluk çıkardı; türeyişi kuştandır, source:"ط ي ر,B003"}, {ar:الطائر من الزجر في التشؤم والتسعد, tr:et-tâ'ir mine'z-zecr fi't-teşe'üm ve't-tese'ud, gloss:kuş, uğur ve uğursuzluk için okunan işarettir, source:"ط ي ر,B003"}. Burada kuşlar bir şeyin habercisi değildir; okunacak işaret olmaktan çıkıp doğrudan vurucunun kendisi olurlar. Dördüncü ayetin fiili {ar:تَرْمِيهِم, tr:termîhim, gloss:onları atıyordu, source:105:4} kökünde isabet etmeyen tahmini de taşır: {ar:رمى فلان يرمي إذا ظن ظنا غير مصيب, tr:ramâ fulânun yermî izâ zanne zannen gayra musîb, gloss:isabetsiz bir zanda bulunduğunda "attı" denir, source:"ر م ي,B009"}. Ayetteki atış ise hedefini bulur. Taşlar, {ar:بِحِجَارَةٍ, tr:bi-hicâratin, gloss:taşlarla, source:105:4}, aklı da adlandıran bir köktendir: {ar:العقل يسمى حجرا لأنه يمنع من إتيان ما لا ينبغي, tr:el-aklu yusemmâ hicran li-ennehû yemneu min ityâni mâ lâ yenbagî, gloss:akla "hicr" denir, çünkü yakışmayanı yapmaktan alıkoyar, source:"ح ج ر,B002"}. Kendilerini alıkoyacak "hicr"i olmayanlara, aynı kökün öbür anlamı, taş, iner.

Kur'an bu bağı kendisi sahneler. Fecr sûresinde Allah yeminlerini sıraladıktan sonra sorar: {ar:هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ, tr:hel fî zâlike kasemun li-zî hicr, gloss:bunda akıl sahibi için bir yemin var mı, source:89:5}; hemen ardından gelen ayet bu sûrenin açılış kalıbının aynısıdır: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ, tr:elem tera keyfe feale rabbüke bi-âd, gloss:Rabbinin Âd'a ne yaptığını görmedin mi, source:89:6}. Orada sahne Âd'dan Semûd'a ve Firavun'a uzanır ve {ar:فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ, tr:fe-sabbe aleyhim rabbüke sevta azâb, gloss:Rabbin üzerlerine bir azap kamçısı döktü, source:89:13} ile kapanır. "Hicr sahibi" ile "görmedin mi" yan yana durur: görmeye çağrılan, aklı olandır. İbrahim sûresinde Allah, yıkılmış zalimlerin yurtlarında oturanlara {ar:وَتَبَيَّنَ لَكُمْ كَيْفَ فَعَلْنَا بِهِمْ, tr:ve tebeyyene leküm keyfe fealnâ bihim, gloss:onlara ne yaptığımız size apaçık belli olmuştu, source:14:45} der; aynı "nasıl yaptı" burada açıkça görülmüş bir bilgi olarak geri gelir. En'âm sûresinde inkârcılara {ar:أَلَمْ يَرَوْا۟ كَمْ أَهْلَكْنَا مِن قَبْلِهِم, tr:elem yerav kem ehleknâ min kablihim, gloss:kendilerinden önce nice nesli helak ettiğimizi görmediler mi, source:6:6} denir; görmek yine tarihin bilgisi demektir.

Yanlış görmenin sahneleri de Kur'an'dadır. Âd kavmi vadilerine yönelen bulutu görür ve yanılır: {ar:قَالُوا۟ هَٰذَا عَارِضٌۭ مُّمْطِرُنَا, tr:kâlû hâzâ âridun mumtirunâ, gloss:"bu bize yağmur getirecek bir bulut" dediler, source:46:24}; ayetin devamı onun bir azap rüzgârı olduğunu söyler, sonraki ayet de sonucu gösterir: {ar:فَأَصْبَحُوا۟ لَا يُرَىٰٓ إِلَّا مَسَٰكِنُهُمْ, tr:fe-asbahû lâ yurâ illâ mesâkinuhum, gloss:sabaha yalnızca evleri görünür hâlde çıktılar, source:46:25}. Tûr sûresinde inkârcılar için {ar:وَإِن يَرَوْا۟ كِسْفًۭا مِّنَ ٱلسَّمَآءِ سَاقِطًۭا يَقُولُوا۟ سَحَابٌۭ مَّرْكُومٌۭ, tr:ve in yerav kisfen mine's-semâ'i sâkitan yekûlû sehâbun merkûm, gloss:gökten düşen bir parça görseler "üst üste yığılmış bulut" derler, source:52:44} denir. Firavun'un ailesi başlarına gelen kötülüğü {ar:يَطَّيَّرُوا۟ بِمُوسَىٰ وَمَن مَّعَهُۥٓ, tr:yettayyerû bi-mûsâ ve men meah, gloss:Musa'dan ve beraberindekilerden uğursuzluk çıkarırlar, source:7:131} ve Allah cevap verir: {ar:أَلَآ إِنَّمَا طَٰٓئِرُهُمْ عِندَ ٱللَّهِ, tr:elâ innemâ tâ'iruhum indallâh, gloss:bilin ki onların "kuşu" Allah katındadır, source:7:131}. Kuş falının düzeltildiği yer burasıdır: işaret insanın elinde değil, Allah katındadır. Mülk sûresinde inkârcılara {ar:أَوَلَمْ يَرَوْا۟ إِلَى ٱلطَّيْرِ فَوْقَهُمْ صَٰٓفَّٰتٍۢ وَيَقْبِضْنَ, tr:e-ve lem yerav ile't-tayri fevkahum sâffâtin ve yakbidn, gloss:üstlerinde kanat açıp kapayan kuşları görmediler mi, source:67:19} denir ve Nûr sûresinde aynı tekil hitap kuşları gösterir: {ar:أَلَمْ تَرَ أَنَّ ٱللَّهَ يُسَبِّحُ لَهُۥ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱلطَّيْرُ صَٰٓفَّٰتٍۢ, tr:elem tera ennallâhe yusebbihu lehû men fi's-semâvâti ve'l-ardi ve't-tayru sâffât, gloss:göklerde ve yerde olanların ve kanat çırpan kuşların Allah'ı tesbih ettiğini görmedin mi, source:24:41}. Bu sûrede kuşa bakmak bir kehanet değil, Rabbin işini görmektir.

Kur'an aynı zamanda belirleyici gücün görünmediğini de söyler. Ahzâb sûresinde Allah mü'minlere, üzerlerine ordular geldiği günü hatırlatır: {ar:فَأَرْسَلْنَا عَلَيْهِمْ رِيحًۭا وَجُنُودًۭا لَّمْ تَرَوْهَا, tr:fe-erselnâ aleyhim rîhan ve cunûden lem teravhâ, gloss:üzerlerine bir rüzgâr ve sizin görmediğiniz ordular gönderdik, source:33:9}. Bu sûrede ise ordu görünür kılınır: kuşlar vardır, taşlar vardır, ve okura "görmedin mi" denir. Aynı kalıp başka ilahi işlerin üzerine de kurulur: {ar:أَلَمْ تَرَ إِلَىٰ رَبِّكَ كَيْفَ مَدَّ ٱلظِّلَّ, tr:elem tera ilâ rabbike keyfe medde'z-zıll, gloss:Rabbinin gölgeyi nasıl uzattığını görmedin mi, source:25:45}; Nuh da kavmine {ar:أَلَمْ تَرَوْا۟ كَيْفَ خَلَقَ ٱللَّهُ سَبْعَ سَمَٰوَٰتٍۢ طِبَاقًۭا, tr:elem teravâ keyfe halakallâhu seb'a semâvâtin tıbâkâ, gloss:Allah'ın yedi göğü kat kat nasıl yarattığını görmediniz mi, source:71:15} der. İki sûre sonra aynı kökün dikkat çağrısı yeniden açılır: {ar:أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ, tr:e-raeyte'llezî yukezzibu bi'd-dîn, gloss:dini yalanlayanı gördün mü, source:107:1}.

Kaynaklar: 105:1 تَرَ ر ء ي B001; 105:1 تَرَ ر ء ي B002; 105:1 تَرَ ر ء ي B013; 105:1 تَرَ ر ء ي B012; 105:1 ٱلْفِيلِ ف ي ل B001; 105:2 تَضْلِيلٍ ض ل ل B001; 105:3 طَيْرًا ط ي ر B003; 105:4 تَرْمِيهِم ر م ي B009; 105:4 بِحِجَارَةٍ ح ج ر B002

## Sürü sürü salınan kuşlar

Üçüncü ayet bir salıvermedir: {ar:وَأَرْسَلَ عَلَيْهِمْ طَيْرًا أَبَابِيلَ, tr:ve ersele aleyhim tayran ebâbîl, gloss:üzerlerine bölük bölük kuşlar gönderdi, source:105:3}. {ar:وَأَرْسَلَ, tr:ve ersele, gloss:ve gönderdi, source:105:3} kökü bir şeyin harekete geçip uzanmasıdır ve tutmanın tersidir: {ar:أصل واحد يدل على الانبعاث والامتداد, tr:aslun vâhidun yedullu ale'l-inbiâsi ve'l-imtidâd, gloss:harekete geçmeyi ve uzanmayı gösteren tek bir köktür, source:"ر س ل,B001"}, {ar:الإرسال يقابل الإمساك, tr:el-irsâlu yukâbilu'l-imsâk, gloss:salıvermek, tutmanın karşıtıdır, source:"ر س ل,B001"}. Aynı kök çobanlıktan bir resim de taşır: otlağa salınan sürü ve birbiri ardınca gelen insan bölükleri: {ar:الرسل ما أرسل من الغنم إلى الرعي وجاء القوم أرسالا يتبع بعضهم بعضا, tr:er-raslu mâ ursile mine'l-ganemi ile'r-ra'y, ve câ'e'l-kavmu ersâlen yetbau ba'duhum ba'dâ, gloss:"rasl", otlağa salınan koyunlardır; kavim "ersâl" hâlinde, birbiri ardınca geldi, source:"ر س ل,B005"}, {ar:الرسل القطيع من الإبل والغنم وجاءت الخيل أرسالا قطيعا قطيعا, tr:er-raslu'l-katîu mine'l-ibili ve'l-ganem, ve câ'eti'l-haylu ersâlen katîan katîâ, gloss:"rasl", deve ve koyun sürüsüdür; atlar sürü sürü geldi, source:"ر س ل,B005"}.

{ar:أَبَابِيلَ, tr:ebâbîl, gloss:bölük bölük, source:105:3} kelimesi aynı sözlerle açıklanır: {ar:طيرا أبابيل أي يتبع بعضها بعضا, tr:tayran ebâbîl, ey yetbau ba'duhâ ba'dâ, gloss:ebâbîl kuşlar, yani biri ötekinin ardından gelen, source:"ء ب ل,B003"}. "Birbirinin ardından gelen" ifadesi, salınan sürülerin "ersâl" gelişini anlatan ifadenin aynısıdır; fiil ile sıfat aynı hareketi iki yandan söyler. Kelimenin açıklamasında deve sürüleri de vardır: {ar:جاءت إبلك أبابيل أي فرقا وطير أبابيل, tr:câ'et ibiluke ebâbîl, ey firakan, ve tayrun ebâbîl, gloss:develerin ebâbîl geldi, yani bölük bölük; ebâbîl kuşlar da böyledir, source:"ء ب ل,B003"}, {ar:طيرا أبابيل أي متفرقة كقطعات إبل, tr:tayran ebâbîl, ey muteferrikaten ke-kıtaâti ibil, gloss:ebâbîl kuşlar, yani deve sürüleri gibi dağınık bölükler, source:"ء ب ل,B003"}. Kelime, tekili olmayan bir topluluk adı olan deve kelimesiyle aynı harflerden kuruludur: {ar:الإبل لا واحد لها, tr:el-ibilu lâ vâhide lehâ, gloss:"ibil"in tekili yoktur, source:"ء ب ل,B001"}, {ar:الإبل معروفة ورجل آبل ومال مؤبل, tr:el-ibilu ma'rûfe, ve raculun âbil, ve mâlun mu'abbel, gloss:deve bilinir; deve gütmeyi bilen adam, deve sürülerinden oluşan mal, source:"ء ب ل,B001"}. {ar:طَيْرًا, tr:tayran, gloss:kuşlar, source:105:3} kanatlı bedenleri havada yüzer gibi gösterir, {ar:الطائر كل ذي جناح يسبح في الهواء, tr:et-tâ'iru küllu zî canâhin yesbahu fi'l-havâ', gloss:kuş, havada yüzen her kanatlıdır, source:"ط ي ر,B001"}, ve kök dağılıp saçılmayı da taşır: {ar:تطاير الشيء تفرق, tr:tetâyera'ş-şey', teferrak, gloss:şey uçuşup dağıldı, source:"ط ي ر,B002"}. Sahnenin işleyişi şudur: tutulan bir güç salıverilir; kuşlar tek bir bulut gibi değil, deve sürülerinin bölük bölük gelişi gibi birbirinin ardından gelir ve ordunun üzerine yayılır. "Üzerlerine" sözü, bu salıvermenin bir otlağa değil, bir topluluğun tepesine yapıldığını söyler.

Kur'an kuşları tutanın Allah olduğunu söyler: {ar:أَوَلَمْ يَرَوْا۟ إِلَى ٱلطَّيْرِ فَوْقَهُمْ صَٰٓفَّٰتٍۢ وَيَقْبِضْنَ ۚ مَا يُمْسِكُهُنَّ إِلَّا ٱلرَّحْمَٰنُ, tr:e-ve lem yerav ile't-tayri fevkahum sâffâtin ve yakbidn, mâ yumsikuhunne ille'r-rahmân, gloss:üstlerinde kanat açıp kapayan kuşları görmediler mi? Onları Rahman'dan başkası tutmuyor, source:67:19}, ve Nahl sûresinde {ar:أَلَمْ يَرَوْا۟ إِلَى ٱلطَّيْرِ مُسَخَّرَٰتٍۢ فِى جَوِّ ٱلسَّمَآءِ مَا يُمْسِكُهُنَّ إِلَّا ٱللَّهُ, tr:elem yerav ile't-tayri musahharâtin fî cevvi's-semâ', mâ yumsikuhunne illallâh, gloss:göğün boşluğunda boyun eğdirilmiş kuşları görmediler mi? Onları Allah'tan başkası tutmuyor, source:16:79}. Bu sûrede tutmanın karşıtı olan salıverme işler. Fâtır sûresi ikisini bir ilke olarak koyar: {ar:وَمَا يُمْسِكْ فَلَا مُرْسِلَ لَهُۥ مِنۢ بَعْدِهِۦ, tr:ve mâ yumsik fe-lâ mursile lehû min ba'dih, gloss:O neyi tutarsa ondan sonra onu salıverecek yoktur, source:35:2}. Firavun'un ailesi üzerine de birbiri ardınca sürüler salınmıştı: {ar:فَأَرْسَلْنَا عَلَيْهِمُ ٱلطُّوفَانَ وَٱلْجَرَادَ وَٱلْقُمَّلَ وَٱلضَّفَادِعَ وَٱلدَّمَ ءَايَٰتٍۢ مُّفَصَّلَٰتٍۢ, tr:fe-erselnâ aleyhimu't-tûfâne ve'l-cerâde ve'l-kummele ve'd-defâdia ve'd-deme âyâtin mufassalât, gloss:üzerlerine tufanı, çekirgeyi, haşereyi, kurbağaları ve kanı ayrı ayrı mucizeler olarak gönderdik, source:7:133}. Kamer sûresinde "üzerlerine gönderdik" kalıbı bir cezanın kalıbıdır: Semûd için {ar:إِنَّآ أَرْسَلْنَا عَلَيْهِمْ صَيْحَةًۭ وَٰحِدَةًۭ, tr:innâ erselnâ aleyhim sayhaten vâhide, gloss:üzerlerine tek bir çığlık gönderdik, source:54:31}, Lut kavmi için {ar:إِنَّآ أَرْسَلْنَا عَلَيْهِمْ حَاصِبًا, tr:innâ erselnâ aleyhim hâsibâ, gloss:üzerlerine taş yağdıran bir rüzgâr gönderdik, source:54:34}.

Kaynaklar: 105:3 وَأَرْسَلَ ر س ل B001; 105:3 وَأَرْسَلَ ر س ل B005; 105:3 طَيْرًا ط ي ر B001; 105:3 طَيْرًا ط ي ر B002; 105:3 أَبَابِيلَ ء ب ل B003; 105:3 أَبَابِيلَ ء ب ل B001

## Av ve avcı: ağırın hafif tarafından vurulması

Dördüncü ayetin fiili bir atıştır: {ar:تَرْمِيهِم بِحِجَارَةٍۢ مِّن سِجِّيلٍۢ, tr:termîhim bi-hicâratin min siccîl, gloss:onlara siccîlden taşlar atıyorlardı, source:105:4}. Fiil dişil kurulmuştur ve öznesi kuşlardır; kuşlar atandır, onlar atılandır. Atmanın kökü nesnelerini kendisi sayar: ok ve taş. {ar:الرمي يقال في الأعيان كالسهم والحجر, tr:er-ramyu yukâlu fi'l-a'yân ke's-sehmi ve'l-hacer, gloss:atmak, ok ve taş gibi somut şeyler için söylenir, source:"ر م ي,B001"}. Kök ava çıkmayı da anlatır: {ar:خرجت أرتمي إذا رميت القنص, tr:haractu ertemî izâ rameytu'l-kanas, gloss:av vurmaya çıktığımda "atmaya çıktım" derim, source:"ر م ي,B001"}, ve atılan her şey bir avdır: {ar:الرمية الصيد الذي يرمى, tr:er-ramiyyetu's-saydu'llezî yurmâ, gloss:"ramiyye", vurulan avdır, source:"ر م ي,B003"}; okun yuvarlak ucuna da bu kökten ad verilir: {ar:المرماة نصل السهم المدور, tr:el-mirmâtu naslu's-sehmi'l-mudevver, gloss:"mirmât", okun yuvarlak temreni, source:"ر م ي,B003"}. Fiile bağlanan "onları" zamiri, filin sahiplerini bu "ramiyye"nin, yani vurulan avın yerine koyar. Göndermenin kökü bile kısa bir oku adlandırır: {ar:المرسال سهم قصير, tr:el-mirsâlu sehmun kasîr, gloss:"mirsâl", kısa bir oktur, source:"ر س ل,B011"}. Taşlar da sert birer mermidir: {ar:الحجر الجوهر الصلب المعروف وجمعه أحجار وحجارة, tr:el-haceru'l-cevheru's-sulbu'l-ma'rûf, ve cem'uhû ahcâr ve hicâra, gloss:taş bilinen sert maddedir, çoğulu ahcâr ve hicâra, source:"ح ج ر,B003"}.

Bu avın tuhaflığı rollerin yer değiştirmesidir. Kuşlar normalde avlanandır; burada avcıdırlar. Hayvanların en irisi ve onun sahipleri ise vurulan avdır. Avın sonu son ayettedir: {ar:مَّأْكُولٍۭ, tr:me'kûl, gloss:yenmiş, source:105:5} kökü, bir yırtıcının yediği avı da adlandırır: {ar:أكيل الذئب الشاة وغيرها؛ أكيلة الأسد فريسته, tr:ekîlu'z-zi'bi'ş-şâtu ve gayruhâ; ekîletu'l-esedi ferîsetuh, gloss:kurdun "ekîl"i yediği koyun ve benzeridir; aslanın "ekîle"si avıdır, source:"ء ك ل,B007"}. Sahne şöyle akar: avcılar salınır, taşlar ok gibi atılır, ordu vurulan av olur ve yenmiş av olarak kalır. Kur'an yırtıcının yediği hayvanı haram kılınanlar arasında sayar, {ar:وَمَآ أَكَلَ ٱلسَّبُعُ, tr:ve mâ ekele's-sebu', gloss:ve yırtıcı hayvanın yediği, source:5:3}; Yusuf'un kardeşleri de babalarına onu kurdun yediğini söyler, {ar:فَأَكَلَهُ ٱلذِّئْبُ, tr:fe-ekelehu'z-zi'b, gloss:onu kurt yedi, source:12:17}. Bu sahnede "yenmiş" olan, bir avın sonudur.

Avın içinde ağır ile hafifin yer değiştirmesi de vardır. Fil en iri hayvandır, {ar:الفيل معروف, tr:el-fîlu ma'rûf, gloss:fil bilinir, source:"ف ي ل,B004"}; ama kökünün temel anlamı gevşeklik ve zayıflıktır: {ar:أصل يدل على استرخاء وضعف, tr:aslun yedullu ale'stirhâ'in ve da'f, gloss:gevşeklik ve zayıflık gösteren bir köktür, source:"ف ي ل,B001"}. En güçlü hayvanın adının altında güçsüzlük yatar. Kuşlar hafif ve hızlıdır: {ar:لكل من خف قد طار وكل سرعة, tr:li-külli men haffe kad târ, ve küllu sur'a, gloss:hafifleyen her şeye "uçtu" denir, her hıza da, source:"ط ي ر,B001"}. Ama bu hafif sürülerin adı ağırlığı ve yenmeyi taşıyan bir köktendir: {ar:أبل الرجل إذا غلب وامتنع والأبلة الثقل, tr:ebile'r-racul izâ galebe ve'mtena', ve'l-ubletu's-sikal, gloss:adam galip gelip direnince "ebile" denir; "uble" ağırlıktır, source:"ء ب ل,B004"}. Taşlar serttir ve siccîl şiddetle açıklanır: {ar:وقالوا السجيل الشديد, tr:ve kâlû es-siccîlu'ş-şedîd, gloss:siccîl, şiddetli olandır dediler, source:"س ج ل,B005"}, {ar:تأويله كثيرة شديدة, tr:te'vîluhû kesîratun şedîde, gloss:anlamı: çok ve şiddetli, source:"س ج ل,B005"}. Son kelime {ar:كَعَصْفٍ, tr:ke-asf, gloss:ekin yaprağı gibi, source:105:5} ise hafiflik ve hızın kökündendir: {ar:أصل واحد صحيح يدل على خفة وسرعة, tr:aslun vâhidun sahîhun yedullu alâ hıffetin ve sur'a, gloss:hafiflik ve hız gösteren sağlam tek bir köktür, source:"ع ص ف,B003"}. Ağır olan hafif olanca vurulur; sert taşlar hafif kuşlardan iner ve en kütleli olan sonunda ağırlığı olmayan bir yaprağa döner.

Kur'an gücün korumadığı kavimleri anlatırken bu tersine dönüşü öne çıkarır. Mü'min sûresinde Allah önceki kavimler için {ar:كَانُوا۟ هُمْ أَشَدَّ مِنْهُمْ قُوَّةًۭ وَءَاثَارًۭا فِى ٱلْأَرْضِ فَأَخَذَهُمُ ٱللَّهُ بِذُنُوبِهِمْ, tr:kânû hum eşedde minhum kuvveten ve âsâran fi'l-ard, fe-ehazehumullâhu bi-zunûbihim, gloss:onlar bunlardan daha güçlü ve yeryüzünde daha çok iz bırakmışlardı, Allah onları günahları yüzünden yakaladı, source:40:21} der. Fussilet sûresinde Âd kavmi {ar:وَقَالُوا۟ مَنْ أَشَدُّ مِنَّا قُوَّةً, tr:ve kâlû men eşeddu minnâ kuvveh, gloss:"bizden daha güçlü kim var" dediler, source:41:15} ve cevap bir göndermedir: {ar:فَأَرْسَلْنَا عَلَيْهِمْ رِيحًۭا صَرْصَرًۭا, tr:fe-erselnâ aleyhim rîhan sarsarâ, gloss:üzerlerine dondurucu, uğultulu bir rüzgâr gönderdik, source:41:16}. Atmanın gerçek sahibi de Enfâl sûresinde açıkça söylenir; Allah elçisine {ar:وَمَا رَمَيْتَ إِذْ رَمَيْتَ وَلَٰكِنَّ ٱللَّهَ رَمَىٰ, tr:ve mâ rameyte iz rameyte ve lâkinnallâhe ramâ, gloss:attığın zaman sen atmadın, Allah attı, source:8:17} der. Orada görünen atıcı bir insandır, burada kuşlardır; atışın sahibi iki yerde de Odur.

Kaynaklar: 105:4 تَرْمِيهِم ر م ي B001; 105:4 تَرْمِيهِم ر م ي B003; 105:3 وَأَرْسَلَ ر س ل B011; 105:4 بِحِجَارَةٍ ح ج ر B003; 105:5 مَّأْكُولٍۭ ء ك ل B007; 105:1 ٱلْفِيلِ ف ي ل B004; 105:1 ٱلْفِيلِ ف ي ل B001; 105:3 طَيْرًا ط ي ر B001; 105:3 أَبَابِيلَ ء ب ل B004; 105:4 سِجِّيلٍ س ج ل B005; 105:5 كَعَصْفٍ ع ص ف B003

## Fırtına: salınan rüzgâr, ağır damlalı bulut, boşalan kova

Üçüncü, dördüncü ve beşinci ayetlerin kökleri bir fırtınanın bütün evrelerini taşır. Göndermenin kökü rüzgârların gönderilişini de adlandırır: {ar:أرسلت فلانا في رسالة والمرسلات الرياح ويقال الملائكة, tr:erseltu fulânen fî risâle, ve'l-murselâtu'r-riyâh, ve yukâlu'l-melâ'ike, gloss:falancayı bir haberle gönderdim; "murselât" rüzgârlardır, meleklerdir de denir, source:"ر س ل,B001"}. Atmanın kökü iri ve sert damlalı büyük bulutu adlandırır: {ar:الرمى السقى وهي السحابة العظيمة القطر الشديدة الوقع, tr:er-ramiyyu's-sakiyy, ve hiye's-sehâbetu'l-azîmetu'l-katri'ş-şedîdetu'l-vak', gloss:"ramiyy", iri damlalı, sert düşen büyük buluttur, source:"ر م ي,B004"}, {ar:ترمى بقطع من السحاب, tr:turmâ bi-kıtain mine's-sehâb, gloss:bulut parçalarıyla atılır, source:"ر م ي,B004"}. Siccîl'in kökünün temeli ise dolduktan sonra boşalmaktır: {ar:أصل واحد يدل على انصباب شيء بعد امتلائه, tr:aslun vâhidun yedullu ale'nsibâbi şey'in ba'de'mtilâ'ih, gloss:bir şeyin dolduktan sonra dökülmesini gösteren tek bir köktür, source:"س ج ل,B001"}, {ar:سجلت الماء فانسجل أي صببته فانصب, tr:seceltu'l-mâ'e fe'nsecel, ey sabebtuhû fe'nsabb, gloss:suyu döktüm, o da döküldü, source:"س ج ل,B001"}, {ar:السجل الدلو ولا يكون سجلا حتى يكون فيه ماء, tr:es-seclu'd-delv, ve lâ yekûnu seclen hattâ yekûne fîhi mâ', gloss:"secl" kovadır; içinde su olmadıkça ona secl denmez, source:"س ج ل,B001"}. Siccîl kelimesi göndermeyle de açıklanır: {ar:سجيل من سجلته أي أرسلته, tr:siccîl, min secceltuh, ey erseltuh, gloss:siccîl, "onu salıverdim" anlamındaki fiildendir, source:"س ج ل,B005"}, ve kökün bir dalı sınırsızca saçılmayı anlatır: {ar:أسجلت الكلام أي أرسلته, tr:escelte'l-kelâm, ey erseltah, gloss:sözü salıverdin, source:"س ج ل,B003"}, {ar:الشيء المسجل وهو المبذول لكل أحد كأنه قد صب صبا, tr:eş-şey'u'l-musecel, ve huve'l-mebzûlu li-külli ehad, ke-ennehû kad subbe sabbâ, gloss:"musecel", herkese bolca verilen, sanki dökülmüş olandır, source:"س ج ل,B003"}. Damlaların yerine düşen ise taşlardır, {ar:الحجر الجوهر الصلب المعروف, tr:el-haceru'l-cevheru's-sulbu'l-ma'rûf, gloss:taş bilinen sert maddedir, source:"ح ج ر,B003"}. Son ayetin kökü de kırıp döken rüzgârdır: {ar:عاصفة ومعصفة تكسر الشيء فتجعله كعصف, tr:âsıfa ve mu'sıfa, tekseru'ş-şey'e fe-tec'aluhû ke-asf, gloss:"âsıfa" ve "mu'sıfa" denen rüzgâr, şeyi kırıp ekin yaprağı gibi yapar, source:"ع ص ف,B002"}, {ar:والمعصفات الرياح التي تثير التراب والورق, tr:ve'l-mu'sıfâtu'r-riyâhu'lletî tusîru't-turâbe ve'l-varak, gloss:"mu'sıfât", toprağı ve yaprağı kaldıran rüzgârlardır, source:"ع ص ف,B002"}. Fırtına salıvermeyle (üçüncü ayet) başlar, bulutun ağır damlaları ve dolu kovanın boşalması gibi inen taşlarla (dördüncü ayet) sürer, kırılmış sapları geride bırakan rüzgârla (beşinci ayet) biter. "Rüzgâr şeyi kırıp asf gibi yapar" sözü, son ayetin "onları asf gibi kıldı" cümlesinin neredeyse aynısıdır.

Kur'an bu taş yağmurunu Lut kavminin kıssasında aynı kelimeyle anlatır: {ar:جَعَلْنَا عَٰلِيَهَا سَافِلَهَا وَأَمْطَرْنَا عَلَيْهَا حِجَارَةًۭ مِّن سِجِّيلٍۢ مَّنضُودٍۢ, tr:cealnâ âliyehâ sâfilehâ ve emtarnâ aleyhâ hicâraten min siccîlin mendûd, gloss:oranın üstünü altına getirdik ve üzerine siccîlden, üst üste dizilmiş taşlar yağdırdık, source:11:82}; Hicr sûresi aynı sahneyi tekrarlar, {ar:وَأَمْطَرْنَا عَلَيْهِمْ حِجَارَةًۭ مِّن سِجِّيلٍ, tr:ve emtarnâ aleyhim hicâraten min siccîl, gloss:üzerlerine siccîlden taşlar yağdırdık, source:15:74}. Zâriyât sûresinde İbrahim'e gelen elçiler kendilerinin {ar:قَالُوٓا۟ إِنَّآ أُرْسِلْنَآ إِلَىٰ قَوْمٍۢ مُّجْرِمِينَ, tr:kâlû innâ ursilnâ ilâ kavmin mucrimîn, gloss:"biz suçlu bir kavme gönderildik" dediler, source:51:32} olduğunu söyler ve görevlerini anlatır: {ar:لِنُرْسِلَ عَلَيْهِمْ حِجَارَةًۭ مِّن طِينٍۢ, tr:li-nursile aleyhim hicâraten min tîn, gloss:üzerlerine çamurdan taşlar göndermek için, source:51:33}. Bu sûrenin "üzerlerine gönderdi" kalıbı, taş ve Rab orada bir aradadır. Mekkeli inkârcılar aynı yağmuru kendileri ister: {ar:فَأَمْطِرْ عَلَيْنَا حِجَارَةًۭ مِّنَ ٱلسَّمَآءِ, tr:fe-emtir aleynâ hicâraten mine's-semâ', gloss:üzerimize gökten taş yağdır, source:8:32}. Mülk sûresi bu göndermeyi bir uyarıya çevirir: {ar:أَمْ أَمِنتُم مَّن فِى ٱلسَّمَآءِ أَن يُرْسِلَ عَلَيْكُمْ حَاصِبًۭا, tr:em emintum men fi's-semâ'i en yursile aleykum hâsibâ, gloss:yoksa gökte olanın üzerinize taş yağdıran bir rüzgâr göndermeyeceğinden emin mi oldunuz, source:67:17}, ve İsrâ sûresi deniz yolcularına {ar:فَيُرْسِلَ عَلَيْكُمْ قَاصِفًۭا مِّنَ ٱلرِّيحِ, tr:fe-yursile aleykum kâsıfan mine'r-rîh, gloss:üzerinize kırıp geçiren bir rüzgâr göndermesinden, source:17:69} söz eder. Mürselât sûresinin ilk iki ayeti göndermenin ve fırtınanın köklerini ardışık koyar: {ar:وَٱلْمُرْسَلَٰتِ عُرْفًۭا, tr:ve'l-murselâti urfâ, gloss:art arda gönderilenlere andolsun, source:77:1}, {ar:فَٱلْعَٰصِفَٰتِ عَصْفًۭا, tr:fe'l-âsıfâti asfâ, gloss:sonra şiddetle esip savuranlara, source:77:2}. Gönderilenler fırtınaya dönüşür, tıpkı bu sûrede gönderilen kuşların sonunun "asf" olması gibi. Fecr sûresinde aynı "görmedin mi" kalıbının ardından dökme fiili gelir: {ar:فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ, tr:fe-sabbe aleyhim rabbüke sevta azâb, gloss:Rabbin üzerlerine bir azap kamçısı döktü, source:89:13}; siccîl'in kökündeki dökülme burada açıkça söylenmiştir. Âd kavmi için {ar:إِذْ أَرْسَلْنَا عَلَيْهِمُ ٱلرِّيحَ ٱلْعَقِيمَ, tr:iz erselnâ aleyhimu'r-rîha'l-akîm, gloss:üzerlerine kısır rüzgârı gönderdiğimizde, source:51:41} denir ve rüzgâr {ar:مَا تَذَرُ مِن شَىْءٍ أَتَتْ عَلَيْهِ إِلَّا جَعَلَتْهُ كَٱلرَّمِيمِ, tr:mâ tezeru min şey'in etet aleyhi illâ cealethu ke'r-ramîm, gloss:uğradığı hiçbir şeyi bırakmaz, onu çürümüş kemik gibi yapardı, source:51:42}; "kıldı" fiili, "gibi" edatı ve bir kalıntı, bu sûrenin son ayetinin çerçevesidir. Bulutu yanlış okuyan Âd'a da rüzgâr gelir: {ar:رِيحٌۭ فِيهَا عَذَابٌ أَلِيمٌۭ, tr:rîhun fîhâ azâbun elîm, gloss:içinde acı bir azap olan bir rüzgâr, source:46:24}. En'âm sûresi ise aynı göndermenin rahmet yüzünü gösterir: {ar:وَأَرْسَلْنَا ٱلسَّمَآءَ عَلَيْهِم مِّدْرَارًۭا, tr:ve erselnâ's-semâ'e aleyhim midrârâ, gloss:üzerlerine göğü bol bol yağmur yağdırır hâlde gönderdik, source:6:6}. Fil sûresinin gökten gelen yağmuru bunun tersidir: damla yerine taş düşer.

Kaynaklar: 105:3 وَأَرْسَلَ ر س ل B001; 105:4 تَرْمِيهِم ر م ي B004; 105:4 سِجِّيلٍ س ج ل B001; 105:4 سِجِّيلٍ س ج ل B005; 105:4 سِجِّيلٍ س ج ل B003; 105:4 بِحِجَارَةٍ ح ج ر B003; 105:5 كَعَصْفٍ ع ص ف B002

## Onlar için yazılmış taşlar

Siccîl'in kökü yazılı kaydı, senedi ve hâkimin tescilini de adlandırır: {ar:السجل كتاب العهدة, tr:es-sicillu kitâbu'l-uhde, gloss:sicil, taahhüt belgesidir, source:"س ج ل,B004"}, {ar:السجل الصك وقد سجل الحاكم تسجيلا, tr:es-sicillu's-sakk, ve kad seccele'l-hâkimu tescîlâ, gloss:sicil senettir; hâkim tescil etti, source:"س ج ل,B004"}. Kökün bir açıklaması sicilin ilkin bir taş olduğunu söyler: {ar:السجل قيل حجر كان يكتب فيه ثم سمي كل ما يكتب فيه سجلا, tr:es-sicil, kîle hacerun kâne yuktebu fîh, summe summiye küllu mâ yuktebu fîhi sicillâ, gloss:sicil, denildiğine göre üzerine yazı yazılan bir taştı; sonra üzerine yazılan her şeye sicil dendi, source:"س ج ل,B004"}. Siccîl kelimesinin kendisi de böyle açıklanır: {ar:من سجل أي ما كتب لهم, tr:min sicil, ey mâ kutibe lehum, gloss:sicilden, yani onlar için yazılmış olandan, source:"س ج ل,B005"}. Bu okumada taşlar yazılı bir hükümdür; "siccîl'den taşlar", onlar için yazılmış olandan gelen taşlardır. Aynı açıklamada siccîl ile siccîn arasında bir ses değişimi de kaydedilir: {ar:أراد سجيلا أي شديدا وإنما أبدل اللام نونا, tr:erâde siccîlen, ey şedîdâ, ve innemâ ebdele'l-lâme nûnâ, gloss:siccîl'i, yani şiddetliyi kastetti; lamı nuna çevirdi, source:"س ج ل,B005"}. Kuş da insanın amelini, boynuna takılan payını adlandırır: {ar:طائر الإنسان عمله الذي قلده, tr:tâ'iru'l-insâni ameluhu'llezî kullideh, gloss:insanın kuşu, boynuna takılan amelidir, source:"ط ي ر,B003"}, {ar:كل إنسان ألزمناه طائره في عنقه أي عمله, tr:küllu insânin elzemnâhu tâ'irahû fî unukıh, ey ameleh, gloss:her insanın kuşunu boynuna doladık, yani amelini, source:"ط ي ر,B003"}, {ar:ألا إنما طائرهم عند الله أي شؤمهم, tr:elâ innemâ tâ'iruhum indallâh, ey şu'muhum, gloss:onların kuşu Allah katındadır, yani uğursuzlukları, source:"ط ي ر,B003"}. Sahne bu iki aile imgesiyle kurulur: kuşlar, üzerinde onların payı yazılmış taşları getirir; her biri yaptığının karşılığını kuşla alır. Taş hem atılan mermi hem de yazının yüzeyidir, {ar:الحجر الجوهر الصلب المعروف وجمعه أحجار وحجارة, tr:el-haceru'l-cevheru's-sulbu'l-ma'rûf, ve cem'uhû ahcâr ve hicâra, gloss:taş bilinen sert maddedir, çoğulu ahcâr ve hicâra, source:"ح ج ر,B003"}. Bu bir aile imgesidir; ayet taşların ne olduğunu değil, nereden geldiğini söyler.

Kur'an kuşu ve yazılı kitabı tek ayette birleştirir: {ar:وَكُلَّ إِنسَٰنٍ أَلْزَمْنَٰهُ طَٰٓئِرَهُۥ فِى عُنُقِهِۦ ۖ وَنُخْرِجُ لَهُۥ يَوْمَ ٱلْقِيَٰمَةِ كِتَٰبًۭا يَلْقَىٰهُ مَنشُورًا, tr:ve külle insânin elzemnâhu tâ'irahû fî unukıhî, ve nuhricu lehû yevme'l-kıyâmeti kitâben yelkâhu menşûrâ, gloss:her insanın kuşunu boynuna doladık; kıyamet günü onun için açılmış olarak bulacağı bir kitap çıkarırız, source:17:13}. Lut kavmine yağdırılan siccîl taşlarının işaretli olduğunu Kur'an iki kez söyler: {ar:مُّسَوَّمَةً عِندَ رَبِّكَ, tr:musevvemeten inde rabbik, gloss:Rabbinin katında işaretlenmiş, source:11:83}, ve {ar:مُّسَوَّمَةً عِندَ رَبِّكَ لِلْمُسْرِفِينَ, tr:musevvemeten inde rabbike li'l-musrifîn, gloss:Rabbinin katında haddi aşanlar için işaretlenmiş, source:51:34}. Taşlar kimin için olduklarını taşıyan, Rabbin katında belirlenmiş şeylerdir. Kuş kelimesiyle uğursuzluk çıkaranlara peygamberlerin cevabı da aynıdır: Salih Semûd'a {ar:قَالَ طَٰٓئِرُكُمْ عِندَ ٱللَّهِ, tr:kâle tâ'iruküm indallâh, gloss:"kuşunuz Allah katındadır" dedi, source:27:47}; bir kente gönderilen elçiler {ar:قَالُوا۟ طَٰٓئِرُكُم مَّعَكُمْ, tr:kâlû tâ'iruküm meaküm, gloss:"kuşunuz sizinle beraberdir" dediler, source:36:19}; Firavun'un ailesi için {ar:أَلَآ إِنَّمَا طَٰٓئِرُهُمْ عِندَ ٱللَّهِ, tr:elâ innemâ tâ'iruhum indallâh, gloss:bilin ki onların kuşu Allah katındadır, source:7:131}. Sicil Kur'an'da yazılı tomarın adıdır: {ar:يَوْمَ نَطْوِى ٱلسَّمَآءَ كَطَىِّ ٱلسِّجِلِّ لِلْكُتُبِ, tr:yevme natvi's-semâ'e ke-tayyi's-sicilli li'l-kutub, gloss:göğü yazılı sayfaların tomarı dürer gibi düreceğimiz gün, source:21:104}. Siccîn de yazılı bir kitaptır: {ar:كَلَّآ إِنَّ كِتَٰبَ ٱلْفُجَّارِ لَفِى سِجِّينٍۢ, tr:kellâ inne kitâbe'l-fuccâri lefî siccîn, gloss:hayır, günahkârların kitabı siccîndedir, source:83:7}, ve hemen ardından açıklanır: {ar:كِتَٰبٌۭ مَّرْقُومٌۭ, tr:kitâbun merkûm, gloss:yazılmış, işaretlenmiş bir kitap, source:83:9}. Siccîl ile siccîn arasındaki ses değişimi bir kök özdeşliği kurmaz; iki kelime ayrı köklerdir, ama ikisi de günahkârlar için yazılmış olanın yanında durur.

Kaynaklar: 105:4 سِجِّيلٍ س ج ل B004; 105:4 سِجِّيلٍ س ج ل B005; 105:4 بِحِجَارَةٍ ح ج ر B003; 105:3 طَيْرًا ط ي ر B003

## Yakıt ve yiyen ateş

{ar:مَّأْكُولٍۭ, tr:me'kûl, gloss:yenmiş, source:105:5} kelimesinin kökü ateşin yemesini de söyler: {ar:أكلت النار الحطب وآكلتها؛ ائتكلت النار إذا اشتد التهابها؛ وعلى طريق التشبيه قيل أكلت النار الحطب, tr:ekeleti'n-nâru'l-hatab ve âkeltuhâ; i'tekeleti'n-nâru izâ işteedde'ltihâbuhâ; ve alâ tarîki't-teşbîh kîle ekeleti'n-nâru'l-hatab, gloss:ateş odunu yedi; alevi şiddetlenince ateş "kendini yedi"; benzetme yoluyla "ateş odunu yedi" denir, source:"ء ك ل,B005"}. {ar:عَصْفٍ, tr:asf, gloss:kuru ekin yaprağı, source:105:5}, kuruyup ufalanan yapraktır, {ar:ما على ساق الزرع من الورق الذي يبس فتفتت, tr:mâ alâ sâkı'z-zer'i mine'l-varaki'llezî yebise fe-tefettet, gloss:ekinin sapı üzerinde kuruyup ufalanan yapraklar, source:"ع ص ف,B001"}, yani ateşin ilk tuttuğu yakıt. Kuşların sıfatının kökü bir odun demetini adlandırır ve bir atasözünde bir yükün üstüne bir başka yük olarak geçer: {ar:الإبالة الحزمة من الحطب, tr:el-ibâletu'l-huzmetu mine'l-hatab, gloss:"ibâle", odun demetidir, source:"ء ب ل,B005"}, {ar:الإبالة الحزمة من الحطب وضغث على إبالة, tr:el-ibâletu'l-huzmetu mine'l-hatab, ve dıgsun alâ ibâleh, gloss:ibâle odun demetidir; "demetin üstüne bir tutam", source:"ء ب ل,B005"}. Düzenin kökü de kalıplaşmış bir ifadede ateşi geç veren çakmak ağacını anlatır: {ar:أن يخرج الزند النار ببطء وشدة, tr:en yuhrice'z-zendu'n-nâre bi-but'in ve şidde, gloss:çakmak ağacının ateşi yavaşça ve zorla çıkarması, source:"ك ي د,B006"}, {ar:كاد الزند إذا تباطأ بإخراج ناره, tr:kâde'z-zend izâ tebâta'e bi-ihrâci nârih, gloss:çakmak ağacı ateşini geç çıkarınca "kâde" denir, source:"ك ي د,B006"}. Siccîl de taş ve çamurun karışımı olarak açıklanır: {ar:السجيل حجر وطين مختلط وأصله فيما قيل فارسي معرب, tr:es-siccîlu hacerun ve tînun muhtalit, ve asluhû fîmâ kîle fârisiyyun mu'arrab, gloss:siccîl, karışık taş ve çamurdur; aslının, denildiğine göre, Arapçalaşmış Farsça olduğu söylenir, source:"س ج ل,B005"}, {ar:السجيل حجارة كالمدر وهو حجر وطين, tr:es-siccîlu hicâratun ke'l-meder, ve huve hacerun ve tîn, gloss:siccîl, kuru kesek gibi taşlardır; taş ve çamurdur, source:"س ج ل,B005"}. Kur'an da Lut kavmine yağan siccîl taşlarını bir başka yerde {ar:حِجَارَةًۭ مِّن طِينٍۢ, tr:hicâraten min tîn, gloss:çamurdan taşlar, source:51:33} diye anar.

Bu aile imgeleri bir tersine dönüş kurar. Onların keyd'i, yani emekle uğraşmaları, ateşi geç veren bir çakmak gibidir: güçle vurulur ama tutuşmaz. Sonunda yenilen ise kendileridir, ateşin kuru samanı yiyişi gibi. Bu bir aile imgesidir; ayet ateşten söz etmez, yalnızca "yenmiş" der. Kur'an ise ateşin yemesini açıkça kullanır: Âl-i İmrân sûresinde bazıları peygambere inanmak için {ar:حَتَّىٰ يَأْتِيَنَا بِقُرْبَانٍۢ تَأْكُلُهُ ٱلنَّارُ, tr:hattâ ye'tiyenâ bi-kurbânin te'kuluhu'n-nâr, gloss:bize ateşin yiyeceği bir kurban getirinceye kadar, source:3:183} şartını koyduklarını söyler. Bakara sûresinde Kur'an'a denk bir sûre getirmeye çağrılan inkârcılara, iki kez tekrarlanan "yapmak" fiilinin ardından, taşların ateşin yakıtı olduğu söylenir: {ar:فَإِن لَّمْ تَفْعَلُوا۟ وَلَن تَفْعَلُوا۟ فَٱتَّقُوا۟ ٱلنَّارَ ٱلَّتِى وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:fe-in lem tef'alû ve len tef'alû fetteku'n-nâre'lletî vekûduhe'n-nâsu ve'l-hicâra, gloss:yapamazsanız, ki asla yapamayacaksınız, yakıtı insanlar ve taşlar olan ateşten sakının, source:2:24}; Tahrîm sûresinde mü'minlere aynı uyarı gelir: {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:kû enfuseküm ve ehlîküm nâran vekûduhe'n-nâsu ve'l-hicâra, gloss:kendinizi ve ailenizi yakıtı insanlar ve taşlar olan ateşten koruyun, source:66:6}. Bakara sûresindeki bir benzetme de rüzgârı ve ateşi bir bahçenin üzerinde birleştirir: {ar:فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ, tr:fe-esâbehâ i'sârun fîhi nârun fehterakat, gloss:içinde ateş bulunan bir kasırga ona çarptı ve bahçe yandı, source:2:266}. Kasırga kelimesi "asf" ile aynı kökten değildir; ama rüzgârın ve ateşin bir ekini yok edişi, bu sûrenin son ayetindeki iki aile imgesinin bir arada sahnelenişidir.

Kaynaklar: 105:5 مَّأْكُولٍۭ ء ك ل B005; 105:5 كَعَصْفٍ ع ص ف B001; 105:3 أَبَابِيلَ ء ب ل B005; 105:2 كَيْدَهُمْ ك ي د B006; 105:4 سِجِّيلٍ س ج ل B005

## Buluşmalar

Sûrenin hareketi, açılıştaki görme çağrısı ile sondaki kırılmış ekin arasında kurulur ve imgeler bu yolda birbirine geçer. Görmenin imgesi ile düzenin imgesi aynı kökte buluşur: yolunu kaybetmeyi anlatan kök, bir işte doğruyu bulamamayı da anlatır. İkinci ayetteki düzen, hem bir yolda saptırılan bir yürüyüş hem de sağlıklı görmeyen bir aklın yanılmasıdır; okura "gör" denirken karşı tarafın düzeni "yolunu bulamaz". Fecr sûresinin "hicr sahibi" ile "Rabbinin ne yaptığını görmedin mi" sorusunu yan yana koyması, bu karşılaşmanın sahnesidir: akıl anlamındaki "hicr" ile taşın kökü aynıdır ve aklı olmayanlara taş iner.

Salınan sürüler, av ve fırtına tek bir sahnede durur. Göndermenin kökü hem otlağa salınan sürüleri hem gönderilen rüzgârları hem kısa bir oku adlandırır; üçüncü ayetin tek fiili, kuşların bölük bölük gelişini, rüzgârın esişini ve okun atılışını birlikte taşır. Atmanın kökü de iki yüzlüdür: ok ve taşla ava atmak ve iri damlalı bulutun yağması. Dördüncü ayetteki kuşlar, bir avcı gibi atar ve bir bulut gibi yağdırır. Mürselât sûresinin "gönderilenler" ile "şiddetle esenler"i ardışık koyması, göndermenin fırtınaya dönüşümünü sahneler; bu sûrede de gönderilen kuşlarla başlayan iş "asf" kelimesiyle biter.

Fırtına ile yazılmış taşlar siccîl kelimesinde buluşur. Kelime hem "salıverdiğim" hem "onlar için yazılmış olan" diye açıklanır: taşlar hem bir buluttan boşalan kovanın dökülüşü gibi iner hem de kimin için olduklarını taşır. Hûd ve Zâriyât sûrelerinin taş yağmuru, bu iki yüzü bir arada gösterir: yağdırılan siccîl taşları "Rabbinin katında işaretlenmiş"tir.

Savaş ile fırtına da siccîl'in kökünde birleşir: savaşın dönüşümlü talihi, su çekerken sırayla dökülen kovadan gelir. Fil sûresinde kova yalnızca bir tarafa, onların üzerine dökülür; fırtınanın boşalan kovası, savaşın sıra beklemeyen kovasıdır. Savaş ile ekin de "asf"ın kökünde buluşur: savaş bir kavmi silip götürür, rüzgâr şeyi kırıp asf gibi yapar ve rüzgârın insanları silip götürmesi bu kırılmaya benzetilerek söylenir.

Av ile ekin "yenmiş" kelimesinde iki ayrı sona ayrılır: yırtıcının yediği av ve ürünü alınıp içi yenmiş ekin. Ekin ile ateş de kuru yaprakta buluşur: kuruyup ufalanan yaprak, ateşin ilk yediği şeydir. Ağır ile hafifin yer değiştirmesi bu sahnelerin hepsinden geçer: en iri hayvan, en hafif kanatlıların avıdır ve sonunda en hafif şeye, ağırlığı olmayan bir yaprağa döner.

Bütün bu imgeleri birinci ve beşinci ayetler arasındaki fiiller bağlar. Rabbin "yapışı", kullanımdaki örneğiyle bir kırmadır; ilk "kılma" onların düzenini sapmaya, ikinci "kılma" onların kendilerini kırılmış ekine çevirir. Zümer sûresi bu yayı tek bir ayette gösterir: "görmedin mi" ile açılır, bir ekin çıkarır, sararmasını gösterir ve "onu kırıntı kılar". Fil sûresi aynı yayı bir topluluğun üzerine kurar: okur görmeye çağrılır, onların emeği yoldan çıkarılır, gökten bölük bölük salınan avcılar yazılmış taşlarını yağdırır ve sonunda geriye, ürünü yenmiş bir ekinin rüzgârla kırılmış yaprağı kalır.

