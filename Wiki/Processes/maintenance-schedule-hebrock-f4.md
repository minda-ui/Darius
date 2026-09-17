---
title: "Maintenance schedule — Hebrock F4 (FA2301)"
category: Processes
status: active
sensitive: false
created: 2026-09-15
updated: 2026-09-15
sources:
 - ../../Raw/part 4.pdf
 - ../../Raw/part 5.pdf
 - ../../Raw/part 6.pdf
related:
 - machinery-maintenance-system.md
 - ../Machinery/hebrock-f4-next-edge-bander.md
 - ../Troubleshooting/troubleshooting-hebrock-f4.md
---

# Maintenance schedule — Hebrock F4 edge bander (`FA2301`)

From the F4 manual, Chapter 7 "Wartung und Pflege" (`part 4/5/6.pdf`). **Always maintain with the
machine switched off and locked out; use manufacturer-approved materials only; never mix lubricants.**
Each row here is a task on the Smartsheet **Maintenance Schedule** (`6753985971226500`) with the ID
shown; log completion by dating **Last Done** there.

## Cleaning & inspection

| ID | Task | Interval |
|---|---|---|
| MT-001 | E-stop buttons — check function | Daily |
| MT-002 | Pneumatic controls — check function | Daily |
| MT-003 | Clean edge-guide channel, nip-roller zone, router station, trim saw & corner-rounder of glue/chips/scraps (remove glue from silicone rollers while cold) | Daily |
| MT-004 | All screws — inspect and retighten | Weekly |
| MT-005 | Glue pot — check heating output (~22 kW); replace defective heater cartridge | Weekly |
| MT-006 | Router station — check cutter sharpness; check feeler-disc wipers and feeler discs; replace if needed | Weekly |
| MT-010 | Chain bed — clean feed interior | 1–2× per year (~182 days) |
| MT-009 | Chain bed — clean & lubricate sliding surfaces (black plates) with WD-40 | Every 3 months |

## Lubrication

| ID | Task | Interval |
|---|---|---|
| MT-007 | Oil trim-saw & corner-rounding router guide shafts (thin machine oil) | Weekly |
| MT-008 | Oil router-station round columns & adjustment screws (thin oil) | Every 4 weeks |
| MT-011 | Grease the chain-bed drive chain | Annually |

## Wear / condition / long-interval

| ID | Task | Interval |
|---|---|---|
| MT-012 | Router-station precision ball bearings — inspect/replace (qualified personnel) | Every 5,000–6,000 operating hours (the only hours-based item) |
| MT-013 | Replace PLC/HMI backup battery | Every 2 years, or immediately on alarm |
| MT-014 | Replace joint-cutter diamond tools, trim-saw blade, router cutters, radius/face scraper blades, buffing wheels | On visible wear/damage (no calendar) |

Spray consumables (release agent, cleaner, glide agent — all Riepe GmbH) are maintenance-free if only
the specified fluids are used; specifically protect the corner-router feeler shoes/rings from glue
build-up. Chain-bed drive-chain tension is checked/adjusted as needed.

**Note (from the machine article):** the feeler-disc wiper / feeler-disc checks (MT-006) belong to the
main router station (Frässtation), **not** the corner-rounding router (Eckenabrundfräse); the
corner-rounder's own scheduled maintenance is the daily clean (MT-003) and weekly guide-shaft oiling
(MT-007) only.

## Sources

[^1]: [Hebrock F2/F4/F5 next manual, part 4](<../../Raw/part 4.pdf>) — ch.6/7, adjustment & maintenance
[^2]: [part 5](<../../Raw/part 5.pdf>) — ch.7 maintenance, ch.8 fault table (odd pages)
[^3]: [part 6](<../../Raw/part 6.pdf>) — ch.7 continued (even pages)

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-15 | Created from the Hebrock article's manual-derived Chapter 7 schedule; rows loaded to the Maintenance Schedule sheet as MT-001…MT-014 | Session — workshop operational systems build |
