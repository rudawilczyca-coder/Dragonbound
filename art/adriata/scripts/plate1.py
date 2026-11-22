from lib import *
p=P()
background(p)
frame(p,'I',"THE SALT-ARCH VILLA & PRINCE'S SEA-CAVERN","Adriata western cliffside · guest quarters of the Autumn delegation · plans at +38 m and +6 m with section A–A′",'ADRIATA & THE SUMMER COURT PALACE','Dragonbound Cartographic Suite · Plate I of IV')
p.d.append('<clipPath id="c1"><rect x="70" y="200" width="1370" height="725" rx="5"/></clipPath><clipPath id="c2"><rect x="70" y="982" width="1370" height="548" rx="5"/></clipPath><clipPath id="c3"><rect x="1490" y="200" width="840" height="800" rx="5"/></clipPath>')
HALO_SEA='style="paint-order:stroke;stroke:#0e566d;stroke-width:3px;stroke-linejoin:round"'
# =================== PANEL I ===================
p.a(panel_head(72,186,'I','MAIN VILLA DECK — CANTILEVERED OVER THE BAY MOUTH (ELEV. +38 m)',1366))
o=[]
o.append(rect(70,200,1370,725,'url(#seaGradH)'))
o.append(rect(70,200,1370,725,'url(#waves)'))
# bathymetry
for i,(x0,lab) in enumerate([(555,'−4'),(495,'−8'),(425,'−12'),(345,'−18'),(255,'−25'),(160,'−32')]):
    pts=[(x0+14*math.sin(y/70+i*1.3)+ (y-560)*0.03*(i-2),y) for y in range(190,940,50)]
    o.append(path(smooth(pts),'none','#bfeef4',1.0,f'stroke-opacity="{0.55-i*0.05}" stroke-dasharray="{"" if i%2==0 else "9 5"}"'))
    ly=912 if i<3 else 792; li=14 if i<3 else 12
    if i==0: continue
    o.append(f'<text x="{pts[li][0]+5:.0f}" y="{ly}" font-family="Noto Sans" font-style="italic" font-size="12" fill="#e3f8fb">{lab} m</text>')
# rock
cl=[(640,200),(626,222),(612,240),(608,400),(606,560),(606,720),(604,885),(612,905),(598,925)]
o.append(path(smooth(cl)+' L1440,925 L1440,200 Z','url(#cliffRock)','#6b5a44',1.5))
o.append(path(smooth(cl)+' L1440,925 L1440,200 Z','url(#rockHatch)'))
# surf line + hachures along visible cliff edge
for (xa,ya,xb,yb) in [(640,200,612,240),(604,885,598,925)]:
    for k in range(7):
        t=k/6; x=xa+(xb-xa)*t; y=ya+(yb-ya)*t
        o.append(line(x-2,y,x-20,y+3,'#f1fbfc',1.2,'stroke-opacity="0.8"'))
        o.append(line(x+3,y,x+16,y-2,'#6b5a44',0.9))
# contours
for i,(x0,lab) in enumerate([(1250,'+40'),(1290,'+45'),(1332,'+50'),(1380,'+55 m')]):
    pts=[(x0+9*math.sin(y/55+i*0.9)+(i*4 if y<350 else 0),y) for y in range(190,940,40)]
    o.append(path(smooth(pts),'none','#8a7350',1.1 if i<3 else 1.6,'stroke-opacity="0.75"'))
    o.append(T(pts[1][0]+2,218,lab,'dim',12.5,extra='style="fill:#4a3716;stroke:#e6dac2;font-weight:700"'))
for (x,y) in [(1408,250),(1418,300),(1402,345),(1420,400),(1410,455),(1415,640),(1421,770),(1409,830),(1418,890)]:
    o.append(cypress(x,y,6))
p.a(G(''.join(o),extra='clip-path="url(#c1)"'))
o=[]
# ---- floors ----
SAL='M540,450 H830 V675 H540 H500 C370,645 370,480 500,450 Z'
DECK='M500,450 C262,470 262,655 500,675 C370,645 370,480 500,450 Z'
POOL='M405,497 C312,515 312,610 405,628 C362,600 362,525 405,497 Z'
ERI='M540,240 H900 V450 H540 C482,410 482,280 540,240 Z'
AUR='M540,675 H900 V885 H540 C482,845 482,715 540,675 Z'
BALN='M540,240 C440,270 440,420 540,450 C482,410 482,280 540,240 Z'
BALS='M540,675 C440,705 440,855 540,885 C482,845 482,715 540,675 Z'
o.append(path(DECK,'url(#planks)',GOLD,2)); o.append(path(POOL,'url(#poolGrad)',TEAL,1.4))
o.append(path('M395,520 q-8,42 0,84','none','#e9fbfd',0.8,'stroke-opacity="0.8"')+path('M380,528 q-10,34 0,68','none','#e9fbfd',0.8,'stroke-opacity="0.6"'))
o.append(path(BALN,'#f3ead6',GOLD,1.6)); o.append(path(BALS,'#f3ead6',GOLD,1.6))
o.append(path(SAL,'url(#tileDiamond)'))
o.append(path(ERI,'url(#tileHerr)')); o.append(path(AUR,'url(#tileHerrB)'))
o.append(rect(900,240,160,210,'url(#tileSq)'))           # war study
o.append(rect(830,450,36,225,'url(#tileHerr)'))          # corridor
o.append(rect(866,450,194,225,'#fdfbf5'))                # gallery
o.append(rect(900,675,160,105,'url(#tileSq)'))           # stair lobby
o.append(rect(900,780,160,105,'url(#tileSmall)'))        # bath
o.append(rect(1060,350,160,160,'url(#tileSq)'))          # caelum
o.append(rect(1060,510,160,105,'url(#tileDiamond)'))     # gate hall
o.append(rect(1060,615,160,160,'url(#tileSq)'))          # pantry
# causeway
o.append(rect(1220,528,222,70,'#efe5cf',WALL,2))
for x in range(1232,1440,16): o.append(line(x,530,x,596,'#cdbd9c',0.7))
o.append(line(1220,534,1442,534,GOLD,1.4)+line(1220,592,1442,592,GOLD,1.4))
for x in range(1262,1440,44): o.append(circ(x,528,3.2,GOLD,WALL,0.7)+circ(x,598,3.2,GOLD,WALL,0.7))
# gate
o.append(line(1244,531,1244,595,DGOLD,4)+line(1250,531,1250,595,GOLD,1.4,'stroke-dasharray="3 3"')+circ(1244,531,4,GOLD,WALL,0.8)+circ(1244,595,4,GOLD,WALL,0.8))
# ---- mosaics ----
m=[circ(650,572,42,'#f4f8f6',TEAL,1.2),circ(650,572,37,'none',GOLD,1),circ(650,572,24,'#dff1f1',TEAL,0.7)]
for i in range(16):
    a=math.pi*i/8; m.append(line(650+24*math.cos(a),572+24*math.sin(a),650+37*math.cos(a),572+37*math.sin(a),TEAL,0.6))
