# Change log — 2026-10-03 — METABOX: the first SmartCabinet side panel checked

**Session 27.** Session-start read: Hub — five Darius rows, unchanged (`AWT-0089`, `-0127`, `-0147`, `-0194`
Open; `-0225` Blocked); `Raw/` — one new file, found only when the owner pointed at it (see (2)).

## (1) `Raw/Side Left.pdf` — is it correct for METABOX?

Owner: *"You have the Side Left file in the Workshop Raw folder; is it correct for MetaBox?"* The file is a
SmartCabinet drilling drawing (75,639 B, id `1bYx_tDIg0xbY_KEAphLc1iawPNwd-Vff`, 1 page, vector with no text
layer — read from a render): **`01 SIDE LEFT L851 × H570 × Z19`**, four METABOX rails.

- **The rails are being drilled.** That answers §7's deciding test: Kosmosoft's import produces the cabinet-side holes.
- **Front hole 37** matches Blum. **The rear hole is at 357**, which is NL 400's alone; 165 and 261 sit on the NL
  400 profile's intermediate holes. **The drawing is an NL 400 rail.**
- **The bottom drawer's line is 99 mm above the bottom panel.** The sides sit on the bottom panel in the shop's
  Cabineo joint (Drive-only `cabineo-joint-geometry-reconciled.md`: bottom bores 11.9 from the outer faces). **Blum
  needs ≥ side height**, so N/M fit and K/H do not, and the import holds K and H only.
- Holes are **Ø5 × 5**: a pilot for chipboard screws, too shallow for system screws.
- **Asked of the owner:** the bottom drawer's height, and whether NL 400 is intended for a 570-deep side.

`blum-metabox-smartcabinet-input.md` §7 amended in place with the check.

## (2) Noticed

- **The morning `Raw/` check missed this file.** It was queried by `modifiedTime > 2026-10-02T17:00Z` and returned
  only the `Blum` folder, though `Side Left.pdf` was created 06:38 today. *A title query found it at once.* The
  session-start `Raw/` check should list the folder, not filter by date.

## (3) The imported rail row — and a correction to two articles

The owner sent a photo of *Guide Cassetto*: one METABOX row, **`320M4000C`** (`LX` 5, `LY` 18, `CX` 0, `LBox` 398,
holes X 37/165/261/357 · Y 81 · Ø5 · φ5), and five LEGRABOX rows.

- **The bottom-drawer question from (1) is answered: the rail is M (86), not K/H.** `LY` 18 + `Y` 81 = **99**,
  exactly the drawing; Blum needs ≥ 88. **It fits, with 11 mm to spare.** The NL 400 reading is confirmed by
  the name.
- `LBox` 398 = Blum's base NL − 2 ✓. `LX` 5 is consistent with LW − 31 if the box system counts a ~10.5 mm side.
  **The cutting list's base width (LW − 31) is the check.**
- **Correction, owned.** On 2026-10-02 both `blum-metabox-smartcabinet-input.md` (§2, §7) and
  `blum-runners-tandem-movento-smartcabinet-input.md` (§5) read SmartCabinet's hole columns as **drawer-side**
  holes and said to leave them empty. **They are the cabinet-side runner holes.** The LEGRABOX rows carry
  LEGRABOX's cabinet-profile positions, and the METABOX row produced the Side Left holes. **Corrected in both
  articles, visibly**, with `Y` for TANDEM/MOVENTO derived (≈ 22.5) and `LX` settled as per side.
  *Lesson: the manual's "laterali dei cassetti" was ambiguous. The shop's own data should have been asked for
  before the mapping was written, and it was asked for (the LEGRABOX photo) — just after the articles went up,
  not before.*
- **Only one METABOX row is visible.** Each height and NL the shop builds needs its own row.

## (4) Pre-production review — `Raw/Review folder/350mm Base unit with Legrabox C Drawers/`

Owner: *"Please review the drawings before we proceed to manufacturing. 350mm unit with drawers, we are using
Metabox K system."* 15 `.TCN` programs + `worklist.xmlst` + `.fnm`, decoded by script (UTF-16; every `W#81` bore
listed). **Not yet reviewed:** the second job in the folder, `1050mm Base Corner Unit v1`.

**Carcass:** sides 851 × 570 × 19 standing on a 350 × 570 bottom (Cabineo), top rails 312 × 150, back 832 × 312 × 19
set 5.2 mm in from the rear edge, so the internal depth is ≈ 546. `03-BOTTOMB` is the plinth-leg pattern
(4 × Ø3 at 64 × 64, four places).

