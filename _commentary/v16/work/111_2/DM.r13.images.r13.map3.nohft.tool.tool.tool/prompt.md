Focus: 111:2. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/111_2/D.r13/context.md =====
# 111:2 — focus

مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ

Anchor translation (canonical reading, reference only):

Malı ve kazandığı şey ona yarar sağlamadı.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | مَآ | مَا |  | NEG |
| 2 | أَغْنَىٰ | أَغْنَىٰ | غ ن ي | V |
| 3 | عَنْهُ | عَن |  | P;PRON |
| 4 | مَالُهُۥ | مَال | م و ل | N;PRON |
| 5 | وَمَا | مَا |  | CONJ;REL |
| 6 | كَسَبَ | كَسَبَ | ك س ب | V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 111 — full text (context; no pericope)

- 111:1 تَبَّتْ يَدَآ أَبِى لَهَبٍۢ وَتَبَّ
- 111:2 ◀ focus مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ
- 111:3 سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ
- 111:4 وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ
- 111:5 فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ


===== _commentary/v16/work/111_2/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## غ ن ي (root_001110) — identity root of أَغْنَىٰ (w2)

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

## م و ل (root_001457) — identity root of مَالُهُۥ (w4)

- **B001** varlık; edinme, çoğalma ve başkasına kazandırma — kişinin sahip olduğu değerli varlık · kişinin sahip olduğu değerli varlıklar · göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri · varlık sahibi veya çok varlıklı kimse · kendine kalıcı varlık edinmek · varlığı çoğalmak veya varlık sahibi duruma gelmek · birini varlık sahibi yapmak veya ona değerli varlık vermek · mal sözcüğünün küçültme biçimi · ne çok varlığı var!
  تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)
- **B002** örümcek için tartışmalı bir ad — 
  إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)

## ك س ب (root_001296) — identity root of كَسَبَ (w6)

- **B001** kendisi için geçimlik ya da yarar arayıp elde etme — geçimlik ve yarar arayıp elde etme · bir şeyi ya da parayı kendisi için kazanmak · bir şeyi özellikle kendisi için edinmek · kazanç sağlamak için uğraşmak · çok kazanan ya da geçimini arayan kimse · kişinin kazandığı şey ya da kazanç yolu · iyi ve temiz kazanç · para kazanan; ayrıca kurt ya da dişi köpek adı olarak kullanılan biçim
  الكاف والسين والباء أصل صحيح وهو يدل على ابتغاء وطلب وإصابة (maqayis)؛ الكسب طلب الرزق (ayn;sihah;tahdhib)؛ الكسب ما يتحراه الإنسان مما فيه اجتلاب نفع وتحصيل حظ ككسب المال (mufradat)؛ كسبت الشيء واكتسبته (jamhara;sihah)
- **B002** birine para ya da iyilik kazandırma — birine para ya da iyilik kazandırmak
  كسب أهله خيرا (maqayis)؛ كسبت الرجل مالا فكسبه (maqayis;jamhara;sihah)؛ فلان يكسب أهله خيرا (tahdhib)؛ الكسب يقال فيما أخذه لنفسه ولغيره ويتعدى إلى مفعولين (mufradat)
- **B003** bedenin iş gören üyeleri — bedenin iş gören üyeleri
  الكواسب الجوارح (sihah)
- **B004** yağdan çıkan özlü sıkım maddesi — yağdan çıkan özlü sıkım maddesi · aynı yağ sıkım maddesi için kullanılan başka bir ad
  الكُسب الكنجارق ويقال الكسبج (ayn)؛ الكُسب عصارة الدهن (sihah)؛ الكُسب الكنجارق وبعض السواديين يسمونه الكسبج (tahdhib)

===== _commentary/v16/out/s111/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 111:2, and ## Buluşmalar) =====
## Eller: toplayan, kazanan ve kaybeden

