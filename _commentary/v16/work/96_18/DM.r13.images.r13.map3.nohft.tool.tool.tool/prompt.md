Focus: 96:18. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/96_18/D.r13/context.md =====
# 96:18 — focus

سَنَدْعُ ٱلزَّبَانِيَةَ

Anchor translation (canonical reading, reference only):

Biz zebanileri çağıracağız.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | سَنَدْعُ | دَعَا | د ع و | FUT;V |
| 2 | ٱلزَّبَانِيَةَ | زَّبَانِيَة | ز ب ن | DET;N |


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
- 96:7 أَن رَّءَاهُ ٱسْتَغْنَىٰٓ
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
- 96:18 ◀ focus سَنَدْعُ ٱلزَّبَانِيَةَ
- 96:19 كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩


===== _commentary/v16/work/96_18/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## د ع و (root_000478) — identity root of سَنَدْعُ (w1)

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

## ز ب ن (root_000622) — identity root of ٱلزَّبَانِيَةَ (w2)

- **B001** itip uzaklaştırma ve savuşturma — itme, savuşturma ve çarpma · onu engelleyip itti · deve sağanı ya da yavrusunu memesinden ayağıyla itti · sağanı tekmeleyip uzaklaştıran huysuz deve · savaş insanlara çarpıp onları sürükler · insanlara çarpıp onları süren savaş · topluluk birbirini itti · kendi tarafını güçlü biçimde savunan adam · kendini savunan, kibirli tavırlı adam · iki pisliği dışarı atan
  الزبن دفع الشيء عن الشيء (ayn;sihah;tahdhib); ناقة زبون إذا زبنت حالبها أو ولدها عن ضرعها برجلها (maqayis;ayn;jamhara;sihah;tahdhib); الحرب تزبن الناس إذا صدمتهم وحرب زبون (maqayis;ayn;jamhara;sihah;tahdhib); رجل ذو زبونة مانع لجانبه ذو دفع (maqayis;sihah;tahdhib); الزَّبين الدافع للأخبثين (tahdhib)
- **B002** zorla sevk eden sert görevliler — sert kolluk görevlileri veya cehenneme süren azap melekleri · bu görevlilerden biri · bu görevlilerden biri · bu görevlilerden biri · bu görevlilerden biri
  الزبانية سموا بذلك لأنهم يدفعون أهل النار إلى النار (maqayis;sihah); الزبانية ملائكة موكلون بتعذيب أهل النار (ayn); من هذا اشتقاق الزبانية (jamhara); الزبانية الشرط في كلام العرب والملائكة الغلاظ الشداد (tahdhib); واحدهم زبنية أو زبني (sihah;tahdhib)
- **B003** ağaçtaki hurmayı kuru hurmayla götürü satma — ağaçtaki yaş hurmayı kuru hurma karşılığında götürü satma
  المزابنة بيع الثمر في رؤوس النخل (maqayis); المزابنة بيع التمر في رأس النخل بالتمر (ayn;tahdhib); بيع الرطب في رؤوس النخل بالتمر ونهى عنه (sihah); لأن كل واحد إذا ندم زبن صاحبه عما عقد عليه (tahdhib)
- **B004** akrebin kıskaçları ve bunları simgeleyen yıldızlar — akrebin iki kıskacı veya boynuzu · Akrep'in kıskaçlarını simgeleyen iki parlak yıldız · bu gök bölgesindeki ilgili yıldız topluluğu
  زباني العقرب يجوز أن يكون من هذا ويجوز أن يكون شاذا (maqayis); الزبانى قرن العقرب ولها زبانيان (jamhara); زبانيا العقرب قرناها والزبانيان كوكبان نيران (sihah); زبانيا العقرب كوكبان وزبانيا العقرب قرناها (tahdhib)
- **B005** uzakta bulunma ve uzaklaşma — uzaklık ve yerleşimden uzaklaşma · topluluğunun evlerinden uzakta konakladı
  الزبن البعد (maqayis); حل فلان زبنا عن قومه وزبنا إذا تباعد عن بيوتهم (jamhara)
- **B006** yiyecekten ihtiyacı kadarını almak [kalıp] — bu yiyecekten ihtiyacım kadarını aldım
  أخذت زبني من هذا الطعام أي حاجتي (tahdhib)
- **B007** orada hiç kimsenin bulunmaması — orada hiç kimse yok
  ما بها زبين أي ليس بها أحد (tahdhib)
