Focus: 88:21. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_21/D.r13/context.md =====
# 88:21 — focus

فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ

Anchor translation (canonical reading, reference only):

O halde hatırlat; sen yalnızca hatırlatansın.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَذَكِّرْ | ذُكِّرَ | ذ ك ر | REM;V |
| 2 | إِنَّمَآ | إِنّ;مَا |  | ACC;PREV |
| 3 | أَنتَ |  |  | PRON |
| 4 | مُذَكِّرٌ | مُذَكِّر | ذ ك ر | N |


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
- 88:7 لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ
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
- 88:21 ◀ focus فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
- 88:22 لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- 88:23 إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- 88:24 فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- 88:25 إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 88:26 ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/work/88_21/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ذ ك ر (root_000516) — identity root of فَذَكِّرْ (w1)

- **B001** erkek cinsiyet ve erkek yavru doğurma — erkek · erkek üreme organı · erkeğin üreme organı çevresindeki organlar · erkekler veya erkeklik · erkek yavru doğurdu · çoğunlukla erkek yavru doğuran dişi · erkek yapılı kadın veya dişi deve · gebe için kolay doğum ve erkek çocuk dileği
  الذكر خلاف الأنثى (sihah;tahdhib;mufradat)؛ الذكورة والذكور والذكران جمع الذكر (ayn;tahdhib;mufradat)؛ أذكرت ولدت ذكرا والمذكار تلد الذكور (maqayis;ayn;sihah;tahdhib;mufradat)
- **B002** sert, keskin ve güçlü olma — demirin en sert ve kuru türü · keskin ve sağlam kılıç · kılıcın veya erkeğin keskinliği · kalın ve sert otlar · güçlü, yiğit ve onurlu adam · çetin ve korkutucu gün, yol veya felaket · şiddetli yağmur, sağlam söz veya güçlü şiir · tehlikeli, yalnız erkeklerin geçtiği veya sert ot bitiren ıssız ova
  سيف مذكر ذو ماء وذو ذكر صارم (maqayis;sihah;mufradat)؛ الذكر من الحديد أيبسه وأشده (ayn;sihah;tahdhib)؛ ذكور البقل ما غلظ منه (maqayis;sihah;tahdhib;mufradat)؛ رجل ذكر قوي شجاع ويوم وطريق وداهية ومطر ذكر للشدة (tahdhib)
- **B003** akılda tutma ve yeniden hatırlama — hatırladı veya aklında tuttu · aklında · hatırlama · ezberlemek için çalışma · belleği güçlü, yiğit veya iyi anılan adam
  ذكرت الشيء خلاف نسيته (maqayis;sihah)؛ الذكر الحفظ للشيء وهو مني على ذكر (ayn;tahdhib)؛ ذكر بالقلب والتذكر طلب ما فات (ayn;tahdhib;mufradat)
- **B004** bir şeyi sözle anma [kalıp] — sözle anma · insanların arkasından kusurlarını söyleme
  ثم حمل عليه الذكر باللسان (maqayis)؛ الذكر جري الشيء على لسانك (ayn;tahdhib)؛ ذكرته بلساني وبقلبي (sihah)؛ كل قول يقال له ذكر وذكر باللسان (mufradat)؛ يذكر الناس أي يغتابهم ويذكر عيوبهم (tahdhib)
- **B005** Tanrı'yı kulluk amacıyla anma — kulluk amacıyla anma, yakarış, övgü, şükretme ve itaat · Tanrı'yı kulluk, övgü ve yakarışla anma
  الذكر الصلاة والدعاء والثناء (ayn;tahdhib)؛ الذكر قراءة القرآن والتسبيح والدعاء والشكر والطاعة (tahdhib)؛ ولذكر الله أكبر واذكروا الله (mufradat)
- **B006** indirildiğine inanılan kutsal kitap — dinin ayrıntılarını bildiren kutsal kitap
  الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر (ayn;tahdhib)؛ القرآن والكتب المتقدمة والزبور من بعد الذكر (mufradat)
