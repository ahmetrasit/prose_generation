Focus: 90:9. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/90_9/D.r13/context.md =====
# 90:9 — focus

وَلِسَانًۭا وَشَفَتَيْنِ

Anchor translation (canonical reading, reference only):

Bir dil ve iki dudak da?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَلِسَانًا | لِسَان | ل س ن | CONJ;N |
| 2 | وَشَفَتَيْنِ | شَفَتَيْن | ش ف ه | CONJ;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 90 — full text (context; no pericope)

- 90:1 لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ
- 90:2 وَأَنتَ حِلٌّۢ بِهَٰذَا ٱلْبَلَدِ
- 90:3 وَوَالِدٍۢ وَمَا وَلَدَ
- 90:4 لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِى كَبَدٍ
- 90:5 أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ
- 90:6 يَقُولُ أَهْلَكْتُ مَالًۭا لُّبَدًا
- 90:7 أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ
- 90:8 أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ
- 90:9 ◀ focus وَلِسَانًۭا وَشَفَتَيْنِ
- 90:10 وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ
- 90:11 فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ
- 90:12 وَمَآ أَدْرَىٰكَ مَا ٱلْعَقَبَةُ
- 90:13 فَكُّ رَقَبَةٍ
- 90:14 أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ
- 90:15 يَتِيمًۭا ذَا مَقْرَبَةٍ
- 90:16 أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ
- 90:17 ثُمَّ كَانَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ وَتَوَاصَوْا۟ بِٱلصَّبْرِ وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ
- 90:18 أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ
- 90:19 وَٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا هُمْ أَصْحَٰبُ ٱلْمَشْـَٔمَةِ
- 90:20 عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ


===== _commentary/v16/work/90_9/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ل س ن (root_001355) — identity root of وَلِسَانًا (w1)

- **B001** konuşma organı ve söyleyiş gücü — konuşma organı olan dil ve onun söyleyiş gücü · konuşma organı anlamındaki dilin çoğulu · konuşma organı anlamındaki dilin çoğulu
  اللسان معروف وهو مذكر والجمع ألسن (maqayis)؛ اللسان ما ينطق يذكر ويؤنث والألسن والألسنة (ayn)؛ اللسان جارحة الكلام (sihah)؛ اللسان يذكر ويؤنث وجمعه ألسن وألسنة (tahdhib)؛ اللسان الجارحة وقوتها (mufradat)
- **B002** birine sözle sataşma — birine sözle sataşmak veya çıkışmak · bana sözle sataştı veya üzerime geldi
  لسنته إذا أخذته بلسانك (maqayis)؛ لسن فلان فلانا يلسنه أي أخذه بلسانه (ayn)؛ لسنته إذا أخذته بلسانك (sihah)؛ لسنت الرجل ألسنه لسنا إذا أخذته بلسانك (tahdhib)
- **B003** açık ve etkili konuşma yetkinliği — açık, düzgün ve etkili konuşma yetkinliği · açık ve etkili konuşan · daha açık, etkili ve gerekçesi güçlü konuşan
  اللسن جودة اللسان والفصاحة (maqayis)؛ رجل لسن بين اللسن (ayn)؛ اللسن الفصاحة وقد لسن فهو لسن وألسن (sihah)؛ رجل لسن بين اللسن إذا كان ذا بيان وفصاحة (tahdhib)؛ أفصح وأبين كلاما وأقدر على الحجة (mufradat)
- **B004** dil ucunu andıran ince ve uzunca biçim — ucu dil gibi olan; ince ve hafif uzun · ön ucu dil biçiminde, ince ve uzunca ayakkabı · ince ve hafif uzun ayak
  أصل يدل على طول لطيف غير بائن ونعل ملسنة على صورة اللسان وقدم ملسنة فيها لطافة وطول يسير (maqayis)؛ شيء ملسن جعل طرفه كطرف اللسان (ayn)؛ الملسن من النعال الذي فيه طول ولطافة على هيئة اللسان وامرأة ملسنة القدمين (sihah)؛ نعل ملسنة إذا جعل طرف مقدمها كطرف اللسان (tahdhib)
- **B005** dil ucunun kesilmesi — kişinin dil ucunu kesmek · dilinin ucu kesilmiş kişi
  لسن الرجل أي قطع طرف لسانه فهو ملسون (ayn)
- **B006** bir topluluğun dili ve konuşması — bir topluluğun dili ve konuşması · bir topluluğun konuştuğu dil · söz, sözcük, haber veya ileti · topluluk adına konuşan kişi, topluluğun sözcüsü · insanların kişi hakkında söylediği övgü · farklı diller ve konuşma sesleri
  اللسن اللغة ويعبر بالرسالة عن اللسان (maqayis)؛ اللسان الكلام (ayn)؛ يكنى بها عن الكلمة واللسن اللغة لكل قوم لسن (sihah)؛ لكل قوم لسن أي لغة ولسان الناس عليك ثناؤهم ولسان بني عامر الكلمة أو الخبر (tahdhib)؛ لكل قوم لسان ولسن أي لغة واختلاف الألسنة إشارة إلى اختلاف اللغات والنغمات (mufradat)
- **B007** ödünç yavruyla dişi devenin sütünü indirtme — ödünç yavruya süt tattırıp onu uzaklaştırarak dişi devenin sütünü indirtme · bu işlem için ödünç yavru verilen yavrusuz dişi deve
  التلسين أن يعير الرجل الرجل فصيلا لتدر عليه ناقته فإذا درت نحي الفصيل ومعناه أنه ذاق اللبن بلسانه (maqayis)؛ التلسين أن يعير الرجل فصيلا لتدر عليه ناقته فإذا درت نحي الفصيل ومعناه أنه ذاق اللبن بلسانه (maqayis-routing)؛ الخلية من الإبل يقال لها المتلسنة وهو التلسن (tahdhib)
