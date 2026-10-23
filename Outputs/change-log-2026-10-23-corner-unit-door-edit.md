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

## (4) "Library" project — workshop cost sheet v0.1
- Owner asked how to cost a project and issue a quote. Answered with the split (Darius: workshop cost; Minda: price/rate/
  margin; Nadia: quote in the CRM; Rachel: invoice), then costed the owner's SmartCabinet export (`library_Panel.csv`,
  `library_Pieces.csv`, uploaded in chat): 24 units, 293 parts, 134.99 m², 29 sheets (yield 80.3 %).
- `Outputs/2026-10-23-library-project-cost-sheet-v0.1.md` (Drive `1EnELNZM6CQm2dP7fu3Ra7bZ-onf4XIgb`). Known materials ≈ £4,958.81 (board
  29 × £150 **proxy** — U702 PM not in the Panel Price Library; edging proxy U708 PM; hinges and Cabineo from the Hardware
  Price Library); **open:** shelf pins, wall fixings, handles, legs/plinth (not in library or scene), labour ≈ 90.5 h
  (Darius's estimate) × the owner's rate. Proxies and estimates marked in the sheet; nothing presented as a quoted price.

## 5. Library cost sheet v0.5 — wall brackets and £45/h
- Owner: *"use kitchen wall unit brackets"* → Häfele concealed hanger 290.03.935 R / 290.03.936 L (130 kg/pair, 16 mm
  behind the back), 48 for 24 units, **indicative** £3.74 ex VAT each (eBay £4.49 inc VAT) = £179.60. Wall rail separate,
  price unknown. Sources: Häfele catalogue https://files.hafele.co.uk/CatalogFiles/www/23T7-220.pdf; eBay 175558001083.
- Owner: *"My rate is £45/hr"* → 90.5 h = £4,072.50 (Option 1); 99.5 h with +10 % care = £4,479.75 (Option 2).
  Owner also wrote *"1 hr at £65"*; recorded as an alternative (£5,882.50 / £6,470.75) to confirm.
- Materials + workshop: **Option 1 £6,970.10**, **Option 2 £10,014.35** — before handles, wall rail, delivery/fitting,
  margin and VAT. Published in place, SAME.

## 6. Library cost sheet v0.6 — machine hours on top
- Owner: *"£45 is my rate, we need to add machinery hours too and top of my rate"* (with the earlier *"1 hr at £65"*):
  labour £45/h on all 90.5 h, plus machine time £65/h on the 35 machine hours (F45 12, Hebrock 8, Vitap 15).
- Option 1: £4,072.50 + £2,275.00 = £6,347.50 workshop; with materials **£9,245.10**.
  Option 2 (+10 %): £4,479.75 + £2,502.50 = £6,982.25; with materials **£12,516.85**. Before handles, rail, delivery,
  margin, VAT. Published in place, SAME.
