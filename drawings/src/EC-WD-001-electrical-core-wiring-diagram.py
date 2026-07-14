"""Generate EC-WD-001 from the controlled electrical-core BOM baseline."""

import csv
from pathlib import Path

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth

REPO_ROOT = Path(__file__).resolve().parents[2]
BOM_PATH = REPO_ROOT / "calculations" / "electrical-core-bom.csv"
OUT = REPO_ROOT / "drawings" / "export" / "EC-WD-001-electrical-core-wiring-diagram.pdf"
PAGE = landscape(A3)
W, H = PAGE

INK = HexColor("#1E2933")
MUTED = HexColor("#66737F")
GRID = HexColor("#CBD3DA")
LIGHT = HexColor("#F5F7F9")
RED = HexColor("#D63C32")
BLACK = HexColor("#20262C")
BLUE = HexColor("#1677B8")
GREEN = HexColor("#277A53")
ORANGE = HexColor("#C76B16")
PURPLE = HexColor("#6E55A3")
TEAL = HexColor("#177D82")
YELLOW = HexColor("#FFF4C7")
ROSE = HexColor("#FCE9E6")
CYAN = HexColor("#E7F5F5")
LAV = HexColor("#EFECF8")


def t(c, x, y, s, size=8, color=INK, font="Helvetica", align="left"):
    c.setFillColor(color)
    c.setFont(font, size)
    if align == "center":
        c.drawCentredString(x, y, s)
    elif align == "right":
        c.drawRightString(x, y, s)
    else:
        c.drawString(x, y, s)


def wrap(c, x, y, s, width, size=7, leading=None, color=INK, font="Helvetica"):
    leading = leading or size * 1.25
    words, lines, line = s.split(), [], ""
    for word in words:
        trial = (line + " " + word).strip()
        if stringWidth(trial, font, size) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    for i, ln in enumerate(lines):
        t(c, x, y - i * leading, ln, size, color, font)
    return y - len(lines) * leading


def header(c, title, subtitle, page, total=7):
    t(c, 30, H - 30, title, 18, INK, "Helvetica-Bold")
    t(c, 30, H - 46, subtitle, 8, MUTED)
    t(c, W - 30, H - 30, "DRAWING: EC-WD-001  |  REV A", 8, MUTED, "Helvetica-Bold", "right")
    c.setStrokeColor(GRID)
    c.line(25, 38, W - 25, 38)
    t(c, 30, 22, "Source: electrical-core-bom.csv | Connection-level design development drawing", 7, MUTED)
    t(c, W - 30, 22, f"Page {page} of {total}", 7, MUTED, align="right")


def section(c, x, y, w, h, title, fill=LIGHT):
    c.setFillColor(fill)
    c.setStrokeColor(GRID)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 7, fill=1, stroke=1)
    t(c, x + 10, y + h - 16, title, 10, INK, "Helvetica-Bold")


def comp(c, x, y, w, h, cid, name, candidate="", terminals=None, fill=white, accent=INK):
    c.setFillColor(fill)
    c.setStrokeColor(accent)
    c.setLineWidth(1.15)
    c.roundRect(x, y, w, h, 5, fill=1, stroke=1)
    c.setFillColor(accent)
    c.roundRect(x + 4, y + h - 20, 53, 16, 3, fill=1, stroke=0)
    t(c, x + 30.5, y + h - 15, cid, 7.2, white, "Helvetica-Bold", "center")
    t(c, x + 63, y + h - 15, name, 8.3, INK, "Helvetica-Bold")
    yy = y + h - 32
    if candidate:
        yy = wrap(c, x + 7, yy, candidate, w - 14, 6.4, 7.6, MUTED)
    if terminals:
        yy -= 3
        for label, desc in terminals:
            c.setFillColor(HexColor("#E9EDF0"))
            c.roundRect(x + 7, yy - 2, 55, 12, 2, fill=1, stroke=0)
            t(c, x + 34.5, yy + 1.5, label, 6.2, accent, "Helvetica-Bold", "center")
            t(c, x + 67, yy + 1.5, desc, 6.1, INK)
            yy -= 14


def node(c, x, y, color):
    c.setFillColor(color)
    c.setStrokeColor(white)
    c.circle(x, y, 3, fill=1, stroke=1)


def wire(c, pts, color, label="", label_xy=None, width=2, dashed=False, arrow=False):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.setDash(5, 3) if dashed else c.setDash()
    p = c.beginPath()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    c.drawPath(p, stroke=1, fill=0)
    c.setDash()
    if arrow and len(pts) >= 2:
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        import math
        a = math.atan2(y2-y1, x2-x1)
        for da in (2.55, -2.55):
            c.line(x2, y2, x2 + 7*math.cos(a+da), y2 + 7*math.sin(a+da))
    if label and label_xy:
        fs = 6.2
        tw = stringWidth(label, "Helvetica-Bold", fs)
        c.setFillColor(white)
        c.rect(label_xy[0]-2, label_xy[1]-2, tw+4, 9, fill=1, stroke=0)
        t(c, label_xy[0], label_xy[1], label, fs, color, "Helvetica-Bold")


def hold(c, x, y, w, text):
    c.setFillColor(YELLOW)
    c.setStrokeColor(ORANGE)
    c.roundRect(x, y, w, 28, 4, fill=1, stroke=1)
    t(c, x + 7, y + 17, "DESIGN HOLD", 6.6, ORANGE, "Helvetica-Bold")
    wrap(c, x + 70, y + 18, text, w - 77, 6.2, 7, INK)


