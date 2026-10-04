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

## (2) Decor end panels: sizes worked out, benchmarked, added to the Standard Kitchen Range draft

**Owner:** *"8 wall decor panels and 5 base decor panels. Wall units are 900mm high, base it's our standard."*
Then legs **150** and decor **U963**. Then: add **20–30 mm** for scribing? Check Howdens and DIY Kitchens. Then
*"yes, add them to the standard range"*.

**Sizes.** The front edge is flush with the door face: carcass + CLIP top front gap 1.5 + door 19, so 591 base and
321 wall. **Each panel is +25 deeper at the back for scribing, and base panels +10 taller for the floor.** That
gives:
- **wall 900 × 346** (950 × 346 with LED under the units);
- **base 880 × 616**.

The back edge is left unedged.

**Benchmarks:**
- **Howdens** (`Raw/` manual, pp. 129–130, 262, 267): decor ends fitted flush with the fronts and "scribe to
  the wall as required"; base decor end 890 = 720 + 170 legs.
- **DIY Kitchens** (end-panel page, read 2026-10-04): wall 772 / 952 × 325 (+52 drop), base 900 × 600; prices
  £34.85 / £42.59 / £67.88 (Altino Alabaster). Their carcass depths could not be confirmed, because the
  product pages load by script.

**Board.** A 2800 × 2070 board of plain U963 takes **12 of the 13** panels. The 13th needs an offcut or a
second board. **U963 has no price** in the Panel Price Library.

**`Outputs/standard-kitchen-range-v0-draft.md`** (in place, 5,999 → 7,520 B):
- a **decor end panel table** (`P-END-B`, `-W90`, `-W90L`, `-W72`, `-W72L`; tall [TBC]);
- **legs set to 150** (the owner, for this job; recorded as the standard);
- **wall depth corrected 320 → 300**, which is the library units' measured depth. v0's 320 was a proposal
  that never matched the library.

## (3) BLUMOTION for METABOX (Z70.0320): fitting from Blum's own sheet, filed and written up

**Owner** (photo of the unit): *"How to fit soft closer to Metabox"*.
- The catalogue (p. 409) gives the part but **no fitting drawing**.
- `www.blum.com` was blocked until the owner added **`*.blum.com`** to the environment. Adding the bare
  `blum.com` was not enough, because it redirects to `www.`, the same pattern as diy-kitchens.
- Blum's sheet **MA-379/0ML 06.10** came from `d2.blum.com` and is **filed in `Raw/Blum/`** (Drive
  `1xnyDYxfNOQ8hGc76r8_DDKGyBZ41ON9A`, 63,996 B, **md5 matches the local copy**).

**What the sheet gives:**
- unit on the left side under the runner: **37 / 261** from the front, **64 below the runner's front hole for M**;
- catch under the drawer bottom: **126 + 32**, **22.5** in.

**METABOX article §7b** written from it. *Not yet done:* drilling the unit's holes on the Vitap with the runner
holes.

**Owner's reply** to *"once it works, say save it"*: *"yes add"*. **Recorded as fitted and working, with the
wording quoted** so the inference is visible.

## (4) Interfit (interfitco.com): hardware prices, and the BU60 cost recomputed

**Owner:** *"i have added interfitco.com"*. **`www.interfitco.com` answers; the bare domain is blocked**, the
same pattern as before, but it doesn't matter here because the site lives on `www.`

