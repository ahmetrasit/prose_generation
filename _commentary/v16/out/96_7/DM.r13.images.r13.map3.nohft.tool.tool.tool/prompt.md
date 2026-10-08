Focus: 96:7. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/96_7/D.r13/context.md =====
# 96:7 — focus

أَن رَّءَاهُ ٱسْتَغْنَىٰٓ

Anchor translation (canonical reading, reference only):

Kendisini yeterli gördüğü için.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | أَن | أَن |  | SUB |
| 2 | رَّءَاهُ | رَءَا | ر ء ي | V;PRON |
| 3 | ٱسْتَغْنَىٰٓ | ٱسْتَغْنَىٰ | غ ن ي | V |


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
- 96:7 ◀ focus أَن رَّءَاهُ ٱسْتَغْنَىٰٓ
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
- 96:19 كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩


===== _commentary/v16/work/96_7/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ر ء ي (root_000531) — identity root of رَّءَاهُ (w2)

- **B001** gözle ya da içsel kavrayışla görme — gözle ya da içsel kavrayışla görmek · görme, gözle algılama · kendi gözüyle görme · yeni ayı görebilmek için dikkatle bakmaya çalıştık
  نظر وإبصار بعين أو بصيرة (maqayis)؛ رأيت بعيني رؤية ورأيته رأي العين (ayn;tahdhib)؛ الرؤية بالعين (sihah)؛ الرؤية إدراك المرئي بالحاسة (mufradat)
- **B002** düşünüp bir görüşe varma — bilmek, sanmak veya öyle olduğuna inanmak · görüş, kanı veya değerlendirme · düşünüp taşınmak ve bir görüşe varmak · ağır ağır ve dikkatle düşünme · bir görüşe varmak için düşünme · adamın görüşünü sordu · onunla görüş alışverişinde bulundu · gözle gördüğünün gereğince öyle sandı
  الرأي ما يراه الإنسان في الأمر (maqayis)؛ الرأي رأي القلب (ayn;tahdhib)؛ بمعنى العلم تتعدى إلى مفعولين ورأى في الفقه رأيا (sihah)؛ الرأي اعتقاد النفس والروية والتروية التفكر (mufradat)؛ استرأيت الرجل في الرأي أي استشرته (tahdhib)
- **B003** uykuda görülen düş — uykuda görülen düş · uykuda görülen düşler
  الرؤيا معروفة والجمع رؤى (maqayis)؛ رأيت رؤيا حسنة (ayn)؛ رأى في منامه رؤيا وجمع الرؤيا رؤى (sihah)؛ لا تجمع الرؤيا وتجمع الرؤيا رؤى (tahdhib)؛ الرؤيا ما يرى في المنام (mufradat)
- **B004** karşı karşıya gelip görünür olma — topluluk birbirini gördü · görünmek üzere karşıma çıktı · birbirine bakar ve karşılıklı konumda
  تراءى القوم إذا رأى بعضهم بعضا (maqayis)؛ تراءى القوم رأى بعضهم بعضا وتراءى لي فلان (ayn)؛ قوم رئاء وبيوتهم رئاء وتراءى الجمعان (sihah)؛ تراءينا أي تلاقينا فرأيته ورآني وداري ترى دار فلان (tahdhib)؛ تراءا الجمعان أي تقاربا وتقابلا ومنازلهم رئاء (mufradat)
- **B005** başkaları görsün diye yapma — başkaları görsün diye yapma · işini başkalarına gösteriş için yaptı · gösteriş yapmaya zorlandı veya özendi
  وراءى فلان يرائي وفعل ذلك رئاء الناس وهو أن يفعل شيئا ليراه الناس (maqayis)؛ فلان مراء والاسم الرياء وفعل ذلك رياء وسمعة (sihah)؛ يرآءون الناس إذا أبصرهم الناس صلوا وإذا لم يروهم تركوا الصلاة (tahdhib)؛ فعل ذلك رئاء الناس أي مراءاة (mufradat)
- **B006** görünüş, belirti ve yansıtıcı yüzey — ayna · aynada yüzüne baktı · güzel ve parlak dış görünüş · göze güzel görünen durum veya donanım · yüzde beliren budalalık belirtisi
  الرئي ما رأت العين من حال حسنة والرواء حسن المنظر والمرآة معروفة (maqayis)؛ المرآة التي ينظر فيها والري ما أريت القوم من حسن الشارة والهيئة والرواء حسن المنظر (ayn)؛ المرآة التي ينظر فيها والمرآة المنظر الحسن والرواء حسن المنظر ورأوة الحمق (sihah)؛ الرئي المنظر والرواء حسن المنظر والمرآة التي ينظر فيها ورأوة أي نظرة ودمامة (tahdhib)؛ المرآة ما يرى فيه صورة الأشياء (mufradat)
- **B007** aybaşı sonu izi ve denetleme bezi — aybaşı sonrası hafif sarı, beyaz veya bulanık iz · aybaşı belirtisi olarak görülen iz
  الترئية والترية ما تراه الحائض من صفرة بعد دم حيض أو أمارات الحيض (maqayis)؛ الترية الخرقة التي تعرف بها المرأة حيضها من طهرها والماء الأصفر عند انقطاع الدم (jamhara)؛ الترية الشيء الخفي اليسير من الصفرة والكدرة (sihah)؛ الترية ما تراه المرأة من بقية حيضها من صفرة أو بياض (tahdhib)
