from pathlib import Path
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import subprocess, json, re, hashlib, time

ROOT=Path('/Volumes/aro/projects/prose_generation')
WORK=ROOT/'enrichment/v1/work/107'
SOURCES=WORK/'sources'
BASE=ROOT/'_commentary/v16/out/s107/images.r13.map3.nohft.tool.tool/images.md'
SOURCES.mkdir(parents=True,exist_ok=True)

class NassParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth=0; self.start=None; self.buf=[]; self.sections=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='div':
            self.depth+=1
            if 'nass' in a.get('class','').split(): self.start=self.depth; self.buf=[]
        if self.start and tag in ('p','br','hr'): self.buf.append('\n')
    def handle_endtag(self,tag):
        if self.start and tag=='p': self.buf.append('\n')
        if tag=='div':
            if self.depth==self.start:
                self.sections.append(re.sub(r'\n\s*\n+', '\n', ''.join(self.buf)).strip()); self.start=None
            self.depth-=1
    def handle_data(self,data):
        if self.start: self.buf.append(data)

def retrieve(item):
    key,url=item; raw=SOURCES/f'{key}.html'; out=SOURCES/f'{key}.txt'
    if not raw.exists():
        r=subprocess.run(['curl','-fsSL','--retry','1','--max-time','45',url,'-o',str(raw)],capture_output=True,text=True)
        if r.returncode: return dict(key=key,url=url,state='failed',error=r.stderr.strip())
    s=raw.read_text(); p=NassParser(); p.feed(s); extracted='\n\n'.join(p.sections)
    out.write_text(extracted+'\n')
    return dict(key=key,url=url,state='retrieved_not_inspected',sections=len(p.sections),chars=len(extracted),lines=len(extracted.splitlines()),text_file=str(out.relative_to(ROOT)),html_sha256=hashlib.sha256(raw.read_bytes()).hexdigest(),text_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),text_prefix=extracted[:110])

