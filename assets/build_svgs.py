"""Generate the skyv26 profile SVG design system (light + dark variants).

Usage: python3 gen_svgs.py <repo_root>
Writes into <repo_root>/assets/{cover,projects,sections,matrix}/
"""
import os, sys

ROOT = sys.argv[1]
ACC = "#E76F36"
MUTED = "#8A8A85"
THEMES = {
    "light": {"ink": "#171717", "soft": "#64748B", "line": "#171717", "lineop": ".30", "gridop": ".07"},
    "dark": {"ink": "#F3F0E8", "soft": "#A3ACB9", "line": "#F3F0E8", "lineop": ".32", "gridop": ".08"},
}
FONT = "'Helvetica Neue', Helvetica, Inter, Arial, ui-sans-serif, system-ui, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def head(w, h, title, desc, t):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">
<title id="t">{esc(title)}</title>
<desc id="d">{esc(desc)}</desc>
<defs>
  <pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="{t['line']}" stroke-opacity="{t['gridop']}" stroke-width="1"/>
  </pattern>
</defs>
<style>
  .ink{{fill:{t['ink']}}} .soft{{fill:{t['soft']}}} .mut{{fill:{MUTED}}} .acc{{fill:{ACC}}}
  .ln{{stroke:{t['line']};stroke-opacity:{t['lineop']};fill:none}}
  .lns{{stroke:{t['ink']};fill:none}}
  .al{{stroke:{ACC};fill:none}}
  text{{font-family:{FONT}}}
  .mono{{font-family:{MONO}}}
