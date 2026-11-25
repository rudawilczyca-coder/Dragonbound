import math, random
from lib import *

p = P(2400, 1600)
background(p)
frame(
    p, 'V',
    'THE DROWNED ARCHIVE OF SUMMER',
    'First Age submarine vault beneath the palace cliffs · dead low water plan, tidal section & Turn 47 positions',
    'ADRIATA & THE SUMMER COURT PALACE',
    'Dragonbound Cartographic Suite · Plate V of V'
)

p.d.append('''
<linearGradient id="basaltWall" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#2c3940"/><stop offset="0.55" stop-color="#1d272d"/><stop offset="1" stop-color="#12191e"/>
</linearGradient>
<linearGradient id="basaltSill" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#29373f"/><stop offset="0.55" stop-color="#3a4b54"/><stop offset="1" stop-color="#233037"/>
</linearGradient>
<linearGradient id="ebbFloor" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#256f80"/><stop offset="0.5" stop-color="#31889a"/><stop offset="1" stop-color="#246574"/>
</linearGradient>
<radialGradient id="wardFlare" cx="0.5" cy="0.5" r="0.5">
  <stop offset="0" stop-color="#e8fbff" stop-opacity="0.95"/>
  <stop offset="0.35" stop-color="#7ee2ff" stop-opacity="0.65"/>
  <stop offset="1" stop-color="#45b8e6" stop-opacity="0"/>
</radialGradient>
<linearGradient id="highWaterFill" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#5bd2e3" stop-opacity="0.34"/>
  <stop offset="1" stop-color="#14677e" stop-opacity="0.42"/>
</linearGradient>
<pattern id="basaltHatch" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(-35)">
  <line x1="0" y1="0" x2="0" y2="12" stroke="#556a75" stroke-width="0.9" stroke-opacity="0.32"/>
</pattern>
<pattern id="ribFloor" width="20" height="18" patternUnits="userSpaceOnUse">
  <line x1="0" y1="9" x2="20" y2="9" stroke="#184a57" stroke-width="1.1" stroke-opacity="0.45"/>
  <line x1="10" y1="0" x2="10" y2="18" stroke="#7ce2ec" stroke-width="0.6" stroke-opacity="0.25"/>
</pattern>
<filter id="glowBlue" x="-40%" y="-40%" width="180%" height="180%">
  <feGaussianBlur stdDeviation="2.4" result="b"/>
  <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
<clipPath id="c1"><rect x="70" y="200" width="1408" height="740" rx="5"/></clipPath>
<clipPath id="c2"><rect x="70" y="996" width="1408" height="534" rx="5"/></clipPath>
<clipPath id="c3"><rect x="1516" y="200" width="814" height="620" rx="5"/></clipPath>
''')

HALO_SEA = 'style="paint-order:stroke;stroke:#0e566d;stroke-width:3.2px;stroke-linejoin:round"'
HALO_DARK = 'style="paint-order:stroke;stroke:#14232b;stroke-width:3.2px;stroke-linejoin:round"'
HALO_ROCK = 'style="paint-order:stroke;stroke:#ddd0b6;stroke-width:3.2px;stroke-linejoin:round"'

def dragon_perched_plan(cx, cy, s=1.0):
    o = []
    o.append('<ellipse cx="-8" cy="4" rx="96" ry="108" fill="#0b1419" fill-opacity="0.34"/>')
    tail_pts = [(-26, 0), (-58, 6), (-86, -8), (-110, 4), (-126, 12)]
    td = smooth(tail_pts)
    o.append(path(td, 'none', '#14232b', 16, 'stroke-linecap="round"'))
    o.append(path(td, 'none', '#f5f9fa', 12, 'stroke-linecap="round"'))
    o.append(path(td, 'none', '#c9e8f2', 4.5, 'stroke-linecap="round" stroke-opacity="0.7"'))
    o.append(path('M-118,8 L-144,18 L-134,3 L-142,-5 L-116,4 Z', 'url(#goldGrad)', '#7a5410', 1.3, 'stroke-linejoin="round"'))

    nw_outer = 'M8,-14 C16,-48 2,-88 -24,-114 C-42,-104 -54,-92 -66,-76 C-56,-68 -64,-54 -76,-42 C-62,-36 -66,-22 -74,-14 C-52,-12 -26,-10 8,-14 Z'
    sw_outer = 'M8,14 C16,48 2,88 -24,114 C-42,104 -54,92 -66,76 C-56,68 -64,54 -76,42 C-62,36 -66,22 -74,14 C-52,12 -26,10 8,14 Z'
    o.append(path(nw_outer, '#eef7fa', '#14232b', 1.6, 'stroke-linejoin="round"'))
    o.append(path(sw_outer, '#eef7fa', '#14232b', 1.6, 'stroke-linejoin="round"'))
    o.append(path('M6,-16 C10,-44 -2,-76 -24,-96 C-34,-84 -42,-68 -48,-46 C-36,-32 -16,-20 6,-16 Z', '#cbe9f4', 'none', 0, 'fill-opacity="0.75"'))
    o.append(path('M6,16 C10,44 -2,76 -24,96 C-34,84 -42,68 -48,46 C-36,32 -16,20 6,16 Z', '#cbe9f4', 'none', 0, 'fill-opacity="0.75"'))
    for fx, fy in [(-24, -108), (-44, -92), (-60, -72), (-68, -42), (-66, -18)]:
        o.append(line(4, -15, fx, fy, '#4f7a8c', 0.9, 'stroke-opacity="0.75"'))
    for fx, fy in [(-24, 108), (-44, 92), (-60, 72), (-68, 42), (-66, 18)]:
        o.append(line(4, 15, fx, fy, '#4f7a8c', 0.9, 'stroke-opacity="0.75"'))
    o.append(path('M10,-13 C18,-48 4,-88 -24,-114', 'none', '#ffffff', 2.4, 'stroke-linecap="round"'))
    o.append(path('M10,13 C18,48 4,88 -24,114', 'none', '#ffffff', 2.4, 'stroke-linecap="round"'))

    o.append(path('M-34,0 C-30,-15 -14,-19 8,-17 C24,-15 36,-9 46,-5 L46,5 C36,9 24,15 8,17 C-14,19 -30,15 -34,0 Z', '#fbfbf8', '#14232b', 1.6))
    o.append(path('M22,-15 L34,-24 M26,-16 L38,-19 M22,15 L34,24 M26,16 L38,19', 'none', '#b8860b', 1.8, 'stroke-linecap="round"'))
    o.append(path('M36,-7 C48,-8 58,-6 68,-4 L68,4 C58,6 48,8 36,7 Z', '#f3f9fb', '#14232b', 1.3))
    o.append(path('M64,-7 L84,-3 Q92,0 84,3 L64,7 Z', '#ffffff', '#14232b', 1.4, 'stroke-linejoin="round"'))
    o.append(path('M66,-5 C58,-16 46,-21 36,-23 M66,5 C58,16 46,21 36,23', 'none', '#d49d2a', 3.2, 'stroke-linecap="round"'))
    o.append(path('M66,-5 C58,-16 46,-21 36,-23 M66,5 C58,16 46,21 36,23', 'none', '#f8df92', 1.1, 'stroke-linecap="round"'))
    for dx in range(-28, 42, 9):
        o.append(line(dx, 0, dx - 4, 0, '#c5963e', 2.4, 'stroke-linecap="round"'))
    o.append(circ(74, -2.5, 1.3, '#144a5c') + circ(74, 2.5, 1.3, '#144a5c'))
    return G(''.join(o), f'translate({cx:.1f},{cy:.1f}) scale({s})')

