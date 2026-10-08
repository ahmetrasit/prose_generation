Focus: 112:2. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/112_2/D.r13/context.md =====
# 112:2 — focus

ٱللَّهُ ٱلصَّمَدُ

Anchor translation (canonical reading, reference only):

Allah, herkesin dayanağıdır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ٱللَّهُ | ٱللَّه | ء ل ه | PN |
| 2 | ٱلصَّمَدُ | صَّمَد | ص م د | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 112 — full text (context; no pericope)

- 112:1 قُلْ هُوَ ٱللَّهُ أَحَدٌ
- 112:2 ◀ focus ٱللَّهُ ٱلصَّمَدُ
- 112:3 لَمْ يَلِدْ وَلَمْ يُولَدْ
- 112:4 وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ


===== _commentary/v16/work/112_2/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ء ل ه (root_000047) — identity root of ٱللَّهُ (w1)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## ص م د (root_000882) — identity root of ٱلصَّمَدُ (w2)

- **B001** dayanak alarak bir hedefe yönelme — amaç edinme ve dayanarak yönelme · onu amaçlayıp ona dayanarak yöneldi · işlerde kendisine başvurulan en üstün kişi · işlerde kendisine yönelinen kişi veya amaçlanan şey · amaçlanıp gidilen ev · kulların dua ve istekle yöneldiği yüce varlığın adı
  الصمد القصد وصمدته صمدا (maqayis); وصمدت قصدت وصمدت صمد كذا أي قصدت قصده واعتمدته (ayn); صمده يصمده صمدا أي قصده والصمد السيد لأنه يصمد إليه في الحوائج وبيت مصمد أي مقصود (sihah); الصمد السيد الذي قد انتهى سؤدده والذي يصمد إليه الأمر وصمدت صمد هذا الأمر أي قصدت قصده واعتمدته (tahdhib); الصمد السيد الذي يصمد إليه في الأمر وصمده قصد معتمدا عليه قصده (mufradat)
- **B002** içi boş olmayan katı bütünlük — sert veya yüksek ve kalın yer · içi boş ve yüzeyi yarık olmayan katı şey · içi boş olmayan · yere sağlam oturmuş düz kaya · dağın kalın bölümünden alçalıp düzleşen ağaçlı arazi
  الصلابة في الشيء والصمد كل مكان صلب (maqayis); المصمت الذي ليس بأجوف والصمدة صخرة راسية (ayn); الصمد المكان المرتفع الغليظ والمصمد لغة في المصمت وهو الذي لا جوف له (sihah); المصمت الذي لا جوف له والمكان المرتفع الغليظ والمصمد الصلب الذي ليس فيه خدد والشديد من الأرض (tahdhib); الصمد الذي ليس بأجوف (mufradat)
- **B003** şişe ağzı tıkacı — şişe ağzı tıkacı · şişeye tıkaç takıp ağzını kapatmak
  الصماد عفاص القارورة وصمدتها صمدا (ayn); الصماد عفاص القارورة (sihah); الصماد سداد القارورة والصماد عفاص القارورة وقد صمدتها أصمدها (tahdhib)
- **B004** başı sarık dışındaki bezle sarma — başını sarık dışındaki bir bezle sardı · sarık olmayan bez baş sargısı
  صمد رأسه تصميدا وذلك إذا لف رأسه بخرقة أو منديل أو ثوب ما خلا العمامة وهي الصماد (tahdhib)
- **B005** bir işin başında durup ona özen gösterme — bir işin başında durup ona özen gösteren
  إني على صمادة من أمر إذا أشرف عليه وحفلت به (tahdhib)
- **B006** değnekle vurma [kalıp] — ona değnekle vurdu
  صمده بالعصا صمدا إذا ضربه بها (tahdhib)
- **B007** kalıcı ve sürekli olma — sürekli ve yok oluştan sonra da kalan · soğuk ve kıtlıkta dayanıp sütü kesilmeyen dişi deve
  الصمد الدائم والدائم الباقي بعد فناء خلقه وناقة مصماد وهي الباقية على القر والجدب الدائمة الرسل (tahdhib)

## و ل ه (root_005296) — documented alternative for ٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

===== _commentary/v16/out/s112/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 112:2, and ## Buluşmalar) =====
## Nesil zinciri: denk eş, doğum, yaşıt ve mirasçı

