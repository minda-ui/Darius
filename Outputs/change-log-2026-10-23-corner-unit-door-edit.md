# Change log — 2026-10-23 — Corner wall unit: door program edited by hand on the owner's request

Session 38.

## (1) Session start
- Raw/: Victoria's framework **v0.2.1** clarification (all team members stay in the master core; nothing changes in
  Darius's access, rows or dates) — information only. Hub: `AWT-0089`, `AWT-0194`, `AWT-0225` Blocked; `AWT-0127`, `AWT-0942`
  In Progress. Fault Log `FL-003` In Progress, `FL-005` Monitoring. Maintenance nothing due. Git nothing new.

## (2) Owner: *"Can you update the door file? SmartCabinet not allowing the changes you're telling me"*
- **Width 420 → 370.5.** Basis: the sides (319 deep, inner faces 581 from each wall) meet the top/bottom diagonal at their
  inner front corners (581, 319) and (319, 581); the opening between them is (581 − 319) × √2 = **370.5**. Blum +45° I
  (set-back front, p. 118): **FB = LW**.
- **Three values changed, nothing else:** `09-DOOR-1.TCN` header `DH=420.0 → 370.5` and `SIDE#1` `HF=420.0 → 370.5`;
  `worklist.xmlst` door row `HEIGHT 420.0 → 370.5`. Hinge cups (Ø35 at X 100 / 796, Y 22.5) and screw pilots (Y 32) are
  measured from the hinge edge (Y 0) and do not move. Encoding kept (UTF-16 LE with BOM), diffed line by line, re-decoded.
- **Not overwritten:** written to a **new folder** `Raw/Review folder/600x600 Corner Wall Unit v2 - door 370.5 (Darius edit 23-10)`
  (`10K9RLtQSuk8aNN1X_Tz_guXSSqNeT_Qn`): `09-DOOR-1.TCN` `1yTMJrepBVJVi6LfuzEplHcvQ7aTUkQz7`, `worklist.xmlst`
  `1OGonYNo8ny_J8L2yE3_HRgj44AlMEXcb`; md5 equal to the local files. The owner's `v2` folder and the `Furniture` machine
  folder were not touched.
- **Caveats given:** a hand edit diverges from the SmartCabinet model (a later re-export brings 420 back); the saw cut size
  comes from the cutting list, so it must say 370.5 too; dry-fit before the hinges are set.

## (3) Shelf joints — option B tried (round 4, `v2 v4`), then option A
- Owner tried the joint table: `50 · 40 · 2 · 0` row, `2 → 1`. **v4 result:** still 2 joints per shelf edge, but both
  parts' rear joints moved to ~40 from the shelf back — **rear aligned (75 / 75.5 from the wall), front still 18.5 out
  (240 vs 221.5)**. The side is 319 deep, the shelf edge follows the 300 line; symmetric table values cannot fix it.
- v4 also **reverted the construction** (sides 900 full height, top/bottom 581 between them, 2 joints per end) — owner told
  not to use v4. Pocket geometry now read from the raw lines: each Cabineo shelf-pin seat is an open slot Ø18.8, centred
  on the `type2` X/Y, from 9.4 outside the edge to 35.6 in.
- **Owner: "Yes, do both"** — (a) **v5 built** in `Raw/Review folder/600x600 Corner Wall Unit v5 (Darius - v3 + door 370.5 +
  plain shelf pins)` (`1cqn1ASdLWL5bNqrsSPQ8FyvjQhqy0hHP`): all parts = round-2/v3 SmartCabinet files (incl. the
  **SmartCabinet** left side, not the TpaCAD re-save), door + worklist = the 370.5 edit, **both shelf programs emptied** of
  their 224 pocket lines (all `W#89/2201/2111`, tool 1002) — shelves sit loose on 5 mm pins in the side rows and the back
  rows. 13 files, all md5 equal to local. (b) **SmartCabinet ticket drafted**
  `Outputs/2026-10-23-smartcabinet-ticket-corner-shelf-joints.md` for the owner to send via the in-app Ticket.
