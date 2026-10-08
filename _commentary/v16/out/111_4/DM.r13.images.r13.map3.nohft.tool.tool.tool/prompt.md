Focus: 111:4. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/111_4/D.r13/context.md =====
# 111:4 — focus

وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ

Anchor translation (canonical reading, reference only):

Odun taşıyan karısı da.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَٱمْرَأَتُهُۥ | ٱمْرَأَت | م ر ء | CONJ;N;PRON |
| 2 | حَمَّالَةَ | حَمَّالَة | ح م ل | N |
| 3 | ٱلْحَطَبِ | حَطَب | ح ط ب | DET;N |


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
- 111:2 مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ
- 111:3 سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ
- 111:4 ◀ focus وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ
- 111:5 فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ


===== _commentary/v16/work/111_4/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## م ر ء (root_001409) — identity root of وَٱمْرَأَتُهُۥ (w1)

- **B001** insan; erkek veya kadın kişi — erkek; bağlama göre kişi · kadın · kadın sözünün değişik söylenişi · kadın sözünün ünlüsü değişen söylenişi · bir kişiye veya İmruülkays'a bağlanan
  يقال امرؤ وامرآن وقوم امرىء؛ وامرأة تأنيث امرىء (maqayis;ayn)؛ المرء الرجل؛ هذه مرأة صالحة ومرة (sihah)؛ امرأة تأنيث امرىء؛ المرء؛ قام امرؤ وضربت امرأ ومررت بامرىء (tahdhib)؛ يقال مرء ومرأة وامرؤ وامرأة (mufradat)
- **B002** erdemli kişilik olgunluğu — erdemli kişilik olgunluğu · erdemli kişilik olgunluğuna erişti · erdemli olgunluğu edinmeye çalıştı · bizim eksiklerimizi öne sürerek kendine erdem payı çıkarıyor · görünüşü ve huyu beğenilen erkek
  المروة كمال الرجولية (maqayis)؛ والمروءة كمال الرجولية؛ مرؤ الرجل وتمرأ إذا تكلف المروءة (ayn;tahdhib)؛ المروءة الإنسانية؛ مرؤ الرجل صار ذا مروءة؛ يتمرأ بنا (sihah)؛ العفة والحرفة؛ المروءة ألا تفعل في السر أمرا وأنت تستحي أن تفعله جهرا؛ المريء الرجل المقبول في خلقه وخلقه (tahdhib)
- **B003** yiyene uygun gelip kolay sindirilme [kalıp] — mideye dokunmadan kolayca sindirilen yemek · yiyene iyi gelip kolay sindirilen yemek · yemek bana iyi geldi · yemek bana uygun geldi · yemeği rahatça yiyip sindirdim · yemeği kolay sindirilir buldum
  المراءة مصدر الشيء المريء الذي يستمرأ؛ مرأني الطعام وامرأني (maqayis)؛ مرؤ الطعام وهو مريء بين المراءة؛ استمرأ (ayn)؛ مرؤ الطعام يمرؤ مراءة صار مريئا؛ مرأني الطعام؛ أمرأني الطعام؛ طعام ممرئ؛ مرئت الطعام استمرأته (sihah)؛ مرئت الطعام استمرأته؛ ما كان مريئا؛ هذا يمرىء الطعام؛ أمرأني الطعام إمراء؛ طعام ممرىء (tahdhib)
- **B004** yemek borusu — yemek borusu
  والمريء رأس المعدة والكرش اللازق بالحلقوم (maqayis)؛ المريء رأس المعدة والكرش اللازق بالحلقوم وهو مجرى الشراب والطعام (ayn)؛ مرئ الجزور والشاة للمتصل بالحلقوم الذي يجري فيه الطعام والشراب (sihah)؛ مرؤ بوزن مرع وهو الذي يجري فيه الطعام والشراب ويدخل فيه؛ الشجر ما لصق بالحلقوم والمريء (tahdhib)
- **B005** yemek yeme veya özel olayda yemek verme — neden yemek yemiyorsun · yemek yedim · ev yapımı veya evlilik dolayısıyla yemek verme
  ما لك لا تمرأ أي ما لك لا تطعم؛ وقد مرأت أي طعمت؛ والمرء الإطعام على بناء دار أو تزويج

## م ر ء (root_001410) — identity root of وَٱمْرَأَتُهُۥ (w1)

- **B001** insan; erkek veya kadın kişi — insan; bağlama göre erkek · kadın · kadın sözünün değişik söylenişi · onun karısı sözünün değişik söylenişi
  يقال امرؤ وامرآن وقوم امرىء؛ وامرأة تأنيث امرىء (maqayis)؛ امرأة ، تأنيث امرىء؛ يقال : هي امرأته ، وهي مرأته ، وهي مرته؛ يحول بين المرء وقلبه (tahdhib)
- **B002** erdemli kişilik olgunluğu — erdemli kişilik olgunluğu · erdemli olgunluğa erişti veya erişmeye çalıştı · erdemli olgunluğu edinmeye çalıştı
  والمروة كمال الرجولية وهي مهموزة مشددة ولا يبنى منه فعل (maqayis)؛ المروءة : كمال الرجولية؛ وقد مرؤ الرجل ، وتمرأ ، إذا تكلف المروءة؛ من المروءة : مرؤ الرجل يمرؤ مروءة (tahdhib)
- **B003** yiyene uygun gelip kolay sindirilme — yemeğin yiyene uygun gelme durumu · hafif ve kolay sindirilen yemek · yemeği rahatça yiyip sindirdim · yemek bana iyi geldi · yemek bana uygun geldi · yemek sana iyi gelir · yemek hafif ve kolay sindirilir oldu · yiyene iyi gelip kolay sindirilen yemek
  والمراءة مصدر الشىء المرىء الذي يستمرأ؛ مرأني الطعام وامرأني (maqayis)؛ مرئت الطعام : استمرأته؛ ما كان الطعام مريئا؛ أمرأني الطعام إمراء؛ مرؤ الطعام يمرؤ مراءة؛ المريء : الطعام الخفيف (tahdhib)
- **B004** yemek yeme veya özel olayda yemek verme — yemek yedi · ev yapımı veya evlilik dolayısıyla yemek verme
  ما لك لا تمرأ ؟ أي ما لك لا تطعم ؟ وقد مرأت ، أي طعمت؛ والمرء : الإطعام على بناء دار ، أو تزويج (tahdhib)
