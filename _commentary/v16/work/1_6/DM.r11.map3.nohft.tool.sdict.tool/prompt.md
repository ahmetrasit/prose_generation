Focus: 1:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and dictionary.md (every attested branch of every root of the surah's words, with the classical dictionaries' source phrases; the focus ayah's roots are those whose heading lists the focus ayah. The other roots are there only to find resonances within the focus ayah: use one where it joins or sharpens a sense of a focus word, never to read the other ayat for their own sake) and map.md (an earlier reader's map of the image chains that run through the whole surah, with the dictionary phrases of their members in other ayat; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/OZTURK/_projects/prose_generation/_commentary/v16/missing.py 1:6 <refs separated by spaces>`. It lists passages from an earlier cross-reference list that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. Run the command only once; no other tool is available.

===== _commentary/v16/prompts/r11/write.md =====
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
another ayah completes it, and so can a scene where two such chains meet; a
chain an earlier ayah opened is recalled briefly.

Keep these guards:

- A family image is heard beside the word's meaning in this ayah, never in
  place of it; say so once, where the first one enters. Show where each
  image comes from: the word, the usage that carries the image, quoted in
  Arabic, then its work in the theme. Report usage as what speakers called
  or said, in varied wording; never name a dictionary, and never make "the family"
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
  give the speaker, the situation and the wording the connection needs.
- The prose never talks about its own sources or process and never hedges in
  the first person ("hafızadan",
  "bildiğim kadarıyla", branch IDs, workflow language). What comes from memory
  rather than the supplied texts goes in the ledger.

Write continuous prose in `##` sections, one theme each, warm and direct:
explain, do not dramatize; no lists and no closing recap.

Every Arabic quotation (Quran, hadith or dictionary phrase) goes in the reader
tag, as normal prose, never in quotation marks or backticks:
{ar:exact Arabic, tr:readable Turkish transliteration, gloss:Turkish meaning}
The gloss gives the ayah's word by its meaning here, a family image by that
image. Cite Quran passages with exact refs, e.g. (2:255), no ranges; copy Quran
Arabic from the supplied text where it is supplied.

Output: the prose; then a line containing only
=== LEDGER ===
then, in plain English, one line per item:
- memory: <what came from memory> (<ref or source>)
- not written: <a finding you weighed and left out> - <what it would have made visible, and why it could not found, reshape or join a theme>


===== _commentary/v16/prompts/r11/additions.md =====
No additions: write.md is the whole brief.


===== _commentary/v16/work/1_6/DM.r3/context.md =====
# 1:6 — focus

ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ

Anchor translation (canonical reading, reference only):

Bizi doğru yola ilet.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ٱهْدِنَا | هَدَى | ه د ي | V;PRON |
| 2 | ٱلصِّرَٰطَ | صِرَٰط | ص ر ط | DET;N |
| 3 | ٱلْمُسْتَقِيمَ | مُّسْتَقِيم | ق و م | DET;ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 1 — full text (context; no pericope)

- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ◀ focus ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ


===== _commentary/v16/work/s001/surah.r2/dictionary.md =====
# Dictionary: every branch of every root of the surah

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## س م و (root_000745): 1:1 بِسْمِ

- **B001** fiziksel ya da toplumsal yükselme — yükselme, yücelme · yükselmek, yücelmek · bakışı yukarı yönelmek · toplumdaki yeri ve değeri yükselmiş olmak · gururla başını ve bakışını kaldırmak
  أصل يدل على العلو؛ سموت إذا علوت (maqayis)؛ سما الشيء يسمو سموا أي ارتفع (ayn)؛ السمو الارتفاع والعلو (sihah)؛ سما الشيء يسمو سموا وهو ارتفاعه، ويقال للحسيب والشريف قد سما (tahdhib)؛ أصله من السمو وهو الذي به رفع ذكر المسمى (mufradat)
- **B002** yükselerek uzaktan beliren görünüş — uzakta yükselip görünür olmak · bir şeyin yüksekte görünen gövdesi veya dış çizgisi · ayın ince yayının ufuktan yükselen görünüşü
  سما لي شخص ارتفع حتى استثبته؛ سماوة الهلال وكل شيء شخصه (maqayis)؛ سما لي شيء؛ سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا (ayn)؛ سما لي شخص؛ سماوة كل شيء شخصه (sihah)؛ سما لي شيء؛ سماوته أي شخصه؛ سماوة الهلال شخصه (tahdhib)؛ السماوة الشخص العالي؛ وسما لي شخص (mufradat)
- **B003** erkek devenin dişi deve sürüsüne atılıp aralarına girmesi [kalıp] — erkek devenin dişi deve sürüsüne atılıp aralarına girmesi
  سما الفحل سطا على شوله سماوة (maqayis)؛ سما الفحل إذا تطاول على شوله (ayn;tahdhib)؛ سما الفحل إذا سطا على شوله سماوة (sihah)؛ سما الفحل على الشول سماوة لتخلله إياها (mufradat)
- **B004** üstteki gök veya örtü ve buna bağlı üstten gelen ya da üstte bulunan şeyler — gök, tavan veya bir şeyin üst yanı · yağmur · bulut · yağmurla çıkan veya yerden yükselen bitki · atın sırtı veya üst yanı · evin tavanı · her şeyin en üst yanı
  العرب تسمى السحاب سماء والمطر سماء؛ السماء سقف البيت وكل عال مطل سماء؛ يسموا النبات سماء (maqayis)؛ السماء كل ما علاك فأظلك؛ السماء المطر؛ السماء ظهر الفرس؛ سماوة البيت سقفه (sihah)؛ السماء سقف كل شيء وكل بيت؛ السماء السحاب؛ السماء المطر (tahdhib)؛ سماء كل شيء أعلاه؛ سمي المطر سماء؛ سمي النبات سماء (mufradat)
- **B005** ad, adlandırma ve ad ya da nitelik bakımından denklik — bir şeyi tanıtan ad · birine bir ad vermek veya onu o adla çağırmak · bir adı edinmek ve o adla anılmak · aynı adı taşıyan kişi, adaş · aynı adı veya niteliği hak eden denk · varlıkları tanıtan tekli veya birleşik sözler ve anlamlar
  أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى (maqayis)؛ الاسم أصل تأسيسه السمو؛ سميت وأسميت وتسميت (ayn)؛ سميت فلانا زيدا؛ هذا سمي فلان؛ الاسم مشتق من سموت لأنه تنويه ورفعة (sihah)؛ الاسم مشتق من السمو وهو الرفعة؛ تنويها على الدلالة على المعنى (tahdhib)؛ الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى؛ سميا أي نظيرا له يستحق اسمه (mufradat)
- **B006** av için ıssız araziye çıkma ve buna bağlı avcı kullanımları — avlanmak için kır ve çöl arazisine çıkmak · avcılar · av hayvanını bulup avlamak üzere aramak · avcının sıcak zeminde beklerken giydiği koruyucu çorap
  خرج القوم للصيد في قفار الأرض وصحاريها قلت سموا وهم السماة أي الصيادون (ayn;tahdhib)؛ السماة الصيادون؛ سموا واستموا إذا خرجوا للصيد (sihah)؛ يستمي الوحش أي يطلبها؛ المسماة جورب الصياد (tahdhib)
- **B007** yarışma, övünerek boy ölçüşme ve karşı koyma — birbiriyle yarışmak ve karşı koymak · övünerek yarışma, boy ölçüşme ve karşı koyma · kimsenin kendisiyle yarışamadığı veya boy ölçüşemediği kişi
  فلان لا يسامى؛ تساموا أي تباروا؛ قد علا من ساماه (sihah)؛ معنى تساميها تباريها وتعارضها؛ المساماة المفاخرة (tahdhib)
- **B008** insanlar arasında yayılan iyi ün — insanlar arasında yayılan iyi ün veya iyi söz
  ذهب صيته في الناس وسماه، أي صوته في الخير لا في الشر (tahdhib)

## و س م (root_001650): documented alternative for 1:1 بِسْمِ: Kûfeli dilciler ve Sa‘leb; İbnü’l-Enbârî’nin aktarımı

- **B001** tanıtıcı fiziksel iz koyma, iz ve araç — bir şeyi tanıtıcı bir iz bırakarak işaretlemek · yakma veya kesme yoluyla bırakılmış tanıtıcı iz · tanınmayı sağlayan görünür işaret · üzerine tanıtıcı işaret konmuş · hayvan damgalamaya yarayan kızgın demir · kendine tanınacağı bir işaret edinmek · alt bölümü pirinçle süslenmiş zırh
  ووسمت الشيء وسما: أثرت فيه بسمة (maqayis;sihah)؛ الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي (ayn)؛ أثر كية، إما كية أو قطع في أذنه أو قرمة تكون علامة له (tahdhib)؛ الميسم المكواة أو الشيء الذي يوسم به الدواب (ayn;sihah;tahdhib)
- **B002** belirtiden karakter veya durum sezme — bir kimsede iyilik ya da kötülük belirtisi görüp niteliğini sezmek · duruma işaret eden belirtileri okuyup sonuç çıkaranlar · üzerinde iyilik ya da kötülük belirtisi bulunan
  الناظرين في السمة الدالة (maqayis)؛ توسمت فيه الخير والشر أي رأيت فيه أثرا (ayn)؛ فلان موسوم بالخير، وقد توسمت فيه الخير أي تفرست (sihah)؛ توسمت في فلان خيرا أي رأيت فيه أثرا منه، وتوسمت فيه الخير أي تفرست (tahdhib)
- **B003** toprağı bitkilendiren yılın ilk yağmuru — toprağı bitkilendiren yılın veya ilkbaharın ilk yağmuru · ilk yağmuru alıp etkisini taşıyan toprak · ilk yağmurun çıkardığı otu aramak
  الوسمى أول المطر لأنه يسم الأرض بالنبات (maqayis)؛ الوسمي أول مطر السنة يسم الأرض بالنبات، وأرض موسومة أصابها الوسمي (ayn)؛ الوسمي مطر الربيع الأول لأنه يسم الأرض بالنبات، والأرض موسومة (sihah)؛ سمي الوسمي من المطر وسميا لأنه يسم الأرض بالنبات فيصير فيها أثرا في أول السنة (tahdhib)
- **B004** belirlenmiş toplu buluşma zamanı ve yeri — kutsal ziyaret için belirlenmiş toplu buluşma zamanı ve yeri · eski Arap pazarlarının belirli toplanma zamanları ve yerleri · belirlenmiş toplu buluşmaya katılmak
  وسمى موسم الحاج موسما لأنه معلم يجتمع إليه الناس (maqayis)؛ موسم الحج موسما لأنه معلم يجتمع فيه وكذلك مواسم أسواق العرب (ayn;tahdhib)؛ موسم الحاج مجمعهم، سمي بذلك لأنه معلم يجتمع إليه (sihah)؛ وسم الناس: شهدوا الموسم (maqayis;sihah)
- **B005** kişide görünen yerleşik güzellik ve zarafet — güzellik; kişide görünen hoşluk · yüzü güzel ve hoş görünümlü · güzel ve hoş görünümlü kadın · üzerinde güzellik ve zarafet etkisi bulunan kadın · kişide görünen güzellik ve hoşluk · güzelleşmek ve hoş bir görünüş kazanmak · birini güzellikte geçmek
  فلانة ذات ميسم إذا كان عليها أثر الجمال، والوسامة الجمال (maqayis)؛ ذات ميسم وجمال وميسمها أثر الجمال فيها وهي وسيمة (ayn)؛ الميسم الجمال، وفلان وسيم أي حسن الوجه، ووسم الرجل وسامة ووساما (sihah)؛ فلانة لذات ميسم وميسمها أثر الجمال والعتق، والوسامة والميسم الحسن، والوسيم الثابت الحسن (tahdhib)
- **B006** yaprakları boya olarak kullanılan bitki — yaprakları boya olarak kullanılan bitki veya küçük ağaç
  الوسم والوسمة الواحدة شجرة ورقها خضاب (ayn;tahdhib)؛ الوسمة والعظلم يختضب به (sihah)

## ء ل ه (root_000047): 1:1 ٱللَّهِ, 1:2 لِلَّهِ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 1:1 ٱللَّهِ, 1:2 لِلَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ر ح م (root_000552): 1:1 ٱلرَّحْمَٰنِ, 1:1 ٱلرَّحِيمِ, 1:3 ٱلرَّحْمَٰنِ, 1:3 ٱلرَّحِيمِ

- **B001** acıma duygusuyla esirgeyip iyilik etme — ona acıyıp onu esirgemek · acıma duygusu ve bu duygunun yönelttiği iyilik · özellikle güçsüze acıyıp onu esirgeme · acıma, iyilik ve gözetme · birbirine acıyıp birbirini esirgemek · onun Tanrı'nın esirgemesine erişmesini dilemek · esirgemesi her şeyi kuşatan Tanrı adı · çok esirgeyen ve bol bol iyilik eden · acınıp esirgenen kimse · acıma ve esirgeme görmüş kimse · acıyan ve esirgeyenlerin en üstünü · ana babasına daha iyi davranan ve daha yakınlık gösteren · acıma ve esirgeme ya da başkasının acımasına konu olma durumu
  أصل واحد يدل على الرقة والعطف والرأفة (maqayis)؛ المرحمة الرحمة ورحمته أرحمه رحمة ومرحمة وترحمت عليه (ayn)؛ رحمته رحمة ورحما ومرحمة والرحمن الرحيم مشتقان من الرحمة (jamhara)؛ الرحمة الرقة والتعطف والمرحمة مثله وتراحم القوم (sihah)؛ ذو الرحمة والرحيم العاطف ورحمة الضعيف والتعطف عليه (tahdhib)؛ الرحمة رقة تقتضي الإحسان إلى المرحوم والرحمن والرحيم (mufradat)
- **B002** yakın soy bağı — yakın soy bağı · soy ve yakınlık bağları · soy bağını sürdürmek ya da koparmak
  الرَّحِم علاقة القرابة (maqayis)؛ بينهما رَحِم أي قرابة قريبة والرحم القرابة تجمع بني أب (ayn)؛ صارت أسباب القرابة أرحاما (jamhara)؛ الرحم أيضا القرابة والرحم بالكسر مثله ووصال رحم (sihah)؛ الرحم القرابة تجمع بني أب وبينهما رحم أي قرابة قريبة (tahdhib)؛ استعير الرحم للقرابة لكونهم خارجين من رحم واحدة (mufradat)
- **B003** döl yatağı — dişinin döl yatağı · döl yatakları
  سميت رحم الأنثى رحما (maqayis)؛ الرحم بيت منبت الولد ووعاؤه في البطن (ayn)؛ الرحم رحم المرأة (jamhara)؛ الرحم رحم الأنثى وهي مؤنثة (sihah)؛ الرحم بيت منبت الولد ووعاؤه في البطن (tahdhib)؛ الرحم رحم المرأة (mufradat)
- **B004** döl yatağı hastalığı ve doğum sonrası bozukluk — doğumdan sonra döl yatağı ağrıyan ya da döl yatağı hastalanan dişi · döl yatağı ağrımak ya da hastalanmak · koyunun doğumdan sonra yavru zarını atamaması · döl yatağı şişmiş koyun ya da koyun sürüsü
  شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)؛ ناقة رحوم أصابها داء في رحمها وقد رحمت المرأة إذا اشتكت رحمها (ayn)؛ ناقة رحوم إذا اشتكت رحمها في عقب الولادة وامرأة رحوم (jamhara)؛ الرحوم الناقة التي تشتكي رحمها بعد النتاج (sihah)؛ ناقة رحوم أصابها داء في رحمها والرحام أن تلد الشاة ثم لا تلقي سلاها وشاة راحم وغنم رواحم إذا ورم رحمها (tahdhib)؛ امرأة رحوم تشتكي رحمها (mufradat)

## ح م د (root_000355): 1:2 ٱلْحَمْدُ

- **B001** yermenin karşıtı olan, iyilik için teşekkürü de kapsayan övgü — yermenin karşıtı olan övgü; iyilik için teşekkür de içerebilir · birini, yaptığı övülesi bir işten dolayı övmek · övgü; yerginin karşıtı · Tanrı'yı güzel sözlerle çokça övme · onun için övgü ve teşekkür · övülecek bir iş yapmak ya da sonunda övgü kazanmak · her şeyi çokça, kimi zaman olduğundan fazla öven kimse · çok öven kimse · seni överek başlarım
  الحمد نقيض الذم (maqayis;ayn;jamhara;sihah;tahdhib)؛ الحمد الثناء (ayn;tahdhib;mufradat)؛ الحمد أعم من الشكر (sihah;mufradat)؛ التحميد كثرة حمد الله بحسن المحامد (ayn;tahdhib)
- **B002** deneyip övülesi ya da uygun bulma — birini deneyip övgüye değer bulmak · bir yeri yerleşmeye ya da otlatmaya elverişli bulmak · bu işi benim için uygun buluyor musun? · idrar kanalını yıkamayı sizin için uygun bulmak
  أحمدت فلانا إذا وجدته محمودا (maqayis;ayn;sihah;tahdhib)؛ أحمدت الأرض إذا رضيت سكناها أو مرعاها (jamhara;sihah)؛ هل تحمد لي هذا الأمر أي هل ترضاه لي (tahdhib)
- **B003** övülen veya birçok övülesi niteliği bulunan kimse — övülen, övgüye değer · çokça övülen, birçok övülesi niteliği bulunan · övülmeye daha çok layık olan ya da daha çok öven · övülen; bağlama göre öven
  رجل محمود ومحمد إذا كثرت خصاله المحمودة (maqayis;sihah)؛ محمد كأنه حمد مرة بعد أخرى (jamhara)؛ فلان محمود إذا حمد ومحمد إذا كثرت خصاله المحمودة (mufradat)؛ الحميد بمعنى المحمود (tahdhib;mufradat)
- **B004** övülesi işin varılabilecek en ileri sınırı — yapabileceğinin en ilerisi ve övülecek olanı · aktarılan sözde kadınlarda övülebilecek niteliklerin en ileri derecesi
  حماداك أن تفعل كذا أي غايتك وفعلك المحمود (maqayis)؛ حماداك أن تفعل كذا أي حمدك (ayn;tahdhib)؛ حماداك في معنى قصاراك (jamhara;sihah)؛ حماديات النساء معناه غاية ما يحمد منهن (tahdhib)؛ حماداك أي غايتك المحمودة (mufradat)
- **B005** iyiliğini başa kakıp kendine pay çıkarma [kalıp] — iyiliğini insanların başına kakıp bununla övgü beklemek
  فلان يتحمد علي أي يمن (sihah)؛ من أنفق ماله على نفسه فلا يتحمد به إلى الناس (sihah;tahdhib)
- **B006** muhatabı katarak övme veya iyilikleri teşekkürle anma [kalıp] — seninle birlikte Tanrı'yı övmek veya onun iyiliklerini sana teşekkürle anmak
  أحمد إليك الله أي معك (ayn;tahdhib)؛ أشكر إليك أياديه ونعمه (tahdhib)

## ر ب ب (root_000532): 1:2 رَبِّ

