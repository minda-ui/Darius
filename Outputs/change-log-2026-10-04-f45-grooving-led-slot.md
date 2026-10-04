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

## (7) IronmongeryDirect: the second ironmongery supplier, and the shop's leg

**Owner:** the legs come from IronmongeryDirect, *"second our supplier for ironmongery"*, and
**`ironmongerydirect.co.uk` was added to the environment**. Then: *"We have purchased 705309 legs"*.

- **Access.** The bare domain is refused by the proxy. **`www.` passes the proxy but the site answers 403 from
  Cloudflare** (*"Attention Required!"*, `server: cloudflare`), which is bot protection. **Not worked around.**
  Product facts came through web search only.
- **`705309`** = *Square Adjustable Cabinet Feet – Plastic – 120–180 mm*, **pack of 4 legs + 2 plinth clips**, 600 kg,
  polypropylene, black. **Added to the Hardware Price Library** as the shop's leg, with the price blank.
- **Unit £ formula changed**: it now stays blank when Pack £ is blank. It had shown **0** for an unknown price.
  Read back: 13 rows, 705309 blank, the others unchanged.
- **Still open:**
  - the **price** (from the invoice);
  - the **top-plate hole pattern** against TD130 64 × 64 (measure a leg).
- `Suppliers/interfit-furniture-components.md` gained an IronmongeryDirect section.

## (8) Raw check: the leg drawing, and the 64 × 64 match confirmed

**Owner:** *"Check workshop Raw folder for new drawing"*. `Raw/` was listed in full (66 items, not filtered by date).
**One new file:** `Emailing 705309.PDF.pdf` (31,422 B, Drive `1XBqmB3xsGfdnvuuN_tC8CDfOE21AvF03`, 2026-10-04
15:59). It is a one-page maker's drawing, titled **TD180**, from a Chinese-language CAD file.

**What it shows:**
- Top plate **92 × 79.5 × 25** with **4 counterbored Ø5 holes on a 64 × 64 square**, plus 4 plain holes.
- Ø33.5 socket; tube Ø41 / 32.5 × 66.5; foot Ø79.5 × 25; thread 88; overall leg 113.

**So the shop's leg (705309) matches SmartCabinet's TD130 drilling (4 × Ø3 × 13 at 64 × 64). ✓** The Ø3 pilots
suit Ø4 screws through the Ø5 holes.
- The legs in the reviewed BU60 sit at X 13–77, so the 79.5 plate's edge is about 5 mm inside the carcass edge.
  That is a reading of the drawing, *not checked on a cabinet*.

**Also seen, not processed:** `Emailing BR_EGGER_Compact_Laminates_en.pdf` (8.2 MB, 2026-10-03 23:16). It is not
in the registers and has not been read. **`Raw/Review folder/`: no changes** since 2026-10-03; the three job
folders' newest files are from that morning.

**Updated:**
- the 705309 row's Notes in the Hardware Price Library;
- `Suppliers/interfit-furniture-components.md`;
- a Processed-items row for the drawing.

## (9) EGGER compact laminates brochure read and written up

**Owner:** *"yes, go through the Egger compact laminates"*. Source: `Raw/Emailing BR_EGGER_Compact_Laminates_en.pdf`
(8,205,540 B, 26 pp., Drive `1BNd-TNvlqJGOfZK9b0j3o_06qKmcMepQ`), uploaded 2026-10-03 23:16 and found
unregistered by today's Raw check.

**New: `Wiki/Processes/egger-compact-laminates.md`.** The points that matter here:

- **Board size 2,790 × 2,060**, not our 2,800 × 2,070.
- **Our decors exist as compact laminate**, including U963 and a coloured-core U9631.
- **Worktops:**
  - allow 2 mm/m for movement;
  - **closed carcass tops are not permitted**; our rails are fine;
  - crossbars on sink and hob units;
  - cut-out radius ≥ 5 mm, ≥ 300 mm from joints;
  - special 12 mm connectors.
- **Shelf and top spans by thickness** (10 / 12 / 13 mm → 310 / 390 / 440).
- **Doors:** cut lengthways; **thin-door hinges** (Blum EXPANDO T and others).
  - Darius's note: **71B3550's 13 mm cup is too deep** for a thin compact door.
- **Dust:** extraction required.

**Not in the brochure:** prices and cutting data. EGGER's separate processing instructions (linked in the
brochure) are **not fetched**. Index entry added; Processed-items row added.

## (10) Uniboards: a second panel supplier, 19 web prices in the Panel Price Library

**Owner:** *"I have added another supplier for panels. It is https://uniboards.co.uk/"*.

