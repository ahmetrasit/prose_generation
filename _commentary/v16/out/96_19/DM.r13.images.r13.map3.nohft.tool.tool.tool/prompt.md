Focus: 96:19. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/96_19/D.r13/context.md =====
# 96:19 — focus

كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩

Anchor translation (canonical reading, reference only):

Hayır! Ona itaat etme, secde et ve yaklaş.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | كَلَّا | كَلَّا |  | AVR |
| 2 | لَا | لَا |  | PRO |
| 3 | تُطِعْهُ | أَطَاعَ | ط و ع | V;PRON |
| 4 | وَٱسْجُدْ | سَجَدَ | س ج د | CONJ;V |
| 5 | وَٱقْتَرِب | ٱقْتَرَبَ | ق ر ب | CONJ;V |


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
- 96:15 كَلَّا لَئِن لَّمْ يَنتَهِ لَنَسْفَعًۢا بِٱلنَّاصِيَةِ
- 96:16 نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ
- 96:17 فَلْيَدْعُ نَادِيَهُۥ
- 96:18 سَنَدْعُ ٱلزَّبَانِيَةَ
- 96:19 ◀ focus كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩


===== _commentary/v16/work/96_19/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ط و ع (root_000956) — identity root of تُطِعْهُ (w3)

- **B001** zorlanmadan boyun eğme ve kolay yönlenme — zorlamanın karşıtı olan isteyerek boyun eğme · emre uyma ve gereğini yerine getirme · ona boyun eğdi · emrini yerine getirdi · zorlanmadan uyan kimse · uyan ve boyun eğen kimse · çok söz dinleyen ve kolay uyan kimse · kolay yönlendirilen ve söz dinleyen · elin altında ve tasarrufa hazır · dizginle kolay yönlendirilen · yatak arkadaşına uyum gösteren · dili buna dönmüyor · güçlüklere alışkın ve onları göğüsleyen
  أصل صحيح واحد يدل على الإصحاب والانقياد (maqayis); الطوع نقيض الكره (ayn;tahdhib;mufradat); طاع له إذا انقاد له (ayn;sihah;tahdhib;mufradat); فرس طوع العنان (ayn;sihah;tahdhib); بعير طيع سلس القياد (tahdhib); لسانه لا يطوع بكذا (sihah)
- **B002** taraflar arasında uyum gösterme — ona uyum gösterdi veya onu izledi · taraflar arasında uyum gösterme · uyumlu olma ve kolay söz dinleme niteliği
  لمن وافق غيره قد طاوعه (maqayis); إذا وافقك فقد طاوعك (ayn;tahdhib); الطواعية اسم لما يكون مصدر المطاوعة (ayn;tahdhib); المطاوعة الموافقة (sihah)
- **B003** bir işi yapabilecek güç ve elverişlilik — bir işi yapabilecek güç ve elverişli durum · bir şeyi yapabildi veya yapabilir oldu
  الاستطاعة مشتقة من الطوع (maqayis;ayn); الاستطاعة الإطاقة (sihah); الاستطاعة استفالة من الطوع وذلك وجود ما يصير به الفعل متأتيا (mufradat); يقال ما أستطيع وما اسطيع وما أسطيع وما أستيع (tahdhib)
- **B004** yapabilir hale gelmek için kendini zorlama — işi yapabilir hale gelene kadar kendini zorladı · yapmaya kendini zorladı veya isteyerek üstlendi
  تطاوع لهذا الأمر حتى تستطيعه (maqayis;ayn;sihah;tahdhib); تطوع أي تكلف استطاعته (maqayis;sihah;tahdhib); وتطوع كذا تحمله طوعا (mufradat)
- **B005** yükümlü olmadığı iyiliği gönüllü yapma — yükümlü olmadığı şeyi gönüllü olarak verdi veya yaptı · zorunlu olmayan iyiliği gönüllü yapma · savaş hizmetine gönüllü katılan topluluk
  التبرع بالشيء قد تطوع به (maqayis); لا يقال هذا إلا في باب الخير والبر (maqayis); التطوع ما تبرعت به مما لا يلزمك فريضته (ayn;sihah;tahdhib); المطوعة القوم الذين يتطوعون بالجهاد (ayn;sihah;tahdhib); التطوع في التعارف التبرع بما لا يلزم كالتنفل (mufradat)
- **B006** iç benliğin işi kolay gösterip yöneltmesi — nefsi ona işi kolay gösterdi ve ona yöneltti
  قد تطوع لك طوعا إذا انقاد (ayn); فطوعت له نفسه رخصت وسهلت (sihah); فتابعته نفسه (tahdhib); شجعته (tahdhib); أعانته على ذلك وأجابته إليه (tahdhib); سمحت وسهلت له نفسه (tahdhib); أسمحت له قرينته وانقادت له وسولت (mufradat)
- **B007** otlak veya meyvenin yararlanılabilir hale gelmesi — otlağı bulup ondan istediği kadar yedi · otlak ona genişleyip otlamaya elverişli oldu · meyveli ağaç ürünü olgunlaşıp toplanabilir oldu · otlak ona genişleyip otlamayı mümkün kıldı
  أطاع لها الكلأ إذا أصابت فأكلت منه ما شاءت (ayn); أطاع النخل والشجر إذا أدرك ثمره وأمكن أن يجتنى (sihah); أطاع له المرتع إذا اتسع له وأمكنه من الرعي (sihah;tahdhib); قد يقال في هذا الموضع طاع (tahdhib)

## س ج د (root_000675) — identity root of وَٱسْجُدْ (w4)

- **B001** alçalıp boyun eğme ve alnı yere koyma — boyun eğmek veya alnını yere koymak · alçalıp boyun eğme; isteyerek ya da zorunlu düzene bağlılık · bir kez alnını yere koyarak eğilme veya bu eğilişin biçimi
  أصل واحد مطرد يدل على تطامن وذل (maqayis)؛ سجد: خضع ومنه سجود الصلاة وهو وضع الجبهة على الأرض (sihah)؛ سجد إذا وضع جبهته بالأرض (tahdhib)؛ السجود أصله التطامن والتذلل (mufradat)
- **B002** alnı yere koyma yeri, buna ayrılmış yapı veya küçük yaygı — toplu tapınma yeri veya bu amaçla kurulmuş yapı · zeminde alnın konduğu yer · iki belirli kutsal kentteki iki tanınmış tapınma yapısı · üzerinde alnı yere koyarak eğilinen küçük dokuma yaygı · tapınma yerleri veya alnı yere koymaya elverişli yerler
  المسجد اسم جامع يجمع المسجد وحيث لا يسجد بعد أن يكون اتخذ لذلك (ayn)؛ المسجد معروف (jamhara)؛ المسجد والمسجد واحد المساجد والمسجدان مسجد مكة ومسجد المدينة (sihah)؛ المسجد موضع الصلاة (mufradat)؛ السجادة الخمرة (sihah)
- **B003** yere dayanan beden bölümleri ve alındaki temas izi — alnı yere koyarken yere dayanan beden bölümleri · alnın yere değen ve temas izi oluşan bölümü · alında tekrarlanan yere temasın bıraktığı iz
  المسجد الإرب الذي يسجد عليه مثل الكفين والركبتين والقدمين والجبهة (jamhara)؛ الآراب السبعة مساجد والمسجد بالفتح جبهة الرجل حيث يصيبه ندب السجود (sihah)؛ المساجد مواضع السجود من الإنسان الجبهة والأنف واليدان والركبتان والرجلان (tahdhib;mufradat)
- **B004** başı ve gövdeyi aşağı eğme veya yük altında yana yatma — başını alçaltıp gövdesini öne eğmek · belden öne eğilmiş durumda olmak · meyve yüküyle eğilip yana yatmış hurma ağacı
  أسجد الرجل إذا طأطأ رأسه وانحنى (maqayis;sihah;tahdhib)؛ أسجد للبعير أي طأطأ لها لتركبه (sihah;tahdhib)؛ سجدا أي ركعا (tahdhib)؛ نخلة ساجدة إذا أمالها حملها (tahdhib)
- **B005** bakışı aşağıda ve devinimsiz tutma, göz kapaklarında gevşeklik — bakışı aşağı yönelmiş durumda uzun süre ve devinimsiz tutma · durgun ve gevşek bakışlı göz · gözleri durgun ve gevşek görünen kadınlar
  الإسجاد إذا أدام النظر في خفض (maqayis)؛ الإسجاد إدامة النظر مع سكون (ayn;tahdhib)؛ أصل السجود إدامة النظر في إطراق إلى الأرض (jamhara)؛ الإسجاد إدامة النظر وإمراض الأجفان (sihah)؛ نساء سجد فاترات الأعين وامرأة ساجدة ساجية (ayn)؛ الإسجاد أيضا فتور الطرف (tahdhib)
