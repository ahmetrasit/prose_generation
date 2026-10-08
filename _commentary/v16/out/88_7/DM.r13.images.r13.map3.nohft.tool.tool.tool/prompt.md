Focus: 88:7. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_7/D.r13/context.md =====
# 88:7 — focus

لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ

Anchor translation (canonical reading, reference only):

O ne besler ne de açlığı giderir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | لَّا | لَا |  | NEG |
| 2 | يُسْمِنُ | يُسْمِنُ | س م ن | V |
| 3 | وَلَا | لَا |  | CONJ;NEG |
| 4 | يُغْنِى | أَغْنَتْ | غ ن ي | V |
| 5 | مِن | مِن |  | P |
| 6 | جُوعٍ | جُوع | ج و ع | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 88 — full text (context; no pericope)

- 88:1 هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ
- 88:2 وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ
- 88:3 عَامِلَةٌۭ نَّاصِبَةٌۭ
- 88:4 تَصْلَىٰ نَارًا حَامِيَةًۭ
- 88:5 تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ
- 88:6 لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ
- 88:7 ◀ focus لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ
- 88:8 وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ
- 88:9 لِّسَعْيِهَا رَاضِيَةٌۭ
- 88:10 فِى جَنَّةٍ عَالِيَةٍۢ
- 88:11 لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ
- 88:12 فِيهَا عَيْنٌۭ جَارِيَةٌۭ
- 88:13 فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ
- 88:14 وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ
- 88:15 وَنَمَارِقُ مَصْفُوفَةٌۭ
- 88:16 وَزَرَابِىُّ مَبْثُوثَةٌ
- 88:17 أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ
- 88:18 وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ
- 88:19 وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ
- 88:20 وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ
- 88:21 فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
- 88:22 لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- 88:23 إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- 88:24 فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- 88:25 إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 88:26 ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/work/88_7/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## س م ن (root_000744) — identity root of يُسْمِنُ (w2)

- **B001** şişmanlık ve şişmanlaştırma — şişmanlık · şişmanlamak · şişman · şişmanlaştırma · kadınlara kilo aldıran ilaç · onu şişman bulmak ya da saymak · şişman bir şeyi satın almak, edinmek ya da başkasına vermek
  السمن نقيض الهزال (ayn;tahdhib;mufradat)؛ خلاف الضمر والهزال (maqayis)؛ السمين خلاف المهزول (sihah)؛ أسمنته وسمنته جعلته سمينا (mufradat)؛ السمنة دواء تسمن به النساء (ayn;sihah;tahdhib;mufradat)
- **B002** arıtılmış tereyağı ve kullanımları — arıtılmış tereyağı · yemeğe arıtılmış tereyağı katmak ya da onunla karıştırmak · topluluğa arıtılmış tereyağı azığı vermek · arıtılmış tereyağının armağan edilmesini istemek · arıtılmış tereyağı satıcısı
  والسمن من هذا (maqayis)؛ السمن سلاء اللبن (ayn;tahdhib)؛ السمن للبقر وقد يكون للمعزى (sihah)؛ سمنت الطعام إذا جعلت فيه السمن (tahdhib)؛ سمنت لهم الطعام إذا لتته بالسمن (sihah)؛ سمنت القوم تسمينا زودتهم السمن (sihah;tahdhib)؛ جاءوا يستسمنون أي يطلبون أن يوهب لهم السمن (sihah;tahdhib)؛ السمان بائع السمن (sihah)
- **B003** soğutma — bir şeyi soğutmak · soğutma
  سمنت الشيء إذا بردته (maqayis)؛ التسمين التبريد (maqayis;tahdhib)؛ سمنها أي بردها (maqayis;sihah;tahdhib)
- **B004** tavuk yavrusuna benzeyen, kimliği tartışmalı kuş — tavuk yavrusuna benzeyen, başka bir kuşla da özdeşleştirilen kuş
  السمانى طائر شبه الفروجة الواحدة سماناة وقيل إنه السلوى (ayn)؛ السماني طائر ولا يقال سمانى بالتشديد (sihah)؛ السمانى طائر وبعضهم يقول إنه السلوى (tahdhib)؛ السمانى طائر (mufradat)
- **B005** Hindistanlı tarihsel inanç topluluğu — Hindistanlı, ayrı inançlı ve kaynaklarda materyalist ya da putperest diye nitelenen topluluk
  السمنية قوم من أهل الهند لهم دين على حدة دهريون (ayn)؛ السمنية فرقة من عبدة الاصنام تقول بالتناسخ (sihah)؛ السمنية قوم من الهند دهريون (tahdhib)
- **B006** bezeme boyaları — bezeme boyaları
  السمان هذه الأصباغ التي يزخرف بها (ayn)
- **B007** kasaba ya da çöldeki yer adı — bir kasabanın ya da çöldeki bir yerin adı
  سمنان بلدة (ayn)؛ سمنان موضع في البادية (tahdhib)