- **B005** yemek borusu — yemek borusu
  والمرىء رأس المعدة والكرش اللازق بالحلقوم (maqayis)؛ المريء ، بالهمز غير مشددة؛ وهو الذي يجري فيه الطعام والشراب ويدخل فيه؛ ما لصق بالحلقوم والمريء (tahdhib)
- **B006** görünüşü ve huyu beğenilen erkek [kalıp] — görünüşü ve huyu beğenilen erkek
  وما كان الرجل مريئا؛ المريء : الرجل المقبول في خلقه وخلقه (tahdhib)

## ح م ل (root_000357) — identity root of حَمَّالَةَ (w2)

- **B001** bir yükü kaldırıp götürme veya üstlenme — bir şeyi kaldırıp taşımak · sırtta, başta veya başka bir yerde dıştan taşınan yük · selin sürükleyip getirdiği çer çöp ve köpük
  حملت الشيء أحمله حملا (maqayis)؛ حملت الشئ على ظهرى أحمله حملا (sihah)؛ حمل الشيء يحمله حملا وحملانا (ayn;tahdhib)؛ حملت الثقل والرسالة والوزر حملا (mufradat)؛ حميل السيل ما يحمله من غثائه (maqayis)؛ حميل السيل ما يحمل من الغثاء (ayn;sihah)؛ حميل السيل ما حمله السيل (tahdhib)؛ حملناكم في الجارية (mufradat)
- **B002** gebelik veya ağacın meyve yükü — rahimdeki yavru veya ağacın üzerindeki meyve · gebe kadın · gebe olmadan sütü gelmek
  الحمل ما كان في بطن أو على رأس شجر (maqayis;sihah)؛ الحمل ما في البطن (ayn)؛ حمل الشجر (ayn)؛ حملت المرأة والشجرة حملا (sihah)؛ حملت المرأة حبلت وكذا حملت الشجرة (mufradat)؛ حملت حملا خفيفا (mufradat)
- **B003** görev veya suç yükünü üstlenme [kalıp] — suçun ve kötülüğün yükünü üzerine almak · güvenilerek verilen işi üstlenmek veya onu yerine getirmemek · iletiyi ulaştırma görevini üstlenmek
  حملت الثقل والرسالة والوزر حملا (mufradat)؛ كلفوا أن يتحملوها أي يقوموا بحقها فلم يحملوها (mufradat)؛ حمل الأمانة أي خيانتها وترك أدائها (tahdhib)؛ من باء بالإثم يسمى حاملا للإثم (tahdhib)؛ وساء لهم يوم القيامة حملا أي وزرا (sihah)
- **B004** başkasının borcunu üstlenip güvence verme — uzlaşma için üstlenilen kan bedeli veya ödeme yükü · başkası adına güvence vermek · borcun ödenmesini güvence altına alan kişi
  الحمالة أن يحمل الرجل دية ثم يسعى عليها والضمان حمالة (maqayis)؛ الحمالة الدية يحملها قوم عن قوم (ayn)؛ الحمالة ما يحمله القوم من الديات (jamhara)؛ حملت به حمالة أي كفلت (sihah)؛ الحميل الكفيل (jamhara;tahdhib;mufradat)؛ الحميل لكونه حاملا للحق مع من عليه الحق (mufradat)
- **B005** soy bağı doğrulanamayan getirilmiş çocuk — terk edilmiş, başka yerden getirilmiş veya soyu doğrulanamayan çocuk · soyu doğrulanamayan kişinin mirası
  الحميل المنبوذ يحمل فيربى (ayn;tahdhib)؛ الحميل الولد في بطن الأم إذا أخذت من أرض الشرك (ayn;tahdhib)؛ الحميل الذي يحمل من بلده صغيرا ولم يولد في الإسلام (sihah)؛ الحميل الدعي (maqayis;sihah)؛ ميراث الحميل لمن لا يتحقق نسبه (mufradat)
- **B006** taşıma kayışı, binek düzeneği veya yük hayvanı — kılıç askısı · deve üzerinde yolcu taşıyan iki yanlı düzenek · yük taşımaya ayrılmış deve veya başka hayvan · yükleri veya yolcu düzenekleriyle birlikte develer · armağan olarak verilen binek hayvanı
  الحمالة والمحمل علاقة السيف (maqayis;ayn;sihah)؛ حمالة السيف وحميلته والجمع الحمائل (jamhara)؛ المحمل الشقان على البعير يحمل فيهما نفسان (ayn)؛ المحمل واحد محامل الحاج (sihah)؛ الحمولة الإبل تحمل عليها الأثقال (maqayis;ayn)؛ الحمولة ما احتمل عليه الحي من بعير أو حمار أو غيره (sihah;tahdhib)
- **B007** zorlanarak yüklenme, eğilme veya dayanak olma — güç bir işe zorlanarak girişmek · yolculukta kendini sonuna kadar zorlamak · birinin üzerine doğru eğilmek veya yüklenmek · güvenilip dayanılan kişi veya şey
  تحاملت إذا تكلفت الشيء على مشقة (maqayis)؛ تحاملت في الشيء إذا تكلفته على مشقة (ayn)؛ حمل على نفسه في السير أي جهدها فيه (sihah)؛ تحامل عليه أي مال (sihah)؛ ما على فلان محمل أي معتمد (sihah;tahdhib)؛ المحمل بفتح الميم المعتمد (tahdhib)
- **B008** öfkeye kapılma veya incinmeye ağırbaşlılıkla katlanma — öfkelenmek veya öfkenin etkisine kapılmak · incitici davranışa öfkesini tutarak katlanmak
  الاحتمال الغضب (maqayis)؛ احتمل إذا غضب (maqayis;tahdhib)؛ احتمله الغضب وأقله الغضب (maqayis)؛ حملت عنه أي حلمت عنه (ayn)؛ احتمل الرجل إذا غضب ويكون بمعنى حلم (tahdhib)
- **B009** kuzu — kuzu
  الحمل الخروف والجميع الحملان (ayn;tahdhib)؛ الحمل من الضأن معروف وهو الجذع فما دونه (jamhara)؛ خص الضأن الصغير بذلك لكونه محمولا (mufradat)