def draw_overview(c):
    header(c, "ELECTRICAL CORE - SYSTEM INTERCONNECTION OVERVIEW",
           "48 Vdc storage core | 800 W PV | 230 Vac inverter/charger | dual isolated 12 V service buses", 1)
    section(c, 25, 595, 340, 180, "ROOF / PV GENERATION", YELLOW)
    section(c, 385, 595, 300, 180, "48 V CHARGING", CYAN)
    section(c, 705, 415, 460, 360, "48 V STORAGE + PROTECTED DISTRIBUTION", LAV)
    section(c, 25, 255, 660, 315, "230 V SHORE + INVERTER/CHARGER", ROSE)
    section(c, 705, 225, 460, 165, "DUAL 12 V SERVICES", CYAN)
    section(c, 705, 55, 460, 150, "MONITORING / CONTROL", LIGHT)

    comp(c, 45, 650, 140, 80, "EC-001", "PV module x4", "Renogy ShadowFlux 200 W each", [("PV+/PV-", "4S string provisional"), ("FRAME", "protective bond")])
    comp(c, 205, 650, 140, 80, "EC-004", "PV isolation + SPD", "all-pole 250 Vdc isolator; conditional Type 2 SPD", [("IN+/IN-", "from roof"), ("OUT+/OUT-", "to MPPT"), ("PE", "bond")])
    comp(c, 405, 640, 260, 100, "EC-005", "MPPT charger", "Victron SmartSolar MPPT 250/60-Tr", [("PV+/PV-", "PV input"), ("BAT+/BAT-", "48 V output"), ("REMOTE H/L", "BMS ATC"), ("VE.Direct", "Cerbo")], fill=HexColor("#EAF3FA"), accent=BLUE)

    comp(c, 735, 640, 180, 95, "EC-006", "LFP battery x2", "Victron Lithium NG 51.2 V 100 Ah; parallel", [("+/−", "power terminals"), ("BMS A/B", "3-pole loop")])
    comp(c, 930, 640, 205, 95, "EC-008A", "Lynx Distributor", "battery-side aggregation", [("BR1/BR2", "fused batteries"), ("BUS+/BUS-", "to BMS")])
    comp(c, 735, 510, 180, 95, "EC-009", "Lynx Smart BMS NG", "500 A M10; contactor/shunt/pre-charge", [("LEFT BUS", "battery side"), ("RIGHT BUS", "system side"), ("I/O 1-13", "ATC/ATD/AUX"), ("VE.Can", "Cerbo")], fill=HexColor("#EAF3FA"), accent=BLUE)
    comp(c, 930, 500, 205, 105, "EC-008B", "Lynx Distributor", "load-side protected distribution", [("BR1 125 A", "MultiPlus"), ("BR2 25 A", "MPPT"), ("BR3 25 A", "EC-015 converter sub-distribution"), ("BR4", "reserved for EC-018; unpopulated")])

    comp(c, 45, 425, 200, 90, "EC-014", "Shore inlet + AC protection", "CEE 16 A inlet; 2-pole switch/RCBO enclosure", [("L/N/PE IN", "shore"), ("L/N/PE OUT", "MultiPlus AC-IN")])
    comp(c, 280, 390, 260, 125, "EC-010", "Inverter charger", "Victron MultiPlus-II 48/3000/35-32 230 V", [("DC+/DC-", "Lynx BR1"), ("AC-IN L/N/PE", "shore panel"), ("AC-OUT1 L/N/PE", "protected loads"), ("VE.Bus", "Cerbo")], fill=HexColor("#EAF3FA"), accent=BLUE)
    comp(c, 565, 420, 95, 70, "EC-014", "AC loads", "output RCBOs", [("L/N/PE", "circuits")])

    comp(c, 735, 300, 180, 65, "EC-011A", "48/12 V converter", "Orion-Tr Smart isolated 30 A; essential", [("IN+/IN-", "EC-015A branch A"), ("OUT+/OUT-", "EC-012A")])
    comp(c, 930, 300, 205, 65, "EC-012A", "12-circuit fuse block", "Blue Sea 5026; essential bus", [("P+/N-", "feed"), ("C1-C12", "branch loads")])
    comp(c, 735, 235, 180, 65, "EC-011B", "48/12 V converter", "Orion-Tr Smart isolated 30 A; non-essential", [("IN+/IN-", "EC-015A branch B"), ("OUT+/OUT-", "EC-012B")])
    comp(c, 930, 235, 205, 65, "EC-012B", "12-circuit fuse block", "Blue Sea 5026; non-essential bus", [("P+/N-", "feed"), ("C1-C12", "branch loads")])

    comp(c, 735, 72, 200, 110, "EC-013A", "Cerbo GX MK2", "system controller", [("POWER +/−", "BMS AUX"), ("VE.Can", "BMS"), ("VE.Bus", "MultiPlus"), ("VE.Direct 1", "MPPT"), ("HDMI+USB", "GX Touch")])
    comp(c, 955, 87, 180, 80, "EC-013B", "GX Touch 50 + sensors", "display plus four temperature sensors", [("HDMI/USB", "Cerbo"), ("TEMP 1-4", "Cerbo inputs")])

    # Major flows
    wire(c, [(185,690),(205,690)], RED, "PV DC", (186,696), arrow=True)
    wire(c, [(345,690),(375,690),(375,690),(405,690)], RED, arrow=True)
    wire(c, [(535,640),(535,615),(1030,615),(1030,605)], RED, "48 V charge via BR2", (670,611), arrow=True)
    wire(c, [(915,687),(930,687)], RED, arrow=True)
    wire(c, [(1030,640),(1030,620),(825,620),(825,605)], RED, arrow=True)
    wire(c, [(915,557),(930,557)], RED, "protected 48 V bus", (916,563), arrow=True)
    wire(c, [(930,535),(690,535),(690,455),(540,455)], RED, "BR1 125 A", (765,531), arrow=True)
    wire(c, [(930,520),(700,520),(700,332),(735,332)], RED, "BR3 25 A via EC-015A", (770,516), arrow=True)
    wire(c, [(700,332),(710,332),(710,267),(735,267)], RED, "split: 20 A each", (712,285), arrow=True)
    wire(c, [(245,465),(280,465)], ORANGE, "AC-IN", (248,471), arrow=True)
    wire(c, [(540,455),(565,455)], ORANGE, "AC-OUT1", (538,461), arrow=True)
    wire(c, [(915,332),(930,332)], RED, arrow=True)
    wire(c, [(915,267),(930,267)], RED, arrow=True)
    wire(c, [(835,80),(835,55)], BLUE, "data/control network - see page 5", (840,60), dashed=True)

    hold(c, 30, 205, 620, "PV string configuration, all fuse interrupt ratings, the service-isolation device and final AC protection are not released by the BOM and require engineering sign-off.")
    wrap(c, 35, 180, "EC-002 roof mounting, EC-003 PV wiring/gland, EC-007 battery enclosure, EC-015 protection/isolation, EC-016 harnesses and EC-017 equipment panels are installation assemblies represented by the connected equipment and notes. EC-018 vehicle-source charger has quantity 0 and is not connected.", 610, 7, 9, MUTED)


