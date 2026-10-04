# Change log — 2026-10-04 — F45 Grooves function, first use (LED-strip slot)

Session 28. Darius (Workshop Operations Assistant), with the owner at the F45.

## (1) A 16 × 9 mm LED-strip slot cut on the F45 with the Grooves function, and saved as a Process article

**Owner:** *"we need to cut slot in shelf for LED trim. I want to use F45. I know there is a setting for step
cutting strip. Strip is 16mm wide 9mm deep"*, then *"All good! Save it for future"*.

**Found in the manuals** (the `Raw/` PDFs, downloaded from Drive and read in the scratchpad, not re-filed):
- **ElmoDrive manual** §1.8.1, pp. 40–41: *Main Menu → Application Technology → Grooves*. The screenshot's
  fields have no labels. **Their meaning was worked out from the manual's own example** (it finishes at 366.8 =
  310 + 5 + 50 + 5 − 3.2). The gap-between-grooves field still needs a dry run before any job with two or more grooves.
- **Main manual**:
  - groove milling tools on **two-way-tilt** machines are limited to **5 mm wide**, so a 16 mm slot must be
    cut with the main blade in several passes;
  - *Concealed cutting, grooving* (p. 103): **leave the riving knife fitted as the rear guard**, push with the
    sliding table, use the crosscut fence for narrow pieces cut across.

**What was done**, from the owner's photo of the screen and messages:
- **Settings:** blade height **9.0**, blade **3.2**, gap 0.0, width **16.0**, start **10.0**, 1 groove,
  giving **6 cuts**. 4000 RPM, scorer off.
- **First cut measured 3.2 mm**, so the blade field (which matched the manual's example value) was right.
- Cuts 2–6 run with **Start → wait for the fence → cut**, same edge to the fence every time.
- **Result: *"All good!"*** The strip fitted; no measured figures were sent, so none are recorded.

**Recorded:**
- **`Wiki/Processes/f45-grooving-slots-with-the-main-blade.md`** (new): fields, method, safety rules and the
  settings that worked.
- **`Wiki/Machinery/altendorf-f45-panel-saw.md`**: a pointer above *Safety*, `related` both ways, and a Changes row.
- **`Wiki/index.md`**: a Processes entry.

**Darius's advice, not the manual's, and labelled as such in the article:** scorer off, a test cut on an
offcut, keep slots clear of shelf-pin and Cabineo positions.
