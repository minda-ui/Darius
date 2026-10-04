---
title: "F45 blades — carbide (TCT) or diamond (PCD)?"
category: Processes
status: draft
sensitive: false
created: 2026-10-04
updated: 2026-10-04
sources:
 - "Owner (Minda), 2026-10-04: asks whether changing the F45's TCT blades to diamond is worth the investment, cuts cleaner, and — staying sharp longer — cuts straighter"
 - "Web search, 2026-10-04 (snippets only; cutektools.com and keybladesfixings.co.uk are blocked to this session's fetcher): Cutek Tools 'PCD vs TCT circular saw blade' and 'panel sizing solutions'; Key Blades 'What is a PCD circular saw blade'; Smarter Production 'scoring blade types'; morecuttingtools.com and tristatetoolgrinding.com on PCD regrinding; toolingideas.com on why blades wander"
 - "UK listings, 2026-10-04: CMT XTreme Diamond Ø350 × 3.5 × 30, Z72, 45° TCG — £800.01 ex VAT (Machinery4Wood / Westcountry) and £607.14 ex VAT (another retailer, per search snippet)"
 - "`egger-compact-laminates.md` §6 — EGGER, Leitz and Leuco guidance filed in `Raw/EGGER/`"
 - "North East Grinding emails in info@, 2026-01-12 to 2026-07-21 (bodies only) — `../Suppliers/north-east-grinding.md`"
 - "`../Machinery/altendorf-f45-panel-saw.md` — calibration test (350 mm / Z72 at 5,000 rpm, < 0.2 mm), RAPIDO Ø180 scorers, troubleshooting table"
related:
 - ../Machinery/altendorf-f45-panel-saw.md
 - maintenance-schedule-altendorf-f45.md
 - egger-compact-laminates.md
 - f45-grooving-slots-with-the-main-blade.md
 - ../Suppliers/scott-sargeant.md
 - ../Suppliers/north-east-grinding.md
---

# F45 blades — carbide (TCT) or diamond (PCD)?

**Short answer.** A diamond (PCD) blade does **not cut cleaner than a sharp carbide one**; it **stays sharp far
longer**, so the clean cut lasts. It makes cuts straighter **only compared with a dull blade**. Whether it is worth
**about £600–800** depends on **how often the carbide blades are changed today**, which is now being logged
(MT-037 / MT-038). **Decision: not yet for MFC alone; yes if compact laminate becomes a product line.**

## Cleaner cuts?

- **New against new, the finish is about the same.** The difference is **how long it lasts**: faced board dulls
  carbide quickly, and once it is dull the melamine starts to chip; PCD holds a chip-free edge for months (vendor
  claim).
- **The scorer matters as much as the main blade.** The **RAPIDO Ø180 scorers** cut the visible underside. A PCD
  main blade with carbide scorers will still chip underneath as the scorers wear. Leitz's EGGER guidance pairs a
  **DP (diamond) main blade with a DP scorer** (`egger-compact-laminates.md` §6).

## Straighter cuts?

**Only against a dull blade.** A dull blade pushes rather than cuts: it heats up, wanders and burns. The F45's own
troubleshooting table lists **"blunt blade"** for jams and burn marks, which is what PCD removes. But straightness
otherwise comes from the machine: **calibration** (Altendorf's test, under **0.2 mm** on 1,000 × 1,000), **free cut**
(scorer alignment), **feed**, and a **flat blade**. **A fresh carbide blade cuts as straight as PCD.**

## Is it worth the money?

| | Carbide (TCT) | Diamond (PCD) |
|---|---|---|
| Ø350 × 30, Z72 | about **£70–170** ex VAT | **about £607–800** ex VAT (CMT XTreme, UK listings) |
| Life | baseline | vendors: **10× or more** in real use; **up to 50×** only in lab conditions |
| Sharpening | cheap, local, many times | **specialist (EDM) only, 2–4 times**; blade goes away, so a **carbide spare** is still needed |
| Weak point | dulls in faced board | **brittle**: one screw or staple can shatter a tooth; dropping it is costly |

PCD scorers: vendor guide puts them at **4–8× carbide's price for 15–50× the life**; a UK price for a Ø180 PCD scorer
was not found.

- **Trade rule of thumb:** PCD pays off when carbide is being **changed or sharpened about once a week or more** on
  chipboard / MFC.
- **Compact laminate changes the answer.** EGGER: **DP recommended, HW "suitable to a limited extent"**.
- **Before buying, check:** PCD blades are often **3.5 mm kerf**, not 3.2 — **riving knife** (MT-026: thickness ≥
  blade body, holder to Ø450), **scorer width** to match, and the **real kerf entered in Grooves**
  (`f45-grooving-slots-with-the-main-blade.md`). Speed: Ø350 at 4,000 rpm = 73 m/s, inside EGGER's 60–90 m/s.
- **Candidates seen:** CMT XTreme PCD Ø350 × 3.5 × 30 Z72 (listings above); CMT 237 Xtreme PCD Ø350 × 30 Z72 kerf 3.2
  (Scott+Sargeant, `../Suppliers/scott-sargeant.md`; price not readable). **No purchase made — the owner's call.**

## What sharpening costs us now (North East Grinding, 2026)

From six emails, bodies only (`../Suppliers/north-east-grinding.md`):
- **A batch every ~3 months, about £200 each** (Jan, 30 Apr, 21 Jul) → **about £800 a year**, *for every TCT blade sent,
  not only the F45's*.
- **One blade sharpened alone: £17.88** (19 Jan). **New Stehle TCT 300 × 96T × 30: about £106 each** (three for £318.60,
  Jan). VAT basis not stated in either.
- **Possibly our blade:** three **Stehle TCT Ø300 × Z96 × 30** were bought in January. *Whether they are the F45's main
  blade is not confirmed* — the F45 manual's calibration test uses Ø350 / Z72.

**First rough payback.** A Ø350 PCD at **£607–800 ex VAT** against **£17.88 a sharpening**: it has to save **34–45
sharpenings** to pay back, plus the downtime of each change. *If* the F45's main blade were most of the ~£800 a year,
that is **about a year**; if it is a small part, several years. **The receipts' line items (blades per batch, sizes)
would settle it** — not yet opened.

## How the decision gets made

**Payback ≈ PCD price ÷ (carbide blades + sharpenings saved per month + downtime per change).** It needs:
1. **What is fitted now** — main and both scorers: diameter, Z, TCT/PCD, maker. *Still unrecorded.*
2. **How often** each is changed or sent for sharpening — **logged from 2026-10-04 as MT-037 (main) and MT-038
   (scorers)** on the Maintenance Schedule: date in *Last Done* (cell history keeps the trail), and blade, reason,
   sharpener and cost noted.
3. **What a sharpening costs** — *partly answered: £17.88 for one blade; ~£200 a quarter for batches (North East Grinding). Line items are in the receipts.*
4. **Whether compact laminate goes ahead** — if yes, PCD is justified on that alone.

*Figures are vendor claims and listing prices from search snippets, not quotes or tests on this machine.*

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-10-04 | Created from the owner's question; MT-037 / MT-038 added to the Maintenance Schedule | `change-log-2026-10-04-f45-grooving-led-slot.md` (20) |
| 2026-10-04 | Sharpening costs from North East Grinding's emails; first rough payback | `change-log-2026-10-04-f45-grooving-led-slot.md` (21) |