def draw_dc_core(c):
    header(c, "48 V BATTERY, BMS AND LYNX DISTRIBUTION",
           "Power terminals, branch assignments, BMS communication loop and 13-pin I/O application", 2)
    section(c, 25, 425, 540, 350, "BATTERY SIDE", LAV)
    section(c, 585, 425, 580, 350, "SYSTEM / LOAD SIDE", CYAN)
    section(c, 25, 55, 1140, 345, "EC-009 LYNX SMART BMS NG - CONNECTION DETAIL", LIGHT)

    comp(c, 45, 610, 190, 120, "EC-006-1", "LFP battery 1", "51.2 V 100 Ah", [("BAT+ M8", "to EC-008A BR1+"), ("BAT− M8", "to BR1−"), ("BMS-A/B", "3-pole circular")])
    comp(c, 45, 460, 190, 120, "EC-006-2", "LFP battery 2", "51.2 V 100 Ah", [("BAT+ M8", "to EC-008A BR2+"), ("BAT− M8", "to BR2−"), ("BMS-A/B", "3-pole circular")])
    comp(c, 300, 515, 235, 190, "EC-008A", "Lynx Distributor M10", "battery-side aggregation", [("BR1+ F1 125 A", "battery 1 positive; 35 mm²"), ("BR1−", "battery 1 negative; 35 mm²"), ("BR2+ F2 125 A", "battery 2 positive; 35 mm²"), ("BR2−", "battery 2 negative; 35 mm²"), ("BR3/4", "spare - mark not used"), ("RIGHT BUS+/−", "to BMS LEFT BUS")], fill=white, accent=PURPLE)
    comp(c, 605, 540, 225, 165, "EC-009", "Lynx Smart BMS NG", "500 A M10", [("LEFT BUS+/−", "battery/source side"), ("RIGHT BUS+/−", "system/load side"), ("BMS PORT A/B", "3-pole loop ends"), ("RJ10 A/B", "distributor monitoring"), ("VE.Can RJ45", "Cerbo GX"), ("I/O 1-13", "shown below")], fill=HexColor("#EAF3FA"), accent=BLUE)
    comp(c, 875, 505, 260, 230, "EC-008B", "Lynx Distributor M10", "load-side protected distribution", [("BR1+ F3 125 A", "EC-010 DC+; 35 mm²"), ("BR1−", "EC-010 DC−"), ("BR2+ F4 25 A", "EC-005 BAT+; 10 mm²"), ("BR2−", "EC-005 BAT−"), ("BR3+ F5 25 A", "EC-015A converter sub-distribution"), ("BR3−", "EC-015A negative bus"), ("BR4+/−", "reserved EC-018; no fuse/no cable"), ("LEFT BUS+/−", "from BMS RIGHT BUS; 70 mm²/250 A if cabled")], fill=white, accent=PURPLE)
    comp(c, 875, 435, 260, 55, "EC-015A", "Converter sub-distribution", "protected split to both EC-011 converters", [("IN+/− 25 A", "from EC-008B BR3"), ("OUT A/B 20 A", "to EC-011A/B inputs")], fill=white, accent=ORANGE)

    # Parallel battery power
    wire(c, [(235,690),(270,690),(270,675),(300,675)], RED, "equal-length cable", (240,696), arrow=True)
    wire(c, [(235,660),(285,660),(285,650),(300,650)], BLACK, arrow=True)
    wire(c, [(235,540),(260,540),(260,620),(300,620)], RED, "equal-length cable", (238,546), arrow=True)
    wire(c, [(235,510),(275,510),(275,595),(300,595)], BLACK, arrow=True)
    wire(c, [(535,620),(570,620),(570,625),(605,625)], RED, "M10 Lynx bus", (540,630), arrow=True)
    wire(c, [(535,595),(580,595),(580,600),(605,600)], BLACK, arrow=True)
    wire(c, [(830,625),(850,625),(850,640),(875,640)], RED, arrow=True)
    wire(c, [(830,600),(860,600),(860,615),(875,615)], BLACK, arrow=True)
    wire(c, [(1135,600),(1150,600),(1150,462),(1135,462)], RED,
         "BR3 25 A / 6 mm²", (1030, 455), arrow=True)
    # BMS cable loop
    wire(c, [(145,610),(145,595),(570,595),(570,675),(605,675)], BLUE, "BMS 3-pole loop end A", (330,591), dashed=True)
    wire(c, [(145,580),(145,565)], BLUE, dashed=True)
    wire(c, [(145,460),(145,445),(590,445),(590,650),(605,650)], BLUE, "BMS loop end B", (350,441), dashed=True)
    wire(c, [(145,580),(120,580),(120,590),(120,460),(145,460)], BLUE, "battery-to-battery daisy chain", (125,515), dashed=True)
    # RJ10
    wire(c, [(535,540),(565,540),(565,565),(605,565)], PURPLE, "RJ10 monitor", (540,546), dashed=True)
    wire(c, [(830,565),(850,565),(850,550),(875,550)], PURPLE, "RJ10 monitor", (832,571), dashed=True)

    # BMS multi connector application
    comp(c, 45, 205, 355, 155, "EC-009", "13-pin multi-connector", "pin numbering left-to-right on removable connector", [
        ("1 AUX+", "Cerbo power +; jumper to pins 3 and 5"),
        ("2 AUX−", "Cerbo power −"),
        ("3→4 ATC", "dry contact; pin 4 to EC-005 Remote H"),
        ("5→6 ATD", "dry contact; pin 6 to both EC-011 Remote H"),
        ("7/8/9", "relay NC / COM / NO; spare"),
        ("10/11", "Remote H / Remote L; system switch"),
        ("12/13", "reserved - do not connect"),
    ], fill=white, accent=BLUE)
    comp(c, 435, 220, 205, 125, "EC-013A", "Cerbo GX MK2", "power and VE.Can", [("POWER+", "from pin 1 via small fuse TBD"), ("POWER−", "from pin 2"), ("VE.Can 1", "to BMS VE.Can; terminate ends")])
    comp(c, 675, 220, 205, 125, "EC-005", "MPPT charger", "charge permission", [("REMOTE H", "from BMS pin 4"), ("REMOTE L", "unused for high-side scheme")])
    comp(c, 915, 220, 220, 125, "EC-011A/B", "Orion converters x2", "discharge permission", [("REMOTE H", "both from BMS pin 6"), ("REMOTE L", "unused for high-side scheme")])
    comp(c, 45, 85, 250, 80, "EC-015", "System on/off switch", "operational switch; not maintenance isolation", [("S1", "between BMS pins 10 and 11")])
    hold(c, 335, 95, 800, "The BMS remote switch opens the contactor but is not a visible, lockable maintenance isolator. Select and place a 60 Vdc fault-rated service disconnect before build release.")

    wire(c, [(400,320),(435,320)], RED, "pin 1 AUX+ / pin 2 AUX−", (402,326), arrow=True)
    wire(c, [(400,285),(675,285)], GREEN, "pin 4 ATC output", (515,291), arrow=True)
    wire(c, [(400,250),(915,250)], GREEN, "pin 6 ATD output - split to both H pins", (575,256), arrow=True)
    wire(c, [(295,125),(315,125),(315,180),(200,180),(200,205)], GREEN, "pins 10-11", (318,131), arrow=True)