def dragon_perched_side(cx, cy, s=1.0):
    o = []
    o.append(path('M-18,-6 C-44,-2 -66,8 -84,12', 'none', '#14232b', 8, 'stroke-linecap="round"'))
    o.append(path('M-18,-6 C-44,-2 -66,8 -84,12', 'none', '#f5f9fa', 5.5, 'stroke-linecap="round"'))
    o.append(path('M-78,10 L-96,17 L-88,9 L-93,3 L-76,8 Z', 'url(#goldGrad)', '#7a5410', 1.1))
    o.append(path('M-2,-16 C-16,-56 -48,-82 -76,-88 C-66,-68 -66,-52 -56,-34 C-38,-22 -18,-16 -2,-16 Z', '#c9e6f0', '#14232b', 1.2))
    o.append(path('M-22,-4 C-14,-22 8,-28 24,-20 C30,-16 32,-6 24,0 L-18,0 Z', '#fbfbf8', '#14232b', 1.4))
    o.append(path('M18,-6 L24,0 L28,0 M-12,-4 L-16,0 L-10,0', 'none', '#14232b', 2.6, 'stroke-linecap="round"'))
    o.append(path('M4,-18 C-4,-64 -34,-94 -66,-102 C-54,-82 -56,-64 -44,-44 C-28,-28 -10,-20 4,-18 Z', '#f3f9fb', '#14232b', 1.5))
    for x2, y2 in [(-60, -96), (-50, -76), (-42, -56), (-32, -38)]:
        o.append(line(0, -20, x2, y2, '#4f7a8c', 0.85))
    o.append(path('M20,-20 C26,-36 32,-50 42,-54 C50,-56 58,-53 62,-48 C56,-44 48,-44 42,-42 C36,-34 32,-22 26,-14 Z', '#fbfbf8', '#14232b', 1.4))
    o.append(path('M44,-54 C36,-66 26,-70 18,-70', 'none', '#d49d2a', 2.6, 'stroke-linecap="round"'))
    o.append(circ(50, -51, 1.2, '#144a5c'))
    return G(''.join(o), f'translate({cx:.1f},{cy:.1f}) scale({s})')

def person_token(cx, cy, letter, fill, ring='#fbf6ec'):
    return G(
        circ(cx, cy, 12.5, fill, ring, 2.2) +
        circ(cx, cy, 15.2, 'none', fill, 1.0, 'stroke-opacity="0.6"') +
        f'<text x="{cx:.1f}" y="{cy+4.2:.1f}" class="kn" font-size="12">{letter}</text>',
        cls='kr'
    )

# ==============================================================================
# PANEL I — SCALE FLOORPLAN AT DEAD LOW WATER (x=70..1478, y=200..940)
# ==============================================================================
p.a(panel_head(72, 186, 'I', 'THE DROWNED ARCHIVE — FLOORPLAN AT DEAD LOW WATER (TURN 47 POSITIONS)', 1406))

CY = 570
o = []
o.append(rect(70, 200, 1408, 740, 'url(#seaGradH)'))
o.append(rect(70, 200, 1408, 740, 'url(#waves)'))

for i, (x0, lab) in enumerate([(128, '−18 ft'), (186, '−12 ft'), (242, '−6 ft')]):
    pts = [(x0 + 12 * math.sin(y / 72 + i * 1.1), y) for y in range(195, 950, 50)]
    da = '' if i % 2 == 0 else '8 5'
    o.append(path(smooth(pts), 'none', '#bfeef4', 1.0, f'stroke-opacity="{0.48 - i*0.04}" stroke-dasharray="{da}"'))
    if i < 2:
        o.append(f'<text x="{pts[12][0]+5:.0f}" y="806" font-family="Noto Sans" font-style="italic" font-size="11.5" fill="#e3f8fb" {HALO_SEA}>{lab}</text>')

# Seaward Sky-Lane
o.append(path('M70,398 Q185,436 284,484 L284,656 Q185,612 70,564 Z', '#f6d88a', 'none', 0, 'fill-opacity="0.16"'))
o.append(path('M70,398 Q185,436 284,484', 'none', '#f6d88a', 1.4, 'stroke-dasharray="9 6"'))
o.append(path('M70,564 Q185,612 284,656', 'none', '#f6d88a', 1.4, 'stroke-dasharray="9 6"'))
o.append(path('M82,480 Q168,512 232,538', 'none', '#f6d88a', 2.8, 'stroke-dasharray="13 6"'))
o.append('<polygon points="248,545 224,544 233,527" fill="#f6d88a"/>')

# Solid Cliff-Limestone East Mass
o.append(rect(1150, 200, 328, 740, 'url(#cliffRock)'))
o.append(rect(1150, 200, 328, 740, 'url(#rockHatch)'))

# Solid Black First Age Basalt & Submarine Reef Shelf
basalt_poly = [
    (478, 200), (1186, 200), (1176, 330), (1184, 460), (1184, 680),
    (1174, 810), (1188, 940), (474, 940), (452, 865), (460, 775),
    (446, 705), (446, 435), (462, 360), (454, 275)
]
basalt_d = smooth(basalt_poly, True)
o.append(path(basalt_d, 'url(#basaltWall)', '#0d151a', 2.2))
o.append(path(basalt_d, 'url(#basaltHatch)'))

seam = [(1186, 200), (1176, 330), (1184, 460), (1184, 680), (1174, 810), (1188, 940)]
o.append(path(smooth(seam), 'none', '#7d6e58', 2.2, 'stroke-dasharray="10 5" stroke-opacity="0.75"'))

for seg in [[(468, 205), (446, 280), (454, 355), (432, 392)], [(432, 748), (450, 795), (444, 870), (464, 938)]]:
    o.append(path(smooth(seg), 'none', '#f4fdfe', 3.2, 'stroke-opacity="0.72" stroke-dasharray="14 5 4 5"'))

# Outer Basalt Sill
sill_pts = [
    (462, 412), (376, 404), (314, 424), (278, 474), (268, 535),
    (266, 605), (282, 668), (320, 718), (382, 736), (462, 728)
]
sill_d = smooth(sill_pts, True)
o.append(path(sill_d, 'none', '#e8fafc', 11, 'stroke-opacity="0.42" stroke-linejoin="round"'))
o.append(path(sill_d, 'none', '#ffffff', 3.0, 'stroke-opacity="0.78" stroke-dasharray="18 7 5 7"'))
o.append(path(sill_d, 'url(#basaltSill)', '#0f181d', 2.2))
for yline in range(435, 710, 26):
    rnd_s = random.Random(yline)
    x1 = 290 + rnd_s.randint(0, 35)
    x2 = x1 + rnd_s.randint(55, 115)
    o.append(line(x1, yline, x2, yline + rnd_s.randint(-5, 5), '#687f8a', 0.85, 'stroke-opacity="0.5"'))