- **B008** kişiye görünen görünmez yoldaş — kişiye alışıp onunla ilişki kuran görünmez varlık · görünmez yoldaşı ona göründü
  الرئي جني يتعرض للرجل يريه كهانة وطبا (ayn)؛ به رئي من الجن أي مس (sihah)؛ رئي من الجن وهو الذي يعتاد الإنسان من الجن وأرأى إذا صار له رئي من الجن (tahdhib)؛ مع فلان رئي من الجن (mufradat)
- **B009** akciğer ve ona gelen zarar — akciğer · akciğerine vurdu veya sapladı · akciğerinden yakındı
  الرئة موضع الريح والنفس وجمعها الرئات والرئين (ayn)؛ الرئة مهموزة وتجمع على رئين ورأيته أي أصبت رئته (sihah)؛ أرأى إذا اشتكى رئته (tahdhib)؛ الرئة العضو المنتشر عن القلب ورئته إذا ضربت رئته (mufradat)
- **B010** meme gelişmesiyle gebeliğin belli olması — dişi devenin gebeliği memesi gelişince belli oldu · dişi koyunun gebeliği memesi büyüyünce belli oldu
  أرأت الناقة إذا أرأى ضرعها أنها أقربت وأنزلت (ayn)؛ أرأت الشاة إذا عظم ضرعها قبل ولادها (sihah)؛ إذا استبان حمل الشاة وعظم ضرعها قيل أرأت (tahdhib)؛ أرأت الناقة إذا أظهرت الحمل حتى يرى صدق حملها (mufradat)
- **B011** görünür yere dikilen bayrak — dikili bayrak veya görünür işaret · bayrağı dikti
  الراية من رايات الأعلام (ayn)؛ الراية العلم لا تهمزها العرب وأصلها الهمز (tahdhib)؛ الراية العلامة المنصوبة للرؤية (mufradat)
- **B012** gösterip görmesini sağlama — bakması için aynayı ona tuttu · ona gösterip görmesini sağladı · ver, uzat · Tanrı onu düşmanını sevindirecek bir duruma düşürdü
  أرني يا فلان ثوبك لأراه وأرنا للمعاطاة (ayn)؛ أريته الشيء فرآه (sihah)؛ رأيت الرجل ترئية إذا أمسكت له المرآة لينظر فيها وأرى الله الناس بفلان (tahdhib)؛ أرنا وبما أراك الله أي بما علمك (mufradat)
- **B013** söyler misin, bir düşün — söyler misin, bir düşün · söyleyin bakalım, bir düşünün
  أرأيتك وأنت تقول أخبرني (tahdhib)؛ يجري أرأيت مجرى أخبرني وكل ذلك فيه معنى التنبيه (mufradat)

## غ ن ي (root_001110) — identity root of ٱسْتَغْنَىٰٓ (w3)

- **B001** maddi bolluk ve ihtiyaçtan bağımsızlık — maddi zenginlik, bolluk ve ihtiyaçsızlık · varlıklı, zengin · zenginleşmek veya başkasına ihtiyaç duymayacak duruma gelmek · ona ihtiyaç duymamak · onunla yetinip başka bir şeye ihtiyaç duymamak · bir şeye ihtiyaç duymama durumu · zenginlik ve bolluk · gönül tokluğu ve az şeye ihtiyaç duyma · zengin etmek veya yoksunluğunu gidermek · Kur'an'la yetinip başka bir şeye ihtiyaç duymamak
  الغنى في المال (maqayis;tahdhib)؛ الغنى مقصور في المال واستغنى الرجل أصاب غنى (ayn;tahdhib)؛ الغنى مقصور اليسار وتغنى الرجل أي استغنى (sihah)؛ الغني ذو الوفر (ayn;tahdhib)؛ عدم الحاجات وقلة الحاجات وكثرة القنيات (mufradat)؛ تغنيت وتغانيت بمعنى استغنيت (maqayis;tahdhib)
- **B002** ihtiyacı karşılayıp yarar sağlama ve yerini tutma — yeterlilik, ihtiyacı karşılama ve yarar · onun yerine yetmek, ihtiyacını karşılamak ve yarar sağlamak · bu sana yetmez ve yarar sağlamaz · yeterli ve ihtiyacı karşılayan · birinin yerini tutan yeterlilik ve işlev · zararını benden uzak tut
  الغناء بالفتح الكفاية ولا يغني أي لا يكفي (maqayis)؛ الغناء الاستغناء والكفاية ورجل مغن أي مجزئ (ayn)؛ ما يغني عنك هذا أي ما يجزئ وما ينفع والغناء بالفتح النفع (sihah)؛ الإجزاء والكفاية ورجل مغن أي مجزئ كاف (tahdhib)؛ أغناني كذا وأغنى عنه كذا إذا كفاه (mufradat)
- **B003** sesle ezgi söyleme, dinleme ve ezgili okuma — şarkı söyleme, ezgili seslendirme ve dinleti · şarkı; ezgili söylenen parça · şarkı söylemek · şarkı söylemek veya sesi ezgili ve duygulu kullanmak · Kur'an'ı hüzünlü, yumuşak ve ezgili bir sesle okumak
  الغناء من الصوت والأغنية اللون من الغناء (maqayis)؛ الغناء ممدود في الصوت وغنى يغني أغنية وغناء (ayn)؛ الأغنية الغناء والجمع الأغاني والغناء بالكسر من السماع (sihah)؛ الغناء الصوت ممدود والتطريب وتحزين القراءة وترقيقها (tahdhib)؛ غنى أغنية وغناء (mufradat)
