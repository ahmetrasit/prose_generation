Focus: 87:5. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. No other command or tool is available.

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


===== _commentary/v16/work/87_5/D.r13/context.md =====
# 87:5 — focus

فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ

Anchor translation (canonical reading, reference only):

Sonra onu kapkara bir çerçöpe çevirdi.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَجَعَلَهُۥ | جَعَلَ | ج ع ل | CONJ;V;PRON |
| 2 | غُثَآءً | غُثَآء | غ ث و | N |
| 3 | أَحْوَىٰ | أَحْوَىٰ | ح و ي | ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 87 — full text (context; no pericope)

- 87:1 سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى
- 87:2 ٱلَّذِى خَلَقَ فَسَوَّىٰ
- 87:3 وَٱلَّذِى قَدَّرَ فَهَدَىٰ
- 87:4 وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ
- 87:5 ◀ focus فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ
- 87:6 سَنُقْرِئُكَ فَلَا تَنسَىٰٓ
- 87:7 إِلَّا مَا شَآءَ ٱللَّهُ ۚ إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ
- 87:8 وَنُيَسِّرُكَ لِلْيُسْرَىٰ
- 87:9 فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ
- 87:10 سَيَذَّكَّرُ مَن يَخْشَىٰ
- 87:11 وَيَتَجَنَّبُهَا ٱلْأَشْقَى
- 87:12 ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ
- 87:13 ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- 87:14 قَدْ أَفْلَحَ مَن تَزَكَّىٰ
- 87:15 وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ
- 87:16 بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- 87:17 وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ
- 87:18 إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ
- 87:19 صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ


===== _commentary/v16/work/87_5/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ج ع ل (root_000248) — identity root of فَجَعَلَهُۥ (w1)

- **B001** bir şeyi yapıp var etme — bir şeyi yapmak, yaratmak veya var etmek
  جعلت الشيء صنعته (maqayis)؛ جعل جعلا صنع صنعا (ayn)؛ جعل خلق؛ خلقنا (tahdhib)؛ يجري مجرى أوجد (mufradat)
- **B002** birini veya şeyi belirli bir duruma getirme — bir şeyi belirli bir duruma, niteliğe veya konuma getirmek · bir şeyi belirli bir duruma getirmek
  جعله الله نبيا أي صيره (sihah)؛ جعل صير؛ جعلته أحذق الناس؛ صيرهم؛ صيرته (tahdhib)
- **B003** öyle adlandırma ya da öyle olduğunu söyleme; başka yorumda öyle kılma — 
  جعلوا الملائكة إناثا أي سموهم (sihah)؛ جعل قال؛ أي قلناه؛ وقال غيره صيرناه (tahdhib)
- **B004** bir eylemi yapmaya başlama — bir şeyi yapmaya başlamak
  تقول جعل يقول ولا تقول صنع يقول (maqayis)؛ جعل يأكل وجعل يصنع كذا (ayn)؛ جعل فلان يصنع كذا كقولك طفق وعلق يفعل (tahdhib)؛ يجري مجرى صار وطفق فلا يتعدى نحو جعل زيد يقول (mufradat)
- **B005** iş karşılığı belirlenen ücret veya ortaklaşa kararlaştırılan ödeme — bir iş karşılığında belirlenen ücret, ödeme veya ödül · önemli bir iş için ortaklaşa kararlaştırılan ödemeler · ona bir ödeme veya armağan ayırmak
  الجعل والجعالة والجعلية ما يجعل للإنسان على الأمر يفعله (maqayis)؛ الجعل ما جعلت لإنسان أجرا له على عمل يعمله؛ الجعالات ما يتجاعل الناس بينهم (ayn)؛ الجعل ما جعل للانسان من شئ على الشئ يفعله؛ الجعالة؛ الجعيلة مثله (sihah)؛ الجعل في العطية؛ الجعالة بالفتح من الشيء تجعله للإنسان؛ ما جعلته للإنسان أجرا على عمله (tahdhib)
- **B006** kısa veya küçük hurma ağaçları — kısa veya küçük hurma ağaçları; tekili bu ağaçlardan biri
  الجعل النخل يفوت اليد والواحدة جعلة (maqayis)؛ الجعل واحدها جعلة وهي النخل الصغار (ayn)؛ الجعل النخل القصار الواحدة جعلة (sihah)؛ الجعل قصار النخل (tahdhib)
- **B007** sıcak tencereyi indirme bezi ve onunla indirme — sıcak tencereyi ateşten indirmeye yarayan koruyucu bez · tencereyi koruyucu bezle ateşten indirmek
  الجعال الخرقة التي تنزل بها القدر عن الأثافي (maqayis)؛ الجعال والجعالة خرقة تنزل بها القدر عن رأس النار يتقى بها من الحر (ayn)؛ الجعال الخرقة التي تنزل بها القدر عن النار؛ أجعلت القدر (sihah)؛ الجعال الخرقة التي تنزل بها القدور؛ أجعلت القدر إجعالا إذا أنزلتها بالجعال (tahdhib)
- **B008** kara küçük yer hayvanı ve bunlarla dolu su — kara renkli küçük bir yer hayvanı · bu hayvanların çokça bulunduğu su
  الجعل دابة من هوام الأرض (ayn)؛ الجعل دويبة؛ جعل الماء بالكسر أي كثر فيه الجعلان (sihah)؛ الجعل دابة سوداء من دواب الأرض تجمع جعلانا؛ ماء مجعل وجعل إذا تهافتت فيه الجعلان (tahdhib)
- **B009** dişinin çiftleşmek için erkeği istemesi — çiftleşmek isteyen dişi köpek · dişinin çiftleşmek için erkeği istemesi
  كلبة مجعل إذا أرادت السفاد (maqayis)؛ أجعلت الكبة واستجعلت فهي مجعل إذا أرادت السفاد وكذلك سائر السباع (sihah)؛ أجعلت الكلبة والسباع كلها إذا اشتهت الفحل؛ استجعلت أيضا بمعناه (tahdhib)
- **B010** deve kuşu yavrusu — deve kuşu yavrusu
  الجعول ولد النعام (maqayis)؛ الجعول الرأل ولد النعام (tahdhib)
- **B011** belirtilmemiş bir yer adı — kimliği belirtilmemiş bir yer adı
  الجَعْلة اسم مكان (maqayis)
- **B012** kısa, şişman ve inatçı olma — kısa, şişman ve inatçı kişi
  الجعل القصر مع السمن واللجاج (tahdhib)

## غ ث و (root_001073) — identity root of غُثَآءً (w2)

- **B001** akışla taşınan veya sıvı yüzeyine çıkan döküntü — selin taşıdığı ya da suyun ve tencerenin yüzüne çıkan kuru bitki, köpük ve döküntü · vadi yüzeyde toplanan değersiz döküntüler getirdi · yüzeyde toplanan döküntü getirdi veya bunlarla doldu · selin taşıdığı kumaş parçası ve benzeri yüzey döküntüsü · selin taşıdığı yüzey döküntüleri · suda hayvan pisliği, yaprak, kamış ve benzeri döküntüler çoğaldı
  الغثاء غثاء السيل (maqayis)؛ الغثاء ما جاء به السيل من نبات قد يبس (ayn)؛ ما يحمله السيل من القماش (sihah)؛ غثا الماء إذا كثر فيه البعر والورق والقصب (tahdhib)؛ الغثاء غثاء السيل والقدر، ما يطفح ويتفرق من النبات اليابس وزبد القدر (mufradat)
- **B002** bitkiyi kuru ve ufalanmış hale getirmek — sel otlağı bir araya yığıp tadını giderdi · otlağı bir araya yığıp tadını giderdi · onu yeşillikten sonra kuru ve ufalanmış ota çevirdi
  غثا السيل المرتع إذا جمع بعضه إلى بعض وأذهب حلاوته (sihah;tahdhib)؛ جففه حتى صيره هشيما جافا كالغثاء (tahdhib)؛ يابسا بعد خضرته (tahdhib)؛ ما يطفح ويتفرق من النبات اليابس (mufradat)
- **B003** iç bulanması — içi bulandı ve rahatsız edici bir şeyle kabardı · bulantı ve iç bulanması · içi bozulup bulandı · iç bulanması ve bulantı
  غثت نفسه تغثي كأنها جاشت بشيء مؤذ (maqayis)؛ الغثيان خبث النفس وغثيت نفسه تغثى (ayn)؛ الغثيان خبث النفس وقد غثت نفسه تغثي غثيا وغثيانا (sihah)؛ غثت نفسه تغثى غثيا وغثيانا (tahdhib)؛ غثت نفسه تغثي غثيانا خبثت (mufradat)