- **B010** Koç burcu ve onunla ilişkilendirilen yağışlı gök olayı — Koç, burçlar kuşağının ilk burcu · bol su taşıyan kara bulut veya şimşek · bol su taşıyan bulut · Koç burcuna bağlanan yağış dönemi
  الحمل برج من البروج (ayn;tahdhib)؛ الحمل أول البروج (sihah)؛ البرق يقال له حمل (maqayis)؛ الحمل السحاب الكثير الماء (jamhara)؛ الحمل السحاب الأسود (tahdhib)؛ الحمل النوء وهو الطلي (tahdhib)؛ الحميل السحاب الكثير الماء لكونه حاملا للماء (mufradat)

## ح ط ب (root_000335) — identity root of ٱلْحَطَبِ (w3)

- **B001** yakacak odun ve odun toplama — yakacak odun · odun toplamak · kendisi için odun arayıp toplamak · birisi için odun toplayıp getirmek · odun toplayan kişi · odun toplayan kişi · odun toplayıp satan kişi · odun toplayanlar topluluğu · odunu bol yer · kuru diken veya odun yiyen dişi deve · bağın odunluk dallarını kesme vakti gelmek · bağın üst dalları odun için kesilecek duruma gelmek · bağdan kesilen odunluk üst dallar
  الحطب معروف (maqayis;ayn;jamhara;sihah;tahdhib)؛ ما يعد للإيقاد (mufradat)؛ حطبت واحتطبت إذا جمعته (sihah)؛ حطبت فلانا إذا احتطبت له (tahdhib)؛ مكان حطيب كثير الحطب (maqayis;jamhara;sihah;mufradat)؛ ناقة محاطبة تأكل الشوك اليابس (maqayis;sihah)؛ قد استحطب عنبكم فاحطبوه حطبا (tahdhib)
- **B002** sözünü karıştırıp gereksizce uzatan kimse [kalıp] — sözünü karıştıran, çok veya uzun konuşan kimse
  يقال للمخلط في كلامه حاطب ليل (maqayis;ayn;sihah;tahdhib;mufradat)؛ المسهب كحاطب الليل (jamhara)؛ المكثار كحاطب ليل (tahdhib)
- **B003** laf taşıyıp kötülük körükleme — laf taşıma ve birini başkasına kötüleme · birini başkasına çekiştirip hakkında söz taşımak · laf taşımanın kinayeli anlatımı · laf taşıyıp insanlar arasındaki kötülüğü körüklemek
  حطب فلان بفلان سعى به (maqayis;ayn;tahdhib;mufradat)؛ حمالة الحطب كناية عن النميمة (maqayis;tahdhib;mufradat)؛ الحطب في القرآن النميمة (ayn)؛ يوقد بالحطب الجزل كناية عن ذلك (mufradat)
- **B004** kuru odun gibi çok zayıf kimse — çok zayıf adam · çok zayıf kimse
  الأحطب الشديد الهزال وكذلك الحطب كأنه شبه بالحطب اليابس (maqayis)؛ يقال للشديد الهزال حطب (ayn)؛ الحطب الرجل الشديد الهزال والأحطب مثله (sihah)

===== _commentary/v16/out/s111/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 111:4, and ## Buluşmalar) =====
## Yakıt, tutuşma ve kızartılan

Üçüncü ve dördüncü ayet birlikte işleyen bir ateşi bütün parçalarıyla kurar: toplanıp sırtta taşınan odun, tutuşan yakıt, dumandan arınmış alev ve bu ateşe giren, onda kalan, sıcağına katlanan bir adam. Üçüncü ayetin fiili kendi kökünde hem yakıtı hem kızartmayı adlandırır: {ar:الصلاء يقال للوقود وللشواء, tr:es-silâu yukâlu li'l-vekûdi ve li'ş-şivâ, gloss:silâ, yakıt için de kebap için de söylenir, source:"ص ل ي,B004"}; {ar:الصلاء ما يصطلى به وما يذكى به النار ويوقد, tr:es-silâu mâ yustalâ bihî ve mâ yuzkâ bihi'n-nâru ve yûkad, gloss:silâ, kendisiyle ısınılan ve ateşin kendisiyle tutuşturulup yakıldığı şeydir, source:"ص ل ي,B004"}. Et ateşte böyle pişirilir: {ar:صليت اللحم صليا شويته, tr:saleytu'l-lahme salyen şeveytuh, gloss:eti ateşte kızarttım, source:"ص ل ي,B004"}. Böylece üçüncü ayetin fiili dördüncü ayetin odununu daha baştan içinde taşır ve adamı etin konduğu yere koyar.