m.append(star(650,572,34,8,9,'#2a8fa3','#144a5c')); m.append(star(650,572,20,4,5,GOLD,INK))
o.append(''.join(m))
m=[circ(963,562,58,'#fbf3dc',GOLD,1.4),circ(963,562,50,'none',TEAL,0.7)]
for i in range(24):
    a=math.pi*i/12
    m.append(f'<polygon points="{963+18*math.cos(a-0.06):.1f},{562+18*math.sin(a-0.06):.1f} {963+50*math.cos(a):.1f},{562+50*math.sin(a):.1f} {963+18*math.cos(a+0.06):.1f},{562+18*math.sin(a+0.06):.1f}" fill="{GOLD if i%2 else "#e9c877"}" fill-opacity="0.75"/>')
m.append(circ(963,562,17,'#fffbe8',GOLD,1.2,'stroke-dasharray="3 2"'))
o.append(''.join(m))
# rugs
o.append(f'<ellipse cx="626" cy="296" rx="62" ry="50" fill="#b5482f" fill-opacity="0.22" stroke="{CORAL}" stroke-width="0.9" stroke-dasharray="2 2"/>')
o.append(f'<ellipse cx="800" cy="335" rx="66" ry="62" fill="#c5963e" fill-opacity="0.16" stroke="{GOLD}" stroke-width="0.9" stroke-dasharray="2 2"/>')
o.append(f'<ellipse cx="626" cy="838" rx="62" ry="48" fill="#2a8fa3" fill-opacity="0.2" stroke="{TEAL}" stroke-width="0.9" stroke-dasharray="2 2"/>')
# ---- walls ----
W=[]
W.append(wall_h(240,540,1060)); W.append(wall_v(1060,240,350)); W.append(wall_h(350,1060,1220)); W.append(wall_v(1220,350,775,[(540,585)]))
W.append(wall_h(775,1060,1220)); W.append(wall_v(1060,775,885)); W.append(wall_h(885,540,1060))
W.append(wall_h(450,500,1060,[(836,860)])); W.append(wall_h(675,500,1060,[(836,860)]))
W.append(wall_v(830,450,675,[(545,580)])); W.append(wall_v(866,450,675,[(545,580)])); W.append(wall_v(1060,350,775,[(545,580)]))
W.append(wall_v(900,240,450,[(392,422)])); W.append(wall_v(900,675,885,[(746,774),(818,848)]))
W.append(wall_h(780,900,1060)); W.append(wall_h(510,1060,1220,[(1090,1120)])); W.append(wall_h(615,1060,1220,[(1090,1120)]))
o.append(''.join(W))
# glass
GL='stroke-dasharray="11 4" stroke-linecap="butt"'
o.append(path('M500,450 C370,480 370,645 500,675','none','#1fa3b8',4.5,GL))
o.append(path('M540,240 C482,280 482,410 540,450','none','#1fa3b8',4.5,GL))
o.append(path('M540,675 C482,715 482,845 540,885','none','#1fa3b8',4.5,GL))
o.append(path('M500,450 C262,470 262,655 500,675','none','#1fa3b8',1.6,'stroke-dasharray="5 3"'))
# doors
o.append(door_h(836,860,450,-1,'l')+door_h(836,860,675,1,'r'))
o.append(door_v(392,422,900,-1,'b')+door_v(746,774,900,1,'b')+door_v(818,848,900,-1,'b'))
o.append(door_h(1090,1120,510,-1,'l')+door_h(1090,1120,615,1,'l'))
for (x,y1,y2) in [(830,545,580),(866,545,580),(1060,545,580)]:
    o.append(line(x,y1,x,y2,GOLD,1.6,'stroke-dasharray="2 3"'))
