import sys,subprocess,json,re,os,tempfile,shutil
svg=sys.argv[1]
s=open(svg).read(); s=s[s.index('<svg'):]
js='''<script>
function bb(e){var r=e.getBoundingClientRect();return [r.left,r.top,r.right,r.bottom];}
var ts=[...document.querySelectorAll('svg text')].filter(e=>!e.querySelector('textPath'));var out=[];
var T=ts.map(e=>{var b=bb(e);var h=b[3]-b[1];var rot=(e.getAttribute('transform')||'').includes('rotate')||!!e.closest('g[transform*=rotate]');return {t:e.textContent.slice(0,40),b:rot?[b[0]+2,b[1]+2,b[2]-2,b[3]-2]:[b[0],b[1]+h*0.28,b[2],b[3]-h*0.2],k:e.classList.contains('kn'),e:e};});
function ix(a,b){var w=Math.min(a[2],b[2])-Math.max(a[0],b[0]);var h=Math.min(a[3],b[3])-Math.max(a[1],b[1]);return (w>1.5&&h>1.5)?w*h:0;}
for(var i=0;i<T.length;i++){var a=T[i];if(a.b[2]-a.b[0]<1)continue;
 if(a.b[0]<50||a.b[1]<46||a.b[2]>WW-50||a.b[3]>HH-46)out.push('OUT-OF-FRAME: '+a.t+' '+a.b.map(Math.round));
 for(var j=i+1;j<T.length;j++){var c=T[j];var v=ix(a.b,c.b);if(v>3)out.push('TEXT/TEXT: "'+a.t+'" x "'+c.t+'" @'+a.b.map(Math.round));}}
var fs=[...document.querySelectorAll('svg g.f, svg line.w, svg g.kr, svg .ob')];
fs.forEach(f=>{var b=bb(f);T.forEach(a=>{if(a.e.closest('g.kr')===f||a.e.closest('.ob')===f||a.e.closest('g.f')===f)return;if(a.b[2]-a.b[0]<1)return;if(a.k&&f.getAttribute('class')=='f')return;var v=ix(a.b,b);if(v>3)out.push('TEXT/OBJ: "'+a.t+'" x '+(f.getAttribute('class'))+' @'+b.map(Math.round));});});
var cl=[...document.querySelectorAll('svg [data-box]')];
cl.forEach(g=>{var q=g.getAttribute('data-box').split(',').map(Number);g.querySelectorAll('text').forEach(e=>{var b=bb(e);if(b[2]-b[0]<1)return;if(b[0]<q[0]||b[1]<q[1]||b[2]>q[2]||b[3]>q[3])out.push('OUT-OF-BOX: "'+e.textContent.slice(0,40)+'" '+b.map(Math.round)+' box '+q);});});
document.getElementById('out').textContent=JSON.stringify(out);
</script>'''
m=re.search(r'viewBox="0 0 (\d+) (\d+)"',s)
js=js.replace('WW',m.group(1)).replace('HH',m.group(2))
h='<html><body style="margin:0">'+s+'<pre id="out"></pre>'+js+'</body></html>'
scratch_dir = '/home/sable/vesper'
tmp_dir = tempfile.mkdtemp(prefix='_adriata_qa_', dir=scratch_dir)
profile_dir = os.path.join(tmp_dir, 'profile')
os.makedirs(profile_dir, exist_ok=True)
tmp = os.path.join(tmp_dir, 'qa.html')
try:
    open(tmp, 'w').write(h)
    assert m is not None
    r = subprocess.run(['/snap/bin/chromium', '--headless=new', '--disable-gpu', '--no-sandbox', f'--user-data-dir={profile_dir}', '--window-size=%s,%s' % (m.group(1), m.group(2)), '--dump-dom', 'file://' + tmp], capture_output=True, text=True, timeout=120)
finally:
    shutil.rmtree(tmp_dir, ignore_errors=True)
mm=re.search(r'<pre id="out">(.*?)</pre>',r.stdout,re.S)
if not mm: print('QA FAILED',r.stderr[-500:]); sys.exit(1)
import html
res=json.loads(html.unescape(mm.group(1)) or '[]')
print(len(res),'issues'); [print(' ',x) for x in res]