- **B007** onur, iyi ün ve saygınlık — onur, iyi ün ve övgü · belleği güçlü, yiğit veya iyi anılan adam
  الذكر العلاء والشرف (maqayis)؛ الذكر الشرف والصوت (ayn;tahdhib)؛ الذكر الصيت والثناء وذي الذكر أي ذي الشرف (sihah)؛ وإنه لذكر لك ولقومك أي شرف (mufradat)
- **B008** hakkı gösteren yazılı belge [kalıp] — hakkı gösteren yazılı belge · yazılı hak belgeleri
  ذكر الحق الصك وجمعه ذكور حقوق (ayn;tahdhib)؛ يقال ذكور حق (ayn;tahdhib)
- **B009** hatırlatma, hatırlamayı sağlayan araç ve sıkça anma — hatırlatma, öğüt alma veya sıkça anma · hatırlatıcı · hatırlatma · ona o şeyi hatırlattı
  الذكرى اسم للتذكير والتذكير مجاوز (ayn)؛ التذكرة ما تستذكر به الحاجة (sihah)؛ الذكرى بمعنى الذكر وبمعنى التذكير (tahdhib)؛ التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر (mufradat)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:21, and ## Buluşmalar) =====
## Kulağa gelen: haber, susan sesler, işitilmeyen söz

