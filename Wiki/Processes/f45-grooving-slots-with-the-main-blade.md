---
title: "F45 — cutting a slot (groove) wider than the blade with the Grooves function"
category: Processes
status: active
sensitive: false
created: 2026-10-04
updated: 2026-10-04
sources:
 - "ElmoDrive control-unit manual, doc 0000010077-001-2020 GB, §1.8.1 Applications — Grooves, pp. 40–41 (`Raw/F45 part 8.pdf` PDF p. 24; `Raw/F45 part 7.pdf` PDF p. 21)"
 - "F45 operating manual, doc 0000010074-011-2023 GB: Operating — *Concealed cutting, grooving* (p. 103); Safety — grooving with milling tools; Product description — Tools and Terms (pp. 22–23)"
 - "First use, 2026-10-04: a 16 × 9 mm slot for an LED strip in a shelf, cut by the owner with Darius following on chat; the owner's photo of the Grooves screen; first cut measured 3.2 mm; result *\"All good!\"*"
related:
 - ../Machinery/altendorf-f45-panel-saw.md
---

# F45 — cutting a slot wider than the blade (Grooves function)

**For:** a slot or housing wider than the saw blade, part-way into a panel. For example, a recess for an LED
strip in a shelf. The F45's control plans the overlapping passes of the **main saw blade** and moves the rip
fence for each one.

**Why the main blade and not a groove cutter.** Our F45 is the **two-way tilt** version, and the manual limits
groove milling tools on those machines to **5 mm wide**. Anything wider is done with this function.

## 1. Where it is

ElmoDrive: **Main Menu → Application Technology → Grooves** (screen title *Grooving/Concealed Cuts*).

## 2. The screen

| Field (icon) | What it is | 2026-10-04 LED slot |
|---|---|---|
| Blade height (arrow up from the table) | **Groove depth** | **9.0** |
| Blade thickness (blade between two arrows) | **Real kerf of the fitted blade** | **3.2** (measured) |
| 1st box under the drawing | **Gap between grooves** (only matters with 2 or more) | 0.0 |
| 2nd box | **Groove width** | **16.0** |
| 3rd box | **Start**: rip fence to the near edge of the first groove | **10.0** |
| "n x" above the drawing | **Number of grooves** | **1** |
| Top right | Current rip-fence position, and *Cut n of N / Groove n of N* | 10.0, Cut 1 of 6 |

**What the gap field means is my reading of the manual's example** (2 grooves, width 5.0, gap 50.0, start
310.0, blade 3.2). It finishes at 366.8 = 310 + 5 + 50 + 5 − 3.2, which only works if the field is the gap
*between* grooves, not the distance from one groove's start to the next. **Check it with a dry run before
the first job with two or more grooves.**

**Number of cuts.** The control picks it, with overlap. 16 mm with a 3.2 blade gave **6 cuts** (about 2.56 mm
steps); 5 would only just meet. **The values stay saved when the machine is switched off.**

## 3. Method

1. **Fit and check the blade. Enter its real thickness.** The 3.2 on the screen came from the manual's
   example and happened to be right for our blade. **Measure the first cut's width**; that is the kerf. If the
   field is wrong, the slot comes out wrong by the difference (a 4.4 blade entered as 3.2 makes a 16 mm slot
   17.2 wide). Cut 1 is not affected, so correct the field before cut 2.
2. **The slot is cut in the face lying on the table.** The blade comes up from below.
3. **Scorer off** (or lowered). A score line can't match a wide slot. *This is Darius's advice; the manual
   doesn't say. It was off on 2026-10-04 and the result was good.*
4. **Riving knife stays fitted**: for a part-depth cut it is the rear guard (manual, *Concealed cutting,
   grooving*).
5. **For each cut:** pull the sliding table back → press yellow **Start** → wait for the fence to stop (screen
   shows *Cut n of N*) → shelf against the rip fence, **always the same edge** → push it through on the sliding
   table, holding it down. **Never press Start with the workpiece touching the fence or blade.**
6. **Back** returns to cut 1. Re-cutting a pass already done does no harm.
7. **Check the first cut** (width = kerf, depth = setting), **then the finished slot** with the part that goes
   in it.

**Narrow pieces, cut across:** use the **crosscut fence** (manual note).

## 4. Before cutting real parts

- **Test on an offcut** with the strip or profile in hand. A flush aluminium profile may want 0.2–0.5 mm extra
  width and depth for glue. The 2026-10-04 slot was cut to the strip's nominal 16 × 9 and fitted.
- **Board left under the slot:** 18 mm board − 9 mm slot = 9 mm. Fine for a shelf on pins. **Keep slots clear
  of shelf-pin and Cabineo positions.**

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-10-04 | Created after the first use of the Grooves function (16 × 9 LED slot, 6 cuts, 3.2 blade); owner: *"Save it for future"* | `change-log-2026-10-04-f45-grooving-led-slot.md` (1) |
