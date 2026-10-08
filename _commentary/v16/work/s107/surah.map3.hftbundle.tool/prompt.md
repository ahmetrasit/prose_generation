Surah: 107. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md and hft.md (both are earlier readers' proposals: ignore their judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S107 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

===== _commentary/v16/prompts/map3/surah_map.md (adapted) =====
Read the surah as one text and write its map of image chains: the lexical images that run through several of
its ayat and join them into one scene, process or movement. A later writer will read one ayah at a time, with
only that ayah's own dictionary. The map lets that writer hear what the ayah's words carry in the surah as a
whole, including senses whose evidence sits under the words of other ayat.

Your evidence is the surah text, the dictionary of every root in the surah (each branch with the classical
dictionaries' own phrases), earlier readers' channel review (channels.md) and activation hypotheses (hft.md),
and your own knowledge of Arabic and the Quran. Where a member or passage comes from memory rather than from
the dictionary or the text, say so. Do not delegate, browse or inspect files; run only the command the header describes.

The channel review and the HFT records are proposals by earlier readers. Ignore their judgements: grades,
strength or confidence labels, reading types, words such as "surprising", "exploratory" or "latent", and every
statement of what a reading may or may not do. Make your own judgement from the surah's words, the dictionary
phrases and the Quran. Do not rediscover what they already assembled: start from their chains, test each one
against the dictionary phrases and the text, and join, extend, split or correct them. Where their wording
abstracts a member, go back to the dictionary phrase and name what it actually says.

A chain belongs on the map when its members are senses the dictionary attests for words that stand in the surah,
and together they make one image or process that the surah's wording or sequence lets a listener hear. A member
need not be the sense that translates its word in its own ayah; a chain is heard across the surah, not in one
word. A chain may join a sense and its reversal as well as the parts of one scene. Mark a member attested only
inside a fixed expression [fixed expression]; add no other label to a member or a chain, and where a source
records a phrase and rejects it, say so of that phrase alone. When the dictionary itself joins two of the
surah's words in one phrase, quote that phrase: it is the strongest evidence a chain can have. Keep a scene at
the level of its objects, their parts and their operation. When proposals share members, do not fold one into
another's more abstract function unless nothing concrete is lost. Carry every chain that meets this test,
however unusual; leave out proposals that do not.

Write the map in English, with Arabic quoted exactly (surah wording from the text, dictionary phrases from the
dictionary). It is working material for the writer, not commentary prose.

1. `## Chains`. For each chain, a `###` heading naming the image. One paragraph on what the image is and how it
   moves through the surah. Then its members, one line each: the ayah ref, the word as it stands in the text,
   the root and branch id, the dictionary's own phrase quoted exactly, and what this member contributes to the
   image. Add Quran passages outside the surah, with exact refs, where they stage or confirm the chain; for
   each, name the speaker and the situation in a few words, and include the ayah that opens its scene when the
   passage continues one.
2. `## Interactions`. Where chains meet: a shared member, a dictionary phrase that joins members of two chains,
   a Quran passage that stages two chains together, or one chain's scene needing another's. One line each: the
   chains, where they meet, the evidence.
3. `## Ayat`. For each ayah in order: the chains its words take part in, what its words add to each, and in one
   line the whole scene each chain makes across the surah, so that a writer who sees only this ayah sees the
   scene, not a fragment.
4. `## Not carried`. Each channel subchannel and each HFT record you did not carry into a chain: one short line
   each, its name and why, no prose.

No ranking and no labels of strength or confidence. No list of what a writer must include. There is no length
target and no required number of chains or members.

===== _commentary/v16/work/s107/surah.r2.hftbundle/text.md =====
# Surah 107

- 107:1 أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ
- 107:2 فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ
- 107:3 وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 107:4 فَوَيْلٌۭ لِّلْمُصَلِّينَ
- 107:5 ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ
- 107:6 ٱلَّذِينَ هُمْ يُرَآءُونَ
- 107:7 وَيَمْنَعُونَ ٱلْمَاعُونَ


===== _commentary/v16/work/s107/surah.r2.hftbundle/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ر ء ي (root_000531): 107:1 أَرَءَيْتَ, 107:6 يُرَآءُونَ

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

## ECHO ر و ي (root_000615): for 107:1 أَرَءَيْتَ, 107:6 يُرَآءُونَ: withheld observed target; not identity

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

## ك ذ ب (root_001290): 107:1 يُكَذِّبُ

- **B001** sözde veya davranışta doğruluğa aykırılık — sözde veya davranışta doğruluğa aykırılık; yalan · yalancı; çok yalan söyleyen kişi · uydurma söz; yalanlar · özürlere kaçınılmaz olarak yalan karışır
  الكذب خلاف الصدق (maqayis;jamhara); الكذاب لغة في الكذب (ayn); كذب كذبا فهو كاذب وكذاب وكذوب (sihah); يقال في المقال والفعال (mufradat)
- **B002** yalan sayma veya yalancı bulma — yalanlama; yalan sayma · birini yalancı saymak veya ona yalan söylediğini bildirmek · birini yalancı bulmak veya yalanını ortaya çıkarmak · seni yalancı saymıyorum
  كذبت فلانا نسبته إلى الكذب وأكذبته وجدته كاذبا (maqayis); كذبته جعلته كاذبا (ayn); كذبت بالحديث كذابا وتكذيبا (jamhara); أكذبت الرجل ألفيته كاذبا وكذبته إذا قلت له كذبت (sihah); كذبته نسبته إلى الكذب (mufradat)
- **B003** onu üstlen; sana düşer [kalıp] — şunu üstlen; sana düşer veya onu yapmalısın
  كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك (maqayis); كذب عليكم الحج أي وجب عليكم ودونكم الحج (ayn); كذب عليك كذا وكذا في معنى الإغراء (jamhara); كذب عليكم الحج أي وجب (sihah); كذب عليك الحج قيل معناه وجب فعليك به (mufradat)
- **B004** hamlede duraksamak; olumsuzda sonuna kadar ilerlemek [kalıp] — saldırıya geçti ama duraksadı veya korktu · saldırıya geçti ve vuruncaya kadar durmadı; korkmadı
  حمل فلان ثم كذب أي لم يصدق في الحملة (maqayis); حمل فلان على فلان فما كذب حتى طعن أو ضرب أي ما وقف (jamhara); حمل فلان فما كذب أي ما جبن (sihah); حمل فلان على قرنه فكذب (mufradat)
- **B005** gecikmeden yapmak [kalıp] — yapmakta gecikmedi; hemen yaptı
  ما كذب فلان أن فعل كذا أي ما لبث (maqayis;sihah)
- **B006** sütün kesilmesi veya beklenenden önce tükenmesi [kalıp] — dişi devenin sütü kesildi veya umulduğu kadar sürmedi
  كذب لبن الناقة ذهب وفيه نظر وقياسه صحيح (maqayis); كذب لبن الناقة أي ذهب (sihah); كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم (mufradat)
- **B007** koşup arkasına bakmak için durmak [kalıp] — yaban hayvanı bir mesafe koşup arkasına bakmak için durdu
  كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه (jamhara)
- **B008** iç benlik — iç benlik; kişinin kendisi
  الكذوب النفس (jamhara)
- **B009** dokuma bezemesi sanısı veren boyalı kumaş — dokuma bezemesi sanısı veren boyalı veya desenli kumaş
  الكذابة ثوب يصبغ بألوان الصبغ كأنه موشي (ayn); الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله (mufradat)

## د ي ن (root_000504): 107:1 بِٱلدِّينِ

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

## د ع ع (root_000477): 107:2 يَدُعُّ

- **B001** itme — sert ve kaba itme · sertçe itmek · yetimi itip azarlamak · ateşe doğru zorla sürmek
  الدَّعّ الدفع (maqayis;tahdhib)؛ دَعَعته أدَعُّه دَعًّا أي دفعته (sihah)؛ دفع في جفوة (ayn)؛ الدفع الشديد (mufradat)
- **B002** sallayarak doldurma — kabı sallayarak doldurma · bir şeyi doldurmak veya hareket ettirerek sıkıştırmak · ağzına kadar dolu büyük çanak · selin vadiyi doldurması
  الدعدعة تحريك المكيال ليستوعب الشيء (maqayis)؛ دعدعت الشيء ملأته وجفنة مدعدعة (sihah)؛ دعدع مكيالا أو جوالقا حتى يكتنز (tahdhib)
- **B003** hayvanı seslenerek yönlendirme — küçükbaş hayvanı seslenerek çağırma veya azarlama · keçilere seslenip onları yönlendirmek · çobanın keçileri yönlendirmek için çıkardığı geleneksel çağrı
  الدعدعة زجر الغنم (maqayis)؛ للمعز خاصة دعدعت بها إذا دعوتها (sihah)؛ يقول الراعي للمعزى داع داع وهو زجر لها (tahdhib)
- **B004** tökezleyeni ayağa kalkmaya çağırma — tökezleyene söylenen 'kalk, toparlan' sözü
  قولك للعاثر دع دع (maqayis)؛ أن تقول للعاثر دع دع أي قم فانتعش (sihah;tahdhib)؛ أصله أن يقال للعاثر دع دع (mufradat)
- **B005** kıvrılarak yavaş koşma — kıvrıla kıvrıla yavaş koşma
  الدعدعة عدو في التواء (maqayis)؛ عدا عدوا فيه بطء والتواء (sihah)؛ عدو في التواء وبطء (tahdhib)
- **B006** kısa boylu adam — 
  دعداع فإن صح فهو من الإبدال من دحداح (maqayis)؛ الدعداع والدحداح الرجل القصير (tahdhib)
- **B007** iki hurma arasındaki açıklık veya seyrek hurmalar — 
  الدعاع ما بين النخلتين؛ الدعاع النخل المتفرق؛ رواه بعضهم في ذعاع النخل بالذال
- **B008** yazın su barındıran, sığırların yediği bitki — yazın su tutan ve sığırların yediği bir bitki
  الدعدع نبت يكون فيه ماء في الصيف يأكله البقر
- **B009** küçük çocuklar ve bakmakla yükümlü olunan küçükler — bir erkeğin küçük çocukları ve bakımına bağlı küçükler · bakımına bağlı küçüklerin sayısı çoğalmak
  الدعاع عيال الرجل الصغار؛ أدع الرجل إذا كثر دعاعه
- **B010** yabani bitki tohumu — yabani bir bitkinin tohumu · kuraklıkta yenen siyah tohum; ona benzeyen siyah karınca · bu tohumu ve başka bir yabani tohumu yemek için toplayan adam
  الدعاع حب شجرة برية؛ الدعاعة حبة سوداء؛ نملة سوداء تشاكل هذه الحبة؛ رجل دعاع فثاث

## ECHO د ع و (root_000478): for 107:2 يَدُعُّ: withheld observed target; not identity

- **B001** seslenerek kendine yöneltme — seslenmek; çağırmak · yemeğe çağırma · belirtilen yeri amaçlayıp oraya gitmek
  أصل واحد وهو أن تميل الشيء إليك بصوت وكلام يكون منك؛ دعوت أدعو دعاء؛ الدعوة إلى الطعام بالفتح؛ دعا فلانا مكان كذا إذا قصد ذلك المكان كأن المكان دعاه
- **B002** hak veya aidiyet ileri sürme — soy bağı ileri sürme · kendisi veya başkası adına hak iddia etme · savaşta soyunu söyleyerek kendini tanıtma · öz babasından başkasına bağlanan kişi
  الادعاء أن تدعي حقا لك أو لغيرك (maqayis)؛ الادعاء في الحرب الاعتزاء (maqayis)؛ الدعوة ادعاء الولد الدعي غير أبيه ويدعيه غير أبيه (ayn)؛ الدعوة في النسب بالكسر (maqayis)
- **B003** sütün devamını çekmek için memede bırakılan pay [kalıp] — sonraki sütü çekmek için memede bırakılan süt payı
  داعية اللبن ما يترك في الضرع ليدعو ما بعده
- **B004** Tanrı'nın birine istemediği bir sıkıntıyı vermesi [kalıp] — Tanrı'nın birinin başına hoşlanmadığı bir sıkıntıyı getirmesi
  دعا الله فلانا بما يكره أي أنزل به ذلك
- **B005** birbiri ardından çökme veya yıkma — duvarların birbiri ardından çökmesi · yapıları üzerlerine birbiri ardından yıkmak
  تداعت الحيطان وذلك إذا سقط واحد وآخر بعده؛ داعيناها عليهم إذا هدمناها واحدا بعد آخر
- **B006** dönemin olaylara yön veren değişimleri [kalıp] — dönemin değişimleri ve getirdiği olaylar
  دواعي الدهر صروفه كأنها تميل الحوادث
- **B007** gizli cevabı buldurmaya yönelik bilmeceleşme — gizli cevabı buldurmak için karşılıklı sorulan bilmeceler · sana bir bilmece sorayım
  لبنى فلان أدعية يتداعون بها وهي مثل الأغلوطة كأنه يدعو المسؤول إلى إخراج ما يعميه عليه
- **B008** evde hiç kimsenin bulunmaması — evde hiç kimse yok
  ما بالدار دَعْوِيّ أي ما بها أحد كأنه ليس بها صائح يدعو بصياحه

## ي ت م (root_001692): 107:2 ٱلْيَتِيمَ

- **B001** babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu olma — insanda babasız, hayvanda annesiz kalma · babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu · çocuk babasını yitirip babasız kaldı · Tanrı onu babasız bıraktı · çocukları babasız bıraktı · babasını yitirmiş çocuklar · babasını yitirmiş çocuklar · çocukları babasız kalmış kadın · çocukları babasız kalmış kadın · onları babasız bıraktı · çocukken kendisini yetiştiren kişiye nispetle, büyüdüğünde de babasını yitirmiş çocuk diye anılan kişi · babasını yitirmiş çocuklar topluluğu
  اليتم في الناس من قبل الأب وفي سائر الحيوان من جهة الأم (maqayis)؛ يتم الصبي إذا صار يتيما وأيتمه الله (jamhara)؛ أيتمت المرأة فهي موتم (jamhara;sihah)؛ يتمهم الله تيتيما (sihah)؛ اليتيم الذي مات أبوه حتى يبلغ (tahdhib)؛ انقطاع الصبي عن أبيه قبل بلوغه وفي سائر الحيوانات من قبل أمه (mufradat)
- **B002** tek kalmış ya da benzeri zor bulunan şey — tek başına veya eşi zor bulunan · tek başına duran veya benzeri olmayan şiir dizesi · tek ve eşi zor bulunan inci · tek başına duran kumluk veya dişil varlık
  لكل منفرد يتيم وبيت من الشعر يتيم (maqayis)؛ اليتيم الفرد (jamhara)؛ كل شيء مفرد يعز نظيره فهو يتيم ودرة يتيمة (sihah)؛ الرملة المنفردة وكل منفرد ومنفردة يتيم ويتيمة (tahdhib)؛ كل منفرد يتيم ودرة يتيمة وبيت يتيم (mufradat)
- **B003** dalgınlık ve gerekeni eksik yapma — dalgınlık ve gerekeni eksik yapma · gidişinde dalgınlık veya eksik davranış yok
  اليتم الغفلة والتقصير وما في سيره يتم أي ما فيه غفلة ولا تقصير (jamhara)؛ أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره (tahdhib)
- **B004** yavaşlama veya gecikme — gidişinde yavaşlama var · yavaşlama ve gecikme
  في سيره يتم أي إبطاء (sihah)؛ اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه (tahdhib)
- **B005** evlilikle sona erip ermediği tartışmalı kadın adlandırması [kalıp] — evlenene dek, başka bir aktarıma göre ise evlendikten sonra da babasını yitirmiş çocuk adıyla anılan kadın · kadınların babasını yitirmiş çocuk adıyla anılabileceğini bildiren söz
  المرأة تدعى يتيما ما لم تتزوج فإذا تزوجت زال عنها اسم اليتم؛ يقال للمرأة يتيمة لا يزول عنها اسم اليتم أبدا (tahdhib)

## ح ض ض (root_000334): 107:3 يَحُضُّ

- **B001** birini belli bir eyleme ısrarla yöneltme — birini bir şeyi yapmaya güçlü biçimde yöneltmek · birini belli bir şeyi yapmaya ısrarla yöneltmek · birbirini bir eyleme yöneltme · iki kişinin birbirini özendirmesi · bir eyleme güçlü biçimde yöneltme · ısrarlı özendirme adı veya biçimi
  حضضته على كذا إذا حضضته عليه وحرضته (maqayis)؛ وقد حض يحض حضا (ayn)؛ حضه على القتال حضا أي حثه وحضضه أي حرضه والتحاض التحاث والمحاضة أن يحث كل واحد منهما صاحبه (sihah)؛ حض يحض حضا وهو الحث على الخير ويقال حضضت القوم على القتال تحضيضا إذا حرضتهم (tahdhib)؛ الحض التحريض كالحث (mufradat)
- **B002** dağ eteğindeki alçak taban — dağ eteğinde veya dağın bitiminde bulunan alçak zemin · dağ eteğinde bulunan taş
  الحضيض وهو قرار الأرض (maqayis)؛ الحضيض قرار الأرض عند سفح الجبل (ayn;tahdhib)؛ الحضيض القرار من الأرض عند منقطع الجبل ويعني بالأرض (sihah)؛ الحضيض وهو قرار الأرض (mufradat)
- **B003** yapısı farklı aktarılan acı reçinemsi sağaltım maddesi — acı reçineye benzetilen bilinen sağaltım maddesi
  الحضض دواء يتخذ من أبوال الإبل (ayn;tahdhib)؛ الحُضُض والحُضَض دواء معروف وهو صمغ مر كالصبر (sihah)؛ الحُضُض والحُضَض صمغ من نحو الصبر والمر (tahdhib)
- **B004** bir kimse için kendinden daha fazlasını isteme [kalıp] — bir kimse için kendinden daha fazlasını istemek
  احتضضت نفسي لفلان وابتضضتها إذا استزدتها (tahdhib)

## ط ع م (root_000934): 107:3 طَعَامِ

- **B001** tatma, yeme ve yenilen besin — tat, lezzet · yemek veya tadına bakmak · yiyecek, besin · özellikle buğday · tadına bakma ve iştahını yoklama · doyuran ve besleyen yiyecek ya da su · yeme isteği veya iştah çekici şey · çok yiyen, obur
  أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء (maqayis)؛ الطعم ذوقه والطعام اسم جامع لكل ما يؤكل (ayn)؛ طعم إذا أكل أو ذاق ومن لم يطعمه أي لم يذقه (sihah)؛ الطعم تناول الغذاء ويستعمل في الشراب (mufradat)
- **B002** başkasını beslemek veya beslenmeyi istemek — yiyecek vermek, doyurmak · kendisini doyurmasını istemek
  الإطعام يقع في كل ما يطعم (maqayis)؛ استطعمه سأله أن يطعمه وأطعمته الطعام (sihah)؛ استطعمه فأطعمه وأطعموا القانع ويطعمون الطعام (mufradat)
- **B003** söz istemek veya takılan imama söz vermek [kalıp] — benden konuşmamı istedi · imam okuyuşta takılırsa sözü hatırlatın
  استطعمني فلان الحديث إذا أرادك على أن تحدثه وإذا استطعمكم الإمام فأطعموه (maqayis)؛ إذا استفتح فافتحوا عليه (sihah)؛ إذا استفتحكم عند الارتياج فلقنوه (mufradat)
- **B004** geçim, bol ikram ve tahsis edilmiş gelir — geçimi yerinde · rızkı açık, kazançlı · çok ikram eden · geçim veya kazanç kaynağı · kazancı temiz veya kötü · araziyi birine geçim payı olarak ayırdı
  رجل طاعم حسن الحال ومطعام كثير القرى ومطعم مرزوق والطعمة المأكلة (maqayis)؛ حسن المطعم وحسن الطعمة (ayn)؛ الطعمة وجه المكسب وجعلت الضيعة طعمة (sihah)؛ ناحية كذا طعمة والخراج والإتاوات والفيء والخراج (tahdhib)
- **B005** olgunlaşıp tat kazanmak [kalıp] — ağacın meyvesi olgunlaşıp tat kazandı · tulumda hoş tat kazanmış süt
  للنخلة إذا أدرك ثمرها قد أطعمت (maqayis)؛ أطعمت النخلة واطعمت البسرة صار لها طعم وأخذت الطعم (sihah)؛ الشجر المثمر الذي يؤكل ثمره واطعمت الثمرة أخذت الطعم (tahdhib)
- **B006** avı kazandıran araç, uzuv veya kişi — av getiren yay · avcı kuşun öndeki kalın parmağı · avdan yana talihli, avı bol
  قوس مطعمة تطعم صاحبها الصيد والإصبع المتقدمة من الجارحة مطعمة (maqayis)؛ المطعمة القوس والمطعمتان في رجل كل طائر (sihah)؛ مطعم للصيد وقوس مطعمة والمطعمة من الجوارح (tahdhib)
- **B007** ilikte yağı beliren, biraz semiz hayvan — iliğinde yağ bulunan deve · biraz semiz, orta yağlı
  المطعم من الإبل الذي يوجد في مخه طعم الشحم وشاة طعوم فيها بعض السمن (maqayis)؛ جزور طعوم وطعيم بين الغثة والسمينة (sihah)؛ ناقة طعوم وجزور طعوم وطعيم (tahdhib)
- **B008** akıl, değer ve düzelmeye açıklık niteliği [kalıp] — akıllı ve sağlam yargılı · aklı, devinimi veya değeri yok · terbiye kabul etmez, uslanmaz
  ما فلان بذي طعم إذا كان غثا (sihah)؛ رجل ذو طعم أي ذو عقل وحزم وما بفلان طعم ولا نويص ولا يطعم أي لا يتأدب ولا يعقل (tahdhib)
- **B009** atın ağız bölümü ve koşma talebi — atın burun altı ve dudak çevresi · attan koşmasını istedi
  مستطعم الفرس جحافله (sihah)؛ مستطعم الفرس ما تحت مرسنه إلى أطراف جحافله واستطعمت الفرس إذا طلبت جريه (tahdhib)
- **B010** eklenen şeyin tutması [kalıp] — dala aşı yaptı ve aşı tuttu · gözüne küçük bir yabancı cisim girdi
  أطعمت الغصن إذا وصلت به غصنا فقبل الوصل وأطعمت عينه قذى فطعمته (tahdhib)
- **B011** gücü yetmek [kalıp] — ona gücü yetti
  الطعم أيضا القدرة يقال طعمت عليه أي قدرت عليه (tahdhib)
- **B012** boğazından yakalayıp sıkmak [kalıp] — boğazından yakalayıp sıktı
  أخذ فلان بمطعمة فلان إذا أخذ بحلقه يعصره ولا يقولونها إلا عند الخنق والقتال (tahdhib)
- **B013** ağız ağıza temas etmek — ağız ağıza temas etme
  التطاعم إدخال الفم في الفم كما يفعل الحمام عند التقبيل (tahdhib)
- **B014** oluşumu ardışık olmak [kalıp] — oluşumu birbirini izleyen bölümlerden kurulu
  متطاعم الخلق أي متتابع الخلق (tahdhib)

## س ك ن (root_000726): 107:3 ٱلْمِسْكِينِ

- **B001** hareketin dinip durulması — hareketin sona erip şeyin durması · hareketi veya çalkantısı dindi ve durdu · rüzgar, yağmur ya da öfke dindi · hareketsiz, yerinde duran veya dingin
  خلاف الاضطراب والحركة؛ سكن الشيء سكونا فهو ساكن؛ السكون ذهاب الحركة؛ استقر وثبت؛ هدأ بعد تحرك؛ ثبوت الشيء بعد تحرك
- **B002** bir yere yerleşip orada yaşama — bir yere yerleşip orada yaşadı · konut, ev veya yaşanan yer · bir evi kira almadan oturması için verme · onu bir evde veya yerde oturttu · konut olarak kullanılan ev veya yer
  يسكنون الدار؛ المنزل وهو المسكن؛ سكون البيت؛ سكنت داري وأسكنتها غيرى؛ سكنى المرأة المسكن؛ يستعمل في الاستيطان واسم المكان مسكن والجمع مساكن
- **B003** ev halkı ve orada yaşayanlar — ev halkı ve aile üyeleri · bir yerde yaşayanlar · evde yaşayanlar; özel anlatıda evde bulunduğu düşünülen görünmez varlıklar
  السكن الأهل الذين يسكنون الدار؛ السكن السكان؛ السكن جزم العيال وهم أهل البيت؛ السكن أهل الدار؛ سكان الدار
- **B004** insanı rahatlatıp içini yatıştıran dayanak — insanın yanında rahatlayıp içinin yatıştığı kişi veya şey · yanında oturulup rahatlık bulunan ateş · senin yakarışların onları rahatlatır · geceyi dinlenme ve dinginleşme zamanı yaptı · eğri sırığı ateş ve yağla doğrultma
  كل ما سكنت إليه من محبوب؛ السكن أيضا كل ما سكنت إليه؛ ما سكنت إليه؛ إن صلواتك سكن لهم؛ جعل الليل سكنا؛ السكن النار التي يسكن بها
- **B005** güven veren ağırbaşlı iç dinginlik — ağırbaşlılık, yumuşak başlılık, güven ve kalp dinginliği · sandıktaki, kalpleri yatıştırıp güven veren şey · inananların kalplerine güven ve dinginlik verdi
  السكينة وهو الوقار؛ السكينة الوداعة والوقار؛ لا يفرون عنه أبدا وتطمئن قلوبهم إليه؛ فيه ما تسكنون به؛ عليك الوقار والوداعة والأمن؛ أنزل السكينة في قلوب المؤمنين
- **B006** yoksulluk, güçsüzlük ve ezilmişlik — yoksul ya da ezilmiş ve güçsüz kişi · yoksulluk veya ezilmişlik durumu · yoksul duruma geldi ya da boyun eğip kendini alçalttı · boyun eğdi ve alçaldı · Tanrı onu yoksul duruma düşürdü
  المسكنة مصدر فعل المسكين؛ المسكين الفقير وقد يكون بمعنى الذلة والضعف؛ تمسكن إذا خضع لله وهي المسكنة للذلة؛ استكان أي خضع وذل
- **B007** kesici bıçak — kesici bıçak · bıçak yapan kimse
  السكين معروف؛ السكين المدية؛ السكين معروف يذكر ويؤنث؛ سمي سكينا لأنها تسكن الذبيحة؛ السكين سمي لإزالته حركة المذبوح
- **B008** geminin kıçındaki dengeleyici yöneltme aracı — geminin kıçındaki, onu dengede tutup yönelten bölüm veya araç · gemiyi dengede tutup çalkantısını azaltan kıç parçası
  سكان السفينة سمى لأنه يسكنها عن الاضطراب؛ السكان ذنب السفينة الذي به تعدل؛ السكان أيضا ذنب السفينة؛ السكان وهو الكوثل؛ سكان السفينة ما يسكن به
- **B009** sabit yer ve konum bildiren özel kullanımlar — başın boyuna oturduğu yer · yerlerinizde, konumlarınızda veya alışılmış düzeninizde · belirli bir bölgedeki özel yer adı
  موضع من أرض الكوفة؛ السكنة مقر الرأس من العنق؛ استقروا على سكناتكم أي على مواضعكم ومساكنكم؛ الناس على سكناتهم أي على استقامتهم؛ على طبقاتهم ومنازلهم
- **B010** yerinde kalmayı sağlayan geçimlik ve bol otlak — bulunduğu yerde geçinmeyi sağlayan yiyecekler · yerinde kalmayı sağlayan bir geçimlik · sürüyü göç ettirmeye gerek bırakmayacak kadar bol otlak
  الأسكان الأقوات واحدها سكن؛ قيل للقوت سكن لأن المكان به يسكن؛ مرعى مسكن إذا كان كثيرا لا يخرج إلى الظعن عنه

## ص ل و (root_000879): 107:4 لِّلْمُصَلِّينَ, 107:5 صَلَاتِهِمْ

- **B001** ateşin yakıcı sıcaklığına maruz kalma ve ateşle işleme — ateşe girip onun yakıcı sıcaklığını çekmek · ateşin yanında ısınmak · eti ateşte pişirmek · ateşte pişirilmiş · birini ateşe atıp yakmak · ateşi besleyen yakacak; ateşte pişirme · değneği ateşte yumuşatıp düzeltmek · bir işin güçlüğünü ve yorgunluğunu çekmek · onun sertliğine kimse yanaşamaz
  صليت العود بالنار (maqayis); اصطليت بالنار (maqayis;sihah); الصلا النار وصلى الكافر نارا (ayn); صليت اللحم شويته (ayn;sihah;tahdhib); الصلاء يقال للوقود وللشواء (mufradat); صلي بالأمر إذا قاسى حره وشدته (sihah;tahdhib)
- **B002** başkası için iyilik dileme; esirgeme, övme ve değer verme — başkası için iyilik ve esenlik dileme · biri için iyilik dilemek, onu övmek veya esirgenmesini istemek · Tanrı'nın esirgemesi, övmesi, bağışlaması ve değer vermesi · meleklerin bağışlanma ve iyilik dilemesi
  الصلاة وهي الدعاء (maqayis;sihah); صلوات الرسول للمسلمين دعاؤه لهم (ayn); الصلاة من الله تعالى الرحمة (maqayis;sihah;tahdhib); صلوات الله حسن ثنائه عليهم وقيل مغفرته لهم (ayn); صلاة الملائكة الاستغفار (ayn;tahdhib;mufradat); صلاة الله للمسلمين تزكيته إياهم (mufradat)
- **B003** ayakta durma, eğilme ve yere kapanma bölümleri olan kurallı tapınma — namaz · namazı bütün gerek ve koşullarını yerine getirerek kılmak
  الصلاة التي جاء بها الشرع من الركوع والسجود وسائر حدود الصلاة (maqayis); الصلاة واحدة الصلوات المفروضة (sihah); الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib); الصلاة التي هي العبادة المخصوصة أصلها الدعاء (mufradat); إقامة الصلاة (mufradat)
- **B004** yakalamak için kurulan tuzak — av için kurulan tuzak · avı veya başka hedefleri yakalayan tuzaklar · birini yıkıma düşürmek için gizlice düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis); المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد (ayn); المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib); صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة (tahdhib)
- **B005** sırtın ortası ve kuyruk kökünün iki yanı — sırtın orta bölümü veya kuyruk kökünün iki yanı · kuyruk kökünün iki yanı · doğum sırasında kuyruk kökü çevresinin açılması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn); كل أنثى إذا ولدت انفرج صلاها (ayn); الصلوين وهما مكتنفا الذنب من الناقة وغيرها (tahdhib); أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها وقرب نتاجها (tahdhib)
- **B006** yarışta birincinin hemen ardındaki ikinci — yarışta birincinin ardından gelen ikinci · yarışta liderin hemen ardından ikinci gelmek
  قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه (ayn); المصلى تالي السابق (sihah); السابق الأول والمصلي الثاني (tahdhib); يكون عند صلا الأول (tahdhib)