def draw_solar(c):
    header(c, "PV ARRAY, ISOLATION, SURGE PROTECTION AND MPPT",
           "Component IDs and terminal-to-terminal connection detail", 3)
    section(c, 25, 470, 1140, 305, "ROOF ARRAY - PROVISIONAL 4S STRING", YELLOW)
    section(c, 25, 190, 1140, 255, "TECHNICAL BAY - PV SWITCHING AND CHARGE CONTROL", CYAN)
    section(c, 25, 55, 1140, 110, "ARRAY CHECKS / DESIGN HOLDS", LIGHT)

    xs = [45, 250, 455, 660]
    for i, x in enumerate(xs, 1):
        comp(c, x, 585, 175, 125, f"EC-001-{i}", f"PV module {i}", "Renogy ShadowFlux RSP200DC-ASR-G1", [("PV+", "positive lead"), ("PV−", "negative lead"), ("FRAME", "bonding lug")])
    comp(c, 875, 585, 250, 125, "EC-002", "Roof mounting system", "vehicle-approved rails, brackets, adhesive and fasteners", [("BOND", "module frame bonding path"), ("CHASSIS/PE", "final point TBD")])

    # Series string connections
    wire(c, [(220,655),(250,655)], RED, "PV1− → PV2+", (221,661), arrow=True)
    wire(c, [(425,655),(455,655)], RED, "PV2− → PV3+", (426,661), arrow=True)
    wire(c, [(630,655),(660,655)], RED, "PV3− → PV4+", (631,661), arrow=True)
    wire(c, [(45,680),(35,680),(35,520),(250,520)], RED, "ARRAY+ = PV1+", (45,526), arrow=True)
    wire(c, [(835,630),(850,630),(850,505),(320,505)], BLACK, "ARRAY− = PV4−", (690,511), arrow=True)
    # Frame bond
    for x in xs:
        wire(c, [(x+87,585),(x+87,555)], GREEN, dashed=True, width=1.3)
    wire(c, [(132,555),(748,555),(748,545),(1000,545),(1000,585)], GREEN, "frame/equipotential bond - route per risk assessment", (430,551), dashed=True, width=1.3)

    comp(c, 55, 285, 250, 120, "EC-003", "PV roof wiring and gland", "UV-resistant 6 mm² PV cable, connectors and double gland", [("PV+ IN/OUT", "array positive"), ("PV− IN/OUT", "array negative"), ("BOND", "if routed separately")])
    comp(c, 360, 260, 285, 145, "EC-004", "PV isolation and surge enclosure", "all-pole 250 Vdc isolator plus conditional Type 2 DC SPD", [("QPV IN+/IN−", "from EC-003"), ("QPV OUT+/OUT−", "to EC-005"), ("SPD +/−", "across protected PV conductors"), ("SPD PE", "short bond to PE/chassis")], fill=white, accent=ORANGE)
    comp(c, 710, 245, 410, 175, "EC-005", "MPPT charger", "Victron SmartSolar MPPT 250/60-Tr", [("PV+ / PV−", "from EC-004 OUT+/OUT−"), ("BAT+ / BAT−", "to EC-008B BR2+/BR2−; F4 25 A; 10 mm²"), ("REMOTE H", "from EC-009 pin 4 ATC"), ("REMOTE L", "unused with high-side ATC scheme"), ("VE.Direct", "to EC-013A VE.Direct 1"), ("RELAY NO/NC/COM", "spare"), ("GROUND SCREW", "protective bond")], fill=HexColor("#EAF3FA"), accent=BLUE)

    wire(c, [(250,345),(360,345)], RED, "PV+", (300,351), arrow=True)
    wire(c, [(305,315),(360,315)], BLACK, "PV−", (315,321), arrow=True)
    wire(c, [(645,345),(710,345)], RED, "QPV OUT+ → PV+", (650,351), arrow=True)
    wire(c, [(645,315),(710,315)], BLACK, "QPV OUT− → PV−", (650,321), arrow=True)
    wire(c, [(500,260),(500,225)], GREEN, "SPD PE", (505,230), dashed=True)
    wire(c, [(850,245),(850,205)], RED, "BAT+ → Lynx BR2 F4 25 A / 10 mm²", (855,220), arrow=True)
    wire(c, [(930,245),(930,205)], BLACK, "BAT− → Lynx BR2−", (935,220), arrow=True)
    wire(c, [(1040,245),(1040,205)], BLUE, "VE.Direct → Cerbo", (1000,195), dashed=True)
    wire(c, [(780,245),(780,205)], GREEN, "Remote H ← BMS pin 4", (690,195), dashed=True)

    hold(c, 40, 105, 530, "4S is a provisional connection inferred from four identical modules and one MPPT. Confirm cold-weather Voc remains below 250 V and perform shading/layout review before release.")
    hold(c, 590, 105, 540, "SPD retention, frame bonding, cable routing and protective-device ratings require an installation-specific lightning/EMC/fault-risk assessment.")
    t(c, 45, 72, "BOM basis: 4 × 200 W; module Voc 36.5 V, Vmp 31.3 V. Nominal 4S values: Voc 146 V, Vmp 125.2 V, power 800 W.", 7, MUTED)


