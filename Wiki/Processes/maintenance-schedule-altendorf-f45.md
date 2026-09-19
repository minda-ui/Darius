---
title: "Maintenance schedule — Altendorf F45 (FA2303)"
category: Processes
status: active
sensitive: false
created: 2026-09-15
updated: 2026-09-15
sources:
 - ../../Raw/F45 part 5.pdf
 - ../../Raw/F45 part 6.pdf
 - ../../Raw/F45 part 1.pdf
related:
 - machinery-maintenance-system.md
 - ../Machinery/altendorf-f45-panel-saw.md
 - f45-monthly-safety-device-check.md
 - ../Troubleshooting/troubleshooting-altendorf-f45.md
---

# Maintenance schedule — Altendorf F45 sliding-table saw (`FA2303`)

From the F45 main manual, Chapter 7 (cleaning/care) and the safety chapter (annual electrical check),
`F45 part 5/6.pdf` and `part 1.pdf`. **Maintain with the machine switched off and locked out.**
Rows are on the Smartsheet **Maintenance Schedule** (`6753985971226500`); the mandatory monthly
safety-device check is tracked separately on the **Safety Check Log** — see
`f45-monthly-safety-device-check.md`.

## Cleaning

| ID | Task | Interval |
|---|---|---|
| MT-021 | Clean-down: machine table, sliding table, extraction; vacuum/brush chips & dust | Daily |
| MT-022 | Deep clean: sliding-table guide/underside (spirit-soaked cloth), sub-rollers, rip-fence round rod, pivot arm (**dry only — do not oil the pivot arm**), tilt segments, interior | ~Every 6 months (see caveat) |

Cleaning agents by soiling type: chips/dust → vacuum/brush/cloth; resin → nitro thinner (general) or
petroleum/spirit on the sliding-table guide; rust prevention → universal oil after cleaning.
**Never apply resin remover to anodised surfaces.**

> **Caveat (from the machine article):** the manual's exact row-to-interval mapping (Daily / Weekly /
> Monthly / 6-monthly) was partly lost in OCR. Check the manual's own page-155 table before treating
> any single daily-vs-weekly pairing as authoritative. The intervals above are the safe reading; the
> genuinely interval-critical items are the lubrication and electrical checks below.

## Lubrication (trigger-based — the machine also prompts by display)

| ID | Task | Trigger |
|---|---|---|
| MT-023 | Grease saw-unit tilt at the lubricating nipple (set blade tilt 45°, cutting height 0 mm) | After 100 m of height-adjustment travel, **or at least once a year** |
| MT-024 | Grease CNC rip fence (DIGIT X) at its lubricating position; **max 5 grease-gun strokes = 7 g** | After 1500 m of travel, **or at least every 12 months** |
| MT-027 | Change the ElmoDrive central lubricator cartridge | On error **E18** "Fresh oil lubricator empty" |

**Over-lubricating the CNC fence from too-short intervals causes failures** — do not exceed 5 strokes.
Approved greases: Aralub HL 2, BEACON 2, BP Energrease LS 2, ELF ROLEXA 2, Gulfcrown No. 2, Marson
EPL 2, Shell Alvania R 2, SKF LGEP 2, Texaco Way Lubricant 220. **Greases with graphite or MoS2
additives are prohibited.**

## Electrical / safety-linked

| ID | Task | Interval |
|---|---|---|
| MT-020 | Monthly documented safety-device check (E-stop, sliding-table & chip-duct limit switches, ON/OFF switch, hood) — **logged in the Safety Check Log** | Monthly (mandatory) |
| MT-025 | PTC winding-shield resistor check by a qualified electrician (cold motor, expect 150–1000 Ω) | At least annually |
| MT-026 | Re-check the riving knife (thickness ≥ main blade; holder rated to Ø450 mm) | Every saw-blade change |
| MT-028 | Inspect scorer & main-saw drive belts and wear parts; replace on wear | Condition-based |

Key wear-part numbers (belts, riving-knife holder B1480.0051, saw shaft B1480.0044, RAPIDO Ø180 mm
scorer blades) and ordering contact are in `../Machinery/altendorf-f45-panel-saw.md` and
`../Suppliers/altendorf-gmbh.md`. **The PTC resistor and the F1/F2/F8/F9/F15/F16 fuses have no
part-number cross-reference** in any of the three manuals — identify them on the machine if one fails.

## Related compliance gap (not a maintenance task)

The F45's EC-type/GS/DGUV-Test certificates (HM 220023–25) **expired 22.02.2024** — an open compliance
question tracked as Task **T007**, not part of routine maintenance. See the machine article.

## Sources

[^1]: [F45 manual, part 5](<../../Raw/F45 part 5.pdf>) — ch.7 cleaning/care, technical data
[^2]: [F45 manual, part 6](<../../Raw/F45 part 6.pdf>) — duplex pair with part 5
[^3]: [F45 manual, part 1](<../../Raw/F45 part 1.pdf>) — safety chapter, annual PTC check

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-15 | Created from the F45 article's manual-derived Chapter 7 schedule + annual electrical check; rows loaded as MT-020…MT-028 | Session — workshop operational systems build |