- **Access:** `uniboards.co.uk` returns 200; `www.` is refused by the proxy, but it isn't needed.
- **Source:** it is a Shopify shop, so its public product data (`/collections/<name>/products.json`) was read as
  JSON: EGGER 221, MFC 254, EGGER edging 243, Kronospan 29, Xylo-Cleaf 55, MDF 116, melamine MDF 12.
- **Price used:** each board has six prices (board only, three machining levels, two machine-hire levels). **The
  *Board only* price is used.**

**Added to the Panel Price Library: 19 rows, Supplier = Uniboards** (16 boards, 3 × 0.8 mm edging), each read back
with its £/m² calculated:
- **W1100 ST9 18 mm £75.99**, the first price this KB has for our carcass decor;
- **U963 ST9 18 mm £87.99**, the first for this week's decor panels;
- W980 ST7 £70.99, W1000 ST9 £74.99, U702 / U708 / U732 / U961 £75.99;
- U999 ST19 £102.99, H1180 £105.99, H1385 £107.99, F422 £96.99;
- PerfectSense: W1100 TM9 19 mm £139.99, U999 TM28 £144.99, W1100 PG and U708 PM MDF £196.99;
- edging £47.00 per 75 m.

**Two cautions, written into every row:**
- **The VAT basis is not stated** on the site, while Lathams' prices are ex VAT. **Not compared until confirmed.**
- **Delivery is extra** (boards £65 in England).

**Finding: W1100 ST9 is listed in 8 and 18 mm only.** Our drawings are 19 mm. **The owner is asked which board the
carcasses are actually made from.**

**Also:** two listings carry URL names for other products (W980 ST7 under `…st2…`; W1100 TM9 under `…u780…`).
The titles and descriptions were followed.

**New: `Suppliers/uniboards.md`.** `Suppliers/lathams-panel-price-library.md` gets a pointer, with `related` linked
both ways. Index entry added.

**BU60 at Uniboards' W1100 ST9 18 mm (£13.11/m²)** gives about **£29.20** of board, or **£33.58** with 15 % waste,
against £23.15 at the W980 stand-in. That's +£10.44 on the £43.02 total, so **about £53.46 with 38 Cabineo and
£46.30 with 14**. *If Uniboards' prices include VAT, the board part falls to £27.98.* **Not yet a firm figure:**
thickness and VAT are both open.

## (11) EGGER processing instructions and the Leitz / Leuco tool guides: fetched, filed, written up

**Owner** added `*.egger.com`, then `*.egger.link`, then `*.egger-cdn.com`. **All three were needed.** The download
chain is `www.egger.com/get_download/…` → `binary.egger.link/dld/…` → `downloads.egger-cdn.com`. The bare
`egger.com` and `www.egger.link` stay refused, which is harmless.

**Fetched and filed in a new `Raw/EGGER/`** (folder `167yUHu3BCw1p_FxnfTVtZUv7gWWZheSn`). **Drive md5 = local md5 for
all four:**

| File | Pages | Bytes | Drive id |
|---|---|---|---|
| `EGGER_Processing_instructions_Compact_Laminates.pdf` (rev. 04, 24 Jun 2026) | 24 | 1,391,802 | `1viLKuzTpheuWmzrK71IKhfH8dlLCNAVr` |
| `EGGER_Processing_instructions_Compact_Laminates_cooperation_Leitz.pdf` (01/2026) | 21 | 3,611,837 | `1qnex6Atz-se2i_jIPUwWHOeY8bICGaaQ` |
| `EGGER_Processing_Instructions_Compact_Laminates_Leuco_en.pdf` | 9 | 2,128,538 | `1A7O24ksQHTclCfBJyYWbB4dExDLP3-Ly` |
| `EGGER_Processing_instructions_Worktops.pdf` | 27 | 2,308,093 | `1VWdWdWfp4aM4R1k8jd8Mo4Xcxa3i_0e0` |

The Leitz tables are images, **read by OCR (tesseract)**, so they are flagged in the article for checking against
the PDF.

**`Processes/egger-compact-laminates.md` §6 rewritten** (6,341 → 12,090 B):
- **sawing:** DP blades, 60–90 m/s; **Ø350 at 4,000 rpm = 73 m/s** on the F45; the guides disagree on blade
  projection (Leitz 5–10, Leuco 15–33 by diameter), so **test**; Leitz DP table-saw blades Ø303 × 3.2 Z60/96 and
  Ø350 × 3.5 Z72;
