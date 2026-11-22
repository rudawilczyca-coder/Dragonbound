from lib import *
p=P(); background(p)
frame(p,'III',"THE SUMMER PALACE — STATE WING","Principal floor at +55 m · arrival loggia, throne hall, council and audience chambers, banquet hall and the open sea-terrace",'ADRIATA & THE SUMMER COURT PALACE','Dragonbound Cartographic Suite · Plate III of IV')
MX0,MY0,MX1,MY1=70,200,1700,1530
p.d.append(f'<clipPath id="m"><rect x="{MX0}" y="{MY0}" width="{MX1-MX0}" height="{MY1-MY0}" rx="5"/></clipPath>')
p.d.append('<pattern id="shellfl" width="26" height="26" patternUnits="userSpaceOnUse"><rect width="26" height="26" fill="#f6efe0"/><circle cx="6" cy="7" r="1.6" fill="#d8c7a0"/><circle cx="19" cy="17" r="1.6" fill="#bfe0e0"/><path d="M12 22 q3 -5 6 0" fill="none" stroke="#d8c7a0" stroke-width="0.8"/><path d="M17 5 q3 -4 6 0" fill="none" stroke="#c9b993" stroke-width="0.7"/></pattern><pattern id="oak" width="14" height="80" patternUnits="userSpaceOnUse"><rect width="14" height="80" fill="#f4ecd9"/><path d="M0 0 V80 M0 40 H14" fill="none" stroke="#dccfaf" stroke-width="0.7"/></pattern><pattern id="tileWave" width="40" height="20" patternUnits="userSpaceOnUse"><rect width="40" height="20" fill="#f3f8f6"/><path d="M0 10 q10 -9 20 0 t20 0" fill="none" stroke="#a8d6d8" stroke-width="0.9"/><path d="M0 20 q10 -9 20 0 t20 0" fill="none" stroke="#cfe6e4" stroke-width="0.7"/></pattern>')
p.a(panel_head(72,186,'I','STATE WING — PRINCIPAL FLOOR PLAN',1626))
o=[rect(MX0,MY0,MX1-MX0,MY1-MY0,'#efe6d0')]
# sea west
o.append(path('M70,200 H250 Q300,360 250,520 Q210,830 250,1140 Q300,1300 250,1530 H70 Z','url(#seaGradH)'))
o.append(path('M70,200 H250 Q300,360 250,520 Q210,830 250,1140 Q300,1300 250,1530 H70 Z','url(#waves)'))
o.append(path('M250,200 Q300,360 250,520 Q210,830 250,1140 Q300,1300 250,1530','none','#6b5a44',1.6))
for i in range(40):
    t=i/39; y=210+t*1310
    x=250+ (50*math.sin(math.pi*min(1,(y-200)/320)) if y<520 else (-40*math.sin(math.pi*(y-520)/620) if y<1140 else 50*math.sin(math.pi*(y-1140)/390)))
    if 500<y<1160: continue
    o.append(line(x+3,y,x+22,y+2,'#6b5a44',1,'stroke-opacity="0.7"'))
# garden courts N and S, court E
o.append(rect(300,205,1050,96,'url(#grass)')); o.append(rect(300,1350,1050,176,'url(#grass)'))
o.append(rect(1340,205,360,315,'url(#grass)')+rect(1340,1140,360,390,'url(#grass)'))
for x in range(330,1340,60):
    o.append(tree(x+10,232,11,'#6f9a5a','#3f6a40','#f2b63a'))
for x in range(330,1340,60):
    o.append(tree(x+10,1492,11,'#6f9a5a','#3f6a40','#f2b63a'))
for (x,y) in [(1380,240),(1440,240),(1500,240),(1560,240),(1620,240),(1670,240),(1670,300),(1670,360),(1670,420),(1670,480),(1380,1490),(1440,1490),(1500,1490),(1560,1490),(1620,1490),(1670,1490),(1670,1430),(1670,1370),(1670,1310),(1670,1250),(1670,1190)]:
    o.append(cypress(x,y,8))