</style>
<rect width="{w}" height="{h}" fill="url(#g)"/>
'''


def write(path, s):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(s)


# ---------------------------------------------------------------- project art
# Each art function draws into a 560x250 region; (ox, oy) is the region origin.

def art_crypto(ox, oy):
    s = f'<g transform="translate({ox} {oy})">'
    # chain of four blocks with hash cells
    for i in range(4):
        x = i * 140
        s += f'<rect x="{x}" y="70" width="100" height="100" class="lns" stroke-width="2"/>'
        for r in range(4):
            for c in range(4):
                if (r * 3 + c * 5 + i * 7) % 4 == 0:
                    s += f'<rect x="{x+14+c*19}" y="{84+r*19}" width="12" height="12" class="{"acc" if (r+c+i)%3==0 else "ink"}" opacity="{1 if (r+c+i)%3==0 else .55}"/>'
                else:
                    s += f'<rect x="{x+14+c*19}" y="{84+r*19}" width="12" height="12" class="ln"/>'
        s += f'<text x="{x}" y="196" class="mut mono" font-size="12" letter-spacing="1">0x0{i+1}</text>'
        if i < 3:
            s += f'<path d="M{x+100} 120H{x+140}" class="lns" stroke-width="2"/>'
    # payment arc
    s += '<path d="M50 60C50 0 470 0 470 60" class="al" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round"/>'
    s += '<circle cx="50" cy="60" r="7" class="acc"/><path d="M462 52L470 64L478 52" class="al" stroke-width="3"/>'
    s += '<text x="0" y="236" class="mut" font-size="12" letter-spacing="3">PAYMENT WORKFLOW / ABSTRACT</text>'
    return s + '</g>'


def art_hydro(ox, oy):
    s = f'<g transform="translate({ox} {oy})">'
    ys = [40, 90, 140, 190]
    for k, y in enumerate(ys):
        s += f'<path d="M0 {y}C90 {y-18} 160 {y+16} 260 {y}S430 {y-20} 560 {y+4}" class="ln" stroke-width="{2 if k%2==0 else 1}"/>'
    # stipple in one stratum
    for i in range(0, 560, 22):
        for j, yy in enumerate((108, 122)):
            s += f'<circle cx="{i + (11 if j else 0)}" cy="{yy}" r="1.6" class="ink" opacity=".45"/>'
    # water table
    s += '<path d="M0 74C120 64 260 84 560 70" class="al" stroke-width="3" stroke-dasharray="10 7"/>'
    s += '<path d="M392 52H416L404 66Z" class="acc"/><path d="M396 70H412M399 75H409" class="al" stroke-width="2"/>'
    # borehole
    s += '<rect x="180" y="0" width="16" height="220" class="lns" stroke-width="2" fill="none"/>'
    s += '<rect x="180" y="74" width="16" height="146" class="acc" opacity=".22"/>'
    for i, d in enumerate(range(0, 221, 44)):
        s += f'<path d="M196 {d}H212" class="lns"/><text x="218" y="{d+4}" class="mut mono" font-size="11">{i*20} m</text>'
    s += '<text x="0" y="246" class="mut" font-size="12" letter-spacing="3">STRATA / WATER TABLE / BOREHOLE — ABSTRACT</text>'
    return s + '</g>'


def art_edqio(ox, oy):
    s = f'<g transform="translate({ox} {oy})">'
    roles = ["PRN", "TCH", "PAR", "STU", "FIN", "ADM"]
    mods = ["REC", "ATT", "FEE", "RPT", "BUS"]
    for i, r in enumerate(roles):
        s += f'<text x="{48+i*30}" y="12" class="mut mono" font-size="10" text-anchor="middle">{r}</text>'
    for j, m in enumerate(mods):
        s += f'<text x="0" y="{40+j*32}" class="mut mono" font-size="10">{m}</text>'
        for i in range(6):
            on = (i * 2 + j * 3) % 5 in (0, 1, 3)
            acc = (i == 4 and j == 2) or (i == 0 and j == 3)
            cls = "acc" if acc else ("ink" if on else None)
            if cls:
                s += f'<rect x="{37+i*30}" y="{24+j*32}" width="22" height="22" class="{cls}" opacity="{1 if acc else .78}"/>'
            else:
                s += f'<rect x="{37+i*30}" y="{24+j*32}" width="22" height="22" class="ln"/>'
    # bus route
    pts = [(260, 190), (300, 120), (360, 140), (400, 70), (470, 90), (500, 30)]
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    s += f'<path d="{d}" class="lns" stroke-width="2" stroke-dasharray="1 0"/>'
    for k, (x, y) in enumerate(pts):
        s += f'<circle cx="{x}" cy="{y}" r="7" class="{"acc" if k==3 else "ink"}"/>' if k in (0, 3, 5) else f'<circle cx="{x}" cy="{y}" r="6" fill="none" stroke="{ACC}" stroke-width="2"/>'
    # verification code
    for r in range(5):
        for c in range(5):
            if (r * 7 + c * 3 + r * c) % 3 != 1 or (r in (0, 4) and c in (0, 4)):
                s += f'<rect x="{480+c*14}" y="{150+r*14}" width="12" height="12" class="ink" opacity=".85"/>'
    s += '<text x="0" y="246" class="mut" font-size="12" letter-spacing="3">ROLES × MODULES / ROUTES / VERIFIABLE REPORTS</text>'
    return s + '</g>'


def art_genuine(ox, oy):
    s = f'<g transform="translate({ox} {oy})">'
    for i in range(13):
        s += f'<path d="M{i*45} 0V220" class="ln" stroke-opacity=".14"/>'
    s += '<rect x="0" y="10" width="270" height="34" class="ink"/>'
    s += '<rect x="0" y="58" width="200" height="10" class="ln"/><rect x="0" y="76" width="235" height="10" class="ln"/><rect x="0" y="94" width="160" height="10" class="ln"/>'
    for i in range(3):
        s += f'<rect x="{i*90}" y="130" width="78" height="78" class="ln" stroke-width="2"/>'
        s += f'<text x="{i*90+10}" y="152" class="mut mono" font-size="11">S/0{i+1}</text>'
    # path to enquiry
    s += '<path d="M300 27H405V120H495V180" class="al" stroke-width="3"/>'
    s += '<circle cx="495" cy="192" r="14" class="acc"/>'
    s += '<rect x="360" y="150" width="70" height="46" class="lns" stroke-width="2"/><path d="M360 150L395 176L430 150" class="lns" stroke-width="2"/>'
    s += '<text x="0" y="246" class="mut" font-size="12" letter-spacing="3">POSITIONING / SERVICES / ENQUIRY</text>'
    return s + '</g>'


def art_smile(ox, oy):
    s = f'<g transform="translate({ox} {oy})">'
    for k in range(14):
        r, c = divmod(k, 7)
        x, y = c * 78, r * 78
        if k == 4:
            s += f'<rect x="{x}" y="{y}" width="64" height="64" class="acc"/>'
            s += f'<path d="M{x+32} {y+14}V{y+50}M{x+14} {y+32}H{x+50}" stroke="#FFFFFF" stroke-width="8"/>'
        else:
            s += f'<rect x="{x}" y="{y}" width="64" height="64" class="ln" stroke-width="{2 if k%3==0 else 1}"/>'
            s += f'<text x="{x+8}" y="{y+20}" class="mut mono" font-size="11">{k+1:02d}</text>'
    s += '<path d="M0 200H170L190 170L215 228L240 150L262 200H546" class="al" stroke-width="3" stroke-linejoin="round"/>'
    s += '<text x="0" y="246" class="mut" font-size="12" letter-spacing="3">14 CLINICAL SERVICES / LAB / INSURANCE / CARE</text>'
    return s + '</g>'


def art_horovista(ox, oy):
    s = f'<g transform="translate({ox} {oy})">'
    # North Indian chart: square, diagonals, inner diamond → 12 houses
    S = 200
    s += f'<rect x="0" y="10" width="{S}" height="{S}" class="lns" stroke-width="2"/>'
    s += f'<path d="M0 10L{S} {S+10}M{S} 10L0 {S+10}" class="lns" stroke-width="1.5"/>'
    s += f'<path d="M{S/2} 10L{S} {S/2+10}L{S/2} {S+10}L0 {S/2+10}Z" class="lns" stroke-width="1.5"/>'
    s += f'<path d="M{S/2} 10L{S*0.75} {S*0.25+10}L{S/2} {S/2+10}L{S*0.25} {S*0.25+10}Z" class="acc" opacity=".9"/>'
    s += f'<text x="{S/2}" y="{S*0.25+15}" class="mono" font-size="13" text-anchor="middle" fill="#FFFFFF">1</text>'
    # book
    s += '<g transform="translate(250 30)">'
    s += '<path d="M0 10Q70 -6 140 10V170Q70 154 0 170Z" class="lns" stroke-width="2"/>'
    s += '<path d="M140 10Q210 -6 280 10V170Q210 154 140 170Z" class="lns" stroke-width="2"/>'
    for i in range(6):
        s += f'<path d="M18 {38+i*20}H120" class="ln"/><path d="M160 {38+i*20}H{262 - (i%2)*30}" class="ln"/>'
    s += '<path d="M232 0V58L244 48L256 58V0" class="acc"/>'
    s += '</g>'
    s += '<path d="M250 222C320 196 460 196 530 222" class="al" stroke-width="2"/><circle cx="390" cy="203" r="6" class="acc"/>'
    s += '<text x="0" y="246" class="mut" font-size="12" letter-spacing="3">12 HOUSES / DASHA TIMELINE / DIGITAL BOOK</text>'
    return s + '</g>'


def art_finance(ox, oy):
    s = f'<g transform="translate({ox} {oy})">'
    # ingots
    s += '<path d="M10 120L30 80H130L150 120Z" class="acc"/><text x="80" y="110" class="mono" font-size="16" text-anchor="middle" fill="#FFFFFF">Au</text>'
    s += '<path d="M40 170L60 130H160L180 170Z" class="lns" stroke-width="2"/><text x="110" y="160" class="ink mono" font-size="16" text-anchor="middle">Ag</text>'
    # scale
    s += '<path d="M230 30V190M190 190H270M170 60H290" class="lns" stroke-width="2"/>'
    s += '<path d="M170 60L150 110H190Z M290 60L270 100H310Z" class="ln" stroke-width="1.5"/>'
    s += '<circle cx="230" cy="30" r="6" class="acc"/>'
    # ledger
    s += '<g transform="translate(340 20)">'
    s += '<rect width="210" height="170" class="lns" stroke-width="2"/><path d="M0 26H210M90 0V170M150 0V170" class="ln"/>'
    for i in range(5):
        y = 50 + i * 26
        s += f'<path d="M10 {y}H70M100 {y}H138M160 {y}H{200 - (i%3)*12}" class="ln"/>'
    s += '<rect x="150" y="104" width="60" height="26" class="acc" opacity=".85"/>'
    s += '<text x="10" y="18" class="mut mono" font-size="10">ITEM</text><text x="98" y="18" class="mut mono" font-size="10">WT g</text><text x="158" y="18" class="mut mono" font-size="10">VALUE</text>'
    s += '</g>'
    s += '<text x="0" y="246" class="mut" font-size="12" letter-spacing="3">VALUATION / INVENTORY / LOANS / MULTI-TENANT</text>'
    return s + '</g>'


def art_ai(ox, oy):
    s = f'<g transform="translate({ox} {oy})">'
    cx, cy, R = 120, 110, 80
    nodes = [("PLAN", 0, -1), ("TOOL", 1, 0), ("RETRIEVE", 0, 1), ("RESPOND", -1, 0)]
    s += f'<circle cx="{cx}" cy="{cy}" r="{R}" class="ln" stroke-width="2"/>'
    for i, (n, dx, dy) in enumerate(nodes):
        x, y = cx + dx * R, cy + dy * R
        s += f'<circle cx="{x}" cy="{y}" r="11" class="{"acc" if i==2 else "ink"}"/>'
        tx = x + (18 if dx >= 0 else -18)
        anchor = "start" if dx >= 0 else "end"
        if dx == 0 and dy < 0:
            tx, anchor = x + 18, "start"
        if dx == 0 and dy > 0:
            tx, anchor = x - 18, "end"
        s += f'<text x="{tx}" y="{y+4}" class="mut mono" font-size="11" text-anchor="{anchor}">{n}</text>'
    # embedding cloud
    import random
    rnd = random.Random(7)
    pts = [(300 + rnd.random() * 240, 20 + rnd.random() * 190) for _ in range(70)]
    q = (420, 110)
    near = sorted(pts, key=lambda p: (p[0]-q[0])**2 + (p[1]-q[1])**2)[:5]
    for p in pts:
        if p in near:
            continue
        s += f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="2.6" class="ink" opacity=".5"/>'
    for p in near:
        s += f'<path d="M{q[0]} {q[1]}L{p[0]:.1f} {p[1]:.1f}" class="al" stroke-width="1.5"/><circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="5" class="acc"/>'
    s += f'<rect x="{q[0]-7}" y="{q[1]-7}" width="14" height="14" class="ink"/>'
    s += f'<path d="M{cx+R+11} {cy+R*0.0}" />'
    s += '<path d="M131 196C210 236 340 226 410 122" class="al" stroke-width="2" stroke-dasharray="4 6"/>'
    s += '<text x="0" y="246" class="mut" font-size="12" letter-spacing="3">AGENT LOOP / EMBEDDINGS / RETRIEVAL</text>'
    return s + '</g>'


PROJECTS = [
    # slug, number, domain, name lines, status, art fn, mirror(art on left), title
    ("crypto-payments", "01", "FINANCIAL TECHNOLOGY", ["CRYPTO", "PAYMENT PLATFORM"], "DEPLOYED / LINK PENDING", art_crypto, False),
    ("hydrogeology", "02", "SCIENTIFIC SOFTWARE", ["HYDROGEOLOGY", "PROJECTS APP"], "DEPLOYED / LINK PENDING", art_hydro, True),
    ("edqio", "03", "EDUCATION TECHNOLOGY / SAAS", ["EDQIO"], "LIVE / EDQIO.COM", art_edqio, False),
    ("genuine-consultancy", "04", "PROFESSIONAL SERVICES", ["GENUINE", "CONSULTANCY SERVICES"], "LIVE PRODUCT", art_genuine, True),
    ("smile-dmi", "05", "HEALTHCARE / INSTITUTIONAL", ["SMILE", "MEDICAL HOSPITAL"], "LIVE / SMILEDMI-SL.COM", art_smile, False),
    ("horovista", "06", "ASTROLOGY / OWN PRODUCT", ["HOROVISTA"], "LIVE / HOROVISTA.COM", art_horovista, True),
    ("jewellery-finance", "A", "FINTECH / SAAS — IN DEVELOPMENT", ["JEWELLERY", "FINANCE SAAS"], "IN DEVELOPMENT", art_finance, False),
    ("ai-systems", "B", "AI ENGINEERING — R&amp;D", ["AI ASSISTANTS", "&amp; AGENTS"], "EXPERIMENTS / R&amp;D", art_ai, True),
]


def project_svg(p, t):
    slug, num, domain, name, status, fn, mirror = p
    W, H = 1200, 340
    plain_name = " ".join(name).replace("&amp;", "&")
    s = head(W, H, f"{num} — {plain_name}", f"Abstract editorial artwork for {plain_name} ({domain.replace('&amp;','&').lower()}).", t)
    tx = 640 if mirror else 48       # text column origin
    ax = 48 if mirror else 600       # art origin
    s += f'<path d="M0 1H1200M0 339H1200" class="ln" stroke-width="2"/>'
    s += f'<path d="M{(600 if mirror else 600) - 24} 30V310" class="ln"/>'
    s += f'<text x="{tx}" y="58" class="mut" font-size="13" letter-spacing="4">{num} / {domain}</text>'
    s += f'<text x="{tx - 6}" y="{200 if len(name) > 1 else 205}" class="acc" font-size="150" font-weight="800" letter-spacing="-8" opacity=".95">{num}</text>'
    ny = 248 if len(name) > 1 else 276
    for i, line in enumerate(name):
        s += f'<text x="{tx}" y="{ny + i*38}" class="ink" font-size="36" font-weight="750" letter-spacing="-1">{line}</text>'
    s += f'<rect x="{tx}" y="74" width="40" height="4" class="acc"/>'
    s += f'<text x="{tx + 54}" y="80" class="ink" font-size="12" letter-spacing="3" font-weight="700">{status}</text>'
    s += fn(ax, 60)
    s += '</svg>\n'
    return s


# ---------------------------------------------------------------- cover

def cover_svg(t):
    W, H = 1200, 420
    s = head(W, H, "Aakash Verma — engineering journal cover", "Editorial cover: Aakash Verma, software engineer, full-stack developer, AI systems and product architecture.", t)
    s += '<path d="M0 1H1200M0 419H1200" class="ln" stroke-width="2"/>'
    s += '<text x="48" y="58" class="mut" font-size="13" letter-spacing="4">ENGINEERING JOURNAL / ISSUE 002 / DEPLOYED WORK</text>'
    s += '<text x="44" y="168" class="ink" font-size="104" font-weight="800" letter-spacing="-5">AAKASH</text>'
    s += '<text x="44" y="268" class="ink" font-size="104" font-weight="800" letter-spacing="-5">VERMA<tspan class="acc">.</tspan></text>'
    s += '<text x="48" y="318" class="soft" font-size="17" letter-spacing="2.5">SOFTWARE ENGINEER  /  FULL-STACK DEVELOPER</text>'
    s += '<text x="48" y="346" class="soft" font-size="17" letter-spacing="2.5">AI SYSTEMS &amp; PRODUCT ARCHITECTURE</text>'
    s += '<path d="M48 384H520" class="al" stroke-width="4"/>'
    # right composition: six domains as an index column
    doms = ["EDUCATION", "HEALTHCARE", "FINTECH", "SCIENCE", "SERVICES", "ASTROLOGY"]
    s += '<path d="M760 30V390" class="ln"/>'
    for i, d in enumerate(doms):
        y = 86 + i * 50
        s += f'<path d="M760 {y+14}H1152" class="ln" stroke-opacity=".18"/>'
        s += f'<text x="780" y="{y}" class="acc mono" font-size="13">0{i+1}</text>'
        s += f'<text x="826" y="{y}" class="ink" font-size="20" font-weight="700" letter-spacing="2">{d}</text>'
        ref = ["P.03", "P.05", "P.01 / A", "P.02", "P.04", "P.06"][i]
        s += f'<text x="1152" y="{y}" class="mut mono" font-size="13" text-anchor="end">{ref}</text>'
    s += '<text x="1152" y="400" class="mut" font-size="12" letter-spacing="3" text-anchor="end">SIX DOMAINS / ONE ENGINEER / SKYV26</text>'
    s += '</svg>\n'
    return s


# ---------------------------------------------------------------- section bands (theme-neutral)
SECTIONS = [
    ("00", "WHO / WHY"), ("01", "PROOF OF WORK"), ("02", "WORK IN PROGRESS"), ("03", "EVIDENCE"),
    ("04", "TOOLS"), ("05", "THINKING"), ("06", "PEOPLE"), ("07", "SIGNAL"),
    ("08", "IDEAS"), ("09", "SKYBREL"), ("10", "SAY HELLO"),
]


def section_svg(num, kicker):
    W, H = 1200, 96
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Section {num}">
<style>text{{font-family:{FONT}}}</style>
<path d="M0 94H1200" stroke="{MUTED}" stroke-opacity=".55" stroke-width="2"/>
<text x="0" y="84" fill="{ACC}" font-size="96" font-weight="800" letter-spacing="-6">{num}</text>
<rect x="150" y="66" width="12" height="12" fill="{ACC}"/>
<text x="176" y="78" fill="{MUTED}" font-size="14" letter-spacing="5">{kicker}</text>
<text x="1200" y="78" fill="{MUTED}" font-size="14" letter-spacing="4" text-anchor="end">{num} / 10</text>
</svg>
'''
    return s


