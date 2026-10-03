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