# ---- floors ----
def fl(x,y,w,h,f): return rect(x,y,w,h,f)
TER='M330,520 C40,560 40,1100 330,1140 Z'
TER2='M330,490 C-10,540 -10,1120 330,1170 Z'
o.append(path(TER2,'#d9ccb2','#6b5a44',1.4)); 
o.append(path('M330,505 C15,550 15,1110 330,1155','none','#6b5a44',0.8)); 
o.append(path(TER,'url(#tileScale)',WALL,2))
o.append(fl(330,340,1010,60,'url(#shellfl)')+fl(330,1250,1010,60,'url(#shellfl)'))
for cx in [480,805,1130]:
    o.append(path(f'M{cx-50},341 A50,42 0 0 1 {cx+50},341 Z','url(#shellfl)')+path(f'M{cx-50},340 A50,42 0 0 1 {cx+50},340','none',WALL,3)+path(f'M{cx-50},1309 A50,42 0 0 0 {cx+50},1309 Z','url(#shellfl)')+path(f'M{cx-50},1310 A50,42 0 0 0 {cx+50},1310','none',WALL,3))
o.append(fl(330,400,230,210,'url(#oak)')+fl(560,400,80,210,'url(#tileSmall)')+fl(640,400,60,850,'url(#tileHerr)')+fl(700,400,300,210,'url(#tileHerrB)')+fl(1000,400,100,210,'url(#tileSq)')+fl(1100,400,120,210,'url(#tileSq)'))
o.append(fl(330,610,310,440,'url(#tileDiamond)')+fl(700,610,400,440,'url(#tileWave)')+fl(1100,610,120,440,'url(#shellfl)'))
o.append(fl(330,1050,310,200,'url(#tileHerr)')+fl(700,1050,400,200,'url(#tileDiamond)')+fl(1100,1050,120,200,'url(#tileSq)'))
o.append(fl(1220,400,120,850,'url(#tileScale)'))
o.append(fl(1340,520,340,620,'url(#gravel)')+rect(1340,520,340,620,'none',WALL,1.6))
p.a(G(''.join(o),extra='clip-path="url(#m)"'))
o=[]
# ---- arrival court ----
o.append(Fg(circ(1505,830,104,'#f7efe0',WALL,1.6)+circ(1505,830,96,'none',GOLD,1.2)+circ(1505,830,70,'#eef6f4',TEAL,0.8)))
m=[]
for i in range(32):
    a=math.pi*i/16
    m.append(f'<polygon points="{1505+30*math.cos(a-0.07):.1f},{830+30*math.sin(a-0.07):.1f} {1505+68*math.cos(a):.1f},{830+68*math.sin(a):.1f} {1505+30*math.cos(a+0.07):.1f},{830+30*math.sin(a+0.07):.1f}" fill="{"#1d879e" if i%2 else GOLD}" fill-opacity="0.7"/>')
o.append(''.join(m)+star(1505,830,28,8,10,GOLD,DGOLD))
o.append(fountain(1420,600,26)+fountain(1420,1060,26))
o.append(rect(1342,792,60,76,'url(#tileSq)',GOLD,1)+rect(1608,792,42,76,'url(#tileSq)',GOLD,1))
for (hx,hy) in [(1400,300),(1490,300),(1580,300),(1400,400),(1490,400),(1580,400)]: o.append(rect(hx,hy,62,62,'url(#hedge)','#3f6a40',1,4)+rect(hx+10,hy+10,42,42,'#e6ddc4','#3f6a40',0.6,3)+tree(hx+31,hy+31,10,'#6f9a5a','#3f6a40','#f2b63a'))
o.append(ship(150,1230,44,-70))
o.append(stairs(1650,720,30,220,6,'e'))
for y in [545,1115]:
    for x in [1375,1470,1565,1650]: o.append(Fg(circ(x,y,9,'#e9c877',WALL,0.9)+tree(x,y,6.5,'#6f9a5a','#3f6a40','#f2b63a')))
