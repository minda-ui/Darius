---
title: "Blum library — catalogue split by product family, searchable"
category: Suppliers
status: active
sensitive: false
created: 2026-10-02
updated: 2026-10-02
sources:
 - "`Raw/Blum_publication.pdf` — *Blum catalogue and technical manual 2022/2023*, KA-150, Julius Blum GmbH, 758 pp., 548,904,350 B, Drive id `1tmR66kPxDRUPeevzLS8eqntF68BwcalQ`, uploaded by the owner 2026-10-02"
related:
 - ../Processes/blum-metabox-smartcabinet-input.md
 - ../Processes/blum-clip-top-hinges-smartcabinet-input.md
 - ../Processes/blum-runners-tandem-movento-smartcabinet-input.md
 - ../Software/smartcabinet-online-manual.md
 - ../Machinery/vitap-k2-panel-saw.md
---

# Blum library

**Owner, 2026-10-02: *"create library where you can access easy and be ready for me when I needed your help
on Blum."*** The full Blum catalogue is split into **37 product-family PDFs**, with a **page-by-page text
file** and a **part-number index**, all in **`Raw/Blum/`** on Drive (folder `1QumXqBo1OXocFEEBVZFMtKB6MfXAtKud`).

**The source is the 2022/2023 catalogue.** Blum revises part numbers and data between editions — anything
going into production or an order should be checked against Blum's current data.

## How to use it (for Darius, next time)

**Quick ids:** full text `1UBmfS7dzkLdiBZur_DDlprsw47cFmewS` (1,215,947 B) · part index
`1uL6ovp1pz-KtJrSJBXmVe0xoVTAocziQ` (59,890 B) · METABOX (B9) `1Z4y4m4fJlzXXHiv90tMRG0ogBEWItX1f` ·
the whole catalogue `1tmR66kPxDRUPeevzLS8eqntF68BwcalQ`.

1. **A part number?** Look it up in `Blum-2022-23_part-index.csv` — **1,627 parts**, each with its catalogue
   pages, PDF pages and family code. It is Blum's own *Part No. Index* (catalogue p. 728), parsed.
2. **A product or a dimension?** Search `Blum-2022-23_full-text.txt` (1.2 MB). Every page is headed
   `===== PDF n | CAT m =====`. **Catalogue page = PDF page − 4.**
3. **A drawing?** Most dimensions are in drawings, not text. Download only the **family PDF** (below), render
   the page, read it, and **mark any value taken from a drawing as such**.
4. **Getting files into the container:** `composio execute GOOGLEDRIVE_DOWNLOAD_FILE --account
   darius-googledrive -d '{"fileId":"<id>"}'` returns a temporary `s3url`; `curl` it to disk. The native
   connector cannot carry files this size. *Composio must be signed in (`composio login`, owner approves).*

## Families