o.append(star(889,380,6,6,2.6,CORAL,INK))   # ward seal on war-study door
# ---- furniture: Eris ----
o.append(bed(600,250,52,56)); o.append(Fg(rect(586,252,11,13,'#d9c79e',WALL,0.8)+rect(655,252,11,13,'#d9c79e',WALL,0.8)+rect(606,312,40,8,'#d9c79e',WALL,0.8,2)))
o.append(divan(762,278,76,24)); o.append(divan(762,368,76,24,180)); o.append(brazier(800,335,13))
o.append(divan(510,343,70,22,90))
o.append(Fg(rect(876,250,18,96,'#d9c79e',WALL,0.9)+''.join(line(876,250+i*16,894,250+i*16,WALL,0.6) for i in range(1,6))))
# war study
o.append(Fg(rect(906,246,148,10,'#b89868',WALL,0.8)+''.join(line(906+i*12,246,906+i*12,256,WALL,0.5) for i in range(1,12))))
o.append(Fg(rect(1044,264,10,116,'#b89868',WALL,0.8)+''.join(line(1044,264+i*12,1054,264+i*12,WALL,0.5) for i in range(1,10))))
o.append(Fg(rect(945,330,76,40,'#c9a871',WALL,1.2,2)+rect(952,335,46,30,'#f6ecd0',DGOLD,0.7)+path('M956,358 q10,-18 20,-6 t18,-8','none',TEAL,0.8)+circ(1008,342,3,GOLD,WALL,0.5)+chair(983,380,10,180)))
o.append(Fg(rect(912,418,24,18,'#5a4a36',WALL,1)+circ(924,427,3,GOLD)))
# salon
o.append(divan(472,550,80,24,90)); o.append(divan(430,508,66,22)); o.append(divan(430,594,66,22,180))
o.append(Fg(circ(462,562,12,'#f7f3ea',WALL,1)+circ(462,562,8,'none',GOLD,0.8)))
o.append(table_long(745,505,30,120,5))
for (x,y) in [(540,468),(540,657),(722,468),(722,657)]: o.append(column(x,y,7))
# gallery pillars
for i in range(8):
    a=math.radians(22.5+45*i); o.append(column(963+74*math.cos(a),562+74*math.sin(a),6.5))
# Aurelie
o.append(circ(626,847,42,'none','#1fa3b8',1,'stroke-dasharray="4 3"'))
o.append(bed(652,875,52,56,180,cover='#2a8fa3'))
o.append(Fg(rect(586,860,11,13,'#d9c79e',WALL,0.8)+rect(655,860,11,13,'#d9c79e',WALL,0.8)))
o.append(divan(510,769,70,22,90,cush='#b5482f'))
o.append(table_round(790,790,13,2))
o.append(Fg(rect(742,866,64,13,'#d9c79e',WALL,0.9,2)+path('M756,866 a18,10 0 0 1 36,0','#dff1f1',TEAL,0.8)+circ(774,856,0.1)))
o.append(Fg(rect(560,683,70,14,'#d9c79e',WALL,0.9)+''.join(line(560+i*14,683,560+i*14,697,WALL,0.6) for i in range(1,5))))
# stair + bath
o.append(spiral(1012,728,30,16))
o.append(T(941,700,'STAIR','rl',12)+T(941,715,'to cavern ↓','rs',11))
b=rect(922,804,118,66,'#f4eee0',WALL,1.2,16)+rect(930,811,102,52,'#cfeef1',TEAL,0.8,13)+rect(938,818,86,38,'#9fdde5',TEAL,0.8,10)+rect(946,825,70,24,'url(#poolGrad)',TEAL,0.8,8)
o.append(Fg(b)); o.append(Fg(rect(908,872,30,8,'#d9c79e',WALL,0.8,2))+T(981,797,'SUNKEN BATH','rl',10.5))
# Caelum
o.append(bed(1070,358,26,46,0,False,cover='#5a6c4a'))
o.append(Fg(rect(1204,362,10,40,'#5a4a36',WALL,0.8)+''.join(line(1200,366+i*8,1214,366+i*8,'#9aa3a8',1.4) for i in range(5))))
o.append(Fg(circ(1186,484,10,'#d9c79e',WALL,0.9)+chair(1168,484,8,-90)))
# pantry
o.append(Fg(rect(1204,625,10,140,'#b89868',WALL,0.8)+''.join(line(1204,625+i*14,1214,625+i*14,WALL,0.5) for i in range(1,10))))
o.append(Fg(rect(1128,747,70,20,'#7a4a3a',WALL,0.9)+''.join(circ(1136+i*9,753,2.6,'#3a1f1a') for i in range(7))+''.join(circ(1136+i*9,761,2.6,'#3a1f1a') for i in range(7))))
o.append(Fg(f'<ellipse cx="1088" cy="745" rx="16" ry="11" fill="#c9a871" stroke="{WALL}" stroke-width="0.9"/><ellipse cx="1088" cy="745" rx="10" ry="6" fill="#e8dcc0"/>'))
o.append(Fg(circ(1180,640,9,'#f7f3ea',WALL,0.9)+circ(1180,640,4,'#b5482f','none',0,'fill-opacity="0.6"')))
# gate hall benches
o.append(Fg(rect(1150,516,60,9,'#d9c79e',WALL,0.8,2))+Fg(rect(1150,600,60,9,'#d9c79e',WALL,0.8,2)))
# ---- labels ----
o.append(ML(690,415,["ERIS'S MASTER SUITE"],'rl',extra='style="fill:#7a2618"')+T(690,432,'curved sea-glass wall · hearth lounge','rs'))
o.append(T(975,292,'WAR STUDY','rl',14)+T(975,308,'ward-sealed door','rs'))
o.append(T(630,481,'GREAT SALON','rl',16)+T(631,499,'cantilevered sea-glass arc','rs'))
o.append(T(963,474,'SUN-GALLERY','rl',14)+T(963,662,'entry rotunda · fluted pillars','rs'))
o.append(f'<text x="848" y="562" transform="rotate(-90 848 562)" dy="4" font-family="Noto Sans" font-weight="700" font-size="10.5" fill="{DGOLD}" text-anchor="middle" letter-spacing="0.8">PRIVATE INNER CORRIDOR</text>')
o.append(T(690,718,"AURELIE'S SUITE",'rl',extra='style="fill:#144a5c"')+T(690,735,'sea-silk canopy · balcony','rs')+T(690,751,'private stair to Prince ↓','rs'))
o.append(ML(1142,430,["CAELUM'S","QUARTERS"],'rl',17,14)+T(1142,464,'gate watch · armoury','rs'))
o.append(ML(1140,668,["WARD & LINEN","PANTRY"],'rl',17,14)+T(1140,702,'tea · wine · hounds','rs'))
o.append(T(1140,558,'GATE HALL','rl',13.5)+T(1140,575,'sole way in','rs'))
o.append(T(1338,558,'CLIFF CAUSEWAY','rl',13.5)+T(1338,576,'guarded · to the palace →','rs',11.5))
o.append(T(1150,268,'LIMESTONE CLIFF','rl',14,extra='style="stroke:#e0d3ba"')+T(1150,286,'rooms cut into living rock','rs',extra='style="stroke:#e0d3ba"'))
o.append(T(1330,700,'CLIFF RISES','rl',13,extra='style="stroke:#e0d3ba"')+T(1330,717,'17 m to the palace terrace','rs',extra='style="stroke:#e0d3ba"'))
# keys
for (x,y,n) in [(354,562,1),(545,562,2),(806,565,3),(650,630,4),(686,262,5),(800,259,6),(446,300,7),(446,826,7),(926,350,8),(686,838,9),(981,837,10),(950,736,11),(1272,506,12),(1186,374,13),(1118,745,14),(1112,757,''),(1166,735,15),(963,562,16)]:
    if n!='': o.append(key(x,y,n))