Üçüncü ve dördüncü ayetin kelimeleri bir arada okununca, insan soyunun nasıl sürdüğünü gösteren eksiksiz bir sahne çıkar ortaya. Sahne bir denklikle başlar. Küf', evlilikte ve soyda dengi olan kişidir: {ar:فلان كفء لفلان في المناكحة أو في المحاربة, tr:fülânün küf'ün li-fülânin fi'l-münâkehati ev fi'l-muhârebe, gloss:falan, falanın evlilikte ya da savaşta dengidir, source:"ك ف ء,B001"}, {ar:هذا كفء له أي مثله في الحسب والمال والحرب, tr:hâzâ küf'ün lehû ey misluhû fi'l-hasebi ve'l-mâli ve'l-harb, gloss:bu onun dengidir, yani soyda, malda ve savaşta onun benzeridir, source:"ك ف ء,B001"}. Birbirine denk iki kişi evlenince anne ve baba olurlar; ikil kalıptaki vâlidân {source:"و ل د,B002"}. Sonra kadın doğurur ve doğumun bir vakti vardır: {ar:ولدت المرأة تلد ولادا وولادة؛ أولدت حان ولادها, tr:veledeti'l-mer'etü telidü vilâden ve vilâdeten; evledet hâne vilâdühâ, gloss:kadın doğurdu; doğum vakti geldi, source:"و ل د,B003"}. Doğan çocuk veleddir ve bu kelime erkeği de kızı da, biri de çoğu da kapsar: {ar:الولد اسم يجمع الواحد والكثير والذكر والأنثى, tr:el-veled ismün yecmeu'l-vâhide ve'l-kesîra ve'z-zekera ve'l-ünsâ, gloss:veled teki ve çoğu, erkeği ve dişiyi toplayan bir addır, source:"و ل د,B001"}. Kökün temel anlamı da soyun devam etmesidir: {ar:أصل صحيح وهو دليل النجل والنسل, tr:aslün sahîh ve hüve delîlü'n-necli ve'n-nesl, gloss:sağlam bir köktür; evladı ve nesli gösterir, source:"و ل د,B001"}. Yeni doğan, hayatı doğduğu andan itibaren ölçülen kişidir: {ar:الوليد الصبي حين يولد, tr:el-velîd es-sabiyyü hîne yûled, gloss:velîd, doğduğu andaki çocuktur, source:"و ل د,B004"}. Her doğanın bir de yaşıtlar kuşağı vardır {source:"و ل د,B006"}.

Sahnenin ikinci yarısı zamandır. Dördüncü ayetteki {ar:يَكُن, tr:yekün, gloss:oldu, source:112:4} fiilinin kökü geçmiş zamanı anlatır: {ar:كان عبارة عما مضى من الزمان, tr:kâne ibâretün ammâ medâ mine'z-zamân, gloss:kâne, geçmiş zamanı anlatır, source:"ك و ن,B001"}. Aynı aile yaşlı adamı da bu fiille adlandırır: {ar:يقال للرجل إذا شاخ كُنْتِيّ؛ كأنه نسب إلى قوله كُنْتُ في شبابي كذا وكذا, tr:yükâlü li'r-racüli izâ şâhe küntiyy; ke-ennehû nüsibe ilâ kavlihî küntü fî şebâbî kezâ ve kezâ, gloss:adam yaşlanınca ona küntî denir, sanki "gençliğimde şöyleydim" deyişine nispet edilmiştir, source:"ك و ن,B005"}. Yaşlı adam, sözünü "ben … idim" diye kuran adamdır. Doğan yaşlanır, yaşlanan ölür, onun yerini de doğurduğu alır. Nesil, ölümlü bir türün kendini sürdürme biçimidir. Bu sahneye karşı ikinci ayetteki {ar:ٱلصَّمَدُ, tr:es-samed, gloss:Samed, source:112:2} kelimesinin bir anlamı durur: {ar:الصمد الدائم والدائم الباقي بعد فناء خلقه, tr:es-samed ed-dâim ve'd-dâim el-bâkî ba'de fenâi halkıh, gloss:Samed, daim olandır; daim olan da yarattıkları yok olduktan sonra kalandır, source:"ص م د,B007"}. Aynı tarifin somut imgesi soğukta ve kıtlıkta sütü kesilmeyen dişi devedir: {ar:ناقة مصماد وهي الباقية على القر والجدب الدائمة الرسل, tr:nâkatün mismâd ve hiye'l-bâkıyetü ale'l-karri ve'l-cedbi'd-dâimetü'r-risl, gloss:mismâd deve, soğuğa ve kıtlığa dayanan, sütü sürekli akan devedir, source:"ص م د,B007"}. Böylece üçüncü ayet Allah'ı nesil zincirinin dışına çıkarır: O'nu başlatan bir doğum yoktur, O'ndan sonra kalacak bir mirasçı da yoktur. Dördüncü ayet de zincirin başlangıç noktasını, yani denk eşi kaldırır.

Kur'an bu bağlantıyı açıkça kurar. Allah, cinleri O'na ortak koşan ve {ar:وَخَرَقُوا۟ لَهُۥ بَنِينَ وَبَنَٰتٍۭ بِغَيْرِ عِلْمٍۢ, tr:ve harakû lehû benîne ve benâtin bi-ğayri ilm, gloss:bilgisizce O'na oğullar ve kızlar uydurdular, source:6:100} diye anlatılan kimselere cevap verir: {ar:أَنَّىٰ يَكُونُ لَهُۥ وَلَدٌۭ وَلَمْ تَكُن لَّهُۥ صَٰحِبَةٌۭ, tr:ennâ yekûnü lehû veledün ve lem tekün lehû sâhibeh, gloss:O'nun eşi olmamışken nasıl çocuğu olur, source:6:101}. Buradaki "lem tekün lehû sâhibe", surenin dördüncü ayetindeki "lem yekün lehû küfüven" ile aynı kalıptadır: eş olmayınca çocuk da olmaz. Kur'an'ı dinleyen cinler de eşi ve çocuğu birlikte reddeder: {ar:مَا ٱتَّخَذَ صَٰحِبَةًۭ وَلَا وَلَدًۭا, tr:mettehaze sâhibeten ve lâ veledâ, gloss:ne eş edindi ne çocuk, source:72:3}. Saffât suresinde Allah, Peygambere Mekkelilere kızları O'na, oğulları kendilerine nasıl ayırdıklarını sormasını emreder {source:37:149}, ve iddia bir soy iddiası olarak adlandırılır: {ar:وَجَعَلُوا۟ بَيْنَهُۥ وَبَيْنَ ٱلْجِنَّةِ نَسَبًۭا, tr:ve cealû beynehû ve beyne'l-cinneti nesebâ, gloss:O'nunla cinler arasında bir soy bağı kurdular, source:37:158}. İnsan sahnesi ise bir yeminde topluca anılır: {ar:وَوَالِدٍۢ وَمَا وَلَدَ, tr:ve vâlidin ve mâ veled, gloss:doğurana ve doğurduğuna andolsun, source:90:3}. Surenin iki fiilinin iki yönü, yani doğuran ve doğurulan, insanlara yapılan bir uyarıda yan yana durur: {ar:لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ وَلَا مَوْلُودٌ هُوَ جَازٍ عَن وَالِدِهِۦ شَيْـًٔا, tr:lâ yeczî vâlidün an veledihî ve lâ mevlûdün hüve câzin an vâlidihî şey'â, gloss:babanın çocuğuna, çocuğun da babasına hiçbir fayda sağlayamayacağı gün, source:31:33}. İnsanlar arasındaki en güçlü bağ olan bu çift, o gün hiçbir şeyi taşıyamaz.