# Drowned Archive Vault Interior (x=460..1060 = 60 ft)
vault_d = (
    'M460,450 L480,450 L480,424 '
    'Q562,336 644,424 L676,424 '
    'Q760,336 844,424 L876,424 '
    'Q958,336 1040,424 L1060,424 L1060,476 L1086,476 '
    'L1086,664 L1060,664 L1060,716 L1040,716 '
    'Q958,804 876,716 L844,716 '
    'Q760,804 676,716 L644,716 '
    'Q562,804 480,716 L480,690 L460,690 Z'
)
o.append(path(vault_d, 'none', '#c9d7d4', 9.5, 'stroke-opacity="0.55" stroke-linejoin="round"'))
o.append(path(vault_d, 'url(#ebbFloor)', '#0d181e', 3.4, 'stroke-linejoin="round"'))
o.append(path(vault_d, 'url(#ribFloor)'))

ebb_pools = [
    (548, 520, 62, 34), (566, 622, 68, 36), (674, 570, 56, 48),
    (772, 486, 64, 30), (766, 650, 66, 32), (880, 564, 62, 44),
    (980, 514, 52, 28), (976, 628, 56, 30)
]
for px, py, rx, ry in ebb_pools:
    o.append(f'<ellipse cx="{px}" cy="{py}" rx="{rx}" ry="{ry}" fill="url(#poolGrad)" fill-opacity="0.62" stroke="#a8f1f8" stroke-width="1.1" stroke-opacity="0.75"/>')
    o.append(f'<path d="M{px-rx*0.45:.1f},{py:.1f} q{rx*0.22:.1f},-6 {rx*0.45:.1f},0 t{rx*0.45:.1f},0" fill="none" stroke="#ebfdff" stroke-width="0.85" stroke-opacity="0.7"/>')

for ry in (476, 534, 606, 664):
    o.append(line(472, ry, 1054, ry, '#173842', 2.4, 'stroke-opacity="0.55"'))
    o.append(line(472, ry - 1.5, 1054, ry - 1.5, '#9cecf5', 0.8, 'stroke-opacity="0.45"'))

for rx in (472, 660, 860, 1048):
    o.append(rect(rx - 10, 412, 20, 26, '#1a252b', '#c9d7d4', 1.2, 3))
    o.append(rect(rx - 10, 702, 20, 26, '#1a252b', '#c9d7d4', 1.2, 3))
    o.append(line(rx, 438, rx, 702, '#e2f4f8', 1.6, 'stroke-dasharray="7 5" stroke-opacity="0.48"'))
for bx1, bx2 in [(472, 660), (660, 860), (860, 1048)]:
    o.append(line(bx1, 438, bx2, 702, '#c8ecf4', 0.9, 'stroke-dasharray="4 6" stroke-opacity="0.28"'))
    o.append(line(bx1, 702, bx2, 438, '#c8ecf4', 0.9, 'stroke-dasharray="4 6" stroke-opacity="0.28"'))

for ax in (562, 760, 958):
    n_arc = f'M{ax-72},422 Q{ax},348 {ax+72},422'
    o.append(path(n_arc, 'none', '#d8e9e8', 3.4, 'stroke-opacity="0.65"'))
    o.append(path(n_arc, 'none', '#84e4ff', 2.0, 'filter="url(#glowBlue)" stroke-dasharray="16 5 6 5"'))
    o.append(circ(ax, 386, 8, 'none', '#9beeff', 1.2, 'stroke-opacity="0.85" filter="url(#glowBlue)"'))
    o.append(circ(ax, 386, 3.2, '#d8f9ff', 'none', 0, 'fill-opacity="0.9"'))
    s_arc = f'M{ax-72},718 Q{ax},792 {ax+72},718'
    o.append(path(s_arc, 'none', '#d8e9e8', 3.4, 'stroke-opacity="0.65"'))
    o.append(path(s_arc, 'none', '#84e4ff', 2.0, 'filter="url(#glowBlue)" stroke-dasharray="16 5 6 5"'))
    o.append(circ(ax, 754, 8, 'none', '#9beeff', 1.2, 'stroke-opacity="0.85" filter="url(#glowBlue)"'))
    o.append(circ(ax, 754, 3.2, '#d8f9ff', 'none', 0, 'fill-opacity="0.9"'))

# Flood-Arch piers
o.append(rect(444, 412, 34, 38, '#172228', '#d5c8ae', 1.6, 3))
o.append(rect(444, 690, 34, 38, '#172228', '#d5c8ae', 1.6, 3))
o.append(line(454, 450, 454, 690, '#f3e5c2', 1.6, 'stroke-dasharray="8 4" stroke-opacity="0.85"'))
o.append(line(466, 450, 466, 690, '#f3e5c2', 1.6, 'stroke-dasharray="8 4" stroke-opacity="0.85"'))

# Two wet steps, Dry Threshold Ledge, Ward-Stone, Grate, Lock, 6-ft Stair
o.append(rect(1060, 514, 26, 112, '#d6ccb8', WALL, 1.4))
o.append(line(1073, 514, 1073, 626, WALL, 1.0))
o.append(rect(1060, 514, 13, 112, '#6ccbd6', 'none', 0, 0, 'fill-opacity="0.32"'))

o.append(rect(1086, 468, 116, 204, 'url(#tileSq)', WALL, 2.6))
o.append(rect(1202, 492, 62, 156, '#ede4d2', WALL, 2.6))
for y1, y2 in [(470, 514), (626, 670)]:
    o.append(line(1088, y1, 1088, y2, '#3d7063', 4.4))
    o.append(line(1088, y1, 1088, y2, '#9ec9ba', 1.4))
    for py in (y1 + 4, (y1 + y2) / 2, y2 - 4):
        o.append(circ(1088, py, 3.6, '#c5963e', '#26353c', 0.9))

WSX, WSY = 1166, 502
o.append(circ(WSX, WSY, 26, 'url(#wardFlare)'))
o.append(rect(WSX - 11, WSY - 11, 22, 22, '#223138', '#8ce6ff', 1.6, 3, 'filter="url(#glowBlue)"'))
o.append(path(f'M{WSX-9},{WSY-8} L{WSX-2},{WSY-1} L{WSX+3},{WSY-4} L{WSX+9},{WSY+9}', 'none', '#0c0d0e', 2.4))
o.append(path(f'M{WSX-9},{WSY-8} L{WSX-2},{WSY-1} L{WSX+3},{WSY-4} L{WSX+9},{WSY+9}', 'none', '#b4f3ff', 0.9))

o.append(line(1202, 492, 1202, 648, '#2f6155', 6.5))
o.append(line(1202, 492, 1202, 648, '#a4d4c6', 2.0, 'stroke-dasharray="5 5"'))
o.append(circ(1214, 480, 10, '#4d7e70', '#1c2b2f', 1.3) + circ(1214, 480, 4, GOLD, '#1c2b2f', 0.8))
o.append(line(1204, 480, 1224, 480, '#1c2b2f', 1.0) + line(1214, 470, 1214, 490, '#1c2b2f', 1.0))

o.append(rect(1264, 532, 30, 76, '#dfd4be', WALL, 2.4))
o.append(path('M1268,534 L1288,544 M1268,606 L1288,596', 'none', '#3c6f62', 4.5, 'stroke-linecap="round"'))
o.append(path('M1268,534 L1288,544 M1268,606 L1288,596', 'none', GOLD, 1.4, 'stroke-linecap="round"'))

