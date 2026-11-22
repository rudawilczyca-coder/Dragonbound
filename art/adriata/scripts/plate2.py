from lib import *
import random
rnd=random.Random(11)
p=P(); background(p)
frame(p,'II',"ADRIATA HEADLAND & THE SUMMER PALACE GROUNDS","Master site-plan of the island-city in its half-moon bay · palace summit, harbour, gardens, cove and the western cliff villa",'ADRIATA & THE SUMMER COURT PALACE','Dragonbound Cartographic Suite · Plate II of IV')
MX0,MY0,MX1,MY1=70,200,1700,1530
p.d.append(f'<clipPath id="m"><rect x="{MX0}" y="{MY0}" width="{MX1-MX0}" height="{MY1-MY0}" rx="5"/></clipPath>')
p.d.append('<radialGradient id="bayG" cx="0.42" cy="0.5" r="0.75"><stop offset="0" stop-color="#58bccb"/><stop offset="0.45" stop-color="#2893a9"/><stop offset="1" stop-color="#0d4f65"/></radialGradient><linearGradient id="landG" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e3d6b8"/><stop offset="1" stop-color="#d3c29c"/></linearGradient>')
p.a(panel_head(72,186,'I','THE ISLAND-CITY OF ADRIATA — SITE PLAN',1626))
def pip(x,y,poly):
    c=False;n=len(poly)
    for i in range(n):
        x1,y1=poly[i];x2,y2=poly[(i+1)%n]
        if (y1>y)!=(y2>y) and x<(x2-x1)*(y-y1)/(y2-y1)+x1: c=not c
    return c
def dseg(px,py,a,b):
    ax,ay=a;bx,by=b;dx,dy=bx-ax,by-ay;L=dx*dx+dy*dy
    t=max(0,min(1,((px-ax)*dx+(py-ay)*dy)/L)) if L else 0
    return math.hypot(px-ax-t*dx,py-ay-t*dy)
def dpoly(px,py,pl): return min(dseg(px,py,pl[i],pl[i+1]) for i in range(len(pl)-1))
ISL=[(372,585),(430,500),(520,452),(640,446),(760,418),(900,438),(1010,430),(1130,490),(1190,560),(1262,610),(1280,720),(1262,800),(1290,900),(1248,985),(1200,1090),(1100,1150),(1050,1215),(930,1232),(860,1262),(720,1240),(640,1236),(596,1224),(568,1182),(550,1128),(514,1094),(474,1090),(446,1118),(440,1168),(424,1204),(400,1172),(386,1100),(376,1030),(366,960),(356,880),(352,760),(356,660)]
NORTH=[(70,200),(1700,200),(1700,560),(1640,470),(1560,395),(1420,340),(1200,318),(950,322),(700,312),(480,300),(300,262),(150,232),(70,226)]
EAST=[(1700,520),(1622,560),(1560,680),(1548,820),(1556,960),(1600,1090),(1700,1150)]
SOUTH=[(70,1530),(1700,1530),(1700,1120),(1640,1230),(1540,1330),(1380,1396),(1150,1430),(900,1436),(650,1444),(430,1462),(250,1492),(70,1506)]
MAIN=[(70,200),(1700,200),(1700,1530),(70,1530),(70,1506),(250,1492),(430,1462),(650,1444),(900,1436),(1150,1430),(1380,1396),(1500,1330),(1560,1230),(1590,1090),(1556,960),(1548,820),(1560,680),(1590,560),(1560,440),(1470,365),(1300,326),(1200,318),(950,322),(700,312),(480,300),(300,262),(150,232),(70,226)]
o=[rect(MX0,MY0,MX1-MX0,MY1-MY0,'url(#bayG)'),rect(MX0,MY0,MX1-MX0,MY1-MY0,'url(#waves)')]
# bathymetry rings
C0=(800,840)
for k,op,da in [(1.07,0.7,''),(1.15,0.5,'10 5'),(1.25,0.4,''),(1.38,0.3,'10 5')]:
    o.append(path(smooth(scale_pts(ISL,C0,k),True),'none','#c9f1f6',1.1,f'stroke-opacity="{op}" stroke-dasharray="{da}"'))
for i in range(5):
    pts=[(300-i*52+16*math.sin(y/90+i),y) for y in range(180,1560,60)]
    o.append(path(smooth(pts),'none','#c9f1f6',1,f'stroke-opacity="{0.35-i*0.04}" stroke-dasharray="{"" if i%2 else "10 5"}"'))