- **B007** tapınma yeri; kilise — Yahudilerin kiliseleri veya bir din topluluğunun tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn); الصلوات كنائس اليهود (tahdhib); قيل إنها مواضع صلوات الصابئين (tahdhib); يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B008** üzerinde dövme yapılan geniş taş — üzerinde malzeme dövülen geniş taş · dövme taşı
  الصلاية الفهر (sihah); الصلاءة بالهمز مثله (sihah); الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib); الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B009** iri başaklı, develerin otladığı bir bitki — iri başaklı, develerin otladığı bir bitki · bu bitkinin yetiştiği arazi
  الصليان نبت (ayn;tahdhib); له سنمة عظيمة كأنها رأس القصبة (ayn); له سبطة عظيمة كأنها رأس القصبة (tahdhib); تسميها العرب خبزة الإبل (ayn;tahdhib)

## ECHO ص ل ي (root_000880): for 107:4 لِّلْمُصَلِّينَ, 107:5 صَلَاتِهِمْ: withheld observed target; not identity

- **B001** ayakta durma, eğilme ve yere kapanmalı yükümlü tapınma — ayakta durma, eğilme ve yere kapanma bölümleri olan yükümlü tapınma
  الصلاة التي جاء بها الشرع من الركوع والسجود (maqayis)؛ الصلاة واحدة الصلوات المفروضة (sihah)؛ الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib)؛ الصلاة التي هي العبادة المخصوصة (mufradat)
- **B002** iyilik dileme; özneye göre esirgeme, övme veya aklama — iyilik dileme; özneye göre esirgeme, övme veya bağışlanma isteme · onun için iyilik dilemek, onu esirgemek ya da aklamak · Tanrı'nın kullarını esirgemesi, övmesi veya aklaması · göksel görevlilerin iyilik ve bağışlanma dilemesi · ölen kişi için iyilik dileme
  الصلاة وهي الدعاء (maqayis)؛ صلوات الرسول للمسلمين دعاؤه لهم وذكرهم (ayn)؛ الصلاة من الله تعالى الرحمة (sihah)؛ الصلاة من الملائكة دعاء واستغفار ومن الله سبحانه رحمة (tahdhib)؛ الصلاة الدعاء والتبريك والتمجيد (mufradat)
- **B003** ateşin veya benzer bir sıkıntının şiddetine uğramak; birini ateşe sokmak [kalıp] — ateşe girip yakıcı sıcağını çekmek · onu ateşe sokmak · ateşin başında ısınmak · bir işin ağır sıkıntısını çekmek · birinin kötülüğüne uğramak · onun sertliğini ve gücünü göze alamamak
  أحدهما النار وما أشبهها من الحمى (maqayis)؛ صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها (ayn)؛ صلي الرجل نارا إذا أدخلته النار (sihah)؛ من يصلى في النار أي يلزم النار (tahdhib)؛ صلي بالنار وبكذا أي بلي بها واصطلى بها (mufradat)
- **B004** ateş yakıtı; ateşte pişirme veya ısıyla düzeltme — ateşi tutuşturan ve başında ısınılan yakıt · ateşte pişirilmiş yiyecek · odun ya da ateş · eti ateşte pişirmek · ateşte pişmiş · değneği ateş üstünde döndürerek yumuşatıp doğrultmak · ateşin üstüne kurulan ocak taşları
  الصلاء ما يصطلى به وما يذكى به النار ويوقد (maqayis)؛ صليت اللحم صليا شويته (ayn;sihah;tahdhib)؛ صلى عصاه إذا أدارها على النار يثقفها (ayn;tahdhib)؛ الصلاء يقال للوقود وللشواء (mufradat)
- **B005** av yakalamak için kurulan kapan — av veya zararlı canlılar için kurulan kapanlar · av yakalamak için kurulan kapan · birini yok oluşa düşürecek bir düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis)؛ المصلاة أن تنصب شركا ونحوه (ayn)؛ المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib)
- **B006** sırtın ortası ve kuyruk dibinin iki yanı — sırtın ortası veya kuyruk dibi ile kuyruk sokumunun iki yanı · kuyruk dibinin iki yanı · doğumda kuyruk dibi bölgesinin açılması · devenin yavrusunun kuyruk dibi bölgesine inmesi ve doğumun yaklaşması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn)؛ انفرج صلاها (ayn)؛ الصلوين مكتنفا الذنب (tahdhib)؛ أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها (tahdhib)
- **B007** yarışta önderin hemen ardındaki ikinci at — yarışta önderin hemen ardındaki ikinci at · atın önder atın hemen ardından gelmesi
  أتى الفرس على أثر الفرس السابق قيل قد صلى وجاء مصليا (ayn)؛ المصلى تالي السابق (sihah)؛ السابق الأول والمصلي الثاني (tahdhib)
- **B008** tapınma yeri, özellikle Yahudi tapınağı — Yahudi tapınakları veya genel olarak tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn)؛ الصلوات كنائس اليهود (tahdhib)؛ يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B009** üzerinde madde dövülen geniş taş — üzerinde koku maddesi veya başka maddeler dövülen geniş taş · üzerinde madde dövülen geniş taş
  الصلاية الفهر (sihah)؛ الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib)؛ الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B010** iri başaklı deve yemi bitkisi — iri başaklı, develere yem olan bitki · bu iri başaklı bitkinin yetiştiği yer
  الصليان نبت على فعلان ويقال فعليان له سنمة عظيمة (ayn)؛ الصليان نبت له سبطة عظيمة (tahdhib)؛ تسميها العرب خبزة الإبل (ayn;tahdhib)

## س ه و (root_003249): 107:5 سَاهُونَ

- **B001** farkinda olmama — 
  السهو الغفلة (maqayis)؛ السهو الغفلة عن الشيء وذهاب القلب عنه (ayn)؛ سهوت في الصلاة أسهو سهوا (maqayis)؛ سها الرجل في صلاته إذا غفل عن شيء منها (ayn)
- **B002** durgunluk — 
  السهو السكون؛ جاء سهوا رهوا
- **B003** kusuru gormezden gelerek iyi gecinme — 
  المساهاة حسن المخالقة (maqayis;ayn)؛ كأن الإنسان يسهو عن زلة إن كانت من غيره (maqayis)
- **B004** ev onu duzenegi — 
  السهوة وهي كالصفة تكون أمام البيت (maqayis)؛ السهوة أربعة أعواد أو ثلاثة يعارض بعضها على بعض يوضع عليها شيء من الأمتعة (ayn)
- **B005** zor gorulen kucuk yildiz — 
  السها خفي جدا فيسهى عن رؤيته (maqayis)؛ السها كويكب صغير (ayn)
- **B006** kanama doneminde cocuk tasima — 
  حملت المرأة ولدها سهوا أي على حيض

## م ن ع (root_001448): 107:7 وَيَمْنَعُونَ

- **B001** vermeme ve esirgeme — vermenin karşıtı olarak vermeme ve esirgeme · vermeyen veya verilecek şeyi elinde tutan · iyiliği sürekli esirgeyen çok cimri kişi · başkasına vermeyen, cimrice elinde tutan kişi · yalnızca vermemeyi hak edenden esirgeyen ve adaletle veren
  خلاف الإعطاء (maqayis;sihah)؛ ضد العطية (mufradat)؛ رجل منوع ومناع إذا كان بخيلا ممسكا (tahdhib)؛ مناع للخير (tahdhib;mufradat)
- **B002** isteğinden alıkoyma — onu istediği şeyden alıkoymak · seni bunu yapmaktan ne alıkoydu? · önüne engel çıkınca geri durmak
  منعته أمنعه منعا فامتنع أي حلت بينه وبين إرادته (ayn)؛ منعت الرجل عن الشئ فامتنع منه (sihah)؛ المنع أن تحول بين الرجل وبين الشيء الذي يريده (tahdhib)؛ ما الذي صدك وحملك على ترك ذلك (mufradat)
- **B003** erişilmez kılan koruyucu güç — inananları çevreleyip koruyan ve destekleyen · gücü ve koruması sayesinde erişilemez · koruyucu güç, saygınlık ve destekçiler · saygınlık ve güçlü koruma içinde
  مكان منيع وهو في عز ومنعة (maqayis)؛ رجل منيع لا يخلص إليه وهو في عز ومنعة (ayn)؛ مكان منيع وقد منع مناعة؛ المنعة جمع مانع أي من يمنعه من عشيرته (sihah)؛ يحوطهم وينصرهم؛ في قوم يمنعونه ويحمونه (tahdhib)؛ يقال في الحماية ومنه مكان منيع وفلان ذو منعة (mufradat)
- **B004** cinsel ahlaksızlığa yanaşmayan kadın [kalıp] — cinsel ahlaksızlığa yanaşmayan, kendini sakınan kadın · ahlak dışı cinsel ilişkiyi kabul etmeyen kadın
  امرأة منيعة متمنعة لا تؤاتى على فاحشة (ayn)؛ امرأة منعة متمنعة لا تؤاتى على فاحشة (tahdhib)؛ امرأة منيعة كناية عن العفيفة (mufradat)
- **B005** Engelle! — Engelle!
  مناع بمعنى امنع (ayn)؛ مناع أي امنع كقولهم نزال أي انزل (mufradat)
- **B006** bir şey üzerinde karşılıklı engelleşme — bir şey üzerinde onunla karşılıklı engelleşmek
  مانعته الشئ ممانعة (sihah)
- **B007** çetin yıla direnen genç dişi deve ile dişi oğlak — gençlikleriyle çetin yıla direnen ve yetişkin hayvanlardan önce doyan genç dişi deve ile dişi oğlak · çetin yıla karşı koyan ve yetişkin hayvanlardan önce doyan genç dişi deve ile dişi oğlak
  المتمنعان البكرة والعناق تمتنعان على السنة بفتائهما (sihah)؛ المتمنعتان البكرة والعناق تمنعان على السنة لفنائهما (tahdhib)؛ المقاتلتان للزمان عن أنفسهما (sihah;tahdhib)

