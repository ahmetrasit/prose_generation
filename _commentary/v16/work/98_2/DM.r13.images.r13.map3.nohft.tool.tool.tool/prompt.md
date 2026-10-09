Focus: 98:2. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/98_2/D.r13/context.md =====
# 98:2 — focus

رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ

Anchor translation (canonical reading, reference only):

Allah'tan bir elçi, arındırılmış sayfalar okur.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | رَسُولٌ | رَسُول | ر س ل | N |
| 2 | مِّنَ | مِن |  | P |
| 3 | ٱللَّهِ | ٱللَّه | ء ل ه | PN |
| 4 | يَتْلُوا۟ | تَلَىٰ | ت ل و | V |
| 5 | صُحُفًا | صُحُف | ص ح ف | N |
| 6 | مُّطَهَّرَةً | مُّطَهَّرَة | ط ه ر | ADJ |


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
- 98:2 ◀ focus رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ
- 98:3 فِيهَا كُتُبٌۭ قَيِّمَةٌۭ
- 98:4 وَمَا تَفَرَّقَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ إِلَّا مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَةُ
- 98:5 وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ
- 98:6 إِنَّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ ۚ أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ
- 98:7 إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ
- 98:8 جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ


===== _commentary/v16/work/98_2/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ر س ل (root_000563) — identity root of رَسُولٌ (w1)

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

## ء ل ه (root_000047) — identity root of ٱللَّهِ (w3)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## ت ل و (root_000186) — identity root of يَتْلُوا۟ (w4)

- **B001** ardından izleme — bir şeyin ardından gelen · onu peşinden izledi · ay onun ardından sıra ve örnek alma bakımından geldi · atlar art arda geldi · hakkımı tam alıncaya kadar izini sürdüm
  أصل واحد وهو الاتباع (maqayis)؛ تلو الشيء الذي يتلوه (sihah)؛ تلاه تبعه متابعة (mufradat)؛ جاءت الخيل تتاليا أي متتابعة (sihah)
- **B002** kutsal kitabı okuyup izleme — indirilen kutsal kitapları okuyup anlamına uymak · kutsal kitabı okudum · onu hakkıyla bilgi ve eylemle izlerler · sözleri sana indirip bildiriyoruz
  تلاوة القرآن لأنه يتبع آية بعد آية (maqayis)؛ تلوت القرآن تلاوة (sihah)؛ التلاوة تختص باتباع كتب الله المنزلة تارة بالقراءة وتارة بالارتسام (mufradat)
- **B003** ardından kalan bakiye — önceki kısmın ardından kalan borç veya hak payı · borç ya da haktan geriye kalan pay · hakkımdan bana kalan bir pay oldu · hakkımdan onun yanında bir pay bıraktım · kalan ihtiyacın peşine düşüyorum · ona izleyip alacağı bir kalan pay bıraktım
  التلية والتلاوة وهي البقية لأنها تتلو ما تقدم منها (maqayis)؛ التلية بقية الدين وكذلك التلاوة (sihah)؛ التلاوة والتلية بقية مما يتلى أي يتبع (mufradat)
- **B004** bağlı güvence ve talep — kişiyi izleyen güvence veya yükümlülük · ona güvence verdim · birini hakkı nedeniyle başka birine yönelttim
  التلاء الذمة لأنها تتبع وتطلب يقال أتليته ذمة (maqayis)؛ التلاء الذمة (sihah)؛ أتليته أحلته من الحوالة (sihah)؛ أتليت فلانا على فلان بحق أي أحلته عليه (mufradat)
- **B005** geride bırakıp terk etme — adamı terk edip yardımsız bıraktım · onu geçtim ve arkamda bıraktım
  تلوت الرجل إذا خذلته وتركته (maqayis;sihah)؛ حتى أتليته أي حتى تقدمته وصار خلفي (sihah)؛ أتليته أي سبقته (sihah)
- **B006** anneyi izleyen yavru — devenin annesini izleyen yavrusu · erken doğuran koyun · devenin yavrusu onun peşinden geldi · Tanrı ona peş peşe çocuklar verdi · sürülerin yavrusuz kalması dileği
  تلو الناقة ولدها الذي يتلوها؛ التلوة من الغنم التي تنتج قبل الصفرية؛ أتلت الناقة إذا تلاها ولدها؛ أتلاه الله أطفالا أي أتبعه أولادا
- **B007** sese karşılık veren eşlikçi — şarkıcıya sesle karşılık veren kişi
  المتالي الذي يراد صاحبه الغناء لأن كل واحد منهما يتلو صاحبه (maqayis)؛ المتالي الذي يراسل المغني بصوت رفيع (sihah)
- **B008** son nefeste olmak [kalıp] — adam son nefesindeydi
  تلى الرجل بالتشديد إذا كان بآخر رمق
- **B009** hakkında yalan söylemek [kalıp] — biri hakkında yalan söylüyor
  فلان يتلو على فلان ويقول عليه أي يكذب عليه

## ص ح ف (root_000845) — identity root of صُحُفًا (w5)

- **B001** yayılmış geniş yüzey — yayılmış geniş yüzey · yeryüzünün görünen yüzü · yüz derisi
  أصل صحيح يدل على انبساط في شيء وسعة (maqayis); الصحيف وجه الأرض (maqayis); صحيفة الوجه بشرة جلده (ayn); الصحيفة المبسوط من الشيء كصحيفة الوجه (mufradat)
- **B002** yazı yaprağı veya kitap — yazı yazılan yaprak veya kitap · yazı yaprakları · yazı yaprakları · yazı yaprakları için seyrek bir çoğul biçim
  الصحيفة وهي التي يكتب فيها والجمع صحائف والصحف (maqayis); الصحف جمع الصحيفة (ayn); الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها (jamhara); الصحيفة الكتاب والجمع صحف وصحائف (sihah); الصحيفة التي يكتب فيها وجمعها صحائف وصحف (mufradat)
- **B003** iki kapak arasında toplanmış yazı yaprakları — iki kapak arasında toplanmış yazı yaprakları bütünü · yazı yapraklarını iki kapak arasında toplamak
  سمي المصحف مصحفا لأنه أصحف أي جعل جامعا للصحف المكتوبة بين الدفتين (ayn); المصحف لأنه صحف جمعت (jamhara); مصحف مأخوذة من أصحف أي جمعت فيه الصحف (sihah); المصحف ما جعل جامعا للصحف المكتوبة (mufradat)
- **B004** yayvan çanak; küçük su biriktirme çukuru — geniş ve yayvan çanak · geniş ve yayvan çanaklar · su için yapılmış küçük biriktirme çukurları
  الصحفة القصعة المسلنطحة (maqayis); الصحاف مناقع صغار تتخذ للماء (maqayis); الصحفة شبه القصعة المسلنطحة العريضة (ayn); الصحفة القصعة وتجمع صحافا (jamhara); الصحفة كالقصعة والجمع صحاف (sihah); الصحفة مثل قصعة عريضة (mufradat)