Sure bir el sahnesiyle açılır: {ar:تَبَّتْ يَدَآ أَبِى لَهَبٍۢ, tr:tebbet yedâ ebî leheb, gloss:Ebû Leheb'in iki eli kurudu, source:111:1}. İlk fiilin kökü bir kaybı adlandırır ve bu kaybı doğrudan ellere bağlayan bir kullanımı vardır: {ar:تبت يداه تبا وتبابا أي خسرت, tr:tebbet yedâhu tebben ve tebâben, ey hasirat, gloss:elleri kurudu, yani zarara uğradı, source:"ت ب ب,B001"}. Burada iflas önce bir organa, iki ele düşer. Aynı kökün masdarı bir beddua kalıbıdır, {ar:تبا لفلان, tr:tebben li-fulân, gloss:kahrolsun falanca, source:"ت ب ب,B001"}; bu yüzden açılış hem bir bildirim hem de bir lanet olarak işitilir. Kök kesmeyi de adlandırır {source:"ت ب ب,B004"}: kuruyan el aynı zamanda kesilen eldir. Hemen arkasından gelen {ar:وَتَبَّ, tr:ve tebbe, gloss:kendisi de kurudu, source:111:1} aynı fiili bu kez adamın kendisine yükler. Kökün bir başka tanımı, {ar:التب والتباب الاستمرار في الخسران, tr:et-tebbu ve't-tebâbu el-istimrâru fi'l-husrân, gloss:zararda kalıp sürmek, source:"ت ب ب,B001"}, ikinci fiilin işini gösterir: kayıp ellerden bütün kişiye geçer ve orada kalır.

Bu sure boyunca bir kelimenin kök ailesinden gelen imgeler, kelimenin ayetteki anlamının yerine değil yanında duyulur. Ayet iki eli söyler; elin kökünün taşıdığı öbür anlamlar bu elin arkasından işitilir. El vurulabilen, kesilebilen bir organdır: {ar:يديت الرجل إذا ضربت يده, tr:yedeytu'r-racule izâ darabtu yedehu, gloss:adamın eline vurdum, source:"ي د ي,B001"}. El güçtür: {ar:اليد القوة, tr:el-yedu el-kuvve, gloss:el, güçtür, source:"ي د ي,B002"}. Elde olan, sahip olunandır: {ar:هذا الشيء في يدي أي في ملكي, tr:hâze'ş-şey'u fî yedî, ey fî milkî, gloss:bu şey elimde, yani mülkümde, source:"ي د ي,B004"}. Ve el kazanılanın ve hesabı verilecek olanın faili olarak anılır: {ar:ذلك بما كسبت يداك, tr:zâlike bimâ kesebet yedâk, gloss:bu, ellerinin kazandığı yüzündendir, source:"ي د ي,B009"}. İkili sayı, yani "iki el", bu yüzden adamın kudretini, mülkünü ve kazancını birlikte tutar; kurutulan şey bütün bu tutuştur.

İkinci ayet ellerin ne tuttuğunu söyler ve onu boşa çıkarır: {ar:مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ, tr:mâ ağnâ anhu mâluhû ve mâ keseb, gloss:ne malı ona fayda verdi ne de kazandığı, source:111:2}. Fiil, bir şeyin birini karşılaması, ona yetmesi demektir: {ar:أغناني كذا وأغنى عنه كذا إذا كفاه, tr:ağnânî kezâ ve ağnâ anhu kezâ izâ kefâhu, gloss:şu bana yetti, şu ondan yana yetti, source:"غ ن ي,B002"}. Fakat aynı kök zenginliğin kendi adıdır, {ar:الغنى في المال, tr:el-ğınâ fi'l-mâl, gloss:zenginlik malda olur, source:"غ ن ي,B001"}. Böylece olumsuzlanan fiil zenginliğin kendi işini inkâr eder: malı onu zengin etmedi, ona yetmedi. Mal, eldeki birikmiş varlıktır; Arapların durumunda sürüdür: {ar:كانت أموال العرب أنعامهم, tr:kânet emvâlü'l-Arabi en'âmehum, gloss:Arapların malları hayvanlarıydı, source:"م و ل,B001"}. Kazanmak ise rızkı arayıp kendine çekmektir, {ar:الكسب طلب الرزق, tr:el-kesbu talebu'r-rızk, gloss:kazanç, rızık aramaktır, source:"ك س ب,B001"}. Ve bu kökün bir kullanımı daireyi kapatır: {ar:الكواسب الجوارح, tr:el-kevâsibu el-cevârih, gloss:kazananlar, uzuvlardır, source:"ك س ب,B003"}. Kazanan şey uzuvların kendisidir; ikinci ayetin kazancı birinci ayetin ellerine döner. Adam ellerini toplamak için uzattı; topladığı şey, aynı ellere düşen kaybın önüne geçmedi.

Kur'an el ile kazancı aynı kalıpta defalarca birleştirir: {ar:بِمَا كَسَبَتْ أَيْدِى ٱلنَّاسِ, tr:bimâ kesebet eydi'n-nâs, gloss:insanların ellerinin kazandığı yüzünden, source:30:41} ve {ar:فَبِمَا كَسَبَتْ أَيْدِيكُمْ, tr:febimâ kesebet eydîkum, gloss:ellerinizin kazandığı yüzünden, source:42:30}. Allah, kitabı kendi elleriyle yazıp "bu Allah katındandır" diyerek az bir bedele satanlar için el ile kazancı aynı lanetin altında toplar: {ar:فَوَيْلٌۭ لَّهُم مِّمَّا كَتَبَتْ أَيْدِيهِمْ وَوَيْلٌۭ لَّهُم مِّمَّا يَكْسِبُونَ, tr:fe-veylün lehum mimmâ ketebet eydîhim ve veylün lehum mimmâ yeksibûn, gloss:ellerinin yazdığından ötürü vay hâllerine, kazandıklarından ötürü vay hâllerine, source:2:79}. Allah hakkında bilgisiz tartışan ve insanları yoldan çıkarmak için böbürlenen kişiden söz eden pasaj {source:22:8}, ona dünyada rüsvaylık ve kıyamet günü yangın azabı tattırılacağını söyler {source:22:9} ve sonra ona şöyle denir: {ar:ذَٰلِكَ بِمَا قَدَّمَتْ يَدَاكَ, tr:zâlike bimâ kaddemet yedâk, gloss:bu, iki elinin önden gönderdiği yüzündendir, source:22:10}. Aynı ikili sayı uyarının gününde de geçer: {ar:يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ, tr:yevme yenzuru'l-mer'u mâ kaddemet yedâh, gloss:kişinin iki elinin önden gönderdiğine bakacağı gün, source:78:40}.

İkinci ayetin cümlesi Kur'an'da kaybedenin kendi ağzından da duyulur. Kitabı sol eline verilen kişi {source:69:25} şöyle der: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ, tr:mâ ağnâ annî mâliyeh, gloss:malım bana fayda vermedi, source:69:28}, ve hemen ardından {ar:هَلَكَ عَنِّى سُلْطَٰنِيَهْ, tr:heleke annî sultâniyeh, gloss:gücüm benden yok olup gitti, source:69:29}. Mal ile güç, yani surenin malı ile iki eli, orada da birlikte elden çıkar. Cimrilik edip kendini müstağni sanan kişiyi anlatan pasajda, {ar:وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ, tr:ve emmâ men bahile vestağnâ, gloss:cimrilik edip kendini yeterli sayana gelince, source:92:8}, kendini yeterli sayma fiili de aynı kökten gelir; birkaç ayet sonra surenin cümlesi neredeyse kelimesi kelimesine gelir: {ar:وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ, tr:ve mâ yuğnî anhu mâluhû izâ teraddâ, gloss:yuvarlanıp düştüğünde malı ona fayda vermez, source:92:11}. Kendini malıyla yeterli sayan, düştüğü anda malının ona yetmediğini görür. Helak edilmiş kavimler için aynı ikili sabit bir sıra hâlinde tekrarlanır, {ar:فَمَآ أَغْنَىٰ عَنْهُم مَّا كَانُوا۟ يَكْسِبُونَ, tr:fe-mâ ağnâ anhum mâ kânû yeksibûn, gloss:kazandıkları onlara fayda vermedi, source:15:84}; bir yerde de cehennemin önlerinde durduğu söylenerek: {ar:وَلَا يُغْنِى عَنْهُم مَّا كَسَبُوا۟ شَيْـًۭٔا, tr:ve lâ yuğnî anhum mâ kesebû şey'â, gloss:kazandıkları onlara hiçbir fayda vermez, source:45:10}. Fayda vermemek ile tebâb bir ayette birleşir; Allah helak edilen kentler için der ki ilahları onlara fayda vermedi ve {ar:وَمَا زَادُوهُمْ غَيْرَ تَتْبِيبٍۢ, tr:ve mâ zâdûhum ğayra tetbîb, gloss:onlara kayıptan başka bir şey katmadılar, source:11:101}. Kule yapılmasını buyuran Firavun'un {source:40:36} tasarısı da aynı kelimeyle biter: {ar:وَمَا كَيْدُ فِرْعَوْنَ إِلَّا فِى تَبَابٍۢ, tr:ve mâ keydu Fir'avne illâ fî tebâb, gloss:Firavun'un düzeni kayıptan başka bir yere varmadı, source:40:37}. İkinci ayetin reddettiği beklenti ise, mal toplayıp sayan dedikoducunun zannında açıkça söylenir: {ar:يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ, tr:yahsebu enne mâlehû ahledeh, gloss:malının kendisini ölümsüz kıldığını sanır, source:104:3}. Bağı yıkılan bahçe sahibinin sahnesi de el ile harcanan malı aynı jestte toplar: {ar:فَأَصْبَحَ يُقَلِّبُ كَفَّيْهِ عَلَىٰ مَآ أَنفَقَ فِيهَا, tr:fe-asbaha yukallibu keffeyhi alâ mâ enfeka fîhâ, gloss:oraya harcadıkları için avuçlarını ovuşturur oldu, source:18:42}. Ve ellere yöneltilmiş beddua kalıbı, Allah'ın elinin bağlı olduğunu söyleyenlere verilen cevapta aynı dilbilgisiyle geçer: {ar:غُلَّتْ أَيْدِيهِمْ وَلُعِنُوا۟, tr:ğullet eydîhim ve lu'inû, gloss:elleri bağlansın ve lanetlendiler, source:5:64}.