- **B006** önünde eğilinilen hükümdar betimli sikkeler [kalıp] — üzerlerindeki betimler veya betimlenen hükümdar önünde eğilinilen sikkeler
  دراهم الإسجاد دراهم كانت عليها صور فيها صور ملوكهم وكانوا إذا رأوها سجدوا لها (maqayis)؛ دراهم كانت عليها صور يسجدون لها (sihah)؛ دراهم عليها صورة ملك سجدوا له (mufradat)
- **B007** Yahudiler için ad, baş vergisi ve bu verginin parası — Yahudiler · baş vergisi · baş vergisi olarak verilen para
  الإسجاد بكسر الهمزة اليهود (tahdhib)؛ أعطونا إسجادا أي الجزية (tahdhib)؛ دراهم الأسجاد عنى دراهم الجزية (tahdhib)

## ق ر ب (root_001212) — identity root of وَٱقْتَرِب (w5)

- **B001** yakın olma, yaklaşma veya yaklaştırma — yakın olmak veya yaklaşmak · yaklaştırmak, yakına getirmek · yaklaşma · ses değişmesiyle yaklaşmak · suyu yakın kuyu · parçaları birbirine yakın, kısa yapılı
  أصل صحيح يدل على خلاف البعد (maqayis)؛ كرب الشيء دنا فليس من الباب وإنما هو من الإبدال من القرب (maqayis-ibdal)؛ قرب الشيء قربا ضد البعد (jamhara)؛ قرب الشيء يقرب قربا أي دنا والقرب ضد البعد (sihah)؛ القرب نقيض البعد والتقرب التدني إلى شيء والاقتراب الدنو والقرب البئر القريبة الماء والرجل القصير متقارب (tahdhib)؛ القرب والبعد يتقابلان ويستعمل ذلك في المكان (mufradat)
- **B002** zamanca yaklaşma veya yakın geçmişe ait olma — vaadin veya hesap vaktinin yaklaşması · son saatin yaklaşması · ürünün olgunlaşma vaktinin yaklaşması · güneşin batmaya yaklaşması · henüz taze olan tuzlu balık
  اقترب الوعد أي تقارب (sihah)؛ تقارب الزمان اقتراب الساعة وتقارب الزرع إذا دنا إدراكه والشيء إذا ولى وأدبر قد تقارب والقريب السمك المملح ما دام في طراءته (tahdhib)؛ في الزمان نحو اقترب للناس حسابهم (mufradat)؛ كربت الشمس دنت للمغيب (maqayis-ibdal)
- **B003** akrabalık ve yakın akraba — akrabalık, soy bağı · yakın akraba · yakın akrabalığı olan kimse
  فلان ذو قرابتي وهو من يقرب منك رحما والقربة والقربى القرابة (maqayis)؛ قريب الرجل مدانيه من نسب أم أو أب والجمع قرابة وقرباء وأقرباء (jamhara)؛ القرابة القربى في الرحم وهو قريبي وذو قرابتي وهم أقربائي وأقاربي (sihah)؛ القريب والقريبة ذو القرابة وفلان ذو قرابتي وذو مقربة وذو قربى (tahdhib)؛ في النسبة أولوا القربى والأقربون وذو قربى ولذي القربى والجار ذي القربى ويتيما ذا مقربة (mufradat)
- **B004** ayrıcalıklı yakın çevre — yakın kılınmış, gözde kişiler · hükümdarın özel çevresi, oturum arkadaşları ve yöneticileri · yakın kılınmış melekler
  قربان الملك وقرابينه وزراؤه وجلساؤه (maqayis)؛ قرابين الملك خاصته وقربان الملك قرابته والجمع قرابين (jamhara)؛ القربان واحد قرابين الملك وهم جلساؤه وخاصته (sihah)؛ القرابين جلساء الملوك وخاصته وقرابين الملك وزراؤه (tahdhib)؛ في الحظوة الملائكة المقربون ومن المقربين وقربناه نجيا (mufradat)؛ الملائكة الكروبيون وهم المقربون (maqayis-ibdal)
- **B005** Tanrı'ya yakınlık kazandıran iş veya sunu — Tanrı'ya yakınlık kazandıran iyi iş veya araç · Tanrı'ya yakınlık için sunulan şey veya kesilen hayvan · iyi bir iş veya sunuyla Tanrı'ya yakınlık aramak
  القربان ما قرب إلى الله تعالى من نسيكة أو غيرها (maqayis)؛ ما له عند الله قربة والقربان الأضاحي وكل ما تقرب إلى الله فهو قربان (jamhara)؛ القربان ما تقربت به إلى الله وتقرب إلى الله بشيء طلب به القربة (sihah)؛ القربان ما قربت إلى الله تبتغي بذلك قربة ووسيلة وهي ذبائح كانوا يذبحونها (tahdhib)؛ القربان ما يتقرب به إلى الله وصار اسما للنسيكة التي هي الذبيحة والقربة قربات عند الله (mufradat)
- **B006** gözetme, güç ve ruhsal yöneliş bakımından yakınlık — gözetip karşılık vermek üzere yakın · gücü ve erişimi bakımından insana en yakından hakim · insanın Tanrı'ya ruhsal yakınlığı
  في الرعاية نحو فإني قريب أجيب دعوة الداع وفي القدرة نحو ونحن أقرب إليه من حبل الوريد وقرب الله تعالى من العبد هو بالإفضال عليه والفيض لا بالمكان وقرب العبد من الله قرب روحاني لا بدني (mufradat)
- **B007** temas edip içine girecek ölçüde yaklaşma — bir işe bulaşmak, girişmek veya onu yapmak üzere olmak · yasak şeye yönelmemek ve onunla temas kurmamak · eşiyle cinsel ilişkide bulunmak
  ما قربت هذا الأمر ولا أقربه إذا لم تشامه ولم تلتبس به (maqayis)؛ قرب فلان أهله قربانا إذا غشيها وما قربت هذا الأمر ولا قربته ولا تقربا هذه الشجرة ولا تقربوا الزنى (tahdhib)؛ ولا تقربوهن كناية عن الجماع ولا تقربوا مال اليتيم أبلغ من النهي عن تناوله ولا تقربوا الزنى (mufradat)
- **B008** geceleyin su kaynağına yönelme — suya varıştan önceki gece yolculuğu · su arayıp kaynağa doğru gitmek · geceleyin su arayan kişi veya hayvan · suya doğru giderken acele etmek · suya gidip gelen hiç kimsesi yok
  من الباب القرب وهي ليلة ورود الإبل الماء والقارب الطالب الماء ليلا (maqayis)؛ القرب أن يرعى القوم بينهم وبين المورد حتى إذا كان بينهم وبين الماء عشية أو ليلة عجلوا فقربوا وحمار قارب يطلب الماء (ayn)؛ قربت الإبل الماء إذا طلبته وليلة القرب ليلة طلب الماء (jamhara)؛ القرب سير الليل لورد الغد والقارب طالب الماء ليلا (sihah)؛ ليلة القرب هو السوق الشديد وتقرب أي اعجل وقربت الماء أي طلبته والقرب سير الليل (tahdhib)؛ رجل قارب قرب من الماء وليلة القرب وأقربوا إبلهم (mufradat)
- **B009** su tulumu — su tulumu, deri su kabı
  القربة معروفة (jamhara)؛ القربة ما يستقى فيه الماء والجمع قربات وقربات وقربات وللكثير قرب (sihah)؛ القربة وجمعها قرب من الأساقي (tahdhib)
- **B010** kılıç kını veya deri dış kabı — kılıç kını veya kını saran deri kap · kılıcı kabına koymak veya ona bir kap yapmak
  منه القراب قراب السيف والجمع قرب (maqayis)؛ قراب السيف جلد يكون فيه وليس بالغمد والجمع قرب (jamhara)؛ قراب السيف جفنه وهو وعاء يكون فيه السيف بغمده وحمالته (sihah)؛ القراب للسيف والسكين وقربته جعلته في القراب (tahdhib)؛ القراب وعاء السيف وقيل جلد فوق الغمد لا الغمد نفسه (mufradat)
- **B011** gemiye bağlı küçük hizmet teknesi — gemiye eşlik eden küçük hizmet teknesi
  القارب سفينة صغيرة تكون مع أصحاب السفن البحرية وكأنها سميت بذلك لقربها منهم (maqayis)؛ قارب السفينة وهو الصغير الذي يتبعها (jamhara)؛ القارب سفينة صغيرة تكون مع أصحاب السفن البحرية تستخف لحوائجهم (sihah)؛ القارب سفينة صغيرة تكون مع أصحاب السفن البحرية تستخف لحوائجهم والجميع القوارب (tahdhib)
- **B012** doğumu yaklaşmış gebe dişi — koyunun doğumu yaklaşmak · doğumu yaklaşmış gebe dişi
  أقربت الشاة دنا نتاجها (maqayis)؛ شاة مقرب إذا دنا ولادها (jamhara)؛ أقربت المرأة إذا قرب ولادها وكذلك الفرس والشاة فهي مقرب ولا يقال للناقة (sihah)؛ أقربت الشاة والأتان فهي مقرب ولا يقال للناقة إلا إذا أدنت فهي مدن (tahdhib)؛ المقرب الحامل التي قربت ولادتها (mufradat)
