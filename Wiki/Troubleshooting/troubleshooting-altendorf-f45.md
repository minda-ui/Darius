---
title: "Troubleshooting — Altendorf F45 (FA2303)"
category: Troubleshooting
status: active
sensitive: false
created: 2026-09-15
updated: 2026-10-11
sources:
 - ../../Raw/F45 part 5.pdf
 - ../../Raw/F45 part 7.pdf
 - ../../Raw/F45 part 8.pdf
related:
 - troubleshooting-and-fault-log-system.md
 - ../Machinery/altendorf-f45-panel-saw.md
 - ../Processes/maintenance-schedule-altendorf-f45.md
---

# Troubleshooting — Altendorf F45 sliding-table saw (`FA2303`)

Fault reference for the F45. Two fault systems: the **mechanical fault table** (main manual, ch.8) and
the **ElmoDrive control-unit error codes** (ElmoDrive manual). Log every fault on the **Fault Log**
(`414932606781316`). **Lock the machine out before clearing a fault; electrical/cabinet work and brake
faults are for a qualified electrician or an Altendorf technician, not the operator.**

## Mechanical fault table (main manual, ch.8)

| Symptom | Cause | Fix |
|---|---|---|
| Machine won't switch on | Main switch off / power or phase failure / overload tripped | Switch to "I" / restore supply, check factory fuses / let motor cool, check the diagnosis display |
| Machine switches off during operation | Sliding table over blade centre line / E-stop pressed / door or base plate open / control-circuit fuse (F1, F2, F8) blown / phase failure | Move table back / rearm E-stop / close door or plate / replace fuse with same rating only / fix supply phase |
| Workpiece jams while feeding | Overload tripped (blunt blade or excess feed) / fuse blown / blunt blade / wrong riving-knife thickness | Change blade or reduce feed & let motor cool / replace fuse / fit sharp blade / fit correct riving knife (≥ blade thickness) |
| Break-outs despite scorer | Feed too low / too many teeth / incorrect free cut / scorer misaligned / scoring blade too narrow / blunt scoring blade | Increase feed / change blade / readjust free cut (~0) / realign / adjust saw width / replace scoring blade |
| Workpiece rises when cut with scorer | Cutting height too low | Set the scoring blade higher |
| Cut size ≠ fence setting (rip or crosscut) | Dimension scale misadjusted / DIGIT X calibration wrong | Reset via test-cut and measure / recalibrate |
| Pivot arm doesn't move smoothly | Soiled telescopic tube / track rollers | Clean, check the wiper |
| Sliding table has lateral play / sits proud at end positions | Sub-rollers incorrectly set | Set the sub-rollers |
| Blade burns on sliding-table side / rip-fence side / both | Free-cut setting wrong (insufficient / excessive / both) | Readjust the free cut on the relevant side(s) |
| Workpiece has burn marks | Jammed workpiece / operating error (guided on rip fence while using sliding table) / blunt blade | Fit riving knife correctly or use a wider one / guide at LH or RH fence only / change blade |
| No air to air-cushion table | Insufficient supply / solenoid valve stuck / TPL/TPV not supplied / fan not working | Check 6 bar supply & hoses / electrician checks coil / check fuses / electrician checks fan |
| No air cushion forms | Ball roller leaking / excess pressure / brush too high | Push ball down or replace roller / lower pressure / lower the brush |

## ElmoDrive error codes (control-unit manual)

Condensed; where the OCR could not confirm the exact fix for E01–E15, check the control unit's own
on-screen text. "Request a service technician" means an Altendorf technician, not operator-fixable.

