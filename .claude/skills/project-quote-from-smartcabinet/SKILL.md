---
name: project-quote-from-smartcabinet
description: Cost and price a furniture project from the owner's SmartCabinet scene export, ready for a quote. Use when the owner says "I got a project to quote", "how do I calculate the project / issue a quote", "price this job", "create options", or uploads SmartCabinet's panel and pieces CSVs (e.g. library_Panel.csv, library_Pieces.csv) or a panel optimisation layout. Builds a cost sheet in Outputs with one column per option, then a printable PDF (customer summary + internal build-up).
---

# Project quote from a SmartCabinet export

Worked out on the "library" project, 2026-10-23 (cost sheet v0.1 → v0.12 in one day, because the rates and rules
arrived one at a time). The worked example is `Outputs/2026-10-23-library-project-cost-sheet-v0.1.md` (Drive
`1EnELNZM6CQm2dP7fu3Ra7bZ-onf4XIgb`) — **copy its layout**, not its prices.

## 1. Read the export
- `*_Panel.csv` = sheets needed (decor, size, qty). `*_Pieces.csv` = every part with size and material. Read them as
  data (`python3 -I`), from their own folder.
- From them: units and parts per unit, m² of parts, sheet count, **yield** (parts m² ÷ sheets m²), edged metres
  (assume fronts of carcase parts and all round doors unless the owner says otherwise — state the assumption).
- Count hardware from the parts: doors × 2 hinges (check Blum's chart for tall doors), shelves × 4 pins, connectors per
  joint. Anything the export doesn't show (handles, legs, plinth, wall fixing) → **ask**, don't invent.

## 2. Price the materials — ex VAT, every price with its source and date
- Boards and edging: **Panel Price Library** (Smartsheet `7248546623522692`). Hardware: **Hardware Price Library**
  (`1554175903270788`).
- A price that is **not for that exact product** (another texture, a similar decor) is a **proxy**: use it, mark it ⚠,
  say what it stands in for. A price older than ~6 months: show its date.
- An owner-stated price ("legs £4 a pack", "rail £100") is used as given and noted *owner-stated, date*. A new
  supplier document the owner uploads → add or update its library row (never copy bank or payment details from it).
- Add any extra sheets not in the optimisation (plinth strips etc.).

## 3. Workshop time
Estimate per stage and show the basis, so the owner can correct it: panel saw (F45) per sheet, edging (Hebrock) per
edged part, drilling (Vitap) per program incl. loading, assembly per unit type, doors hang/adjust, check and pack.
A harder material (lacquered MDF, PerfectSense) → suggest +10 % and say so.

## 4. Price build-up — the owner's rules (23/10/2026; ask if any has changed)
1. **Materials** at cost.
2. **Margin 15 % on materials**, added on cost (a mark-up). Labour and machine time carry none.
3. **Labour £45/h** on every workshop hour.
4. **Machine time £65/h on top**, for the hours a machine runs (saw + edging + drilling).
5. **VAT 20 %** on the total.
6. **Delivery and fitting are not included** unless the owner says so — and the quote says so.

The *cost* of a machine hour (to test the £65) is in the worked example's §3a: depreciation + maintenance over yearly
hours, plus power and the compressor/extractor share — ≈ £15–£34 depending on hours run.

## 5. Options
One column per option (e.g. 18 mm MFC vs 19 mm PerfectSense). Flag when an option differs from how the scene was drawn
(units drawn in 19 mm, option in 18 mm → **re-optimise in SmartCabinet before ordering**; sheet count may move).

## 6. Printable PDF
Write HTML (A4, `@page` margins, DejaVu Sans) and print it with
`/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --no-sandbox --no-pdf-header-footer --print-to-pdf=<out> <html>`;
render a PNG preview with `pdftoppm` and look at it before sending.
- **Page 1 — customer:** what's included, the options with ex VAT / VAT / inc VAT, not included. Blank customer line.
  Says *not a formal quote* — **the formal quote is issued through the CRM** unless the owner says this is it.
- **Page 2 — internal, marked "do not hand to customer":** the full build-up and the ⚠ list.

## 7. Record and publish
Cost sheet and PDF in `Outputs/`, change-log section per revision (quote the owner's words), Drive in place + `chk.sh`,
commit, push. Offer a Lathams quote request (supplier-quote-request) to replace proxies.

## Boundaries
Darius costs; **Minda prices and sends**. Never send a quote or contact a customer or supplier (§6a). No order is placed.
