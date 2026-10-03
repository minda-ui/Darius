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