| Code | Meaning | Fix |
|---|---|---|
| E01–E15 | Internal errors; limit switches ES MIN1/MIN2/MAX reached; coupling/collision/positioning/reference-run/short-circuit errors; optimisation limit; axis comms not released; VH/VS position errors | Service technician **or** new reference run (per-code text on screen) |
| E16 | Scorer motor running with a large blade installed | Turn the motor off before parking |
| E17 | Blade-size detection inconsistent | — |
| E18 | Fresh-oil lubricator empty | Change the cartridge (MT-027) |
| E19 | Tool speed faulty, speed will be deleted | — |
| E21–E22 | Update-file errors on USB drive | — |
| E23 | Remote-maintenance file missing | Check the data-carrier directory |
| E29 | No remote-maintenance connection | — |
| E31 | Swivel-segment sensor failure | Check the sensor |
| E40 / E41 | 20 VAC / 24 VAC control voltage missing | Check fuse **F9** / **F8** — F9 feeds the scorer drives, see *E40 and a scorer that will not rise* |
| E42 / E43 | Scoring / main-saw motor overheated | Allow to cool |
| E44–E49 | Sliding-table limit switch / blade cover / door / E-stop 1/2/3 actuated | Close / rearm as applicable |
| E50 | Speed-sensor setting | Check setting and sensor |
| E51 | Brake unit: phase failure / rotation | Check fuses **F15 / F16** |
| E52 / E53 / E55 | Brake-unit timeout / mains contactor / comms error | Service technician |
| E54 | Operating error — riving-knife or speed wrong for the fitted blade; **drives cannot start** | Check speed and riving-knife position |
| E56–E58 | Frequency-converter phase/overvoltage / excessive speed / comms error | Press any button / restart, then service / service technician |
| E59 | Emergency-running block at 3500 rpm | Switch the main blade off and on again |
| E61 | Drive positioning / current-consumption error | Lubricate the axle |
| E81 / E82 | Shaft-encoder errors | Service technician if recurring |
| E91K / E93K | STOP / START button K-contact error | Service technician — **but see the E91K note below first** |
| E92 | AC stop-circuit signal missing | Service technician if recurring |
| E94 | K-free signal missing | — |
| E99 | Control electronics over-temperature | Switch off, let cool; service technician if recurring |
| M01 / M02 | VH/VS or large-blade axis not referenced | Reference the axis |
| M03 | STOP actuated | Continue with START |
| M04 | Scorer not parked, main motor can't start | Return to position with START |
| M05 / M06 | Drive positioning error | Return to position with START |
| M07A / M07E | Collision risk with attachments / rip fence extended | — |
| M08 | Workpiece not removed | — |

## E91K can mean the yellow START button, not a STOP button

**Found on this machine, 2026-10-01 (Fault Log `FL-004`).** The screen read *"E91K: K-contact of Stop
button faulty"*. It appeared when the **yellow START** button was pressed to position the fence — and
the fault was **dust in that START button**, not in a STOP button. Blowing the START button out with
compressed air cleared it.

**Outcome (2026-10-11):** no E91K in the week after the clean, with extraction back to full suction from
2026-10-10 — `FL-004` closed **Resolved**. If it returns, reopen `FL-004` rather than raise a new fault;
the weekly blow-out is `MT-029`.

**So if E91K appears when pressing the yellow START:**
1. Switch the machine off and blow out the **yellow START** button first, then the I/0 buttons.
2. Restart. If E91K returns, call an electrician or Altendorf technician to inspect that button's
   contact block — tell them the screen says STOP but the trigger is START.
3. **Never bridge or bypass a button contact** — they are part of the safety circuit.

*Why the control reports a dirty START contact as E91K rather than E93K is not known. It is recorded
as observed, not explained.* Dust builds up fastest when extraction is off or weak; routine blow-out
is `MT-029` in the maintenance schedule.

## Note

No F45 fault-table entry describes an edge-band/glue-line "jagged corner" defect the way the Hebrock's
did — this is a saw, so its quality faults are scorer break-outs and burn marks. A furniture-corner
edge defect belongs to the Hebrock, not here.

## Sources

[^1]: [F45 manual, part 5](<../../Raw/F45 part 5.pdf>) — ch.8 mechanical fault table
[^2]: [ElmoDrive manual, part 7](<../../Raw/F45 part 7.pdf>) — error-code list
[^3]: [ElmoDrive manual, part 8](<../../Raw/F45 part 8.pdf>) — error-code list continued