o.append(rect(1294, 540, 164, 60, '#e8dcc4', WALL, 2.8))
for sx in range(1306, 1454, 12):
    o.append(line(sx, 540, sx, 600, '#786852', 0.9))
o.append(line(1438, 570, 1316, 570, INK, 1.3) + '<polygon points="1306,570 1318,565 1318,575" fill="#1b2d36"/>')
o.append(line(1458, 534, 1458, 606, '#3c6f62', 6.5) + line(1458, 534, 1458, 606, GOLD, 2.0))

o.append(line(446, 570, 1084, 570, '#ffe89e', 1.4, 'stroke-dasharray="8 5" stroke-opacity="0.85"'))
o.append(dragon_perched_plan(364, 570, 1.0))
o.append(circ(1238, 618, 18, '#f6e7a8', 'none', 0, 'fill-opacity="0.35"'))

p.a(G(''.join(o), extra='clip-path="url(#c1)"'))

# Panel I labels, tokens, badges & dimensions
o = []
o.append(person_token(1106, 570, 'A', '#2a8fa3'))
o.append(person_token(1126, 616, 'E', '#9e331f'))
o.append(person_token(1230, 526, 'V', '#144a5c'))
o.append(person_token(1234, 618, 'W', '#657882'))

for bx, by, n in [(1376, 520, 1), (1144, 686, 2), (1166, 466, 3), (760, 532, 4), (760, 356, 5), (461, 392, 6)]:
    o.append(key(bx, by, n))

o.append(compass(166, 294, 48, labels=('N', 'E', 'S', 'W'), light=True))
o.append(scalebar(96, 896, 10, (0, 10, 20, 30), light=True, label='feet'))

o.append(T(172, 444, 'SEAWARD SKY-LANE', 'rll', 13, extra=HALO_SEA))
o.append(T(172, 461, 'from Salt-Arch cavern →', 'rsl', 11.5, extra=HALO_SEA))
o.append(T(168, 698, 'ADRIATA', 'sea', 18, extra='letter-spacing="4" ' + HALO_SEA))
o.append(T(168, 721, 'BAY', 'sea', 18, extra='letter-spacing="4" ' + HALO_SEA))
o.append(T(168, 742, 'open sky behind wings', 'sea', 11.5, extra=HALO_SEA))

o.append(T(348, 756, 'OUTER BASALT SILL', 'rll', 13, extra=HALO_SEA))
o.append(T(348, 773, 'Prince (24-ft span) holds exit', 'rsl', 11.5, extra=HALO_SEA))
o.append(T(358, 378, 'PRINCE', 'rll', 14.5, extra=HALO_SEA))
o.append(T(358, 395, 'facing inward · 60 ft to Aurelie', 'rsl', 11.5, extra=HALO_SEA))

o.append(T(518, 296, 'SEAWARD FLOOD-ARCH', 'rll', 13.5, extra=HALO_DARK))
o.append(T(518, 313, '24 ft wide × 18 ft high', 'rsl', 12, extra=HALO_DARK))
o.append(line(494, 320, 468, 382, '#e8f7fa', 1.1, 'stroke-dasharray="3 2"'))
o.append(dimline(498, 450, 498, 690, '24 ft arch', off=14).replace('class="dim"', 'class="dim" style="fill:#e9fbfd;stroke:#14232b"').replace(f'stroke="{TEAL}"', 'stroke="#d8f6fa"'))

o.append(T(760, 268, 'NORTH FLANK — PRE-TREATY RELIEF ALCOVES', 'rll', 14, extra=HALO_DARK))
o.append(T(760, 286, 'carved dark basalt · salt-bloom · silver-blue light waking', 'rsl', 12, extra=HALO_DARK))
o.append(T(760, 886, 'SOUTH FLANK — PRE-TREATY RELIEF ALCOVES', 'rll', 14, extra=HALO_DARK))
o.append(T(760, 904, 'trench spirals · leviathan coils · First Age tide-glyphs', 'rsl', 12, extra=HALO_DARK))

o.append(T(760, 562, 'THE WADING FLOOR (60 FT)', 'rll', 15.5, extra=HALO_DARK))
o.append(T(760, 588, '60 ft straight sightline · Aurelie ↔ Prince', 'rsl', 12, extra='style="fill:#fff2be;paint-order:stroke;stroke:#14232b;stroke-width:3px"'))
o.append(T(760, 612, 'ribbed basalt channels & ankle-deep turquoise ebb pools', 'rsl', 12, extra=HALO_DARK))

o.append(dimline(460, 846, 1060, 846, '60 ft wading floor (arch sill to wet steps)', off=-8).replace('class="dim"', 'class="dim" style="fill:#e9fbfd;stroke:#14232b"').replace(f'stroke="{TEAL}"', 'stroke="#d8f6fa"'))
o.append(line(460, 730, 460, 844, '#9eeaf5', 0.8, 'stroke-dasharray="3 3" stroke-opacity="0.65"'))
o.append(line(1060, 720, 1060, 844, '#9eeaf5', 0.8, 'stroke-dasharray="3 3" stroke-opacity="0.65"'))

o.append(rect(1038, 356, 206, 46, PARCH, '#2c7e96', 1.3, 4, 'fill-opacity="0.95"'))
o.append(T(1141, 375, 'DORMANT WARD-STONE', 'rl', 12))
o.append(T(1141, 392, 'Hybern fracture · flaring silver-blue', 'rs', 11))
o.append(line(1154, 402, 1164, 454, '#8ce6ff', 1.4))

o.append(rect(1062, 720, 186, 62, PARCH, TEAL, 1.3, 4, 'fill-opacity="0.95"'))
o.append(T(1155, 739, 'DRY THRESHOLD LEDGE', 'rl', 12))
o.append(T(1155, 756, 'A: Aurelie (top wet step)', 'rs', 11))
o.append(T(1155, 772, 'E: Eris (left shoulder · rail)', 'rs', 11))
o.append(line(1126, 720, 1126, 632, '#9e331f', 1.2, 'stroke-dasharray="3 2"'))

o.append(rect(1266, 396, 198, 56, PARCH, '#3c6f62', 1.3, 4, 'fill-opacity="0.95"'))
o.append(T(1365, 415, 'INNER WARD-GRATE', 'rl', 12))
o.append(T(1365, 431, 'V: Varian at wheel (raised)', 'rs', 11))
o.append(T(1365, 445, 'Upper Tide-Lock unbarred', 'rs', 10.8))
o.append(line(1266, 434, 1236, 512, '#144a5c', 1.2, 'stroke-dasharray="3 2"'))

o.append(rect(1272, 668, 192, 44, PARCH, '#657882', 1.2, 4, 'fill-opacity="0.95"'))
o.append(T(1368, 687, 'W: SILVER WARD-SMITH', 'rl', 11.5))
o.append(T(1368, 703, 'behind grate · sea-glass lantern', 'rs', 10.8))
o.append(line(1272, 682, 1244, 628, '#657882', 1.2, 'stroke-dasharray="3 2"'))