## م ع ن (root_004706): 107:7 ٱلْمَاعُونَ

- **B001** akan su ve suyun akışı — 
  معن الماء جرى (maqayis;tahdhib)؛ ماء معين أي جار (maqayis;sihah;tahdhib)؛ المعنة ماء قليل يجري (maqayis)؛ المعنان مجاري الماء في الوادي (maqayis;sihah)؛ أمعنت الأرض رويت وكلأ ممعون جرى فيه الماء (maqayis;sihah;tahdhib)؛ معن الوادي كثر فيه الماء المعين (maqayis)
- **B002** atın veya benzeri hayvanın koşarak uzaklaşması — 
  أمعن الفرس في عدوه (maqayis)؛ أمعن الفرس ونحوه إمعانا إذا تباعد يعدو (ayn)؛ أمعن الفرس تباعد في عدوه (sihah;tahdhib)
- **B003** kolaylık ve hafiflik; bağlama göre azlık ya da çokluk — 
  رجل معن في حاجته سهل (maqayis;sihah)؛ ضياع مالك غير معن أي غير سهل (maqayis)؛ المعن الشيء اليسير الهين (sihah)؛ ماله سعنة ولا معنة أي شيء (sihah)؛ المعن القليل والمعن الكثير (tahdhib)
- **B004** hakkı alıp götürmek; hak sahibine yönelince hakkı tanıyıp boyun eğmek — 
  أمعن بحقي ذهب به (maqayis;sihah)؛ أمعن لي بحقي إذا أقر به وانقاد (tahdhib)
- **B005** sağlanan yarar veya kullanıma sunulan ev eşyası — 
  الماعون يفسر بالزكاة والصدقة ويقال هو أسقاط البيت نحو الفأس والقدر والدلو (ayn)؛ الماعون اسم جامع لمنافع البيت (sihah)؛ يسمى الماء أيضا ماعونا (sihah)؛ الماعون في الجاهلية كل منفعة وعطية وفي الإسلام الطاعة والزكاة (sihah)؛ الماعون المعروف كله والقصعة والقدر والفأس (tahdhib)؛ كل ما يستعار من قدوم وسفرة وشفرة (tahdhib)؛ الماعون الطاعة (tahdhib)
- **B006** barınılan yer — 
  قولهم للمنزل معان وجمعه معن (maqayis)؛ المعان المباءة والمنزل ومعان موضع بالشأم (sihah)

## ECHO ع و ن (root_001064): for 107:7 ٱلْمَاعُونَ: withheld observed target; not identity

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



===== _commentary/v16/work/s107/surah.r2.hftbundle/channels.md =====
(source: latent_activation/network/v3/reviews/s107/reader_a_pilot.md)

# s107 Semantic Channel Discovery

## Parent Channels

### 1. Care and Circulation of Sustenance
- Semantic invariant: Life-sustaining food, shelter, and useful goods move toward vulnerable recipients through feeding, lending, and shared use, while repulsion and withholding interrupt that movement.
- Surface relation: direct; 107:2 يَدُعُّ ٱلْيَتِيمَ, 107:3 يَحُضُّ / طَعَامِ / مِسْكِينِ, and 107:7 يَمْنَعُونَ ٱلْمَاعُونَ.
- Surprising reach: The same circulation frame extends from a meal to free lodging, household loans, credit, and provision that allows a household to remain settled.

#### Subchannel A. Feeding the Vulnerable
- Reading type: surface-primary
- Scene or process: A dependent child or poor person is placed before an agent who either thrusts the recipient away or mobilizes food on the recipient's behalf.
- Active motifs: orphaned child (ي ت م:B001/m01); forceful rebuff (د ع ع:B001/m01); exhortation toward food and good (ح ض ض:B001/m01); food as sustenance (ط ع م:B001/m02); feeding another (ط ع م:B002/m01); poor and humbled recipient (س ك ن:B006/m01)
- Ayah anchors: 107:2 يَدُعُّ (د ع ع), 107:2 ٱلْيَتِيمَ (ي ت م), 107:3 يَحُضُّ (ح ض ض), 107:3 طَعَامِ (ط ع م), 107:3 مِسْكِينِ (س ك ن)
- Synthesis: The orphan and the poor person occupy the recipient role, food is the transferable object, and exhortation is the social action that should set provision in motion. The violent shove reverses that process by turning proximity to a dependent into expulsion.

#### Subchannel B. Household Aid, Lodging, and Credit
- Reading type: mixed
- Scene or process: Small useful resources circulate through lending, hospitality, charity, and deferred exchange, or are stopped by an owner who keeps them back.
- Active motifs: domestic utility or loan (م ع ن:B005/m01); small gift or charity (م ع ن:B005/m02); small and light-value thing (م ع ن:B003/m01); free lodging (س ك ن:B002/m02); debt obligation (د ي ن:B003/m01); lending and borrowing (د ي ن:B003/m02); withholding goods and good (م ن ع:B001/m01)
- Ayah anchors: 107:1 دِّينِ (د ي ن), 107:3 مِسْكِينِ (س ك ن), 107:7 مَاعُونَ (م ع ن), 107:7 يَمْنَعُونَ (م ن ع)
- Synthesis: A utensil, gift, room, or loan can be modest in scale yet decisive in use. Debt and deferred exchange enlarge the same interpersonal frame: one party has temporary command of a resource, another has a claim upon it, and withholding closes the route by which benefit should return.

#### Subchannel C. Livelihood That Permits Staying
- Reading type: latent/lexical
- Scene or process: Water, income, food, and pasture accumulate into a dependable provision base that lets residents remain in one place.
- Active motifs: well-provisioned livelihood (ط ع م:B004/m01); income source or productive holding (ط ع م:B004/m03); provisions that sustain residence (س ك ن:B010/m01); pasture that prevents migration (س ك ن:B010/m02); flowing visible water (م ع ن:B001/m01); dwelling place (م ع ن:B006/m01)
- Ayah anchors: 107:3 طَعَامِ (ط ع م), 107:3 مِسْكِينِ (س ك ن), 107:7 مَاعُونَ (م ع ن)
- Synthesis: The scene moves from available water and productive assets to stored or renewable provision, then to continued residence. Livelihood is not merely possession here; it is the material condition that converts movement into settlement.

### 2. Worship, Judgment, and Moral Exposure
- Semantic invariant: Religious obligation becomes visible through prayer, mercy, and social response, while denial, neglect, and display place the actor before reckoning and consequence.
- Surface relation: direct; 107:1 دِّينِ / يُكَذِّبُ, 107:4 وَيْلٌ لِّلْمُصَلِّينَ, 107:5 صَلَاتِهِمْ سَاهُونَ, and 107:6 يُرَآءُونَ.
- Surprising reach: Prayer spans ritual performance, blessing, divine mercy, personal solace, and exposure to punitive heat.

#### Subchannel A. Reckoning, Denial, and Doom
- Reading type: mixed
- Scene or process: A denied judgment culminates in recompense, ruin, and exposure to an ordeal figured as consuming heat.
- Active motifs: judgment and reckoning (د ي ن:B002/m01); recompense (د ي ن:B002/m02); denial or attribution of falsehood (ك ذ ب:B002/m01); doom and destruction (و ي ل:B001/m01); exposure to heat and ordeal (ص ل و:B001/m03)
- Ayah anchors: 107:1 دِّينِ (د ي ن), 107:1 يُكَذِّبُ (ك ذ ب), 107:4 وَيْلٌ (و ي ل), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و)
- Synthesis: Denial targets the reality of reckoning, but the judgment sense of religion restores an answering event in which acts receive recompense. Woe names the outcome, while the fire sense of the prayer root supplies a concrete image of ordeal.

#### Subchannel B. Obedience, Prayer, and Blessing
- Reading type: mixed
- Scene or process: A worshipper enters an order of obedience, performs prescribed prayer, and directs blessing or mercy toward another.
- Active motifs: obedience and submission (د ي ن:B001/m01); creed and worship order (د ي ن:B001/m02); prescribed ritual prayer (ص ل و:B003/m01); prayer and blessing for another (ص ل و:B002/m01); divine mercy and purification (ص ل و:B002/m02); prayer as a source of repose (س ك ن:B004/m01); religious due and obedience (م ع ن:B005/m03)
- Ayah anchors: 107:1 دِّينِ (د ي ن), 107:3 مِسْكِينِ (س ك ن), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و), 107:7 مَاعُونَ (م ع ن)
- Synthesis: Obedience supplies the governing relation, ritual prayer supplies the enacted form, and blessing or mercy supplies the outward-directed effect. Prayer can also become a place of inward repose, while the religious-due sense of small aid carries observance into material service.

#### Subchannel C. Negligent and Ostentatious Observance
- Reading type: surface-primary
- Scene or process: Ritual action remains publicly visible while attention leaves the act and concern shifts toward the gaze of other people.
- Active motifs: prescribed ritual prayer (ص ل و:B003/m01); lapse within prayer (س ه و:B001/m02); general neglect and shortcoming (ي ت م:B003/m01); ostentatious display (ر ء ي:B005/m01); deceptive action (ك ذ ب:B001/m02)
- Ayah anchors: 107:1 يُكَذِّبُ (ك ذ ب), 107:2 ٱلْيَتِيمَ (ي ت م), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و), 107:5 سَاهُونَ (س ه و), 107:6 يُرَآءُونَ (ر ء ي)
- Synthesis: The body preserves the recognizable form of prayer, but attention has withdrawn and the act is redirected toward spectators. Neglect names the inner absence, ostentation names the social orientation, and deceptive action names the gap between visible observance and operative purpose.

### 3. Visibility, Display, and Readable Signs
- Semantic invariant: Sight makes an object, person, or hidden state legible through reflection, public display, or a diagnostic trace.
- Surface relation: direct; 107:1 أَرَءَيْتَ and 107:6 يُرَآءُونَ.
- Surprising reach: Visuality reaches from mirrors and banners to pregnancy, menstrual indication, facial marks, and barely perceptible celestial signs.

#### Subchannel A. Reflective Inspection and Outward Form
- Reading type: latent/lexical
- Scene or process: An observer uses direct sight or a mirror to inspect outward form and read what appears on a face or in a visibly flourishing condition.
- Active motifs: sensory sight (ر ء ي:B001/m01); mirror (ر ء ي:B006/m01); outward beauty and appearance (ر ء ي:B006/m02); facial sign (ر ء ي:B006/m03); mirror presentation (ر ء ي:B012/m02); well-provisioned condition (ط ع م:B004/m01)
- Ayah anchors: 107:1 أَرَءَيْتَ and 107:6 يُرَآءُونَ (ر ء ي), 107:3 طَعَامِ (ط ع م)
- Synthesis: The mirror and the eye form an inspection mechanism: outward form is presented, viewed, and interpreted. A flourishing livelihood can register in appearance, so material condition becomes visible rather than remaining an unseen possession.

#### Subchannel B. Public Display and Visual Standards
- Reading type: mixed
- Scene or process: People or groups arrange themselves to be seen, using display, mutual visibility, and raised markers to direct a public gaze.
- Active motifs: mutual visibility and facing (ر ء ي:B004/m01); ostentatious display (ر ء ي:B005/m01); raised standard or banner (ر ء ي:B011/m01); deliberate showing (ر ء ي:B012/m01); deceptive patterned cloth (ك ذ ب:B009/m01)
- Ayah anchors: 107:1 أَرَءَيْتَ and 107:6 يُرَآءُونَ (ر ء ي), 107:1 يُكَذِّبُ (ك ذ ب)
- Synthesis: Facing groups establish a field of mutual sight, the banner fixes a visible point within it, and deliberate showing turns action into spectacle. The patterned cloth adds a material warning that visibility can be engineered to present a state other than the underlying one.

#### Subchannel C. Bodily and Subtle Indicators
- Reading type: latent/lexical
- Scene or process: A concealed bodily or environmental state is inferred from a small visible trace.
- Active motifs: menstrual indication (ر ء ي:B007/m01); visible animal pregnancy (ر ء ي:B010/m01); enlarged udder as gestational sign (ر ء ي:B010/m02); facial indication (ر ء ي:B006/m03); faint overlooked star (س ه و:B005/m01)
- Ayah anchors: 107:1 أَرَءَيْتَ and 107:6 يُرَآءُونَ (ر ء ي), 107:5 سَاهُونَ (س ه و)
- Synthesis: A discharge marker, enlarged udder, facial trace, or tiny star does not display the whole state; it provides a discriminating sign from which that state is known. Seeing therefore includes sustained attention to what is easy to overlook.

### 4. Settlement, Sacred Space, and Civic Order
- Semantic invariant: Dwelling becomes communal settlement through domestic structure, worship space, shared utility, authority, and protection.
- Surface relation: indirect; 107:1 دِّينِ, 107:3 مِسْكِينِ, 107:4-5 مُصَلِّينَ / صَلَاتِهِمْ, 107:5 سَاهُونَ, and 107:7 مَاعُونَ / يَمْنَعُونَ.
- Surprising reach: A porch beam, household loan, temple, fortified town, and civic obedience occupy successive scales of one inhabited order.

#### Subchannel A. Household Residence and Storage
- Reading type: latent/lexical
- Scene or process: Residents inhabit a house whose porch, storage supports, sources of repose, and shared implements make daily life possible.
- Active motifs: dwelling and home (س ك ن:B002/m01); residents and household (س ك ن:B003/m01); source of repose (س ك ن:B004/m01); settled place (س ك ن:B009/m01); front porch (س ه و:B004/m01); storage crossbeams (س ه و:B004/m02); domestic utility or loan (م ع ن:B005/m01); dwelling place (م ع ن:B006/m01)
- Ayah anchors: 107:3 مِسْكِينِ (س ك ن), 107:5 سَاهُونَ (س ه و), 107:7 مَاعُونَ (م ع ن)
- Synthesis: The house is both enclosure and working system. Residents gather within it, the porch marks its threshold, crossbeams hold goods, and loanable implements move between neighboring interiors without dissolving the settled center.

#### Subchannel B. Protected Civic and Sacred Center
- Reading type: latent/lexical
- Scene or process: A town organizes obedience around a house of worship, maintains communal dues, and protects its inhabited territory.
- Active motifs: city as a seat of obedience (د ي ن:B006/m01); house of worship (ص ل و:B007/m01); fortified place (م ن ع:B003/m02); defensive strength (م ن ع:B003/m01); communal religious due (م ع ن:B005/m03); settled place (س ك ن:B009/m01)
- Ayah anchors: 107:1 دِّينِ (د ي ن), 107:3 مِسْكِينِ (س ك ن), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و), 107:7 مَاعُونَ (م ع ن), 107:7 يَمْنَعُونَ (م ن ع)
- Synthesis: Authority, worship, and defense converge in a protected settlement. The worship house gives the town a ritual center, civic obedience supplies order, communal dues circulate benefit, and fortification preserves access to the shared place.

### 5. Plant Gathering, Cultivation, and Preparation
- Semantic invariant: Water and human handling transform wild or cultivated plant material into pasture, food, or remedy.
- Surface relation: indirect; 107:2 يَدُعُّ, 107:3 يَحُضُّ / طَعَامِ / مِسْكِينِ, 107:4-5 مُصَلِّينَ / صَلَاتِهِمْ, and 107:7 مَاعُونَ.
- Surprising reach: Food provision opens onto aquatic forage, tufted camel grass, famine seed, graft acceptance, grinding stone, and bitter medicinal resin.

#### Subchannel A. Watered Pasture and Cattle Feed
- Reading type: latent/lexical
- Scene or process: Flowing water sustains summer plants and abundant pasture, grazing animals consume the forage, and nourishment appears in bodily fat.
- Active motifs: flowing visible water (م ع ن:B001/m01); summer water plant grazed by cattle (د ع ع:B008/m01); camel forage grass (ص ل و:B009/m01); pasture that prevents migration (س ك ن:B010/m02); livestock fat and marrow condition (ط ع م:B007/m01)
- Ayah anchors: 107:2 يَدُعُّ (د ع ع), 107:3 مِسْكِينِ (س ك ن), 107:3 طَعَامِ (ط ع م), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و), 107:7 مَاعُونَ (م ع ن)
- Synthesis: Water produces a grazing zone durable enough to halt migration. Aquatic plants and tufted grass pass into the herd as nourishment, with fat and marrow marking the outcome of successful pasture.

#### Subchannel B. Famine Seed and Grinding Slab
- Reading type: latent/lexical
- Scene or process: A wild edible seed is gathered under scarcity and reduced on a broad stone into usable food.
- Active motifs: wild famine seed (د ع ع:B010/m01); black-ant lookalike (د ع ع:B010/m02); grinding slab (ص ل و:B008/m01); food as sustenance (ط ع م:B001/m02); productive livelihood (ط ع م:B004/m03)
- Ayah anchors: 107:2 يَدُعُّ (د ع ع), 107:3 طَعَامِ (ط ع م), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و)
- Synthesis: The seed supplies an emergency food object, its ant-like form aids recognition, and the slab supplies the processing tool. Scarcity thus produces a compact gathering-and-pounding scene rather than an abstract notion of provision.

#### Subchannel C. Grafting, Ripening, and Fruitful Yield
- Reading type: latent/lexical
- Scene or process: A foreign branch is joined to a tree, the union takes, water sustains growth, and fruit reaches perceptible maturity.
- Active motifs: graft acceptance (ط ع م:B010/m01); fruit ripening (ط ع م:B005/m01); productive tree or milk yield (ط ع م:B005/m03); flowing irrigation water (م ع ن:B001/m02); sensory inspection (ر ء ي:B001/m01)
- Ayah anchors: 107:1 أَرَءَيْتَ and 107:6 يُرَآءُونَ (ر ء ي), 107:3 طَعَامِ (ط ع م), 107:7 مَاعُونَ (م ع ن)
- Synthesis: Joining is followed by acceptance, growth, and visible yield. The eye verifies the successful union and ripening, while water provides the material continuity between graft and fruit.

#### Subchannel D. Bitter Medicinal Material
- Reading type: latent/lexical
- Scene or process: A bitter resinous substance, including an animal-derived preparation, is gathered and handled as medicine alongside other wild plant materials.
- Active motifs: bitter medicinal resin (ح ض ض:B003/m01); camel-derived medicinal preparation (ح ض ض:B003/m02); forage plant material (ص ل و:B009/m01); grinding slab (ص ل و:B008/m01); visible inspection of appearance (ر ء ي:B006/m02)
- Ayah anchors: 107:3 يَحُضُّ (ح ض ض), 107:1 أَرَءَيْتَ and 107:6 يُرَآءُونَ (ر ء ي), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و)
- Synthesis: The medicinal object is defined by bitterness, resinous matter, and an unusual animal-derived ingredient. Plant material and a pounding surface place it within a preparation scene, while visual inspection tracks the material being handled.

### 6. Blocking, Capturing, and Defending
- Semantic invariant: An actor controls access or escape by shoving, restraining, trapping, fortifying, or refusing entry.
- Surface relation: direct; 107:2 يَدُعُّ and 107:7 يَمْنَعُونَ.
- Surprising reach: Social repulsion and withheld aid extend into battlefield resistance, hunting capture, defended settlements, and personal chastity.

#### Subchannel A. Forceful Exclusion and Reciprocal Struggle
- Reading type: mixed
- Scene or process: One actor drives another away or toward danger, while opposing force turns unilateral coercion into a contest.
- Active motifs: forceful shove and rebuff (د ع ع:B001/m01); coercive redirection (د ع ع:B001/m02); battle incitement (ح ض ض:B001/m02); reciprocal resistance (م ن ع:B006/m01); choking restraint (ط ع م:B012/m02); coercive domination (د ي ن:B004/m01)
- Ayah anchors: 107:1 دِّينِ (د ي ن), 107:2 يَدُعُّ (د ع ع), 107:3 يَحُضُّ (ح ض ض), 107:3 طَعَامِ (ط ع م), 107:7 يَمْنَعُونَ (م ن ع)
- Synthesis: Shoving, incitement, and throat restraint place force directly on a body. Reciprocal resistance changes the relation from expulsion to struggle, while domination names the durable hierarchy that coercion seeks to produce.

