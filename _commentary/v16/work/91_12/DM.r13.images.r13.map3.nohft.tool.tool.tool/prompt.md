Focus: 91:12. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/91_12/D.r13/context.md =====
# 91:12 — focus

إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا

Anchor translation (canonical reading, reference only):

İçlerindeki en kötü kişi harekete geçtiğinde,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | إِذِ | إِذ |  | T |
| 2 | ٱنۢبَعَثَ | ٱنۢبَعَثَ | ب ع ث | V |
| 3 | أَشْقَىٰهَا | أَشْقَى | ش ق و | N;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 91 — full text (context; no pericope)

- 91:1 وَٱلشَّمْسِ وَضُحَىٰهَا
- 91:2 وَٱلْقَمَرِ إِذَا تَلَىٰهَا
- 91:3 وَٱلنَّهَارِ إِذَا جَلَّىٰهَا
- 91:4 وَٱلَّيْلِ إِذَا يَغْشَىٰهَا
- 91:5 وَٱلسَّمَآءِ وَمَا بَنَىٰهَا
- 91:6 وَٱلْأَرْضِ وَمَا طَحَىٰهَا
- 91:7 وَنَفْسٍۢ وَمَا سَوَّىٰهَا
- 91:8 فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا
- 91:9 قَدْ أَفْلَحَ مَن زَكَّىٰهَا
- 91:10 وَقَدْ خَابَ مَن دَسَّىٰهَا
- 91:11 كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ
- 91:12 ◀ focus إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا
- 91:13 فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا
- 91:14 فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا
- 91:15 وَلَا يَخَافُ عُقْبَٰهَا


===== _commentary/v16/work/91_12/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ب ع ث (root_000129) — identity root of ٱنۢبَعَثَ (w2)

- **B001** durgun olanı harekete geçirme — harekete geçirmek; uyandırmak · devenin bağını çözüp onu ayağa kaldırmak · uyuyanı uyandırmak · kargaşanın kabarmaları ve alevlenmeleri · neredeyse hiç uyumayan adam · neredeyse hiç çökmeyen dişi deve
  الباء والعين والثاء أصل واحد وهو الإثارة (maqayis)؛ بعثت الناقة إذا أثرتها (maqayis;sihah)؛ بعثت البعير أرسلته وحللت عقاله أو كان باركا فهجته (ayn)؛ بعثت البعير فانبعث إذا حللت عقاله وأرسلته لو كان باركا فأثرته (tahdhib)؛ بعثته من نومه فانبعث وبعثت النائم إذا أهببته (sihah;tahdhib)؛ أصل البعث إثارة الشيء وتوجيهه (mufradat)
- **B002** gönderme veya yöneltme — göndermek; yöneltmek · görevle göndermek; yola çıkarmak · birini bir iş için göndermek · birini bir işi yapmaya isteklendirip yöneltmek · asker birliğini düşmana karşı göndermek · göreve gönderilmiş topluluk veya birlik · gönderilmiş ordular
  البعث الإرسال كبعث الله من في القبور (ayn)؛ بعثت الرجل في الحاجة وبعثته على الشيء إذا أرغته أن يفعله (jamhara)؛ ابتعثه بمعنى أي أرسله (sihah)؛ البعث بعث الجند إلى العدو والقوم المبعوثون المشخصون (tahdhib)؛ بعث الإنسان في حاجة وفبعث الله غرابا أي قيضه ولقد بعثنا في كل أمة رسولا نحو أرسلنا رسلنا (mufradat)
- **B004** yola koyulup ilerleme — harekete geçip ilerlemek; hızlanmak · yola koyulma ve ilerleme · şiir benden akıp geldi
  انبعث القوم في الخير والشر انبعاثا إذا تتابعوا (jamhara)؛ انبعث في السير أي أسرع (sihah)؛ كره الله انبعاثهم أي توجههم ومضيهم (mufradat)

## ش ق و (root_000808) — identity root of أَشْقَىٰهَا (w3)

- **B001** mutluluğun karşıtı olan mutsuzluk — mutsuzluk, bahtsızlık · mutsuz, bahtsız kimse · Tanrı onu mutsuzluğa düşürdü
  الشقوة خلاف السعادة (maqayis)؛ الشقاء والشقاوة بالفتح: نقيض السعادة (sihah)؛ الشقاوة: خلاف السعادة، والشقاوة الأخروية والدنيوية (mufradat)
- **B002** güçlük çekme ve zorluğa dayanma — güçlük, sıkıntı ve yorucu uğraş · bu işte yoruldum ve güçlük çektim · zorluğa katlanma, uğraşıp dayanma ve savaşta boğuşma · onunla uğraştım ve güçlüğüne katlandım · o işle uğraşıp güçlüğünü çektim
  أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (maqayis;sihah)؛ الشقاء: الشدة والعسر، وشاقيته أي صابرته، وشاقيت ذلك الأمر بمعنى عانيته، والمشاقاة: المعالجة في الحرب وغيرها (tahdhib)؛ يوضع الشقاء موضع التعب، وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)
- **B003** karşılıklı uğraşta ötekini yenme [kalıp] — benimle çekişti, ben de o işte onu yendim
  شاقاني فلان فشقوته أشقوه، أي غلبته فيه (sihah)
- **B004** uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı — uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı; bu tür dağ sırtları
  الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)

## ECHO ش ق ي (root_000809) — for أَشْقَىٰهَا (w3): withheld observed target; not identity