- **B005** harf benzerliğinden doğan yanlış okuma veya aktarım — benzer harfleri karıştırmaktan doğan yanlış okuma veya aktarım · benzer harfleri karıştırıp metni yanlış aktaran kişi
  الصحفي الذي يروي الخطأ عن قراءة الصحف بأشباه الحروف (ayn); التصحيف الخطأ في الصحيفة (sihah); التصحيف قراءة المصحف وروايته على غير ما هو لاشتباه حروفه (mufradat)

## ط ه ر (root_000953) — identity root of مُّطَهَّرَةً (w6)

- **B001** kir ve kusurdan arınmışlık — kirden arılık · kirden arındı, temiz oldu · bedensel temizlik · kendisi temiz ve kusurdan uzak · kirden ve kusurdan arınmış · bedensel ve davranışsal kirlerden arındırılmış eşler · arınmış olanlar; bağlama göre temiz varlıklar veya gerçeği kavramak için kendini bozulmadan arındıranlar · kirden uzak, tertemiz içecek
  أصل واحد صحيح يدل على نقاء وزوال دنس (maqayis)؛ طهر الشئ وطهر أيضا طهارة والاسم الطهر (sihah)؛ طاهرة من النجاسة ومن العيوب (sihah)؛ الطهارة ضربان طهارة جسم وطهارة نفس (mufradat)
- **B002** adet kanamasının kesilmesi ve kanamasız dönem — kadının adet kanaması kesildi · adet kanamasının bulunmadığı dönem · kadınların kanamasız dönemleri · kadın, kanama kesildikten sonra yıkandı
  الطهر نقيض الحيض يقال طهرت المرأة (ayn;tahdhib)؛ والمرأة طاهر من الحيض (sihah)؛ طهرت المرأة طهرا وطهارة خلاف طمثت (mufradat)؛ فإذا اغتسلت قيل تطهرت واطهرت (tahdhib)
- **B003** suyla veya eşdeğer bir araçla yıkanıp temizlenme — kadın, kanama kesildikten sonra yıkandı · suyla yıkandı ve temizlendi · temizlenmek için yıkanma · suyla temizlenirler, özellikle tuvalet sonrasında yıkanırlar
  تطهرت أي اغتسلت وأطهرت والاطهار الاغتسال (ayn)؛ وتطهرت بالماء وهم قوم يتطهرون (sihah)؛ فإن معناه الاستنجاء بالماء (tahdhib)؛ فاطهروا أي استعملوا الماء أو ما يقوم مقامه (mufradat)
- **B004** kendisi temiz, başkasını temizleyen su veya araç — temizlenmede kullanılan arındırıcı şey, özellikle su · kendisi temiz olup başkasını temizleyen su · kendisi temiz ve başkasını temizleyici · temizlenme suyunun konduğu kap · diş temizleme çubuğu ağzı temizler · kirden uzak, tertemiz içecek
  والطهور الماء (maqayis)؛ الطهور الطاهر في نفسه المطهر لغيره (maqayis)؛ الطهور اسم للماء الذي يتطهر به (ayn)؛ والطهور ما يتطهر به (sihah)؛ كل طهور طاهر وليس كل طاهر طهورا (tahdhib)؛ الماء بأنه طهور تنبيها على هذا المعنى (mufradat)
- **B005** kötüden uzaklaşıp davranışını arındırma — davranışını kınanacak kirden uzak tutan · kınanacak ve kötü davranışlardan uzak durma · iç dünyayı bozulma ve kötülük kirinden arındırma · davranışını düzelt; kendini kusurlardan arındır · işlediği kötülükten dönüp yaptırıma boyun eğerek arınma · bedensel ve davranışsal kirlerden arındırılmış eşler · arınmış olanlar; bağlama göre temiz varlıklar veya gerçeği kavramak için kendini bozulmadan arındıranlar · kalpleriniz için daha temiz ve kuşkudan daha uzak
  والتطهر التنزه عن الذم وكل قبيح (maqayis)؛ التطهر أيضا التنزه والكف عن الإثم (ayn)؛ يتطهرون أي يتنزهون من الادناس ورجل طاهر الثياب أي متنزه (sihah)؛ التطهر التنزه عن الإثم وما لا يحمد (tahdhib)؛ التاركين للذنب والعاملين للصلاح (mufradat)
- **B006** kutsal yapıyı yasak eylem ve put kirinden arındırma [kalıp] — kutsal evimi yasak eylemlerden ve putların kirinden arındır
  أن طهرا بيتي يعني من المعاصي والأفعال المحرمة (tahdhib)؛ فحث على تطهير الكعبة من نجاسة الأوثان (mufradat)
- **B007** izinli ilişkiyi yasak olandan daha temiz sayma [kalıp] — onlar sizin için daha izinli ve yasaktan daha uzak bir seçenektir
  هن أطهر لكم أي أحل لكم والتطهر التنزه عما لا يحل (tahdhib)؛ حيث قال لهم هن أطهر لكم (mufradat)

## و ل ه (root_005296) — documented alternative for ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ECHO ت ل ل (root_000185) — for يَتْلُوا۟ (w4): withheld observed target; not identity

- **B001** küçük tepe veya yer kabartısı — tepe, tepecik veya yüksekçe yer
  التل معروف (maqayis); التل واحد التلال (sihah); التلال الروابي المخلوقة; التل من أصاغر الآكام (tahdhib); أصل التل المكان المرتفع (mufradat)
- **B002** boyun — boyun
  التليل العنق (maqayis); التليل العنق (sihah); التليل العنق; بعنق ذي خصل من الشعر (tahdhib); والتليل العنق (mufradat)
- **B003** yere serme veya yüzüstü düşürme — yere serdi veya düşürdü · alnı ya da yüzü üzerine düşürdü · yere serilmiş kimse · yere serilmiş kimse
  فتله أي صرعه; وتله للجبين (maqayis); وتله للجبين أي صرعه; كبه لوجهه (sihah); معنى تله صرعه; كبه لفيه (tahdhib); تله للجبين أسقطه على التل; أسقطه على تليله (mufradat)
- **B004** dökme; ele verme veya teslim etme — eline verdi veya teslim etti · döktü · bir dökümlük miktar veya dökülen şey · elime döküldü veya bırakıldı
  تل إذا صب; التلة الصبة; فتلت في يدي معناه فصبت في يدي; تللت في يديه أي دفعت إليه سلما
- **B005** sarsıp huzursuz etme; ağır sıkıntılar — sarsma, oynatma ve huzursuz etme · sarstı, oynattı ve huzursuz etti · ağır sıkıntılar · huzursuz etme ve hareket
  التلتلة الإقلاق (maqayis); تلتله أي زعزعه وأقلقه وزلزله; التلاتل الشدائد (sihah); التليلة الإقلاق والحركة; البلابل والتلاتل الشدائد (tahdhib)