# flight corridor
VX,VY=352,668
o.append(path(f'M316,{VY-12} L70,{VY-12-205} L70,{VY+12-20} L316,{VY+12} Z','#f6d88a','none',0,'fill-opacity="0.2"'))
o.append(line(316,VY-12,70,VY-12-205,'#f6d88a',1.5,'stroke-dasharray="10 6"')+line(316,VY+12,70,VY+12-20,'#f6d88a',1.5,'stroke-dasharray="10 6"'))
o.append(line(306,VY-8,100,VY-100,'#f6d88a',2.8,'stroke-dasharray="14 7"')+f'<polygon points="80,{VY-107} 108,{VY-109} 100,{VY-86}" fill="#f6d88a"/>')
o.append(dragon_fly(178,594,0.62,22))
# mainland
md=smooth(MAIN[4:],False)
mpath=smooth(MAIN[4:])+' L70,200 L1700,200 L1700,1530 L70,1530 Z'
# build mainland as: full rect minus bay -> draw coast polygon explicitly
coast=MAIN[4:]
mp='M70,200 L1700,200 L1700,1530 L70,1530 '+smooth(coast).replace('M','L',1)+' Z'
o.append(path(mp,'none','#f4fdfe',7,'stroke-opacity="0.45"'))
o.append(path(mp,'url(#landG)','#6b5a44',1.4)); o.append(path(mp,'url(#rockHatch)','none',0,'fill-opacity="0.5"'))
# tidal flats north channel
o.append(path(smooth([(520,330),(700,352),(900,356),(1100,350),(1220,342),(1100,372),(900,384),(700,380),(540,356)],True),'url(#sand)','none',0,'fill-opacity="0.55"'))
# reef "The Teeth"
for (x,y,r) in [(250,520),(275,548,6),(232,560,5),(292,500,4),(262,585,7),(300,566,4),(240,610,5),(285,618,4)]+[] if False else [(250,480,7),(275,508,6),(232,520,5),(292,468,4),(262,545,7),(300,526,4),(240,566,5),(285,578,4)]:
    o.append(circ(x,y,r+3.5,'none','#f4fdfe',1.1,'stroke-opacity="0.75"')+circ(x,y,r,'#8f7d62','#4a3d2c',0.9))
# island
idp=smooth(ISL,True)
o.append(path(idp,'none','#f4fdfe',9,'stroke-opacity="0.5"'))
o.append(path(idp,'url(#landG)','#5c4e3d',1.8))
PC=(650,815)
p.d.append(f'<clipPath id="isl"><path d="{idp}"/></clipPath>')
ct=[]
for k,colr in [(0.9,'#dccba6'),(0.82,'#e0d0ad'),(0.74,'#e4d6b5'),(0.66,'#e8dbbd'),(0.6,'#ecdfc4')]:
    ct.append(path(smooth(scale_pts(ISL,PC,k),True),colr,'#8a7350',0.9,'stroke-opacity="0.75"'))
o.append(G(''.join(ct),extra='clip-path="url(#isl)"'))
PLAT=[(440,640),(600,612),(800,625),(960,700),(992,820),(960,940),(800,985),(650,992),(420,984),(376,900),(372,740)]
o.append(G(path(smooth(PLAT,True),'#f1e8d2','#8a7350',1.4),extra='clip-path="url(#isl)"'))
GARD=[(388,972),(650,985),(668,1070),(648,1204),(604,1208),(580,1172),(562,1122),(520,1080),(468,1076),(432,1108),(428,1164),(420,1188),(408,1164),(398,1096),(386,1030)]
# west cliff hachures
for i in range(34):
    t=i/33; y=600+t*400; x=354+6*math.sin(t*9)+ (20*(t-0.9) if t>0.9 else 0)
    if 636<y<736: continue
    o.append(line(x+3,y,x+24,y+2,'#6b5a44',1,'stroke-opacity="0.8"'))
# cove beach

# roads
ROADS=[[(905,322),(900,440),(880,520),(940,580),(1040,660),(1050,760),(1010,816),(950,816)],
       [(1548,830),(1272,810),(1180,812),(1090,800),(1050,760)],
       [(900,1436),(880,1250),(900,1140),(1000,1060),(1050,940),(1040,860),(1010,816)],
       [(1262,640),(1180,640),(1100,600),(1000,570),(940,580)],
       [(1200,1090),(1100,1080),(1000,1060)],
       [(880,520),(720,500),(560,520),(450,600)],
       [(900,1140),(780,1100),(700,1060),(680,1000)]]