p.a(''.join(o))
# sea labels, compass, scale, section marks
p.a(compass(205,350,62,labels=('N','E','S','W')))
p.a(T(205,470,'← open sea · palace east →','sea',12))
p.a(T(210,650,'MOUTH OF','sea',17,extra='letter-spacing="5"')+T(210,675,'ADRIATA BAY','sea',21,extra='letter-spacing="5"')+T(210,697,'38 m sheer drop to the surf','sea',12.5))
p.a(scalebar(100,880,16,(0,2,5,10),light=True))
p.a(dimline(321,222,606,222,'17.8 m cantilever beyond the cliff face',off=-7).replace('class="dim"','class="dim" style="fill:#e9fbfd;stroke:#0e566d"').replace(f'stroke="{TEAL}"','stroke="#e9fbfd"'))
p.a(dimline(540,906,1220,906,'42.5 m · suites to gate',off=-6).replace('class="dim"','class="dim" style="stroke:#e0d3ba"'))
for (x,l) in [(96,'A'),(1426,'A′')]:
    p.a(G(circ(x,562,10,PARCH,INK,1.4)+f'<text x="{x}" y="566.5" text-anchor="middle" font-family="Noto Serif" font-weight="700" font-size="12" fill="{INK}">{l}</text>',cls='kr'))
p.a(line(108,562,318,562,'#e9fbfd',1.2,'stroke-dasharray="12 3 2 3" stroke-opacity="0.8"'))
p.a(rect(70,200,1370,725,'none',TEAL,2,5))
# locator
isl=[(40,60),(70,30),(120,22),(160,40),(178,80),(165,120),(120,138),(70,130),(38,100)]
LOC=G(rect(0,0,200,170,'#fdfaf3',TEAL,1.4,4)+rect(4,4,192,162,'url(#seaGradH)','none',0,3)+path('M4,4 H196 V30 Q150,22 120,10 Q60,16 4,34 Z','#d9c9a8','#6b5a44',0.8)+path('M4,166 H196 V140 Q150,150 110,158 Q50,156 4,142 Z','#d9c9a8','#6b5a44',0.8)+path('M196,30 Q176,80 196,140 Z','#d9c9a8','#6b5a44',0.8)+path(smooth(isl,True),'#e6d9bd','#6b5a44',1)+rect(66,62,44,30,'#fff',WALL,1)+path('M40,70 L4,56 L4,108 L40,92 Z','#f6d88a','none',0,'fill-opacity="0.35"')+circ(44,82,5,CORAL,'#fff',1.2)+T(100,160,'KEY PLAN · see Plate II','rsl',11)+T(88,81,'palace','rs',10)+T(52,112,'villa','rll',11,'start')+T(150,96,'city','rs',10),'translate(1228,1330)',extra='data-box="1228,1330,1428,1500"')
# =================== PANEL II ===================
p.a(panel_head(72,968,'II',"LOWER LEVEL — PRINCE'S VAULTED SEA-CAVERN (DIRECTLY BELOW, ELEV. +6 m) · IN REGISTER WITH I",1366))
DY=680
o=[rect(70,982,1370,548,'url(#seaGradH)'),rect(70,982,1370,548,'url(#waves)')]
for i,(x0,lab) in enumerate([(555,'−4'),(495,'−8'),(425,'−12'),(345,'−18'),(255,'−25'),(160,'−32')]):
    pts=[(x0+14*math.sin((y-DY)/70+i*1.3)+ (y-DY-560)*0.03*(i-2),y) for y in range(970,1560,50)]
    o.append(path(smooth(pts),'none','#bfeef4',1.0,f'stroke-opacity="{0.55-i*0.05}" stroke-dasharray="{"" if i%2==0 else "9 5"}"'))
# flight corridor
o.append(path('M590,1150 L70,1040 L70,1484 L590,1374 Z','#f6d88a','none',0,'fill-opacity="0.16"'))
o.append(line(590,1150,70,1040,'#f6d88a',1.4,'stroke-dasharray="10 6"')+line(590,1374,70,1484,'#f6d88a',1.4,'stroke-dasharray="10 6"'))
o.append(line(540,1262,150,1262,'#f6d88a',2.6,'stroke-dasharray="14 7"')+'<polygon points="126,1262 154,1251 154,1273" fill="#f6d88a"/>')
cl2=[(640,982),(622,1030),(608,1078),(606,1086),(606,1262),(604,1438),(600,1450),(612,1492),(596,1530)]
rock=smooth(cl2)+' L1440,1530 L1440,982 Z'
o.append(path(rock,'url(#cliffRock)','#6b5a44',1.5)); o.append(path(rock,'url(#rockHatch)')); o.append(path(rock,'url(#rockHatch2)','none',0,'fill-opacity="0.6"'))
# surf
o.append(path(smooth([(628,985),(606,1040),(592,1090)]),'none','#f4fdfe',3,'stroke-opacity="0.75" stroke-dasharray="14 5 4 5"'))
o.append(path(smooth([(590,1445),(598,1490),(582,1530)]),'none','#f4fdfe',3,'stroke-opacity="0.75" stroke-dasharray="14 5 4 5"'))
for (x,y,r) in [(540,1010,9),(556,1032,5),(520,1505,10),(545,1488,6),(486,1515,4)]:
    o.append(circ(x,y,r+3,'none','#f4fdfe',1,'stroke-opacity="0.6"')+circ(x,y,r,'#8f7d62','#4a3d2c',1))