- **B006** iri ve güçlü oluş; kalın, sağlam mızrak — iri ve güçlü; kalın, sağlam mızrak · kalın, sağlam ve yere seren mızrak · iri yapılı ve güçlü adam
  المتل الرمح الذي يصرع به (maqayis); المتل الشديد; رمح متل يتل به (sihah); رجل متل إذا كان غليظا شديدا; رمح متل غليظ شديد (tahdhib); المتل الرمح الذي يتل به (mufradat)
- **B007** hurma salkımı kabuğundan içki kabı — hurma salkımı kabuğundan içki kabı
  التلتلة مشربة تتخذ من قيقاءة الطلع (sihah); التلتلة قشر الطلعة يشرب فيه النبيذ; منه قيل للمشربة تلتلة لأنه يصب ما فيها في الحلق (tahdhib)
- **B008** kötü durumda olma — kötü durumda olma
  هو بتلة سوء; ببيئة سوء; بحالة سوء
- **B009** uzanma ya da tembellik — uzanıp yatma; tembellik
  والتلة الضجعة والكسل
- **B010** borçtan kalan tutar — borçtan kalan bölüm
  والتلة بقية الدين
- **B011** ağızdaki ıslaklık — ağızdaki nem veya ıslaklık
  ما هذه التلة بفيك أي البلة; التلل والبلل والتلة والبلة شيء واحد
- **B012** sapma sözünde uyaklı pekiştirme — sapmış, büsbütün sapmış · sapıklık ve onu pekiştiren uyaklı söz
  رجل ضال تال; جاءنا بالضلالة والتلالة; كل ذلك إتباع (sihah); ضال تال آل وجاء بالضلالة والتلالة والألالة (tahdhib)
- **B013** kısrağa damızlık erkek aramaya gitme — kısrağına damızlık erkek aramaya gitti
  ذهب يتال أي يطلب لفرسه فحلا وهو يفاعل

===== _commentary/v16/out/s098/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 98:2, and ## Buluşmalar) =====
## Mühürlü yazı: getirilir, açılır, okunur