**Interfit Furniture Components** is a UK distributor of Blum, Lamello, Häfele and Sensio. Its prices are public.
**Read 2026-10-04, GBP ex VAT** (the page's own ex-VAT figure; inc-VAT = ×1.2):

| Part | Interfit SKU | Price ex VAT | Unit |
|---|---|---|---|
| METABOX M, NL 400 (rail + side, pair) | 320M4000C | **£7.34** | pair |
| BLUMOTION for METABOX | Z70.0320 | **£3.27** | each |
| METABOX front fixing, screw-on, set | ZSF.1700 | **£1.18** | L+R |
| METABOX front fixing, knock-in | ZSF.1800L | **£0.67** | each |
| CLIP top 110° soft-close hinge, overlay | 71B3550 | **£2.42** | each |
| CLIP mounting plate, cam, 0 mm | 175H3100 | **£0.48** | each |
| **Lamello Cabineo X** | 186360 | **£98.02** | box of 500 → **£0.196** each |
| Cabineo X screws | 186380 | **£51.00** | box of 500 → **£0.102** each |
| Cabineo cover caps | 186350W | **£8.19** | pack of 100 → £0.082 each |
| Adjustable 150 mm plinth legs | LEG150S | **£1.12** | pack of 4 |
| Bigfoot 150 mm leg | IBF115 | £0.44 | each |
| Häfele AXILO 150 mm leg | 637.76.355 | £1.06 | each |

**Cabineo X per joint (housing + screw) = £0.30 at Interfit, against the KB's earlier retail ≈ £0.87**
(`carcase-fixings-cabineo-x-vs-confirmat.md`). Caps are extra where a joint is visible.

**BU60 materials recomputed** from (52). Board is still the W980 stand-in at £52.40, because W1100 ST9 has no price yet.

| Item | 38 Cabineo | 14 Cabineo |
|---|---|---|
| Board (15 % waste) | £23.15 | £23.15 |
| Edging | £1.74 | £1.74 |
| Cabineo X + screws | **£11.33** | **£4.17** |
| 2 hinges + 2 plates | £5.80 | £5.80 |
| 4 legs (LEG150S) | £1.12 | £1.12 |
| **Materials, ex VAT** | **£43.14** | **£35.98** |

**Against the £47 selling price** (the classifier's figure, "without doors"), materials alone leave **£3.86** with
38 Cabineo or **£11.02** with 14. **That is before labour, machine time and the real carcass-board price.**

*Prices are list prices on a public website on one day. They are not quotes, and no trade discount is
assumed. Nothing ordered; §6a.*

## (5) Hardware Price Library: a second price sheet, beside the panel one

**Owner:** *"yes, add the hardware sheet"*.
- **Smartsheet `Hardware Price Library`** (`1554175903270788`, workspace `Workshop`), new:
  - 15 columns, including **Pack £ / Pack qty** with a formula column **Unit £**, and **Price type**
    (*Web list price* / *Quote* / *Invoice*);
  - **12 rows** from (4), **read back after writing**: every part no., pack price, pack qty and date matches;
    Unit £ calculates (Cabineo X 0.196, legs 0.28).
- **`Wiki/Suppliers/interfit-furniture-components.md`** (new): the supplier, the sheet, the 12 rows as built,
  and what is unchecked:
  - the 175H3100 plate against the shop's hinges;
  - the legs against TD130;
  - list price against trade price.
- **`Wiki/index.md`**: a Suppliers entry.

**Owed (same as the Panel Price Library):** §1 of `CLAUDE.md` lists the Workshop sheets and names **neither**
price library. This is held for the next charter version.

## (6) Hardware Price Library: the hinge plate and the legs checked against ours

**Owner:** *"check the plate and legs against ours"*.

**Plate: wrong row, corrected.**
- The reviewed drawings (2026-10-03: the corner unit and BU60, `change-log-2026-10-03-metabox-side-left-check.md`) drill the plate pilots **Ø3 × 5 at 37 from the
  front, 32 apart**. That is the **37/32 cruciform** pattern for chipboard screws.
- **175H3100 is a horizontal 20/32 plate**, which does not fit that drilling.
- The row is now **173H7100** (steel, cam, MD 0, **£0.42**). MD 0 is what the hinge plan used (TB 6.5).
- Alternatives recorded in the row: 175H7100 £0.55, 173L6100 £0.16.
- **BU60 materials: £43.02 / £35.86** (was £43.14 / £35.98).

**Legs: not confirmable from here.**
- TD130 = **4 × Ø3 × 13 on a 64 × 64 square**.
- Interfit publishes **no top-plate hole pattern**. The drawings are on `cdn11.bigcommerce.com`, which this
  environment blocks.
- **Bigfoot and AXILO prices are leg only**; the top section is an extra option. **LEG150S** fixing is not described.
- All four leg rows now say so in Notes.
- **To settle it:** measure the screw holes on a leg the shop already uses, or allow the CDN host.

**Updated:**
- 4 rows of the sheet (`update_rows`, no failures);
- `Suppliers/interfit-furniture-components.md` in place.