- **B001** bedbahtlık ve bedbaht duruma düşürme — bedbaht olmak · bedbahtlık · bedbahtlık · bu dünyada veya ölümden sonraki yaşamda bedbahtlık · onu bedbaht duruma düşürmek
  الشقوة خلاف السعادة (maqayis)؛ شقي شقاء وشقوة وأصل الشقاء والشقوة (ayn)؛ الشقاء والشقاوة نقيض السعادة وأشقاه الله (sihah)؛ شقي شقاء وشقاوة وشقوة (tahdhib)؛ الشقاوة خلاف السعادة (mufradat)
- **B002** zorluk ve yorucu uğraş — güçlük, zorluk ve yorucu sıkıntı · bir işte yorulmak veya güçlük çekmek · uğraşma, yaşayarak sürdürme ve katlanma · bir işle uğraşmak ve ona katlanmak
  أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (sihah)؛ الشقاء الشدة والعسر وشاقيت ذلك الأمر بمعنى عانيته (tahdhib)؛ يوضع الشقاء موضع التعب وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)
- **B003** biriyle karşılıklı uğraşıp mücadele etme — biriyle ilişki kurup ona karşı direnmek veya onunla uğraşmak · benimle çekişti, ben de onu o işte yendim
  المشاقاة المعاناة والممارسة (maqayis;sihah)؛ شاقاني فلان فشقوته أي غلبته فيه (sihah)؛ شاقيت فلانا مشاقاة إذا عاشرته وعاشرك (tahdhib)؛ شاقيته أي صابرته والمشاقاة المعالجة في الحرب وغيرها (tahdhib)
- **B004** kolay çıkılan, oturmaya elverişli uzun dağ sırtı — kolay çıkılan ve oturmaya elverişli uzun dağ sırtı
  الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)

===== _commentary/v16/out/s091/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 91:12, and ## Buluşmalar) =====
## Taşkın ve set

Sekizinci ayet nefse iki şey verir: önce bir fışkırma, sonra bir set. Fucûrun kökü suyun dışarı fırlamasını anlatır ve bunu on ikinci ayetin fiiliyle yapar: {ar:وانفجر الماء وغيره انفجارا إذا انبعث سائلا, tr:ve'nfecera'l-mâu ve ğayruhû inficâran izâ inbe'ase sâilen, gloss:su ve benzeri, akarak fırladığında "infecera" denir, source:"ف ج ر,B001"}. Ahlaktaki anlamı da aynı fiille tanımlanır: {ar:الانبعاث والتفتح في المعاصي فجورا, tr:el-inbi'âsu ve't-tefettuhu fi'l-meâsî fucûran, gloss:günaha atılıp açılmaya fucûr denir, source:"ف ج ر,B004"}. Kökün temelinde ise sapma vardır: {ar:كل مائل عن الحق فاجر, tr:kullu mâilin ani'l-hakkı fâcir, gloss:haktan sapan herkes fâcirdir, source:"ف ج ر,B004"}. Takvâ bunun karşısında, iki şeyin arasına konan bir engeldir: {ar:دفع شيء عن شيء بغيره, tr:def'u şey'in an şey'in bi-ğayrih, gloss:bir şeyi başka bir şey araya koyarak bir şeyden uzak tutmak, source:"و ق ي,B001"}. Engelin konduğu yer de bellidir: {ar:التقوى جعل النفس في وقاية مما يخاف, tr:et-takvâ ce'lu'n-nefsi fî vikâyetin mimmâ yuhâf, gloss:takvâ, nefsi korkulan şeye karşı bir siperin içine koymaktır, source:"و ق ي,B002"}; {ar:اتق الله توقه أي اجعل بينك وبينه كالوقاية, tr:ittaki'llâhe tevakkahu, ey ic'al beyneke ve beynehû ke'l-vikâye, gloss:Allah'tan sakın, yani seninle O'nun arasına bir siper gibi bir şey koy, source:"و ق ي,B002"}. Böylece nefse hem bentten taşan su hem de bendin kendisi bildirilir.

On birinci ayet Semûd'un hangi tarafı seçtiğini söyler: {ar:كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ, tr:kezzebet Semûdu bi-tağvâhâ, gloss:Semûd taşkınlığı yüzünden yalanladı, source:91:11}. Tağvâ, sınırı aşmaktır: {ar:مجاوزة الحد في العصيان, tr:mucâvezetu'l-haddi fi'l-isyân, gloss:isyanda sınırı aşmak, source:"ط غ ي,B001"}. Kökün ilk sahnesi ise sudur: {ar:طغى السيل إذا جاء بماء كثير, tr:tağa's-seylu izâ câe bi-mâin kesîr, gloss:sel, bol suyla geldiğinde "tağâ" denir, source:"ط غ ي,B002"}; {ar:طغا البحر والماء إذا علا كل شيء فاجترفه, tr:tağa'l-bahru ve'l-mâu izâ alâ kulle şey'in fe'cterafeh, gloss:deniz ve su her şeyin üstüne çıkıp onu sürükleyip götürdüğünde "tağâ" denir, source:"ط غ ي,B002"}. Kur'an bu fiziksel anlamı Nûh tufanında kullanır: {ar:إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ, tr:innâ lemmâ tağa'l-mâu hamelnâkum fi'l-câriye, gloss:su taştığında sizi akıp giden gemide taşıdık, source:69:11}. On ikinci ayette taşkın bir kişide yüzeye çıkar: {ar:إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا, tr:izi'nbe'ase eşkâhâ, gloss:en bedbahtları atılıp kalktığında, source:91:12}. Fiil bir şeyi harekete geçirip bir yöne sevk etmektir: {ar:أصل البعث إثارة الشيء وتوجيهه, tr:aslu'l-ba'si isâretu'ş-şey'i ve tevcîhuh, gloss:ba'sın aslı, bir şeyi kaldırıp bir yöne yöneltmektir, source:"ب ع ث,B001"}. Ardından başkalarının gelmesini de içerir: {ar:انبعث القوم في الخير والشر انبعاثا إذا تتابعوا, tr:inbe'ase'l-kavmu fi'l-hayri ve'ş-şerri inbi'âsen izâ tetâba'û, gloss:kavim iyilikte ya da kötülükte birbiri ardınca atıldığında "inbe'ase" denir, source:"ب ع ث,B004"}. Sekizinci ayetteki fucûru ve suyun fırlamasını tanımlayan fiil, on ikinci ayette en bedbahtın kalkışıdır. Nefse verilen fışkırma, Semûd'da bir adamın atılışı olur ve kavim onun ardından akar.

