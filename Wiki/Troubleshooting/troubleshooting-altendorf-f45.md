---
title: "Troubleshooting — Altendorf F45 (FA2303)"
category: Troubleshooting
status: active
sensitive: false
created: 2026-09-15
updated: 2026-09-15
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
| E40 / E41 | 20 VAC / 24 VAC control voltage missing | Check fuse **F9** / **F8** |
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
| E91K / E93K | STOP / START button K-contact error | Service technician |
| E92 | AC stop-circuit signal missing | Service technician if recurring |
| E94 | K-free signal missing | — |
| E99 | Control electronics over-temperature | Switch off, let cool; service technician if recurring |
| M01 / M02 | VH/VS or large-blade axis not referenced | Reference the axis |
| M03 | STOP actuated | Continue with START |
| M04 | Scorer not parked, main motor can't start | Return to position with START |
| M05 / M06 | Drive positioning error | Return to position with START |
| M07A / M07E | Collision risk with attachments / rip fence extended | — |
| M08 | Workpiece not removed | — |

## Note

No F45 fault-table entry describes an edge-band/glue-line "jagged corner" defect the way the Hebrock's
did — this is a saw, so its quality faults are scorer break-outs and burn marks. A furniture-corner
edge defect belongs to the Hebrock, not here.

## Sources

[^1]: [F45 manual, part 5](<../../Raw/F45 part 5.pdf>) — ch.8 mechanical fault table
[^2]: [ElmoDrive manual, part 7](<../../Raw/F45 part 7.pdf>) — error-code list
[^3]: [ElmoDrive manual, part 8](<../../Raw/F45 part 8.pdf>) — error-code list continued

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-15 | Created; mechanical fault table + full ElmoDrive error-code list carried over from the machine article's Fault-diagnosis section | Session — workshop operational systems build |