- **drilling:** Leuco 4,000–4,500 rpm, 1.5–2 m/min, peck above 12 mm, "Light" cylinder bits for hinge cups;
  residual ≥ 1.5 mm (blind) and ≥ 3 mm (edge);
- **screws:** pre-drill, RAMPA sleeves, flat-head, fixed and sliding points, spacing table;
- cut-out radius ≥ 5, production direction, adhesives, storage at 80° or flat, dust.

**Flagged:**
- **Cabineo X in compact laminate is not covered by EGGER.**
- **The F45's fitted blade (diameter, Z, HW or DP) isn't recorded.**
- Altendorf is not in Leitz's machine list: **check bore and pin holes** before buying a blade.

## (12) Scott+Sargeant recorded as the tooling supplier

**Owner:** *"https://www.scosarg.com/ is a place where I am buying tooling for workshop machinery."*

- **`www.scosarg.com` returns 403 from Cloudflare** (*"Just a moment…"*). Like IronmongeryDirect, it is **not worked
  around**; the bare domain is refused by the proxy. **Web search only.**
- **Found:** **CMT 237 Xtreme PCD, Ø350 × 30, Z72, kerf 3.2**. It is diamond, which is what EGGER and Leitz advise for
  compact laminate, and its **kerf equals the 3.2 measured on the F45** today. Whether it is the fitted blade is not known.
- **New: `Suppliers/scott-sargeant.md`.** `egger-compact-laminates.md` §8 points to the blade, with `related` linked
  both ways. Index entry added.

## (13) Confirmat as Plan B: the holes and the bits researched

**Owner:** *"It's worth to research comformat screw option, but it needed right bits too."* Cabineo X stays the
decision (2026-09-19, re-confirmed 2026-09-28). This makes the in-stock confirmat fallback usable.

**Before editing, the git copy of `Processes/carcase-fixings-cabineo-x-vs-confirmat.md` was found BEHIND Drive.**
- Git had 23,245 B, last touched in the 2026-09-27 sync (`a020f5f`).
- Drive (`1d260Ed3tcBVcWh4igSeVkB5uFULbXtjB`) had 32,327 B, modified 2026-09-28: the Cabineo trade-price and divider
  sections.
- **The Drive copy was taken as the base** (Drive is the source of truth), so this commit also brings git up to
  that version. *This is the AWT-0225 lag again, in a file the v36 catch-up didn't cover. Other articles last
  touched 2026-09-28 may be behind too, not checked.*

**Researched (web search; Scott+Sargeant's site is Cloudflare-blocked):**
- **7 × 50 confirmat:** Ø7–7.6 clearance and Ø10–11 countersink in the face panel; **Ø5 core ≥ 33 mm** into the
  mating edge (50 − 19 + 2); edge distance ≥ 8 mm.
- **Bench route:** one stepped bit. **CMT 515.050.31, Ø5 / 7.6 / 10.6, L 93.7, shank 9**, £9.60 inc VAT
  (£8.00 ex) at Scott+Sargeant. **Added to the Hardware Price Library** as a web list price.
- **Vitap route:**
  - **Ø5 horizontal bushes 43, 44, 52, 53 exist** (layout), but their useful length is unread;
  - **no Ø7 and no countersink on the head**, so it needs a Ø7 through drill (or Ø8 with play) and a separate
    countersink.
- **Not for compact laminate:** 2.5 mm per side in a 12 mm edge, against EGGER's ≥ 3 mm, and a coarse thread.

**Article:** a new section, *"2026-10-04 — confirmat as Plan B"*. The open question about the horizontal spindles is
partly answered. `related` is linked both ways with `egger-compact-laminates.md`, whose §6 notes confirmat.

**To close Plan B:**
1. which confirmat size is in stock;
2. buy one bit and trial a joint;
3. read bushes 43 / 44 / 52 / 53.

## (14) Confirmat stock: about 3,000 screws

**Owner:** *"We got around 3000 comformat screws in the shop."*
- Recorded in the fixings article's Plan B list.
- **What it covers:** about **375 units** at the 8 carcase fixings per unit counted in the article, or about **78
  units** at BU60's 38 joint positions.
- **Size still unknown.** It decides the stepped bit.

## (15) The confirmat screws are IronmongeryDirect 659270

**Owner:** *"They are from ironmongery direct under 659270."*
- **Size not found:** web search doesn't index the code, and the site returns 403 (Cloudflare) to WebFetch as well
  as curl.
- **Added to the Hardware Price Library** as the shop's stock, with size, pack and price blank and a note to read
  them from the box or invoice.
- Code recorded in the fixings article's Plan B list and in the supplier article's IronmongeryDirect section.