- **B008** boynundan tutmak [kalıp] — boynundan
  خذ بقردنه وبزبونته أي بعنقه (tahdhib)

## ECHO د ع ع (root_000477) — for سَنَدْعُ (w1): withheld observed target; not identity

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

===== _commentary/v16/out/s096/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 96:18, and ## Buluşmalar) =====
## Başından tutulan hayvan

Perçemden tutma sahnesi bir hayvanı da çağırır. Huysuz hayvan sağanı teper ya da insanlara direnir; perçeminden, burun ipinin ucundan tutulur. Dizgine uyan hayvan kolay yönetilir. Soylu at yakında tutulur ve değer görür.

On sekizinci ayetin {ar:ٱلزَّبَانِيَةَ, tr:ez-zebâniye, gloss:zebaniler, source:96:18} kelimesinin ailesinde, sağanı ya da yavrusunu ayağıyla iten deve vardır: {ar:ناقة زبون إذا زبنت حالبها أو ولدها عن ضرعها برجلها, tr:nâkatun zebûn, gloss:sağanı ya da yavrusunu ayağıyla memesinden iten deve, source:"ز ب ن,B001"}. Onuncu ayetin kul kelimesinin ailesinde iki zıt deve bulunur: {ar:بعير متعبد ومتأبد إذا امتنع على الناس صعوبة, tr:baʿîrun mutaʿabbid, gloss:insanlara direnen huysuz deve, source:"ع ب د,B011"} ve {ar:البعير المعبد المهنوء بالقطران المذلل, tr:el-baʿîru'l-muʿabbed, gloss:katranla bakılmış, alıştırılmış deve, source:"ع ب د,B005"}. On beşinci ayetin vazgeçme fiilinin ailesinde burun ipinin ucu vardır: {ar:النهاية طرف العران الذي في أنف البعير, tr:en-nihâye tarafu'l-ʿirân, gloss:nihâye, devenin burnundaki ipin ucudur, source:"ن ه ي,B002"}. Son ayetin {ar:تُطِعْهُ, tr:tutiʿhu, gloss:ona boyun eğme, source:96:19} fiilinin ailesinde de dizgine uyan at vardır: {ar:فرس طوع العنان, tr:ferasun tavʿu'l-ʿinân, gloss:dizgine uysal at, source:"ط و ع,B001"}.

Son ayetin {ar:وَٱقْتَرِب, tr:vakterib, gloss:ve yaklaş, source:96:19} emrinin ailesinde yakında tutulan at vardır: {ar:فرس مقربة وهي التي تدنى وتقرب ولا تترك أن ترود والمقربة المكرمة, tr:ferasun mukrabe … ve'l-mukrabetu'l-mukrame, gloss:mukrabe at, yakına alınıp otlamaya salınmayan attır; mukrabe, değer verilen demektir, source:"ق ر ب,B013"}. Bu ifade yakınlığı üçüncü ayetteki cömertlik köküyle birleştirir. Onuncu ayetin namaz fiilinin ailesinde de yarışta ikinci gelen at vardır: {ar:السابق الأول والمصلي الثاني, tr:es-sâbiku'l-evvel ve'l-musallî es-sânî, gloss:sâbık birincidir, musallî ikinci, source:"ص ل و,B006"}. İkinci atın başı öndekinin sağrısını izler. Kurân önde olanları yakınlıkla adlandırır: {ar:وَٱلسَّٰبِقُونَ ٱلسَّٰبِقُونَ, tr:ve's-sâbikûne's-sâbikûn, gloss:önde olanlar, önde olanlardır, source:56:10}, {ar:أُو۟لَٰٓئِكَ ٱلْمُقَرَّبُونَ, tr:ulâ'ike'l-mukarrabûn, gloss:onlar yakınlaştırılanlardır, source:56:11}. Atlar ile nankör insan da bir surede yan yana gelir: {ar:وَٱلْعَٰدِيَٰتِ ضَبْحًا, tr:ve'l-ʿâdiyâti dabhâ, gloss:soluk soluğa koşanlara andolsun, source:100:1}, {ar:إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌ, tr:inne'l-insâne li rabbihî le kenûd, gloss:insan Rabbine karşı gerçekten nankördür, source:100:6}.

Bu sahnede azmak, dizgine direnmektir: {ar:مجاوزة الحد في العصيان, tr:mucâvezetu'l-hadd fi'l-ʿisyân, gloss:isyanda sınırı aşmak, source:"ط غ ي,B001"}. Yasaklayan adam huysuz hayvan gibi perçeminden tutulur. Kul ise yakında tutulan, değer gören at gibi yaklaşmaya çağrılır. "Ona boyun eğme" emri, hangi elin dizgine sahip olduğu sorusunu sorar.

Kaynaklar: 96:18 ٱلزَّبَانِيَةَ ز ب ن B001; 96:10 عَبْدًا ع ب د B011; 96:10 عَبْدًا ع ب د B005; 96:15 يَنتَهِ ن ه ي B002; 96:19 تُطِعْهُ ط و ع B001; 96:19 وَٱقْتَرِب ق ر ب B013; 96:10 صَلَّىٰٓ ص ل و B006; 96:6 لَيَطْغَىٰٓ ط غ ي B001

## İki çağrı, iki meclis

Çağırmak, birini sesle kendine doğru çekmektir: {ar:أصل واحد وهو أن تميل الشيء إليك بصوت وكلام يكون منك, tr:aslun vâhid, ve huve en tumîle'ş-şey'e ileyke bi savt, gloss:tek bir asıl: bir şeyi sesinle ve sözünle kendine yöneltmek, source:"د ع و,B001"}. On yedinci ayette adam {ar:فَلْيَدْعُ نَادِيَهُۥ, tr:felyedʿu nâdiyeh, gloss:meclisini çağırsın, source:96:17} diye meydan okunur. Meclis, çevresinde toplanılan yerdir: {ar:النادي المجلس يندو إليه من حواليه, tr:en-nâdî el-meclis, gloss:nâdî, çevredekilerin toplandığı meclistir, source:"ن د و,B001"}. Meclis kelimesi, içindeki insanlarla birlikte anlam kazanır: {ar:النادي… لا يسمى ناديا حتى يكون فيه أهله, tr:lâ yusemmâ nâdiyen hattâ yekûne fîhi ehluh, gloss:içinde halkı bulunmadıkça nâdî denmez, source:"ن د و,B001"}. Kök sesin yükselip uzağa ulaşmasını da kapsar: {ar:النداء رفع الصوت وظهوره, tr:en-nidâ' ref'u's-savt, gloss:nida sesi yükseltip duyurmaktır, source:"ن د و,B002"}. Kurân bu meclisi, ayetler okunduğunda inkârcıların övündüğü bir şey olarak gösterir: {ar:أَىُّ ٱلْفَرِيقَيْنِ خَيْرٌ مَّقَامًا وَأَحْسَنُ نَدِيًّا, tr:eyyu'l-ferîkayni hayrun makâmen ve ahsenu nediyyâ, gloss:iki topluluktan hangisinin yeri daha iyi, meclisi daha güzel, source:19:73}. Lut da kavmine meclislerinde yaptıklarını sorar: {ar:وَتَأْتُونَ فِى نَادِيكُمُ ٱلْمُنكَرَ, tr:ve te'tûne fî nâdîkumu'l-munker, gloss:meclisinizde de çirkinliği işliyorsunuz, source:29:29}. Firavun da toplayıp çağırır: {ar:فَحَشَرَ فَنَادَىٰ, tr:fe haşera fe nâdâ, gloss:topladı ve seslendi, source:79:23}.

On sekizinci ayet karşı çağrıdır: {ar:سَنَدْعُ ٱلزَّبَانِيَةَ, tr:senedʿu'z-zebâniye, gloss:biz de zebanileri çağıracağız, source:96:18}. Zebanilerin adı itmekten gelir: {ar:الزبن دفع الشيء عن الشيء, tr:ez-zebnu defʿu'ş-şey'i ʿani'ş-şey', gloss:zebn bir şeyi bir şeyden itmektir, source:"ز ب ن,B001"}; {ar:الزبانية سموا بذلك لأنهم يدفعون أهل النار إلى النار, tr:ez-zebâniye summû bi zâlike li ennehum yedfaʿûne ehle'n-nâr, gloss:zebanilere bu ad, ateş ehlini ateşe ittikleri için verilmiştir, source:"ز ب ن,B002"}. Kök uzaklığı da adlandırır: {ar:الزبن البعد, tr:ez-zebnu'l-buʿd, gloss:zebn uzaklıktır, source:"ز ب ن,B005"}. Kurân ateşin bekçilerini şöyle anlatır: {ar:عَلَيْهَا مَلَٰٓئِكَةٌ غِلَاظٌ شِدَادٌ لَّا يَعْصُونَ ٱللَّهَ مَآ أَمَرَهُمْ, tr:ʿaleyhâ melâ'iketun gilâzun şidâd, lâ yaʿsûna'llâhe mâ emerahum, gloss:başında Allah'ın emrine karşı gelmeyen sert, güçlü melekler vardır, source:66:6}, {ar:عَلَيْهَا تِسْعَةَ عَشَرَ, tr:ʿaleyhâ tisʿate ʿaşer, gloss:başında on dokuz vardır, source:74:30}. İtmenin kendisi de anlatılır: {ar:يَوْمَ يُدَعُّونَ إِلَىٰ نَارِ جَهَنَّمَ دَعًّا, tr:yevme yudaʿʿûne ilâ nâri cehenneme daʿʿâ, gloss:cehennem ateşine itilip kakıldıkları gün, source:52:13}.

Üçüncü bir çağrı da vardır. Onuncu ayetin namazı bir çağrıdır: {ar:الصلاة وهي الدعاء, tr:es-salâtu ve hiye'd-duʿâ', gloss:salât duadır, source:"ص ل و,B002"}. Kurân Allah'ın kulunun dua ederken kuşatılmasını cinlerin ağzından anlatır: {ar:لَمَّا قَامَ عَبْدُ ٱللَّهِ يَدْعُوهُ كَادُوا۟ يَكُونُونَ عَلَيْهِ لِبَدًا, tr:lemmâ kâme ʿabdu'llâhi yedʿûhu kâdû yekûnûne ʿaleyhi libedâ, gloss:Allah'ın kulu O'na dua etmeye kalkınca neredeyse üstüne yığılacaklardı, source:72:19}. Son ayetin yaklaşma emri bu çağrıya karşılık verir. Kökte hükümdarın yakın çevresi vardır: {ar:القربان واحد قرابين الملك وهم جلساؤه وخاصته, tr:el-kurbânu vâhidu karâbîni'l-melik, gloss:kurbân, hükümdarın meclis arkadaşları ve has adamlarından biridir, source:"ق ر ب,B004"}. Yakınlık aynı zamanda çağrıya karşılık verilmesidir: {ar:في الرعاية نحو فإني قريب أجيب دعوة الداع, tr:fi'r-riʿâye nahve fe innî karîbun ucîbu daʿvete'd-dâʿ, gloss:gözetme anlamında, "Ben yakınım, dua edenin duasına karşılık veririm" gibi, source:"ق ر ب,B006"}. Kurân'daki ifade şudur: {ar:فَإِنِّى قَرِيبٌ أُجِيبُ دَعْوَةَ ٱلدَّاعِ إِذَا دَعَانِ, tr:fe innî karîb, ucîbu daʿvete'd-dâʿi izâ daʿân, gloss:Ben yakınım; dua eden bana dua ettiğinde karşılık veririm, source:2:186}. Çağıranlar yakınlığı arar: {ar:يَبْتَغُونَ إِلَىٰ رَبِّهِمُ ٱلْوَسِيلَةَ أَيُّهُمْ أَقْرَبُ, tr:yebtegûne ilâ rabbihimu'l-vesîlete eyyuhum akrab, gloss:hangisi daha yakın olacak diye Rablerine yol ararlar, source:17:57}. Yakın meclis secde eder: {ar:إِنَّ ٱلَّذِينَ عِندَ رَبِّكَ لَا يَسْتَكْبِرُونَ عَنْ عِبَادَتِهِۦ, tr:inne'llezîne ʿinde rabbike lâ yestekbirûne ʿan ʿibâdetih, gloss:Rabbinin yanında olanlar O'na kulluk etmekten büyüklenmezler, source:7:206}, {ar:وَلَهُۥ يَسْجُدُونَ, tr:ve lehû yescudûn, gloss:ve O'na secde ederler, source:7:206}.

Böylece sahnede üç hareket vardır. Adam meclisini çevresine toplar. Allah, uzaklaştırıp iten bekçileri çağırır. Kul ise hükümdarın yakın meclisine çağrılır. Düz bir anlatım bunu tehdit ve emir olarak verir; bu sahne iki karşıt sarayı gösterir.

Kaynaklar: 96:17 فَلْيَدْعُ د ع و B001; 96:17 نَادِيَهُۥ ن د و B001; 96:17 نَادِيَهُۥ ن د و B002; 96:18 ٱلزَّبَانِيَةَ ز ب ن B001; 96:18 ٱلزَّبَانِيَةَ ز ب ن B002; 96:18 ٱلزَّبَانِيَةَ ز ب ن B005; 96:10 صَلَّىٰٓ ص ل و B002; 96:19 وَٱقْتَرِب ق ر ب B004; 96:19 وَٱقْتَرِب ق ر ب B006

## Buluşmalar

İmgeler en açık şekilde baş sahnesinde buluşur. On beşinci ayetin fiili hem perçemden tutmak hem de yüzü karartmaktır. Böylece başın önü, avın yakalandığı yer, huysuz hayvanın tutulduğu yer ve ateşin yaladığı deri aynı noktada birleşir. Aynı alın son ayette yere konur ve secde izini taşır. İşaret imgesi buraya da uzanır: bir alın kararmış bir lekeyle işaretlenir, öteki secdenin iziyle. Kurân her iki tarafı da yüzlerindeki işaretle tanıtır: biri {ar:مِّنْ أَثَرِ ٱلسُّجُودِ, tr:min eseri's-sucûd, gloss:secdenin izinden, source:48:29}, öteki {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. Sure ad ile başlar ve iki işaretli alınla biter.

Göz ile yeterlilik imgeleri yedinci ayette buluşur. Kendini aynada gören adam ile süse ihtiyaç duymayan güzel kadın aynı kelime çiftinde birleşir: kendini görmek ve yeterli saymak. Su imgesi de buna bağlanır. Azan insan ölçüsünü aşan bir taşkın gibidir; on beşinci ayette durması istenir. Kökün göletteki duruluşu adlandırdığı hatırlanırsa, sekizinci ayet bu suyun nereye varacağını söyler. Kurân'ın varış ayeti bu iki imgeyi aynı yapıda birleştirir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Yol imgesi de bu dönüşe katılır, çünkü dönüş başlangıca dönmektir ve bu başlangıç rahimdeki ilk tutunuştur.

Rahim ile okuma, surenin ilk kelimesinde buluşur. Okumanın kökü hem rahmin bir şeyi toplayıp tutmasını hem de harflerin toplanmasını adlandırır. Pıhtıyı tutan kökle sözü toplayan kök aynıdır. İnsanın yaratılışı ve öğretilmesi bu yüzden aynı işin iki yüzü olarak duyulur. Kurân'daki benzer sıra da bunu destekler: Kurân'ı öğretmek, insanı yaratmak ve ona açıklamayı öğretmek. Okuma ile secde de buluşur: okuyucu aynı zamanda kulluk edendir ve sure, ilk emri okumak, son emri secde etmek olan bir eğri çizer. Kurân bu ikisini, okunduğunda secde edenler ile etmeyenler üzerinden birleştirir.

Ateş ile çağrı imgeleri onuncu, on yedinci ve on sekizinci ayetlerde buluşur. Namaz hem çağrıdır hem de kökü ateşe girmeyi adlandırır. Adam meclisini çağırır, Allah ateşe iten bekçileri çağırır ve kul yakın meclise çağrılır. Ateşin kendisinin de çağırdığı söylenir: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Bu yüz çevirme on üçüncü ayetin fiilidir.

İtaat ile hayvan imgeleri son ayette buluşur. Rab, itaat edilen efendidir; dizgine uyan at da itaatin bir figürüdür. Kul bu yüzden kendini rab ilan eden birine boyun eğmez, yakında tutulan ve değer gören at gibi yaklaşır. Yaratma ile uydurma da on altıncı ayette buluşur. Gerçek ölçüyle yaratan Rab'bin karşısında, yalanı içinde ölçen yalancı perçem durur.

Bu buluşmalar surenin hareketini taşır. Sure, rahimde toplanan ve tutunan bir varlıkla başlar; bu varlık sözü toplamayı ve kalemle yazmayı öğrenir. Sonra kendini aynada yeterli görür, taşkın su gibi ölçüsünü aşar, başını kaldırır ve namaz kılan kulu engellemeye çalışır. Dönüş ayeti ve Allah'ın görmesi bu yükselişin önüne bir sınır koyar. Yasaklayan perçeminden yakalanır, meclisi yerine bekçiler gelir. Kul ise yüz çevirmeden, başını yere koyarak, çağrılmış olduğu yakınlığa yürür.