- **B008** iletiyi ulaştırma — iletiyi ulaştırma · o kişiden veya o kişiye haberi benim için ilet · o kişiyle ilgili sözü benim için ilet
  يعبر بالرسالة عن اللسان (maqayis)؛ الإلسان إبلاغ الرسالة وألسني فلانا وألسن لي فلانا كذا أي أبلغ لي (tahdhib)
- **B009** lifi ezip şeritlere ayırarak büküme hazırlama — lifi ezip ince şeritler hâline getirerek büküme hazırlamak · lifi ezip ince şeritlere ayırarak büküme hazırlama
  لسنت الليف إذا مشنته ثم جعلته فتائل مهيأة للفتل ويسمى ذلك التلسين (tahdhib)
- **B010** yalancı — yalancı; kullanımı tartışmalı
  الملسون الكذاب (sihah)؛ يقولون الملسون الكذاب وهذا مشتق من اللسان (maqayis)؛ الملسون الكذاب قال الشيخ لا أعرفه (tahdhib)

## ش ف ه (root_000804) — identity root of وَشَفَتَيْنِ (w2)

- **B001** dudak; dudak yapısı ve dudaksıl sesler — dudak; ağız kenarındaki organ · dudaklar · küçük dudak · organ adının eski son sessizini koruyan biçimi · dudakları kapanmayan adam · iri dudaklı adam · dudaksıl harfler; dudaklarla çıkarılan üç belirli harf
  الشفة حذفت منها الهاء وتصغيرها شفيهة والجميع الشفاه (ayn;tahdhib)؛ رجل أشفى إذا كان لا تنضم شفتاه (sihah)؛ رجل شفاهي عظيم الشفتين (sihah)؛ الحروف الشفهية الباء والفاء والميم (sihah)
- **B002** yüz yüze konuşma; olumsuz kalıplarda tek söz — yüz yüze konuşma; doğrudan sözlü iletişim · ona tek söz söylemedim · ondan tek söz işitmedim
  المشافهة بالكلام المواجهة من فيك إلى فيه (ayn)؛ المشافهة المخاطبة من فيك إلى فيه (sihah)؛ ما كلمته ببنت شفة أي بكلمة (sihah)؛ ما سمعت منه ذات شفة أي كلمة (tahdhib)
- **B003** meşgul etme; yoğun taleple tüketme veya kıtlaştırma — meşguliyet; uğraş · beni bundan alıkoydu · otlağı ve suyu senin kullanımından alıkoyuyoruz; ikisinde de fazlalık yok · ısrarlı istekleriyle beni tüketti · insanların üşüşerek azalttığı veya azlığından kullanımı engellenen su · insanların üşüştüğü veya çoğu tüketilmiş sular · az yiyecek · insanların istekleriyle elindekiler tüketilmiş adam · çok kalabalık bir ailen oldu ya da soru ve sözle bunaltıldın · bizden uzak, başkalarının yoğun talepleriyle meşgul · insanlardan az isteyen · o kişinin iyiliğinden sana düşen hiçbir şeyi meşgul edip tüketmedim
  ماء مشفوة أي مطلوب مسؤول وهو الذي كثر عليه الناس وأنفدوه إلا أقله (ayn)؛ طعام مشفوه أي قليل (ayn)؛ الشفه الشغل (sihah)؛ شفهني عن كذا أي شغلني (sihah)؛ خفيف الشفة أي قليل السؤال للناس (sihah)؛ رجل مشفوه إذا كثر سؤال الناس إياه حتى نفذ ما عنده (sihah)؛ ماء مشفوه وهو الذي كثر عليه الناس (tahdhib)؛ ما شفهت عليك من خير فلان شيئا (tahdhib)؛ فلان مشفوة عنا أي مشغول عنا مكثور عليه (tahdhib)؛ كان مشفوها أي كان قليلا (tahdhib)
- **B004** insanlar arasındaki iyi ad ve övgü [kalıp] — insanlar arasında iyi bir adı ve övgüsü var · insanların senin hakkındaki sözü ve övgüsü güzel
  له في الناس شفة أي ثناء حسن (sihah)؛ شفة الناس عليك لحسنة أي ذكرهم لك وثناءهم عليك حسن (tahdhib)

===== _commentary/v16/out/s090/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 90:9, and ## Buluşmalar) =====
## Harcanan mal: övünme, gösteriş ve hesap