| Code | Family | PDF pages | Cat. pages |
|---|---|---|---|
| 00 | Cover, contents, product overview | 1–17 | — |
| **Lift systems** | | | |
| L1 | AVENTOS HF — bi-fold lift (+ chapter overview) | 18–33 | 14–29 |
| L2 | AVENTOS HS — up and over | 34–39 | 30–35 |
| L3 | AVENTOS HL — lift up | 40–45 | 36–41 |
| L4 | AVENTOS HK top — stay lift | 46–55 | 42–51 |
| L5 | AVENTOS HK-S — stay lift | 56–61 | 52–57 |
| L6 | AVENTOS HK-XS — stay lift | 62–68 | 58–64 |
| L7 | AVENTOS mitred and rebated, accessories | 69–71 | 65–67 |
| **Hinge systems** | | | |
| H1 | CLIP top BLUMOTION and CLIP top hinges (+ chapter overview) | 72–147 | 68–143 |
| H2 | CLIP top mounting plates, angled spacers, accessories | 148–159 | 144–155 |
| H3 | BLUMOTION for doors | 160–173 | 156–169 |
| H4 | TIP-ON for doors | 174–177 | 170–173 |
| H5 | MODUL hinges | 178–191 | 174–187 |
| **Box systems** | | | |
| B1 | LEGRABOX (+ chapter overview) | 192–247 | 188–243 |
| B2 | TIP-ON BLUMOTION and TIP-ON for LEGRABOX | 248–259 | 244–255 |
| B3 | MERIVOBOX | 260–299 | 256–295 |
| B4 | TIP-ON BLUMOTION for MERIVOBOX | 300–305 | 296–301 |
| B5 | TANDEMBOX antaro | 306–351 | 302–347 |
| B6 | TANDEMBOX plus | 352–353 | 348–349 |
| B7 | TIP-ON BLUMOTION for TANDEMBOX | 354–361 | 350–357 |
| B8 | SERVO-DRIVE for LEGRABOX / MERIVOBOX / TANDEMBOX | 362–393 | 358–389 |
| **B9** | **METABOX** — *see `../Processes/blum-metabox-smartcabinet-input.md`* | 394–417 | 390–413 |
| **Runner systems** | | | |
| R1 | MOVENTO (+ chapter overview) | 418–437 | 414–433 |
| R2 | TIP-ON BLUMOTION and TIP-ON for MOVENTO | 438–449 | 434–445 |
| R3 | TANDEM | 450–495 | 446–491 |
| R4 | SERVO-DRIVE for MOVENTO and TANDEM | 496–529 | 492–525 |
| **Inner dividing** | | | |
| I1 | AMBIA-LINE for LEGRABOX and MERIVOBOX (+ chapter overview) | 530–543 | 526–539 |
| I2 | ORGA-LINE for TANDEMBOX | 544–561 | 540–557 |
| **Other** | | | |
| M1 | Motion technologies — SERVO-DRIVE single applications | 562–575 | 558–571 |
| F1 | Further products — SPACE STEP, CABLOXX, EXPANDO T, wall brackets, cabinet connectors | 576–593 | 572–589 |
| E1 | E-SERVICES (+ chapter overview) | 594–607 | 590–603 |
| E2 | Drilling and insertion machines | 608–647 | 604–643 |
| E3 | Assembly devices | 648–653 | 644–649 |
| E4 | Templates | 654–701 | 650–697 |
| X1 | General, safety and planning information (lift, hinge, box, runner) | 702–723 | 698–719 |
| X2 | Blum subsidiaries and contacts | 724–731 | 720–727 |
| X3 | Part No. Index | 732–758 | 728–754 |

File names follow `Blum-2022-23_<code>_<family>_pdf<from>-<to>.pdf`; the Drive ids are in
`Outputs/kb-registers.md` (Drive ids table, 2026-10-02).

**How the split was made.** By script, not by hand: each family's first page was **found from the page
header** (*"Box systems 〉 METABOX …"*), not read off the chapter overview pages — a first attempt that read
the overview's page numbers put six box/runner boundaries one item early, and was discarded. The 37 ranges
were asserted contiguous and to cover all 758 pages. *Chapter title and overview pages ride with the first
family of each chapter.*

## What the shop is likely to need first

| Need | Where |
|---|---|
| METABOX drawers into SmartCabinet | **B9**; worked up in `../Processes/blum-metabox-smartcabinet-input.md` |
| Hinges — CLIP top, cup drilling, mounting plates | **H1**, **H2**; the 110° hinge worked up in `../Processes/blum-clip-top-hinges-smartcabinet-input.md` |
| Soft close for doors | **H3** |
| Push-to-open | **H4** (doors), **R2** (MOVENTO), **B2/B4/B7** (boxes) |
| Runners under wooden drawers | **R1** MOVENTO, **R3** TANDEM; worked up in `../Processes/blum-runners-tandem-movento-smartcabinet-input.md` |
| Drilling patterns, overlay, gap and planning rules | **X1** |
| Blum drilling templates and jigs | **E4**, **E2** |

## Limits

- **No prices.** The catalogue carries none; costs come from invoices or a distributor list.
- **Drawings are not in the text file.** Most dimensions are drawn; the text gives part numbers, ranges,
  deductions and notes. Read the drawing, and say so when a figure came from one.
- **2022/2023 edition.** Check current data before ordering.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-10-02 | Created: 37 family PDFs, full text, part index, on the owner's instruction | Session 26 |
| 2026-10-02 | Hinge row points to the new CLIP top 110° article | Session 26 |
| 2026-10-02 | Runner row points to the new TANDEM/MOVENTO article | Session 26 |