def draw_ac(c):
    header(c, "230 VAC SHORE INPUT, MULTIPLUS-II AND OUTPUT PROTECTION",
           "Functional pin designations; EC-014 protective-device models remain to be selected by a qualified designer", 4)
    section(c, 25, 455, 1140, 320, "AC POWER PATH", ROSE)
    section(c, 25, 190, 1140, 240, "EC-010 MULTIPLUS-II TERMINAL DETAIL", CYAN)
    section(c, 25, 55, 1140, 110, "PROTECTIVE EARTH / DESIGN HOLDS", LIGHT)

    comp(c, 45, 575, 180, 130, "EC-014A", "CEE 16 A shore inlet", "body-mounted inlet", [("L", "line"), ("N", "neutral"), ("PE", "protective earth")], accent=ORANGE)
    comp(c, 270, 560, 205, 145, "EC-014B", "2-pole authorization switch", "exact device selection open", [("IN L/N", "from inlet"), ("OUT L/N", "to input RCBO"), ("PE", "not switched; to PE bus")], accent=ORANGE)
    comp(c, 515, 550, 205, 155, "EC-014C", "Input RCBO", "2-pole; rating/type/curve TBD; inlet limit 16 A", [("LINE L/N", "from authorization switch"), ("LOAD L/N", "to EC-010 AC-IN"), ("PE", "bypasses RCBO to PE bus")], accent=ORANGE)
    comp(c, 770, 535, 205, 170, "EC-010", "MultiPlus-II", "48/3000/35-32 230 V", [("AC-IN L/N/PE", "from EC-014C"), ("AC-OUT1 L/N/PE", "main protected loads"), ("AC-OUT2 L/N/PE", "switched output; spare"), ("DC+ / DC− M8", "Lynx BR1"), ("VE.Bus RJ45", "Cerbo")], fill=HexColor("#EAF3FA"), accent=BLUE)
    comp(c, 1015, 575, 120, 130, "EC-014D", "Output RCBOs", "one per final AC circuit", [("IN L/N/PE", "AC-OUT1"), ("OUT L/N/PE", "AC loads")], accent=ORANGE)

    wire(c, [(225,655),(270,655)], ORANGE, "L", (235,661), arrow=True)
    wire(c, [(225,630),(270,630)], BLUE, "N", (235,636), arrow=True)
    wire(c, [(225,605),(250,605),(250,500),(1090,500)], GREEN, "PE bus", (280,496), arrow=True)
    wire(c, [(475,655),(515,655)], ORANGE, "L", (485,661), arrow=True)
    wire(c, [(475,630),(515,630)], BLUE, "N", (485,636), arrow=True)
    wire(c, [(720,655),(770,655)], ORANGE, "L → AC-IN L", (725,661), arrow=True)
    wire(c, [(720,630),(770,630)], BLUE, "N → AC-IN N", (725,636), arrow=True)
    wire(c, [(850,535),(850,500)], GREEN, "AC-IN PE / chassis M6", (855,506), arrow=True)
    wire(c, [(975,655),(1015,655)], ORANGE, "AC-OUT1 L", (976,661), arrow=True)
    wire(c, [(975,630),(1015,630)], BLUE, "AC-OUT1 N", (976,636), arrow=True)
    wire(c, [(1075,575),(1075,500)], GREEN, "AC-OUT1 PE", (1080,525), arrow=True)

    comp(c, 45, 255, 250, 125, "EC-010", "DC / control terminals", "MultiPlus-II 3000 VA connection area", [("H DC+ M8", "Lynx BR1+ through 125 A fuse"), ("I DC− M8", "Lynx BR1−"), ("K REMOTE", "short=ON; unused in shown GX scheme"), ("L VE.Bus 1/2", "Cerbo VE.Bus")], fill=white, accent=BLUE)
    comp(c, 335, 240, 300, 140, "EC-010", "AC terminal blocks", "manufacturer connection designations", [("A AC-OUT1", "left-to-right N / PE / L"), ("B AC-OUT2", "left-to-right N / PE / L"), ("C AC-IN", "left-to-right N / PE / L"), ("F PE M6", "primary ground connection")], fill=white, accent=BLUE)
    comp(c, 675, 240, 240, 140, "EC-013A", "Cerbo GX MK2", "supervisory control", [("VE.Bus", "to either EC-010 VE.Bus RJ45"), ("VE.Can", "to EC-009 BMS")])
    comp(c, 955, 240, 180, 140, "EC-015", "DC protection", "MultiPlus branch protection", [("F3 125 A", "Lynx EC-008B BR1"), ("35 mm²", "0-5 m manufacturer recommendation")])
    wire(c, [(295,330),(335,330)], RED, "DC+/DC−", (300,336), arrow=True)
    wire(c, [(635,300),(675,300)], BLUE, "VE.Bus RJ45", (640,306), dashed=True, arrow=True)

    hold(c, 40, 105, 540, "Select EC-014 authorization switch and RCBO arrangement for the jurisdiction, vehicle construction, prospective fault current and RCD compatibility. Do not infer ratings from this drawing alone.")
    hold(c, 600, 105, 530, "PE is never switched. Bond inlet PE, MultiPlus PE/chassis and output PE to the approved vehicle protective-bonding point. Neutral-earth behavior must follow the MultiPlus relay configuration and inspection regime.")