# ---- mosaics / carpets ----
TC=(900,830)
o.append(rect(770,812,330,36,'#b5482f','none',0,0,'fill-opacity="0.16"')+line(770,812,1100,812,GOLD,1)+line(770,848,1100,848,GOLD,1))
m=[circ(900,830,84,'#f4f8f6',TEAL,1.4),circ(900,830,78,'none',GOLD,1.2),circ(900,830,56,'#dff1f1',TEAL,0.8)]
for i in range(24):
    a=math.pi*i/12; m.append(line(900+56*math.cos(a),830+56*math.sin(a),900+78*math.cos(a),830+78*math.sin(a),TEAL,0.6))
m.append(star(900,830,72,16,30,'#2a8fa3','#144a5c')); m.append(star(900,830,48,8,16,GOLD,INK)); m.append(circ(900,830,14,'#fbf6ec',GOLD,1.2)); m.append(shell(900,830,9))
o.append(''.join(m))
# chandeliers (overhead)
for (x,y,r) in [(900,830,97),(485,830,60),(445,505,46)]:
    o.append(circ(x,y,r,'none','#1fa3b8',1,'stroke-dasharray="2 5"'))
# runnels
RUN='#7fdbe4'
o.append(''.join(rect(x,y,w,9,RUN,TEAL,0.8,4) for y in (628,1023) for x,w in ((720,135),(945,135))))
o.append(rect(1112,640,9,120,RUN,TEAL,0.8,4)+rect(1112,900,9,120,RUN,TEAL,0.8,4)+rect(1199,640,9,120,RUN,TEAL,0.8,4)+rect(1199,900,9,120,RUN,TEAL,0.8,4))
o.append(fountain(1160,680,22)+fountain(1160,980,22))
# ---- walls ----
W=[]
W.append(wall_h(400,330,1220,[(430,462),(655,685),(780,812)]))
W.append(wall_h(610,330,640,[(345,385),(584,616)])); W.append(wall_h(610,700,1220,[(875,925),(1146,1178)]))
W.append(wall_h(1050,330,640,[(460,510)])); W.append(wall_h(1050,700,1220,[(875,925),(1146,1178)]))
W.append(wall_h(1250,330,1220,[(468,500),(655,685),(880,920)]))
W.append(wall_v(560,400,610)); W.append(wall_v(640,400,1250,[(796,864),(1130,1162)]))
W.append(wall_v(700,400,1250,[(655,695),(965,1005)])); W.append(wall_v(1000,400,610,[(436,468)]))
W.append(wall_v(1100,400,1250,[(790,870)])); W.append(wall_v(1220,400,1250,[(488,520),(790,870)]))
W.append(wall_v(330,1050,1050.1)); 
o.append(''.join(W))
GL='stroke-dasharray="11 4"'
o.append(line(330,400,330,610,'#1fa3b8',5,GL)+line(330,1050,330,1250,'#1fa3b8',5,GL))
# sea-glass doors
o.append(line(1220,790,1220,870,'#1fa3b8',6)+line(1220,830,1220,830.1,WALL,1)+circ(1220,790,4,GOLD,WALL,0.8)+circ(1220,870,4,GOLD,WALL,0.8)+circ(1220,830,3,GOLD,WALL,0.8))
o.append(path('M1220,790 A40,40 0 0 1 1260,830 A40,40 0 0 1 1220,870','none','#1fa3b8',0.9,'stroke-dasharray="3 2"'))
for (x,y1,y2) in [(1100,790,870),(640,796,864)]: o.append(line(x,y1,x,y2,GOLD,1.8,'stroke-dasharray="2 3"'))
# doors
o.append(door_h(430,462,400,-1,'r')+door_h(780,812,400,-1,'l')+door_h(345,385,610,-1,'l')+door_h(584,616,610,1,'r')+door_h(875,925,610,1,'l')+door_h(1146,1178,610,-1,'l'))
o.append(door_h(460,510,1050,1,'l')+door_h(875,925,1050,-1,'r')+door_h(1146,1178,1050,-1,'l')+door_h(468,500,1250,-1,'l')+door_h(880,920,1250,-1,'r'))
o.append(door_v(1130,1162,640,-1,'t')+door_v(655,695,700,1,'b')+door_v(965,1005,700,1,'t')+door_v(436,468,1000,-1,'t')+door_v(488,520,1220,1,'t'))
o.append(star(1196,1064,7,6,3,CORAL,INK))
for (x,y) in [(712,412),(986,414),(712,598),(988,598)]: o.append(star(x,y,6,6,2.6,'#2a8fa3',INK))
# ---- columns ----
for x in range(355,1340,50):
    if any(abs(x-c)<30 for c in [480,805,1130]): continue
    o.append(column(x,340,6)); o.append(column(x,1310,6))
