import math, random, html
from PIL import ImageFont
FD='/usr/share/fonts/truetype/noto/'
_F={}
def font(kind,size):
    k=(kind,size)
    if k not in _F:
        fn={'sans':'NotoSans-Regular.ttf','sansb':'NotoSans-Bold.ttf','serif':'NotoSerif-Regular.ttf','serifb':'NotoSerif-Bold.ttf','serifi':'NotoSerif-Italic.ttf','disp':'NotoSerifDisplay-Bold.ttf'}[kind]
        _F[k]=ImageFont.truetype(FD+fn,int(round(size*4)))
    return _F[k]
def tw(s,kind='sans',size=13,ls=0):
    return font(kind,size).getlength(s)/4*1.04+ls*len(s)
def esc(s): return html.escape(str(s),quote=False)

INK='#1b2d36'; TEAL='#144a5c'; GOLD='#c5963e'; DGOLD='#8f651d'; PARCH='#fbf6ec'; CORAL='#b5482f'; WALL='#26353c'

DEFS='''
<linearGradient id="parchment" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fbf6ea"/><stop offset="1" stop-color="#efe3cc"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.5" r="0.75"><stop offset="0.6" stop-color="#7a5a2a" stop-opacity="0"/><stop offset="1" stop-color="#7a5a2a" stop-opacity="0.22"/></radialGradient>
<linearGradient id="seaGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0e566d"/><stop offset="0.55" stop-color="#1b8098"/><stop offset="1" stop-color="#45adbd"/></linearGradient>
<linearGradient id="seaGradH" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0e566d"/><stop offset="0.7" stop-color="#1f8aa1"/><stop offset="1" stop-color="#58bccb"/></linearGradient>
<linearGradient id="seaGradV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3fa9ba"/><stop offset="1" stop-color="#0d4f65"/></linearGradient>
<linearGradient id="poolGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7fdbe4"/><stop offset="1" stop-color="#2b9fb4"/></linearGradient>
<linearGradient id="cliffRock" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c9b698"/><stop offset="1" stop-color="#e2d5bd"/></linearGradient>
<linearGradient id="cavernDark" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#36505e"/><stop offset="0.6" stop-color="#263a45"/><stop offset="1" stop-color="#18262e"/></linearGradient>
<linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c6e3f0"/><stop offset="0.6" stop-color="#ecf4ef"/><stop offset="1" stop-color="#fae6c2"/></linearGradient>
<linearGradient id="goldGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e9c877"/><stop offset="1" stop-color="#b07f2a"/></linearGradient>
<pattern id="rockHatch" width="13" height="13" patternUnits="userSpaceOnUse" patternTransform="rotate(35)"><line x1="0" y1="0" x2="0" y2="13" stroke="#9c8868" stroke-width="0.9" stroke-opacity="0.38"/></pattern>
<pattern id="rockHatch2" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(-40)"><line x1="0" y1="0" x2="0" y2="9" stroke="#8a7758" stroke-width="0.8" stroke-opacity="0.35"/></pattern>
<pattern id="waves" width="46" height="22" patternUnits="userSpaceOnUse"><path d="M2 8 q6 -5 12 0 t12 0" fill="none" stroke="#c9f1f6" stroke-width="0.9" stroke-opacity="0.28"/><path d="M25 19 q5 -4 10 0 t10 0" fill="none" stroke="#c9f1f6" stroke-width="0.8" stroke-opacity="0.2"/></pattern>
<pattern id="tileDiamond" width="32" height="32" patternUnits="userSpaceOnUse"><rect width="32" height="32" fill="#fdfbf5"/><path d="M16 0 L32 16 L16 32 L0 16 Z" fill="#f1ebdd" stroke="#d9cdb4" stroke-width="0.7"/><circle cx="0" cy="0" r="2" fill="#c5963e" fill-opacity="0.55"/><circle cx="32" cy="0" r="2" fill="#c5963e" fill-opacity="0.55"/><circle cx="0" cy="32" r="2" fill="#c5963e" fill-opacity="0.55"/><circle cx="32" cy="32" r="2" fill="#c5963e" fill-opacity="0.55"/></pattern>
<pattern id="tileHerr" width="24" height="24" patternUnits="userSpaceOnUse"><rect width="24" height="24" fill="#faf3e4"/><path d="M0 12 L12 0 M12 24 L24 12 M0 12 L12 24 M12 0 L24 12" fill="none" stroke="#dccfb2" stroke-width="0.8"/></pattern>
<pattern id="tileHerrB" width="24" height="24" patternUnits="userSpaceOnUse"><rect width="24" height="24" fill="#eef7f7"/><path d="M0 12 L12 0 M12 24 L24 12 M0 12 L12 24 M12 0 L24 12" fill="none" stroke="#c4dcdd" stroke-width="0.8"/></pattern>
<pattern id="tileSmall" width="10" height="10" patternUnits="userSpaceOnUse"><rect width="10" height="10" fill="#e6f3f2"/><path d="M0 0 H10 V10" fill="none" stroke="#a9d2d4" stroke-width="0.7"/></pattern>
<pattern id="tileSq" width="20" height="20" patternUnits="userSpaceOnUse"><rect width="20" height="20" fill="#f8f2e5"/><path d="M0 0 H20 V20" fill="none" stroke="#dbcfb6" stroke-width="0.7"/></pattern>
<pattern id="tileScale" width="20" height="14" patternUnits="userSpaceOnUse"><rect width="20" height="14" fill="#f3f7f2"/><path d="M0 7 a10 10 0 0 1 20 0 M-10 14 a10 10 0 0 1 20 0 M10 14 a10 10 0 0 1 20 0" fill="none" stroke="#9ecfd2" stroke-width="0.8"/></pattern>
<pattern id="planks" width="12" height="60" patternUnits="userSpaceOnUse"><rect width="12" height="60" fill="#f3ead6"/><path d="M0 0 V60 M0 30 H12" fill="none" stroke="#d2c19e" stroke-width="0.7"/></pattern>
<pattern id="sand" width="18" height="18" patternUnits="userSpaceOnUse"><rect width="18" height="18" fill="#ecdcb6"/><circle cx="3" cy="4" r="0.9" fill="#b99c63"/><circle cx="11" cy="9" r="0.8" fill="#b99c63"/><circle cx="6" cy="14" r="0.8" fill="#c8ad78"/><circle cx="15" cy="2" r="0.7" fill="#c8ad78"/><circle cx="14" cy="15" r="0.9" fill="#b99c63"/></pattern>
<pattern id="grass" width="16" height="16" patternUnits="userSpaceOnUse"><rect width="16" height="16" fill="#cfdcae"/><path d="M3 5 l1 -3 M10 12 l1 -3 M13 4 l1 -2 M5 13 l1 -2" stroke="#8fa868" stroke-width="0.8"/></pattern>
<pattern id="hedge" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#5f8a55"/><circle cx="2" cy="2" r="1.6" fill="#4a7344"/><circle cx="6" cy="6" r="1.6" fill="#76a067"/></pattern>
<pattern id="gravel" width="12" height="12" patternUnits="userSpaceOnUse"><rect width="12" height="12" fill="#f1e8d3"/><circle cx="2" cy="3" r="0.7" fill="#c9b792"/><circle cx="8" cy="7" r="0.7" fill="#c9b792"/><circle cx="5" cy="10" r="0.6" fill="#d6c7a6"/></pattern>
<pattern id="border" width="28" height="12" patternUnits="userSpaceOnUse"><path d="M0 8 q7 -8 14 0 q3 3 0 4 q-4 0 -3 -4 M14 8 q7 -8 14 0" fill="none" stroke="#c5963e" stroke-width="1.1"/></pattern>
<filter id="paper" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="7"/><feColorMatrix values="0 0 0 0 0.5  0 0 0 0 0.38  0 0 0 0 0.2  0 0 0 0.11 0"/></filter>
<filter id="blotch" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.006" numOctaves="3" seed="21"/><feColorMatrix values="0 0 0 0 0.6  0 0 0 0 0.45  0 0 0 0 0.22  0 0 0 0.35 -0.08"/></filter>
<filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="shadow" x="-10%" y="-10%" width="130%" height="130%"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#3a2a10" flood-opacity="0.28"/></filter>
'''
CSS='''
.ti{font-family:'Noto Serif Display','Noto Serif',serif;font-weight:700;fill:#16303b}
.sub{font-family:'Noto Serif',serif;font-style:italic;fill:#55676e}
.ph{font-family:'Noto Serif',serif;font-weight:700;font-size:19px;fill:#144a5c;letter-spacing:1.4px}
.rl{font-family:'Noto Serif',serif;font-weight:700;font-size:15px;fill:#1b2d36;text-anchor:middle;paint-order:stroke;stroke:#fdfaf3;stroke-width:3.5px;stroke-linejoin:round}

.rs{font-family:'Noto Sans',sans-serif;font-size:12.5px;fill:#2b3d45;text-anchor:middle;paint-order:stroke;stroke:#fdfaf3;stroke-width:3px;stroke-linejoin:round}
.rll{font-family:'Noto Serif',serif;font-weight:700;font-size:15px;fill:#ffffff;text-anchor:middle;paint-order:stroke;stroke:#14232b;stroke-width:3.5px;stroke-linejoin:round}

.rsl{font-family:'Noto Sans',sans-serif;font-size:12.5px;fill:#e2f5f8;text-anchor:middle;paint-order:stroke;stroke:#14232b;stroke-width:3px;stroke-linejoin:round}
.nt{font-family:'Noto Sans',sans-serif;font-size:13.5px;fill:#26383f}
.nb{font-family:'Noto Serif',serif;font-weight:700;fill:#144a5c}
.kn{font-family:'Noto Sans',sans-serif;font-weight:700;font-size:11px;fill:#ffffff;text-anchor:middle}
.sea{font-family:'Noto Serif',serif;font-style:italic;fill:#e3f8fb;text-anchor:middle}
.dim{font-family:'Noto Sans',sans-serif;font-style:italic;font-size:12.5px;fill:#144a5c;text-anchor:middle;paint-order:stroke;stroke:#fdfaf3;stroke-width:3px;stroke-linejoin:round}
.el{font-family:'Noto Sans',sans-serif;font-weight:700;font-size:12px;fill:#1b2d36}
'''
class P:
    def __init__(s,W=2400,H=1600):
        s.W=W;s.H=H;s.o=[];s.d=[DEFS];s.css=[CSS]
    def a(s,*x):
        s.o.extend(x)
    def save(s,path):
        out=f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {s.W} {s.H}" width="{s.W}" height="{s.H}">\n<defs>{"".join(s.d)}<style>{"".join(s.css)}</style></defs>\n'+'\n'.join(s.o)+'\n</svg>\n'
        open(path,'w').write(out)
