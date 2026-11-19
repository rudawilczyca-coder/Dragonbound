#!/usr/bin/env python3
"""Winter Court warlord tattoo — bindrune & kill-tally sheets.

Generates, next to this script:
  winter_warlord_tattoo_blueprint.svg          dual-view sheet, bone/ice ink on charcoal slate
  winter_warlord_tattoo_stencil_parchment.svg  flat artist stencil, black ink on parchment

  python3 generate_tattoo_svg.py            # write the SVGs
  python3 generate_tattoo_svg.py --render   # also render PNGs through Chrome CDP (127.0.0.1:9222)

All tattoo geometry is drawn once, in a "torso-local" coordinate space (x = 0 on the
spine / sternum, y grows downward, roughly 1 unit = 1 px at scale 1), and reused by
both sheets.  Only the right half is authored; the left is a mirror.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 2800, 1750

# --------------------------------------------------------------------------- helpers


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def path(pts, cls, closed=False):
    d = "M" + " L".join(f"{f(x)},{f(y)}" for x, y in pts) + (" Z" if closed else "")
    return f'<path class="{cls}" d="{d}"/>'


def line(a, b, cls):
    return path([a, b], cls)


def diamond(cx, cy, hw, hh, cls, rot=0.0):
    """Lozenge; rot (radians) aligns the long axis (hh) with a shaft direction."""
    pts = [(0, -hh), (hw, 0), (0, hh), (-hw, 0)]
    c, s = math.cos(rot), math.sin(rot)
    return path([(cx + x * c - y * s, cy + x * s + y * c) for x, y in pts], cls, True)


def circle(cx, cy, r, cls):
    return f'<circle class="{cls}" cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}"/>'


def chevron(y, w, h, cls, cx=0.0):
    """Apex on the axis at y; arms run to (cx±w, y+h)."""
    return path([(cx - w, y + h), (cx, y), (cx + w, y + h)], cls)


def crescent(cx, cy, r, cls, horns="left", a_deg=15):
    """Filled lune. horns='left' -> the horns point left (bulge on the right)."""
    a = math.radians(a_deg)
    sx = -1 if horns == "left" else 1
    hx = cx + sx * r * math.sin(a)
    p1, p2 = (hx, cy - r * math.cos(a)), (hx, cy + r * math.cos(a))
    sw_out, sw_in = (1, 0) if horns == "left" else (0, 1)
    return (f'<path class="{cls}" d="M{f(p1[0])},{f(p1[1])} A{f(r)},{f(r)} 0 1 {sw_out} {f(p2[0])},{f(p2[1])} '
            f'A{f(r)},{f(r)} 0 0 {sw_in} {f(p1[0])},{f(p1[1])} Z"/>')


def unit(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    n = math.hypot(dx, dy)
    return dx / n, dy / n


def along(a, b, d):
    u = unit(a, b)
    return a[0] + u[0] * d, a[1] + u[1] * d


def mirror(svg):
    return f'<g transform="scale(-1,1)">{svg}</g>'


def both(svg):
    return svg + mirror(svg)


def catmull(pts, n=14):
    """Dense polyline through pts (uniform Catmull-Rom)."""
    out = []
    P = [pts[0]] + list(pts) + [pts[-1]]
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for k in range(n):
            t = k / n
            out.append(tuple(
                0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t
                       + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                       + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t ** 3) for j in (0, 1)))
    out.append(pts[-1])
    return out


# --------------------------------------------------------------------------- torso

SHOULDER = catmull([(58, 10), (60, 60), (70, 112), (120, 132), (175, 152), (228, 172),
                    (285, 205), (316, 270), (322, 350), (318, 450), (312, 560)])
INNER_ARM = catmull([(258, 560), (250, 480), (240, 415)])
FLANK = catmull([(240, 415), (236, 500), (220, 620), (192, 760), (182, 830),
                 (190, 900), (206, 980), (212, 1070)])


def seg_hit(p, q, a, b):
    """Intersection of segment pq with the infinite line through a,b (or None)."""
    d1 = (q[0] - p[0], q[1] - p[1])
    d2 = (b[0] - a[0], b[1] - a[1])
    den = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(den) < 1e-9:
        return None
    t = ((a[0] - p[0]) * d2[1] - (a[1] - p[1]) * d2[0]) / den
    return (p[0] + d1[0] * t, p[1] + d1[1] * t) if 0 <= t <= 1 else None


def shoulder_hit(a, b, xmin, xmax):
    for p, q in zip(SHOULDER, SHOULDER[1:]):
        if xmin <= p[0] <= xmax:
            h = seg_hit(p, q, a, b)
            if h:
                return h
    raise ValueError("no shoulder intersection")


def torso(view):
    """Faint anatomical silhouette + guides. view = 'back' | 'front'."""
    right = SHOULDER + INNER_ARM + FLANK
    left = [(-x, y) for x, y in reversed(right)]
    o = [path(right + left, "skin", True)]
    for run in (SHOULDER, INNER_ARM, FLANK):
        o.append(both(path(run, "edge")))
    g = []
    if view == "back":
        scap = catmull([(50, 236), (130, 214), (206, 222), (214, 300), (170, 400), (118, 468),
                        (60, 410), (46, 320), (50, 236)])
        g.append(both(path(scap, "guide")))
        g.append(line((0, 118), (0, 1050), "guide dash"))
        g.append(both(path(catmull([(84, 1012), (130, 974), (196, 952)]), "guide")))
        g.append(path(catmull([(-66, 112), (-34, 124), (0, 128), (34, 124), (66, 112)]), "collar"))
    else:
        g.append(both(path(catmull([(14, 172), (80, 180), (150, 172), (222, 180)]), "guide")))
        g.append(both(path(catmull([(10, 436), (70, 462), (150, 452), (214, 410), (238, 372)]), "guide")))
        g.append(line((0, 500), (0, 1000), "guide dash"))
        for y, w in ((560, 96), (660, 92), (760, 86)):
            g.append(both(path(catmull([(12, y), (w * 0.55, y + 8), (w, y - 4)]), "guide")))
        g.append(circle(0, 880, 5, "guide"))
        g.append(both(path(catmull([(196, 960), (150, 1010), (96, 1060)]), "guide")))
        collar = catmull([(-68, 108), (-40, 138), (0, 152), (40, 138), (68, 108)])
        g.append(path(collar, "collar"))
        for i in range(7, len(collar) - 6, 7):          # pyramid studs under the collar edge
            x, y = collar[i]
            g.append(path([(x - 4, y + 5), (x, y + 12), (x + 4, y + 5)], "stud", True))
    fade = ('<defs><linearGradient id="fd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/>'
            '<stop offset="1" stop-color="#000"/></linearGradient>'
            '<linearGradient id="fu" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#fff"/>'
            '<stop offset="1" stop-color="#000"/></linearGradient>'
            f'<mask id="tm-{view}" maskUnits="userSpaceOnUse" x="-340" y="0" width="680" height="1080">'
            '<rect x="-340" y="0" width="680" height="1080" fill="#fff"/>'
            '<rect x="-340" y="1024" width="680" height="56" fill="#000"/>'
            '<rect x="-340" y="1026" width="680" height="46" fill="url(#fd)"/>'
            '<rect x="-80" y="0" width="160" height="12" fill="#000"/>'
            '<rect x="-80" y="10" width="160" height="50" fill="url(#fu)"/>'
            + "".join(f'<rect x="{x}" y="548" width="92" height="20" fill="#000"/>'
                      f'<rect x="{x}" y="470" width="92" height="80" fill="url(#fd)"/>' for x in (245, -337))
            + '</mask></defs>')
    return f'{fade}<g mask="url(#tm-{view})">' + "".join(o) + "".join(g) + "</g>"


# --------------------------------------------------------------------------- shared anchor points

LOCK = (0.0, 330.0)                 # wing-root lock, between the shoulder blades
J1, J2 = (92.0, 262.0), (188.0, 232.0)   # wing joints along the arm-shaft
HEART = (0.0, 335.0)
HW, HH = 70.0, 62.0                 # heart diamond half-width / half-height
M = HH / HW                         # slope of the four chest staves
TOP, BOT = (0.0, HEART[1] - HH), (0.0, HEART[1] + HH)
# clavicle stave R_a: y = TOP.y - M x   (right shoulder -> top node -> far-left corner)
# deltoid  stave R_b: y = BOT.y - M x   (right shoulder -> right corner -> stops short of BOT)
E_TRAP = shoulder_hit(TOP, (100.0, TOP[1] - M * 100.0), 100, 215)   # where R_a meets the trapezius ridge
E_DELT = next(p for p in SHOULDER if p[0] > 230 and p[1] >= 228)     # stave exit on the deltoid cap
KNEE = (196.0, BOT[1] - M * 196.0)                                   # front knee of the deltoid stave

BLADE_STEP, BLADE_LEN, BLADE_W, BLADE_ANG = 27.0, 38.0, 8.0, math.radians(38)
TALON_LEN, TALON_TURN = 36.0, math.radians(40)


def _rib(origin, lean_deg, length, blades):
    """Rib-stave leaning lean_deg outward from vertical; the talon kinks back toward the spine."""
    a = math.radians(lean_deg)
    knee = (origin[0] + length * math.sin(a), origin[1] + length * math.cos(a))
    t = a - TALON_TURN
    return origin, knee, (knee[0] + TALON_LEN * math.sin(t), knee[1] + TALON_LEN * math.cos(t)), blades


# one wing = four rib-staves fanned 4 / 9 / 14 / 19 degrees, longest nearest the spine (a folded wing)
RIBS = [
    _rib(J2, 19, 150, 4),
    _rib(((J1[0] + J2[0]) / 2, (J1[1] + J2[1]) / 2), 14, 225, 6),
    _rib(J1, 9, 285, 7),
    _rib((54.0, 290.1), 4, 322, 7),
]


def rib_frame(o, k):
    """(shaft unit, blade direction, counter-tick direction, length) for a rib o->k."""
    u = unit(o, k)
    nrm = (-u[1], u[0])
    if nrm[0] < 0:                       # trailing side = lateral (away from the spine)
        nrm = (-nrm[0], -nrm[1])
    ca, sa = math.cos(BLADE_ANG), math.sin(BLADE_ANG)
    return (u, (ca * u[0] + sa * nrm[0], ca * u[1] + sa * nrm[1]),
            (ca * u[0] - sa * nrm[0], ca * u[1] - sa * nrm[1]), math.hypot(k[0] - o[0], k[1] - o[1]))


def blade_tip(ri, i=0):
    """Tip of the i-th blade (counted up from the knee) on rib ri."""
    o, k, _, _ = RIBS[ri]
    u, v, _, length = rib_frame(o, k)
    d = length - 14 - i * BLADE_STEP
    return o[0] + u[0] * d + v[0] * BLADE_LEN, o[1] + u[1] * d + v[1] * BLADE_LEN


# --------------------------------------------------------------------------- back: spine axis

def spine():
    o, blades = [], 0
    # crown blade — the single axial tally
    o.append(path([(-6, 252), (6, 252), (0, 176)], "blade", True)); blades += 1
    o.append(line((0, 252), (0, 290), "p"))
    o.append(chevron(264, 17, 12, "s"))
    # shaft runs, broken by the locks
    for a, b in ((372, 426), (610, 692), (731, 754), (802, 825), (863, 930)):
        o.append(line((0, a), (0, b), "p"))
    o.append(chevron(388, 16, -11, "s"))
    o.append(chevron(402, 16, -11, "s"))
    # stacked diamond lattice (thoracic)
    o.append(diamond(0, 446, 16, 22, "s lock"))
    o.append(diamond(0, 518, 34, 50, "p lock"))
    o.append(diamond(0, 518, 18, 25, "s"))
    o.append(line((-34, 518), (34, 518), "h"))
    o.append(line((0, 468), (0, 568), "h"))
    o.append(diamond(0, 590, 16, 22, "s lock"))
    # vertebra ticks
    for y, w in ((632, 15), (652, 11), (672, 7)):
        o.append(line((-w, y), (w, y), "s"))
    # lunar axis: waxing — eclipse — waning
    o.append(crescent(0, 712, 19, "blade", "left"))
    o.append(circle(0, 778, 24, "s lock"))
    o.append(circle(0, 778, 12, "blade"))
    for deg in (0, 45, 135, 180, 225, 315):
        c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
        o.append(line((31 * c, 778 + 31 * s), (40 * c, 778 + 40 * s), "s"))
    o.append(crescent(0, 844, 19, "blade", "right"))
    # root
    o.append(path([(-18, 898), (0, 884), (18, 898)], "s"))
    o.append(path([(-27, 925), (0, 904), (27, 925)], "s"))
    o.append(path([(-50, 990), (0, 930), (50, 990)], "p"))
    o.append(line((0, 930), (0, 1002), "p"))
    o.append(both(line((43, 996), (57, 984), "h")))
    o.append(circle(0, 1018, 3.2, "blade"))
    # wing-root lock (drawn last so it sits over the arm-shafts)
    lock = diamond(0, 330, 30, 44, "p lock") + diamond(0, 330, 13, 19, "s") + circle(0, 330, 3, "blade")
    return "".join(o), lock, blades


# --------------------------------------------------------------------------- back: one wing

def rib(o, k, t, n):
    """Rib-stave o->k with an inward talon k->t and n kill-tally blades on the trailing side."""
    out = [path([o, k, t], "r")]
    u, v, cv, length = rib_frame(o, k)
    h = BLADE_W / 2
    for i in range(n):
        d = length - 14 - i * BLADE_STEP
        b = (o[0] + u[0] * d, o[1] + u[1] * d)
        out.append(path([(b[0] - u[0] * h, b[1] - u[1] * h), (b[0] + u[0] * h, b[1] + u[1] * h),
                         (b[0] + v[0] * BLADE_LEN, b[1] + v[1] * BLADE_LEN)], "blade", True))
        out.append(line(b, (b[0] + cv[0] * 13, b[1] + cv[1] * 13), "h"))      # counter-tick, ornament
    return "".join(out), n


def wing(unwrap=False):
    """Right wing (mirror for the left). Returns (svg, blade count)."""
    o, blades = [], 0
    o.append(path([LOCK, J1, J2], "p"))                       # arm-shaft
    o.append(line(J1, E_TRAP, "p"))                           # over the trapezius -> clavicle stave
    if not unwrap:
        o.append(line(J2, E_DELT, "p"))                       # round the deltoid cap -> deltoid stave
    # stave notches on the over-shoulder runs
    for a, b, ds in ((J1, E_TRAP, (48, 60, 72)), (J2, E_DELT, (52, 64))):
        if unwrap and b is E_DELT:
            continue
        u = unit(a, b)
        for d in ds:
            c = along(a, b, d)
            o.append(line((c[0] - u[1] * 9, c[1] + u[0] * 9), (c[0] + u[1] * 9, c[1] - u[0] * 9), "h"))
    for org, k, t, n in RIBS:
        s, c = rib(org, k, t, n)
        o.append(s); blades += c
    # one bead-lock on the bare upper run of the three inner ribs
    for org, k, _, _ in RIBS[1:]:
        u = unit(org, k)
        c = along(org, k, 46)
        o.append(diamond(c[0], c[1], 6.5, 13, "s lock", math.atan2(u[1], u[0]) - math.pi / 2))
    # joint locks
    for j, prev in ((J1, LOCK), (J2, J1)):
        u = unit(prev, j)
        rot = math.atan2(u[1], u[0]) - math.pi / 2
        o.append(diamond(j[0], j[1], 12, 20, "s lock", rot))
        o.append(circle(j[0], j[1], 2.6, "blade"))
    return "".join(o), blades


def back_design(unwrap=False):
    sp, lock, n1 = spine()
    wg, n2 = wing(unwrap)
    return both(wg) + sp + lock, n1 + 2 * n2


# --------------------------------------------------------------------------- front: chest lock

WEAVE_GAP, OVERSHOOT, SHORT = 10.0, 34.0, 18.0


def chest_staves(unwrap=False):
    """The four interlaced staves. Right pair runs down-left, left pair down-right.

    Weave: right clavicle stave passes OVER the left one at the top node and UNDER the left
    deltoid stave at the far corner; the left clavicle stave does the reverse on its side.
    """
    o = []
    n = math.hypot(1, M)
    for sx, over_top in ((1, True), (-1, False)):
        d = (-sx / n, M / n)                                  # travel direction toward / past the sternum
        e_trap, e_delt, knee = (sx * E_TRAP[0], E_TRAP[1]), (sx * E_DELT[0], E_DELT[1]), (sx * KNEE[0], KNEE[1])
        far, nearc = (-sx * HW, HEART[1]), (sx * HW, HEART[1])
        step = lambda p, k: (p[0] + d[0] * k, p[1] + d[1] * k)
        # clavicle stave: ridge -> top node -> far corner (+ overshoot)
        if over_top:      # over at the top node, under at the far corner
            o.append(line(e_trap, step(far, -WEAVE_GAP), "p"))
            o.append(line(step(far, WEAVE_GAP), step(far, OVERSHOOT), "p"))
        else:             # under at the top node, over at the far corner
            o.append(line(e_trap, step(TOP, -WEAVE_GAP), "p"))
            o.append(line(step(TOP, WEAVE_GAP), step(far, OVERSHOOT), "p"))
        # deltoid stave: shoulder cap -> knee -> near corner -> stops short of the lowest point
        stop = step(BOT, -SHORT)
        head = [knee] if unwrap else [e_delt, knee]
        if over_top:      # this side's deltoid stave ducks under the other clavicle stave
            o.append(path(head + [step(nearc, -WEAVE_GAP)], "p"))
            o.append(line(step(nearc, WEAVE_GAP), stop, "p"))
        else:
            o.append(path(head + [stop], "p"))
    return "".join(o)


def chest_half(unwrap=False):
    """Mirrored furniture of one side (ticks, pinions, crescent, knee lock)."""
    o = []
    dl = (-1 / math.hypot(1, M), M / math.hypot(1, M))        # unit vector, down-left along the staves
    # compass ticks on the clavicle stave
    for d in (38, 50, 62):
        c = along(E_TRAP, TOP, d)
        o.append(line((c[0] - dl[1] * 9, c[1] + dl[0] * 9), (c[0] + dl[1] * 9, c[1] - dl[0] * 9), "h"))
    if not unwrap:
        u = unit(KNEE, E_DELT)
        for d in (44, 56):
            c = along(KNEE, E_DELT, d)
            o.append(line((c[0] - u[1] * 9, c[1] + u[0] * 9), (c[0] + u[1] * 9, c[1] - u[0] * 9), "h"))
    # pectoral pinions hanging from the deltoid stave (notched, not tallied)
    for x, ln in PINIONS:
        a = (x, BOT[1] - M * x)
        b = (x - 8, a[1] + ln)
        u = unit(a, b)
        o.append(line(a, b, "r"))
        for d in (ln * 0.45, ln * 0.62):
            c = along(a, b, d)
            o.append(line(c, (c[0] + 11, c[1] + 9), "h"))
        o.append(diamond(b[0] + u[0] * 9, b[1] + u[1] * 9, 4.5, 9, "blade", math.atan2(u[1], u[0]) - math.pi / 2))
    # lunar ward between the two staves
    o.append(crescent(122, 230, 15, "blade", "left"))
    # knee lock
    u = unit(KNEE, (HW, HEART[1]))
    o.append(diamond(KNEE[0], KNEE[1], 10, 16, "s lock", math.atan2(u[1], u[0]) - math.pi / 2))
    o.append(circle(KNEE[0], KNEE[1], 2.4, "blade"))
    return "".join(o)


PINIONS = ((120, 78), (149, 86), (178, 90))


def pinion_tip(i):
    x, ln = PINIONS[i]
    return x - 8, BOT[1] - M * x + ln + 18


def chest_core():
    o = []
    # sacred heart-sigil: quartered eclipse inside the interlaced diamond
    o.append(both(line((28, HEART[1]), (HW - 20, HEART[1]), "h")))
    o.append(line((0, HEART[1] - 28), (0, TOP[1] + 20), "h"))
    o.append(line((0, HEART[1] + 28), (0, BOT[1] - 26), "h"))
    o.append(circle(0, HEART[1], 23, "s lock"))
    o.append(circle(0, HEART[1], 11, "blade"))
    # crown above the top node
    o.append(line((0, TOP[1] - 22), (0, TOP[1] - 42), "s"))
    o.append(chevron(TOP[1] - 42, 12, 10, "s"))
    o.append(circle(0, TOP[1] - 54, 3, "blade"))
    # below the open point: one hollow blade (outline only) and a dot
    o.append(path([(-5.5, BOT[1] + 14), (5.5, BOT[1] + 14), (0, BOT[1] + 66)], "s hollow", True))
    o.append(circle(0, BOT[1] + 80, 3, "blade"))
    return "".join(o)


def front_design(unwrap=False):
    return chest_staves(unwrap) + both(chest_half(unwrap)) + chest_core()


# --------------------------------------------------------------------------- text

CAP = "'Palatino Linotype','Book Antiqua',Palatino,Georgia,serif"
ITA = "Georgia,'Times New Roman',serif"


def text(x, y, s, cls, anchor="start", extra=""):
    return f'<text class="{cls}" x="{f(x)}" y="{f(y)}" text-anchor="{anchor}" {extra}>{esc(s)}</text>'


def wrap(s, n):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > n:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    return lines


def notes(x, y, items, width_chars, cls="it", lh=25, gap=11, bullet_cls="blade"):
    o = []
    for it in items:
        o.append(diamond(x + 5, y - 5, 4, 6.5, bullet_cls))
        for ln in wrap(it, width_chars):
            o.append(text(x + 22, y, ln, cls))
            y += lh
        y += gap
    return "".join(o), y


def callout(tx, ty, title, sub, anchor, targets, elbow=None):
    """Two-line label at (tx,ty) + hairline leader(s) from the label's inner end to each target."""
    o = [text(tx, ty, title, "cap", anchor), text(tx, ty + 23, sub, "it", anchor)]
    for i, tg in enumerate(targets):
        pts = [elbow[i]] if elbow and elbow[i] else []
        start = pts.pop(0) if pts else None
        o.append(path(([start] if start else []) + pts + [tg] if start else [tg, tg], "lead"))
        o.append(circle(tg[0], tg[1], 3.2, "leaddot"))
    return "".join(o)