Doğumun ardından ölümün geldiğini Kur'an, sonradan "oğul" diye anılacak olanın ağzından da söyletir. Allah Yahya için {ar:يَوْمَ وُلِدَ وَيَوْمَ يَمُوتُ وَيَوْمَ يُبْعَثُ حَيًّۭا, tr:yevme vülide ve yevme yemûtü ve yevme yüb'asü hayyâ, gloss:doğduğu gün, öleceği gün ve diri olarak kaldırılacağı gün, source:19:15} der. Beşikteki İsa da kendisi için aynı sırayı söyler: {ar:يَوْمَ وُلِدتُّ وَيَوْمَ أَمُوتُ, tr:yevme vülidtü ve yevme emût, gloss:doğduğum gün ve öleceğim gün, source:19:33}. Mirasçıya neden ihtiyaç duyulduğunu ise Zekeriya'nın duası gösterir. Yaşlanmış, karısı kısır bir adam Rabbine yalvarır: {ar:وَهَنَ ٱلْعَظْمُ مِنِّى وَٱشْتَعَلَ ٱلرَّأْسُ شَيْبًۭا, tr:vehene'l-azmu minnî ve'şteale'r-re'sü şeybâ, gloss:kemiğim zayıfladı, başım ağarmış saçla tutuştu, source:19:4}. Kendisinden sonra yakınlarının ne yapacağından korkar ve bir veli ister {source:19:5}. O veli de {ar:يَرِثُنِى, tr:yerisünî, gloss:bana mirasçı olsun, source:19:6}. Başka bir surede aynı dua şöyle geçer: {ar:رَبِّ لَا تَذَرْنِى فَرْدًۭا وَأَنتَ خَيْرُ ٱلْوَٰرِثِينَ, tr:rabbi lâ tezernî ferden ve ente hayru'l-vârisîn, gloss:Rabbim beni tek başıma bırakma; sen mirasçıların en hayırlısısın, source:21:89}. Ölümlü insan yalnız kalmaktan korkar ve çocuk ister; seslendiği Rab ise mirasçıya ihtiyacı olmayan, bizzat kendisi mirasçı olandır: {ar:إِنَّا نَحْنُ نَرِثُ ٱلْأَرْضَ وَمَنْ عَلَيْهَا, tr:innâ nahnü nerisü'l-arda ve men aleyhâ, gloss:yeryüzüne ve üzerindekilere biz vâris oluruz, source:19:40}. İnsan ömrünün bütün eğrisi tek bir ayette anlatılır: {ar:خَلَقَكُم مِّن ضَعْفٍۢ ثُمَّ جَعَلَ مِنۢ بَعْدِ ضَعْفٍۢ قُوَّةًۭ ثُمَّ جَعَلَ مِنۢ بَعْدِ قُوَّةٍۢ ضَعْفًۭا وَشَيْبَةًۭ, tr:halakaküm min da'fin sümme ceale min ba'di da'fin kuvvaten sümme ceale min ba'di kuvvetin da'fen ve şeybeh, gloss:sizi zayıflıktan yarattı, sonra zayıflığın ardından güç verdi, sonra gücün ardından zayıflık ve yaşlılık verdi, source:30:54}. Nesillerin birbirinin yerine geçmesi de Allah'ın elindedir: {ar:إِن يَشَأْ يُذْهِبْكُمْ وَيَسْتَخْلِفْ مِنۢ بَعْدِكُم مَّا يَشَآءُ كَمَآ أَنشَأَكُم مِّن ذُرِّيَّةِ قَوْمٍ ءَاخَرِينَ, tr:in yeşe' yüzhibküm ve yestahlif min ba'diküm mâ yeşâü kemâ enşeeküm min zürriyyeti kavmin âharîn, gloss:dilerse sizi götürür, sizi başka bir kavmin soyundan var ettiği gibi ardınızdan dilediğini yerinize getirir, source:6:133}. Samed'in "yarattıkları yok olduktan sonra kalan" anlamı da Kur'an'daki karşılığını bulur: {ar:كُلُّ مَنْ عَلَيْهَا فَانٍۢ, tr:küllü men aleyhâ fân, gloss:yeryüzündeki herkes yok olucudur, source:55:26}, {ar:وَيَبْقَىٰ وَجْهُ رَبِّكَ, tr:ve yebkâ vechü rabbik, gloss:Rabbinin yüzü kalır, source:55:27}. Nesil zinciri, ölümün kaçınılmaz olduğu yerde işler; Samed ise bu zincirin dışında kalandır.