o.append(T(1376, 622, '6-FT INTERIOR STAIR', 'rl', 12, extra=HALO_ROCK))
o.append(T(1376, 638, 'Fae single-file · no wings', 'rs', 11, extra=HALO_ROCK))
o.append(T(1376, 250, 'PALACE CLIFF', 'rl', 13.5, extra=HALO_ROCK))
o.append(T(1376, 267, 'solid limestone', 'rs', 12, extra=HALO_ROCK))
o.append(T(1376, 822, 'PALACE TIDE-HEAD →', 'rl', 12.5, extra=HALO_ROCK))
o.append(T(1376, 839, 'bronze door at cliff-root', 'rs', 11.5, extra=HALO_ROCK))
o.append(line(1450, 804, 1456, 610, '#8f651d', 1.1, 'stroke-dasharray="4 3"'))

for sx, sl in [(96, 'A'), (1452, 'A′')]:
    o.append(G(circ(sx, 570, 11, PARCH, INK, 1.5) + f'<text x="{sx}" y="574.5" text-anchor="middle" font-family="Noto Serif" font-weight="700" font-size="12" fill="{INK}">{sl}</text>', cls='kr'))

p.a(''.join(o))
p.a(rect(70, 200, 1408, 740, 'none', TEAL, 2, 5))

# ==============================================================================
# PANEL II — VERTICAL CLIFF & TIDE SECTION A–A′ (x=70..1478, y=996..1530)
# ==============================================================================
p.a(panel_head(72, 982, 'II', 'VERTICAL CLIFF & TIDE SECTION A–A′ (W → E, LOOKING NORTH · IN REGISTER WITH I)', 1406))

SL = 1446
def Y(ft):
    return SL - ft * 7.0

o = []
o.append(rect(70, 996, 1408, 534, 'url(#skyGrad)'))
for bx, by, bs in [(200, 1052, 0.9), (242, 1072, 0.7), (340, 1044, 0.8), (610, 1028, 0.65)]:
    o.append(path(f'M{bx-9*bs},{by} q{4*bs},{-5*bs} {9*bs},0 q{5*bs},{-5*bs} {9*bs},0', 'none', '#4d6068', 1.1))

o.append(rect(70, SL, 1408, 1530 - SL, 'url(#seaGradV)'))
o.append(path('M70,1530 L70,1514 Q180,1504 245,1476 L278,1434 L460,1434 L460,1530 Z', '#47555c', '#1a252b', 1.5))

cliff_pts = [
    (460, 1530), (460, Y(25)), (476, Y(32)), (520, Y(39)), (595, Y(45)),
    (700, Y(48)), (1478, Y(48)), (1478, 1530)
]
cliff_d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in cliff_pts) + ' Z'
o.append(path(cliff_d, 'url(#cliffRock)', '#5c4e3d', 2.0))
o.append(path(cliff_d, 'url(#rockHatch)'))

basalt_sec = [(272, 1530), (274, Y(1.5)), (460, Y(1.5)), (460, Y(25)), (1186, Y(25)), (1186, 1530)]
basalt_sd = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in basalt_sec) + ' Z'
o.append(path(basalt_sd, 'url(#basaltWall)', '#0d151a', 2.0))
o.append(path(basalt_sd, 'url(#basaltHatch)'))

GY = Y(48)
o.append(rect(690, GY - 5, 788, 5, '#ffffff', WALL, 1.1))
for gx in range(700, 1474, 16):
    o.append(line(gx, GY - 14, gx, GY - 5, WALL, 0.9))
o.append(line(690, GY - 14, 1478, GY - 14, WALL, 1.4))
for cx, ch in [(750, 32), (770, 24), (860, 36), (1120, 34), (1142, 26), (1380, 30)]:
    o.append(f'<ellipse cx="{cx}" cy="{GY-14-ch/2:.1f}" rx="5.5" ry="{ch/2:.1f}" fill="#2f5a3c" stroke="#1e3f2a" stroke-width="0.8"/>')
for px in (948, 968, 988, 1008):
    o.append(rect(px - 2, GY - 48, 4, 34, '#fff', WALL, 0.7))
o.append(path(f'M940,{GY-48:.1f} Q978,{GY-84:.1f} 1016,{GY-48:.1f} Z', '#1d879e', GOLD, 1.4))

arch_d = (
    f'M460,{Y(0):.1f} L460,{Y(18):.1f} '
    f'Q510,{Y(24):.1f} 600,{Y(24):.1f} L960,{Y(24):.1f} '
    f'Q1040,{Y(24):.1f} 1074,{Y(17):.1f} L1264,{Y(17):.1f} '
    f'L1264,{Y(2.5):.1f} L1086,{Y(2.5):.1f} L1060,{Y(0.5):.1f} L460,{Y(0.5):.1f} Z'
)
o.append(path(arch_d, 'url(#cavernDark)', '#0d151a', 2.4))

for bx in (562, 760, 958):
    o.append(path(f'M{bx-66},{Y(0.5):.1f} V{Y(16):.1f} Q{bx},{Y(22):.1f} {bx+66},{Y(16):.1f} V{Y(0.5):.1f} Z', '#1a262d', '#485d68', 1.2))
    o.append(rect(bx - 64, Y(5.5), 128, Y(0.5) - Y(5.5), '#d4e2df', 'none', 0, 0, 'fill-opacity="0.16"'))
    for gx in (bx - 38, bx, bx + 38):
        o.append(line(gx, Y(2.0), gx, Y(16.5), '#8be6ff', 1.1, 'stroke-dasharray="7 4 3 4" stroke-opacity="0.78" filter="url(#glowBlue)"'))
    o.append(circ(bx, Y(11.5), 14, 'none', '#8be6ff', 1.1, 'stroke-opacity="0.75" filter="url(#glowBlue)"'))

for rx in (472, 660, 860, 1048):
    o.append(rect(rx - 6, Y(24), 12, Y(0.5) - Y(24), '#28363e', '#0d151a', 1.0, 0, 'fill-opacity="0.85"'))

o.append(rect(460, Y(1.0), 600, Y(0) - Y(1.0) + 4, 'url(#poolGrad)', 'none', 0, 0, 'fill-opacity="0.72"'))
o.append(path(f'M1060,{Y(0.5):.1f} H1073 V{Y(1.5):.1f} H1086 V{Y(2.5):.1f} H1264 V{Y(0):.1f} H1060 Z', '#e2d7c0', WALL, 1.5))
o.append(rect(1086, Y(6.2), 4, Y(2.5) - Y(6.2), '#4d8273', '#1c2b2f', 0.8))

o.append(circ(1166, Y(5.0), 22, 'url(#wardFlare)'))
o.append(rect(1158, Y(6.8), 16, Y(2.5) - Y(6.8), '#23323a', '#8be6ff', 1.2, 2))
o.append(path(f'M1161,{Y(6.4):.1f} L1168,{Y(4.5):.1f} L1164,{Y(3.0):.1f}', 'none', '#0a0b0c', 1.8))

o.append(rect(1198, Y(17), 8, Y(10.5) - Y(17), '#4d8273', '#1c2b2f', 1.0))
o.append(line(1202, Y(10.5), 1202, Y(2.5), '#8fbdb0', 1.0, 'stroke-dasharray="3 4" stroke-opacity="0.65"'))
o.append(circ(1214, Y(8.0), 7, '#4d7e70', '#1c2b2f', 1.1))
o.append(rect(1264, Y(12.5), 26, Y(2.5) - Y(12.5), '#3c6f62', '#1c2b2f', 1.2, 0, 'fill-opacity="0.55"'))