- **B013** yakında tutulan ve binmeye hazırlanan hayvan — yakında tutulan, gözetilen ve binmeye hazır at · binmek için bağlanmış veya eyerlenmiş develer
  فرس مقربة وهي التي ترتاد وتقرب ولا تترك أن ترود (maqayis)؛ فرس مقربة وهي التي تدنى وتقرب ولا تترك أن ترود والمقربة المكرمة (jamhara)؛ المقرب من الخيل الذي يدنى ويكرم والأنثى مقربة (sihah)؛ الخيل المقربة التي تكون قريبا معدة والتي تدنى وتقرب وتكرم والإبل المقربة التي حزمت للركوب (tahdhib)
- **B014** atın dörtnaldan yavaş özel koşusu — atın dörtnaldan yavaş özel koşu biçimi
  قرب الفرس تقريبا وهو دون الحضر وله تقريبان أدنى وأعلى (maqayis)؛ قرب الفرس تقريبا وهو تقريبان التقريب الأدنى والتقريب الأعلى وهو دون الحضر (jamhara)؛ التقريب ضرب من العدو وهو دون الحضر (sihah)؛ إذا رفع الفرس يديه معا ووضعهما معا فذلك التقريب (tahdhib)؛ تقريب الفرس سير يقرب من عدوه (mufradat)
- **B015** böğür, bedenin yan bölgesi — böğür, bel ile karnın alt yanı arasındaki bölge · böğürler, bedenin yanları · yürürken elini böğrüne koymuş
  الخاصرة هي القرب سميت لقربها من الجنب (maqayis)؛ قرب الفرس كشحه وهو الخصر والجمع أقراب (jamhara)؛ القرب من الشاكلة إلى مراق البطن والجمع الأقراب (sihah)؛ القرب من لدن الشاكلة إلى مراق البطن ومتقربا أي واضعا يده على قربه (tahdhib)؛ فرس لاحق الأقراب أي الخواصر (mufradat)
- **B016** bir ölçü veya sınıra yaklaşık olma — bir şeyin doluluğuna, sayısına veya miktarına yakın değer · neredeyse dolu kap · ses değişmesiyle neredeyse dolu kap · orta kalitede veya ucuz kumaş · satışta önerileri birbirine yaklaştırmak · akşama veya geceye yakın vakit
  ثوب مقارب إذا لم يكن جيدا وهذا على معنى أنه مقارب في ثمنه (maqayis)؛ الدراهم قراب مائة وإناء قربان إذا قارب أن يمتلىء وقراب كل شيء ما قارب الامتلاء (jamhara)؛ شيء مقارب وسط بين الجيد والردئ أو رخيص وقدح قربان إذا قارب أن يمتلئ وقاربته في البيع مقاربة (sihah)؛ القراب مقاربة الشيء معه ألف درهم أو قرابه وأتيته قراب العشي أو قراب الليل وقدح قربان ماء ولو أن في قراب هذا ذهبا (tahdhib)؛ القراب المقاربة وقدح قربان قريب من الملء (mufradat)؛ إناء كربان كرب أن يمتلىء (maqayis-ibdal)

## ECHO س ط ع (root_000706) — for تُطِعْهُ (w3): withheld observed target; not identity

- **B001** havada uzama, yükselme veya yayılma — havada yükselmek, uzamak veya yayılmak · yukarı doğru uzanan sabah aydınlığı · sabah aydınlığı · okun göğe yükselip parlaması · misk kokusunun burnuna ulaşması
  أصل يدل على طول الشيء وارتفاعه في الهواء (maqayis)؛ كل شيء ينتشر فينبسط نحو البرق والغبار والريح الطيبة (ayn)؛ سطع الغبار والرائحة والصبح إذا ارتفع (sihah)؛ سطع ضوؤه في السماء والبرق يسطع في السماء وسطع السهم فشخص في السماء وسطعت الرائحة إذا فاحت (tahdhib)
- **B002** boyun uzunluğu — boyun uzunluğu · başını kaldırıp boynunu uzatmak · uzun boyunlu erkek devekuşu · uzun boyunlu dişi devekuşu
  السطع وهو طول العنق وظليم أسطع ونعامة سطعاء (maqayis)؛ السطع طول العنق نعامة سطعاء (sihah)؛ ظليم أسطع إذا كان عنقه طويلا والأنثى سطعاء وفي عنقه سطع أي طول (tahdhib)
- **B003** ev direği — ev veya çadır direği · direğe benzetilen uzun deve
  السطاع عمود من عمد البيت (maqayis)؛ السطاع عمود البيت (sihah)؛ السطاع عمود من أعمدة البيت وللبعير الطويل سطاع تشبيها بسطاع البيت (tahdhib)
- **B004** deve boynundaki uzunlamasına damga — deve boynundaki uzunlamasına damga · boynu uzunlamasına damgalı deve
  السطاع سمة في عنق البعير بالطول يقال بعير مسطع (sihah)؛ السطاع من سمات الإبل في العنق بالطول وناقة مسطوعة وإبل مسطعة (tahdhib)
- **B005** avuç ya da parmak vuruşu ve sesi — bir şeye avuç içiyle veya parmakla vurma · vuruş sesi · vuruş veya vuruş sesi
  السطع ارتفاع صوت الشيء إذا ضربت عليه شيئا يقال سطعة (maqayis)؛ السطع أن تسطع شيئا براحتك أو بإصبعك ضربا وسمعت لضربته سطعا يعني صوت الضربة (tahdhib)
- **B006** belirli bir dağın özel adı — belirli bir dağın özel adı
  أما السطاع في شعر هذيل فهو جبل بعينه (maqayis)؛ السطاع اسم جبل بعينه (tahdhib)

===== _commentary/v16/out/s096/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 96:19, and ## Buluşmalar) =====
## Rahimde toplanan, tutunan, biçim alan

Bu surenin kelimelerinin çoğu, ayetteki anlamlarının yanında aynı kök ailesinin başka bir sahnesini de duyurur. Bu aile imgesi kelimenin ayetteki anlamının yerine geçmez; onun yanında işitilir. Aşağıdaki her bölüm bu yan sahneleri ayetin kendi anlamına dayanarak okur.

İlk sahne bir rahimdir. Kan rahimde toplanır, rahim onun üzerine kapanır, toplanan şey tutunur ve gebelik kalıcı olur. Sonra biçim belirir, ardından doğum yaklaşır. Gebelik bazen de biçim belli olmadan düşer. Surenin ilk emri olan {ar:ٱقْرَأْ, tr:ikra, gloss:oku, source:96:1} kelimesinin kökü, okumanın yanında dişinin rahminde bir şey taşımasını da adlandırır: {ar:ما قرأت الناقة سلى قط … لم تحمل علقة أي دما ولا جنينا, tr:mâ kara'eti'n-nâkatu selan katt … lem tahmil ʿalakaten ey demen ve lâ cenînen, gloss:dişi deve hiç yavru zarı taşımadı … yani hiç kan pıhtısı ya da cenin taşımadı, source:"ق ر ء,B004"}. Bu söz okumanın kökünü, ikinci ayetin {ar:عَلَقٍ, tr:alak, gloss:tutunan pıhtı, source:96:2} kelimesiyle aynı cümlede birleştirir. Aynı kök, rahmin temizlik ve kanama dönemlerini de adlandırır: {ar:القرء الحيض والقرء أيضا الطهر, tr:el-kur'u'l-hayzu ve'l-kur'u eyzan et-tuhr, gloss:kur' hem âdet hem temizlik dönemidir, source:"ق ر ء,B003"}. Kurân bu kelimeyi tam bu anlamda kullanır ve hemen arkasından rahimde yaratılanı anar. Boşanmış kadınlar {ar:ثَلَٰثَةَ قُرُوٓءٍ, tr:selâsete kurû', gloss:üç dönem, source:2:228} bekler ve {ar:مَا خَلَقَ ٱللَّهُ فِىٓ أَرْحَامِهِنَّ, tr:mâ halaka'llâhu fî erhâmihinn, gloss:Allah'ın rahimlerinde yarattığını, source:2:228} gizlemezler. Böylece okumanın kökü ile yaratmanın fiili aynı ayette rahimde buluşur.