Altıncı ayet bir sözdür. Adam konuşur: {ar:يَقُولُ, tr:yekûlu, gloss:der, source:90:6}. Sözün kökü dilden çıkan sesi bildirir: {ar:القول من النطق, tr:el-kavlu mine'n-nutk, gloss:kavl konuşmadandır, source:"ق و ل,B001"}. Aynı kök, insanlar arasında yayılan adı da bildirir: {ar:انتشرت له قالة حسنة أو قبيحة في الناس, tr:inteşeret lehû kâletun hasenetun ev kabîhatun fi'n-nâs, gloss:insanlar arasında onun hakkında iyi ya da kötü bir söz yayıldı, source:"ق و ل,B007"}. Övünme bu yayılmayı hedefler. Söylenen şey {ar:أَهْلَكْتُ مَالًۭا, tr:ehlektu mâlen, gloss:mal tükettim, source:90:6} sözüdür. Fiil bir şeyin yok olmasının bütün yollarını kapsar: {ar:الهلاك على أوجه افتقاد الشيء واستحالة وفساد والموت وبطلان الشيء وعدمه, tr:el-helâku alâ evcuh iftikâdu'ş-şey' ve'stihâle ve fesâd ve'l-mevt ve butlânu'ş-şey' ve ademuh, gloss:helak birkaç türlüdür: kaybolmak ve bozulmak ve ölüm ve bir şeyin boşa çıkıp yok olması, source:"ه ل ك,B001"}. Mal da edinilip tutulan şeydir: {ar:تمول الرجل اتخذ مالا, tr:temevvele'r-racul ittehaze mâlâ, gloss:adam mal edindi, source:"م و ل,B001"}. Bu kelimenin eski dünyasında mal çoğunlukla sürüdür: {ar:كانت أموال العرب أنعامهم, tr:kânet emvâlu'l-arabi en'âmehum, gloss:Arapların malları hayvanlarıydı, source:"م و ل,B001"}. Adamın övündüğü şey bir harcama değil, bir yok edişin sayımıdır. Hesabı tutulan yalnızca miktardır, nereye gittiği değil.

Yedinci ayet bu sözü bir soruyla karşılar: {ar:أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ, tr:e-yahsebu en lem yerahû ehad, gloss:onu hiç kimsenin görmediğini mi sanıyor, source:90:7}. "Görmek" fiilinin ailesinde gösteriş de vardır: {ar:وهو أن يفعل شيئا ليراه الناس, tr:ve huve en yef'ale şey'en li-yerâhu'n-nâs, gloss:insanlar görsün diye bir şey yapmaktır, source:"ر ء ي,B005"}. Sahnenin içindeki çelişki böylece görünür olur: harcamasının insanlarca görülmesini isteyen adam, kendisinin görülmediğini sanır. "Yahsebu" fiilinin kökü de aynı çifte işler. Bir yanda insanın sayılan şerefi vardır: {ar:الحسب الذي يعد من الإنسان, tr:el-hasebu'llezî yu'addu mine'l-insân, gloss:haseb insandan sayılıp dökülen şeydir, source:"ح س ب,B004"}. Bir başka söyleyiş de {ar:ما يعده الإنسان من مفاخر آبائه, tr:mâ yeudduhu'l-insânu min mefâhiri âbâih, gloss:insanın atalarının övünç konularından saydığı şeyler, source:"ح س ب,B004"}. Öbür yanda bunun tam tersi bir sayım vardır: {ar:احتسبت بكذا أجرا عند الله, tr:ihtesebtu bi-kezâ ecran indallâh, gloss:şunu Allah katında ecir olarak hesaba yazdım, source:"ح س ب,B005"}. Kaybedileni ya da verileni Allah'ın hesabına yazmak, övünmenin sayımının karşıtıdır. Ayetteki fiil ise ikisinin de yerine geçen sanıdır: {ar:الحسبان الظن, tr:el-husbânu'z-zann, gloss:husbân sanıdır, source:"ح س ب,B002"}. Kök bir de gökten inen ateşi adlandırır: {ar:حسبانا من السماء أي نارا تحرقها, tr:husbânen mine's-semâ ey nâran tuhrikuhâ, gloss:gökten bir husbân yani onu yakan bir ateş, source:"ح س ب,B007"}.

Sekizinci ve dokuzuncu ayetler insana verilen araçları sayar: {ar:وَلِسَانًۭا وَشَفَتَيْنِ, tr:ve lisânen ve şefeteyn, gloss:ve bir dil ve iki dudak, source:90:9}. Bu iki kelimenin ailesi de övgü dilini bilir: {ar:لسان الناس عليك ثناؤهم, tr:lisânu'n-nâsi aleyke senâuhum, gloss:insanların senin üzerine dili onların seni övmesidir, source:"ل س ن,B006"}. Bir başka söyleyiş de {ar:له في الناس شفة أي ثناء حسن, tr:lehû fi'n-nâsi şefe ey senâun hasen, gloss:onun insanlar arasında bir dudağı var yani güzel bir anılışı, source:"ش ف ه,B004"}. Övünen adamın istediği tam budur: insanların dilinde ve dudağında olmak. Ama dudağın ailesinde bir başka adam da vardır: {ar:رجل مشفوه إذا كثر سؤال الناس إياه حتى نفذ ما عنده, tr:raculun meşfûh izâ kesura suâlu'n-nâsi iyyâh hattâ nefize mâ indeh, gloss:insanlar ondan o kadar çok istedi ki elindeki tükendi, source:"ش ف ه,B003"}. Malın gerçekten tükenmesi de böyle olur: birçok ağız ister, el verir, elde bir şey kalmaz. Övünmenin "tükettim"i ile verenin tükenişi aynı kelimeyle söylenebilir, ama farklı iki sahnedir.

Kur'an bu sahneyi birçok kez kurar. Allah müminlere {ar:لَا تُبْطِلُوا۟ صَدَقَٰتِكُم بِٱلْمَنِّ وَٱلْأَذَىٰ كَٱلَّذِى يُنفِقُ مَالَهُۥ رِئَآءَ ٱلنَّاسِ, tr:lâ tubtılû sadakâtikum bi'l-menni ve'l-ezâ ke'llezî yunfiku mâlehû riâe'n-nâs, gloss:sadakalarınızı başa kakma ve eziyetle boşa çıkarmayın tıpkı malını insanlara gösteriş için harcayan gibi, source:2:264} der. Aynı ayetin sonunda bu harcayanlar için {ar:لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟, tr:lâ yakdirûne alâ şey'in mimmâ kesebû, gloss:kazandıklarından hiçbir şeye güç yetiremezler, source:2:264} denir. Gösteriş harcaması, beşinci ayetin "kadara" fiiliyle biter. Aynı figür başka bir yerde de görünür: {ar:وَٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ رِئَآءَ ٱلنَّاسِ, tr:vellezîne yunfikûne emvâlehum riâe'n-nâs, gloss:mallarını insanlara gösteriş için harcayanlar, source:4:38}. Yetimi iten ve yoksulun yemeğine teşvik etmeyen kişinin anlatıldığı surede de iki kusur yan yana gelir: {ar:ٱلَّذِينَ هُمْ يُرَآءُونَ, tr:ellezîne hum yurâûn, gloss:onlar gösteriş yaparlar, source:107:6} ve {ar:وَيَمْنَعُونَ ٱلْمَاعُونَ, tr:ve yemne'ûne'l-mâ'ûn, gloss:ve en küçük yardımı esirgerler, source:107:7}. Allah'ın kınadığı mal yığıcının sahnesinde de aynı iki fiil vardır: {ar:ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ, tr:ellezî ceme'a mâlen ve addedeh, gloss:mal toplayıp onu sayan, source:104:2} ve {ar:يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ, tr:yahsebu enne mâlehû ahledeh, gloss:malının onu ebedî kılacağını sanır, source:104:3}. Saymak ve sanmak yine yan yanadır.

İki adam misalinde, bağının sahibi bağına girer ve {ar:مَآ أَظُنُّ أَن تَبِيدَ هَٰذِهِۦٓ أَبَدًۭا, tr:mâ ezunnu en tebîde hâzihî ebedâ, gloss:bunun hiç yok olacağını sanmıyorum, source:18:35} der. Arkadaşı Rabbinin {ar:وَيُرْسِلَ عَلَيْهَا حُسْبَانًۭا مِّنَ ٱلسَّمَآءِ, tr:ve yursile aleyhâ husbânen mine's-semâ, gloss:ve onun üstüne gökten bir husbân göndermesini, source:18:40} umar. Sonunda bağ sahibi {ar:يُقَلِّبُ كَفَّيْهِ عَلَىٰ مَآ أَنفَقَ فِيهَا, tr:yukallibu keffeyhi alâ mâ enfeka fîhâ, gloss:oraya harcadıkları için ellerini ovuşturur, source:18:42} ve {ar:يَٰلَيْتَنِى لَمْ أُشْرِكْ بِرَبِّىٓ أَحَدًۭا, tr:yâ leytenî lem uşrik bi-rabbî ehadâ, gloss:keşke Rabbime kimseyi ortak koşmasaydım, source:18:42} der. Harcanan mal, sanı, gökten gelen ateş ve "ehad" kelimesi tek bir sahnede toplanır. Kitabı sol eline verilen adam da kendi sözüyle konuşur: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ, tr:mâ ağnâ annî mâliyeh, gloss:malım bana bir yarar sağlamadı, source:69:28} ve {ar:هَلَكَ عَنِّى سُلْطَٰنِيَهْ, tr:heleke annî sultâniyeh, gloss:gücüm benden yok olup gitti, source:69:29}. Altıncı ayette "tükettim" diyen fiil, o gün adamın kendisinden tükenen gücü anlatır. Kendisine hazineler verilen Karun da malı için {ar:إِنَّمَآ أُوتِيتُهُۥ عَلَىٰ عِلْمٍ عِندِىٓ, tr:innemâ ûtîtuhû alâ ilmin indî, gloss:bu bana ancak bendeki bir bilgi sayesinde verildi, source:28:78} der. Aynı ayet fiili bu kez Allah'ı özne yaparak kullanır: {ar:أَوَلَمْ يَعْلَمْ أَنَّ ٱللَّهَ قَدْ أَهْلَكَ مِن قَبْلِهِۦ, tr:e-ve lem ya'lem ennallâhe kad ehleke min kablih, gloss:Allah'ın ondan önce nicelerini helak ettiğini bilmiyor muydu, source:28:78}. Kendini görmek de bir tehlike olarak anılır: {ar:كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ, tr:kellâ inne'l-insâne le-yatğâ, gloss:hayır insan gerçekten azar, source:96:6} ve {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en reâhu'steğnâ, gloss:kendini yeterli gördüğünde, source:96:7}. Yığılmış malın sonu da açıkça söylenir: {ar:هَٰذَا مَا كَنَزْتُمْ لِأَنفُسِكُمْ فَذُوقُوا۟ مَا كُنتُمْ تَكْنِزُونَ, tr:hâzâ mâ kenaztum li-enfusikum fe-zûkû mâ kuntum teknizûn, gloss:işte kendiniz için biriktirdiğiniz bu; biriktirdiğinizi tadın, source:9:35}.

Karşıt söz de Kur'an'da vardır. Doyuranlar şöyle konuşur: {ar:إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءًۭ وَلَا شُكُورًا, tr:innemâ nut'imukum li-vechillâhi lâ nurîdu minkum cezâen ve lâ şukûrâ, gloss:sizi yalnızca Allah'ın yüzü için doyuruyoruz; sizden ne bir karşılık ne de bir teşekkür istiyoruz, source:76:9}. Malını veren sakınan kişi için de {ar:ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ, tr:ellezî yu'tî mâlehû yetezekkâ, gloss:arınmak için malını veren, source:92:18} ve {ar:إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ, tr:illebtiğâe vechi rabbihi'l-a'lâ, gloss:yalnızca yüce Rabbinin yüzünü arayarak, source:92:20} denir. Harcayıp başa kakmayanlar da şöyle anılır: {ar:ثُمَّ لَا يُتْبِعُونَ مَآ أَنفَقُوا۟ مَنًّۭا وَلَآ أَذًۭى, tr:summe lâ yutbi'ûne mâ enfekû mennen ve lâ ezâ, gloss:sonra harcadıklarının ardından ne başa kakma ne eziyet getirirler, source:2:262}. Dilin doğru övgüsü de vardır. İbrahim Rabbinden {ar:وَٱجْعَل لِّى لِسَانَ صِدْقٍۢ فِى ٱلْءَاخِرِينَ, tr:vec'al lî lisâne sıdkın fi'l-âhirîn, gloss:sonrakiler arasında benim için doğru bir dil kıl, source:26:84} diye ister. Övünen adam bu dili kendi sözüyle almaya çalışır, İbrahim ise onu Rabbinden ister.

Kaynaklar: 90:6 يَقُولُ ق و ل B001, B007; 90:6 أَهْلَكْتُ ه ل ك B001; 90:6 مَالًۭا م و ل B001; 90:6 لُّبَدًا ل ب د B002; 90:7 يَرَهُۥٓ ر ء ي B005; 90:5 أَيَحْسَبُ ح س ب B002, B004, B005, B007; 90:7 أَيَحْسَبُ ح س ب B002, B004, B005; 90:9 وَلِسَانًۭا ل س ن B006; 90:9 وَشَفَتَيْنِ ش ف ه B003, B004

## Yapılmış beden ve ağzın iki yönlü işi

Sure bedeni parça parça adlandırır. Dördüncü ayetin "kebed"i, zorluk anlamının yanında içteki bir organın da adıdır: {ar:الأكباد جمع كبد وهي اللحمة السوداء في البطن, tr:el-ekbâdu cem'u kebid ve hiye'l-lahmetu's-sevdâu fi'l-batn, gloss:ekbâd kebidin çoğuludur ve o karındaki kara ettir, source:"ك ب د,B001"}. Yani ciğer. Aynı ayeti, kelimeyi dikliğe bağlayarak okuyan bir söyleyiş de vardır: {ar:خلقناه منتصبا معتدلا, tr:halaknâhu muntesıben mu'tedilâ, gloss:onu dik ve dengeli yarattık, source:"ك ب د,B009"}. Bir başka söyleyiş de {ar:الكبد الاستواء والاستقامة, tr:el-kebedu'l-istivâu ve'l-istikâme, gloss:kebed düzgünlük ve dikliktir, source:"ك ب د,B009"}. Yaratma fiilinin ailesi de tamlığı bilir: {ar:رجل خليق ومختلق أي تام الخلق معتدل, tr:raculun halîkun ve muhtelak ey tâmmu'l-halki mu'tedil, gloss:yaratılışı tam ve dengeli adam, source:"خ ل ق,B003"}. Ana karnındaki parça da öyle: {ar:مضغة مخلقة أي تامة الخلق, tr:mudğatun muhallaka ey tâmmetu'l-halk, gloss:yaratılışı tamamlanmış et parçası, source:"خ ل ق,B003"}. Sonra sekizinci ve dokuzuncu ayetler gelir: iki göz, bir dil, iki dudak. Dil konuşma organıdır: {ar:اللسان جارحة الكلام, tr:el-lisânu cârihatu'l-kelâm, gloss:dil konuşma organıdır, source:"ل س ن,B001"}. On üçüncü ayet çeneyi ve boynu getirir. "Fekk" çenedir: {ar:الفك اللحي, tr:el-fekku'l-lahy, gloss:fekk çene kemiğidir, source:"ف ك ك,B004"}. Bir başka söyleyiş de {ar:الفكان ملتقى الشدقين, tr:el-fekkâni multeka'ş-şidkayn, gloss:iki fekk iki yanağın buluştuğu yerdir, source:"ف ك ك,B004"}. Boyun da dikliğinden adını alır: {ar:الرقبة مؤخر أصل العنق, tr:er-rakabetu muahharu asli'l-unuk, gloss:rakabe boynun dibinin arkasıdır, source:"ر ق ب,B004"} ve {ar:اشتقاق الرقبة لأنها منتصبة, tr:iştikâku'r-rakabeti li-ennehâ muntesıba, gloss:rakabe dik durduğu için bu adı aldı, source:"ر ق ب,B004"}. Birinci ayetin "beled"i göğsü ({ar:البلدة الصدر وفلان واسع البلدة أي واسع الصدر, tr:el-beldetu's-sadr ve fulânun vâsi'u'l-belde, gloss:belde göğüstür ve göğsü geniş adama belde'si geniş denir, source:"ب ل د,B002"}), on altıncı ayetin "matrabe"si gerdanlık kemiklerini anar: {ar:الترائب موضع القلادة من الصدر, tr:et-terâibu mevdi'u'l-kılâdeti mine's-sadr, gloss:terâib göğüste gerdanlığın durduğu yerdir, source:"ت ر ب,B005"}. On sekizinci ayetin "meymene"si sağ elin adıyla kurulur: {ar:اليمين أصله الجارحة والميمنة ناحية اليمين, tr:el-yemînu asluhu'l-câriha ve'l-meymenetu nâhiyetu'l-yemîn, gloss:yeminin aslı eldir ve meymene sağ taraftır, source:"ي م ن,B002"}.

Bu sayımın düz bir anlatımın veremeyeceği yanı şudur: sure, kendini kimsenin görmediğini ve kimsenin ona güç yetiremeyeceğini sanan adamın bedenini, bir zanaatkârın tezgâhındaki parçalar gibi sayar. Gözler, dil ve dudaklar verilmiş araçlardır. Sorulacak şey bu araçların neye kullanıldığıdır.

Ağız bu bedenin en çok işleyen yeridir ve surede iki yönde çalışır. Dışarıya söz çıkar. Altıncı ayetin fiili dili kendi adıyla anar: {ar:المقول اللسان, tr:el-mikvelu'l-lisân, gloss:mikvel yani söyleyen dildir, source:"ق و ل,B002"}. "Yekûlu" ile "lisân" böylece aynı aletin işi ve adı olur. Dudak ağızdan ağıza konuşmayı adlandırır: {ar:المشافهة المخاطبة من فيك إلى فيه, tr:el-muşâfehetu'l-muhâtabetu min fîke ilâ fîh, gloss:müşafehe senin ağzından onun ağzına konuşmaktır, source:"ش ف ه,B002"}. Birçok ağzın içip neredeyse kuruttuğu su da dudak kökünün sözüdür: {ar:ماء مشفوة أي مطلوب مسؤول وهو الذي كثر عليه الناس وأنفدوه إلا أقله, tr:mâun meşfûh ey matlûbun mes'ûl, gloss:çok aranan ve istenen su ki insanlar üstüne üşüşüp azı dışında tüketmişlerdir, source:"ش ف ه,B003"}. İçeriye ise yemek girer. On dördüncü ayetin {ar:إِطْعَٰمٌۭ, tr:it'âm, gloss:doyurmak, source:90:14} kelimesi önce tatmaktır: {ar:الطعم ذوقه والطعام اسم جامع لكل ما يؤكل, tr:et-ta'mu zevkuh ve't-taâmu ismun câmi'un li-kulli mâ yu'kel, gloss:tat onun tadılmasıdır ve taam yenen her şeyin adıdır, source:"ط ع م,B001"}. Fiil iki kişi arasında işler: {ar:استطعمه سأله أن يطعمه وأطعمته الطعام, tr:istat'amehû seelehû en yut'imeh ve et'amtuhu't-taâm, gloss:ondan doyurmasını istedi ve ben ona yemek yedirdim, source:"ط ع م,B002"}. Biri ister, öbürü verir. Dil burada iki yönü birleştirir: {ar:استطعمني فلان الحديث إذا أرادك على أن تحدثه, tr:istat'amenî fulânun'l-hadîs, gloss:biri benden sözü tatmak istedi yani konuşmamı istedi, source:"ط ع م,B003"}. Söz de doyurulan bir şeydir. Kök bir yakınlık sahnesi de bilir: {ar:التطاعم إدخال الفم في الفم كما يفعل الحمام عند التقبيل, tr:et-tetâ'umu idhâlu'l-femi fi'l-fem, gloss:tetâum güvercinlerin öpüşürken yaptığı gibi ağzı ağza koymaktır, source:"ط ع م,B013"}. On üçüncü ayetin "fekk"i iki çenenin açılışını anlatır: {ar:فككت الشيء فانفك ككتاب مختوم تفك خاتمه وكما تفك الحنكين تفصل بينهما, tr:fekektu'ş-şey'e fe'nfekke ke-kitâbin mahtûm tefukku hâtemeh ve kemâ tefukku'l-hanekeyn, gloss:şeyi açtım ve açıldı; mühürlü bir mektubun mührünü açtığın ya da iki çeneyi birbirinden ayırdığın gibi, source:"ف ك ك,B001"}. Ters yüzü de vardır: {ar:أخذ فلان بمطعمة فلان إذا أخذ بحلقه يعصره, tr:ehaze fulânun bi-mat'ameti fulân izâ ehaze bi-halkıhî ya'suruh, gloss:birinin yemek yerinden tuttu yani boğazını tutup sıktı, source:"ط ع م,B012"}. Altıncı ayetin kökü sofralarda itişen adamı da adlandırır: {ar:يقال للمزاحم على الموائد المتهالك, tr:yukâlu li'l-muzâhimi ale'l-mevâid el-mutehâlik, gloss:sofralarda itişene mutehâlik denir, source:"ه ل ك,B012"}.

Surenin ağızla ilgili işleyişi buradan görünür. Altıncı ayette ağızdan övünme çıkar. On dördüncü ayette istenen şey başka ağızlara yemek koymaktır. Dil ve dudak doğru yöne çevrildiğinde ağız, boğazı sıkılan yoksulun ağzına doğru açılır.

Kur'an bedenin aynı çerçevesini başka bir yemin suresinde kurar: {ar:لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِىٓ أَحْسَنِ تَقْوِيمٍۢ, tr:lekad halaknâ'l-insâne fî ahseni takvîm, gloss:andolsun insanı en güzel biçimde yarattık, source:95:4}. Söz kalıbı dördüncü ayetle aynıdır, yalnız "kebed"in yerinde dik ve düzgün kuruluş vardır. Allah insanı annelerin karnından çıkardığını ve ona organlar verdiğini de söyler: {ar:وَٱللَّهُ أَخْرَجَكُم مِّنۢ بُطُونِ أُمَّهَٰتِكُمْ لَا تَعْلَمُونَ شَيْـًۭٔا, tr:vallâhu ahracekum min butûni ummehâtikum lâ ta'lemûne şey'â, gloss:Allah sizi hiçbir şey bilmezken annelerinizin karınlarından çıkardı, source:16:78}. İnsanın çıktığı su da terâib ile anılır: {ar:يَخْرُجُ مِنۢ بَيْنِ ٱلصُّلْبِ وَٱلتَّرَآئِبِ, tr:yahrucu min beyni's-sulbi ve't-terâib, gloss:bel ile göğüs kemikleri arasından çıkar, source:86:7}. Verilen organlar bir gün sahiplerine karşı konuşur: {ar:يَوْمَ تَشْهَدُ عَلَيْهِمْ أَلْسِنَتُهُمْ وَأَيْدِيهِمْ وَأَرْجُلُهُم, tr:yevme teşhedu aleyhim elsinetuhum ve eydîhim ve erculuhum, gloss:dillerinin ve ellerinin ve ayaklarının onlar aleyhine tanıklık edeceği gün, source:24:24}. Başka bir yerde de ağız mühürlenir: {ar:ٱلْيَوْمَ نَخْتِمُ عَلَىٰٓ أَفْوَٰهِهِمْ, tr:el-yevme nahtimu alâ efvâhihim, gloss:bugün ağızlarını mühürleriz, source:36:65}. Övünen ağız kapanır, el konuşur. Dilin düğümü de Kur'an'da bir duadır. Musa {ar:وَٱحْلُلْ عُقْدَةًۭ مِّن لِّسَانِى, tr:vahlul ukdeten min lisânî, gloss:dilimden düğümü çöz, source:20:27} ve {ar:يَفْقَهُوا۟ قَوْلِى, tr:yefkahû kavlî, gloss:sözümü anlasınlar, source:20:28} der. İkinci ayetin "hıll"i ile aynı kökten bir fiil, dil ve söz bir arada durur. İbrahim de yaratmayı, yol göstermeyi ve doyurmayı tek bir itirafta toplar: {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:ellezî halakanî fe-huve yehdîn, gloss:beni yaratan ve bana yol gösteren O'dur, source:26:78} ve {ar:وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ, tr:vellezî huve yut'imunî ve yeskîn, gloss:beni yediren ve içiren O'dur, source:26:79}. Bu sıra surenin dördüncü, onuncu ve on dördüncü ayetleridir. Ağzın iki işi Kur'an'da birlikte de emredilir. Mirası paylaşırken yakınlar, yetimler ve yoksullar hazır bulunduğunda {ar:فَٱرْزُقُوهُم مِّنْهُ وَقُولُوا۟ لَهُمْ قَوْلًۭا مَّعْرُوفًۭا, tr:ferzukûhum minhu ve kûlû lehum kavlen ma'rûfâ, gloss:ondan onları rızıklandırın ve onlara güzel söz söyleyin, source:4:8}. Bir başka ölçü de verilir: {ar:قَوْلٌۭ مَّعْرُوفٌۭ وَمَغْفِرَةٌ خَيْرٌۭ مِّن صَدَقَةٍۢ يَتْبَعُهَآ أَذًۭى, tr:kavlun ma'rûfun ve mağfiretun hayrun min sadakatin yetbe'uhâ ezâ, gloss:güzel bir söz ve bağışlama ardından eziyet gelen sadakadan daha hayırlıdır, source:2:263}. Ters yüz de anılır: yetimlerin mallarını haksız yere yiyenler {ar:إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا, tr:innemâ ye'kulûne fî butûnihim nârâ, gloss:karınlarına ancak ateş yerler, source:4:10}. Yoksulun yemeğine teşvik etmeyen adamın orada {ar:وَلَا طَعَامٌ إِلَّا مِنْ غِسْلِينٍۢ, tr:ve lâ taâmun illâ min ğıslîn, gloss:irinden başka yemeği de yoktur, source:69:36}.

Kaynaklar: 90:4 كَبَدٍ ك ب د B001, B009; 90:4 خَلَقْنَا خ ل ق B003; 90:8 عَيْنَيْنِ ع ي ن B001; 90:9 وَلِسَانًۭا ل س ن B001; 90:9 وَشَفَتَيْنِ ش ف ه B002, B003; 90:13 فَكُّ ف ك ك B001, B004; 90:13 رَقَبَةٍ ر ق ب B004; 90:1 ٱلْبَلَدِ ب ل د B002; 90:16 مَتْرَبَةٍۢ ت ر ب B005; 90:18 ٱلْمَيْمَنَةِ ي م ن B002; 90:6 يَقُولُ ق و ل B002; 90:6 أَهْلَكْتُ ه ل ك B012; 90:14 إِطْعَٰمٌۭ ط ع م B001, B002, B003, B012, B013

## Buluşmalar

Görüntülerin en sık buluştuğu sahne yoldur. Onuncu ayetteki "necd" yolu kendi kendine yol gösterir, ateşin kökü de yüksek yerde yol gösterilsin diye yakılan ateşi anlatır. Sırt ile işaret ateşi aynı işi görür: gece yolcusuna nereye çıkacağını göstermek. Musa'nın sahnesi bu iki görüntüyü tek bir ayette taşır: dağın yanında görülen ateş ve {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ev ecidu ale'n-nâri hudâ, gloss:ya da ateşin başında bir yol gösterici bulurum, source:20:10} umudu. Bu surede ise yolun sonundaki ateş bir işaret değildir, üstü kapatılmıştır. Yol sahnesiyle ateş sahnesi arasındaki fark, bir yolculuğun nasıl tersine döndüğünü gösterir. Atılmayan geçidin karşısında, içine dalınan bir ateş vardır: {ar:هَٰذَا فَوْجٌۭ مُّقْتَحِمٌۭ مَّعَكُمْ, tr:hâzâ fevcun muktehimun meakum, gloss:bu sizinle birlikte içeri dalan bir kalabalıktır, source:38:59}. Sabrın kökü de bu iki sahne arasında ikiye bölünür. Yokuşta kendini panikten tutan sabır vardır. Bir de kitabı gizleyenlerin {ar:فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ, tr:fe-mâ asberahum ale'n-nâr, gloss:ateşe karşı ne kadar dayanıklılar, source:2:175} sözündeki ateşe cüret vardır.

İkinci büyük buluşma boyunla kapak arasındadır. On üçüncü ayetin fiili Arapçada kapalıyı açmak olarak tanımlanır: {ar:فكاك الرهن وهو فتحه من الانغلاق, tr:fikâku'r-rahni ve huve fethuhû mine'l-inğılâk, gloss:rehnin fikâkı onu kapalılıktan açmaktır, source:"ف ك ك,B002"}. Yirminci ayetin fiili de kapamak olarak tanımlanır: {ar:أوصدت الباب أغلقته, tr:evsadtu'l-bâbe ağlaktuh, gloss:kapıyı kapattım yani kilitledim, source:"و ص د,B001"}. Sure açılan bir boyundan kapanan bir ateşe doğru ilerler, ve iki fiil birbirinin tam tersidir. Bu iki ucu Kur'an'da tek bir sahne birleştirir. Kitabı sol eline verilen adamın boynu bağlanır ve bunun sebebi yoksulun yemeğine teşvik etmemesidir: {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ taâmi'l-miskîn, gloss:ve yoksulun yemeğine teşvik etmiyordu, source:69:34}. Sol taraf, boyundaki halka ve doyurulmayan yoksul bir aradadır. Malının bir işe yaramadığını söyleyen ve gücünün yok olup gittiğini gören de aynı adamdır. Bu sahnede sağ ile sol, harcanan mal, kıtlık ve boyun görüntüleri aynı yerde durur. Altıncı ayetteki "tükettim" orada şu söze döner: {ar:هَلَكَ عَنِّى سُلْطَٰنِيَهْ, tr:heleke annî sultâniyeh, gloss:gücüm benden yok olup gitti, source:69:29}.

Üçüncü buluşma yeminle geçit arasındadır. Yeminin kefareti ayeti, surenin on üçüncü ve on dördüncü ayetlerini birlikte sayar. Yeminler düğümlenir, sonra on yoksul doyurulur ya da bir boyun çözülür. Birinci ayetin yemini, ikinci ayetin "hıll"i, geçidin iki işi, on sekizinci ayetin sağ eli ve on dokuzuncu ayetin örtme kökü, bir yeminin bağlanıp çözülmesinin bütün aşamalarını taşır. Kur'an'ın bahçe sahipleri ise yemini ters yönde kullanır: yoksulu dışarıda bırakmak için yemin ederler. Bu ikisinin karşı karşıya gelmesi, surenin açılış yemininin neye açıldığını gösterir. Bu yemin bir şehirle başlar, şehirdeki yoksulun ağzıyla devam eder.

Gözetleyen göz ile harcanan mal, gösteriş kelimesinde buluşur. Gösteriş için harcayan, insanların görmesini ister ama Allah'ın görmediğini sanır. Bu çelişki tek bir ayette sahnelenir: malını {ar:رِئَآءَ ٱلنَّاسِ, tr:riâe'n-nâs, gloss:insanlara gösteriş için, source:2:264} harcayanın emeği kayanın üstündeki toprak gibi yıkanır gider. Aynı misal yere yapışma görüntüsünü de taşır: toprak, kaya ve yağmurla çıplak kalan taş. Ölçme görüntüsü de aynı ayete girer: {ar:لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟, tr:lâ yakdirûne alâ şey'in mimmâ kesebû, gloss:kazandıklarından hiçbir şeye güç yetiremezler, source:2:264}. "Kimse bana güç yetiremez" sanısı, kendi kazancına güç yetirememekle biter. Ölçme ile yol da Kur'an'da tek bir dizide buluşur, ve bu dizi surenin sırasıdır: yaratan, ölçen, yol gösteren.

Soy ile kıtlık "yetim" kelimesinde buluşur. Babasından kopan çocuk, iyiliğin geç ulaştığı ve açlık gününde açlık çeken çocuktur. Dil bu ikisini tek bir örnekte birleştirir: {ar:يتيم ذو مسغبة أي ذو مجاعة, tr:yetîmun zû mesğabe ey zû mecâa, gloss:açlık sahibi yetim yani kıtlık içindeki yetim, source:"س غ ب,B001"}. Şehir ile kıtlık da kıtlık yılının tanımında buluşur: yıl bedevileri şehirlere atar. Kur'an'da doyurulan şehrin sahnesi de buradadır: {ar:ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ, tr:ellezî at'amehum min cû'in ve âmenehum min havf, gloss:onları açlıktan doyuran ve korkudan güvenliğe kavuşturan, source:106:4}. Yere yapışma ile geçit, yükselme ile saplanmanın aynı ayette karşı karşıya geldiği sahnede buluşur: ayetlerle yükseltilebilecekken yere saplanan adam. Bu da on dokuzuncu ayetin ayetleri inkâr edenlerine bağlanır.

Bütün bu görüntüler birlikte surenin hareketini taşır. Hareket yere oturmuş bir şehirde başlar. İnsan zorluğun ortasında yaratılmıştır. Malı keçeleşmiştir, kendini görülmez ve ölçülmez sanır. Ona gözler, dil ve dudaklar verilmiş, önüne görünen iki sırt konmuştur. İstenen şey yukarıya atılmaktır. Bu atılış da yere yapışmış olana eğilmek, bir boynun düğümünü çözmek ve aç bir ağza yemek koymaktır. Böyle atılanlar bitkiler gibi birbirine bitişir, aynı rahimden çıkmış gibi birbirine acır ve sağ tarafa yerleşir. Ayetleri örtenlerin üstü ise, yolda yol gösterebilecek bir ateşle kapatılır. Mağara sahnesindeki eşikte köpek ön ayaklarını uzatmış yatar: {ar:وَكَلْبُهُم بَٰسِطٌۭ ذِرَاعَيْهِ بِٱلْوَصِيدِ, tr:ve kelbuhum bâsitun zirâ'ayhi bi'l-vasîd, gloss:köpekleri iki ön ayağını eşiğe uzatmıştı, source:18:18}. Aynı ayette uyuyanlar sağa ve sola çevrilir. Yirminci ayetin kökü, sağ ve sol ile o eşiği orada tek bir sahnede bir araya getirir.

