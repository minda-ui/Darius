---
title: "Blum CLIP top 110° hinges — drilling, overlay and SmartCabinet input"
category: Processes
status: active
sensitive: false
created: 2026-10-02
updated: 2026-10-02
sources:
 - "`Raw/Blum_publication.pdf` — *Blum catalogue and technical manual 2022/2023* (KA-150). 110° hinge: PDF pp. 78–79 (cat. 74–75); overview and number of hinges: PDF pp. 76–77 (cat. 72–73); mounting plates: PDF pp. 148–152 (cat. 144–148); planning and front overlay: PDF pp. 710–713 (cat. 706–709). Extracts: `Raw/Blum/` families **H1** and **H2**"
 - "SmartCabinet online manual, `mainit/smartcabinet/tabelle_cam_accessori_cerniere.html`, fetched 2026-10-02"
related:
 - ../Suppliers/blum-library.md
 - blum-metabox-smartcabinet-input.md
 - ../Software/smartcabinet-online-manual.md
---

# Blum CLIP top 110° hinges — drilling, overlay and SmartCabinet input

**Owner, 2026-10-02: *"Yes, start with hinges."*** This covers the **standard 110° CLIP top / CLIP top
BLUMOTION hinge** and its **37/32 mounting plates**, the everyday cabinet-door hinge. Other hinges
(107°, 155°, 170°, angled, glass, blind corner, thin door) are in family **H1** of the Blum library and
are not worked up here yet.

**Every figure is from the Blum 2022/2023 catalogue.** Values marked *(drawing)* were read off a rendered
drawing. Values marked *(derived)* were calculated from printed values and are not printed as such.
Check them on a test door before a batch.

## 1. Which hinge — the three cranks

The front's position on the cabinet side decides the hinge arm:

| Application | Arm | Door position | Boss overlay TO − crank |
|---|---|---|---|
| **Overlay** (full overlay) | straight, **0 mm** | covers the cabinet side | 11 − 0 = **11** |
| **Dual** (half overlay) | cranked **9.5 mm** | two doors share one side | 11 − 9.5 = **1.5** |
| **Inset** | double cranked **18 mm** | sits inside the cabinet | 11 − 18 = **−7** |

**Boss overlay TO = 11.0 mm** (fixed, ±0.5) for 100°–170° CLIP top hinges, and **13.0** for the 110°
*special* hinge for thick cabinet sides. **Front gap FS = 1.5 mm** for CLIP top / CLIP top BLUMOTION.

## 2. Part numbers — 110° hinge (web code DQDELA)

| Boss fixing | | Overlay | Dual | Inset |
|---|---|---|---|---|
| **INSERTA** (tool-free, press in) | BLUMOTION | **71B3590** | **71B3690** | **71B3790** |
| | spring | 71T3590 | 71T3690 | 71T3790 |
| | unsprung | 70T3590.TL | 70T3690.TL | 70T3790.TL |
| **Screw-on** | BLUMOTION | **71B3550** | **71B3650** | **71B3750** |
| | spring | 71T3550 | 71T3650 | 71T3750 |
| | unsprung | 70T3550.TL | 70T3650.TL | 70T3750.TL |
| **Knock-in** | BLUMOTION | 71B3580 | 71B3680 | 71B3780 |
| | spring | 71T3580 | 71T3680 | 71T3780 |
| | unsprung | 70T3580.TL | — | — |

**Reading the code:** `71B` = BLUMOTION, `71T` = spring, `70T…TL` = unsprung (for TIP-ON). Then `35` =
overlay, `36` = dual, `37` = inset. Then `90` = INSERTA, `50` = screw-on, `80` = knock-in. Colours are
nickel (NI), and onyx black (ONS) on most.

**110° special hinge** (TO 13, for thick cabinet sides), overlay only: `73B3590` / `73T3590` / `72T3590.TL`
(INSERTA), `73B3550` / `73T3550` / `72T3550.TL` (screw-on), `73B3580` / `73T3580` (knock-in).

**Accessories:**

