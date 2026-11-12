import json,glob,subprocess,os,sys
calls=json.load(open('calls.json'))
items=[]
for f in sorted(glob.glob('/root/.claude/projects/-home-user/3a5c4b7d-4602-5541-b0fe-22f390b862a8/tool-results/mcp-Magica-get_generations-*.txt')):
    items+=json.load(open(f))['items']
dest='../book/img'
got=0; missing=[]
for k,inp in calls:
    p=inp['prompt']
    m=[i for i in items if i['prompt'] and i['prompt'].strip()==p.strip()]
    out=f'{dest}/{k}.png'
    if os.path.exists(out): got+=1; continue
    if not m: missing.append(k); continue
    url=sorted(m,key=lambda i:i['createdAt'])[-1]['url']
    r=subprocess.run(['curl','-sS','-o',out,url]); 
    if r.returncode==0: got+=1
    else: missing.append(k)
print('have',got,'missing',missing)
