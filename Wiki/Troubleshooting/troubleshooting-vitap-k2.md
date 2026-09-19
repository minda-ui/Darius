---
title: "Troubleshooting — Vitap K2-2.0 (FA2304)"
category: Troubleshooting
status: active
sensitive: false
created: 2026-09-15
updated: 2026-09-15
sources:
 - ../../Raw/Vitap K2 2.0 manual part 4.pdf
related:
 - troubleshooting-and-fault-log-system.md
 - ../Machinery/vitap-k2-panel-saw.md
 - ../Processes/maintenance-schedule-vitap-k2.md
---

# Troubleshooting — Vitap K2-2.0 CNC boring/routing centre (`FA2304`)

Fault reference for the Vitap K2-2.0. The machine also has an **on-screen self-diagnosis** (TPA
Albatros): a fault symbol appears on the operator interface; press it to open the failure page. Log
every fault on the **Fault Log** (`414932606781316`). **Press E-stop and isolate power + air before
working on the machine — a "standby stop" can restart on its own.** Electrical faults and phase work
are for a qualified electrician (operator category D); "contact assistance service" = VITAP.

## Fault table (manual §7.8)

OCR on this page was imperfect; transcribed as faithfully as possible from the machine article.

| Problem | Likely cause | Solution |
|---|---|---|
| Faulty drilling | Worn drill bit | Replace per §5.3 |
| Faulty drilling | Unsuitable drill-bit type | Replace with a spade bit |
| Faulty drilling | Wrong feed speed | Decrease the drill-bit feed speed |
| Inadequate line voltage | Supply doesn't match the machine rating | Contact assistance service |
| Pedal doesn't respond | Faulty pedal or wrong connection | Check, then contact assistance service |
| Spindles rotate the wrong way | Inverted phases | Swap two phases in the line connector (electrician) |
| Spindles don't turn | Burnt fuse / gear breakage | Check motor fuses; contact assistance service |
| Machine won't start / start button inactive | An emergency device is active | Check E-stop, side-door limit switch, and the left/right limit switches |
| Pressers don't hold the piece | Insufficient air pressure | Check pneumatic-system pressure (0.6–0.8 MPa) |
| Panel damaged in the clamp pick-up area | Excessive clamp pressure | Adjust per §5.3.6 |

## Time-out failure (§7.6)

A separate procedure, not a table: a sensor-monitored move that doesn't complete in time. Switch off,
open the guard door, check the flagged sensor and its wiring, clear any obstruction, restart.

## Preventive links

Faulty drilling most often traces to tool wear or feed settings — the event-triggered inspection on
tool change (MT-034) and keeping the pneumatic system in check (MT-033) prevent the pressure/clamp
faults. See `../Processes/maintenance-schedule-vitap-k2.md`.

## Sources

[^1]: [Vitap manual, part 4](<../../Raw/Vitap K2 2.0 manual part 4.pdf>) — §7.5 failures / self-diagnosis, §7.6 time-out failure, §7.8 troubleshooting table

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-15 | Created; §7.8 fault table + §7.6 time-out procedure carried over from the machine article's Fault-diagnosis section | Session — workshop operational systems build |