| Check | Programs | Blum METABOX K | Verdict |
|---|---|---|---|
| Rail holes, both sides | Ø5 × 5 at **37 · 165 · 261 · 357**, four lines, L/R mirrored | K, NL 400: **37, 165, 261, 357** (K page, PDF p. 403) | ✓ **exact**. *(Correction to (3): for K, 165/261 are Blum's own fixing holes, not extras)* |
| Rail height | lines 96.3 / 313.5 / 530.8 / 720 from the top end | `Y` 113 = K | ✓ |
| Bottom drawer | line **131** above the bottom panel | ≥ 118 + 2 | ✓ 11 spare |
| Top drawer | 77 below the top rails | ≥ 24 | ✓ |
| Between drawers | 217.2 / 217.3 / 189.2 | ≥ 120 + profile | ✓ |
| Front fixing (4 fronts 347 × 214.3) | Ø3 × 5 pilots, **26** from each edge, 64 apart | screw-on bracket: FA (17.5) + **8.5** = 26; holes **40.5 and 104.5** above the box bottom | ✓ horizontally; vertically ≈ 38.7 / 102.8 by reconstruction, *depends on assumed front gaps; check on drawer 1* |
| **Drawer bottoms ×4** | **292 × 388 × 10** | **LW − 31 = 281 × NL − 2 = 398 × 16 mm** | **✗ 11 mm too wide** (will not fit between the steel sides), **10 mm short, 10 mm instead of 16** |
| Drawer bottom machining | 2 mm cuts, tool **182**, at X 38 / 254, Y 348–816, mostly **off** the 388 panel | none (screw-on version) | **✗ anomaly**: looks like a wooden-box leftover |
| Drawer backs ×4, `FRONTAL` ×4 | listed in the `.fnm`, **no CNC program**: sizes unknown | back **281 × 103 × 16** | **? need the cutting list.** A METABOX drawer has no inner front, so the 4 `FRONTAL` parts may be superfluous |
| NL | 400 | internal depth ≈ 546 allows **NL 500** (≥ 505 with BLUMOTION) | **? intent.** NL 500 K holes: 37, 165, 261, 389, 453 |
| Folder name | *"Legrabox C Drawers"* | programs are METABOX K | naming only |

**Verdict given to the owner:** carcass and fronts are right for METABOX K NL 400. **Do not cut the drawer
bottoms.** Likely cause: the box configuration (`Box Config file` / `.SCS` on the METABOX *Scatola Cassetto* row)
is still building a wooden-drawer base. The sides are correctly omitted (System = metal); base thickness, width
and length are not.

## (5) The cutting list — `Cutting list.pdf` in the same folder

Owner: *"check folder for cutting list."* `Cutting list.pdf` (181,121 B, id `1RfN50UrZ1Lljk6lcbOGzkTiEZIUCWwTd`,
4 pages, optimiser output, 4 mm blade) holds **two boards and 10 parts only**:

- **W1100 ST9, 19 mm** (2800 × 2070, 26 % used): sides 851 × 570 ×2, bottom 350 × 570, top rails 312 × 150 ×2,
  back 832 × 312. **Matches the programs.**
- **U963 ST9 Diamond Grey, 19 mm** (5 % used): drawer fronts **347 × 214** ×4. *The programs say 214.3. Most likely
  the list rounds for display; the saw operator should cut to 214.3, or the gaps change.*

**Not on the cutting list at all: the 4 drawer bottoms, 4 drawer backs and 4 `FRONTAL` parts.** No board is
planned for the drawer boxes. So the base error in (4) has a second half: even corrected, the drawer parts will
not be cut unless they are added. Blum K, NL 400: **base 281 × 398 × 16**, **back 281 × 103 × 16**, no inner front.

## (6) Pre-production review — `1050mm Base Corner Unit v1`

Owner: *"Review the 1050 corner unit now."* 8 `.TCN` + worklist + `.fnm`; **no cutting list in this folder**.
Decoded by script, every bore and pocket checked joint by joint. *Method note, worth keeping: a Cabineo pocket's
`W#89` X is the circle's **start point**, 7.5 mm (one Ø15 radius) from its centre. Read naively, the back-to-bottom
joints look 7.5 mm out. They are not: centre 50 + 19 = 69, exactly the bottom's bore.*

**Parts:** sides 701 × 570 ×2, bottom 1050 × 570 (sides stand on it), top rails 1012 × 150 ×2, fixed shelf 1011 × 441,
back 1012 × 682. All 19 mm.

| Joint / feature | Programs | Verdict |
|---|---|---|
| Sides → bottom (Cabineo) | side pockets Y 40 / 285 / 530 ↔ bottom Ø5 × 12 at X 11.9 / 1038.1, same Y | ✓ |
| Back → bottom (Cabineo ×5) | back pocket centres 50 … 962 (+19) ↔ bottom Ø5 at 69 … 981, Y 462.9 | ✓ |
| Back → sides (Cabineo ×3 each) | back Y 50 / 341 / 632 ↔ side X 651 / 360 / 69 (left; right mirrored) | ✓ |
| Top rails → sides | **Ø8 dowels**: rail ends Ø8 × 30 at 15 / 75 / 135; sides Ø8 × 12 at 9.5 | ✓ fits (42 for a 40 dowel). **Differs from the 350 unit, which uses Cabineo for its rails**: glue needed, intended? |
| Shelf (Cabineo both ends, Y 74 / 367) | sides: two System 32 rows Ø5 × 12 at **84 / 377** from the front, 7 holes each, 32 pitch | ✓ **if the shelf sits 10 mm back**: its screws land in the shelf-pin holes, so the fixed shelf is re-positionable. Shelf 441 + 10 clears the back (455.8) by 4.8 |
| Width | rails 1012 = 1050 − 38; shelf 1011 | ✓ |

**Questions raised with the owner, none of them errors in the joinery:**

1. **Carcass height.** This unit is **720** (701 + 19); the 350 drawer unit is **870** (851 + 19). Both have the same leg
   pattern. On the same run they are 150 mm apart. **One of them is probably wrong.**
2. **No door and no hinge drilling.** No door part, and no 37/32 mounting-plate holes on either side. How is the corner
   closed: door on a filler, or made separately?
3. **The back is set 107 mm forward** (side bores at Y 462.9; the 350 unit's at 552.9), leaving a ~95 mm void behind
   it. Sink/services void, intended?
4. **Four legs under a 1050 bottom**, all at the ends (X 13–77 and 973–1037). *Judgement, not a spec:* add a middle
   pair.
5. No cutting list in this folder.

## (7) 350 mm unit, version 2 — `Review folder/350mm Base unit with Metabox K/`

Owner: *"I have updated with new folder for 350mm wide Base unit."* The old *Legrabox C* folder is gone. 15 `.TCN`
+ worklist + `.fnm` (still named *…Legrabox C Drawers.fnm*); **no cutting list**. **Compared byte-for-byte with
version 1**:

| Part | v2 against v1 | Verdict |
|---|---|---|
| Sides | **851 → 701**: the carcass is now **720**, the same as the corner unit | ✓ **question 1 of (6) resolved** |
| Rail lines (from the top) | 58.8 / 238.5 / 418.3 / 570, both sides mirrored; still 37 · 165 · 261 · 357, Ø5 × 5 | ✓ K, NL 400. Bottom drawer **131** above the bottom panel (≥ 120); top **39.8** below the rails (≥ 24); gaps 179.7 / 179.8 / 151.7 |
| Back | 832 → **682** × 312; side bores re-placed (70 / 341 / 612 from the bottom) | ✓ consistent |
| Bottom, top rails, legs | **byte-identical** to v1 | ✓ |
| Fronts | 214.3 → **176.8** high (4 × 176.8 + 4 × 3.2 = 720); Ø3 pilots 26 from the edges, 64 apart | ✓. Heights reconstruct to **~2 mm** off Blum's 40.5 / 104.5 *consistently on all four*, within the front's height adjustment (or BLUMOTION's +2) |
| **Drawer bottoms ×4** | **byte-identical to v1**: still **292 × 388 × 10**, still the tool-182 cuts off the panel | **✗ NOT FIXED** |
| Drawer backs, `FRONTAL` ×4 | still in the `.fnm`, still no program, no cutting list | **✗ still unplanned** |
| NL | still 400 against ≈ 546 internal depth | **? unanswered** |

Also: a copy of the folder *"Shelf unit for TV unit 30_09"* sits **inside** the 350 folder as well as beside it,
probably dropped in by accident. Not reviewed yet.

## (8) Pre-production review — `Shelf unit for TV unit 30_09`

Owner: *"Yes, review the TV shelf unit."* Two copies exist (beside and inside the 350 folder). **Their programs are
identical by md5**; only the outer copy has the cutting list. Reviewed the outer one: 10 `.TCN`, worklist, `.fnm`,
`Cutting list Shelf unit for TV unit 30 09.pdf` (one board, **H1307 ST19 Brown Warmia Walnut** 19 mm, 38 % used).

**Unit:** 500 wide × 1780 high × 250 deep. Sides 1780 × 250 run full height; bottom and top 462 × 250 sit between
them; three shelves 461 × 211; full 19 mm back 1742 × 462 inside the carcass. **The cutting list matches the
programs part for part (8 parts).**

| Joint | Programs | Verdict |
|---|---|---|
| Bottom / top → sides (Cabineo, 2 per end) | pockets in the machined faces (`BOTTOMB` underside, `UPB` top) at Y 40 / 210, centres 3.6 from the end ↔ side Ø5 × 12 at **7.1** from each end, Y 40 / 210 | ✓ (axis 7.1 from the machined face, flush with the side's end) |
| Back → bottom / top (×3 each) | back pockets at 50 / 231 / 412 ↔ bottom and top Ø5 at 50 / 231 / 412, Y 232.9 | ✓ |
| Back → sides (×7 each) | back pocket centres 50 … 1692 (+19) ↔ side Ø5 at 69 … 1711, Y 232.9 | ✓ all seven |
| Back position | inner face 225.8, set 5.2 in from the rear: same as the kitchen units | ✓ |
| Shelves (Cabineo both ends, Y 40 / 171) | sides: three bands of **5 × Ø5 × 12 at 32 pitch**, rows **Y 50 / 181**; left and right mirrored correctly | ✓ shelf sits 10 back, its screws land in the pin holes, so each shelf has 5 heights. 10 + 211 = 221 clears the back (225.8) |
| Widths | 462 = 500 − 38; shelves 461 | ✓ |

**Verdict: correct as drawn, ready to make.** One recommendation, judgement rather than a defect: **a 1780-tall,
250-deep unit should be fixed to the wall against tipping**, and the programs carry no wall-fixing provision.
Fit a bracket or screw through the back on site. The duplicate copy inside the 350 folder can be deleted by the owner.

## (9) Owner's decision — NL 400

Owner: *"Use 400 mm rails, keep as is."* **NL 400 is the owner's choice for the 350 mm METABOX K unit, and the open question
is closed.** The rail holes (37 · 165 · 261 · 357) and the drawer clearances stay as reviewed in (7). **Still open on
this unit:** drawer bottoms (need **281 × 398 × 16**; the programs say 292 × 388 × 10) and drawer backs (**281 × 103 × 16**),
not yet on a cutting list.

## (10) 350 mm unit, version 3 — same folder, files replaced, cutting list added

Owner: *"I have updated the 350 unit folder again."* Programs compared byte-for-byte with v2; joints re-checked
across v1–v3 by script. New: `Cutting list for Base Unit with Metabox K.pdf` (6 pp., three boards).

**Carcass ✓.** The only program changes are the **top-rail joints**, moved from 30 / 120 to **40 / 110** on the rails
and to 40 / 110 / 460 / 530 on both sides. Consistent: back rail at 420 + 40 / 110. Sides to bottom are unchanged
(40 / 270 / 500 ↔ 40 / 270 / 500). v1 and v2 were also consistent; this is a deliberate move, not a fix. Back,
bottom, legs and fronts are unchanged.

**Drawer parts: the cutting list now has them, but they are still not Blum's METABOX K / NL 400:**

| Part | Cutting list (board) | Program | Blum | Verdict |
|---|---|---|---|---|
| Bottom ×4 | **292 × 388**, U961 ST7 Graphite Grey **16** | 292 × 388 × **10**, byte-identical to v1/v2 (incl. tool-182 cuts) | **281 × 398 × 16** | **✗** width +11, length −10. **The program is stale**: it still says 10 mm |
| Back ×4 | **302 × 103**, Graphite Grey 16 | none | **281 × 103 × 16** | **✗ width +21** (height ✓) |
| `FRONTAL` ×4 | **302 × 103**, **U963 Diamond Grey 19** | none | **none**: METABOX has no inner front | **✗ not needed**, and 302 will not pass between the steel sides |
| Fronts ×4 | **347 × 177**, on the **Graphite Grey 16** board | 347 × 176.8 × **19** | — | **✗? material**: v1 had them on Diamond Grey 19, and the programs still say 19. **Looks swapped with `FRONTAL`** |

**Likely single root cause** *(derived)*: SmartCabinet builds the box **302 wide = LW − 2 × `LX` (5)**, as if the
drawer sides were **0 mm thick**. Blum's wooden parts are **LW − 31**, i.e. 15.5 a side = `LX` 5 + **~10.5 for the
steel side**. **Giving the METABOX box system a 10.5 mm side** would bring back and base to 281 at once. **The base
length** wants SmartCabinet's *"extend the bottom under the back"* option (*Progettazione cassetti* ➑a): Blum's base
is NL − 2 = 398 with the back standing on it. **Delete or disable the `FRONTAL` part**; restore the fronts to
19 mm Diamond Grey.

## (11) 350 mm unit, version 4 — only the cutting list changed

Owner: *"I have updated the 350 unit folder again."* **All 15 programs, the worklist and `.fnm` have the same md5 as
v3.** Only `Cutting list for Base Unit with Metabox K.pdf` is new (07:46).

| Item | v3 | v4 | Verdict |
|---|---|---|---|
| `FRONTAL` ×4 | 302 × 103, Diamond Grey 19 | **gone** | **✓ fixed** |
| Fronts ×4 | 347 × 177 on Graphite 16 | **347 × 177 on U963 Diamond Grey 19** | **✓ fixed**, matches the 19 mm programs |
| Carcass (W1100, 19) | 6 parts | unchanged | ✓ |
| Backs ×4 (Graphite 16) | 302 × 103 | **302 × 103** | **✗ still 21 too wide**: Blum 281 × 103 × 16 |
| Bottoms ×4 (Graphite 16) | 292 × 388 | **292 × 388** | **✗ still**: Blum 281 × 398 × 16 |
| Bottom programs | 10 mm, tool-182 cuts | **unchanged** | **✗ stale**: they disagree with the 16 mm on the cutting list |

Two of four drawer issues fixed. **Still blocking:** box width (the side-thickness setting, (10)) and base length
(*extend the bottom under the back*), then regenerate the programs so the bottoms are re-programmed at 16 mm.

## (12) Drawer-box settings for METABOX — `blum-metabox-smartcabinet-input.md` §7a

Owner: *"I need help with drawer box settings in SmartCabinet."* Read the manual's *Progettazione dei Cassetti*
(the box window: side / base / front / back thicknesses, back-to-side joint, base extension) and fetched Kosmosoft's
**`legrabox_default_scs.pdf`** and **`parametri_legrabox_ini.pdf`**: the `.SCS` parameters for prefabricated sides.
**Diagnosis:** the 302-wide back is what `bCassDDIE=0` produces (back across the sides' outer edges), and the
292 base is consistent with a side thickness well under the 10.5 METABOX needs. **Proposed set** (LX 5, LY 18, sides
10.5, base dz 0, base 16, back 16, front 0, back between the sides, back standing on the base) written into §7a with
the expected result to check. *Derived values flagged; no METABOX `.SCS` from Kosmosoft has been seen.*

## (13) The English *Drawer Box settings* window mapped

The owner sent a screenshot of the English window. Mapped field by field to the Italian manual's numbering in
`blum-metabox-smartcabinet-input.md` §7a. **The values found reproduce the bad parts exactly**: sides 16 with 10 mm
grooves → base ≈ 292; back joint "back across the sides" → back 302. **Changes given:** sides **10.5**, front **0**,
back joint **2nd option**, base-under-front-and-back **on**, groove depths **0 / 0**. Save as a named `.SCS`, **not**
*Set as Default*. Also visible: *Drawer guide* now reads **`320K4000C METABOX`** (the K rail row exists) and *Box
system* **METABOX K** on each drawer.

## (14) 350 mm unit, version 5 — after the drawer-box settings

Owner regenerated after setting the box window (13). Compared with v4; nesting programs decoded.

| Item | v5 | Blum K / NL 400 | Verdict |
|---|---|---|---|
| Base ×4 | **281** × **382** × 16 | 281 × **398** × 16 | **width ✓; length 16 short** |
| Back ×4 | **281** × **87** × 16 | 281 × **103** × 16 | **width ✓; height 16 short** |
| Inner front | gone | none | ✓ |
| Fronts | 347 × 176.8 × 19, Diamond Grey; screw pilots moved 11 mm with the rails | — | ✓ consistent |
| Rail lines (from the top) | **47.8** / 227.5 / 407.3 / 570, mirrored | top ≥ 24 below the rails; bottom ≥ 120 | ✓ top **28.8**; bottom 131; gaps ≥ 162.7 |
| Carcass | unchanged | — | ✓ |
| **New: nesting** | `27-NESTING01-SP19-W1100`, `28-…02-SP16-U961`, `29-…03-SP19-U963`: full-sheet cut-and-drill programs | — | contours carry **no tool number** (`#205=` blank): check in TpaCAD before running. **`NESTING02` has no tool-182 cuts** |
| Single bottom programs | still two **tool-182** cuts, now **8 mm deep**, 38 from each edge, running off the 382 panel | none | **✗ unexplained**: do not run these single files; the nesting doesn't include them |
| **Stale files** | v4's `13-…2-FRONT`, `16-…2-BOTTOM` (292 × 388 × 10), `19-…3-FRONT`, `22-…3-BOTTOM` (old), `25-…4-FRONT`, `28-…4-BOTTOM` (old) still in the folder; **new numbering re-uses 22 and 25** | — | **✗ delete them**: one wrong file is one click away |

**Why the base and back are both 16 short:** with *base under front and back* ticked, SmartCabinet stands the back
on the base and takes the base out of the back's height (103 − 16 = **87**). The base stops at **382 = 398 − 16**.
**Two routes given to the owner:** (A) **untick it**. The back goes back to **103** and runs down past a 382 base:
overall box depth 382 + 16 = **398**, the same as Blum, with only the base/back joint differing from Blum's drawing.
(B) keep Blum's exact build (398 base, back on it) by raising the back height and box depth. **Not recommended
until tested**: this KB has no verified setting for it.

## (15) 350 mm unit, version 6 — folder cleaned, drawer sizes unchanged

Owner: *"I have updated the 350 unit folder again."* **The six stale v4 files are gone**: the folder now holds
exactly the worklist's 18 programs, plus `.fnm` and the cutting list. **Every program is byte-identical to v5**. The
cutting list was re-exported (new md5) with the **same parts**: base 281 × 382, back 281 × 87. **Still open:** base 16
short / back 16 short (routes A and B in (14)); tool-182 cuts in the single bottom files (the nesting has none);
no tool number on the nesting contours.

## (16) Unticking "base under front and back" changed nothing

Owner: *"I done it, but it still generates same sizes."* **So that checkbox is not what puts the back on the base.**
Kosmosoft's sheet says prefabricated-side boxes have **further parameters only in the `.SCS` file**, and two of them
govern exactly this: `bCassDIESOT` (0 = back runs down past the base, 1 = back stands on the base) and
`bCassDIESOTFILO` (with DIESOT = 0: 1 = back down to the underside of the base). **The window does not appear to
show them.** The 87 = 103 − 16 is what `bCassDIESOT=1` produces, which matches §7a's own instruction to set it to 1:
*my instruction, and the cause of the 87.* **Asked of the owner:** set `bCassDIESOT=0` and `bCassDIESOTFILO=1` in the
saved `METABOX_K.scs` (Notepad, copy first), reload and regenerate. Expected **back 281 × 103**, base 281 × 382: **398**
overall. Also check that **BH = 103** on the METABOX K row of *Scatola Cassetto*. Better still, put the `.SCS` file in
`Raw/` so the values can be read rather than inferred.

## (17) The `.SCS` file read — `cass_sot_dy=16` is the 87 mm back

The owner photographed the `.SCS` in Notepad (lines from `cass_sp_P_CP` down; the first lines, incl.
`cass01` / `cass03` / `cass05`, were off-screen). **`bCassDIESOT=0` and `bCassDIESOTFILO=1` were already set**, so (16)'s
fix was already in place and could not have changed anything. **The cause is `cass_sot_dy=16.00`**: the base sits
16 above the bottom of the steel sides, and the back, running down to the base's underside, comes out
103 − 16 = **87**. **Fix given: `cass_sot_dy=0.00`.** Expected: back **281 × 103**, base 281 × 382 (398 overall). Also
asked: scroll up to confirm `cass05_spess=10.50`, `cass01_dist_lat=5.00`, `cass03_dist_sot=18.00`. The Notepad tabs read
*FP-Inbox-Report-Routine-Prompt* and *Scripts.txt*, so **confirm the open file is the `.SCS` that the METABOX row
loads**. Rest of the file as read: base 16, back 16, front 0, dz 0, back between the sides (`bCassDDIE=1`), no
mitre, `szEccCass=CABINEO` (irrelevant with no wooden sides).

## (18) 350 mm unit, version 7 — back still 87

Every program is **byte-identical to v6**. The nesting programs were removed (worklist re-exported). Cutting list
unchanged: base 281 × 382, **back 281 × 87**. **So the `cass_sot_dy=0` change did not reach the output**: either it
was not reloaded, or the back height comes from elsewhere. *Two of my three diagnoses on this point have now failed
in practice, so I stopped inferring.* Mapping read from the screenshots: the window's 4th-row middle group **teal 16 =
`cass_sot_inc`** and **red 16 = `cass_sot_dy`**, matching the file's `cass_sot_inc=16` / `cass_sot_dy=16`. **Asked of
the owner:** set the red 16 to 0 **in the window itself**, save, tick, regenerate. If the back is still 87, send the
METABOX K row of the drawer-box table (H, BH …), because a `BH` of 87 there would explain it. **If that fails too,
take it to Kosmosoft support** (the shop's contract covers it) rather than iterate further.

## (19) 350 mm unit, version 8 — Way 2 loads the file: back height fixed, width lost

Owner: *"Way 2: on the METABOX row … this way works."* **Loading the `.SCS` through *Box Config file* on the METABOX
row is the route that takes effect.** Recorded as the method. Result against v7:

| Part | v7 | v8 | Blum | Verdict |
|---|---|---|---|---|
| Back ×4 | 281 × 87 | **302 × 103** | 281 × 103 | **height ✓ fixed**; width ✗ back to 302 |
| Base ×4 | 281 × 382 | **302 × 382** | 281 × 382 (route A) | width ✗ back to 302 |
| Everything else | — | byte-identical to v7; `NESTING01`/`03` back, `NESTING02` (graphite) absent | — | ✓ |

**Reading:** 302 = LW − 2 × 5, i.e. the file now loaded has **`cass05_spess` at 0, not 10.50**. The 10.5 typed in the
window earlier never went into this file (the owner's photo of it started below the `cass05` line). **Fix given:**
in the same `.SCS`, set `cass05_spess=10.50`, keep `cass_sot_dy=0.00`, save, restart SmartCabinet, regenerate.
Expected: **base 281 × 382, back 281 × 103**. Also recorded in `blum-metabox-smartcabinet-input.md` §7a: **edit the
`.SCS` and load it on the METABOX row; the window's own save does not reach the box system.**

## (20) 350 mm unit, version 9 — drawer parts right; job ready

Owner set `cass05_spess=10.50` in the `.SCS` and loaded it on the METABOX row. **Drawer bottoms 281 × 382 × 16 and
backs 281 × 103 × 16**, on the cutting list and in `28-NESTING02-SP16-U961` (4 + 4 contours, exact sizes).
**Every carcass and front program is byte-identical to v8.** The **verified `.SCS` set is now written into §7a** as
the METABOX K standard.

**Verdict given: ready to make, from the nesting programs / cutting list.** Two checks kept:
- The single `…DRAWER-n-BOTTOM.TCN` files still carry two **tool-182, 8 mm** cuts running mostly off the panel. The
  nesting has none. **Do not run the single bottom files.**
- The nesting contours carry no tool number: confirm the cutter in TpaCAD's simulation before the first sheet.

## (21) 1050 corner unit — blind corner, door on the right, 500 wide: the plan given

Owner: *"Blind corner, door on the right, 500 wide."* Read SmartCabinet's *Ante* pages (`ante_progettazione`,
`ante_ferramenta`, fetched 2026-10-03). The door types include **single door opening on the left with hinges on the
right** and a **fixed door (*anta fissa*) for closing a space permanently**, plus *shorten left / right / top / bottom*
parameters. In *door hardware*: hinge model, **number of hinges (auto by size if blank)**, and distance of the top /
bottom hinge from the door edges.

**Plan given (derived; check after regeneration):**
- **Door:** single, hinges on the **right cabinet side**, full overlay. Full-width door would be 1050 − 3 = 1047;
  **shorten left by 547 → 500**. Height as the 350 unit's fronts (720 with the shop's 3.2 gap → **716.8**).
- **Hinge:** the shop's **71B3550** (CLIP top BLUMOTION 110°, overlay, screw-on). FA = 19 − 1.5 = **17.5** → with plate
  MD 0, **TB 6.5** (FA = 11 + TB − MD, `blum-clip-top-hinges-smartcabinet-input.md` §4), so the **cup centre is 24 from
  the door edge**, Ø35 × 13. **2 hinges** (≈ 716 high, ~4–5 kg at 19 mm: Blum's 2-hinge band ≤ ~750 / 4–6 kg).
  Plate holes in the right side at **37 from the front, 32 apart**: clear of the shelf-pin band (242–434 above the base).
- **Blank:** 1047 − 500 − 3 = **544** × 716.8, as a fixed door (*anta fissa*) or a loose part fixed on site. Asked
  which the shop prefers.
- Still unanswered: **the back's 107 mm setback** and the **middle legs**.

## (22) Corner unit — owner's decisions, and where they are set in SmartCabinet

Owner: *"Fixed door in SmartCabinet, back at the rear, add middle legs."* Read `progettazione_schienale`,
`tabelle_cam_accessori_piedini` and `progettazione_zoccolo` (fetched 2026-10-03).

- **Blank = fixed door** (*Ante fisse*: *"for closing a space permanently"*). **544** wide (shorten **right** by 503),
  716.8 high, in the fronts' Diamond Grey. If SmartCabinet allows one door per space and the second replaces the
  first, the front must be split (grid / divider): to be looked up if it happens.
- **Back to the rear:** the corner unit's back is the *internal* type (*schienale interno*), whose setting is **how far
  in from the rear edge**. The 350 unit's side bores sit at **552.9** (back face ~5 mm in); the corner unit's at
  **462.9**, 90 further in. **Copy the 350 unit's value.** Expected after regeneration: side and bottom back-joint bores at
  Y **552.9**, as on the 350 unit.
- **Middle legs:** the leg table sets each leg's **hole pattern** (the shop's 4 × Ø3 at 64 × 64 underneath = Type 3), not
  how many legs or where. **The control for count / position was not found in the pages read**: told the owner
  so. Fallback: the plinth legs screw on; a middle pair can be fixed at assembly without CNC holes.

## (23) Corner unit — "it's not allowing to split into two doors": dummy divider

Owner: *"1. problem. it's not allowing to split into two doors."* Confirms one door per space. Read
`progettazione_divisori_v` and `progettazione_griglie` (fetched 2026-10-03). **Both pages say the same: a divider or
grid with thickness 0 is *fittizio* (dummy): it only creates spaces for doors and drawers, with no part and no CN
machining.** Given: Vertical dividers → **1**, **thickness 0**, set the **right space** width (spaces numbered from the
left; 0 = automatic). **Start at ~484** *(derived: 500 door − 17.5 overlay on the right side + 1.5 half-gap)* and correct
by the difference shown. Then **right space: single door, hinges right, 71B3550**; **left space: fixed door**;
shortening values back to **0**. **Check on regeneration:** the shelf must still come out as **one 1011 piece**. A
divider may split it into two.

## (24) Legs CAM table photographed

The owner sent *Cam Table: Legs*: **TD130 — Type 3, Scheme 3, 64 / 64, Ø3, depth 13** (four Ø3 × 13 holes at 64 × 64 in the
underside of the bottom). **This confirms (22): the table sets the hole pattern per leg, not the number of legs or
their positions.** Asked for the cabinet-side place where the legs are assigned (likely the cabinet's hardware
panel, near *Wall Support*). Fallback stands: screw the middle pair on at assembly.

## (25) Middle legs — found by the owner

Owner, with a photo of the cabinet's **Legs** panel: *"Blue value is max distance between legs, I have lowered to
500mm and now have one pair extra in the middle."* **Recorded as the method:** *Legs* panel → **blue dot = maximum
distance between legs**. Above it SmartCabinet adds intermediate pairs. Other fields read: **45 / 45** in from the sides
(front and back rows), **85** (back row) and **80** (front row) in from the edges, *Add on Divider* ticked. For the 1050
unit: end-leg span 1050 − 90 = 960 > 500 → **one middle pair** at ~525 *(derived)*. **Caution given:** *Add on Divider*
is ticked and the corner unit now has a **0 mm dummy divider**. Check the regenerated `BOTTOMB` for a **second, unwanted
pair under the divider line** (~528–547 from the left), next to the middle pair; untick it if so.

## (26) Corner unit v2 — `Review folder/1050mm Base Corner Unit v2/`

14 programs + worklist + `.fnm`, decoded by script; **no cutting list**. v1's folder is gone from *Review*.

| Item | v2 | Verdict |
|---|---|---|
| **Hinges** | door `10-DOOR-2` 716 × **516**: 2 × **Ø35 × 13** cups **100 from each end**, **22.5** from the hinge edge (TB 5); screw pilots Ø3 × 5, 45 apart, 9.5 behind. Right side: plate pilots **Ø3 × 5 at 37 from the front, 32 apart**, centred at 102 / 618 above the carcass underside | ✓ **cups and plates line up exactly** (side + 19 = door + 2). FA with TB 5 / MD 0 is 16 against the needed 17.5: **within the hinge's ±2 side adjustment** |
| **Door width** | **516** | **✗ 500 wanted**: reduce space 2 by 16 |
| **Blank** (`09-DOOR-1`, fixed) | 716 × **528**, Ø8 × 12 dowels on three edges ↔ left side front edge, bottom front edge, front rail edge (Ø8 × 30) | ✓ every dowel aligns (offsets = the 2 mm / 1.5 mm gaps). Becomes **544** when the door is 500 |
| **Back** | side and bottom bores still at **Y 462.9** | **✗ not moved**: still ~95 mm forward |
| **Shelf** | **split into 511 + 499** at the dummy divider; each half fixed to its side and, by two Cabineo, to the back (new `08-BACK-1B`: 4 columns × 7 Ø5 × 12) | **✗ as warned**: the two front corners at the split have no support. **Fix:** one 1011 shelf. v1's `06-SHELF-1.TCN` (1011 × 441) still fits the unchanged side pin rows; skip `08-BACK-1B` |
| **Legs** | 6: ends + **one middle pair** at X 487–551 | ✓, **no extra pair at the divider** |
| Top rails | now **Cabineo** (back rail 200 wide), sides Ø5 at 15 / 135 / 385 / 555 | ✓ consistent; now matches the 350 unit |
| **Side ↔ bottom Cabineo** | pockets moved to the **`B` (outer) face** of both sides; bottom bores at **7.1** (v1: inner face, 11.9) | **? pockets now on the outside of both sides**: visible on any exposed end. Intended? |
| Front heights | door / blank **716** (2 mm top and bottom) vs the 350 unit's **176.8 × 4 with 3.2 gaps** | ? 1–2 mm line difference if the units stand side by side |

## (27) Corner unit — the back position is intentional (owner's ruling)

The owner, replying to (26): **the back is set forward on purpose, so that pipes can run behind the unit.** The "**✗ not
moved**" row in (26) is therefore **withdrawn**: the back at **Y 462.9** is the design, not a fault, and it is **not** to be
moved to the rear or copied from the 350 unit.

**Consequences, checked against v2:** the shelf (one 1011 piece, per (26)) and the bottom stay within the depth in front of
the back, so the void does not affect them. What remains to fix on the corner unit: **door 516 → 500** (blank becomes 544) and
**one 1011 shelf instead of 511 + 499** (skip `08-BACK-1B`). Questions still open: Cabineo pockets on the outer faces of
both sides; 716 / 2 mm gaps vs the 350 unit's 3.2 mm; no cutting list in the folder.

*Lesson for future reviews:* a back set in from the rear on a base unit can be a **service void**; ask before calling it a
fault.

## (28) Corner unit v2, regenerated 10:41 — door and blank fixed; shelf still split

Same folder, regenerated; **cutting list now present** (3 pages). Sides (`01`/`02` and their `B` faces), back `08-BACK-1`
and back rail are **byte-identical** to (26); `08-BACK-1B` is **gone**.

| Item | Regenerated | Verdict |
|---|---|---|
| **Door** `10-DOOR-2` | **716 × 500**; cups Ø35 × 13 at 100 / 616, **22.5** from the hinge edge | ✓. Right side unchanged → plates still line up |
| **Blank** `09-DOOR-1` | **716 × 544**; Ø8 dowels at 105.5 … 457.5 | ✓ align with the bottom (107 … 459, the same 1.5 offset as before) and the front rail (924 … 572 mirrored; sum 1031 as before) |
| **Back** | Y 462.9 | ✓ intentional, pipe void (27) |
| **Legs** | middle pair moved to X **471–535** (follows the divider) | ✓ one middle pair |
| **Shelf** | **still split, now 527 + 483**. Each piece: two Cabineo to its side (into the side's Ø5 / 32 rows at 84 / 377) **and two Cabineo at the split end that now meet nothing** — the back fixing went with `08-BACK-1B` | **✗ worse than v2**: each half is held only at its outer end. **Fix: one 1011 shelf.** v1's `06-SHELF-1.TCN` (1011 × 441, Cabineo at both ends, slots at Y 83.5 / 376.4) **still fits**: the sides' rows (84 / 377, 458.4→266.4, pitch 32) are unchanged. Cut it in place of `06` + `07`, or get SmartCabinet to put the shelf across the whole carcass (the split follows the dummy divider) |
| Side Cabineo on the outer faces | unchanged | ? still to be answered |
| Front gaps | 716 / 2 mm vs the 350 unit's 3.2 | ? still to be answered |

**Verdict given:** everything except the shelf is ready; **do not cut `06-SHELF-1` / `07-SHELF-2` from this set**.

## (29) Corner unit — owner's answers to the two open questions

1. **Cabineo pockets on the outer faces of both sides: intended** (owner). Closed.
2. **Match the front gaps to the 350 unit: yes** (owner). **Correction to my own (26) figure, worked out before asking for
   a change:** both carcasses are 720 high (701 sides on a 19 bottom). The 350 unit's stack is 4 × 176.8 + 3 × 3.2 = 716.8,
   so its **top and bottom gaps are 1.6**; the corner unit's are **2.0** (716). **The edges differ by 0.4 mm at the top and
   0.4 at the bottom, not the "1–2 mm" I gave**: the 3.2 is the gap *between* drawers, which has no counterpart on a
   single door. To match exactly: set the corner unit's top/bottom front gap to **1.6** → door and blank **716.8** high.
   Left to the owner whether 0.4 mm is worth the regeneration.

## (30) Corner unit — closed by the owner

Owner: *"all good and noted about shelves"*. Read as: the regenerated set (28) is accepted as is, the **2 mm front gaps
stay** (0.4 mm difference accepted, (29)), and the owner will handle the shelf themselves (one 1011 shelf, **not**
`06-SHELF-1` + `07-SHELF-2` from this set, (28)). **Corner unit review closed.** All three Review-folder units now
reviewed: 350 METABOX K (v9 ✓), TV shelf unit (✓), 1050 corner unit (✓ with the shelf caveat).

## (31) Blum, continued — LEGRABOX written up

Owner: *"please carry on with Blum."* **Next system chosen: LEGRABOX**, because the shop already has Kosmosoft's LEGRABOX
rows under `25 GUIDE CASSETTO` and Kosmosoft's `legrabox_default.scs`. **`Wiki/Processes/blum-legrabox-smartcabinet-input.md`
created** (**8,686 B**, id `17cZnqRHkDCo8BPCEuxV2IgD64zSFWHvo`, placeholder then in-place upload, downloaded back
byte-identical). From catalogue PDF pp. 196–246 (B1) and the two Kosmosoft sheets.

- **Heights** N/M/K/C/F: sides 66.5 / 90.5 / 128.5 / 177 / 241; chipboard backs **39 / 63 / 101 / 148 / 212**; space above
  the hole line 42 / 68 / 106 / 155 / 219 incl. 2 mm tilt *(drawing)*; hole line ≥ 38 above the part below.
- **Cutting:** base **LW − 35 × NL − 10** (NL − 21 with the steel back), back **LW − 38**, 16 mm chipboard. Cabinet depth ≥ NL + 3.
- **750 cabinet-profile holes** read off p. 242 per NL *(drawing)*. **The shop's Kosmosoft rows (37 · 69 · 261 · 293 · 357)
  agree** with the NL 550–600 pattern.
- **Kosmosoft's `.SCS` defaults against Blum:** widths come out right as shipped. `cass05_spess` 14 is a **notional** side
  (real 12.8), chosen so that 5 + 14 − 1.5 gives LW − 35. **Not to be "corrected".** Back thickness 19 vs Blum's 16 is an
  owner choice. **Depth and back height are unproven until the first LEGRABOX job's cutting list.** The check sheet is §5.
- **Open:** the base rebate (16 · 8 · 38) and whether SmartCabinet machines it; the 753 (70 kg) pattern; TIP-ON / SERVO-DRIVE /
  AMBIA-LINE not covered.
- `blum-library.md` (B1 row, needs table, Changes) and `Wiki/index.md` amended in place; registers rows added.
- Drive reports the new article as `text/plain`, not `text/markdown` like the older ones. The content is identical; noted.

## (32) Blum, continued — AVENTOS written up

Owner: *"Do AVENTOS next."* **`Wiki/Processes/blum-aventos-lift-systems-smartcabinet-input.md` created** (**9,783 B**, id
`1E-T8xFm0-Tqq3gEzaBzHXONCK7k8XY4q`, placeholder then in-place upload, downloaded back byte-identical). From catalogue PDF pp. 18–71 (L1–L7) and the
SmartCabinet manual page *Supporto Anta (Aventos)* (`tabelle_cam_accessori_aventos.html`, fetched today).

- **Choosing:** HK top / HK-S / HK-XS (stay lift), HL (lift up), HS (up and over), HF (bi-fold), by how the front opens and
  KH. **LF = KH × FG incl. handles.** HK top max. 18 kg on two mechanisms; a third mechanism gives +50 % LF.
- **Cabinet holes** *(drawing)*: HK top **37/69/133/165 at 36 from the top, Ø5 × 11.5**; HS/HL **37/229** at 80/88 + SOB;
  HF **37/229** at KH × 0.3 − 28 (KH < 550) or − 57; HK-S pegs 37/101 at 74; HK-XS 137 + MD + K + SOB.
- **Fronts:** HK top brackets at 62 + FAo, +32 ×3, SFA + 12.5 in; HF arm bracket X (70/47) below the lower front's
  mid-height. HF hinge set `78Z5500T12` (2 × 120° `70T5550.TL` + 2 × centre `78Z5500T`).
- **SmartCabinet:** one row per hole, S (cabinet: X from the front, Y from the top) or D (front: X from the top/bottom, Y
  from the sides), drilled both sides; `Min/Max H Anta` limit the rows; on HF the D holes go on the lower front. A
  worked S-row set for HK top is in §5. The **`Y`-datum (top of the side or underside of the top panel)** is left to check
  on a sample.
- **Correction, owned:** my reply after (31) said the shop's `79T8500` goes with AVENTOS HF. **It does not**: Blum p. 114
  lists it as the **corner-cabinet bi-fold hinge** (with a CLIP top 155° hinge). Recorded in the AVENTOS article and in
  `blum-clip-top-hinges-smartcabinet-input.md` §8.
- `blum-library.md`, `Wiki/index.md` and the registers amended in place.

## (33) AVENTOS — the front holes filled in

Owner sent *"Do AVENTOS next"* again, after (32) was already published. **Read as "carry on with AVENTOS"**, and the gap
(32) left was closed: §4 of `blum-aventos-lift-systems-smartcabinet-input.md` now has the **front fixing holes for HS, HL,
HK-S and HK-XS** *(drawing)*, read from PDF pp. 38, 44, 59 and 66:

| Type | Holes | Datum |
|---|---|---|
| HS | 196.5, +32 × 3 | SFA + 12.5 |
| HL | X = 153 / 203 / 253 / 303 by lever arm `20L3200` / `3500` / `3800` / `3900`, +32 × 3 | SFA + 12.5 |
| HK-S | 78 − F, 110 − F | SFA + 12.5 |
| HK-XS | 125.5 + MD + K, +32 (131.5 + MD + K at 100 deep) | SFA + 15.5 |

**The reference line differs between types** (HK top adds FAo; HK-S subtracts F). **One sample front to be drilled and
offered up before D rows go into SmartCabinet.** Article 9,783 -> 11,155 B, in place, same id; registers amended.

## (34) AVENTOS — chosen per customer

Owner: *"It depends from customer about Aventos."* **No house AVENTOS type**: the system is chosen per job. The open item
in the AVENTOS article §6 is closed and replaced by a **per-job routine**: type from §1 → LF = KH × FG incl. handles → part
numbers §2 → holes §3/§4 → SmartCabinet rows §5 → one sample per new type. Still open: whether Import Accessori already
holds Blum AVENTOS rows.

## (35) AVENTOS import check handed to the owner; Blum doors — BLUMOTION and TIP-ON

**AVENTOS import.** Owner: *"Need to check which Aventos SmartCabinet is already got for import from library."* Darius
cannot see the shop's SmartCabinet. **Steps given**, from the manual page *Import Accessori*: **+** → *Advanced search* →
Supplier Blum / AVENTOS → screenshot, without importing. Plus screenshots of the Accessory Register and *Supporto Anta
(Aventos)*. **Awaiting the owner's screenshots**: Darius will then check Kosmosoft's rows against the AVENTOS article.

**Next topic.** Owner: *"Move to next."* **`Wiki/Processes/blum-doors-blumotion-and-tip-on.md` created** (**6,722 B**, id `1HMICvxFvLfxy0ooKXvqwES9ifhZjnciG`,
placeholder then in-place upload, downloaded back byte-identical). From PDF p. 78 (CLIP top 110° order page), H3 pp. 160–173
and H4 pp. 174–177.

- **Soft close: nothing to add.** The shop's `71B3550/3650/3750` are CLIP top BLUMOTION. H3's separate units are only for
  hinges without it (glass, mini, alu, corner bi-fold `970.1002`).
- **TIP-ON needs a different hinge.** Blum pairs TIP-ON only with CLIP top **sprung** (`71T…`, with the 956A bumper unit) or
  **unsprung** (`70T…TL`, with the 956/956A magnet units), not BLUMOTION. Same drilling, different part number.
- **Units:** `956.1004` short (Ø10 × 50, fronts up to ~1300), `956A1004` long (Ø10 × 76, taller or inset), `956A1006` bumper.
  Front gap ≥ 1.5 (magnet) / 3.2 (bumper).
- **Fitting:** a drilled-in unit needs a **Ø10 × 50/76 edge bore**, *probably not possible on the K2 as read on 2026-09-23*:
  its Ø10 is vertical, and which bushes are horizontal is my inference. **Adapter plates avoid it**: 20/17 `956.1201`,
  20/32 `956A1201`, **37/32 cruciform `956A1501`** on the hinge-plate line.
- **SmartCabinet:** TIP-ON is not named on the door-hardware pages read. Route: a handle-less door with the sprung or
  unsprung hinge row (duplicate of the `71B` row) and an adapter plate; check Import Accessori first.
- `blum-library.md`, `Wiki/index.md`, `blum-clip-top-hinges-smartcabinet-input.md` (`related:`) and the registers amended
  in place.

## (36) Blum, one more batch — drawer add-ons

Owner: *"Let's do one more batch."* **`Wiki/Processes/blum-drawer-addons-tip-on-servo-drive-ambia-line.md` created**
(**6,364 B**, id `1ZVskCHZxTc5kzDMIdlBPfa3ooJM5sC92`, placeholder then in-place upload, downloaded back byte-identical). From B2 (PDF 248–259), R2 (438–449),
B8 (362–393), R4 (496–529) and I1 (530–543).

- **METABOX has no TIP-ON and no SERVO-DRIVE.** A text search of B9 found neither, so **handle-less drawers mean LEGRABOX
  or MOVENTO**.
- **TIP-ON BLUMOTION** (2.5 gap): standard `…S` rails + set `T60L7040/7140/7340/7540/7570` by NL and pull-out weight; sync
  cut LW − 221 / − 247 (LEGRABOX), − 241 / − 267 (MOVENTO).
- **Plain TIP-ON** (3.5 gap): **different rails** `750.…T` / `760H…T`; sync `T57.7400.01` + `ZST.1160W`, cut LW − 229 / − 249.
- **SERVO-DRIVE:** bracket profile cut LH − 10, one drive unit `Z10A3000.03` per pull-out, bumpers, a 24 W supply and **a
  socket (electrician)**; LEGRABOX LW ≥ 267. The depth behind the drawers is to be read per job (cat. p. 362).
- **AMBIA-LINE:** inserts for LEGRABOX, chosen per job; no machining.
- `blum-library.md`, `Wiki/index.md` and the registers amended in place.

## (37) End of the day — handover

Owner: *"Tomorrow morning I am in office and will do a screenshots."* **Waiting on, for the morning of 2026-10-04:** the
Import Accessori list filtered to Blum AVENTOS (and, if convenient, TIP-ON), plus the *Accessory Register* and *Supporto
Anta (Aventos)* screenshots. When they arrive, Darius checks Kosmosoft's rows against
`blum-aventos-lift-systems-smartcabinet-input.md` §3–§5, including the Y-datum question.

**Still open from today:** `Raw/Side Left.pdf` can now be filed (the 350 unit is settled); the corner unit's single 1011
shelf is with the owner; FL-003 and the Hub rows AWT-0089, -0127, -0147, -0194 and -0225 were not touched this session.
`change-log-index.md`'s session-27 row was extended to cover the whole day.

## (38) The drawing check saved as a skill

Owner: *"Today, we done great job with creating one extra quality control step. This drawings check before we send them to
production. Save it as your new skill."* Two parts, so that the method has a governed copy and a runnable one:

- **`Wiki/Processes/pre-production-drawing-check.md`** (**9,380 B**, id `1W80CWjMxZzRRDWv9zhU0vEbfMvma_QUi`, placeholder then in-place upload, downloaded back
  byte-identical). **The checklist**, distilled from sections (4)–(30):
  - get every file (list, never date-filter; md5 per round);
  - decode; the three size sources must agree;
  - check sizes and materials;
  - check the joints (dowel sums, Cabineo, back, shelves supported);
  - check the Blum hardware (drawer formulas, NL vs depth, hinge cups ↔ plates, legs);
  - check the fronts (asked-for sizes, gaps vs neighbours);
  - check the machining (single vs nesting, unexplained cuts, tool numbers, K2 diameters with date);
  - check use and safety;
  - verdict ✓ / ✗ with the exact SmartCabinet fix / ? (**never guess intent**); record.
  
  Plus the SmartCabinet lessons of the day (`.SCS` on the row + restart, `cass_sot_dy`, the dummy divider, the legs
  max distance).
- **`.claude/skills/pre-production-drawing-check/`** in the git mirror: **`SKILL.md`** (when to use it, how to run it,
  boundaries) and **`tcn_decode.py`** (the decoder used today, made reusable: worklist, `.fnm`, `W#81`/`W#89`/`W#1001`
  per face, cutting-list lines, and `--diff` against the previous round by md5). **Tested on the corner unit's two rounds**:
  it reproduced (28)'s changed / unchanged / removed (`08-BACK-1B`) list. *First version read the `.fnm` as UTF-16. It is
  plain text, so it was fixed before saving.* **The skill is git-only**: Drive cannot run it, and the article is the
  governed copy it points to. It loads in future Claude Code sessions on this repository.
- `Wiki/index.md` and the registers amended in place; the Review-folder Processed item now points at the article.

## (39) Business process: order from Sales to handover — first discussion

Owner asked for thoughts on the process from **order received from Sales to finished furniture handed back to Sales**.
Darius proposed **gates** on the existing Job Tracker spine (`Software/smartcabinet-and-production-workflow.md`):

- **Gate 0**, release from Sales;
- **Gate 1**, the drawing check;
- **Gate 2**, final QC against the order spec;
- **Gate 3**, handover pack to Sales;

plus change control after release and a snag loop from site. **Nothing written to the workflow article yet: discussion
only.**

**Owner's direction, recorded:**
- **Sales give the workshop a 3D render and dimensions.** Step one is a **checklist that lets the workshop create
  production drawings** from them. Darius drafted it (layout, carcass, fronts, hardware, drawer materials, site
  constraints, appliances/scope; each item marked render / dimensions / house default / ask Sales).
- **Two directions for the workshop:**
  1. **Standardised kitchen production**: a library of standard unit sizes, where the client chooses only panel decor,
     edging and colours. This allows **a clear delivery term**.
  2. **Bespoke production**: the opposite end.

Darius's response and questions are in the session reply. **Awaiting the owner's answers before anything is written
into the workflow article.**