İkinci ayet bu sahnenin başlangıcını adlandırır. Alak hem donmuş kan parçasıdır, {ar:العلق الدم الجامد والقطعة منه علقة, tr:el-ʿalaku'd-demu'l-câmid, gloss:alak donmuş kandır, bir parçasına alaka denir, source:"ع ل ق,B003"}, hem de gebeliğin tutunmasıdır, {ar:علقت المرأة حبلت, tr:ʿalikati'l-mer'e: hebilet, gloss:kadın tutundu, yani gebe kaldı, source:"ع ل ق,B009"}. Birinci ve ikinci ayetlerdeki {ar:خَلَقَ, tr:halaka, gloss:yarattı, source:96:2} fiilinin ailesinde biçimi belirmiş cenin vardır: {ar:مخلقة قد بدا خلقها وغير مخلقة لم تصور, tr:muhallaka kad bedâ halkuhâ ve gayru muhallaka lem tusavver, gloss:biçimlenmiş, yani yaratılışı belirmiş; biçimlenmemiş, yani henüz şekil verilmemiş, source:"خ ل ق,B003"}. Kurân bu aşamaları yeniden diriliş için kanıt olarak sayar. Allah insanlara, dirilişten şüphe ediyorlarsa, onları {ar:مِنْ عَلَقَةٍ ثُمَّ مِن مُّضْغَةٍ مُّخَلَّقَةٍ وَغَيْرِ مُخَلَّقَةٍ, tr:min ʿalakatin summe min mudgatin muhallakatin ve gayri muhallaka, gloss:bir pıhtıdan, sonra biçimlenmiş ve biçimlenmemiş bir çiğnemlik etten, source:22:5} yarattığını söyler ve ekler: {ar:وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ, tr:ve nukirru fi'l-erhâmi mâ neşâ', gloss:dilediğimizi rahimlerde durdururuz, source:22:5}. Başka bir yerde aşamalar birbirine yaratma fiiliyle bağlanır: {ar:فَخَلَقْنَا ٱلْعَلَقَةَ مُضْغَةً, tr:fe halaknâ'l-ʿalakate mudga, gloss:pıhtıyı bir çiğnemlik et olarak yarattık, source:23:14}. Dirilişi inkâr eden insana da aynı soru sorulur: {ar:ثُمَّ كَانَ عَلَقَةً فَخَلَقَ فَسَوَّىٰ, tr:summe kâne ʿalakaten fe halaka fe sevvâ, gloss:sonra bir pıhtı oldu, O da yarattı ve düzenledi, source:75:38}. Biçimi verenin kim olduğu da açıkça söylenir: {ar:يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ, tr:yusavvirukum fi'l-erhâm, gloss:sizi rahimlerde biçimlendirir, source:3:6}.