stair_shaft = f'M1288,{Y(2.5):.1f} L1456,{Y(30.5):.1f} L1456,{Y(40.0):.1f} L1288,{Y(12.5):.1f} Z'
o.append(path(stair_shaft, '#e8dcc4', WALL, 2.0))
for k in range(18):
    t = k / 18
    sx = 1290 + t * 164
    sy = Y(2.5 + t * 28.0)
    o.append(line(sx, sy, sx + 9.2, sy, '#786852', 1.1))
    o.append(line(sx + 9.2, sy, sx + 9.2, sy - 11.6, '#786852', 0.9))
o.append(rect(1450, Y(40.5), 14, Y(30.5) - Y(40.5), '#3c6f62', GOLD, 1.5))

HWY = Y(16.0)
o.append(rect(70, HWY, 1220, SL - HWY, 'url(#highWaterFill)'))
o.append(path(f'M1288,{HWY:.1f} L1369,{HWY:.1f} L1288,{Y(2.5):.1f} Z', '#2a9fb4', 'none', 0, 'fill-opacity="0.38"'))
o.append(line(70, HWY, 1372, HWY, '#e6fcff', 2.4, 'stroke-dasharray="10 5"'))
o.append(line(70, HWY, 1372, HWY, '#125a6e', 0.9, 'stroke-dasharray="10 5"'))
o.append(line(1312, HWY, 1372, HWY, '#ffffff', 3.4, 'stroke-opacity="0.85"'))

o.append(path(f'M70,{SL} ' + ' '.join('q12,-5 24,0' for _ in range(16)), 'none', '#f4fdfe', 2.0))
o.append(line(460, SL, 1060, SL, '#ccf7fc', 1.5, 'stroke-dasharray="6 4"'))

def tiny_fig(fx, fy, col):
    return circ(fx, fy - 36, 4.0, col, '#fff', 0.8) + line(fx, fy - 32, fx, fy - 12, col, 3.2) + line(fx, fy - 12, fx - 3, fy, col, 2.0) + line(fx, fy - 12, fx + 3, fy, col, 2.0)
o.append(tiny_fig(1106, Y(2.5), '#2a8fa3'))
o.append(tiny_fig(1126, Y(2.5), '#9e331f'))
o.append(tiny_fig(1226, Y(2.5), '#144a5c'))
o.append(tiny_fig(1244, Y(2.5), '#657882'))
o.append(dragon_perched_side(356, Y(1.5), 1.0))

p.a(G(''.join(o), extra='clip-path="url(#c2)"'))

o = []
o.append(line(88, Y(0), 88, Y(48), INK, 1.3))
for ft in range(0, 50, 6):
    o.append(line(88, Y(ft), 96 if ft % 12 else 100, Y(ft), INK, 1.0))
for ft, lab in [(0, '0 ft · Dead Low Water'), (16, '+16 ft · High-Water Flood'), (24, '+24 ft · Vault Crown'), (34, '+34 ft · Palace Tide-Head'), (48, '+48 ft · Palace Gardens')]:
    o.append(line(88, Y(ft), 104, Y(ft), TEAL, 1.6) + T(109, Y(ft) + 4, lab, 'el', 11.5, extra='style="paint-order:stroke;stroke:#f4f7f2;stroke-width:3px"'))

o.append(dimline(442, Y(0), 442, Y(18), '18 ft arch', off=-13).replace('class="dim"', 'class="dim" style="fill:#144a5c;stroke:#eef6f4"'))

o.append(rect(546, HWY - 34, 412, 26, PARCH, TEAL, 1.2, 4, 'fill-opacity="0.95"'))
o.append(T(752, HWY - 17, 'HIGH-WATER FLOOD LINE · +10 ft up stair · submerges locks & reliefs', 'rl', 11.5))
o.append(line(752, HWY - 8, 752, HWY, TEAL, 1.2))

o.append(rect(560, SL + 22, 384, 24, '#0e566d', '#9cecf5', 1.1, 4, 'fill-opacity="0.92"'))
o.append(T(752, SL + 38, 'DEAD LOW WATER · 2-hour ebb window · ankle-deep pools', 'rsl', 11.5))

o.append(T(978, GY - 80, 'SUMMER PALACE GARDENS', 'rl', 13, extra='style="stroke:#dbeef2"'))
o.append(T(1344, Y(42.5), 'PALACE TIDE-HEAD', 'rl', 12, extra=HALO_ROCK))
o.append(T(1344, Y(40.3), 'cliff-root bronze door', 'rs', 11, extra=HALO_ROCK))
o.append(line(1408, Y(41.5), 1448, Y(36.0), '#8f651d', 1.1))
o.append(T(1386, Y(10.5), '6-ft Interior Stair', 'rl', 11.5, extra=HALO_ROCK))
o.append(T(1386, Y(8.3), 'high-tide rings +10 ft', 'rs', 10.8, extra=HALO_ROCK))
o.append(line(1360, Y(12.0), 1344, Y(15.5), '#5c4e3d', 1.0, 'stroke-dasharray="3 2"'))
o.append(T(318, Y(22.0), 'Prince on Outer Sill', 'rl', 12.5, extra='style="stroke:#eef6f4"'))
o.append(T(318, Y(19.6), 'open bay air behind wings', 'rs', 11, extra='style="stroke:#eef6f4"'))
o.append(T(1156, Y(21.0), 'DRY LEDGE & GRATE', 'rl', 11.5, extra=HALO_ROCK))
o.append(T(1156, Y(18.8), 'A · E · V · W (Turn 47)', 'rs', 10.8, extra=HALO_ROCK))
o.append(T(200, 1496, 'ADRIATA BAY', 'sea', 16, extra='letter-spacing="3" ' + HALO_SEA))

p.a(''.join(o))
p.a(rect(70, 996, 1408, 534, 'none', TEAL, 2, 5))

# ==============================================================================
# PANEL III — MORNING ROUTE & NEXT-BEAT KEY (x=1516..2330, y=200..820)
# ==============================================================================
p.a(panel_head(1518, 186, 'III', 'MORNING ROUTE & NEXT-BEAT KEY — ADRIATA COAST', 812))

o = []
o.append(rect(1516, 200, 814, 620, 'url(#seaGrad)'))
o.append(rect(1516, 200, 814, 620, 'url(#waves)'))

headland = [
    (1635, 340), (1710, 275), (1860, 248), (2060, 255), (2215, 315),
    (2265, 425), (2250, 565), (2175, 650), (2050, 680), (1905, 668),
    (1795, 620), (1705, 565), (1648, 495), (1625, 415)
]
hd = smooth(headland, True)
for k, op in [(1.09, 0.35), (1.19, 0.22)]:
    o.append(path(smooth(scale_pts(headland, (1940, 465), k), True), 'none', '#c9f1f6', 1.1, f'stroke-opacity="{op}" stroke-dasharray="8 5"'))
