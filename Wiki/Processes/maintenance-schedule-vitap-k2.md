---
title: "Maintenance schedule — Vitap K2-2.0 (FA2304)"
category: Processes
status: active
sensitive: false
created: 2026-09-15
updated: 2026-09-15
sources:
 - ../../Raw/Vitap K2 2.0 manual part 3.pdf
 - ../../Raw/Vitap K2 2.0 manual part 4.pdf
related:
 - machinery-maintenance-system.md
 - ../Machinery/vitap-k2-panel-saw.md
 - ../Troubleshooting/troubleshooting-vitap-k2.md
---

# Maintenance schedule — Vitap K2-2.0 CNC boring/routing centre (`FA2304`)

From the Vitap K2-2.0 manual, Chapter 7 "Routine and extraordinary maintenance" (`part 3/4.pdf`).
This machine's maintenance is **hours-based and event-triggered** — there is no daily/weekly calendar
table like the Hebrock's. **Lock out (disconnector to O, padlocked) and isolate the pneumatic inlet
before any maintenance; wait ≥10 minutes after opening an electrical panel for residual energy.**
Rows are on the Smartsheet **Maintenance Schedule** (`6753985971226500`).

| ID | Task | Interval / trigger |
|---|---|---|
| MT-030 | Lubricate spindle-holder head & channel head (MOLYGUARD GS ARTIC grease), §7.2.5.1 drain-nipple procedure | Every 200 operating hours |
| MT-031 | Lubricate all ball-recirculating units (VANGUARD LIKO EPO grease) — operating unit, clamps/mobile shoulder, pressers, tool magazine | Every 200 operating hours |
| MT-032 | Grease each fitted optional aggregated head (front-milling / LAMELLO / OVVO), ~3 g per head | Every 100 operating hours |
| MT-033 | Full pneumatic-system check: wiring/tubing for leaks, quick-drain valves, regulator calibration | At least every 500 operating hours |
| MT-034 | Unscheduled inspection (§7.3.2) of drives, measurement systems, encoders, potentiometers | Every time a tool/part is replaced or removed |
| MT-035 | Routine cleaning: exterior, sawdust from rollers/guides/axes; operator interface; fan filters; pneumatic-system filter | Routine (no fixed interval — treat as daily habitual) |
| MT-036 | Safety-device efficiency check (§6.8) | Before every automatic-mode activation, and after any maintenance |

**Note on MT-036 / §6.8:** unlike the Altendorf F45's monthly check, the Vitap manual states §6.8 as a
mandatory *functional test before automatic mode* — it does **not** state a written-log/dated-record
requirement. So it is **not** put on the Smartsheet Safety Check Log unless the owner decides it should
be. This is an open question (see the machine article and troubleshooting article).

**Lubricants named:** MOLYGUARD GS ARTIC (heads), VANGUARD LIKO EPO (ball-recirculating units). Use
only these; qualified maintenance personnel (operator category C) for the lubrication points.
"Extraordinary" mechanical maintenance is VITAP-technician-only.

## Sources

[^1]: [Vitap manual, part 3](<../../Raw/Vitap K2 2.0 manual part 3.pdf>) — ch.7 routine maintenance & scheduled lubrication (pages 60-126 even)
[^2]: [Vitap manual, part 4](<../../Raw/Vitap K2 2.0 manual part 4.pdf>) — ch.7 continued (pages 125-61 odd)

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-15 | Created from the Vitap article's manual-derived Chapter 7 schedule; rows loaded as MT-030…MT-036 | Session — workshop operational systems build |