Surenin üçüncü ve sekizinci ayetlerinde de geçen {ar:رَبِّكَ, tr:rabbike, gloss:Rabbin, source:96:1} kelimesinin ailesi bu sahneye bir işleyiş ekler: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye: inşâu'ş-şey'i hâlen fe hâlen ilâ haddi't-temâm, gloss:bir şeyi hal hal, tamamlanacağı sınıra kadar geliştirmek, source:"ر ب ب,B002"}. Yaratan Rab, pıhtıyı aşama aşama tamamlanmaya götürendir. Beşinci ayetin {ar:مَا لَمْ يَعْلَمْ, tr:mâ lem yaʿlem, gloss:bilmediğini, source:96:5} ifadesi bu doğuma bağlanır, çünkü doğan insan hiçbir şey bilmez: {ar:أَخْرَجَكُم مِّنۢ بُطُونِ أُمَّهَٰتِكُمْ لَا تَعْلَمُونَ شَيْـًٔا, tr:ahraceküm min butûni ummehâtikum lâ taʿlemûne şey'â, gloss:sizi annelerinizin karınlarından hiçbir şey bilmez halde çıkardı, source:16:78}. Sekizinci ayetin {ar:ٱلرُّجْعَىٰٓ, tr:er-ruc'â, gloss:dönüş, source:96:8} kelimesinin ailesinde ise sahnenin tersi vardır: {ar:إذا ألقت الناقة حملها قبل أن يستبين خلقه قيل قد رجعت, tr:izâ elkati'n-nâkatu hamlehâ kable en yestebîne halkuhû kîle kad racaʿat, gloss:dişi deve yükünü biçimi belli olmadan düşürünce "döndü" denir, source:"ر ج ع,B013"}. Bu kalıp ifade dönüşü ve biçimi tek cümlede birleştirir. Kurân yaratılış ile geri döndürmeyi bir sahnede birlikte anlatır. İnsan {ar:يَخْرُجُ مِنۢ بَيْنِ ٱلصُّلْبِ وَٱلتَّرَآئِبِ, tr:yahrucu min beyni's-sulbi ve't-terâ'ib, gloss:bel ile göğüs kemikleri arasından çıkan, source:86:7} bir sudan yaratılmıştır ve {ar:إِنَّهُۥ عَلَىٰ رَجْعِهِۦ لَقَادِرٌ, tr:innehû ʿalâ rac'ihî le kâdir, gloss:O onu geri döndürmeye elbette gücü yetendir, source:86:8}. Surenin sonundaki iki kelimenin ailesinde doğumun yaklaşması da vardır: onuncu ayetin fiili için {ar:أصلت الناقة … إذا وقع ولدها في صلاها وقرب نتاجها, tr:aslati'n-nâka … izâ vakaʿa veleduhâ fî salâhâ, gloss:dişi devenin yavrusu sağrısına indi ve doğumu yaklaştı, source:"ص ل و,B005"}, son ayetin emri için {ar:أقربت المرأة إذا قرب ولادها, tr:akrabeti'l-mer'e, gloss:kadının doğumu yaklaştı, source:"ق ر ب,B012"}. Bu iki aile anlamı uzak birer yankıdır, ama kuruluşları ortadadır.

Bu sahne, insanın düz bir anlatımla verilemeyecek bir yanını gösterir: okunması emredilen kişi, kendisi de toplanmış, tutunmuş ve biçimlendirilmiş bir varlıktır. Surenin dönüş ayeti, rahimden çıkan hayatı tekrar başladığı yere bağlar.

Kaynaklar: 96:1 ٱقْرَأْ ق ر ء B004; 96:1 ٱقْرَأْ ق ر ء B003; 96:2 عَلَقٍ ع ل ق B003; 96:2 عَلَقٍ ع ل ق B009; 96:1 خَلَقَ خ ل ق B003; 96:1 رَبِّكَ ر ب ب B002; 96:5 يَعْلَمْ ع ل م B001; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B013; 96:10 صَلَّىٰٓ ص ل و B005; 96:19 وَٱقْتَرِب ق ر ب B012

## Ad, iz, işaret

Bir şey, üzerine yükseltilen ya da içine bastırılan bir işaretle tanınır. Sure {ar:بِٱسْمِ, tr:bismi, gloss:adıyla, source:96:1} diye başlar. Ad kelimesinin kökü yüksekliktir: {ar:أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى, tr:aslu ismin sumuvvun ve huve mine'l-ʿuluvv, gloss:ismin aslı yükselmedir; çünkü anlamı ortaya çıkarır ve ona işaret eder, source:"س م و,B005"}. Kayıtlı bir başka türetmeye göre ise ad bir damgadır: {ar:ووسمت الشيء وسما: أثرت فيه بسمة, tr:ve vesemtu'ş-şey'e vesmen, gloss:bir şeye damga vurarak iz bıraktım, source:"و س م,B001"}. İlk anlamda ad, yükseğe kaldırılan bir işarettir; ikinci anlamda bir şeye bastırılan izdir. Kurân Rab'bin adını yükseklikle ve yaratmayla birlikte anar: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-aʿlâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1}, {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî halaka fe sevvâ, gloss:ki yarattı ve düzenledi, source:87:2}. Bu yapı surenin ilk ayetine çok yakındır. Adı anmak secdeye de bağlanır: {ar:وَٱذْكُرِ ٱسْمَ رَبِّكَ بُكْرَةً وَأَصِيلًا, tr:vezkuri'sme rabbike bukraten ve asîlâ, gloss:sabah akşam Rabbinin adını an, source:76:25}, {ar:وَمِنَ ٱلَّيْلِ فَٱسْجُدْ لَهُۥ, tr:ve mine'l-leyli fescud leh, gloss:gecenin bir kısmında O'na secde et, source:76:26}.

Öğretme kökü de işarettir: {ar:أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره, tr:aslun sahîhun vâhidun yedullu ʿalâ eserin bi'ş-şey', gloss:bir şeyi diğerlerinden ayıran bir ize delalet eden tek bir asıl, source:"ع ل م,B002"}. Bu kök sancağı ve kumaşın kenar nakışını da adlandırır: {ar:العلم الراية, tr:el-ʿalemu'r-râye, gloss:alem sancaktır, source:"ع ل م,B002"}. Görme kökü de bu sancağa varır: {ar:الراية العلامة المنصوبة للرؤية, tr:er-râyetu'l-ʿalâmetu'l-mensûbetu li'r-ru'ye, gloss:sancak, görülmek için dikilmiş işarettir, source:"ر ء ي,B011"}. On ikinci ayetteki {ar:أَمَرَ, tr:emera, gloss:emretti, source:96:12} fiilinin ailesinde yol işareti vardır: {ar:الأمارة العلامة، والأمار أمار الطريق معالمه, tr:el-emâretu'l-ʿalâme, gloss:emâre işarettir; emâr, yolun belirtileridir, source:"ء م ر,B005"}. Sekizinci ayetin dönüş kelimesinin ailesinde, yazının çizgilerinin tekrar tekrar mürekkeplenmesi bulunur: {ar:أن يعاد عليه السواد مرة بعد أخرى, tr:en yuʿâde ʿaleyhi's-sevâdu merraten baʿde uhrâ, gloss:üzerine siyahın tekrar tekrar geçirilmesi, source:"ر ج ع,B009"}.

Sure bu işaretleri yüze taşır. On beşinci ayetin {ar:لَنَسْفَعًۢا, tr:le nesfaʿan, gloss:mutlaka yakalarız, source:96:15} fiilinin ailesinde koyu bir leke vardır: {ar:السفعة بالضم سواد مشرب حمرة, tr:es-sufʿa sevâdun uşribe humra, gloss:sufʿa, kırmızıya çalan siyahlıktır, source:"س ف ع,B002"}. Son ayetin secdesinin ailesinde ise alındaki iz vardır: {ar:المسجد بالفتح جبهة الرجل حيث يصيبه ندب السجود, tr:el-mesced cebhetu'r-racul, gloss:mesced, adamın secde izinin düştüğü alnıdır, source:"س ج د,B003"}. Kurân iki tarafın da yüzüne iz koyar. Müminler için {ar:سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ, tr:sîmâhum fî vucûhihim min eseri's-sucûd, gloss:secde izinden belirtileri yüzlerindedir, source:48:29} denir. Çok yemin eden iftiracı için {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16} denir. Suçlular da yüzlerindeki işaretle tanınır: {ar:يُعْرَفُ ٱلْمُجْرِمُونَ بِسِيمَٰهُمْ فَيُؤْخَذُ بِٱلنَّوَٰصِى وَٱلْأَقْدَامِ, tr:yuʿrafu'l-mucrimûne bi sîmâhum fe yu'hazu bi'n-nevâsî ve'l-akdâm, gloss:suçlular belirtilerinden tanınır, perçemlerinden ve ayaklarından yakalanırlar, source:55:41}. Yazılı kayıt da işaretlenmiştir: {ar:كِتَٰبٌ مَّرْقُومٌ, tr:kitâbun merkûm, gloss:işaretlenmiş bir kitap, source:83:20}, {ar:يَشْهَدُهُ ٱلْمُقَرَّبُونَ, tr:yeşheduhu'l-mukarrabûn, gloss:ona yakınlaştırılanlar şahit olur, source:83:21}.

Böylece sure Rab'bin adıyla başlar, işaret koyan bir araçla öğretir ve iki işaretli alınla biter: biri yakalanıp karartılan alın, öteki secdenin iz bıraktığı alın.

Kaynaklar: 96:1 بِٱسْمِ س م و B005; 96:1 بِٱسْمِ و س م B001; 96:4 عَلَّمَ ع ل م B002; 96:7 رَّءَاهُ ر ء ي B011; 96:12 أَمَرَ ء م ر B005; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B009; 96:15 لَنَسْفَعًۢا س ف ع B002; 96:19 وَٱسْجُدْ س ج د B003

## Göz bebeğindeki insan, ayna ve bakış

Surede üç kez geçen {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan, source:96:2} kelimesinin ailesinde, göz bebeğinin karasında görülen küçük suret de vardır: {ar:إنسان العين المثال الذي يرى في السواد أي سواد العين, tr:insânu'l-ʿayn el-misâlu'llezî yurâ fi's-sevâd, gloss:gözün insanı, göz karasında görülen surettir, source:"ء ن س,B005"}. Aynı kök görerek fark etmeyi de anlatır: {ar:آنسته أبصرته, tr:ânestuhû: ebsartuhû, gloss:onu fark ettim, yani gördüm, source:"ء ن س,B002"}.

Yedinci ayette insan kendini görür: {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en ra'âhu'stagnâ, gloss:kendini yeterli gördüğü için, source:96:7}. Fiilin öznesi de nesnesi de aynı kişidir. Görme kökünün ailesinde ayna vardır: {ar:المرآة ما يرى فيه صورة الأشياء, tr:el-mir'âtu mâ yurâ fîhi sûretu'l-eşyâ', gloss:ayna, içinde şeylerin suretinin görüldüğü şeydir, source:"ر ء ي,B006"}; {ar:رأيت الرجل ترئية إذا أمسكت له المرآة لينظر فيها, tr:ra'eytu'r-racule terʾiyeten, gloss:adama bakması için ayna tuttum, source:"ر ء ي,B012"}. Bu ayette görmek aynı zamanda bir yargıdır: {ar:الرأي اعتقاد النفس, tr:er-ra'yu'ʿtikâdu'n-nefs, gloss:re'y, nefsin kanaatidir, source:"ر ء ي,B002"}. İnsan kendine bakar ve gördüğü suretten yeterli olduğu yargısını çıkarır.

Sure dinleyene üç kez seslenir: {ar:أَرَءَيْتَ, tr:e ra'eyte, gloss:gördün mü, source:96:9}. Bu kalıp hem "bana haber ver" anlamına gelir hem de uyarır: {ar:يجري أرأيت مجرى أخبرني وكل ذلك فيه معنى التنبيه, tr:yecrî e ra'eyte mecrâ ahbirnî, gloss:"gördün mü" "bana haber ver" yerine geçer ve hepsinde uyarı anlamı vardır, source:"ر ء ي,B013"}. On dördüncü ayet ise bu bakışların hepsini çevreleyen bakışı söyler: {ar:أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ, tr:e lem yaʿlem bi ennallâhe yerâ, gloss:Allah'ın gördüğünü bilmedi mi, source:96:14}. Burada bilmek bir şeyi gerçekte olduğu gibi kavramaktır: {ar:إدراك الشيء بحقيقته, tr:idrâku'ş-şey'i bi hakîkatih, gloss:bir şeyi hakikatiyle kavramak, source:"ع ل م,B001"}. Kurân aynı çerçeveyi bir başka yerde kurar: {ar:أَفَرَءَيْتَ ٱلَّذِى تَوَلَّىٰ, tr:e fe ra'eyte'llezî tevellâ, gloss:yüz çevireni gördün mü, source:53:33}, {ar:أَعِندَهُۥ عِلْمُ ٱلْغَيْبِ فَهُوَ يَرَىٰٓ, tr:e ʿindehû ʿilmu'l-gaybi fe huve yerâ, gloss:yanında gaybın bilgisi var da o mu görüyor, source:53:35}. Yüz çevirme, bilme ve görme burada da birlikte gelir. Malını harcamakla övünen insana da aynı soru sorulur: {ar:أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ, tr:e yahsebu en lem yerahû ehad, gloss:onu kimsenin görmediğini mi sanıyor, source:90:7}. Geri dönmeyeceğini sanan için de {ar:بَلَىٰٓ إِنَّ رَبَّهُۥ كَانَ بِهِۦ بَصِيرًا, tr:belâ inne rabbehû kâne bihî basîrâ, gloss:hayır, Rabbi onu hep görüyordu, source:84:15} denir. Namaz kılan kulun görülmesi ise Peygamber'e bir teselli olarak söylenir: {ar:ٱلَّذِى يَرَىٰكَ حِينَ تَقُومُ, tr:ellezî yerâke hîne tekûm, gloss:kalktığında seni gören, source:26:218}, {ar:وَتَقَلُّبَكَ فِى ٱلسَّٰجِدِينَ, tr:ve tekallubeke fi's-sâcidîn, gloss:secde edenler arasında dönüp durmanı da, source:26:219}.

Görme kökü bunun tersini de içerir. Görülmek için yapılan iş: {ar:يرآءون الناس إذا أبصرهم الناس صلوا, tr:yurâ'ûne'n-nâs, gloss:insanlara gösteriş yaparlar; insanlar onları görünce namaz kılarlar, source:"ر ء ي,B005"}. Kurân bunu namaz kılanlar için söyler: {ar:فَوَيْلٌ لِّلْمُصَلِّينَ, tr:fe veylun li'l-musallîn, gloss:yazık o namaz kılanlara, source:107:4}, {ar:ٱلَّذِينَ هُمْ يُرَآءُونَ, tr:ellezîne hum yurâ'ûn, gloss:ki onlar gösteriş yaparlar, source:107:6}. Surenin kulu ise Allah'ın görmesi altında namaz kılar. Son ayetteki secdenin kökü de bir bakış biçimini adlandırır: {ar:أصل السجود إدامة النظر في إطراق إلى الأرض, tr:aslu's-sucûd idâmetu'n-nazar fî itrâk, gloss:secdenin aslı, gözü yere indirerek uzun uzun bakmaktır, source:"س ج د,B005"}. Secdeden kaçınanların gözü ise bunun tersidir: {ar:وَيُدْعَوْنَ إِلَى ٱلسُّجُودِ فَلَا يَسْتَطِيعُونَ, tr:ve yudʿavne ile's-sucûdi fe lâ yestatîʿûn, gloss:secdeye çağrılırlar ama güç yetiremezler, source:68:42}, {ar:خَٰشِعَةً أَبْصَٰرُهُمْ, tr:hâşiʿaten ebsâruhum, gloss:gözleri yere eğik halde, source:68:43}.

Bakış bu sırayla ilerler: önce kendini aynada yeterli görmek, sonra dinleyenin bakmaya çağrılması, sonra Allah'ın görmesi ve en sonunda yere indirilen göz. Bir düz anlatım bunu yalnızca bir uyarı olarak verir; bu sahne bakışın yön değiştirmesini gösterir.

Kaynaklar: 96:2 ٱلْإِنسَٰنَ ء ن س B005; 96:2 ٱلْإِنسَٰنَ ء ن س B002; 96:7 رَّءَاهُ ر ء ي B006; 96:7 رَّءَاهُ ر ء ي B012; 96:7 رَّءَاهُ ر ء ي B002; 96:9 أَرَءَيْتَ ر ء ي B013; 96:14 يَرَىٰ ر ء ي B001; 96:14 يَعْلَم ع ل م B001; 96:7 رَّءَاهُ ر ء ي B005; 96:19 وَٱسْجُدْ س ج د B005

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

## İki çağrı, iki meclis

Çağırmak, birini sesle kendine doğru çekmektir: {ar:أصل واحد وهو أن تميل الشيء إليك بصوت وكلام يكون منك, tr:aslun vâhid, ve huve en tumîle'ş-şey'e ileyke bi savt, gloss:tek bir asıl: bir şeyi sesinle ve sözünle kendine yöneltmek, source:"د ع و,B001"}. On yedinci ayette adam {ar:فَلْيَدْعُ نَادِيَهُۥ, tr:felyedʿu nâdiyeh, gloss:meclisini çağırsın, source:96:17} diye meydan okunur. Meclis, çevresinde toplanılan yerdir: {ar:النادي المجلس يندو إليه من حواليه, tr:en-nâdî el-meclis, gloss:nâdî, çevredekilerin toplandığı meclistir, source:"ن د و,B001"}. Meclis kelimesi, içindeki insanlarla birlikte anlam kazanır: {ar:النادي… لا يسمى ناديا حتى يكون فيه أهله, tr:lâ yusemmâ nâdiyen hattâ yekûne fîhi ehluh, gloss:içinde halkı bulunmadıkça nâdî denmez, source:"ن د و,B001"}. Kök sesin yükselip uzağa ulaşmasını da kapsar: {ar:النداء رفع الصوت وظهوره, tr:en-nidâ' ref'u's-savt, gloss:nida sesi yükseltip duyurmaktır, source:"ن د و,B002"}. Kurân bu meclisi, ayetler okunduğunda inkârcıların övündüğü bir şey olarak gösterir: {ar:أَىُّ ٱلْفَرِيقَيْنِ خَيْرٌ مَّقَامًا وَأَحْسَنُ نَدِيًّا, tr:eyyu'l-ferîkayni hayrun makâmen ve ahsenu nediyyâ, gloss:iki topluluktan hangisinin yeri daha iyi, meclisi daha güzel, source:19:73}. Lut da kavmine meclislerinde yaptıklarını sorar: {ar:وَتَأْتُونَ فِى نَادِيكُمُ ٱلْمُنكَرَ, tr:ve te'tûne fî nâdîkumu'l-munker, gloss:meclisinizde de çirkinliği işliyorsunuz, source:29:29}. Firavun da toplayıp çağırır: {ar:فَحَشَرَ فَنَادَىٰ, tr:fe haşera fe nâdâ, gloss:topladı ve seslendi, source:79:23}.

On sekizinci ayet karşı çağrıdır: {ar:سَنَدْعُ ٱلزَّبَانِيَةَ, tr:senedʿu'z-zebâniye, gloss:biz de zebanileri çağıracağız, source:96:18}. Zebanilerin adı itmekten gelir: {ar:الزبن دفع الشيء عن الشيء, tr:ez-zebnu defʿu'ş-şey'i ʿani'ş-şey', gloss:zebn bir şeyi bir şeyden itmektir, source:"ز ب ن,B001"}; {ar:الزبانية سموا بذلك لأنهم يدفعون أهل النار إلى النار, tr:ez-zebâniye summû bi zâlike li ennehum yedfaʿûne ehle'n-nâr, gloss:zebanilere bu ad, ateş ehlini ateşe ittikleri için verilmiştir, source:"ز ب ن,B002"}. Kök uzaklığı da adlandırır: {ar:الزبن البعد, tr:ez-zebnu'l-buʿd, gloss:zebn uzaklıktır, source:"ز ب ن,B005"}. Kurân ateşin bekçilerini şöyle anlatır: {ar:عَلَيْهَا مَلَٰٓئِكَةٌ غِلَاظٌ شِدَادٌ لَّا يَعْصُونَ ٱللَّهَ مَآ أَمَرَهُمْ, tr:ʿaleyhâ melâ'iketun gilâzun şidâd, lâ yaʿsûna'llâhe mâ emerahum, gloss:başında Allah'ın emrine karşı gelmeyen sert, güçlü melekler vardır, source:66:6}, {ar:عَلَيْهَا تِسْعَةَ عَشَرَ, tr:ʿaleyhâ tisʿate ʿaşer, gloss:başında on dokuz vardır, source:74:30}. İtmenin kendisi de anlatılır: {ar:يَوْمَ يُدَعُّونَ إِلَىٰ نَارِ جَهَنَّمَ دَعًّا, tr:yevme yudaʿʿûne ilâ nâri cehenneme daʿʿâ, gloss:cehennem ateşine itilip kakıldıkları gün, source:52:13}.

Üçüncü bir çağrı da vardır. Onuncu ayetin namazı bir çağrıdır: {ar:الصلاة وهي الدعاء, tr:es-salâtu ve hiye'd-duʿâ', gloss:salât duadır, source:"ص ل و,B002"}. Kurân Allah'ın kulunun dua ederken kuşatılmasını cinlerin ağzından anlatır: {ar:لَمَّا قَامَ عَبْدُ ٱللَّهِ يَدْعُوهُ كَادُوا۟ يَكُونُونَ عَلَيْهِ لِبَدًا, tr:lemmâ kâme ʿabdu'llâhi yedʿûhu kâdû yekûnûne ʿaleyhi libedâ, gloss:Allah'ın kulu O'na dua etmeye kalkınca neredeyse üstüne yığılacaklardı, source:72:19}. Son ayetin yaklaşma emri bu çağrıya karşılık verir. Kökte hükümdarın yakın çevresi vardır: {ar:القربان واحد قرابين الملك وهم جلساؤه وخاصته, tr:el-kurbânu vâhidu karâbîni'l-melik, gloss:kurbân, hükümdarın meclis arkadaşları ve has adamlarından biridir, source:"ق ر ب,B004"}. Yakınlık aynı zamanda çağrıya karşılık verilmesidir: {ar:في الرعاية نحو فإني قريب أجيب دعوة الداع, tr:fi'r-riʿâye nahve fe innî karîbun ucîbu daʿvete'd-dâʿ, gloss:gözetme anlamında, "Ben yakınım, dua edenin duasına karşılık veririm" gibi, source:"ق ر ب,B006"}. Kurân'daki ifade şudur: {ar:فَإِنِّى قَرِيبٌ أُجِيبُ دَعْوَةَ ٱلدَّاعِ إِذَا دَعَانِ, tr:fe innî karîb, ucîbu daʿvete'd-dâʿi izâ daʿân, gloss:Ben yakınım; dua eden bana dua ettiğinde karşılık veririm, source:2:186}. Çağıranlar yakınlığı arar: {ar:يَبْتَغُونَ إِلَىٰ رَبِّهِمُ ٱلْوَسِيلَةَ أَيُّهُمْ أَقْرَبُ, tr:yebtegûne ilâ rabbihimu'l-vesîlete eyyuhum akrab, gloss:hangisi daha yakın olacak diye Rablerine yol ararlar, source:17:57}. Yakın meclis secde eder: {ar:إِنَّ ٱلَّذِينَ عِندَ رَبِّكَ لَا يَسْتَكْبِرُونَ عَنْ عِبَادَتِهِۦ, tr:inne'llezîne ʿinde rabbike lâ yestekbirûne ʿan ʿibâdetih, gloss:Rabbinin yanında olanlar O'na kulluk etmekten büyüklenmezler, source:7:206}, {ar:وَلَهُۥ يَسْجُدُونَ, tr:ve lehû yescudûn, gloss:ve O'na secde ederler, source:7:206}.

Böylece sahnede üç hareket vardır. Adam meclisini çevresine toplar. Allah, uzaklaştırıp iten bekçileri çağırır. Kul ise hükümdarın yakın meclisine çağrılır. Düz bir anlatım bunu tehdit ve emir olarak verir; bu sahne iki karşıt sarayı gösterir.

Kaynaklar: 96:17 فَلْيَدْعُ د ع و B001; 96:17 نَادِيَهُۥ ن د و B001; 96:17 نَادِيَهُۥ ن د و B002; 96:18 ٱلزَّبَانِيَةَ ز ب ن B001; 96:18 ٱلزَّبَانِيَةَ ز ب ن B002; 96:18 ٱلزَّبَانِيَةَ ز ب ن B005; 96:10 صَلَّىٰٓ ص ل و B002; 96:19 وَٱقْتَرِب ق ر ب B004; 96:19 وَٱقْتَرِب ق ر ب B006

## Yol: doğru yolda olmak, sapmak, dönmek, yaklaşmak

Bir yolcu yoldadır. Hedefi ıskalayabilir, yönünden sapabilir ya da sırtını dönüp kaçabilir. Sonunda herkes başladığı yere döner ve yolun bir varış noktası vardır. On birinci ayetin {ar:عَلَى ٱلْهُدَىٰٓ, tr:ʿale'l-hudâ, gloss:doğru yol üzerinde, source:96:11} ifadesi yolcuyu yolun üzerinde gösterir: {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytuhu't-tarîk, gloss:ona yolu ve evi gösterdim, yani tanıttım, source:"ه د ي,B001"}; {ar:الهداية دلالة بلطف, tr:el-hidâye delâletun bi lutf, gloss:hidayet, incelikle yol göstermektir, source:"ه د ي,B001"}. Kök sakin bir yürüyüşü de adlandırır: {ar:لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن, tr:lem yusriʿ isrâʿa'l-munhezim, gloss:bozguna uğrayan gibi koşmadı, sükûnet ve güzel bir yürüyüşle gitti, source:"ه د ي,B010"}. Kurân yolcuları karşılaştırır: {ar:أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ, tr:e fe men yemşî mukibben ʿalâ vechihî ehdâ em men yemşî seviyyen ʿalâ sırâtın mustakîm, gloss:yüzüstü kapanarak yürüyen mi daha doğru yoldadır, yoksa dosdoğru bir yolda dimdik yürüyen mi, source:67:22}. Bu ayette yüz, yolun karşısında bir yürüyüş biçimi olarak geçer; bu da perçem sahnesine yakındır.

On altıncı ayetin günahkâr kelimesi yönden sapmaktır: {ar:الخطأ العدول عن الجهة, tr:el-hata'u'l-ʿudûlu ʿani'l-cihe, gloss:hata yönden sapmaktır, source:"خ ط ء,B001"}. On üçüncü ayetin yüz çevirme fiili, bedenle ya da dinlememekle sırt dönmektir: {ar:التولي قد يكون بالجسم وقد يكون بترك الإصغاء والائتمار, tr:et-tevellî kad yekûnu bi'l-cism, gloss:yüz çevirmek bedenle de olur, dinlememek ve emre uymamakla da, source:"و ل ي,B007"}. Aynı kök kesintisiz yakınlığı da adlandırır: {ar:الولي القرب والدنو, tr:el-velyu'l-kurbu ve'd-dunuvv, gloss:vely yakınlık ve yaklaşmaktır, source:"و ل ي,B001"}. Böylece yüz çevirmek, yakınlığın tersine çevrilmiş halidir. Yalanlama fiilinin ailesinde saldırıda duraksamak da vardır: {ar:حمل فلان ثم كذب أي لم يصدق في الحملة, tr:hamele fulânun summe kezeb, gloss:falan saldırdı, sonra geri durdu, yani saldırısında sözünü tutmadı, source:"ك ذ ب,B004"}.

Sekizinci ayetin dönüşü başlangıca dönüştür: {ar:الرجوع العود إلى ما كان منه البدء, tr:er-rucûʿu'l-ʿavdu ilâ mâ kâne minhu'l-bed', gloss:dönüş, başlangıcın olduğu yere geri gelmektir, source:"ر ج ع,B001"}. Bu başlangıç, ilk iki ayetin yaratmasıdır. Kurân dönüşü yaratılışın başlangıcına bağlar: {ar:إِلَيْهِ مَرْجِعُكُمْ جَمِيعًا, tr:ileyhi merciʿukum cemîʿâ, gloss:hepinizin dönüşü O'nadır, source:10:4}, {ar:إِنَّهُۥ يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ, tr:innehû yebde'u'l-halka summe yuʿîduh, gloss:O yaratmayı başlatır, sonra onu geri getirir, source:10:4}; {ar:كَمَا بَدَأَكُمْ تَعُودُونَ, tr:kemâ bede'ekum teʿûdûn, gloss:sizi başlattığı gibi döneceksiniz, source:7:29}. İnsanın yolu da Rab'be doğru bir uğraş olarak tanımlanır: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًا فَمُلَٰقِيهِ, tr:yâ eyyuhe'l-insânu inneke kâdihun ilâ rabbike kedhan fe mulâkîh, gloss:ey insan, sen Rabbine doğru zahmetle çabalıyorsun ve O'na kavuşacaksın, source:84:6}. Dönmeyeceğini sanan kişi de anlatılır: {ar:إِنَّهُۥ ظَنَّ أَن لَّن يَحُورَ, tr:innehû zanne en len yahûr, gloss:o asla geri dönmeyeceğini sanmıştı, source:84:14}. Yedinci ayetin yeterlilik kökü bu sanıyı yere yerleşmekle de anlatır: {ar:غني القوم في دارهم أقاموا, tr:ganiye'l-kavmu fî dârihim, gloss:topluluk yurdunda yerleşip kaldı, source:"غ ن ي,B004"}. Dönüş kelimesinin ailesinde günahtan dönmek de vardır: {ar:يرجعون عن الذنب, tr:yarciʿûne ʿani'z-zenb, gloss:günahtan dönerler, source:"ر ج ع,B003"}. Bu, on beşinci ayetteki "vazgeçmezse" şartının açık bıraktığı yoldur.

Yolun bir son noktası vardır: {ar:النهاية الغاية حيث ينتهي إليه الشيء, tr:en-nihâyetu'l-gâye, gloss:nihâye, bir şeyin vardığı son noktadır, source:"ن ه ي,B002"}. Son ayetin emri ise yaklaşmaktır: {ar:القرب نقيض البعد والتقرب التدني إلى شيء والاقتراب الدنو, tr:el-kurbu nakîdu'l-buʿd, gloss:yakınlık uzaklığın zıddıdır; yaklaşmak bir şeye doğru alçalıp gelmektir, source:"ق ر ب,B001"}. On ikinci ayetin sakınma kökü yolda dikkatle yürüyen atı da adlandırır: {ar:فرس واق إذا كان يهاب المشي من وجع يجده في حافره, tr:ferasun vâk, gloss:toynağındaki ağrıdan ötürü yürümekten çekinen at, source:"و ق ي,B003"}. Sure böylece yolda olmayı, sapmayı, sırt dönmeyi ve sonunda yaklaşmayı tek bir yol üzerinde sıralar.

Kaynaklar: 96:11 ٱلْهُدَىٰٓ ه د ي B001; 96:11 ٱلْهُدَىٰٓ ه د ي B010; 96:16 خَاطِئَةٍ خ ط ء B001; 96:13 وَتَوَلَّىٰٓ و ل ي B007; 96:13 وَتَوَلَّىٰٓ و ل ي B001; 96:13 كَذَّبَ ك ذ ب B004; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B001; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B003; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B004; 96:15 يَنتَهِ ن ه ي B002; 96:19 وَٱقْتَرِب ق ر ب B001; 96:12 بِٱلتَّقْوَىٰٓ و ق ي B003

## Efendi, kul ve itaat

Bu sahnede bir sahip ve sahip olunan vardır. Rab kelimesi sahibi ve itaat edilen efendiyi adlandırır: {ar:يكون الرب: المالك؛ ويكون الرب: السيد المطاع, tr:yekûnu'r-rabb el-mâlik, ve yekûnu'r-rabb es-seyyidu'l-mutâʿ, gloss:rab sahip demektir; rab, itaat edilen efendi demektir de, source:"ر ب ب,B001"}. Bu tanım rabbi son ayetteki itaat fiiline bağlar. Onuncu ayetin kulu hem sahip olunandır hem de kulluğunu gösterendir: {ar:العبودية إظهار التذلل والعبادة غاية التذلل, tr:el-ʿubûdiyyetu izhâru't-tezellul, gloss:kulluk, alçakgönüllülüğü göstermektir; ibadet ise alçakgönüllülüğün en ileri derecesidir, source:"ع ب د,B003"}. Kulluk itaatle de birleşir: {ar:إياك نعبد إياك نطيع الطاعة التي نخضع معها, tr:iyyâke naʿbudu: iyyâke nutîʿ, gloss:"yalnız sana kulluk ederiz": yalnız sana, boyun eğerek itaat ederiz, source:"ع ب د,B003"}. Kökte çok yürünmüş, düzleşmiş yol da vardır: {ar:الطريق المعبد وهو المسلوك المذلل, tr:et-tarîku'l-muʿabbed, gloss:muabbed yol, çok yürünüp düzlenmiş yoldur, source:"ع ب د,B005"}.

Dokuzuncu ayetin {ar:يَنْهَىٰ, tr:yenhâ, gloss:men eder, source:96:9} fiili emrin zıddıdır: {ar:النهي خلاف الأمر, tr:en-nehyu hilâfu'l-emr, gloss:nehiy emrin zıddıdır, source:"ن ه ي,B001"}. On ikinci ayetin {ar:أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ, tr:ev emera bi't-takvâ, gloss:ya da sakınmayı emrettiyse, source:96:12} ifadesi, aynı kişinin aslında emredebilecek olduğunu söyler: {ar:الأمر الذي هو نقيض النهي, tr:el-emru'llezî huve nakîdu'n-nehy, gloss:nehyin zıddı olan emir, source:"ء م ر,B002"}. Aynı kök aklı da adlandırır: {ar:النهية العقل لأنه ينهى عن قبيح الفعل, tr:en-nuhye el-ʿakl, gloss:nuhye akıldır, çünkü çirkin işten alıkoyar, source:"ن ه ي,B003"}. Namazı yasaklayan adam, kendi aklının görevini tersine çevirir. Kurân namazın kendisinin yasakladığını söyler: {ar:إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ, tr:inne's-salâte tenhâ ʿani'l-fahşâ'i ve'l-munker, gloss:namaz hayâsızlıktan ve kötülükten alıkoyar, source:29:45}. Doğru yasaklama da nefsin kendisine yöneltilir: {ar:وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ, tr:ve nehe'n-nefse ʿani'l-hevâ, gloss:nefsini keyfî istekten alıkoyan, source:79:40}. Allah'ın mescitlerinde adının anılmasını engelleyen de anılır: {ar:وَمَنْ أَظْلَمُ مِمَّن مَّنَعَ مَسَٰجِدَ ٱللَّهِ أَن يُذْكَرَ فِيهَا ٱسْمُهُۥ, tr:ve men azlemu mimmen menaʿa mesâcida'llâhi en yuzkera fîhe'smuh, gloss:Allah'ın mescitlerinde adının anılmasını engelleyenden daha zalim kim olabilir, source:2:114}. Bu ayet, adla başlayan ve secdeyle biten surenin yasaklayanına yakındır.

Altıncı ayetin azma fiili itaatte sınırı aşmaktır; kök sahte mabudu da adlandırır: {ar:الطاغوت… كل معبود من دون الله, tr:et-tâgût … kullu maʿbûdin min dûni'llâh, gloss:tâgût, Allah'tan başka tapılan her şeydir, source:"ط غ ي,B003"}. Kurân bunun en açık örneği olarak Firavun'u gösterir: {ar:ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ, tr:izheb ilâ firʿavne innehû tagâ, gloss:Firavun'a git, çünkü o azdı, source:79:17}. Firavun sonunda kendini rab ilan eder. On dördüncü ayetteki Allah adının kökü ise tapılanı adlandırır: {ar:إله اسما لكل معبود… فالإله على هذا هو المعبود, tr:ilâh … el-maʿbûd, gloss:ilah, tapılan her şeyin adıdır; buna göre ilah tapılandır, source:"ء ل ه,B001"}.

Son ayetin {ar:لَا تُطِعْهُ, tr:lâ tutiʿhu, gloss:ona boyun eğme, source:96:19} emri, isteyerek boyun eğmeyi yasaklar: {ar:الطوع نقيض الكره, tr:et-tavʿu nakîdu'l-kerh, gloss:tav, zorlamanın zıddıdır, source:"ط و ع,B001"}. Kurân aynı yasağı Peygamber'e başka yerlerde de verir: {ar:فَلَا تُطِعِ ٱلْمُكَذِّبِينَ, tr:fe lâ tutiʿi'l-mukezzibîn, gloss:yalanlayanlara boyun eğme, source:68:8}; {ar:وَلَا تُطِعْ كُلَّ حَلَّافٍ مَّهِينٍ, tr:ve lâ tutiʿ kulle hallâfin mehîn, gloss:çok yemin eden aşağılık kimseye boyun eğme, source:68:10}. Bir başka yerde bu yasak, adı anmak ve secde etmekle aynı yerde geçer: {ar:وَلَا تُطِعْ مِنْهُمْ ءَاثِمًا أَوْ كَفُورًا, tr:ve lâ tutiʿ minhum âsimen ev kefûrâ, gloss:onlardan hiçbir günahkâra ya da nanköre boyun eğme, source:76:24}. Bundan hemen sonra adı anmak ve gece secde etmek emredilir. Bu, surenin son ayetinin yapısıyla aynıdır. Sahne surenin sorusunu açıkça ortaya koyar: kul kime itaat edecek? Sahibi Rab olan kul, kendini rab yerine koyan adama boyun eğmez.

Kaynaklar: 96:1 رَبِّكَ ر ب ب B001; 96:10 عَبْدًا ع ب د B003; 96:10 عَبْدًا ع ب د B005; 96:9 يَنْهَىٰ ن ه ي B001; 96:12 أَمَرَ ء م ر B002; 96:9 يَنْهَىٰ ن ه ي B003; 96:6 لَيَطْغَىٰٓ ط غ ي B003; 96:14 ٱللَّهَ ء ل ه B001; 96:19 تُطِعْهُ ط و ع B001

## Buluşmalar

İmgeler en açık şekilde baş sahnesinde buluşur. On beşinci ayetin fiili hem perçemden tutmak hem de yüzü karartmaktır. Böylece başın önü, avın yakalandığı yer, huysuz hayvanın tutulduğu yer ve ateşin yaladığı deri aynı noktada birleşir. Aynı alın son ayette yere konur ve secde izini taşır. İşaret imgesi buraya da uzanır: bir alın kararmış bir lekeyle işaretlenir, öteki secdenin iziyle. Kurân her iki tarafı da yüzlerindeki işaretle tanıtır: biri {ar:مِّنْ أَثَرِ ٱلسُّجُودِ, tr:min eseri's-sucûd, gloss:secdenin izinden, source:48:29}, öteki {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. Sure ad ile başlar ve iki işaretli alınla biter.

Göz ile yeterlilik imgeleri yedinci ayette buluşur. Kendini aynada gören adam ile süse ihtiyaç duymayan güzel kadın aynı kelime çiftinde birleşir: kendini görmek ve yeterli saymak. Su imgesi de buna bağlanır. Azan insan ölçüsünü aşan bir taşkın gibidir; on beşinci ayette durması istenir. Kökün göletteki duruluşu adlandırdığı hatırlanırsa, sekizinci ayet bu suyun nereye varacağını söyler. Kurân'ın varış ayeti bu iki imgeyi aynı yapıda birleştirir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Yol imgesi de bu dönüşe katılır, çünkü dönüş başlangıca dönmektir ve bu başlangıç rahimdeki ilk tutunuştur.

Rahim ile okuma, surenin ilk kelimesinde buluşur. Okumanın kökü hem rahmin bir şeyi toplayıp tutmasını hem de harflerin toplanmasını adlandırır. Pıhtıyı tutan kökle sözü toplayan kök aynıdır. İnsanın yaratılışı ve öğretilmesi bu yüzden aynı işin iki yüzü olarak duyulur. Kurân'daki benzer sıra da bunu destekler: Kurân'ı öğretmek, insanı yaratmak ve ona açıklamayı öğretmek. Okuma ile secde de buluşur: okuyucu aynı zamanda kulluk edendir ve sure, ilk emri okumak, son emri secde etmek olan bir eğri çizer. Kurân bu ikisini, okunduğunda secde edenler ile etmeyenler üzerinden birleştirir.

Ateş ile çağrı imgeleri onuncu, on yedinci ve on sekizinci ayetlerde buluşur. Namaz hem çağrıdır hem de kökü ateşe girmeyi adlandırır. Adam meclisini çağırır, Allah ateşe iten bekçileri çağırır ve kul yakın meclise çağrılır. Ateşin kendisinin de çağırdığı söylenir: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Bu yüz çevirme on üçüncü ayetin fiilidir.

İtaat ile hayvan imgeleri son ayette buluşur. Rab, itaat edilen efendidir; dizgine uyan at da itaatin bir figürüdür. Kul bu yüzden kendini rab ilan eden birine boyun eğmez, yakında tutulan ve değer gören at gibi yaklaşır. Yaratma ile uydurma da on altıncı ayette buluşur. Gerçek ölçüyle yaratan Rab'bin karşısında, yalanı içinde ölçen yalancı perçem durur.

Bu buluşmalar surenin hareketini taşır. Sure, rahimde toplanan ve tutunan bir varlıkla başlar; bu varlık sözü toplamayı ve kalemle yazmayı öğrenir. Sonra kendini aynada yeterli görür, taşkın su gibi ölçüsünü aşar, başını kaldırır ve namaz kılan kulu engellemeye çalışır. Dönüş ayeti ve Allah'ın görmesi bu yükselişin önüne bir sınır koyar. Yasaklayan perçeminden yakalanır, meclisi yerine bekçiler gelir. Kul ise yüz çevirmeden, başını yere koyarak, çağrılmış olduğu yakınlığa yürür.