Kaynaklar: 112:4 كُفُوًا ك ف ء B001; 112:3 يَلِدْ و ل د B002; 112:3 يَلِدْ و ل د B003; 112:3 يُولَدْ و ل د B001; 112:3 يُولَدْ و ل د B004; 112:3 يُولَدْ و ل د B006; 112:4 يَكُن ك و ن B001; 112:4 يَكُن ك و ن B005; 112:2 ٱلصَّمَدُ ص م د B007

## İçi boş olmayan dolu beden

Samed'in en somut anlamı fiziksel bir niteliktir. Samed, baştan sona dolu olan, içinde boşluk bulunmayan şeydir: {ar:المصمت الذي ليس بأجوف والصمدة صخرة راسية, tr:el-musmet ellezî leyse bi-ecvef ve's-samdetü sahratün râsiyeh, gloss:içi boş olmayan dolu şey; samde, yere sağlamca oturmuş kayadır, source:"ص م د,B002"}. Aynı aile yarığı olmayan sert toprağı da adlandırır: {ar:المصمد الصلب الذي ليس فيه خدد والشديد من الأرض, tr:el-musmed es-sulb ellezî leyse fîhi hudad ve'ş-şedîdü mine'l-ard, gloss:musmed, içinde yarık bulunmayan sert şey ve toprağın sert olanıdır, source:"ص م د,B002"}. Kökte bir şişenin ağzını kapatan tıpa da vardır: {ar:الصماد عفاص القارورة وصمدتها صمدا, tr:es-simâd ifâsu'l-kârûre ve samedtühâ samden, gloss:simâd şişenin tıpasıdır; onu tıpaladım, source:"ص م د,B003"}. Tıpalı şişenin ağzından ne bir şey girer ne bir şey çıkar.

Üçüncü ayet hemen bu kelimenin arkasından gelir ve çıkışın iki yönünü sayar: O'ndan bir şey çıkmaz ({ar:لَمْ يَلِدْ, tr:lem yelid, gloss:doğurmadı, source:112:3}), O da bir şeyden çıkmamıştır ({ar:وَلَمْ يُولَدْ, tr:ve lem yûled, gloss:ve doğurulmadı, source:112:3}). Doğum, içinde bir şey taşıyan bir bedenin bu taşıdığını dışarı bırakmasıdır: {ar:الولادة فهو وضع الوالدة ولدها؛ شاة والد وهي الحامل, tr:el-vilâde fe-hüve vad'u'l-vâlideti veledehâ; şâtün vâlid ve hiye'l-hâmil, gloss:doğum, annenin çocuğunu bırakmasıdır; gebe koyuna şâtün vâlid denir, source:"و ل د,B003"}. Aynı kökten gelen tevellüd, bir şeyin başka bir şeyden çıkıp oluşmasıdır: {ar:تولد الشيء عن الشيء حصل عنه, tr:tevelleda'ş-şey'ü ani'ş-şey' hasale anh, gloss:bir şey öbüründen doğdu, ondan meydana geldi, source:"و ل د,B005"}. Dördüncü ayetteki denk kelimesinin kökü ise içi boş kabın bir başka işleyişini anlatır: {ar:كفأت الإناء إذا كببته, tr:kefe'tü'l-inâe izâ kebebtühû, gloss:kabı ters çevirip boşalttım, source:"ك ف ء,B002"}. Böylece sahne fiziksel terimlerle işler. İçi boş bir beden bir şey taşır ve taşıdığını dışarı bırakabilir: ya doğurur ya da devrilip boşalır. Dolu bir bedenin ise verecek bir içi de, içinden çıktığı bir başka iç de yoktur. İkinci ayetin "Samed" sözünden sonra üçüncü ayetin "doğurmadı ve doğurulmadı" sözünün gelmesi, bu imgeyi ardı ardına okutur. Sade bir açıklama "Allah'ın çocuğu yoktur" der ve orada kalır. İmge ise bu yokluğun nedenini gösterir: doğurmak bir iç gerektirir, Samed'in içi yoktur.

