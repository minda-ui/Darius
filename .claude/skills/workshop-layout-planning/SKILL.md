---
name: workshop-layout-planning
description: Plan or redraw the workshop floor layout (Units 30/31) — where machines, panel racks, offcut storage, assembly, extraction and services go. Use when the owner says "plan the workshop", "where should the … go", "draw it", "move the F45 / extractor / rack", sends a floor plan, or marks areas on a plan screenshot. Draws scaled drafts on the plan and keeps one plan document with every decision.
---

# Workshop layout planning

Adopted at the 2026-10-28 good night, after a day that went from the plans to draft v0.5. The working document is
`Outputs/2026-10-28-workshop-layout-plan.md` (Drive `1mTiTZr-6xvtETHErZrZcwxSK0Xe2H-eo`) — **read it first; it holds the
current frame, decisions, drafts and open checks.** Change log of that day: `Outputs/change-log-2026-10-28-workshop-plan.md`.

## Steps
1. **Phase first.** Phase 1 = the layout as it stands (confirmed by the owner); phase 2 = the new layout. Don't draw the
   new before the existing is confirmed.
2. **Calibrate the drawing, never trust its stated scale.** `pdftocairo -svg plan.pdf plan.svg`, then
   `python3 -I .claude/skills/workshop-layout-planning/pdf_dims.py plan.svg`: written value (mm) ÷ dimension line (pt)
   = mm/pt. GF_30 says 1:100 (35.3 mm/pt) but measures 36.95–38.0 — use **37.5 ± 5 %**.
3. **One frame for everything.** Origin and axes from wall segments (the script lists them). Current frame (GF_30):
   origin = Unit 30 bay bottom-right inside corner (759.4, 824.6) pt; x along the bottom wall (−0.866, −0.5006);
   y away from it (0.5005, −0.866). Positions are mm in that frame; the plan's table lists every item's x/y.
4. **Owner's marks → mm.** A mark on a screenshot: screenshot px → PDF pt (× page width pt / image width px) → frame
   (inverse of step 3). Say which positions are traced (rougher) and which are measured.
5. **Draw** a new numbered draft with `draft_example_v05.py` as the pattern (PIL over a 100-dpi render): zones, machines
   with footprint + clearance, aisles, crane reach, flow arrows, title with version and accuracy. Look at the PNG before
   sending. **Never overwrite an earlier draft**; mark it superseded in the plan.
6. **Check every draft against:** manual footprints and clearances (Vitap ≥ 1,000 all round; F4 ≥ 500 and panel-length
   in/out-feed; F45 working area; extractor service space); clear forklift aisle and fire routes; one-way board flow;
   short duct runs; things the owner said are not workshop (the tools/construction strip).
7. **Record** each decision in the plan's decisions table with the owner's words; publish in place (`chk.sh`), log,
   commit, push. Hand the draft over with what changed, what was assumed, and 2–4 checks.

## Known facts that shaped it (owner, 28/10)
Forklift is **diesel — rack loading only**; one rack bay 3,000 × 2,270 × 3.6 m loaded from the short side; entry by the
roller shutter then the **2.4 m doors** between meeting room and canteen; planning height 3.6 m; vacuum lifter rack →
F45 only. **Planning only — no quotes or drafts to suppliers until the owner says** (§6a).