o.append(path(hd, 'none', '#f4fdfe', 8, 'stroke-opacity="0.48"'))
o.append(path(hd, 'url(#cliffRock)', '#5c4e3d', 1.8))
o.append(path(hd, 'url(#rockHatch)', 'none', 0, 'fill-opacity="0.45"'))

plat = [(1790, 322), (1950, 296), (2085, 336), (2100, 442), (1975, 485), (1810, 465), (1765, 392)]
o.append(path(smooth(plat, True), '#f3ebd6', '#8a7350', 1.3))
o.append(rect(1896, 340, 128, 72, '#ffffff', WALL, 1.5, 4))
o.append(circ(1960, 376, 18, '#1d879e', GOLD, 1.6) + circ(1920, 376, 10, '#2a9fb4', GOLD, 1.1) + circ(2000, 376, 10, '#2a9fb4', GOLD, 1.1))

o.append(path('M1775,460 Q1880,485 1965,495 Q1940,565 1860,595 Q1785,570 1758,505 Z', 'url(#grass)', '#5f8a55', 0.9, 'fill-opacity="0.75"'))

o.append(path('M2250,510 Q2228,595 2168,648', 'none', '#3a2a10', 9) + path('M2250,510 Q2228,595 2168,648', 'none', '#efe6cf', 5.5))
for px, py, ang in [(2252, 540, 12), (2230, 594, 30), (2194, 636, 48)]:
    o.append(G(rect(0, -4, 34, 8, '#efe6cf', '#3a2a10', 1.0), f'translate({px},{py}) rotate({ang})'))

o.append(path('M1628,402 C1596,408 1596,442 1628,448 L1654,448 L1654,402 Z', '#ffffff', WALL, 1.4))
o.append(path('M1624,412 C1606,416 1606,434 1624,438 Z', 'url(#poolGrad)', TEAL, 0.8))

foot_pts = [(1654, 425), (1736, 434), (1792, 468), (1832, 526), (1854, 592)]
o.append(path(smooth(foot_pts), 'none', '#5c2014', 4.2, 'stroke-opacity="0.35"'))
o.append(path(smooth(foot_pts), 'none', CORAL, 2.6, 'stroke-dasharray="7 4"'))
o.append(circ(1816, 502, 5.5, '#5a6c4a', '#ffffff', 1.3))

sky_pts = [(1612, 446), (1586, 548), (1638, 632), (1742, 660), (1842, 622)]
o.append(path(smooth(sky_pts), 'none', '#5a3d0a', 5.0, 'stroke-opacity="0.45"'))
o.append(path(smooth(sky_pts), 'none', '#f6d88a', 2.8, 'stroke-dasharray="11 5"'))
o.append('<polygon points="1850,618 1830,616 1837,631" fill="#f6d88a"/>')
o.append(dragon_fly(1676, 646, 0.56, 16))

next1 = [(1878, 610), (1995, 645), (2120, 628), (2194, 592)]
o.append(path(smooth(next1), 'none', '#ffffff', 3.4, 'stroke-opacity="0.65"'))
o.append(path(smooth(next1), 'none', TEAL, 2.2, 'stroke-dasharray="5 4"'))
next2 = [(2202, 574), (2142, 492), (2068, 412), (2004, 384)]
o.append(path(smooth(next2), 'none', '#ffffff', 3.4, 'stroke-opacity="0.65"'))
o.append(path(smooth(next2), 'none', TEAL, 2.2, 'stroke-dasharray="5 4"'))

o.append(circ(1862, 606, 22, '#f6d88a', 'none', 0, 'fill-opacity="0.32"'))
o.append(circ(1862, 606, 16, 'none', '#8be6ff', 2.0, 'stroke-dasharray="4 3"'))

p.a(G(''.join(o), extra='clip-path="url(#c3)"'))

o = []
def stop_badge(x, y, ch, col=TEAL):
    return G(circ(x, y, 12, col, '#f6e0a2', 1.8) + f'<text x="{x}" y="{y+4.2}" class="kn" font-size="12.5">{ch}</text>', cls='kr')

o.append(stop_badge(1624, 425, 'A', '#8f651d'))
o.append(stop_badge(1862, 606, 'B', CORAL))
o.append(stop_badge(2204, 584, 'C', TEAL))
o.append(stop_badge(1960, 376, 'D', '#144a5c'))

o.append(rect(1532, 214, 218, 46, PARCH, '#8f651d', 1.2, 4, 'fill-opacity="0.94"'))
o.append(T(1641, 233, 'A · SALT-ARCH VILLA', 'rl', 12))
o.append(T(1641, 249, '+38 m deck · cavern 60 m below', 'rs', 10.8))
o.append(line(1624, 260, 1624, 410, '#f6d88a', 1.2, 'stroke-dasharray="3 2"'))

o.append(rect(2034, 214, 280, 46, PARCH, TEAL, 1.2, 4, 'fill-opacity="0.94"'))
o.append(T(2174, 233, 'D · UPPER COUNCIL LOGGIA', 'rl', 12))
o.append(T(2174, 249, "Tarquin's 10-min closed-door audience", 'rs', 10.8))
o.append(line(2082, 260, 1974, 366, TEAL, 1.2, 'stroke-dasharray="3 2"'))

o.append(rect(2042, 686, 272, 46, PARCH, TEAL, 1.2, 4, 'fill-opacity="0.94"'))
o.append(T(2178, 705, 'C · HARBOR SALT-FIRE ANVIL', 'rl', 12))
o.append(T(2178, 721, 'burn tracking-thread from shed token', 'rs', 10.8))
o.append(line(2204, 686, 2204, 598, TEAL, 1.2, 'stroke-dasharray="3 2"'))

o.append(rect(1690, 704, 294, 46, PARCH, CORAL, 1.4, 4, 'fill-opacity="0.95"'))
o.append(T(1837, 723, 'B · DROWNED ARCHIVE (TURN 47)', 'rl', 12, extra='style="fill:#8f2d1b"'))
o.append(T(1837, 739, 'Palace Tide-Head · submarine cliff-root', 'rs', 10.8))
o.append(line(1862, 704, 1862, 622, CORAL, 1.3, 'stroke-dasharray="3 2"'))

o.append(T(1614, 670, 'SEAWARD SKY-LANE', 'rll', 11.5, extra=HALO_SEA))
o.append(T(1614, 685, 'Prince (cleared by wardens)', 'rsl', 10.5, extra=HALO_SEA))
o.append(T(1752, 404, 'Causeway', 'rl', 11, extra=HALO_ROCK))
o.append(T(1856, 512, 'Caelum (arch)', 'rs', 10.5, 'start', extra=HALO_ROCK))
o.append(T(2038, 616, 'next: B → C', 'rs', 10.8, extra=HALO_ROCK))
o.append(T(2132, 460, 'C → D', 'rs', 10.8, extra=HALO_ROCK))

o.append(rect(1528, 766, 790, 42, '#fdfaf3', GOLD, 1.1, 4, 'fill-opacity="0.94"'))
o.append(line(1544, 787, 1584, 787, CORAL, 2.6, 'stroke-dasharray="6 3"') + T(1592, 791, 'Foot route (causeway & stair)', 'nt', 11.8))
o.append(line(1786, 787, 1826, 787, '#d49d2a', 2.8, 'stroke-dasharray="10 4"') + T(1834, 791, 'Wing route (sky-lane)', 'nt', 11.8))
o.append(line(1996, 787, 2036, 787, TEAL, 2.2, 'stroke-dasharray="5 4"') + T(2044, 791, 'Next beats: Archive → Anvil → Loggia', 'nt', 11.8))