#### Subchannel B. Trapping and Capture
- Reading type: latent/lexical
- Scene or process: A hunter marks or watches a field, sets a snare, uses a hunting implement, and stills the captured animal.
- Active motifs: raised visual standard (ر ء ي:B011/m01); hunting snare (ص ل و:B004/m01); hunting implement or animal that supplies prey (ط ع م:B006/m01); knife (س ك ن:B007/m01); stilling through slaughter (س ك ن:B007/m02); obstacle or barrier (م ن ع:B002/m01)
- Ayah anchors: 107:1 أَرَءَيْتَ and 107:6 يُرَآءُونَ (ر ء ي), 107:3 مِسْكِينِ (س ك ن), 107:3 طَعَامِ (ط ع م), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و), 107:7 يَمْنَعُونَ (م ن ع)
- Synthesis: The visible marker organizes the hunting space, the snare and barrier close an escape route, and the bow or trained animal converts capture into food. The knife completes the mechanism by ending the prey's movement.

#### Subchannel C. Fortification and Protective Strength
- Reading type: latent/lexical
- Scene or process: A defended place prevents hostile access through enclosure, collective strength, and protective aid.
- Active motifs: obstacle or barrier (م ن ع:B002/m01); defensive strength (م ن ع:B003/m01); fortified place (م ن ع:B003/m02); protective aid (م ن ع:B003/m03); city as seat of authority (د ي ن:B006/m01)
- Ayah anchors: 107:1 دِّينِ (د ي ن), 107:7 يَمْنَعُونَ (م ن ع)
- Synthesis: The barrier supplies the immediate obstruction, the fortress gives it durable spatial form, and collective strength supplies an agent capable of maintaining it. Protective aid turns prevention from private refusal into communal defense.

#### Subchannel D. Chastity and Guarded Personal Access
- Reading type: latent/lexical
- Scene or process: A woman without a spouse maintains bodily and social boundaries through refusal and guarded access.
- Active motifs: chaste refusal (م ن ع:B004/m01); woman without a spouse (ي ت م:B005/m01); menstrual indication (ر ء ي:B007/m01); self-directed resolve (ح ض ض:B004/m01)
- Ayah anchors: 107:2 ٱلْيَتِيمَ (ي ت م), 107:3 يَحُضُّ (ح ض ض), 107:1 أَرَءَيْتَ and 107:6 يُرَآءُونَ (ر ء ي), 107:7 يَمْنَعُونَ (م ن ع)
- Synthesis: Marital status, bodily indication, and deliberate refusal define a guarded personal sphere. The resistance sense of prevention becomes self-protection rather than an obstacle imposed by an external adversary.

### 7. Motion, Stilling, and Ordered Position
- Semantic invariant: Movement is prompted, extended, slowed, interrupted, ranked, or stabilized by a controlling mechanism.
- Surface relation: indirect; 107:2 يَدُعُّ / ٱلْيَتِيمَ, 107:3 طَعَامِ / مِسْكِينِ, 107:4-5 مُصَلِّينَ / صَلَاتِهِمْ, and 107:7 مَاعُونَ.
- Surprising reach: A horse's muzzle, the second runner, a stopping animal, a ship's rudder, and successive formation all encode controlled progression.

#### Subchannel A. Horse Race and Second Position
- Reading type: latent/lexical
- Scene or process: A horse is prompted from the muzzle into an extended run and takes a measured position immediately behind the leader.
- Active motifs: horse muzzle and lips (ط ع م:B009/m01); prompting a horse to run (ط ع م:B009/m02); extended run (م ع ن:B002/m01); second horse behind the winner (ص ل و:B006/m01)
- Ayah anchors: 107:3 طَعَامِ (ط ع م), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و), 107:7 مَاعُونَ (م ع ن)
- Synthesis: Contact at the muzzle initiates motion, the run opens distance, and the second horse receives a position defined by the leader's body. The scene combines propulsion with relational ranking.

#### Subchannel B. Slow and Interrupted Movement
- Reading type: latent/lexical
- Scene or process: A moving body twists or lags, then may halt and look back rather than complete an uninterrupted course.
- Active motifs: slow winding run (د ع ع:B005/m01); slow travel (ي ت م:B004/m01); animal run interrupted by a backward stop (ك ذ ب:B007/m01); cessation of movement (س ك ن:B001/m01); calm stillness (س ه و:B002/m01)
- Ayah anchors: 107:1 يُكَذِّبُ (ك ذ ب), 107:2 يَدُعُّ (د ع ع), 107:2 ٱلْيَتِيمَ (ي ت م), 107:3 مِسْكِينِ (س ك ن), 107:5 سَاهُونَ (س ه و)
- Synthesis: Twisting gait and delayed travel weaken forward progress before the stopping animal makes interruption explicit. Stillness is the endpoint of the sequence, while the backward glance gives the halt a directional reversal.

#### Subchannel C. Steering a Vessel into Stability
- Reading type: latent/lexical
- Scene or process: A vessel moves on flowing water while a rudder or stern element counters oscillation and establishes a stable course.
- Active motifs: flowing water (م ع ن:B001/m01); ship's rudder or stabilizing stern (س ك ن:B008/m01); stability after motion (س ك ن:B001/m02); obstacle that redirects action (م ن ع:B002/m01)
- Ayah anchors: 107:3 مِسْكِينِ (س ك ن), 107:7 مَاعُونَ (م ع ن), 107:7 يَمْنَعُونَ (م ن ع)
- Synthesis: Water supplies the moving setting, the steering component resists unwanted deviation, and stability is the resulting state. Prevention here is functional redirection rather than simple refusal.

#### Subchannel D. Succession and Ordered Formation
- Reading type: latent/lexical
- Scene or process: One formed unit follows another in an ordered series, analogous to a second runner maintaining position in forward motion.
- Active motifs: successive formation (ط ع م:B014/m01); second position (ص ل و:B006/m01); extended forward motion (م ع ن:B002/m01); action without delay (ك ذ ب:B005/m01)
- Ayah anchors: 107:1 يُكَذِّبُ (ك ذ ب), 107:3 طَعَامِ (ط ع م), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و), 107:7 مَاعُونَ (م ع ن)
- Synthesis: Sequence is represented as close following: a second unit appears after the first without breaking continuity. The race image gives spatial form to succession, while prompt action preserves the temporal link.

### 8. Livestock Body, Reproduction, and Dependency
- Semantic invariant: Animal life is read through anatomy, gestation, milk, grazing, maternal attachment, and youthful resilience.
- Surface relation: indirect; 107:1 أَرَءَيْتَ / يُكَذِّبُ, 107:2 يَدُعُّ / ٱلْيَتِيمَ, 107:3 طَعَامِ, 107:4-5 مُصَلِّينَ / صَلَاتِهِمْ, and 107:7 يَمْنَعُونَ.
- Surprising reach: Visual pregnancy, loins, lung, marrow, failed milk, orphaned animals, and young stock resisting the year form a single husbandry horizon.

#### Subchannel A. Anatomy and Bodily Condition
- Reading type: latent/lexical
- Scene or process: An animal's condition is assessed through its loins, lung, fat, and marrow.
- Active motifs: loins and tail flanks (ص ل و:B005/m01); lung (ر ء ي:B009/m01); pulmonary ailment (ر ء ي:B009/m02); livestock fat and marrow condition (ط ع م:B007/m01)
- Ayah anchors: 107:1 أَرَءَيْتَ and 107:6 يُرَآءُونَ (ر ء ي), 107:3 طَعَامِ (ط ع م), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و)
- Synthesis: External frame, internal organ, and nutritive tissue create a part-to-condition map of the animal body. The loins give structural form, the lung supplies vital function, and fat or marrow registers nourishment.

#### Subchannel B. Pregnancy, Milk, and Maternal Severance
- Reading type: latent/lexical
- Scene or process: Gestation becomes visible in body and udder, but milk may fail and the young animal may be cut off from its mother.
- Active motifs: visible pregnancy (ر ء ي:B010/m01); enlarged udder (ر ء ي:B010/m02); milk yield that fails to persist (ك ذ ب:B006/m01); motherless animal (ي ت م:B001/m02); productive milk yield (ط ع م:B005/m03)
- Ayah anchors: 107:1 أَرَءَيْتَ / يُكَذِّبُ and 107:6 يُرَآءُونَ (ر ء ي, ك ذ ب), 107:2 ٱلْيَتِيمَ (ي ت م), 107:3 طَعَامِ (ط ع م)
- Synthesis: Pregnancy is inferred from enlargement, and the udder carries an expectation of nourishment. Failed milk breaks that expectation, while maternal loss turns interrupted yield into a condition of dependency.

#### Subchannel C. Herding and Seasonal Resilience
- Reading type: latent/lexical
- Scene or process: A herder calls young stock through a grazing landscape where water plants and forage allow them to withstand the year.
- Active motifs: herding call and rebuke (د ع ع:B003/m01); summer water plant grazed by cattle (د ع ع:B008/m01); camel forage grass (ص ل و:B009/m01); pasture that prevents migration (س ك ن:B010/m02); youthful camel or goat resisting the year (م ن ع:B007/m01)
- Ayah anchors: 107:2 يَدُعُّ (د ع ع), 107:3 مِسْكِينِ (س ك ن), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و), 107:7 يَمْنَعُونَ (م ن ع)
- Synthesis: The call supplies human direction, pasture supplies the feeding setting, and youth supplies the animals' capacity to endure seasonal pressure. Resistance is physiological persistence rather than conflict with another agent.

### 9. Inner Attention, Self-Deception, and Recovery
- Semantic invariant: The inner self can deliberate and urge itself toward action, lose attention, deceive itself, or recover through renewed direction.
- Surface relation: direct; 107:1 أَرَءَيْتَ / يُكَذِّبُ, 107:3 يَحُضُّ / طَعَامِ, and 107:5 سَاهُونَ.
- Surprising reach: Exhortation shifts inward, while taste vocabulary supplies reason, worth, responsiveness, and capacity as faculties of self-command.

#### Subchannel A. Deliberation and Self-Exhortation
- Reading type: latent/lexical
- Scene or process: A person considers a course, consults judgment, and presses the self toward increased action.
- Active motifs: opinion and judgment (ر ء ي:B002/m01); deliberation and consultation (ر ء ي:B002/m02); self-exhortation toward increase (ح ض ض:B004/m01); reason and prudence (ط ع م:B008/m01); capacity for action (ط ع م:B011/m01)
- Ayah anchors: 107:1 أَرَءَيْتَ and 107:6 يُرَآءُونَ (ر ء ي), 107:3 يَحُضُّ (ح ض ض), 107:3 طَعَامِ (ط ع م)
- Synthesis: Reflection establishes possible action, prudence weighs it, capacity makes it executable, and self-exhortation supplies the internal push. The scene converts command from an interpersonal speech act into self-government.

#### Subchannel B. Inattention and the Deceptive Self
- Reading type: mixed
- Scene or process: Attention leaves an obligation while the self supplies a misleading account of its own state or value.
- Active motifs: mental inattention (س ه و:B001/m01); neglect and shortcoming (ي ت م:B003/m01); deceptive self (ك ذ ب:B008/m01); loss of worth or responsiveness (ط ع م:B008/m02); attention and inquiry (ر ء ي:B013/m01)
- Ayah anchors: 107:1 أَرَءَيْتَ / يُكَذِّبُ (ر ء ي, ك ذ ب), 107:2 ٱلْيَتِيمَ (ي ت م), 107:3 طَعَامِ (ط ع م), 107:5 سَاهُونَ (س ه و)
- Synthesis: Neglect is a withdrawal of attention, but self-deception obscures that withdrawal from the actor. The inquiry formula interrupts the closed loop by directing perception back toward conduct and consequence.

#### Subchannel C. Forbearance After a Stumble
- Reading type: latent/lexical
- Scene or process: A faltering person is called to rise while another overlooks the lapse and answers with a restorative blessing.
- Active motifs: restorative call to one who stumbles (د ع ع:B004/m01); wish or blessing to be raised (د ع ع:B004/m02); forbearance and overlooking another's slip (س ه و:B003/m01); prayer and blessing for another (ص ل و:B002/m01)
- Ayah anchors: 107:2 يَدُعُّ (د ع ع), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و), 107:5 سَاهُونَ (س ه و)
- Synthesis: The stumble provides the lapse, the call supplies immediate direction, and forbearance prevents the lapse from becoming permanent exclusion. Blessing completes the recovery by turning rebuke into a wish for renewed standing.

### 10. Truth, Pretense, and Reliability
- Semantic invariant: A word, surface, charge, yield, or motion is tested by whether appearance and expectation continue into actuality.
- Surface relation: direct; 107:1 أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ and 107:6 يُرَآءُونَ.
- Surprising reach: False speech extends into patterned cloth, failed milk, a broken charge, an animal that stops mid-run, and the contrasting image of action carried through without delay.

#### Subchannel A. False Assertion and Attribution
- Reading type: surface-primary
- Scene or process: A speaker advances a false claim or assigns falsehood to another, while judgment and testimony establish the contested truth frame.
- Active motifs: false speech (ك ذ ب:B001/m01); attribution of falsehood or denial (ك ذ ب:B002/m01); judgment and reckoning (د ي ن:B002/m01); certification in judgment or oath (د ي ن:B007/m01); attention and request for report (ر ء ي:B013/m01)
- Ayah anchors: 107:1 أَرَءَيْتَ (ر ء ي), 107:1 يُكَذِّبُ (ك ذ ب), 107:1 دِّينِ (د ي ن)
- Synthesis: Inquiry opens a reportable claim, denial contests it, and judgment supplies the setting in which claim and claimant are assessed. Certification or oath introduces the counter-operation of entrusting a speaker within that truth relation.

#### Subchannel B. Deceptive Surface and Public Pretense
- Reading type: mixed
- Scene or process: A crafted appearance presents itself as more or other than it is, and public performance uses the same gap between surface and state.
- Active motifs: deceptive patterned cloth (ك ذ ب:B009/m01); deceptive action (ك ذ ب:B001/m02); ostentatious display (ر ء ي:B005/m01); outward appearance (ر ء ي:B006/m02); mirror (ر ء ي:B006/m01)
- Ayah anchors: 107:1 يُكَذِّبُ (ك ذ ب), 107:1 أَرَءَيْتَ and 107:6 يُرَآءُونَ (ر ء ي)
- Synthesis: Pattern and color make cloth appear unlike its underlying state; ostentation performs the same operation socially. The mirror and the watching eye provide the apparatus by which the crafted surface is produced and received.

#### Subchannel C. Failure to Persist
- Reading type: latent/lexical
- Scene or process: An expected action or yield begins but breaks off before its promise is fulfilled.
- Active motifs: failed or cowardly charge (ك ذ ب:B004/m01); milk yield that disappears (ك ذ ب:B006/m01); animal run interrupted by a stop and backward look (ك ذ ب:B007/m01); slow travel (ي ت م:B004/m01)
- Ayah anchors: 107:1 يُكَذِّبُ (ك ذ ب), 107:2 ٱلْيَتِيمَ (ي ت م)
- Synthesis: Charge, milk, and flight each create an expectation of continuation. Their premature ending gives falsehood a temporal form: the beginning announces a course that the outcome does not sustain.

#### Subchannel D. Prompt and Resolute Continuation
- Reading type: latent/lexical
- Scene or process: An actor commits to movement and carries it forward without delay or retreat.
- Active motifs: resolute charge (ك ذ ب:B004/m02); action without delay (ك ذ ب:B005/m01); extended run (م ع ن:B002/m01); capacity for action (ط ع م:B011/m01)
- Ayah anchors: 107:1 يُكَذِّبُ (ك ذ ب), 107:3 طَعَامِ (ط ع م), 107:7 مَاعُونَ (م ع ن)
- Synthesis: Capacity initiates action, promptness removes hesitation, and extended motion demonstrates persistence. The resolute charge reverses the failed-continuation scene by aligning announced movement with completed advance.

### 11. Questions, Commands, and Calls
- Semantic invariant: Directed utterances organize attention and action by asking, pointing, exhorting, prohibiting, calling, or lamenting.
- Surface relation: direct; 107:1 أَرَءَيْتَ, 107:3 يَحُضُّ, and 107:4 وَيْلٌ.
- Surprising reach: The discourse frame includes demonstratives and relative linkage as well as battle cries, herding calls, restorative formulas, and prohibitive commands.

#### Subchannel A. Inquiry and Deictic Attention
- Reading type: mixed
- Scene or process: A speaker summons an addressee's attention, points out a referent, and frames a request for identification or report.
- Active motifs: attention and inquiry formula (ر ء ي:B013/m01); demonstrative pointer (ذ و و:B003/m01); interrogative compound (ذ و و:B004/m01); relative connector (ذ و و:B002/m01); possession and attribution (ذ و و:B001/m01)
- Ayah anchors: 107:1 أَرَءَيْتَ (ر ء ي); 107:2 فَذَٰلِكَ / ٱلَّذِى (ذ و و)
- Synthesis: The attention formula opens the inquiry, the demonstrative fixes a target, and relative or possessive linkage identifies that target through relation. Questioning is therefore built as a sequence of orientation, pointing, and specification.

#### Subchannel B. Exhortation and Prohibitive Command
- Reading type: mixed
- Scene or process: A speaker attempts to move another person toward an act or stop an act already contemplated.
- Active motifs: exhortation toward good or food (ح ض ض:B001/m01); battle incitement (ح ض ض:B001/m02); imperative to take up or adhere (ك ذ ب:B003/m01); prohibitive command (م ن ع:B005/m01); coercive redirection (د ع ع:B001/m02)
- Ayah anchors: 107:1 يُكَذِّبُ (ك ذ ب), 107:2 يَدُعُّ (د ع ع), 107:3 يَحُضُّ (ح ض ض), 107:7 يَمْنَعُونَ (م ن ع)
- Synthesis: Exhortation projects a desired action, the imperative presses immediate adherence, and prohibition blocks a competing course. Battle incitement and charitable urging reveal opposite practical ends carried by the same directive force.

#### Subchannel C. Herding Call, Restorative Cry, and Lament
- Reading type: latent/lexical
- Scene or process: A voiced formula reaches an animal, a fallen person, or a community in distress and attempts to orient the hearer to danger, movement, or recovery.
- Active motifs: herding call and rebuke (د ع ع:B003/m01); restorative rise-call (د ع ع:B004/m01); blessing to be raised (د ع ع:B004/m02); lament cry (و ي ل:B002/m01); disgrace and calamity (و ي ل:B002/m02)
- Ayah anchors: 107:2 يَدُعُّ (د ع ع), 107:4 وَيْلٌ (و ي ل)
- Synthesis: The herding cry directs movement, the rise-call answers a stumble, and lament voices a calamity already present. Across the three settings, sound marks urgency and reorients attention toward an immediate condition.

### 12. Fire as Comfort and Ordeal
- Semantic invariant: Contact with fire can sustain domestic life through warmth and cooking or consume the sufferer as punitive heat.
- Surface relation: indirect; 107:3 طَعَامِ / مِسْكِينِ, 107:4 وَيْلٌ / مُصَلِّينَ, and 107:5 صَلَاتِهِمْ.
- Surprising reach: The prayer root opens both the hearth scene and the ordeal scene, while the dwelling root names fire as a source of repose.

#### Subchannel A. Hearth Warmth and Roasting
- Reading type: latent/lexical
- Scene or process: People gather near fire for warmth while food is exposed to heat for roasting.
- Active motifs: warming oneself by fire (ص ل و:B001/m01); roasting and burning (ص ل و:B001/m02); fire as a source of repose (س ك ن:B004/m01); food and tasting (ط ع م:B001/m01)
- Ayah anchors: 107:3 مِسْكِينِ (س ك ن), 107:3 طَعَامِ (ط ع م), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و)
- Synthesis: Fire creates a domestic center by warming bodies and transforming food. Its heat is welcomed and controlled, and the resulting comfort helps define the inhabited setting.

#### Subchannel B. Punitive Heat and Woe
- Reading type: mixed
- Scene or process: The same heat becomes an imposed ordeal associated with ruin, judgment, and lament.
- Active motifs: exposure to heat and hardship (ص ل و:B001/m03); doom and destruction (و ي ل:B001/m01); lament and calamity (و ي ل:B002/m01); judgment and recompense (د ي ن:B002/m01)
- Ayah anchors: 107:1 دِّينِ (د ي ن), 107:4 وَيْلٌ (و ي ل), 107:4 مُصَلِّينَ and 107:5 صَلَاتِهِمْ (ص ل و)
- Synthesis: Controlled warmth becomes uncontrolled exposure, and the hearth's sustaining function reverses into suffering. Judgment supplies the cause-and-consequence frame, while woe voices the resulting destruction.

## Standalone Subchannels

