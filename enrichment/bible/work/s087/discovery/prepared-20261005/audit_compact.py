"""Display tool code for operator review; never attests or launches agents."""
import json,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parent
for key in sys.argv[1:]:
 target,model=key.rsplit('/',1)
 r=subprocess.run([sys.executable,'-B',str(root/'operator.py'),'audit','--target',target,'--model',model],capture_output=True,text=True)
 d=root/target.replace(':','_')/model
 print(f'JOB {target}/{model}',flush=True)
 for line in (r.stdout+r.stderr).splitlines():
  try:item=json.loads(line)
  except ValueError:print(line);continue
  if 'code' not in item:
   print(json.dumps(item,ensure_ascii=False));continue
  code=item['code'].replace(str(d),'$JOB').replace(str(d.relative_to(root.parents[5])),'$JOB')
  print(f"P{item['phase']} {item['name']} {item['call_id']} (omitted {item['omitted_tsv_data_lines']} data lines)\n{code}",flush=True)
