---
title: "Klug Innobox (Taiming 908SH-A86) — data for SmartCabinet"
category: Processes
status: active
sensitive: false
created: 2026-11-04
updated: 2026-11-04
sources:
 - "`Raw/758810.pdf` (owner, 04/11/2026) — Taiming *motion 908SH-A86 NOBLE DRAWER*, catalogue pp. 5, 6 and 15 (specifications, components, assembly). Scanned: **no text layer**, every figure read off the page image (*drawing*)"
 - "`Wiki/Processes/blum-metabox-smartcabinet-input.md` — how the shop's SmartCabinet takes a steel-sided drawer (runner row + box `.SCS`), proved on METABOX 2026-10-02/03"
related:
 - blum-metabox-smartcabinet-input.md
 - ../Software/smartcabinet-online-manual.md
---

# Klug Innobox (Taiming 908SH-A86) — data for SmartCabinet

**Owner, 2026-11-04:** *"We need to klug innobox to SmartCabinet"* — first used on ENQ-0002 (3 drawers, NL 450, 500-wide
carcase). The drawing the owner supplied for "Klug Innobox" is **Taiming's 908SH-A86 "Noble Drawer"**, so Innobox is
taken to be that product sold under the Klug name. *Confirm the Klug part number matches 908SH-A86 when ordering.*

**Every figure below is read off a scanned drawing.** Nothing here is printed text a script could check. Values marked
**⚠ measure** need a real set in the hand before a production run.

## 1. Try the import first

As with METABOX: **Utility → Import Accessori**, search `Klug`, `Innobox`, `Taiming` or `A86`. Kosmosoft's library is
mostly the big brands, so **expect it not to be there**, and then enter it by hand with §3–§5.

## 2. What it is

| | Innobox A86 | METABOX M (for comparison) |
|---|---|---|
| Side | **double-wall steel, 86 high** | single-wall steel, 86 high |
| Runner | **separate full-extension runner under the side**, soft close built in | the side is the runner, single extension |
| Load | **35 kg** | 25 kg |
| Front fixing | **front fixing brackets L/R** screwed to the front, 3D adjustment (height ±2, side ±1) | knock-in / screw-on brackets |
| Wooden parts | **base, back (or metal back, accessory 11), front** | base, back, front |
| In the box | runners L/R, drawer profiles L/R, rear connecting brackets L/R, front fixing brackets L/R | — |

**Lengths and depths** (page 5, printed in the table):

| NL | Internal drawer length | Min. cabinet depth |
|---|---|---|
| 270 | 244 | 280 |
| 300 | 274 | 310 |
| 350 | 324 | 360 |
| 400 | 374 | 410 |
| 450 | 424 | 460 |
| 500 | 474 | 510 |
| 550 | 524 | 560 |

So **internal length = NL − 26** and **min. depth = NL + 10**. A 570-deep base unit (internal ≈ 551 with a 19 back set in)
takes **NL 500**; the 500-deep ENQ-0002 carcase (482 inside) takes **NL 450**.

## 3. Runner row — *Tabelle CAM Accessori → Guide Cassetto* (category `25 GUIDE CASSETTO`)

**One row per NL**, coded e.g. `A86-450 INNOBOX`. Fill as for METABOX (§7 of the METABOX article: the hole groups are
the **cabinet-side** runner holes).