def leader(pts):
    return path(pts, "lead") + circle(pts[-1][0], pts[-1][1], 3.2, "leaddot")


def svg_open(css):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f'<style>{css}</style>')


def ink_css(sel, p, s, r, h):
    return (f"{sel} .p{{stroke-width:{p}}}{sel} .s{{stroke-width:{s}}}"
            f"{sel} .r{{stroke-width:{r}}}{sel} .h{{stroke-width:{h}}}")


# --------------------------------------------------------------------------- sheet A: blueprint

def blueprint():
    BG, SKIN, BONE, ICE = "#141619", "#1B1F24", "#EDE6D6", "#A9C4D6"
    css = f"""
    .p,.s,.r,.h{{fill:none;stroke-linecap:round;stroke-linejoin:miter;stroke-miterlimit:8}}
    .p,.r{{stroke:{BONE}}} .s{{stroke:{BONE}}} .h{{stroke:{ICE}}} .web{{opacity:.55}}
    {ink_css('', 4.8, 2.3, 3.5, 1.5)}
    .blade{{fill:{BONE};stroke:none}} .lock{{fill:{SKIN}}} .hollow{{fill:{SKIN};stroke:{BONE};stroke-width:2.2}}
    .skin{{fill:{SKIN}}} .edge{{fill:none;stroke:#414955;stroke-width:1.6;stroke-linecap:round}}
    .guide{{fill:none;stroke:#2B3139;stroke-width:1.4;stroke-linecap:round}} .dash{{stroke-dasharray:3 9}}
    .collar{{fill:none;stroke:#6F8798;stroke-width:1.8;stroke-dasharray:9 6}} .stud{{fill:#6F8798}}
    text{{font-family:{CAP};fill:{BONE}}}
    .title{{font-size:46px;letter-spacing:13px}} .sub{{font-size:19px;letter-spacing:7px;fill:{ICE}}}
    .view{{font-size:25px;letter-spacing:9px}}
    .cap{{font-size:16px;letter-spacing:3.2px;fill:{BONE}}}
    .it{{font-family:{ITA};font-style:italic;font-size:16.5px;fill:#8FA3B3}}
    .capt{{font-family:{ITA};font-style:italic;font-size:18px;fill:#9DAEBB}}
    .lead{{fill:none;stroke:{ICE};stroke-width:1.1;opacity:.75}} .leaddot{{fill:{ICE}}}
    .rule{{stroke:#39414B;stroke-width:1.2}} .frame{{fill:none;stroke:#2E353E;stroke-width:1.5}}
    """
    S, TY = 1.1, 232
    CXB, CXF = 712, 2088
    o = [svg_open(css),
         '<defs><radialGradient id="vg" cx="50%" cy="46%" r="75%"><stop offset="0" stop-color="#1A1D22"/>'
         f'<stop offset="1" stop-color="{BG}"/></radialGradient></defs>',
         f'<rect class="bg" width="{W}" height="{H}" fill="{BG}"/><rect class="bg" width="{W}" height="{H}" fill="url(#vg)"/>',
         f'<rect class="frame" x="34" y="34" width="{W - 68}" height="{H - 68}"/>',
         text(W / 2, 104, "WINTER COURT WARLORD", "title", "middle"),
         text(W / 2, 142, "BINDRUNE STAVE & KILL-TALLY TATTOO  ·  BLUEPRINT", "sub", "middle"),
         f'<line class="rule" x1="{W / 2 - 520}" y1="166" x2="{W / 2 + 520}" y2="166"/>',
         f'<line class="rule" x1="{W / 2}" y1="250" x2="{W / 2}" y2="1500" stroke-dasharray="2 10"/>']

    back, n = back_design()
    assert n == 49, n
    for cx, view, art, name in ((CXB, "back", back, "BACK VIEW"),
                                (CXF, "front", front_design(), "FRONT  ·  CHEST VIEW")):
        o.append(text(cx, 214, name, "view", "middle"))
        o.append(f'<g transform="translate({cx},{TY}) scale({S})">{torso(view)}{art}</g>')

    def B(x, y): return (CXB + S * x, TY + S * y)
    def F(x, y): return (CXF + S * x, TY + S * y)

    def label(T, x, y, title, sub, anchor):
        px, py = T(x, y)
        return text(px, py, title, "cap", anchor) + text(px, py + 23, sub, "it", anchor)

    # ---- back callouts
    o.append(label(B, -152, 44, "CROWN BLADE", "the forty-ninth tally", "end"))
    o.append(leader([B(-144, 62), B(-7, 186)]))
    o.append(label(B, 166, 44, "OVER-SHOULDER STAVES", "both carry on to the chest", "start"))
    o.append(leader([B(170, 78), B(E_TRAP[0] + 5, E_TRAP[1] - 13)]))
    o.append(leader([B(262, 78), B(E_DELT[0] + 3, E_DELT[1] - 12)]))
    kt = blade_tip(0, 1)
    o.append(label(B, 352, kt[1], "KILL-TALLY BLADES", "4 rib-staves · 24 blades a wing", "start"))
    o.append(leader([B(344, kt[1]), B(kt[0] + 4, kt[1])]))
    o.append(label(B, -352, 772, "LUNAR AXIS", "waxing · eclipse · waning", "end"))
    o.append(leader([B(-344, 772), B(-47, 772)]))
    o.append(label(B, 352, 972, "SPLAYED ROOT", "lower lumbar", "start"))
    o.append(leader([B(344, 972), B(62, 972)]))
    # ---- front callouts
    o.append(label(F, -152, 44, "BARE THROAT", "no ink above the collar line", "end"))
    o.append(leader([F(-144, 62), F(-74, 104)]))
    o.append(label(F, 166, 44, "CLAVICLE STAVES", "arrive over the trapezius", "start"))
    o.append(leader([F(170, 78), F(E_TRAP[0] + 5, E_TRAP[1] - 13)]))
    o.append(label(F, 352, E_DELT[1], "DELTOID STAVES", "wrap the shoulder cap", "start"))
    o.append(leader([F(344, E_DELT[1]), F(E_DELT[0] + 4, E_DELT[1])]))
    o.append(label(F, -352, 452, "HEART-LOCK", "eclipse in an unclosed diamond", "end"))
    o.append(leader([F(-344, 452), F(-78, 452), F(-27, BOT[1] + 5)]))
    pt = pinion_tip(2)
    o.append(label(F, 352, pt[1] + 44, "PECTORAL PINIONS", "three a side, uncounted", "start"))
    o.append(leader([F(344, pt[1] + 44), F(pt[0] + 46, pt[1] + 44), F(pt[0] + 7, pt[1] + 7)]))

    # ---- captions
    o.append(text(CXB, 1464, "Lumbar root · lunar axis · stacked diamonds · wing-root lock · crown blade.", "capt", "middle"))
    o.append(text(CXB, 1492, "Two wings of four rib-staves fold down across the shoulder blades.", "capt", "middle"))
    o.append(text(CXF, 1464, "The clavicle staves cross at the sternum and weave through the deltoid staves.", "capt", "middle"))
    o.append(text(CXF, 1492, "The diamond’s lowest point is left open; one hollow blade hangs beneath it.", "capt", "middle"))

    # ---- legend strip
    o.append(f'<line class="rule" x1="160" y1="1540" x2="{W - 160}" y2="1540"/>')
    ly = 1590
    items = (("p", "PRIMARY STAVE"), ("r", "RIB-STAVE"), ("s", "RUNE-LOCK LINE"), ("h", "HAIRLINE TICK"),
             ("blade", "ONE BLADE = ONE KILL"), ("s hollow", "HOLLOW BLADE = UNCUT"))
    col = (W - 320) / len(items)
    for i, (cls, name) in enumerate(items):
        x = 160 + col * (i + 0.5)
        if cls == "blade":
            o.append(path([(x - 23, ly + 3.5), (x - 23, ly - 3.5), (x + 23, ly)], cls, True))
        elif cls == "s hollow":
            o.append(path([(x - 25, ly + 5.5), (x - 25, ly - 5.5), (x + 25, ly)], cls, True))
        else:
            o.append(line((x - 40, ly), (x + 40, ly), cls))
        o.append(text(x, ly + 34, name, "cap", "middle"))
    o.append(text(W / 2, 1676, "Tally roll, back:  4 + 6 + 7 + 7 = 24 to a wing  ·  24 + 24 + the crown blade = 49",
                  "capt", "middle"))
    o.append("</svg>")
    return "".join(o)