Kur'an içinde bir şey taşıyan bedeni ve onun taşıdığını bırakmasını sahneler. İmran'ın karısı hamileyken taşıdığı çocuğu Rabbine adar ve onu {ar:مَا فِى بَطْنِى, tr:mâ fî batnî, gloss:karnımdaki, source:3:35} diye anar. Doğumdan sonra da şöyle der: {ar:فَلَمَّا وَضَعَتْهَا قَالَتْ رَبِّ إِنِّى وَضَعْتُهَآ أُنثَىٰ, tr:fe-lemmâ vadaathâ kâlet rabbi innî vada'tühâ ünsâ, gloss:onu doğurunca "Rabbim, onu kız doğurdum" dedi, source:3:36}. Burada kullanılan "vad'" fiili, doğumun tarifindeki fiilin ta kendisidir. İnsana anne babası hakkında verilen öğütte de aynı işlem iki adımda anlatılır: {ar:حَمَلَتْهُ أُمُّهُۥ كُرْهًۭا وَوَضَعَتْهُ كُرْهًۭا, tr:hamelethü ümmühû kurhen ve vadaathü kurhâ, gloss:annesi onu zahmetle taşıdı ve zahmetle doğurdu, source:46:15}. İnsan bedeninin bir içi olduğunu Kur'an başka bir yerde açıkça söyler: {ar:مَّا جَعَلَ ٱللَّهُ لِرَجُلٍۢ مِّن قَلْبَيْنِ فِى جَوْفِهِۦ, tr:mâ cealallâhü li-racülin min kalbeyni fî cevfih, gloss:Allah bir adamın içinde iki kalp yaratmadı, source:33:4}. "Cevf", Samed'in tarifinde yokluğu söylenen boşluğun kökünden gelir.

İçi olan bir beden yalnızca dışarı vermez, dışarıdan da alır. Allah, Mesih'in ilahlığı iddiasına cevap verirken anneyi ve oğlu birlikte anar: {ar:كَانَا يَأْكُلَانِ ٱلطَّعَامَ, tr:kânâ ye'külâni't-taâm, gloss:ikisi de yemek yerlerdi, source:5:75}. Bir doğuran ile bir doğurulan, yani üçüncü ayetin iki yönü, burada yemek yiyen iki beden olarak ilahlığın karşısına konur. Elçiler hakkında da şöyle denir: {ar:وَمَا جَعَلْنَٰهُمْ جَسَدًۭا لَّا يَأْكُلُونَ ٱلطَّعَامَ وَمَا كَانُوا۟ خَٰلِدِينَ, tr:ve mâ cealnâhüm ceseden lâ ye'külûne't-taâme ve mâ kânû hâlidîn, gloss:onları yemek yemeyen bedenler kılmadık; ölümsüz de değillerdi, source:21:8}. Allah ise bunun tam tersiyle anlatılır: {ar:وَهُوَ يُطْعِمُ وَلَا يُطْعَمُ, tr:ve hüve yut'imü ve lâ yut'am, gloss:O doyurur, kendisi doyurulmaz, source:6:14}. Cinleri ve insanları niçin yarattığını anlattığı yerde de şöyle der: {ar:وَمَآ أُرِيدُ أَن يُطْعِمُونِ, tr:ve mâ ürîdü en yut'imûn, gloss:beni doyurmalarını istemem, source:51:57}. Ne bir şey girer ne bir şey çıkar.

Kaynaklar: 112:2 ٱلصَّمَدُ ص م د B002; 112:2 ٱلصَّمَدُ ص م د B003; 112:3 يَلِدْ و ل د B003; 112:3 يَلِدْ و ل د B005; 112:4 كُفُوًا ك ف ء B002

## Kapısına gidilen efendi