## E40 and a scorer that will not rise — fuse F9 feeds the scorer drives

**From the manual's circuit diagram, Fig. 5-34 (p.77; Drive `F45 part 3.pdf`, PDF page 2), found on 2026-10-11 for
fault `FL-005`.** The control transformer, after fuses **F1–F2**, has three secondary taps:

| Tap | Fuse | Feeds |
|---|---|---|
| 18 V | F11 / F7 | diode laser (option) / display, sensors, Digit_X |
| **20 V** | **F9** | **→ `K5E` (supply contactor for adjustment drives) → `GL1` (rectifier) → scorer height and scorer side drives** (*Verstellantriebe Ritzerhöhe / Ritzerseite*) |
| 24 V | F10 / F8 | spray (option) / the safety chain and contactor control |

**So E40 (*"20 VAC control voltage missing — check fuse F9"*) and a scorer that will not move up or sideways are the
same circuit.** Check, machine isolated and locked off: **F9** (blown, or loose in its holder) → `K5E` → `GL1` → the
wiring between. Replace a fuse with the **same rating only**; if F9 blows again, there is a short downstream —
electrician or Altendorf. **Never bridge a fuse.**

Fuse legend (manual p.78): **F1–F2** control primary · **F4–F6** scorer motor · **F7–F9** control secondary ·
**F10–F11** spray/laser · **F12–F14** CEKON · **F15–F16** brake unit (E51). *This is the manual's generic diagram, not
this machine's drawing `B1434.0220`.*

**Where F9 is — from the owner's photograph of the right-hand cabinet, 2026-10-11.** Top of the panel: control
transformer **`T1`** (BLOCK B1307116, 280/700 VA; primary taps 380/400/420 V). Immediately right of it, contactor
**`K5E`** (Schneider LC1SK0600); then **four fuse terminals in a row, labelled left to right `F9`, `F8`, `F7`, `F11`** —
**F9 is the first one, right next to `K5E`.** `GL1` (rectifier) is just below and right of them. *(F10 — spray — is not
fitted.)* Lower rail: `F1`/`F2` (primary) at the left, `F4`/`F5`/`F6` (scorer motor U/V/W) in the middle.

**Fuse rating, as printed on `T1`'s plate (read from the photo — confirm on the fuse itself):** 24 V secondary 2.08 A →
**2.0 AT**; 18 V 6.1 A → **6.3 AT**; **20 V 6.0 A → 4.0 AT**. So F9 should be a **4 A time-lag (T)** fuse.

**Two hazards in this cabinet, before touching anything:**
- **The mains terminals `L1`/`L2`/`L3` (bottom right) stay live with the main switch off** — they are upstream of it.
  Isolate at the wall supply as well, or do not go near that corner.
- **Two KEB inverters** (main saw "5,0 KW BS" left, blue unit right): their label says capacitors take **5 minutes** to
  discharge. Wait 5 minutes after switching off.

The second photo the same day — the **ElmoDrive control board** in the other cabinet — showed **sawdust on the cabinet
floor**; the board's LEDs were green.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-15 | Created; mechanical fault table + full ElmoDrive error-code list carried over from the machine article's Fault-diagnosis section | Session — workshop operational systems build |
| 2026-10-01 | Added the E91K / yellow START note from fault `FL-004`, on the owner's instruction | Session — 2026-10-01 extractor and F45 faults |
| 2026-10-11 | Outcome line: `FL-004` closed Resolved after a week with no E91K (owner) | Session — 2026-10-11 |
| 2026-10-11 | New section: E40 / fuse F9 feeds the scorer height and side drives (manual Fig. 5-34), for `FL-005` | Session — 2026-10-11 |
| 2026-10-11 | F9's position, rating (4 AT per `T1` plate) and cabinet hazards, from the owner's cabinet photo | Session — 2026-10-11 |