# --------------------------------------------------------------------------- sheet B: parchment stencil

def stencil():
    PAPER, INK = "#F5F0E6", "#111315"
    css = f"""
    .p,.s,.r,.h{{fill:none;stroke:{INK};stroke-linecap:round;stroke-linejoin:miter;stroke-miterlimit:8}}
    .web{{opacity:.8}}
    {ink_css('', 4.8, 2.2, 3.3, 1.25)}
    {ink_css('.dA', 3.8, 1.9, 2.7, 1.05)} {ink_css('.dB', 3.6, 1.8, 2.6, 1.0)} {ink_css('.dC', 3.8, 1.9, 2.7, 1.05)}
    .blade{{fill:{INK};stroke:none}} .lock{{fill:{PAPER}}} .hollow{{fill:{PAPER};stroke:{INK}}}
    text{{font-family:{CAP};fill:{INK}}}
    .title{{font-size:42px;letter-spacing:11px}} .sub{{font-size:18px;letter-spacing:6px;fill:#4B4A46}}
    .ph{{font-size:22px;letter-spacing:6px}} .pl{{font-size:15px;letter-spacing:4px;fill:#5A5852}}
    .cap{{font-size:14.5px;letter-spacing:2.6px}}
    .it{{font-family:{ITA};font-style:italic;font-size:17px;fill:#2A2B2B}}
    .sm{{font-family:{ITA};font-style:italic;font-size:15.5px;fill:#3B3B39}}
    .lead{{fill:none;stroke:{INK};stroke-width:1.1;opacity:.9}} .leaddot{{fill:{INK}}}
    .rule{{stroke:#8E877A;stroke-width:1.1;fill:none}} .frame{{fill:none;stroke:#8E877A;stroke-width:1.4}}
    .fold{{stroke:#6D675C;stroke-width:1.3;stroke-dasharray:14 5 2 5;fill:none}}
    .nohole{{fill:none;stroke:#6D675C;stroke-width:1.3;stroke-dasharray:5 5}}
    .reg{{fill:none;stroke:{INK};stroke-width:1.2}}
    """
    o = [svg_open(css),
         '<defs><radialGradient id="pg" cx="50%" cy="45%" r="78%"><stop offset="0" stop-color="#F8F4EB"/>'
         f'<stop offset=".7" stop-color="{PAPER}"/><stop offset="1" stop-color="#E9E1D0"/></radialGradient></defs>',
         f'<rect class="bg" width="{W}" height="{H}" fill="{PAPER}"/><rect class="bg" width="{W}" height="{H}" fill="url(#pg)"/>',
         f'<rect class="frame" x="34" y="34" width="{W - 68}" height="{H - 68}"/>',
         text(W / 2, 100, "WINTER COURT WARLORD  ·  FLAT STENCIL", "title", "middle"),
         text(W / 2, 138, "BACK · SPINE · WINGS · CHEST-LOCK, UNWRAPPED OVER THE SHOULDERS", "sub", "middle"),
         f'<line class="rule" x1="{W / 2 - 620}" y1="162" x2="{W / 2 + 620}" y2="162"/>']

    # ---------------- unwrapped master (left) ----------------
    Y0 = E_TRAP[1]                       # shoulder fold: the chest is flipped up about this line
    S, CX = 1.14, 535
    TYM = 214 + (2 * Y0 - (BOT[1] + 83) ) * -S      # chest's lowest dot becomes the top of the figure
    back, n = back_design(unwrap=True)
    assert n == 49, n
    apex = (E_DELT[0] + 24, Y0)
    knee_f = (KNEE[0], 2 * Y0 - KNEE[1])
    dart = both(path([J2, apex, knee_f], "p") + path([(apex[0] + 7, apex[1] - 9), (apex[0] + 7, apex[1] + 9)], "h"))
    fold = both(line((84, Y0), (E_TRAP[0] - 12, Y0), "fold") + line((E_TRAP[0] + 12, Y0), (apex[0] - 12, Y0), "fold")
                + line((apex[0] + 16, Y0), (apex[0] + 46, Y0), "fold"))
    hole = f'<ellipse class="nohole" cx="0" cy="{f(Y0)}" rx="68" ry="30"/>'
    o.append(f'<g transform="translate({CX},{f(TYM)}) scale({S})">{fold}{hole}'
             f'<g transform="translate(0,{f(2 * Y0)}) scale(1,-1)">{front_design(unwrap=True)}</g>{back}{dart}</g>')

    def Mm(x, y): return (CX + S * x, TYM + S * y)
    o.append(text(*Mm(0, Y0 + 4), "NO INK", "cap", "middle"))
    px, py = Mm(-apex[0] - 60, Y0 - 175)
    o.append(text(px, py, "CHEST · UNFOLDED UPWARD", "pl", "middle", f'transform="rotate(-90 {f(px)} {f(py)})"'))
    px, py = Mm(-apex[0] - 60, Y0 + 430)
    o.append(text(px, py, "BACK", "pl", "middle", f'transform="rotate(-90 {f(px)} {f(py)})"'))
    px, py = Mm(apex[0] + 46, Y0)
    px += 26
    o.append(text(px, py, "SHOULDER FOLD", "pl", "middle", f'transform="rotate(90 {f(px)} {f(py)})"'))
    o.append(text(CX, 1676, "Master line-work, 49 kill-tally blades. Chest panel is drawn flipped upward across the shoulder fold.",
                  "sm", "middle"))

    # panel dividers
    for x in (1030, 1500, 2120):
        o.append(f'<line class="rule" x1="{x}" y1="200" x2="{x}" y2="1690" stroke-dasharray="2 9"/>')

    # ---------------- A · the spine axis ----------------
    ax, asc = 1150, 1.5
    aty = 300 - 196 * asc
    sp, lock, _ = spine()
    stubs = both(path([LOCK, along(LOCK, J1, 52)], "p") + path([along(LOCK, J1, 59), along(LOCK, J1, 72)], "h"))
    o.append(text(1265, 232, "A · THE SPINE AXIS", "ph", "middle"))
    o.append(f'<g class="dA" transform="translate({ax},{f(aty)}) scale({asc})">{stubs}{sp}{lock}</g>')
    for y, edge, t1, t2 in ((214, 10, "CROWN BLADE", "49th tally"), (330, 36, "WING-ROOT LOCK", "wings branch here"),
                            (395, 22, "RUNE NOTCHES", None), (518, 38, "STACKED DIAMONDS", "quartered lattice"),
                            (652, 20, "VERTEBRA TICKS", None), (712, 24, "WAXING", None),
                            (778, 44, "ECLIPSE", "ring, disc, corona"), (844, 9, "WANING", None),
                            (914, 20, "ROOT BARBS", None), (984, 50, "SPLAYED ROOT", "lower lumbar")):
        py = aty + asc * y
        o.append(leader([(1262, py), (ax + asc * edge + 6, py)]))
        o.append(text(1272, py + 5, t1, "cap"))
        if t2:
            o.append(text(1272, py + 25, t2, "sm"))

    # ---------------- B · scapula wing-staves & kill-notches ----------------
    bx, bsc = 1566, 1.66
    bty = 312 - 132 * bsc
    wg, _ = wing()
    o.append(text(1810, 232, "B · THE SCAPULA WING-STAVES", "ph", "middle"))
    o.append(text(1810, 262, "& KILL-NOTCHES", "ph", "middle"))
    o.append('<defs><clipPath id="cb"><rect x="-34" y="120" width="380" height="570"/></clipPath></defs>')
    o.append(f'<g class="dB" transform="translate({bx},{f(bty)}) scale({bsc})"><g clip-path="url(#cb)">'
             f'{wg}{path([(-6, 252), (6, 252), (0, 176)], "blade", True)}{line((0, 252), (0, 290), "p")}'
             f'{chevron(264, 17, 12, "s")}{line((0, 372), (0, 420), "p")}{lock}</g></g>')

    def Bp(x, y): return (bx + bsc * x, bty + bsc * y)
    px, py = Bp(E_TRAP[0] + 12, E_TRAP[1] + 2)
    o.append(text(px, py, "TO CLAVICLE", "cap"))
    px, py = Bp(E_DELT[0] + 4, E_DELT[1] + 26)
    o.append(text(px, py, "TO DELTOID", "cap", "end"))
    px, py = Bp(J2[0] + 6, J2[1] - 34)
    o.append(text(px, py, "JOINT LOCK", "cap", "middle"))
    o.append(leader([(px, py + 7), Bp(J2[0] + 3, J2[1] - 22)]))
    kt = blade_tip(1, 0)
    px, py = Bp(kt[0] + 22, kt[1] + 22)
    o.append(text(px, py, "KILL-TALLY", "cap") + text(px, py + 20, "BLADES", "cap"))
    o.append(leader([Bp(kt[0] + 19, kt[1] + 16), Bp(kt[0] + 3, kt[1] + 3)]))
    kn = RIBS[2][1]
    px, py = Bp(kn[0] + 24, kn[1] + 34)
    o.append(text(px, py, "TALON KINK", "cap"))
    o.append(leader([Bp(kn[0] + 21, kn[1] + 27), Bp(kn[0] + 2, kn[1] + 6)]))
    ny = bty + bsc * 652 + 44
    s, nyb = notes(1528, ny, [
        "Arm-shaft: wing-root lock to joint lock to joint lock, then over the shoulder.",
        "Four rib-staves a wing, each ending in an inward talon kink.",
        "Kill-tally blades ride the trailing side only: 4 · 6 · 7 · 7 = 24 a wing.",
        "Hairline counter-ticks are ornament, not tallies. One bead-lock a rib.",
        "24 + 24 + the crown blade = 49.",
    ], 62)
    o.append(s)

    # D · one kill-notch, enlarged
    dy = nyb + 26
    o.append(f'<line class="rule" x1="1528" y1="{dy - 30}" x2="2092" y2="{dy - 30}"/>')
    o.append(text(1810, dy + 8, "D · THE KILL-NOTCH, ENLARGED", "ph", "middle"))
    sy = dy + 52
    o.append(line((1570, sy), (2050, sy), "p"))
    ca, sa = math.cos(BLADE_ANG), math.sin(BLADE_ANG)
    for bxn in (1625, 1740, 1855, 1970):
        o.append(path([(bxn - 8, sy), (bxn + 8, sy), (bxn + ca * 82, sy + sa * 82)], "blade", True))
        o.append(line((bxn, sy), (bxn + ca * 30, sy - sa * 30), "h"))
    o.append(text(1810, sy + 82, "Blade: a solid sliver 38° off the stave, point trailing to the talon.", "sm", "middle"))
    o.append(text(1810, sy + 105, "Counter-tick: a hairline on the leading side, never counted.", "sm", "middle"))
    # ---------------- C · sternum / heart convergence ----------------
    cx, csc = 2440, 1.3
    cty = 304 - 136 * csc
    o.append(text(cx, 232, "C · THE STERNUM / HEART", "ph", "middle"))
    o.append(text(cx, 262, "CONVERGENCE", "ph", "middle"))
    o.append('<defs><clipPath id="cc"><rect x="-224" y="130" width="448" height="370"/></clipPath></defs>')
    o.append(f'<g class="dC" transform="translate({cx},{f(cty)}) scale({csc})"><g clip-path="url(#cc)">'
             f'{front_design()}</g></g>')

    def Cp(x, y): return (cx + csc * x, cty + csc * y)
    px, py = Cp(34, 452)
    o.append(text(px, py, "HOLLOW BLADE", "cap"))
    o.append(leader([Cp(30, 448), Cp(8, 440)]))
    px, py = Cp(-34, 420)
    o.append(text(px, py, "OPEN POINT", "cap", "end"))
    o.append(leader([Cp(-30, 414), Cp(-5, BOT[1] - 1)]))
    ny = cty + csc * 500 + 40
    s, ny = notes(2148, ny, [
        "The clavicle staves cross above the heart, one over, one under, and run on to the far corners.",
        "Each deltoid stave turns at its knee lock, weaves through, and stops short: the lowest point stays open.",
        "Quartered eclipse at the heart; one hollow blade beneath, outline only.",
        "Three pinions a side hang from the deltoid stave: notched, uncounted.",
        "Nothing rises above the collar line. Throat and neck stay bare.",
    ], 62)
    o.append(s)
    # sheet key
    ky = ny + 40
    o.append(f'<line class="rule" x1="2148" y1="{ky - 30}" x2="2732" y2="{ky - 30}"/>')
    o.append(text(cx, ky + 8, "SHEET KEY", "ph", "middle"))
    ky += 64
    for cls, name in (("p", "PRIMARY STAVE"), ("r", "RIB-STAVE"), ("s", "RUNE-LOCK LINE"), ("h", "HAIRLINE TICK")):
        o.append(line((2200, ky - 5), (2290, ky - 5), cls))
        o.append(text(2320, ky, name, "cap"))
        ky += 42
    o.append(path([(2222, ky - 1), (2222, ky - 9), (2268, ky - 5)], "blade", True))
    o.append(text(2320, ky, "KILL-TALLY BLADE, SOLID", "cap"))
    ky += 42
    o.append(path([(2220, ky + 0.5), (2220, ky - 10.5), (2270, ky - 5)], "s hollow", True))
    o.append(text(2320, ky, "HOLLOW BLADE, OUTLINE ONLY", "cap"))
    ky += 42
    o.append(f'<line class="fold" x1="2200" y1="{ky - 5}" x2="2290" y2="{ky - 5}"/>')
    o.append(text(2320, ky, "SHOULDER FOLD / NO-INK ZONE", "cap"))
    o.append("</svg>")
    return "".join(o)


