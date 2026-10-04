---
title: "Interfit Furniture Components — hardware supplier, and the Hardware Price Library"
category: Suppliers
status: active
sensitive: false
created: 2026-10-04
updated: 2026-10-04
sources:
 - "www.interfitco.com product pages, read 2026-10-04 (public prices, ex and inc VAT on each page)"
 - "Smartsheet **Hardware Price Library** (`1554175903270788`, workspace `Workshop`) — the live copy"
related: []
---

# Interfit Furniture Components — hardware supplier, and the Hardware Price Library

**Owner, 2026-10-04: *"i have added interfitco.com"*, then *"yes, add the hardware sheet"*.**

**Interfit** (`www.interfitco.com`) is a UK distributor of furniture fittings. It carries **Blum** (METABOX,
LEGRABOX, CLIP top, AVENTOS, MOVENTO, TANDEM, SERVO-DRIVE), **Lamello** (Cabineo X, Tenso), **Häfele** (legs) and
**Sensio** (LED strips and profiles), plus Festool tools. **Prices are public, shown ex and inc VAT.** It offers
trade accounts (*New trade customers*); **we have no account recorded**, so list prices are what we have.

**Access:** the environment allows `www.interfitco.com`. The bare `interfitco.com` is blocked, which doesn't
matter because the site runs on `www.`

## The Hardware Price Library

**Live copy: Smartsheet `Hardware Price Library`** (`1554175903270788`, workspace `Workshop`,
<https://app.smartsheet.eu/sheets/jQ2RpqGG3WVRWhhHMvXJMc5gJw5MqQCW7wVpjC21>). It sits beside the **Panel Price
Library** (boards and edging, `lathams-panel-price-library.md`).

One row per part:
- part, category, brand, **Blum / Lamello / Häfele part number**, supplier, supplier SKU;
- **Pack £** (ex VAT) and **Pack qty**; **Unit £** is calculated (Pack £ / Pack qty);
- price date, **price type** (*Web list price* / *Quote* / *Invoice*), source URL, where it is used, notes.

**As built, 2026-10-04 (12 rows, all Interfit web list prices, ex VAT):**

| Part | Part no. | Pack | Unit £ |
|---|---|---|---|
| METABOX M 86, NL 400 (pair) | 320M4000C | £7.34 / pair | 7.34 |
| BLUMOTION for METABOX | Z70.0320 | £3.27 | 3.27 |
| METABOX front fixing, screw-on, set | ZSF.1700 | £1.18 / set | 1.18 |
| METABOX front fixing, knock-in | ZSF.1800 | £0.67 each | 0.67 |
| CLIP top 110° soft-close hinge, overlay | 71B3550 | £2.42 | 2.42 |
| CLIP **cruciform 37/32** plate, cam, 0 mm | **173H7100** | £0.42 | 0.42 |
| Lamello Cabineo X | 186360 | £98.02 / 500 | 0.196 |
| Cabineo X screws | 186380 | £51.00 / 500 | 0.102 |
| Cabineo cover caps | 186350W | £8.19 / 100 | 0.082 |
| Adjustable plinth leg 150, set of 4 | LEG150S | £1.12 / 4 | 0.28 |
| Bigfoot plinth leg 150 | IBF115 | £0.44 | 0.44 |
| Häfele AXILO leg 150 (250 kg) | 637.76.355 | £1.06 | 1.06 |

**What changed because of it:** **Cabineo X costs £0.30 per joint** (housing + screw), against the **≈ £0.87** the KB
used before (`../Processes/carcase-fixings-cabineo-x-vs-confirmat.md`). BU60 materials recomputed: **£43.02**
with 38 Cabineo, **£35.86** with 14 (with the corrected plate). The board is still a stand-in (change log 2026-10-04 (4)).

## Not yet checked

- ~~**The 175H3100 plate**~~ — **checked 2026-10-04 and corrected.** Our reviewed drawings drill the plate
  pilots **Ø3 at 37 from the front, 32 apart**, so the plate is a **37/32 cruciform for chipboard screws**.
  175H3100 is a **horizontal 20/32** plate, the wrong pattern. The row is now **173H7100** (steel, cam ±2,
  **£0.42**); MD 0 matches the hinge setting the reviews used (TB 6.5).
  - Alternatives on Interfit: **175H7100** (zinc, screw adjustment) £0.55; **173L6100** (elongated hole ±3) £0.16.
  - *What is in the shop's stock is still not seen.*
- **The legs: not confirmable from Interfit.** Our **TD130** drilling is **4 × Ø3 × 13 on a 64 × 64 square**
  under the bottom. **No Interfit page gives the top-plate hole pattern**, and the product drawings sit on
  `cdn11.bigcommerce.com`, which this environment blocks. Also:
  - the **Bigfoot** and **AXILO** prices are **for the leg only**; the screw-fixing top section is an extra option;
  - **LEG150S** comes with "base shoes", fixing not described.
  - **Check by measuring a leg the shop already uses**, or allow `cdn11.bigcommerce.com` so I can read the
    drawings.
- **List price ≠ our price.** A trade account, a quote or an invoice replaces a row's price and its *Price type*.

## Keeping it current

**New price →** update **Pack £ / Pack qty / Price date / Price type / Source** on the row; the old price goes in
**Notes**. **New part →** add a row with its maker's part number. **Nothing is ordered from here** (§6a).

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-10-04 | Created with the Hardware Price Library sheet (12 rows) | `change-log-2026-10-04-f45-grooving-led-slot.md` (5) |
| 2026-10-04 | Plate checked against the shop's drilling: 175H3100 → **173H7100**; legs not confirmable from Interfit, flagged | `change-log-2026-10-04-f45-grooving-led-slot.md` (6) |