- **B008** fazlayı geri vererek ortaklık paylarını denkleştirme — fazla pay alanın eksik kalana geri vererek ortaklık paylarını denkleştirmesi
  التسمين أن تقسم شيئا بين الشركاء فيكون في الأنصباء فضل لبعضهما على بعض فيرد كل من في يده فضل على الذي خسر نصيبه (ayn)
- **B009** eskimiş bel örtüleri — eskimiş bel örtüleri
  الأسمال والأسمان الأزر الخلقان (tahdhib)
- **B010** sahip olmadığı iyilik ve saygınlıkla övünme — kendilerinde bulunmayan iyilik ve saygınlıkla övünmek ya da seçkinlere yetişmek için mal biriktirmek
  يتسمنون أي يتكثرون بما ليس فيهم من الخير ويدعون ما ليس لهم من الشرف (tahdhib)؛ وقيل معناه جمعهم المال ليلحقوا بذوي الشرف (tahdhib)؛ باب كثرة الأكل وما يذم منه (tahdhib)

## غ ن ي (root_001110) — identity root of يُغْنِى (w4)

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

## ج و ع (root_000278) — identity root of جُوعٍ (w6)

- **B001** midenin boş kalmasından doğan açlık — açlık · acıkmak · aç kimse · aç kadın · çok aç kimse · aç kadın · aç kimseler · açlar · bir kez açlık çekme · sürekli aç görünen ya da sık sık azar azar yiyen kimse
  الجوع ضد الشبع (maqayis;jamhara;sihah)؛ الجوع اسم جامع للمخمصة (ayn)؛ الجوع اسم للمخمصة (tahdhib)؛ الألم الذي ينال الحيوان من خلو المعدة من الطعام (mufradat)؛ الجوعة المرة من الجوع (jamhara;sihah;tahdhib)؛ المستجيع الذي يأكل كل ساعة الشيء بعد الشيء (tahdhib)
- **B002** yaygın açlık dönemi — yaygın açlık dönemi · açlık yılı
  عام مجاعة ومجوعة (maqayis;sihah)؛ المجاعة عام فيه جوع (ayn;tahdhib)؛ المجاعة عبارة عن زمان الجدب (mufradat)
- **B003** aç bırakma ya da bilerek aç kalma — onu aç bıraktı · onu aç bıraktı · başkasını aç bırakma · birini aç bırakma · bilerek aç kalmak · sağaltım için doyuncaya kadar yememek
  أجعته وجوعته فجاع يجوع (ayn;tahdhib)؛ المتعدي الإجاعة والتجويع (ayn)؛ أجاعه وجوعه (sihah)؛ تجوع أي تعمد الجوع (sihah)؛ تجوع للدواء أي لا تستوف الطعام (tahdhib)
- **B004** yapıya göre özlem, kap boşluğu ya da karın inceliği [kalıp] — seninle buluşmayı çok özledim · kabı dolu değil · karnı ince kadın
  جعت إلى لقائك وعطشت إلى لقائك؛ جائع القدر إذا لم تكن قدره ملأى؛ امرأة جائعة الوشاح إذا كانت ضامرة البطن

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:7, and ## Buluşmalar) =====
## Emek, ücret ve sayım

Üçüncü ayetteki ilk sıfat amaçlı yapılan iştir: {ar:كل فعل يكون من الحيوان بقصد, tr:küllü fi'lin yekûnu mine'l-hayevâni bi-kasd, gloss:canlıdan kasıtla çıkan her iş, source:"ع م ل,B001"}. Böyle bir iş karşılığında ücret beklenir: {ar:العمالة أجر ما عمل, tr:el-umâletü ecru mâ amel, gloss:umâle yapılan işin ücretidir, source:"ع م ل,B004"}. İkinci sıfatın kökü ise hem yorgunluğu hem de pay almayı anlatır: {ar:النصيب الحظ من الشيء, tr:en-nasîbu'l-hazzu mine'ş-şey', gloss:nasip bir şeyden düşen paydır, source:"ن ص ب,B005"}. Ayetteki anlam yorgunluktur. Yanında ise payın kendisi duyulur. Bu yüz çalışmış ve yorulmuştur, ama eline geçen tek şey yorgunluktur. Yedinci ayet bu kazancın neye yaradığını söyler: {ar:الغناء بالفتح الكفاية ولا يغني أي لا يكفي, tr:el-ğanâu bi'l-feth el-kifâye ve lâ yuğnî ey lâ yekfî, gloss:ğanâ yeterliliktir; lâ yuğnî yetmez demektir, source:"غ ن ي,B002"}.