# cavern
cav=[(606,1086),(680,1072),(820,1066),(980,1070),(1110,1090),(1172,1150),(1190,1262),(1172,1370),(1100,1436),(1030,1452),(985,1456),(940,1452),(880,1456),(720,1452),(604,1438)]
cd=smooth(cav[:-1]+[cav[-1]])
cd=smooth(cav)+' L590,1424 L590,1100 Z'
o.append(path(cd,'url(#cavernDark)','#14232b',4,'stroke-linejoin="round"'))
# ledge
o.append(path('M590,1100 L735,1090 Q768,1262 735,1434 L590,1424 Z','#566d78','#e6cfa0',1.4,'stroke-dasharray="5 3" fill-opacity="0.9"'))
for y in range(1115,1420,22): o.append(line(596,y,596+random.Random(y).randint(40,120),y+random.Random(y+1).randint(-4,4),'#8fa3ab',0.6,'stroke-opacity="0.6"'))
# tidal pool
o.append(f'<ellipse cx="850" cy="1160" rx="84" ry="46" fill="#14232b" fill-opacity="0.5"/><ellipse cx="850" cy="1160" rx="80" ry="42" fill="url(#poolGrad)" fill-opacity="0.85" stroke="#9eeaf5" stroke-width="1.6"/><ellipse cx="850" cy="1160" rx="60" ry="29" fill="none" stroke="#e9fbfd" stroke-width="0.7" stroke-opacity="0.6"/>')
o.append(path('M780,1140 Q740,1100 760,1072','none','#7fdbe4',2,'stroke-dasharray="3 3"'))
# sand bed
o.append(f'<ellipse cx="1078" cy="1262" rx="94" ry="88" fill="url(#sand)" stroke="#e6cfa0" stroke-width="1.5"/>')
o.append(dragon_coil(1080,1258,44,20))
# stalagmites + lanterns
for (x,y,r) in [(700,1120,7),(700,1392,8),(905,1090,6),(1010,1130,8),(1140,1180,6),(1150,1350,7),(915,1345,6)]:
    o.append(circ(x,y,r,'#5b727d','#14232b',1.2)+circ(x-1,y-1,r*0.4,'#8fa3ab'))
for (x,y) in [(660,1082),(860,1074),(1060,1086),(1168,1200),(1176,1330),(1090,1432),(840,1448),(680,1444)]:
    o.append(circ(x,y,7,'#f6d88a','none',0,'fill-opacity="0.35"')+circ(x,y,3,'#f6d88a','#8f651d',0.8))
# stair landing
o.append(path('M930,1368 H1040 V1440 Q985,1452 930,1440 Z','#efe4ce',GOLD,1.6))
o.append(spiral(985,1408,28,16,col='#dfd0b2'))
# villa footprint overhead
fp=f'M540,{240+DY} H1060 V{350+DY} H1220 V{775+DY} H1060 V{885+DY} H540 C440,{855+DY} 440,{705+DY} 540,{675+DY} H500 C262,{655+DY} 262,{470+DY} 500,{450+DY} H540 C440,{420+DY} 440,{270+DY} 540,{240+DY} Z'
o.append(path(fp,'none','#4a3208',3.6,'stroke-dasharray="9 6" stroke-opacity="0.55"')+path(fp,'none','#f6d88a',2,'stroke-dasharray="9 6"'))
p.a(G(''.join(o),extra='clip-path="url(#c2)"'))
o=[]
o.append(T(668,1250,'LAUNCH','rll',14)+T(668,1267,'LEDGE','rll',14)+T(668,1285,'sun-warmed stone','rsl',11.5))
o.append(T(850,1157,'TIDAL POOL','rll',13)+T(850,1175,'salt · blow-hole fed','rsl',12))
o.append(T(850,1252,"PRINCE'S VAULTED AERIE",'rll',16)+T(850,1272,'36 × 24 m · 16 m vault','rsl',12.5)+T(850,1289,'blind to every palace sightline','rsl',12.5))
o.append(T(1078,1337,'sand bed','rs',12,extra='style="stroke:#ecdcb6;font-weight:700"'))
o.append(T(822,1404,'STAIR LANDING','rll',13)+T(822,1421,"from Aurelie's lobby",'rsl',12))
o.append(T(205,1206,'OPEN FLIGHT','sea',18,extra='letter-spacing="4" '+HALO_SEA)+T(205,1231,'CORRIDOR','sea',18,extra='letter-spacing="4" '+HALO_SEA)+T(205,1295,'launch due west over open water;','sea',13,extra=HALO_SEA)+T(205,1313,'no palace roof, quay or scryer-post','sea',13,extra=HALO_SEA)+T(205,1331,'has a line on the arch','sea',13,extra=HALO_SEA))
o.append(T(1252,1054,'villa footprint overhead','rs',12.5,'start',extra='style="stroke:#e6dac2;font-weight:700;fill:#4a3716"')+T(1252,1070,'(+38 m, dashed)','rs',12,'start',extra='style="stroke:#e6dac2;fill:#4a3716"'))
o.append(T(1322,1180,'SOLID LIMESTONE','rl',14,extra='style="stroke:#e6dac2"')+T(1322,1198,'16 m of rock between','rs',12.5,extra='style="stroke:#e6dac2"')+T(1322,1214,'vault crown and villa floor','rs',12.5,extra='style="stroke:#e6dac2"'))
o.append(LOC)
o.append(dimline(572,1086,572,1438,'22 m sea-arch',off=-9).replace('class="dim"','class="dim" style="fill:#e9fbfd;stroke:#0e566d"').replace(f'stroke="{TEAL}"','stroke="#e9fbfd"'))
o.append(scalebar(100,1496,16,(0,2,5,10),light=True))
p.a(''.join(o)); p.a(rect(70,982,1370,548,'none',TEAL,2,5))
# =================== PANEL III ===================
p.a(panel_head(1492,186,'III','CLIFFSIDE SECTION A–A′ (W → E, LOOKING NORTH)',836))
SL=905; X0=1800
def Y(m): return SL-m*10
o=[rect(1490,200,840,800,'url(#skyGrad)')]
o.append(circ(1610,290,62,'#ffe7a8','none',0,'fill-opacity="0.3"')+circ(1610,290,40,'#ffe7a8','none',0,'fill-opacity="0.55"')+circ(1610,290,26,'#fff3cf'))
for (x,y,s) in [(1700,250,1),(1740,275,0.7),(1560,400,0.8),(1900,260,0.6)]:
    o.append(path(f'M{x-9*s},{y} q{4*s},{-6*s} {9*s},0 q{5*s},{-6*s} {9*s},0','none','#4d6068',1.2))
