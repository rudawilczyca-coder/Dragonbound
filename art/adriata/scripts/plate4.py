from lib import *
import random
rnd=random.Random(5)
p=P(); background(p)
frame(p,'IV',"GUEST WING, TERRACED GARDENS & THE TIDE STAIR","South-west slope of the palace summit · citrus terraces, reflecting pool, tide baths, labyrinth and the private sea-cove",'ADRIATA & THE SUMMER COURT PALACE','Dragonbound Cartographic Suite · Plate IV of IV')
MX0,MY0,MX1,MY1=70,200,1700,1530
p.d.append(f'<clipPath id="m"><rect x="{MX0}" y="{MY0}" width="{MX1-MX0}" height="{MY1-MY0}" rx="5"/></clipPath>')
p.d.append('<pattern id="shellfl" width="26" height="26" patternUnits="userSpaceOnUse"><rect width="26" height="26" fill="#f6efe0"/><circle cx="6" cy="7" r="1.6" fill="#d8c7a0"/><circle cx="19" cy="17" r="1.6" fill="#bfe0e0"/><path d="M12 22 q3 -5 6 0" fill="none" stroke="#d8c7a0" stroke-width="0.8"/></pattern><pattern id="perg" width="14" height="14" patternUnits="userSpaceOnUse"><rect width="14" height="14" fill="#e9dcc0"/><path d="M0 0 V14" stroke="#8a6a3a" stroke-width="2.2"/><circle cx="8" cy="5" r="2.2" fill="#b0508f"/><circle cx="10" cy="11" r="1.8" fill="#c76aa6"/></pattern><pattern id="grass2" width="16" height="16" patternUnits="userSpaceOnUse"><rect width="16" height="16" fill="#bfd29c"/><path d="M3 5 l1 -3 M10 12 l1 -3 M13 4 l1 -2" stroke="#8fa868" stroke-width="0.8"/></pattern>')
p.a(panel_head(72,186,'I','THE SOUTH-WEST GARDENS — PLAN',1626))
HS='style="paint-order:stroke;stroke:#0e566d;stroke-width:3.5px;stroke-linejoin:round"'
GS='style="stroke:#dfe8c6"'
o=[rect(MX0,MY0,MX1-MX0,MY1-MY0,'url(#seaGrad)'),rect(MX0,MY0,MX1-MX0,MY1-MY0,'url(#waves)')]
LAND=[(400,200),(1700,200),(1700,1530),(1190,1530),(1150,1462),(1090,1402),(1010,1368),(930,1340),(850,1296),(780,1266),(700,1266),(640,1292),(606,1340),(596,1420),(574,1486),(524,1474),(492,1380),(468,1280),(452,1180),(440,1050),(404,950),(430,800),(420,640),(440,480),(410,330)]
coast=LAND[2:]+[LAND[0]]
ld='M400,200 L1700,200 L1700,1530 '+smooth(coast).replace('M','L',1)+' Z'
# bathymetry
for k,op in [(14,0.6),(34,0.45),(60,0.35),(92,0.28)]:
    o.append(path('M400,200 L1700,200 L1700,1530 '+smooth(coast).replace('M','L',1)+' Z','none','#c9f1f6',k*2,f'stroke-opacity="{0.07}" stroke-linejoin="round"'))
o.append(path(ld,'none','#f4fdfe',8,'stroke-opacity="0.5"'))
o.append(path(ld,'url(#cliffRock)','#5c4e3d',1.8)); o.append(path(ld,'url(#rockHatch)','none',0,'fill-opacity="0.6"'))
# cliff hachures west
wc=[(410,330),(440,480),(420,640),(430,800),(404,950),(440,1050),(452,1180),(468,1280),(492,1380)]
for i in range(len(wc)-1):
    a,b=wc[i],wc[i+1]
    for k in range(8):
        t=k/8; x=a[0]+(b[0]-a[0])*t; y=a[1]+(b[1]-a[1])*t
        o.append(line(x+4,y,x+24,y+2,'#6b5a44',1,'stroke-opacity="0.75"'))
