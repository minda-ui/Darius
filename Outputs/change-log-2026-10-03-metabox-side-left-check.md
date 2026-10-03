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
