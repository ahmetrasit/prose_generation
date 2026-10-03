import hashlib
import json
import re
from pathlib import Path

ROOT = Path('/Volumes/aro/projects/prose_generation')
WORK = ROOT / 'enrichment/v1/work/1'
BASE = ROOT / '_commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md'
summaries = {
3:['Hidayet istenir; abd ailesindeki çiğnenmiş yol kulluk anlamının yanında okunur.'],
5:['Hidayetin yolu/evi tanıtma, önden gitme, devam etme dalları ihdinâ duasında birleştirilir.'],
7:['Sırat düz yol olarak tanımlanır; s/ṣ/z telaffuzları; q-w-m düz çizgi ve mızrak.'],
9:['İstek bilgiyi aşan toplulukla yürüme olarak sunulur; 1:7 önceki nimet sahiplerinin yolu.'],
11:['âlemîn/alam nişanları; mâlik/milk yol ortası; dîn/âdet sürdürülen yürüyüş.'],
13:['abd/abâbîd dağılışı; mustaqîm/kavm; anʿamta/ana yol ve dağılış; dalâl/ev bulamama; hidayet karşıtlığı.'],
15:['6:153 tek yol/çok yol; 6:161 din/yol; 28:22 yol ortası; 16:15–16 yollar/işaretler.'],
17:['6:71 şaşkın yolcu; 93:7 dalâl; 7:16–17 dört yönlü pusu; 36:60–62 ve 3:51 kulluk/yol; 37:23 cehennem yönü.'],
23:['ʿabd ailesinde yol, katranlı deve ve insan köleleştirme müzellel niteliğiyle bağlanır.'],
25:['Allah/ilah/mabud; Rabb efendi/sahip; mâlik elin tuttuğu mülk; memlûk köle.'],
27:['dîn boyun eğdirme/itaat/mülk dalları sahibi–kul sahnesine katılır; ayet dîn=karşılık.'],
29:['1:5 iltifat: üçüncü kişiden ikinci kişiye geçiş; iyyâka öne alınması; ibadet=nihai boyun eğme.'],
31:['Yaratılmış insanın Allahʿa aitliği; 19:93; ibadetin bunu kabul olması; muʿabbed/ağırlanan kişi evine eklenir.'],
33:['16:75 köle ve hamd; 36:71–72 hayvanlar; 26:18–22 Firavun; 12:23 rabbî insan efendi yorumu; 3:64 ve 12:40 sınır.'],
39:['Yevmüʿd-dîn hesap/hüküm/karşılık günüdür.'],
41:['Yevm olay ve şiddetli gün; yevmeizin; mâlik ile melik/hükümdarın güçlü eli.'],
43:['mustaqîm/qiyâma/kayyûm ailesi diriliş; Allahʿa gazap=cezalandırma tanımı.'],
45:['dîn ve dayn farklı kelimelerdir; hesap borç kapanışı; q-w-m kıymet/fiyat/denge sikke.'],
47:['gh-y-r diyet/takas; d-l-l kanın boşa gitmesi/unutan tanık; bunlar 1:7 anlamının yanında.'],
49:['Surenin doğru yolu ve şaşmayan teraziyi aynı kökte anması; borç–fiyat–tartı sentezi.'],
51:['82:16–19 yetkinin Allahʿa aitliği; 83:3–6 eksik tartı/ayağa kalkış; 40:16,25:26; 21:47 ve 101:6–8 teraziler.'],
53:['2:282 borç/unutma/akvem; 26:182 ve 17:35 müstakîm tartı; diyet/fidye sınırı; 2:16 hidayet takası; 51:6 ve 26:82.'],
59:['r-h-m rahmet/rahim/akrabalık; rahim ev olarak tasvir; doğum acısı; Allahʿın rahmeti iyilikle ayrıştırılmalı.'],
61:['Rabb terbiye/tamamlama; üvey ebeveyn ve dadı; süt koyunu; rabbânî öğretici.'],
63:['Basmala rahmet–Rab–rahmet çerçevesi rahim→terbiye evine dönüştürülür; q-w-m ev idaresi; nimetli çocuk ve gh-y-r erzak/kıskançlık.'],
65:['3:6 rahimler;4:1 akrabalık;4:23 üvey kızlar;17:23–24 ibadet, rahmet, alçalma ve büyütme birlikte.'],
67:['Musa annesi/ev/ilahi göz altında yetişme; Firavunʿun büyütme iddiasının sınırı;3:79 rabbânî ve55:1–4 öğretme.'],
73:['n-ʿ-m el/iyilik/tamamlama; Rabb nimeti ve sanîʿayı tamamlar.'],
75:['Hamd–şükür kapsam iddiası; ahmedu ilayka nimet anlatımı; yetehammedu başa kakma.'],
77:['Rahmet iyilik kaynağı; hamd nimet adı anılmadan önde; nimet yol nimeti ve tamamlanması yürüyüş.'],
79:['48:2,2:150,5:3,12:6,16:121 nimet/hidayet/tamamlama;93:11 anlatma;106:3–4;7:43,10:10 sonunda hamd;26:22 başa kakma.'],
85:['1:7 üçlü sınıflama ve aleyhim; nimet aktif/gazap pasif; hamd–rıza/nimet–niʿma/gazap karşıtlıkları.'],
87:['İnsan gazabının kan/kırmızı/asık/şiş yüz dalları; nimetin yumuşak/serin göz dalları karşılaştırılır.'],
89:['İki sonuç iki yüz diye kuruluyor; eyyâmullâh azap ve nimet günleri;14:5.'],
91:['20:81–82 ve86 gazap inişi ve hidayet;7:152;5:60;3:162 rıza–gazap yürüyüşü.'],
93:['4:69 nimet sahipleri ve refik;19:58;88:2,8–9,83:24,80:38–41 yüzler; aleyhâ/alayhim benzeşimi.'],
99:['Bism/ism s-m-w yükselme; alternatif w-s-m damga; iz okuma; iki etimoloji tek işlem diye birleştirilir.'],
101:['ʿ-l-m iz/dağ/sancak/bilgi; âlem varlığı bildiren işaret; çoğulun kapsamı.'],
103:['Ad–âlem işaret çifti; Allah en büyük ad şeklindeki nakil; işin altına ad koyma sentezi.'],
105:['87:1,55:78,96:1,19:65 ad/yükseklik/kulluk/bilgi;17:110;25:60;12:40 ataların adları.'],
107:['27:29–30 mektup basmalası;11:41 gemi;2:31 Âdemʿin adları;15:75 ve68:16 vesm izleri.'],
113:['Yevm güneşli gün; q-w-m öğle/gündüz terazisi; s-m-w hilal/semâ; n-ʿ-m Ay konağı; âlem felek.'],
115:['Öğlen gölgesizliği ve yol düzlüğü; ilâhe güneşin adı ve ibadetin ondan ayrılması.'],
117:['41:37 güneş/ay secdesi yasağı;6:75–79 İbrahimʿin sözleri ve hidayet;27:23–24;10:5,2:189 hesap;18:17.'],
123:['Rabb bulut/kalma; n-ʿ-m güney rüzgârı; s-m-w yağmur/bitki; w-s-m ilk yağmur izi.'],
125:['Rabb yazın solmayan ot/bol su; gh-y-r yağmurla düzeltme/sulama; n-ʿ-m taze hayat; hamd beğenilen toprak.'],
127:['ʿaylam kuyu; naʿâma kiriş; qâma makara; malik/melk yolcu suyu ve su kralları; qiwâm–milâk.'],
129:['Rab/bitkiyi büyüten bulut ve mustaqîm/makara Fatihaʿya eklenir; susuz kalmayan yolcu sentezi.'],
131:['42:28 yağmur/rahmet/hamd;7:57 rahmet/diriliş;30:48–50 iz;80:24–32 besin;32:27 çorak toprak.'],
133:['28:22–24 Musa yol/su/gölge;12:10,19 Yusuf kuyusu;67:30 su kaybı;26:78–79 yaratma/hidayet/su.'],
139:['Sürü Rabb/mâlik; enʿâm; damga/taranmış deve; milk/hâdî öncü ve boyun; merabb/otlak.'],
141:['Dâlle sahibi bilinmeyen deve, kopuş; Rabb–mâlik tanımlarda; rabrab ve âne yabani sürüler.'],
143:['İhdinâ sürü öncüsü ardında yürümek olarak görselleştirilir; dâllîn sahibinden kopmuş hayvan.'],
145:['16:5–9 hayvanlardan yola geçiş;36:71–72;7:179,25:44 daha sapmış insan; hayvan sahibini tanır çıkarımı.'],
151:['ʿ-b-d yolda kalma; q-w-m bineğin durması; h-d-y güçsüz/yaslanarak sallanma ve ihdinâ bağlantısı.'],
153:['nastaʿîn talebüʿl-avn; q-w-m doğrulma/destek; hedy iyi yürüyüş; m-l-k duvar/kalp; ʿabada güç ayrı çekirdek.'],
155:['1:5→6 yardım→yol ilişkisi; beden/omuz/dik duruş; duası yorgun binekli yolcu diye sentezlenir.'],
157:['18:77 duvar;18:95 güçle yardım;12:18 ve21:112;7:128,2:45,5:2;67:22 ve25:63 yürüyüş karşılaştırması.'],
163:['Sırat s-r-ṭ yutma/gözden kaybolma; dalâl gizlenme/gömülme/sütte kayıp/unutan hafıza.'],
165:['Yönü olan ve varışsız iki kayboluşun 1:6–7 karşılaştırması.'],
167:['32:10 ölüm/diriliş;6:24 ortak kaybı;82:16 kaybolamama;20:52 Allahʿın kaybetmemesi;Yusuf kayıp ve36:66 kör yol.'],
173:['H-d-y kurbanlık/Harem/varış/kurbet; enʿâm/uysallaştırma; ad/yükselme; vesm/hac mevsimi.'],
175:['H-d-y gelin eve/hediye dosta/sığınan koruma; m-l-k nikâh; Rabb/ribâbe ahit.'],
177:['Hidayet bütün dört götürüşü eve varış şeklinde birleştirir; düz mealin varışsız olduğu iddiası.'],
179:['22:33–37 ad/kurbanlık/hidayet;2:196,5:95,48:25,5:2;9:6 güvene ulaştırma;27:35–36 hediye;6:118.'],
185:['Kulluk ve yol aynılaştırılır; müzellel deve/yol;36:61.'],
187:['Sürü/yol kayıp deveyle;16:9 ikinci Türkçe gloss farkı;kurbanlık/ad/uysallaştırma/hidayet.'],
189:['Rahim/tamamlama Rabbʿde;26:18–22 beş ağ ve sahte büyüten–gerçek Rab karşıtlığı.'],
191:['Gazap/hesap yüzleri;20:81 düşüş ile tökezleme aynılaştırılır;67:22 doğrulma.'],
193:['2:282 borç/unutma/akvem;öğle terazisi;83:3–6 ölçü–ayağa kalkış; yazı/dik durma yorumu.'],
195:['Musa Medyen yol/su/gölge ile kiriş/makara;26:78–82 hayat ve hesap sırası.'],
197:['İbrahim yıldız/ay/güneş semâve;Rab/değişen gök;işaret ile işaret edilen ayrımı.'],
199:['Tüm sure ad→besleyen Rab→hesap→kul/yardım→öncü/destek→ev→kayıp deve bütünleşik ağında okunur.'],
}

