from pathlib import Path
import hashlib, json, re

W=Path(__file__).resolve().parent
BASE=W.parents[3]/'_commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md'
# Resolve explicitly: research artifacts are scoped to this work directory.
BASE=Path('/Volumes/aro/projects/prose_generation/_commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md')
chunks=[p for p in re.split(r'\n[ \t]*\n',BASE.read_text()) if p.strip()]
claims=[
 ('C01',[1],'methodological','Process/checker preamble is base prose, not reader commentary; preserve and flag.'),
 ('C02',[3,4],'contextual|grammar|lexical','Opening oath: running/panting animals; horses inferred, feminine active participles, fa-linked sequence; camel/hajj alternative must be assessed.'),
 ('C03',[5,6,7],'project_synthesis|lexical|structural','Horse body, lean arrow shaft, collected run, rider-side, witness-run, shadd-run and winning chest form horse/man-Lord contrast.'),
 ('C04',[8],'cross_quran|project_synthesis','38:31–33 horses/hubb al-khayr/Rabb; 3:14 attractive wealth; ambiguous an and wiping/slaughter reading require control.'),
 ('C05',[11,12],'contextual|historical|lexical','Dawn raid, root of mughīrāt; all raiding inferred unethical from udwān? Night approach and unarmed sleeping host claimed.'),
 ('C06',[13,14],'contextual|grammar|lexical|project_synthesis','Dust and cry; bihī antecedents; penetrating host; communal/loot slaughter resonance.'),
 ('C07',[15,70],'project_synthesis|cross_quran|nazm','Dawn raid as rehearsal of sudden eschatological judgment; dust/graves; 37:177 etc; no escape and all human gathering.'),
 ('C08',[18,19],'contextual|historical|lexical','Hooves strike sparks; generic iron/flint mechanism; dabh burn/ash extensions and stones.'),
 ('C09',[20,21],'project_synthesis|lexical','Useless hubāhib sparks, lasting morning/lamp, man seeing fire and thinking by striking; beneficial/error fire.'),
 ('C10',[22],'cross_quran|project_synthesis','56:71–73 and 36:78–80 fire/resurrection; Moses 28:29/27:7/20:10 fire→news→habīr.'),
 ('C11',[25,26,29],'lexical|contextual|cross_quran|project_synthesis','Stirring/ploughing/grasshoppers; baʿthara vs thawr distinct roots; graves turned out; mā object-like inference; 82:4 and 54:7 etc.'),
 ('C12',[27,71],'lexical|project_synthesis|cross_quran','W-r-y fire and concealment/grave; 5:31 burial reversed; fire/tree and rain/earth resurrection converge.'),
 ('C13',[28,32],'lexical|contextual|historical|project_synthesis','Tahṣīl gold/ore, grain/chaff, collection/account remainder; miner woman; passive Form II does not mechanically prove temporal stepwise work.'),
 ('C14',[33,34,72],'project_synthesis|lexical|theological','Love/grain/heart kernel/husk/crop waste/crop-chest; hidden graves and chests; treasure purged and hoarder gathered.'),
 ('C15',[35],'cross_quran|historical','3:154 battle/Uhud chest purification; 3:29/47:29/86:9/99:7 hidden acts exposed.'),
 ('C16',[38,39],'contextual|lexical|project_synthesis','Rabb nurture, ownership, cloud/water; kenūd cut rope/thanks, counting harms vs gifts; barren ground; benefaction return rope.'),
 ('C17',[40,42,71],'project_synthesis|cross_quran','Cloud raised, pooled water/good clay/low-ground habrā/farmer habīr/grain→unproductive kenūd ground; 7:57–58 and 30:48.'),
 ('C18',[41,64,65,75],'contextual|grammar|theological|project_synthesis','Shahīd pronoun man vs God; plural rabba-hum; witness→knowledge→inner divine knowledge; God knowledge not acquired by experiment.'),
 ('C19',[42,75],'cross_quran|project_synthesis','Counting gifts, rescued ingratitude, independence, generous Lord; 7:172 Rabb/witness primordial covenant.'),
 ('C20',[45],'contextual|semantic_history|lexical','Khayr wealth, much/licit wealth requirement from lexical branch; normative restrictions cannot automatically bind Q100.'),
 ('C21',[46,47,49,50],'contextual|lexical|project_synthesis','Love as attachment/stalled camel; shadīd intense love vs miser; closed fist/shackle/collecting wealth, collected chest reversal.'),
 ('C22',[47,48,51],'rivayet|hadith|historical|project_synthesis','Kenūd solitary eater/beat slave/withhold aid report; shared cauldron/ladle/cup/lot arrows/quiver/meat division; maysir context distinct from Qurʾan approval.'),
 ('C23',[54,55,56,74],'lexical|cross_quran|project_synthesis','Morning camel watering/pool/quenching/habb-drinking/sadr-return; 28:23 and 99:6 human dispersal; proverb experienced drinker→habīr.'),
 ('C24',[59,60,61,70],'lexical|structural|project_synthesis','Jamʿ host→universal gathering; mashhad/ḥaṣala collecting and yawmāidh; hajj Jamʿ/Muzdalifa antecedent and scale change.'),
 ('C25',[64,65,66],'project_synthesis|cross_quran|theological','Witness/knowing/habīr triad; 67:13–14 mirror, 75:13–15 self witness, 24:24/41:21 body evidence, 50:16 closeness, 99:4 earth news.'),
 ('C26',[69],'project_synthesis','Running-raiding-spark-sabah combined overt scene; lexical variants are supporting, not alternative contextual translation.'),
 ('C27',[72],'project_synthesis|cross_quran','Love wealth/gold purification/9:34–35 fiery punishment and 47:37 hidden rancor; old ingredients vs combined network.'),
 ('C28',[73],'project_synthesis|cross_quran','68:17–33 morning harvest, miserly exclusion, sleeping garden destruction, Lord; raid/being raided analogy is inferential.'),
 ('C29',[76],'project_synthesis|nazm','Entire surah sensory exterior→hidden chest/interiority; all eleven roots joined through layered scenes and epistemic progression.'),
 ('C30',[1,11],'rejected_candidate|method','Rejected rain/provision ghy-r for mughīrāt; owl/echo lore, loose rabb/riḅbiyyūn and maysir narration previously excluded, now assess relevant authorized evidence distinctly.'),
]
W.mkdir(parents=True,exist_ok=True)
(W/'sources').mkdir(exist_ok=True)
payload={'scope':{'surah_number':100,'ayah_scope':'100:1-11','base_file':str(BASE),'output_language':'Turkish','mode':'comprehensive'},'base_sha256':hashlib.sha256(BASE.read_bytes()).hexdigest(),'instructions_read':'all 990 lines, bounded ranges','base_read':'all 151 lines, bounded ranges; aggregate-truncated portions re-read individually','paragraphs':[{'index':i,'sha256':hashlib.sha256(p.encode()).hexdigest(),'kind':'heading' if p.startswith('#') else 'source_line' if p.startswith('Kaynaklar:') else 'prose','incipit':p[:180]} for i,p in enumerate(chunks,1)],'claims':[{'id':i,'base_blocks':b,'classes':c.split('|'),'claim':t} for i,b,c,t in claims],'workflow_state':'claim_map_written_before_annotations; evidence_matrix_pending_primary_inspection'}
(W/'claim_map.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print('claim map:',len(claims),'major claims;',len(chunks),'base blocks')
