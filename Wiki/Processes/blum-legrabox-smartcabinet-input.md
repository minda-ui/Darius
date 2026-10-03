---
title: "Blum LEGRABOX — data for SmartCabinet"
category: Processes
status: active
sensitive: false
created: 2026-10-03
updated: 2026-10-03
sources:
 - "`Raw/Blum_publication.pdf` — *Blum catalogue and technical manual 2022/2023* (KA-150); LEGRABOX is PDF pp. 192–247 (catalogue pp. 188–243). Extract: `Raw/Blum/Blum-2022-23_B1_LEGRABOX_pdf192-247.pdf`"
 - "Kosmosoft reference sheets `legrabox_default_scs.pdf` and `parametri_legrabox_ini.pdf` (SmartCabinet `.SCS` / `.ini` parameters for LEGRABOX), fetched 2026-10-03"
 - "The shop's own Kosmosoft LEGRABOX rows in *Guide Cassetto*, from the owner's photo of 2026-10-03"
related:
 - ../Suppliers/blum-library.md
 - blum-metabox-smartcabinet-input.md
 - blum-runners-tandem-movento-smartcabinet-input.md
 - ../Software/smartcabinet-online-manual.md
---

# Blum LEGRABOX — data for SmartCabinet

**Owner, 2026-10-03: *"please carry on with Blum."*** LEGRABOX is the next system after METABOX because **the shop
already has LEGRABOX in SmartCabinet**: Kosmosoft's rows sit under `25 GUIDE CASSETTO`, and Kosmosoft's own
`legrabox_default.scs` is the sheet the METABOX settings were worked out from. This article is the **check sheet for
the first LEGRABOX job**, so it does not need the six rounds the 350 METABOX unit took.

Every figure is from the Blum 2022/2023 catalogue. **Values marked *(drawing)* were read off a rendered drawing**;
check them on the first job. *2022/2023 edition: check current data before ordering.*

## 1. Heights, lengths, loads

LEGRABOX has **12.8 mm steel sides** and soft close (BLUMOTION S) built in. One cutting rule covers every height.

| Height | Side height | Chipboard back height | NL available | Space above the hole line *(drawing)* | Cat. page |
|---|---|---|---|---|---|
| **N** | 66.5 | **39** | 400–550 | ≥ 42 | 194 |
| **M** | 90.5 | **63** | 270–650 | ≥ 68 | 196 |
| **K** | 128.5 | **101** | 300–600 | ≥ 106 | 200 |
| **C** (high fronted, *pure*) | 177 | **148** | 270–650 | ≥ 155 | 204 |
| **F** (high fronted, *pure*) | 241 | **212** | 400–650 | ≥ 219 | 210 |

- **Hole line height:** the cabinet-profile screw line sits **≥ 38 above the part below** (+1 if the profile goes on
  before the cabinet is assembled). Space above it is the column above, **including 2 mm tilt adjustment** *(drawing)*.
- **Cabinet depth:** inside depth **≥ NL + 3**.
- **Loads:** cabinet profile **750 = 40 kg** (NL 270–600); **753 = 70 kg** (NL 450–650).
- **Inner drawers** (M, K, C) have their own pages (198, 202, 206–217): inner front **LW − 126**. Not written up here.

## 2. Cutting list — 16 mm chipboard

| Part | Width | Depth / height |
|---|---|---|
| **Base (A)** | **LW − 35** | **NL − 10** with a chipboard back · **NL − 21** with the steel back |
| **Back (B)** | **LW − 38** | the back height from §1 (N 39 · M 63 · K 101 · C 148 · F 212) |