- **B004** değersiz görülüp önemsenmeyen kimse veya şey — toplumun aşağı ve değersiz görülen kesimi · değer verilmeyip boşa giden şey
  يقال لسفلة الناس الغثاء تشبيها بالذي ذكرناه (maqayis)؛ يضرب به المثل فيما يضيع ويذهب غير معتد به (mufradat)

## ح و ي (root_000374) — identity root of أَحْوَىٰ (w3)

- **B001** toplayıp güvenceye veya denetim altına alma — bir şeyi toplamak ve güvenceye almak · üzerinde denetim kurup kendi tasarrufuna almak · hak kazandıktan sonra sahip olan kimse
  حويت الشيء أحويه حيا إذا جمعته (maqayis)؛ حوى فلان مالا حيا وحواية أي جمعه وأحرزه واحتوى عليه (ayn;tahdhib)؛ احتوى فلان على كذا إذا استولى عليه (jamhara)؛ حواه يحويه حيا أي جمعه واحتواه مثله (sihah)؛ الحوي المالك بعد استحقاق (tahdhib)
- **B002** toplanıp dairesel biçimde kıvrılma — dairesel biçimde kıvrılma · toplanıp kıvrılarak halka olmak
  الحوي استدارة كل شيء كحوي الحية وكحوي بعض النجوم (ayn;tahdhib)؛ تحوى أي تجمع واستدار يقال تحوت الحية (sihah)
- **B003** bağırsaklar ve karındaki kıvrımlı bölümleri — bağırsak veya bağırsakların bir bölümü · bağırsağın kıvrımlı bir bölümü · bağırsakların tek bir kıvrımlı bölümü · bağırsaklar ve karındaki kıvrımlı iç bölümler
  الحوية والواحدة من الحوايا وهي الأمعاء (maqayis)؛ الحوية والحاوية والجميع الحوايا الأمعاء (ayn)؛ الحاوية والحاوياء الأمعاء التي تسمى بنات اللبن (jamhara)؛ حوية البطن وحاوية البطن وحاوياء البطن كله بمعنى وجمع الحوية حوايا وهي الأمعاء (sihah)؛ هي المباعر وبنات اللبن وهي الحواية والحاوية وهي الدوارة التي في بطن الشاة (tahdhib)
- **B004** kadın bineği veya hörgüç çevresine sarılan binme minderi — kadın bineği veya hörgüç çevresine sarılan binme minderi · üzerine binilen taşıma düzenekleri
  الحوية كساء يحوي حول سنام البعير ثم يركب (maqayis;tahdhib)؛ الحوية مركب يهيأ للمرأة (ayn;tahdhib)؛ الحوية مركب من مراكب النساء ليس بحدج ولا هودج (jamhara)؛ الحوية كساء محشو يدار حول سنام البعير (sihah)؛ الحوية شبيهة بالمحفة تركبها النساء (jamhara)
- **B005** tek barınak veya yakın barınaklardan oluşan yerleşim kümesi — tek çadır veya yakın çadırlardan oluşan konaklama kümesi · konaklama kümeleri · topluluğun evlerinin bir araya geldiği yer · toplu konaklama yeri · aynı konaklama kümesinde yaşayan topluluk
  الحي من أحياء العرب والحواء البيت الواحد (maqayis)؛ الحواء جماعة بيوت من الناس مجتمعة والجمع الأحوية وهي من الوبر (sihah)؛ الحواء أخبية تدانى بعضها من بعض وهم أهل حواء واحد وجمع الحواء أحوية (tahdhib)؛ لمجتمع بيوت الحي محوى وحواء ومحتوى والجميع أحوية ومحاء (tahdhib)
- **B006** siyah veya siyaha çalan koyu kızıl, esmer ya da yeşil renk — siyaha çalan koyu kızıl veya koyu esmer renk · siyah ya da siyah karışmış koyu yeşil renkli · siyah veya siyaha çalan koyu renkli dişi · atın siyah veya siyaha çalan koyu renge dönüşmesi
  الحوة شية من شيات الخيل وهي بين الدهمة والكمتة وكل أسود أحوى وامرأة حواء (jamhara)؛ الحوة لون يخالط الكمتة وحمرة تضرب إلى السواد والحوة سمرة الشفة وبعير أحوى إذا خالط خضرته سواد وصفرة (sihah)؛ الأحوى من الخيل هو الأحمر السراة والحوة في الشفاه شبيه باللمى والأحوى الأسود من الخضرة (tahdhib)
- **B007** ok uçlu yapraklı veya kurt renkli belirli bir ot — belirli bir ot veya otsu bitki · bu bitkinin tek bir örneği · aynı bitkinin sığırla ilişkilendirilen türü · tuzcul çalılar arasında yetişen kaba türü
  الحواء ضرب من البقل يشبه ورقه بنصال السهام (jamhara)؛ الحواء نبت يشبه لون الذئب الواحدة حواءة (sihah)؛ الحواء نبت معروف الواحدة حوءة وحواء الذعاليق وحواء البقر وحواء الكلاب (tahdhib)
- **B008** suyu tutan küçük yalak, kıvrımlı çukur veya çevrili yüzey — deve sulamak için yapılmış küçük yalak · sel suyunu tutan kıvrımlı çukurlar veya çevrili yüzeyler
  الحوي الحويض الصغير يسويه الرجل لبعيره يسقيه فيه (tahdhib)؛ الحوايا التي تكون في القيعان والرياض حفائر ملتوية يملؤها ماء السيل (tahdhib)؛ الحوايا المساطح وهو أن يعمدوا إلى الصفا فيحوون له ترابا وحجارة ليحبس عليهم الماء (tahdhib)
- **B009** hasta veya rahatsız kimse — hasta veya rahatsız kimse
  الحوي العليل والدوي الأحمق مشددات كلها (tahdhib)

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 87:5, and ## Buluşmalar) =====
## Gökten otlağa: bulut, ilk yağmur ve kararan ot

Surenin ilk beş ayeti bir bitkinin bütün ömrünü kısa tutarak anlatır. Dördüncü ayet {ar:وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ, tr:velleẕî ahrace'l-mer'â, gloss:otlağı çıkaran O'dur, source:87:4} der, beşinci ayet ise {ar:فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ, tr:fe-ce'alehû ğuŝâen ahvâ, gloss:sonra onu kapkara bir sel döküntüsüne çevirdi, source:87:5} diye biter. İki ayet arasında otu topraktan çıkaran şeyin, yani yağmurun adı geçmez. Bu eksik halkayı surenin başka kelimelerinin aileleri tamamlar. Burada ve sonraki bölümlerde, bir kelimenin kök ailesinden gelen görüntü kelimenin kendi ayetindeki anlamının yanında duyulur, hiçbir zaman onun yerine geçmez. Birinci ayetteki "ad" yine addır, "Rab" yine Rab'dir. Aile görüntüsü, bu anlamın arkasında Arapçayı bilen kulağa ayrıca ulaşan sahnedir.