Samed'in bir başka anlamı, tek bir tarifte hem bir hareketi hem de bir rütbeyi bir arada tutar: {ar:صمده يصمده صمدا أي قصده والصمد السيد لأنه يصمد إليه في الحوائج وبيت مصمد أي مقصود, tr:samedehû yasmüdühû samden ey kasadehû ve's-samed es-seyyid li-ennehû yusmedü ileyhi fi'l-havâic ve beytün musammed ey maksûd, gloss:samedehû, ona yöneldi demektir; Samed efendidir, çünkü ihtiyaçlarda ona yönelinir; beytün musammed, gidilen ev demektir, source:"ص م د,B001"}. Sahnede bir ev ve bir kapı vardır. İnsanlar ihtiyaçlarını alıp oraya giderler. Kapısına gidilen kişi efendidir ve efendiliği de tam olarak bu yönelişten gelir. Yöneliş bir dayanmayı da içerir: {ar:وصمده قصد معتمدا عليه قصده, tr:ve samedehû kasade mu'temiden aleyhi kasdehû, gloss:ona dayanarak yöneldi, source:"ص م د,B001"}. Bu efendinin efendiliği en son noktasına varmıştır: {ar:الصمد السيد الذي قد انتهى سؤدده, tr:es-samed es-seyyid ellezî kad inteha sü'dedüh, gloss:Samed, efendiliği son noktasına varmış efendidir, source:"ص م د,B001"}. Kendisine gelen işi gözetir ve onunla ilgilenir: {ar:إني على صمادة من أمر إذا أشرف عليه وحفلت به, tr:innî alâ samâdetin min emrin izâ eşrafe aleyhi ve hafeltü bih, gloss:bir işi gözetip onunla ilgilendiğimde "o işin samâdesi üzerindeyim" denir, source:"ص م د,B005"}.

Birinci ve ikinci ayetteki {ar:ٱللَّهُ, tr:Allah, gloss:Allah, source:112:2} adı da aynı yönelişi taşır. Kök kulluk etmeyi anlatır ve ilah, kulluk edilen olduğu için bu adı alır: {ar:أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود, tr:aslün vâhid ve hüve't-teabbüd, fe'l-ilâh Allâhu teâlâ li-ennehû ma'bûd, gloss:tek bir köktür, kulluk etmeyi anlatır; ilah, kulluk edilen olduğu için yüce Allah'tır, source:"ء ل ه,B001"}. Kulun bu yöneliş içindeki hâli de aynı köktendir: {ar:التأله التنسك والتعبد, tr:et-teellüh et-tenessük ve't-teabbüd, gloss:teellüh, kendini ibadete vermektir, source:"ء ل ه,B001"}. Ad, ihtiyacı olanın seslendiği addır: {ar:يا ألله اغفر لي, tr:yâ allâhu'ğfir lî, gloss:ey Allah, beni bağışla, source:"ء ل ه,B002"}. Yönelişin bir de tersi vardır. Aynı kök çok yöne dağılmış kulluğu da adlandırır: {ar:الآلهة الأصنام, tr:el-âlihe el-esnâm, gloss:âlihe putlardır, source:"ء ل ه,B001"}; bir kavim ona taptığı için güneşe bile bu kökten bir ad verilmiştir {source:"ء ل ه,B001"}. Dördüncü ayetteki denk kelimesinin kökü de yönelişi saptırmayı anlatır: {ar:كفأت القوم إذا صرفتهم إلى غيره, tr:kefe'tü'l-kavme izâ sarafthüm ilâ ğayrih, gloss:bir kavmi başka birine yönelttim, source:"ك ف ء,B002"}.

Kapısına gidilen efendinin çevresinde rütbeleri olan bir düzen vardır. Dördüncü ayetteki fiilin kökü konumu ve itibarı anlatır: {ar:المكانة المنزلة؛ مكين عند فلان بين المكانة, tr:el-mekâne el-menzile; mekînün inde fülânin beyyinü'l-mekâne, gloss:mekâne konum ve itibardır; falanın yanında itibarı açıkça yüksektir, source:"ك و ن,B002"}. Aynı kök birine kefil olmayı da anlatır: {ar:الكيانة الكفالة؛ كنت على فلان أكون كونا أي تكفلت به, tr:el-kiyâne el-kefâle; küntü alâ fülânin ekûnü kevnen ey tekeffeltü bih, gloss:kiyâne kefalettir; falana kefil oldum, source:"ك و ن,B003"}. Alttakilerin boyun eğişini de anlatır: {ar:الاستكانة الخضوع, tr:el-istikâne el-hudû', gloss:istikâne boyun eğmektir, source:"ك و ن,B004"}. Birinci ayetin ilk kelimesi olan {ar:قُلْ, tr:kul, gloss:de, source:112:1} fiilinin kökü de bu düzende bir hükümdarı adlandırır: {ar:القيل ملك من ملوك حمير دون الملك الأعظم, tr:el-kayl melikün min mülûki himyer dûne'l-meliki'l-a'zam, gloss:kayl, en büyük hükümdardan aşağı rütbedeki Himyer krallarından biridir, source:"ق و ل,B004"}. Bu adı, sözü yerine getirildiği için almıştır: {ar:كأنه الذي له قول أي ينفذ قوله, tr:ke-ennehû'llezî lehû kavlün ey yenfüzü kavlüh, gloss:sanki sözü olan, yani sözü yürüyen kişidir, source:"ق و ل,B004"}. Denk ise böyle bir düzende hükümdarın karşısına çıkabilecek tek kişidir. O, soyda, malda ve savaşta dengidir {source:"ك ف ء,B001"}; hükümdarın evine kız verebilir, onunla eşit şartlarda savaşabilir, iyiliğine aynısıyla karşılık verebilir: {ar:المكافأة مجازاة النعم, tr:el-mükâfee mücâzâtü'n-niam, gloss:mükâfee, nimetlere karşılık vermektir, source:"ك ف ء,B001"}. Kapıya ihtiyacıyla gelen kişi ise aldığına aynısıyla karşılık veremez. Dördüncü ayet bu düzenden yalnızca bir kişiyi çıkarır: zirvede efendiye denk olabilecek kişiyi. Kapıya gelenler, kefil olunanlar ve boyun eğenler yerlerinde kalır.

Kur'an kapıya gidişi insanın kendi hâli olarak gösterir. Allah insanlara, sahip oldukları her nimetin O'ndan geldiğini hatırlattıktan sonra şöyle der: {ar:ثُمَّ إِذَا مَسَّكُمُ ٱلضُّرُّ فَإِلَيْهِ تَجْـَٔرُونَ, tr:sümme izâ messekümü'd-durru fe-ileyhi tec'erûn, gloss:sonra size bir sıkıntı dokununca yalnız O'na yalvarırsınız, source:16:53}. Bir başka yerde aynı yöneliş bir soru hâlinde gelir: {ar:أَمَّن يُجِيبُ ٱلْمُضْطَرَّ إِذَا دَعَاهُ وَيَكْشِفُ ٱلسُّوٓءَ, tr:em men yücîbü'l-mudtarra izâ deâhü ve yekşifü's-sû', gloss:darda kalan kendisine yalvardığında ona karşılık veren ve sıkıntıyı gideren kimdir, source:27:62}. Hemen ardından da {ar:أَءِلَٰهٌۭ مَّعَ ٱللَّهِ, tr:e-ilâhün maallâh, gloss:Allah'la birlikte başka bir ilah mı var, source:27:62} diye sorulur. Kapıya gelenlerin sayısı varlığın tamamıdır: {ar:يَسْـَٔلُهُۥ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:yes'elühû men fi's-semâvâti ve'l-ard, gloss:göklerde ve yerde olan herkes O'ndan ister, source:55:29}. Kapıya gelenlerle efendi arasındaki fark da bir cümlede söylenir: {ar:أَنتُمُ ٱلْفُقَرَآءُ إِلَى ٱللَّهِ ۖ وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:entümü'l-fukarâü ilallâh, vallâhü hüve'l-ğaniyyü'l-hamîd, gloss:siz Allah'a muhtaçsınız; Allah ise zengin olandır, övülendir, source:35:15}. Kulun kendi sözü kulluğu ve dayanmayı aynı tek yöne çevirir: {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyâke na'büdü ve iyyâke neste'în, gloss:yalnız sana kulluk eder, yalnız senden yardım isteriz, source:1:5}. Yönelişin saptırıldığı sahne de Kur'an'da vardır. Aracılar edinenler şöyle der: {ar:مَا نَعْبُدُهُمْ إِلَّا لِيُقَرِّبُونَآ إِلَى ٱللَّهِ زُلْفَىٰٓ, tr:mâ na'büdühüm illâ li-yukarribûnâ ilallâhi zülfâ, gloss:onlara, bizi Allah'a yaklaştırsınlar diye kulluk ediyoruz, source:39:3}. Yusuf da zindan arkadaşlarına şunu sorar: {ar:ءَأَرْبَابٌۭ مُّتَفَرِّقُونَ خَيْرٌ أَمِ ٱللَّهُ ٱلْوَٰحِدُ ٱلْقَهَّارُ, tr:e-erbâbün müteferrikûne hayrun emillâhü'l-vâhidü'l-kahhâr, gloss:birbirinden ayrı birçok rab mı daha iyidir, yoksa her şeye galip olan tek Allah mı, source:12:39}. Allah'tan başka ilahlar edinenler hakkında ise şu söylenir: {ar:لَّا يَخْلُقُونَ شَيْـًۭٔا وَهُمْ يُخْلَقُونَ, tr:lâ yahlukûne şey'en ve hüm yuhlakûn, gloss:hiçbir şey yaratmazlar, kendileri yaratılırlar, source:25:3}.

Zirvede bir denk bulunsaydı ne olacağı da sahnelenir. Peygambere surenin kalıbıyla örülmüş bir övgü emredilir: {ar:وَقُلِ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى لَمْ يَتَّخِذْ وَلَدًۭا وَلَمْ يَكُن لَّهُۥ شَرِيكٌۭ فِى ٱلْمُلْكِ وَلَمْ يَكُن لَّهُۥ وَلِىٌّۭ مِّنَ ٱلذُّلِّ, tr:ve kuli'l-hamdü lillâhi'llezî lem yettehiz veleden ve lem yekün lehû şerîkün fi'l-mülki ve lem yekün lehû veliyyün mine'z-züll, gloss:de ki: övgü, çocuk edinmeyen, mülkte ortağı olmayan ve düşkünlükten ötürü bir koruyucuya ihtiyacı olmayan Allah'adır, source:17:111}. Ayette "kul", "veled" ve "lem yekün lehû" bir arada geçer ve bu kez mülke, yani hükümranlığa uygulanır. Allah, çocuğu ve yanında başka ilahları reddederken eşit rütbedekilerin ne yapacağını söyler: {ar:إِذًۭا لَّذَهَبَ كُلُّ إِلَٰهٍۭ بِمَا خَلَقَ وَلَعَلَا بَعْضُهُمْ عَلَىٰ بَعْضٍۢ, tr:izen le-zehebe küllü ilâhin bi-mâ halaka ve le-alâ ba'duhüm alâ ba'd, gloss:o zaman her ilah kendi yarattığını alıp giderdi ve biri öbürüne üstün gelmeye kalkardı, source:23:91}. Peygambere söylemesi emredilen sözde de aynı şey vardır: {ar:إِذًۭا لَّٱبْتَغَوْا۟ إِلَىٰ ذِى ٱلْعَرْشِ سَبِيلًۭا, tr:izen le'bteğav ilâ zi'l-arşi sebîlâ, gloss:o zaman Arş'ın sahibine bir yol ararlardı, source:17:42}. Savaşta denk olanın tarifi burada sahne olmuştur: eşit güçteki ikinci, tahtı ister. Sonuç da açıkça söylenir: {ar:لَوْ كَانَ فِيهِمَآ ءَالِهَةٌ إِلَّا ٱللَّهُ لَفَسَدَتَا, tr:lev kâne fîhimâ âlihetün illallâhü le-fesedetâ, gloss:yerde ve gökte Allah'tan başka ilahlar olsaydı ikisi de bozulurdu, source:21:22}.

Kaynaklar: 112:2 ٱلصَّمَدُ ص م د B001; 112:2 ٱلصَّمَدُ ص م د B005; 112:1 ٱللَّهُ ء ل ه B001; 112:1 ٱللَّهُ ء ل ه B002; 112:1 قُلْ ق و ل B004; 112:4 يَكُن ك و ن B002; 112:4 يَكُن ك و ن B003; 112:4 يَكُن ك و ن B004; 112:4 كُفُوًا ك ف ء B001; 112:4 كُفُوًا ك ف ء B002; 112:1 أَحَدٌ ء ح د B005

## Buluşmalar

Birde duran sayı ile içi boş olmayan dolu beden aynı işlemin iki yüzüdür. İçi olan bir beden ikinci bir varlık doğurur; doğum bir şeyden başka bir şeyin çıkması, yani birin ikiye bölünmesidir. Samed'in dolu oluşu ile ehad'in ikiye geçmeyişi, üçüncü ayette tek bir cümleye dönüşür: içinden bir şey çıkmayan, ikincisi de olmayandır. En’âm suresindeki ayet bu iki imgeyi ve nesil zincirini bir arada tutar: {ar:أَنَّىٰ يَكُونُ لَهُۥ وَلَدٌۭ وَلَمْ تَكُن لَّهُۥ صَٰحِبَةٌۭ, tr:ennâ yekûnü lehû veledün ve lem tekün lehû sâhibeh, gloss:O'nun eşi olmamışken nasıl çocuğu olur, source:6:101}. Eş bir ikincidir, çocuk bir başka ikincidir; ikisi de olmayınca sayı birde kalır. Yaratılmışların çift hâlinde var olması ile O'nun benzerinin olmaması da Şûrâ suresinde aynı ayette durur {source:42:11}.

Samed kelimesinin iki anlamı, yani içi boş olmayan dolu beden ve yarattıkları yok olduktan sonra kalan daim varlık, üçüncü ayette birlikte karşılık bulur: O'nda doğuracak bir iç yoktur ve ölen bir zincirde yeri yoktur. Enbiyâ suresinde elçiler hakkında söylenen söz bu iki imgeyi tek bir sahnede birleştirir: {ar:وَمَا جَعَلْنَٰهُمْ جَسَدًۭا لَّا يَأْكُلُونَ ٱلطَّعَامَ وَمَا كَانُوا۟ خَٰلِدِينَ, tr:ve mâ cealnâhüm ceseden lâ ye'külûne't-taâme ve mâ kânû hâlidîn, gloss:onları yemek yemeyen bedenler kılmadık; ölümsüz de değillerdi, source:21:8}. Yemek yiyen beden, yani içi olan beden, ölen bedendir. Mesih ile annesinin birlikte yemek yediğini söyleyen ayet de {source:5:75} doğuran ile doğurulanı içi olan iki beden olarak gösterir.

Kapısına gidilen efendi ile nesil zinciri, Meryem suresinde birbirine bağlanır. Çocuk olduğu iddia edilenler kapıya gelen kullardır: {ar:إِن كُلُّ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ إِلَّآ ءَاتِى ٱلرَّحْمَٰنِ عَبْدًۭا, tr:in küllü men fi's-semâvâti ve'l-ardı illâ âti'r-rahmâni abdâ, gloss:göklerde ve yerde olan herkes Rahman'a ancak kul olarak gelecektir, source:19:93}. Hemen önceki ayette {ar:وَمَا يَنۢبَغِى لِلرَّحْمَٰنِ أَن يَتَّخِذَ وَلَدًا, tr:ve mâ yenbeğî li'r-rahmâni en yettehıze veledâ, gloss:çocuk edinmek Rahman'a yakışmaz, source:19:92} denmiştir. Aynı iddiaya bir başka yerde verilen cevap da aynıdır: {ar:بَلْ عِبَادٌۭ مُّكْرَمُونَ, tr:bel ibâdün mükramûn, gloss:hayır, onlar ikram edilmiş kullardır, source:21:26}. Mesih'in kendisi de beşikte ilk sözünü bu yönde söyler: {ar:إِنِّى عَبْدُ ٱللَّهِ, tr:innî abdullâh, gloss:ben Allah'ın kuluyum, source:19:30}. Zincirde çocuk yerine konmak istenen, efendinin kapısındaki kuldur.

Efendi imgesi ile birde duran sayı, zirvedeki denkte buluşur. Soyda, malda ve savaşta denk olan kişinin yokluğunu dördüncü ayet olumsuz ehad ile söyler. Eşit rütbede ikinci bir ilah olsaydı neler olacağını anlatan ayetler {source:23:91} {source:17:42}, savaşta denk olanın tarifini sahneye dönüştürür. İsrâ suresindeki övgü {source:17:111} da surenin kalıbını hükümranlığa uygular.

Söz imgelerinin ikisi Bakara suresinde iki ayet arasında karşılaşır. Uydurulmuş söz {ar:وَقَالُوا۟ ٱتَّخَذَ ٱللَّهُ وَلَدًۭا, tr:ve kâlü'ttehazallâhü veledâ, gloss:Allah çocuk edindi dediler, source:2:116} ile başlar, yaratıcı söz {ar:يَقُولُ لَهُۥ كُن فَيَكُونُ, tr:yekûlü lehû kün fe-yekûn, gloss:ona "ol" der, o da olur, source:2:117} ile biter. Her iki ayet de aynı soruya cevap verir: şeyler Allah'tan doğarak mı, yoksa O'nun sözüyle mi var olur? Ahzâb suresindeki ayet de iki sözü yan yana koyar; bir yanda ağızla söylenen söz, öbür yanda {ar:وَٱللَّهُ يَقُولُ ٱلْحَقَّ, tr:vallâhü yekûlü'l-hakk, gloss:Allah doğruyu söyler, source:33:4}. Doğum kökünün uydurulmuş söz için de kullanılması, sözler yarışmasını nesil zincirine bağlar: "Allah doğurdu" diyenlerin sözü {source:37:152}, kendisi de "doğurulmuş", yani uydurulmuş bir sözdür.

Bu buluşmalar surenin hareketini taşır. Birinci ayet bir sözle açılır ve sayıyı bire koyar. İkinci ayet bütün yönelişi, kapısına gidilen, içi boş olmayan ve her şey yok olduktan sonra kalan tek bir efendiye çevirir. Üçüncü ayet bu efendiden çıkışı da efendinin bir şeyden çıkışını da kapatır ve nesil zincirini, uydurulmuş "doğurdu" sözüyle birlikte dışarıda bırakır. Dördüncü ayet olumsuz kevn ile hiçbir dengin hiçbir zaman var olmadığını söyler ve sureyi başladığı kelimeyle, bu kez içinde hiç kimse bulunmayan ehad ile kapatır.