def corpus():
    jobs=[]
    for author in ['tabary','katheer','qortobi']:
        jobs += [(f'{author}_107_{a}',f'https://quran.ksu.edu.sa/tafseer/{author}/sura107-aya{a}.html') for a in range(1,8)]
    for author in ['seoty','zamakhshary','alrazy','baidawy','beqaay']:
        jobs += [(f'{author}_107_{a}',f'https://quran-tafsir.net/{author}/sura107-aya{a}.html') for a in range(1,8)]
    with ThreadPoolExecutor(max_workers=6) as pool: rows=list(pool.map(retrieve,jobs))
    (WORK/'retrieval_index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    for row in rows: print(row['key'],row['state'],row.get('chars',0),row.get('lines',0),row.get('error',''))

summaries={
2:'Eraeyte dinleyiciyi uyarıp haber isteme kalıbıdır; görme göz ve içgörü kapsamındadır.',
3:'Riya başka gözler için davranma; karşılıklı görme, ayna ve güzel kılık imgeleriyle yüzey sahnesi kurulur; altıncı ayet kapanış gibi adlandırılır.',
4:'Aile imgelerinin bağlamsal anlamı değiştirmediği kontrolü.',
5:'Açılıştaki gerçekliği gören bakış ile gösteriş için aranan yüzey bakışı karşı karşıya konur.',
6:'İşaret edatı hareketi görünür kılar; yetim, yapılmayan teşvik, namaz, seyirci ve esirgenen küçük şey bir bakış güzergahıdır.',
7:'Alak, Şuara, Nisa, İnsan ve Leyl sahneleri gerçek seyirci/gösterişsiz verme karşıtlığına bağlanır.',
10:'Tekzib kökünün söz/fiil yalanı, boya ile dokuma süsü taklit eden kumaş ile okunur.',
11:'Yarıda kalan hücum, süt, koşu; gebeliği belli eden deve ile yalan/doğru ve devamlılık imgesi.',
12:'Yalanlama davranışın yüzeyi/niyeti ve başlangıcı/devamı arasındaki tutarsızlık olarak resmedilir; din niyete göre yargı sözleriyle birleştirilir.',
13:'Fe sonucu/delili, an/fi ayrımı; görünür namazın ibadetten uzaklığı; seyirciye bakan koşu ve yetime geç kalan iyilik.',
14:'Kaya/toprak, kütükler, iyilik/namaz/zekat ve yarıda kesilen verme; sürdürülen ibadete karşı sahneler.',
17:'Yetim kopuş/yalnızlık; gaflet ve gecikme etimolojileri sehv ile tanım üzerinden birleştirilir.',
18:'Suhâ yıldızı, tek inci, gözden kaçan çocuk ve müsâhât ile iyi/kötü gözden kaçırma karşıtlığı.',
19:'Yetimin ihmali ve namaz ihmali, kendini görünür kılma arzusuna bağlanır; üçüncü ayette yemeğin hiç anılmadığı sözü kontrol edilmeli.',
20:'51:11 gaflet seli, 93:6 barındırma ve 9:67 karşılıklı unutma ana ağa katılır.',
23:'Sert itiş, koyun sürme ve düşene kalk deme aynı ailede aşağı/yukarı hareket imgesine bağlanır.',
24:'Hadd teşvik/karşılıklı teşvik; hadîd dip noktası yoksula yönelen itiş sahnesidir.',
25:'Miskin durgun/güçsüz; sehv durgunluğu; engel olma ile koruyucu çevre karşıtlığı; baba kaybı tüm koruma kaybı gibi sunulur.',
26:'Muzari alışkanlık; teşvik etmeme doğrudan vermemeden bile az bedelli eksiklik; namazdaki durgunluk ve men engeli.',
27:'Tur itiş/ateş; Fecr ve Duha yetim/teşvik; Nisa ve Kalem cimrilik; Beled merhamet karşı sahnesi.',
30:'Çoluk çocuk, ev, ev halkı, azık, sehve sundurması/rafı aynı evin parçalarıdır.',
31:'Maun ev araçları, ödünç nesneler, ev/konak ve küçüklük anlamları; borç eşya verme az maliyetli yardım olarak sunulur.',
32:'Daʿdaʿa ölçek/çuval/tabak doldurma, itme ailesi içinde; yemek, yemek isteme, çok konuk ağırlama, maun iyilik ve vermeme.',
33:'Yetimi iten el dolu kap eli olabilirdi; ev, azık ve raf kelime sırasına yerleştirilir.',
34:'İnsan doyurma; Yasin vermeyi reddetme; Kehf konuk ağırlamayan kasaba ve yetimler; Yusuf ölçek, Mutaffifin eksik ölçü, Nisa hak paylaşımı.',
37:'Maun/maʿin akan su, vadi yatakları, sulanmış toprak/ot, yerleşme sağlayan otlak, tatmanın suya uzanması.',
38:'Yemeği ve maunu esirgeme akan su yatağını tıkama olarak yorumlanır.',
39:'67:30 eraeytum/maʿin; 23:50 barınak, karar ve su; 93:6 yetime sığınak bağlantısı.',
42:'Salat ailesine eklenen ateş/ısınma/pişirme/değnek düzeltme/şiddet anlamları; seken ocak.',
43:'Veyl felaket çığlığı; ocak yardımı esirgeme ile ahiret ateşine geçiş; namaz kökü ateş taşır savı.',
44:'Hakka teşvik etmeme/ateş; Mutaffifin veyl/tekzib/din/yanma; Leyl, Nisa yetim malı, Kaf engelleyen el.',
47:'Din hesabı, dayn borcu, itaat ve tekzib; kalıp kezebe aleyke vacip/teşvik anlamıyla borcun inkârı karşıtı.',
48:'Maunun cahiliye/İslam anlamları; itaat/zekat; emʿane bi-hakkî ile emʿane lî bi-hakkî ve inkıyad; din-maun itaat bağı.',
49:'İlk din nesnesi-son küçük borç; hesap defteri; 82:9,1:4 ve Meâric karşı dizisi; Fussilet, İsra ve Zariyat hak.',
52:'Salat ibadet/dua; Allahın salatı insan duasından ayrılmalı; seken huzur anlamı ve miskin ailesi.',
53:'9:103 sadaka→arındırma→dua→huzur döngüsü maun zekatına bağlanır.',
54:'107 namazının dışa dönük toplumsal huzur etkisi kopmuştur; görünüş seyirciye döner.',
55:'Hud, Meryem, Bakara, Tevbe, Ankebut ve yitirilen namaz; salat ve mal ahlakı birlikte.',
58:'Suhâ görme/gaflet ağı ile Alak namaz engelleme/tekzib/ilahi görme birleşir.',
59:'Tur 52:13-14 yetimi itenin ateşe itilmesi; Hakka pişirilmeyen ocak-ceza karşılığı.',
60:'Müddessir namaz/yoksul/gaflet/tekzib kelime dizisi tüm imgelerin tek itirafı sayılır.',
61:'Maun ev/su/borç; âvâ iki sahne; itiş çocuk/tabak; men koruyucu çevre ile esirgeme birleşimleri.',
62:'Meâric borç-hak/namaz; Tevbe pay-dua-huzur bütünleşik ağ; 107 çözülmüş karşı sahne.',
63:'Tüm sure bakış-hesap→ev kapısı→namaz/ateş→seyirci→raf; din/maun itaat uçları olarak bütünleştirilir.'}

def claim_map():
    b=BASE.read_text(); blocks=[p for p in re.split(r'\n[ \t]*\n',b) if p.strip()]
    rows=[]; section=''
    for n,p in enumerate(blocks,1):
        if p.startswith('## '): section=p[3:]
        if n not in summaries: continue
        lex=sorted(set(re.findall(r'source:"([^"\n]+,B\d+)"',p)))
        refs=sorted(set(re.findall(r'source:(\d+:\d+)',p)),key=lambda x:tuple(map(int,x.split(':'))))
        categories=['project_synthesis']
        if lex:categories.append('lexical_root_resonance')
        if refs:categories.append('contextual_meaning_or_cross_quran')
        rows.append(dict(id=f'S107-P{n:02}',base_block=n,section=section,claims=summaries[n],categories=categories,quran_refs=refs,lexical_branches=lex,paragraph_sha256=hashlib.sha256(p.encode()).hexdigest()))
    assert len(rows)==sum(not p.startswith(('##','Kaynaklar:')) for p in blocks)
    record=dict(scope=dict(surah_number=107,ayah_scope='107:1-7',base_file=str(BASE),language='Turkish',mode='comprehensive'),reads=dict(instructions_complete=True,instruction_chunks=[[1,180],[181,360],[361,550],[551,730],[731,990]],base_complete=True,base_chunks=[[1,24],[25,47],[48,69],[70,93],[94,125]],truncated_aggregate_25_69_reread=True,final_reads_truncated=False,ledger_complete=True,reference_implementation='absent; no contents inferred'),base_sha256=hashlib.sha256(BASE.read_bytes()).hexdigest(),physical_lines=len(b.splitlines()),base_blocks=len(blocks),prose_paragraphs=len(rows),claims=rows)
    (WORK/'claim_map.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    (WORK/'evidence_matrix.json').write_text(json.dumps(dict(stage='claim_inventory_before_research',annotations_composed=False,claims=[dict(claim_id=r['id'],claim=r['claims'],supporting_sources=[],contradicting_sources=[],early_attestation=[],later_development=[],hadith_relation='pending',historical_context='pending',novelty_status='pending',confidence='pending') for r in rows]),ensure_ascii=False,indent=2)+'\n')
    print('claim map',len(rows),'prose paragraphs',len(blocks),'base blocks')

if __name__=='__main__':
    import sys
    if 'claims' in sys.argv:claim_map()
    if 'corpus' in sys.argv:corpus()