MROADS=[[(905,200),(905,322)],[(905,290),(600,270),(300,235),(70,215)],[(905,290),(1250,300),(1480,350),(1600,470),(1700,500)],[(1548,830),(1700,830)],[(1620,470),(1640,830),(1620,1180),(1500,1340),(1200,1445),(900,1470),(500,1490),(70,1520)],[(900,1436),(900,1530)]]
# buildings
KEEP=[]  # (x,y,w,h) label keep-outs
def ok_lab(x,y):
    return all(not (kx-6<x<kx+kw+6 and ky-6<y<ky+kh+6) for kx,ky,kw,kh in KEEP)
KEEP+=[(640,598,180,36),(1072,880,180,58),(640,470,220,48),(1578,636,108,44),(1210,226,250,48),(1120,1444,240,48),(1052,1090,110,26),(930,206,190,24),(960,620,60,60)]
ROOF=['#c0563a','#b84d33','#cc6a48','#d9c7a0','#f4efe2','#c9603f','#e8dcc0','#b5482f']
gardens=[(395,890),(540,880),(560,1130),(450,1120),(380,990)]
bl=[]
ISL_IN=scale_pts(ISL,C0,0.955); PLAT_OUT=scale_pts(PLAT,PC,1.07)
placed=[]
tries=0
while len(placed)<900 and tries<60000:
    tries+=1
    x=rnd.uniform(350,1280); y=rnd.uniform(430,1255)
    if not pip(x,y,ISL_IN) or pip(x,y,PLAT_OUT) or pip(x,y,scale_pts(GARD,(540,1090),1.22)) : continue
    if x<470 and y<900: continue
    if (x<480 and y>1090) or (x<630 and y>1150): continue
    if not ok_lab(x,y): continue
    if any(dpoly(x,y,r)<9 for r in ROADS): continue
    if any(math.hypot(x-a,y-b)<13 for a,b in placed): continue
    placed.append((x,y))
    ang=math.degrees(math.atan2(y-PC[1],x-PC[0]))+90+rnd.uniform(-8,8)
    w=rnd.uniform(9,17);h=rnd.uniform(6,10)
    bl.append(f'<rect x="{-w/2:.1f}" y="{-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{rnd.choice(ROOF)}" stroke="#5a4028" stroke-width="0.5" transform="translate({x:.1f},{y:.1f}) rotate({ang:.0f})"/>')
# mainland buildings
MB=[]
tries=0
while len(MB)<650 and tries<60000:
    tries+=1
    x=rnd.uniform(75,1695); y=rnd.uniform(205,1525)
    if not pip(x,y,MAIN): continue
    d=dpoly(x,y,coast)
    if d<14 or d>rnd.uniform(40,150): continue
    if not ok_lab(x,y): continue
    if any(dpoly(x,y,r)<8 for r in MROADS): continue
    if any(math.hypot(x-a,y-b)<14 for a,b in MB): continue
    MB.append((x,y))
    w=rnd.uniform(9,17);h=rnd.uniform(6,10)
    kk=min(range(len(coast)-1),key=lambda i:dseg(x,y,coast[i],coast[i+1])); ang=math.degrees(math.atan2(coast[kk+1][1]-coast[kk][1],coast[kk+1][0]-coast[kk][0]))+rnd.choice([0,0,90])
    bl.append(f'<rect x="{-w/2:.1f}" y="{-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{rnd.choice(ROOF)}" stroke="#5a4028" stroke-width="0.5" transform="translate({x:.1f},{y:.1f}) rotate({ang:.0f})"/>')
# mainland trees
for _ in range(260):
    x=rnd.uniform(75,1695); y=rnd.uniform(205,1525)
    if pip(x,y,MAIN) and dpoly(x,y,coast)>120 and ok_lab(x,y) and all(dpoly(x,y,r)>8 for r in MROADS):
        bl.append(circ(x,y,rnd.uniform(4,7),'#7d9c62','#4f7346',0.5,'fill-opacity="0.85"'))
