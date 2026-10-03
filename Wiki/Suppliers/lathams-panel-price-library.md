---
title: "James Latham Gateshead — panel and edging price library"
category: Suppliers
status: active
sensitive: false
created: 2026-10-03
updated: 2026-10-03
sources:
 - "Every quotation and sales order from Steven Elliott (`steven.elliott@lathams.co.uk`) in info@fishboneconstruction.co.uk, 06/01/2025 – 15/06/2026: 15 quotes and 13 sales orders (28 PDFs, 75 lines), read 2026-10-03 under §6b of `CLAUDE-Rules.md`. The documents themselves are not filed in git."
 - "Smartsheet **Panel Price Library** (`7248546623522692`, workspace `Workshop`) — the live copy"
related: []
---

# James Latham Gateshead — panel and edging price library

**Owner, 2026-10-03: *"Create a library for panels with price."*** Every board and edging price Lathams has sent
to info@ is in one place, with the latest price per material and its history.

**The live copy is the Smartsheet sheet `Panel Price Library`** (`7248546623522692`, workspace `Workshop`,
<https://app.smartsheet.eu/sheets/fCG2PF48wHmwrhcr3PhX8VF58JMGmhHwH672PqF1>). **Add new prices there.** This
article is the snapshot as built, and says how it was built and what to watch.

## The supplier

**James Latham Gateshead** (Lathams Limited), Nest Rd, Felling Ind Estate, Gateshead, tel 0191 4694211. Contact
**Steven Elliott**. Our account **`FISHB000`**, invoiced to **Fishbone Construction Ltd** and delivered to Unit
30-32 Point Pleasant Industrial Estate, Wallsend. *Same group-company pattern as the machinery (§0 of `CLAUDE.md`).*

## How it was built

- **Mail:** search `from:steven.elliott@lathams.co.uk` through `darius-gmail-info-v2` — **50 messages**,
  01/2025 – 06/2026. **Opened:** the 45 quotes, sales orders and replies. **Not opened:** 4 auto-replies and
  **1 cash-sale invoice** (invoices are left unopened). Nothing sent, replied to, labelled or changed.
- **Parsed:** 28 PDFs (15 quotes, 13 sales orders) by script, **75 priced lines; every document's lines add up
  to its own "Goods" total to the penny**, so no line was missed or misread.
- **Grouped** into **37 materials** (19 boards, 1 laminate, 17 edgings). Quote and sales order for the same job
  count as one price event each, so the history shows both.
- **Rate:** boards £ per m² of one board; edging £ per metre of a 75 m roll. **All prices ex VAT, per board or
  per roll, as Lathams quoted them** — no discounts, delivery or waste added.

## Boards and laminate

| Material | Latest £ ex VAT | Rate | Date | Source | Ordered |
|---|---|---|---|---|---|
| 16 mm MFC U732 ST9 Dust Grey | **£55.95** | £9.65/m² | 2025-02-12 | SO 540255 | yes |
| 18 mm MFC F422 ST10 White Linen | **£85.65** | £14.78/m² | 2026-06-15 | Quote 412541 |  |
| 18 mm MFC H1180 ST37 Natural Halifax Oak | **£95.50** | £16.48/m² | 2026-02-04 | Quote 343425 |  |
| 18 mm MFC H1385 ST40 Natural Casella Oak | **£110.00** (was £84.25, 2025-12-16) | £18.98/m² | 2026-06-15 | Quote 412541 | yes |
| 18 mm MFC H3043 ST12 Dark Brown Eucalyptus | **£78.80** | £13.60/m² | 2026-02-04 | Quote 343425 |  |
| 18 mm MFC U702 ST9 Cashmere Grey | **£62.30** | £10.75/m² | 2025-05-22 | SO 1005830 | yes |
| 18 mm MFC U999 ST19 Black | **£75.75** | £13.07/m² | 2025-07-25 | SO 1304425 | yes |
| 18 mm MFC W980 ST2 Platinum White | **£48.50** | £8.37/m² | 2025-10-02 | SO 1623705 | yes |
| 18 mm MFC W980 ST7 Platinum White | **£52.40** (was £48.50, 2025-11-03) | £9.04/m² | 2026-06-15 | Quote 412541 | yes |
| 18 mm Decor MDF W1000 ST9 Premium White | **£101.60** | £17.53/m² | 2026-05-01 | SO 2619630 | yes |
| 18 mm Decor MDF W980 ST7 Platinum White | **£99.80** | £17.22/m² | 2026-04-30 | Quote 389348 |  |
| 18 mm MF MDF 020 White Textured | **£44.50** | £14.95/m² | 2025-01-06 | SO 354785 | yes |
| 18 mm MF MDF 8685 Snow White (textured) | **£47.40** | £15.92/m² | 2026-04-30 | Quote 389763 |  |
| 15 mm Raw MDF Raw | **£20.55** | £6.90/m² | 2025-10-16 | SO 1692245 | yes |
| 19 mm PerfectSense Texture MFC U999 TM28 Black | **£165.20** (was £148.60, 2026-02-04) | £28.50/m² | 2026-05-01 | SO 2619630 | yes |
| 19 mm PerfectSense Gloss MDF U702 PG Cashmere Grey | **£150.00** | £25.88/m² | 2025-12-16 | SO 1993765 | yes |
| 19 mm PerfectSense Gloss MDF U708 PG Light Grey | **£150.00** | £25.88/m² | 2025-12-16 | SO 1993765 | yes |
| 19 mm PerfectSense Gloss MDF W1100 PG Alpine White | **£175.10** | £30.21/m² | 2026-05-01 | SO 2619630 | yes |
| 19 mm PerfectSense Matt MDF U708 PM Light Grey | **£190.04** | £32.79/m² | 2026-06-15 | Quote 412541 |  |
| 0.8 mm Laminate (HPL) H1385 ST40 Natural Casella Oak | **£136.50** | £23.75/m² | 2026-01-27 | Quote 338618 |  |

## Edging (75 m rolls)

| Material | Latest £ ex VAT | Rate | Date | Source | Ordered |
|---|---|---|---|---|---|
| Edging ABS 23x0.8 F422 White Linen ST10 | **£35.20** | £0.47/m | 2026-06-15 | Quote 412541 |  |
| Edging ABS 23x0.8 H1180 Natural Halifax Oak | **£30.00** | £0.40/m | 2026-02-04 | Quote 343425 |  |
| Edging ABS 23x0.8 H1385 Natural Casella Oak ST40 | **£40.00** (was £30.00, 2025-12-16) | £0.53/m | 2026-01-13 | SO 2072370 | yes |
| Edging ABS 23x0.8 H3043 Dark Brown Eucalyptus ST12 | **£30.00** | £0.40/m | 2026-02-04 | Quote 343425 |  |
| Edging ABS 23x0.8 U732 Dust Grey ST9 | **£30.00** | £0.40/m | 2025-02-12 | SO 540255 | yes |
| Edging ABS 23x0.8 W1000 Premium White ST9 | **£32.00** | £0.43/m | 2026-05-01 | SO 2619630 | yes |
| Edging ABS 23x0.8 W980 Platinum White ST7 | **£35.20** | £0.47/m | 2026-06-15 | Quote 412541 |  |
| Edging ABS 23x1 U702 Cashmere Grey (PerfectSense Gloss) | **£40.00** | £0.53/m | 2025-12-16 | SO 1993765 | yes |
| Edging ABS 23x1 U708 Light Grey (PerfectSense Gloss) | **£40.00** | £0.53/m | 2025-12-16 | SO 1993765 | yes |
| Edging ABS 23x1 U708 Light Grey (PerfectSense Matt) | **£46.20** | £0.62/m | 2026-06-15 | Quote 412541 |  |
| Edging ABS 23x1 U999 Black (PerfectSense Feelwood) | **£40.00** (was £80.00, 2026-04-29) | £0.53/m | 2026-04-30 | Quote 389763 |  |
| Edging ABS 23x1 W1100 Alpine White (PerfectSense Gloss) | **£42.00** | £0.56/m | 2026-05-01 | SO 2619630 | yes |
| Edging ABS 43x2 H1385 Natural Casella Oak ST40 | **£195.00** | £2.60/m | 2026-06-15 | Quote 412541 |  |
| Edging ABS 23x2 U702 Cashmere Grey ST9 | **£45.00** | £0.60/m | 2025-05-22 | SO 1005830 | yes |
| Edging ABS 43x2 U702 Cashmere Grey ST9 | **£185.20** | £2.47/m | 2025-05-22 | SO 1005830 | yes |
| Edging ABS 23x2 U999 Black ST19 | **£45.00** | £0.60/m | 2025-07-25 | SO 1304425 | yes |
| Edging ABS 43x2 U999 Black ST19 | **£188.50** | £2.51/m | 2025-07-25 | SO 1304425 | yes |

## What to watch

- **No price for the board our carcasses are drawn in.** BU60 and the library units are drawn in **19 mm W1100
  ST9 MFC**; Lathams have never quoted it. The **W1100** they did quote is **19 mm PerfectSense Gloss MDF** at
  **£175.10** — a front board, not a carcass board. The cheapest white carcass board quoted is **18 mm W980 ST7
  MFC at £52.40** (15/06/2026, quote expired 16/07/2026). **Ask Lathams for 19 mm W1100 ST9** before costing.
- **Prices are rising.** H1385 MFC **+30.6 %** (£84.25 → £110.00, Dec 2025 → Jun 2026); W980 MFC **+8.0 %**;
  U999 PerfectSense Texture **+11.2 %**; H1385 23 × 0.8 edging **+33.3 %**. Lathams' June note warns prices may
  move with energy costs. **Treat anything older than a quote's validity as indicative, not a price.**
- **Quotes expire in about a month.** The latest price shown may be out of date even when it is the newest one held.
- **W980 ST2 vs ST7.** Quote 287611 / SO 1623705 say ST2; every later W980 line says ST7. Kept as two rows
  until confirmed; probably the same board.
- **U999 Feelwood edging** was £80.00 on quote 388938 and £40.00 on 389763 the next day — the second is taken as
  the price.

## Keeping it current

**When a new Lathams quote arrives**, read it (§6b), then in the sheet: update **Latest £ / date / source**, append
to **Price history**, tick **Ordered** if a sales order follows. **Add a row for a new material.** Leave **First £**
as it is, so **Change %** keeps showing the movement. **Other suppliers** (a new sender domain) need the owner's OK
first (§6b).

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-10-03 | Created at the owner's request; Smartsheet sheet built and populated, 37 rows | Session 27 (54) |