Dokuzuncu ayet karşı tarafı tek bir kelimeyle kurar: {ar:لِّسَعْيِهَا رَاضِيَةٌۭ, tr:li-sa'yihâ râdiye, gloss:çabasından hoşnut, source:88:9}. Çaba, kazanç getiren iştir: {ar:كل عمل من خير أو شر فهو السعي؛ السعي العمل أي الكسب, tr:küllü amelin min hayrin ev şerrin fe-huve's-sa'y; es-sa'yu'l-amel ey el-kesb, gloss:iyi ya da kötü her iş sa'ydir; sa'y kazançtır, source:"س ع ي,B002"}. Hoşnutluk iki yönlüdür: {ar:ورضا العبد عن الله ورضا الله عن العبد, tr:ve rıda'l-abdi anillâhi ve rıdallâhi ani'l-abd, gloss:kulun Allah'tan ve Allah'ın kuldan razı olması, source:"ر ض و,B001"}. Bu yüz dönüp kendi emeğine bakar ve gördüğünden memnun kalır. Öteki yüzün emeği ise üstünde yorgunluk olarak kalmıştır.

On birinci ayetteki kelimenin bir başka kolu, hesaba geçmeyen şeyi anlatır: {ar:ألغيت هذه الكلمة أي رأيتها باطلا وفضلا وحشوا وما يلغى من الحساب, tr:elğaytü hâzihi'l-kelimete ey raeytühâ bâtılen ve fadlen ve haşven ve mâ yulğâ mine'l-hısâb, gloss:bu sözü boş ve fazlalık saydım; hesaptan düşülen şey, source:"ل غ و,B001"}. Yirmi altıncı ayet de bir sayımla kapanır: {ar:الحساب عدك الأشياء, tr:el-hısâbu addüke'l-eşyâ', gloss:hesap şeyleri tek tek saymandır, source:"ح س ب,B001"}. Bahçede boş söz işitilmez. Hesapta da boş olan sayılmaz. Sayım ise surenin sonunda yalnızca "Bize" aittir.

Kur'an emeğin hesabını açıkça anlatır. Musa'nın ve İbrahim'in sayfalarında bulunduğu bildirilen sözler arasında şunlar vardır: {ar:وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ, tr:ve en leyse li'l-insâni illâ mâ seâ, gloss:insan için çabaladığından başkası yoktur, source:53:39}; {ar:وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ, tr:ve enne sa'yehû sevfe yurâ, gloss:çabası görülecektir, source:53:40}; {ar:ثُمَّ يُجْزَىٰهُ ٱلْجَزَآءَ ٱلْأَوْفَىٰ, tr:summe yuczâhu'l-cezâe'l-evfâ, gloss:sonra karşılığı tam olarak verilecektir, source:53:41}. Ahireti isteyip onun için çabalayanların çabası {ar:فَأُو۟لَٰٓئِكَ كَانَ سَعْيُهُم مَّشْكُورًۭا, tr:fe-ülâike kâne sa'yuhum meşkûrâ, gloss:işte onların çabası karşılık görür, source:17:19} diye anılır. Bahçe halkına, gümüş kaplarla ve kadehlerle ağırlandıktan sonra şöyle denir: {ar:وَكَانَ سَعْيُكُم مَّشْكُورًا, tr:ve kâne sa'yukum meşkûrâ, gloss:çabanız karşılık gördü, source:76:22}. Büyük felaket geldiğinde çaba yeniden hatırlanır: {ar:يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ, tr:yevme yetezekkeru'l-insânu mâ seâ, gloss:insanın çabaladığı şeyi hatırlayacağı gün, source:79:35}. Boşa giden emek için ise şöyle denir: {ar:فَجَعَلْنَٰهُ هَبَآءًۭ مَّنثُورًا, tr:fe-cealnâhu hebâen mensûrâ, gloss:onu dağılmış toza çevirdik, source:25:23}. Başka bir yerde de {ar:ٱلَّذِينَ ضَلَّ سَعْيُهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا وَهُمْ يَحْسَبُونَ أَنَّهُمْ يُحْسِنُونَ صُنْعًا, tr:ellezîne dalle sa'yuhum fi'l-hayâti'd-dünyâ ve hum yahsebûne ennehum yuhsinûne sun'â, gloss:dünya hayatında çabaları boşa gidip de güzel iş yaptıklarını sananlar, source:18:104} diye anlatılırlar. Buradaki "sanmak" fiili hesap ile aynı köktendir. Bu insanlar yanlış saymıştır.