for r in ROADS: o.append(path(smooth(r),'none','#8a7350',5.5,'stroke-linecap="round"')+path(smooth(r),'none','#fbf3df',3.6,'stroke-linecap="round"'))
for r in MROADS: o.append(path(smooth(r),'none','#8a7350',5.5)+path(smooth(r),'none','#fbf3df',3.6))
o.append(''.join(bl))
# bridges
def bridge(x1,y1,x2,y2,draw=False):
    dx,dy=x2-x1,y2-y1;L=math.hypot(dx,dy);ux,uy=dx/L,dy/L;px,py=-uy,ux
    s=line(x1,y1,x2,y2,'#3a2a10',15)+line(x1,y1,x2,y2,'#fbf3df',11)
    n=int(L//18)
    for i in range(1,n):
        cx,cy=x1+dx*i/n,y1+dy*i/n
        s+=line(cx-px*7,cy-py*7,cx+px*7,cy+py*7,'#8a7350',1)+circ(cx-px*8,cy-py*8,2.2,'#3a2a10')+circ(cx+px*8,cy+py*8,2.2,'#3a2a10')
    if draw:
        mx,my=(x1+x2)/2,(y1+y2)/2
        s+=line(mx-ux*14,my-uy*14,mx+ux*14,my+uy*14,'#1b8098',11)+line(mx-ux*14-px*8,my-uy*14-py*8,mx-ux*14+px*8,my-uy*14+py*8,CORAL,2.4)+line(mx+ux*14-px*8,my+uy*14-py*8,mx+ux*14+px*8,my+uy*14+py*8,CORAL,2.4)
    return s
o.append(bridge(905,322,902,438)); o.append(bridge(1272,810,1548,830,True)); o.append(bridge(880,1250,900,1436,True))
# harbour quays & piers
quay=ISL[9:17]
o.append(path(smooth(quay),'none','#3a2a10',8)+path(smooth(quay),'none','#efe6cf',5))
import itertools
acc=0
for a_,b_ in zip(quay[:-1],quay[1:]):
    L_=math.hypot(b_[0]-a_[0],b_[1]-a_[1]); n_=max(1,int(L_//48))
    for i_ in range(n_):
        t_=(i_+0.5)/n_; x=a_[0]+(b_[0]-a_[0])*t_; y=a_[1]+(b_[1]-a_[1])*t_
        if abs(x-1272)<26 and abs(y-810)<40: continue
        nx,ny=(b_[1]-a_[1])/L_,-(b_[0]-a_[0])/L_
        if (x+nx*20-C0[0])**2+(y+ny*20-C0[1])**2<(x-C0[0])**2+(y-C0[1])**2: nx,ny=-nx,-ny
        x+=nx*4;y+=ny*4;Lp=50+ (acc%3)*8; acc+=1; ex,ey=x+nx*Lp,y+ny*Lp
        o.append(line(x,y,ex,ey,'#3a2a10',6.5)+line(x,y,ex,ey,'#d9c7a0',4))
        if acc%4!=0: o.append(ship(x+nx*Lp*0.6-ny*13,y+ny*Lp*0.6+nx*13,24,math.degrees(math.atan2(ny,nx))))
for (x,y,a) in [(1440,700,80),(1470,1060,100),(1360,1190,125),(1210,1300,170),(1060,1338,178),(700,1338,182),(380,1322,188),(150,1300,200),(1480,600,70),(130,800,60),(600,372,5)]:
    o.append(ship(x,y,30,a))
for (x,y,a,L) in [(1552,740,180,40),(1550,900,180,40),(1570,1010,190,40),(1590,600,170,36)]:
    ar=math.radians(a); ex,ey=x+L*math.cos(ar),y+L*math.sin(ar)
    o.append(line(x,y,ex,ey,'#5c4e3d',6)+line(x,y,ex,ey,'#d9c7a0',4))
# shipping lane
lane=[(70,1250),(330,1300),(640,1338),(900,1345),(1150,1320),(1330,1230),(1400,1110),(1390,1010)]
o.append(path(smooth(lane),'none','#e9fbfd',1.6,'stroke-dasharray="3 9" stroke-opacity="0.9"'))
# pleasure barge
o.append(G(path('M-22,0 Q-8,-10 22,-5 L22,5 Q-8,10 -22,0 Z','url(#goldGrad)','#3a2a10',0.9)+rect(-6,-4,18,8,'#1d879e','#3a2a10',0.6,2),'translate(1118,1202) rotate(-38) scale(1.25)'))
# tide temple
TX,TY=1170,372
o.append(path(f'M1085,470 Q1120,420 {TX-8},{TY+10}','none','#ecdcb6',5,'stroke-dasharray="2 5" stroke-linecap="round"'))
o.append(circ(TX,TY,20,'url(#sand)','#8a7350',1)+rect(TX-9,TY-9,18,18,'#fff',WALL,1)+circ(TX,TY,5.5,'#1d879e',GOLD,1.2))
# scryer posts
SCRY=[(340,300),(1512,372),(1600,1168),(420,1432),(1262,612),(1050,1196)]
for (x,y) in SCRY:
    o.append(circ(x,y,7,'#f4fdfe',TEAL,1.4)+circ(x,y,3,TEAL)+circ(x,y,11,'none','#f4fdfe',0.9,'stroke-dasharray="2 3"'))
# ---------- palace summit ----------
g=[]
gg=[path(smooth(GARD,True),'#b9cf95','#6f8a55',1)]
p.d.append(f'<clipPath id="gard"><path d="{smooth(GARD,True)}"/></clipPath>')
tr=[]
for i,(r,c) in enumerate([(232,'#a8c486'),(186,'#b9cf95'),(140,'#a8c486'),(94,'#c6d8a4')]):
    tr.append(circ(492,1132,r,c,'#f7f1e2',2.2))
gg.append(G(''.join(tr),extra='clip-path="url(#gard)"'))
for r_,n_ in [(209,11),(163,9),(117,6)]:
    for i_ in range(n_):
        a_=math.radians(-78+i_*(86/(n_-1)) ) ; x=492+r_*math.cos(a_); y=1132+r_*math.sin(a_)
        if pip(x,y,scale_pts(GARD,(540,1070),0.9)): gg.append(tree(x,y,7,'#6f9a5a','#3f6a40','#f2b63a'))
gg.append(fountain(520,1012,12)); gg.append(circ(622,1128,13,'#f4eee0',WALL,1)+circ(622,1128,10,'url(#poolGrad)',TEAL,0.8))
gg.append(path(smooth([(443,1140),(450,1112),(476,1091),(514,1095),(548,1126),(558,1150)]),'none','url(#sand)',13,'stroke-linecap="round"')+path(smooth([(443,1140),(450,1112),(476,1091),(514,1095),(548,1126),(558,1150)]),'none','#b99c63',1,'stroke-dasharray="1 4"'))
gg.append(line(500,1040,494,1090,'#3a2a10',7)+line(500,1040,494,1090,'#fff',4.5,'stroke-dasharray="2.5 2.5"'))
o.append(''.join(gg))
# north back wing (ruined)
g.append(rect(560,706,170,56,'#e9dfc8','#7a6a52',1.2,0,'stroke-dasharray="6 3"')+rect(560,706,170,56,'url(#rockHatch2)'))
g.append(rect(540,690,22,90,'#fff',WALL,1)+rect(728,720,22,60,'#fff',WALL,1))
g.append(path('M500,776 A40,40 0 0 0 500,856 Z','#f7efe0',WALL,1.2)+path('M500,786 A30,30 0 0 0 500,846','none',GOLD,0.9))
g.append(rect(500,780,270,72,'#ffffff',WALL,1.3))
g.append(rect(500,780,82,72,'#f6ecd4',WALL,0.9)+rect(582,772,100,88,'#ffffff',WALL,1.2)+rect(682,786,56,60,'#f6ecd4',WALL,0.9))
g.append(circ(632,816,30,'#1d879e',GOLD,1.6)+circ(632,816,20,'none','#e9c877',0.8)+star(632,816,14,8,5,GOLD,'#8f651d'))
for x in range(690,738,8): g.append(circ(x,786,1.8,GOLD)+circ(x,846,1.8,GOLD))
for x in range(508,580,9): g.append(circ(x,784,1.5,GOLD)+circ(x,848,1.5,GOLD))
g.append(rect(516,806,50,20,'#fbf6ec',GOLD,0.8,3))
g.append(rect(738,770,72,92,'#f1e8d3',WALL,1)+circ(778,816,22,'#fbf6ec',GOLD,1.3)+star(778,816,18,8,6,'#e9c877',DGOLD))
g.append(rect(540,872,180,40,'#ffffff',WALL,1.2)+rect(606,866,48,52,'#f6ecd4',WALL,1)+path('M606,918 A24,14 0 0 0 654,918','#f7efe0',WALL,0.9))
g.append(rect(540,852,22,22,'#fff',WALL,1)+rect(700,852,22,22,'#fff',WALL,1))
for x in range(566,700,10): g.append(line(x,852,x,872,'#d9cdb4',0.7))
for (x,y) in [(540,690),(562,690),(728,720),(750,720),(540,912),(720,912),(500,780),(500,852),(770,780),(770,852)]:
    g.append(circ(x,y,6,'#1d879e',GOLD,1.1))
for (x,y) in [(520,740),(760,880),(790,750),(800,880),(520,880),(770,740),(810,760),(810,870)]: g.append(cypress(x,y,4))
o.append(G(''.join(g),'translate(455,816) scale(1.4) translate(-455,-816)'))
g=[]
# causeway + villa
cw=[(508,764),(466,728),(442,690),(422,668)]
g.append(path(smooth(cw),'none','#3a2a10',10)+path(smooth(cw),'none','#fff8e6',7)+path(smooth(cw),'none',GOLD,1.2,'stroke-dasharray="4 3"'))
g.append(rect(476,734,12,12,CORAL,'#fff',1.2,0,'transform="rotate(38 482 740)"')+rect(431,674,12,12,CORAL,'#fff',1.2,0,'transform="rotate(40 437 680)"'))
vs=[path('M500,450 C150,470 150,655 500,675 Z','#efe2c4',GOLD,12),path('M330,500 C215,520 215,605 330,625 C285,600 285,525 330,500 Z','url(#poolGrad)',TEAL,7),
    path('M540,240 H1060 V350 H1220 V775 H1060 V885 H540 C390,860 390,700 540,675 H500 C290,650 290,475 500,450 H540 C390,425 390,265 540,240 Z','#ffffff',WALL,18,'stroke-linejoin="round"'),
    path('M500,450 C290,475 290,650 500,675 M540,240 C390,265 390,425 540,450 M540,675 C390,700 390,860 540,885','none','#1fa3b8',34),
    circ(963,562,70,'#1d879e',GOLD,14), rect(1060,510,160,105,'#e9c877',WALL,10)]
g.append(path('M336,708 Q358,724 382,708','none','#14232b',5)+path('M336,708 Q358,724 382,708','none','#f6d88a',1.4,'stroke-dasharray="3 2"'))
g.append(G(''.join(vs),'translate(287.3,606.2) scale(0.11)'))
o.append(''.join(g))
# delegation route
route=[(905,205),(905,322),(902,438),(880,520),(940,580),(1040,660),(1050,760),(1010,816),(940,816)]
o.append(path(smooth(route),'none','#fff',5,'stroke-opacity="0.7"')+path(smooth(route),'none',CORAL,2.6,'stroke-dasharray="9 5"'))
o.append(circ(1000,650,13,'#fbf6ec',GOLD,1.4)+star(1000,650,9,8,3.5,'#e9c877',DGOLD))
p.a(G(''.join(o),extra='clip-path="url(#m)"'))
# ---------- labels ----------
o=[]
HS='style="paint-order:stroke;stroke:#0e566d;stroke-width:3.5px;stroke-linejoin:round"'
def plate(x,y,w,h): return rect(x-w/2,y,w,h,'#fbf6ec',GOLD,1,5,'fill-opacity="0.9"')
o.append(plate(1162,884,172,50)+T(1162,905,'THE ISLAND-CITY','rl',15,extra='letter-spacing="2"')+T(1162,923,'red roofs · tan coral-stone','rs',12))
o.append(plate(750,474,200,42)+T(750,492,'NORTH TERRACES','rl',14,extra='letter-spacing="2"')+T(750,508,'shipwrights · sail lofts','rs',12))
o.append(plate(1107,1094,100,20)+T(1107,1109,'FISH QUAY','rl',12.5))
o.append(plate(1335,230,240,42)+T(1335,248,'NORTH SHORE','rl',14,extra='letter-spacing="2"')+T(1335,264,'warehouses · caravan yards','rs',12))
o.append(plate(1240,1448,232,42)+T(1240,1466,'SOUTH SHORE','rl',14,extra='letter-spacing="2"')+T(1240,1482,'vineyards · villas · ferry stairs','rs',12))
o.append(plate(1632,640,96,38)+T(1632,656,'EAST','rl',13)+T(1632,672,'SHORE','rl',13))
o.append(plate(1025,209,184,20)+T(1025,224,'to the Salt-Lantern · 5 miles ↑','rs',12,extra='style="font-weight:700;fill:#8a2f1c"'))
o.append(plate(730,604,164,24)+T(730,621,'SUMMER PALACE','rl',13.5,extra='letter-spacing="2"'))
o.append(line(300,742,334,706,'#fbf6ec',1.4)+plate(222,728,178,42)+T(222,746,'SALT-ARCH VILLA','rl',13.5,extra='letter-spacing="1"')+T(222,762,'cavern mouth beneath','rs',12))
o.append(T(218,905,'MOUTH OF THE BAY','sea',18.5,extra='letter-spacing="3" '+HS)+T(218,932,'open sea westward','sea',14,extra=HS)+T(218,952,'“green and cobalt and midnight”','sea',13,extra=HS))
o.append(T(1420,925,'GRAND','sea',19,extra='letter-spacing="4" '+HS)+T(1420,950,'HARBOUR','sea',19,extra='letter-spacing="4" '+HS))
o.append(T(640,1380,'SOUTH CHANNEL · deep water · ship lane','sea',14,extra='letter-spacing="1.5" '+HS))
o.append(T(700,400,'NORTH CHANNEL · tidal shallows','sea',14,extra='letter-spacing="1.5" '+HS))
o.append(T(215,388,"PRINCE'S FLIGHT CORRIDOR",'sea',14.5,extra='letter-spacing="1.5" style="font-weight:700;font-style:normal;fill:#ffe9a8;paint-order:stroke;stroke:#0e566d;stroke-width:3.5px"')+T(215,407,'due west-north-west, low over the water','sea',12.5,extra=HS))
o.append(T(268,446,'THE TEETH · reef','sea',13,extra='letter-spacing="1.5" '+HS))
# keys
KEYS=[(648,770,1),(938,768,2),(492,816,3),(721,701,4),(700,930,5),(566,1006,6),(494,1150,7),(476,696,8),(372,612,9),(404,724,10),(812,816,11),(1345,1010,12),(1146,1232,13),(934,380,14),(1410,786,15),(930,1300,16),(TX+36,TY-8,17),(376,298,18),(326,500,19),(972,676,20)]
for x,y,n in KEYS: o.append(circ(x,y,12.5,'#fbf6ec','none',0,'fill-opacity="0.85"')+key(x,y,n))
p.a(G(''.join(o),extra='data-box="76,204,1694,1526"'))
rh=''.join(line(205,1150,205+900*math.cos(math.radians(a)),1150+900*math.sin(math.radians(a)),'#c9f1f6',0.6,'stroke-opacity="0.35"') for a in [-78,-56,-33,-11,11,33,56,78,-101,101])
p.a(G(rh,extra='clip-path="url(#m)"'))
p.a(compass(205,1150,70))
p.a(G(rect(92,1440,336,74,'#0e566d','#c9f1f6',1,4,'fill-opacity="0.8"')+scalebar(112,1462,1,(0,50,100,200),light=True)+T(260,1504,'palace & villa drawn at twice scale for legibility','sea',11.5)))
p.a(rect(MX0,MY0,MX1-MX0,MY1-MY0,'none',TEAL,2,5))
# ---------- sidebar ----------
SX=1742; SW=588
p.a(panel_head(SX,186,'II','GAZETTEER OF THE HEADLAND',SW))
p.a(rect(SX-2,200,SW+2,566,'#fdfaf3',TEAL,2,5,'fill-opacity="0.82"'))
GZ=[('Summer Palace — State Wing','Plate III'),('Arrival Court & landing platform','canon'),('West Sea-Terrace & banquet hall','Plate III'),('Back wing — still in ruin since Amarantha','canon'),('Guest Wing — suites round a sea-lounge','canon'),('Terraced Citrus & Fountain Gardens','Plate IV'),('Private Sea-Cove & the Tide Stair','Plate IV'),('Guarded Cliff Causeway — two posts','⚑'),('The Salt-Arch Villa (+38 m)','Plate I'),("Prince's sea-cavern, beneath the villa",'Plate I'),('Treasure vaults — palm-locked doors','canon'),('Grand Harbour & merchant quays','canon'),("High Lord's pleasure-barge mooring",'canon'),('North Bridge — the delegation\'s way in','canon'),('East Drawbridge','canon'),('South Drawbridge over the ship lane','canon'),('Tide-Temple — causeway bare at low tide','canon'),('Shore water-scryer posts (six)','⚑'),('The Teeth — reef that keeps hulls off','⚑'),('Pearl Market & the upper city stair','⚑')]
o=[]
for i,(t,tag) in enumerate(GZ):
    y=228+i*26.5
    col={'canon':TEAL,'⚑':CORAL}.get(tag,DGOLD)
    o.append(key(SX+22,y,i+1)+T(SX+42,y+4.5,t,'nt',13.5)+T(SX+SW-18,y+4.5,tag,'nb',12,'end',f'style="fill:{col};font-style:italic"'))
    o.append(line(SX+42,y+13,SX+SW-18,y+13,'#d9cdb4',0.6))
o.append(T(SX+SW/2,759,'canon = from the books   ·   ⚑ = devised for this table','sub',12,'middle'))
p.a(G(''.join(o),extra=f'data-box="{SX},202,{SX+SW},766"'))
# legend
y0=812
p.a(panel_head(SX,y0-14,'III','LEGEND',SW))
p.a(rect(SX-2,y0,SW+2,172,'#fdfaf3',TEAL,2,5,'fill-opacity="0.82"'))
L=[(line(0,0,40,0,CORAL,2.4,'stroke-dasharray="9 5"'),"Autumn delegation's route"),(rect(0,-7,40,14,'#1b8098')+line(0,0,40,0,'#f6d88a',2.6,'stroke-dasharray="10 5"'),"Prince's flight corridor"),
(line(0,0,40,0,'#5c4e3d',6.5)+line(0,0,40,0,'#fff8e6',4)+line(0,0,40,0,GOLD,1,'stroke-dasharray="3 3"')+rect(15,-5,10,10,CORAL,'#fff',1,0,'transform="rotate(45 20 0)"'),'Causeway · guard post'),(G(circ(20,0,7,'#f4fdfe',TEAL,1.4)+circ(20,0,3,TEAL)),'Water-scryer post'),
(line(0,0,40,0,'#5c4e3d',9)+line(0,0,40,0,'#fbf3df',6)+line(14,0,26,0,'#1b8098',7),'Bridge · raising span'),(rect(0,-7,40,14,'#1b8098')+line(0,0,40,0,'#e9fbfd',1.8,'stroke-dasharray="3 7"'),'Deep-water ship lane'),
(path('M0,3 q10,-9 20,0 t20,0','none','#8a7350',1.3),'Contour, 10 m (summit +55 m)'),(rect(0,-7,40,14,'url(#sand)','#b99c63',0.6),'Sand · tidal flat'),
(rect(2,-6,14,10,'#c0563a','#5a4028',0.5)+rect(22,-3,14,9,'#f4efe2','#5a4028',0.5),'City roofs (tile · coral-stone)'),(circ(20,0,7,'#1d879e',GOLD,1.3),'Palace turret · sea-glass dome'),
(G(tree(20,0,7,'#6f9a5a','#3f6a40','#f2b63a')),'Citrus terrace'),(rect(0,-7,40,14,'#e9dfc8','#7a6a52',1.2,0,'stroke-dasharray="7 4"')+rect(0,-7,40,14,'url(#rockHatch2)'),'Ruined wing, rebuilding')]
o=[]
for i,(sym,txt) in enumerate(L):
    x=SX+18+(i%2)*290; y=y0+24+(i//2)*25.5
    o.append(G(sym,f'translate({x},{y})')+T(x+50,y+4.5,txt,'nt',13))
p.a(''.join(o))
# notes
y1=1030
p.a(panel_head(SX,y1-14,'IV','CANON & TACTICAL NOTES',SW))
p.a(rect(SX-2,y1,SW+2,500,'#fdfaf3',TEAL,2,5,'fill-opacity="0.82"'))
notes=[('The lie of the land.','A tan-stone palace on a mountain-island in the heart of a half-moon bay; the mainland circles it on three sides and the west lies open to the sea.'),
('Three bridges.','All traffic funnels over them. The east and south spans raise for ships, and a raised span cuts the island off within minutes.'),
('The delegation\'s way in.','Coast road from the Salt-Lantern, North Bridge, the upper city stair, then the Arrival Court and its sea-glass doors.'),
('The villa stands apart.','One causeway, two guard posts, and a west cliff with no beach beneath it. Whoever comes to the Salt-Arch comes announced.'),
('Prince\'s corridor.','The cavern mouth faces west-north-west. The Teeth keep hulls a quarter-mile off, the palace mass blocks the city, and the nearest scryer post is on the far north shore.'),
('Where he is seen.','Above 60 m, or anywhere east of the summit, he is in view of the whole harbour. Fly at dusk, low, and turn only beyond the reef.'),
('Slipping away.','The gardens fall south-west to the private cove. The Tide Stair is overlooked by nothing but the guest-wing balconies.')]
o=[]; yy=y1+30
for lead,body in notes:
    s_,h=para(SX+16,yy,lead,body,SW-40,13.5,18.5); o.append(s_); yy+=h+16
print('notes end',yy,'limit',y1+500, 'bld',len(placed),len(MB))
p.a(G(''.join(o),extra=f'data-box="{SX},{y1+2},{SX+SW},{y1+498}"'))
p.save('/home/sable/Dragonbound/art/adriata/plate02_adriata_palace_grounds.svg')