### S1. Filled Vessel and Lowland Catchment
- Reading type: latent/lexical
- Scene or process: Repeated agitation packs a vessel to capacity, while flowing water fills a low place at the foot of a mountain.
- Active motifs: shaking a vessel until full (د ع ع:B002/m01); filled platter or valley (د ع ع:B002/m02); lowland at a mountain foot (ح ض ض:B002/m01); base surface for placing (ح ض ض:B002/m02); flowing water (م ع ن:B001/m01)
- Ayah anchors: 107:2 يَدُعُّ (د ع ع), 107:3 يَحُضُّ (ح ض ض), 107:7 مَاعُونَ (م ع ن)
- Synthesis: Container and terrain share a form-and-capacity relation. Agitation makes a bounded vessel receive more material, while gravity makes the lowland receive running water; in both cases a lower enclosing surface becomes full.

### S2. Dream Images in Flowing Sequence
- Reading type: latent/lexical
- Scene or process: Dream images appear one after another with the continuity and movement of visible running water.
- Active motifs: dream vision (ر ء ي:B003/m01); successive formation (ط ع م:B014/m01); flowing visible water (م ع ن:B001/m01); sensory sight (ر ء ي:B001/m01)
- Ayah anchors: 107:1 أَرَءَيْتَ and 107:6 يُرَآءُونَ (ر ء ي), 107:3 طَعَامِ (ط ع م), 107:7 مَاعُونَ (م ع ن)
- Synthesis: The dream supplies the perceptual setting, successive formation supplies temporal order, and running water supplies the motion analogy. The resulting channel treats imagination as a visible sequence whose forms continuously replace one another.

### S3. Spirit-Mediated Divination and Healing
- Reading type: latent/lexical
- Scene or process: A spirit familiar appears to a person and discloses divinatory or healing knowledge.
- Active motifs: appearing spirit familiar (ر ء ي:B008/m01); divinatory or healing disclosure (ر ء ي:B008/m02)
- Ayah anchors: 107:1 أَرَءَيْتَ and 107:6 يُرَآءُونَ (ر ء ي)
- Synthesis: The familiar is the mediating agent, appearance establishes contact, and disclosed divination or medicine is the outcome. Vision functions here as an encounter that transfers otherwise inaccessible knowledge.


===== _commentary/v16/work/s107/surah.r2.hftbundle/hft.md =====
# HFT: earlier activation hypotheses, per focus ayah of surah 107

Note: HFT used an older root map; a trace step on a root the gateway now withholds is an echo, not identity.

# Focus 107:1

## alerted recognition
- reading: An alerting summons to recognize a recurring human type whose relation to lived dīn can be inspected.
- mechanism: The seeing root combines perceptual recognition with an alerting tell-me formula. The question therefore recruits the addressee as a witness who must identify a type, while the denial root supplies the type's defining relation to dīn.
- trace:
  - 107:1 **أَرَءَيْتَ** ر ء ي B013: The alerting and inquiring use makes the opening a summons to recognize and characterize, not a request for bare visual history.
  - 107:1 **أَرَءَيْتَ** ر ء ي B001: Eye-seeing and insight keep the demanded recognition both observable and interpretive.
  - 107:1 **يُكَذِّبُ** ك ذ ب B002: Declaring a thing false supplies the relation by which the person is to be recognized.
  - 107:1 **بِٱلدِّينِ** د ي ن B001: Obedience and lived submission make dīn a practice-bearing object rather than a label alone.

## rejected reckoning
- reading: The person nullifies the claim that action is answerable and will be requited, a stance the addressee is asked to diagnose.
- mechanism: Denial targets not only a religious proposition but the operative claim that deeds enter judgment and return as recompense. Reflective seeing asks the addressee to grasp the behavioral consequences of treating that account as false.
- trace:
  - 107:1 **يُكَذِّبُ** ك ذ ب B002: Attribution of falsehood gives denial an object whose authority is actively rejected.
  - 107:1 **بِٱلدِّينِ** د ي ن B002: Reckoning and requital make the rejected object an account in which conduct has consequences.
  - 107:1 **أَرَءَيْتَ** ر ء ي B002: Reflective judgment turns seeing into inference from a person's stance toward accountability.

## moral default
- reading: Denial is a practical default on an entrusted and eventually settleable obligation.
- mechanism: Dīn can configure an obligation as something owed, while denial can be tested by whether a charge is fulfilled or fails in execution. The denier is thus readable as a practical defaulter who treats a due claim as though it will never mature.
- trace:
  - 107:1 **بِٱلدِّينِ** د ي ن B003: Debt and deferred settlement supply an obligation that remains due even before collection.
  - 107:1 **يُكَذِّبُ** ك ذ ب B004: A charge that fails to be carried through converts falsehood from speech into nonperformance.
  - 107:1 **بِٱلدِّينِ** د ي ن B007: Crediting a person and leaving him to conscience sharpens the risk that entrusted responsibility will be betrayed.

## lived counterfeit
- reading: The denier may be identified by a lived surface whose repeated condition falsifies the order it appears to bear.
- mechanism: A visible surface can misstate its own condition, while dīn can name a customary mode of life. The focus ayah can therefore hold open a person whose displayed identity and practiced habit contradict one another, even before context specifies the contradiction.
- trace:
  - 107:1 **أَرَءَيْتَ** ر ء ي B006: Visible appearance and the mirror supply a surface that may need interpretation rather than trust.
  - 107:1 **يُكَذِّبُ** ك ذ ب B009: The deceptively patterned cloth supplies an image of a condition whose surface gives a false account of itself.
  - 107:1 **بِٱلدِّينِ** د ي ن B005: Habit and customary state relocate dīn into the person's repeated way of being.

## deictic social proof
- reading: The demonstratively identified denier is recognized by force that deepens an already vulnerable person's social severance.
- mechanism: The deictic answer converts the opening recognition task into an observable test: the denier forcibly drives away someone already cut off from a caregiver. Severe force aggravates prior severance, so repudiating dīn becomes enacted refusal of a protective debt rather than an invisible opinion.
- trace:
  - 107:1 **أَرَءَيْتَ** ر ء ي B013: The alerting question creates the demand that the following conduct answer.
  - 107:1 **يُكَذِّبُ** ك ذ ب B004: Failure to carry through a charge lets conduct prove the professed obligation false.
  - 107:1 **بِٱلدِّينِ** د ي ن B003: Debt supplies the protective obligation on which the agent practically defaults.
  - 107:2 **يَدُعُّ** د ع ع B001: Severe pushing makes the denial bodily, directional, and publicly inspectable.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Severance from a caregiver identifies the vulnerable relation that the push further ruptures.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B002: Isolation broadens orphanhood into the social condition intensified by expulsion.

## disallowed claim
- reading: He reenacts that falsification by treating the orphan's claim to kinship-like support as invalid.
- mechanism: The non-dominant mapped branch of the pushing root activates a claim of right or affiliation. Without replacing the direct severe-push sense, it lets the act be read as a counter-verdict: the orphan's claim to belonging and support is treated as false, mirroring the focus subject's falsification of dīn.
- trace:
  - 107:1 **يُكَذِّبُ** ك ذ ب B002: Declaring a person or claim false supplies the juridical shape of rejection.
  - 107:1 **بِٱلدِّينِ** د ي ن B003: Debt makes the rejected affiliation carry a concrete claim to support.
  - 107:2 **يَدُعُّ** د ع ع B001: The dominant branch preserves the literal core of forceful expulsion.
  - 107:2 **يَدُعُّ** د ع ع B002: The split mapped image of asserting right or affiliation overlays the shove with a refused claim to belonging.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Loss of a caregiver makes affiliation and support precisely what is at stake.

## distributed provision
- reading: Denial also appears as refusal to activate a wider provision network capable of stabilizing those in need.
- mechanism: The evidence expands from direct violence to failure of social mobilization. Urging is an action upon other agents; food is provision and livelihood; the miskīn inventory supplies both abasement and the sustenance by which a dwelling remains stable. Denial now disables a civic distribution process, not merely one person's private generosity.
- trace:
  - 107:1 **بِٱلدِّينِ** د ي ن B006: The city as ordered authority supplies a communal system whose obedience is tested by provision.
  - 107:1 **بِٱلدِّينِ** د ي ن B003: Debt makes provision an owed relation rather than discretionary surplus.
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging supplies the missing act of recruiting and pressuring others toward provision.
  - 107:3 **طَعَامِ** ط ع م B002: Feeding another makes the object a transfer to a recipient, not merely food as a substance.
  - 107:3 **طَعَامِ** ط ع م B004: Livelihood and good condition extend feeding into durable maintenance of life.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B006: Abasement locates the recipient in a social condition that provision should answer.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B010: Sustenance that stabilizes residence turns food into infrastructure for remaining securely in place.

## social graft
- reading: The denier blocks a reparative graft by which excluded people could regain stable attachment to the social order.
- mechanism: A cross-material model emerges: orphanhood isolates, low ground spatializes social descent, a food-root branch depicts a branch accepting graft, and dwelling-root stability supplies the result. The missing urging can then be read as refusal to graft the severed or lowered person back into a sustaining social body.
- trace:
  - 107:1 **بِٱلدِّينِ** د ي ن B006: Ordered civic obedience supplies the social body into which repair would reconnect the excluded.
  - 107:1 **يُكَذِّبُ** ك ذ ب B004: A charge failing in execution lets the absence of repair falsify the claimed order.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B002: Isolation supplies the severed condition requiring reconnection.
  - 107:3 **يَحُضُّ** ح ض ض B002: The lowest ground spatializes the vulnerable person's socially depressed position.
  - 107:3 **طَعَامِ** ط ع م B010: A branch accepting graft contributes the repair image of one life being joined into a sustaining stock.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B009: A place of settlement supplies the stable outcome that successful reconnection would enable.

## ritual counterfeit
- reading: The denier-type can inhabit ritual form while a heedless life makes that form a deceptive surface rather than operative obedience.
- mechanism: Obligatory worship supplies a visible pattern of obedience, but heart-level heedlessness and distance from the prayer prevent that pattern from governing conduct. The earlier counterfeit baseline is sharpened: ritual can be present as surface while the life carrying it falsifies dīn.
- trace:
  - 107:1 **أَرَءَيْتَ** ر ء ي B006: Visible appearance and mirroring make outward form an object that can conceal rather than disclose condition.
  - 107:1 **يُكَذِّبُ** ك ذ ب B009: A patterned surface that deceives supplies the model for correct-looking ritual with a contradictory condition.
  - 107:1 **بِٱلدِّينِ** د ي ن B001: Obedience and submission define what the ritual should enact beyond its visible performance.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B003: Specified worship supplies the outwardly valid ritual form under scrutiny.
  - 107:5 **صَلَاتِهِمْ** ص ل و B001: Obligatory worship raises the stakes of being detached from what is performed.
  - 107:5 **سَاهُونَ** س ه و B001: Heedlessness of the heart supplies the internal disconnection beneath the ritual surface.

## failed annealing
- reading: The prayer is a formative process that has failed: repeated exposure leaves conduct unstraightened and inert.
- mechanism: The non-dominant prayer mapping carries fire and the straightening of a thing by heat, while heedlessness can image motionless stasis. As a material analogy, repeated worship should expose the person to a formative heat; if conduct remains inert, the discipline has failed to anneal the moral charge into action.
- trace:
  - 107:1 **يُكَذِّبُ** ك ذ ب B004: A charge proves false when it is not carried through, providing the test for failed transformation.
  - 107:1 **بِٱلدِّينِ** د ي ن B001: Obedience supplies the intended formed condition that ritual discipline should produce.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B001: Encountering fire and heat begins the material analogy of formative exposure.
  - 107:5 **صَلَاتِهِمْ** ص ل و B004: Heating that straightens a thing supplies the inferred transformative function of repeated discipline.
  - 107:5 **سَاهُونَ** س ه و B002: Stillness supplies the contrary result: exposure without moral movement.

## gaze reversal
- reading: أرأيت trains a counter-gaze: recognize the denier by seeing through the pious visibility he deliberately manufactures.
- mechanism: The focus begins by asking the addressee to see with insight; the same root later names action performed so others will see. This reverses the direction of gaze. The denier attempts to manufacture the very evidence by which the opening asks to judge him, so genuine recognition must look through staged visibility to the social effects surrounding it.
- trace:
  - 107:1 **أَرَءَيْتَ** ر ء ي B001: Eye-seeing joined to insight establishes the addressee's diagnostic gaze.
  - 107:1 **أَرَءَيْتَ** ر ء ي B013: The alerting formula recruits the addressee to answer by recognition.
  - 107:1 **يُكَذِّبُ** ك ذ ب B009: A deceptive visible condition explains why the gaze must discriminate rather than merely register display.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: Performing for people to see supplies the denier's attempt to control public perception.
  - 107:6 **يُرَآءُونَ** ر ء ي B012: Causing something to be seen makes visibility an actively produced artifact.
  - 107:6 **يُرَآءُونَ** ر ء ي B006: Appearance and mirroring provide the managed surface placed before observers.

## blocked aid circuit
- reading: Denial is maintained by repeatedly engineering blockages in the ordinary circulation of mutual aid.
- mechanism: Withholding is not a passive absence but a hand checked and a barrier interposed; the mapped object branch supplies aid and mutual backing. The final act therefore exposes denial as negative infrastructure: the subject blocks small circulations of support and defaults on dīn's social debt.
- trace:
  - 107:1 **بِٱلدِّينِ** د ي ن B003: Debt makes assistance a due relation whose nontransfer can count as default.
  - 107:1 **يُكَذِّبُ** ك ذ ب B004: Failure to carry through a charge makes blocked support a practical falsification.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B001: The hand held back from giving turns omission into a controlled bodily act.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: A barrier between a person and what is sought supplies the architecture of blocked circulation.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Aid and mutual backing identify what the barrier prevents from reaching another.

## fortified possession
- reading: The denier uses power and possession as a fortification against the claims of mutual assistance.
- mechanism: A branch of withholding is protective strength that cannot be penetrated. Joined to dīn's possession and subjugation branch, it activates an inversion: power that could protect the vulnerable instead fortifies possessions against claims for assistance. Denial becomes a property regime that safeguards control rather than relation.
- trace:
  - 107:1 **بِٱلدِّينِ** د ي ن B004: Subjugation and possession supply the asymmetry by which control of goods becomes control over people.
  - 107:1 **بِٱلدِّينِ** د ي ن B006: Ordered authority supplies the public alternative in which strength serves a shared civic relation.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B003: Protective power that cannot be reached supplies the image of resources enclosed behind strength.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance identifies the relational use from which fortified resources are diverted.

## narrated reputation
- reading: He authors a performance designed to become a favorable circulating report and thereby obtain social credit.
- mechanism: 
- trace:
  - 107:1 **أَرَءَيْتَ** ر ء ي B003: Relaying reports and poetry lets the opening recognition circulate as an account about a person.
  - 107:1 **يُكَذِّبُ** ك ذ ب B009: A condition that deceives by appearance supplies the possibility of a false public story.
  - 107:1 **بِٱلدِّينِ** د ي ن B007: Crediting a person and leaving him to conscience gives reputation the function of social credit.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: Showing off supplies the public performance from which a favorable report can be manufactured.
  - 107:6 **يُرَآءُونَ** ر ء ي B003: The split report branch at the recurring root keeps the reputation mechanism active at the point of display.

## hidden obligation star
- reading: Denial is an allocation of visibility: spectacular piety is made bright while small binding assistance is rendered faint.
- mechanism: 
- trace:
  - 107:1 **أَرَءَيْتَ** ر ء ي B001: Seeing by eye or insight supplies the task of noticing what public display obscures.
  - 107:1 **بِٱلدِّينِ** د ي ن B003: Debt supplies the small but real obligation that remains due even when attention leaves it.
  - 107:5 **سَاهُونَ** س ه و B005: The faint hidden star images an obligation present in the field yet easy to overlook.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: Ostentation redirects attention toward conspicuous acts selected for observers.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Ordinary assistance supplies the low-visibility obligation eclipsed by the staged display.

## quenching and burden
- reading: At the edge of the split mapping, recognition tests whether a person's social practice carries relief, quenches need, and bears what is owed.
- mechanism: 
- trace:
  - 107:1 **أَرَءَيْتَ** ر ء ي B001: Quenching and release from thirst supply the material outcome of need being genuinely answered.
  - 107:1 **أَرَءَيْتَ** ر ء ي B002: Bringing and carrying water contributes the labor required to move relief toward another.
  - 107:1 **أَرَءَيْتَ** ر ء ي B015: Chiefs who bear communal burdens scale carrying from a vessel to social responsibility.
  - 107:1 **بِٱلدِّينِ** د ي ن B003: Debt anchors burden-bearing as something due rather than merely admirable.
  - 107:3 **طَعَامِ** ط ع م B004: Livelihood and sound condition extend quenching into sustained material provision.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Aid and backing connect the burden image to the passage's final withheld relation.


# Focus 107:2

## forceful resevering
- reading: He actively re-enacts orphaning: force is used to drive an already unprotected dependent farther from access, belonging, and protection.
- mechanism: Forceful driving meets a person already defined by severance from a protector. The act therefore does more than fail to repair vulnerability: it actively repeats and intensifies the orphan's constitutive separation.
- trace:
  - 107:2 **يَدُعُّ** د ع ع B001: Supplies rough, forceful thrusting and makes the predicate an enacted expulsion rather than passive neglect.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Supplies a child cut off from parental protection, so the thrust compounds an already broken protective relation.

## summons reversed
- reading: The shove is the inverse of hospitality and summons: the isolated person who should be drawn into relation is deliberately driven out of it.
- mechanism: The opposed branch directions create a relational reversal. A person who most needs to be called into proximity is instead propelled outward; exclusion becomes the corruption of an available summons.
- trace:
  - 107:2 **يَدُعُّ** د ع ع B001: Contributes outward force and supplies the expelling pole of the reversal.
  - 107:2 **يَدُعُّ** د ع ع B001: Contributes calling that draws near and supplies the unrealized relational alternative to expulsion.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B002: Contributes solitary disconnection, making nearness versus further isolation the mechanism's decisive axis.

## herding the singular
- reading: The orphan is coercively managed and de-personed: singular vulnerability is treated as a troublesome dependent category to be driven along.
- mechanism: The act can be carried as social reduction: a singular person is handled as a steerable unit, moved by rebuke rather than addressed as a claimant or relation. The reading coexists with literal bodily force but shifts attention to dehumanizing command.
- trace:
  - 107:2 **يَدُعُّ** د ع ع B003: Supplies the chiding call used to drive a herd and frames the action as coercive management by voice.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B002: Supplies isolated singularity, highlighting the violence of reducing an irreducible person to movable stock.
  - 107:2 **يَدُعُّ** د ع ع B009: Supplies small dependents as a branch image and keeps the coercive management attached to the focus object's dependency.

## evidentiary ledger
- reading: The cruel act is a public fingerprint of an otherwise hidden denial: the orphan's treatment becomes the place where the actor's real account is made visible.
- mechanism: The preceding summons to attend, attribution of falsification, and account/recompense convert the focus action into visible evidence. Treatment of the least protected person functions as the bodily ledger in which a hidden rejection becomes inspectable.
- trace:
  - 107:2 **يَدُعُّ** د ع ع B001: Supplies the observable forceful act that can bear evidentiary weight.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Supplies the unprotected test case whose treatment exposes the actor's operative commitments.
  - 107:1 **أَرَءَيْتَ** ر ء ي B013: Supplies attention-directing inquiry and turns the next action into the requested object of recognition.
  - 107:1 **يُكَذِّبُ** ك ذ ب B002: Supplies active attribution of falsity and frames rejection as a stance manifested through conduct.
  - 107:1 **بِٱلدِّينِ** د ي ن B002: Supplies accounting and recompense, allowing the social act to register as an entry in a moral ledger.

## claim foreclosure
- reading: The actor first makes the orphan's claim socially unreal, then makes the claimant physically absent; the shove is enforcement of denied standing.
- mechanism: The focus split root supplies the assertion of a right or affiliation; the context supplies discrediting and debt. Physical expulsion can therefore enforce a prior discursive move: mark the vulnerable claimant false so that kinship, property, or care obligations never enter the account.
- trace:
  - 107:2 **يَدُعُّ** د ع ع B002: Supplies claiming a right or affiliation and makes the focus object legible as a bearer of a denied claim.
  - 107:2 **يَدُعُّ** د ع ع B001: Supplies the force that physically executes exclusion after the claim is refused.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Supplies loss of the normal protector who could validate or enforce the claim.
  - 107:1 **يُكَذِّبُ** ك ذ ب B002: Supplies the act of imputing falsehood and functions as the discursive foreclosure of the claim.
  - 107:1 **بِٱلدِّينِ** د ي ن B003: Supplies financial indebtedness and renders care or property as an obligation the actor refuses to recognize.