def T(x,y,s,cls='rl',size=None,anchor=None,extra=''):
    st=''
    if size: st+=f' font-size="{size}"'
    if anchor: st+=f' text-anchor="{anchor}"'
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}"{st} {extra}>{esc(s)}</text>'
def ML(x,y,lines,cls='rl',lh=17,size=None,extra=''):
    return ''.join(T(x,y+i*lh,l,cls,size,None,extra) for i,l in enumerate(lines))
def rect(x,y,w,h,fill='none',stroke='none',sw=1,rx=0,extra=''):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
def line(x1,y1,x2,y2,stroke=INK,sw=1,extra=''):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
def circ(cx,cy,r,fill='none',stroke='none',sw=1,extra=''):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
def path(d,fill='none',stroke='none',sw=1,extra=''):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
def G(content,tr='',cls='',extra=''):
    c=f' class="{cls}"' if cls else ''
    t=f' transform="{tr}"' if tr else ''
    return f'<g{c}{t} {extra}>{content}</g>'
def smooth(pts,closed=False,t=0.5):
    n=len(pts)
    if n<3: return 'M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)
    def p(i):
        if closed: return pts[i%n]
        return pts[max(0,min(n-1,i))]
    d=f'M{pts[0][0]:.1f},{pts[0][1]:.1f}'
    rng=n if closed else n-1
    for i in range(rng):
        p0,p1,p2,p3=p(i-1),p(i),p(i+1),p(i+2)
        c1=(p1[0]+(p2[0]-p0[0])*t/3*2/1, p1[1]+(p2[1]-p0[1])*t/3*2/1)
        c1=(p1[0]+(p2[0]-p0[0])/6, p1[1]+(p2[1]-p0[1])/6)
        c2=(p2[0]-(p3[0]-p1[0])/6, p2[1]-(p3[1]-p1[1])/6)
        d+=f' C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}'
    return d+(' Z' if closed else '')
