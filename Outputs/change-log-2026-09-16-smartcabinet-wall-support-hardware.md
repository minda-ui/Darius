# Change log — SmartCabinet Wall Support hardware added (2026-09-16)

Session 10. Live troubleshooting session, no manual processed. Continued the TpaCAD tool-ambiguity
work from the previous session (owner tried the Tool [T] field approach on the CNC computer), then
switched to a different live task: adding two new hardware items to SmartCabinet's "Wall Support"
Cam Table so they can be used on real cabinet jobs.

## What happened

- Owner reported no Tool ID exists for the 3mm/5mm drill bushes on the Vitap outfit even though
 cutters (Fresa positions 101-104) do carry real IDs. Worked through this live: cutters use IDs
 because a single physical pantograph holder is swapped between many cutter definitions; fixed
 drill spindles apparently don't work the same way. Confirmed on a milling SETUP row that Tool [T]
 does take a real catalog-style ID (1002) directly — meaning the fix is likely to live entirely in
 getting a real "Dia. 5mm" CN Tools entry created and referenced directly on the failing HOLE/
 FITTINGX operation's own Tool [T] field, not in the outfit's per-bush Technology dialog. **Not
 yet fully tested end-to-end** (the CN Tools add + cross-computer transfer + Tool [T] entry has not
 been completed) — Task T016 stays open, updated with this refined understanding.
- Confirmed directly against the TPA CAD manual text that "CN Tools"/"Cam Table" don't appear
 anywhere in it — that catalog is entirely SmartCabinet's own, with no documentation in the
 machine-side manual. Also confirmed the two computers (SmartCabinet design PC, CNC control PC)
 are **not** live-networked — files (including, presumably, the tool database) move by manual
 transfer, same as `.TCN` job files. This answers an open question from yesterday's Processes
 article about whether the two systems auto-sync.
- Separately, added two new hardware items to SmartCabinet's Wall Support Cam Table:
 1. A Häfele "Concealed Cabinet Hanger, Dowel/Screw Mounting" — 4 side-panel holes.
 2. An adjustable wall-bracket system with 3 side-panel fixing holes and 2 backrest adjustment
 holes (through-holes).
- While building these, found the software's own built-in help text for every Cam Table column
 (B/S, X, Y, Ø, φ, Min H, Max H, D, L, H) — notably that φ means hole **depth**, not diameter or
 angle, and that X's sign convention depends on B/S and which edge a distance is measured from.
- **Found an unresolved discrepancy**: both hardware items' side-panel holes were described as
 "measured from the back edge," but the first needed X = -15 and the second needed X = +5 — opposite
 signs for the same stated reference edge. Did not force one to match the other; recorded both as
 actually used/confirmed and flagged the contradiction openly rather than guessing which is "right."

## What was done

- Created `Wiki/Processes/smartcabinet-wall-support-cam-table-reference.md`: full column reference
 quoted from the software's own help text, both worked examples, and the flagged X-sign
 discrepancy with an explicit warning not to generalise a rule from either example alone.
- Updated `Wiki/index.md`, `Outputs/kb-registers.md`, `CLAUDE.md` (v7).
- Smartsheet Tasks: updated T016 with the refined Tool [T]-field understanding; added T017 (resolve
 the SmartCabinet Wall Support X-sign discrepancy — check both hardware items' hole placement
 visually in SmartCabinet's preview once used on a real job).

## Judgement calls made, flagged for the owner

1. Did **not** try to make the two hardware items' X signs agree with each other by assuming one is
 wrong — both were the actual values confirmed/used at the time, and picking one to "correct" the
 other without evidence would just be guessing dressed up as a fix. Recorded the contradiction
 openly instead.
2. Did **not** mark Task T016 (TpaCAD tool-ambiguity fix) as resolved despite a much better
 understanding of the mechanism (Tool [T] field takes a CN Tools ID directly) — the actual fix
 (add the CN Tools entry, transfer it across computers, reference it on the operation) has not
 been completed end-to-end yet.
3. Treated the "no live network sync between SmartCabinet and the CNC computer" finding as worth
 recording in the KB on its own, since it directly answered an open question left in yesterday's
 TpaCAD Processes article, rather than only mentioning it in passing.