text = BASE.read_text()
lines = text.splitlines()
prose_lines = [i for i,s in enumerate(lines,1) if s and not s.startswith(('##', 'Kaynaklar:'))]
assert sorted(summaries) == prose_lines
section = None
rows = []
for i,s in enumerate(lines,1):
    if s.startswith('## '): section=s[3:]
    if i not in summaries: continue
    tags = re.findall(r'\{[^{}]+\}',s)
    qrefs = sorted(set(re.findall(r'source:(\d+:\d+)',s)), key=lambda t:tuple(map(int,t.split(':'))))
    lex = sorted(set(re.findall(r'source:"([^"\n]+,B\d+)"',s)))
    cats=[]
    if lex: cats.append('lexical_root_resonance')
    if any(not x.startswith('1:') for x in qrefs): cats.append('cross_quran')
    if i in (3,5,7,9,25,27,29,31,39,43,61,75,85,93,99,101,103,153,173,175): cats.append('contextual_meaning_or_grammar')
    if i in (11,13,49,63,77,89,103,113,115,123,127,129,139,141,143,151,155,163,165,177) or i>=185: cats.append('project_synthesis')
    rows.append(dict(id=f'S1-P{i:03d}',base_line=i,section=section,base_paragraph_sha256=hashlib.sha256(s.encode()).hexdigest(),claims=summaries[i],categories=cats,quran_refs=qrefs,lexical_branches=lex,inline_tags=len(tags)))

