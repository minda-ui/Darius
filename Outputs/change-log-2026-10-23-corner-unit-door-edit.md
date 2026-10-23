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