# ---------------------------------------------------------------- matrix

COLS = ["01", "02", "03", "04", "05", "06", "A", "B"]
COLNAMES = ["CRYPTO", "HYDRO", "EDQIO", "GENUINE", "SMILE", "HOROVISTA", "JEWEL FIN", "AI R&amp;D"]
# V verified on live product, S stated by author / pending verification, E exploration / in development
ROWS = [
    ("APPLICATION ENGINEERING", "S S V S V V E E"),
    ("FINTECH &amp; FINANCIAL", "S . V . . V E ."),
    ("EDUCATION &amp; INSTITUTIONAL", ". . V S V . . ."),
    ("SCIENTIFIC &amp; SPECIALISED", ". S . . . V . ."),
    ("AI &amp; INTELLIGENT SYSTEMS", ". . . . . S . E"),
    ("INFRASTRUCTURE &amp; DELIVERY", "S S V V V V . ."),
]


def matrix_svg(t):
    W = 1200
    top = 120
    rowh = 52
    H = top + rowh * len(ROWS) + 90
    s = head(W, H, "Engineering in Practice matrix", "Matrix mapping six engineering capability areas to the projects that evidence them. Filled square: verified on the live product. Half square: stated by the author, pending public verification. Outline: in development or exploration.", t)
    s += '<path d="M0 1H1200" class="ln" stroke-width="2"/>'
    s += '<text x="0" y="40" class="mut" font-size="13" letter-spacing="4">CAPABILITY × EVIDENCE</text>'
    x0, cw = 420, 97
    for i, (c, n) in enumerate(zip(COLS, COLNAMES)):
        x = x0 + i * cw + cw / 2
        s += f'<text x="{x}" y="84" class="acc mono" font-size="15" text-anchor="middle" font-weight="700">{c}</text>'
        s += f'<text x="{x}" y="104" class="mut" font-size="10.5" letter-spacing="1" text-anchor="middle">{n}</text>'
        s += f'<path d="M{x0 + i*cw} 70V{top + rowh*len(ROWS)}" class="ln" stroke-opacity=".12"/>'
    s += f'<path d="M{x0 + 6*cw} 64V{top + rowh*len(ROWS)}" class="ln" stroke-dasharray="3 5"/>'
    for r, (name, marks) in enumerate(ROWS):
        y = top + r * rowh
        s += f'<path d="M0 {y}H1200" class="ln" stroke-opacity=".22"/>'
        s += f'<text x="0" y="{y+32}" class="ink" font-size="15" font-weight="700" letter-spacing="1.5">{name}</text>'
        for i, m in enumerate(marks.split()):
            x = x0 + i * cw + cw / 2 - 9
            yy = y + 17
            if m == "V":
                s += f'<rect x="{x}" y="{yy}" width="18" height="18" class="acc"/>'
            elif m == "S":
                s += f'<rect x="{x}" y="{yy}" width="18" height="18" fill="none" stroke="{ACC}" stroke-width="2"/><path d="M{x} {yy}H{x+18}V{yy+18}Z" class="acc"/>'
            elif m == "E":
                s += f'<rect x="{x+1}" y="{yy+1}" width="16" height="16" class="lns" stroke-width="2" stroke-dasharray="3 3"/>'
    yb = top + rowh * len(ROWS)
    s += f'<path d="M0 {yb}H1200" class="ln" stroke-width="2"/>'
    ly = yb + 46
    s += f'<rect x="0" y="{ly-14}" width="16" height="16" class="acc"/><text x="26" y="{ly}" class="soft" font-size="13" letter-spacing="1.5">VERIFIED ON THE LIVE PRODUCT</text>'
    s += f'<rect x="330" y="{ly-14}" width="16" height="16" fill="none" stroke="{ACC}" stroke-width="2"/><path d="M330 {ly-14}H346V{ly+2}Z" class="acc"/><text x="356" y="{ly}" class="soft" font-size="13" letter-spacing="1.5">STATED / PENDING PUBLIC VERIFICATION</text>'
    s += f'<rect x="731" y="{ly-13}" width="14" height="14" class="lns" stroke-width="2" stroke-dasharray="3 3"/><text x="756" y="{ly}" class="soft" font-size="13" letter-spacing="1.5">IN DEVELOPMENT / EXPLORATION</text>'
    s += '</svg>\n'
    return s


if __name__ == "__main__":
    A = os.path.join(ROOT, "assets")
    for th, t in THEMES.items():
        write(f"{A}/cover/cover-{th}.svg", cover_svg(t))
        write(f"{A}/matrix/engineering-matrix-{th}.svg", matrix_svg(t))
        for p in PROJECTS:
            write(f"{A}/projects/{p[0]}-{th}.svg", project_svg(p, t))
    for num, k in SECTIONS:
        write(f"{A}/sections/section-{num}.svg", section_svg(num, k))
    print("ok")