LW = inside cabinet width. *(Catalogue p. 195 and each height's planning page.)* Blum also draws a **rebate
dimension** on the base (**16 · 8 · 38**, *(drawing)*, p. 195). **Whether SmartCabinet machines it is unconfirmed.
Check the first LEGRABOX base program** before cutting.

**Front fixing (screw-on brackets), holes in the drawer front** *(drawing)*: first hole **45.5 (N) / 51 (M, K, C, F)**
above the base underside, the second **16 (N) / 32** above it; C and F add further holes up the front (96 / 32 pitch).
Bracket edge 23.4 (N–K) / 24.4 (C, F); **14** in from the cabinet side. EXPANDO fronts: Ø10 holes, min. 12 from the
front's inner face.

## 3. Cabinet-profile holes — from the cabinet front edge

From the fixing-positions page (p. 242), **750 (40 kg)** profile *(drawing; the arithmetic is mine)*:

| NL | Front holes | Rear holes |
|---|---|---|
| 270 | 18*, 37, 69 | 197 |
| 300, 350 | 18*, 37, 69 | 261 (229 optional) |
| 400–500 | 18*, 37, 69 | 243, 261, 293 |
| 550–600 | 18*, 37, 69 | 243, 261, 293, 357 |

Screws: **A = chipboard screw Ø4 × 15**, **B = system screw Ø6 × 14.5** (`661.1450.HG`); \* = can be a chipboard
screw instead. **The 753 (70 kg) profile has its own pattern** (p. 242: rear holes reach 37 + 416 at NL 650). Read it
from the drawing before entering a 753 row.

**The shop's Kosmosoft LEGRABOX rows carry 37 · 69 · 261 · 293 · 357**, the 750 pattern for NL 550 and above. They
**agree with Blum**. For shorter NL the rear holes move as above, so **each NL needs its own row**, as with METABOX.

## 4. Part numbers (order pages 194–215)

| What | Part no. pattern | Example |
|---|---|---|
| Cabinet profile 40 kg | `750.<NL>01S` | `750.4501S` = NL 450 |
| Cabinet profile 70 kg | `753.<NL>01S` | `753.5001S` |
| Drawer side set | `770<height><NL>02` + colour | `770M4502S` (SW-M / OG-M / CS-M), `770M4502I` (stainless) |
| Chipboard back fixings | `ZB7<height>000S` | `ZB7N000S`, `ZB7M000S`, `ZB7K000S`, `ZB7C000S`, `ZB7F000S` |
| Front fixing brackets | `ZF7<height>7002` screw-on · `70E2` EXPANDO · `70T2` EXPANDO T | `ZF7M7002` (C and F use the C and M brackets) |

Colours: SW-M silk white · OG-M orion grey · CS-M carbon black · INGL stainless · NI nickel. *The side-set table also
lists `…01S` numbers next to `…02S`. Check the order page before ordering, rather than relying on this pattern.*

## 5. SmartCabinet — the drawer-box settings (`.SCS`)

**The lesson from METABOX applies:** the settings that count are the ones in the **`.SCS` file loaded on the box-system
row** (*Tabelle CAM Accessori → Scatola Cassetto → Box Config file*), not the values typed in the window. See
`blum-metabox-smartcabinet-input.md` §7a.

Kosmosoft's `legrabox_default.scs` (in `\Kosmosoft\SmartCabinet\dati_server\system_sc\Data\`) against Blum:

| Parameter | Kosmosoft default | What it gives | Blum | Verdict |
|---|---|---|---|---|
| `cass01_dist_lat` (= rail `LX`) | 5.00 | — | — | keep; matches the rows |
| `cass03_dist_sot` (= rail `LY`) | 18.00 | lowest drawer | hole line ≥ 38 above the part below | check `LY` + the row's `Y` ≥ 38 |
| `cass05_spess` | **14.00** | **base LW − 2·(5 + 14) + 2·1.5 = LW − 35** | LW − 35 | ✓ the 14 is a **notional** side (the real one is 12.8), chosen so the width comes out right. **Do not "correct" it to 12.8** |
| `cass_sot_dz` | 1.50 | base enters the sides 1.5 each | — | ✓ part of the LW − 35 sum |
| `bCassDDIE` | 1 | back between the sides: **LW − 2·(5 + 14) = LW − 38** | LW − 38 | ✓ |
| `cass_sp_sot` | 16.00 | base 16 | 16 | ✓ |
| `cass_sp_die` | **19.00** | back 19 | **16 mm chipboard** in Blum's cutting list | **? set 16** if the shop uses 16 for backs, as on METABOX. *Whether `ZB7…` back fixings take 19 is not stated on these pages* |
| `cass_sp_fro` | 0.00 | no inner front | — | ✓ |
| `cass_sot_dy` | 17.50 | base 17.5 above the bottom of the sides | *(not printed)* | Kosmosoft's LEGRABOX default; Blum prints no equivalent. **Leave it unless the back height comes out wrong** (on METABOX this was the parameter that cut the back short) |
| `bCassDIESOT` / `bCassDIESOTFILO` | 0 / 1 | back runs down to the base underside | Blum's back drawing (p. 195) *(not decoded)* | **the depth and back height are what to check**: see below |

**Widths are right out of the box; depth and back height are not proven.** **Check the first job's cutting list**
against §2:

1. Base **LW − 35 × NL − 10**.
2. Back **LW − 38 × the height from §1** (N 39 · M 63 · K 101 · C 148 · F 212).

If they differ, change one parameter at a time in a **copy** of the `.SCS`, reload it on the LEGRABOX row, and
regenerate. **Restart SmartCabinet before reloading.** *That sequence is what finally worked for METABOX.*

**`parametri_LEGRABOX.ini`** holds the same values under `Auto_…` names, plus the **front stabiliser** option:
`StabilizerLimitLengthBox=1` drills two holes to fix a wide/thin front to the base (`StabilizerDX` 25,
`StabilizerDY` 30). Blum's matching part is the front/base stabiliser on p. 239. Leave it off unless fronts are wide or
thin.

## 6. Open

- The base **rebate** (16 · 8 · 38): what it is for, and whether SmartCabinet machines it. **Check the first base program.**
- **Back thickness 19 or 16**: the owner's choice. Blum's cutting list says 16.
- **Depth and back height** from the Kosmosoft defaults: **unproven until the first LEGRABOX job's cutting list.**
- The **753 (70 kg)** hole pattern is not yet tabulated.
- **Not covered here:** TIP-ON / TIP-ON BLUMOTION for LEGRABOX (B2), SERVO-DRIVE (B8), AMBIA-LINE inner dividing (I1).

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-10-03 | Created on the owner's *"please carry on with Blum"* | Session 27 (31) |