Fiilin surede kurduğu yapı, kökün kayıtlı bir kullanımıyla birebir aynıdır: {ar:صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها, tr:saliye'l-kâfiru nâran fehuve yaslâhâ, ey kâsâ harrahâ ve şiddetehâ, gloss:kâfir ateşe yandı, yani sıcağına ve şiddetine katlandı, source:"ص ل ي,B003"}. Fiil girmeyi ve orada kalmayı da söyler: {ar:من يصلى في النار أي يلزم النار, tr:men yuslâ fi'n-nâr, ey yelzemu'n-nâr, gloss:ateşte yakılan, yani ateşten ayrılmayan, source:"ص ل ي,B003"}. Ateş kelimesi, kökünde ışığın yanında kıpırtıyı da taşır: {ar:ولأن ذلك يكون مضطربا سريع الحركة, tr:ve li-enne zâlike yekûnu muztariben serîa'l-hareke, gloss:çünkü o çalkantılı ve hızlı hareketlidir, source:"ن و ر,B002"}. Alev ise ateşin tam tutuşmuş hâlidir: {ar:اشتعال النار الذي قد خلص من الدخان, tr:iştiâlu'n-nâri'llezî kad halusa mine'd-duhân, gloss:dumandan arınmış ateşin yanışı, source:"ل ه ب,B001"}. Kök bu sıcaklığı susuzlukla da adlandırır: {ar:يستعمل اللهاب في النار والعطش جميعا, tr:yusta'melu'l-luhâbu fi'n-nâri ve'l-ataşi cemîan, gloss:luhâb hem ateş hem susuzluk için kullanılır, source:"ل ه ب,B002"}. Alevin içindeki aynı zamanda susuzdur.

Dördüncü ayet yakıtı getirir: {ar:وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ, tr:vemraetuhû hammâlete'l-hatab, gloss:karısı da, o odun hamalı, source:111:4}. Odun, yakmak için hazırlanmış şeydir, {ar:ما يعد للإيقاد, tr:mâ yu'addu li'l-îkâd, gloss:tutuşturmak için hazırlanan, source:"ح ط ب,B001"}, ve toplanır: {ar:حطبت واحتطبت إذا جمعته, tr:hatabtu vehtatabtu izâ cema'tuh, gloss:odun topladım, source:"ح ط ب,B001"}. Taşıma fiilinin temel sahnesi sırttır: {ar:حملت الشئ على ظهرى أحمله حملا, tr:hameltu'ş-şey'e alâ zahrî ahmiluhû hamlen, gloss:şeyi sırtımda taşıdım, source:"ح م ل,B001"}. Kelimenin kalıbı, bir defalık taşımayı değil, işi alışkanlık edinmiş, ağır yük taşıyan kişiyi söyler. Odun kökü insanı da odun diye anar: {ar:الحطب الرجل الشديد الهزال, tr:el-hatabu er-raculu'ş-şedîdu'l-huzâl, gloss:çok zayıf adam, source:"ح ط ب,B004"}, {ar:كأنه شبه بالحطب اليابس, tr:keennehû şubbihe bi'l-hatabi'l-yâbis, gloss:sanki kuru oduna benzetildi, source:"ح ط ب,B004"}. Kadının taşıdığı odun ile adamın yandığı ateş bir ve aynı ateştir.

Kur'an insanı ateşin yakıtı olarak açıkça anar. Cinler kendi aralarında konuşurken der ki: {ar:وَأَمَّا ٱلْقَٰسِطُونَ فَكَانُوا۟ لِجَهَنَّمَ حَطَبًۭا, tr:ve emme'l-kâsitûne fe-kânû li-cehenneme hatabâ, gloss:haktan sapanlara gelince, onlar cehenneme odun oldular, source:72:15}; surenin kelimesi burada insanların adıdır. Müşriklere ve taptıklarına söylenen sözde başka bir kelime aynı işi görür, {ar:حَصَبُ جَهَنَّمَ, tr:hasabu cehennem, gloss:cehenneme atılan yakıt, source:21:98}. Müminlere hitap eden ayette ateşin yakıtı insanlar ve taşlardır, {ar:وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:vekûduhe'n-nâsu ve'l-hicâra, gloss:yakıtı insanlar ve taşlardır, source:66:6}. Bir başka ayette mal ve evladın fayda vermeyişi doğrudan yakıta bağlanır: {ar:لَن تُغْنِىَ عَنْهُمْ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُم مِّنَ ٱللَّهِ شَيْـًۭٔا ۖ وَأُو۟لَٰٓئِكَ هُمْ وَقُودُ ٱلنَّارِ, tr:len tuğniye anhum emvâluhum ve lâ evlâduhum mina'llâhi şey'en, ve ulâike hum vekûdu'n-nâr, gloss:malları da evlatları da onlara Allah'a karşı hiçbir fayda vermez; işte onlar ateşin yakıtıdır, source:3:10}. İkinci ayetten üçüncü ayete geçiş orada tek bir ayettir.