def scale_pts(pts,c,k,dx=0,dy=0):
    return [(c[0]+(x-c[0])*k+dx,c[1]+(y-c[1])*k+dy) for x,y in pts]

def background(p):
    W,H=p.W,p.H
    p.a(rect(0,0,W,H,'url(#parchment)'), rect(0,0,W,H,'#000',extra='filter="url(#blotch)"'), rect(0,0,W,H,'#000',extra='filter="url(#paper)"'), rect(0,0,W,H,'url(#vign)'))
def frame(p, plate, title, subtitle, right1, right2):
    W,H=p.W,p.H
    p.a(rect(22,22,W-44,H-44,'none',TEAL,3), rect(30,30,W-60,H-60,'none',GOLD,1), rect(30,30,W-60,12,'url(#border)'), rect(30,H-42,W-60,12,'url(#border)'), rect(44,44,W-88,H-88,'none',GOLD,1.2), rect(48,48,W-96,H-96,'none',TEAL,0.8))
    for cx,cy in [(36,36),(W-36,36),(36,H-36),(W-36,H-36)]:
        p.a(rect(cx-13,cy-13,26,26,PARCH,TEAL,1.5), star(cx,cy,10,4,3.2,GOLD,TEAL))
    # plate roundel
    p.a(circ(122,104,40,'#fbf6ec',TEAL,2.2), circ(122,104,34,'none',GOLD,1.2), T(122,96,'PLATE','nb',11,'middle','letter-spacing="2"'), T(122,124,plate,'ti',27,'middle'))
    p.a(T(182,100,title,'ti',38,None,'letter-spacing="1.5"'), T(184,132,subtitle,'sub',16.5))
    p.a(T(W-72,84,right1,'nb',14,'end','letter-spacing="2.5"'), T(W-72,108,right2,'sub',14,'end'), T(W-72,131,'Drawn for the Autumn delegation · Vanserra household copy','sub',13,'end','style="fill:#3d4f56"'))
    p.a(line(70,152,W-70,152,GOLD,1.4), line(70,156,W-70,156,TEAL,0.6))