record=dict(scope=dict(surah_number=1,ayah_scope='1:1-7',base_file=str(BASE),output_language='Turkish',mode='comprehensive',base_numbering='basmala = 1:1'),reads=dict(instructions_complete=True,instruction_chunks=[[1,250],[251,500],[501,750],[751,990]],base_complete=True,base_chunks=[[1,25],[26,50],[51,75],[76,100],[101,125],[126,150],[151,175],[176,199]],canonical_and_base_truncation=False),base_sha256=hashlib.sha256(BASE.read_bytes()).hexdigest(),physical_lines=len(lines),base_blank_separated_blocks=len(re.split(r'\n\s*\n',text.strip())),prose_paragraphs=len(rows),claims=rows)
WORK.mkdir(parents=True,exist_ok=True)
(WORK/'claim_map.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
matrix = dict(stage='precomposition_claim_inventory',annotations_composed=False,claims=[dict(claim_id=r['id'],claim=r['claims'],supporting_sources=[],contradicting_sources=[],early_attestation=[],later_development=[],hadith_relation='pending',historical_context='pending',novelty_status='pending',confidence='pending',retrieval_state='pending') for r in rows])
(WORK/'evidence_matrix.json').write_text(json.dumps(matrix,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'prose_paragraphs':len(rows),'base_blocks':record['base_blank_separated_blocks'],'claim_map':'claim_map.json','matrix':'evidence_matrix.json','stage':matrix['stage']}))