Bu sahnelerin en yakını, kitabı sağından verilen kişinin sevincidir: {ar:إِنِّى ظَنَنتُ أَنِّى مُلَٰقٍ حِسَابِيَهْ, tr:innî zanentu ennî mulâkin hısâbiyeh, gloss:hesabıma kavuşacağımı zaten biliyordum, source:69:20}. Ardından surenin dokuzuncu ve onuncu ayetlerindeki sözler gelir: {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:artık o hoşnut bir yaşayıştadır, source:69:21}; {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüce bir bahçede, source:69:22}. Kitabı solundan verilen ise {ar:وَلَمْ أَدْرِ مَا حِسَابِيَهْ, tr:ve lem edri mâ hısâbiyeh, gloss:keşke hesabımın ne olduğunu bilmeseydim, source:69:26} der. Teraziler tartıldığında ağır gelen de {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:o hoşnut bir yaşayıştadır, source:101:7} diye anılır. Hesap kökü yetecek kadar vermeyi de anlatır: {ar:عطاء حسابا أي كافيا, tr:atâen hısâben ey kâfiyen, gloss:yeterli bir bağış, source:"ح س ب,B003"}. Kur'an bunu takva sahiplerinin karşılığı için söyler: {ar:جَزَآءًۭ مِّن رَّبِّكَ عَطَآءً حِسَابًۭا, tr:cezâen min rabbike atâen hısâbâ, gloss:Rabbinden bir karşılık; yeterli bir bağış, source:78:36}. Birinin emeği "yetmez" diye biter. Ötekinin karşılığı "yeter" diye verilir.

Kaynaklar: 88:3 عَامِلَةٌ ع م ل B001; 88:3 عَامِلَةٌ ع م ل B004; 88:3 نَّاصِبَةٌ ن ص ب B004; 88:3 نَّاصِبَةٌ ن ص ب B005; 88:7 يُغْنِى غ ن ي B002; 88:9 لِّسَعْيِهَا س ع ي B002; 88:9 رَاضِيَةٌ ر ض و B001; 88:11 لَٰغِيَةً ل غ و B001; 88:26 حِسَابَهُم ح س ب B001; 88:26 حِسَابَهُم ح س ب B003

## Doyurmayan yemek