for cx in [480,805,1130]:
    o.append(Fg(path(f'M{cx-36},332 A36,28 0 0 1 {cx+36},332','none','#b89868',6)))
    o.append(Fg(path(f'M{cx-36},1318 A36,28 0 0 0 {cx+36},1318','none','#b89868',6)))
for y in range(425,1250,50):
    if 760<y<900: 
        continue
    o.append(column(1340,y,7))
for y in range(450,1250,100):
    if 780<y<880: continue
    o.append(column(1265,y,6))
o.append(column(1340,790,8)+column(1340,870,8))
for y in range(656,1030,46): o.append(column(330,y,7))
for i in range(12):
    a=math.radians(15+30*i)
    if abs(math.sin(a))<0.3: continue
    o.append(column(900+150*math.cos(a),830+150*math.sin(a),7.5))
for y in [440,560,720,940,1090,1210]:
    o.append(column(652,y,5)); o.append(Fg(line(696,y-26,696,y+26,CORAL,4)))
# ---- furniture ----
# dais & thrones
d=''.join(path(f'M703,{830-r} A{r},{r} 0 0 1 703,{830+r} Z',c,WALL,1) for r,c in [(84,'#efe6d2'),(68,'#f7f1e2'),(52,'#fffaf0')])
o.append(Fg(d))
o.append(Fg(rect(708,815,26,30,'url(#goldGrad)',WALL,1.2,4)+rect(705,812,8,36,'#1d879e',WALL,0.8,2)+shell(722,830,7,90)))
o.append(Fg(rect(712,772,18,20,'#e9c877',WALL,0.9,3))+Fg(rect(712,868,18,20,'#e9c877',WALL,0.9,3)))
for (x,y) in [(1060,650),(1060,1010)]: o.append(brazier(x,y,10))
# banquet hall tables
for x in [392,472,552]: o.append(table_long(x,690,26,290,11))
o.append(Fg(rect(530,1012,96,26,'#d9c79e',WALL,1)+''.join(line(530+i*24,1012,530+i*24,1038,WALL,0.5) for i in range(1,4))))
# terrace: high table
o.append(table_long(196,700,30,260,9))
o.append(Fg(G(rect(-5.5,-5.5,11,11,CORAL,WALL,1,2)+rect(-5.5,-8,11,3.5,'#7a2618',WALL,0.5,1),'translate(235,801.1) rotate(90)')+rect(-4.5,-4.5,9,9,'#e9c877',INK,1.1,0,'transform="translate(251,818) rotate(45)"')))
for (x,y) in [(164,690),(164,972),(285,585),(285,1075)]: o.append(brazier(x,y,10))
for (x,y) in [(140,760),(140,900)]: o.append(Fg(circ(x,y,9,'#e9c877',WALL,0.9)+tree(x,y,6.5,'#6f9a5a','#3f6a40','#f2b63a')))
# dining room: pearl table
o.append(Fg(rect(365,478,150,54,'#fdfbf5',WALL,1.3,27)+rect(370,483,140,44,'none','#bfe0e0',1.4,22)+''.join(chair(385+i*27.5,468,9,0)+chair(385+i*27.5,542,9,180) for i in range(5))+chair(355,505,9,-90)+chair(525,505,9,90)))
o.append(Fg(rect(410,588,120,12,'#d9c79e',WALL,0.9,2))+Fg(rect(538,420,14,120,'#d9c79e',WALL,0.9,2)))
# buttery
o.append(Fg(rect(583,410,34,50,'#7a4a3a',WALL,0.9)+''.join(circ(591+j*9,418+i*9,3,'#3a1f1a') for i in range(5) for j in range(3))))
o.append(Fg(rect(596,540,38,18,'#d9c79e',WALL,0.9,2)+circ(606,549,3.5,'#e9c877',WALL,0.5)+circ(616,549,3.5,'#e9c877',WALL,0.5)+circ(626,549,3.5,'#e9c877',WALL,0.5)))
# council
o.append(Fg(f'<ellipse cx="850" cy="505" rx="92" ry="40" fill="#c9a871" stroke="{WALL}" stroke-width="1.3"/><ellipse cx="850" cy="505" rx="80" ry="30" fill="#f6ecd0" stroke="{DGOLD}" stroke-width="0.8"/>'+path('M790,512 q20,-22 44,-8 t40,-6 t34,10','none',TEAL,0.9)+''.join(chair(850+105*math.cos(math.radians(a)),505+52*math.sin(math.radians(a)),9,a+90) for a in [0,36,72,108,144,180,216,252,288,324])))
o.append(brazier(960,570,9))
# scribes
o.append(Fg(rect(1010,410,80,14,'#b89868',WALL,0.8)+''.join(line(1010+i*10,410,1010+i*10,424,WALL,0.5) for i in range(1,8))))
o.append(Fg(rect(1040,440,44,24,'#d9c79e',WALL,0.9,2)+chair(1062,474,9,180))+Fg(rect(1040,548,44,24,'#d9c79e',WALL,0.9,2)+chair(1062,538,9,0)))
# steward
o.append(Fg(rect(1110,410,100,14,'#b89868',WALL,0.8)+''.join(line(1110+i*10,410,1110+i*10,424,WALL,0.5) for i in range(1,10))))
o.append(Fg(rect(1125,452,66,30,'#c9a871',WALL,1,2)+rect(1132,457,34,20,'#f6ecd0',DGOLD,0.6)+chair(1158,439,9,0)+chair(1146,493,8,180)+chair(1170,493,8,180)))
# withdrawing room
o.append(divan(350,1070,74,22)+divan(350,1128,74,22,180)+Fg(circ(387,1110,9,'#f7f3ea',WALL,0.9)))
o.append(divan(545,1168,74,22,90))
o.append(table_round(575,1098,13,4))
o.append(Fg(line(440,1062,440,1120,'#8a6a3a',3,'stroke-dasharray="14 3"')))
# lesser hall
o.append(Fg(rect(706,1090,52,120,'#efe6d2',WALL,1)+rect(706,1104,40,92,'#f7f1e2',WALL,0.8)+rect(712,1135,24,30,'url(#goldGrad)',WALL,1.1,4)))
o.append(Fg(rect(770,1062,90,10,'#d9c79e',WALL,0.8,2))+Fg(rect(940,1062,140,10,'#d9c79e',WALL,0.8,2))+Fg(rect(940,1230,150,10,'#d9c79e',WALL,0.8,2))+Fg(rect(770,1230,90,10,'#d9c79e',WALL,0.8,2)))
o.append(Fg(rect(1030,1120,34,70,'#c9a871',WALL,1,2)+chair(1076,1140,9,90)+chair(1076,1170,9,90)))
o.append(Fg(circ(840,1150,15,'none',GOLD,1.6)+circ(840,1150,10,'none',CORAL,1.2,'stroke-dasharray="2 2"')+star(840,1150,6,4,2,CORAL,INK)))
# treasury stair
o.append(spiral(1160,1160,36,14))
# loggia benches & urns
for y in [580,670,1010,1100,1190]: o.append(Fg(rect(1228,y-20,10,40,'#d9c79e',WALL,0.8,2)))
for y in [770,890]: o.append(Fg(circ(1290,y,10,'#e9c877',WALL,0.9)+tree(1290,y,7,'#6f9a5a','#3f6a40','#f2b63a')))
# passage statue niches
# ---- labels ----
o.append(T(900,713,'THRONE HALL','rl',18,extra='letter-spacing="2"')+T(900,729,'domed rotunda','rs',12))
o.append(T(900,936,'freshwater runnels','rs')+T(900,952,'along both walls','rs'))
o.append(T(472,638,'GRAND BANQUET HALL','rl',15))
o.append(T(252,616,'OPEN','rl',15,extra='letter-spacing="1"')+T(252,635,'SEA-TERRACE','rl',15,extra='letter-spacing="1"')+T(252,654,'high table at banquets','rs'))
o.append(T(250,1008,'balustrade · fire-bowls','rs')+T(250,1024,'tide-steps below','rs'))
o.append(T(432,427,'VAULTED DINING ROOM','rl',13.5)+T(470,572,'white oak · green glass','rs',12))
o.append(T(600,490,'BUTTERY','rl',11)+T(600,506,"cupbearers'",'rs',11)+T(600,520,'pass','rs',11))
o.append(T(850,432,'COUNCIL CHAMBER','rl',14.5)+T(850,584,'chart-table · four sea-wards','rs'))
o.append(T(1050,502,"SCRIBES'",'rl',12)+T(1050,517,'CABINET','rl',12))
o.append(T(1160,530,'HARBOUR-','rl',12)+T(1160,545,"STEWARD'S",'rl',12)+T(1160,560,'OFFICE','rl',12))
o.append(T(1160,812,'SHELL','rl',13.5)+T(1160,829,'VESTIBULE','rl',13.5)+T(1160,846,'fountains','rs',12))
o.append(T(925,1100,'LESSER HALL','rl',16,extra='letter-spacing="1.5"')+T(925,1119,'audience chamber · day-court','rs'))
o.append(T(1160,1088,'VAULT STAIR','rl',12)+T(1160,1103,'palm-sealed','rs',11.5))
o.append(T(470,1148,'CORAL','rl',13.5)+T(470,1165,'WITHDRAWING','rl',13.5)+T(470,1182,'ROOM','rl',13.5))
o.append(f'<text x="670" y="830" transform="rotate(-90 670 830)" dy="4" class="rl" font-size="12.5" letter-spacing="2">TAPESTRY PASSAGE</text>')
o.append(f'<text x="1296" y="590" transform="rotate(-90 1296 590)" dy="4" class="rl" font-size="14" letter-spacing="3">GRAND ARRIVAL LOGGIA</text>')
o.append(f'<text x="1296" y="1080" transform="rotate(-90 1296 1080)" dy="4" class="rs" font-size="12">shell-flecked paving</text>')
o.append(T(640,374,'NORTH COLONNADE','rl',13.5,extra='letter-spacing="3"')+T(960,374,'three conversation exedrae','rs'))
o.append(T(640,1284,'SOUTH COLONNADE','rl',13.5,extra='letter-spacing="3"')+T(980,1284,'opens on the gardens','rs'))
o.append(T(1505,688,'ARRIVAL COURT','rl',15,extra='letter-spacing="2"')+T(1505,972,'LANDING PLATFORM','rl',13)+T(1505,989,'winnowing point','rs'))
o.append(T(1560,1100,'stair down to the city →','rs',12))
o.append(T(820,272,'FOUNTAIN COURT · to the back wing, unroofed since Amarantha ↑','rl',13,extra='style="stroke:#d5e0b6"'))
o.append(T(820,1392,'↓ to the Guest Wing, terraced gardens and the Tide Stair · Plate IV','rl',13,extra='style="stroke:#d5e0b6"'))
HS='style="paint-order:stroke;stroke:#0e566d;stroke-width:3.5px;stroke-linejoin:round"'
o.append(T(160,246,'MOUTH OF','sea',17,extra='letter-spacing="3" '+HS)+T(160,270,'THE BAY','sea',17,extra='letter-spacing="3" '+HS)+T(160,292,'17 m below the terrace','sea',12.5,extra=HS))
o.append(T(168,1330,'to the Salt-Arch Villa','sea',13,extra=HS)+T(168,1348,'by the cliff causeway','sea',13,extra=HS)+T(168,1366,'(north-west, Plate I)','sea',12.5,extra=HS))
# keys
KEYS=[(1505,790,1),(1260,830,2),(1160,745,3),(722,800,4),(748,752,5),(1000,650,6),(671,640,7),(850,468,8),(1160,1120,9),(840,1182,10),(730,1118,11),(440,505,12),(600,582,13),(436,735,14),(160,830,15),(272,796,16),(480,304,17),(540,1085,18),(578,1025,19),(94,830,20)]
for x,y,n in KEYS: o.append(key(x,y,n))
p.a(G(''.join(o),extra='data-box="74,204,1696,1526"'))
p.a(compass(160,410,46))
p.a(G(rect(1392,1392,256,60,'#fbf6ec',TEAL,1,4,'fill-opacity="0.92"')+scalebar(1412,1417,8,(0,5,10,20))))
p.a(rect(MX0,MY0,MX1-MX0,MY1-MY0,'none',TEAL,2,5))
# ---------- sidebar ----------
SX=1742; SW=588
p.a(panel_head(SX,186,'II','KEY TO THE STATE WING',SW))
p.a(rect(SX-2,200,SW+2,566,'#fdfaf3',TEAL,2,5,'fill-opacity="0.82"'))
GZ=[('Landing platform — guests arrive here','canon'),('The pair of sea-glass doors','canon'),('Shell-flecked walls, freshwater fountains','canon'),("Tarquin's throne on a three-step dais",'⚑'),("Seats of Cresseida and Varian",'⚑'),('Sea-glass chandelier, gilt column ring','canon'),('Tapestried pillar niches — unlit','⚑'),('Chart-table; sea-wards seal the doors','⚑'),('Vault stair — opens to the High Lord\'s palm','canon'),('Presentation mark before the low dais','⚑'),("High Lord's chair, lesser hall",'⚑'),('Mother-of-pearl table, wide sea windows','canon'),("Cupbearers' pass — wine comes this way",'⚑'),('Long tables, eleven a side','⚑'),('High table on the terrace','⚑'),("Guest of honour's chair & cupbearer's post",'⚑'),('Conversation exedra (six in all)','⚑'),('Screened divans, garden door','⚑'),('Minstrels\' bench','⚑'),('Tide-steps — the lowest wets at spring tide','⚑')]
o=[]
for i,(t,tag) in enumerate(GZ):
    y=228+i*26.5
    col={'canon':TEAL,'⚑':CORAL}.get(tag,DGOLD)
    o.append(key(SX+22,y,i+1)+T(SX+42,y+4.5,t,'nt',13.5)+T(SX+SW-18,y+4.5,tag,'nb',12,'end',f'style="fill:{col};font-style:italic"'))
    o.append(line(SX+42,y+13,SX+SW-18,y+13,'#d9cdb4',0.6))