Fiilin ateşle kurduğu yapı Kur'an'da sabittir: {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4}; {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona ancak en bedbaht olan girer, source:92:15}. Gelecek eki ile aynı fiil, öksüzlerin mallarını haksızca yiyenler için malın ardından gelir: {ar:وَسَيَصْلَوْنَ سَعِيرًۭا, tr:ve se-yaslevne seîrâ, gloss:alevli ateşe girip yanacaklar, source:4:10}; o ayet, yenen malın karınlarda zaten ateş olduğunu da söyler. Allah'ın tek yarattığı ve kendisine uzanıp giden mal ile yanında hazır oğullar verdiği adam hakkındaki pasajda {source:74:11}, mal {source:74:12} ve oğullar {source:74:13} sayıldıktan sonra aynı gelecek ve aynı kök gelir: {ar:سَأُصْلِيهِ سَقَرَ, tr:se-uslîhi sekar, gloss:onu sekar'a sokup yakacağım, source:74:26}. Kızartma imgesi ayetlerine inkâr edenler için en açık hâlini alır: {ar:كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا, tr:kullemâ nadicet culûduhum beddelnâhum culûden ğayrahâ, gloss:derileri piştikçe yerine başka deriler koyarız, source:4:56}. Mal toplayıp sayan dedikoducunun ateşi de yakılmış bir ateştir, {ar:نَارُ ٱللَّهِ ٱلْمُوقَدَةُ, tr:nâru'llâhi'l-mûkade, gloss:Allah'ın tutuşturulmuş ateşi, source:104:6}. Odun ile ateş arasındaki bağı Allah kendi yaratışında gösterir: {ar:ٱلَّذِى جَعَلَ لَكُم مِّنَ ٱلشَّجَرِ ٱلْأَخْضَرِ نَارًۭا, tr:ellezî ceale lekum mine'ş-şeceri'l-ahdari nârâ, gloss:size yeşil ağaçtan ateş çıkaran, source:36:80}.

Kaynaklar: 111:3 سَيَصْلَىٰ ص ل ي B004; 111:3 سَيَصْلَىٰ ص ل ي B003; 111:3 نَارًۭا ن و ر B002; 111:3 لَهَبٍۢ ل ه ب B001; 111:3 لَهَبٍۢ ل ه ب B002; 111:4 ٱلْحَطَبِ ح ط ب B001; 111:4 ٱلْحَطَبِ ح ط ب B004; 111:4 حَمَّالَةَ ح م ل B001

## Ev ocağı ve soy: tersine dönen hane

Bir ev; ailesi için kazanan bir erkek, bir eş, evlenmede ya da ev kurulurken verilen bir ziyafet, ev için toplanan odun ve et kızartılan, başında ısınılan bir ocakla döner. Surenin kelimeleri bu ev sahnesinin bütün parçalarını kökleriyle taşır. Kazanmak, ailesi için hayır kazanmaktır: {ar:فلان يكسب أهله خيرا, tr:fulânun yeksibu ehlehû hayran, gloss:falanca ailesine hayır kazandırır, source:"ك س ب,B002"}. Baba, besleyendir: {ar:فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده, tr:fulânun ye'bû hâze'l-yetîme ibâveten, ey yağzûhu kemâ yağzu'l-vâlidu veledeh, gloss:falanca bu yetime babalık eder, yani babanın çocuğunu beslediği gibi onu besler, source:"ء ب و,B001"}. Dördüncü ayetin ilk kelimesi eştir, {ar:هي امرأته, tr:hiye'mraetuh, gloss:o, onun karısıdır, source:"م ر ء,B001"}, ve kökü evin kuruluşundaki ziyafeti adlandırır: {ar:والمرء : الإطعام على بناء دار ، أو تزويج, tr:ve'l-mer'u el-it'âmu alâ binâi dârin ev tezvîc, gloss:mer', ev yapımında ya da evlenmede yemek vermektir, source:"م ر ء,B004"}. İkinci ayetin fiilinin kökü evliliği de adlandırır, {ar:الغنى التزويج, tr:el-ğınâ et-tezvîc, gloss:ğınâ, evlendirmedir, source:"غ ن ي,B006"}, ve kocasıyla yetinen kadını: {ar:الغانية المستغنية بزوجها عن الزينة, tr:el-ğâniye el-mustağniye bi-zevcihâ ani'z-zîne, gloss:ğâniye, kocası sayesinde süse ihtiyaç duymayan kadındır, source:"غ ن ي,B005"}. Odun kökü birisi için odun toplamayı bilir, {ar:حطبت فلانا إذا احتطبت له, tr:hatabtu fulânen izehtatabtu leh, gloss:falancaya odun topladım, source:"ح ط ب,B001"}, ve üçüncü ayetin fiili ocağın kendisidir: ısınılan ve kızartılan ateş {source:"ص ل ي,B004"}.

Surede bu ev bütünüyle tersine döner. Kazanan erkeğin kazancı kendine bile yetmez; ikinci ayetin fiili, kocası karısına yeten evliliğin kökünden gelir ama burada koca kendini bile karşılayamaz. Eş, kocasının içinde yanacağı ateşe odun taşır; ev ocağı Ateş olur. Bu ters çevrilmenin karşı sahnesi Kur'an'da Mûsâ'dadır. Süresini doldurup ailesiyle yola çıkan Mûsâ, Tûr'un yanında bir ateş görür ve ailesine şöyle der: {ar:لَعَلِّىٓ ءَاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ جَذْوَةٍۢ مِّنَ ٱلنَّارِ لَعَلَّكُمْ تَصْطَلُونَ, tr:lealî âtîkum minhâ bi-haberin ev cezvetin mine'n-nâri lealekum tastalûn, gloss:belki oradan size bir haber ya da bir ateş koru getiririm, belki ısınırsınız, source:28:29}; aynı söz başka bir yerde {ar:بِشِهَابٍۢ قَبَسٍۢ, tr:bi-şihâbin kabes, gloss:alınmış bir ateş parçasıyla, source:27:7} diye geçer {source:20:10}. Orada "ısınmak" fiili surenin "yanmak" fiiliyle aynı köktendir: bir koca ailesini ısıtmak için ateş getirir; burada bir eş, kocasının yanacağı ateşe odun taşır. Müminlere hitap eden ayet, insanın kendini ve ailesini yakıtı insanlar olan bir ateşten korumasını ister: {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا, tr:kû enfusekum ve ehlîkum nârâ, gloss:kendinizi ve ailenizi bir ateşten koruyun, source:66:6}. Kitabı arkasından verilen kişi için {source:84:10} yanmak, ailesi içindeki eski sevincin karşısına konur: {ar:وَيَصْلَىٰ سَعِيرًا إِنَّهُۥ كَانَ فِىٓ أَهْلِهِۦ مَسْرُورًا, tr:ve yaslâ seîran innehû kâne fî ehlihî mesrûrâ, gloss:alevli ateşe girer; çünkü o ailesi içinde sevinçliydi, source:84:12}. Allah'ın inkâr edenlere örnek verdiği Nûh'un ve Lût'un karılarında eş, fayda vermeme fiili ve Ateş bir araya gelir: {ar:فَلَمْ يُغْنِيَا عَنْهُمَا مِنَ ٱللَّهِ شَيْـًۭٔا وَقِيلَ ٱدْخُلَا ٱلنَّارَ مَعَ ٱلدَّٰخِلِينَ, tr:felem yuğniyâ anhumâ mina'llâhi şey'en ve kîle'dhulâ'n-nâra mea'd-dâhilîn, gloss:kocaları onlara Allah'a karşı hiçbir fayda vermedi ve onlara "girenlerle birlikte ateşe girin" denildi, source:66:10}. Hemen ardından Firavun'un karısı, kocasından ve onun işinden kurtarılmayı dileyen bir eş olarak gelir {source:66:11}: evlilik orada kaderi paylaştırmaz. Surede ise eş ve koca aynı ateşin iki ucundadır.

Dördüncü ve beşinci ayetin iki kelimesi bu evin bir başka parçasını, soyu da işitir. Taşımak, kökünde hamileliktir: {ar:حملت المرأة حبلت, tr:hamelet'il-mer'etu hebilet, gloss:kadın gebe kaldı, source:"ح م ل,B002"}, {ar:الحمل ما كان في بطن, tr:el-hamlu mâ kâne fî batn, gloss:haml, karında olandır, source:"ح م ل,B002"}. İp de kökünde aynı şeydir: {ar:الحبل الحمل وقد حبلت المرأة فهي حبلى, tr:el-habelu el-hamlu ve kad hebileti'l-mer'etu fe-hiye hublâ, gloss:habel gebeliktir; kadın gebe kaldı, o hâmiledir, source:"ح ب ل,B006"}. Bir tanım, iki kelimeyi birbiriyle açıklar ve gebeliğin ipe benzerliğini günlerin onunla uzamasında görür: {ar:الحبل وهو الحمل وذلك أن الأيام تمتد به, tr:el-habelu ve huve'l-hamlu ve zâlike enne'l-eyyâme temteddu bih, gloss:habel gebeliktir, çünkü günler onunla uzar, source:"ح ب ل,B006"}. Kadının iki ayetindeki iki kelime, onun taşıyacağı soyun kelimeleridir; oysa sahnede taşıdığı odun, boynundaki iptir. Birinci ayetin baba kelimesi bu soyun öbür ucunu tutar {source:"ء ب و,B001"}. Kur'an, ikinci ayetin cümlesini başka yerlerde malın yanına evladı koyarak kurar: {ar:مَن لَّمْ يَزِدْهُ مَالُهُۥ وَوَلَدُهُۥٓ إِلَّا خَسَارًۭا, tr:men lem yezidhu mâluhû ve veleduhû illâ hasârâ, gloss:malı ve evladı kendisine kayıptan başka bir şey katmayan, source:71:21}. Bu, Nûh'un kavminin kendisine isyan edip izledikleri önderlerden yakınmasıdır; "kayıp" kelimesi de tebâbın tanımında geçen kelimedir. İbrâhîm'in duasında o gün {ar:يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ, tr:yevme lâ yenfau mâlun ve lâ benûn, gloss:ne malın ne oğulların fayda vereceği gün, source:26:88} diye anılır. Mal ile evladın onlara fayda vermediği ve onların ateşin ehli olduğu ayette {source:58:17} ve yukarıda geçen ayette {source:3:10} bu ikili ikinci ve üçüncü ayetin sırasını kurar. Surede ikinci sırada "kazandığı" durur; o yerde evladı duymak bir okumadır, kelimenin söylediği değil. Suçlunun o gün kurtulmak için fidye olarak vermek isteyeceği şeyler de bu evin halkıdır: {ar:بِبَنِيهِ وَصَٰحِبَتِهِۦ وَأَخِيهِ, tr:bi-benîhi ve sâhibetihî ve ehîh, gloss:oğulları, eşi ve kardeşiyle, source:70:12}.

Kaynaklar: 111:1 أَبِى ء ب و B001; 111:2 كَسَبَ ك س ب B002; 111:2 أَغْنَىٰ غ ن ي B006; 111:2 أَغْنَىٰ غ ن ي B005; 111:3 سَيَصْلَىٰ ص ل ي B004; 111:4 وَٱمْرَأَتُهُۥ م ر ء B001; 111:4 وَٱمْرَأَتُهُۥ م ر ء B004; 111:4 ٱلْحَطَبِ ح ط ب B001; 111:4 حَمَّالَةَ ح م ل B002; 111:5 حَبْلٌۭ ح ب ل B006

## Odun taşıyan, söz taşıyan

Dördüncü ayetin ifadesi, dilin içinde başlı başına bir mecaz olarak da kayıtlıdır: {ar:حمالة الحطب كناية عن النميمة, tr:hammâletu'l-hatabi kinâyetun ani'n-nemîme, gloss:odun hamalı, söz taşımanın kinayesidir, source:"ح ط ب,B003"}. Odun fiil olarak birinin aleyhine konuşmaktır: {ar:حطب فلان بفلان سعى به, tr:hatabe fulânun bi-fulânin seâ bih, gloss:falanca falancayı çekiştirdi, onu ele verdi, source:"ح ط ب,B003"}. Mecazın işleyişi de kayıtlıdır: söz taşıyan, ateşi kalın odunla besler: {ar:يوقد بالحطب الجزل كناية عن ذلك, tr:yûkidu bi'l-hatabi'l-cezli kinâyeten an zâlik, gloss:kalın odunla ateş yakar; bu, onun kinayesidir, source:"ح ط ب,B003"}. Taşıma fiili ise yükü de haberi de aynı kelimeyle söyler: {ar:حملت الثقل والرسالة والوزر حملا, tr:hameltu's-sikale ve'r-risâlete ve'l-vizra hamlen, gloss:ağırlığı, mesajı ve vebali taşıdım, source:"ح م ل,B001"}. Yük taşımak, haber taşımak ve laf taşımak tek bir taşıma işidir. Odun yanacağı yere götürülür; laf insanlar arasına götürülür ve orada düşmanlık tutuşturur. Bu düşmanlığın adı da ateşin kökünden gelir: {ar:بينهم نائرة أي عداوة وشحناء, tr:beynehum nâiretun, ey adâvetun ve şahnâ, gloss:aralarında nâire var, yani düşmanlık ve kin, source:"ن و ر,B007"}. Alev kökünün tutuşturma fiili, taşınan yakıtın ateş alışını söyler: {ar:التهبت النار وتلهبت وألهبتها, tr:iltehebeti'n-nâru ve telehhebet ve elhebtuhâ, gloss:ateş alevlendi, ben onu alevlendirdim, source:"ل ه ب,B001"}. Karanlıkta rastgele odun toplayan, sözünü karıştıran kişinin adıdır: {ar:يقال للمخلط في كلامه حاطب ليل, tr:yukâlu li'l-muhallıtı fî kelâmihî hâtıbu leyl, gloss:sözünü karıştırana "gece oduncusu" denir, source:"ح ط ب,B002"}. Bu okumada kadının insanlar arasında beslediği ateş ile üçüncü ayetin ateşi karşılaşır.

Kur'an söz taşıyanı mal sahibiyle aynı tarifte verir. Allah Peygamber'e şöyle der: {ar:وَلَا تُطِعْ كُلَّ حَلَّافٍۢ مَّهِينٍ, tr:ve lâ tutı' kulle hallâfin mehîn, gloss:çok yemin eden aşağılık kimseye uyma, source:68:10}, {ar:هَمَّازٍۢ مَّشَّآءٍۭ بِنَمِيمٍۢ, tr:hemmâzin meşşâin bi-nemîm, gloss:kusur arayan, laf taşıyıp dolaşan, source:68:11}, ve birkaç ayet sonra bu tavrın sebebini söyler: {ar:أَن كَانَ ذَا مَالٍۢ وَبَنِينَ, tr:en kâne zâ mâlin ve benîn, gloss:mal ve oğullar sahibi oldu diye, source:68:14}. Laf taşımak, mal ve oğullar: surenin ikinci ve dördüncü ayetlerinin malzemesi orada tek bir portrededir. Bir başka surede kusur arayan dedikoducu {ar:وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ, tr:veylün li-kulli humezetin lumeze, gloss:her arkadan çekiştirene, yüze karşı kusur bulana vay hâline, source:104:1}, mal toplayıp sayan {source:104:2} ve tutuşturulmuş ateşe atılan kişidir {source:104:6}. Allah'ın elinin bağlı olduğunu söyleyenlerin arasına Allah düşmanlık ve kin atar, ve bu düşmanlık ateş olarak sahnelenir: {ar:كُلَّمَآ أَوْقَدُوا۟ نَارًۭا لِّلْحَرْبِ أَطْفَأَهَا ٱللَّهُ, tr:kullemâ evkadû nâran li'l-harbi atfeehe'llâh, gloss:savaş için ne zaman bir ateş yaktılarsa Allah onu söndürdü, source:5:64}. Kazanmak ile taşımak bir ayette buluşur: bir suç kazanıp onu suçsuz birinin üstüne atan kişi {ar:فَقَدِ ٱحْتَمَلَ بُهْتَٰنًۭا وَإِثْمًۭا مُّبِينًۭا, tr:fe-kadi'htemele buhtânen ve ismen mubînâ, gloss:bir iftirayı ve apaçık bir günahı yüklenmiş olur, source:4:112}. İftira sahnesinin kendisinde de laf ağızdan ağıza taşınan bir şeydir, {ar:إِذْ تَلَقَّوْنَهُۥ بِأَلْسِنَتِكُمْ, tr:iz telakkavnehû bi-elsinetikum, gloss:onu dillerinizle birbirinizden alırken, source:24:15}, ve orada her kişiye kazandığı günah düşer: {ar:لِكُلِّ ٱمْرِئٍۢ مِّنْهُم مَّا ٱكْتَسَبَ مِنَ ٱلْإِثْمِ, tr:li-kulli'mriin minhum me'ktesebe mine'l-ism, gloss:onlardan her kişiye kazandığı günah vardır, source:24:11}.

Kaynaklar: 111:4 حَمَّالَةَ ٱلْحَطَبِ ح ط ب B003; 111:4 ٱلْحَطَبِ ح ط ب B002; 111:4 حَمَّالَةَ ح م ل B001; 111:3 نَارًۭا ن و ر B007; 111:3 لَهَبٍۢ ل ه ب B001

## Sırttaki yük: yük hayvanı, yular, vebal

Sırtında odun, boynunda hurma lifinden bir ip: dördüncü ve beşinci ayetin kelimeleri kökleriyle bir yük hayvanı sahnesi kurar. Taşımanın temel yeri sırttır {source:"ح م ل,B001"}; aynı kök yük taşıyan develeri adlandırır: {ar:الحمولة الإبل تحمل عليها الأثقال, tr:el-hamûle el-ibilu tuhmelu aleyhe'l-eskâl, gloss:hamûle, üzerine ağırlık yüklenen develerdir, source:"ح م ل,B006"}. Kök zorlanarak taşımayı da bilir: {ar:تحاملت إذا تكلفت الشيء على مشقة, tr:tehâmeltu izâ tekellefte'ş-şey'e alâ meşakka, gloss:bir şeyi zahmetle üstlendim, source:"ح م ل,B007"}. Odun kökünden kuru diken otlayan dişi deve adını alır: {ar:ناقة محاطبة تأكل الشوك اليابس, tr:nâkatun muhâtıbe te'kulu'ş-şevke'l-yâbis, gloss:kuru diken yiyen dişi deve, source:"ح ط ب,B001"}. Beşinci ayetin ipi bir yulardır: {ar:الحبل الرسن, tr:el-hablu er-resen, gloss:ip, yulardır, source:"ح ب ل,B001"}. İpin maddesi de bu dünyadan gelir; mesed, deve yününden ya da hurma lifinden bükülmüş kaba iş ipidir: {ar:المسد حبل يتخذ من أوبار الإبل, tr:el-mesedu hablun yuttehazu min evbâri'l-ibil, gloss:mesed, deve yününden yapılan iptir, source:"م س د,B001"}, {ar:حبل من ليف أو خوص, tr:hablun min lîfin ev havs, gloss:lif ya da hurma yaprağından ip, source:"م س د,B001"}. Birinci ayetin fiili bile yük hayvanını bilir; sırtı yara olmuş eşek ya da deve onunla anılır: {ar:حمار تاب الظهر إذا دبر, tr:himârun tâbbu'z-zahri izâ debir, gloss:sırtı yağır olmuş eşek, source:"ت ب ب,B003"}.

Taşınan yük bir de vebaldir: {ar:من باء بالإثم يسمى حاملا للإثم, tr:men bâe bi'l-ismi yusemmâ hâmilen li'l-ism, gloss:günahı yüklenen kişiye günah taşıyan denir, source:"ح م ل,B003"}. Kur'an bu yükü sırta koyar. Allah ile karşılaşmayı yalanlayanlar, Saat ansızın geldiğinde hasretle bağırırken {ar:وَهُمْ يَحْمِلُونَ أَوْزَارَهُمْ عَلَىٰ ظُهُورِهِمْ, tr:ve hum yahmilûne evzârahum alâ zuhûrihim, gloss:onlar günah yüklerini sırtlarında taşırlar, source:6:31}; aynı ayet {ar:قَدْ خَسِرَ, tr:kad hasira, gloss:kaybetti, source:6:31} diye açılır, yani tebâbın tanımındaki kayıpla. Zikirden yüz çeviren kıyamet günü bir vebal taşır {source:20:100} ve {ar:وَسَآءَ لَهُمْ يَوْمَ ٱلْقِيَٰمَةِ حِمْلًۭا, tr:ve sâe lehum yevme'l-kıyâmeti himlâ, gloss:kıyamet günü onlar için ne kötü bir yüktür, source:20:101}. Başkalarını yoldan çıkaranlar kendi yükleriyle birlikte saptırdıklarının yükünü de taşır {source:16:25}: {ar:وَلَيَحْمِلُنَّ أَثْقَالَهُمْ وَأَثْقَالًۭا مَّعَ أَثْقَالِهِمْ, tr:ve le-yahmilunne eskâlehum ve eskâlen mea eskâlihim, gloss:kendi ağırlıklarını ve kendi ağırlıklarıyla birlikte başka ağırlıkları da mutlaka taşıyacaklar, source:29:13}. Yükün paylaşılmazlığı ise dişil bir yüklüyle söylenir: {ar:وَإِن تَدْعُ مُثْقَلَةٌ إِلَىٰ حِمْلِهَا لَا يُحْمَلْ مِنْهُ شَىْءٌۭ وَلَوْ كَانَ ذَا قُرْبَىٰٓ, tr:ve in ted'u muskaletun ilâ himlihâ lâ yuhmel minhu şey'un ve lev kâne zâ kurbâ, gloss:yükü ağır bir kişi yüküne yardım için çağırsa, yakını bile olsa ondan hiçbir şey taşınmaz, source:35:18}. Kazanç ile yük bir ayette yan yana durur: {ar:وَلَا تَكْسِبُ كُلُّ نَفْسٍ إِلَّا عَلَيْهَا ۚ وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ, tr:ve lâ teksibu kullu nefsin illâ aleyhâ, ve lâ teziru vâziratun vizra uhrâ, gloss:her kişinin kazandığı yalnız kendi aleyhinedir; hiçbir yük taşıyan başkasının yükünü taşımaz, source:6:164}. Kadın sırtında yükünü taşır, kocası onun yükünü almaz, o da kocasınınkini.

Kaynaklar: 111:4 حَمَّالَةَ ح م ل B001; 111:4 حَمَّالَةَ ح م ل B006; 111:4 حَمَّالَةَ ح م ل B003; 111:4 حَمَّالَةَ ح م ل B007; 111:4 ٱلْحَطَبِ ح ط ب B001; 111:5 حَبْلٌۭ ح ب ل B001; 111:5 مَّسَدٍۭ م س د B001; 111:1 تَبَّتْ ت ب ب B003

## Buluşmalar

İlk buluşma birinci ayetin kendisindedir: kuruyan eller, alevle adlandırılmış adama aittir. Alev kökünün surenin ifadesini kendi adlandırma anlamının altında anması {source:"ل ه ب,B006"} iki imgeyi tek bir tamlamada tutar: kaybeden eller ile ateşe giden ad aynı kişinin iki yüzüdür. Elin kaybı ile ateş, ikinci ve üçüncü ayetin sırasında birleşir. Kur'an bu sırayı başka bir surede aynı kelimelerle kurar: önce {ar:وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ, tr:ve mâ yuğnî anhu mâluhû izâ teraddâ, gloss:yuvarlanıp düştüğünde malı ona fayda vermez, source:92:11}, birkaç ayet sonra {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona ancak en bedbaht olan girer, source:92:15}. Fayda vermeme fiili ile alev kelimesi de bir ayette yan yanadır {source:77:31}.

Alev ile yakıt, adın içinde buluşur. Baba kökü besleyeni adlandırır {source:"ء ب و,B001"}, odun ise yakmak için hazırlanan şeydir {source:"ح ط ب,B001"}. Alevin babası alevi besleyen olarak birinci ayette durur, alevin yakıtı dördüncü ayette sırtta taşınır, ve ikisi üçüncü ayetin ateşinde birleşir. Aynı ateş ev ocağıyla da buluşur: yakma fiilinin kökü hem ısınılan ocağı hem Ateşi adlandırır {source:"ص ل ي,B004"}. Mûsâ'nın ailesine getirdiği ateşte {ar:لَعَلَّكُمْ تَصْطَلُونَ, tr:lealekum tastalûn, gloss:belki ısınırsınız, source:27:7} ile surenin {ar:سَيَصْلَىٰ, tr:se-yaslâ, gloss:yanacak, source:111:3} kelimesi aynı kökün iki ucudur. Odun bir de söz odunudur: yakıt olarak taşınan ile laf olarak taşınan aynı kelimedir, ve laf insanlar arasında ateşin kökünden adını alan bir düşmanlık tutuşturur {source:"ن و ر,B007"}. Mal toplayan dedikoducunun tutuşturulmuş ateşe atıldığı sahne {source:104:6} ve savaş için yakılan ateşler {source:5:64} bu iki odunu tek sahnede tutar.

Sırttaki yük ile boyundaki ip, beşinci ayetin ipinde birleşir: yular yük hayvanının boyun ipidir {source:"ح ب ل,B001"}, mesed de deve yününden bükülen iptir {source:"م س د,B001"}. Sırtına yük vurulmuş bir hayvanın boynunda yular vardır; kadının sırtında odun, boynunda ip vardır. Kur'an yük ile süsü bir ayette birleştirir: buzağı olayında İsrailoğulları {ar:حُمِّلْنَآ أَوْزَارًۭا مِّن زِينَةِ ٱلْقَوْمِ, tr:hummilnâ evzâren min zîneti'l-kavm, gloss:kavmin süs eşyasından yükler yüklendik, source:20:87} derler. Süs yük olur; surede gerdanlığın yeri ip taşır. Kazanç ile yük de bir ayette buluşur {source:6:164}: birinci ve ikinci ayetin kazanan elleri ile dördüncü ayetin taşıyan sırtı, kişinin kazandığının kendi yükü oluşunun iki yarısıdır.

El ile boyun, birinci ve beşinci ayet arasında buluşur. Elin boyna bağlanmasını yasaklayan talimat {source:17:29} ve esirgenen malın boyun halkasına dönüşmesi {source:3:180}, surenin iki ucunu tek bir bedende birleştirir: kazanan el ile bağlanan boyun. İp kendi içinde üç sahneyi birden tutar: boyundaki halka, avcının tuzağı ve kesilen bağ. Gece gündüz kurulan düzenin boyunlardaki halkalarla bittiği ayet {source:34:33} halka ile tuzağı, Allah'ın ipine tutunmayı ateş çukurunun kıyısına koyan ayet {source:3:103} bağ ile ateşi birleştirir. Bükümün ipe verdiği güç, birinde birleştirmeye, ötekinde bir boynu bağlamaya gider.

Surenin hareketi bedenin üzerinden ilerler: birinci ayette eller, ikinci ayette ellerin tuttuğu mal ve kazanç, üçüncü ayette bütün bedenin girdiği ateş, dördüncü ayette sırt, beşinci ayette boyun. Adamın kazanan elleri ile kadının taşıyan sırtı aynı ateşe çalışır; biri kazandığının kendisine yetmediğini görür, öteki taşıdığı odunun yandığı yere bağlanır. İlk kelime ellere düşen bir kayıp ve bir kesiştir, son kelime boyna geçen bükülmüş bir ip; arada, adın içinde daha baştan yanan alev durur.

