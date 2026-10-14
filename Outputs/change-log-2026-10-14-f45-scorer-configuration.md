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

## (3) Extractor — LRE16 arrived (`FL-003`)
- **Owner:** LRE16 has arrived; fitting **Saturday 17 Oct**; nobody in the workshop until then (extractor not running).
  `FL-003` updated with the Saturday checklist: swap on K1 at 11.6 A, retighten terminals, star→delta check, three phase
  currents, suction at all three ports, old motor's B/C readings.

## (4) `AWT-0537` — workshop facts delivered to Anna
- **Owner:** *"AWT-0537 - Go ahead."* Facts gathered from the KB (machines and makers' hazards, extraction, rules
  already followed, pre-production check, F-Gas, what does not fit a site-job procedure); **gaps stated, not filled**:
  inductions, authorised users, PPE, first aid, fire points, final checks, waste routes, finishes, lone working, noise
  and airflow readings.
- **Delivered into Anna's Raw/** (`18PkuxAxchaS0rEkgdexw2zOvzoidcJFA`, parent "Anna - AI Construction Assistant",
  checked before writing) as `2026-10-14_Darius-to-Anna_workshop-facts-for-HSE-QC-ENV.md`, id
  `1EBtUPxea_DvybUHVxnIQsNY46uKiaJ6b`, SAME. Own copy in `Outputs/`, id `15b996e79bO7tsWuLhRvp3GIrIuQnNd9B`, SAME.
  Victoria's request was answered on `AWT-0537` itself (In Progress until Minda's answers follow), not a new row.
- Two claims removed before sending because the KB does not support them (a board size; an overload "fitted" on a
  future date).
- **Side finding:** `Wiki/Troubleshooting/troubleshooting-aes-saf-10000.md` is in `Wiki/index.md` and on Drive
  (`1p6fM3mEWB3vcmfmOxtf_spC2w2OMUSkf`) but **not in the git mirror** — to back-fill.