- **B001** sahip olup yönetme — Tanrı; sahip, buyruğu geçen yönetici veya düzenleyici · bir şeyin sahibi · evin sahibi veya ev işlerini yöneten kadın · sahiplik, egemenlik ve yönetim yetkisi
  الرب: الله تبارك وتعالى؛ ورب كل شيء مالكه (jamhara); رب كل شئ: مالكه؛ وقد قالوه في الجاهلية للملك؛ رببت القوم: سستهم (sihah); يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح (tahdhib); الرب مصدر مستعار للفاعل؛ لا يقال الرب مطلقا إلا لله؛ رب الدار ورب الفرس (mufradat); فالرب المالك والخالق والصاحب؛ والله جل ثناؤه الرب (maqayis)
- **B002** adım adım yetiştirip tamamlama — yapılan iyiliği eksiksiz kılmak · mülkü gözetip iyileştirmek · çocuğunu yetiştirmek · bir şeyi aşama aşama olgunlaştırma · yetiştirme anlamındaki değişmeli söyleyiş
  رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها (jamhara); رب الضيعة أي أصلحها وأتمها؛ رب فلان ولده؛ رباه (sihah); رب الشيء أي أصلحه؛ رب فلان الصنيعة إذا أتمها وأصلحها (tahdhib); التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام؛ ربه ورباه ورببه (mufradat); رب فلان ضيعته إذا قام على إصلاحها؛ رببت الصبي أربه (maqayis); ربته تربيتا إذا رببه (maqayis-rbt)
- **B003** Tanrı bilgisiyle yetiştiren bilgin — Tanrı bilgisine sahip bilgin ve öğretici
  الرباني: المتأله العارف بالله تعالى (sihah); الرباني: العالم؛ العلماء بالحلال والحرام؛ حكماء علماء؛ العالم المعلم الذي يغذو الناس بصغار العلوم (tahdhib); الرباني... يرب العلم؛ يرب نفسه بالعلم؛ منسوب إلى الرب (mufradat); الربي العارف بالرب (maqayis)
- **B004** büyük insan topluluğu — büyük topluluk; on bin kişilik topluluk · tek birlik hâlinde birleşmiş beş kabile · insanları toplayan kişi veya toplanma yeri
  الربي: واحد الربيين، وهم الألوف من الناس؛ الرباب خمس قبائل تجمعوا (sihah); الربيون: الألوف؛ الربيون: الجماعات الكثيرة؛ الربة: عشرة آلاف؛ الربان: الجماعة (tahdhib); يجوز أن يضم الربرب إلى الباب الثالث لتجمعه (maqayis)
- **B005** bakımla kurulan üvey aile bağı — üvey oğul veya bakım altında yetişen erkek çocuk · üvey kız veya bakım altında yetişen kız çocuk · bakıcı kadın; evde sütü için beslenen dişi hayvan · çocuğun bakımını üstlenen üvey baba veya üvey anne
  الراب: زوج الأم؛ الرابة: امرأة الأب؛ ربيب الرجل: ابن امرأته من غيره؛ الربيبة: الحاضنة (sihah); الربيب: ابن امرأة الرجل من غيره؛ ربيبة الرجل: بنت امرأته من غيره؛ راب ورابة (tahdhib); الراب والرابة بأحد الزوجين إذا تولى تربية الولد؛ الربيب والربيبة بذلك الولد (mufradat); ربيب الرجل ابن امرأته؛ الراب الذي يقوم على أمر الربيب (maqayis)
- **B006** koyu öz veya yağ tortusu — koyu meyve özü veya yağ tortusu · koyu özle işlenmiş veya güçlendirilmiş · koyu meyve özüyle hazırlanmış yiyecekler
  رب السمن والزيت: ثفله الأسود؛ سقاء مربوب إذا أصلح بالرب (jamhara); الرب: الطلاء الخاثر؛ سقاء مربوب؛ المرببات الأنبجات (sihah); رب فلان نحيه إذا جعل فيه الرب ومتنه به؛ نحي مربوب (tahdhib); رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب (mufradat); هذا سقاء مربوب بالرب؛ الرب للعنب وغيره لأنه يرب به الشيء (maqayis)
- **B007** bir yerde kalıp sürme — bir yerde kalıp ayrılmamak · develerin sürekli kaldığı yer · bulut sürüp gitti · dişi deve erkeğe bağlandı · bir şeye yaklaşma
  رب بالمكان وأرب إذا أقام به (jamhara); مرب الإبل حيث لزمته؛ أربت الإبل؛ أربت الناقة؛ أربت الجنوب والسحابة أي دامت؛ الأرباب الدنو (sihah); أرب فلان بالمكان إذا أقام به فلم يبرحه؛ مرب الإبل أي حيث لزمته (tahdhib); أربت السحابة: دامت؛ أرب فلان بمكان كذا (mufradat); الأصل الآخر لزوم الشيء والإقامة عليه؛ أربت السحابة؛ الإرباب الدنو (maqayis)
- **B008** katmanlı asılı bulut kümesi — beyaz olabilen, katmanlı veya aşağıda asılı bulut
  الرباب: سحاب أبيض؛ الواحدة ربابة (sihah); الربابة: السحابة التي قد ركب بعضها بعضا؛ جمعها رباب (tahdhib); الرباب: السحاب، سمي بذلك لأنه يرب النبات (mufradat); سمي السحاب ربابا؛ السحاب المتعلق دون السحاب يكون أبيض ويكون أسود (maqayis)
- **B009** başlangıçtaki tazelik — yeni doğurmuş veya sütü için evde tutulan koyun · bir şeyin yeni ve taze dönemi · gençliğin ilk ve taze dönemi
  الربى: الشاة التي وضعت حديثا؛ قرب العهد بالولادة؛ بربانه أي بحدثانه وجدته وطراءته (sihah); الربى: أول الشباب؛ الربان من كل شيء: حدثانه؛ الشاة فهي ربى (tahdhib); الشاة الربي التي تحتبس في البيت للبن؛ التي وضعت حديثا (maqayis)
- **B010** kura oklarını toplayan kap — kura oklarını bir arada tutan deri veya bez kap
  الربابة: قطعة من أدم تجمع فيها القداح (jamhara); الربابة شبيهة بالكنانة تجمع فيها سهام الميسر؛ جماعة السهام (sihah); الربابة: جماعة السهام؛ الجلدة التي تجمع فيها السهام (tahdhib); لما يجمع فيه القدح ربابة (mufradat); الخرقة التي يجعل فيها القداح ربابة (maqayis)
- **B011** bağlayıcı söz ve güvence — tarafları birleştiren bağlayıcı söz veya sözleşme · sözleşmeye bağlı taraflar · bağlayıcı söz; söz gibi bağlayıcı vergi payı
  الربابة: العهد والمعاهدون أربة (jamhara); الربابة: العهد والميثاق؛ الأربة أهل الميثاق (sihah); الرباب: العهد؛ الرباب: العشور (tahdhib); العقد في موالاة الغير: الربابة (mufradat); الربابة وهو العهد؛ للمعاهدين أربة؛ الرباب العشور (maqayis)
- **B012** belirli bir yeşil bitki türü — belirli bir bitki, yumuşak ot veya küçük ağaç türü
  الربة: ضرب من الشجر أو النبت (jamhara); الربة بالكسر: ضرب من النبت، والجمع الربب (sihah); الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف (tahdhib)
- **B013** bol ve toplanmış su — çok miktarda su; bazen bol tatlı su
  الربب، بالفتح: الماء الكثير، ويقال العذب (sihah); الربب وهو الماء الكثير سمي بذلك لاجتماعه (maqayis)
- **B014** yaban sığırı sürüsü — yaban sığırı sürüsü; bazen sığır veya deve topluluğu
  الربرب: القطيع من بقر الوحش (sihah); الربرب: جماعة البقر، وكذلك الإبل (tahdhib); الربرب القطيع من بقر الوحش؛ يجوز أن يضم إلى الباب الثالث لتجمعه (maqayis)
- **B015** azlık bildiren ilgeç — belirsiz adla azlık bildiren ilgeç; nice az · eylem önünde bazen veya kimi zaman · azlık ilgecinin sonuna ses eklenmiş ağız biçimi · belirsiz öğe eklenmiş azlık ilgeci biçimi
  رب: كلمة؛ ربما؛ ربت في معنى رب (jamhara); رب حرف خافض؛ ربما؛ ربت؛ ربه رجلا (sihah); رب من حروف المعاني؛ رب للتقليل؛ ربما؛ ربتما؛ تزيد في رب هاء (tahdhib); رب لاستقلال الشيء، ولما يكون وقتا بعد وقت، نحو ربما (mufradat); رب فكلمة تستعمل في الكلام لتقليل الشيء؛ ولا يعرف لها اشتقاق (maqayis)
- **B016** gereksinim, sıkı düğüm veya iyilik — gereksinim · sıkıca bağlanmış düğüm · iyilik ve başkasına yarar sağlama
  الربى: الحاجة؛ الربى: الرابة؛ الربى: العقدة المحكمة؛ الربى: النعمة والإحسان (tahdhib)
- **B017** gemicilerin başı — gemicilerin başı, kaptan
  رباني: رئيس الملاحين (tahdhib)

## ECHO ر ب و (root_000537): for 1:2 رَبِّ: withheld observed target; not identity

- **B001** artmak veya yükselmek — bir şey arttı veya yükseldi · toprak suyla kabarıp arttı · yükselen veya fazla köpük · olağandan daha şiddetli yakalayış · onun üzerine çıktı veya üstünde bulundu
  ربا الجرح والأرض والمال وكل شيء يربو إذا زاد (ayn)؛ ربا الشيء يربو ربوا إذا ارتفع (jamhara)؛ ربا الشيء يربو ربوا أي زاد (sihah;tahdhib)؛ ربت أي زادت، وزبدا رابيا، وأخذة رابية (tahdhib;mufradat)؛ أربى عليه أي أشرف عليه (mufradat)
- **B002** yükselmiş arazi — yükselmiş arazi · çevresinden yüksek yer · arazideki yükselti
  الرابية ما ارتفع من الأرض، والربوة لغات أرض مرتفعة (ayn)؛ الربو والربوة والرباوة واحد وهو العلو من الأرض (jamhara)؛ الرابية الربو وهو ما ارتفع من الأرض، وكذلك الربوة (sihah)؛ الرباوة والرابية والرباة كل ذلك ما ارتفع من الأرض (tahdhib)؛ ربوة وربوة وربوة ورباوة، وسميت الربوة رابية (mufradat)
- **B003** belirli işlem biçimleriyle sınırlı anapara fazlalığı — belirli alışveriş veya borç biçimlerinde anaparayı aşan fazlalık · işlemdeki anapara fazlalığının özel adı veya bir söyleyiş biçimi · mal bu işlemde fazlalıkla arttı · anaparaya fazlalık eklenen işleme girdi
  ربا المال يربو في الربا أي يزداد، والربا في كتاب الله حرام، والربية هي الربا خاصة (ayn)؛ الربا في البيع، والربية لغة في الربا (sihah)؛ الربا ربوان، فالحرام كل قرض يؤخذ به أكثر منه (tahdhib)؛ الربا الزيادة على رأس المال، لكن خص في الشرع بالزيادة على وجه دون وجه (mufradat)
- **B004** soluğu yükselip sıkışmak — yüksek ve sıkışık soluma · soluğu sıkıştı · at koşu ya da ürkme yüzünden şişip soluksuz kaldı · soluğu yükselip tıkanmış
  ربا فلان أي أصابه نفس في جوفه ودابة بها ربو (ayn)؛ أصابه ربو من مشي أو عدو إذا علت أنفاسه (jamhara)؛ الربو النفس العالي، وربا الفرس إذا انتفخ من عدو أو فزع (sihah)؛ أخذها الربو وهو البهر (tahdhib)؛ الربو الانبهار سمي بذلك تصورا لتصعده (mufradat)
- **B005** besleyip büyütmek ve yetişmek — onu besleyip büyüttü · onların arasında yetişti · çocuğu besleyip büyüttü, çocuk gelişti
  ربيته وتربيته أي غذوته (ayn)؛ ربوت في بني فلان وربيت أي نشأت فيهم، وربيته تربية وتربيته أي غذوته، هذا لكل ما ينمي كالولد والزرع (sihah)؛ ربيت الولد فربا من هذا (mufradat)
- **B006** uyluk kökü ve iç yanlardaki iki çıkıntılı et parçası — uyluk kökü veya kasık eti · uyluk köklerinin iç yanlarındaki iki çıkıntılı et parçası
  الأربية أصل الفخذ، وهما أربيتان (sihah)؛ الأربيتان لحمتان ناتئتان في أصول الفخذين من باطن (mufradat)
- **B007** baba tarafından yakın hane halkının arasına gelmek [kalıp] — kendi topluluğundaki baba tarafından yakın hane halkının arasına geldi
  جاء فلان في أربية قومه، أي في أهل بيته من بني الأعمام ونحوهم، ولا تكون الأربية من غيرهم (sihah)

## ع ل م (root_001040): 1:2 ٱلْعَٰلَمِينَ

- **B001** bilme ve gerçeğini kavrama — bilgi; bir şeyi gerçeğiyle kavrama · bir şeyi bilmek ve tanımak · haberinden haberdar olmak · bildirmek, haberdar etmek · öğretmek, öğrenmesini sağlamak · öğrenmek, kavramaya yönelmek · bilmek; buyrukta bil ki · bilgi yarışında yenmek · bilen ve bildiğine göre davranan kişi · bilgili, bilgi sahibi · çok bilgili, çok bilen · son derece bilgili kişi
  العلم نقيض الجهل (maqayis;ayn;tahdhib)؛ علمت الشيء عرفته (sihah;tahdhib)؛ إدراك الشيء بحقيقته (mufradat)؛ ما علمت بخبرك أي ما شعرت به (ayn;tahdhib)؛ أعلمته بكذا وعلمته تعليما (ayn)؛ التعليم تنبيه النفس لتصور المعاني (mufradat)؛ تعلم بمعنى اعلم (maqayis;sihah;tahdhib)؛ عالمت الرجل فعلمته (sihah;tahdhib)
- **B002** ayırt edici ve yol gösterici işaret — ayırt edici işaret · bayrak, sancak · yol gösteren belirgin dağ · kumaşın kenar işareti veya deseni · yol gösteren iz veya belirti · savaşta kendine ayırt edici işaret takmak · kumaşı işaretlemek · işaret olarak kullanılan kına · sarığı tanıtıcı bir biçimde sarmak · tanınmış ve öne çıkan kişi · son saatin yaklaştığını gösteren belirti
  أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره (maqayis)؛ العلامة وهي معروفة (maqayis)؛ العلم الراية والجمع أعلام (maqayis;sihah;tahdhib)؛ العلم الجبل الطويل والجميع الأعلام (ayn)؛ العلم الجبل (sihah;mufradat)؛ المعلم الأثر يستدل به على الطريق (sihah;tahdhib)؛ علم الثوب ورقمه في أطرافه (sihah;tahdhib;mufradat)؛ أعلم الفارس إذا كانت له علامة في الحرب (maqayis;sihah;tahdhib)؛ العلام الحناء (maqayis;sihah;tahdhib;mufradat)؛ علمت عمتي أعلمها علما (tahdhib)
- **B003** evren ve bütün yaratılmışlar — evren veya yaratılmışlar bütünü · bütün yaratıklar veya varlık sınıfları · evrenler, varlık dünyaları
  العالمون كل جنس من الخلق فهو في نفسه معلم وعلم (maqayis)؛ العالم الخلق والجمع العوالم (sihah)؛ العالمين رب الجن والإنس ورب الخلق كلهم (tahdhib)؛ العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به (mufradat)؛ أصناف الخلائق (mufradat)
- **B004** üst dudak yarığı — üst dudaktaki yarık · üst dudağı yarık kişi veya deve · üst dudağını yarmak
  العلم الشق في الشفة العليا والرجل أعلم (maqayis)؛ الأعلم الذي انشقت شفته العليا (ayn)؛ علم الرجل يعلم علما إذا صار أعلم وهو المشقوق الشفة العليا (sihah)؛ علمت الرجل أعلمه علما إذا شققت شفته العليا (tahdhib)؛ البعير يقال له أعلم لعلم في مشفره الأعلى (tahdhib)؛ الشق في الشفة العليا علم (mufradat)
- **B005** deniz ya da suyu bol kuyu — deniz · suyu bol kuyu
  العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء (maqayis)؛ العيلم الركية الكثيرة الماء (sihah)؛ العيلم البئر الكثيرة الماء (tahdhib)
- **B006** doğan veya atmaca türü yırtıcı kuş — doğan veya atmaca · çevik ve zeki adam
  العلام الصقر؛ العلامي الرجل الخفيف الذكي مأخوذ من العلام؛ العلام الباشق (tahdhib)
- **B007** erkek sırtlan — erkek sırtlan
  العيلام الذكر من الضباع (sihah)؛ العيلام الضبعان وهو ذكر الضباع (tahdhib)

## م ل ك (root_001444): 1:4 مَٰلِكِ

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

## ي و م (root_001700): 1:4 يَوْمِ

- **B001** güneşin doğuşundan batışına kadarki gün — güneşin doğuşundan batışına kadarki gün · bu anlamdaki günlerin çoğulu · gün gün veya gündelik esasa göre yapılan işlem
  اليوم: الواحد من الأيام (maqayis)؛ اليوم مقداره من طلوع الشمس إلى غروبها (ayn;tahdhib)؛ اليوم معروف والجمع أيام (sihah)؛ اليوم يعبر به عن وقت طلوع الشمس إلى غروبها (mufradat)
- **B002** herhangi bir zaman dilimi; bağlama göre devir — herhangi bir zaman dilimi; bağlama göre devir · iki devri veya bollukla sıkıntı, cömertlikle savaş gibi iki karşıt hali
  مدة من الزمان أي مدة كانت (mufradat)؛ اليوم ها هنا بمعنى الدهر (tahdhib)؛ شر أيام دهرها (tahdhib)
- **B003** büyük olayın yaşandığı çetin gün veya olay — büyük olay, olayın gerçekleştiği kritik gün veya çetin gün · çok çetin gün veya savaş günü · bilinen günlerde gerçekleşmiş olaylar · çok çetin gün · kötülüğü insanlar üzerinde uzun süren çetin gün · kötülüğü insanlar üzerinde uzun süren çetin gün
  يستعيرونه في الأمر العظيم ويقولون نعم فلان في اليوم إذا نزل (maqayis)؛ اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت (ayn;tahdhib)؛ الشدة باليوم (sihah)؛ اليوم الشديد: يوم ذو أيام (ayn;tahdhib)؛ الأيام في معنى الوقائع (tahdhib)
- **B004** Tanrı'nın nimet ve ibret verici işleriyle anılan günler [kalıp] — Tanrı'nın nimet, bağışlama ve cezalandırma olaylarıyla anılan günleri
  وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب، وبالعفو عن آخرين (tahdhib)؛ جاءت الأيام بمعنى الوقائع والنعم (tahdhib)؛ أيامه: نعمه (tahdhib)؛ إضافة الأيام إلى الله تشريف لأمرها لما أفاض الله عليهم من نعمه فيها (mufradat)
- **B005** bağlamda işaret edilen o gün veya o sırada — o gün; o sırada
  يركب يوم مع إذ، فيقال: يومئذ؛ وربما يعرب ويبنى، وإذا بني فللإضافة إلى إذ (mufradat)

## د ي ن (root_000504): 1:4 ٱلدِّينِ