- **B004** bir yerde uzun süre kalıp yaşama — bir yerde oturmak ve uzun süre kalmak · sanki daha dün orada hiç yaşamamıştı · bir topluluğun oturduğu evler ve yurtlar · oturma eylemi veya oturulan yer
  غني القوم في دارهم أقاموا ومغانيهم منازلهم (maqayis)؛ غني القوم في المحلة طال مقامهم فيها وكأن لم يغن بالأمس أي كأن لم يكن (ayn)؛ غنى بالمكان أي أقام وغني أي عاش والمغنى واحد المغاني (sihah)؛ غني القوم في دارهم إذا طال مقامهم والمغاني المنازل (tahdhib)؛ غنى في مكان كذا إذا طال مقامه فيه والمغنى للمصدر وللمكان (mufradat)
- **B005** süsten bağımsız sayılan; bazen genç, güzel veya evli kadın — eşi veya güzelliği sayesinde süse ihtiyaç duymadığı düşünülen; ayrıca genç, güzel ya da evli kadın · bu niteliklerle anılan kadınlar; bazı kullanımlarda genç, güzel, evli ya da genel olarak kadınlar
  الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي (maqayis)؛ الغانية الشابة المتزوجة غنيت بزوجها وغنيت بجمالها عن الزينة (ayn)؛ الغانية الجارية التي غنيت بزوجها وقد تكون التي غنيت بحسنها وجمالها (sihah)؛ الغواني ذوات الأزواج أو الشواب أو الجارية الحسناء أو كل امرأة (tahdhib)؛ الغانية المستغنية بزوجها عن الزينة أو بحسنها عن التزين (mufradat)
- **B006** evlenme ve evlendirme — evlenme; bekâr kişi için koruyucu sayılan evlilik · gelinleri evlendirme
  الأغناء إملاكات العرائس (tahdhib)؛ الغنى التزويج (tahdhib)؛ الغنى حصن للعزب أي التزويج (tahdhib)

## ECHO ر و ي (root_000615) — for رَّءَاهُ (w2): withheld observed target; not identity

- **B001** suya kanma ve susuzluğun giderilmesi — susuzluğu sona erinceye kadar su içmek · suya kanmak · suya kanmışlık; susuzluğun sona ermesi · suya kanmış, susuzluğu kalmamış · tatlı ve içeni iyice kandıran bol su · bol sulu pınar
  خلاف العطش (maqayis)؛ رويت من الماء ريا وارتويت وترويت (sihah)؛ روي فلان من الماء يروى ريا فهو ريان (tahdhib)؛ ماء رواء وروى (sihah;tahdhib;mufradat)؛ عين رية (sihah)
- **B002** başkaları için su çekip getirme — ailesine su getirip taşımak · topluluk için su çekmek · su çekmede kullanılan yük hayvanı veya su çeken kişi · su taşımaya yarayan büyük tulum · su taşıma işini meslek edinen kimse · hacıların sonraki günler için su tedarik ettiği gün
  رويت على أهلي أروي ريا (maqayis;sihah;tahdhib)؛ رويت القوم أرويهم إذا استقيت لهم (sihah;tahdhib)؛ الراوية البعير أو البغل أو الحمار الذي يستقى عليه (sihah)؛ الراوية هو البعير الذي يستقى عليه الماء والرجل المستقي أيضا راوية (tahdhib)؛ يوم التروية سمي به لأنهم يرتوون فيه من الماء (sihah;tahdhib)
- **B003** anlatı veya şiir aktarma — anlatıyı veya şiiri aktarmak · anlatı veya şiir aktaran kimse · çok sayıda şiir ya da anlatı aktaran kimse · birine şiiri tekrar ederek ezberletmek
  رويت الحديث والشعر رواية فأنا راو (sihah)؛ روى فلان حديثا وشعرا يرويه رواية فهو راو (tahdhib)؛ روى فلان فلانا شعرا إذا رواه له حتى حفظه للرواية عنه (tahdhib)؛ الذي يأتي القوم بعلم أو خبر فيرويه كأنه أتاهم بريهم من ذلك (maqayis)
- **B004** enine boyuna düşünüp değerlendirme — enine boyuna düşünme; değerlendirme · bir mesele üzerinde düşünüp değerlendirmek
  الرَّوِيَّة التفكر في الأمر (sihah)؛ رويت في الأمر إذا نظرت فيه وفكرت (sihah)؛ روأت في الأمر وريأت فكرت (tahdhib)
- **B005** birinden beklenen ihtiyaç veya talep [kalıp] — birinden beklenen ihtiyaç veya talep
  لنا قبلك روية أي حاجة (sihah)؛ لنا عند فلان روية وأشكلة وهما الحاجة (tahdhib)
- **B006** geriye kalan bölüm veya miktar — borçtan ya da başka bir şeyden kalan miktar
  الرَّوِيَّة البقية من الدين ونحوه (sihah)؛ بقيت منه روية أي بقية مثل التلية (tahdhib)