# sea
o.append(rect(1490,SL,840,95,'url(#seaGradV)'))
o.append(path(f'M1490,1000 L1490,985 Q1600,975 1700,958 Q1770,945 1802,925 L1802,1000 Z','#b9a57e','#6b5a44',1))
o.append(path(f'M1490,{SL} q14,-7 28,0 t28,0 t28,0 t28,0 t28,0 t28,0 t28,0 t28,0 t28,0 t28,0 t28,0','none','#f4fdfe',2))
for (x,y) in [(1530,935),(1640,948),(1590,962),(1720,930)]:
    o.append(path(f'M{x},{y} q8,-4 16,0 t16,0','none','#c9f1f6',0.9,'stroke-opacity="0.6"'))
# cliff
cp=[(1780,1000),(1800,SL),(1806,870),(1799,800),(1803,740),(1797,660),(1802,590),(1800,545),(1812,477),(1824,440),(1840,404),(1856,380),(1884,368),(1915,Y(55)),(2330,Y(55)),(2330,1000)]
cpd='M'+' L'.join(f'{x},{y}' for x,y in cp)+' Z'
p.d.append(f'<clipPath id="ccl"><path d="{cpd}"/></clipPath>')
o.append(path(cpd,'url(#cliffRock)','#5c4e3d',2.2)); o.append(path(cpd,'url(#rockHatch)'))
st=[]
for i,y0 in enumerate(range(395,1000,34)):
    pts=[(x,y0+6*math.sin(x/90+i)+ (x-1800)*0.02) for x in range(1780,2340,40)]
    st.append(path(smooth(pts),'none','#8a7350',0.9,f'stroke-opacity="0.55" stroke-dasharray="{"" if i%3 else "22 6"}"'))
o.append(G(''.join(st),extra='clip-path="url(#ccl)"'))
# surf rocks
o.append(circ(1772,SL+2,9,'#8f7d62','#4a3d2c',1)+circ(1752,SL+4,5,'#8f7d62','#4a3d2c',1)+path(f'M1740,{SL-2} q10,-10 22,-2 q10,-12 24,0','none','#fff',2,'stroke-opacity="0.9"'))
# cavern
FL=Y(6); 
cav3=f'M1786,{FL} L2150,{FL} Q2152,{FL-60} 2150,{FL-118} Q2080,{Y(22)-4} 1960,{Y(22)} Q1860,{Y(22)+4} 1800,{Y(20)} L1800,{FL-6} L1786,{FL-4} Z'
o.append(path(cav3,'url(#cavernDark)','#14232b',3,'stroke-linejoin="round"'))
for (x,h) in [(1850,16),(1890,10),(1935,20),(1990,12),(2040,18),(2090,11),(2125,14)]:
    yy=Y(22)+ (6 if x<1900 or x>2100 else 1)+ (10 if x>2120 else 0)
    o.append(f'<polygon points="{x-4},{yy} {x+4},{yy} {x},{yy+h}" fill="#5b727d" stroke="#14232b" stroke-width="0.8"/>')
o.append(rect(1786,FL,364,7,'#b8a68a',WALL,1.4))
o.append(path(f'M1894,{FL} q50,12 100,0 Z','url(#poolGrad)',TEAL,0.8))
o.append(path(f'M2030,{FL} q55,-16 118,0 Z','url(#sand)','#b99c63',0.8))