p.a(''.join(o))
p.a(rect(1516, 200, 814, 620, 'none', TEAL, 2, 5))

# ==============================================================================
# PANEL IV — LEGEND, KEY & SPATIAL NOTES FOR PLAY (x=1516..2330, y=874..1530)
# ==============================================================================
Y4 = 874
p.a(panel_head(1518, Y4 - 14, 'IV', 'LEGEND, KEY & SPATIAL NOTES FOR PLAY', 812))
p.a(rect(1516, Y4, 814, 656, '#fdfaf3', TEAL, 2, 5, 'fill-opacity="0.86"'))

o = []
LEG = [
    (rect(0, -6, 36, 12, 'url(#basaltWall)', '#0d151a', 1.1), 'First Age basalt & reef'),
    (rect(0, -6, 36, 12, 'url(#cliffRock)', '#6b5a44', 1.0) + rect(0, -6, 36, 12, 'url(#rockHatch)'), 'Solid cliff-limestone'),
    (rect(0, -6, 36, 12, 'url(#poolGrad)', TEAL, 1.0, 3), 'Ankle-deep ebb pools'),
    (line(0, 0, 36, 0, '#84e4ff', 3.0) + circ(18, 0, 3.2, '#e6fbff', '#1c7c96', 0.8), 'Waking silver-blue light'),
    (line(0, 0, 36, 0, '#2f6155', 5.5) + line(0, 0, 36, 0, GOLD, 1.5, 'stroke-dasharray="5 4"'), 'Bronze grate / tide-lock'),
    (line(0, 0, 36, 0, '#14677e', 2.4, 'stroke-dasharray="7 4"'), 'High-water flood line'),
    (line(0, 0, 36, 0, CORAL, 2.5, 'stroke-dasharray="6 3"'), 'Foot route (Fae only)'),
    (line(0, 0, 36, 0, '#d49d2a', 2.6, 'stroke-dasharray="10 4"'), "Prince's seaward sky-lane"),
    (circ(8, 0, 6.5, '#2a8fa3', '#fff', 1) + circ(22, 0, 6.5, '#9e331f', '#fff', 1) + circ(36, 0, 6.5, '#144a5c', '#fff', 1), 'Turn 47 live positions')
]
for i, (sym, txt) in enumerate(LEG):
    col = i % 3; row = i // 3
    lx = 1538 + col * 264; ly = Y4 + 28 + row * 26
    o.append(G(sym, f'translate({lx},{ly})') + T(lx + 48, ly + 4.5, txt, 'nt', 12.5))

o.append(line(1536, Y4 + 102, 2310, Y4 + 102, GOLD, 1.0))
o.append(T(1538, Y4 + 125, 'KEY TO ARCHIVE FEATURES (PANEL I)', 'nb', 13.5, extra='letter-spacing="1.4"'))

KEY_ITEMS = [
    '6-ft Interior Palace Tide Stair & Upper Tide-Lock',
    'Dry Threshold Ledge & Bronze Inner Ward-Grate',
    'Dormant Vault Ward-Stone (cracked · flaring)',
    'The Wading Floor (60 ft · ribbed basalt & pools)',
    'Pre-Treaty Relief Alcoves (N & S flanks)',
    'Seaward Flood-Arch (24 × 18 ft) & Outer Basalt Sill'
]
for i, txt in enumerate(KEY_ITEMS):
    col = i // 3; row = i % 3
    kx = 1548 + col * 392; ky = Y4 + 150 + row * 25
    o.append(key(kx, ky, i + 1) + T(kx + 18, ky + 4.5, txt, 'nt', 12.5))

o.append(line(1536, Y4 + 224, 2310, Y4 + 224, GOLD, 1.0))
o.append(T(1538, Y4 + 247, 'SPATIAL & TACTICAL NOTES FOR PLAY', 'nb', 13.5, extra='letter-spacing="1.4"'))

NOTES = [
    ('Footing & surfaces.',
     'Dry limestone Threshold Ledge sits two wet steps above the 60-ft Wading Floor (ribbed basalt channels & ankle-deep glass-clear pools). Outside the arch lies the broad, wave-washed black Outer Basalt Sill over bay rollers.'),
    ('Sightlines (Turn 47).',
     'Sixty feet straight west from Aurelie at the top wet step to Prince filling the 24-ft Flood-Arch. Eris stays dry one pace behind her left shoulder at the bronze rail; Varian holds the grate wheel with the ward-smith behind.'),
    ('Two separate approaches.',
     "The 6-ft Interior Tide Stair admits Fae single-file only — Prince's 24-ft wings cannot enter the shaft. He approached by the cleared Seaward Sky-Lane and holds the 24 × 18 ft seaward exit with open sky behind him."),
    ('Two-hour flood-sill clock.',
     'Upper locks drained eight minutes prior at morning dead low water. When the tide turns, seawater climbs +10 ft up the limestone stair shaft, submerging reliefs, ward-stone, bronze grate, and locks.'),
    ('Next beats (C → D).',
     "Any shed token goes first to the Harbor Quay Salt-Fire Anvil (C) to burn out tracking-threads, then up to the Upper Palace Council Loggia (D) for Tarquin's ten-minute closed-door audience.")
]
yy = Y4 + 273
for lead, body in NOTES:
    s_, h = para(1538, yy, lead, body, 756, 13.0, 18.0)
    o.append(s_)
    yy += h + 9

# Turn 47 Live Roster strip at bottom of Panel IV
ry_rule = Y4 + 558
o.append(line(1536, ry_rule, 2310, ry_rule, GOLD, 1.0))
o.append(T(1538, ry_rule + 22, 'TURN 47 LIVE POSITIONS (TOKENS IN PANELS I & II)', 'nb', 12.8, extra='letter-spacing="1.3"'))
ROSTER = [
    ('A', '#2a8fa3', 'Aurelie', 'top wet step · facing west'),
    ('E', '#9e331f', 'Eris', 'left shoulder · dry rail'),
    ('V', '#144a5c', 'Varian', 'inner grate wheel'),
    ('W', '#657882', 'Ward-smith', 'behind grate · lantern'),
]
for idx, (ch, col, nm, pos) in enumerate(ROSTER):
    rx = 1554 + (idx % 2) * 384
    ry = ry_rule + 48 + (idx // 2) * 29
    o.append(G(circ(rx, ry, 10, col, '#fbf6ec', 1.6) + f'<text x="{rx}" y="{ry+3.6}" class="kn" font-size="10.5">{ch}</text>', cls='kr'))
    o.append(T(rx + 18, ry + 4, f'{nm} — {pos}', 'nt', 12.2))
print('Panel IV notes end:', yy, 'roster bottom:', ry_rule + 88, 'limit:', Y4 + 650)

p.a(G(''.join(o), extra=f'data-box="1518,{Y4+2},2328,{Y4+654}"'))

OUT_SVG = '/home/sable/Dragonbound/art/adriata/plate05_drowned_archive.svg'
p.save(OUT_SVG)
print('Saved:', OUT_SVG)
