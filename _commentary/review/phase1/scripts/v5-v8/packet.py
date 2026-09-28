import json,sys,re
p=sys.argv[1]
t=open(p,encoding='utf-8').read()
i=t.find('<lane_packet_json>'); j=t.find('</lane_packet_json>')
print('prompt bytes',len(t.encode()),'packet bytes',len(t[i:j].encode()), 'pre-packet bytes', len(t[:i].encode()))
pk=json.loads(t[i+len('<lane_packet_json>'):j])
def sz(x): return len(json.dumps(x,ensure_ascii=False).encode())
for k,v in pk.items():
    extra=''
    if isinstance(v,list): extra=f'list[{len(v)}]'
    elif isinstance(v,dict): extra='dict keys='+','.join(list(v.keys())[:12])
    print(f'{k:40s} {sz(v):>9d} {extra}')
