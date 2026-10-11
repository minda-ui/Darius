---
name: machine-control-fault
description: Work a control or electrical fault on any workshop machine (F45, Vitap, edgebander, extractor panel, compressor) that is not a three-phase motor problem — an error code on the display, an axis or drive that "won't move", a button fault, an intermittent message, "display shows…". For motors that won't start, buzz, run slow or trip, use three-phase-motor-fault instead.
---

# Machine control fault

Adopted at the 2026-10-11 good night, from `FL-004` (F45 E91K, 10-01, closed 10-11 after a clear week) and `FL-005`
(F45 scorer will not move, intermittent E40, 10-11).

## Steps
1. **Log it at once** — Fault Log `414932606781316`, next `FL-` number, Status **Open**: the symptom in the owner's
   words, *not* a diagnosis. Ask **what has been worked on** and **what exactly the screen says** (photo; the code and
   full text — the text can mislead, as E91K did).
2. **Look it up** — the machine's troubleshooting article, then its manual (`machine-manual-lookup`): what the code
   means, what circuit it names, what else that circuit feeds.
3. **Cheapest checks first, owner-safe:** clean the button/area of dust; fuses **isolated**, like-for-like rating;
   power-cycle and note whether it returns. Write each result on the row as it comes.
4. **Split test to halve the circuit** — find two things that share a supply or a control path and ask which works (e.g.
   scorer height vs side: both dead = the shared supply; one dead = that drive). Put the result and its meaning in
   *Probable cause*.
5. **Hand over cleanly when it needs live measurement:** a table on the row — reading, where, and what a failure means —
   so an electrician or the manufacturer can start without us. Include the manufacturer's service contact
   (`Wiki/Suppliers/`).
6. **Safety in every message:** isolate at the wall where supply terminals sit upstream of the main switch; inverter
   capacitor discharge time; **never bridge a fuse, a contact or a safety device.**
7. **Close properly:** fixed → **Monitoring**; **Resolved only after a clear week** (or the owner says so), Date Resolved =
   date confirmed; a recurrence reopens the same row. Add the lesson to the troubleshooting article (in place, SAME) and
   a change-log entry; a recurring cause becomes a Maintenance Schedule task (as `MT-029` did).

## Never
- Never call a cause established without a measurement or the owner's finding at the machine.
- Never write "two faults" or "one fault" as fact before a split test supports it.