- **B001** boyun eğerek uyma ve buna dayalı inanç düzeni — boyun eğme, kulluk ve inanç düzeni · ona boyun eğdi ve buyruğuna uydu · gerçek inanç yolu · hükümdarın buyruğu ya da yargısı
  أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل (maqayis)؛ فالدين الطاعة (maqayis;sihah)؛ الدين لله طاعته والتعبد له (tahdhib)؛ الدين كالملة اعتبارا بالطاعة والانقياد للشريعة (mufradat)
- **B002** yargılayıp hesap görerek karşılığını verme — hesap, yargı ve yapılanın karşılığı · hesap ve karşılık günü · hesaba çekilip karşılığı verilecek olanlar · yargılayan ve karşılığını veren · hükümdarın buyruğu ya da yargısı · kendini alçalttı ya da hesaba çekti
  يوم الدين أي يوم الحكم والحساب والجزاء (maqayis)؛ الدين الجزاء والمكافأة (sihah)؛ الدين الحساب ومنه مالك يوم الدين ومالك يوم الجزاء (tahdhib)؛ غير مدينين أي غير مجزيين (mufradat)
- **B003** borç alıp verme ve vadeli ödeme ilişkisi — borç ve vadeli ödeme yükümlülüğü · onunla borç alıp verme işlemi yaptı · ona ödünç verdi · ödünç aldı ve borçlandı · borçlu veya çok borçlanmış kişi · onu vadeli olarak sattım
  الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء (maqayis)؛ الدين واحد الديون وتداينوا تبايعوا بالدين (sihah)؛ دنت الرجل أقرضته وأدنت الرجل إذا أقرضته (tahdhib)؛ التداين والمداينة دفع الدين (mufradat)
- **B004** zorla alçaltıp egemenliği altına alma — onu alçalttı, boyunduruk altına aldı ve köleleştirdi · topluluğu alçalttım ve köleleştirdim · onu mülk edindim veya buyruğum altına aldım · köleleştirilmiş erkek · köleleştirilmiş kadın · kendini alçalttı ya da hesaba çekti · kalbini alçaltan şey; ayrıca alışkanlık, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz
  العبد مدين كأنهما أذلهما العمل ويا دين قلبك أي أذل (maqayis)؛ دانه دينا أي أذله واستعبده ودينته ملكته (sihah)؛ غير مدينين غير مملوكين ودنت القوم أدينهم إذا أذللتهم (tahdhib)؛ المدين والمدينة العبد والأمة (mufradat)
- **B005** alışılmış davranış ve öteden beri bilinen hal — alışkanlık, olağan iş ve öteden beri bilinen hal · kalbinin alışkanlığı; ayrıca alçaltma, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz
  العادة يقال لها دين (maqayis)؛ الدين بالكسر العادة والشأن (sihah)؛ الدين أيضا العادة (tahdhib)؛ الحال والأمر الذي تعهده (maqayis)
- **B006** kent — kent; yöneticilerin buyruğuna uyulan yer olarak açıklanan büyük yerleşim
  المدينة كأنها مفعلة سميت بذلك لأنها تقام فيها طاعة ذوي الأمر (maqayis)؛ ومنه سمى المصر مدينة (sihah)؛ جعل بعضهم المدينة من هذا الباب (mufradat)
- **B007** kişiyi sözüne ve vicdani sorumluluğuna göre değerlendirme — onu vicdani yükümlülüğüyle baş başa bıraktı · yargıda veya Tanrı'yla arasındaki konuda sözünü doğru kabul etti · yeminini kendi niyetine göre değerlendirdi
  دينت الرجل تديينا إذا وكلته إلى دينه (sihah)؛ دينت الرجل في القضاء وفيما بينه وبين الله أي صدقته (tahdhib)؛ دينت الحالف أي نويته فيما حلف وهو التديين (tahdhib)

## ع ب د (root_000973): 1:5 نَعْبُدُ

- **B001** özgür olmayan, sahip olunan kişi — özgür olmayan, sahip olunan kişi · köleler · köle doğmuş veya kuşaklar boyunca köle kalmış kişiler
  العبد وهو المملوك (maqayis)؛ العبد المملوك وجمعه عبيد (ayn)؛ العبد ضد الحر (jamhara)؛ العبد خلاف الحر والجمع عبيد (sihah)؛ العبيد مماليك (tahdhib)؛ عبد بحكم الشرع الإنسان الذي يصح بيعه وابتياعه (mufradat)
- **B002** Tanrı'ya ait sayılan insan veya topluluk — Tanrı'nın kulu · Tanrı'nın kulları veya ona bağlı topluluk · Tanrı'ya ait sayılan bütün kullar
  تفرقة ما بين عباد الله والعبيد المملوكين (maqayis)؛ العبد الإنسان حرا أو رقيقا هو عبد الله (ayn)؛ فادخلي في عبادي أي في حزبي (sihah)؛ عبد بالإيجاد وذلك ليس إلا لله (mufradat)
- **B003** boyun eğerek itaat ve tapınma — Tanrı'ya boyun eğerek tapındı · boyun eğerek tapınma · kendini tapınmaya verme · sahte tanrısal güce boyun eğip itaat etti · sahte tanrısal güçlere veya putlara tapan topluluk
  عبد يعبد عبادة فلا يقال إلا لمن يعبد الله (maqayis;ayn)؛ تعبدت للرجل إذا تذللت له (jamhara)؛ العبادة الطاعة والتعبد التنسك (sihah)؛ إياك نعبد إياك نطيع الطاعة التي نخضع معها (tahdhib)؛ العبودية إظهار التذلل والعبادة غاية التذلل (mufradat)
- **B004** köleleştirmek veya köle gibi boyunduruk altına almak — onu köleleştirdi · kişiyi ezip köleleştirdi; topluluğu köle edindi · onu köle durumuna getirdi · özgür olsa da onu köle gibi boyunduruk altına aldı
  استعبدت فلانا اتخذته عبدا (maqayis;ayn)؛ عبدت الرجل إذا ذللته وعبدت القوم اتخذتهم عبيدا (jamhara)؛ التعبيد الاستعباد (sihah)؛ عبدت العبيد وأعبدتهم أي صيرتهم عبيدا (tahdhib)؛ عبدت فلانا إذا ذللته وإذا اتخذته عبدا (mufradat)
- **B005** düzleşmiş yol, katranlanmış deve veya kaplanmış gemi — çok geçilerek düzleşmiş yol · derisi baştan başa katranlanmış ve uysallaştırılmış deve · katranla kaplanmış gemi
  الطريق المعبد وهو المسلوك المذلل (maqayis)؛ طريق معبد أي مذلل (jamhara;mufradat)؛ البعير المعبد المهنوء بالقطران المذلل (maqayis;sihah)؛ المعبدة السفينة المقيرة (sihah;tahdhib)؛ المعبد من الإبل الذي عم جلده بالقطران (tahdhib)
- **B006** saygı gösterilip hizmet edilen kişi — saygı gösterilen, yüceltilen ve hizmet edilen kişi
  المعبد المكرم والمعظم كأنه يعبد (jamhara)؛ المعبد أي معظما مخدوما (tahdhib)
- **B007** güç, sağlamlık ve dayanıklılık — güç, sağlamlık ve dayanıklılık · güçlü ve semiz dişi deve · kumaşının hiç dayanıklılığı yok
  العبدة وهي القوة والصلابة (maqayis)؛ ناقة ذات عبدة أي ذات قوة وسمن وما لثوبك عبدة أي قوة (sihah)؛ العبدة البقاء وقيل الشدة (tahdhib)
- **B008** incinmiş gurur, öfke veya kederli iç duygulanım — incinmiş gurur, öfke, keder veya iç sıkıntısı · gururu incindiği için sustu
  العبد مثل الأنف والحمية (maqayis)؛ العبد الأنفة وعبدت فصمت أي أنفت فسكت (jamhara)؛ العبد بالتحريك الغضب والأنف والاسم العبدة (sihah)؛ العبد الأنف والحمية ويقال عبد عليه أي غضب والعبد الحزن والوجد (tahdhib)
- **B009** gecikmeden yapmak veya koşuda biraz hızlanmak [kalıp] — yapmakta gecikmedi · koşarken biraz hızlandı
  ما عبد أن فعل ذاك أي ما لبث (sihah;tahdhib)؛ عبد يعدو إذا أسرع بعض الإسراع (tahdhib)
- **B010** her yana dağılmış kümeler, nesneler veya yollar — her yana dağılmış insan kümeleri, nesneler veya yollar
  العباديد الفرق من الناس الذاهبون في كل وجه وكذلك العبابيد (sihah)؛ العباديد والعبابيد الأطراف البعيدة والأشياء المتفرقة والطرق المختلفة (tahdhib)
- **B011** bineği yüzünden yolda kalma veya güçlükle direnen deve — bineği yorulduğu, zarar gördüğü veya kaybolduğu için yolda kaldı · insanlara güçlük çıkararak direnen deve
  أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت (sihah)؛ أعبد به إذا ذهبت راحلته وكذلك أبدع به (tahdhib)؛ بعير متعبد ومتأبد إذا امتنع على الناس صعوبة (tahdhib)
- **B012** güzel koku maddesi ezme taşı — güzel koku maddelerini ezme taşı
  العبدة صلاءة الطيب (jamhara)

## ع و ن (root_001064): 1:5 نَسْتَعِينُ

- **B001** yardım, destek ve dayanışma — yardım, destek veya işe yarayan yardımcı şey · yardım etme, destek sağlama · yardım etti, destek oldu · yardımlaştı veya destek verdi · birinden yardım istedi · birbirine yardım etti, dayanıştı · çok yardımsever, sıkça yardım eden · yardım, destek · yardım anlamındaki tekil biçim veya yardım sözünün çoğulu
  كل شيء استعنت به أو أعانك فهو عونك (ayn); العون الظهيرة على الأمر والمعونة الإعانة واستعنت بفلان فأعانني وعاونني وتعاون القوم (sihah); كل شيء أعانك فهو عون لك وأعنته إعانة واستعنت به وعاونته وقد تعاونا (tahdhib); العون المعاونة والمظاهرة والتعاون التظاهر والاستعانة طلب العون (mufradat)
- **B002** yaşça orta evrede olan — yaşça orta evrede olan · ne genç ne yaşlı sığır · orta yaşlı veya evlenmiş kadın · orta yaşlı at · orta yaşta olanlar
  العوان البقرة النصف في سنها ويقال للمرأة النصف عوان (ayn); العوان النصف في سنها من كل شيء وبقرة عوان لا فارض مسنة ولا بكر صغيرة (sihah); العوان النصف التي بين الفارض وهي المسنة وبين البكر وهي الصغيرة ويقال فرس عوان وخيل عون (tahdhib); العوان المتوسط بين السنين وجعل كناية عن المسنة من النساء (mufradat)
- **B003** yinelenmiş veya öncülü olan savaş [kalıp] — daha önce yaşanmış ya da yinelenmiş savaş
  الحرب العوان التي كانت قبلها حرب بكر (ayn); العوان من الحروب التي قوتل فيها مرة بعد مرة (sihah); استعير للحرب التي قد تكررت وقدمت (mufradat)
- **B004** yaşlı hurma ağacı — yaşlı hurma ağacı
  وقيل العوانة للنخلة القديمة (mufradat)
- **B005** bedensel denge ve güç olgunluğu [kalıp] — bedeni dengeli kadın veya yaş almış, etli kadın · gücü ile yaşı birbirine yetişmiş yük atı
  المتعاونة من النساء التي طعنت في السن ولا تكون إلا مع كثرة اللحم (sihah); امرأة متعاونة إذا اعتدل خلقها فلم يبد حجمها وبرذون متعاون إذا لحقت قوته وسنه (tahdhib)
- **B006** yaban eşeği sürüsü — yaban eşeği sürüsü · yaban eşeği sürüleri · yaban eşeği sürüleri
  العانة القطيع من حمر الوحش وتجمع على عانات وعون (ayn); العانة القطيع من حمر الوحش والجمع عون (sihah); العانة قطيع من حمر الوحش وجمع على عانات وعون (mufradat)
- **B007** erkekte kasık kılları — erkeğin kasık kılları · kasık kıllarını küçülterek söyleyen biçim · kasık kıllarını tıraş etti
  عانة الرجل إسبه من الشعر على فرجه وتصغيره عوينة (ayn); العانة شعر الركب واستعان فلان حلق عانته (sihah); عانة الرجل شعره النابت على فرجه وتصغيره عوينة (mufradat)
- **B008** bir yer adı ve o yere bağlanan şarap adı — şarabıyla ilişkilendirilen bir yer veya köy adı · aynı yer adıyla ilişkili değişken ad biçimi · söz konusu yerden geldiği belirtilen şarap
  عانات موضع من ناحية الجزيرة تنسب إليه الخمر العانية (ayn); عانة قرية على الفرات تنسب إليها الخمر فيقال عانية (sihah)

## ECHO ع ي ن (root_001069): for 1:5 نَسْتَعِينُ: withheld observed target; not identity

- **B001** gören göz — göz, görme organı
  العين الناظرة لكل ذي بصر (maqayis;ayn); العين: حاسة الرؤية (sihah); العين: التي يبصر بها الناظر (tahdhib); العين الجارحة (mufradat)
- **B002** gözle görüp kesin biçimde tanıma — gözle görerek, yüz yüze · yüz yüze görerek · bilerek, görüp emin olarak · gördükten sonra ayrıca iz aramam
  رأيت الشيء عيانا أي معاينة (maqayis); لا أطلب أثرا بعد عين أي بعد معاينة (ayn;sihah;tahdhib); عيانا أي مواجهة (tahdhib); فعلت ذلك عمد عين (sihah)
- **B003** koruyup gözetme — korumam altında, özenle gözeterek · gözümün önünde, korumam altında · gözetimimiz ve korumamız altında
  أنت على عيني، في الإكرام والحفظ جميعا (sihah); على عيني قصدت زيدا يريدون الإشفاق (tahdhib); فلان بعيني أي أحفظه وأراعيه (mufradat); بحيث نرى ونحفظ (mufradat)
- **B004** kötü bakışla zarar verme — gözüyle zarar verdi · gözü değen kimse · göz değmiş kimse · gözü sık değen kimse
  عنت الرجل إذا أصبته بعينك (maqayis); عنت الشيء بعينه فأنا أعينه عينا وهو معيون (ayn); عنت الرجل: أصبته بعينى، فأنا عائن (sihah); عان الرجل فلانا يعينه عينا إذا ما أصابه بالعين (tahdhib); عنته: أصبته بعيني (mufradat)
- **B005** haber toplayan gizli gözcü — gizli gözcü veya öncü · gizli gözcü · bizim için çevreyi yoklayıp haber getirdi
  العين الذي تبعثه يتجسس الخبر (maqayis); العين الذي تبعثه لتجسس الخبر (ayn); العين: الديدبان، والجاسوس (sihah); بعثنا عينا أي طليعة (tahdhib); قيل للمتجسس عين (mufradat)
- **B006** akan su kaynağı — akan su kaynağı · göz önünde akan su · su aktı veya kaynağı ortaya çıktı
  العين الجارية النابعة من عيون الماء (maqayis); عين الماء (ayn;sihah); العين الينبوع الذي ينبع من الأرض ويجري (tahdhib); لمنبع الماء: عين (mufradat); ماء معين أي ظاهر للعيون (mufradat)
- **B007** su sızdıran ince delik — su kabındaki ince veya delik sızıntı yeri · incelip su tutamaz olmuş su kabı · dikiş delikleri kapansın diye kaba su döktü
  عين السقاء (maqayis); تعين السقاء أي بلي ورق منه مواضع (ayn); بالجلد عين، وهي دوائر رقيقة (sihah); سقاء عين إذا رق فلم يمسك الماء (tahdhib); الثقب في المزادة تشبيها بها في الهيئة وفي سيلان الماء (mufradat)
- **B008** güneş yuvarlağı — güneşin gövdesi veya yuvarlağı
  عين الشمس مشبه بعين الإنسان (maqayis); عين الشمس صيخدها (ayn); العين: عين الشمس (sihah); طلعت العين وغابت العين، أي الشمس (tahdhib)
- **B009** göze benzer çukur, yer veya eğim — dizin önündeki çukur · kuyunun kaynak yeri veya çukuru · terazideki küçük eğim veya dengesizlik · yayda merminin yerleştiği bölüm
  عين الركية وهما عينان كأنهما نقرتان في مقدمها (maqayis); عين الركبة (ayn;sihah;tahdhib); في الميزان عين إذا رجحت إحدى كفتيه (tahdhib); عين القوس التي يقع فيها البندق (tahdhib)
- **B010** belirli yönden gelen bulut veya dinmeyen yağmur — kıblenin sağından gelen bulut · günlerce dinmeyen yağmur
  العين السحاب ما جاء من ناحية القبلة (maqayis); العين من السحاب ما أقبل عن يمين القبلة (ayn); العين: ما عن يمين قبلة العراق (sihah;tahdhib); العين: مطر أيام لا يقلع (sihah;tahdhib)
- **B011** hemen elde bulunan para — elde hazır bulunan para · altın para, eldeki para
  العين وهو المال العتيد الحاضر (maqayis); عين غير دين أي مال حاضر (ayn); العين: الدينار؛ العين: المال الناض (sihah); العين: النقد (tahdhib); قيل للذهب: عين (mufradat)
- **B012** ertelenmiş ödemeli alımla para edinme — önceden verilen para veya para sağlamak için yapılan satış · malı ödemesi ertelenmiş olarak satın aldı
  العينة السلف (maqayis;ayn;sihah); تعين فلان من فلان عينة (ayn); اعتان الرجل، إذا اشترى الشئ بنسيئة (sihah); عين التاجر يعين تعيينا وعينة قبيحة (tahdhib); سميت عينة لحصول النقد لطالب العينة (tahdhib)
- **B013** şeyin bizzat kendisi ve belirlenmiş olanı — şeyin bizzat kendisi · tam kendisi, yerine başkası değil · bir şeyi topluluk içinden belirleyip ayırma
  عين الشيء نفسه (maqayis;sihah;tahdhib); خذ درهمك بعينه (maqayis); تعيين الشئ: تخصيصه من الجملة (sihah); دراهمك بأعيانها وهي أعيان دراهمك (tahdhib); ذات الشيء (mufradat)
- **B014** bir şeyin en iyi ve seçkin bölümü — bir şeyin en iyi ve seçkin bölümü
  عينة كل شيء خياره (maqayis); العينة: خيار الشيء (tahdhib); عين الشئ: خياره (sihah); عينة المال أيضا: خياره (sihah); العين تشبيها بها في كونها أفضل الجواهر (mufradat)
- **B015** önde gelen kişiler veya anne baba bir kardeşler — topluluğun önde gelen seçkin kişileri · anne baba bir kardeşler veya aynı kadının çocukları
  أعيان القوم أي أشرافهم (maqayis;sihah;tahdhib); هؤلاء أعيان إخوتهم (maqayis); الأعيان: الأخوة بنو أب واحد وأم واحدة (sihah); أعيان بني الأم يتوارثون (tahdhib); أعيان القوم لأفاضلهم، وأعيان الإخوة (mufradat)
- **B016** geniş ve güzel gözlü olma — geniş ve güzel gözlü · gözlerinin güzelliğiyle adlandırılan yaban sığırı · geniş ve güzel gözlü kadınlar · göz benzeri küçük kare desenli kumaş
  توصف البقرة بسعة العين فيقال بقرة عيناء (maqayis); العين بقر الوحش (ayn;sihah;tahdhib); العين عظم سواد العين في سعتها (ayn); رجل أعين واسع العين (sihah;tahdhib); قاصرات الطرف عين؛ وحور عين (mufradat)
