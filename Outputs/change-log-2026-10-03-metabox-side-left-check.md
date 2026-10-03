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
