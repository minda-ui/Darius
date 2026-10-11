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