- **B017** kimse veya orada bulunan insanlar — orada hiç kimse yok · ev halkı veya orada bulunanlar · bir topluluk içinde
  ما بها عين متحركة الياء تريد أحدا له عين (maqayis); ما بها عائن، وكذلك ما بها عين، أي أحد (sihah); العين، بالتحريك: أهل الدار (sihah); العين: أهل الدار (tahdhib); جاء فلان في عين، أي في جماعة (sihah)

## ه د ي (root_001583): 1:6 ٱهْدِنَا

- **B001** doğru yolu gösterme ve doğruya yönelme — doğru yol, doğruyu gösterme ve açıklama · ona yolu gösterip tanıttım · doğru yolu kabul edip buldu · yol gösteren, doğruya çağıran kimse
  الهدى نقيض الضلالة؛ هدي فاهتدى (ayn;tahdhib)؛ الهدى الرشاد والدلالة؛ هداه الله للدين هدى؛ أولم يبين لهم؛ هديته الطريق والبيت هداية أي عرفته (sihah)؛ الهدى البيان وإخراج شيء إلى شيء والطاعة والورع؛ دله على الطريق (tahdhib)؛ الهداية دلالة بلطف؛ تعريف الطرق؛ التوفيق (mufradat)؛ التقدم للإرشاد؛ هديته الطريق هداية؛ الهدى خلاف الضلالة (maqayis)
- **B002** yön, izlenen yol ve tutum — işin yönü, doğrultusu ve amacı · bir kimsenin gidişi, tutumu ve yöntemi · onun benzeri veya onu yeniden yapma
  خذ في هديتك أي فيما كنت فيه من الحديث أو العمل ولا تعدل عنه؛ هدية أمره وسيرته؛ هدى هدي فلان أي سار سيرته (sihah)؛ هدية أمره أي جهة أمره؛ هديت به أي قصدت به؛ هديه أي سمته؛ ليس لهذا الأمر هدية ولا قبلة ولا دبرة ولا وجهة؛ هدياها أي مثلها أو أعاودك (tahdhib)؛ هدية فلان وهديه أي طريقته (mufradat)؛ نظر فلان هدي أمره أي جهته؛ ما أحسن هديته أي هديه؛ رميت بآخر هدياه أي قصده (maqayis)
- **B003** bir şeyin ilk veya öndeki bölümü — bir şeyin ilki veya öndeki bölümü · atların boyunları ya da ilk sırası; yaban hayvanlarının öncüleri · okun ucu ve koyunun boynu
  الهادي من كل شيء أوله؛ هوادي الخيل أعناقها أو أول رعيل؛ العصا هاديا لأنها تتقدمه؛ الدليل يسمى هاديا لتقدمه (ayn)؛ هادي السهم نصله؛ الهادي العنق؛ هوادي الخيل أعناقها أو أول رعيل؛ الهاديات أوائل الوحش (sihah)؛ الهادية من كل شيء أوله وما تقدم منه؛ هادية الشاة الرقبة؛ هوادي الخيل أعناقها أو أول رعيل؛ هاديات الوحش أوائلها (tahdhib)؛ هوادي الوحش متقدماتها الهادية لغيرها (mufradat)؛ كل متقدم لذلك هاد؛ هوادي الخيل أعناقها؛ هاديها أول رعيل؛ الهادية العصا لأنها تتقدم ممسكها (maqayis)
- **B004** incelik göstergesi armağan verme — yakınlık ve incelik göstergesi armağan · armağan gönderdi veya verdi · karşılıklı armağanlaşma · armağanın sunulduğu tabak · sık sık armağan veren kimse
  الهدية ما أهديت إلى ذي مودة من بر (ayn)؛ الهدية واحدة الهدايا؛ أهديت له وإليه؛ المهدى ما يهدى فيه؛ التهادي أن يهدي بعضهم إلى بعض؛ المهداء الذي من عادته أن يهدي (sihah)؛ أهديت الهدية إهداء؛ امرأة مهداء؛ المهدى الطبق الذي يهدى عليه (tahdhib)؛ الهدية مختصة باللطف؛ المهدى الطبق؛ المهداء من يكثر إهداء الهدية (mufradat)؛ الهدية ما أهديت من لطف إلى ذي مودة؛ المهدي الطبق تهدى عليه (maqayis)
- **B005** kutsal yere adanan hayvan, mal veya eşya — kutsal bölgeye adanan hayvan, mal veya eşya · adanmış sunu adından genişleyen deve adı
  الهدي والهدي ما أهديت إلى مكة؛ كل شيء تهديه من مال أو متاع فهو هدي (ayn)؛ الهدي ما يهدى إلى الحرم من النعم؛ مالى هدي؛ حتى يبلغ الهدى محله (sihah)؛ أهديت الهدي إلى بيت الله؛ الهدي خفيف وعليه هدية أي بدنة؛ ما يهدى إلى مكة من النعم وغيره من مال أو متاع؛ العرب تسمي الإبل هديا (tahdhib)؛ الهدي مختص بما يهدى إلى البيت؛ فما استيسر من الهدي؛ هديا بالغ الكعبة (mufradat)؛ الهدي والهدي ما أهدي من النعم إلى الحرم قربة إلى الله تعالى (maqayis)
- **B006** gelini eşinin yanına götürme — gelini eşinin yanına götürdü · gelinin eşinin yanına götürülmesi · eşine götürülen gelin
  الهداء مصدر قولك هديت المرأة إلى زوجها؛ وهي مهدية وهدي (sihah)؛ هديت العروس فأنا أهديها هداء؛ أهدى الرجل امرأته جمعها إليه وضمها؛ المرأة سميت هديا لأنها كالأسيرة عند زوجها أو لأنها تهدى إلى زوجها (tahdhib)؛ الهدي يقال في العروس؛ هديت العروس إلى زوجها (mufradat)؛ الهدى العروس وقد هديت إلى بعلها هداء (maqayis)
- **B007** dokunulmaz sığınmacı; kimi açıklamalarda tutsak — dokunulmaz sığınmacı; kimi açıklamalarda tutsak
  الرجل الذي له حرمة كحرمة هدي البيت؛ يقال للأسير أيضا هدي (sihah)؛ الهدي الرجل ذو الحرمة وهو أن يأتي القوم يستجيرهم أو يأخذ منهم عهدا؛ يقال للأسير أيضا الهدي (tahdhib)؛ وقيل الهدي الأسير (maqayis)
- **B008** sallanarak, gerektiğinde başkalarına dayanarak yürüme — güçsüzlükten iki kişiye dayanarak yürümek · yürürken sağa sola sallandı
  التهادي مشي في تمايل يمينا وشمالا كمشي النساء والإبل الثقال (ayn)؛ يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله؛ المرأة إذا تمايلت في مشيتها قيل تهادى (sihah)؛ يهادى بين اثنين معناه يعتمد عليهما من ضعفه وتمايله؛ هي تهادى إذا تمايلت في مشيها (tahdhib)؛ يهادي بين اثنين إذا مشى بينهما معتمدا عليهما؛ تهادت المرأة إذا مشت مشي الهدي (mufradat)؛ جاء فلان يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما (maqayis)
- **B009** bön, güçsüz ve ağır kimse — bön, güçsüz, ağır ve uyuşuk adam
  الهداء الرجل البليد الضعيف (ayn)؛ رجل هداء وهدان للثقيل الوخم (tahdhib)
- **B010** sakin, ölçülü ve düzgün ilerleyiş — sakinlik ve güzel, telaşsız tutum
  الهدي السكون؛ ما هدى هدي مهزوم؛ لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن (ayn)؛ الهدي السكون؛ لم يسرع إسراع المنهزم ولكن على سكون وحسن هدي (tahdhib)
- **B011** övgü veya yergi şiiri sunma ve şiirle yergileşme — birine övgü veya yergi şiiri sunma · şiirle karşılıklı yergileşme
  الإهداء أن تهدي إلى إنسان مديحا أو هجاء شعرا (ayn)؛ هاداني فلان الشعر وهاديته أي هاجاني وهاجيته (tahdhib)

## ECHO ه د د (root_001580): for 1:6 ٱهْدِنَا: withheld observed target; not identity

- **B001** agir kirip yikma — kirip yikmak, sarsip bozmak · agir yikim ve kirilma · kirilip yikilmak · bir felaketin kisiyi sarsip gucunu kirmasi · yer cokmesi ya da yikima benzer agir olay
  أصل صحيح يدل على كسر وهضم وهدم (maqayis)؛ الهد الهدم الشديد (ayn;tahdhib)؛ هددت الحائط إذا هدمته (jamhara)؛ هد البناء يهده هدا كسره وضعضعه (sihah;tahdhib)؛ انهد الجبل أي انكسر (sihah)؛ الهدة الخسوف والهد الهدم (tahdhib)؛ هد ركني إذا بلغ منه وكسره (tahdhib)
- **B002** zayif ve korkak kisi — zayif veya korkak adam · korkak veya zayif adam · korkak adam · korkak topluluk · birini zayif saymak · zayif olmayan
  الهد من الرجال الضعيف كأنه هد (maqayis)؛ رجل هد جبان (jamhara)؛ رجل هد وأهد بمعنى الجبن والضعف (jamhara)؛ الهد الرجل الضعيف (sihah;tahdhib)؛ الهد بالكسر الجبان الضعيف (sihah;tahdhib)؛ استهددت فلانا أي استضعفته (tahdhib)
- **B003** cömert ve guclu kisi — cömert, degerli veya guclu adam · adam gucu ve dayanikliligiyla ovulmek · adami dayanikli diye ovmek
  الهد من الرجال الجواد الكريم (maqayis;tahdhib)؛ الهد الكريم الهاد لماله (maqayis)؛ فلان يهد إذا أثني عليه بالجلد والقوة (sihah)؛ لهد الرجل إذا أثني عليه بالجلد والشدة (tahdhib)؛ هد الرجل جلد الرجل (tahdhib)
- **B004** siddetli ugultu — duvar, kose veya dag dusmesinin siddetli sesi · deniz tarafindan duyulan siddetli ugultu · gok gurultusu · ses ve ugultu · kumru veya erkek devenin gurleyis ugultusu
  الهدة صوت وقع الحائط (maqayis;sihah)؛ الهدة صوت تسمعه من سقوط ركن أو ناحية جبل (ayn;tahdhib)؛ الهاد صوت شديد يسمعه أهل السواحل (ayn;sihah;tahdhib)؛ ما سمعنا العام هادة أي رعدا (jamhara)؛ هدهد الحمام صوت (maqayis)؛ الفحل يهدهد في هديره (ayn;sihah;tahdhib)؛ الهديد والغديد الصوت (tahdhib)
- **B005** ibibik kusu — ibibik kusu · ibibik veya guvercine benzetilen kus adlari
  الهدهد معروف (maqayis;tahdhib)؛ الهدهد طائر والهداهد مثله (sihah)؛ الهداهد طائر يشبه الحمام (tahdhib)؛ هداهد تصغير هدهد (tahdhib)
- **B006** uyutmak icin sallama [kalıp] — cocugu uyusun diye sallamak
  هدهدت المرأة ابنها حركته لينام (maqayis;sihah)؛ الهدهدة تحريك الأم ولدها لينام (tahdhib)؛ يهدهد الصبي (tahdhib)
- **B007** ovgu yeterlik kalibi — bir erkegi 'ona diyecek yok' anlaminda oven kalip
  مررت برجل هدك من رجل كقولهم حسبك من رجل (maqayis)؛ هدك فلان من رجل أي حسبك به (jamhara)؛ مررت برجل هدك من رجل معناه أثقلك وصف محاسنه (sihah)؛ مررت برجل هدك من رجل فهو بمعنى حسبك وهو مدح (tahdhib)
- **B008** agir basarak yurume [kalıp] — yururken yere cok sert basmak
  فلان يهد الأرض في مشيه إذا جاء يطأ وطأ شديدا (jamhara)
- **B009** sarp inisli gecit — sarp inisli tepe veya zorlu gecit
  أكمة هدود صعبة المنحدر وربما تردت الإبل منها (jamhara)؛ الهدود العقبة الشاقة (tahdhib)
- **B010** gozdagi vererek korkutma — gozdagi verme ve korkutma · korkutma ve gozdagi verme · gozdagi verme · uzaktan savrulan gozdagi
  التهديد التخويف وكذلك التهدد (sihah)؛ التهدد والتهديد والتهداد من الوعيد (tahdhib)؛ يقال للوعيد من وراء وراء الفديد والهديد (tahdhib)
- **B011** kesinlesmemis sani [kalıp] — kisinin icine kesinlesmemis bir sani gibi belirmek
  يقال يهدهد إلي كذا إذا شبه للإنسان في نفسه بالظن ما لم يثبته ولم يعقد عليه التشبيه (tahdhib)
- **B012** uzun boylu adam — uzun boylu adam
  الهديد الرجل الطويل (tahdhib)

## ص ر ط (root_000858): 1:6 ٱلصِّرَٰطَ, 1:7 صِرَٰطَ

- **B001** yol, özellikle düz yol — yol, özellikle düz yol · yol veya düz yol · yol
  الصراط والسراط والزراط: الطريق (sihah)؛ الصراط: الطريق المستقيم؛ ويقال له سراط (mufradat)؛ صرط من باب الإبدال وقد ذكر في السين وهو الطريق (maqayis 2074)؛ بعض أهل العلم يقول السراط مشتق من ذلك لأن الذاهب فيه يغيب (maqayis 1774)
- **B002** geçişte gözden kaybolmak; özellikle yiyeceği yutmak — yiyeceği boğazdan geçirip gözden kaybolacak biçimde yutmak · kolayca yutulan pelte kıvamlı tatlı · geniş boğazlı
  أصل صحيح واحد يدل على غيبة في مر وذهاب؛ سرطت الطعام إذا بلعته لأنه إذا سرط غاب؛ السرطراط على فعلال الفالوذ لأنه يسترط (maqayis 1774)؛ السرطم: الواسع الحلق، والميم فيه زائدة، وإنما هو من سرط، إذا بلع (maqayis السرطم)
- **B003** vuruşta kesip ilerleyen kılıç — vuruşta kesip ilerleyen kılıç
  والسراط السيف القاطع الماضي في الضريبة (maqayis 1774)

## ق و م (root_001273): 1:6 ٱلْمُسْتَقِيمَ

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

## ن ع م (root_001525): 1:7 أَنْعَمْتَ

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

## غ ي ر (root_001119): 1:7 غَيْرِ

- **B001** yarar sağlayıp durumunu iyileştirme — aileyi geçindiren azık ve ihtiyaç payı · aileye geçimlik ve yarar sağlama · ailesine geçimlik sağladı ve yarar dokundurdu · ona yarar sağladı ve ihtiyacını giderdi · Tanrı onlara yağmur verip durumlarını iyileştirdi · yağmur toprağı suladı · sulanmış toprak · sulanmış toprak · yük takımlarını düzeltiyorlar · devesinin yükünü indirip durumunu düzeltti · hayvanı rahatlatmak için yük takımını düzenleyen kişi
  الغِيرة بالكسر: الميرة (sihah)؛ يميرهم وينفعهم (sihah)؛ غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم (maqayis)؛ سقاهم (sihah)؛ يصلحون الرحال (sihah)؛ حط عنه رحله وأصلح من شأنه (tahdhib)
- **B002** cana karşılık ceza yerine kabul edilen kan bedeli — bana kan bedelini ödedi · kan bedeli · cana karşılık ceza yerine kabul edilen kan bedeli
  غارني الرجل إذا وداك من الدية والاسم الغِيرة (sihah)؛ الدية فإنها تسمى الغير (maqayis)؛ تقبلوا الغيرا (maqayis;sihah)
- **B003** biçimini değiştirme veya yerine başkasını koyma — şeyi değiştirdi ve öncekinden farklı hale getirdi · biçimini değiştirme veya yerine başkasını koyma · durumundan ayrılıp farklı hale geldi · yanlış olanı doğru olanla değiştirip giderdi · onunla alışverişte karşılıklı değiş tokuş yaptı · yerine konan karşılık
  الاسم من قولك غيرت الشيء فتغير (sihah)؛ تغير فلان عن حاله (tahdhib)؛ تغيير صورة الشيء دون ذاته (mufradat)؛ تبديله بغيره (mufradat)؛ يدفعون ذلك المنكر بغيره من الحق (tahdhib)؛ قود فغير إلى الدية (maqayis)؛ غايرت الرجل أي عارضته بالبيع وبادلته والغيار البدال (sihah)
- **B004** eşini veya ailesini kıskanarak koruma duygusu — eşini veya ailesini kıskanarak koruma duygusu · eşini veya ailesini kıskanıp sakındı · eşine veya ailesine karşı kıskanç ve korumacı · eşine veya ailesine karşı kıskanç erkek · eşine veya ailesine karşı kıskanç kadın · eşine veya ailesine karşı çok kıskanç kişi · eşini veya ailesini kıskanarak koruma duygusunun bir başka söylenişi
  الغَيرة بالفتح مصدر قولك غار الرجل على أهله (sihah)؛ رجل غيور وغيران وامرأة غيور وغيرى (sihah)؛ غيرة الرجل على أهله (maqayis)؛ الغار لغة في الغيرة (maqayis)
- **B005** başka olma, dışta bırakma veya olumsuzlama — başka, aynı olmayan veya aykırı · dışında, dışta bırakarak · değil, olmayan · doğru olmayan, yanlış · biri öteki olmayan iki şey · şeyler birbirinden farklılaştı
  هذا الشيء غير ذاك أي هو سواه وخلافه (maqayis)؛ غير بمعنى سوى (sihah;tahdhib)؛ يوصف بها ويستثنى (sihah)؛ يكون استثناء (tahdhib)؛ يكون غير اسما (tahdhib)؛ معنى غير معنى لا (tahdhib)؛ للنفي المجرد (mufradat)؛ بمعنى إلا (mufradat)؛ لنفي صورة من غير مادتها (mufradat)؛ متناولا لذات (mufradat)؛ الغيرين أعم من المختلفين (mufradat)؛ تغايرت الأشياء اختلف (sihah)

## غ ض ب (root_001092): 1:7 ٱلْمَغْضُوبِ

- **B001** şiddetli öfke ve öç alma yönelimi — şiddetli öfke ve öç alma isteği · ona çok öfkelenmek · öfke ve kızgınlık · onu öfkelendirmek · öfkelenmek veya öfkesini göstermek · öfkeli · öfkeli kadın veya öfkeli topluluk · öfkeli kadın · öfkeli topluluklar · çok ve şiddetli öfkelenen · çok veya çabuk öfkelenen adam · çok ve şiddetli öfkelenen adam
  الغضب لأنه اشتداد السخط (maqayis)؛ رجل غضوب وغضب وغضبة وغضب أي كثير الغضب شديده (ayn)؛ الغضب ضد الرضا ورجل غضبة كثير الغضب (jamhara)؛ غضب عليه غضبا ورجل غضبان وغضبة يغضب سريعا (sihah)؛ الغضب ثوران دم القلب إرادة الانتقام وإذا وصف الله تعالى به فالمراد به الانتقام (mufradat)