def star(cx,cy,R,n,r,f1,f2):
    pts=[]
    for i in range(n*2):
        a=math.pi*i/n-math.pi/2; rr=R if i%2==0 else r
        pts.append(f'{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" fill="{f1}" stroke="{f2}" stroke-width="0.8"/>'
def compass(cx,cy,R,rot=0,labels=('N','E','S','W'),light=False):
    o=[]
    o.append(circ(0,0,R+10,'#fbf6ec',TEAL,1.6,'fill-opacity="0.95"')); o.append(circ(0,0,R+5,'none',GOLD,1)); o.append(circ(0,0,R*0.62,'none',GOLD,0.8)); o.append(circ(0,0,R*0.3,'none',TEAL,0.8))
    for i in range(72):
        a=math.radians(i*5); r1=R+5; r2=R+(10 if i%2 else 10); r0=R+ (1 if i%9==0 else 5 if i%2 else 3)
        o.append(line(r0*math.sin(a),-r0*math.cos(a),(R+10)*math.sin(a),-(R+10)*math.cos(a),TEAL,0.7))
    def pt(ang,L,w,c1,c2):
        a=math.radians(ang); ux,uy=math.sin(a),-math.cos(a); px,py=-uy,ux
        tip=(L*ux,L*uy); b1=(w*px+w*0.9*ux,w*py+w*0.9*uy); b2=(-w*px+w*0.9*ux,-w*py+w*0.9*uy)
        return f'<polygon points="0,0 {b1[0]:.1f},{b1[1]:.1f} {tip[0]:.1f},{tip[1]:.1f}" fill="{c1}" stroke="{INK}" stroke-width="0.6"/><polygon points="0,0 {b2[0]:.1f},{b2[1]:.1f} {tip[0]:.1f},{tip[1]:.1f}" fill="{c2}" stroke="{INK}" stroke-width="0.6"/>'
    for ang in range(0,360,45):
        if ang%90: continue
    for ang in [22.5+45*i for i in range(8)]: o.append(pt(ang,R*0.5,R*0.07,'#d9c79e','#fbf6ec'))
    for ang in [45,135,225,315]: o.append(pt(ang,R*0.72,R*0.1,GOLD,'#f3e2b4'))
    for ang in [0,90,180,270]: o.append(pt(ang,R,R*0.13,TEAL,'#f7f1e2'))
    o.append(circ(0,0,R*0.09,GOLD,INK,0.8))
    g=G(''.join(o),f'translate({cx},{cy}) rotate({rot})')
    lab=[]
    for (ang,l) in zip([0,90,180,270],labels):
        a=math.radians(ang+rot); rr=R+24
        x=cx+rr*math.sin(a); y=cy-rr*math.cos(a)+5
        lab.append(T(x,y,l,'nb',15 if ang==0 else 12.5,'middle', 'style="paint-order:stroke;stroke:#fbf6ec;stroke-width:3px"' if not light else 'style="fill:#fff;paint-order:stroke;stroke:#0e566d;stroke-width:3px"'))
    return g+''.join(lab)
def scalebar(x,y,pxm,units=(0,5,10,20),light=False,label='metres'):
    c='#e9fbfd' if light else INK; o=[]
    L=units[-1]*pxm
    o.append(rect(x,y-4,L,8,'#fbf6ec' if not light else '#0e566d',c,1.2))
    for i in range(len(units)-1):
        if i%2==0: o.append(rect(x+units[i]*pxm,y-4,(units[i+1]-units[i])*pxm,8,c))
    for u in units:
        o.append(line(x+u*pxm,y-9,x+u*pxm,y+4,c,1.2))
        o.append(f'<text x="{x+u*pxm:.1f}" y="{y+21}" text-anchor="middle" font-family="Noto Sans" font-size="11.5" fill="{c}">{u}</text>')
    o.append(f'<text x="{x+L+14:.1f}" y="{y+21}" font-family="Noto Serif" font-style="italic" font-size="12" fill="{c}">{label}</text>')
    return ''.join(o)
def key(x,y,n,col=TEAL):
    return G(circ(x,y,9.5,col,'#f3dfa8',1.3)+f'<text x="{x:.1f}" y="{y+4:.1f}" class="kn">{n}</text>',cls='kr')
def panel_head(x,y,num,title,w):
    return T(x,y,f'{num}.  {title}','ph')+line(x,y+7,x+w,y+7,GOLD,1)
def para(x,y,lead,body,maxw,size=13.5,lh=18.5,bullet='◆'):
    """returns svg, height"""
    out=[]; words=body.split(' '); lines=[]; cur=''
    leadw=tw(bullet+' '+lead+' ','serifb',size)+2 if lead else tw(bullet+' ','sans',size)
    avail=maxw-leadw; first=True
    for w in words:
        t=(cur+' '+w).strip()
        if tw(t,'sans',size)<=avail: cur=t
        else:
            lines.append(cur); cur=w; first=False; avail=maxw-16
    lines.append(cur)
    for i,l in enumerate(lines):
        if i==0:
            out.append(f'<text x="{x}" y="{y}" class="nt" font-size="{size}"><tspan fill="{GOLD}">{bullet} </tspan><tspan class="nb">{esc(lead)} </tspan>{esc(l)}</text>')
        else:
            out.append(f'<text x="{x+16}" y="{y+i*lh}" class="nt" font-size="{size}">{esc(l)}</text>')
    return ''.join(out), len(lines)*lh
def dimline(x1,y1,x2,y2,label,off=-6,col=TEAL):
    o=[line(x1,y1,x2,y2,col,0.9)]
    if abs(y1-y2)<1:
        o+= [line(x1,y1-5,x1,y1+5,col,1), line(x2,y2-5,x2,y2+5,col,1), line(x1-3,y1+3,x1+3,y1-3,col,1), line(x2-3,y2+3,x2+3,y2-3,col,1)]
        o.append(T((x1+x2)/2,y1+off,label,'dim'))
    else:
        o+= [line(x1-5,y1,x1+5,y1,col,1), line(x2-5,y2,x2+5,y2,col,1), line(x1-3,y1+3,x1+3,y1-3,col,1), line(x2-3,y2+3,x2+3,y2-3,col,1)]
        mx,my=(x1+x2)/2+off,(y1+y2)/2
        o.append(T(mx,my,label,'dim',extra=f'transform="rotate(-90 {mx:.1f} {my:.1f})"'))
    return ''.join(o)
# ---------- walls ----------
def wall_h(y,x1,x2,gaps=(),sw=5,col=WALL):
    o=[];cur=x1
    for a,b in sorted(gaps):
        if a>cur: o.append(line(cur,y,a,y,col,sw,'class="w" stroke-linecap="square"'))
        cur=b
    if cur<x2: o.append(line(cur,y,x2,y,col,sw,'class="w" stroke-linecap="square"'))
    return ''.join(o)
def wall_v(x,y1,y2,gaps=(),sw=5,col=WALL):
    o=[];cur=y1
    for a,b in sorted(gaps):
        if a>cur: o.append(line(x,cur,x,a,col,sw,'class="w" stroke-linecap="square"'))
        cur=b
    if cur<y2: o.append(line(x,cur,x,y2,col,sw,'class="w" stroke-linecap="square"'))
    return ''.join(o)
def door_h(x1,x2,y,side=1,hinge='l',col=DGOLD):
    """door in horizontal wall between x1..x2; leaf swings to side (+1 down, -1 up)"""
    w=x2-x1; hx=x1 if hinge=='l' else x2; ex=x2 if hinge=='l' else x1
    sweep=1 if (hinge=='l')==(side<0) else 0
    sweep=1-sweep
    return line(hx,y,hx,y+side*w,col,1.6)+path(f'M{hx},{y+side*w} A{w},{w} 0 0 {sweep} {ex},{y}','none',col,0.8,'stroke-dasharray="3 2"')
def door_v(y1,y2,x,side=1,hinge='t',col=DGOLD):
    w=y2-y1; hy=y1 if hinge=='t' else y2; ey=y2 if hinge=='t' else y1
    sweep=1 if (hinge=='t')==(side>0) else 0
    return line(x,hy,x+side*w,hy,col,1.6)+path(f'M{x+side*w},{hy} A{w},{w} 0 0 {sweep} {x},{ey}','none',col,0.8,'stroke-dasharray="3 2"')
# ---------- furniture ----------
def Fg(c,tr=''): return G(c,tr,'f')
def column(cx,cy,r=7,gold=True):
    o=rect(cx-r-2,cy-r-2,2*r+4,2*r+4,'#efe6d2',WALL,0.8)+circ(cx,cy,r,'url(#goldGrad)' if gold else '#fff',WALL,1.1)+circ(cx,cy,r*0.45,'none','#fff8e0',0.8)
    return Fg(o)
def bed(x,y,w,h,rot=0,canopy=True,col='#f6ecd9',cover='#b5482f'):
    o=rect(0,0,w,h,col,WALL,1.2,3)
    o+=rect(0,-4,w,5,'#8a6a3a',WALL,0.8,2)
    o+=rect(w*0.08,3,w*0.38,h*0.2,'#fff',WALL,0.7,4)+rect(w*0.54,3,w*0.38,h*0.2,'#fff',WALL,0.7,4)
    o+=rect(1.5,h*0.42,w-3,h*0.58-1.5,cover,'none',0,2,'fill-opacity="0.55"')+line(1,h*0.42,w-1,h*0.42,WALL,0.8)
    o+=path(f'M{w*0.15},{h*0.55} q{w*0.35},{h*0.12} {w*0.7},0','none','#fff',0.8,'stroke-opacity="0.7"')
    if canopy:
        for px,py in [(0,0),(w,0),(0,h),(w,h)]: o+=circ(px,py,2.6,GOLD,WALL,0.7)
        o+=rect(-2,-2,w+4,h+4,'none',GOLD,0.8,0,'stroke-dasharray="5 3"')
    return Fg(o,f'translate({x},{y}) rotate({rot})')
def divan(x,y,w,h,rot=0,col='#e8dcc0',cush='#2a8fa3'):
    o=rect(0,0,w,h,col,WALL,1.1,5)+rect(0,0,w,h*0.3,'#d6c5a0',WALL,0.8,4)
    n=max(2,int(w//18))
    for i in range(n):
        o+=rect(3+i*(w-6)/n,h*0.36,(w-6)/n-2,h*0.52,cush,'none',0,3,'fill-opacity="0.55"')
    return Fg(o,f'translate({x},{y}) rotate({rot} {w/2} {h/2})')
def chair(cx,cy,s=9,rot=0,col='#e3d3ad'):
    o=rect(-s/2,-s/2,s,s,col,WALL,0.8,2)+rect(-s/2,-s/2-2,s,3,'#8a6a3a',WALL,0.5,1)
    return G(o,f'translate({cx},{cy}) rotate({rot})')
def table_long(x,y,w,h,n,vertical=True,col='#f7f3ea',edge=GOLD):
    o=rect(x,y,w,h,col,WALL,1.2,6)+rect(x+3,y+3,w-6,h-6,'none',edge,0.9,4)
    if vertical:
        for i in range(n):
            cy=y+h*(i+0.5)/n
            o+=chair(x-9,cy,9,-90)+chair(x+w+9,cy,9,90)
            o+=circ(x+w*0.28,cy,2.2,'#fff',WALL,0.5)+circ(x+w*0.72,cy,2.2,'#fff',WALL,0.5)
        o+=chair(x+w/2,y-9,9,0)+chair(x+w/2,y+h+9,9,180)
    else:
        for i in range(n):
            cx=x+w*(i+0.5)/n
            o+=chair(cx,y-9,9,0)+chair(cx,y+h+9,9,180)
            o+=circ(cx,y+h*0.28,2.2,'#fff',WALL,0.5)+circ(cx,y+h*0.72,2.2,'#fff',WALL,0.5)
        o+=chair(x-9,y+h/2,9,-90)+chair(x+w+9,y+h/2,9,90)
    return Fg(o)
def table_round(cx,cy,r,n,col='#f7f3ea'):
    o=circ(cx,cy,r,col,WALL,1.2)+circ(cx,cy,r-3,'none',GOLD,0.8)
    for i in range(n):
        a=2*math.pi*i/n
        o+=chair(cx+(r+8)*math.sin(a),cy-(r+8)*math.cos(a),8,math.degrees(a))
    return Fg(o)
def brazier(cx,cy,r=13):
    o=circ(cx,cy,r,'#3a3f42',WALL,1.2)+circ(cx,cy,r-3,'#7a2b12','#e2a13a',1)
    o+=star(cx,cy,r-4,6,(r-4)*0.45,'#f6b040','#b5482f')
    return Fg(o)
def spiral(cx,cy,r,n=14,label=None,col='#e8dcc4'):
    o=circ(cx,cy,r,col,DGOLD,2)
    for i in range(n):
        a=2*math.pi*i/n
        o+=line(cx+r*0.18*math.cos(a),cy+r*0.18*math.sin(a),cx+r*math.cos(a),cy+r*math.sin(a),DGOLD,1)
    o+=circ(cx,cy,r*0.18,DGOLD,WALL,0.8)
    # direction arrow
    ra=r*0.62
    o+=path(f'M{cx+ra*math.cos(-2.4):.1f},{cy+ra*math.sin(-2.4):.1f} A{ra},{ra} 0 1 1 {cx+ra*math.cos(1.9):.1f},{cy+ra*math.sin(1.9):.1f}','none',INK,1.1)
    ex,ey=cx+ra*math.cos(1.9),cy+ra*math.sin(1.9)
    o+=f'<polygon points="{ex-6:.1f},{ey-1:.1f} {ex+2:.1f},{ey-5:.1f} {ex+1:.1f},{ey+4:.1f}" fill="{INK}"/>'
    return Fg(o)
def stairs(x,y,w,h,n,direction='e',col='#f1e8d4',arrow=True):
    o=rect(x,y,w,h,col,WALL,1.1)
    if direction in 'ew':
        for i in range(1,n): o+=line(x+w*i/n,y,x+w*i/n,y+h,WALL,0.7)
        if arrow:
            x1,x2=(x+6,x+w-6) if direction=='e' else (x+w-6,x+6)
            s=1 if direction=='e' else -1
            o+=line(x1,y+h/2,x2,y+h/2,INK,1)+f'<polygon points="{x2},{y+h/2} {x2-7*s},{y+h/2-4} {x2-7*s},{y+h/2+4}" fill="{INK}"/>'
    else:
        for i in range(1,n): o+=line(x,y+h*i/n,x+w,y+h*i/n,WALL,0.7)
        if arrow:
            y1,y2=(y+6,y+h-6) if direction=='s' else (y+h-6,y+6)
            s=1 if direction=='s' else -1
            o+=line(x+w/2,y1,x+w/2,y2,INK,1)+f'<polygon points="{x+w/2},{y2} {x+w/2-4},{y2-7*s} {x+w/2+4},{y2-7*s}" fill="{INK}"/>'
    return Fg(o)
def tree(cx,cy,r,col='#5f8a55',dark='#3f6a40',fruit=None):
    o=circ(cx+1.5,cy+2,r,'#3a2a10','none',0,'fill-opacity="0.18"')+circ(cx,cy,r,col,dark,0.9)
    for i in range(5):
        a=i*2.2+cx*0.1; o+=circ(cx+r*0.45*math.cos(a),cy+r*0.45*math.sin(a),r*0.38,dark,'none',0,'fill-opacity="0.35"')
    if fruit:
        for i in range(4):
            a=i*1.7+cy*0.1; o+=circ(cx+r*0.5*math.cos(a),cy+r*0.5*math.sin(a),max(1.1,r*0.14),fruit)
    return o
def cypress(cx,cy,r=5):
    return circ(cx+1,cy+1.5,r,'#3a2a10','none',0,'fill-opacity="0.2"')+circ(cx,cy,r,'#2f5a3c','#1e3f2a',0.8)+circ(cx-r*0.25,cy-r*0.25,r*0.4,'#4f8058')
def fountain(cx,cy,r,tiers=2):
    o=circ(cx,cy,r,'#f4eee0',WALL,1.2)+circ(cx,cy,r-3,'url(#poolGrad)',TEAL,0.8)
    o+=circ(cx,cy,r*0.45,'#f4eee0',WALL,0.9)+circ(cx,cy,r*0.3,'url(#poolGrad)',TEAL,0.6)+circ(cx,cy,r*0.1,GOLD,WALL,0.6)
    for i in range(8):
        a=math.pi*i/4; o+=line(cx+r*0.5*math.cos(a),cy+r*0.5*math.sin(a),cx+(r-4)*math.cos(a),cy+(r-4)*math.sin(a),'#e3f8fb',0.7)
    return Fg(o)
def shell(cx,cy,r,rot=0,fill='#f7efe0',stroke=GOLD):
    o=path(f'M0,{r*0.9} C{-r*1.3},{r*0.3} {-r*1.1},{-r} 0,{-r} C{r*1.1},{-r} {r*1.3},{r*0.3} 0,{r*0.9} Z',fill,stroke,1)
    for i in range(-3,4):
        o+=line(0,r*0.85,i*r*0.28,-r*0.8+abs(i)*r*0.12,stroke,0.7)
    return G(o,f'translate({cx},{cy}) rotate({rot})')
def ship(cx,cy,L,rot=0,sail='#fbf3df'):
    o=path(f'M{-L/2},0 Q{-L*0.2},{-L*0.2} {L/2},0 Q{-L*0.2},{L*0.2} {-L/2},0 Z','#8a6a3a','#3a2a10',0.8)
    o+=rect(-L*0.12,-L*0.2,L*0.08,L*0.4,sail,'#3a2a10',0.5)+rect(L*0.12,-L*0.15,L*0.06,L*0.3,sail,'#3a2a10',0.5)
    return G(o,f'translate({cx:.1f},{cy:.1f}) rotate({rot})')
def legend_swatch(kind,x,y):
    return ''
def dragon_coil(cx,cy,R,rot=0):
    pts=[]
    for i in range(0,61):
        t=i/60; a=t*2*math.pi*1.3; r=R*(1.0-0.55*t)
        pts.append((r*math.cos(a),r*math.sin(a)))
    body=smooth(pts[:36]); tail=smooth(pts[34:])
    o=f'<ellipse cx="3" cy="5" rx="{R*1.25:.1f}" ry="{R*1.2:.1f}" fill="#3a2a10" fill-opacity="0.22"/>'
    # wing folded over the flank
    o+=path(f'M{-R*0.3:.1f},{R*0.9:.1f} L{-R*1.5:.1f},{R*0.75:.1f} L{-R*1.2:.1f},{R*0.35:.1f} L{-R*1.55:.1f},{-R*0.05:.1f} L{-R*1.1:.1f},{-R*0.3:.1f} L{-R*0.9:.1f},{R*0.2:.1f} Z','#dfe6e4','#14232b',1.2,'stroke-linejoin="round"')
    for ex,ey in [(-1.5,0.75),(-1.2,0.35),(-1.55,-0.05)]: o+=line(-R*0.6,R*0.5,R*ex,R*ey,'#14232b',0.8)
    o+=path(tail,'none','#14232b',R*0.2+2.4,'stroke-linecap="round"')+path(tail,'none','#fbfbf6',R*0.2,'stroke-linecap="round"')
    o+=path(body,'none','#14232b',R*0.36+2.6,'stroke-linecap="round"')+path(body,'none','#fbfbf6',R*0.36,'stroke-linecap="round"')
    # dorsal spines
    for i in range(3,58,3):
        x,y=pts[i]; n=math.hypot(x,y); k=(0.19 if i<36 else 0.11)
        o+=line(x,y,x+x/n*R*k,y+y/n*R*k,'#c5963e',1.8)
    # head: wedge snout pointing tangentially, two gold horns
    hx,hy=pts[0]
    o+=path(f'M{hx-R*0.2:.1f},{hy+R*0.12:.1f} L{hx-R*0.13:.1f},{hy-R*0.52:.1f} Q{hx:.1f},{hy-R*0.7:.1f} {hx+R*0.13:.1f},{hy-R*0.52:.1f} L{hx+R*0.2:.1f},{hy+R*0.12:.1f} Z','#fbfbf6','#14232b',1.3,'stroke-linejoin="round"')
    o+=path(f'M{hx-R*0.14:.1f},{hy+R*0.05:.1f} l{-R*0.3:.1f},{R*0.42:.1f} M{hx+R*0.14:.1f},{hy+R*0.05:.1f} l{R*0.3:.1f},{R*0.42:.1f}','none','#b8860b',3.2,'stroke-linecap="round"')
    o+=circ(hx-R*0.07,hy-R*0.25,1.3,'#14232b')+circ(hx+R*0.07,hy-R*0.25,1.3,'#14232b')
    return G(o,f'translate({cx},{cy}) rotate({rot})')
def dragon_fly(cx,cy,s=1,rot=0,flip=False):
    o=path('M-12,1 C-18,-18 -14,-34 -2,-46 C-2,-34 2,-28 8,-22 C0,-18 -4,-10 -4,1 Z','#d9dedb','#14232b',0.8)
    o+=path('M-46,2 C-40,-4 -32,-5 -26,-1 C-18,3 -8,2 2,1 C16,0 30,4 50,14 C34,12 18,10 4,9 C-8,9 -18,10 -26,6 C-32,9 -40,8 -46,2 Z','#fbfbf6','#14232b',1.4)
    o+=path('M-8,2 C-6,-22 6,-40 30,-50 C24,-38 26,-30 34,-26 C24,-24 20,-18 24,-10 C14,-12 6,-6 4,2 Z','#fbfbf6','#14232b',1.4)
    o+=line(-40,-3,-33,-10,'#e2b24a',1.6)
    sx=-s if flip else s
    return G(o,f'translate({cx},{cy}) rotate({rot}) scale({sx},{s})')