| Item | Part no. |
|---|---|
| Hinge arm cover cap, overlay | **70.1503** (Blum stamped `70.1503.BP`) |
| Hinge arm cover cap, dual and inset | **70.1663** (`70.1663.BP`) |
| Opening angle stop, 86° | 70T3553 |
| Hinge boss cover cap | 70T3504 |
| Hinge boss spacing 1.5 mm | 70T3507.21 |
| Chipboard screws Ø3.5 × 15 / × 17 | **609.1500** / **609.1700** |
| Insertion ram (knock-in) | MZM.0040 |
| TIP-ON for doors (with unsprung hinges) | 956.1004 short; 956A1004 / 956A1006 / 956A1006F extended |

**Blum's own warning:** mixing CLIP top BLUMOTION and sprung CLIP top hinges on one front needs a trial on
small, light fronts up to 300 mm wide. **Do not mix them on wider fronts.**

## 3. Door drilling — the hinge cup (boss)

| Value | Figure | Note |
|---|---|---|
| Cup diameter | **Ø35 mm** (+0.2/0 for INSERTA and knock-in) | printed |
| Cup depth | **min. 13 mm** | *(drawing)* |
| **Drilling distance TB** (door edge to **edge** of the cup) | **3–7 mm** | printed |
| Cup centre from door edge | **TB + 17.5** (e.g. TB 5 → **22.5 mm**) | *(derived)* |
| INSERTA / knock-in dowel holes | **Ø8 mm** (±0.1), **45 mm** apart, along the door edge | *(drawing)* |
| Dowel line offset | **9.5 mm** further from the door edge than the cup centre | *(drawing)* |
| Screw-on | two chipboard screws, positions marked but **not dimensioned** on this page | — |
| Boss flange | 57 wide × 37.5 (INSERTA **43**) high, sits 3.2 (INSERTA **6.4**) proud | *(drawing)* |

*The depth of the Ø8 dowel holes is not printed on the pages read. Measure a hinge before setting it.*

## 4. Front overlay — the formula

The tables for the 110° hinge follow one rule exactly. It was checked against every cell of all three
tables:

> **FA = TO + TB − MD − crank**, i.e.
> **overlay: FA = 11 + TB − MD** · **dual: FA = 1.5 + TB − MD** · **inset: FA = −7 + TB − MD**