- **B002** biri için ya da uğruna öfkelenmek [kalıp] — yaşayan biri için öfkelenmek · ölen biri uğruna öfkelenmek · ölen kişi uğruna öfkeli olmak
  غضبت لفلان إذا كان حيا وغضبت به إذا كان ميتا (maqayis;sihah;mufradat)
- **B003** karşı koyup muhalefet etmek — ona karşı koyup muhalefet etmek · topluluğuna karşı çıkan
  غاضبه: راغمه؛ مغاضبا أي مراغما لقومه (sihah)
- **B004** sert, yığılmış veya yuvarlak kaya — sert, yığılmış veya yuvarlak kaya
  الغضبة الصخرة الصلبة (maqayis)؛ الغضبة الصخرة الصلبة المتراكمة في الجبل (ayn)؛ الغضبة صخرة مستديرة (jamhara)؛ الغضبة كالصخرة (mufradat)
- **B005** kalın derili ya da çok kızıl — kalın derili adam · kızıl ve kalın yapılı adam · çok kızıl · çok kızıl olan
  رجل غضاب إذا كان غليظ الجلد؛ رجل غضب إذا كان أحمر غليظا (jamhara)؛ الغضب الأحمر الشديد الحمرة ويقال أحمر غضب (sihah)
- **B006** üst göz kapağı çıkıntısı veya göz çevresi şişliği — üst göz kapağında doğuştan çıkıntı veya göz çevresi şişliği · göz çevresinin şişmesi · göz altı şişmiş adam
  الغضب بخصة في الجفن الأعلى خلقة (ayn)؛ غضبت عين الرجل إذا ورم ما حولها ورجل به غضب إذا ورم ما تحت عينه (jamhara)
- **B007** somurtkan, huysuz; iri yılan — iri yılan; somurtkan veya huysuz olan · somurtkan veya huysuz dişi deve · somurtkan kadın
  الغضوب الحية العظيمة (maqayis)؛ ناقة غضوب عبوس (ayn)؛ امرأة غضوب أي عبوس (sihah)؛ توصف به الحية والناقة الضجور (mufradat)
- **B008** belirli hayvan derileri veya kalkan gibi katlanmış deri — yaşlı dağ keçisinin yüzülmüş derisi veya kalkan gibi katlanmış deve derisi · kaplumbağa derisi
  الغضبة جلد المسن من الوعول حين يسلخ (ayn)؛ يسمى جلد السلحفاة الغضب؛ الغضبة قطعة من جلد البعير يطوى بعضها على بعض ويجعل شبيها بالدرقة (jamhara)

## ض ل ل (root_000913): 1:7 ٱلضَّآلِّينَ

- **B001** doğru yoldan ve amaçtan sapma ya da başkasını saptırma — doğru yoldan, amaçtan veya doğruluktan sapmak · doğru yoldan ve doğruluktan sapma · doğru yoldan veya amaçtan sapmış kimse · sapmada direnen, çok sapmış kimse · iyilikten uzak, yanlış ve boş işlere dalmış kimse · asılsız ve yanlış düşünceler · birini doğru yoldan saptırmak · bir kimseyi sapmış saymak · yanlışlığın ve sapmanın içine düşülen yer · yolun bulunamadığı şaşırtıcı arazi · o işi yanlış ve sağduyusuz bir tutumla yapmak
  كل جائر عن القصد ضال؛ الضلال والضلالة بمعنى (maqayis); ضل إذا جار عن القصد؛ لا يوفق لخير صاحب غوايات وبطالات (ayn); الضلال ضد الهدى؛ ضل في الأمر إذا لم يهتد له؛ ضل في الأرض إذا لم يهتد للسبيل (jamhara); الضلال والضلالة ضد الرشاد؛ رجل ضليل ومضلل أي ضال جدا (sihah); الإضلال في كلام العرب ضد الهداية والإرشاد؛ ضل الكافر غاب عن الحجة؛ ضل فلان عن القصد إذا جار (tahdhib)
- **B002** gizlenerek, karışıp eriyerek veya gömülerek gözden yitme — gizlenip gözden kaybolmak · ölüyü gömüp gözden kaldırmak · bir sıvının ötekine karışıp içinde kaybolması · kaya altında güneş görmeyen su
  أضل الميت إذا دفن؛ ضل اللبن في الماء ثم استهلك (maqayis); ضل الشيء إذا خفي وغاب؛ أئذا ضللنا في الأرض أي خفينا وغبنا (jamhara); أضل الميت إذا دفن؛ أضل عنه أي أخفى عليه وأغيب؛ أئذا ضللنا في الأرض أي خفينا وغبنا (sihah); أصل الضلال الغيبوبة؛ ضل الماء في اللبن؛ أضلت بنو قيس عميدها أي دفنته (tahdhib)
- **B003** bir şeyi yitirme veya yerini bulamama; özel olarak kanın karşılıksız kalması — bir şeyin kaybolması, yitip gitmesi veya yok olması · devesini ya da başka bir hayvanını kaybetmek · evin, ibadet yerinin ya da başka bir yerin konumunu bulamamak · bir işin elinden kaçması ve ona güç yetirememek · kanı yerde kalmak, öcü alınmamak · yitme veya yok olma
  أضللت بعيري إذا ذهب منك؛ ضللت المسجد والدار إذا لم تهتد لهما (maqayis); ضللت مكاني إذا لم تهتد له؛ أضل بعيره إذا أفلت فذهب (ayn); ذهب فلان ضلة إذا لم يدر أين ذهب؛ ذهب دمه ضلة إذا لم يثأر به (jamhara); أضللت بعيري إذا ذهب منك؛ ضللت المسجد والدار إذا لم تعرف موضعهما (sihah); أضللت الشيء إذا ضاع منك؛ ضللت الشيء أضله إذا جعلته في مكان ولم تدر أين هو (tahdhib)
- **B004** bir şeyi unutmak veya bellekte tutamamak [kalıp] — bir şeyi unutmak ya da belleğinde tutamamak
  ضللت الشيء أنسيته (jamhara); إن تضل أي إن تنس؛ أن تضل إحداهما أي تغيب عن حفظها أو يغيب حفظها عنها (tahdhib)
- **B005** sahibi bilinmeyen kayıp hayvan, özellikle deve — sahibi bilinmeyen kayıp hayvan, özellikle deve · sahibi bilinmeyen kayıp hayvanlar veya develer
  الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها الذكر والأنثى فيه سواء (ayn); الضالة ما ضل من البهيمة للذكر والأنثى (sihah); الضالة من الإبل التي بمضيعة لا يعرف لها مالك؛ الجميع الضوال (tahdhib)