# --------------------------------------------------------------------------- render (Chrome CDP)

async def render(jobs, port=9222):
    """Render each (svg_path, png_path) in a temporary background tab, then close that tab."""
    import asyncio, base64, json, urllib.request
    import websockets

    ver = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version"))
    async with websockets.connect(ver["webSocketDebuggerUrl"], max_size=None) as ws:
        mid = 0

        async def call(method, params=None, sid=None):
            nonlocal mid
            mid += 1
            msg = {"id": mid, "method": method, "params": params or {}}
            if sid:
                msg["sessionId"] = sid
            await ws.send(json.dumps(msg))

            async def reply():
                while True:
                    r = json.loads(await ws.recv())
                    if r.get("id") == mid:
                        if "error" in r:
                            raise RuntimeError(f"{method}: {r['error']}")
                        return r["result"]
            return await asyncio.wait_for(reply(), 25)     # never hang with the temp tab left open

        async def shoot(svg_path, png_path):
            """One sheet in one fresh background tab; the tab is closed whatever happens."""
            tid = (await call("Target.createTarget", {"url": "about:blank", "background": True}))["targetId"]
            try:
                sid = (await call("Target.attachToTarget", {"targetId": tid, "flatten": True}))["sessionId"]
                await call("Emulation.setDeviceMetricsOverride",
                           {"width": W, "height": H, "deviceScaleFactor": 1, "mobile": False}, sid)
                frame = (await call("Page.getFrameTree", sid=sid))["frameTree"]["frame"]["id"]
                svg = open(svg_path, encoding="utf-8").read()
                html = ('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;'
                        'background:#000;overflow:hidden}svg{display:block}</style></head><body>'
                        + svg + "</body></html>")
                await call("Page.setDocumentContent", {"frameId": frame, "html": html}, sid)
                await call("Runtime.evaluate", {
                    # setTimeout, not requestAnimationFrame: rAF never fires in a background tab
                    "expression": "document.fonts.ready.then(()=>new Promise(r=>setTimeout(()=>r(1),250)))",
                    "awaitPromise": True}, sid)
                shot = await call("Page.captureScreenshot", {
                    "format": "png", "captureBeyondViewport": True,
                    "clip": {"x": 0, "y": 0, "width": W, "height": H, "scale": 1}}, sid)
                with open(png_path, "wb") as fh:
                    fh.write(base64.b64decode(shot["data"]))
                print("rendered", png_path)
            finally:
                await call("Target.closeTarget", {"targetId": tid})

        for job in jobs:
            for attempt in (1, 2, 3):          # a background-tab screenshot occasionally stalls; retry fresh
                try:
                    await shoot(*job)
                    break
                except asyncio.TimeoutError:
                    if attempt == 3:
                        raise
                    print("screenshot stalled, retrying", job[1])


def main():
    jobs = []
    for name, fn in (("winter_warlord_tattoo_blueprint", blueprint),
                     ("winter_warlord_tattoo_stencil_parchment", stencil)):
        p = os.path.join(HERE, name + ".svg")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(fn())
        print("wrote", p)
        jobs.append((p, os.path.join(HERE, name + ".png")))
    if "--render" in sys.argv:
        import asyncio
        asyncio.run(render(jobs))


if __name__ == "__main__":
    main()