Kur'an aynı fiili Allah'ın istemediği bir çıkış için de kullanır. Savaşa çıkmayan münafıklar için şöyle der: {ar:وَلَٰكِن كَرِهَ ٱللَّهُ ٱنۢبِعَاثَهُمْ فَثَبَّطَهُمْ, tr:ve lâkin kerihe'llâhu'nbi'âsehum fe-sebbetahum, gloss:ama Allah onların harekete geçmesini istemedi ve onları alıkoydu, source:9:46}. İnsanın taşma eğilimini de açıkça adlandırır: {ar:بَلْ يُرِيدُ ٱلْإِنسَٰنُ لِيَفْجُرَ أَمَامَهُۥ, tr:bel yurîdu'l-insânu li-yefcura emâmeh, gloss:bilakis insan, önündeki günleri de yarıp taşmak ister, source:75:5}; {ar:كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ, tr:kellâ inne'l-insâne le-yatğâ, gloss:hayır, insan gerçekten taşar, source:96:6}; {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en raâhu'staÄŸnâ, gloss:kendini yeterli gördüğü için, source:96:7}. Nâziât Suresi'nde Allah, Mûsâ'yı taşan birine gönderir ve ona büyüme yolunu teklif ettirir: {ar:ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ, tr:izheb ilâ Fir'avne innehû tağâ, gloss:Firavun'a git, o taştı, source:79:17}; {ar:فَقُلْ هَل لَّكَ إِلَىٰٓ أَن تَزَكَّىٰ, tr:fe-kul hel leke ilâ en tezekkâ, gloss:de ki: arınıp büyümeye ne dersin, source:79:18}. Taşkın ile büyüme orada da karşı karşıya durur. Aynı surede iki sonuç yan yana sayılır: {ar:فَأَمَّا مَن طَغَىٰ, tr:fe-emmâ men tağâ, gloss:taşana gelince, source:79:37}; {ar:وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ, tr:ve emmâ men hâfe makâme rabbihî ve neha'n-nefse ani'l-hevâ, gloss:Rabbinin huzurunda durmaktan korkup nefsi arzudan alıkoyana gelince, source:79:40}. Nefsi alıkoymak, bendin işidir. Salih de Semûd'dan tam olarak bunu ister ve onları taşkınlara uymaktan alıkoymaya çalışır: {ar:فَٱتَّقُوا۟ ٱللَّهَ وَأَطِيعُونِ, tr:fe'ttakullâhe ve etî'ûn, gloss:Allah'tan sakının ve bana uyun, source:26:150}; {ar:وَلَا تُطِيعُوٓا۟ أَمْرَ ٱلْمُسْرِفِينَ, tr:ve lâ tutî'û emra'l-musrifîn, gloss:ölçüyü aşanların buyruğuna uymayın, source:26:151}.

Taşkın sonunda dönüp taşanı alır. Kök, Semûd'un neyle helak olduğunu kendi adıyla söyler: {ar:أهلكوا بالطاغية أي بطغيانهم, tr:uhlikû bi't-tâğıye, ey bi-tuğyânihim, gloss:tâğıye ile helak edildiler, yani kendi taşkınlıklarıyla, source:"ط غ ي,B004"}. Kur'an'daki karşılığı da aynı kelimedir: {ar:فَأَمَّا ثَمُودُ فَأُهْلِكُوا۟ بِٱلطَّاغِيَةِ, tr:fe-emmâ Semûdu fe-uhlikû bi't-tâğıye, gloss:Semûd'a gelince, o taşkın şeyle helak edildiler, source:69:5}. Fecr Suresi'nde Âd, Semûd ve Firavun için taşkının karşılığı yukarıdan dökülen bir azaptır: {ar:ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ, tr:ellezîne tağav fi'l-bilâd, gloss:ülkelerde taşanlar, source:89:11}; {ar:فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ, tr:fe-sabbe aleyhim rabbuke savte azâb, gloss:Rabbin de üstlerine bir azap kamçısı döktü, source:89:13}. Fucûr kelimesinin kendisi de bu dönüşü taşır: {ar:انفجرت عليهم الدواهي إذا جاءهم الكثير منها بغتة, tr:infecerat aleyhimu'd-devâhî izâ câehumu'l-kesîru minhâ bağteten, gloss:belalar ansızın ve çok sayıda geldiğinde "üstlerine fışkırdı" denir, source:"ف ج ر,B003"}. Düz bir anlatım "isyan ettiler, cezalandırıldılar" der. Bu imge ise cezayı suçun suyuyla gösterir: içte bent yıkılır, dışta sel gelir.