Kaynaklar: 111:1 تَبَّتْ ت ب ب B001; 111:1 تَبَّتْ ت ب ب B004; 111:1 وَتَبَّ ت ب ب B001; 111:1 يَدَآ ي د ي B001; 111:1 يَدَآ ي د ي B002; 111:1 يَدَآ ي د ي B004; 111:1 يَدَآ ي د ي B009; 111:2 أَغْنَىٰ غ ن ي B001; 111:2 أَغْنَىٰ غ ن ي B002; 111:2 مَالُهُۥ م و ل B001; 111:2 كَسَبَ ك س ب B001; 111:2 كَسَبَ ك س ب B003

## Ev ocağı ve soy: tersine dönen hane

Bir ev; ailesi için kazanan bir erkek, bir eş, evlenmede ya da ev kurulurken verilen bir ziyafet, ev için toplanan odun ve et kızartılan, başında ısınılan bir ocakla döner. Surenin kelimeleri bu ev sahnesinin bütün parçalarını kökleriyle taşır. Kazanmak, ailesi için hayır kazanmaktır: {ar:فلان يكسب أهله خيرا, tr:fulânun yeksibu ehlehû hayran, gloss:falanca ailesine hayır kazandırır, source:"ك س ب,B002"}. Baba, besleyendir: {ar:فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده, tr:fulânun ye'bû hâze'l-yetîme ibâveten, ey yağzûhu kemâ yağzu'l-vâlidu veledeh, gloss:falanca bu yetime babalık eder, yani babanın çocuğunu beslediği gibi onu besler, source:"ء ب و,B001"}. Dördüncü ayetin ilk kelimesi eştir, {ar:هي امرأته, tr:hiye'mraetuh, gloss:o, onun karısıdır, source:"م ر ء,B001"}, ve kökü evin kuruluşundaki ziyafeti adlandırır: {ar:والمرء : الإطعام على بناء دار ، أو تزويج, tr:ve'l-mer'u el-it'âmu alâ binâi dârin ev tezvîc, gloss:mer', ev yapımında ya da evlenmede yemek vermektir, source:"م ر ء,B004"}. İkinci ayetin fiilinin kökü evliliği de adlandırır, {ar:الغنى التزويج, tr:el-ğınâ et-tezvîc, gloss:ğınâ, evlendirmedir, source:"غ ن ي,B006"}, ve kocasıyla yetinen kadını: {ar:الغانية المستغنية بزوجها عن الزينة, tr:el-ğâniye el-mustağniye bi-zevcihâ ani'z-zîne, gloss:ğâniye, kocası sayesinde süse ihtiyaç duymayan kadındır, source:"غ ن ي,B005"}. Odun kökü birisi için odun toplamayı bilir, {ar:حطبت فلانا إذا احتطبت له, tr:hatabtu fulânen izehtatabtu leh, gloss:falancaya odun topladım, source:"ح ط ب,B001"}, ve üçüncü ayetin fiili ocağın kendisidir: ısınılan ve kızartılan ateş {source:"ص ل ي,B004"}.

Surede bu ev bütünüyle tersine döner. Kazanan erkeğin kazancı kendine bile yetmez; ikinci ayetin fiili, kocası karısına yeten evliliğin kökünden gelir ama burada koca kendini bile karşılayamaz. Eş, kocasının içinde yanacağı ateşe odun taşır; ev ocağı Ateş olur. Bu ters çevrilmenin karşı sahnesi Kur'an'da Mûsâ'dadır. Süresini doldurup ailesiyle yola çıkan Mûsâ, Tûr'un yanında bir ateş görür ve ailesine şöyle der: {ar:لَعَلِّىٓ ءَاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ جَذْوَةٍۢ مِّنَ ٱلنَّارِ لَعَلَّكُمْ تَصْطَلُونَ, tr:lealî âtîkum minhâ bi-haberin ev cezvetin mine'n-nâri lealekum tastalûn, gloss:belki oradan size bir haber ya da bir ateş koru getiririm, belki ısınırsınız, source:28:29}; aynı söz başka bir yerde {ar:بِشِهَابٍۢ قَبَسٍۢ, tr:bi-şihâbin kabes, gloss:alınmış bir ateş parçasıyla, source:27:7} diye geçer {source:20:10}. Orada "ısınmak" fiili surenin "yanmak" fiiliyle aynı köktendir: bir koca ailesini ısıtmak için ateş getirir; burada bir eş, kocasının yanacağı ateşe odun taşır. Müminlere hitap eden ayet, insanın kendini ve ailesini yakıtı insanlar olan bir ateşten korumasını ister: {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا, tr:kû enfusekum ve ehlîkum nârâ, gloss:kendinizi ve ailenizi bir ateşten koruyun, source:66:6}. Kitabı arkasından verilen kişi için {source:84:10} yanmak, ailesi içindeki eski sevincin karşısına konur: {ar:وَيَصْلَىٰ سَعِيرًا إِنَّهُۥ كَانَ فِىٓ أَهْلِهِۦ مَسْرُورًا, tr:ve yaslâ seîran innehû kâne fî ehlihî mesrûrâ, gloss:alevli ateşe girer; çünkü o ailesi içinde sevinçliydi, source:84:12}. Allah'ın inkâr edenlere örnek verdiği Nûh'un ve Lût'un karılarında eş, fayda vermeme fiili ve Ateş bir araya gelir: {ar:فَلَمْ يُغْنِيَا عَنْهُمَا مِنَ ٱللَّهِ شَيْـًۭٔا وَقِيلَ ٱدْخُلَا ٱلنَّارَ مَعَ ٱلدَّٰخِلِينَ, tr:felem yuğniyâ anhumâ mina'llâhi şey'en ve kîle'dhulâ'n-nâra mea'd-dâhilîn, gloss:kocaları onlara Allah'a karşı hiçbir fayda vermedi ve onlara "girenlerle birlikte ateşe girin" denildi, source:66:10}. Hemen ardından Firavun'un karısı, kocasından ve onun işinden kurtarılmayı dileyen bir eş olarak gelir {source:66:11}: evlilik orada kaderi paylaştırmaz. Surede ise eş ve koca aynı ateşin iki ucundadır.

Dördüncü ve beşinci ayetin iki kelimesi bu evin bir başka parçasını, soyu da işitir. Taşımak, kökünde hamileliktir: {ar:حملت المرأة حبلت, tr:hamelet'il-mer'etu hebilet, gloss:kadın gebe kaldı, source:"ح م ل,B002"}, {ar:الحمل ما كان في بطن, tr:el-hamlu mâ kâne fî batn, gloss:haml, karında olandır, source:"ح م ل,B002"}. İp de kökünde aynı şeydir: {ar:الحبل الحمل وقد حبلت المرأة فهي حبلى, tr:el-habelu el-hamlu ve kad hebileti'l-mer'etu fe-hiye hublâ, gloss:habel gebeliktir; kadın gebe kaldı, o hâmiledir, source:"ح ب ل,B006"}. Bir tanım, iki kelimeyi birbiriyle açıklar ve gebeliğin ipe benzerliğini günlerin onunla uzamasında görür: {ar:الحبل وهو الحمل وذلك أن الأيام تمتد به, tr:el-habelu ve huve'l-hamlu ve zâlike enne'l-eyyâme temteddu bih, gloss:habel gebeliktir, çünkü günler onunla uzar, source:"ح ب ل,B006"}. Kadının iki ayetindeki iki kelime, onun taşıyacağı soyun kelimeleridir; oysa sahnede taşıdığı odun, boynundaki iptir. Birinci ayetin baba kelimesi bu soyun öbür ucunu tutar {source:"ء ب و,B001"}. Kur'an, ikinci ayetin cümlesini başka yerlerde malın yanına evladı koyarak kurar: {ar:مَن لَّمْ يَزِدْهُ مَالُهُۥ وَوَلَدُهُۥٓ إِلَّا خَسَارًۭا, tr:men lem yezidhu mâluhû ve veleduhû illâ hasârâ, gloss:malı ve evladı kendisine kayıptan başka bir şey katmayan, source:71:21}. Bu, Nûh'un kavminin kendisine isyan edip izledikleri önderlerden yakınmasıdır; "kayıp" kelimesi de tebâbın tanımında geçen kelimedir. İbrâhîm'in duasında o gün {ar:يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ, tr:yevme lâ yenfau mâlun ve lâ benûn, gloss:ne malın ne oğulların fayda vereceği gün, source:26:88} diye anılır. Mal ile evladın onlara fayda vermediği ve onların ateşin ehli olduğu ayette {source:58:17} ve yukarıda geçen ayette {source:3:10} bu ikili ikinci ve üçüncü ayetin sırasını kurar. Surede ikinci sırada "kazandığı" durur; o yerde evladı duymak bir okumadır, kelimenin söylediği değil. Suçlunun o gün kurtulmak için fidye olarak vermek isteyeceği şeyler de bu evin halkıdır: {ar:بِبَنِيهِ وَصَٰحِبَتِهِۦ وَأَخِيهِ, tr:bi-benîhi ve sâhibetihî ve ehîh, gloss:oğulları, eşi ve kardeşiyle, source:70:12}.

Kaynaklar: 111:1 أَبِى ء ب و B001; 111:2 كَسَبَ ك س ب B002; 111:2 أَغْنَىٰ غ ن ي B006; 111:2 أَغْنَىٰ غ ن ي B005; 111:3 سَيَصْلَىٰ ص ل ي B004; 111:4 وَٱمْرَأَتُهُۥ م ر ء B001; 111:4 وَٱمْرَأَتُهُۥ م ر ء B004; 111:4 ٱلْحَطَبِ ح ط ب B001; 111:4 حَمَّالَةَ ح م ل B002; 111:5 حَبْلٌۭ ح ب ل B006

## Boyundaki ip: gerdanlıktan tasmaya

Beşinci ayet ipi boynun belirli bir yerine koyar: {ar:فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ, tr:fî cîdihâ hablun min mesed, gloss:boynunda bükülmüş liften bir ip, source:111:5}. Cîd, boynun ön yüzüdür, {ar:الجيد مقدم العنق, tr:el-cîdu mukaddemu'l-unuk, gloss:cîd, boynun önüdür, source:"ج ي د,B001"}, ve övgüyle anılan, uzunluğu ve güzelliği söylenen boyundur: {ar:امرأة جيداء حسنة الجيد إذا كانت طويلة العنق, tr:imraetun caydâu haseneti'l-cîdi izâ kânet tavîlete'l-unuk, gloss:boynu uzun olan kadına "güzel boyunlu" denir, source:"ج ي د,B001"}. Bu, gerdanlığın takıldığı yerdir. İp kökü de gerdanlıktaki bir süs taşını adlandırır: {ar:الحبلة حلي يجعل في القلائد, tr:el-hablatu huliyyun yuc'alu fi'l-kalâid, gloss:habla, gerdanlıklara takılan bir süstür, source:"ح ب ل,B008"}. Süsün kelimesi burada kaba bir ip olarak görünür. Kocası ya da güzelliği sayesinde süse ihtiyaç duymayan kadının adı ikinci ayetin fiilinin kökündendir {source:"غ ن ي,B005"}; surede süse ihtiyaç duymaması gereken boyun bir ip taşır.

Mesed sıkı bükülmüş iptir: {ar:مسدت الحبل أي أجدت فتله, tr:mesedtu'l-habl, ey eceddu fetlehu, gloss:ipi mesedledim, yani iyice büktüm, source:"م س د,B001"}. Aynı kök, sıkı yapılı bir kadının bedenini de bu iple anar: {ar:امرأة ممسودة مجدولة الخلق كالحبل الممسود, tr:imraetun memsûdetun meclûdetu'l-halki ke'l-habli'l-memsûd, gloss:bükülmüş ip gibi sıkı yapılı kadın, source:"م س د,B002"}. Kadın ile boynundaki ip tek bir kelimeyi paylaşır. Kök demirden bir mili de bilir: {ar:المسد المحور إذا كان من حديد, tr:el-mesedu el-mihveru izâ kâne min hadîd, gloss:mesed, demirden olduğunda mil, source:"م س د,B005"}. Kelime liften demire uzanır. İpin boyunda yaptığı iş de kökte kayıtlıdır: yular hayvanı yerinde tutar ve götürür {source:"ح ب ل,B001"}, ve bağlanmış gibi yerinden ayrılamayan kişi ipin adıyla anılır, ölüm de bu adı alır: {ar:للواقف مكانه لا يفر حبيل براح كأنه محبول, tr:li'l-vâkıfi mekânehû lâ yefirru habîlu berâh, keennehû mahbûl, gloss:yerinde durup kaçmayana "habîlu berâh" denir, sanki bağlanmıştır, source:"ح ب ل,B012"}. İpin altında boynun kendi ipi vardır: {ar:حبل الوريد عرق في العنق, tr:hablu'l-verîd ırkun fi'l-unuk, gloss:şah damarı boyundaki bir damardır, source:"ح ب ل,B004"}. Kur'an bu ipi Allah'ın yakınlığının ölçüsü yapar: {ar:وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ, tr:ve nahnu akrabu ileyhi min habli'l-verîd, gloss:biz ona şah damarından daha yakınız, source:50:16}.

Kur'an'da boyuna konan şey, insanın sahip olduğunun ya da yaptığının boyuna dönüşmüş hâlidir. Cimriler için: {ar:سَيُطَوَّقُونَ مَا بَخِلُوا۟ بِهِۦ يَوْمَ ٱلْقِيَٰمَةِ, tr:se-yutavvakûne mâ bahilû bihî yevme'l-kıyâme, gloss:cimrilik ettikleri şey kıyamet günü boyunlarına dolanacak, source:3:180}; esirgenen mal bir boyun halkası olur ve gelecek eki üçüncü ayetin fiilindekiyle aynıdır. Allah'ın talimatı eli boyna bağlar: {ar:وَلَا تَجْعَلْ يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:ve lâ tec'al yedeke mağlûleten ilâ unukik, gloss:elini boynuna bağlı kılma, source:17:29}. Her insanın payı boynuna bağlanır: {ar:وَكُلَّ إِنسَٰنٍ أَلْزَمْنَٰهُ طَٰٓئِرَهُۥ فِى عُنُقِهِۦ, tr:ve kulle insânin elzemnâhu tâirahû fî unukıh, gloss:her insanın amelini boynuna bağladık, source:17:13}. Yeniden dirilişi inkâr edenler hakkında {ar:وَأُو۟لَٰٓئِكَ ٱلْأَغْلَٰلُ فِىٓ أَعْنَاقِهِمْ, tr:ve ulâike'l-ağlâlu fî a'nâkıhim, gloss:işte boyunlarında halkalar olanlar onlardır, source:13:5} denir; halka çeneye kadar çıkar ve başı yukarı kaldırır {source:36:8}. Sürüklenme sahnesi halka ile zinciri birlikte gösterir: {ar:إِذِ ٱلْأَغْلَٰلُ فِىٓ أَعْنَٰقِهِمْ وَٱلسَّلَٰسِلُ يُسْحَبُونَ, tr:izi'l-ağlâlu fî a'nâkıhim ve's-selâsilu yushabûn, gloss:boyunlarında halkalar ve zincirlerle sürüklenirken, source:40:71}. Kitabı sol eline verilen kişinin sahnesinde {source:69:25} bağlama ile yakma aynı sırada gelir: {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe-ğullûh, gloss:tutun onu, boynuna halka geçirin, source:69:30}, {ar:ثُمَّ ٱلْجَحِيمَ صَلُّوهُ, tr:summe'l-cahîme sallûh, gloss:sonra onu cehenneme sokup yakın, source:69:31}, {ar:ثُمَّ فِى سِلْسِلَةٍۢ ذَرْعُهَا سَبْعُونَ ذِرَاعًۭا فَٱسْلُكُوهُ, tr:summe fî silsiletin zer'uhâ seb'ûne zirâan feslukûh, gloss:sonra onu yetmiş arşınlık bir zincire geçirin, source:69:32}. Ateş ile bağın yan yana durduğu öbür yerler de vardır: {ar:سَلَٰسِلَا۟ وَأَغْلَٰلًۭا وَسَعِيرًا, tr:selâsile ve ağlâlen ve seîrâ, gloss:zincirler, halkalar ve alevli ateş, source:76:4}; {ar:إِنَّ لَدَيْنَآ أَنكَالًۭا وَجَحِيمًۭا, tr:inne ledeynâ enkâlen ve cahîmâ, gloss:bizim katımızda ağır bukağılar ve cehennem var, source:73:12}. Surede de ateş üçüncü ayette, ip beşinci ayettedir. Boynun karşı sahnesi de Kur'an'dadır: sarp yokuşun ilk adımı {ar:فَكُّ رَقَبَةٍ, tr:fekku rakabe, gloss:bir boynu çözmek, source:90:13}.

Kaynaklar: 111:5 جِيدِهَا ج ي د B001; 111:5 حَبْلٌۭ ح ب ل B008; 111:5 حَبْلٌۭ ح ب ل B001; 111:5 حَبْلٌۭ ح ب ل B012; 111:5 حَبْلٌۭ ح ب ل B004; 111:5 مَّسَدٍۭ م س د B001; 111:5 مَّسَدٍۭ م س د B002; 111:5 مَّسَدٍۭ م س د B005; 111:2 أَغْنَىٰ غ ن ي B005

## Buluşmalar

İlk buluşma birinci ayetin kendisindedir: kuruyan eller, alevle adlandırılmış adama aittir. Alev kökünün surenin ifadesini kendi adlandırma anlamının altında anması {source:"ل ه ب,B006"} iki imgeyi tek bir tamlamada tutar: kaybeden eller ile ateşe giden ad aynı kişinin iki yüzüdür. Elin kaybı ile ateş, ikinci ve üçüncü ayetin sırasında birleşir. Kur'an bu sırayı başka bir surede aynı kelimelerle kurar: önce {ar:وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ, tr:ve mâ yuğnî anhu mâluhû izâ teraddâ, gloss:yuvarlanıp düştüğünde malı ona fayda vermez, source:92:11}, birkaç ayet sonra {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona ancak en bedbaht olan girer, source:92:15}. Fayda vermeme fiili ile alev kelimesi de bir ayette yan yanadır {source:77:31}.

Alev ile yakıt, adın içinde buluşur. Baba kökü besleyeni adlandırır {source:"ء ب و,B001"}, odun ise yakmak için hazırlanan şeydir {source:"ح ط ب,B001"}. Alevin babası alevi besleyen olarak birinci ayette durur, alevin yakıtı dördüncü ayette sırtta taşınır, ve ikisi üçüncü ayetin ateşinde birleşir. Aynı ateş ev ocağıyla da buluşur: yakma fiilinin kökü hem ısınılan ocağı hem Ateşi adlandırır {source:"ص ل ي,B004"}. Mûsâ'nın ailesine getirdiği ateşte {ar:لَعَلَّكُمْ تَصْطَلُونَ, tr:lealekum tastalûn, gloss:belki ısınırsınız, source:27:7} ile surenin {ar:سَيَصْلَىٰ, tr:se-yaslâ, gloss:yanacak, source:111:3} kelimesi aynı kökün iki ucudur. Odun bir de söz odunudur: yakıt olarak taşınan ile laf olarak taşınan aynı kelimedir, ve laf insanlar arasında ateşin kökünden adını alan bir düşmanlık tutuşturur {source:"ن و ر,B007"}. Mal toplayan dedikoducunun tutuşturulmuş ateşe atıldığı sahne {source:104:6} ve savaş için yakılan ateşler {source:5:64} bu iki odunu tek sahnede tutar.

Sırttaki yük ile boyundaki ip, beşinci ayetin ipinde birleşir: yular yük hayvanının boyun ipidir {source:"ح ب ل,B001"}, mesed de deve yününden bükülen iptir {source:"م س د,B001"}. Sırtına yük vurulmuş bir hayvanın boynunda yular vardır; kadının sırtında odun, boynunda ip vardır. Kur'an yük ile süsü bir ayette birleştirir: buzağı olayında İsrailoğulları {ar:حُمِّلْنَآ أَوْزَارًۭا مِّن زِينَةِ ٱلْقَوْمِ, tr:hummilnâ evzâren min zîneti'l-kavm, gloss:kavmin süs eşyasından yükler yüklendik, source:20:87} derler. Süs yük olur; surede gerdanlığın yeri ip taşır. Kazanç ile yük de bir ayette buluşur {source:6:164}: birinci ve ikinci ayetin kazanan elleri ile dördüncü ayetin taşıyan sırtı, kişinin kazandığının kendi yükü oluşunun iki yarısıdır.

El ile boyun, birinci ve beşinci ayet arasında buluşur. Elin boyna bağlanmasını yasaklayan talimat {source:17:29} ve esirgenen malın boyun halkasına dönüşmesi {source:3:180}, surenin iki ucunu tek bir bedende birleştirir: kazanan el ile bağlanan boyun. İp kendi içinde üç sahneyi birden tutar: boyundaki halka, avcının tuzağı ve kesilen bağ. Gece gündüz kurulan düzenin boyunlardaki halkalarla bittiği ayet {source:34:33} halka ile tuzağı, Allah'ın ipine tutunmayı ateş çukurunun kıyısına koyan ayet {source:3:103} bağ ile ateşi birleştirir. Bükümün ipe verdiği güç, birinde birleştirmeye, ötekinde bir boynu bağlamaya gider.

Surenin hareketi bedenin üzerinden ilerler: birinci ayette eller, ikinci ayette ellerin tuttuğu mal ve kazanç, üçüncü ayette bütün bedenin girdiği ateş, dördüncü ayette sırt, beşinci ayette boyun. Adamın kazanan elleri ile kadının taşıyan sırtı aynı ateşe çalışır; biri kazandığının kendisine yetmediğini görür, öteki taşıdığı odunun yandığı yere bağlanır. İlk kelime ellere düşen bir kayıp ve bir kesiştir, son kelime boyna geçen bükülmüş bir ip; arada, adın içinde daha baştan yanan alev durur.