Altıncı ayet önce kesin bir yokluk bildirir, sonra tek bir istisna koyar: {ar:لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ, tr:leyse lehum taâmun illâ min darî', gloss:onlar için darî'den başka yemek yoktur, source:88:6}. Yedinci ayet bu istisnanın da yemeğin iki işinden hiçbirini görmediğini söyler: {ar:لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ, tr:lâ yusminu ve lâ yuğnî min cû', gloss:ne besler ne de açlığı giderir, source:88:7}. Yemek iki iş görür: bedeni doldurur ve eksikliği giderir. ضريع bu ikisini de yapmaz. Ayrıca adı bu iki eksikliği de taşır.

ضريع kuruyunca bu adı alan dikenli bir bitkidir: {ar:الضريع يبيس الشبرق وهو نبت, tr:ed-darîu yebîsu'ş-şibrik ve huve nebt, gloss:darî' kurumuş şibriktir; bir bitkidir, source:"ض ر ع,B005"}; {ar:الضريع نبت يقال له الشبرق وأهل الحجاز يسمونه الضريع إذا يبس, tr:ed-darîu nebtun yukâlü lehu'ş-şibriku ve ehlü'l-Hicâzi yüsemmûnehu'd-darîa izâ yebis, gloss:şibrik denen bitki; Hicaz halkı kuruyunca ona darî' der, source:"ض ر ع,B005"}; {ar:قيل هو يبيس الشبرق وقيل نبات أحمر منتن الريح, tr:kîle huve yebîsu'ş-şibriki ve kîle nebâtun ahmeru müntinü'r-rîh, gloss:kurumuş şibrik ya da kırmızı ve pis kokulu bir bitki, source:"ض ر ع,B005"}. Aynı harfler zayıflamış bedeni de anlatır: {ar:لضارع الجسم أي نحيف ضعيف, tr:le-dâriu'l-cism ey nahîfun daîf, gloss:bedeni zayıf ve cılız, source:"ض ر ع,B003"}. Yoksulluğu da anlatır: {ar:مظهرين الضراعة وهي شدة الفقر إلى الشيء والحاجة إليه, tr:muzhirîne'd-darâata ve hiye şiddetü'l-fakri ile'ş-şey'i ve'l-hâceti ileyh, gloss:bir şeye şiddetli yoksulluk ve muhtaçlık, source:"ض ر ع,B002"}. İki karşılık da yedinci ayetteki iki olumsuzluğun karşısına düşer. Besleme kelimesi semizliktir ve zayıflığın karşıtıdır: {ar:السمن نقيض الهزال, tr:es-simenu nakîdu'l-hüzâl, gloss:semizlik zayıflığın zıddıdır, source:"س م ن,B001"}. Gidermek kelimesi ise zenginlik ve ihtiyaçsızlıktır: {ar:عدم الحاجات وقلة الحاجات وكثرة القنيات, tr:ademü'l-hâcâti ve kılletü'l-hâcâti ve kesretü'l-kınyât, gloss:ihtiyaçların yokluğu ya da azlığı ve malın çokluğu, source:"غ ن ي,B001"}. Yemeğin adı yokluğu söyler, ayet de yemeğin yokluğu gidermediğini. Açlık bile yemeğin yokluğuyla tanımlanır: {ar:الألم الذي ينال الحيوان من خلو المعدة من الطعام, tr:el-elemu'llezî yenâlü'l-hayevâne min hulüvvi'l-mideti mine't-taâm, gloss:midenin yemekten boş kalmasıyla canlıya gelen acı, source:"ج و ع,B001"}. Böylece yedinci ayetin son kelimesi, altıncı ayetin yemek kelimesine geri bağlanır. Arapçada iyi beslenen adam için {ar:رجل طاعم حسن الحال, tr:racülün tâimun hasenü'l-hâl, gloss:doymuş adam hali iyi adamdır, source:"ط ع م,B004"} denir. Bunlar ise doyuramayan bir yemekle baş başa kalmıştır.

Aynı harfler bir de yan anlamda duyulur. Darî, memesi büyük koyuna da verilen addır: {ar:شاة ضريع وضريعة عظيمة الضرع, tr:şâtun darîun ve darîatun azîmetü'd-dar', gloss:memesi iri koyun, source:"ض ر ع,B001"}. Kelime ayette kuru dikendir. Yanında ise sütle dolu bir meme duyulur, yani bu yemeğin hiç taşımadığı bolluk. Kökün bir başka kolu, yemeğin içecek olarak da gelebileceğini gösterir: {ar:الضريع الشراب الرقيق, tr:ed-darîu'ş-şerâbü'r-rakîk, gloss:darî' sulu ince içecek, source:"ض ر ع,B011"}.

Kur'an bu yapıyı başka bir sahnede de kurar. Kitabı solundan verilen kişi için şöyle denir: {ar:فَلَيْسَ لَهُ ٱلْيَوْمَ هَٰهُنَا حَمِيمٌۭ, tr:fe-leyse lehü'l-yevme hâhunâ hamîm, gloss:bugün burada onun için yakın bir dost yoktur, source:69:35}; {ar:وَلَا طَعَامٌ إِلَّا مِنْ غِسْلِينٍۢ, tr:ve lâ taâmun illâ min ğıslîn, gloss:irin dışında bir yemek de yoktur, source:69:36}; {ar:لَّا يَأْكُلُهُۥٓ إِلَّا ٱلْخَٰطِـُٔونَ, tr:lâ ye'kuluhû ille'l-hâtiûn, gloss:onu suçlulardan başkası yemez, source:69:37}. Burada da yokluk ve istisna aynı sırayla gelir. Zakkum ağacı için ise {ar:فَإِنَّهُمْ لَءَاكِلُونَ مِنْهَا فَمَالِـُٔونَ مِنْهَا ٱلْبُطُونَ, tr:fe-innehum le-âkilûne minhâ fe-mâliûne minhe'l-butûn, gloss:ondan yiyip karınlarını dolduracaklar, source:37:66} denir. Karın dolar, ama yedinci ayetteki gibi beden beslenmez. Kur'an başka yerde boğazda kalan yemekten söz eder: {ar:وَطَعَامًۭا ذَا غُصَّةٍۢ وَعَذَابًا أَلِيمًۭا, tr:ve taâmen zâ ğussatin ve azâben elîmâ, gloss:boğazda kalan bir yemek ve acı bir azap, source:73:13}. Yalanlayıcıların gönderildiği gölge de aynı fiille anlatılır: {ar:لَّا ظَلِيلٍۢ وَلَا يُغْنِى مِنَ ٱللَّهَبِ, tr:lâ zalîlin ve lâ yuğnî mine'l-leheb, gloss:ne gölgelendirir ne de alevden korur, source:77:31}. Bu gölge gölge değildir, o yemek de yemek değildir.

Karşı resim de Kur'an'dadır. Allah, Beyt'in Rabbine kulluğa çağırdığı bir topluluğa şunu hatırlatır: {ar:ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ, tr:ellezî at'amehum min cûin ve âmenehum min havf, gloss:onları açlıktan doyuran ve korkudan güvene erdiren, source:106:4}. Buradaki "açlıktan" sözü yedinci ayettekiyle aynıdır. Allah bahçede Âdem'e {ar:إِنَّ لَكَ أَلَّا تَجُوعَ فِيهَا وَلَا تَعْرَىٰ, tr:inne leke ellâ tecûa fîhâ ve lâ ta'râ, gloss:burada acıkmaman ve çıplak kalmaman senin içindir, source:20:118} der. İbrahim de beşinci ve altıncı ayetlerin iki fiilini Rabbine bağlar: {ar:وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ, tr:vellezî huve yut'imunî ve yeskîn, gloss:beni doyuran ve bana içiren O'dur, source:26:79}.

Kaynaklar: 88:6 لَّيْسَ ل ي س B001; 88:6 طَعَامٌ ط ع م B004; 88:6 ضَرِيعٍ ض ر ع B001; 88:6 ضَرِيعٍ ض ر ع B002; 88:6 ضَرِيعٍ ض ر ع B003; 88:6 ضَرِيعٍ ض ر ع B005; 88:6 ضَرِيعٍ ض ر ع B011; 88:7 يُسْمِنُ س م ن B001; 88:7 يُغْنِى غ ن ي B001; 88:7 جُوعٍ ج و ع B001

## Deve: sürü, süt ve yolculuk

Bakılacak dört şeyin ilki devedir. Gök, dağlar ve yer uzaktadır. Deve ise insanın yanındadır, insan onun üstündedir. Arapçada deve bir servettir: {ar:الإبل معروفة ورجل آبل ومال مؤبل, tr:el-ibilu ma'rûfetun ve racülün âbilün ve mâlün muebbel, gloss:deve bilinir; develi adam ve deveden oluşan mal, source:"ء ب ل,B001"}. Kökün bir kolu devenin suya muhtaç kalmadan yaşı otla yetinmesini anlatır: {ar:أبلت الإبل والوحش اجتزأت بالرطب عن الماء, tr:ebeleti'l-ibilu ve'l-vahşu'ctezeet bi'r-ratbi ani'l-mâ', gloss:develer ve yaban hayvanları sudan vazgeçip yaş otla yetindi, source:"ء ب ل,B002"}. Altıncı ve yedinci ayetlerde hiçbir şeyin yetmediği insanlar vardır. On yedinci ayette ise azla yetinen bir hayvana bakılması istenir.

Surenin önceki kelimelerinde de devenin bedeni yan anlam olarak duyulur. Nâime'nin kökü sürüye ad verir: {ar:النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم, tr:en-neamu'l-ibilu limâ fîhi mine'l-hayri ve'n-ni'meti ve'l-en'âmu'l-behâim, gloss:neam devedir; içindeki hayır ve nimetten dolayı; en'âm hayvanlardır, source:"ن ع م,B005"}. Hâşia, yorgun düşmüş bir devenin hörgücünü anlatır: {ar:خشع سنام البعير إذا أنضي فذهب شحمه وتطأطأ شرفه, tr:haşaa senâmü'l-baîri izâ undiye fe-zehebe şahmuhû ve teta'tae şerefuh, gloss:yorulan devenin hörgücünün yağı gidip tepesi çöktü, source:"خ ش ع,B004"}. Âmile, çalışmaya yatkın soylu dişi deveye ad verir: {ar:اليعملة الناقة النجيبة المطبوعة على العمل, tr:el-ya'meletü'n-nâkatü'n-necîbetü'l-matbûatu ale'l-amel, gloss:çalışmaya yaratılışça yatkın soylu dişi deve, source:"ع م ل,B008"}. Ateşe girme fiilinin kökü bir bitkiye de ad verir: {ar:تسميها العرب خبزة الإبل, tr:tüsemmîhe'l-arabu hubzete'l-ibil, gloss:Araplar ona develerin ekmeği der, source:"ص ل ي,B010"}. Yemek, yağ ve deve tek bir cümlede birleşir: {ar:المطعم من الإبل الذي يوجد في مخه طعم الشحم وشاة طعوم فيها بعض السمن, tr:el-mut'imu mine'l-ibili'llezî yûcedu fî muhhihî ta'mu'ş-şahm ve şâtun taûmun fîhâ ba'du's-simen, gloss:iliğinde yağ tadı bulunan deve; biraz semizliği olan koyun, source:"ط ع م,B007"}. Mevdûa'nın kökü tuzlu otlakta yayılan develeri anlatır: {ar:الواضعات الإبل تأكل الخلة, tr:el-vâdiâtü'l-ibilu te'kulu'l-hulle, gloss:vâdiât hulle otunu yiyen develerdir, source:"و ض ع,B007"}. Masfûfe ise kurban için sıraya dizilen develeri anlatır: {ar:البدن الصواف التي تصفف ثم تنحر, tr:el-budnü's-savâffu'lletî tusaffefu summe tunhar, gloss:sıraya dizilip sonra kesilen kurbanlık develer, source:"ص ف ف,B001"}. Kur'an aynı kelimeyi kurbanlık develer için kullanır: {ar:فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ, tr:fezkurusmallâhi aleyhâ savâff, gloss:sıraya dizilmişken üzerlerine Allah'ın adını anın, source:22:36}. O ayette sıra, anma ve doyurma bir aradadır. Ayet ardından {ar:وَأَطْعِمُوا۟ ٱلْقَانِعَ وَٱلْمُعْتَرَّ, tr:ve at'imu'l-kânia ve'l-mu'terr, gloss:yetineni ve isteyeni doyurun, source:22:36} der.

Süt de aynı kelimelerden geçer. Darî'in kökü memedir: {ar:الضرع لكل ذات خف أو ظلف, tr:ed-dar'u li-külli zâti huffin ev zılf, gloss:dar' tabanlı ve tırnaklı her hayvanın memesidir, source:"ض ر ع,B001"}. Merfûa'nın kökü sütünü memesinde tutan deveye ad verir: {ar:ناقة رافع إذا رفعت اللبأ في ضرعها, tr:nâkatun râfiun izâ rafeati'l-lebee fî dar'ihâ, gloss:ağız sütünü memesinde tutan dişi deveye râfi' denir, source:"ر ف ع,B007"}. Masfûfe'nin kökü tek sağımda kadehleri sıra sıra dolduran deveye ad verir: {ar:ناقة صفوف للتي تصف أقداحا من لبنها, tr:nâkatun safûfun li'lletî tesuffu akdâhan min lebenihâ, gloss:sütünden kadehleri sıra sıra dolduran dişi deve, source:"ص ف ف,B002"}. On dördüncü ayetteki kevb de böyle bir kadehtir. Besleme kelimesinin kökü sütten çıkan yağa ad verir: {ar:السمن سلاء اللبن, tr:es-semnu sulâü'l-leben, gloss:semn sütten eritilen yağdır, source:"س م ن,B002"}. Sulamanın kökü ise hem su hem süt taşıyan kırbayı anlatır: {ar:السقاء القربة للماء واللبن, tr:es-sikâü'l-kırbetü li'l-mâi ve'l-leben, gloss:su ve süt için kırba, source:"س ق ي,B004"}. Kur'an bu içirmeyi bir ibret olarak anlatır: {ar:نُّسْقِيكُم مِّمَّا فِى بُطُونِهِۦ مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:nuskîkum mimmâ fî butûnihî min beyni fersin ve demin lebenen hâlisan sâiğan li'ş-şâribîn, gloss:karınlarındakinden; fışkı ile kan arasından içenlerin boğazından kolayca geçen arı bir süt içiririz, source:16:66}. Buradaki fiil, beşinci ayetteki "içirilir" fiiliyle aynıdır. Kolay yutulan süt, cehennemdeki içeceğin tersidir: {ar:يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ, tr:yetecerrauhû ve lâ yekâdu yusîğuh, gloss:yudum yudum içer ama yutamaz, source:14:17}. "Kolayca geçen" ve "yutamaz" aynı köktendir.

Yolculuk da aynı kelimelerden duyulur. Surenin ilk fiili, yürüyen bir devenin ön ayaklarının salınımını anlatır: {ar:ما أحسن أتو يدي هذه الناقة وأتي أيضا أي رجع يديها في السير, tr:mâ ahsene etve yedey hâzihi'n-nâka ey rac'a yedeyhâ fi's-seyr, gloss:bu devenin ön ayaklarını yürürken geri atışı ne güzel, source:"ء ت ي,B009"}. Son ayetten bir önceki ayetteki dönüş kelimesi de aynı salınımı ve gün boyu yürüyüşü anlatır: {ar:الأوب سرعة تقليب اليدين والرجلين في السير والتأويب أن تسير النهار أجمع وتنزل الليل, tr:el-evbü sur'atü taklîbi'l-yedeyni ve'r-ricleyni fi's-seyr ve't-te'vîbü en tesîra'n-nehâra ecmea ve tenzile'l-leyl, gloss:yürüyüşte el ve ayakları çabuk oynatmak; bütün gün yürüyüp gece konmak, source:"ء و ب,B003"}; {ar:كل راجع مع الليل فهو آئب, tr:küllü râciin mea'l-leyli fe-huve âib, gloss:gece olunca dönen herkes âibdir, source:"ء و ب,B006"}. Aradaki kelimeler de yürüyüşün türlerini adlandırır: {ar:نصب القوم ساروا يومهم وهو سير لين, tr:nasaba'l-kavmu sârû yevmehum ve huve seyrun leyyin, gloss:topluluk bütün gün yumuşak bir yürüyüşle yürüdü, source:"ن ص ب,B010"}; {ar:السعي عدو ليس بشديد, tr:es-sa'yu adven leyse bi-şedîd, gloss:sa'y şiddetli olmayan koşudur, source:"س ع ي,B001"}; {ar:مرفوع الناقة في سيرها خلاف الموضوع, tr:merfûu'n-nâkati fî seyrihâ hılâfu'l-mevdû', gloss:devenin yürüyüşünde merfû mevdûun zıddıdır, source:"ر ف ع,B003"}; {ar:وضع البعير وغيره أي أسرع في سيره, tr:vadaa'l-baîru ve ğayruhû ey esraa fî seyrih, gloss:deve hızlandı, source:"و ض ع,B003"}. Bunlar yan anlamlardır ve ayetlerin anlamının yerine geçmez. Ama surenin "geldi mi" ile başlayıp "dönüşleri" ile biten yolu, deve sürücülerinin bir günlük yürüyüşü anlattığı kelimelerle kurulmuştur.

Kur'an deveyi yaratılmış ve insana boyun eğdirilmiş bir nimet olarak anlatır: {ar:وَٱلْأَنْعَٰمَ خَلَقَهَا ۗ لَكُمْ فِيهَا دِفْءٌۭ وَمَنَٰفِعُ وَمِنْهَا تَأْكُلُونَ, tr:ve'l-en'âme halakahâ lekum fîhâ dif'un ve menâfiu ve minhâ te'kulûn, gloss:hayvanları yarattı; onlarda sizin için ısınma ve faydalar vardır ve onlardan yersiniz, source:16:5}; {ar:وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ, tr:ve tahmilu eskâlekum ilâ beledin lem tekûnû bâliğîhi illâ bi-şıkkı'l-enfus, gloss:ancak canınızı tüketerek varabileceğiniz bir yere yüklerinizi taşırlar, source:16:7}. Başka bir ayette Allah'ın kendi işi anlatılır: {ar:أَوَلَمْ يَرَوْا۟ أَنَّا خَلَقْنَا لَهُم مِّمَّا عَمِلَتْ أَيْدِينَآ أَنْعَٰمًۭا, tr:e-ve-lem yerav ennâ halaknâ lehum mimmâ amilet eydînâ en'âmen, gloss:ellerimizin işinden onlar için hayvanlar yarattığımızı görmediler mi, source:36:71}; {ar:وَذَلَّلْنَٰهَا لَهُمْ فَمِنْهَا رَكُوبُهُمْ وَمِنْهَا يَأْكُلُونَ, tr:ve zellelnâhâ lehum fe-minhâ rakûbuhum ve minhâ ye'kulûn, gloss:onları kendilerine boyun eğdirdik; bir kısmına biner bir kısmından yerler, source:36:72}. Bu ayetteki "iş" kelimesi, üçüncü ayetteki âmile ile aynı köktendir, ama burada iş Allah'ındır. Boyun eğdirme fiili de aşağılanma kelimesiyle aynı köktendir, ama burada bir lütuf olarak hayvana uygulanır. Deve, surenin döşediği odayı da döşer: {ar:وَجَعَلَ لَكُم مِّن جُلُودِ ٱلْأَنْعَٰمِ بُيُوتًۭا, tr:ve ceale lekum min cülûdi'l-en'âmi buyûten, gloss:hayvanların derilerinden size evler yaptı, source:16:80}; {ar:وَمِنْ أَصْوَافِهَا وَأَوْبَارِهَا وَأَشْعَارِهَآ أَثَٰثًۭا وَمَتَٰعًا, tr:ve min asvâfihâ ve evbârihâ ve eş'ârihâ esâsen ve metâan, gloss:yünlerinden yapağılarından ve kıllarından ev eşyası ve kullanılacak şeyler, source:16:80}. Allah İbrahim'e insanları hacca çağırmasını söylerken develer de gelişin aracıdır: {ar:يَأْتُوكَ رِجَالًۭا وَعَلَىٰ كُلِّ ضَامِرٍۢ يَأْتِينَ مِن كُلِّ فَجٍّ عَمِيقٍۢ, tr:ye'tûke ricâlen ve alâ külli dâmirin ye'tîne min külli feccin amîk, gloss:yaya olarak ve her uzak yoldan gelen arık develer üstünde sana gelsinler, source:22:27}. Bakmanın yiyeceğe yöneltildiği yerde de hayvanlar anılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bu bakış {ar:مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ, tr:metâan lekum ve li-en'âmikum, gloss:size ve hayvanlarınıza bir yararlanma olarak, source:80:32} diye biter.

Kaynaklar: 88:1 أَتَىٰكَ ء ت ي B009; 88:2 خَٰشِعَةٌ خ ش ع B004; 88:3 عَامِلَةٌ ع م ل B008; 88:3 نَّاصِبَةٌ ن ص ب B010; 88:4 تَصْلَىٰ ص ل ي B010; 88:5 تُسْقَىٰ س ق ي B004; 88:6 ضَرِيعٍ ض ر ع B001; 88:6 طَعَامٌ ط ع م B007; 88:7 يُسْمِنُ س م ن B002; 88:8 نَّاعِمَةٌ ن ع م B005; 88:9 لِّسَعْيِهَا س ع ي B001; 88:13 مَّرْفُوعَةٌ ر ف ع B003; 88:13 مَّرْفُوعَةٌ ر ف ع B007; 88:14 مَّوْضُوعَةٌ و ض ع B003; 88:14 مَّوْضُوعَةٌ و ض ع B007; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:15 مَصْفُوفَةٌ ص ف ف B002; 88:17 ٱلْإِبِلِ ء ب ل B001; 88:17 ٱلْإِبِلِ ء ب ل B002; 88:25 إِيَابَهُمْ ء و ب B003; 88:25 إِيَابَهُمْ ء و ب B006

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