| Field | Value | Basis |
|---|---|---|
| `LX` (per side, to the side's outer face) | **5** to start ⚠ measure | METABOX/LEGRABOX rows use 5; the real figure is fixed by the box `.SCS` (§4) |
| `LY` (under the lowest drawer) | **0–18** so that `LY + Y` ≥ **56** ⚠ | drawing p. 15: runner screw line **min. 56** above the part below; **min. 105** height per drawer |
| `CX` | **0** | no groove |
| `LBox` | **NL − 26** (e.g. 424 for NL 450) ⚠ | internal drawer length, p. 5; whether `LBox` must be the base or the overall box is checked in §6 |
| Hole 1 | **X 37**, Y = hole line, Ø5 φ5 | runner front fixing, p. 15 |
| Hole 2 | **X 261** (37 + 224), Ø5 φ5 | runner rear fixing, p. 15 — **the drawing gives one pattern for every NL 270–550** |
| Holes 3–4 (optional) | X 69 (37 + 32) and X 229 (261 − 32) | the further holes in each bracket, 32 apart; a 9 mm step is also dimensioned |
| Hole line `Y` | so that `LY + Y` = **56** (e.g. `LY` 18 → `Y` 38) ⚠ | — |

**Hole size:** the drawing shows wood screws, no system screws. **Ø5 φ5** (a pilot) matches the shop's METABOX row; change
it if the Innobox screws want something else ⚠.

**NL 270 has no room for a 261 rear hole**, but the drawing claims one pattern. ⚠ Check the NL 270 runner before drawing
one.

## 4. Drawer box — `.SCS` file on the Innobox row of *Scatola Cassetto*

Copy `METABOX_K.scs` to `INNOBOX_A86.scs`, change the values below, and load it through **Box Config file** (on METABOX,
values typed into the window did not take effect; the loaded file did).

| Parameter | Set | Basis |
|---|---|---|
| `cass05_spess` (sides) | so that **5 + side = 37.5** → **32.5** ⚠ | drawing p. 15: **37.5 ± 0.5** from the cabinet side to the edge of the base → **base = LW − 75** (the usual double-wall figure) |
| `cass_sp_sot` (base) | **16** ⚠ | drawing shows a screwed-in base; thickness not printed |
| `cass_sp_die` (back) | **16** (wooden back) | the back screws to the rear connecting brackets: 2 holes **32 apart**, **9** from the back's end ⚠ |
| `cass_sp_fro` (inner front) | **0** | no inner front |
| `bCassDDIE` | **1** (back between the sides) | back edge **44.5** from the cabinet side → **back = LW − 89** ⚠ measure |
| `cass_sot_dz`, `cass_sot_dy` | **0** | base sits on the profile's flange, no groove |
| `bCassDIESOT` / `FILO` | as METABOX (0 / 1), check the result | — |

**Expected cut sizes (ENQ-0002: NL 450, 500 carcase in 18 mm, LW 464):** base **389** wide (464 − 75), back **375** wide (464 − 89),
base depth ≈ **424** less the back if the back stands on it. Back height: **not on the drawing** ⚠ measure (≈ 70 likely
for an 86 side).

## 5. Front

- Front fixing bracket screws into the front: **2 holes 32 apart**, the lower **min. 54** above the front's bottom
  reference, **Ø10** (side view shows a 10 hole) ⚠ — confirm whether that is a Ø10 dowel/insert hole or a screw.
- Bracket position: **37.5 ± 0.5** in from the cabinet side, **20** from the front's back face line *(drawing)*.
- All front holes on the Vitap (shop rule) — they need a hardware entry or a hand-edited program, like METABOX's knock-in
  holes.

## 6. Proving it — one drawer, before any job

1. Enter **one** runner row (NL 450) and the `.SCS`.
2. Draw a 500-wide, 500-deep carcase with **one** Innobox drawer (= ENQ-0002).
3. Check the export (`pre-production-drawing-check`):
   - side: holes at **37 and 261** on one line, **56** above the part below;
   - base **LW − 75**, back **LW − 89**, depth per §4;
   - drawer front: 2 holes 32 apart, lowest ≥ 54 up.
4. **Dry-fit against a real Innobox set** before cutting the rest: the ⚠ figures (side allowance, back width, back height,
   hole line) are drawing reads, not measurements.

Then add the other NLs (only the `LBox` changes; holes stay 37 / 261).

## 7. Still open

- Klug part number = Taiming 908SH-A86? (ordering)
- ⚠ items above, all to measure on the first set.
- Price: £17.95 ex VAT per set (indicative, ENQ-0002 costing) — add to the **Hardware Price Library** once invoiced.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-11-04 | Created from the owner's Klug drawing (Taiming 908SH-A86) and the METABOX method | `change-log-2026-11-04-fl003-closed.md` (11) |