# stair shaft
o.append(rect(2023,Y(38)+8,22,Y(22)-Y(38)-12,'#e8dcc4',DGOLD,1.8))
for i in range(11): o.append(line(2023,Y(38)+20+i*13,2045,Y(38)+27+i*13,DGOLD,1.1))
o.append(rect(2023,Y(22)-2,22,FL-Y(22)+2,'none','#f2d084',1.4,0,'stroke-dasharray="4 4" stroke-opacity="0.8"'))
# villa
VF=Y(38); VC=VF-50
o.append(path(f'M1640,{VF+8} Q1745,{VF+12} 1800,{VF+100} L1800,{VF+8} Z','#d9ccb2',WALL,1.6))
o.append(path(f'M1660,{VF+8} Q1750,{VF+20} 1800,{VF+78}','none',GOLD,1)+path(f'M1700,{VF+8} Q1765,{VF+22} 1800,{VF+56}','none',GOLD,0.8))
o.append(rect(1672,VC,265,50,'#eef8f9')); o.append(rect(1937,VC,244,50,'#fbf4e6'))
o.append(rect(1628,VF,553,8,'#ffffff',WALL,1.8))
o.append(path(f'M1662,{VC} Q1740,{VC-14} 1818,{VC-2} L1818,{VC+6} L1662,{VC+6} Z','#ffffff',WALL,1.6)+path(f'M1662,{VC} Q1740,{VC-14} 1818,{VC-2}','none',GOLD,1.6))
o.append(line(1672,VC+6,1672,VF,'#1fa3b8',3))
o.append(rect(1636,VF-5,30,5,'url(#poolGrad)',TEAL,1)+line(1631,VF-14,1631,VF,'#1fa3b8',1.6))
for x in [1756,1870,1978,2063]: o.append(rect(x-2,VC+6 if x<1818 else VC,4,44 if x<1818 else 50,GOLD,WALL,0.5))
for x in [1937,1960,2081]: o.append(line(x,VC,x,VF,WALL,2.2))
o.append(line(2181,VC,2181,VF,DGOLD,3))
o.append(line(1818,VC,2181,VC,WALL,1.6))
# furniture silhouettes
o.append(rect(1716,VF-9,30,9,'#2a8fa3',WALL,0.7,3)+rect(1742,VF-17,5,17,'#d6c5a0',WALL,0.6,2))
o.append(rect(1880,VF-13,26,3,'#f7f3ea',WALL,0.7)+line(1884,VF-10,1884,VF,WALL,1)+line(1902,VF-10,1902,VF,WALL,1))
o.append(rect(2104,VF-9,40,9,'#d9c79e',WALL,0.7,2))
# figure for scale
o.append(circ(1790,VF-21,2.6,'#7a2618')+line(1790,VF-18,1790,VF-1,'#7a2618',2.2))
# oculus sun-well
o.append(rect(2015,Y(55),12,VC-Y(55),'#fff6d6',GOLD,1)+path(f'M2011,{Y(55)} q10,-12 20,0 Z','#bfe6ec',GOLD,1))
o.append(path(f'M2015,{VC} L2003,{VF} L2039,{VF} L2027,{VC} Z','#ffe7a8','none',0,'fill-opacity="0.45"'))
# causeway beyond
o.append(path(f'M2181,{VF} l20,0 l0,-14 l20,0 l0,-14 l20,0 l0,-14 l20,0 l0,-14 l20,0 l0,-14 l20,0 l0,-14 l20,0 l0,-14 l9,0','none',GOLD,2.4,'stroke-dasharray="6 3"'))
# palace terrace
PY=Y(55)
o.append(rect(2140,PY-5,190,5,'#ffffff',WALL,1.2))
for x in range(2146,2330,12): o.append(line(x,PY-16,x,PY-5,WALL,1))
o.append(line(2140,PY-16,2330,PY-16,WALL,1.6))
for x in [2232,2254,2276,2298]: o.append(rect(x-2,PY-52,4,47,'#fff',WALL,0.8))
o.append(path(f'M2224,{PY-52} Q2265,{PY-98} 2306,{PY-52} Z','#1d879e',GOLD,1.6)+line(2265,PY-76,2265,PY-90,GOLD,1.6)+circ(2265,PY-92,2.5,GOLD))
o.append(rect(2222,PY-56,86,5,'#fff',WALL,0.9))
for (x,h) in [(1945,34),(1962,26),(2090,38),(2108,28),(2180,30)]:
    o.append(f'<ellipse cx="{x}" cy="{PY-h/2}" rx="5" ry="{h/2}" fill="#2f5a3c" stroke="#1e3f2a" stroke-width="0.8"/>')
# flight arc
o.append(path(f'M1782,{FL-40} Q1700,{FL-44} 1622,{FL-84}','none',GOLD,2.6,'stroke-dasharray="9 5"'))
o.append(dragon_fly(1585,FL-92,0.8,-14))
o.append(line(2140,PY-16,1492,Y(55)-16+48,CORAL,1.3,'stroke-dasharray="3 5"'))
p.a(G(''.join(o),extra='clip-path="url(#c3)"'))
o=[]
# ruler
o.append(line(1506,Y(0),1506,Y(55),INK,1.2))
for m in range(0,56,5): o.append(line(1506,Y(m),1512 if m%10 else 1516,Y(m),INK,1))
for (m,l) in [(0,'0 m · sea'),(6,'+6 m · cavern'),(22,'+22 m · vault'),(38,'+38 m · villa'),(55,'+55 m · palace')]:
    o.append(line(1506,Y(m),1524,Y(m),TEAL,1.6)+T(1529,Y(m)-5,l,'el'))