## asymmetric social force
- reading: The actor is highly active, but only in the wrong direction: force expels need, while no force is spent mobilizing nourishment toward it.
- mechanism: The sequence contrasts abundant coercive energy toward the orphan with absent motivating energy toward feeding the poor. This is not simple apathy: social force is selectively vectored, pushing vulnerability away while refusing to move others or resources toward relief.
- trace:
  - 107:2 **يَدُعُّ** د ع ع B001: Supplies strong outward propulsion and establishes that the actor is capable of forceful initiative.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Supplies the first unprotected recipient toward whom force is directed.
  - 107:3 **يَحُضُّ** ح ض ض B001: Supplies vigorous urging and, under negation, marks the missing counter-force that could mobilize care.
  - 107:3 **طَعَامِ** ط ع م B002: Supplies feeding another and gives the withheld social motion a concrete destination.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B006: Supplies abject need and links the second vulnerable person to the orphan's exposure.

## motion produces stasis
- reading: The shove removes the conditions of stable agency: outward displacement and delayed provision make the vulnerable person less able to move, dwell, or recover.
- mechanism: The focus applies violent motion to a person whose care is already delayed; the context couples livelihood with loss of motion and sustenance that stabilizes a dwelling. The paradoxical result is that imposed movement produces social immobility by removing access to what lets a person remain and recover.
- trace:
  - 107:2 **يَدُعُّ** د ع ع B001: Supplies imposed bodily or social motion and initiates the displacement mechanism.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B004: Supplies delayed care and makes deprivation temporal as well as relational.
  - 107:3 **طَعَامِ** ط ع م B004: Supplies livelihood and well-being as the resource base removed by exclusion.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B001: Supplies cessation of motion and names the disabling endpoint of resource deprivation.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B010: Supplies sustenance that fixes residence and clarifies what would permit stable belonging.

## mercy ritual inversion
- reading: The expulsion is the embodied falsification of ritual mercy: the mouth calls blessing near while the body drives its possible recipient away.
- mechanism: Prayer branches supply supplication, blessing, and mercy, while heedlessness supplies failure of inward attention. Against them, the focus verb's split call-near branch and literal thrust expose a reversal: ritual speech draws mercy near in form while embodied conduct drives its human addressee away.
- trace:
  - 107:2 **يَدُعُّ** د ع ع B001: Supplies a call that draws near and creates the relational action ritual mercy would be expected to perform.
  - 107:2 **يَدُعُّ** د ع ع B001: Supplies the contrary bodily action, turning invocation into expulsion.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Supplies the unprotected human recipient through whom claimed mercy can be tested.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B002: Supplies prayer as supplication, praise, and mercy and establishes the ritual pole of the contradiction.
  - 107:5 **صَلَاتِهِمْ** ص ل و B002: Supplies blessing and mercy from the non-dominant mapped root, reinforcing relational beneficence rather than mere ceremony.
  - 107:5 **سَاهُونَ** س ه و B001: Supplies inward heedlessness and explains how ritual language can fail to redirect embodied conduct.

## visibility choreography
- reading: The actor curates visibility: need is pushed out of frame so that a polished religious self can occupy the frame uncontested.
- mechanism: The opening directs sight toward the actor, and the later occurrence supplies ostentatious visibility. Forceful displacement of an isolated person can then be read as scene management: remove need from the field while placing the pious self inside it.
- trace:
  - 107:2 **يَدُعُّ** د ع ع B001: Supplies the physical force capable of editing who remains present in the social scene.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B002: Supplies isolated singularity and makes the removed person easy to erase from collective view.
  - 107:1 **أَرَءَيْتَ** ر ء ي B013: Supplies an attention-directing frame that asks the reader to watch how identity is disclosed.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: Supplies ostentatious display and makes controlled visibility a motive-bearing social mechanism.
  - 107:6 **يُرَآءُونَ** ر ء ي B012: Supplies making something visible and frames the actor's self-presentation as selective revelation.

## aid boundary system
- reading: The shove is the bodily edge of an aid-denial system: exclusion is reproduced through space, gesture, and control of ordinary assistance.
- mechanism: The final roots supply a withheld hand, a barrier, and assistance. They generalize the focus shove from an episode into boundary infrastructure: body, hand, and resource all enforce the same rule that aid must not cross toward the dependent.
- trace:
  - 107:2 **يَدُعُّ** د ع ع B001: Supplies the bodily push as the first enacted boundary against access.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Supplies the dependent already lacking a protector and therefore most exposed to an access barrier.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B001: Supplies the hand deliberately held back from giving and extends bodily rejection into resource withholding.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: Supplies a barrier between a person and what is sought, making exclusion a durable arrangement.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Supplies assistance and names precisely what the barrier prevents from reaching the vulnerable person.

## protection inverted
- reading: The orphan is orphaned again by a social protector in reverse: available strength fortifies resources against the child instead of sheltering the child.
- mechanism: The orphan branch names lost protection, while the prevention branch includes strength that protects against penetration. The actor has protective capacity but turns it around: strength guards possessions and boundaries from the orphan instead of guarding the orphan from exposure.
- trace:
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Supplies the absence of a protecting parent and establishes protection as the focus object's missing relation.
  - 107:2 **يَدُعُّ** د ع ع B001: Supplies force that can either defend or expel and here is directed against the unprotected person.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B003: Supplies protective strength that cannot be penetrated and reveals the actor's capacity to construct safety.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Supplies assistance and marks the alternative object toward which protective strength could have been directed.

## stumbler recovery reversed
- reading: The line stages anti-rescue: the verbal space that could tell the unsupported person to rise is converted into the force that makes rising harder.
- mechanism: 
- trace:
  - 107:2 **يَدُعُّ** د ع ع B004: Supplies a restorative cry to a stumbler and creates the help-to-rise pole of the reversal.
  - 107:2 **يَدُعُّ** د ع ع B001: Supplies actual rough thrusting and turns potential restoration into renewed downfall.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Supplies missing support and makes the failure to raise the fallen relationally exact.

## refused social graft
- reading: The orphan is treated as a graft the social stock refuses to receive; expulsion preserves isolation by blocking nourishing union.
- mechanism: 
- trace:
  - 107:2 **يَدُعُّ** د ع ع B001: Supplies the rejecting force that prevents incorporation.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B002: Supplies isolated singleness and defines the social condition that a successful joining would change.
  - 107:3 **طَعَامِ** ط ع م B010: Supplies a branch accepting a graft and models nourishment as successful union with a sustaining body.

## reputational editing
- reading: The actor removes the counter-story: visible need is expelled so a handsome public account of the self can circulate without contradiction.
- mechanism: 
- trace:
  - 107:2 **يَدُعُّ** د ع ع B001: Supplies forceful removal and gives reputational editing a concrete spatial operation.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B002: Supplies isolated singularity and makes the vulnerable person an easily omitted counter-image.
  - 107:6 **يُرَآءُونَ** ر ء ي B003: Supplies transmission of a report and activates control over the story others receive.
  - 107:6 **يُرَآءُونَ** ر ء ي B009: Supplies attractive outward appearance and gives the edited report a polished visual aim.

## packed container enclosure
- reading: Person-removal and resource-retention form one packing logic: social space is compressed around possession, and delayed care is what gets shaken out.
- mechanism: 
- trace:
  - 107:2 **يَدُعُّ** د ع ع B002: Supplies shaking a container until it packs full and models accumulation through rearrangement and pressure.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B004: Supplies delayed care and identifies who is displaced when accumulation takes priority.
  - 107:3 **طَعَامِ** ط ع م B004: Supplies livelihood and well-being as the material contents around which enclosure operates.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: Supplies the barrier that keeps packed resources from crossing toward a claimant.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Supplies assistance as the excluded flow that would otherwise open the container outward.


# Focus 107:3

## social exhortation circuit
- reading: The verse also faults refusal to activate a wider provisioning network on behalf of someone whose weakness limits self-advocacy.
- mechanism: The failure occurs upstream of a meal: the actor refuses to use interpersonal pressure to recruit other people into a directed transfer of nourishment. The focus therefore diagnoses a broken social activation circuit, not merely an unopened private hand.
- trace:
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging supplies the interpersonal speech-force that should mobilize action toward a concrete end.
  - 107:3 **طَعَامِ** ط ع م B002: Giving food or answering a request supplies the directed transfer that the mobilizing speech is meant to produce.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B006: Poverty, weakness, and abasement specify the vulnerable condition at the receiving end of the failed circuit.

## provision as stability
- reading: Food is also livelihood infrastructure whose circulation allows a vulnerable person to remain housed, settled, and socially present.
- mechanism: Provision can be livelihood rather than a single edible object, while the recipient root can describe both dwelling and the supplies that permit continued residence. Exhorting toward food can thus mean mobilizing the material conditions that prevent displacement and make stable life possible.
- trace:
  - 107:3 **طَعَامِ** ط ع م B004: Provision, livelihood, earnings, and a lawful share widen food into an enduring material basis of life.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B010: Supplies that let one remain in place make nourishment function as the condition of durable staying.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B002: Dwelling and lodging provide the stable social endpoint that adequate provision can preserve.

## reintegrative graft
- reading: Provision can be the bond by which an excluded recipient is grafted back into a sustaining household or community.
- mechanism: A form-distant food branch imagines successful grafting as accepting an insertion, while the recipient root can name household inhabitants. On this activation, material provision is a joining medium: exhortation recruits the social body to receive someone at risk of exclusion into its sustaining circulation.
- trace:
  - 107:3 **طَعَامِ** ط ع م B010: A graft that accepts an inserted branch supplies the material image of successful social attachment.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B003: Household inhabitants supply the collective body into which the vulnerable person could be received.
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging functions as recruitment of that household or community into the act of attachment.

## restored motion capacity
- reading: The omitted mobilization leaves a person socially motionless by withholding the provision through which practical agency could return.
- mechanism: Need is read kinetically as constrained movement or agency. Provision restores capacity, and exhortation is the initiating impulse that should set both resources and the recipient's possibilities in motion; refusing it helps preserve immobilization.
- trace:
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B001: Cessation of motion supplies the recipient's constrained or stalled condition.
  - 107:3 **طَعَامِ** ط ع م B011: Ability or capacity makes nourishment a means of restored agency rather than mere caloric intake.
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging supplies the initiating impulse that should move people and resources toward restoring capacity.

## visible counterproof
- reading: The focus supplies observable counter-evidence: failure to mobilize food reveals what an abstract denial looks like when enacted.
- mechanism: The opening demand for attention, attribution of falsity, and accounting frame turn the focus behavior into inspectable evidence. Refusal to recruit nourishment is not only a breach inside a moral system; it is the concrete counter-performance by which denial of that system becomes visible.
- trace:
  - 107:3 **يَحُضُّ** ح ض ض B001: The absent act of urging supplies the observable social behavior under inspection.
  - 107:3 **طَعَامِ** ط ع م B002: Feeding another supplies the concrete outcome against which the actor's claim is behaviorally tested.
  - 107:1 **أَرَءَيْتَ** ر ء ي B013: Attention and inquiry direct the reader to treat subsequent conduct as diagnostic evidence.
  - 107:1 **يُكَذِّبُ** ك ذ ب B002: Attributing falsity supplies the contradiction that the actor's treatment of provision makes concrete.
  - 107:1 **بِٱلدِّينِ** د ي ن B002: Accounting and recompense supply the moral order whose denial is exposed through social conduct.

## liability ledger
- reading: Urging food can be advocacy for payment of an outstanding social claim whose nonrecognition is itself part of denial.
- mechanism: The financial-debt and accounting branches recode provision as a claim that can be owed and reckoned. Urging is then the social act of acknowledging and recruiting discharge of a vulnerable person's outstanding material claim, not an appeal to optional generosity.
- trace:
  - 107:3 **طَعَامِ** ط ع م B004: Livelihood, revenue, and lawful share make the provision capable of being read as an allocated material entitlement.
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging becomes collective recognition and enforcement of that material claim.
  - 107:1 **بِٱلدِّينِ** د ي ن B003: Financial debt supplies the creditor-debtor structure for construing unmet need as liability.
  - 107:1 **بِٱلدِّينِ** د ي ن B002: Accounting and recompense supply the ledger in which refusal to provision remains answerable.

## broken provision continuity
- reading: The social mechanism that would keep nourishment circulating is allowed to stall, making provision episodic and incapable of stabilizing life.
- mechanism: Two distant falsity branches picture a resource that vanishes instead of lasting and motion that begins then stops. Coupled to livelihood and supplies that permit staying, they activate a process reading: the vice is failure to make provision continuous and self-renewing, so relief repeatedly starts and collapses.
- trace:
  - 107:1 **يُكَذِّبُ** ك ذ ب B006: A milk supply that disappears and does not last supplies the image of unreliable nourishment.
  - 107:1 **يُكَذِّبُ** ك ذ ب B007: Running followed by stopping supplies the temporal pattern of an aid process that fails to continue.
  - 107:3 **طَعَامِ** ط ع م B004: Livelihood makes persistence, rather than one isolated meal, the relevant provisioning scale.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B010: Supplies that enable staying define the stabilizing result that interrupted provision cannot achieve.

## force direction reversal
- reading: The actor possesses force but allocates it asymmetrically: coercion travels toward vulnerability while mobilizing speech and resources do not.
- mechanism: The adjacent actions form a directional reversal. The actor is not inert or short of force: force is discharged physically against a person cut off from support, while verbal and social force is withheld from moving provision toward vulnerability. A non-dominant split branch keeps a latent calling channel beside the dominant shove, making the missing call to care especially sharp.
- trace:
  - 107:2 **يَدُعُّ** د ع ع B001: A severe push supplies active force directed away from the vulnerable person.
  - 107:2 **يَدُعُّ** د ع ع B001: The split mapping's verbal call and inclination supply a latent speech channel that could instead have drawn others toward care.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Severance from a caregiver identifies the prior loss of support that makes the direction of force consequential.
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging supplies the prosocial force that should move other agents toward provision but is negated.
  - 107:3 **طَعَامِ** ط ع م B002: Feeding another fixes the missing force's intended direction and material endpoint.

## repair severed support
- reading: Provision is a means of repairing a broken support relation by reattaching the vulnerable person to a sustaining social body.
- mechanism: The orphan branch supplies severance from a sustaining caregiver, while the food branch supplies a graft that can accept an insertion and the recipient root supplies a household. Provision becomes reparative attachment: the community should receive a severed person into a new support line, but pushing and non-urging jointly prevent that repair.
- trace:
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Loss of a caregiver supplies the severed support relation that requires replacement or repair.
  - 107:2 **يَدُعُّ** د ع ع B001: The severe shove functions as failed reception, increasing rather than repairing separation.
  - 107:3 **طَعَامِ** ط ع م B010: Successful grafting supplies a model for attaching a disconnected life to a new sustaining line.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B003: The household supplies the social organism capable of receiving and sustaining that attachment.
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging recruits the receiving community into the work of reparative attachment.

## ritual to material translation
- reading: Failure to urge feeding is the missing conversion point where ritual speech should have become coordinated material mercy.
- mechanism: The prayer inventories supply specialized worship, mercy-bearing speech, and binding practice. Set beside negated exhortation, they expose a failed transducer: devotional utterance and disciplined form do not become speech that coordinates nourishment. The focus is the missing social output of ritual language.
- trace:
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging supplies the outward, other-moving speech act into which devotional speech would have to translate.
  - 107:3 **طَعَامِ** ط ع م B002: Feeding another supplies the material output by which that translation becomes effective.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B003: Specialized worship supplies the formal ritual input whose social consequence is being tested.
  - 107:5 **صَلَاتِهِمْ** ص ل و B002: Prayer, praise, and mercy supply a speech field that should be capable of generating merciful coordination.
  - 107:5 **صَلَاتِهِمْ** ص ل و B001: The non-dominant mapped branch's binding worship image adds regular obligation rather than a fleeting devotional mood.

## stillness feedback loop
- reading: The missing recommendation is the absent impulse in a kinetic system: heedless stillness upstream perpetuates constrained agency downstream.
- mechanism: A context branch equates heedlessness with stillness, resonating with the focus recipient root's cessation of motion. This yields a feedback loop: inward ritual stillness fails to launch exhortation, resources remain still, and the vulnerable person's practical capacity remains stalled.
- trace:
  - 107:5 **سَاهُونَ** س ه و B002: Heedlessness as stillness supplies the unmoving source state from which no social impulse departs.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B001: Cessation of motion supplies the vulnerable person's stalled endpoint and creates a cross-root stillness echo.
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging is the missing kinetic impulse that could move people and provision out of that stillness.
  - 107:3 **طَعَامِ** ط ع م B011: Capacity defines the agency that moving provision could restore at the receiving end.

## exhortation under anti spectacle constraint
- reading: The remedy is recipient-centered mobilization that can be public without turning advocacy or the vulnerable person into a prop.
- mechanism: The focus demands an outward social speech act, but the later visibility branches warn that outwardness can be converted into display for an audience. Genuine exhortation is therefore neither silence nor spectacle: it mobilizes people toward the recipient's nourishment, with transfer rather than visibility as its controlling end.
- trace:
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging requires socially outward speech and therefore creates the possibility of both real mobilization and public performance.
  - 107:3 **طَعَامِ** ط ع م B002: Actual feeding supplies the recipient-centered outcome that distinguishes effective advocacy from display.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: Showing oneself to people supplies the corrupt audience-oriented mode that can mimic outward moral action.
  - 107:6 **يُرَآءُونَ** ر ء ي B012: Causing something to appear supplies the mechanism by which an act can optimize its image instead of its material result.

## mutual aid recruitment layer
- reading: The actor closes the aid ecology at both ends, suppressing the social signal that would recruit provision and the cooperative transfer that would deliver it.
- mechanism: The final context supplies a withheld hand, an access barrier, and assistance. These clarify two layers of one aid system: exhortation is upstream recruitment and norm formation; assistance and provision are downstream flow. The actor suppresses both the signal that would enlist others and the aid that would cross the barrier.
- trace:
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging supplies the upstream recruitment signal by which a community is enlisted into aid.
  - 107:3 **طَعَامِ** ط ع م B004: Livelihood and allocated provision supply the resource stream the recruited network should move.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B001: A hand held back from giving supplies the downstream closure of actual transfer.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: A barrier between a person and what is sought supplies the access obstruction produced by that closure.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance and mutual backing supply the cooperative infrastructure being withheld.

## engineered low ground
- reading: The sequence can picture poverty as engineered low ground: coercion presses vulnerability downward, and absent mobilization lets that assigned position harden.
- mechanism: 
- trace:
  - 107:3 **يَحُضُّ** ح ض ض B002: Low ground at a mountain's foot supplies a vertical social position beneath those with mobility and resources.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B009: A settled position supplies the risk that the vulnerable person's low placement becomes fixed.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B006: Poverty and abasement give the vertical image a social rather than merely topographic referent.
  - 107:2 **يَدُعُّ** د ع ع B001: The severe push supplies the force by which vulnerability is driven into or kept in that lower position.

## bitter communal medicine
- reading: Exhortation can be carried as bitter communal medicine: refusing to voice it leaves a social body accustomed to need untreated.
- mechanism: 
- trace:
  - 107:3 **يَحُضُّ** ح ض ض B003: The bitter medicinal substance supplies a corrective that is unpleasant yet potentially curative.
  - 107:3 **طَعَامِ** ط ع م B001: Tasting and taking nourishment in supply the ingestion pathway by which the corrective could enter communal practice.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B006: Need and abasement identify the social illness whose normalization requires correction.

## deprivation at the throat
- reading: The combined branches let deprivation register as applied pressure: social barriers tighten around the very channel through which sustaining intake should pass.
- mechanism: 
- trace:
  - 107:3 **طَعَامِ** ط ع م B012: Gripping and squeezing the throat turns denial of nourishment into pressure at the channel of intake.
  - 107:2 **يَدُعُّ** د ع ع B001: The preceding severe push supplies a second bodily force against vulnerability.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: An access barrier generalizes the bodily blockage into a social obstruction between need and its object.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B006: Weakness and abasement identify who bears the compounded pressure.