o.append(T(SX+SW/2,759,'canon = from the books   ·   ⚑ = devised for this table','sub',12,'middle'))
p.a(G(''.join(o),extra=f'data-box="{SX},202,{SX+SW},766"'))
y0=812
p.a(panel_head(SX,y0-14,'III','LEGEND',SW))
p.a(rect(SX-2,y0,SW+2,146,'#fdfaf3',TEAL,2,5,'fill-opacity="0.82"'))
L=[(line(0,0,40,0,WALL,5),'Coral-stone wall'),(line(0,0,40,0,'#1fa3b8',4.5,'stroke-dasharray="11 4"'),'Sea-glass window wall'),
(G(column(20,0,6)),'Gilt-capped column'),(rect(0,-4.5,40,9,'#7fdbe4',TEAL,0.8,4),'Freshwater runnel · fountain'),
(line(8,8,8,-10,DGOLD,1.6)+path('M8,-10 A18,18 0 0 1 26,8','none',DGOLD,0.8,'stroke-dasharray="3 2"')+line(0,8,8,8,WALL,4)+line(26,8,40,8,WALL,4),'Door & swing'),(circ(20,0,9,'none','#1fa3b8',1.2,'stroke-dasharray="2 4"'),'Sea-glass chandelier above'),
(line(20,-9,20,9,CORAL,4),'Hanging tapestry'),(star(12,0,7,6,3,CORAL,INK)+star(30,0,7,6,3,'#2a8fa3',INK),'Palm-seal · sea-ward sigil'),
(G(brazier(20,0,8)),'Fire-bowl / brazier'),(G(circ(20,0,8,'#e9c877',WALL,0.9)+tree(20,0,6,'#6f9a5a','#3f6a40','#f2b63a')),'Lemon tree in gilt shell urn')]
o=[]
for i,(sym,txt) in enumerate(L):
    x=SX+18+(i%2)*290; y=y0+24+(i//2)*25.5
    o.append(G(sym,f'translate({x},{y})')+T(x+50,y+4.5,txt,'nt',13))
p.a(''.join(o))
y1=1004
p.a(panel_head(SX,y1-14,'IV','COURT-CRAFT: WHO SEES WHAT',SW))
p.a(rect(SX-2,y1,SW+2,526,'#fdfaf3',TEAL,2,5,'fill-opacity="0.82"'))
notes=[('The processional axis.','Landing platform, sea-glass doors, vestibule, fifty metres of carpet to the dais. Everyone in the hall watches a guest walk it.'),
('Two halls, two registers.','The Throne Hall is for the whole court. The Lesser Hall is where Tarquin does his real business, with stewards and a dozen courtiers, and where an attendant is presented.'),
('The council chamber.','One door from the throne hall, one to the colonnade. With the four sea-wards raised nothing said at the chart-table carries past the walls.'),
('Dark corners.','The Tapestry Passage runs the full depth of the wing between hall and banquet, six pillar niches behind the hangings and no lamps. The exedrae of both colonnades hide a seated pair from the walk.'),
('The cupbearer\'s road.','Buttery, banquet hall, arcade, terrace: seventy metres carried in full view, and a post at the right elbow of the guest of honour.'),
('The view.','The high table and the dining room both face the mouth of the bay — green and cobalt and midnight. Nothing on the terrace is hidden from the hall arcade.'),
('Ways out.','South colonnade to the gardens and the Tide Stair; north colonnade toward the cliff causeway and the villa.')]
o=[]; yy=y1+30
for lead,body in notes:
    s_,h=para(SX+16,yy,lead,body,SW-40,13.5,18.5); o.append(s_); yy+=h+16
print('notes end',yy,'limit',y1+526)
p.a(G(''.join(o),extra=f'data-box="{SX},{y1+2},{SX+SW},{y1+524}"'))
p.save('/home/sable/Dragonbound/art/adriata/plate03_summer_palace_state_wing.svg')