o.append(line(1700,VC-22,1716,VC-8,TEAL,1.1)+rect(1574,VC-50,222,28,PARCH,TEAL,1.2,4,'fill-opacity="0.95"')+T(1685,VC-31,'SALT-ARCH VILLA · +38 m','rl',13))
o.append(T(1770,Y(55)-12,'palace sightline — all below is blind ground','rs',12,extra='style="font-style:italic;font-weight:700;fill:#8a2f1c;stroke:#eef5f0"'))
o.append(T(1626,VF+46,'cantilevered deck &','rs',12,extra='style="font-weight:700;fill:#144a5c"')+T(1626,VF+61,'infinity plunge pool','rs',12,extra='style="font-weight:700;fill:#144a5c"'))
o.append(line(1640,VF+32,1648,VF+10,TEAL,1.1))
o.append(T(1925,FL-88,"PRINCE'S CAVERN",'rll',15)+T(1925,FL-69,'vaulted aerie · 16 m vault','rsl',12.5))
o.append(rect(2096,Y(38)+62,196,40,PARCH,DGOLD,1,4,'fill-opacity="0.95"')+T(2194,Y(38)+79,'ROCK-CUT SPIRAL STAIR','rl',12)+T(2194,Y(38)+95,'160 treads · 32 m · private','rs',11.5))
o.append(line(2047,Y(38)+82,2096,Y(38)+82,DGOLD,1))
o.append(dimline(1900,VF+9,1900,Y(22)-3,'16 m solid limestone',off=-14).replace('class="dim"','class="dim" style="stroke:#dccfb6"'))
o.append(T(2150,PY-112,'SUMMER PALACE','rl',14)+T(2150,PY-95,'west sea-terrace','rs',12))
o.append(T(2232,Y(38)+22,'causeway stair climbs east','rs',12,extra='style="stroke:#e6dac2;font-weight:700;fill:#4a3716"')+T(2232,Y(38)+38,'(beyond the section plane)','rs',12,extra='style="stroke:#e6dac2;fill:#4a3716"'))
o.append(T(1690,FL-18,'dragon launch arc','rs',12.5,extra='style="font-style:italic;font-weight:700;fill:#144a5c;stroke:#f3f1e4"'))
o.append(T(1640,962,'ADRIATA BAY','sea',18,extra='letter-spacing="3" '+HALO_SEA))
o.append(T(2052,Y(55)+50,'oculus sun-well','rs',12,'start',extra='style="stroke:#e6dac2;fill:#4a3716"'))
o.append(scalebar(2120,968,10,(0,5,10,15)))
p.a(''.join(o)); p.a(rect(1490,200,840,800,'none',TEAL,2,5))
# =================== PANEL IV ===================
y0=1054
p.a(panel_head(1492,y0-14,'IV','LEGEND, KEY & TACTICAL NOTES',836))
p.a(rect(1490,y0,840,476,'#fdfaf3',TEAL,2,5,'fill-opacity="0.82"'))
o=[]
def leg(col,row,sym,txt):
    x=1512+col*272; y=y0+26+row*25
    return G(sym,f'translate({x},{y})')+T(x+56,y+4.5,txt,'nt',12.5)
L=[(line(0,0,40,0,WALL,5),'Marble / rock-cut wall'),(line(0,0,40,0,'#1fa3b8',4.5,'stroke-dasharray="11 4"'),'Sea-glass wall'),(rect(0,-7,40,14,'url(#poolGrad)',TEAL,1,3),'Pool · bath · tide-pool'),(G(column(20,0,6)),'Fluted gilt pillar'),
(line(8,8,8,-10,DGOLD,1.6)+path('M8,-10 A18,18 0 0 1 26,8','none',DGOLD,0.8,'stroke-dasharray="3 2"')+line(0,8,8,8,WALL,4)+line(26,8,40,8,WALL,4),'Door & swing'),(line(0,0,40,0,'#4a3208',3.6,'stroke-dasharray="9 6" stroke-opacity="0.55"')+line(0,0,40,0,'#f6d88a',2,'stroke-dasharray="9 6"'),'Villa overhead'),(path('M0,2 q10,-8 20,0 t20,0','none','#8a7350',1.3),'Cliff contour (5 m)'),(rect(0,-7,40,14,'#1b8098')+path('M0,2 q10,-8 20,0 t20,0','none','#bfeef4',1),'Bathymetry (metres)'),
(G(brazier(20,0,8)),'Hearth-brazier'),(star(20,0,7,6,3,CORAL,INK),'Ward seal'),(cypress(20,0,6),'Cypress'),(circ(20,0,7,'#f6d88a','none',0,'fill-opacity="0.5"')+circ(20,0,3,'#f6d88a','#8f651d',0.8),'Glow-lantern niche')]
for i,(sym,txt) in enumerate(L):
    x=1512+(i%4)*200; y=y0+26+(i//4)*25
    o.append(G(sym,f'translate({x},{y})')+T(x+50,y+4.5,txt,'nt',12.5))
o.append(line(1510,y0+90,2310,y0+90,GOLD,1))
o.append(T(1512,y0+112,'KEY TO FURNISHINGS','nb',13.5,extra='letter-spacing="1.5"'))
items=['Infinity pool & sun-deck','Divans & tide-table','Pearl table, ten seats','Compass-rose mosaic','Canopied bed (Autumn)','Hearth-brazier lounge','Sea-glass balconies','Locked map desk','Sea-silk canopy bed','Sunken bath, 3 steps','Spiral stair to cavern','Wrought-gold gate','Rack & watch cot','Hound niche','Wine & tea stores','Oculus sun-well']
for i,it in enumerate(items):
    c=i//4; r=i%4; x=1522+c*200; y=y0+136+r*21
    o.append(key(x,y,i+1)+T(x+16,y+4.5,it,'nt',12.5))
o.append(line(1510,y0+214,2310,y0+214,GOLD,1))
o.append(T(1512,y0+236,'TACTICAL & SCENE NOTES','nb',13.5,extra='letter-spacing="1.5"'))
notes=[('Single bottleneck.','One guarded causeway joins the villa to Tarquin\'s palace. Caelum\'s door commands the gate hall; no one reaches either suite unseen.'),
('Private inner corridor.','Joins the two suites behind the salon and bolts from within — no crossing the lit glass after dark, no witness on the deck.'),
('Prince\'s cover.','Sixteen metres of limestone lie between vault and villa. The sea-arch faces due west, blind to palace balconies, harbour and shore scryers.'),
('The stair.','160 rock-cut treads from Aurelie\'s lobby, barred on her side. The only other door to the cavern is the sky.'),
('Flight discipline.','Launch west over open water, climb beyond the bay mouth before turning, and come home at dusk with the sun behind him.')]
yy=y0+260
for lead,body in notes:
    s_,h=para(1512,yy,lead,body,770,13,17.5); o.append(s_); yy+=h+6
print('notes end',yy,'limit',y0+476)
p.a(G(''.join(o),extra=f'data-box="1492,{y0+2},2328,{y0+474}"'))
p.save('/home/sable/Dragonbound/art/adriata/plate01_salt_arch_villa_master.svg')