===== _commentary/v16/out/s001/surah.map3.nohft.tool/map.md (without ## Not carried) =====
## Chains

### The trodden road: guide, centre line, landmark, and the one who loses the way
A road made smooth by many feet, with a guide walking ahead, landmarks to read along it, and a centre line to keep to. One travelling company goes along it. At the far end are its reversals: the walker who cannot find the way in open land, and a company that breaks up along many separate tracks. The surah moves through this road in order. نَعْبُدُ names the smoothly trodden road (1:5). ٱهْدِنَا asks to be shown the road and led ahead on it (1:6). ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ is the road and its straight line (1:6). صِرَٰطَ ٱلَّذِينَ is the road as one company's track (1:7). ٱلضَّآلِّينَ are those who could not find the road (1:7). The dictionary joins the two ends itself: «الهدى نقيض الضلالة» and «الضلال ضد الهدى».
- 1:5 نَعْبُدُ — ع ب د B005 — «الطريق المعبد وهو المسلوك المذلل» (maqayis); «طريق معبد أي مذلل» (jamhara; mufradat) — the road beaten smooth by being walked.
- 1:6 ٱهْدِنَا — ه د ي B001 — «هديته الطريق والبيت هداية أي عرفته» (sihah); «دله على الطريق» (tahdhib); «الهداية دلالة بلطف؛ تعريف الطرق» (mufradat) — showing someone the road and the house it leads to.
- 1:6 ٱهْدِنَا — ه د ي B003 — «الدليل يسمى هاديا لتقدمه»; «العصا هاديا لأنها تتقدمه» (ayn); «كل متقدم لذلك هاد» (maqayis) — the guide walks in front, as the staff goes in front of the hand that holds it.
- 1:6 ٱهْدِنَا — ه د ي B002 — «هدى هدي فلان أي سار سيرته»; «خذ في هديتك أي فيما كنت فيه من الحديث أو العمل ولا تعدل عنه» (sihah) — going someone else's way and keeping to a course without turning off.
- 1:6 ٱلصِّرَٰطَ / 1:7 صِرَٰطَ — ص ر ط B001 — «الصراط: الطريق المستقيم» (mufradat); «الصراط والسراط والزراط: الطريق» (sihah) — the road itself. The dictionary's definition already contains the surah's adjective.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B008 — «الاستقامة في الطريق الذي يكون على خط مستو» (mufradat); «إذا انقاد واستمرت طريقته فقد استقام» (ayn); «رمح قويم» (ayn) — the road's straight line, like a straight spear shaft.
- 1:4 مَٰلِكِ — م ل ك B006 — «الزم ملك الطريق أي وسطه»; «وملك الطريق معظمه ووسطه» (tahdhib) — the middle of the road, where the walker is told to keep.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B002 — «المعلم الأثر يستدل به على الطريق» (sihah; tahdhib); «العلم الجبل الطويل والجميع الأعلام» (ayn) — the trace and the tall mountain a traveller reads to find the road.
- 1:7 أَنْعَمْتَ — ن ع م B007 — «وابن النعامة عرق الرجل ومحجة الطريق» (tahdhib) — the beaten main track.
- 1:7 أَنْعَمْتَ — ن ع م B012 [fixed expression] — «تنعمت زيدا طلبته كأنه أراد أعمل إليه نعامته وهي باطن قدمه» (maqayis); «تنعم فلان إذا مشى مشيا خفيفا» (mufradat) — going to someone on the soles of one's own feet.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B001 — «قوم كل رجل شيعته وعشيرته» (ayn; tahdhib) — the company whose road it is: «صِرَٰطَ ٱلَّذِينَ».
- 1:4 ٱلدِّينِ — د ي ن B005 — «الدين بالكسر العادة والشأن» (sihah); «الحال والأمر الذي تعهده» (maqayis) — the familiar way one keeps going.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B001 — «ضل في الأرض إذا لم يهتد للسبيل» (jamhara); «كل جائر عن القصد ضال» (maqayis); «الإضلال في كلام العرب ضد الهداية والإرشاد» (tahdhib) — the walker who cannot find the road and veers off the direct line.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B003 — «ضللت المسجد والدار إذا لم تهتد لهما» (maqayis) — failing to find the house the road leads to. This reverses «هديته الطريق والبيت».
- 1:5 نَعْبُدُ — ع ب د B010 — «العباديد الفرق من الناس الذاهبون في كل وجه» (sihah); «والأشياء المتفرقة والطرق المختلفة» (tahdhib) — groups going off in every direction along different roads.
- 1:7 أَنْعَمْتَ — ن ع م B008 [fixed expression] — «شالت نعامتهم إذا تفرقوا» (maqayis) — a company that breaks up.
- 1:1 ٱللَّهِ — و ل ه B001 (the dictionary's documented alternative derivation of ٱللَّهِ) — «البلاد التي توله الإنسان أي تحيره» (sihah) — land that leaves the walker bewildered.
- Quran: 6:153 (God's charge to the believers) «وأن هذا صراطي مستقيما فاتبعوه ولا تتبعوا السبل فتفرق بكم عن سبيله» — one straight road against many roads that scatter. 6:161 (the Prophet is told to say) «قل إنني هداني ربي إلى صراط مستقيم دينا قيما». 16:15–16 (God's provisions on the earth) «وسبلا لعلكم تهتدون وعلامات وبالنجم هم يهتدون» — roads, landmarks and stars for finding the way. 28:22 (Moses setting out toward Madyan) «عسى ربي أن يهديني سواء السبيل». 67:22 «أفمن يمشي مكبا على وجهه أهدى أمن يمشي سويا على صراط مستقيم». 7:16 (Iblis vowing to God) «لأقعدن لهم صراطك المستقيم» — an ambush on the road. 36:60–62 (God speaking to the children of Adam) «وأن اعبدوني هذا صراط مستقيم ولقد أضل منكم جبلا كثيرا». 3:51, 19:36, 43:64 (Jesus) «إن الله ربي وربكم فاعبدوه هذا صراط مستقيم». 37:22–24 (angels ordered on the Day) «فاهدوهم إلى صراط الجحيم وقفوهم إنهم مسئولون» — the road reversed.

### Made pliant: owner, owned, and the servant brought low
A master and what he owns: a house, a horse, a slave. The owned thing has been made pliant. A road is trodden until it is smooth, a camel is tarred until it is tame, a person is brought low until he serves. رَبِّ and مَٰلِكِ (1:2, 1:4) name the owner. ٱلدِّينِ (1:4) names both the bringing low and the obedience. نَعْبُدُ (1:5) is the owned one's own voice. One adjective, «المذلل», covers the road, the camel and the servant. The dictionary joins the roots directly: «دانه دينا أي أذله واستعبده ودينته ملكته» and «العبد مدين». The scene also holds its reverse: the served one, honoured as if worshipped.
- 1:2 رَبِّ — ر ب ب B001 — «ويكون الرب: السيد المطاع» (tahdhib); «ورب كل شيء مالكه» (jamhara); «رب الدار ورب الفرس» (mufradat) — the obeyed master and owner of a house or a horse. The jamhara phrase joins رَبِّ to مَٰلِكِ.
- 1:4 مَٰلِكِ — م ل ك B002 — «الملك ما ملكت اليد من مال وخول» (ayn; tahdhib); «المملوك يختص في التعارف بالرقيق من الأملاك» (mufradat) — what the hand holds, slaves included.
- 1:4 ٱلدِّينِ — د ي ن B004 — «دانه دينا أي أذله واستعبده ودينته ملكته» (sihah); «العبد مدين كأنهما أذلهما العمل» (maqayis); «غير مدينين غير مملوكين» (tahdhib); «المدين والمدينة العبد والأمة» (mufradat) — bringing someone low into service and owning him. One phrase joins دين, عبد and ملك.
- 1:4 ٱلدِّينِ — د ي ن B001 — «فالدين الطاعة» (maqayis; sihah); «الدين لله طاعته والتعبد له» (tahdhib); «جنس من الانقياد والذل» (maqayis) — the obedience owed.
- 1:5 نَعْبُدُ — ع ب د B001 — «العبد المملوك وجمعه عبيد» (ayn) — the owned person.
- 1:5 نَعْبُدُ — ع ب د B003 — «إياك نعبد إياك نطيع الطاعة التي نخضع معها» (tahdhib); «تعبدت للرجل إذا تذللت له» (jamhara); «العبودية إظهار التذلل والعبادة غاية التذلل» (mufradat) — the servant lowering himself. tahdhib glosses the surah's own words.
- 1:5 نَعْبُدُ — ع ب د B004 — «عبدت الرجل إذا ذللته وعبدت القوم اتخذتهم عبيدا» (jamhara) — making someone pliant by force.
- 1:5 نَعْبُدُ — ع ب د B005 — «البعير المعبد المهنوء بالقطران المذلل» (maqayis; sihah); «الطريق المعبد وهو المسلوك المذلل» (maqayis) — the tarred, tamed camel and the trodden road: the pliant state seen in an animal and in the ground.
- 1:5 نَعْبُدُ — ع ب د B002 — «العبد الإنسان حرا أو رقيقا هو عبد الله» (ayn); «عبد بالإيجاد وذلك ليس إلا لله» (mufradat) — every person, free or slave, belongs to God by having been brought into being.
- 1:5 نَعْبُدُ — ع ب د B006 — «المعبد المكرم والمعظم كأنه يعبد» (jamhara) — the reverse view: the one who is served and honoured.
- 1:1 ٱللَّهِ / 1:2 لِلَّهِ — ء ل ه B001 — «فالإله الله تعالى لأنه معبود» (maqayis); «لا يكون إلاها حتى يكون معبودا» (tahdhib) — the one served is named by the service paid to him.
- Quran: 16:75 (a parable God strikes) «عبدا مملوكا لا يقدر على شيء». 36:71–72 (God's signs in livestock) «أنعاما فهم لها مالكون وذللناها لهم فمنها ركوبهم» — owners of herds made pliant for them. 26:18–22 (Pharaoh and Moses at court; opens 26:18 «ألم نربك فينا وليدا») — Moses answers in 26:22 «وتلك نعمة تمنها علي أن عبدت بني إسرائيل». 12:23 (Joseph of his Egyptian master) «إنه ربي أحسن مثواي». 3:64 «ولا يتخذ بعضنا بعضا أربابا من دون الله». 19:93 «إن كل من في السماوات والأرض إلا آتي الرحمن عبدا». 12:40 (Joseph in prison) «أمر ألا تعبدوا إلا إياه ذلك الدين القيم». 17:111 «ولم يكن له شريك في الملك ولم يكن له ولي من الذل».

### The day of reckoning: the king, the risen, the recompense
A heavy day arrives. People stand up from their graves before a king who disposes of everything, and each is given his account and his recompense. 1:4 holds the whole scene in three words. The dictionary quotes the ayah under دين: «الدين الحساب ومنه مالك يوم الدين». Under قيامة it quotes «يوم يقوم الناس لرب العالمين» (83:6), which joins ٱلْمُسْتَقِيمَ's root to رَبِّ ٱلْعَٰلَمِينَ.
- 1:4 مَٰلِكِ — م ل ك B003 — «الملك لله المالك المليك» (ayn); «الملك هو المتصرف بالأمر والنهي في الجمهور» (mufradat); «لأن يده فيه قوية صحيحة» (maqayis) — the king who commands and forbids, with a firm hand.
- 1:4 يَوْمِ — ي و م B003 — «اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت» (ayn; tahdhib); «اليوم الشديد: يوم ذو أيام» (ayn; tahdhib) — the day as an event that comes down, a hard day that holds many days.
- 1:4 يَوْمِ — ي و م B005 — «يركب يوم مع إذ، فيقال: يومئذ» (mufradat) — "that day", the word the Quran uses for this scene.
- 1:4 ٱلدِّينِ — د ي ن B002 — «يوم الدين أي يوم الحكم والحساب والجزاء» (maqayis); «الدين الحساب ومنه مالك يوم الدين ومالك يوم الجزاء» (tahdhib); «الدين الجزاء والمكافأة» (sihah) — judgment, account and repayment.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B013 — «القيامة يوم البعث يوم يقوم فيه الخلق بين يدي الحي القيوم» (tahdhib); «يوم يقوم الناس لرب العالمين» (mufradat) — creation rising to its feet before the judge.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B004 — «القيوم القائم على كل شيء» (tahdhib) — the one who stands over everything.
- 1:7 ٱلْمَغْضُوبِ — غ ض ب B001 — «وإذا وصف الله تعالى به فالمراد به الانتقام» (mufradat) — the requital that comes on that day.
- Quran: 82:17–19 «وما أدراك ما يوم الدين ... يوم لا تملك نفس لنفس شيئا والأمر يومئذ لله». 83:4–6 «ليوم عظيم يوم يقوم الناس لرب العالمين». 40:16 «لمن الملك اليوم لله الواحد القهار». 25:26 «الملك يومئذ الحق للرحمن». 22:56 «الملك يومئذ لله يحكم بينهم». 37:22–24 (the gathered are led on and halted) «وقفوهم إنهم مسئولون».

### Debt and the level scale
A loan given and taken, sold on credit until a set term. Goods are priced. A coin of full weight sits on a scale that does not dip. A life taken is answered with blood-money in place of retaliation, or the blood goes unavenged. ٱلدِّينِ (1:4) brings the debt, ٱلْمُسْتَقِيمَ (1:6) the price, the full-weight coin and the balance, غَيْرِ (1:7) the blood-money and the exchange. ٱلضَّآلِّينَ (1:7) brings the blood that is lost, and the forgetting that 2:282 guards against.
- 1:4 ٱلدِّينِ — د ي ن B003 — «الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء» (maqayis); «الدين واحد الديون وتداينوا تبايعوا بالدين» (sihah) — the loan and the deferred sale.
- 1:4 ٱلدِّينِ — د ي ن B002 — «الدين الجزاء والمكافأة» (sihah) — repayment in full.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B010 — «القيمة ثمن الشيء بالتقويم» (ayn; tahdhib); «قامت الأمة مائة دينار أي بلغت قيمتها» (tahdhib) — the price set by valuing.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B015 — «دنانير قوم وقيم ودينار قائم إذا كان مثقالا سواء لا يرجح» (tahdhib) — a coin of exact weight that does not tip the scale.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B017 — «قام ميزان النهار فاعتدل» (tahdhib) — the day's own balance coming level at noon.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B007 [fixed expression] — «أصل القيمة الواو وأصله أنك تقيم هذا مكان ذاك» (maqayis) — one thing set in another's place: the logic of a price.
- 1:7 غَيْرِ — غ ي ر B002 — «غارني الرجل إذا وداك من الدية والاسم الغِيرة» (sihah); «تقبلوا الغيرا» (maqayis; sihah) — blood-money paid.
- 1:7 غَيْرِ — غ ي ر B003 — «قود فغير إلى الدية» (maqayis); «غايرت الرجل أي عارضته بالبيع وبادلته والغيار البدال» (sihah) — retaliation exchanged for payment; trade by exchange.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B003 — «ذهب دمه ضلة إذا لم يثأر به» (jamhara) — the opposite outcome: blood left unavenged and unpaid.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B004 [fixed expression] — «أن تضل إحداهما أي تغيب عن حفظها أو يغيب حفظها عنها» (tahdhib) — a witness to a debt who forgets.
- Quran: 2:282 (the debt-writing ayah) «إذا تداينتم بدين إلى أجل مسمى فاكتبوه ... أن تضل إحداهما فتذكر إحداهما الأخرى» — debt, a named term and forgetting in one ayah. 17:35 «وزنوا بالقسطاس المستقيم», and 26:182 (Shu‘ayb to Madyan) in the same words — the straight scale. 21:47 «ونضع الموازين القسط ليوم القيامة فلا تظلم نفس شيئا وإن كان مثقال حبة». 2:178 (the law of retaliation) «فمن عفي له من أخيه شيء فاتباع بالمعروف وأداء إليه بإحسان». 4:92 «ودية مسلمة إلى أهله».

### Womb and rearing: mother, child, and the one who brings to completion
The womb is the house where a child grows. Birth comes and the mother is sore afterward. A ewe that has just given birth is kept at home for her milk. A parent or step-parent then raises the child stage by stage until it is complete: providing for the household, guarding it, letting it live in ease. The reverse is a mother parted from her child and crazed with longing. ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (1:1, 1:3) opens the womb image. رَبِّ (1:2) carries the rearing. أَنْعَمْتَ, غَيْرِ (1:7) and ٱلْمُسْتَقِيمَ (1:6) carry the household's ease, provisioning, jealous guarding and upkeep.
- 1:1, 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ — ر ح م B003 — «الرحم بيت منبت الولد ووعاؤه في البطن» (ayn; tahdhib) — the house and vessel where the child grows.
- 1:1, 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ — ر ح م B004 — «الرحوم الناقة التي تشتكي رحمها بعد النتاج» (sihah) — the soreness after birth.
- 1:1, 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ — ر ح م B001 — «الرحمة رقة تقتضي الإحسان إلى المرحوم» (mufradat); «ورحمة الضعيف والتعطف عليه» (tahdhib) — tenderness that turns into doing good to the weak.
- 1:1, 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ — ر ح م B002 — «استعير الرحم للقرابة لكونهم خارجين من رحم واحدة» (mufradat) — kin as those who came out of one womb.
- 1:2 رَبِّ — ر ب ب B002 — «رب فلان ولده؛ رباه» (sihah); «التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام» (mufradat); «رببت الصبي أربه» (maqayis) — raising a child stage by stage to completion.
- 1:2 رَبِّ — ر ب ب B005 — «الراب والرابة بأحد الزوجين إذا تولى تربية الولد» (mufradat); «الربيبة: الحاضنة» (sihah) — the step-parent who takes the child on; the nurse.
- 1:2 رَبِّ — ر ب ب B009 — «الربى: الشاة التي وضعت حديثا؛ قرب العهد بالولادة» (sihah); «الشاة الربي التي تحتبس في البيت للبن» (maqayis) — the newly delivered ewe kept in the house for milk.
- 1:2 رَبِّ — ر ب ب B003 — «العالم المعلم الذي يغذو الناس بصغار العلوم» (tahdhib) — the rearing carried into teaching: feeding people the small parts of knowledge first. The phrase joins رَبِّ to ٱلْعَٰلَمِينَ's root.
- 1:7 أَنْعَمْتَ — ن ع م B002 — «نعم فلان أولاده ترفهم» (maqayis) — children raised in ease.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B004 — «قوام أهل بيته وقيام أهل بيته؛ الذي يقيم شأنهم» (sihah) — the one who keeps the household going.
- 1:7 غَيْرِ — غ ي ر B001 — «الغِيرة بالكسر: الميرة»; «يميرهم وينفعهم» (sihah) — food brought in for the family.
- 1:7 غَيْرِ — غ ي ر B004 — «الغَيرة بالفتح مصدر قولك غار الرجل على أهله» (sihah) — jealous guarding of one's household.
- 1:1 ٱللَّهِ — و ل ه B002 (alternative derivation) — «لا توله والدة عن ولدها» (maqayis; tahdhib); «التوليه أن يفرق بين المرأة وولدها» (maqayis; sihah); «لا تجعل والها وذلك في السبايا» (sihah) — the mother parted from her child among the captives.
- 1:1 ٱللَّهِ — و ل ه B001 (alternative derivation) — «ناقة واله إذا اشتد وجدها على ولدها» (sihah) — the she-camel crazed with longing for her young.
- Quran: 17:23–24 (God's command on parents) «وقضى ربك ألا تعبدوا إلا إياه وبالوالدين إحسانا ... واخفض لهما جناح الذل من الرحمة وقل رب ارحمهما كما ربياني صغيرا» — رب, mercy, lowering oneself and child-rearing in one prayer. 3:6 «هو الذي يصوركم في الأرحام كيف يشاء». 4:1 «واتقوا الله الذي تساءلون به والأرحام». 4:23 «وربائبكم اللاتي في حجوركم». 28:7–13 (Moses' mother; opens 28:7 «أن أرضعيه») — 28:10 «وأصبح فؤاد أم موسى فارغا», 28:13 «فرددناه إلى أمه كي تقر عينها»; also 20:40. 3:79 «كونوا ربانيين بما كنتم تعلمون الكتاب». From memory, hadith (not Quran): the captive woman who found her child and nursed it, and the Prophet's words that God is more merciful to His servants than she is to her child.

### The favour carried to completion, and the favour counted against its receiver
A benefit is handed to someone, then made more and finished. The receiver answers by naming the giver's gifts with thanks. The reverse is the giver who keeps reminding the receiver of what he gave. رَبِّ (1:2) and أَنْعَمْتَ (1:7) meet in one dictionary phrase: «رب الرجل النعمة يربها ربا ... إذا تممها». ٱلْحَمْدُ (1:2) is the answer to the favour, and it also holds the reverse (يتحمد).
- 1:2 رَبِّ — ر ب ب B002 — «رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها» (jamhara); «رب فلان الصنيعة إذا أتمها وأصلحها» (tahdhib) — finishing a favour and setting it right.
- 1:2 رَبِّ — ر ب ب B016 — «الربى: النعمة والإحسان» (tahdhib) — the favour itself under the رب root.
- 1:7 أَنْعَمْتَ — ن ع م B001 — «النعمة اليد والصنيعة والمنة وما أنعم به عليك» (sihah); «النعمة الحالة الحسنة والإنعام إيصال الإحسان إلى الغير» (mufradat) — the open hand, the good deed, and good reaching another person.
- 1:7 أَنْعَمْتَ — ن ع م B010 — «أنعم أفضل وزاد» (tahdhib); «دققت دواء فأنعمت دقه أي بالغت وزدت» (tahdhib) — going further, finishing the job thoroughly.
- 1:1, 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ — ر ح م B001 — «الرحمة رقة تقتضي الإحسان إلى المرحوم» (mufradat) — the tenderness the favour comes from.
- 1:2 ٱلْحَمْدُ — ح م د B001 — «الحمد أعم من الشكر» (sihah; mufradat) — the answer, wider than thanks.
- 1:2 ٱلْحَمْدُ — ح م د B006 [fixed expression] — «أحمد إليك الله أي معك» (ayn; tahdhib); «أشكر إليك أياديه ونعمه» (tahdhib) — listing the giver's gifts in thanks, in company with others.
- 1:2 ٱلْحَمْدُ — ح م د B005 [fixed expression] — «فلان يتحمد علي أي يمن» (sihah); «من أنفق ماله على نفسه فلا يتحمد به إلى الناس» (sihah; tahdhib) — the reverse: holding one's favour over the receiver. Sihah's «المنة» under نعمة names the same act.
- Quran: 48:1–2 (the opening victory) «ويتم نعمته عليك ويهديك صراطا مستقيما». 2:150 «ولأتم نعمتي عليكم ولعلكم تهتدون». 5:3 «اليوم أكملت لكم دينكم وأتممت عليكم نعمتي ورضيت لكم الإسلام دينا». 93:11 «وأما بنعمة ربك فحدث». 106:3–4 «فليعبدوا رب هذا البيت الذي أطعمهم من جوع». 26:18–22 (Pharaoh's claim to have raised Moses, and Moses' reply «وتلك نعمة تمنها علي») — the counted favour.

### Approval and anger: what comes down upon a people, and the faces it leaves
The surah ends with two groups. The same «عَلَيْهِمْ» comes after each: favour comes down on one, anger on the other. Each word has an opposite in the dictionary. Praise is the opposite of blame, نعم of بئس, anger of approval (رضا). The scene is bodily too. The face of anger frowns, reddens and swells around the eye. The face of favour is soft, and its eye is cooled. 1:2 ٱلْحَمْدُ opens on approval. 1:7 sets أَنْعَمْتَ against ٱلْمَغْضُوبِ.
- 1:2 ٱلْحَمْدُ — ح م د B001 — «الحمد نقيض الذم» (maqayis; ayn; jamhara; sihah; tahdhib) — praise against blame.
- 1:2 ٱلْحَمْدُ — ح م د B002 — «هل تحمد لي هذا الأمر أي هل ترضاه لي» (tahdhib); «أحمدت فلانا إذا وجدته محمودا» — finding something good and approving it. This is the رضا that anger is defined against.
- 1:7 أَنْعَمْتَ — ن ع م B003 — «نعم ضد بئس» (maqayis); «نعم كلمة تستعمل في المدح بإزاء بئس» (mufradat) — the word of approval against the word of blame.
- 1:7 أَنْعَمْتَ — ن ع م B001 — «وما أنعم به عليك» (sihah) — favour that comes "upon" someone.
- 1:7 ٱلْمَغْضُوبِ — غ ض ب B001 — «الغضب ضد الرضا» (jamhara); «الغضب لأنه اشتداد السخط» (maqayis); «الغضب ثوران دم القلب إرادة الانتقام» (mufradat) — anger against approval, as the heart's blood rising.
- 1:7 ٱلْمَغْضُوبِ — غ ض ب B005 — «الغضب الأحمر الشديد الحمرة» (sihah) — deep red.
- 1:7 ٱلْمَغْضُوبِ — غ ض ب B007 — «امرأة غضوب أي عبوس» (sihah) — the frowning face.
- 1:7 ٱلْمَغْضُوبِ — غ ض ب B006 — «غضبت عين الرجل إذا ورم ما حولها» (jamhara) — swelling around the eye.
- 1:7 أَنْعَمْتَ — ن ع م B002 — «نعم الشيء صار ناعما لينا» (sihah) — softness, as of a face at ease.
- 1:7 أَنْعَمْتَ — ن ع م B013 [fixed expression] — «نعمة العين قرتها» (sihah) — the eye cooled and at rest.
- 1:4 يَوْمِ — ي و م B004 [fixed expression] — «وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب، وبالعفو عن آخرين»; «أيامه: نعمه» (tahdhib) — God's days, on which punishment came down on some and pardon and favour on others.
- Quran: 20:80–82 (God to Israel after the rescue; opens 20:80) «فيحل عليكم غضبي ومن يحلل عليه غضبي فقد هوى وإني لغفار لمن تاب ... ثم اهتدى» — anger coming down and the one who falls, against guidance. 4:69 «فأولئك مع الذين أنعم الله عليهم من النبيين والصديقين والشهداء والصالحين». 19:58 «أولئك الذين أنعم الله عليهم ... وممن هدينا واجتبينا». 3:162 «أفمن اتبع رضوان الله كمن باء بسخط من الله». 88:2 and 88:8 «وجوه يومئذ خاشعة ... وجوه يومئذ ناعمة». 83:24 «تعرف في وجوههم نضرة النعيم». 80:38–40 «وجوه يومئذ مسفرة ... ووجوه يومئذ عليها غبرة».

### Name, brand and landmark: what is raised up or burned in so a thing is known
A thing becomes known by a mark. A name is raised up and spoken. A brand is burned into a camel's hide. A banner and a tall mountain stand up to be seen. A shape rises on the horizon until the eye can make it out. The created kinds are themselves signs. بِسْمِ (1:1) holds two documented derivations: height (س م و) and branding (و س م). ٱلْعَٰلَمِينَ (1:2) names the worlds after the sign by which a thing is known. ٱللَّهِ is the name invoked.
- 1:1 بِسْمِ — س م و B005 — «الاسم مشتق من السمو وهو الرفعة؛ تنويها على الدلالة على المعنى» (tahdhib); «الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى» (mufradat) — the name raised up so that what it names is known.
- 1:1 بِسْمِ — س م و B005 — «سميا أي نظيرا له يستحق اسمه» (mufradat) — the namesake, the equal who could claim the same name.
- 1:1 بِسْمِ — س م و B001 — «السمو الارتفاع والعلو» (sihah) — height.
- 1:1 بِسْمِ — س م و B002 — «سما لي شخص ارتفع حتى استثبته» (maqayis) — a shape rising into view until it is recognised.
- 1:1 بِسْمِ — س م و B008 — «ذهب صيته في الناس وسماه، أي صوته في الخير لا في الشر» (tahdhib) — a good name travelling among people.
- 1:1 بِسْمِ — و س م B001 (the Kufans' documented derivation) — «الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي» (ayn); «الميسم المكواة أو الشيء الذي يوسم به الدواب» — the brand burned in so the animal is known.
- 1:1 بِسْمِ — و س م B002 — «توسمت فيه الخير والشر أي رأيت فيه أثرا» (ayn) — reading the mark to know what someone is.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B002 — «أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره» (maqayis); «العلم الراية والجمع أعلام» ; «أعلم الفارس إذا كانت له علامة في الحرب» — the mark that sets a thing apart: a banner, a horseman's emblem in battle.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B003 — «العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به» (mufradat); «العالمون كل جنس من الخلق فهو في نفسه معلم وعلم» (maqayis) — each kind of creature is itself a mark.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B001 — «علمت الشيء عرفته» (sihah; tahdhib) — the knowing the mark makes possible.
- 1:1 ٱللَّهِ — ء ل ه B002 — «اسم الله الأكبر هو الله» (ayn; tahdhib); «يا ألله اغفر لي» (sihah); «الله ما فعلت ذاك تريد والله ما فعلته» (ayn) — the name itself spoken in a call and in an oath.
- Quran: 19:65 «رب السماوات والأرض وما بينهما فاعبده واصطبر لعبادته هل تعلم له سميا» — رب, service, knowing and the namesake together. 87:1 «سبح اسم ربك الأعلى» — name, رب and height. 96:1 «اقرأ باسم ربك الذي خلق». 17:110 «قل ادعوا الله أو ادعوا الرحمن أيا ما تدعوا فله الأسماء الحسنى». 12:40 (Joseph to his fellow prisoners) «ما تعبدون من دونه إلا أسماء سميتموها». 27:30 (Solomon's letter to Sheba) «إنه من سليمان وإنه بسم الله الرحمن الرحيم». 2:31 «وعلم آدم الأسماء كلها». 15:75 (after Lot's town was overturned; scene opens 15:61) «إن في ذلك لآيات للمتوسمين». 68:16 «سنسمه على الخرطوم».

### Sun, crescent, and the sky's sphere
A day runs from sunrise to sunset. At noon the sun stands overhead, shadows almost vanish, and the day's balance comes level. At evening a crescent rises a little off the horizon. The moon moves through its stations. All of it turns inside the sphere. In the reverse, the sun itself is worshipped. يَوْمِ (1:4) is the day, ٱلْمُسْتَقِيمَ (1:6) the noon sun standing, بِسْمِ (1:1) the crescent and the sky, أَنْعَمْتَ (1:7) the lunar station, ٱلْعَٰلَمِينَ (1:2) the sphere. ٱللَّهِ (1:1) carries «الإلاهة», the sun named for being worshipped, against نَعْبُدُ «إِيَّاكَ».
- 1:4 يَوْمِ — ي و م B001 — «اليوم مقداره من طلوع الشمس إلى غروبها» (ayn; tahdhib) — the span from sunrise to sunset.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B017 — «قام قائم الظهيرة إذا قامت الشمس وكاد الظل يعقل» (ayn; tahdhib); «قام ميزان النهار فاعتدل» (tahdhib) — the sun standing at noon, the day's balance level.
- 1:1 بِسْمِ — س م و B002 — «سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا» (ayn) — the crescent's shape lifting off the horizon.
- 1:1 بِسْمِ — س م و B004 — «السماء كل ما علاك فأظلك» (sihah) — everything overhead that shades you.
- 1:7 أَنْعَمْتَ — ن ع م B007 — «والنعائم منزل من منازل القمر» (sihah) — a station of the moon.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B003 — «العالم اسم للفلك وما يحويه» (mufradat) — the sphere and what it holds.
- 1:1 ٱللَّهِ — ء ل ه B001 — «والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها» (maqayis) — the sun given the name of worship.
- Quran: 41:37 «لا تسجدوا للشمس ولا للقمر واسجدوا لله الذي خلقهن إن كنتم إياه تعبدون». 6:75–79 (Abraham watching star, moon and sun) — 6:77 «فلما رأى القمر بازغا قال هذا ربي فلما أفل قال لئن لم يهدني ربي لأكونن من القوم الضالين». 27:24 (the hoopoe reporting on Sheba; scene opens 27:20) «يسجدون للشمس من دون الله ... فصدهم عن السبيل فهم لا يهتدون». 10:5 «والقمر نورا وقدره منازل لتعلموا عدد السنين والحساب». From memory: 2:189 «يسألونك عن الأهلة قل هي مواقيت للناس والحج».

### Rain that rears the land
The sky clouds over in layers. The cloud stays, and the soft wet south wind keeps blowing. The year's first rain marks the ground with plants. The cloud is named for rearing what grows. A tender herb stays green through summer. Water gathers in plenty, people and land are given drink, and their condition is set right. Herders find the pasture good. رَبِّ (1:2) gives the cloud, its staying, the herb and the gathered water. بِسْمِ (1:1) gives sky, rain and plant, and the first rain that brands the earth. أَنْعَمْتَ (1:7) gives the wind and fresh green living. غَيْرِ (1:7) gives the rain's set-right. ٱلْحَمْدُ (1:2) gives the pasture found good.
- 1:1 بِسْمِ — س م و B004 — «العرب تسمى السحاب سماء والمطر سماء»; «يسموا النبات سماء» (maqayis) — cloud, rain and plant under one name.
- 1:1 بِسْمِ — و س م B003 (alternative derivation) — «الوسمي أول مطر السنة يسم الأرض بالنبات، وأرض موسومة أصابها الوسمي» (ayn) — the first rain branding the ground with green.
- 1:2 رَبِّ — ر ب ب B008 — «الرباب: السحاب، سمي بذلك لأنه يرب النبات» (mufradat); «الربابة: السحابة التي قد ركب بعضها بعضا» (tahdhib) — the layered cloud, named for rearing the plants.
- 1:2 رَبِّ — ر ب ب B007 — «أربت الجنوب والسحابة أي دامت» (sihah) — south wind and cloud staying.
- 1:7 أَنْعَمْتَ — ن ع م B009 — «النعامى ريح الجنوب لأنها أبل الرياح وأرطبها» (sihah); «من أسماء الجنوب النعامى» (tahdhib) — the wettest, softest wind. Sihah's «أربت الجنوب» joins it to رَبِّ.
- 1:2 رَبِّ — ر ب ب B012 — «الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف» (tahdhib) — a tender plant that does not wither in summer.
- 1:2 رَبِّ — ر ب ب B013 — «الربب، بالفتح: الماء الكثير، ويقال العذب» (sihah) — plentiful sweet water.
- 1:7 غَيْرِ — غ ي ر B001 — «غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم» (maqayis); «سقاهم» (sihah) — rain sent to set people's state right.
- 1:7 أَنْعَمْتَ — ن ع م B002 — «نعمة العيش حسنه وغضارته» (tahdhib) — life fresh and green.
- 1:2 ٱلْحَمْدُ — ح م د B002 — «أحمدت الأرض إذا رضيت سكناها أو مرعاها» (jamhara; sihah) — land found good to live on and graze.
- Quran: 42:28 «وهو الذي ينزل الغيث من بعد ما قنطوا وينشر رحمته وهو الولي الحميد» — rain, mercy and praise together. 7:57 «يرسل الرياح بشرا بين يدي رحمته حتى إذا أقلت سحابا ثقالا». 30:48–50 «فتثير سحابا فيبسطه في السماء ... فانظر إلى آثار رحمت الله كيف يحيي الأرض بعد موتها». 80:24–32 (the human being told to look at his food) «أنا صببنا الماء صبا ... متاعا لكم ولأنعامكم». 32:27 «نسوق الماء إلى الأرض الجرز فنخرج به زرعا تأكل منه أنعامهم».

### The herd: owner, lead animal, pasture, and the stray
A camel herd belongs to an owner and carries his brand. The lead animal walks in front and the rest follow. A mount is carried by its legs and steered by its neck. The tamed camel is tarred. The herd keeps to its grazing ground. Then one camel slips loose. It stays lost in the open, «لا يعرف ربها», or it pines for the companions it has lost. Out beyond the owned herd run the wild herds. The dictionary joins the stray to both owner words of the surah: «لا يعرف ربها» and «لا يعرف لها مالك».
- 1:2 رَبِّ — ر ب ب B001 — «ورب كل شيء مالكه» (jamhara) — the owner.
- 1:4 مَٰلِكِ — م ل ك B008 [fixed expression] — «ملك الإبل والشاء ما يتقدم ويتبعه سائره» (mufradat); «ملك الدابة قوائمها وهاديها» (sihah; tahdhib); «مليك النحل يعسوبها» (sihah) — the animal in front that the rest follow; a mount's legs and neck. The sihah phrase joins مَٰلِكِ and ٱهْدِنَا's root.
- 1:6 ٱهْدِنَا — ه د ي B003 — «هوادي الوحش متقدماتها الهادية لغيرها» (mufradat); «الهاديات أوائل الوحش» (sihah); «هوادي الخيل أعناقها أو أول رعيل» — the leaders at the head of a herd; horses' necks; the first rank.
- 1:7 أَنْعَمْتَ — ن ع م B005 — «النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم» (maqayis) — camels, named for the good they bring.
- 1:5 نَعْبُدُ — ع ب د B005 — «البعير المعبد المهنوء بالقطران المذلل» (maqayis; sihah) — the tarred, tamed camel.
- 1:1 بِسْمِ — و س م B001 (alternative derivation) — «وبعير موسوم وسم بسمة يعرف بها» (ayn) — the brand that lets anyone know whose camel it is.
- 1:2 رَبِّ — ر ب ب B007 — «مرب الإبل حيث لزمته» (sihah; tahdhib) — the ground the camels keep to.
- 1:2 ٱلْحَمْدُ — ح م د B002 — «أحمدت الأرض إذا رضيت سكناها أو مرعاها» — pasture found good.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B005 — «الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها الذكر والأنثى فيه سواء» (ayn); «الضالة من الإبل التي بمضيعة لا يعرف لها مالك» (tahdhib) — the stray whose owner is unknown.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B003 — «أضل بعيره إذا أفلت فذهب» (ayn); «أضللت بعيري إذا ذهب منك» (maqayis) — the owner's side: the camel got loose and is gone.
- 1:1 ٱللَّهِ — و ل ه B001 (alternative derivation) — «الجمل إذا فقد ألافه فحن إليها واله» (tahdhib) — the camel cut off from its companions, yearning for them.
- 1:2 رَبِّ — ر ب ب B014 — «الربرب: القطيع من بقر الوحش» (sihah); 1:5 نَسْتَعِينُ — ع و ن B006 — «العانة القطيع من حمر الوحش» (ayn; sihah) — the wild herds that no one owns.
- Quran: 16:5–9 (God's gift of livestock) «والأنعام خلقها لكم ... ولكم فيها جمال حين تريحون وحين تسرحون ... إن ربكم لرءوف رحيم ... وعلى الله قصد السبيل ومنها جائر ولو شاء لهداكم أجمعين» — the herd going out and coming home, then the straight road and the road that veers off. 7:179 «أولئك كالأنعام بل هم أضل». 25:44 «إن هم إلا كالأنعام بل هم أضل سبيلا». 36:71–72 «أنعاما فهم لها مالكون وذللناها لهم». From memory, hadith (not Quran): on a stray camel, «معها سقاؤها وحذاؤها ترد الماء وتأكل الشجر حتى يلقاها ربها»; and God's joy at a servant's repentance, likened to a man whose mount ran off in empty desert and then came back.

### The well-head: crossbeam, pulley, and water that keeps a thing standing
A deep well full of water has a crossbeam over its mouth, and from the beam hangs a pulley for drawing water. Water is what keeps a traveller's affairs on their feet. A tribe's wells are its "kings". The reverse is a spring whose water runs out into the desert and is lost. أَنْعَمْتَ (1:7) and ٱلْمُسْتَقِيمَ (1:6) meet in one tahdhib phrase about this structure. ٱلْعَٰلَمِينَ (1:2) gives the full well. مَٰلِكِ (1:4) gives water as what keeps life going, and the dictionary joins it to قوام.
- 1:7 أَنْعَمْتَ — ن ع م B007 — «النعامة الخشبة المعترضة على الزرنوقين» (sihah; tahdhib); «النعامة المظلة في الجبل وعلى رأس البئر تشبيها بالنعامة في الهيئة» (mufradat) — the beam across the two posts, the shade over the well-head.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B012 — «القامة البكرة التي يستقى بها الماء؛ النعامة الخشبة المعترضة ثم تعلق القامة» (tahdhib); «القامة البكرة بأداتها» (sihah; maqayis) — the pulley hung from the beam. One phrase joins both surah words. The ayn phrase «القامة مقدار قيام الرجل كهيئة الرجل يبنى على شفير بئر» is a reading the dictionary records and counts wrong.
- 1:2 ٱلْعَٰلَمِينَ — ع ل م B005 — «العيلم الركية الكثيرة الماء» (sihah); «العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء» (maqayis) — the deep, full well.
- 1:2 رَبِّ — ر ب ب B013 — «الربب وهو الماء الكثير سمي بذلك لاجتماعه» (maqayis) — water gathered in plenty.
- 1:4 مَٰلِكِ — م ل ك B007 [fixed expression] — «الماء ملك أمر أي يقوم به الأمر» (sihah); «والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره» (maqayis); «مياهنا ملوكنا» (tahdhib) — water as what keeps affairs standing. Sihah's gloss uses يقوم.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B009 — «قوام الأمر ملاكه» (sihah); «القوام من العيش ما يقيمك ويغنيك» (ayn) — what keeps one standing. This phrase joins ق و م to م ل ك.
- 1:7 غَيْرِ — غ ي ر B001 — «سقاهم» (sihah) — giving people drink.
- 1:1 ٱللَّهِ — و ل ه B003 (alternative derivation) — «عين مولهة إذا أرسل ماؤها فذهب في الصحارى» (maqayis) — the reverse: a spring's water lost in the desert.
- Quran: 28:22–24 (Moses on the road to Madyan, then at its well) «عسى ربي أن يهديني سواء السبيل ... ولما ورد ماء مدين وجد عليه أمة من الناس يسقون ... فسقى لهما ثم تولى إلى الظل فقال رب إني لما أنزلت إلي من خير فقير» — the road, the well, giving drink, shade and رب in one passage. 12:10 and 12:19 (Joseph in the well) «وألقوه في غيابت الجب» and «فأرسلوا واردهم فأدلى دلوه». 67:30 «إن أصبح ماؤكم غورا فمن يأتيكم بماء معين».

### Leaning and standing: the walker who asks for support
A walker's mount gives out and he is stranded. Weak, he sways and walks propped between two men, leaning on them. Help comes as a back to lean on. Then the body stands upright again and walks at its own calm pace, not the rush of a man in flight. A wall holds because its parts hold together. نَسْتَعِينُ (1:5) is the asking. ٱهْدِنَا (1:6) is walking supported between two men and walking calmly. ٱلْمُسْتَقِيمَ (1:6) is standing upright and the prop that holds. نَعْبُدُ (1:5) gives the stranded rider and firmness. مَٰلِكِ (1:4) gives a wall's cohesion and the heart that holds the body together.
- 1:5 نَعْبُدُ — ع ب د B011 — «أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت» (sihah) — left on the road when his mount gave out.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B016 [fixed expression] — «قامت لفلان دابته إذا كلت أو عيت فلم تسر» (tahdhib) — the mount stopping dead.
- 1:6 ٱهْدِنَا — ه د ي B009 — «الهداء الرجل البليد الضعيف» (ayn) — the weak, heavy man.
- 1:6 ٱهْدِنَا — ه د ي B008 — «يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله» (sihah); «التهادي مشي في تمايل يمينا وشمالا» (ayn) — walking between two men, leaning on them, swaying.
- 1:5 نَسْتَعِينُ — ع و ن B001 — «العون الظهيرة على الأمر» (sihah); «كل شيء استعنت به أو أعانك فهو عونك» (ayn); «الاستعانة طلب العون» (mufradat) — help as backing; asking for it.
- 1:5 نَسْتَعِينُ — ع و ن B005 [fixed expression] — «برذون متعاون إذا لحقت قوته وسنه» (tahdhib) — strength that has caught up with age.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B002 — «قام قياما والقومة المرة الواحدة إذا انتصب» (maqayis); «تركتموها قائمة على أصولها» (mufradat) — rising upright; left standing on its roots.
- 1:6 ٱلْمُسْتَقِيمَ — ق و م B009 — «القيام العماد» (tahdhib) — the prop.
- 1:6 ٱهْدِنَا — ه د ي B010 — «لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن» (ayn) — the steady gait of the one who is not running away.
- 1:4 مَٰلِكِ — م ل ك B001 — «حائط ليس له ملاك أي تماسك» (mufradat); «أصل صحيح يدل على قوة في الشيء وصحة» (maqayis) — a wall that holds together.
- 1:4 مَٰلِكِ — م ل ك B005 [fixed expression] — «القلب ملاك الجسد» (ayn; sihah; mufradat) — the heart that holds the body together.
- 1:5 نَعْبُدُ — ع ب د B007 — «العبدة وهي القوة والصلابة» (maqayis) — firmness.
- Quran: 18:77 (Moses and al-Khidr in a town that refused them food; the scene opens there) «فوجدا فيها جدارا يريد أن ينقض فأقامه» — a falling wall set upright. 18:94–95 (Dhu'l-Qarnayn asked for a barrier) «فأعينوني بقوة أجعل بينكم وبينهم ردما». 21:112 «وربنا الرحمن المستعان». 12:18 (Jacob) «والله المستعان على ما تصفون». 7:128 (Moses to his people) «استعينوا بالله واصبروا». 67:22 «أمن يمشي سويا على صراط مستقيم». From memory, hadith: in his last illness the Prophet came out «يهادى بين رجلين».

### Passing out of sight: the road that takes its walker on, and the one lost in the earth
Two kinds of going out of sight. Food goes down the throat and is gone. A walker goes on along a road until he is out of view. Both are a passage to where they belong. Against them stands the one who disappears with no one knowing where: the dead hidden in the earth, milk lost in water, a spring's water gone into the desert, a memory that slips away. The dictionary uses the same verb, غاب, for both ends: «لأن الذاهب فيه يغيب» under صراط and «ضل الشيء إذا خفي وغاب» under ضلال. The surah moves from ٱلصِّرَٰطَ (1:6) to ٱلضَّآلِّينَ (1:7).
- 1:6 ٱلصِّرَٰطَ / 1:7 صِرَٰطَ — ص ر ط B002 — «أصل صحيح واحد يدل على غيبة في مر وذهاب؛ سرطت الطعام إذا بلعته لأنه إذا سرط غاب» (maqayis) — going out of sight in passing through; swallowed food.
- 1:6 ٱلصِّرَٰطَ — ص ر ط B001 — «بعض أهل العلم يقول السراط مشتق من ذلك لأن الذاهب فيه يغيب» (maqayis) — the road takes the walker out of sight. Maqayis gives this as some scholars' view.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B002 — «ضل الشيء إذا خفي وغاب؛ أئذا ضللنا في الأرض أي خفينا وغبنا» (jamhara; sihah); «أصل الضلال الغيبوبة» (tahdhib); «أضل الميت إذا دفن»; «ضل اللبن في الماء ثم استهلك» (maqayis) — hidden in the earth, buried, dissolved away.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B003 — «ذهب فلان ضلة إذا لم يدر أين ذهب» (jamhara) — gone, and no one knows where.
- 1:7 ٱلضَّآلِّينَ — ض ل ل B004 [fixed expression] — «أن تضل إحداهما أي تغيب عن حفظها أو يغيب حفظها عنها» (tahdhib) — gone from memory.
- 1:1 ٱللَّهِ — و ل ه B003 (alternative derivation) — «ماء موله وموله أرسل في الصحراء فذهب» (sihah) — water let go into the desert and lost.
- Quran: 32:10 (the deniers' question) «أئذا ضللنا في الأرض أئنا لفي خلق جديد». 6:24 «وضل عنهم ما كانوا يفترون». 12:10 «وألقوه في غيابت الجب يلتقطه بعض السيارة». 36:66 «فاستبقوا الصراط فأنى يبصرون».

### Led to the house: the offering, the bride, the refugee
Something is led along a road to a house where it will belong. A sacrificial camel from the herd is driven to the Sanctuary, and God's name is spoken over it. A bride is brought to her husband's house after the marriage is contracted. A gift is carried on a tray to a friend. A man who asks a people for protection becomes sacred like the Sanctuary's offering. The pilgrimage season is a fixed marker where people gather. ٱهْدِنَا (1:6) names every one of these conveyings. Sihah ties the offering to أَنْعَمْتَ: «من النعم». بِسْمِ (1:1) gives the name spoken over the beast and the season of gathering. مَٰلِكِ (1:4) gives the marriage. رَبِّ (1:2) gives the covenant.
- 1:6 ٱهْدِنَا — ه د ي B005 — «الهدي ما يهدى إلى الحرم من النعم؛ حتى يبلغ الهدى محله» (sihah); «العرب تسمي الإبل هديا» (tahdhib); «ما أهدي من النعم إلى الحرم قربة إلى الله تعالى» (maqayis) — the beast driven to the Sanctuary until it reaches its place.
- 1:7 أَنْعَمْتَ — ن ع م B005 — «النعم الإبل» (maqayis) — the herd the offering is taken from.
- 1:5 نَعْبُدُ — ع ب د B005 / B003 — «البعير المعبد المهنوء بالقطران المذلل»; «العبادة الطاعة والتعبد التنسك» (sihah) — the tamed camel being led; the act of worship it serves.
- 1:1 بِسْمِ — س م و B005 — «به رفع ذكر المسمى» (mufradat) — the name raised over the offering, as 22:34 and 22:36 stage it.
- 1:1 بِسْمِ — و س م B004 (alternative derivation) — «موسم الحج موسما لأنه معلم يجتمع فيه» (ayn; tahdhib); «وسم الناس: شهدوا الموسم» (maqayis; sihah) — the pilgrimage season as a fixed marker of gathering. The phrase joins وسم and the ع ل م of ٱلْعَٰلَمِينَ.
- 1:6 ٱهْدِنَا — ه د ي B006 — «هديت العروس فأنا أهديها هداء»; «المرأة سميت هديا لأنها كالأسيرة عند زوجها أو لأنها تهدى إلى زوجها»; «أهدى الرجل امرأته جمعها إليه وضمها» (tahdhib) — the bride brought to her husband and gathered to him.
- 1:4 مَٰلِكِ — م ل ك B004 — «أملكنا فلانا فلانة إذا زوجناه إياها» (sihah); «الإملاك التزويج» (ayn) — the marriage contracted.
- 1:6 ٱهْدِنَا — ه د ي B004 — «الهدية ما أهديت إلى ذي مودة من بر» (ayn); «المهدى الطبق الذي يهدى عليه» (tahdhib) — a gift carried on its tray to a friend.
- 1:6 ٱهْدِنَا — ه د ي B007 — «الرجل الذي له حرمة كحرمة هدي البيت» (sihah); «الهدي الرجل ذو الحرمة وهو أن يأتي القوم يستجيرهم أو يأخذ منهم عهدا» (tahdhib) — the refugee, sacred like the offering.
- 1:2 رَبِّ — ر ب ب B011 — «الربابة: العهد والميثاق؛ الأربة أهل الميثاق» (sihah) — the covenant that protects him.
- 1:6 ٱهْدِنَا — ه د ي B001 — «هديته الطريق والبيت» (sihah) — showing the road and the house.
- Quran: 22:33–37 (the rites of the sacrificial animals) «ثم محلها إلى البيت العتيق ... ليذكروا اسم الله على ما رزقهم من بهيمة الأنعام ... فاذكروا اسم الله عليها صواف ... كذلك سخرها لكم لتكبروا الله على ما هداكم» — the offering, the name, the herd and guidance together. 2:196 «ولا تحلقوا رءوسكم حتى يبلغ الهدي محله». 5:95 «هديا بالغ الكعبة». 48:25 «والهدي معكوفا أن يبلغ محله». From memory: 5:2 «ولا الهدي ولا القلائد ولا آمين البيت الحرام». 2:189 «قل هي مواقيت للناس والحج».

## Interactions
- Trodden road / Made pliant: shared member ع ب د B005. Maqayis uses «المذلل» for the road («الطريق المعبد وهو المسلوك المذلل») and maqayis/sihah use it for the camel («البعير المعبد ... المذلل»). نَعْبُدُ is both the servant's word and the road's surface.
- Trodden road / Herd: ه د ي B003 is both the guide ahead on the road and the lead animals of a herd («هوادي الوحش متقدماتها الهادية لغيرها»). 16:5–9 moves from herds going out and coming home straight to «قصد السبيل ومنها جائر».
- Trodden road / Herd / Passing out of sight: ض ل ل B001/B003/B005 is the lost walker, the house he cannot find, and the camel without an owner. «كل جائر عن القصد ضال» meets «ومنها جائر» in 16:9. 7:179 «كالأنعام بل هم أضل».
- Herd / Made pliant: the dictionary joins the stray to the surah's two owner words, «لا يعرف ربها» and «لا يعرف لها مالك». 36:71–72 «فهم لها مالكون وذللناها لهم».
- Herd / Name and brand: و س م B001 «بعير موسوم وسم بسمة يعرف بها». The brand shows who owns the animal, and the stray is defined as the one whose owner «لا يعرف».
- Herd / Leaning and standing: م ل ك B008 «ملك الدابة قوائمها وهاديها». One phrase holds مَٰلِكِ and ٱهْدِنَا's root for the legs and neck that carry and steer a mount.
- Trodden road / Well-head: 28:22–24 stages both. Moses asks «أن يهديني سواء السبيل», reaches the water of Madyan, draws water and calls on «رب».
- Well-head / Leaning and standing: sihah «الماء ملك أمر أي يقوم به الأمر» and «قوام الأمر ملاكه» join م ل ك and ق و م. Water and a prop do the same work of keeping something standing.
- Well-head / Rain: ر ب ب B013 «الماء الكثير» and غ ي ر B001 «سقاهم». Gathered water and rain that sets things right are one supply.
- Rain / Herd: ح م د B002 «أحمدت الأرض إذا رضيت سكناها أو مرعاها». 80:25–32 «متاعا لكم ولأنعامكم».
- Rain / Womb and rearing: «الرباب: السحاب، سمي بذلك لأنه يرب النبات» uses the same verb as «رب فلان ولده». The cloud raises plants as a parent raises a child. 42:28 calls the rain His «رحمته».
- Womb and rearing / Favour completed: ر ب ب B002 holds both «رب فلان ولده» and «رب الرجل النعمة ... إذا تممها». mufradat «إلى حد التمام» covers child and favour alike. 17:24 «رب ارحمهما كما ربياني صغيرا».
- Favour completed / Trodden road: 48:2 «ويتم نعمته عليك ويهديك صراطا مستقيما» and 2:150 «ولأتم نعمتي عليكم ولعلكم تهتدون» stage a completed favour together with guidance on the road.
- Favour completed / Made pliant: 26:18–22. Pharaoh claims «ألم نربك فينا وليدا» and Moses answers «نعمة تمنها علي أن عبدت بني إسرائيل». The rearing, the favour held over him and the enslaving all fall in one exchange (ح م د B005 «يتحمد علي أي يمن»).
- Approval and anger / Day of reckoning: ي و م B004 «بما نزل بعاد وثمود ... من العذاب، وبالعفو عن آخرين». 88:2 and 88:8 «وجوه يومئذ» set the two faces on that day.
- Approval and anger / Trodden road: 20:81–82. «ومن يحلل عليه غضبي فقد هوى» is a fall, and «ثم اهتدى» is guidance. 19:58 joins «أنعم الله عليهم» with «هدينا».
- Day of reckoning / Debt and scale: د ي ن B002 «الجزاء والمكافأة» against B003, the loan. ق و م B013 against B015. 21:47 sets «الموازين القسط ليوم القيامة» and «مثقال».
- Debt and scale / Sun and sky: ق و م B017 «قام ميزان النهار فاعتدل» is the noon sun and a level balance in one phrase.
- Debt and scale / Passing out of sight: ض ل ل B004 is the forgetting that 2:282 guards against in a debt. ض ل ل B003 «ذهب دمه ضلة» is blood lost without the blood-money of غ ي ر B002.
- Sun and sky / Made pliant: ء ل ه B001 «الإلاهة الشمس ... لأن قوما كانوا يعبدونها» against «إِيَّاكَ نَعْبُدُ». 41:37 «لا تسجدوا للشمس ... إن كنتم إياه تعبدون».
- Sun and sky / Trodden road: 6:77 «لئن لم يهدني ربي لأكونن من القوم الضالين», said over the rising moon. 16:16 «وبالنجم هم يهتدون».
- Sun and sky / Name and brand: س م و B002 «سما لي شخص ارتفع حتى استثبته» and «سماوة الهلال». A shape rising into view and the crescent are one image.
- Name and brand / Led to the house: و س م B004 «موسم الحج ... معلم يجتمع فيه» joins وسم and علم. 22:34 «ليذكروا اسم الله على ما رزقهم من بهيمة الأنعام».
- Name and brand / Made pliant: 19:65 «فاعبده واصطبر لعبادته هل تعلم له سميا». 12:40 «ما تعبدون من دونه إلا أسماء سميتموها».
- Name and brand / Trodden road: ع ل م B002 «المعلم الأثر يستدل به على الطريق». The marker and the road meet in 16:16 «وعلامات وبالنجم هم يهتدون».
- Led to the house / Trodden road: ه د ي B001 «هديته الطريق والبيت». Showing the road and driving the offering to the House are the same act of leading.
- Leaning and standing / Trodden road: 67:22 «أفمن يمشي مكبا على وجهه أهدى أمن يمشي سويا على صراط مستقيم».
- Leaning and standing / Herd: ق و م B016 «قامت ... دابته إذا كلت» and ع ب د B011 «إذا كلت راحلته». The tired mount links the walker's halt to the animals.
- Passing out of sight / Trodden road: maqayis «السراط ... لأن الذاهب فيه يغيب» against «ضل الشيء إذا خفي وغاب».
- Passing out of sight / Well-head: 12:10 and 12:19, Joseph hidden in «غيابت الجب» and drawn out by a bucket. و ل ه B003 is the water lost in the desert.
- Womb and rearing / Herd: و ل ه B001 «ناقة واله ... على ولدها» and «الجمل إذا فقد ألافه». The parted mother and the camel cut off from its companions are one longing.

## Ayat
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
  - Name and brand: بِسْمِ is the name raised up (س م و B005/B001), a good name travelling (B008), a shape rising into view (B002), and the brand burned in (و س م B001). ٱللَّهِ is the name itself spoken in a call and an oath (ء ل ه B002). Scene: a thing is known by a mark raised up or burned in, such as a name, a brand, a banner or a mountain, and the created kinds (ٱلْعَٰلَمِينَ) are themselves marks.
  - Rain: بِسْمِ is the sky that is cloud, rain and plant (س م و B004), and the first rain branding the earth green (و س م B003). Scene: layered clouds stay (رَبِّ), the soft south wind blows (أَنْعَمْتَ), the first rain greens the land, water gathers, rain sets things right (غَيْرِ), and pasture is found good (ٱلْحَمْدُ).
  - Sun and sky: بِسْمِ is the crescent lifting off the horizon and the sky overhead. ٱللَّهِ carries «الإلاهة», the sun named for being worshipped. Scene: the day runs from sunrise to sunset (يَوْمِ), the noon sun stands (ٱلْمُسْتَقِيمَ), the moon moves through its stations (أَنْعَمْتَ) inside the sphere (ٱلْعَٰلَمِينَ), and the sun is worshipped against «إِيَّاكَ نَعْبُدُ».
  - Made pliant: ٱللَّهِ is the one worshipped («لأنه معبود»). Scene: the owner and master (رَبِّ، مَٰلِكِ), the one brought low and owned (ٱلدِّينِ), and the servant (نَعْبُدُ), whose pliant state is also a road trodden smooth and a tamed camel.
  - Womb and rearing: ٱلرَّحْمَٰنِ ٱلرَّحِيمِ is the womb as the child's house, the soreness after birth, kin from one womb, and tenderness to the weak. ٱللَّهِ, through the alternative و ل ه, is the mother parted from her child. Scene: womb, birth, the ewe kept for milk, a child raised stage by stage (رَبِّ), fed and guarded and kept in ease (غَيْرِ، أَنْعَمْتَ، ٱلْمُسْتَقِيمَ), and the reverse in the parted mother.
  - Favour completed: ٱلرَّحْمَٰنِ ٱلرَّحِيمِ is the tenderness that turns into doing good. Scene: a favour handed over (أَنْعَمْتَ), then finished (رَبِّ), answered with praise (ٱلْحَمْدُ), its reverse the favour held over the receiver.
  - Herd: ٱللَّهِ (و ل ه) is the camel that has lost its companions. بِسْمِ (و س م) is the owner's brand. Scene: owner, brand, lead animal, tamed camel and pasture, and the stray whose owner is unknown (ٱلضَّآلِّينَ).
  - Well-head and Passing out of sight: ٱللَّهِ (و ل ه B003) is water let out into the desert and lost. Scenes: a crossbeam and pulley over a full well, water that keeps a thing standing; and the road that takes its walker on out of sight against the one lost in the earth.
  - Trodden road: ٱللَّهِ (و ل ه B001) is land that leaves the walker bewildered. Scene: a smooth road, a guide ahead, a centre line, landmarks, and its reversals in the lost walker and the company that scatters.
  - Led to the house: بِسْمِ is the name spoken over the offering and the pilgrimage season (و س م B004). Scene: an offering, a bride, a gift and a refugee each led to the house where they belong.
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
  - Approval and anger: ٱلْحَمْدُ is praise against blame and finding something good. Scene: favour comes down on one people and anger on another, the same «عَلَيْهِمْ» after each, leaving soft faces with cooled eyes and red, frowning, swollen ones.
  - Favour completed: ٱلْحَمْدُ is the answer that names the gifts, and also the reverse, holding one's favour over the receiver. رَبِّ is finishing a favour and the favour itself (B002, B016). Scene: a favour handed over, finished, and thanked for, or held over the receiver.
  - Made pliant: رَبِّ is the obeyed master and owner of house and horse. لِلَّهِ is the one worshipped. Scene as at 1:1.
  - Womb and rearing: رَبِّ is raising the child, the step-parent, the newly delivered ewe, and the teacher who feeds knowledge in small parts. Scene as at 1:1.
  - Rain: رَبِّ is the layered cloud that rears the plants, the cloud and south wind staying, the herb green through summer, and plentiful water. ٱلْحَمْدُ is pasture found good. Scene as at 1:1.
  - Herd: رَبِّ is the owner of the stray («لا يعرف ربها»), the ground camels keep to, and the wild herd. ٱلْحَمْدُ is the pasture. Scene as at 1:1.
  - Well-head: ٱلْعَٰلَمِينَ is the deep, full well. رَبِّ is gathered water. Scene as at 1:1.
  - Name and brand: ٱلْعَٰلَمِينَ is the mark that sets a thing apart, the banner, and the kinds of creatures as marks. Scene as at 1:1.
  - Trodden road: ٱلْعَٰلَمِينَ is the trace and the mountain a traveller reads. Scene as at 1:1.
  - Sun and sky: ٱلْعَٰلَمِينَ is the sphere and what it holds. Scene as at 1:1.
  - Led to the house: رَبِّ is the covenant that protects the refugee. Scene as at 1:1.
  - Day of reckoning: «يوم يقوم الناس لرب العالمين» (mufradat under قيامة). Scene: a heavy day comes down, people rise before the king, and each is judged and repaid.
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
  - Womb and rearing, Favour completed and Rain carry the same senses as at 1:1. Here they come straight after رَبِّ ٱلْعَٰلَمِينَ: the womb and rearing next to the one who raises, the tenderness next to the finished favour, rain-mercy next to the cloud that rears plants. Scenes as at 1:1.
  - Day of reckoning: just before مَٰلِكِ يَوْمِ ٱلدِّينِ. 25:26 «الملك يومئذ الحق للرحمن» puts this name on the king of that day. Scene as at 1:2.
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
  - Day of reckoning: the whole scene is in this ayah. The dictionary itself glosses it: «الدين الحساب ومنه مالك يوم الدين». مَٰلِكِ is the king who commands and forbids. يَوْمِ is the heavy day that comes down. ٱلدِّينِ is judgment, account and repayment. Scene as at 1:2.
  - Made pliant: مَٰلِكِ is what the hand holds, slaves included. ٱلدِّينِ is «دانه ... أذله واستعبده ودينته ملكته», and also obedience. Scene as at 1:1.
  - Debt and scale: ٱلدِّينِ is the loan and the deferred sale, and repayment in full. Scene: credit until a term, a price, a full-weight coin on a scale that does not dip (ٱلْمُسْتَقِيمَ), blood-money in place of retaliation (غَيْرِ), and blood or memory that is lost (ٱلضَّآلِّينَ).
  - Herd: مَٰلِكِ is the owner of the stray («لا يعرف لها مالك») and the lead animal the rest follow. Scene as at 1:1.
  - Trodden road: مَٰلِكِ is the middle of the road to keep to. ٱلدِّينِ is the familiar way one keeps going. Scene as at 1:1.
  - Well-head: مَٰلِكِ is water as what keeps affairs standing («الماء ملك أمر»). Scene as at 1:1.
  - Leaning and standing: مَٰلِكِ is the wall that holds together and the heart that holds the body. Scene: the mount gives out, the weak man walks between two, help is asked, and the body stands upright and walks calmly.
  - Sun and sky: يَوْمِ is the span from sunrise to sunset. Scene as at 1:1.
  - Approval and anger: يَوْمِ is «أيام الله», days of punishment coming down and of pardon. Scene as at 1:2.
  - Led to the house: مَٰلِكِ is the marriage contracted before the bride is brought. Scene as at 1:1.
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
  - Made pliant: نَعْبُدُ is the servant lowering himself, the owned person, the one made pliant, and the road and camel made pliant. Tahdhib glosses this very ayah: «إياك نعبد إياك نطيع الطاعة التي نخضع معها». Scene as at 1:1.
  - Trodden road: نَعْبُدُ is the road beaten smooth, and in reverse «العباديد», groups going off along different roads. Scene as at 1:1.
  - Leaning and standing: نَسْتَعِينُ is asking for a back to lean on. نَعْبُدُ is the rider stranded when his mount gave out, and firmness. Scene as at 1:4.
  - Herd: نَعْبُدُ is the tarred, tamed camel. نَسْتَعِينُ is the wild-ass herd. Scene as at 1:1.
  - Sun and sky: إِيَّاكَ نَعْبُدُ stands against the sun worshipped («الإلاهة»). Scene as at 1:1.
  - Led to the house: نَعْبُدُ is the act of worship the offering serves and the tamed beast being led. Scene as at 1:1.
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
  - Trodden road: ٱهْدِنَا is showing the road and the house, the guide walking ahead, and going someone's way without turning off. ٱلصِّرَٰطَ is the road («الطريق المستقيم»). ٱلْمُسْتَقِيمَ is its straight line and the company that walks it. Scene as at 1:1.
  - Passing out of sight: ٱلصِّرَٰطَ is the road that takes its walker on out of view, a passing like swallowed food. Scene: going out of sight to where one belongs, against vanishing where no one knows (ٱلضَّآلِّينَ).
  - Leaning and standing: ٱهْدِنَا is walking propped between two men, the weak man, and the calm gait. ٱلْمُسْتَقِيمَ is rising upright, the prop, and the mount stopping dead. Scene as at 1:4.
  - Herd: ٱهْدِنَا is the lead animals and the necks of horses. Scene as at 1:1.
  - Led to the house: ٱهْدِنَا is the offering driven to the Sanctuary, the bride brought, the gift carried, the refugee made sacred. Scene as at 1:1.
  - Day of reckoning: ٱلْمُسْتَقِيمَ is «القيامة», creation rising to its feet, and «القيوم». Scene as at 1:2.
  - Debt and scale: ٱلْمُسْتَقِيمَ is the price, the full-weight coin and the day's level balance. Scene as at 1:4.
  - Sun and sky: ٱلْمُسْتَقِيمَ is the sun standing at noon. Scene as at 1:1.
  - Well-head: ٱلْمُسْتَقِيمَ is the pulley hung from the crossbeam («النعامة الخشبة المعترضة ثم تعلق القامة») and what keeps one standing. Scene as at 1:1.
  - Womb and rearing: ٱلْمُسْتَقِيمَ is the one who keeps the household going. Scene as at 1:1.
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ
  - Trodden road: صِرَٰطَ is the road as one company's track. أَنْعَمْتَ is the beaten main track and going on foot. ٱلضَّآلِّينَ is the walker who cannot find the road or the house. أَنْعَمْتَ also holds «شالت نعامتهم», the company scattering. Scene as at 1:1.
  - Approval and anger: أَنْعَمْتَ عَلَيْهِمْ is favour coming down and the word of approval, with the soft face and cooled eye. ٱلْمَغْضُوبِ عَلَيْهِمْ is anger against approval: the blood rising, the red, frowning, swollen face. Scene as at 1:2.
  - Favour completed: أَنْعَمْتَ is good reaching another, made more and finished. Scene as at 1:1.
  - Herd: ٱلضَّآلِّينَ is the stray camel «لا يعرف ربها» and the camel that slipped loose. أَنْعَمْتَ is the camels as wealth. Scene as at 1:1.
  - Passing out of sight: ٱلضَّآلِّينَ is the hidden, the buried, milk lost in water, the one gone «إذا لم يدر أين ذهب», the memory that slips. صِرَٰطَ is the road that takes its walker on. Scene as at 1:6.
  - Debt and scale: غَيْرِ is blood-money and exchange. ٱلضَّآلِّينَ is blood left unpaid and the witness who forgets. Scene as at 1:4.
  - Womb and rearing: غَيْرِ is provisioning the family and jealous guarding of the household. أَنْعَمْتَ is children raised in ease. Scene as at 1:1.
  - Rain: أَنْعَمْتَ is the wet south wind and fresh green living. غَيْرِ is rain that sets things right and gives drink. Scene as at 1:1.
  - Well-head: أَنْعَمْتَ is the crossbeam over the well. غَيْرِ is giving drink. Scene as at 1:1.
  - Sun and sky: أَنْعَمْتَ is a station of the moon. Scene as at 1:1.
  - Led to the house: أَنْعَمْتَ is the herd the offering is taken from («ما يهدى إلى الحرم من النعم»). Scene as at 1:1.
  - Day of reckoning: ٱلْمَغْضُوبِ is the requital («فالمراد به الانتقام»). Scene as at 1:2.

