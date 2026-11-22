s=open('plate1.py').read()
def R(a,b,cnt=1):
    global s
    assert s.count(a)>=1,('MISSING',a[:60])
    s=s.replace(a,b) if cnt==0 else s.replace(a,b,cnt)
# stair lobby
R("W.append(wall_v(900,675,885,[(712,742),(818,848)]))","W.append(wall_v(900,675,885,[(746,774),(818,848)]))")
R("door_v(712,742,900,1,'t')","door_v(746,774,900,1,'b')")
R("o.append(spiral(985,728,32,16))","o.append(spiral(1012,728,30,16))\no.append(T(941,700,'STAIR','rl',12)+T(941,715,'to cavern ↓','rs',11))")
i=s.index("p.d.append('<path id=\"ring1\""); j=s.index("b=rect(922,797"); s=s[:i]+s[j:]
R("b=rect(922,797,118,72,'#f4eee0',WALL,1.2,16)+rect(930,805,102,56,'#cfeef1',TEAL,0.8,13)+rect(938,813,86,40,'#9fdde5',TEAL,0.8,10)+rect(946,821,70,24,'url(#poolGrad)',TEAL,0.8,8)","b=rect(922,804,118,66,'#f4eee0',WALL,1.2,16)+rect(930,811,102,52,'#cfeef1',TEAL,0.8,13)+rect(938,818,86,38,'#9fdde5',TEAL,0.8,10)+rect(946,825,70,24,'url(#poolGrad)',TEAL,0.8,8)")
R("+brazier(1046,790,6))","+T(981,797,'SUNKEN BATH','rl',10.5))")
R("(981,833,10),(1044,692,11),(1262,512,12),(1196,416,13)","(981,837,10),(950,736,11),(1272,506,12),(1186,374,13)")
R("(866,300,6),(487,345,7),(487,780,7)","(800,259,6),(446,300,7),(446,826,7)")
R("ML(690,420,[\"ERIS'S MASTER SUITE\"],'rl',extra='style=\"fill:#7a2618\"')+T(690,437,","ML(690,415,[\"ERIS'S MASTER SUITE\"],'rl',extra='style=\"fill:#7a2618\"')+T(690,432,")
R("'guarded · to palace +55 m →','rs',11.5","'guarded · to the palace →','rs',11.5")
R("(1415,660),(1404,715),(1421,770)","(1415,640),(1421,770)")
R("""o.append(f'<text x="{pts[14][0]+5:.0f}" y="917" font-family="Noto Sans" font-style="italic" font-size="10.5" fill="#c9f1f6">{lab}</text>')""","""o.append(f'<text x="{pts[12][0]+5:.0f}" y="792" font-family="Noto Sans" font-style="italic" font-size="12" fill="#e3f8fb">{lab} m</text>')""")
R("o.append(T(pts[1][0],216,lab,'dim',10.5,extra='style=\"fill:#6b5230;stroke:#dccfb6\"'))","o.append(T(pts[1][0]+2,218,lab,'dim',12.5,extra='style=\"fill:#4a3716;stroke:#e6dac2;font-weight:700\"'))")
# panel II
R("o.append(path('M590,1100 L740,1092 Q770,1262 738,1430 L590,1424 Z'","o.append(path('M590,1100 L735,1090 Q768,1262 735,1434 L590,1424 Z'")
R("o.append(line(570,1300,150,1300,'#f6d88a',2.6,'stroke-dasharray=\"14 7\"')+'<polygon points=\"128,1300 154,1290 154,1310\" fill=\"#f6d88a\"/>')","o.append(line(570,1262,150,1262,'#f6d88a',2.6,'stroke-dasharray=\"14 7\"')+'<polygon points=\"126,1262 154,1251 154,1273\" fill=\"#f6d88a\"/>')")
R("(1150,1350,7),(900,1340,6),(790,1330,5)]","(1150,1350,7),(915,1345,6)]")
R("(760,1400,9)","(700,1392,8)")
R("o.append(path(fp,'none','#f2d084',2,'stroke-dasharray=\"9 6\" stroke-opacity=\"0.95\"'))","o.append(path(fp,'none','#4a3208',3.6,'stroke-dasharray=\"9 6\" stroke-opacity=\"0.55\"')+path(fp,'none','#f6d88a',2,'stroke-dasharray=\"9 6\"'))")
R("o.append(T(850,1157,'TIDAL SALT-POOL','rll',12.5)+T(850,1174,'blow-hole fed','rsl',11.5))","o.append(T(850,1157,'TIDAL POOL','rll',13)+T(850,1175,'salt · blow-hole fed','rsl',12))")
R("o.append(T(858,1250,\"PRINCE'S VAULTED AERIE\",'rll',16)+T(858,1270,'36 m deep × 24 m wide × 16 m vault','rsl')+T(858,1287,'hidden from every palace sightline','rsl'))","o.append(T(850,1252,\"PRINCE'S VAULTED AERIE\",'rll',16)+T(850,1272,'36 × 24 m · 16 m vault','rsl',12.5)+T(850,1289,'blind to every palace sightline','rsl',12.5))")
R("o.append(T(1078,1372,'dry sea-sand bed','rsl',11.5))","o.append(T(1078,1337,'sand bed','rs',12,extra='style=\"stroke:#ecdcb6;font-weight:700\"'))")
R("o.append(T(842,1402,'STAIR LANDING','rll',12.5)+T(842,1419,\"from Aurelie's lobby · 160 treads\",'rsl',11.5))","o.append(T(822,1404,'STAIR LANDING','rll',13)+T(822,1421,\"from Aurelie's lobby\",'rsl',12))")
R("o.append(T(200,1228,'OPEN FLIGHT','sea',17,extra='letter-spacing=\"4\"')+T(200,1252,'CORRIDOR','sea',17,extra='letter-spacing=\"4\"')+T(200,1274,'launch due west over open water;','sea',12)+T(200,1326,'no palace roof, quay or scryer-post','sea',12)+T(200,1342,'has a line on the arch','sea',12))",
"o.append(T(205,1206,'OPEN FLIGHT','sea',18,extra='letter-spacing=\"4\" '+HALO_SEA)+T(205,1231,'CORRIDOR','sea',18,extra='letter-spacing=\"4\" '+HALO_SEA)+T(205,1295,'launch due west over open water;','sea',13,extra=HALO_SEA)+T(205,1313,'no palace roof, quay or scryer-post','sea',13,extra=HALO_SEA)+T(205,1331,'has a line on the arch','sea',13,extra=HALO_SEA))")
R("o.append(T(1236,1054,'villa footprint overhead (+38 m)','rs',12,'start',extra='style=\"stroke:#e0d3ba;font-style:italic\"'))","o.append(T(1236,1054,'villa footprint overhead','rs',12.5,'start',extra='style=\"stroke:#e6dac2;font-weight:700;fill:#4a3716\"')+T(1236,1070,'(+38 m, dashed)','rs',12,'start',extra='style=\"stroke:#e6dac2;fill:#4a3716\"'))")
R("o.append(T(1300,1300,'SOLID LIMESTONE','rl',13.5,extra='style=\"stroke:#e0d3ba\"')+T(1300,1317,'16 m of rock between vault and villa','rs',extra='style=\"stroke:#e0d3ba\"'))","o.append(T(1322,1180,'SOLID LIMESTONE','rl',14,extra='style=\"stroke:#e6dac2\"')+T(1322,1198,'16 m of rock between','rs',12.5,extra='style=\"stroke:#e6dac2\"')+T(1322,1214,'vault crown and villa floor','rs',12.5,extra='style=\"stroke:#e6dac2\"'))\no.append(LOC)")
# locator inset
R("# =================== PANEL II ===================","""# locator
isl=[(40,60),(70,30),(120,22),(160,40),(178,80),(165,120),(120,138),(70,130),(38,100)]
LOC=G(rect(0,0,200,170,'#fdfaf3',TEAL,1.4,4)+rect(4,4,192,162,'url(#seaGradH)','none',0,3)+path('M4,4 H196 V30 Q150,22 120,10 Q60,16 4,34 Z','#d9c9a8','#6b5a44',0.8)+path('M4,166 H196 V140 Q150,150 110,158 Q50,156 4,142 Z','#d9c9a8','#6b5a44',0.8)+path('M196,30 Q176,80 196,140 Z','#d9c9a8','#6b5a44',0.8)+path(smooth(isl,True),'#e6d9bd','#6b5a44',1)+rect(66,62,44,30,'#fff',WALL,1)+path('M40,70 L4,56 L4,108 L40,92 Z','#f6d88a','none',0,'fill-opacity="0.35"')+circ(44,82,5,CORAL,'#fff',1.2)+T(100,160,'KEY PLAN · see Plate II','rsl',11)+T(88,81,'palace','rs',10)+T(52,112,'villa','rll',11,'start')+T(150,96,'city','rs',10),'translate(1228,1330)',extra='data-box="1228,1330,1428,1500"')
# =================== PANEL II ===================""")
# panel III
R("o.append(path(f'M2052,{FL-7} q10,-18 34,-16 q26,2 36,14 q10,2 18,9 l-90,0 Z','#fbfbf6','#14232b',1)+line(2056,FL-12,2050,FL-20,'#e2b24a',1.6))","")
R("o.append(path(f'M1782,{FL-40} Q1690,{FL-42} 1580,{FL-128}','none',GOLD,2.6,'stroke-dasharray=\"9 5\"'))\no.append(dragon_fly(1548,FL-150,0.8,-18))","o.append(path(f'M1782,{FL-40} Q1700,{FL-44} 1622,{FL-84}','none',GOLD,2.6,'stroke-dasharray=\"9 5\"'))\no.append(dragon_fly(1585,FL-92,0.8,-14))\no.append(line(2140,PY-16,1492,Y(55)-16+48,CORAL,1.3,'stroke-dasharray=\"3 5\"'))")
R("(0,'0 m · sea'),(6,'+6 m · cavern floor'),(22,'+22 m · vault crown'),(38,'+38 m · villa deck'),(55,'+55 m · palace terrace')","(0,'0 m · sea'),(6,'+6 m · cavern'),(22,'+22 m · vault'),(38,'+38 m · villa'),(55,'+55 m · palace')")
R("T(1529,Y(m)+4,l,'el')","T(1529,Y(m)-5,l,'el')")
R("o.append(rect(1586,VC-48,196,25,PARCH,TEAL,1.2,4,'fill-opacity=\"0.95\"')+T(1684,VC-30.5,'SALT-ARCH VILLA · +38 m','rl',12.5))","o.append(line(1700,VC-22,1716,VC-8,TEAL,1.1)+rect(1574,VC-50,222,28,PARCH,TEAL,1.2,4,'fill-opacity=\"0.95\"')+T(1685,VC-31,'SALT-ARCH VILLA · +38 m','rl',13))\no.append(T(1640,Y(55)+12,'palace sightline — all below is blind ground','rs',12,extra='style=\"font-style:italic;font-weight:700;fill:#8a2f1c;stroke:#eef5f0\"'))")
R("o.append(T(1975,FL-90,\"PRINCE'S CAVERN\",'rll',14)+T(1975,FL-72,'vaulted aerie · 16 m vault','rsl'))","o.append(T(1925,FL-88,\"PRINCE'S CAVERN\",'rll',15)+T(1925,FL-69,'vaulted aerie · 16 m vault','rsl',12.5))")
R("'16 m solid limestone',off=-10)","'16 m solid limestone',off=-14)")
R("o.append(T(2262,Y(38)-58,'causeway stair','rs',11.5,extra='style=\"stroke:#dccfb6;font-style:italic\"')+T(2262,Y(38)-44,'(beyond section)','rs',11.5,extra='style=\"stroke:#dccfb6;font-style:italic\"'))","o.append(T(2232,Y(38)+22,'causeway stair climbs east','rs',12,extra='style=\"stroke:#e6dac2;font-weight:700;fill:#4a3716\"')+T(2232,Y(38)+38,'(beyond the section plane)','rs',12,extra='style=\"stroke:#e6dac2;fill:#4a3716\"'))")
R("o.append(T(1672,FL-8,'dragon launch arc','rs',12,extra='style=\"font-style:italic;font-weight:700;fill:#8f651d\"'))","o.append(T(1690,FL-18,'dragon launch arc','rs',12.5,extra='style=\"font-style:italic;font-weight:700;fill:#144a5c;stroke:#f3f1e4\"'))")
R("o.append(T(1640,962,'ADRIATA BAY','sea',16,extra='letter-spacing=\"3\"'))","o.append(T(1640,962,'ADRIATA BAY','sea',18,extra='letter-spacing=\"3\" '+HALO_SEA))")
R("o.append(T(2020,Y(55)+24,'sun-well','rs',11,extra='style=\"stroke:#dccfb6;font-style:italic\"'))","o.append(T(2036,Y(55)+60,'oculus sun-well','rs',12,'start',extra='style=\"stroke:#e6dac2;fill:#4a3716\"'))")
# panel IV
i=s.index("o.append(leg(0,0,"); j=s.index("p.a(G(''.join(o),extra=f'data-box=")
new='''L=[(line(0,0,40,0,WALL,5),'Marble / rock-cut wall'),(line(0,0,40,0,'#1fa3b8',4.5,'stroke-dasharray="11 4"'),'Sea-glass wall'),(rect(0,-7,40,14,'url(#poolGrad)',TEAL,1,3),'Pool · bath · tide-pool'),(G(column(20,0,6)),'Fluted gilt pillar'),
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
notes=[('Single bottleneck.','One guarded causeway joins the villa to Tarquin\\'s palace. Caelum\\'s door commands the gate hall; no one reaches either suite unseen.'),
('Private inner corridor.','Joins the two suites behind the salon and bolts from within — no crossing the lit glass after dark, no witness on the deck.'),
('Prince\\'s cover.','Sixteen metres of limestone lie between vault and villa. The sea-arch faces due west, blind to palace balconies, harbour and shore scryers.'),
('The stair.','160 rock-cut treads from Aurelie\\'s lobby, barred on her side. The only other door to the cavern is the sky.'),
('Flight discipline.','Launch west over open water, climb beyond the bay mouth before turning, and come home at dusk with the sun behind him.')]
yy=y0+260
for lead,body in notes:
    s_,h=para(1512,yy,lead,body,770,13,17.5); o.append(s_); yy+=h+6
print('notes end',yy,'limit',y0+476)
'''
s=s[:i]+new+s[j:]
open('plate1.py','w').write(s)
l=open('lib.py').read()
l=l.replace("T(W-72,131,'Drawn for the Autumn delegation · Vanserra household copy','sub',12.5,'end')","T(W-72,131,'Drawn for the Autumn delegation · Vanserra household copy','sub',13,'end','style=\"fill:#3d4f56\"')")
l=l.replace("return font(kind,size).getlength(s)/4+ls*len(s)","return font(kind,size).getlength(s)/4*1.04+ls*len(s)")
l=l.replace(".rs{font-family:'Noto Sans',sans-serif;font-size:12px;fill:#34474f","\n.rs{font-family:'Noto Sans',sans-serif;font-size:12.5px;fill:#2b3d45")
l=l.replace(".rsl{font-family:'Noto Sans',sans-serif;font-size:12px","\n.rsl{font-family:'Noto Sans',sans-serif;font-size:12.5px")
l=l.replace("font-size:11.5px;fill:#144a5c;text-anchor:middle;paint-order:stroke;stroke:#fdfaf3","font-size:12.5px;fill:#144a5c;text-anchor:middle;paint-order:stroke;stroke:#fdfaf3")
open('lib.py','w').write(l)
q=open('qa.py').read()
q=q.replace("var ts=[...document.querySelectorAll('svg text')];","var ts=[...document.querySelectorAll('svg text')].filter(e=>!e.querySelector('textPath'));")
open('qa.py','w').write(q)