## faint recipient attention
- reading: The actor leaves need below the threshold of collective notice while attention is available for amplifying the self.
- mechanism: 
- trace:
  - 107:5 **سَاهُونَ** س ه و B005: A faint celestial point supplies the image of a real but easily overlooked signal.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: Self-display before people supplies the competing signal that captures and amplifies public attention.
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging would function as attention redirection, making overlooked need socially salient enough to mobilize response.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B006: Weakness and abasement anchor the faint signal in the actual condition of the focus recipient.


# Focus 107:4

## prescribed insider warning
- reading: An insider warning: people can bear the agentive identity of prayer and still stand under the threat, so performance is evidence to examine rather than immunity.
- mechanism: The focus does not attack an abstract rite from outside; it places liability inside the class named by performing a binding, embodied practice. Ritual membership therefore cannot itself close the moral question.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B003: The prescribed-rite sense fixes the agent noun to embodied, rule-governed worship and makes the threat an insider address.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B001: The non-dominant mapped branch reinforces prayer as an obligation borne by the named practitioners rather than a loose devotional mood.

## mercy vector reversed
- reading: The praying ones are also potential conduits of blessing; woe marks the possibility that the conduit has been occupied but functionally reversed or blocked.
- mechanism: Prayer can be modeled as an outward relational vector rather than a self-contained possession. The collision of that vector with woe creates a reversal: a practitioner may occupy the form while blocking what should pass through it.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B002: The branch supplies prayer as benefit directed toward another, making outward transmission a live function of the practitioner label.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B002: The split-root counterpart keeps blessing and mercy active beside formal worship, supporting a relational rather than merely procedural baseline.

## heat encounter
- reading: The focus also admits a threshold reading: these practitioners repeatedly approach a transforming heat, and the threat lies in an encounter that does not transform.
- mechanism: The split root lets the practitioner label carry a thermal shadow. Woe is no longer only a sentence imposed after worship; it can disclose that prayer is an exposure meant to affect the one who enters it, with danger concentrated in remaining unchanged at the threshold.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B001: The dominant mapped branch contributes proximity to consuming or testing heat as a material shadow of entering prayer.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B003: The non-dominant mapped branch makes undergoing heat explicit and turns the worshipper label into a possible exposure-state.

## second runner
- reading: The named group can also be heard as followers in formation; the focus leaves open whether they carry a worthy course onward or merely trail its visible form.
- mechanism: The plural can carry a formation-image: practitioners as second runners positioned by another's course. That does not replace the prayer sense, but it raises a live question about derivative alignment, imitation, and whether following transmits the leader's motion or only preserves rank.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B006: The race image supplies a practitioner who is defined by close pursuit of a predecessor, activating ordered following within the plural.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B007: The split-root counterpart confirms the near-behind position and makes borrowed trajectory a stable exploratory mechanism.

## visibility loop
- reading: It warns practitioners who have rewired prayer into a seeing-and-being-seen technology, using a sacred form to manufacture an audience-facing self.
- mechanism: The context brackets the focus with a summons to notice and an act of making oneself noticed. The praying agent is thereby relocated inside a visibility circuit: an observer is recruited, then the practitioner recruits observers, turning prayer from relation into display.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B003: The formal rite supplies the visible, repeatable action that can become the object carried through the seeing circuit.
  - 107:1 **أَرَءَيْتَ** ر ء ي B013: The opening attention-question installs the reader as witness and makes observation an active operation rather than background scenery.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: The later branch supplies conduct calibrated for human eyes, reversing the opening act of seeing into solicitation of being seen.

## lying vestment
- reading: The noun may classify the outer form while simultaneously exposing it as a false social vestment: authentic motion can carry an inauthentic report.
- mechanism: A branch in the denial root pictures clothing whose appearance misreports its condition. That material analogy activates the prayer agent noun as identity-clothing: a true ritual form can still give a false report about the person wearing it.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B003: The recognized rite provides a socially legible form capable of serving as an identity surface.
  - 107:1 **يُكَذِّبُ** ك ذ ب B009: The deceptive-garment image contributes a surface that makes a false claim through its condition, modeling ritual identity as misreport.

## account not credit
- reading: Prayer enters one account with the practitioner's other obligations; performed ritual cannot settle a balance that the same person keeps producing elsewhere.
- mechanism: The account, recompense, and debt branches turn the threat into a ledger event. Prayer is not a detachable credit that cancels other liabilities; the practitioner is precisely the one whose claimed worship is entered into an unresolved account.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B001: Binding worship supplies an obligation whose performance might be mistakenly treated as sufficient credit.
  - 107:1 **بِٱلدِّينِ** د ي ن B002: The reckoning branch supplies evaluation and consequence, making the focus threat an audit of the practitioner claim.
  - 107:1 **بِٱلدِّينِ** د ي ن B003: The financial-liability branch contributes an unpaid-balance model in which ritual performance cannot erase obligations elsewhere.

## split body expulsion
- reading: The threat exposes a body divided against its own worship: ritually disciplined in one space, violently extending another person's abandonment in the next.
- mechanism: The context puts severe bodily expulsion beside the person already cut off from a protector. This revises defective prayer into a split-body mechanism: the body can execute prescribed devotional positions while using its force to deepen another's severance.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B003: The prescribed rite supplies disciplined bodily motion whose ethical continuity is put under pressure.
  - 107:2 **يَدُعُّ** د ع ع B001: The forceful-expulsion branch supplies the contrary bodily vector: movement used to drive a vulnerable person away.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: The severance-from-protection branch identifies what the expelling motion aggravates, turning bodily contradiction into a causal harm.

## mercy must circulate
- reading: Their prayer has failed as an activation system: it does not propagate mercy into persuasion, provision, and the stabilization of vulnerable life.
- mechanism: Prayer's outward blessing branch is given a material transmission path: urge others, move food, stabilize the person whose means of remaining are weak. The failure is therefore not only refusal to give; it is refusal to activate a care network.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B002: Prayer as benefit directed toward others supplies the relational current that the context can materialize or interrupt.
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging supplies activation of additional agents, expanding care from a private gift into coordinated circulation.
  - 107:3 **طَعَامِ** ط ع م B002: The feeding branch gives the circulating benefit a concrete transfer and recipient-facing direction.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B010: Sustenance that lets a person remain supplies the downstream effect: nourishment becomes social stability rather than a momentary token.

## ritual motion social stasis
- reading: The line can expose liturgical motion that produces no mobilization: the body cycles through worship while attention and the surrounding field of care remain still.
- mechanism: Two context branches converge on stillness while the focus branch entails bodily motion. This creates a kinetic paradox: repeated ritual movement can coexist with arrested attention and can leave another person's social immobility untouched.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B003: The embodied rite supplies patterned movement and makes immobility an effect to compare rather than a literal description of prayer.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B001: Cessation of movement supplies the vulnerable person's arrested social condition as the external result left unchanged.
  - 107:5 **سَاهُونَ** س ه و B002: The stillness branch supplies arrested attention within the practitioner, linking inward non-response to outward non-mobilization.

## owned prayer estrangement
- reading: It concerns estranged ownership: prayer is theirs as schedule, label, and possession while they remain away from the claims that would make it present.
- mechanism: The agent noun is immediately unpacked by people who grammatically possess 'their prayer' while standing in a distancing relation to it. Heedlessness turns possession without presence into the central defect: the rite belongs to their identity, but its demand does not hold their attention.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B003: The focus branch establishes the public practitioner category that the next verse internally qualifies.
  - 107:5 **صَلَاتِهِمْ** ص ل و B001: The repeated prayer root presents the rite as binding and possessed, sharpening the contradiction of being oriented away from it.
  - 107:5 **سَاهُونَ** س ه و B001: The heedless-heart branch supplies the missing presence that separates nominal ownership from responsive practice.

## heat encounter unstraightened
- reading: It can also portray prayer itself as a repeated straightening exposure whose heat reaches the practitioner without altering the social shape.
- mechanism: A split-root branch models heat as a means of straightening material. Repeated prayer plus heedlessness revises the baseline thermal shadow: these practitioners enter the heating process, but inattention interrupts transfer, so neither posture nor conduct is reshaped.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B004: The material branch supplies heating and turning as a process that can straighten what is exposed to it.
  - 107:5 **صَلَاتِهِمْ** ص ل و B004: Repetition of the same root after the focus makes the transformative process recurrent rather than a one-time threshold.
  - 107:5 **سَاهُونَ** س ه و B001: Heart-level inattention supplies the insulation that lets repeated exposure occur without responsive change.

## closed hand blocks aid
- reading: Their inattention has an outward valve: prayer does not cross the hand into assistance, and the practitioner becomes the point at which benefit is deliberately stopped.
- mechanism: The final clause places restraint of giving directly against an object mapped to assistance. This completes the blocked-mercy model: a body can enact prayer while functioning as a gate that stops help at the hand.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B002: The outward-benefit branch of prayer supplies what should cross from practitioner toward another.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B001: The restrained-hand branch locates blockage at the concrete point where giving would leave the practitioner.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: The mapped assistance branch identifies the stopped object by function: help that should reinforce another.

## prestige snare resource gate
- reading: The prayer-form may be actively productive in reverse: it captures prestige for the practitioner while operating as a gate against assistance to others.
- mechanism: The focus root's trap branch combines with display, barrier, and aid to produce an institutional reading. Ritual form can capture prestige from observers while simultaneously controlling the passage of useful help; what looks empty is operationally effective at concentrating reputation and blocking resources.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B004: The set-catching device supplies a focus-root image of ritual form arranged to capture something rather than transmit mercy.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: People-facing display identifies reputation and attention as what the ritual arrangement can capture.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: The intervening-barrier branch supplies the complementary operation of preventing desired goods from passing through.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance supplies the resource whose blocked circulation makes the reputational trap socially consequential.

## pounding without nourishing
- reading: As a contained material analogy, the rite becomes pounding without preparation: pressure is repeatedly enacted, yet it bears on the vulnerable instead of processing provision toward them.
- mechanism: 
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B008: The processing slab supplies repetitive pressure as an odd material shadow of patterned ritual action.
  - 107:2 **يَدُعُّ** د ع ع B001: Severe pushing converts pressure from neutral processing into force directed against a vulnerable body.
  - 107:3 **طَعَامِ** ط ع م B002: Feeding supplies the absent productive output: material pressure should prepare provision for another rather than merely bear down.

## follower broken relay
- reading: They may be failed relay-runners: close behind the visible religious course, yet unwilling to recruit the next helper or pass assistance onward.
- mechanism: 
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B006: The second-runner branch supplies close following and the expectation that motion continues through a sequence.
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging another supplies the missing handoff by which one person's concern should recruit the next agent.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance supplies what the relay is meant to carry onward rather than merely preserving ceremonial position.

## grazing on prayer prestige
- reading: In an explicitly speculative ecological resonance, the group can graze on the nourishment and prestige of prayer while failing to move sustaining food toward the person whose life is made precarious.
- mechanism: 
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B009: The grazed plant supplies an ecological image of consuming nourishment attached to the focus root.
  - 107:3 **طَعَامِ** ط ع م B002: Feeding another supplies the human transfer against which consumption of ritual benefit can be reversed.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B010: Provision that sustains remaining supplies the life-preserving destination absent from the practitioner's consumption.


# Focus 107:5

## ritual displacement
- reading: Their characteristic relation is to be turned away from the prescribed prayer itself, whether or not they continue its visible form.
- mechanism: Prescribed worship is the object from which the heart repeatedly departs. The line therefore profiles a settled orientation away from prayer even when its external motions may still occur.
- trace:
  - 107:5 **صَلَاتِهِمْ** ص ل و B003: Prescribed worship supplies the concrete instituted practice from which the construction marks displacement.
  - 107:5 **سَاهُونَ** س ه و B001: The heart's turning away supplies the inward motion that makes ʿan a sustained departure rather than a momentary mistake.

## relational mercy lost
- reading: The defect may also be that their prayer no longer carries supplication, praise, or mercy toward another.
- mechanism: Prayer has an outward relational vector: it asks, blesses, praises, and carries mercy. Heedlessness from it can therefore mean loss of that relational vector, not only deficient concentration during ritual.
- trace:
  - 107:5 **صَلَاتِهِمْ** ص ل و B002: Supplication, praise, and mercy make prayer a relation that should extend beyond the worshipper.
  - 107:5 **سَاهُونَ** س ه و B001: Heedlessness of the heart supplies the severing of attention from that merciful relation.

## inert binding form
- reading: Here stillness can be pathological: a binding form remains while awareness and response have stopped moving.
- mechanism: A binding form can remain in place while its responsive movement has gone still. The reading distinguishes ritual stability from living attentiveness: fixed form is not itself faithful orientation.
- trace:
  - 107:5 **صَلَاتِهِمْ** ص ل و B001: Binding ritual worship supplies the maintained form whose claim remains upon the practitioners.
  - 107:5 **سَاهُونَ** س ه و B002: Stillness supplies an arrested inner response, turning stable ritual form into inert practice.

## hidden signal
- reading: Prayer remains available as an orienting signal, but they have made it functionally too faint to govern attention.
- mechanism: Prayer can function as a faint orienting signal that is genuinely present yet allowed to become too small in the field of attention. The problem is not total absence but trained non-noticing.
- trace:
  - 107:5 **صَلَاتِهِمْ** ص ل و B003: Prescribed worship supplies the real but neglected orienting object.
  - 107:5 **سَاهُونَ** س ه و B005: The barely visible star supplies a model of something present in the visual field yet habitually overlooked.

## visible form accounted falsehood
- reading: Their visible prayer can become a behavioral falsehood under account: it signifies nearness while their governing direction is away.
- mechanism: The opening demand to see, the possibility of an exterior that misstates its condition, and the register of account together turn the focus ayah into diagnostic evidence. Visible prayer can declare one orientation while ʿan records the opposite inward direction, and that contradiction is answerable rather than trivial.
- trace:
  - 107:5 **صَلَاتِهِمْ** ص ل و B003: Prescribed worship supplies the publicly legible form whose meaning can be contradicted by the worshipper's orientation.
  - 107:5 **سَاهُونَ** س ه و B001: The heart's departure supplies the hidden condition against which the visible form is tested.
  - 107:1 **أَرَءَيْتَ** ر ء ي B013: An attention-demanding inquiry frames the later prayer conduct as something to inspect and recognize.
  - 107:1 **يُكَذِّبُ** ك ذ ب B009: A garment whose appearance lies about its condition supplies the model of devotional form misreporting inward reality.
  - 107:1 **بِٱلدِّينِ** د ي ن B002: Account and recompense make the mismatch between performed prayer and actual direction consequential.

## nonenduring prayer
- reading: They repeatedly produce the beginning or shell of prayer but do not sustain its attention, claim, or yield.
- mechanism: Two process-images of failure to continue activate a temporal reading of sāhūn. Their prayer may begin, appear viable, and then lose continuity; heedlessness is not a puncture in an otherwise maintained practice but the mechanism by which practice repeatedly runs out.
- trace:
  - 107:5 **صَلَاتِهِمْ** ص ل و B001: Binding worship supplies the practice whose defining demand is maintenance rather than a merely punctual appearance.
  - 107:5 **سَاهُونَ** س ه و B001: The heart's turning away supplies the internal break that interrupts duration.
  - 107:1 **يُكَذِّبُ** ك ذ ب B006: Milk that disappears instead of lasting supplies a material image of devotional yield that fails to persist.
  - 107:1 **يُكَذِّبُ** ك ذ ب B007: An animal that runs and then stops supplies the start-stop temporal profile of an unmaintained prayer relation.

## praying call embodied shove
- reading: Their prayer may still voice a merciful call, but heedlessness is proven when their embodied direction violently reverses that call.
- mechanism: The split mapping holds a sharp reversal: prayer can be supplicatory speech, and the context root can activate both calling someone toward oneself and violently thrusting someone away. Their prayer calls in language while their body pushes away; sāhūn names the severance that lets those opposed vectors coexist.
- trace:
  - 107:5 **صَلَاتِهِمْ** ص ل و B002: Supplication and mercy supply the prayer's verbal and relational movement toward another.
  - 107:5 **سَاهُونَ** س ه و B001: Heart-departure supplies the internal disconnection that permits speech and embodied conduct to point in opposite directions.
  - 107:2 **يَدُعُّ** د ع ع B001: Forceful pushing supplies the enacted outward vector that reverses prayer's merciful address.
  - 107:2 **يَدُعُّ** د ع ع B001: The non-dominant mapped image of calling and inclining by speech exposes the verbal vector that the shove contradicts.

## orphaned prayer
- reading: Their possessive claim is ironic: they leave their own binding prayer without the inward keeper needed to sustain it.
- mechanism: The possessive says the prayer is theirs, yet the severance image activates an inversion: they behave as absent keepers of their own binding practice. Prayer is 'orphaned' inside their ownership, cut off from the attention and maintenance that should sponsor it.
- trace:
  - 107:5 **صَلَاتِهِمْ** ص ل و B001: Binding worship supplies something entrusted to its practitioners for continued maintenance.
  - 107:5 **سَاهُونَ** س ه و B001: The heart's departure supplies the practitioner's functional absence from what remains grammatically theirs.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Severance of a child from a sustaining keeper supplies the relational pattern transferred to an unattended prayer.

## inert prayer fails to feed
- reading: Its stillness is socially diagnostic: prayer has stalled before it can impel feeding and help restore another person's stability.
- mechanism: The focus stillness becomes a blocked kinetic chain. Living prayer should impel a person toward feeding another, and provision should restore some stability to one immobilized by need; their prayer remains inert before it can become social motion.
- trace:
  - 107:5 **صَلَاتِهِمْ** ص ل و B001: Binding worship supplies the recurrent source-practice whose effects are being tested.
  - 107:5 **سَاهُونَ** س ه و B002: Stillness supplies the arrest that prevents ritual form from becoming responsive movement.
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging toward an act supplies the missing propulsion between inward worship and outward conduct.
  - 107:3 **طَعَامِ** ط ع م B002: Feeding another supplies the concrete transfer that the absent propulsion should produce.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B001: Loss of movement supplies the vulnerable recipient's arrested condition and echoes the worshipper's inert response.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B010: Sustenance that stabilizes a dwelling supplies the restorative endpoint of the blocked chain.

## practitioner exterior interior split
- reading: They can be recognizably among the praying while their actual orientation remains away from the very practice that names them.
- mechanism: The repeated prayer root first includes them among practitioners and only then exposes their relation to 'their prayer.' The target is therefore not simple nonperformance: the external class-marker and the internal directional stance have split.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B003: The context occurrence identifies them by prescribed worship, preserving real external inclusion among practitioners.
  - 107:5 **صَلَاتِهِمْ** ص ل و B003: The possessed prayer becomes the same practice toward which their hidden relation is then measured.
  - 107:5 **سَاهُونَ** س ه و B001: Heart-departure supplies the interior difference concealed by membership in the praying class.

## corrective heat evaded
- reading: Prayer is also a corrective exposure they approach without allowing it to heat, move, or straighten them.
- mechanism: The split-root inventory permits prayer to activate a process in which heat straightens what is bent. Beside the warning to worshippers, ʿan can then picture evasion of prayer's re-forming exposure: the form is approached, but the practitioner remains still and withdraws before being reshaped.
- trace:
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B004: The non-dominant split-root image of heating and straightening supplies a corrective process activated beside the warning.
  - 107:5 **صَلَاتِهِمْ** ص ل و B004: The same focus-root branch anchors the proposed re-forming force inside 'their prayer' rather than in an independent theme.
  - 107:5 **سَاهُونَ** س ه و B002: Stillness supplies resistance to the movement and reshaping that corrective heat would produce.

## attention reallocated to audience
- reading: They may be intensely attentive, but to viewers and to the story of themselves as worshippers rather than to prayer's own object and demand.
- mechanism: The following display-root reveals that attention has not disappeared; it has been reallocated. The true prayer becomes the faint object missed, while spectators and the narrated devotional persona become the bright object tracked with care.
- trace:
  - 107:5 **صَلَاتِهِمْ** ص ل و B003: Prescribed worship supplies the nominal object whose own claim loses priority.
  - 107:5 **سَاهُونَ** س ه و B005: The tiny star missed by sight models true prayer receding beneath a more conspicuous social signal.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: Performance for other people's sight supplies the competing target that captures the worshipper's attention.
  - 107:6 **يُرَآءُونَ** ر ء ي B003: The non-dominant split-root image of transmitting a report supplies a devotional identity curated as a story for others.