Birinci ayet {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:yüce Rabbinin adını tesbih et, source:87:1} der. "Ad" anlamındaki اسم kelimesi س م و kökündendir ve bu kök gökyüzünü de verir. Araplar için {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tusemmi's-sehâbe semâen ve'l-matara semâen, gloss:Araplar buluta da yağmura da semâ der, source:"س م و,B004"}, ve aynı ad yağmurun bitirdiği ota da verilir: {ar:يسموا النبات سماء, tr:yusemmû'n-nebâte semâen, gloss:bitkiye de semâ derler, source:"س م و,B004"}. Ölçüt basittir: {ar:السماء كل ما علاك فأظلك, tr:es-semâu kullu mâ alâke fe-ezalleke, gloss:semâ senin üstüne çıkıp sana gölge salan her şeydir, source:"س م و,B004"}. Tek bir kök böylece başın üstündeki örtüden buluta, buluttan yağmura, yağmurdan topraktan çıkan ota kadar uzanan bütün dikey sütunu kapsar. "Rab" kelimesinin ailesi bu sütunun içinde belirli bir bulutu gösterir: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb sumiye bi-ẕâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur; bitkiyi besleyip büyüttüğü için bu adı almıştır, source:"ر ب ب,B008"}. Bu, ötekilerin altında sarkan alçak buluttur: {ar:السحاب المتعلق دون السحاب, tr:es-sehâbu'l-muteallaku dûne's-sehâb, gloss:bulutların altında asılı duran bulut, source:"ر ب ب,B008"}. Aynı kök bulutun bir yerde durup gitmemesini de söyler: {ar:أربت السحابة: دامت, tr:erabbeti's-sehâbe dâmet, gloss:bulut durdu ve sürdü, source:"ر ب ب,B007"}. Aynı kalıp güney rüzgârı için de kullanılır: {ar:أربت الجنوب والسحابة أي دامت, tr:erabbeti'l-cenûbu ve's-sehâbe ey dâmet, gloss:güney rüzgârı da bulut da sürdü, source:"ر ب ب,B007"}. Bulutu süren bu rüzgârın adı olan cenûb, on birinci ayetteki يَتَجَنَّبُهَا kelimesiyle aynı köktendir: {ar:الجنوب ريح تجيء عن يمين القبلة, tr:el-cenûbu rîhun tecîu an yemîni'l-kıble, gloss:cenûb kıblenin sağ yanından gelen rüzgârdır, source:"ج ن ب,B006"}.

Bulut ilk belirdiğinde Arapça ona dördüncü ayetin fiilinden bir ad verir: {ar:الخروج السحاب أول ما يبدأ, tr:el-hurûc es-sehâbu evvele mâ yebdeu, gloss:hurûc bulutun ilk belirişidir, source:"خ ر ج,B005"}. Bulutun kenarlarında zayıf bir şimşek çakar. Bunu anlatan fiil, yedinci ayetteki يَخْفَىٰ ile aynı köktendir: {ar:خفا البرق يخفو خفوا ويخفى خفيا إذا لمع لمعا ضعيفا معترضا في نواحى الغيم, tr:hafe'l-berku yahfû hufuvven ve yahfî hafyen iẕâ leme'a lem'an daîfen mu'teridan fî nevâhi'l-ğaym, gloss:şimşek bulutun kenarlarında yan yan zayıfça parladığında hafâ denir, source:"خ ف ي,B004"}. Bu ışığı bütün gece gözleyen kişiyi ise on yedinci ayetteki أَبْقَىٰٓ kelimesinin kökü anlatır: {ar:بات فلان يبقي البرق أي ينظر إليه من أين يلمع, tr:bâte fulânun yubkı'l-berka ey yenzuru ileyhi min eyne yelma', gloss:falanca şimşeğin nereden çakacağına bakarak geceyi geçirdi, source:"ب ق ي,B005"}. Sonunda yağmur gelir ve adını verdiği hayattan alır: {ar:يسمى المطر حيا لأن به حياة الأرض, tr:yusemme'l-mataru hayâen li-enne bihî hayâte'l-ard, gloss:yağmura hayâ denir çünkü yerin hayatı onunladır, source:"ح ي ي,B002"}. On üçüncü ayetteki يَحْيَىٰ fiili ve on altıncı ayetteki ٱلْحَيَوٰةَ kelimesi bu köktendir. Yağmur yuvalarındaki fareleri de dışarı sürer. Bu sürüş yine "gizli" kökünden bir fiille söylenir, açıklaması da dördüncü ayetin fiiliyle yapılır: {ar:وخفا المطر الفأر من حجرتهن أخرجهن, tr:ve hafe'l-mataru'l-fe'ra min hucurâtihinne ahracehunne, gloss:yağmur fareleri deliklerinden çıkardı, source:"خ ف ي,B003"}.

اسم kelimesi için Arapçada kayıtlı ikinci bir türetme vardır. Bu türetme kelimeyi "damga" anlamındaki وسم köküne bağlar. Bu, kök kimliği değil, kayıtlı bir alternatiftir. Ama bu yoldan da aynı sahneye varılır, çünkü yılın ilk yağmurunun adı bu köktendir: {ar:سمي الوسمي من المطر وسميا لأنه يسم الأرض بالنبات فيصير فيها أثرا في أول السنة, tr:sumiye'l-vesmiyyu mine'l-matari vesmiyyen li-ennehû yesimu'l-arda bi'n-nebâti fe-yasîru fîhâ eseran fî evveli's-sene, gloss:ilk yağmura vesmî denir çünkü yeri bitkiyle damgalar ve yılın başında yerde bir iz olur, source:"و س م,B003"}. Yağmur toprağa yeşil bir iz basar.

Dördüncü ayetin fiili أخرج, somut bir şeyin bulunduğu yerden dışarı alınmasıdır: {ar:الإخراج أكثر ما يقال في الأعيان, tr:el-ihrâcu ekŝeru mâ yukâlu fi'l-a'yân, gloss:ihrâc çoğunlukla somut şeyler için söylenir, source:"خ ر ج,B002"}. Ot gerçekten topraktan çekilip çıkarılan bir şeydir. Aynı kökün ailesi ilk çıkışın görünüşünü de verir: {ar:أرض مخرجة نبتها في مكان دون مكان, tr:ardun muhrecetun nebtuhâ fî mekânin dûne mekân, gloss:otu bir yerde bitip başka yerde bitmeyen toprak, source:"خ ر ج,B007"}. İlk yeşil, toprağa yama yama düşer. Aynı ailede bir renk adı da vardır: {ar:الأخرج لون سواده أكثر من بياضه, tr:el-ahrecu levnun sevâduhû ekŝeru min beyâdih, gloss:karası akından çok olan renk, source:"خ ر ج,B007"}. المرعى ise tek kelimede otu, otlağın yerini ve otlamanın kendisini birlikte taşır: {ar:المرعى الرعي والموضع والمصدر, tr:el-mer'â er-ra'yu ve'l-mevdiu ve'l-masdar, gloss:mer'â hem ot hem yer hem otlamadır, source:"ر ع ي,B001"}.

Beşinci ayetteki جعل, bir şeyi bir halden başka bir hale çevirmektir: {ar:جعل صير, tr:ce'ale sayyera, gloss:ce'ale bir şeyi başka bir hale soktu demektir, source:"ج ع ل,B002"}. Otun çevrildiği şey olan غثاء, otun sonunu üç adımda anlatır: ot kurur, tadını yitirir, sel onu yığıp götürür. {ar:غثا السيل المرتع إذا جمع بعضه إلى بعض وأذهب حلاوته, tr:ğaŝe's-seylu'l-merte'a iẕâ ceme'a ba'dahû ilâ ba'din ve eẕhebe halâvetehû, gloss:sel otlağı üst üste yığıp tadını giderdiğinde ğaŝâ denir, source:"غ ث و,B002"}. Ot bu noktada {ar:يابسا بعد خضرته, tr:yâbisen ba'de hudratihî, gloss:yeşilliğinden sonra kurumuş olarak, source:"غ ث و,B002"} kalır. غثاء de {ar:الغثاء ما جاء به السيل من نبات قد يبس, tr:el-ğuŝâu mâ câe bihi's-seylu min nebâtin kad yebise, gloss:ğuŝâ selin getirdiği kurumuş bitkidir, source:"غ ث و,B001"}. Ardından gelen أحوى bir renktir: {ar:الأحوى الأسود من الخضرة, tr:el-ahvâ el-esvedu mine'l-hudra, gloss:ahvâ yeşilden kararmış olandır, source:"ح و ي,B006"}. Bir deve için de {ar:بعير أحوى إذا خالط خضرته سواد وصفرة, tr:baîrun ahvâ iẕâ hâlata hudratehû sevâdun ve sufra, gloss:yeşiline kara ve sarı karışmış deveye ahvâ denir, source:"ح و ي,B006"}. Rengin adı {ar:حُوَّة, tr:huvve, gloss:yeşile çalan koyu renk, source:"memory"} kelimesidir. Ayette kelime غثاء'nın sıfatı olarak durur. Ama tanımı hem gür yeşilin koyuluğunu hem de çürüyen otun kararmasını kapsar. Bu yüzden tek kelime otun iki ucunu, taze koyuluğu ve kapkara döküntüyü yan yana tutar. Kur'an gür yeşilin koyuluğunu başka bir yerde tek kelimeyle, cennet bahçeleri için verir: {ar:مُدْهَآمَّتَانِ, tr:müdhâmmetân, gloss:yeşillikten koyu kara görünen iki bahçe, source:55:64}.

Bu sahne surenin geri kalanında karşılık bulur. On üçüncü ayetteki "yaşamak" fiilinin ailesi diri otu {ar:الحي من النبات ما كان طريا يهتز, tr:el-hayyu mine'n-nebâti mâ kâne tariyyen yehtezzu, gloss:bitkinin dirisi taze olup titreşenidir, source:"ح ي ي,B002"} diye tanımlar. "Ölmek" fiilinin ailesi de {ar:الموتان الأرض لم تحي بعد بزرع ولا إصلاح, tr:el-mevtân el-ardu lem tuhye ba'du bi-zer'in ve lâ islâh, gloss:mevtân ekinle ya da bakımla henüz diriltilmemiş topraktır, source:"م و ت,B003"}. Otun yolculuğu böylece ölü topraktan titreşen yeşile, oradan kuru döküntüye uzanır. On üçüncü ayetin ateşteki adam için söylediği şey ise bu uçlardan hiçbirinde olmamaktır. "Rab" kelimesinin ailesinde bu yolculuğun karşısında duran bir bitki adı da vardır: {ar:اسم لعدة من النبات لا تهيج في الصيف, tr:ismun li-iddetin mine'n-nebâti lâ tehîcu fi's-sayf, gloss:yazın sararıp kurumayan birkaç bitkinin adı, source:"ر ب ب,B012"}. Kur'an dünya hayatı benzetmesinde tam da bu "sararıp kurumak" fiilini kullanır. Rab adının ailesindeki sararmayan ot bu sayede otlağın kaderinin karşısına konabilir. Bu bağı dil değil, okuma kurar.

Kur'an bu yolculuğu kendi sözleriyle sahneler. Allah kendini, rüzgârları rahmetinin önünde müjdeci olarak gönderen ve ağır bulutları ölü bir beldeye süren olarak anlatır, sonra şöyle der: {ar:فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:fe-enzelnâ bihi'l-mâe fe-ahracnâ bihî min kulli'ŝ-ŝemerât keẕâlike nuhrici'l-mevtâ leallekum teẕekkerûn, gloss:oraya suyu indirdik ve onunla her türlü üründen çıkardık; ölüleri de böyle çıkarırız; belki düşünüp hatırlarsınız, source:7:57}. Çıkarmak fiili burada hem bitkiye hem ölülere, sonunda da hatırlamaya bağlanır. Sure de dördüncü ayetteki çıkarmadan dokuzuncu ayetteki hatırlatmaya aynı yolla uzanır. Hemen sonraki ayet, iyi toprağın bitkisini {ar:بِإِذْنِ رَبِّهِۦ, tr:bi-izni rabbih, gloss:Rabbinin izniyle, source:7:58} çıkardığını söyler. Başka bir yerde Allah gökten bereketli su indirip onunla ölü bir beldeyi dirilttiğini anlatır ve {ar:كَذَٰلِكَ ٱلْخُرُوجُ, tr:keẕâlike'l-hurûc, gloss:çıkış da böyledir, source:50:11} der. Firavun Musa'ya {ar:فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:fe-men rabbukumâ yâ mûsâ, gloss:ikinizin Rabbi kimdir ey Musa, source:20:49} diye sorduğunda Musa'nın cevabı bu surenin ilk ayetlerindeki sırayı izler: {ar:رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:rabbunelleẕî a'tâ kulle şey'in halkahû ŝumme hedâ, gloss:Rabbimiz her şeye yaratılışını veren sonra yol gösterendir, source:20:50}. Birkaç ayet sonra gökten su indirilir ve {ar:فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ, tr:fe-ahracnâ bihî ezvâcen min nebâtin şettâ, gloss:onunla çeşit çeşit bitkiden çiftler çıkardık, source:20:53}. Surenin son ayetinde sayfaları anılan Musa, Rabbini tanıtırken aynı yaratma, yol gösterme ve çıkarma sırasını kullanır. Bir başka yerde yeryüzü için {ar:أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا, tr:ahrace minhâ mâehâ ve mer'âhâ, gloss:ondan suyunu ve otlağını çıkardı, source:79:31} denir.

Kur'an otun ikinci yarısını, yani kuruyup savrulmasını, dünya hayatının benzetmesi yapar. İki bahçe sahibinin hikâyesinden sonra Allah Peygamber'e şöyle der: {ar:وَٱضْرِبْ لَهُم مَّثَلَ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ, tr:vadrib lehum meŝele'l-hayâti'd-dunyâ ke-mâin enzelnâhu mine's-semâ, gloss:onlara dünya hayatının örneğini ver; gökten indirdiğimiz bir su gibidir, source:18:45}. Yerin bitkisi o suyla karışır, sonra {ar:هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ, tr:heşîmen teẕrûhu'r-riyâh, gloss:rüzgârların savurduğu kuru çöp, source:18:45} olur. Hemen sonraki ayet karşı kefeyi koyar: {ar:وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا, tr:ve'l-bâkıyâtu's-sâlihâtu hayrun inde rabbike sevâben, gloss:kalıcı iyi işler ise Rabbinin katında karşılık bakımından daha hayırlıdır, source:18:46}. Bu iki ayet, beşinci ayetteki döküntüyü on altıncı ve on yedinci ayetteki "dünya hayatı" ile "daha hayırlı ve daha kalıcı" ayrımına bağlayan köprüyü Kur'an'ın kendi ağzından kurar. Aynı benzetme başka bir yerde şu sözlerle gelir: {ar:ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا, tr:ŝumme yehîcu fe-terâhu musferran ŝumme yekûnu hutâmâ, gloss:sonra kurur da onu sapsarı görürsün sonra çer çöp olur, source:57:20}. Bir başka yerde aynı süreç {ar:ثُمَّ يَجْعَلُهُۥ حُطَٰمًا ۚ إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ, tr:ŝumme yec'aluhû hutâmâ inne fî ẕâlike le-ẕikrâ, gloss:sonra onu çer çöpe çevirir; bunda elbette bir öğüt vardır, source:39:21} sözleriyle anlatılır. Bu cümle beşinci ayetteki "çevirdi" fiilini ve dokuzuncu ayetteki "öğüt" kelimesini bir arada tutar. Başka bir yerde yeryüzü süslenir, sahipleri ona güç yetirdiklerini sanır, sonra buyruk gelir: {ar:فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:fe-ce'alnâhâ hasîden ke-en lem teğne bi'l-ems, gloss:onu dün hiç yokmuş gibi biçilmiş hale getirdik, source:10:24}. Kelimenin kendisi de Kur'an'da bir topluluk için kullanılır. Bir önceki kavimden sonra yaratılan bir neslin hikâyesinde, onları yakalayan çığlığın ardından şöyle denir: {ar:فَجَعَلْنَٰهُمْ غُثَآءًۭ, tr:fe-ce'alnâhum ğuŝâen, gloss:onları sel döküntüsüne çevirdik, source:23:41}. Fiil de kelime de aynıdır, ama burada ot yerine insanlar vardır.

Kaynaklar: 87:1 ٱسْمَ س م و B004; 87:1 ٱسْمَ و س م B003; 87:1 رَبِّ ر ب ب B008; 87:1 رَبِّ ر ب ب B007; 87:1 رَبِّ ر ب ب B012; 87:11 يَتَجَنَّبُهَا ج ن ب B006; 87:4 أَخْرَجَ خ ر ج B005; 87:4 أَخْرَجَ خ ر ج B002; 87:4 أَخْرَجَ خ ر ج B007; 87:4 ٱلْمَرْعَىٰ ر ع ي B001; 87:5 فَجَعَلَهُۥ ج ع ل B002; 87:5 غُثَآءً غ ث و B002; 87:5 غُثَآءً غ ث و B001; 87:5 أَحْوَىٰ ح و ي B006; 87:7 يَخْفَىٰ خ ف ي B004; 87:7 يَخْفَىٰ خ ف ي B003; 87:17 أَبْقَىٰٓ ب ق ي B005; 87:13 يَحْيَىٰ ح ي ي B002; 87:13 يَمُوتُ م و ت B003

## Sel: köpük gider, su kalır

Beşinci ayetteki غثاء yalnızca kurumuş ot değildir, selin yüzünde yüzen şeydir de. Arapça onu iki ayrı kaba birden koyar: {ar:الغثاء غثاء السيل والقدر، ما يطفح ويتفرق من النبات اليابس وزبد القدر, tr:el-ğuŝâu ğuŝâu's-seyli ve'l-kıdr mâ yatfahu ve yetefarraku mine'n-nebâti'l-yâbisi ve zebedi'l-kıdr, gloss:ğuŝâ selin de tencerenin de ğuŝâsıdır; kuru bitkiden ve tencere köpüğünden yüzeye taşıp dağılandır, source:"غ ث و,B001"}. Kelime bir atasözü değeri de taşır: {ar:يضرب به المثل فيما يضيع ويذهب غير معتد به, tr:yudrabu bihi'l-meŝelu fî mâ yadîu ve yeẕhebu ğayra mu'teddin bih, gloss:kaybolup giden ve hesaba katılmayan şey için örnek olarak anılır, source:"غ ث و,B004"}. Selin öbür yüzü sudur. Surenin kelimelerinin aileleri suyun nerede toplanıp kaldığını gösterir.

İkinci ayetteki "yarattı" fiilinin ailesinde kayalardaki oyuklar vardır: {ar:الخليقة نقر في صخرة يجتمع فيه ماء السماء, tr:el-halîka nakrun fî sahratin yectemiu fîhi mâu's-semâ, gloss:halîka kayada gök suyunun toplandığı oyuktur, source:"خ ل ق,B011"}. Bu oyuklar şöyle de anlatılır: {ar:قلاتا تمسك ماء السحاب في صفاة خلقها الله فيها تسميها العرب الخلائق, tr:kılâten tumsiku mâe's-sehâbi fî safâtin halakahallâhu fîhâ tusemmîhe'l-arabu'l-halâik, gloss:Allah'ın düz kayada yarattığı ve bulut suyunu tutan çukurlar; Araplar onlara halâik der, source:"خ ل ق,B011"}. Beşinci ayetteki أحوى'nın ailesinde selin doldurduğu kıvrımlı çukurlar vardır: {ar:الحوايا التي تكون في القيعان والرياض حفائر ملتوية يملؤها ماء السيل, tr:el-havâyâ elletî tekûnu fi'l-kîâni ve'r-riyâdi hafâiru multeviyetun yemleuhâ mâu's-seyl, gloss:havâyâ düzlüklerde ve çayırlarda selin doldurduğu kıvrımlı çukurlardır, source:"ح و ي,B008"}. "Rab" kelimesinin ailesinde bol su, toplandığı için bu adı alır: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabeb ve huve'l-mâu'l-keŝîr sumiye bi-ẕâlike li-ictimâih, gloss:rabeb boldur ve toplandığı için bu adı almıştır, source:"ر ب ب,B013"}. Yedinci ayetteki "açık" kelimesinin ailesinde kuyu temizlenir: {ar:جهرت الركية إذا كان ماؤها قد غطى الطين فنقى ذلك حتى يظهر الماء ويصفو, tr:cehertu'r-rakiyye iẕâ kâne mâuhâ kad ğattâhu't-tînu fe-nakkâ ẕâlike hattâ yezhera'l-mâu ve yesfû, gloss:suyunu çamur örtmüş kuyuyu su görünüp duruluncaya kadar temizledim, source:"ج ه ر,B008"}. Aynı ayetteki "bilir" fiilinin ailesinde de suyu bol kuyu vardır: {ar:العيلم البئر الكثيرة الماء, tr:el-aylem el-bi'ru'l-keŝîratu'l-mâ, gloss:aylem suyu bol kuyudur, source:"ع ل م,B005"}.

Dokuzuncu ayet öğütten "fayda verirse" diye söz eder, on yedinci ayet ahireti "daha kalıcı" diye niteler. Fayda, {ar:ما يستعان به في الوصول إلى الخيرات, tr:mâ yusteânu bihî fi'l-vusûli ile'l-hayrât, gloss:iyiliklere ulaşmak için yardım alınan şey, source:"ن ف ع,B001"} diye tanımlanır. Bu tanım on yedinci ayetteki "hayırlı" kelimesinin kökünü de taşır. Kalıcılık ise şudur: {ar:البقاء ثبات الشيء على حاله الأولى وهو يضاد الفناء, tr:el-bekâu ŝebâtu'ş-şey'i alâ hâlihi'l-ûlâ ve huve yudâddu'l-fenâ, gloss:bekâ bir şeyin ilk halinde sabit durmasıdır ve yok olmanın zıddıdır, source:"ب ق ي,B001"}. Bu tanımda on sekizinci ayetteki "ilk" kelimesi de vardır.

Kur'an'da bu iki yüzü bir sahnede toplayan benzetmeyi Allah verir. Gökten su iner, vadiler {ar:فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا, tr:fe-sâlet evdiyetun bi-kaderihâ, gloss:vadiler kendi ölçülerince akar, source:13:17}. Burada üçüncü ayetteki "ölçtü" fiilinin kökü geçer. Sel kabarık bir köpük taşır. İnsanların süs ya da eşya için ateşte erittikleri madenin de benzer bir köpüğü vardır. Sonra ayırım gelir: {ar:فَأَمَّا ٱلزَّبَدُ فَيَذْهَبُ جُفَآءًۭ ۖ وَأَمَّا مَا يَنفَعُ ٱلنَّاسَ فَيَمْكُثُ فِى ٱلْأَرْضِ, tr:fe-emme'z-zebedu fe-yeẕhebu cufâen ve emmâ mâ yenfau'n-nâse fe-yemkuŝu fi'l-ard, gloss:köpük atılıp gider; insanlara fayda veren ise yerde kalır, source:13:17}. Kelime farklıdır, orada غثاء değil زبد geçer. Ama sahne aynıdır. Surenin beşinci, dokuzuncu ve on yedinci ayetlere dağıttığı döküntü, fayda ve kalıcılık bu ayette tek bir selin içinde bir aradadır. Bu yan yana koyuş surenin kendi sözü değildir, ama bu ayet ona Kur'an'dan bir dayanak verir. Fayda verirse sunulan öğüt, kayadaki oyukta tutulan suya benzer. Çerçöp ise akıntıyla gidip hesaba katılmayan şeydir.

Kaynaklar: 87:5 غُثَآءً غ ث و B001; 87:5 غُثَآءً غ ث و B004; 87:9 نَّفَعَتِ ن ف ع B001; 87:17 أَبْقَىٰٓ ب ق ي B001; 87:2 خَلَقَ خ ل ق B011; 87:5 أَحْوَىٰ ح و ي B008; 87:1 رَبِّ ر ب ب B013; 87:7 ٱلْجَهْرَ ج ه ر B008; 87:7 يَعْلَمُ ع ل م B005

## Yol ve binek: önde giden, kolaylaşan, yana çekilen

Üçüncü, sekizinci ve on birinci ayetler bir yolculuğun izini sürer. هدى önden gidip yolu göstermektir: {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytuhu't-tarîka ve'l-beyte hidâyeten ey arraftuh, gloss:ona yolu ve evi gösterdim yani tanıttım, source:"ه د ي,B001"}. {ar:التقدم للإرشاد, tr:et-tekaddumu li'l-irşâd, gloss:yol göstermek için öne geçmek, source:"ه د ي,B001"}. {ar:الدليل يسمى هاديا لتقدمه, tr:ed-delîlu yusemmâ hâdiyen li-tekaddumih, gloss:kılavuza önden gittiği için hâdî denir, source:"ه د ي,B003"}. Aynı kök zayıf birinin iki kişiye dayanarak yürümesini de anlatır: {ar:يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله, tr:yuhâdî beyne'sneyni iẕâ kâne yemşî beynehumâ mu'temiden aleyhimâ min da'fihî ve temâyulih, gloss:zayıflığından ve sendelemesinden iki kişinin arasında onlara dayanarak yürüdü, source:"ه د ي,B008"}. Telaşsız ve sakin bir yürüyüşü de anlatır: {ar:لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن, tr:lem yusri' isrâa'l-munhezimi ve lâkin alâ sukûnin ve hedyin hasen, gloss:kaçan biri gibi koşmadı; sakin ve güzel bir gidişle yürüdü, source:"ه د ي,B010"}. Sekizinci ayet {ar:وَنُيَسِّرُكَ لِلْيُسْرَىٰ, tr:ve nuyessiruke li'l-yusrâ, gloss:seni en kolaya kolaylaştıracağız, source:87:8} der. يسر hazır ve kolay olandır: {ar:الميسور: ضد المعسور، وتيسر واستيسر بمعنى تهيأ, tr:el-meysûr diddu'l-ma'sûr ve teyessera ve'steysera bi-ma'nâ teheyyee, gloss:meysûr zor olanın zıddıdır; teyessera hazır oldu demektir, source:"ي س ر,B001"}. Kök kolay güdülen bineği de anlatır: {ar:يسر أي لين الانقياد سريع المتابعة يوصف به الإنسان والفرس, tr:yesrun ey leyyinu'l-inkıyâdi serîu'l-mutâbaa yûsafu bihi'l-insânu ve'l-feres, gloss:yesr kolay güdülen ve çabuk ardından gelen demektir; insan ve at için söylenir, source:"ي س ر,B005"}. Hafif bacakları da anlatır: {ar:اليسرات: القوائم الخفاف, tr:el-yeserât el-kavâimu'l-hıfâf, gloss:yeserât hafif bacaklardır, source:"ي س ر,B005"}. Sekizinci ayetin fiili düz anlamında Peygamber'e verilen bir vaattir. Aile resmi bu vaade bir binek görüntüsü katar: üzerindekinin isteğine kolayca uyan ve yolu hafif adımlarla alan bir hayvan.

On birinci ayetteki الأشقى'nın kökü zahmettir: {ar:أصل يدل على المعاناة وخلاف السهولة, tr:aslun yedullu ale'l-muânâti ve hilâfi's-suhûle, gloss:katlanmayı ve kolaylığın zıddını gösteren köktür, source:"ش ق و,B002"}. Ama aynı kök bir dağ sırtını da adlandırır, ve bu tanımda üç kök birden geçer: {ar:الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان, tr:eş-şâkî min huyûdi'l-cibâli't-tâliu't-tavîl ve mea tûlihî eyseru suûden ve akdaru mak'aden li'l-insân, gloss:şâkî dağ çıkıntılarından uzun yükselen sırttır; uzunluğuna rağmen tırmanması daha kolay ve insan için oturmaya daha elverişlidir, source:"ش ق و,B004"}. "Zahmet" kelimesinin kökü burada "daha kolay" ve "ölçüye daha uygun" kelimeleriyle aynı cümlededir. Bu yüzden yol aynı olabilir. Fark, yolcunun onu nasıl yürüdüğündedir. On birinci ayetin fiili ise yolculuğun bir başka hareketidir. جنب bir hayvanı yanında yedeğe almaktır: {ar:جنبت الدابة إذا قدتها إلى جنبك وكذلك جنبت الأسير, tr:cenebtu'd-dâbbete iẕâ kudtuhâ ilâ cenbike ve keẕâlike cenebtu'l-esîr, gloss:hayvanı yanında yedeğe aldım; esiri de öyle, source:"ج ن ب,B005"}. Ayetteki biçim ise bir şeyi yanında uzak tutmaktır: {ar:جانبه وتجانبه وتجنبه واجتنبه كله بمعنى وجنبته الشيء أي نحيته عنه, tr:cânebehû ve tecânebehû ve teceннebehû ve'ctenebehû kulluhû bi-ma'nâ ve cenebtuhu'ş-şey'e ey nahheytuhû anh, gloss:cânebe tecânebe tecennebe ictenebe hep aynı anlamdadır; onu bir şeyden uzak tuttum yani o şeyi ondan ayırdım, source:"ج ن ب,B003"}. En bedbaht kişi öğüdü reddetmez, onun yanından geçer ve onu kendi yolunun kenarında tutar.

İkinci ayetin سوّى fiilinin ailesinde binicinin oturuşu vardır: {ar:استوى على ظهر دابته أي علا واستقر, tr:istevâ alâ zahri dâbbetihî ey alâ ve'stekarr, gloss:hayvanının sırtına oturdu yani üstüne çıkıp yerleşti, source:"س و ي,B003"}. Bu tanım birinci ayetteki yükseklik kökünü de içerir. Semere serilen örtü de bu ailedendir: {ar:السَّويّة كساء يلف ويجعل شبيها بالحوية يلقى على سنام البعير, tr:es-seviyye kisâun yuleffu ve yuc'alu şebîhen bi'l-haviyyeti yulkâ alâ senâmi'l-baîr, gloss:seviyye sarılıp haviyyeye benzetilerek devenin hörgücüne konan örtüdür, source:"س و ي,B010"}. Benzetildiği haviyye de beşinci ayetteki أحوى'nın kökündendir: {ar:الحوية كساء يحوي حول سنام البعير ثم يركب, tr:el-haviyye kisâun yahvî havle senâmi'l-baîri ŝumme yurkeb, gloss:haviyye devenin hörgücünü saran ve üstüne binilen örtüdür, source:"ح و ي,B004"}. Aynı kök yolun ortasını da adlandırır: {ar:مكان سوى أي عدل ووسط, tr:mekânun suven ey adlun ve vasat, gloss:dengeli ve orta bir yer, source:"س و ي,B006"}. Ama "cehennemin ortası" da bu kelimeyle söylenir: {ar:في سواء الجحيم, tr:fî sevâi'l-cahîm, gloss:cehennemin ortasında, source:"س و ي,B006"}.

Kur'an bu yolu sahneler. Yeminlerle açılan bir surede verenler ile cimrilik edenler ayrılır: {ar:فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ, tr:fe-senuyessiruhû li'l-yusrâ, gloss:onu en kolaya kolaylaştıracağız, source:92:7}, {ar:فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ, tr:fe-senuyessiruhû li'l-usrâ, gloss:onu en zora kolaylaştıracağız, source:92:10}. Aynı fiil iki yöne çalışır. Birinin bineği kolaylığa, ötekininki zorluğa gider. Ardından {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hudâ, gloss:yol göstermek elbette bize düşer, source:92:12} denir. İnsan için {ar:ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ, tr:ŝumme's-sebîle yesserah, gloss:sonra yolu ona kolaylaştırdı, source:80:20} ve {ar:إِنَّا هَدَيْنَٰهُ ٱلسَّبِيلَ إِمَّا شَاكِرًۭا وَإِمَّا كَفُورًا, tr:innâ hedeynâhu's-sebîle immâ şâkiran ve immâ kefûrâ, gloss:biz ona yolu gösterdik; ister şükreden olsun ister nankör, source:76:3} denir. Bir başka yerde yol iki sırttır ve tırmanılmaz: {ar:وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ, tr:ve hedeynâhu'n-necdeyn, gloss:ona iki yüksek yolu gösterdik, source:90:10}, {ar:فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ, tr:fe-le'ktehame'l-akabe, gloss:ama o sarp yokuşa atılmadı, source:90:11}. Zahmet kelimesi Adem'in hikâyesinde geçer. Allah onu uyarır: {ar:فَلَا يُخْرِجَنَّكُمَا مِنَ ٱلْجَنَّةِ فَتَشْقَىٰٓ, tr:fe-lâ yuhricennekumâ mine'l-cenneti fe-teşkâ, gloss:sakın sizi cennetten çıkarmasın; yoksa zahmete düşersin, source:20:117}. Yere indirilirken de şöyle der: {ar:فَمَنِ ٱتَّبَعَ هُدَاىَ فَلَا يَضِلُّ وَلَا يَشْقَىٰ, tr:fe-meni't-tebea hudâye fe-lâ yadillu ve lâ yeşkâ, gloss:kim benim yol göstermemi izlerse ne yolunu şaşırır ne de bedbaht olur, source:20:123}. Peygamber'e de {ar:مَآ أَنزَلْنَا عَلَيْكَ ٱلْقُرْءَانَ لِتَشْقَىٰٓ, tr:mâ enzelnâ aleyke'l-kur'âne li-teşkâ, gloss:Kur'an'ı sana zahmet çekesin diye indirmedik, source:20:2} denir. Musa Firavun'a gönderilirken {ar:وَيَسِّرْ لِىٓ أَمْرِى, tr:ve yessir lî emrî, gloss:işimi bana kolaylaştır, source:20:26} diye dua eder. Kolaylık zorlukla birlikte gelir: {ar:فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا, tr:fe-inne mea'l-usri yusrâ, gloss:zorlukla birlikte bir kolaylık vardır, source:94:5}. Surenin son ayetinde adı geçen İbrahim, yana çekilmeyi kendisi için ister: {ar:وَٱجْنُبْنِى وَبَنِىَّ أَن نَّعْبُدَ ٱلْأَصْنَامَ, tr:vecnubnî ve beniyye en na'bude'l-esnâm, gloss:beni ve oğullarımı putlara tapmaktan uzak tut, source:14:35}. On birinci ayetin kökü burada tersine çalışır. Bedbaht öğüdü kendinden uzak tutar, İbrahim ise Rabbinden kendisini puttan uzak tutmasını ister. Yolun yanlış ucu da gösterilir. Cennetteki bir kişi dünyadaki arkadaşını hatırlar, aşağıya bakar ve {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fettalea fe-raâhu fî sevâi'l-cahîm, gloss:baktı ve onu cehennemin ortasında gördü, source:37:55}.

Kaynaklar: 87:3 فَهَدَىٰ ه د ي B001; 87:3 فَهَدَىٰ ه د ي B003; 87:3 فَهَدَىٰ ه د ي B008; 87:3 فَهَدَىٰ ه د ي B010; 87:8 نُيَسِّرُكَ ي س ر B001; 87:8 لِلْيُسْرَىٰ ي س ر B005; 87:11 ٱلْأَشْقَى ش ق و B004; 87:11 ٱلْأَشْقَى ش ق و B002; 87:11 يَتَجَنَّبُهَا ج ن ب B005; 87:11 يَتَجَنَّبُهَا ج ن ب B003; 87:2 فَسَوَّىٰ س و ي B003; 87:2 فَسَوَّىٰ س و ي B010; 87:5 أَحْوَىٰ ح و ي B004; 87:2 فَسَوَّىٰ س و ي B006

## Seçmek: seçkin ve döküntü

On altıncı ayet {ar:بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:bel tu'ŝirûne'l-hayâte'd-dunyâ, gloss:hayır; siz dünya hayatını tercih ediyorsunuz, source:87:16} der. On yedinci ayet buna şöyle karşılık verir: {ar:وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:ve'l-âhiratu hayrun ve ebkâ, gloss:oysa ahiret daha hayırlı ve daha kalıcıdır, source:87:17}. Tercih fiili, bir şeyi kayırıp kendine ayırmaktır. Kayırılan kişi {ar:الأثير الكريم عليك الذي تؤثره بفضلك وصلتك, tr:el-eŝîr el-kerîmu aleyke'lleẕî tu'ŝiruhû bi-fadlike ve sıletik, gloss:esîr senin için değerli olandır; ona iyiliğinle ve bağışınla öncelik verirsin, source:"ء ث ر,B005"}. Başkasını kendine tercih etmek de bu köktendir: {ar:آثرت فلانا على نفسي من الإيثار, tr:âŝertu fulânen alâ nefsî mine'l-îŝâr, gloss:falancayı kendime tercih ettim, source:"ء ث ر,B005"}. Kendine ayırmak da: {ar:استأثر الله بالبقاء أي انفرد بالبقاء, tr:ista'ŝerallâhu bi'l-bekâi ey infarada bi'l-bekâ, gloss:Allah kalıcılığı kendine ayırdı yani kalıcılıkta tek kaldı, source:"ء ث ر,B006"}. Bu ifade on altıncı ayetin fiilini on yedinci ayetin kalıcılığına bağlar. Seçmek daha iyiyi aramaktır: {ar:الاختيار طلب ما هو خير وفعله, tr:el-ihtiyâru talebu mâ huve hayrun ve fi'luh, gloss:seçmek daha hayırlı olanı arayıp yapmaktır, source:"خ ي ر,B003"}. Seçilmiş olan döküntü içermez: {ar:فيهن مختارات لا رذل فيهن, tr:fîhinne muhtârâtun lâ reẕle fîhinn, gloss:onların arasında seçkinler var; aralarında döküntü yok, source:"خ ي ر,B002"}. Mal ancak bol ve temiz kaynaklı olunca hayır diye anılmayı hak eder: {ar:لا يقال للمال خير حتى يكون كثيرا ومن مكان طيب, tr:lâ yukâlu li'l-mâli hayrun hattâ yekûne keŝîran ve min mekânin tayyib, gloss:mal bol olmadıkça ve temiz bir yerden gelmedikçe ona hayır denmez, source:"خ ي ر,B004"}.

Öbür kefede dünya kelimesinin kökünden gelen aşağılık vardır: {ar:خص الدنيء بالحقير القدر, tr:hussa'd-denîu bi'l-hakîri'l-kadr, gloss:denî değeri düşük olana özgü kılınmıştır, source:"د ن و,B003"}. {ar:الأدنى عن الأرذل, tr:el-ednâ ani'l-erẕel, gloss:ednâ en aşağılık olanı anlatır, source:"د ن و,B003"}. "Değer" diye çevrilen kelime üçüncü ayetteki ölçmek fiilinin köküdür. Beşinci ayetin döküntüsü insanlar için de kullanılır: {ar:يقال لسفلة الناس الغثاء تشبيها بالذي ذكرناه, tr:yukâlu li-sefeleti'n-nâsi'l-ğuŝâ teşbîhen bi'lleẕî ẕekernâh, gloss:insanların aşağısına da ona benzetilerek ğuŝâ denir, source:"غ ث و,B004"}. Göç yerinde düşürülen değersiz eşya da bu kefededir. Kalan şey ise hâlâ iyilik taşır: {ar:أولو بقية من دين قوم لهم بقية إذا كانت بهم مسكة وفيهم خير, tr:ulû bakıyyetin min dînin kavmun lehum bakıyyetun iẕâ kânet bihim misketun ve fîhim hayr, gloss:dinden bir bakıyye sahipleri; tutunacak bir şeyleri ve içlerinde iyilik bulunan topluluk, source:"ب ق ي,B002"}.

Bu ayrım surenin önceki imgelerini bir seçim olarak toplar. Beşinci ayetteki çerçöp, altıncı ayetteki unutulan döküntü ve on altıncı ayetteki aşağı olan bir kefededir. On yedinci ayetteki hayırlı ve kalıcı olan, seçilmiş ve döküntüsüz olan öbür kefededir. Düz bir anlatım "dünya" ile "ahiret" arasında bir tercih görür. Kök aileleri bu tercihin bir ayıklama olduğunu duyurur: seçkin olan alınır, döküntü bırakılır. Kınanan şey ise döküntüyü seçmektir.

Kur'an bu seçimi açıkça sahneler. Firavun'un en yüce rab olma iddiasının anlatıldığı surede hüküm şudur: {ar:فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ, tr:fe-inne'l-cahîme hiye'l-me'vâ, gloss:artık barınağı cehennemdir, source:79:39}. Karşı tarafta {ar:وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ, tr:ve emmâ men hâfe makâme rabbihî ve nehe'n-nefse ani'l-hevâ, gloss:Rabbinin huzuruna çıkmaktan korkan ve nefsini hevesten alıkoyana gelince, source:79:40} vardır. Musa'nın karşısındaki sihirbazlar bu seçimi tehdit altında yapar: {ar:لَن نُّؤْثِرَكَ عَلَىٰ مَا جَآءَنَا مِنَ ٱلْبَيِّنَٰتِ وَٱلَّذِى فَطَرَنَا ۖ فَٱقْضِ مَآ أَنتَ قَاضٍ ۖ إِنَّمَا تَقْضِى هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:len nu'ŝirake alâ mâ câenâ mine'l-beyyinâti velleẕî fataranâ fakdı mâ ente kâd innemâ takdî hâẕihi'l-hayâte'd-dunyâ, gloss:bize gelen açık delillere ve bizi yaratana seni asla tercih etmeyiz; vereceğin hükmü ver; sen ancak bu dünya hayatında hüküm verebilirsin, source:20:72}. Sözlerini şöyle bitirirler: {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73}. Bu iki ayette surenin on altıncı ve on yedinci ayetlerinin dört kelimesi bulunur. Peygamber'e de {ar:وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ زَهْرَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا, tr:ve lâ temuddenne ayneyke ilâ mâ metta'nâ bihî ezvâcen minhum zehrate'l-hayâti'd-dunyâ, gloss:onlardan bazılarına verdiğimiz dünya hayatının çiçeğine gözünü dikme, source:20:131} denir. Ayet {ar:وَرِزْقُ رَبِّكَ خَيْرٌۭ وَأَبْقَىٰ, tr:ve rızku rabbike hayrun ve ebkâ, gloss:Rabbinin rızkı daha hayırlı ve daha kalıcıdır, source:20:131} diye biter. Dünya hayatı burada bir çiçektir. Otlağın imgesi seçimin tam içindedir. Aynı karşıtlık başka yerlerde de geçer: {ar:وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰٓ ۚ أَفَلَا تَعْقِلُونَ, tr:ve mâ indallâhi hayrun ve ebkâ e-fe-lâ ta'kılûn, gloss:Allah katında olan daha hayırlı ve daha kalıcıdır; akıl etmez misiniz, source:28:60}, {ar:وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰ لِلَّذِينَ ءَامَنُوا۟, tr:ve mâ indallâhi hayrun ve ebkâ li'lleẕîne âmenû, gloss:Allah katında olan iman edenler için daha hayırlı ve daha kalıcıdır, source:42:36}, {ar:مَا عِندَكُمْ يَنفَدُ ۖ وَمَا عِندَ ٱللَّهِ بَاقٍۢ, tr:mâ indekum yenfedu ve mâ indallâhi bâk, gloss:sizin yanınızdaki tükenir; Allah'ın katındaki ise kalır, source:16:96}. Kalıcılık kötü yönde de geçer: {ar:وَلَعَذَابُ ٱلْءَاخِرَةِ أَشَدُّ وَأَبْقَىٰٓ, tr:ve le-azâbu'l-âhirati eşeddu ve ebkâ, gloss:ahiret azabı ise elbette daha çetin ve daha kalıcıdır, source:20:127}. Tercih fiili Kur'an'da iyi yönde de kullanılır. Yusuf'un kardeşleri onu tanıdıklarında {ar:تَٱللَّهِ لَقَدْ ءَاثَرَكَ ٱللَّهُ عَلَيْنَا, tr:tallâhi lekad âŝerakallâhu aleynâ, gloss:Allah'a andolsun ki Allah seni bize üstün kıldı, source:12:91} derler. Hicret edenleri barındıranlar için de {ar:وَيُؤْثِرُونَ عَلَىٰٓ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌۭ, tr:ve yu'ŝirûne alâ enfusihim ve lev kâne bihim hasâsa, gloss:kendileri ihtiyaç içinde olsalar bile onları kendilerine tercih ederler, source:59:9} denir. Bu ayet {ar:فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ, tr:fe-ulâike humu'l-muflihûn, gloss:işte kurtuluşa erenler onlardır, source:59:9} diye biter. Burada tercih ile kurtuluş, yani surenin on altıncı ve on dördüncü ayetlerinin fiilleri, doğru yönde birleşir. Kalanlar da şöyle anılır: {ar:فَلَوْلَا كَانَ مِنَ ٱلْقُرُونِ مِن قَبْلِكُمْ أُو۟لُوا۟ بَقِيَّةٍۢ يَنْهَوْنَ عَنِ ٱلْفَسَادِ فِى ٱلْأَرْضِ, tr:fe-lev lâ kâne mine'l-kurûni min kablikum ulû bakıyyetin yenhevne ani'l-fesâdi fi'l-ard, gloss:sizden önceki nesiller arasında yeryüzünde bozgunculuğu önleyecek bir kalıntı sahibi olsaydı ya, source:11:116}.

Kaynaklar: 87:16 تُؤْثِرُونَ ء ث ر B005; 87:16 تُؤْثِرُونَ ء ث ر B006; 87:17 خَيْرٌۭ خ ي ر B003; 87:17 خَيْرٌۭ خ ي ر B002; 87:17 خَيْرٌۭ خ ي ر B004; 87:16 ٱلدُّنْيَا د ن و B003; 87:5 غُثَآءً غ ث و B004; 87:6 تَنسَىٰٓ ن س ي B003; 87:17 أَبْقَىٰٓ ب ق ي B002

## Buluşmalar

İmgelerin çoğu, surenin son ayetinde adı geçen Musa'nın hikâyesinde buluşur. Musa uzakta bir ateş görür ve {ar:أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ecidu ale'n-nâri hudâ, gloss:ateşin başında bir yol gösteren bulurum, source:20:10} umuduyla ona yönelir. Uzaktan görülen ateşin sahnesi ile yol sahnesi burada aynı cümlededir. Ateşin başında önce seçim gelir: {ar:وَأَنَا ٱخْتَرْتُكَ, tr:ve ene'htertuk, gloss:seni ben seçtim, source:20:13}. Sonra namaz ve anma gelir: {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14}. Sonra gizli olan gelir: {ar:أَكَادُ أُخْفِيهَا, tr:ekâdu uhfîhâ, gloss:onu neredeyse gizli tutuyorum, source:20:15}. Başka bir anlatımda ateşin başında tesbih söylenir: {ar:وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve subhânallâhi rabbi'l-âlemîn, gloss:Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu sahnede surenin on ikinci ve on beşinci ayetleri arasındaki karşıtlık bir kişinin yolculuğunda çözülür. Aynı ateşe yaklaşan biri onun içine sokulmaz. Ateş ona yol, seçilmişlik, namaz ve anma verir. Surede bu iki son iki ayrı kişiye düşer: on ikinci ayetteki kişi ateşe girer, on beşinci ayetteki kişi namaz kılar. Kelimelerin harf benzerliği bu ayrılığı kulakta da duyurur.

İkinci büyük buluşma selin sahnesidir. Gökten inen suyun vadilerde {ar:بِقَدَرِهَا, tr:bi-kaderihâ, gloss:kendi ölçülerince, source:13:17} akması, ölçüp biçme sahnesini çağırır. Selin taşıdığı köpük, otlağın vardığı döküntüdür. İnsanların {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâr, gloss:ateşte üzerine yaktıkları şeyden, source:13:17} çıkan köpük ise ateşin sahnesine girer. Faydalı olanın yerde kalması da öğüdün ve kalıcılığın sahnesidir. Kurumuş otun tencerenin köpüğüyle aynı adı taşıması, bu iki köpüğün Arapçada zaten tek bir kelimede birleştiğini gösterir. Bu ayet surenin beşinci ayetinden on yedinci ayetine uzanan çizgiyi tek bir manzaraya sığdırır. Bir yanda giden döküntü, öbür yanda kalan fayda vardır.

Üçüncü buluşma, Musa'nın karşısındaki sihirbazların sahnesidir. Sihirbazlar secdeye kapanır. Firavun kendi azabının daha çetin ve {ar:وَأَبْقَىٰ, tr:ve ebkâ, gloss:ve daha kalıcı, source:20:71} olduğunu söyler. Sihirbazlar da onu {ar:لَن نُّؤْثِرَكَ, tr:len nu'ŝirak, gloss:seni asla tercih etmeyiz, source:20:72} diye reddeder, yalnızca {ar:هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:hâẕihi'l-hayâte'd-dunyâ, gloss:bu dünya hayatı, source:20:72} üzerinde hüküm verebileceğini söyler ve {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} der. Sonra suçlu için {ar:لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:lâ yemûtu fîhâ ve lâ yahyâ, gloss:orada ne ölür ne yaşar, source:20:74} der, iman edenler için {ar:ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:ed-derecâtu'l-ulâ, gloss:en yüce dereceler, source:20:75} der, ve hepsini {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76} sözüyle bağlar. Bu birkaç ayette seçim, kalıcı hayat, yükseklik ve yarılan tarlanın kelimeleri birlikte konuşur. Firavun'un "en yüce" iddiası da başka bir anlatımda bu sahneye eklenir. Surenin ikinci yarısı, on üçüncü ayetten on yedinci ayete kadar, neredeyse kelimesi kelimesine Musa'nın hikâyesindeki bir topluluğun ağzından gelmiştir. Son ayetin Musa'nın sayfalarını anması da bu yüzden önem taşır.

Dördüncü buluşma ot ile seçimdir. Dünya hayatının kuruyan ota benzetildiği ayetin hemen ardından kalıcı iyi işlerin daha hayırlı olduğu söylenir. Dünya hayatı başka bir yerde bir {ar:زَهْرَةَ, tr:zehrate, gloss:çiçek, source:20:131} olarak anılır, ve aynı ayet {ar:خَيْرٌۭ وَأَبْقَىٰ, tr:hayrun ve ebkâ, gloss:daha hayırlı ve daha kalıcı, source:20:131} diye biter. Otlağın sahnesi seçimin sahnesine bu yolla girer. Beşinci ayetteki ot ile on altıncı ayetteki tercih edilen hayat aynı nesnedir. Kalıcı olan ise ayıklanıp seçilen şeydir. Tarlanın sahnesi bu iki uç arasında bir yol açar. Kalıcı iyilik anlamına gelen kurtuluş kelimesi on dördüncü ayette, toprağı yaran çiftçinin kelimesiyle söylenir. Yabani ot kendi haline kalınca kurur ve selle gider. İşlenen toprağın ürünü ise büyür, hakkı verilir ve geriye kalan bir pay bırakır. Biri dünya tarlası, öbürü ahiret tarlasıdır.

Beşinci buluşma, yaratma fiillerinde zanaat ile bedenin birleşmesidir. İkinci ayetteki ikili hem yontulmuş oku hem de ceninin biçimlenmesini anlatır. Rahimden başlayan ayetin toprağın yağmurla titreşmesiyle bitmesi, beden ile otlağı da birbirine bağlar. Aynı aile, üçüncü ayetteki ölçmeyi pay ölçmeye de taşır, ve on altıncı ayetteki tercih bir pay seçimine döner. Değneği ateşte doğrultmanın fiili on ikinci ayetin fiilidir. Bu fiil aynı ateşin düzelten bir işi ile içine düşenin katlandığı bir işi olduğunu duyurur. Bu son bağ dilin yankısıdır, ayetin sözü değildir.

Bu buluşmalar surenin hareketini taşır. Sure tesbih emriyle ve yükseklikle açılır. Ölçen, yontan ve yol gösteren Rabbin işiyle devam eder. Yağmurun çıkardığı ve selin götürdüğü ot ile sona gelen bir ömür gösterir. Sonra sözün toplanıp unutulmamasına, sunulan öğüde ve öğüt karşısında ikiye ayrılan insanlara geçer. Biri ateşe girer ve ne ölü ne diri kalır. Öbürü arınır, Rabbinin adını anar ve namaz kılar, yani surenin başındaki emri yerine getirir. Ardından seçim gelir: yakın olan öne konmuştur, ama arkadan gelen daha hayırlı ve daha kalıcıdır. Sure, bu sözün ilk sayfalarda, ateşin başında namaz ve anma emrini alan Musa'nın ve Rabbinden kendisini puttan uzak tutmasını isteyen İbrahim'in sayfalarında yazılı olduğunu söyleyerek kapanır.

