# Change log — 2026-10-14 — F45 scorer: the cause was configuration, not electrics

Session 34.

## (1) Session start
- **Raw/:** nothing new since 2026-10-10. **Hub:** `AWT-0089`, `AWT-0127`, `AWT-0194`, `AWT-0225` (Blocked), `AWT-0537`
  (four days, not started). **Fault Log:** `FL-003`, `FL-005` In Progress. **Maintenance:** nothing due. **Git:** nothing new.

## (2) `FL-005` — cause found by the owner: configuration
- **Owner:** *"Yes it was configuration. It was set not go up."* The scorer moves again.
- **`FL-005` → Monitoring**, category → *Control / error code*. Resolved after a clear week with no recurrence and no
  "20 V" message. Exact setting to be recorded from the owner.
- **Correction, stated:** on 2026-10-11 Darius read the split test (no up, down or side) as the shared 20 V supply
  (F9 → K5E → GL1) and sent the owner to fuses and terminals. **Wrong.** A parked or disabled scorer fails every
  movement together, exactly like a dead supply; the ElmoDrive manual's scorer menu (parking position — *"cannot be
  adjusted in this situation"*) was not checked. The F9 facts stay as reference; they were not the cause.
- `troubleshooting-altendorf-f45.md`: new section *Scorer will not move? Check its settings on the screen first*,
  in place, SAME. **Skill `machine-control-fault` amended:** new step 3 *Settings and modes before electrics*, and a
  *Never* line on reading a split test as electrical.