`FA` front overlay, `TB` cup drilling distance (3–7), `MD` mounting plate spacing (0, 3, 6, 9 — the
plate's "height" code). Side adjustment then gives **±2 mm** more.

**Worked examples** *(derived from the formula — check on a door)*:

| Job | Want FA | Use |
|---|---|---|
| Full overlay on an 18 mm side, 2 mm reveal | 16 | overlay hinge, **TB 5, MD 0** |
| Two doors on one 18 mm partition | ~7.5 each | **dual** hinge, **TB 6, MD 0** |
| Inset door | — | **inset** hinge; **move the plate back by FD + 1.5 mm** (18 mm door → plate holes at **37 + 19.5 = 56.5 mm**) |

**Minimum gap F between door and neighbour** (1 mm edge radius, factory setting): for **18 mm** doors it
is **0.8 mm at any TB**; 16 mm → 0.5; 19 → 0.9–1.0; 22 → 1.6–1.8. Add 0.4 for 18 mm if the hinge is
side-adjusted +2 mm. From 28 mm, Blum says trial first.

## 5. Number of hinges (for a door 600 mm wide)

| Door height up to | Door weight | Hinges |
|---|---|---|
| ~750 mm | 4–6 kg | **2** |
| 1500 mm | 6–12 kg | **3** |
| ~2100 mm | 12–17 kg | **4** |
| 2500 mm | 17–22 kg | **5** |

*(drawing — bar chart; heights read off the axis)*. **Space the hinges as far apart as possible.**

## 6. Cabinet drilling — mounting plates 37/32

**37/32** means the two fixing holes are **37 mm from the cabinet front edge** and **32 mm apart**
vertically: the System 32 line. The hinge centre falls between them.

| Plate | Fixing | Material | Height adj. | MD 0 | MD 3 | Other |
|---|---|---|---|---|---|---|
| Cruciform **cam** 37/32 | chipboard screws Ø3.5/Ø4 | steel | cam ±2 | **173H7100** | 173H7130 | — |
| Cruciform **INSERTA** 37/32 | tool-free | steel/zinc | cam ±2 | 174H7100I | 174H7130I | — |
| Cruciform **cam EXPANDO** 37/32 | pre-fitted screws, **Ø5** holes, min. 11.5 deep | steel | cam ±2 | **174H7100E** | 174H7130E | twin: 174H710ZE / 174H713ZE |
| Cruciform 37/32 | chipboard screws, 17 mm | zinc | ±2 | 175H7100 | 175H7130 | MD 9 175H7190, 18 175H7190.22 |
| Cruciform 37/32 | **system screws Ø6 × 14.5, 661.1450.HG** in **Ø5** holes | zinc | ±2 | **175H9100** | 175H9130 | MD 6 175H9160, 9 175H9190, 18 175H9190.22 |
| Cruciform 37/32 | chipboard screws, elongated hole | steel | ±3 | 173L6100 | 173L6130 | — |
| Cruciform 37/32 EXPANDO | elongated hole | steel | ±2 | 174E6100.01 | 174E6130.01 | — |
| Horizontal cam **20/32** | chipboard screws | steel | cam ±2 | 175H3100 | 175H3130 | EXPANDO 177H3100E / 177H3130E |

**Plate height:** MD 0 = 8.5 mm, MD 3 = 11.5, MD 6 = 14.5, MD 9 = 17.5, MD 18 = 26.5.
**For System 32 drilling on the Vitap**, the plates that use the drilled holes are the **EXPANDO** (Ø5,
min. 11.5 deep) and the **system-screw** zinc plate (Ø5). Chipboard-screw plates need no drilling, or a
pilot only. *Wide-angle and 0-protrusion hinges need an extra screw (drawing: 26 mm behind the hole line
on the zinc plates).*

## 7. Into SmartCabinet — Tabelle CAM Accessori → Cerniere

**Check Utilità → Import Accessori first**, as for METABOX: Kosmosoft may already supply Blum hinges with
their CAM data. If they are there, import rather than type.

The hinge must already be in **Anagrafica Accessori**. Then, in **Cerniere**, `D…` columns are the
**door** (anta) and `S…` columns the **cabinet** (struttura):

| SmartCabinet | Meaning | Blum 110° value |
|---|---|---|
| `DX` | cup centre from the door edge | **TB + 17.5** — e.g. **22.5** for TB 5 *(derived)* |
| `DØ` | cup diameter | **35** |
| `Dφ` | cup depth | **13** *(drawing, "min. 13")* |
| `DX2` | small holes' centre from the door edge | INSERTA/knock-in: **DX + 9.5** — e.g. **32.0** *(drawing)*; screw-on: leave empty |
| `DY2` | distance between the two small holes | **45** *(drawing)* |
| `DØ2` | small hole diameter | **8** |
| `Dφ2` | small hole depth | **not printed — measure the dowel** |
| `SX` | plate holes from the cabinet front edge | **37** (inset: **37 + FD + 1.5**) |
| `SY` | between the two plate holes | **32** |
| `SØ` | plate hole diameter | **5** for EXPANDO / system screws; chipboard-screw plates need none |
| `Sφ` | plate hole depth | **11.5** for EXPANDO (printed min. 11.5); for system screws not printed — check |
| `SX2` | third hole behind the pair | only for wide-angle hinges — leave empty for 110° |
| `Tool` / `N° Step Z` | end mill for the cup, passes | leave empty to drill the cup with a Ø35 bit; set if the Vitap mills it |
| `Offset su Divisori` | moves the `S` holes inward on vertical dividers | per job |

*Where SmartCabinet places the hinges along the door height (distance from top and bottom) is set
elsewhere, not in this table. Not checked yet.*

## 8. What is still open

- Whether Import Accessori already offers these Blum hinges (**check first**, §7).
- `Dφ2`: the depth of the Ø8 dowel holes.
- The screw-on hinge's screw positions: not dimensioned on the pages read.
- Which hinge and which plate the shop actually stocks. **Read one from the box or an invoice** so the
  table can be cut down to the shop's own two or three rows.
- One test door, drilled and hung, before a batch: TB, MD and the overlay formula.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-10-02 | Created from the Blum 2022/2023 catalogue (110° hinge, mounting plates, hinge planning pages) and the SmartCabinet *Cerniere* manual page, on the owner's instruction | Session 26 |
