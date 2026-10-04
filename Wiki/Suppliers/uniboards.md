---
title: "Uniboards — panel supplier (EGGER, Kronospan, Xylo-Cleaf boards and edging), web prices"
category: Suppliers
status: active
sensitive: false
created: 2026-10-04
updated: 2026-10-04
sources:
 - "uniboards.co.uk, read 2026-10-04 via the shop's public product data (`/collections/<name>/products.json`) and product pages"
 - "Smartsheet **Panel Price Library** (`7248546623522692`) — 19 rows with Supplier = Uniboards"
related:
 - lathams-panel-price-library.md
---

# Uniboards — panel supplier

**Owner, 2026-10-04: *"I have added another supplier for panels. It is https://uniboards.co.uk/"*.**

**Uniboards** (`uniboards.co.uk`, sales@uniboards.co.uk, 0126 843 7493, VAT no. 157363006) sells:
- **EGGER, Kronospan and Xylo-Cleaf MFC**, EGGER PerfectSense MDF, Alvic, Valchromat, plywood and fluted panels;
- **EGGER and Alvic edging**;
- cutting, edging and drilling services, and machine hire (beam saw, CNC, edgebander, spray booth).

**Access:** the environment allows `uniboards.co.uk`, but **not `www.uniboards.co.uk`**. That doesn't matter, because
the site runs without `www.` It is a Shopify shop, so **its product data is read as structured JSON**, not
scraped from pages: 221 EGGER, 254 MFC and 243 edging products listed.

## Prices — read this first

- **Each board has six prices:** *Board only*, three *Machining service* levels (cut / cut & edge / cut, edge &
  drill) and two *Machines hire* levels. **The library holds the *Board only* price.**
- **The site does not say whether prices include VAT.** Lathams' prices are **ex VAT**. **Don't compare the two
  until this is confirmed.** If Uniboards are inc VAT, divide by 1.2.
- **Delivery is extra:** boards **£65** (England), 10′ boards £95–125, Scotland & Wales more.

## What it gives us (2026-10-04, *Board only*)

| Board / edging | Uniboards | Lathams (ex VAT) |
|---|---|---|
| **18 mm MFC W1100 ST9 Alpine White** | **£75.99** | *never quoted* |
| 19 mm PerfectSense Matt MFC **W1100 TM9** | £139.99 | — |
| 18 mm MFC W980 ST7 | £70.99 | £52.40 (Jun 2026) |
| 18 mm MFC W1000 ST9 | £74.99 | — (18 mm W1000 MDF £101.60) |
| **18 mm MFC U963 ST9 Diamond Grey** | **£87.99** | *never quoted* |
| 18 mm MFC U702 / U708 / U732 ST9 | £75.99 each | U702 £62.30 (May 2025) |
| 18 mm MFC U961 ST7 | £75.99 | — |
| 18 mm MFC U999 ST19 | £102.99 | £75.75 (Jul 2025) |
| 18.5 mm MFC H1180 ST37 / H1385 ST40 | £105.99 / £107.99 | £95.50 / £110.00 |
| 18 mm MFC F422 ST10 | £96.99 | £85.65 |
| 19 mm PerfectSense Texture U999 TM28 | £144.99 | £165.20 |
| 19 mm PerfectSense Gloss MDF W1100 PG | £196.99 | £175.10 |
| 19 mm PerfectSense Matt MDF U708 PM | £196.99 | £190.04 |
| Edging 23 × 0.8, 75 m (U963 / W1100 / W980) | £47.00 | W980 £35.20 |

**The sheet's £/m² for each row is worked out by Smartsheet.** All boards are 2,800 × 2,070.

## Two findings

1. **W1100 ST9, our carcass decor, has a price for the first time, but only in 18 mm.** Uniboards lists W1100 ST9
   in **8 and 18 mm only**. The only 19 mm W1100 is **PerfectSense Matt TM9** at £139.99. **Our drawings
   (BU60 and the library units) are 19 mm.** *Is the shop's carcass board really 19 mm W1100 ST9, and from whom?*
   If it is 18 mm, SmartCabinet's thickness needs changing. If it is 19 mm, the source is still unknown.
2. **Two listings have URL names that don't match the product** (W980 ST7 under `…w980-st2…`; W1100 TM9 under
   `…u780-tm9…`). **The title and description were taken as the product.** Check before ordering.

## Keeping it current

Re-read a product's JSON (`/products/<handle>.js`) for a fresh price. Then update the row's **Latest £ / date**
and append to **Price history**. **Confirm the VAT basis once** and record it here.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-10-04 | Created; 19 rows added to the Panel Price Library | `change-log-2026-10-04-f45-grooving-led-slot.md` (10) |