def draw_12v_monitoring(c):
    header(c, "ISOLATED 12 V SERVICES AND MONITORING / DATA NETWORK",
           "Separate essential and non-essential buses; Cerbo GX port assignments and BMS control signals", 5)
    section(c, 25, 425, 760, 350, "DUAL 48 V TO 12 V CONVERSION", CYAN)
    section(c, 805, 425, 360, 350, "CERBO GX / DISPLAY / SENSORS", LIGHT)
    section(c, 25, 55, 1140, 345, "NETWORK AND REMOTE-CONTROL CONNECTIONS", LAV)

    comp(c, 45, 585, 225, 140, "EC-015A", "Converter sub-distribution", "fed by EC-008B BR3 through 25 A / 6 mm²", [("IN+ / IN−", "from Lynx BR3"), ("OUT A 20 A", "EC-011A IN+/IN−"), ("OUT B 20 A", "EC-011B IN+/IN−"), ("LYNX BR4", "reserved EC-018; unpopulated")], accent=ORANGE)
    comp(c, 300, 585, 225, 140, "EC-011A", "Isolated DC-DC converter", "Orion-Tr Smart 48/12-30 - ESSENTIAL", [("IN+ / IN−", "EC-015A OUT A; 20 A input fuse"), ("OUT+ / OUT−", "EC-012A; 40 A / 10 mm²"), ("REMOTE H", "EC-009 pin 6 ATD"), ("REMOTE L", "unused high-side scheme")], fill=HexColor("#EAF3FA"), accent=BLUE)
    comp(c, 560, 585, 195, 140, "EC-012A", "12-circuit fuse block", "Blue Sea 5026 - ESSENTIAL", [("P+ STUD", "from EC-011A OUT+ via 40 A"), ("N− STUD", "from EC-011A OUT−"), ("C1+..C12+", "loads via EC-016 harness"), ("C1−..C12−", "negative returns")])
    comp(c, 45, 445, 225, 120, "EC-017", "Panels and ventilation", "removable equipment panels; optional fan provision", [("FAN+/FAN−", "not populated; device TBD"), ("BOND", "bond conductive guards if required")])
    comp(c, 300, 445, 225, 120, "EC-011B", "Isolated DC-DC converter", "Orion-Tr Smart 48/12-30 - NON-ESSENTIAL", [("IN+ / IN−", "EC-015A OUT B; 20 A input fuse"), ("OUT+ / OUT−", "EC-012B; 40 A / 10 mm²"), ("REMOTE H", "EC-009 pin 6 ATD")], fill=HexColor("#EAF3FA"), accent=BLUE)
    comp(c, 560, 445, 195, 120, "EC-012B", "12-circuit fuse block", "Blue Sea 5026 - NON-ESSENTIAL", [("P+ / N− STUD", "converter feed/return"), ("C1..C12", "loads via EC-016 harness")])

    wire(c, [(270,660),(300,660)], RED, "OUT A+ through 20 A", (270,666), arrow=True)
    wire(c, [(270,625),(300,625)], BLACK, "OUT A−", (275,631), arrow=True)
    wire(c, [(270,640),(285,640),(285,515),(300,515)], RED, "OUT B+ through 20 A", (190,511), arrow=True)
    wire(c, [(270,610),(280,610),(280,485),(300,485)], BLACK, "OUT B−", (235,481), arrow=True)
    wire(c, [(525,660),(560,660)], RED, "40 A / 10 mm²", (526,666), arrow=True)
    wire(c, [(525,625),(560,625)], BLACK, "12 V−", (530,631), arrow=True)
    wire(c, [(525,515),(560,515)], RED, "40 A / 10 mm²", (526,521), arrow=True)
    wire(c, [(525,485),(560,485)], BLACK, "12 V−", (530,491), arrow=True)

    comp(c, 825, 555, 315, 175, "EC-013A", "Cerbo GX MK2", "connection assignments", [("POWER IN +/−", "EC-009 pins 1/2"), ("VE.Can 1", "EC-009 VE.Can; RJ45 terminators"), ("VE.Bus", "EC-010 VE.Bus"), ("VE.Direct 1", "EC-005 VE.Direct"), ("HDMI", "EC-013B GX Touch"), ("USB 1", "EC-013B GX Touch power"), ("TEMP 1..4", "EC-013 TS1..TS4")], fill=HexColor("#EAF3FA"), accent=BLUE)
    comp(c, 825, 445, 145, 90, "EC-013B", "GX Touch 50", "display", [("HDMI", "Cerbo HDMI"), ("USB", "Cerbo USB")])
    comp(c, 990, 445, 150, 90, "EC-013-TS1..4", "Temperature sensors", "four sensors; locations to be finalized", [("2-pin", "Cerbo TEMP 1..4")])

    # Network detail
    comp(c, 45, 225, 205, 130, "EC-009", "Lynx Smart BMS NG", "network/control source", [("VE.Can RJ45", "Cerbo VE.Can 1"), ("PIN 1/2", "Cerbo power +/−"), ("PIN 4", "ATC to MPPT H"), ("PIN 6", "ATD to both Orion H")], accent=BLUE)
    comp(c, 285, 225, 205, 130, "EC-013A", "Cerbo GX MK2", "central controller", [("VE.Can", "BMS"), ("VE.Bus", "MultiPlus"), ("VE.Direct", "MPPT"), ("HDMI/USB", "GX Touch")], accent=BLUE)
    comp(c, 525, 235, 175, 110, "EC-010", "MultiPlus-II", "data", [("VE.Bus 1/2", "Cerbo VE.Bus")])
    comp(c, 735, 235, 175, 110, "EC-005", "MPPT", "data + permission", [("VE.Direct", "Cerbo port 1"), ("REMOTE H", "BMS pin 4")])
    comp(c, 945, 225, 190, 130, "EC-011A/B", "Orion x2", "permission only; Bluetooth configuration", [("REMOTE H", "both from BMS pin 6"), ("REMOTE L", "unused"), ("DATA", "no VE.Direct port")])
    wire(c, [(250,320),(285,320)], BLUE, "VE.Can", (255,326), dashed=True, arrow=True)
    wire(c, [(490,310),(525,310)], BLUE, "VE.Bus", (495,316), dashed=True, arrow=True)
    wire(c, [(490,275),(715,275),(715,300),(735,300)], BLUE, "VE.Direct", (600,271), dashed=True, arrow=True)
    wire(c, [(250,280),(720,280),(720,270),(735,270)], GREEN, "ATC pin 4 → Remote H", (430,286), dashed=True, arrow=True)
    wire(c, [(250,250),(925,250),(925,285),(945,285)], GREEN, "ATD pin 6 → both Remote H", (515,246), dashed=True, arrow=True)
    wire(c, [(145,225),(145,190),(385,190),(385,225)], RED, "AUX pins 1/2 → Cerbo power", (205,186), arrow=True)

    hold(c, 45, 95, 520, "The two 12 V negative buses are isolated from the 48 V negative by EC-011. Any chassis bond must be a deliberate single-point design decision; do not add casual cross-bonds.")
    hold(c, 585, 95, 550, "Assign every EC-012 branch a circuit ID, load name, cable size and fuse value. The 5026 limit is 100 A per block and 30 A per circuit; each converter limits available service current to 30 A.")