# beach
bp=[(606,1336),(640,1292),(700,1266),(780,1266),(850,1296),(930,1340),(1006,1366)]
o.append(path(smooth(bp),'none','url(#sand)',34,'stroke-linecap="round"')+path(smooth(bp),'none','#b99c63',1,'stroke-dasharray="1 5"'))
# terraces ground
o.append(rect(540,440,940,204,'url(#gravel)','#8a7350',1))           # parterre +52
o.append(rect(500,664,1020,182,'url(#grass2)','#6f8a55',1))          # citrus +46
o.append(rect(470,866,1230,180,'url(#gravel)','#8a7350',1))          # pool terrace +40
o.append(path('M480,1066 H1280 V1230 Q1100,1262 960,1240 Q860,1200 780,1186 Q660,1180 560,1232 Q500,1160 480,1066 Z','url(#grass2)','#6f8a55',1))  # sea garden +30
# retaining walls
for y,x1,x2 in [(440,540,1480),(644,540,1480),(664,500,1520),(846,500,1520),(866,470,1700),(1046,470,1290),(1066,480,1280)]:
    o.append(line(x1,y,x2,y,'#5c4e3d',4)+line(x1,y,x2,y,'#f7efe0',1.6,'stroke-dasharray="6 4"'))
p.a(G(''.join(o),extra='clip-path="url(#m)"'))
o=[]
# ---- south colonnade & guest wing ----
o.append(rect(560,205,900,34,'url(#shellfl)',WALL,1.4))
for x in range(580,1460,44): o.append(column(x,239,5))
GW=[]
GW.append(rect(600,262,820,150,'#fdfbf5',WALL,3))
GW.append(path('M900,412 H1120 V432 Q1010,476 900,432 Z','url(#tileDiamond)',WALL,3))
GW.append(rect(900,262,220,150,'url(#tileDiamond)'))
GW.append(rect(600,262,300,150,'url(#tileHerrB)')+rect(1120,262,300,150,'url(#tileHerr)'))
GW.append(rect(600,262,820,150,'none',WALL,3))
GW.append(wall_v(750,262,412,[(330,356)],3.5)+wall_v(900,262,412,[(330,356)],3.5)+wall_v(1120,262,412,[(330,356)],3.5)+wall_v(1270,262,412,[(330,356)],3.5))
for x in [750,900,1120,1270]: GW.append(line(x,330,x,356,GOLD,1.6,'stroke-dasharray="2 3"'))
GW.append(line(900,412,1120,412,'#fdfbf5',4)+line(600,412,900,412,'#1fa3b8',4,'stroke-dasharray="11 4"')+line(1120,412,1420,412,'#1fa3b8',4,'stroke-dasharray="11 4"'))
GW.append(rect(600,414,300,12,'#f3ead6',GOLD,1)+rect(1120,414,300,12,'#f3ead6',GOLD,1))
o.append(''.join(GW))
for (x,c) in [(630,'#2a8fa3'),(780,'#2a8fa3'),(1150,'#b5482f'),(1300,'#2a8fa3')]: o.append(bed(x,272,30,34,0,False,cover=c))
for x in [930,970,1010,1050,1090]: o.append(column(x,440+ (10 if x in(970,1050) else 0) + (14 if x==1010 else 0),5))
o.append(divan(940,300,60,18)+divan(1020,300,60,18)+brazier(1010,352,9))
# ---- upper parterre ----
def hbed(x,y,w,h):
    return Fg(rect(x,y,w,h,'url(#hedge)','#3f6a40',1.2,10)+rect(x+12,y+12,w-24,h-24,'#e9dfc8','#3f6a40',0.8,6)+''.join(tree(x+w*(i+0.5)/3,y+h/2,9,'#c76aa6','#8a3d6e') if i==1 else tree(x+w*(i+0.5)/3,y+h/2,8,'#6f9a5a','#3f6a40','#f2b63a') for i in range(3)))
for (x,y) in [(580,462),(580,560),(790,462),(790,560),(1070,462),(1070,560),(1280,462),(1280,560)]:
    o.append(hbed(x,y,170,64 if y<500 else 52))
