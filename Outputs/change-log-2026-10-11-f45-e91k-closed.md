# Change log — 2026-10-11 — F45 `E91K` closed; Victoria's HSE/QC/ENV request received

Session 33.

## (1) Session start — Hub, Raw/, workshop state
- **Raw/** (direct listing): **`2026-10-10_Victoria-to-Darius_workshop-hazards-input-for-HSE-QC-ENV.md`**
  (`1DdShP90TbgV6pGSDSnv9Cb7ygMM7cXuJ`, 1,030 B), new last night — Hub **`AWT-0537`** (new, Darius): facts for Anna's
  HSE, Quality and Environmental procedures, which now cover the workshop (owner, 10/10). Not yet started.
- **Hub, open rows assigned to Darius:** `AWT-0089`, `AWT-0127`, `AWT-0194`, `AWT-0225` (Blocked), **`AWT-0537`**.
- **Fault Log:** `FL-003` In Progress (LRE16 awaited), `FL-004` Monitoring. **Maintenance Schedule:** nothing Red/Yellow.
- **Git:** nothing new on `main`.

## (2) F45 `E91K` — `FL-004` closed Resolved
- **Owner:** *"No error for last week."* A week clear since the 2026-10-01 clean of the yellow START, with extraction
  back to full suction from 2026-10-10. **`FL-004` → Resolved**, Date Resolved 2026-10-11 (the fix itself 10-01); if it
  returns, reopen `FL-004` and see `MT-029`.
- `Wiki/Troubleshooting/troubleshooting-altendorf-f45.md`: outcome line + Changes row (8,017 → **8,378 B**), in place
  on `15GhXBr63eyV5CUd9GyJ5AKLPoVF4nOo5`, SAME.

## (3) F45 scorer will not raise; intermittent "20 V" error — `FL-005` opened
- **Owner:** the scorer won't go up; the display sometimes shows a "20 V" error; no screenshot yet.
- **Lead, not a diagnosis:** ElmoDrive **E40 = 20 VAC control voltage missing → fuse F9** (E41 = 24 VAC → F8). Whether
  the scorer raise runs off that supply is **not in the KB** (schematic sheets 9–12, 19–24 unread). One fault or two: open.
- **Fault Log `FL-005`** (row `6683835796948868`, Open): photo of the screen; what the scorer does; F9/F8 checked
  isolated, like-for-like only; blow out the scorer button; electrician/Altendorf if it recurs. Never bridge a fuse.

## (4) Where F9 is, and what it feeds — `FL-005` narrowed
- **Owner:** *"Do you have position of F9 fuse?"* Not in the KB; searched the F45 manual scans. **Found Fig. 5-34
  "Circuit diagram" (p.77, `F45 part 3.pdf` PDF page 2) and the device legend (p.78, `F45 part 4.pdf` PDF page 24).**
- **F9 is on the transformer's 20 V tap and feeds `K5E` → `GL1` rectifier → the scorer height and side drives.** So the
  scorer not rising and E40 are **one circuit**. `FL-005` probable cause rewritten accordingly.
- **Physical position of F9: not in any document held** — only "control fuses (secondary) F7–F9" in the cabinet. Owner to
  find it by label and photograph it.
- `troubleshooting-altendorf-f45.md`: new section + E40 row pointer + Changes row, in place, SAME.
- *Lesson candidate:* the scans' page order is shuffled across parts (p.75–77 sit at the start of part 3, p.78 at the end
  of part 4) — search all parts by printed page number, not by part.

## (5) Owner's cabinet photos — F9 located
- **RH cabinet:** `T1` transformer top; right of it `K5E`, then fuse terminals **`F9` `F8` `F7` `F11`** (F9 first, next to
  `K5E`); `GL1` below right. `T1` plate: **20 V 6.0 A → 4.0 AT** (24 V → 2.0 AT, 18 V → 6.3 AT). F10 not fitted.
- **Hazards recorded:** mains terminals live with the main switch off; KEB inverters 5-minute capacitor discharge.
- **Second photo:** ElmoDrive board in the other cabinet, LEDs green, **sawdust on the cabinet floor**.
- Wiki section extended, `FL-005` updated. Photos not filed (chat only).
