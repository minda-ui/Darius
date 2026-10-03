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