- **B007** yük bağlama ipi — yükü veya su tulumlarını yük hayvanına bağlayan ip · yükü veya su tulumlarını özel iple hayvana bağlamak · su tulumlarını yük hayvanına bağlayan ip
  الرِّوَاء حبل يشد به المتاع على البعير (sihah)؛ رويته على الرجل إذا شددته على ظهر البعير (sihah)؛ الرِّوَاء الحبل الذي يروى به على الراوية إذا عكمت المزادتان (tahdhib)؛ يقال له المروى وجمعه مراوى (tahdhib)
- **B008** yapıya göre dolgunlaşma veya suya kavuşma [kalıp] — ipin lifleri kalınlaşıp bükümü sıkılaşmak · eklemler dengeli ve dolgun hale gelmek · sırtı semirip dolgunlaşmış at · kurak yere dikildikten sonra kökten sulanmak
  ارتوى الحبل غلظت قواه (sihah)؛ ارتوت مفاصل الرجل اعتدلت وغلظت (sihah)؛ ارتوت مفاصل الدابة إذا اعتدلت وغلظت (tahdhib)؛ فرس ريان الظهر إذا سمن متناه (tahdhib)؛ ارتوت النخلة إذا غرست في قفر ثم سقيت في أصلها (tahdhib)
- **B009** hoş ve güzel dış görünüş — hoş dış görünüş; görünen güzellik · kökeni tartışmalı bir görünüş güzelliği biçimi
  رجل له رُوَاء أي منظر (sihah)؛ من لم يهمز رئيا جعله من روي كأنه ريان من الحسن (mufradat)
- **B010** hoş koku — hoş koku; bir şeyin güzel kokusu
  طيبة الرِّيَا إذا كانت عطرة الجرم (tahdhib)؛ ريا كل شيء طيب رائحته (tahdhib)
- **B011** dişi dağ keçisi — dağ keçisi; özellikle dişisi, bazı kullanımlarda erkeği de · çok sayıda dağ keçisi; dağ keçileri topluluğu · kadın adı
  الإِرْوِيَّة الأنثى من الوعول (sihah)؛ أروى أيضا اسم امرأة (sihah)؛ الأُرْوِيَّة الأنثى من الوعول (tahdhib)؛ يقال للأنثى أروية وللذكر أروية (tahdhib)؛ لا تجمع بين الأروى والنعام (tahdhib)
- **B012** bayrak — bayrak; sancak
  الرَّايَة العلم (sihah)
- **B013** temel uyak harfi — şiir boyunca değişmeyen temel uyak harfi
  الرَّوِيّ حرف القافية (sihah)؛ قصيدتان على روي واحد (sihah)
- **B014** iri damlalı güçlü yağmur bulutu — iri damlalı, sert yağan yağmur bulutu
  الرَّوِيّ سحابة عظيمة القطر شديدة الوقع (sihah)
- **B015** topluluğun ağır yükümlülüklerini üstlenen ileri gelenler — topluluk adına kan bedeli ve ağır yükümlülükleri üstlenen ileri gelenler
  يقال لسادة القوم الروايا (tahdhib)؛ شبه السيد الذي تحمل الديات عن الحي بالبعير الراوية (tahdhib)؛ روايا الثقل حوامل ثقل الديات (tahdhib)

===== _commentary/v16/out/s096/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 96:7, and ## Buluşmalar) =====
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

## Tutunmak ve kendini yeterli görmek

İnsan, tutunan bir şeyden yaratılmıştır. Alak kökü asılmayı ve yapışmayı adlandırır: {ar:يناط الشيء بالشيء العالي, tr:yunâtu'ş-şey'u bi'ş-şey'i'l-ʿâlî, gloss:bir şeyin yüksekteki bir şeye asılması, source:"ع ل ق,B001"}; {ar:علق بالشيء نشب به, tr:ʿalika bi'ş-şey'i neşibe bih, gloss:bir şeye takıldı, ona yapıştı, source:"ع ل ق,B001"}. Aynı kök suya yapışan sülüğü de adlandırır: {ar:دويبة في الماء تجمع على علق, tr:duveybetun fi'l-mâ', gloss:suda yaşayan küçük bir hayvan; çoğulu alaktır, source:"ع ل ق,B003"}. Ayrıca canı ayakta tutan en az lokmayı adlandırır: {ar:ما يأكل فلان إلا علقة أي ما يمسك نفسه, tr:mâ ye'kulu fulânun illâ ʿulka, gloss:falan ancak canını tutacak kadar yer, source:"ع ل ق,B006"}. İnsanın başlangıcı yüksekteki bir şeye asılı, tutunarak ve azla yaşayan bir şeydir.