CONNECTION_ROWS = [
    ("C-001", "EC-001-1 PV+", "EC-003 ARRAY+", "PV power", "6 mm² PV", "Provisional 4S end"),
    ("C-002", "EC-001-1 PV−", "EC-001-2 PV+", "PV power", "module lead", "Series link"),
    ("C-003", "EC-001-2 PV−", "EC-001-3 PV+", "PV power", "module lead", "Series link"),
    ("C-004", "EC-001-3 PV−", "EC-001-4 PV+", "PV power", "module lead", "Series link"),
    ("C-005", "EC-001-4 PV−", "EC-003 ARRAY−", "PV power", "6 mm² PV", "Provisional 4S end"),
    ("C-006", "EC-003 PV+/PV−", "EC-004 QPV IN+/IN−", "PV power", "6 mm² PV", "Through roof gland"),
    ("C-007", "EC-004 QPV OUT+/OUT−", "EC-005 PV+/PV−", "PV power", "6 mm² PV", "All-pole isolation"),
    ("C-008", "EC-004 SPD PE", "Vehicle PE/bond point", "Bond", "TBD", "Shortest practicable path"),
    ("C-009", "EC-006-1 BAT+/BAT−", "EC-008A BR1+/BR1−", "48 V power", "35 mm² equal length", "125 A provisional"),
    ("C-010", "EC-006-2 BAT+/BAT−", "EC-008A BR2+/BR2−", "48 V power", "35 mm² equal length", "125 A provisional"),
    ("C-011", "EC-006 BMS loop ends", "EC-009 BMS ports A/B", "Battery data", "3-pole circular", "Daisy-chain both batteries"),
    ("C-012", "EC-008A RIGHT BUS+/−", "EC-009 LEFT BUS+/−", "48 V bus", "M10 Lynx link", "Battery/source side"),
    ("C-013", "EC-009 RIGHT BUS+/−", "EC-008B LEFT BUS+/−", "48 V bus", "M10 link or 70 mm²", "250 A provisional; system/load side"),
    ("C-014", "EC-008B BR1+/−", "EC-010 DC+/DC− M8", "48 V power", "35 mm² ≤5 m", "125 A fuse"),
    ("C-015", "EC-008B BR2+/−", "EC-005 BAT+/BAT−", "48 V charge", "10 mm²", "25 A provisional; sized to installed 800 W array"),
    ("C-016", "EC-008B BR3+/−", "EC-015A IN+/IN−", "48 V power", "6 mm²", "25 A provisional"),
    ("C-017", "EC-015A OUT A/B +/−", "EC-011A/B IN+/IN−", "48 V power", "2.5-6 mm² by run", "20 A each; BR4 reserved for EC-018"),
    ("C-018", "EC-011A OUT+/OUT−", "EC-012A P+/N−", "12 V power", "10 mm²", "40 A provisional; essential"),
    ("C-019", "EC-011B OUT+/OUT−", "EC-012B P+/N−", "12 V power", "10 mm²", "40 A provisional; non-essential"),
    ("C-020", "EC-014 inlet L/N/PE", "EC-014B IN L/N + PE bus", "230 Vac", "TBD approved cable", "16 A inlet"),
    ("C-021", "EC-014C LOAD L/N + PE", "EC-010 AC-IN L/N/PE", "230 Vac", "TBD approved cable", "2-pole input protection"),
    ("C-022", "EC-010 AC-OUT1 L/N/PE", "EC-014D output RCBOs", "230 Vac", "TBD approved cable", "Final circuits TBD"),
    ("C-023", "EC-009 VE.Can", "EC-013A VE.Can 1", "Data", "RJ45 VE.Can", "Terminate first and last device"),
    ("C-024", "EC-010 VE.Bus", "EC-013A VE.Bus", "Data", "RJ45 UTP", "Use either MultiPlus VE.Bus socket"),
    ("C-025", "EC-005 VE.Direct", "EC-013A VE.Direct 1", "Data", "VE.Direct cable", "Maximum route per manufacturer"),
    ("C-026", "EC-009 pin 1/2 AUX+/−", "EC-013A POWER+/−", "Aux power", "small fused pair", "BMS AUX max 1.1 A"),
    ("C-027", "EC-009 pin 4 ATC", "EC-005 Remote H", "Control", "small signal wire", "Pin 3 jumpered from AUX+"),
    ("C-028", "EC-009 pin 6 ATD", "EC-011A/B Remote H", "Control", "small signal wire", "Pin 5 jumpered from AUX+"),
    ("C-029", "EC-009 pin 10/11", "EC-015 system switch", "Control", "2-core", "Operational contactor control"),
    ("C-030", "EC-013A HDMI + USB", "EC-013B GX Touch", "Display", "integral display cable", "Connect before powering Cerbo"),
    ("C-031", "EC-013 TS1..TS4", "EC-013A TEMP1..TEMP4", "Sensors", "sensor leads", "Locations TBD"),
    ("C-032", "EC-008A/B RJ10", "EC-009 RJ10 A/B", "Fuse monitoring", "RJ10", "One cable per distributor"),
]


def table_header(c, x, y, widths, labels):
    c.setFillColor(HexColor("#E5EAEE"))
    c.rect(x, y-22, sum(widths), 22, fill=1, stroke=0)
    xx = x
    for w, label in zip(widths, labels):
        t(c, xx+5, y-14, label, 6.6, INK, "Helvetica-Bold")
        xx += w


def table_row(c, x, y, widths, vals, h=22, fill=None, sizes=None):
    if fill:
        c.setFillColor(fill); c.rect(x, y-h, sum(widths), h, fill=1, stroke=0)
    c.setStrokeColor(GRID); c.line(x, y-h, x+sum(widths), y-h)
    xx = x
    for i, (w, val) in enumerate(zip(widths, vals)):
        fs = sizes[i] if sizes else 6.3
        wrap(c, xx+4, y-9, str(val), w-8, fs, fs*1.15, INK)
        xx += w
    return y-h


def draw_connection_schedule(c):
    header(c, "TERMINAL-TO-TERMINAL CONNECTION SCHEDULE",
           "Each connection is shown on pages 1-5; sizes marked TBD require measured route lengths and engineering calculations", 6)
    widths = [55, 205, 205, 90, 130, 445]
    x, y = 30, H-72
    table_header(c, x, y, widths, ["CONN", "FROM TERMINAL", "TO TERMINAL", "SERVICE", "CABLE", "PROTECTION / NOTE"])
    y -= 22
    for i, row in enumerate(CONNECTION_ROWS):
        y = table_row(c, x, y, widths, row, 20, HexColor("#F8FAFB") if i%2 else None)
    hold(c, 30, 55, W-60, "This schedule is a connection map, not a released cable schedule. Replace every TBD with conductor material, cross-section, insulation class, route length, voltage-drop result, fuse type/rating/interrupt capacity and termination specification before construction.")