## withheld mercy circuit
- reading: Heedlessness is the inward form of the same blockage later visible in the closed hand: prayer's mercy never completes its passage into aid.
- mechanism: Prayer as mercy and supplication forms a potential circuit of aid. Heart-departure interrupts it inwardly; the withholding hand and blocked assistance show the same interruption outwardly. The possessive 'their prayer' becomes ironic enclosure when what should circulate is held as private devotional property.
- trace:
  - 107:5 **صَلَاتِهِمْ** ص ل و B002: Supplication, blessing, and mercy supply the relational content that ought to pass through prayer into conduct.
  - 107:5 **سَاهُونَ** س ه و B001: Heart-departure supplies the inward break in the circuit before mercy becomes material response.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B001: The hand held back from giving supplies the circuit's visible terminal blockage.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: A barrier between a person and a desired object supplies the spatial geometry shared by withheld aid and being away from prayer.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Aid and mutual support supply the beneficial flow whose denial reveals what the prayer failed to carry.

## reputation snare
- reading: 'their prayer' can become a reputation-catching apparatus whose success in public deepens its owners' hidden entanglement.
- mechanism: 
- trace:
  - 107:5 **صَلَاتِهِمْ** ص ل و B004: A set snare supplies the material model of prayer arranged to capture social regard and entangle its arranger.
  - 107:5 **سَاهُونَ** س ه و B001: Heart-departure explains why the worshipper does not register the contradiction produced by the instrument.
  - 107:1 **يُكَذِّبُ** ك ذ ب B009: A deceptive exterior supplies the snare's attractive devotional covering.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: Public display supplies the social attention that the devotional snare is arranged to catch.

## second place imitation
- reading: They may keep social pace as visible followers while never orienting themselves to the prayer they imitate.
- mechanism: 
- trace:
  - 107:5 **صَلَاتِهِمْ** ص ل و B007: The second racer following at the leader's flank supplies close external conformity without identity of aim.
  - 107:5 **سَاهُونَ** س ه و B001: Heart-departure distinguishes bodily or social following from genuine orientation.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: Performance for observers supplies a motive for keeping visible pace with a devotional leader.


# Focus 107:6

## audience as end
- reading: They do the act for the witnessing itself, making public recognition part of what the act is meant to produce.
- mechanism: The act is arranged so that another person's sight completes it; recognition by an audience is the intended payoff.
- trace:
  - 107:6 **يُرَآءُونَ** ر ء ي B005: The branch literally supplies action done for people to see and makes their recognition the causal endpoint of the performance.

## mutual gaze circuit
- reading: They stage a reciprocal encounter in which their visible signs solicit a confirming look from others.
- mechanism: The performers expose selected signs, spectators return recognition, and that returned recognition closes a mutual-visibility circuit.
- trace:
  - 107:6 **يُرَآءُونَ** ر ء ي B004: The branch literally supplies parties facing and seeing one another, turning the audience from a passive backdrop into the returning half of the circuit.
  - 107:6 **يُرَآءُونَ** ر ء ي B012: The branch literally supplies making something visible to another and assigns the performers the work of producing the sign that enters the circuit.

## public surface as identity
- reading: They erect a visible version of themselves and let that public surface certify who they claim to be.
- mechanism: A legible public surface is manufactured and then treated as an identity-marker; what can be seen substitutes for what cannot be inspected inwardly.
- trace:
  - 107:6 **يُرَآءُونَ** ر ء ي B006: The branch literally supplies a visible aspect and mirror, enabling a projected surface to function as the inspectable version of the self.
  - 107:6 **يُرَآءُونَ** ر ء ي B011: The branch literally supplies a marker erected to be noticed and makes the displayed act a public sign of claimed identity.

## commanded sight exposes staged sight
- reading: They try to control the visible evidence about themselves, but the surah's opening gaze instructs the reader to see through that controlled surface by following its social effects.
- mechanism: The opening summons the reader to inspect a person, while the focus person tries to manufacture what observers see. The repeated root therefore reverses control of the gaze: staged visibility is itself made an object of diagnostic visibility.
- trace:
  - 107:6 **يُرَآءُونَ** ر ء ي B005: The focus branch supplies conduct engineered for human sight and thus the appearance that the opening gaze must test.
  - 107:1 **أَرَءَيْتَ** ر ء ي B013: The context branch literally supplies an alerting tell-me formula and recruits the reader's attention as an investigative gaze.

## false surface and public ledger
- reading: They wear a visible ethical costume and post public credit for it, while the account that would test that credit remains unpaid.
- mechanism: The shown self becomes both a misleading outer condition and a posted public account: visible piety records social credit while concealed liability remains outside the display.
- trace:
  - 107:6 **يُرَآءُونَ** ر ء ي B006: The focus branch supplies the inspectable appearance or mirror-surface on which a persuasive ethical image can be presented.
  - 107:1 **يُكَذِّبُ** ك ذ ب B009: The branch literally supplies a garment whose condition misrepresents, making the public surface function as evidence that lies by how it looks.
  - 107:1 **بِٱلدِّينِ** د ي ن B002: The branch literally supplies accounting and recompense, turning displayed virtue into an entry in a public moral ledger.
  - 107:1 **بِٱلدِّينِ** د ي ن B003: The branch literally supplies financial debt and keeps an unpaid-liability model live beside the broader reckoning model.

## selective field of visibility
- reading: They curate who may enter the scene: approving witnesses are solicited, while the vulnerable witness whose need would falsify the image is driven outside it.
- mechanism: The performer occupies the center of mutual visibility by forcefully removing the person cut off from protection. Spectacle thus has a boundary: the claimant whose presence would test the shown identity is pushed out of frame.
- trace:
  - 107:6 **يُرَآءُونَ** ر ء ي B004: The focus branch supplies a face-to-face visible field and lets the context specify who is admitted to or expelled from that field.
  - 107:2 **يَدُعُّ** د ع ع B001: The branch literally supplies forceful pushing and provides the spatial action by which an inconvenient person is removed from view.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: The branch literally supplies a child cut off from a protector, identifying the vulnerable claimant whose exclusion preserves the performance.

## captured social influence
- reading: They absorb a public's mobilizable attention into spectacle and fail to relay that social force toward nourishment and stability.
- mechanism: Showing demonstrates an ability to organize attention, yet no urging travels outward toward feeding and stabilizing the person without secure subsistence. Public influence is captured around the performer instead of converted into care.
- trace:
  - 107:6 **يُرَآءُونَ** ر ء ي B012: The focus branch literally supplies making a sign visible to others and therefore a channel through which the performer can direct collective attention.
  - 107:3 **يَحُضُّ** ح ض ض B001: The branch literally supplies urging toward an action and marks the outward mobilization that the visible performance fails to generate.
  - 107:3 **طَعَامِ** ط ع م B002: The branch literally supplies feeding another or responding to a request for food, giving the absent mobilization a concrete recipient and outcome.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B010: The branch literally supplies sustenance that lets a person remain settled and expands feeding from a momentary gift into material stabilization.

## attention rerouted into spectators
- reading: Their attention has not simply disappeared; it has changed destination, with the spectators' gaze becoming the effective orientation of the retained ritual form.
- mechanism: Heedlessness does not leave the ritual empty: reciprocal human visibility supplies a replacement orientation. Prayer remains as form, but spectators become the operative point toward which attention is organized.
- trace:
  - 107:6 **يُرَآءُونَ** ر ء ي B004: The focus branch supplies mutual facing and lets human observers become the direction that replaces the prayer's lost inward attention.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B003: The branch literally supplies the specified act of worship, preserving the ritual form whose effective orientation is being tested.
  - 107:5 **سَاهُونَ** س ه و B001: The branch literally supplies a lapse of the heart and opens the attentional vacancy that audience-consciousness can occupy.

## one way recognition economy
- reading: They take recognition from the social field while preventing assistance from returning to it: visibility flows in, help does not flow out.
- mechanism: The display imports recognition but exports no assistance: gaze is drawn toward the performer, while hand and help are barred from traveling outward. The focus becomes the intake valve of a one-way social economy.
- trace:
  - 107:6 **يُرَآءُونَ** ر ء ي B012: The focus branch literally supplies producing something for another to see and establishes the inward flow of recognition.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B001: The branch literally supplies holding the hand back from giving and closes the outward material channel.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: The mapped branch literally supplies assistance and identifies what the closed outward channel would otherwise convey.

## relayed reputation
- reading: They shape the performance so that witnesses can relay a favorable account after the scene has ended.
- mechanism: 
- trace:
  - 107:6 **يُرَآءُونَ** ر ء ي B003: The split-mapped branch literally supplies transmission of reports or poetry and turns observers into carriers of the performer's desired reputation.

## prayer as status race
- reading: They enter a visible status race, measuring their place behind or against other performers through the observers' response.
- mechanism: 
- trace:
  - 107:6 **يُرَآءُونَ** ر ء ي B004: The focus branch literally supplies parties in one another's visible range and provides the peer field in which comparative standing can emerge.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B006: The context branch literally supplies following the leader in a race and makes displayed worship an exploratory vehicle for status positioning.

## hidden star beneath flag
- reading: They raise a bright public flag over an inward point that has become as difficult to find as a faint star.
- mechanism: 
- trace:
  - 107:6 **يُرَآءُونَ** ر ء ي B011: The focus branch literally supplies a raised marker meant to be noticed and gives the outer identity maximal legibility.
  - 107:5 **سَاهُونَ** س ه و B005: The context branch literally supplies a faint hidden star and figures the nearly imperceptible inward point beneath the conspicuous marker.

## hydraulic repletion
- reading: They appear socially full and quenched while refusing to become carriers through whom nourishment and assistance reach anyone else.
- mechanism: 
- trace:
  - 107:6 **يُرَآءُونَ** ر ء ي B001: The split-mapped branch literally supplies quenching and fullness and lets the public image appear socially satisfied or replete.
  - 107:6 **يُرَآءُونَ** ر ء ي B002: The split-mapped branch literally supplies carrying water to people and introduces the outward provisioning movement missing from mere replete appearance.
  - 107:3 **طَعَامِ** ط ع م B002: The context branch literally supplies feeding another and gives the provisioning flow a concrete material analogue.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: The mapped context branch literally supplies assistance and extends the absent outward flow beyond food to ordinary support.


# Focus 107:7

## blocked transfer
- reading: They actively stop usable help from crossing from their control into another's use.
- mechanism: An agent who could let assistance pass instead arrests its transfer at the point of giving.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B001: A hand held back from giving supplies the action of stopping an outward transfer.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Helping and backing supply the withheld object's function as practical support.

## gatekept access
- reading: They act as gatekeepers, placing accessible help behind a barrier of control.
- mechanism: Withholding can operate spatially and institutionally: the holders interpose themselves between a seeker and available support, making aid inaccessible without necessarily destroying it.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: The interposed barrier turns refusal into control of another person's access.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B003: Protected inaccessibility supplies the enclosed reserve that the gatekeeper keeps beyond reach.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance remains the thing enclosed, so the spatial model stays anchored in the focus object.

## contested mutuality
- reading: They turn a potential relation of mutual aid into a struggle over who controls the useful thing.
- mechanism: A resource whose proper logic is cooperation is recoded as an object of resistance and possession; mutuality becomes a contest.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B006: Reciprocal resistance over an object supplies the adversarial handling of the resource.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Mutual help supplies the cooperative relation that is being converted into contention.

## protective reserve
- reading: In focus-only isolation, a minority reading can hear guarded help preserved against a lean period.
- mechanism: Read without context, withholding could preserve an aid-stock against depletion: a protective enclosure rather than selfish non-giving.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B003: Protective strength supplies the possibility that inaccessibility guards rather than merely hoards.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B007: Resilience through a hard year supplies a scarcity-management motive for temporary restraint.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance supplies the reserve's proposed communal purpose.

## accountable due
- reading: They enact denial by refusing an accountable claim of assistance.
- mechanism: The opening demand to inspect, followed by denial and the account/debt field, makes the final withholding observable evidence of repudiating an obligation. Assistance shifts from optional generosity to something answerable and relationally due.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B001: Stopped giving provides the concrete act entered into the moral account.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Practical assistance supplies the due whose non-transfer becomes diagnostic.
  - 107:1 **أَرَءَيْتَ** ر ء ي B013: The attention-directing inquiry frames the final act as something to inspect and recognize.
  - 107:1 **يُكَذِّبُ** ك ذ ب B001: Contradiction of truth supplies the gap between a claimed order and the enacted refusal.
  - 107:1 **بِٱلدِّينِ** د ي ن B002: Accounting and recompense make the withheld act answerable rather than socially negligible.
  - 107:1 **بِٱلدِّينِ** د ي ن B003: Financial indebtedness sharpens assistance into a due relation rather than a surplus favor.

## severance and exclusion
- reading: They maintain social expulsion by barring substitute support from someone already severed from a protector.
- mechanism: Severe expulsion meets a person defined by loss of a sustaining guardian. The focus barrier therefore becomes a second severance: replacement support is kept from one already cut off from primary support.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: An interposed barrier supplies the access-denial that continues the earlier exclusion.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Helping and backing supply the replacement support being barred.
  - 107:2 **يَدُعُّ** د ع ع B001: Forceful pushing supplies the outward motion of social expulsion.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Separation from a caretaker supplies the prior rupture that makes blocked aid especially consequential.

## rejected claim and belonging
- reading: They deny the requester's recognized claim on the helping relation itself.
- mechanism: The non-dominant mapped branch activates claim and affiliation beneath the scene of pushing. Withholding help can then reject not only a requested object but the claimant's standing to ask and belong.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: The barrier supplies a boundary that can exclude a claimant from recognized access.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance supplies the relation through which standing and belonging would become practical.
  - 107:2 **يَدُعُّ** د ع ع B002: A claim of right or affiliation supplies the socially asserted bond that the final gatekeeping can refuse.

## blocked support network
- reading: They suppress an aid network, blocking both direct provision and the social multiplier that could sustain a vulnerable life.
- mechanism: Refusal to urge, failure to feed, and provision that would stabilize a life form a social supply chain. The focus action blocks both the direct input and the recruitment of other helpers, preventing support from multiplying.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B001: Holding back from giving supplies the last blocked link in the support chain.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Mutual assistance supplies the network relation that could distribute support among multiple agents.
  - 107:3 **يَحُضُّ** ح ض ض B001: Urging toward an act supplies the missing recruitment mechanism by which one helper could activate others.
  - 107:3 **طَعَامِ** ط ع م B002: Feeding another supplies the concrete transfer that social urging should produce.
  - 107:3 **ٱلْمِسْكِينِ** س ك ن B010: Sustenance that stabilizes residence supplies the durable outcome that repeated small help could maintain.

## withheld capability
- reading: They withhold the practical means by which another person could regain capacity and act.
- mechanism: A food-root branch reaches capacity over a thing. In contact with assistance, the focus object can be heard as an enabling means: what is withheld is another person's ability to act, not only something to consume.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: The barrier supplies obstruction between a person and the means of action sought.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance supplies the enabling relation rather than a merely consumable object.
  - 107:3 **طَعَامِ** ط ع م B011: Capacity to do a thing supplies the downstream agency that practical support can unlock.

## ritual without mercy output
- reading: Withholding aid is the missing material consequence of a rite that invokes mercy but fails to transmit it.
- mechanism: Prayer activates worship, supplication, and mercy, while heedlessness breaks attention. The focus refusal becomes a failed material output: mercy is invoked or displayed but does not travel outward as help.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B001: The arrested hand supplies the point where voiced mercy fails to become material transfer.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Helping supplies the practical form that mercy would take outside the rite.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B002: Supplication, praise, and mercy supply the ritual content expected to issue in care.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B003: Specified worship supplies the performed form whose practical consequence is being tested.
  - 107:5 **سَاهُونَ** س ه و B001: Heedlessness of heart supplies the break between ritual attention and another person's need.

## stalled follow through
- reading: They allow the leading rite to run while stopping its practical follower before aid arrives.
- mechanism: A prayer-root branch pictures the runner following the leader, while heedlessness can be stillness. The sequence activates a process model in which practical aid ought to follow ritual, but the second movement stalls.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: The barrier supplies the obstacle that prevents the practical follower from reaching its destination.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance supplies the expected second movement after ritual performance.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B006: The runner following a predecessor supplies the image of ethical consequence trailing ritual action.
  - 107:5 **سَاهُونَ** س ه و B002: Stillness supplies the stalled transition in which no practical follow-through arrives.

## unnoticed ordinary help
- reading: Some withholding is sustained by trained inattention: ordinary help is made too minor to notice while the result remains real.
- mechanism: Heedlessness and the image of a faint, easily missed object introduce a second agency model beside deliberate refusal. Ordinary help can be withheld by being kept below attention until non-transfer becomes habitual.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B001: Non-giving supplies the observable result even when its maintenance is inattentive rather than freshly chosen.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Practical help supplies the ordinary claim that slips outside the actor's field of concern.
  - 107:5 **سَاهُونَ** س ه و B001: Heart-level heedlessness supplies the mechanism by which another's need goes unattended.
  - 107:5 **سَاهُونَ** س ه و B005: A faint celestial object supplies the low-visibility quality of mundane assistance in the moral field.

## display without circulation
- reading: They allocate outward flow to reputation instead of utility: their image travels to people while their help does not.
- mechanism: The actors cause themselves or their acts to be seen, then prevent help from leaving their control. Visibility circulates while assistance does not; the final object becomes a diagnostic counterweight to public performance.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B001: Holding back the hand supplies the private non-circulation set against public projection.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance supplies the socially useful thing that fails to circulate.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: Performance for people's sight supplies the outward circulation of reputation.
  - 107:6 **يُرَآءُونَ** ر ء ي B012: Making something visible supplies the active production of an image for observers.

## protective reading reversed
- reading: The context reverses the likely beneficiary: the enclosure protects the holders and their stock or standing from others' claims.
- mechanism: The focus-only possibility of guarding a communal reserve loses plausibility when the surrounding actions push away the vulnerable, refuse to mobilize provision, and cultivate public display. Protection is not erased from the root inventory, but its likely beneficiary reverses from community to holder.
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B003: Protective inaccessibility preserves the baseline possibility now being reassigned toward self-protection.
  - 107:7 **وَيَمْنَعُونَ** م ن ع B007: Scarcity-resilience supplies the rationing rationale that context sharply weakens.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance supplies the proposed common good whose communal destination the context undermines.
  - 107:2 **يَدُعُّ** د ع ع B001: Forceful expulsion makes care for the vulnerable an unlikely motive for enclosure.
  - 107:3 **يَحُضُّ** ح ض ض B001: The absent mobilization toward provision removes evidence of a genuinely communal reserve policy.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: Public performance supplies a self-regarding motive more coherent with the surrounding sequence.

## social graft refused
- reading: They prevent the practical graft by which a severed person could be joined back into a sustaining social body.
- mechanism: 
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: The barrier supplies resistance at the point where a severed life might be reconnected.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance supplies the sustaining relation needed for social reconnection.
  - 107:2 **ٱلْيَتِيمَ** ي ت م B001: Separation from a caretaker supplies the severed condition requiring a new supporting bond.
  - 107:3 **طَعَامِ** ط ع م B010: A branch accepting a graft supplies the material analogy for joining a vulnerable person back into sustaining stock.

## water carrier without delivery
- reading: They resemble full carriers whose visible load advertises capacity while relief never completes the trip.
- mechanism: 
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: The barrier supplies the failed last mile between a carried resource and its recipient.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance supplies the relief that should be delivered rather than merely possessed.
  - 107:6 **يُرَآءُونَ** ر ء ي B002: Bringing and carrying water supplies a concrete model of aid in transit.
  - 107:6 **يُرَآءُونَ** ر ء ي B008: Visible fullness supplies the appearance of abundance that can coexist with failed delivery.

## ritual snare
- reading: Display can function as a snare that captures moral credit and helps keep concrete claims on assistance outside the gate.
- mechanism: 
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B002: The barrier supplies the screening of material claims behind a favorable public surface.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B001: Assistance supplies the practical claim that the reputational mechanism diverts or captures.
  - 107:4 **لِّلْمُصَلِّينَ** ص ل و B005: The snare supplies a mechanism that captures social credit through the performed rite.
  - 107:6 **يُرَآءُونَ** ر ء ي B005: Performance for observers supplies the bait-like visibility by which esteem is captured.

## cooperation becomes repeated war
- reading: Repeated contest over useful support can harden the helping relation into a seasoned social war.
- mechanism: 
- trace:
  - 107:7 **وَيَمْنَعُونَ** م ن ع B006: Mutual resistance over an object supplies the contested exchange.
  - 107:7 **ٱلْمَاعُونَ** م ع ن B003: Seasoned, recurring conflict supplies the temporal pattern into which repeated failures of mutual aid can harden.