Beşinci ayet bu eksik varlığa öğretilen şeyi anar: bilmediği şey ona verilir. Yedinci ayet sonra tersine döner: insan kendini {ar:ٱسْتَغْنَىٰٓ, tr:istagnâ, gloss:muhtaç olmayan, yeterli, source:96:7} görür. Kök ihtiyaçsızlığı adlandırır: {ar:عدم الحاجات وقلة الحاجات وكثرة القنيات, tr:ʿademu'l-hâcât ve killetu'l-hâcât ve kesretu'l-kunyât, gloss:ihtiyaçların olmaması, azlığı ve edinilmiş şeylerin çokluğu, source:"غ ن ي,B001"}. Aynı kök bir şeyin yetip yetmemesini de anlatır: {ar:ما يغني عنك هذا أي ما يجزئ وما ينفع, tr:mâ yugnî ʿanke hâzâ, gloss:bu sana yetmez, fayda vermez, source:"غ ن ي,B002"}. Kökte kendine bakışla yeterliliği tek figürde birleştiren bir kadın da vardır: {ar:الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي, tr:el-gâniye, gloss:gâniye, kocası ya da güzelliği sayesinde süs takmaya ihtiyaç duymayan kadındır, source:"غ ن ي,B005"}. Yedinci ayetteki "kendini görmek" ile "yeterli olmak" bu figürde bir araya gelir.

Kurân bu kelimeyi birkaç sahnede inkârla birleştirir: {ar:وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ, tr:ve emmâ men bahile ve'stagnâ, gloss:cimrilik eden ve kendini muhtaç görmeyene gelince, source:92:8}, {ar:وَكَذَّبَ بِٱلْحُسْنَىٰ, tr:ve kezzebe bi'l-husnâ, gloss:ve en güzeli yalanlayan, source:92:9}. Peygamber'e, kendini yeterli gören zengin kişiye yönelmesi hatırlatılır: {ar:أَمَّا مَنِ ٱسْتَغْنَىٰ, tr:emmâ meni'stagnâ, gloss:kendini muhtaç görmeyene gelince, source:80:5}, {ar:فَأَنتَ لَهُۥ تَصَدَّىٰ, tr:fe ente lehû tesaddâ, gloss:sen ona yöneliyorsun, source:80:6}. Gerçek yeterliliğin kime ait olduğu da söylenir. Elçilerini reddedenler için {ar:فَكَفَرُوا۟ وَتَوَلَّوا۟ وَّٱسْتَغْنَى ٱللَّهُ, tr:fe keferû ve tevellev vestagna'llâh, gloss:inkâr ettiler ve yüz çevirdiler, Allah da onlara ihtiyaç duymadı, source:64:6} denir. Tüm insanlara da {ar:أَنتُمُ ٱلْفُقَرَآءُ إِلَى ٱللَّهِ وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:entumu'l-fukarâ'u ila'llâh, va'llâhu huve'l-ganiyyu'l-hamîd, gloss:Allah'a muhtaç olanlar sizsiniz, ihtiyaçsız ve övülmeye layık olan Allah'tır, source:35:15} denir. Hesap gününde ise yeterlilik iddiası kendi ağzından çöker: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ, tr:mâ agnâ ʿannî mâliyeh, gloss:malım bana hiçbir yarar sağlamadı, source:69:28}.

Rab kelimesinin ailesinde ihtiyaç ile nimet tek kelimede birleşir: {ar:الربى: الحاجة؛ … الربى: النعمة والإحسان, tr:er-rubbâ: el-hâce … er-rubbâ: en-niʿmetu ve'l-ihsân, gloss:rubbâ ihtiyaçtır; rubbâ nimet ve iyiliktir da, source:"ر ب ب,B016"}. Üçüncü ayetteki en cömert sıfatı ihtiyacı gideren vericiyi anlatır: {ar:الكثير الخير الجواد المنعم المفضل, tr:el-kesîru'l-hayr el-cevâdu'l-munʿim, gloss:hayrı çok, cömert, nimet veren, lütfeden, source:"ك ر م,B001"}. Kurân insanın bu cömertliğe nasıl karşılık verdiğini anlatır: {ar:فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ, tr:fe ekramehû ve naʿʿamehû fe yekûlu rabbî ekramen, gloss:Rabbi ona ikram edip nimet verince "Rabbim bana ikram etti" der, source:89:15}. Hemen ardından rızkı daraltılınca {ar:فَيَقُولُ رَبِّىٓ أَهَٰنَنِ, tr:fe yekûlu rabbî ehânen, gloss:"Rabbim beni aşağıladı" der, source:89:16}. Kısacası insan, ikramı kendi değerinin kanıtı sayar.

On beşinci ayetteki {ar:يَنتَهِ, tr:yentehi, gloss:vazgeçer, source:96:15} fiilinin ailesinde "yeter" anlamı vardır: {ar:فلان ناهيك من رجل… كما يقال حسبك, tr:fulânun nâhîke min racul, gloss:falan sana yeter bir adamdır, "hasbuk" dendiği gibi, source:"ن ه ي,B005"}. Onuncu ayetin kulu ise kendine ait bir şeyi olmayandır: {ar:العبد وهو المملوك, tr:el-ʿabdu ve huve'l-memlûk, gloss:kul, sahip olunandır, source:"ع ب د,B001"}. Sekizinci ayetteki dönüş, yeterlilik iddiasını geçersiz kılar: asılı başlayan varlık, asıl olduğu yere döner.

Kaynaklar: 96:2 عَلَقٍ ع ل ق B001; 96:2 عَلَقٍ ع ل ق B003; 96:2 عَلَقٍ ع ل ق B006; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B001; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B002; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B005; 96:1 رَبِّكَ ر ب ب B016; 96:3 ٱلْأَكْرَمُ ك ر م B001; 96:15 يَنتَهِ ن ه ي B005; 96:10 عَبْدًا ع ب د B001

## Yol: doğru yolda olmak, sapmak, dönmek, yaklaşmak

Bir yolcu yoldadır. Hedefi ıskalayabilir, yönünden sapabilir ya da sırtını dönüp kaçabilir. Sonunda herkes başladığı yere döner ve yolun bir varış noktası vardır. On birinci ayetin {ar:عَلَى ٱلْهُدَىٰٓ, tr:ʿale'l-hudâ, gloss:doğru yol üzerinde, source:96:11} ifadesi yolcuyu yolun üzerinde gösterir: {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytuhu't-tarîk, gloss:ona yolu ve evi gösterdim, yani tanıttım, source:"ه د ي,B001"}; {ar:الهداية دلالة بلطف, tr:el-hidâye delâletun bi lutf, gloss:hidayet, incelikle yol göstermektir, source:"ه د ي,B001"}. Kök sakin bir yürüyüşü de adlandırır: {ar:لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن, tr:lem yusriʿ isrâʿa'l-munhezim, gloss:bozguna uğrayan gibi koşmadı, sükûnet ve güzel bir yürüyüşle gitti, source:"ه د ي,B010"}. Kurân yolcuları karşılaştırır: {ar:أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ, tr:e fe men yemşî mukibben ʿalâ vechihî ehdâ em men yemşî seviyyen ʿalâ sırâtın mustakîm, gloss:yüzüstü kapanarak yürüyen mi daha doğru yoldadır, yoksa dosdoğru bir yolda dimdik yürüyen mi, source:67:22}. Bu ayette yüz, yolun karşısında bir yürüyüş biçimi olarak geçer; bu da perçem sahnesine yakındır.

On altıncı ayetin günahkâr kelimesi yönden sapmaktır: {ar:الخطأ العدول عن الجهة, tr:el-hata'u'l-ʿudûlu ʿani'l-cihe, gloss:hata yönden sapmaktır, source:"خ ط ء,B001"}. On üçüncü ayetin yüz çevirme fiili, bedenle ya da dinlememekle sırt dönmektir: {ar:التولي قد يكون بالجسم وقد يكون بترك الإصغاء والائتمار, tr:et-tevellî kad yekûnu bi'l-cism, gloss:yüz çevirmek bedenle de olur, dinlememek ve emre uymamakla da, source:"و ل ي,B007"}. Aynı kök kesintisiz yakınlığı da adlandırır: {ar:الولي القرب والدنو, tr:el-velyu'l-kurbu ve'd-dunuvv, gloss:vely yakınlık ve yaklaşmaktır, source:"و ل ي,B001"}. Böylece yüz çevirmek, yakınlığın tersine çevrilmiş halidir. Yalanlama fiilinin ailesinde saldırıda duraksamak da vardır: {ar:حمل فلان ثم كذب أي لم يصدق في الحملة, tr:hamele fulânun summe kezeb, gloss:falan saldırdı, sonra geri durdu, yani saldırısında sözünü tutmadı, source:"ك ذ ب,B004"}.

Sekizinci ayetin dönüşü başlangıca dönüştür: {ar:الرجوع العود إلى ما كان منه البدء, tr:er-rucûʿu'l-ʿavdu ilâ mâ kâne minhu'l-bed', gloss:dönüş, başlangıcın olduğu yere geri gelmektir, source:"ر ج ع,B001"}. Bu başlangıç, ilk iki ayetin yaratmasıdır. Kurân dönüşü yaratılışın başlangıcına bağlar: {ar:إِلَيْهِ مَرْجِعُكُمْ جَمِيعًا, tr:ileyhi merciʿukum cemîʿâ, gloss:hepinizin dönüşü O'nadır, source:10:4}, {ar:إِنَّهُۥ يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ, tr:innehû yebde'u'l-halka summe yuʿîduh, gloss:O yaratmayı başlatır, sonra onu geri getirir, source:10:4}; {ar:كَمَا بَدَأَكُمْ تَعُودُونَ, tr:kemâ bede'ekum teʿûdûn, gloss:sizi başlattığı gibi döneceksiniz, source:7:29}. İnsanın yolu da Rab'be doğru bir uğraş olarak tanımlanır: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًا فَمُلَٰقِيهِ, tr:yâ eyyuhe'l-insânu inneke kâdihun ilâ rabbike kedhan fe mulâkîh, gloss:ey insan, sen Rabbine doğru zahmetle çabalıyorsun ve O'na kavuşacaksın, source:84:6}. Dönmeyeceğini sanan kişi de anlatılır: {ar:إِنَّهُۥ ظَنَّ أَن لَّن يَحُورَ, tr:innehû zanne en len yahûr, gloss:o asla geri dönmeyeceğini sanmıştı, source:84:14}. Yedinci ayetin yeterlilik kökü bu sanıyı yere yerleşmekle de anlatır: {ar:غني القوم في دارهم أقاموا, tr:ganiye'l-kavmu fî dârihim, gloss:topluluk yurdunda yerleşip kaldı, source:"غ ن ي,B004"}. Dönüş kelimesinin ailesinde günahtan dönmek de vardır: {ar:يرجعون عن الذنب, tr:yarciʿûne ʿani'z-zenb, gloss:günahtan dönerler, source:"ر ج ع,B003"}. Bu, on beşinci ayetteki "vazgeçmezse" şartının açık bıraktığı yoldur.

Yolun bir son noktası vardır: {ar:النهاية الغاية حيث ينتهي إليه الشيء, tr:en-nihâyetu'l-gâye, gloss:nihâye, bir şeyin vardığı son noktadır, source:"ن ه ي,B002"}. Son ayetin emri ise yaklaşmaktır: {ar:القرب نقيض البعد والتقرب التدني إلى شيء والاقتراب الدنو, tr:el-kurbu nakîdu'l-buʿd, gloss:yakınlık uzaklığın zıddıdır; yaklaşmak bir şeye doğru alçalıp gelmektir, source:"ق ر ب,B001"}. On ikinci ayetin sakınma kökü yolda dikkatle yürüyen atı da adlandırır: {ar:فرس واق إذا كان يهاب المشي من وجع يجده في حافره, tr:ferasun vâk, gloss:toynağındaki ağrıdan ötürü yürümekten çekinen at, source:"و ق ي,B003"}. Sure böylece yolda olmayı, sapmayı, sırt dönmeyi ve sonunda yaklaşmayı tek bir yol üzerinde sıralar.

Kaynaklar: 96:11 ٱلْهُدَىٰٓ ه د ي B001; 96:11 ٱلْهُدَىٰٓ ه د ي B010; 96:16 خَاطِئَةٍ خ ط ء B001; 96:13 وَتَوَلَّىٰٓ و ل ي B007; 96:13 وَتَوَلَّىٰٓ و ل ي B001; 96:13 كَذَّبَ ك ذ ب B004; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B001; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B003; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B004; 96:15 يَنتَهِ ن ه ي B002; 96:19 وَٱقْتَرِب ق ر ب B001; 96:12 بِٱلتَّقْوَىٰٓ و ق ي B003

## Ölçerek yaratmak ve uydurmak

Yaratmak doğru ölçmektir. Aynı kök uydurmayı da adlandırır: {ar:الخلق خلق الكذب وهو اختلاقه واختراعه وتقديره في النفس, tr:el-halku halku'l-kezib, gloss:halk, yalanı uydurmak, icat etmek ve onu nefiste ölçüp biçmektir, source:"خ ل ق,B007"}. Bu tanım yaratma kökünü yalan köküyle birleştirir. Rab gerçeği ölçerek yaratır; yalancı ise yalanı içinde ölçüp biçer. Kurân bu anlamı İbrahim'in kavmine söylediği sözde kullanır: {ar:إِنَّمَا تَعْبُدُونَ مِن دُونِ ٱللَّهِ أَوْثَٰنًا وَتَخْلُقُونَ إِفْكًا, tr:innemâ taʿbudûne min dûni'llâhi evsânen ve tahlukûne ifkâ, gloss:siz Allah'ı bırakıp putlara tapıyor ve yalan uyduruyorsunuz, source:29:17}. Mekkeli ileri gelenler de vahyi bu kelimeyle niteler: {ar:إِنْ هَٰذَآ إِلَّا ٱخْتِلَٰقٌ, tr:in hâzâ ille'htilâk, gloss:bu bir uydurmadan başka bir şey değil, source:38:7}. Gerçek yaratıcının övgüsü de aynı kökle yapılır: {ar:فَتَبَارَكَ ٱللَّهُ أَحْسَنُ ٱلْخَٰلِقِينَ, tr:fe tebâreka'llâhu ahsenu'l-hâlikîn, gloss:yaratanların en güzeli Allah ne yücedir, source:23:14}.

On üçüncü ayetin yalanlama fiili ile on altıncı ayetin yalancı sıfatı aynı köktendir: {ar:الكذب خلاف الصدق, tr:el-kezibu hilâfu's-sidk, gloss:yalan doğruluğun zıddıdır, source:"ك ذ ب,B001"}. Kökte görünüşüyle yalan söyleyen bir kumaş da vardır: {ar:الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله, tr:el-kezzâbe sevbun yunkaşu bi levni sıbg, gloss:kezzâbe, boyayla nakışlı gibi gösterilen kumaştır; çünkü haliyle yalan söyler, source:"ك ذ ب,B009"}. Öğretme kökündeki gerçek dokuma kenarı bunun karşısında durur: {ar:علم الثوب ورقمه في أطرافه, tr:ʿalemu's-sevb, gloss:kumaşın alemi, kenarlarındaki dokuma nakışıdır, source:"ع ل م,B002"}. Kökte beklenenden önce kesilen süt de yer alır: {ar:كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم, tr:kezebe lebenu'n-nâka, gloss:devenin sütü bir süre süreceği sanıldığı halde kesildi, source:"ك ذ ب,B006"}. Görüntü ile sürekliliğin çatıştığı bir figürdür bu. Yedinci ayetin görme kökünde güzel görünüş de vardır: {ar:الرواء حسن المنظر, tr:er-ruvâ' husnu'l-manzar, gloss:ruvâ, görünüş güzelliğidir, source:"ر ء ي,B006"}.

On altıncı ayetin sıfatı kasıtlı günahı seçer: {ar:الخطأ ما لم يتعمد … الخطيئة الذنب على عمد, tr:el-hata'u mâ lem yutaʿammad … el-hatî'etu'z-zenbu ʿalâ ʿamd, gloss:hata kasıtsız olandır; hatîe kasıtlı günahtır, source:"خ ط ء,B002"}. Kurân bu kelimeyi helak edilmiş toplumlar için kullanır: {ar:وَجَآءَ فِرْعَوْنُ وَمَن قَبْلَهُۥ وَٱلْمُؤْتَفِكَٰتُ بِٱلْخَاطِئَةِ, tr:ve câ'e firʿavnu ve men kablehû ve'l-mu'tefikâtu bi'l-hâti'e, gloss:Firavun, ondan öncekiler ve altı üstüne getirilen şehirler o günahı işlediler, source:69:9}, {ar:فَأَخَذَهُمْ أَخْذَةً رَّابِيَةً, tr:fe ehazehum ahzeten râbiye, gloss:O da onları şiddetli bir yakalayışla yakaladı, source:69:10}. Günahın ardından gelen yakalama, on beşinci ayetteki perçemden yakalamayla aynı yapıdadır.

Bu sahne şunu gösterir: on altıncı ayetteki yalancı perçem, olmadığı bir şeyi iddia eden yüksek baştır, boyanmış ama dokunmamış bir kumaş gibidir. Gerçek ölçüyü yaratan Rab'bin karşısında, uydurma bir ölçüyle kendini yeterli görür.

Kaynaklar: 96:1 خَلَقَ خ ل ق B001; 96:1 خَلَقَ خ ل ق B007; 96:13 كَذَّبَ ك ذ ب B001; 96:16 كَٰذِبَةٍ ك ذ ب B009; 96:16 كَٰذِبَةٍ ك ذ ب B006; 96:4 عَلَّمَ ع ل م B002; 96:7 رَّءَاهُ ر ء ي B006; 96:16 خَاطِئَةٍ خ ط ء B002

## Buluşmalar

İmgeler en açık şekilde baş sahnesinde buluşur. On beşinci ayetin fiili hem perçemden tutmak hem de yüzü karartmaktır. Böylece başın önü, avın yakalandığı yer, huysuz hayvanın tutulduğu yer ve ateşin yaladığı deri aynı noktada birleşir. Aynı alın son ayette yere konur ve secde izini taşır. İşaret imgesi buraya da uzanır: bir alın kararmış bir lekeyle işaretlenir, öteki secdenin iziyle. Kurân her iki tarafı da yüzlerindeki işaretle tanıtır: biri {ar:مِّنْ أَثَرِ ٱلسُّجُودِ, tr:min eseri's-sucûd, gloss:secdenin izinden, source:48:29}, öteki {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. Sure ad ile başlar ve iki işaretli alınla biter.

Göz ile yeterlilik imgeleri yedinci ayette buluşur. Kendini aynada gören adam ile süse ihtiyaç duymayan güzel kadın aynı kelime çiftinde birleşir: kendini görmek ve yeterli saymak. Su imgesi de buna bağlanır. Azan insan ölçüsünü aşan bir taşkın gibidir; on beşinci ayette durması istenir. Kökün göletteki duruluşu adlandırdığı hatırlanırsa, sekizinci ayet bu suyun nereye varacağını söyler. Kurân'ın varış ayeti bu iki imgeyi aynı yapıda birleştirir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Yol imgesi de bu dönüşe katılır, çünkü dönüş başlangıca dönmektir ve bu başlangıç rahimdeki ilk tutunuştur.

Rahim ile okuma, surenin ilk kelimesinde buluşur. Okumanın kökü hem rahmin bir şeyi toplayıp tutmasını hem de harflerin toplanmasını adlandırır. Pıhtıyı tutan kökle sözü toplayan kök aynıdır. İnsanın yaratılışı ve öğretilmesi bu yüzden aynı işin iki yüzü olarak duyulur. Kurân'daki benzer sıra da bunu destekler: Kurân'ı öğretmek, insanı yaratmak ve ona açıklamayı öğretmek. Okuma ile secde de buluşur: okuyucu aynı zamanda kulluk edendir ve sure, ilk emri okumak, son emri secde etmek olan bir eğri çizer. Kurân bu ikisini, okunduğunda secde edenler ile etmeyenler üzerinden birleştirir.

Ateş ile çağrı imgeleri onuncu, on yedinci ve on sekizinci ayetlerde buluşur. Namaz hem çağrıdır hem de kökü ateşe girmeyi adlandırır. Adam meclisini çağırır, Allah ateşe iten bekçileri çağırır ve kul yakın meclise çağrılır. Ateşin kendisinin de çağırdığı söylenir: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Bu yüz çevirme on üçüncü ayetin fiilidir.

İtaat ile hayvan imgeleri son ayette buluşur. Rab, itaat edilen efendidir; dizgine uyan at da itaatin bir figürüdür. Kul bu yüzden kendini rab ilan eden birine boyun eğmez, yakında tutulan ve değer gören at gibi yaklaşır. Yaratma ile uydurma da on altıncı ayette buluşur. Gerçek ölçüyle yaratan Rab'bin karşısında, yalanı içinde ölçen yalancı perçem durur.

Bu buluşmalar surenin hareketini taşır. Sure, rahimde toplanan ve tutunan bir varlıkla başlar; bu varlık sözü toplamayı ve kalemle yazmayı öğrenir. Sonra kendini aynada yeterli görür, taşkın su gibi ölçüsünü aşar, başını kaldırır ve namaz kılan kulu engellemeye çalışır. Dönüş ayeti ve Allah'ın görmesi bu yükselişin önüne bir sınır koyar. Yasaklayan perçeminden yakalanır, meclisi yerine bekçiler gelir. Kul ise yüz çevirmeden, başını yere koyarak, çağrılmış olduğu yakınlığa yürür.