Kaynaklar: 91:8 فُجُورَهَا ف ج ر B001; 91:8 فُجُورَهَا ف ج ر B003; 91:8 فُجُورَهَا ف ج ر B004; 91:8 تَقْوَىٰهَا و ق ي B001; 91:8 تَقْوَىٰهَا و ق ي B002; 91:11 بِطَغْوَىٰهَآ ط غ ي B001; 91:11 بِطَغْوَىٰهَآ ط غ ي B002; 91:11 بِطَغْوَىٰهَآ ط غ ي B004; 91:12 ٱنۢبَعَثَ ب ع ث B001; 91:12 ٱنۢبَعَثَ ب ع ث B004

## Dişi devenin bedeni

Surenin birçok kelimesi bir dişi deveyle uğraşmanın dilinden gelir. Merkezde devenin kendisi durur: {ar:ناقة ونوق, tr:nâkatun ve nûk, gloss:nâka, dişi deve; çoğulu nûk, source:"ن و ق,B002"}. On ikinci ayetin fiili de deve sürmenin dilindendir: {ar:بعثت الناقة إذا أثرتها, tr:ba'astu'n-nâkate izâ eseartuhâ, gloss:dişi deveyi kaldırdığımda "ba'astu" derim, source:"ب ع ث,B001"}. İşin tamamı şöyle anlatılır: {ar:بعثت البعير فانبعث إذا حللت عقاله وأرسلته لو كان باركا فأثرته, tr:ba'astu'l-ba'îra fe'nbe'ase izâ halaltu ıkâlehû ve erseltuh, ev kâne bârikan fe-esertuh, gloss:deveyi kaldırdım, o da kalktı; yani köstekini çözüp saldım ya da çökmüşse ayağa kaldırdım, source:"ب ع ث,B001"}. Deve sürücüsünün fiilinde iki taraf vardır: biri kaldırır, deve kalkar. On ikinci ayette ise kaldıran yoktur, yalnızca kalkan vardır. Köstekten kurtulan, en bedbaht adamdır ve kalkışı devenin üstüne yönelir.

İkinci ayetteki fiil, devenin ardından yürüyen yavruyu adlandırır: {ar:تلو الناقة ولدها الذي يتلوها, tr:tilvu'n-nâkati veleduhe'llezî yetlûhâ, gloss:devenin tilvu, onu izleyen yavrusudur, source:"ت ل و,B006"}. Ay güneşi, yavrunun anasını izlediği gibi izler. Elçinin adının kökü de devenin yürüyüşünü anlatır: {ar:ناقة رسلة لينة المفاصل, tr:nâkatun resletun leyyinetu'l-mefâsıl, gloss:resle deve, eklemleri yumuşak devedir, source:"ر س ل,B003"}; {ar:ناقة رسلة سهلة السير وإبل مراسيل منبعثة انبعاثا سهلا, tr:nâkatun resletun sehletu's-seyr, ve ibilun merâsîlu munbe'isetun inbi'âsen sehlen, gloss:resle deve, yürüyüşü kolay devedir; merâsîl develer, kolayca harekete geçen develerdir, source:"ر س ل,B003"}. Sekizinci ayetteki fiil memedeki yavruyu taşır, on üçüncü ayetteki kelime devenin suyunu. Bu sahne yukarıdaki iki imgede gösterildi.

On dördüncü ayette devenin bedenine yönelen fiil gelir. Bu fiil eşek arısı sokması gibi bir dokunuş değildir; ayağı biçmektir: {ar:عقر البعير كسف عرقوبه ثم جعل النحر عقرا, tr:akru'l-ba'îri kesfu urkûbih, summe cu'ile'n-nahru akran, gloss:deveyi akr etmek, topuk kirişini kesmektir; sonra boğazlamaya da akr denmiştir, source:"ع ق ر,B002"}. Kesilen kirişin adı on beşinci ayetteki kelimenin kökündendir: {ar:العرقوب عقب موتر خلف الكعبين والراء زائدة, tr:el-urkûbu akabun mûterun halfe'l-ka'beyn, ve'r-râu zâide, gloss:urkûb, iki aşık kemiğinin arkasında gerilmiş bir kiriştir; içindeki "r" harfi fazladan gelmiştir, source:"ع ق ب,B001"}; {ar:العقب العصب الذي تعمل منه الأوتار, tr:el-akabu'l-asabu'llezî tu'melu minhu'l-evtâr, gloss:akab, yay kirişlerinin yapıldığı sinirdir, source:"ع ق ب,B001"}. Topuğun kendisi de aynı köktendir: {ar:العقب مؤخر القدم, tr:el-akibu mu'ahharu'l-kadem, gloss:akib, ayağın arka ucudur, source:"ع ق ب,B002"}. On dördüncü ayetteki günah kelimesinin kökü de hayvanın arka tarafını adlandırır: {ar:ذنب وهو مؤخر الدواب, tr:zenebun, ve huve mu'ahharu'd-devâbb, gloss:zeneb, hayvanların arka ucudur, kuyruğudur, source:"ذ ن ب,B002"}. Ayakları biçen kılıç tam bu arka tarafa iner.

Kur'an devenin hikâyesini birkaç yerde anlatır. Allah Salih'e şöyle der: {ar:إِنَّا مُرْسِلُوا۟ ٱلنَّاقَةِ فِتْنَةًۭ لَّهُمْ فَٱرْتَقِبْهُمْ وَٱصْطَبِرْ, tr:innâ mursilu'n-nâkati fitneten lehum fe'rtakıbhum ve'stabir, gloss:onları sınamak için dişi deveyi gönderiyoruz; sen onları gözle ve sabret, source:54:27}. Burada deve "gönderilir", ve fiil elçinin adının köküyle kurulur. Ardından o tek adam bıçağa uzanır: {ar:فَنَادَوْا۟ صَاحِبَهُمْ فَتَعَاطَىٰ فَعَقَرَ, tr:fe-nâdev sâhibehum fe-teâtâ fe-akar, gloss:arkadaşlarını çağırdılar; o da eline aldı ve ayaklarını biçti, source:54:29}. Salih'in uyarısında devenin otlama hakkı da vardır, dokunma yasağı da: {ar:هَٰذِهِۦ نَاقَةُ ٱللَّهِ لَكُمْ ءَايَةًۭ ۖ فَذَرُوهَا تَأْكُلْ فِىٓ أَرْضِ ٱللَّهِ ۖ وَلَا تَمَسُّوهَا بِسُوٓءٍۢ, tr:hâzihî nâkatu'llâhi lekum âyeten, fe-zerûhâ te'kul fî ardı'llâhi ve lâ temessûhâ bi-sû', gloss:bu, size bir işaret olarak Allah'ın devesi; bırakın Allah'ın yerinde otlasın, ona kötülükle dokunmayın, source:7:73}. Şuarâ Suresi'nde ise devirmenin hemen ardından pişmanlık gelir: {ar:فَعَقَرُوهَا فَأَصْبَحُوا۟ نَٰدِمِينَ, tr:fe-akarûhâ fe-asbahû nâdimîn, gloss:ayaklarını biçtiler ve pişman oldular, source:26:157}. Düz bir anlatım "deveyi öldürdüler" der. Fiil ise işin yerini gösterir: önce topuğa, sonra yere yapılan bir iş. Kelimelerin dağılımı da bir sıra gösterir. Kaldırılan, izlenen, rahat yürüyen ve sulanan bir deve, sonunda arkasından biçilir. Bu ardından gelen kelimeler, son ayette suçun ardından gelecek olanı haber verir.

Kaynaklar: 91:2 تَلَىٰهَا ت ل و B006; 91:8 فَأَلْهَمَهَا ل ه م B001; 91:12 ٱنۢبَعَثَ ب ع ث B001; 91:13 نَاقَةَ ن و ق B002; 91:13 رَسُولُ ر س ل B003; 91:13 وَسُقْيَٰهَا س ق ي B001; 91:14 فَعَقَرُوهَا ع ق ر B002; 91:14 بِذَنۢبِهِمْ ذ ن ب B002; 91:15 عُقْبَٰهَا ع ق ب B001; 91:15 عُقْبَٰهَا ع ق ب B002

## Gönderilen ve peşine düşülen

Surenin başında doğru bir izleme vardır: ay güneşi izler. İzleme fiilinin bir kolu, vahyedilmiş kitabı izlemeyi anlatır: {ar:التلاوة تختص باتباع كتب الله المنزلة تارة بالقراءة وتارة بالارتسام, tr:et-tilâvetu tahtessu bi'ttibâ'i kutubi'llâhi'l-munzele, târeten bi'l-kırâe ve târeten bi'l-irtisâm, gloss:tilâvet, Allah'ın indirdiği kitapları izlemeye mahsustur; bazen okuyarak, bazen izine uyarak, source:"ت ل و,B002"}. İkinci ayetteki ayın işi, on üçüncü ayette elçinin getirdiği sözü izlemenin ölçüsü olur.

Elçinin adının kökü, salıvermeyi ve uzanmayı anlatır: {ar:أصل واحد يدل على الانبعاث والامتداد, tr:aslun vâhidun yedullu ale'l-inbi'âsi ve'l-imtidâd, gloss:harekete geçmeyi ve uzanmayı gösteren tek bir kök, source:"ر س ل,B001"}; {ar:الإرسال يقابل الإمساك, tr:el-irsâlu yukâbilu'l-imsâk, gloss:irsâl, tutmanın karşıtıdır, source:"ر س ل,B001"}. Elçi taşıdığı sözün adıyla da anılır: {ar:الرسول يقال للقول المتحمل وتارة لمتحمل القول والرسالة, tr:er-rasûlu yukâlu li'l-kavli'l-mutehammel, ve târeten li-mutehammili'l-kavli ve'r-risâle, gloss:resûl, taşınan söze de, sözü ve mesajı taşıyana da denir, source:"ر س ل,B002"}. Gönderme fiili ile on ikinci ayetin fiili aynı aileye bağlanır: {ar:ولقد بعثنا في كل أمة رسولا نحو أرسلنا رسلنا, tr:ve le-kad ba'asnâ fî kulli ummetin rasûlen, nahvu erselnâ rusulenâ, gloss:"her ümmete bir elçi ba'as ettik" sözü, "elçilerimizi irsâl ettik" gibidir, source:"ب ع ث,B002"}. Kur'an'daki karşılığı bir ayette göndermeyi, inkârı ve sonucu birlikte toplar: {ar:وَلَقَدْ بَعَثْنَا فِى كُلِّ أُمَّةٍۢ رَّسُولًا, tr:ve le-kad ba'asnâ fî kulli ummetin rasûlen, gloss:andolsun, her ümmete bir elçi gönderdik, source:16:36}. Aynı ayet şöyle biter: {ar:فَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ, tr:fe'nzurû keyfe kâne âkıbetu'l-mukezzibîn, gloss:yalanlayanların sonunun nasıl olduğuna bakın, source:16:36}. On ikinci ayette ise fiil, göndereni olmayan bir kalkış biçiminde gelir. Allah'ın göndermesine karşılık bir adam kendini gönderir.

Bu adam kavmin başındadır ve kavmin en bedbahtıdır: {ar:الشقوة خلاف السعادة, tr:eş-şikvetu hılâfu's-seâde, gloss:şikve, mutluluğun karşıtıdır, source:"ش ق و,B001"}. Kavim de onun peşine düşer. On dördüncü ayetteki "zenb" kelimesinin bir kolu bu izleyenlerin adıdır: {ar:ذنب الرجل أتباعه وأذناب القوم أتباع الرؤساء, tr:zenebu'r-raculi etbâ'uh, ve ezenâbu'l-kavmi etbâ'u'r-ruesâ', gloss:adamın kuyruğu, ona uyanlardır; kavmin kuyrukları, reislere uyanlardır, source:"ذ ن ب,B003"}. On beşinci ayetteki kelimenin kökü de birinin izinden gelmeyi anlatır: {ar:العاقب الذي يجيء في أثر صاحبه, tr:el-âkıbu'llezî yecîu fî eseri sâhibih, gloss:âkıb, arkadaşının izinden gelendir, source:"ع ق ب,B005"}. İzlenmesi gereken elçi ise yalanlanır: {ar:كذبته نسبته إلى الكذب, tr:kezzebtuhû: nesebtuhû ile'l-kezib, gloss:onu yalanladım, yani ona yalan isnat ettim, source:"ك ذ ب,B002"}. Kavmin elçiye cevabı söze karşı söz olarak gelir. Elçi "ve kâle", "dedi ki" diye konuşur: {ar:القول من النطق, tr:el-kavlu mine'n-nutk, gloss:kavl, konuşmadan gelir, source:"ق و ل,B001"}.

Kur'an Semûd'un bu reddini kendi sözleriyle aktarır. Bir insanı izlemeyi küçümserler: {ar:أَبَشَرًۭا مِّنَّا وَٰحِدًۭا نَّتَّبِعُهُۥٓ, tr:e beşeren minnâ vâhiden nettebi'uh, gloss:aramızdan tek bir insana mı uyacağız, source:54:24}. Ve onu yalancılıkla suçlarlar: {ar:بَلْ هُوَ كَذَّابٌ أَشِرٌۭ, tr:bel huve kezzâbun eşir, gloss:hayır, o şımarık bir yalancıdır, source:54:25}. Aynı sure, tek bir adamın ardına düşüldüğü sahneyle sürer: {ar:فَنَادَوْا۟ صَاحِبَهُمْ فَتَعَاطَىٰ فَعَقَرَ, tr:fe-nâdev sâhibehum fe-teâtâ fe-akar, gloss:arkadaşlarını çağırdılar; o da eline aldı ve ayaklarını biçti, source:54:29}. Elçiye uymayı reddedenler, kendi seçtikleri adamı izler. A'râf Suresi'nde de büyüklenen ileri gelenler müminlere sorar: {ar:أَتَعْلَمُونَ أَنَّ صَٰلِحًۭا مُّرْسَلٌۭ مِّن رَّبِّهِۦ, tr:e ta'lemûne enne Sâlihan murselun min rabbih, gloss:Salih'in Rabbi tarafından gönderildiğini mi biliyorsunuz, source:7:75}. Deveyi biçtikten sonra da alay ederler: {ar:إِن كُنتَ مِنَ ٱلْمُرْسَلِينَ, tr:in kunte mine'l-murselîn, gloss:eğer gönderilenlerdensen, source:7:77}. Şuarâ Suresi'nde de anlatım bir yalanlamayla açılır: {ar:كَذَّبَتْ ثَمُودُ ٱلْمُرْسَلِينَ, tr:kezzebet Semûdu'l-murselîn, gloss:Semûd gönderilenleri yalanladı, source:26:141}. Salih'in kendini tanıtması da şudur: {ar:إِنِّى لَكُمْ رَسُولٌ أَمِينٌۭ, tr:innî lekum rasûlun emîn, gloss:ben size gönderilmiş güvenilir bir elçiyim, source:26:143}. Neml Suresi bu izleyiciliğin içindeki bir çekirdekten bahseder: {ar:وَكَانَ فِى ٱلْمَدِينَةِ تِسْعَةُ رَهْطٍۢ, tr:ve kâne fi'l-medîneti tis'atu rahtin, gloss:şehirde dokuz kişilik bir çete vardı, source:27:48}. Elçinin son sözü, taşıdığı yükü teslim ettiğidir: {ar:لَقَدْ أَبْلَغْتُكُمْ رِسَالَةَ رَبِّى, tr:le-kad eblağtukum risâlete rabbî, gloss:Rabbimin mesajını size ulaştırdım, source:7:79}. Düz bir anlatım "yalanladılar" der. Bu imge ise iki izleme hattı çizer: biri gökte ve doğru, ay güneşin ardından gider; öteki yerde ve yanlış, kavim kendi en bedbahtının ardından gider. Birinde sıra korunur, ötekinde başa geçen, peşindekileri yıkıma götürür.

Kaynaklar: 91:2 تَلَىٰهَا ت ل و B001; 91:2 تَلَىٰهَا ت ل و B002; 91:11 كَذَّبَتْ ك ذ ب B002; 91:12 ٱنۢبَعَثَ ب ع ث B002; 91:12 أَشْقَىٰهَا ش ق و B001; 91:13 فَقَالَ ق و ل B001; 91:13 رَسُولُ ر س ل B001; 91:13 رَسُولُ ر س ل B002; 91:14 فَكَذَّبُوهُ ك ذ ب B002; 91:14 بِذَنۢبِهِمْ ذ ن ب B003; 91:15 عُقْبَٰهَا ع ق ب B005

## Arayanın eline geçen

Dokuzuncu ve onuncu ayetler iki arayışın sonucunu söyler. "Efleha" kalmayı ve aranana ulaşmayı anlatır: {ar:الفلاح والفلح البقاء في الخير, tr:el-felâhu ve'l-felahu el-bekâu fi'l-hayr, gloss:felâh ve felah, iyilik içinde kalıcı olmaktır, source:"ف ل ح,B005"}; {ar:أفلح وأنجح إذا أدرك مطلوبه, tr:efleha ve encaha izâ edreke matlûbeh, gloss:aradığına erişince "efleha" ve "encaha" denir, source:"ف ل ح,B005"}. "Hâbe" ise aranandan yoksun kalmaktır: {ar:سعى في أمر فخاب إذا حرم فلم يفد خيرا, tr:se'â fî emrin fe-hâbe izâ hurime fe-lem yufid hayran, gloss:bir iş için koştu ve eli boş kaldı, yani yoksun kaldı, hiçbir hayır elde edemedi, source:"خ ي ب,B001"}; {ar:الخيبة فوت الطلب, tr:el-hayebetu fevtu't-taleb, gloss:hayebe, aranan şeyi kaçırmaktır, source:"خ ي ب,B001"}. Kökün aslı bir somut nesneye dayanır: {ar:الأصل قولهم للقدح الذي لا يوري هو خياب, tr:el-aslu kavluhum li'l-kadhi'llezî lâ yûrî: huve hayyâb, gloss:aslı, ateş vermeyen çakmak çubuğuna "hayyâb" demeleridir, source:"خ ي ب,B002"}. Ateş çakan biri çubuğu sürter, sürter, ama kıvılcım çıkmaz. Elinde, ışık vermeyen bir çubukla kalır. Sure ışıkla açılmıştı. Onuncu ayetteki kişinin eli ise kıvılcımsız kalır.

Onuncu ayetin iki fiili dilde tek bir cümlede birleşir: {ar:خاب من دس نفسه أي أخملها وخسس حظها, tr:hâbe men dessâ nefseh, ey ahmelehâ ve hassese hazzahâ, gloss:nefsini gizleyen eli boş kalmıştır; yani onu sönük bırakmış ve payını küçültmüştür, source:"د س و,B002"}. Gizlenen nefsin payı küçülür. On ikinci ayetteki en bedbaht ise bir yorgunluğun da adıdır: {ar:يوضع الشقاء موضع التعب وكل شقاوة تعب وليس كل تعب شقاوة, tr:yuveda'u'ş-şekâu mevdı'a't-ta'ab, ve kullu şekâvetin ta'ab, ve leyse kullu ta'abin şekâve, gloss:şekâ, yorgunluk yerine kullanılır; her bedbahtlık yorgunluktur, ama her yorgunluk bedbahtlık değildir, source:"ش ق و,B002"}. En bedbaht kişi en çok çabalayandır, ama emeğinin sonu tükenişe çıkar.

Kur'an bu kelimeleri yan yana koyar. A'lâ Suresi'nde öğüt, ondan yararlanan ile kaçan arasında bölünür: {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yezzekkeru men yahşâ, gloss:içi titreyen öğüt alacak, source:87:10}; {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht ise ondan kaçınacak, source:87:11}. Birkaç ayet sonra bu surenin dokuzuncu ayetine çok yakın bir söz gelir: {ar:قَدْ أَفْلَحَ مَن تَزَكَّىٰ, tr:kad efleha men tezekkâ, gloss:arınıp büyüyen kurtuluşa ermiştir, source:87:14}. Hemen ardından gelen sure de bu kelimeyi tekrarlar: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}. Hesap günü insanlar iki yöne ayrılır: {ar:فَمِنْهُمْ شَقِىٌّۭ وَسَعِيدٌۭ, tr:fe-minhum şakıyyun ve se'îd, gloss:onlardan kimi bedbaht, kimi mutludur, source:11:105}. Cehennemdekiler de kendi bedbahtlıklarını itiraf eder: {ar:رَبَّنَا غَلَبَتْ عَلَيْنَا شِقْوَتُنَا, tr:rabbenâ ğalebet aleynâ şikvetunâ, gloss:Rabbimiz, bedbahtlığımız bizi yendi, source:23:106}. Eli boş kalmanın anlatıldığı yerlerde de aynı kalıp gelir. Mûsâ sihirbazlara şöyle seslenir: {ar:وَقَدْ خَابَ مَنِ ٱفْتَرَىٰ, tr:ve kad hâbe meni'fterâ, gloss:yalan uyduran eli boş kalmıştır, source:20:61}. Hesap gününde de: {ar:وَقَدْ خَابَ مَنْ حَمَلَ ظُلْمًۭا, tr:ve kad hâbe men hamele zulmâ, gloss:zulüm yüklenen eli boş kalmıştır, source:20:111}. Elçilerin yardım dilediği sahnede de: {ar:وَخَابَ كُلُّ جَبَّارٍ عَنِيدٍۢ, tr:ve hâbe kullu cebbârin anîd, gloss:her inatçı zorba eli boş kaldı, source:14:15}. Arınmanın kazancı ise arınanın kendisinedir: {ar:وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ, tr:ve men tezekkâ fe-innemâ yetezekkâ li-nefsih, gloss:arınıp büyüyen, ancak kendisi için arınıp büyür, source:35:18}. Düz bir anlatım "kurtuldu" ve "kaybetti" der. Bu kelimeler ise bir arayışı gösterir: biri iyilikte kalır, öbürünün elinde kıvılcım çıkarmayan bir çubuk, ötekinin payında da boşa giden bir yorgunluk kalır.

Kaynaklar: 91:9 أَفْلَحَ ف ل ح B005; 91:10 خَابَ خ ي ب B001; 91:10 خَابَ خ ي ب B002; 91:10 دَسَّىٰهَا د س و B002; 91:12 أَشْقَىٰهَا ش ق و B002

## Buluşmalar

İlk buluşma sekizinci ayette olur. "Fucûr" kelimesi aynı kökten üç sahneyi bir arada tutar: geceyi yaran şafağı, bentten fırlayan suyu ve din perdesini yırtmayı. Gökte yarılma ışık getirir, nefiste ise koruyucu örtüyü yırtar ve bir taşkın başlatır. Takvâ aynı ayette hem bir örtüdür hem de bir settir. Tek bir kelime bu iki imgeyi birlikte taşır: örten ve alıkoyan. Böylece surenin başındaki düzenli nöbet nefsin içine taşınır. Gece güneşin üstünü sırası gelince örter ve sırası gelince açılır. Nefis ise ya kendi örtüsünü yerinde tutar ya da onu yırtıp taşar.

İkinci buluşma on ikinci ayetteki "inbe'ase" fiilindedir. Bu fiil üç imgeyi birden toplar. Fucûru tanımlayan atılıştır, deveyi köstekinden çözüp kaldırmanın sonucudur ve Allah'ın elçi gönderişinin eşi olan bir fiildir. Deve sürücüsünün dilinde biri kaldırır, deve kalkar. Bu ayette ise kaldıran yoktur. Adam kendi kendine, köstekinden kurtulmuş bir hayvan gibi kalkar ve Allah'ın gönderdiği deveye yönelir. Elçi gönderilmiştir, deve gönderilmiştir. Taşkın olan ise kendini gönderir.

Üçüncü buluşma, on dördüncü ayetten on beşinciye geçen bedenin arka ucudur. "Akr" topuk kirişini keser. O kirişin adı on beşinci ayetteki "ukbâ" kelimesinin kökündendir. Günahın adı olan "zenb" de hayvanın arka ucunun adıdır. Devenin imgesi ile suçun ardından gelen sonucun imgesi böylece aynı noktada birleşir. Kavim devenin arkasına vurur; karşılık da onların "arkalarından", yani günahlarının ardından gelir. Kova ile günahın aynı kökten gelmesi bunu ölçüye bağlar. Devenin su payını çiğneyenler kendi kova paylarını alırlar.

Dördüncü buluşma "sevvâ" fiilindedir. Bu fiil göğün ve nefsin bitirilişini Semûd'un yerle bir edilişine bağlar. Altıncı ayetteki yayılmış yer bu iki ucun arasında durur. Kavim ovaya saray kurmuştu. Yayılan yere kurulan sarayları yayılmış bir yer gibi dümdüz olur. Gökten yağan su, sürülen toprak ve büyüyen ekin bu yere bağlıdır. Hurmanın başını kesmeyi ve hiçbir şey bitirmeyen kumu anlatan "akr" fiili, kavmin tarlasını bir çorak yere çevirir.

Bu buluşmalar birlikte surenin hareketini taşır. Sure, her cismin yerini bildiği bir gökle başlar: ışık yayılır, ay onu izler, gündüz açar, gece örter. Ardından gök ve yerden bir ev kurulur ve aynı el nefsi bu evin üçüncü yapısı olarak düzenler. Nefse iki lokma yutturulur: hem yırtan ve taşan hem de örten ve alıkoyan. Dokuzuncu ve onuncu ayetler bu iki lokmanın sonucunu iki tarla gibi gösterir: biri sürülmüş ve büyümüş, öbürü gömülmüş. Semûd ise yanlış yolu seçer. Sınırı aşar, kendi en bedbahtının ardına düşer, gönderilen deveyi arkasından biçer. Karşılık gece gibi üstlerine kapanır ve evleri ile birlikte onları yayılmış bir yer gibi dümdüz eder. Sure, gece ile gündüzün nöbetleşmesini de adlandıran bir kelimeyle kapanır. Ama bu son nöbette, hükmün ardından gelecek ve onu geri çevirecek hiçbir şey yoktur.