o.append(fountain(1010,545,40)); o.append(Fg(''.join(shell(1010+56*math.cos(math.radians(a)),545+56*math.sin(math.radians(a)),7,a+90) for a in (45,135,225,315))))
o.append(stairs(990,640,40,28,4,'s')+stairs(548,640,36,28,4,'s')+stairs(1436,640,36,28,4,'s'))
# ---- citrus terrace ----
for yy in (702,752,802):
    for x in range(600,1440,56):
        if abs(x-1010)<40: continue
        o.append(tree(x,yy,13,'#6f9a5a','#3f6a40','#f2b63a' if (x//56+yy)%2 else '#f08a2a'))
o.append(rect(996,668,28,174,'url(#gravel)','#8a7350',0.8))
o.append(Fg(rect(560,822,400,20,'url(#perg)','#8a6a3a',1.2))+Fg(rect(1060,822,400,20,'url(#perg)','#8a6a3a',1.2)))
o.append(Fg(circ(528,752,30,'#f7efe0',WALL,1.4)+circ(528,752,24,'#c76aa6','#8a3d6e',1,'fill-opacity="0.55"')+''.join(circ(528+27*math.cos(i*math.pi/3),752+27*math.sin(i*math.pi/3),3.2,GOLD,WALL,0.6) for i in range(6))))
o.append(Fg(rect(1462,722,56,60,'#f7efe0',WALL,1.4)+rect(1470,730,40,44,'#f6e9a8',GOLD,1)+''.join(circ(x,y,3.2,GOLD,WALL,0.6) for x in (1462,1518) for y in (722,782))))
o.append(stairs(990,842,40,28,4,'s')+stairs(1480,842,36,28,4,'s')+stairs(508,842,36,28,4,'s'))
# ---- pool terrace ----
o.append(Fg(rect(690,922,560,60,'#f4eee0',WALL,1.4,30)+rect(698,930,544,44,'url(#poolGrad)',TEAL,1,22)+''.join(path(f'M{720+i*64},952 q16,-8 32,0','none','#e9fbfd',0.9) for i in range(8))))
for x in range(700,1250,50): o.append(cypress(x,896,7)+cypress(x,1010,7))
# channel to tholos & cascade
o.append(rect(440,946,252,12,'#7fdbe4',TEAL,0.9)+path('M440,940 L404,930 L404,974 L440,964 Z','#e9fbfd',TEAL,0.8)+''.join(line(436-i*8,943+i,436-i*8,961-i,'#7fdbe4',1.6) for i in range(1,4)))
th=circ(560,952,48,'#f7efe0',WALL,1.6)+circ(560,952,38,'#1d879e',GOLD,2)+circ(560,952,26,'none','#e9c877',1)+''.join(line(560+10*math.cos(a),952+10*math.sin(a),560+38*math.cos(a),952+38*math.sin(a),'#e9c877',0.9) for a in [i*math.pi/6 for i in range(12)])+circ(560,952,6,GOLD,WALL,0.8)
th+=''.join(circ(560+43*math.cos(a),952+43*math.sin(a),4,GOLD,WALL,0.7) for a in [i*math.pi/4+0.39 for i in range(8)])
o.append(Fg(th))
o.append(stairs(990,1042,40,28,4,'s')+stairs(640,1042,36,28,4,'s')+stairs(1262,1042,36,28,4,'s'))
# ---- tide baths ----
B=[rect(1310,884,350,290,'#fdfbf5',WALL,3),rect(1310,884,110,130,'url(#tileSq)'),rect(1420,884,240,160,'url(#tileScale)'),rect(1310,1014,110,160,'url(#tileSmall)'),rect(1420,1044,240,130,'url(#tileSmall)'),rect(1310,884,350,290,'none',WALL,3)]
B.append(wall_v(1420,884,1174,[(936,966),(1090,1120)],3.5)+wall_h(1014,1310,1420,[(1350,1380)],3.5)+wall_h(1044,1420,1660,[(1524,1556)],3.5))
B.append(line(1310,936,1310,966,'#fdfbf5',4)+line(1310,936,1310,966,GOLD,1.6,'stroke-dasharray="2 3"'))
B.append(line(1420,1174,1660,1174,'#fdfbf5',4)+line(1420,1174,1660,1174,'#1fa3b8',4,'stroke-dasharray="11 4"'))
o.append(''.join(B))
o.append(Fg(circ(1540,964,56,'#f4eee0',WALL,1.3)+circ(1540,964,47,'#cfeef1',TEAL,0.8)+circ(1540,964,38,'#9fdde5',TEAL,0.8)+circ(1540,964,28,'url(#poolGrad)',TEAL,0.8)))
o.append(Fg(rect(1444,1068,192,84,'#f4eee0',WALL,1.3,10)+rect(1452,1076,176,68,'url(#poolGrad)',TEAL,0.9,8)))
o.append(Fg(circ(1365,1110,30,'#f4eee0',WALL,1.2)+circ(1365,1110,22,'#f1c9a0','#b5482f',1)+star(1365,1110,12,6,5,'#f6b040',CORAL)))
o.append(Fg(rect(1318,892,12,34,'#d9c79e',WALL,0.8,2))+Fg(rect(1318,976,12,30,'#d9c79e',WALL,0.8,2))+Fg(rect(1340,892,70,10,'#d9c79e',WALL,0.8,2)))
for (x,y) in [(1436,900),(1644,900),(1436,1028),(1644,1028)]: o.append(column(x,y,5))
o.append(path('M1540,1174 V1240 Q1500,1420 1160,1470','none','#14232b',4.5,'stroke-opacity="0.5"')+path('M1540,1174 V1240 Q1500,1420 1160,1470','none','#7fdbe4',2.6,'stroke-dasharray="4 4"'))
# ---- sea-garden: labyrinth, tamarisk, bench ----
LC=(1130,1150); lab=[]
lab.append(circ(LC[0],LC[1],80,'#e9dfc8','#3f6a40',1))
for i,r in enumerate([74,60,46,32,18]):
    g0=(i*97+20)%360; gap=26+ i*6
    a1=math.radians(g0+gap/2); a2=math.radians(g0-gap/2+360)
    x1,y1=LC[0]+r*math.cos(a1),LC[1]+r*math.sin(a1); x2,y2=LC[0]+r*math.cos(a2),LC[1]+r*math.sin(a2)
    lab.append(f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 1 1 {x2:.1f},{y2:.1f}" fill="none" stroke="#4a7344" stroke-width="8"/><path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 1 1 {x2:.1f},{y2:.1f}" fill="none" stroke="#76a067" stroke-width="3" stroke-dasharray="3 3"/>')
lab.append(circ(LC[0],LC[1],7,'#f7efe0',GOLD,1.4))
o.append(Fg(''.join(lab)))
for (x,y) in [(520,1090),(556,1118),(600,1096),(650,1128),(700,1100),(750,1136),(800,1104),(860,1132),(912,1100),(960,1150)]:
    o.append(tree(x,y,rnd.uniform(10,14),'#9db88a','#5f8a55'))
o.append(Fg(path('M930,1232 Q965,1220 1000,1236','none','#b89868',7)+path('M930,1232 Q965,1220 1000,1236','none','#f1e8d4',3)))
# ---- tide stair ----
ts=[]
ts.append(rect(0,-14,112,28,'#e8dcc4',WALL,1.3))
for i in range(1,16): ts.append(line(i*7,-14,i*7,14,WALL,0.7))
ts.append(rect(70,-14,42,28,'#3fa9ba','none',0,0,'fill-opacity="0.55"')+line(70,-18,70,18,'#e9fbfd',1.6,'stroke-dasharray="3 2"')+line(98,-18,98,18,'#e9fbfd',1.2,'stroke-dasharray="1 3"'))
ts.append(line(6,0,60,0,INK,1)+'<polygon points="60,0 53,-4 53,4" fill="#1b2d36"/>')
o.append(Fg(G(''.join(ts),'translate(520,1262) rotate(31)')))
o.append(path('M560,1232 Q528,1240 520,1262','none','#8a7350',5)+path('M560,1232 Q528,1240 520,1262','none','#fbf3df',3))
# grotto + skiff
o.append(path('M1012,1362 Q1060,1318 1096,1398 Q1050,1372 1012,1362 Z','#14232b','#5c4e3d',1.5)+circ(1040,1352,3,'#f6d88a')+circ(1078,1372,3,'#f6d88a'))
o.append(ship(1000,1408,30,-25,'#fbf3df')+ship(1040,1486,26,60))
# cliff path west
cp=[(512,952),(470,900),(458,800),(450,640),(468,480),(440,330),(440,205)]
o.append(path(smooth(cp),'none','#5c4e3d',5)+path(smooth(cp),'none','#fbf3df',3,'stroke-dasharray="6 4"'))
# sightline wedge from lounge
o.append(path('M1010,452 L700,846 L1320,846 Z','#f6d88a','none',0,'fill-opacity="0.16"')+line(1010,452,700,846,'#b8860b',1,'stroke-dasharray="8 5"')+line(1010,452,1320,846,'#b8860b',1,'stroke-dasharray="8 5"'))
# quiet route
qr=[(1454,240),(1520,330),(1542,560),(1542,780),(1498,856),(1400,874),(1290,884),(1276,980),(1280,1056),(1262,1090),(1236,1160),(1190,1228),(1080,1242),(980,1206),(900,1182),(820,1198),(700,1204),(560,1232)]
o.append(path(smooth(qr),'none','#fff',5,'stroke-opacity="0.65"')+path(smooth(qr),'none',CORAL,2.6,'stroke-dasharray="9 5"'))
for _ in range(70):
    x=rnd.uniform(1576,1690); y=rnd.uniform(380,850)
    o.append(tree(x,y,rnd.uniform(7,11),'#9db88a','#5f8a55'))
for _ in range(60):
    x=rnd.uniform(1230,1684); y=rnd.uniform(1390,1512)
    if y> 1380+ (1690-x)*0.2 and not (1380<x<1690 and 1432<y<1506): o.append(tree(x,y,rnd.uniform(6,10),'#9db88a','#5f8a55'))
for i in range(3):
    pts=[(1700,1270+i*34),(1560,1290+i*36),(1400,1330+i*34),(1280,1400+i*30),(1210,1470+i*26)]
    o.append(path(smooth(pts),'none','#8a7350',1,'stroke-opacity="0.6"'))
o.append(rect(1560,250,120,70,'#f4efe2',WALL,1.6)+line(1560,285,1680,285,'#d9cdb4',1)+line(1620,250,1620,320,'#d9cdb4',1))
o.append(ship(250,840,34,-65))
o.append(T(1176,1366,'sea-grotto','rs',12.5,extra='style="stroke:#e6dac2;font-style:italic"'))
# ---- labels ----
o.append(T(820,227,'SOUTH COLONNADE OF THE STATE WING · Plate III ↑','rl',12.5,extra='letter-spacing="1"'))
o.append(T(1010,385,'SEA-LOUNGE','rl',13.5)+T(675,372,'SEAFOAM','rl',11.5)+T(675,387,'ROOM','rl',11.5)+T(825,372,'PEARL','rl',11.5)+T(825,387,'ROOM','rl',11.5)+T(1195,372,'CORAL','rl',11.5)+T(1195,387,'ROOM','rl',11.5)+T(1345,372,'TIDE','rl',11.5)+T(1345,387,'ROOM','rl',11.5))
o.append(T(520,300,'GUEST','rl',15,extra='letter-spacing="2"')+T(520,319,'WING','rl',15,extra='letter-spacing="2"')+T(520,337,'four linked rooms','rs',12))
o.append(T(1010,633,'UPPER PARTERRE · +52 m','rl',14,extra='letter-spacing="1.5"'))
o.append(T(1235,827,'CITRUS TERRACE · +46 m','rl',14,extra='letter-spacing="1.5" '+GS)) if False else None
o.append(T(682,683,'CITRUS TERRACE · +46 m','rl',14,extra='letter-spacing="1.5" '+GS))
o.append(T(826,1036,'REFLECTING POOL · +40 m','rl',12.5,extra='letter-spacing="1"'))
o.append(T(560,1022,'POOL PAVILION','rl',12.5)+T(560,890,'sea-glass dome','rs',12))
o.append(T(1540,905,'TEPID HALL','rl',12.5)+T(1540,1062,'SEA-PLUNGE','rl',12.5)+T(1365,1036,'HOT ROOM','rl',11.5)+T(1368,954,'ROBING','rl',11.5))
o.append(T(1410,1202,'THE TIDE BATHS','rl',15,extra='letter-spacing="2" style="stroke:#e6dac2"')+T(1410,1220,'sea-fed at every flood','rs',12.5,extra='style="stroke:#e6dac2"')+T(1596,1250,'sea conduit','rs',12,extra='style="stroke:#e6dac2;font-style:italic"'))
o.append(T(1150,1284,'↑ MYRTLE LABYRINTH','rl',12.5,extra='style="stroke:#e6dac2"'))
o.append(T(700,1166,'SEA-GARDEN · +30 m','rl',14,extra='letter-spacing="1.5" '+GS)+T(700,1183,'tamarisk · rosemary · myrtle','rs',12.5,extra=GS))
o.append(T(800,1356,'THE PRIVATE COVE','sea',19,extra='letter-spacing="3" '+HS)+T(800,1380,'white sand · no path but the stair','sea',13,extra=HS))
o.append(T(815,1470,'MOUTH OF THE BAY','sea',15,extra='letter-spacing="3" '+HS))
o.append(T(1130,1385,'sea-grotto','sea',12.5,extra=HS)) if False else None
o.append(T(1590,1340,'CLIFF · 30 m','rl',13,extra='style="stroke:#e6dac2"')+T(1590,1357,'no descent east of the cove','rs',12.5,extra='style="stroke:#e6dac2"'))
o.append(T(238,640,'cliff path to','sea',13,extra=HS)+T(238,658,'the causeway &','sea',13,extra=HS)+T(238,676,'the Salt-Arch Villa','sea',13,extra=HS)+T(238,694,'(Plate I) ↑','sea',12.5,extra=HS))
o.append(T(300,956,'THE CASCADE','sea',13,extra='letter-spacing="2" '+HS)+T(300,974,'pool spills 40 m','sea',12.5,extra=HS))
o.append(T(1620,340,'kitchens &','rs',12.5,extra='style="stroke:#e6dac2"')+T(1620,356,'service court','rs',12.5,extra='style="stroke:#e6dac2"')+T(1634,612,'olive grove','rs',12.5,extra='style="stroke:#e6dac2;font-style:italic"'))
KEYS=[(1010,326,1),(1010,545,2),(528,752,3),(1490,752,4),(760,832,5),(560,952,6),(1200,952,7),(418,952,8),(1540,964,9),(1540,1110,10),(1365,1110,11),(1130,1150,12),(910,1244,13),(500,1244,14),(580,1336,15),(1058,1352,16),(456,560,17),(1522,440,18)]
for x,y,n in KEYS: o.append(circ(x,y,12.5,'#fbf6ec','none',0,'fill-opacity="0.85"')+key(x,y,n))
o=[x for x in o if x]
p.a(G(''.join(o),extra='data-box="74,204,1696,1526"'))
p.a(compass(238,360,56))
# ---- inset: tide stair section ----
IX,IY,IW,IH=92,1090,330,418
ins=[rect(IX,IY,IW,IH,'#fbf6ec',TEAL,1.6,5),rect(IX+5,IY+5,IW-10,IH-10,'none',GOLD,0.8,3)]
ins.append(T(IX+IW/2,IY+28,'THE TIDE STAIR','nb',15,'middle','letter-spacing="2"')+T(IX+IW/2,IY+46,'section looking north · 24 rock-cut treads','sub',12.5,'middle'))
sx,sy=IX+34,IY+96; n=24; tw_,th_=8,10
pts=[(IX+12,sy)]+[(sx,sy)]
for i in range(n):
    pts.append((sx+i*tw_,sy+(i+1)*th_)); pts.append((sx+(i+1)*tw_,sy+(i+1)*th_))
pts+=[(IX+IW-12,sy+n*th_),(IX+IW-12,IY+IH-58),(IX+12,IY+IH-58)]
pd='M'+' L'.join(f'{x:.0f},{y:.0f}' for x,y in pts)+' Z'
HW=sy+17*th_-4; LW=sy+24*th_-3
ins.append(rect(IX+12,HW,IW-24,IY+IH-58-HW,'#bfe6ec','none',0,0,'fill-opacity="0.6"')+rect(IX+12,LW,IW-24,IY+IH-58-LW,'#2893a9','none',0,0,'fill-opacity="0.75"'))
ins.append(line(IX+12,HW,IX+IW-12,HW,TEAL,1.3,'stroke-dasharray="7 4"')+line(IX+12,LW,IX+IW-12,LW,TEAL,1.3))
ins.append(path(pd,'url(#cliffRock)',WALL,1.4)+path(pd,'url(#rockHatch)'))

ins.append(T(IX+IW-18,HW-6,'high water','nt',11.5,'end','style="fill:#144a5c;font-style:italic"')+T(IX+IW-18,LW-7,'low water','nt',11.5,'end','style="fill:#144a5c;font-style:italic"'))
ins.append(T(sx-8,sy-8,'rock shelf below the sea-garden','nt',11.5,'start'))
# arrows for flood
ax=IX+IW-86
ins.append(line(ax,LW-24,ax,HW+22,CORAL,1.6)+f'<polygon points="{ax},{HW+14} {ax-5},{HW+24} {ax+5},{HW+24}" fill="{CORAL}"/>')
ins.append(T(IX+IW/2,IY+IH-36,'The evening flood covers seven treads,','nt',12,'middle')+T(IX+IW/2,IY+IH-19,'one every few minutes.','nt',12,'middle'))
p.a(G(''.join(ins),extra=f'data-box="{IX},{IY},{IX+IW},{IY+IH}"'))
p.a(G(rect(1394,1440,290,58,'#fbf6ec',TEAL,1,4,'fill-opacity="0.92"')+scalebar(1412,1464,10,(0,5,10,20))))
p.a(rect(MX0,MY0,MX1-MX0,MY1-MY0,'none',TEAL,2,5))
# ---------- sidebar ----------
SX=1742; SW=588
p.a(panel_head(SX,186,'II','KEY TO THE GARDENS',SW))
p.a(rect(SX-2,200,SW+2,520,'#fdfaf3',TEAL,2,5,'fill-opacity="0.82"'))
GZ=[('Sea-lounge, open to the bay; rooms connect','canon'),('Shell Fountain, four clipped parterres','⚑'),('Bougainvillea bower — screened seat for two','⚑'),('Lemon Pavilion, shaded and shuttered','⚑'),('Wisteria pergola under the retaining wall','⚑'),('Pool Pavilion — domed tholos on the point','⚑'),('Reflecting pool, sixty paces long','⚑'),('The Cascade, falling to the sea','⚑'),('Tepid hall — stepped round pool','⚑'),('Sea-plunge, refilled by each flood','⚑'),('Hot room over a banked fire-bowl','⚑'),('Myrtle labyrinth, head-high hedges','⚑'),('Whisper bench above the cove','⚑'),('Head of the Tide Stair','⚑'),('Lowest dry tread at dusk','⚑'),('Sea-grotto and skiff mooring','⚑'),('Cliff path to the causeway','⚑'),('Service stair from the colonnade','⚑')]
o=[]
for i,(t,tag) in enumerate(GZ):
    y=228+i*26.5
    col={'canon':TEAL,'⚑':CORAL}.get(tag,DGOLD)
    o.append(key(SX+22,y,i+1)+T(SX+42,y+4.5,t,'nt',13.5)+T(SX+SW-18,y+4.5,tag,'nb',12,'end',f'style="fill:{col};font-style:italic"'))
    o.append(line(SX+42,y+13,SX+SW-18,y+13,'#d9cdb4',0.6))
o.append(T(SX+SW/2,708,'canon = from the books   ·   ⚑ = devised for this table','sub',12,'middle'))
p.a(G(''.join(o),extra=f'data-box="{SX},202,{SX+SW},720"'))
y0=766
p.a(panel_head(SX,y0-14,'III','LEGEND',SW))
p.a(rect(SX-2,y0,SW+2,146,'#fdfaf3',TEAL,2,5,'fill-opacity="0.82"'))
L=[(line(0,0,40,0,CORAL,2.6,'stroke-dasharray="9 5"'),'The quiet way down'),(path('M0,8 L20,-8 L40,8 Z','#f6d88a','#b8860b',1,'fill-opacity="0.4" stroke-dasharray="6 4"'),'Overlooked from the lounge'),
(line(0,0,40,0,'#5c4e3d',4)+line(0,0,40,0,'#f7efe0',1.6,'stroke-dasharray="6 4"'),'Retaining wall & balustrade'),(G(tree(12,0,7,'#6f9a5a','#3f6a40','#f2b63a')+tree(30,0,7,'#6f9a5a','#3f6a40','#f08a2a')),'Lemon · bitter orange'),
(rect(0,-6,40,12,'url(#perg)','#8a6a3a',1),'Pergola in flower'),(G(cypress(12,0,6)+tree(30,0,7,'#9db88a','#5f8a55')),'Cypress · tamarisk'),
(rect(0,-6,40,12,'url(#hedge)','#3f6a40',1,3),'Clipped myrtle hedge'),(rect(0,-6,40,12,'url(#poolGrad)',TEAL,1,3),'Pool · fountain · runnel'),
(rect(0,-6,40,12,'url(#sand)','#b99c63',0.6),'Sand beach'),(G(stairs(4,-7,32,14,4,'e',arrow=False)),'Stair (arrow points down)')]
o=[]
for i,(sym,txt) in enumerate(L):
    x=SX+18+(i%2)*290; y=y0+24+(i//2)*25.5
    o.append(G(sym,f'translate({x},{y})')+T(x+50,y+4.5,txt,'nt',13))
p.a(''.join(o))
y1=958
p.a(panel_head(SX,y1-14,'IV','WALKING, SCHEMING, SLIPPING AWAY',SW))
p.a(rect(SX-2,y1,SW+2,572,'#fdfaf3',TEAL,2,5,'fill-opacity="0.82"'))
notes=[('Four levels, twenty-two metres.','Each terrace hides the one below it from the palace. Only the parterre and the middle of the citrus rows lie under the guest-wing balconies.'),
('The guest wing.','Linked rooms round a lounge open to the sea, as Summer lodges visiting courts. A late-arriving emissary would be put here, a short walk from every garden stair.'),
('To be seen walking.','The parterre and the pool are where the court strolls before dinner. A pair pacing the cypress allée is visible, proper and out of earshot.'),
('To talk unheard.','The bougainvillea bower, the shuttered Lemon Pavilion, and the heart of the labyrinth, where head-high myrtle swallows a voice at six paces.'),
('The quiet way.','Service stair, east steps, behind the Lemon Pavilion, round the baths and the labyrinth hedge: from the colonnade to the Tide Stair without once crossing the lounge sightline.'),
('The Tide Stair.','Rock-cut, twenty-four treads, the last seven under water at the flood. It is the only way to the cove, and the only way back passes the sea-garden in full view of anyone at the whisper bench.'),
('By water.','A skiff in the grotto reaches the west cliff below the Salt-Arch in a quarter-hour at slack tide; the Teeth lie beyond.'),
('After dark.','Only the parterre lanterns and the pavilion dome are lit. The lower terraces, the labyrinth and the stair keep no lamps.')]
o=[]; yy=y1+30
for lead,body in notes:
    s_,h=para(SX+16,yy,lead,body,SW-40,13.5,18.5); o.append(s_); yy+=h+9
print('notes end',yy,'limit',y1+572)
p.a(G(''.join(o),extra=f'data-box="{SX},{y1+2},{SX+SW},{y1+570}"'))
p.save('/home/sable/Dragonbound/art/adriata/plate04_summer_palace_gardens_and_baths.svg')