Surenin belgeleri elle tutulur nesnelerdir. Kitap kelimesinin kökü bir şeyi bir şeye eklemek, dikmektir: {ar:أصل الكتب ضمك الشيء إلى الشيء, tr:aslü'l-ketbi dammüke'ş-şey'e ile'ş-şey', gloss:ketbin aslı bir şeyi bir şeye katıp birleştirmendir, source:"ك ت ب,B001"}; {ar:كتبت السقاء إذا خرزته, tr:ketebtü's-sikâe izâ harraztühû, gloss:su tulumunu diktim, source:"ك ت ب,B001"}. Yazı, harflerin deri parçaları gibi birbirine dikilmesidir: {ar:في التعارف ضم الحروف بعضها إلى بعض بالخط, tr:fi't-teâruf dammü'l-hurûf, gloss:yaygın kullanımda harfleri yazıyla birbirine katmak, source:"ك ت ب,B002"}. Sayfa kelimesi açılıp serilmiş bir yüzeydir: {ar:الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها, tr:es-suhuf vâhidetühâ sahîfe, gloss:suhuf, tekili sahîfe; üzerine yazılan beyaz deri ya da parşömen parçası, source:"ص ح ف,B002"}. Bu yapraklar iki kapak arasında toplanınca mushaf olur: {ar:جعل جامعا للصحف المكتوبة بين الدفتين, tr:cuile câmian li's-suhufi'l-mektûbe beyne'd-deffeteyn, gloss:yazılı yaprakları iki kapak arasında toplayan kılındı, source:"ص ح ف,B003"}.

İlk ayetteki münfekkîn kelimesinin kökü bu nesneye de uzanır: {ar:فككت الشيء فانفك ككتاب مختوم تفك خاتمه, tr:fekektü'ş-şey'e fenfekke ke-kitâbin mahtûmin tefükkü hâtemehû, gloss:şeyi çözdüm, o da çözüldü; mühürlü bir mektubun mührünü açman gibi, source:"ف ك ك,B001"}. Bu açıklama infikâkın köküyle kitabı tek cümlede birleştirir. Birinci ayetin düz anlamı ayrılmamaktır; arka planında ise kapalı bir mektup ve mührün henüz kırılmamış olması duyulur. Mühürü açacak olan şey ayetin sonunda gelir: {ar:ٱلْبَيِّنَةُ, tr:el-beyyine, gloss:apaçık kanıt, source:98:1}; kök anlamı {ar:البيان الكشف عن الشيء, tr:el-beyânü el-keşfü ani'ş-şey', gloss:beyan, bir şeyi açığa çıkarmaktır, source:"ب ي ن,B005"}.

İkinci ayet bu kanıtı bir taşıyıcı ve bir eylem olarak gösterir: {ar:رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ, tr:resûlün mina'llâhi yetlû suhufen mutahhera, gloss:Allah'tan, tertemiz sayfaları okuyan bir elçi, source:98:2}. Resûl hem taşınan söz hem taşıyandır: {ar:الرسول يقال للقول المتحمل وتارة لمتحمل القول, tr:er-resûlü yukâlü li'l-kavli'l-mütehammel, gloss:resûl, yüklenilen söze de sözü yüklenene de denir, source:"ر س ل,B002"}; aynı kök acele etmeden okumayı da adlandırır: {ar:على رسلك أي اتئد فيه وترسل في قراءته, tr:alâ rislik, gloss:yavaş ol, okuyuşunda ağır ve tane tane git, source:"ر س ل,B004"}. Tilâvet ise izlemektir: {ar:تلاوة القرآن لأنه يتبع آية بعد آية, tr:tilâvetü'l-Kur'ân li-ennehû yetbau âyeten ba'de âye, gloss:Kur'an'ın tilâveti, ayetin ayeti izlemesindendir, source:"ت ل و,B002"}. Mühür açıldıktan sonra okuyan, satırları birbiri ardınca izler. Yapraklar {ar:مُّطَهَّرَةًۭ, tr:mutahhera, gloss:arındırılmış, source:98:2} olarak nitelenir: {ar:أصل واحد صحيح يدل على نقاء وزوال دنس, tr:aslün vâhidün yedüllü alâ nekâin ve zevâli denes, gloss:temizliğe ve kirin gitmesine delalet eden tek kök, source:"ط ه ر,B001"}; beyaz derinin üstünde leke yoktur. Üçüncü ayet açılan yaprakların içine bakar: {ar:فِيهَا كُتُبٌۭ قَيِّمَةٌۭ, tr:fîhâ kütübün kayyime, gloss:içlerinde dosdoğru yazılar vardır, source:98:3}; dikilip birleştirilmiş yazılar dimdik durur, {ar:قومت الشيء فهو قويم أي مستقيم, tr:kavvemtü'ş-şey'e fehüve kavîm, gloss:şeyi doğrulttum, o da düzgün, dosdoğru oldu, source:"ق و م,B008"}.

Dördüncü ayet aynı aktarımı alanların tarafından görür: {ar:ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ, tr:ellezîne ûtu'l-kitâb, gloss:kendilerine kitap verilenler, source:98:4}. Gelmek, getirmek ve vermek tek köktür: {ar:آتاه إيتاء أي أعطاه وآتاه أيضا أي أتى به, tr:âtâhu îtâen, gloss:ona verdi; ayrıca onu getirdi, source:"ء ت ي,B001"}. Birinci ayetteki ta'tiyehüm ("onlara gelinceye kadar") ile dördüncü ayetteki ûtû ("verildi") aynı hareketin iki ucudur; ayetin sonundaki {ar:جَآءَتْهُمُ ٱلْبَيِّنَةُ, tr:câet'hümü'l-beyyine, gloss:apaçık kanıt onlara geldi, source:98:4} de bu getirişi tekrarlar: {ar:جاء بكذا: استحضره, tr:câe bi-kezâ, gloss:onu getirip hazır etti, source:"ج ي ء,B004"}.

Kur'an bu nesneyi başka yerlerde de sahneler. Abese suresinde Allah zikri {ar:فِى صُحُفٍۢ مُّكَرَّمَةٍۢ, tr:fî suhufin mükerreme, gloss:değerli sayfalarda, source:80:13}, {ar:مَّرْفُوعَةٍۢ مُّطَهَّرَةٍۭ, tr:merfûatin mutahhera, gloss:yüceltilmiş, arındırılmış, source:80:14}, {ar:بِأَيْدِى سَفَرَةٍۢ, tr:bi-eydî sefera, gloss:yazıcıların ellerinde, source:80:15} diye anlatır; surenin ikinci ayetinin en yakın eşidir ve yaprakları tutan elleri de gösterir. Tâhâ suresinde inkârcılar "Rabbinden bize bir ayet getirmeli değil miydi" deyince cevap verilir: {ar:أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:e-ve lem te'tihim beyyinetü mâ fi's-suhufi'l-ûlâ, gloss:önceki sayfalarda olanın apaçık kanıtı onlara gelmedi mi, source:20:133}; gelmek, beyyine ve suhuf bir arada. Müddessir suresinde inkârcıların her biri sayfaların kendisine açılmış olarak teslim edilmesini ister: {ar:أَن يُؤْتَىٰ صُحُفًۭا مُّنَشَّرَةًۭ, tr:en yü'tâ suhufen müneşşera, gloss:kendisine açılıp serilmiş sayfalar verilmesini, source:74:52}. A'lâ suresi bu sayfaları adlarıyla anar: {ar:صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ, tr:suhufi İbrâhîme ve Mûsâ, gloss:İbrahim'in ve Musa'nın sayfaları, source:87:19}. Tûr suresi serilmiş parşömen üzerine yazılmış bir kitaba yemin eder {source:52:3}, Tekvîr suresi ise kıyamette sayfaların açılmasını haber verir: {ar:وَإِذَا ٱلصُّحُفُ نُشِرَتْ, tr:ve ize's-suhufu nüşirat, gloss:sayfalar açılıp serildiğinde, source:81:10}. Vâkıa suresi örtülü bir kitaptan ve temizliğin şartından söz eder: {ar:فِى كِتَٰبٍۢ مَّكْنُونٍۢ, tr:fî kitâbin meknûn, gloss:korunmuş, örtülü bir kitapta, source:56:78}, {ar:لَّا يَمَسُّهُۥٓ إِلَّا ٱلْمُطَهَّرُونَ, tr:lâ yemessühû ille'l-mutahharûn, gloss:ona ancak arındırılmışlar dokunur, source:56:79}. Okuyan elçi formülü Cuma suresinde aynen geçer: {ar:رَسُولًۭا مِّنْهُمْ يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِهِۦ وَيُزَكِّيهِمْ, tr:resûlen minhüm yetlû aleyhim âyâtihî ve yüzekkîhim, gloss:içlerinden, onlara ayetlerini okuyan ve onları arındıran bir elçi, source:62:2}; Bakara suresinde İbrahim aynı elçiyi dua ile ister {source:2:129}. Ankebût suresi ise okuyuşu elle yazmaktan ayırır: {ar:وَمَا كُنتَ تَتْلُوا۟ مِن قَبْلِهِۦ مِن كِتَٰبٍۢ وَلَا تَخُطُّهُۥ بِيَمِينِكَ, tr:ve mâ künte tetlû min kablihî min kitâbin ve lâ tehuttuhû bi-yemînik, gloss:bundan önce bir kitap okumuyordun, onu sağ elinle de yazmıyordun, source:29:48}. Müzzemmil suresindeki emir, {ar:وَرَتِّلِ ٱلْقُرْءَانَ تَرْتِيلًا, tr:ve rattili'l-Kur'âne tertîlâ, gloss:Kur'an'ı tane tane oku, source:73:4}, resûl kökündeki ağır okuyuşun yanına konabilir.

Kaynaklar: 98:1 مُنفَكِّينَ ف ك ك B001; 98:1 ٱلْكِتَٰبِ ك ت ب B001; 98:3 كُتُبٌ ك ت ب B002; 98:2 صُحُفًا ص ح ف B002 B003; 98:2 مُّطَهَّرَةً ط ه ر B001; 98:3 قَيِّمَةٌ ق و م B008; 98:2 يَتْلُوا۟ ت ل و B002; 98:2 رَسُولٌ ر س ل B002 B004; 98:1 تَأْتِيَهُمُ ء ت ي B001; 98:4 أُوتُوا۟ ء ت ي B001; 98:4 جَآءَتْهُمُ ج ي ء B004; 98:1 ٱلْبَيِّنَةُ ب ي ن B005

## Sıra hâlinde atlar: önde giden, ardından gelen

Tilâvetin kökündeki izleme, Arapçada bir yarış alanında da görülür: {ar:جاءت الخيل تتاليا أي متتابعة, tr:câeti'l-haylü tetâliyen, gloss:atlar birbiri ardınca geldi, source:"ت ل و,B001"}. Atlar ardışık bölükler hâlinde de gelir ve bu, resûl kökünün sözüdür: {ar:جاءت الخيل أرسالا قطيعا قطيعا, tr:câeti'l-haylü ersâlen, gloss:atlar bölük bölük geldi, source:"ر س ل,B005"}. Yarışta ikinci gelen atın adı ise namaz kelimesinin kökünden gelir: {ar:قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه, tr:kad sallâ ve câe musalliyen, gloss:ikinci geldi, çünkü başı önündeki atın sağrısını izliyordu, source:"ص ل و,B006"}; kısaca {ar:المصلى تالي السابق, tr:el-musallî tâli's-sâbık, gloss:musallî, öndekinin ardından gelendir, source:"ص ل و,B006"}. Burada tilâvetin kökü ile salâtın kökü tek cümlede birleşir: ikinci at başını birincinin sağrısına dayayarak onun izini sürer.

Bu sahne ikinci ayetteki {ar:يَتْلُوا۟, tr:yetlû, gloss:okuyor, source:98:2} kelimesine bir hareket verir: okuyuş, satırın satırı izlemesidir, tıpkı atın atı izlemesi gibi. Beşinci ayetteki {ar:وَيُقِيمُوا۟ ٱلصَّلَوٰةَ, tr:ve yükîmu's-salât, gloss:namazı kılsınlar, source:98:5} emri de arka planda bu izleme duygusunu taşır: önde gideni takip eden konum. Yarışın bir de bitiş çizgisi vardır ve bu ad gelmek kökündendir: {ar:الميتاء والميداء آخر الغاية حيث ينتهي إليه جري الخيل, tr:el-mîtâ' ve'l-mîdâ', gloss:mîtâ, atların koşusunun sona erdiği son hedef, source:"ء ت ي,B010"}. Bu tanım, birinci ayetteki ta'tiyehüm ile sekizinci ayetteki {ar:تَجْرِى, tr:tecrî, gloss:akar, source:98:8} kelimelerinin köklerini tek cümlede toplar; koşu fiilinin kendisi de atlar için kullanılır: {ar:الخيل تجري والرياح تجري, tr:el-haylü tecrî, gloss:atlar koşar, rüzgârlar eser, source:"ج ر ي,B001"}. Surenin sekizinci ayetinde akan şey nehirlerdir; atların koşusu yalnızca kökün arka planında duyulur.

Kur'an elçilerin ardışıklığını aynı izleme diliyle anlatır: {ar:ثُمَّ أَرْسَلْنَا رُسُلَنَا تَتْرَا, tr:sümme erselnâ rusulenâ tetrâ, gloss:sonra elçilerimizi birbiri ardınca gönderdik, source:23:44}; aynı ayette {ar:فَأَتْبَعْنَا بَعْضَهُم بَعْضًۭا, tr:fe-etba'nâ ba'dahum ba'dâ, gloss:onların bir kısmını bir kısmının ardından getirdik, source:23:44}. Mürselât suresi ardışık gönderilenlere yemin ederek açılır {source:77:1}, Sâffât suresi de okuyanlara: {ar:فَٱلتَّٰلِيَٰتِ ذِكْرًا, tr:fe't-tâliyâti zikrâ, gloss:zikri okuyanlara andolsun, source:37:3}. Vâkıa suresi kıyamette insanları sınıflarken öne geçenleri ayrı anar: {ar:وَٱلسَّٰبِقُونَ ٱلسَّٰبِقُونَ, tr:ve's-sâbikûne's-sâbikûn, gloss:öne geçenler, öne geçenlerdir, source:56:10}.

Kaynaklar: 98:2 يَتْلُوا۟ ت ل و B001; 98:2 رَسُولٌ ر س ل B005; 98:5 ٱلصَّلَوٰةَ ص ل و B006; 98:1 تَأْتِيَهُمُ ء ت ي B010; 98:8 تَجْرِى ج ر ي B001

## Katkıyı ayıklamak: yıkamak, süzmek, saf olanı ayırmak

İkinci ayette sayfalar arındırılmıştır; beşinci ayette kulluk edenlerden muhlis olmaları ve zekât vermeleri istenir; altıncı ve yedinci ayetler yaratılmışları iki uca ayırır. Bu kelimelerin altında somut işlemler vardır. Tahâret suyla yıkanmaktır: {ar:تطهرت بالماء, tr:tetahhartü bi'l-mâ', gloss:suyla temizlendim, source:"ط ه ر,B003"}; su kendisi temizdir ve temizler: {ar:الطهور الطاهر في نفسه المطهر لغيره, tr:et-tahûr et-tâhiru fî nefsihî el-mutahhiru li-gayrih, gloss:tahûr, kendisi temiz olan ve başkasını temizleyendir, source:"ط ه ر,B004"}. İhlâsın kökü katkıdan arınmış olandır: {ar:الخالص هو ما زال عنه شوبه بعد أن كان فيه, tr:el-hâlisu mâ zâle anhü şevbühû ba'de en kâne fîh, gloss:hâlis, içindeki karışım giderilmiş olandır, source:"خ ل ص,B001"}. İşlemin kendisi tereyağını süzmektir: {ar:خلاصة السمن ما ألقي فيه من تمر أو سويق ليخلص به, tr:hulâsatü's-semn, gloss:yağın hulâsası, arınsın diye içine atılan hurma ya da kavrulmuş undur, source:"خ ل ص,B008"}; dipte kalan tortunun da adı vardır: {ar:الثفل الذي يكون أسفل هو الخلوص, tr:es-süfl ellezî yekûnü esfel, gloss:dipteki tortu, source:"خ ل ص,B008"}. Yağ kaynatılır, içine hurma ya da un atılır, karışım dibe çöker, üstteki berrak kısım alınır. Surenin kendi ifadesi bu işlemle açıklanır: {ar:أخلصت لله ديني أمحضته, tr:ahlastü li'llâhi dînî emhadtühû, gloss:dinimi Allah'a halis kıldım, onu katışıksız yaptım, source:"خ ل ص,B005"}. {ar:مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:muhlisîne lehü'd-dîn, gloss:dini O'na has kılarak, source:98:5} sözünün arka planında, tortusundan ayrılmış berrak yağ duyulur.

Zekât da arınmadır: {ar:زكاة لأنها طهارة, tr:zekâtün li-ennehâ tahâra, gloss:zekâttır, çünkü bir temizliktir, source:"ز ك و,B002"}; bu tanım zekâtı ikinci ayetteki mutahhera kelimesinin köküne bağlar. Sayfaların lekeden arınması ile dinin karışımdan arınması aynı işlemin iki yüzüdür. Berîye kelimesinin kökü de kusurdan ve hastalıktan kurtulmayı anlatır: {ar:البراءة من العيب والمكروه, tr:el-berâetü mine'l-ayb, gloss:kusurdan ve hoşa gitmeyenden uzak olmak, source:"ب ر ء,B002"}; {ar:البرء السلامة من السقم, tr:el-bur'u es-selâmetü mine's-sekam, gloss:iyileşmek, hastalıktan kurtulmak, source:"ب ر ء,B003"}. Ayıklamanın iki ucu altıncı ve yedinci ayettedir. Hayr herkesin istediği, her şeyin seçkin kısmıdır: {ar:الخير ما يرغب فيه الكل وضده الشر, tr:el-hayru mâ yerğabu fîhi'l-küll, gloss:hayır, herkesin rağbet ettiği şeydir, karşıtı şerdir, source:"خ ي ر,B001"}; {ar:الخيرات جمع خيرة وهي الفاضلة من كل شيء, tr:el-hayrât, gloss:her şeyin en üstünü, source:"خ ي ر,B002"}. Şerr ise {ar:الشر الذي يرغب عنه الكل, tr:eş-şerru ellezî yerğabu anhü'l-küll, gloss:herkesin yüz çevirdiği şey, source:"ش ر ر,B001"}. {ar:شَرُّ ٱلْبَرِيَّةِ, tr:şerru'l-beriyye, gloss:yaratılmışların en kötüsü, source:98:6} ile {ar:خَيْرُ ٱلْبَرِيَّةِ, tr:hayru'l-beriyye, gloss:yaratılmışların en hayırlısı, source:98:7} böylece süzmenin iki ürünü olarak duyulur: alınıp saklanan berrak kısım ve dibe çöküp atılan tortu.

Kur'an bu işlemleri yan yana koyar. Tevbe suresinde Peygamber'e {ar:خُذْ مِنْ أَمْوَٰلِهِمْ صَدَقَةًۭ تُطَهِّرُهُمْ وَتُزَكِّيهِم بِهَا وَصَلِّ عَلَيْهِمْ, tr:huz min emvâlihim sadakaten tutahhiruhüm ve tüzekkîhim bihâ ve salli aleyhim, gloss:mallarından onları temizleyip arındıracak bir sadaka al ve onlar için dua et, source:9:103} denir; tahâret, zekât ve salât tek ayettedir. Nahl suresinde hayvanlardan çıkan süt, halisin tortudan ayrılmasını gösterir: {ar:مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:min beyni fersin ve demin lebenen hâlisan sâiğan li'ş-şâribîn, gloss:işkembedeki artıkla kan arasından, içenlere kolayca geçen halis bir süt, source:16:66}. Zümer suresinde Peygamber'e verilen emir surenin beşinci ayetine çok yakındır: {ar:فَٱعْبُدِ ٱللَّهَ مُخْلِصًۭا لَّهُ ٱلدِّينَ, tr:fa'budi'llâhe muhlisan lehü'd-dîn, gloss:dini yalnız O'na has kılarak Allah'a kulluk et, source:39:2}; ardından {ar:أَلَا لِلَّهِ ٱلدِّينُ ٱلْخَالِصُ, tr:elâ li'llâhi'd-dînü'l-hâlis, gloss:iyi bilin ki halis din Allah'ındır, source:39:3}. Nisâ suresi tövbe edenleri {ar:وَأَخْلَصُوا۟ دِينَهُمْ لِلَّهِ, tr:ve ahlasû dînehüm li'llâh, gloss:dinlerini Allah'a halis kıldılar, source:4:146} diye anar. Leyl suresinde arınmak için malını veren {ar:ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ, tr:ellezî yü'tî mâlehû yetezekkâ, gloss:arınmak için malını veren, source:92:18} anılır; Furkân suresinde gökten indirilen su {ar:مَآءًۭ طَهُورًۭا, tr:mâen tahûrâ, gloss:tertemiz ve temizleyici bir su, source:25:48} olarak Allah'ın ayetleri arasında sayılır.

Kaynaklar: 98:2 مُّطَهَّرَةً ط ه ر B003 B004; 98:5 مُخْلِصِينَ خ ل ص B001 B005 B008; 98:5 ٱلزَّكَوٰةَ ز ك و B002; 98:6 ٱلْبَرِيَّةِ ب ر ء B002 B003; 98:7 خَيْرُ خ ي ر B001 B002; 98:6 شَرُّ ش ر ر B001

## Hesap: borç, rehin, kefil, ödeme ve ibra

Din kelimesi itaattir; borç vermek ve almak da bu köktedir: {ar:الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء, tr:ed-deyn ve dâyentü fülânen, gloss:deyn; filanla alarak ya da vererek borç alışverişi yaptım, source:"د ي ن,B003"}; ve din karşılığın kendisidir: {ar:الدين الجزاء والمكافأة, tr:ed-dînü el-cezâü ve'l-mükâfee, gloss:din, karşılık ve bedeldir, source:"د ي ن,B002"}. Ceza da borcun ödenmesi ve tahsilidir: {ar:جزيت فلانا حقه؛ جزيته قرضه, tr:cezeytü fülânen hakkahû, gloss:filana hakkını ödedim; borcunu ödedim, source:"ج ز ي,B002"}; {ar:تجازيت ديني على فلان إذا تقاضيته, tr:tecâzeytü deynî alâ fülân, gloss:filandaki alacağımı tahsil ettim, source:"ج ز ي,B003"}. Bu son cümle ceza ile din köklerini birleştirir. Karşılığın ölçüsü de verilir: {ar:الجزاء ما فيه الكفاية من المقابلة إن خيرا فخير وإن شرا فشر, tr:el-cezâü mâ fîhi'l-kifâyetü mine'l-mukâbele, in hayran fe-hayr ve in şerran fe-şer, gloss:ceza, karşılıkta yeterli olandır: iyilikse iyilik, kötülükse kötülük, source:"ج ز ي,B001"}. Bu tanım altıncı ve yedinci ayetlerdeki şerr ve hayr kelimelerini sekizinci ayetteki {ar:جَزَآؤُهُمْ, tr:cezâühüm, gloss:karşılıkları, source:98:8} kelimesine bağlar.

Hesabın diğer parçaları surenin başka kelimelerinde durur. İnfikâkın kökü rehnin çözülmesidir: {ar:فك الرقبة تخليصها من إسار الرق وفك الرهن وفكاكه تخليصه من غلق الرهن, tr:fekkü'r-rakabeti tahlîsuhâ min isâri'r-rıkk ve fekkü'r-rehn, gloss:boynu çözmek onu kölelik bağından kurtarmak, rehni çözmek onu rehin kilidinden kurtarmaktır, source:"ف ك ك,B002"}; açıklamada kurtarmak için kullanılan tahlîs, muhlisîn kelimesinin köküdür. Berîye kelimesinin kökü borçtan aklanmaktır: {ar:برئت من الديون, tr:beri'tü mine'd-düyûn, gloss:borçlardan kurtuldum, source:"ب ر ء,B004"}. Tilâvetin kökü borcun kalanını ve alacağın devrini anlatır: {ar:التلية بقية الدين, tr:et-tuliyyetü bakıyyetü'd-deyn, gloss:tuliyye, borcun kalanıdır, source:"ت ل و,B003"}. Kitabın kökü, kölenin bedelini taksitle ödeyip özgürlüğünü satın aldığı sözleşmedir: {ar:المكاتب العبد يكاتب على نفسه بثمنه فإذا سعى وأداه عتق, tr:el-mükâteb, gloss:mükâteb, kendi bedeli üzerine yazılı anlaşma yapan köledir; çalışıp ödeyince özgür olur, source:"ك ت ب,B005"}. Kayyime bir şeyin biçilen değeridir: {ar:القيمة ثمن الشيء بالتقويم, tr:el-kıymetü semenü'ş-şey'i bi't-takvîm, gloss:kıymet, değer biçmeyle belirlenen bedel, source:"ق و م,B010"}. Surenin üç kelimesi kefili adlandırır: {ar:كنت على فلان أكون كونا أي تكفلت به, tr:küntü alâ fülân, gloss:filana kefil oldum, source:"ك و ن,B003"}; {ar:الجري الضامن, tr:el-cerî ed-dâmin, gloss:cerî, kefildir, source:"ج ر ي,B003"}; {ar:الرضي المطيع والرضي المحب والرضي الضامن, tr:er-radiyy, gloss:radî, itaat eden, seven ve kefil olandır, source:"ر ض و,B006"}.

Ödemenin ters yönü de vardır. Gelmek kökü haracı adlandırır ve ceza köküyle eşitlenir: {ar:الإتاوة الخراج أو الجزية يؤديه القوم إلى الملك, tr:el-itâve el-harâc evi'l-cizye, gloss:itâve, bir topluluğun hükümdara ödediği harac ya da cizye, source:"ء ت ي,B008"}. Cizye de üzerindekini ödemektir: {ar:الجزية … سميت جزية لأنها قضاء منه لما عليه, tr:el-cizye, gloss:cizye, üzerindeki borcu ödemesi olduğu için bu adı aldı, source:"ج ز ي,B004"}. Gönüllü verişin de bir adı vardır: {ar:إلا من أعطى في رسلها أي بطيب نفس منه, tr:illâ men a'tâ fî rislihâ, gloss:gönül hoşluğuyla veren hariç, source:"ر س ل,B010"}; hayr da hibe ve maldır: {ar:الخير الهبة, tr:el-hayru el-hibe, gloss:hayır, bağıştır, source:"خ ي ر,B005"}. Zekât, insanın Allah hakkı olarak fakirlere çıkardığıdır: {ar:ما يخرج الإنسان من حق الله تعالى إلى الفقراء, tr:mâ yuhricü'l-insânu min hakkı'llâh, gloss:insanın Allah hakkından fakirlere çıkardığı, source:"ز ك و,B003"}.

Bu kelimelerle sure bir hesap olarak duyulur. Dördüncü ayette kitap verilir; beşinci ayette verilenlerden din, yani borç bilinciyle sürdürülen bir itaat ve zekâtın verilmesi istenir; altıncı ve yedinci ayetlerde hayr ve şerr tartılır; sekizinci ayette ödeme yapılır ve hesap Rableri katında, {ar:عِندَ رَبِّهِمْ, tr:inde rabbihim, gloss:Rableri katında, source:98:8}, emanet gibi saklanır. Hesap karşılıklı bir hoşnutlukla kapanır: {ar:رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ, tr:radıya'llâhü anhüm ve radû anh, gloss:Allah onlardan razı olmuş, onlar da O'ndan razı olmuşlardır, source:98:8}; {ar:المراضاة من اثنين, tr:el-murâdâtü mine'sneyn, gloss:murâdât iki taraf arasında olur, source:"ر ض و,B003"}. Alışverişin sonunda iki tarafın birbirinden razı olması gibi.

Kur'an borcu, yazıyı ve ödemeyi açıkça birleştirir. Bakara suresinde müminlere {ar:إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ, tr:izâ tedâyentüm bi-deynin ilâ ecelin müsemmen fektübûh, gloss:belirli bir süreye kadar borçlandığınızda onu yazın, source:2:282} denir. Müddessir suresinde {ar:كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ رَهِينَةٌ, tr:küllü nefsin bimâ kesebet rehîne, gloss:her can kazandığına karşılık rehindir, source:74:38}; Beled suresinde sarp yokuş {ar:فَكُّ رَقَبَةٍ, tr:fekkü rakabe, gloss:bir boyun çözmek, source:90:13} diye açıklanır. Nûr suresinde özgürlük sözleşmesi yazıyla ve vermeyle kurulur: {ar:فَكَاتِبُوهُمْ إِنْ عَلِمْتُمْ فِيهِمْ خَيْرًۭا ۖ وَءَاتُوهُم مِّن مَّالِ ٱللَّهِ ٱلَّذِىٓ ءَاتَىٰكُمْ, tr:fe-kâtibûhüm in alimtüm fîhim hayrâ, ve âtûhüm min mâli'llâhi'llezî âtâküm, gloss:onlarda bir hayır görürseniz onlarla yazılı anlaşma yapın ve Allah'ın size verdiği maldan onlara verin, source:24:33}. Tevbe suresinde Allah müminlerden canlarını ve mallarını satın alır: {ar:بِأَنَّ لَهُمُ ٱلْجَنَّةَ, tr:bi-enne lehümü'l-cenne, gloss:karşılığında cennet onlarındır, source:9:111}. Karşılığın denkliği Nebe' suresinde {ar:جَزَآءًۭ وِفَاقًا, tr:cezâen vifâkâ, gloss:tam denk bir karşılık, source:78:26}, Rahmân suresinde iyilik için söylenir {source:55:60}. Lokmân suresinde o gün kimse kimsenin borcunu ödeyemez: {ar:وَٱخْشَوْا۟ يَوْمًۭا لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ, tr:vahşev yevmen lâ yeczî vâlidün an veledih, gloss:babanın evladı yerine ödeme yapamayacağı günden korkun, source:31:33}; sekizinci ayetin son kelimesindeki haşyet burada da vardır. Fâtiha'daki {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:mâliki yevmi'd-dîn, gloss:din gününün sahibi, source:1:4} ve Bakara suresindeki aynı uyarı {source:2:48} bu hesabın gününü adlandırır. Tevbe suresi müşriklere bir ibra ilanıyla açılır: {ar:بَرَآءَةٌۭ مِّنَ ٱللَّهِ وَرَسُولِهِۦٓ إِلَى ٱلَّذِينَ عَٰهَدتُّم مِّنَ ٱلْمُشْرِكِينَ, tr:berâetün mina'llâhi ve resûlihî ile'llezîne âhedtüm mine'l-müşrikîn, gloss:Allah'tan ve elçisinden, antlaşma yaptığınız müşriklere bir ilişik kesme, source:9:1}. Aynı surede kitap verilenlerin cizyesi {ar:حَتَّىٰ يُعْطُوا۟ ٱلْجِزْيَةَ عَن يَدٍۢ, tr:hattâ yu'tu'l-cizyete an yed, gloss:cizyeyi elden verinceye kadar, source:9:29} diye anılır; muhataplar surenin dördüncü ayetindeki ûtu'l-kitâb'dır. Gönüllü veriş de aynı surededir: sadakalar fakirlere, toplayıcılara, boyunların çözülmesine ve borçlulara verilir {source:9:60}; namazı kılıp zekâtı verenler ise {ar:فَإِخْوَٰنُكُمْ فِى ٱلدِّينِ, tr:fe-ihvânüküm fi'd-dîn, gloss:dinde kardeşlerinizdir, source:9:11}. Karşılıklı hoşnutluk Tevbe suresinde surenin sekizinci ayetinin sözleriyle tekrarlanır: {ar:رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ وَأَعَدَّ لَهُمْ جَنَّٰتٍۢ تَجْرِى تَحْتَهَا ٱلْأَنْهَٰرُ, tr:radıya'llâhü anhüm ve radû anhü ve eadde lehüm cennâtin tecrî tahtehe'l-enhâr, gloss:Allah onlardan razı olmuş, onlar da O'ndan razı olmuşlardır; onlara altlarından ırmaklar akan cennetler hazırlamıştır, source:9:100}; Mâide suresinde de Allah'ın kıyamet günü sözüyle {source:5:119}. Fecr suresinde huzura kavuşmuş cana {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdıyeten mardıyye, gloss:Rabbine razı edici ve razı olunmuş olarak dön, source:89:28} denir.

Kaynaklar: 98:5 ٱلدِّينَ د ي ن B002 B003; 98:8 جَزَآؤُهُمْ ج ز ي B001 B002 B003 B004; 98:1 مُنفَكِّينَ ف ك ك B002; 98:6 ٱلْبَرِيَّةِ ب ر ء B004; 98:2 يَتْلُوا۟ ت ل و B003; 98:1 ٱلْكِتَٰبِ ك ت ب B005; 98:5 ٱلْقَيِّمَةِ ق و م B010; 98:1 يَكُنِ ك و ن B003; 98:8 تَجْرِى ج ر ي B003; 98:8 رَّضِىَ ر ض و B003 B006; 98:5 وَيُؤْتُوا۟ ء ت ي B008; 98:2 رَسُولٌ ر س ل B010; 98:7 خَيْرُ خ ي ر B005; 98:5 ٱلزَّكَوٰةَ ز ك و B003

## Buluşmalar

En yoğun buluşma beşinci ayetteki salât kelimesindedir. Kökü bir yandan ateşte ısıtılıp düzeltilen çubuğu, {ar:صليت العود بالنار, tr:salleytü'l-ûde bi'n-nâr, gloss:çubuğu ateşte ısıtıp yumuşattım, source:"ص ل و,B001"}, öbür yandan ateşe girip yanan kâfiri, {ar:صلى الكافر نارا, tr:sale'l-kâfiru nârâ, gloss:kâfir ateşe girip yandı, source:"ص ل و,B001"}, adlandırır. Aynı ateş iki iş görür: eğri olanı doğrultur ya da yakar. Beşinci ayette ateş bir doğrultma aletidir; altıncı ayette inkâr edenlerin kaldığı yerdir. Doğrultma ile ocak sahneleri böylece tek bir kökün iki işlemi olarak birleşir ve surenin ikiye ayrılan yolunu taşır: kanıttan sonra doğrulup ayağa kalkanlar ve ateşte kalanlar. Aynı kök tuzağı da adlandırır; ama surede salât tuzaktan sıyrılmış olanların fiilidir.

Münfekkîn kelimesi üç sahneyi bir noktada tutar. Kökü tuzaktan kurtulan ceylanı, mührü açılan mektubu ve çözülen rehni anlatır. Birinci ayette bu kelime olumsuzdur: ip çözülmemiş, mühür açılmamış, rehin kurtarılmamıştır, ve bütün bunlar kanıtın gelişine bağlıdır. Rehnin çözülmesini anlatan cümlede infikâkın ve ihlâsın kökü yan yanadır, tuzaktan kurtulmayı anlatan cümlelerde de; bu yüzden birinci ayetteki çözülmeme ile beşinci ayetteki muhlisîn, hem avın hem borçlunun kurtuluşu olarak duyulur. Yazı ile kenet de aynı kelimede buluşur: mühürlü mektubun açılması ile iki çenenin ayrılması tek cümlede verilir ve dördüncü ayette açılan yazının ardından gelen ayrılık bunun devamıdır.

Teferruk kelimesi kenet ile yol sahnesini birleştirir. En'âm suresinde yan yollara uyunca insanların yoldan ayrı düşmesi {source:6:153}, hem çatallanan yolu hem bölünen topluluğu tek cümlede gösterir. Müşriklerin kökü ana yoldan ayrılan küçük patikaları adlandırdığı için dördüncü ayetteki ayrılık arka planda bir çatal noktasına, beşinci ayetteki hunefâ ise yan patikadan ana yola dönüşe dönüşür. Yol ile binek sahnesi müzellel kelimesinde birleşir: yürünmekle düzleşen yol ile katranla uysallaşan deve aynı kelimeyle anlatılır ve inde kelimesinin kökü ikisinin de tersini, yoldan sapan ve dizgini çeken deveyi verir. Doğrultma ile yol da kayyime kelimesinde birleşir: dik duran beden ile düz hat üzerindeki yol aynı kökle anlatılır; En'âm suresinde Peygamber'e söyletilen söz {source:6:161} yolu, kayyim olanı, hanifi ve müşrikleri tek ayette toplar.

Arındırma ile ekim zekâtta birleşir. Zekât hem bir temizliktir hem ekinin büyümesi ve hurmanın ürünüdür. Tâhâ suresinde surenin sekizinci ayetinin bahçesi tam olarak bu kelimeyle bağlanır: Adn cennetleri {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76}. Beşinci ayetteki zekât, sekizinci ayetteki bahçenin tohumu gibi durur. Arındırma ile hesap da hayr ve şerr kelimelerinde buluşur: süzmenin iki ürünü, karşılığın iki ölçüsüne dönüşür, iyiliğe iyilik ve kötülüğe kötülük.

Örtü ile ocak da kesişir: küfrün kökü üstü örtülmüş külü adlandırır. Örtü ile ekim ise aynı kelimede, tohumu örten çiftçide buluşur. Bakara suresindeki temsil {source:2:266} bu sahnelerin üçünü birden tutar: altından ırmaklar akan hurma bahçesi ve onu yakan ateşli kasırga. Altıncı ve sekizinci ayetler aynı sözü, hâlidîne fîhâ, ateş ve bahçe için kullanır; hulûdun kökü bir yandan ateşin içinde kalan ocak taşlarını, öbür yandan bir yerde yerleşip kalmayı adlandırır. Kalmanın iki yeri böylece aynı kelimede yan yana durur.

Bu buluşmalar surenin hareketini taşır. Birinci ayette bir şey kapalıdır: ilmek düğümlü, mühür kırılmamış, topluluk kendi hâlinde. Kanıt bir elçinin elinde, arındırılmış sayfalar olarak gelir ve okunur. Dördüncü ayette topluluk bu kanıtın ardından bölünür. Beşinci ayet çıkış yolunu tek cümlede verir: işaretli, düzleşmiş, dosdoğru bir yol; katkısından süzülmüş bir din; ateşte doğrultulan bir beden; tuzaktan sıyrılış; ürün veren bir ekin. Altıncı ve yedinci ayetler sonucu iki uca ayırır. Sekizinci ayet bir yerleşmeyle biter: Rableri katında, örtülü bir bahçede, ebedî bir kalış ve iki tarafın birbirinden razı olduğu kapanmış bir hesap.