Sure göze değil kulağa seslenerek başlar. "Sana geldi mi" diye sorulan şey bir haberdir. Haber de kulaktan ulaşan sözdür: {ar:كل كلام يبلغ الإنسان من جهة السمع أو الوحي يقال له حديث, tr:küllü kelâmin yeblüğu'l-insâne min cihetí's-sem'i evi'l-vahyi yukâlü lehû hadîs, gloss:insana işitme ya da vahiy yoluyla ulaşan her söze hadîs denir, source:"ح د ث,B003"}. Kur'an aynı açılışı başka yerlerde de kullanır ve ardından her seferinde bir kıssa gelir: {ar:وَهَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ, tr:ve hel etâke hadîsü Mûsâ, gloss:Musa'nın haberi sana geldi mi, source:20:9}; {ar:هَلْ أَتَىٰكَ حَدِيثُ ضَيْفِ إِبْرَٰهِيمَ ٱلْمُكْرَمِينَ, tr:hel etâke hadîsü dayfi İbrâhîme'l-mükramîn, gloss:İbrahim'in ağırlanan misafirlerinin haberi sana geldi mi, source:51:24}; {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْجُنُودِ, tr:hel etâke hadîsü'l-cunûd, gloss:orduların haberi sana geldi mi, source:85:17}. Bunlarda anlatılan şey geçmişte kalmıştır. Bu surede ise henüz gelmemiş bir gün, gelmiş bir haber gibi anlatılır. Kelimenin bir kolu, haberlerde ibret olarak anlatılan insanlara da ad verir: {ar:فجعلناهم أحاديث أي أخبارا يتمثل بهم, tr:fe-cealnâhum ehâdîse ey ahbâran yütemesselü bihim, gloss:onları örnek gösterilen haberler yaptık, source:"ح د ث,B004"}. Bu anlam surenin haberinin yanında duyulur: haberi dinleyen, kendisi de bir haber olabilir.

İkinci ayetteki eğiklik sesleri de kapsar: {ar:خشعت الأصوات أي سكنت, tr:haşaati'l-asvâtu ey sekenet, gloss:sesler kısıldı yani dindi, source:"خ ش ع,B001"}. Kur'an bu susuşu Sur'a üfürülen günün sahnesinde gösterir. Herkes çağırıcının ardından sapmadan yürür: {ar:وَخَشَعَتِ ٱلْأَصْوَاتُ لِلرَّحْمَٰنِ فَلَا تَسْمَعُ إِلَّا هَمْسًۭا, tr:ve haşaati'l-asvâtu li'r-Rahmâni fe-lâ tesmeu illâ hemsâ, gloss:sesler Rahman'a karşı kısılır; bir fısıltıdan başkasını işitmezsin, source:20:108}. Bu ayetteki "işitmezsin" sözü, on birinci ayetteki ile harfi harfine aynıdır: {ar:لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ, tr:lâ tesmeu fîhâ lâğiye, gloss:orada boş bir söz işitmezsin, source:88:11}. Böylece iki ayrı sessizlik ortaya çıkar. Birinde sesler korkudan kısılır. Ötekinde kulak çirkin sözden korunur. İşitmek, sesi kulakla yakalamaktır: {ar:إيناس الشيء بالأذن, tr:înâsu'ş-şey'i bi'l-üzün, gloss:bir şeyi kulakla fark etmek, source:"س م ع,B001"}. Bu kelime anlamayı ve söz dinlemeyi de içerir: {ar:تارة عن الفهم وتارة عن الطاعة, tr:târaten ani'l-fehmi ve târaten ani't-tâa, gloss:kimi zaman anlamayı kimi zaman itaati anlatır, source:"س م ع,B003"}. Bahçede işitilmeyen kelime de tek tek tanımlanır: {ar:لاغية كلمة قبيحة أو فاحشة, tr:lâğiyetun kelimetun kabîhatun ev fâhişe, gloss:çirkin ya da hayasız söz, source:"ل غ و,B002"}. Kökün bir kolu, anlamsız gürültüyü ve köpek havlamasını da anlatır: {ar:اللغا: الصوت مثل الوغا ونباح الكلب لغو أيضا, tr:el-leğâ es-savtu misle'l-vağâ ve nubâhu'l-kelbi lağvun eydan, gloss:gürültü; köpek havlaması da lağvdır, source:"ل غ و,B003"}. Kur'an bahçenin bu sessizliğini sık sık anlatır ve yerine konan sözü de söyler: {ar:لَّا يَسْمَعُونَ فِيهَا لَغْوًا إِلَّا سَلَٰمًۭا, tr:lâ yesmeûne fîhâ lağven illâ selâmâ, gloss:orada boş söz değil yalnız selam işitirler, source:19:62}; {ar:لَا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا تَأْثِيمًا, tr:lâ yesmeûne fîhâ lağven ve lâ te'sîmâ, gloss:orada ne boş söz işitirler ne günaha sokan söz, source:56:25}; {ar:إِلَّا قِيلًۭا سَلَٰمًۭا سَلَٰمًۭا, tr:illâ kîlen selâmen selâmâ, gloss:yalnızca selam selam diye bir söz, source:56:26}; {ar:لَّا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا كِذَّٰبًۭا, tr:lâ yesmeûne fîhâ lağven ve lâ kizzâbâ, gloss:orada ne boş söz işitirler ne yalan, source:78:35}.

Yirmi birinci ayette haber çizgisi döner: {ar:فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ, tr:fe-zekkir innemâ ente müzekkir, gloss:hatırlat; sen yalnızca hatırlatansın, source:88:21}. Hatırlatmak önce bir şeyi dile getirmektir: {ar:الذكر جري الشيء على لسانك, tr:ez-zikru ceryü'ş-şey'i alâ lisânik, gloss:zikir bir şeyin dilinden akmasıdır, source:"ذ ك ر,B004"}. Dinleyende ise unutmanın karşıtını uyandırmaktır: {ar:ذكرت الشيء خلاف نسيته, tr:zekertü'ş-şey'e hılâfe nesîtüh, gloss:hatırladım unuttum'un zıddıdır, source:"ذ ك ر,B003"}. Sure "sana geldi mi" diye başlamış, "sen hatırlatansın" diye bu çizgiyi kapatır. Habere ilk muhatap olan kişi, aynı haberi başkalarının kulağına ulaştıran olur.

Kaynaklar: 88:1 أَتَىٰكَ ء ت ي B001; 88:1 حَدِيثُ ح د ث B003; 88:1 حَدِيثُ ح د ث B004; 88:2 خَٰشِعَةٌ خ ش ع B001; 88:11 تَسْمَعُ س م ع B001; 88:11 تَسْمَعُ س م ع B003; 88:11 لَٰغِيَةً ل غ و B002; 88:11 لَٰغِيَةً ل غ و B003; 88:21 فَذَكِّرْ ذ ك ر B004; 88:21 مُذَكِّرٌ ذ ك ر B003

## Eğilmek ve yanmak

İkinci, üçüncü ve dördüncü ayetlerin kelimeleri, ibadetin duruşlarını da adlandırır. Eğik yüzü anlatan kelime rükû edeni de anlatır: {ar:الخاشع المستكين والراكع, tr:el-hâşiu'l-müstekînu ve'r-râki', gloss:hâşi boyun eğen ve rükû edendir, source:"خ ش ع,B001"}; {ar:الخاشع الراكع, tr:el-hâşiu'r-râki', gloss:hâşi rükû edendir, source:"خ ش ع,B001"}. Nâsıba, ayakta durup yorulmaktır: {ar:النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي, tr:en-nasabu'l-anâ ve ma'nâhu enne'l-insâne lâ yezâlü muntasiben hattâ yu'yî, gloss:insanın tükenene dek ayakta durması, source:"ن ص ب,B004"}. Ateşe girme fiilinin kökü, rükû ve secdeden oluşan namazı da adlandırır: {ar:الصلاة التي جاء بها الشرع من الركوع والسجود, tr:es-salâtü'lletî câe bihe'ş-şer'u mine'r-rukûi ve's-sucûd, gloss:dinin getirdiği rükû ve secdeden oluşan namaz, source:"ص ل ي,B001"}. Ayette bu üç kelimenin anlamı eğiklik, yorgunluk ve ateştir. Yanlarında ise rükû, kıyam ve namaz duyulur. Sure bu yüzlerin kim olduğunu söylemez. Ama kelimeler, eğilmiş ve ayakta yorulmuş bir bedeni ateşe bağlar.

Kur'an bu kelimelerin her birini ibadet için de kullanır. Kurtuluşa erenleri anlatırken {ar:ٱلَّذِينَ هُمْ فِى صَلَاتِهِمْ خَٰشِعُونَ, tr:ellezîne hum fî salâtihim hâşiûn, gloss:namazlarında huşu içinde olanlar, source:23:2} der. Allah Peygamber'e {ar:فَإِذَا فَرَغْتَ فَٱنصَبْ, tr:fe-izâ ferağte fensab, gloss:boşaldığında kalk ve yorul, source:94:7} der. Önceki surede aynı kök birkaç ayet arayla iki anlamda kullanılır: {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasla'n-nâre'l-kübrâ, gloss:en büyük ateşe girecek olan, source:87:12}; {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve zekera'sme rabbihî fe-sallâ, gloss:Rabbinin adını anıp namaz kılan, source:87:15}. Biri ateşe girer, öteki namaz kılar. Namaz da orada anmayla birlikte gelir. Anmanın namaz anlamı da vardır: {ar:الذكر الصلاة والدعاء والثناء, tr:ez-zikru's-salâtü ve'd-duâu ve's-senâ', gloss:zikir namaz dua ve övgüdür, source:"ذ ك ر,B005"}. Ölüm anındaki inkârcı için de şöyle denir: {ar:فَلَا صَدَّقَ وَلَا صَلَّىٰ, tr:fe-lâ saddeka ve lâ sallâ, gloss:ne doğruladı ne namaz kıldı, source:75:31}; {ar:وَلَٰكِن كَذَّبَ وَتَوَلَّىٰ, tr:ve lâkin kezzebe ve tevellâ, gloss:ama yalanladı ve yüz çevirdi, source:75:32}. Namaz kılmamak ve yüz çevirmek burada bir arada, tıpkı yirmi üçüncü ayetteki yüz çevirme gibi.

Bu sahnelerin en keskini, o günün eğik bakışını dünyadaki secde çağrısına bağlar: {ar:خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ ۖ وَقَدْ كَانُوا۟ يُدْعَوْنَ إِلَى ٱلسُّجُودِ وَهُمْ سَٰلِمُونَ, tr:hâşiaten ebsâruhum terhakuhum zilletün ve kad kânû yud'avne ile's-sucûdi ve hum sâlimûn, gloss:gözleri eğik ve kendilerini aşağılanma bürümüş; oysa sağlıklıyken secdeye çağrılıyorlardı, source:68:43}. Dünyada istenen eğilme gönüllü olabilirdi. O gün ise zorla gelir. İkinci ayetteki kelime bu iki eğilmeyi birlikte duyurur.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:3 نَّاصِبَةٌ ن ص ب B004; 88:4 تَصْلَىٰ ص ل ي B001; 88:4 تَصْلَىٰ ص ل ي B003; 88:21 فَذَكِّرْ ذ ك ر B005

## Hatırlatıcı, gözetmen değil

Yirmi birinci ayet Peygamber'in işini tek bir kelimeye indirir: hatırlatmak. "Ancak" sözü bu işin sınırını çizer. Hatırlatma, bir şeyin akla getirilmesini sağlayan şeydir ve tekrar edilir: {ar:التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر, tr:et-tezkiretü mâ yütezekkeru bihi'ş-şey' ve'z-zikrâ kesretü'z-zikr, gloss:tezkire bir şeyin hatırlandığı araçtır; zikra çok anmaktır, source:"ذ ك ر,B009"}. Yirmi ikinci ayet de bu işin olmadığı şeyi söyler: {ar:لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ, tr:leste aleyhim bi-musaytır, gloss:sen onların üstünde bir gözetmen değilsin, source:88:22}. Musaytır, bir şeyin başına konup onu gözeten ve yaptığını yazan kişidir: {ar:المسيطر والمصيطر المسلط على الشيء ليشرف عليه ويتعهد أحواله ويكتب عمله, tr:el-museytıru ve'l-musaytıru'l-musallatu ale'ş-şey'i li-yuşrife aleyhi ve yeteahhede ahvâlehû ve yektübe amelehû, gloss:bir şeyin başına konup onu gözeten halini kollayan ve işini yazan kişi, source:"س ط ر,B003"}; {ar:السيطرة مصدر المسيطر وهو كالرقيب الحافظ المتعهد للشيء, tr:es-saytaratu masdaru'l-museytır ve huve ke'r-rakîbi'l-hâfızı'l-müteahhidi li'ş-şey', gloss:bir şeyi bekleyen ve koruyan gözcü gibi olan, source:"س ط ر,B003"}. Bu yetkinin asıl sahipleri efendilerdir: {ar:المسيطرون الأرباب المسلطون, tr:el-museytırûne'l-erbâbü'l-musallatûn, gloss:başa geçirilmiş efendiler, source:"س ط ر,B003"}. Kökün aslı satırdır: {ar:أصل مطرد يدل على اصطفاف الشيء كالكتاب والشجر, tr:aslun muttaridun yedullü ale'stıfâfi'ş-şey'i ke'l-kitâbi ve'ş-şecer, gloss:yazı ve ağaç gibi şeylerin dizilişini gösteren kök, source:"س ط ر,B001"}; {ar:السطر سطر من كتب وسطر من شجر مغروس, tr:es-satru satrun min kütübin ve satrun min şecerin mağrûs, gloss:satır yazıdan bir satır ve dikilmiş ağaçtan bir sıradır, source:"س ط ر,B001"}. Gözetmen, kayıtları satır satır tutan kişidir. Bu kökün tanımında geçen diziliş kelimesi, on beşinci ayette yastıkların dizilişini anlatan kelimedir. Bu bağ kök birliğinden değil, kelimelerin açıklamasından gelir. Bahçede yastıkları dizen bir el vardır. Amelleri satıra dizen el de vardır, ama Peygamber'in eli değildir.

Kur'an bu kaydı Allah'a bağlar. Önceki kavimlerin anlatıldığı surenin sonunda şöyle denir: {ar:وَكُلُّ صَغِيرٍۢ وَكَبِيرٍۢ مُّسْتَطَرٌ, tr:ve küllü sağîrin ve kebîrin mustatar, gloss:küçük büyük her şey satır satır yazılmıştır, source:54:53}. Buradaki "yazılmış" kelimesi musaytır ile aynı köktendir. Kur'an'da bu kelimenin geçtiği tek başka yer, inkârcılara sorulan bir sorudur: {ar:أَمْ عِندَهُمْ خَزَآئِنُ رَبِّكَ أَمْ هُمُ ٱلْمُصَۣيْطِرُونَ, tr:em indehum hazâinu rabbike em humu'l-musaytırûn, gloss:yoksa Rabbinin hazineleri onların yanında mı, yoksa gözetmenler onlar mı, source:52:37}. Gözetmenlik ne Peygamber'indir ne de onu reddedenlerin.

Kur'an bu sınırı başka yerlerde de çizer. Kaf suresinin sonunda Allah şöyle der: {ar:وَمَآ أَنتَ عَلَيْهِم بِجَبَّارٍۢ ۖ فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ, tr:ve mâ ente aleyhim bi-cebbârin fe-zekkir bi'l-Kur'âni men yehâfu vaîd, gloss:sen onları zorlayan değilsin; tehdidimden korkana Kur'an ile hatırlat, source:50:45}. Başka yerlerde de {ar:فَمَآ أَرْسَلْنَٰكَ عَلَيْهِمْ حَفِيظًا ۖ إِنْ عَلَيْكَ إِلَّا ٱلْبَلَٰغُ, tr:fe-mâ erselnâke aleyhim hafîzan in aleyke ille'l-belâğ, gloss:seni onların üstüne bekçi göndermedik; sana düşen yalnızca duyurmaktır, source:42:48} ve {ar:وَمَا جَعَلْنَٰكَ عَلَيْهِمْ حَفِيظًۭا ۖ وَمَآ أَنتَ عَلَيْهِم بِوَكِيلٍۢ, tr:ve mâ cealnâke aleyhim hafîzan ve mâ ente aleyhim bi-vekîl, gloss:seni onlara bekçi yapmadık; sen onların vekili de değilsin, source:6:107} denir. Cezalandırmak da Allah'ın işidir: {ar:إِن يَشَأْ يَرْحَمْكُمْ أَوْ إِن يَشَأْ يُعَذِّبْكُمْ ۚ وَمَآ أَرْسَلْنَٰكَ عَلَيْهِمْ وَكِيلًۭا, tr:in yeşe' yerhamkum ev in yeşe' yuazzibkum ve mâ erselnâke aleyhim vekîlâ, gloss:dilerse size merhamet eder, dilerse azap eder; seni onlara vekil göndermedik, source:17:54}. Zorlama da sorunun içinde reddedilir: {ar:أَفَأَنتَ تُكْرِهُ ٱلنَّاسَ حَتَّىٰ يَكُونُوا۟ مُؤْمِنِينَ, tr:e-fe-ente tukrihu'n-nâse hattâ yekûnû mu'minîn, gloss:inanan olsunlar diye insanları sen mi zorlayacaksın, source:10:99}.

Yirmi üçüncü ayetteki istisna bu sınırın içinden çıkar: {ar:إِلَّا مَن تَوَلَّىٰ وَكَفَرَ, tr:illâ men tevellâ ve kefer, gloss:ancak yüz çevirip inkâr eden, source:88:23}. Yüz çevirme fiilinin kökü bir göreve geçmeyi de anlatır: {ar:تولى العمل أي تقلد, tr:tevelle'l-amele ey tekalled, gloss:işi üstlendi yani göreve geçti, source:"و ل ي,B003"}. Ayetteki anlam sırt dönmektir: {ar:ولى الرجل أي أدبر, tr:vellâ'r-raculu ey edbar, gloss:adam arkasını döndü, source:"و ل ي,B007"}. Yanında ise başa geçme anlamı duyulur. Peygamber'e verilmeyen göreve karşılık, yüz çeviren kendisi için yüz çevirmeyi üstlenmiştir. Yirmi dördüncü ayet cezayı Peygamber'e değil Allah'a verir: {ar:فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ, tr:fe-yuazzibuhullâhu'l-azâbe'l-ekber, gloss:Allah da onu en büyük azapla cezalandırır, source:88:24}. Allah'ın adı kulluk edilenin adıdır: {ar:فالإله الله تعالى لأنه معبود, tr:fe'l-ilâhu'llâhu teâlâ li-ennehû ma'bûd, gloss:ilah Allah'tır çünkü kulluk edilendir, source:"ء ل ه,B001"}. Son iki ayette konuşan "Biz" olur ve iş bölümü tamamlanır: {ar:إِنَّ إِلَيْنَآ إِيَابَهُمْ, tr:inne ileynâ iyâbehum, gloss:dönüşleri şüphesiz Bize'dir, source:88:25}; {ar:ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم, tr:summe inne aleynâ hısâbehum, gloss:sonra hesapları da şüphesiz Bize düşer, source:88:26}. Kur'an aynı bölüşümü tek bir cümlede söyler. Allah Peygamber'e, vaat edilenin bir kısmını ona göstersin ya da canını alsın, şunu der: {ar:فَإِنَّمَا عَلَيْكَ ٱلْبَلَٰغُ وَعَلَيْنَا ٱلْحِسَابُ, tr:fe-innemâ aleyke'l-belâğu ve aleyne'l-hısâb, gloss:sana düşen yalnızca duyurmaktır, hesap ise Bize düşer, source:13:40}. Önceki sure de aynı sırayı izler: önce {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-zekkir in nefeati'z-zikrâ, gloss:hatırlatma fayda verirse hatırlat, source:87:9}, sonra {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yezzekkeru men yahşâ, gloss:içi titreyen öğüt alacak, source:87:10}, sonra {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht ondan kaçınacak, source:87:11} ve en büyük ateş gelir. Başka yerlerde de şöyle denir: {ar:وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ, tr:ve zekkir fe-inne'z-zikrâ tenfeu'l-mu'minîn, gloss:hatırlat; hatırlatma inananlara fayda verir, source:51:55}; {ar:كَلَّآ إِنَّهَا تَذْكِرَةٌۭ, tr:kellâ innehâ tezkira, gloss:hayır; bu bir hatırlatmadır, source:80:11}; {ar:فَمَن شَآءَ ذَكَرَهُۥ, tr:fe-men şâe zekerah, gloss:dileyen onu anar, source:80:12}.

Kaynaklar: 88:21 فَذَكِّرْ ذ ك ر B009; 88:21 مُذَكِّرٌ ذ ك ر B003; 88:22 لَّسْتَ ل ي س B001; 88:22 بِمُصَيْطِرٍ س ط ر B001; 88:22 بِمُصَيْطِرٍ س ط ر B003; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:23 تَوَلَّىٰ و ل ي B003; 88:23 تَوَلَّىٰ و ل ي B007; 88:23 وَكَفَرَ ك ف ر B003; 88:24 ٱللَّهُ ء ل ه B001; 88:26 حِسَابَهُم ح س ب B001

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