BOM_ROWS = [
    ("EC-001", "solar", "PV module", "4", "Renogy ShadowFlux 200 W", "Connected; provisional 4S"),
    ("EC-002", "solar", "Roof mounting system", "1", "Rails/brackets/adhesive/fasteners", "Mechanical + bond design hold"),
    ("EC-003", "solar", "PV roof wiring and gland", "1", "6 mm² PV cable/connectors/double gland", "Connected"),
    ("EC-004", "solar", "PV isolation and surge enclosure", "1", "250 Vdc all-pole isolator + conditional SPD", "Selection/risk hold"),
    ("EC-005", "solar", "MPPT charger", "1", "Victron SmartSolar MPPT 250/60-Tr", "Connected"),
    ("EC-006", "storage", "LFP battery", "2", "Victron Lithium NG 51.2 V 100 Ah", "Parallel power + daisy-chain BMS"),
    ("EC-007", "storage", "Battery enclosure and restraint", "1", "Restraint/thermal barriers/service cradle", "No electrical pins; bond if conductive"),
    ("EC-008", "distribution", "Lynx Distributor", "2", "Victron Lynx Distributor M10", "A=battery side; B=load side"),
    ("EC-009", "storage", "Battery management system", "1", "Lynx Smart BMS NG 500A M10", "Connected; pin map pages 2/5"),
    ("EC-010", "ac power", "Inverter charger", "1", "MultiPlus-II 48/3000/35-32 230 V", "Connected"),
    ("EC-011", "12v conversion", "Isolated DC-DC converter", "2", "Orion-Tr Smart 48/12-30 isolated", "A=essential; B=non-essential"),
    ("EC-012", "12v distribution", "12-circuit fuse block", "2", "Blue Sea 5026 ST Blade", "Branch assignments TBD"),
    ("EC-013", "monitoring", "System controller display and sensors", "1 set", "Cerbo GX MK2 + GX Touch 50 + 4 sensors", "Connected; sensor locations TBD"),
    ("EC-014", "ac power", "Shore inlet and AC protection", "1 set", "CEE 16 A + 2-pole switch/RCBOs", "Device selection/design hold"),
    ("EC-015", "distribution", "DC protection and isolation", "1 set", "Fuses/holders/service disconnect/guards", "Partial ratings shown; fault study hold"),
    ("EC-016", "distribution", "Power and signal harnesses", "1 set", "Conductors/lugs/supports/data/labels", "Measured cable schedule required"),
    ("EC-017", "mechanical", "Equipment panels and ventilation", "1 set", "Panels/rails/guards/grilles/fan provision", "Fan not selected"),
    ("EC-018", "vehicle interface", "Vehicle-source charger", "0", "Renault-approved interface and charger", "DEFERRED - NO CONNECTION"),
]


def validate_bom_source():
    """Fail generation if the drawing component IDs/names drift from the BOM."""
    with BOM_PATH.open(newline="", encoding="utf-8") as handle:
        source_rows = list(csv.DictReader(handle))
    source = {row["component_id"]: row["component"] for row in source_rows}
    drawing = {row[0]: row[2] for row in BOM_ROWS}
    if source != drawing:
        missing = sorted(source.keys() - drawing.keys())
        extra = sorted(drawing.keys() - source.keys())
        renamed = sorted(key for key in source.keys() & drawing.keys() if source[key] != drawing[key])
        raise ValueError(
            "EC-WD-001 is out of sync with electrical-core-bom.csv: "
            f"missing={missing}, extra={extra}, renamed={renamed}"
        )


def draw_bom_and_sources(c):
    header(c, "BOM CROSS-REFERENCE, DESIGN HOLDS AND SOURCE MANUALS",
           "Every electrical-core-bom.csv row is represented; quantity-zero item is explicitly excluded", 7)
    t(c, 30, H-72, "A. BOM CROSS-REFERENCE", 10, INK, "Helvetica-Bold")
    widths = [70, 110, 210, 55, 390, 300]
    x, y = 30, H-84
    table_header(c, x, y, widths, ["ID", "SUBSYSTEM", "COMPONENT NAME", "QTY", "CANDIDATE / DESCRIPTION", "DIAGRAM STATUS"])
    y -= 22
    for i, row in enumerate(BOM_ROWS):
        y = table_row(c, x, y, widths, row, 24, HexColor("#F8FAFB") if i%2 else None)

    y -= 12
    t(c, 30, y, "B. RELEASE-BLOCKING DESIGN HOLDS", 10, INK, "Helvetica-Bold")
    y -= 14
    holds = [
        "H1 - Confirm PV 4S topology using cold-weather Voc, shading and roof-layout calculations.",
        "H2 - Complete 48 V battery fault-current study; select battery branch fuses, fuse class and interrupt ratings.",
        "H3 - Select a visible, lockable 60 Vdc maintenance isolator; the BMS remote switch is only operational control.",
        "H4 - Measure every route and release the EC-016 cable schedule including voltage drop, derating and terminations.",
        "H5 - Qualified AC designer to release EC-014 inlet, authorization, RCBO/RCD, PE and neutral-earth arrangement.",
        "H6 - Assign all 24 EC-012 branch circuits and decide whether either isolated 12 V negative bus bonds to chassis.",
        "H7 - Verify crash restraint, thermal management, IP protection, ventilation and service clearances.",
        "H8 - EC-018 remains disconnected until Renault approval evidence and a compatible charger/interface exist.",
    ]
    for item in holds:
        y = wrap(c, 40, y, item, 1110, 6.8, 8.2, INK) - 2

    y -= 4
    t(c, 30, y, "C. PRIMARY TECHNICAL SOURCES", 10, INK, "Helvetica-Bold")
    y -= 14
    sources = [
        "BOM: electrical-core-bom.csv",
        "Victron Lynx Smart BMS NG manual: https://www.victronenergy.com/media/pg/Lynx_Smart_BMS_NG/en/index-en.html",
        "Victron Lynx Distributor manual: https://www.victronenergy.com/media/pg/Lynx_Distributor/en/index-en.html",
        "Victron Lithium NG 51.2 V manual: https://www.victronenergy.com/media/pg/Lithium_NG_battery_51%2C2_V/en/index-en.html",
        "Victron SmartSolar 150/60-250/70 manual: https://www.victronenergy.com/media/pg/Manual_SmartSolar_MPPT_150-60_up_to_250-70/en/index-en.html",
        "Victron MultiPlus-II 230 V manual: https://www.victronenergy.com/media/pg/MultiPlus-II_230V/en/index-en.html",
        "Victron Orion-Tr Smart isolated manual: https://www.victronenergy.com/media/pg/Orion-Tr_Smart_DC-DC_Charger_-_Isolated/en/index-en.html",
        "Victron Cerbo GX manual: https://www.victronenergy.com/media/pg/Cerbo_GX/en/index-en.html",
        "Blue Sea Systems 5026: https://www.bluesea.com/products/5026/ST%20Blade%20Fuse%20Block%20-%2012%20Circuits%20with%20Negative%20Bus%20and%20Cover",
    ]
    for src in sources:
        y = wrap(c, 40, y, src, 1110, 6.2, 7.2, MUTED) - 1


def main():
    validate_bom_source()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=PAGE)
    c.setTitle("Electrical Core BOM Wiring Diagram")
    c.setAuthor("OpenAI Codex - connection-level drawing from electrical-core-bom.csv")
    for fn in (draw_overview, draw_dc_core, draw_solar, draw_ac, draw_12v_monitoring, draw_connection_schedule, draw_bom_and_sources):
        fn(c)
        c.showPage()
    c.save()


if __name__ == "__main__":
    main()
