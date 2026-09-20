---
title: "Batch production from the unit library (proposed)"
category: Processes
status: draft
sensitive: false
created: 2026-09-20
updated: 2026-09-20
sources:
 - "Owner (Minda), 2026-09-20: *\"Mostly side elements are same through all units, it's only up, bottom and back which are specific to width\"*"
 - "`AMFA Wall Unit 300 LH 900/01-SIDE-LEFT.TCN` (1sYdx4InTyfuV2rJKPOvhkUtlLgm6UqQo) and `AMFA Wall Unit 500 LH 900 high/01-SIDE-LEFT.TCN` (1Q3FvNhVKPwhG87rih2MVToHsgvW_eqOc), downloaded as exact bytes and diffed 2026-09-20 - identical, sha256 ac79530d4aa8ba14..."
 - "`AMFA Wall Unit 300 RH 900/02-SIDE-RIGHT.TCN` (1C1oOYeN-tt6dyx5QcGPLUpMVcAOe5S-l), downloaded and diffed against the LH left side 2026-09-20"
 - "`AMFA Wall Unit 300 LH/03-BOTTOM.TCN` (1wU6ema5eXeDSEEtvbm0kHsge0Cg7u32C), decoded 2026-09-20"
 - "`Wiki/Processes/panel-production-route.md` - the serial line the proposal has to live inside"
related:
 - ../Software/kitchen-unit-library.md
 - ../Processes/panel-production-route.md
---

# Batch production from the unit library (proposed)

**Status: measured findings, proposed method. Nothing adopted, nothing changed on Drive.** The owner
observed on 2026-09-20 that *"mostly side elements are same through all units, it's only up, bottom and
back which are specific to width"*, and asked whether that helps the workshop cope with a bigger load.
This article records **what was measured rather than assumed**, and sets out the method the measurement
makes possible. **The decisions in it are the owner's**, and several depend on checks that can only be
made at the machine.

## Key facts

- **The side is the only width-invariant part, and it is invariant all the way down to the byte.**
  `01-SIDE-LEFT.TCN` from `AMFA Wall Unit 300 LH 900` and from `AMFA Wall Unit 500 LH 900 high` are
  **byte-identical** — same sha256, 20,400 bytes each. Not merely the same blank: the same program,
  same holes, same pockets.
- **The observation understated itself slightly.** Shelves and the door are width-specific too. Of the
  nine parts, **two are constant and seven vary**.
- **The constant part is the most machined one.** The sides carry the Ø10 row, the Ø5 rows and every
  routed pocket; the seven that vary are comparatively plain panels. *The complicated part is the one
  that does not change* — which is the condition that makes a stock/order split possible at all.
- **Hand is a mirror, not a redesign.** `LH/01-SIDE-LEFT` and `RH/02-SIDE-RIGHT` are the same part
  mirrored about the panel's length centre, and differ by **one character** (20,400 vs 20,402 bytes).
- **Two blanks cover every side in the library**: 862 × 300 × 19 (900 high) and 682 × 300 × 19 (720 high).
- **Routing carries a tool; drilling does not.** Every routed setup reads `#205=1002`; every drilled
  hole reads `#1001=0`. *That reading of the parameter indices is mine and is not documented in the
  TpaCAD extract this KB holds* — but it is consistent across three files, and if it is right then
  **T016 is a drilling-only fault**.

## What was measured

### Width does not touch the side

Two units, same height, different width:

| | `AMFA Wall Unit 300 LH 900` | `AMFA Wall Unit 500 LH 900 high` |
|---|---|---|
| `01-SIDE-LEFT.TCN` | 20,400 B | 20,400 B |
| sha256 | `ac79530d4aa8ba14…` | `ac79530d4aa8ba14…` |

**Byte-identical.** Every coordinate in the file is referenced to the side's own 862 × 300 face, so
nothing in it can depend on how wide the carcase is. A size match alone would prove nothing (§3); this
is a `diff` of the decoded bytes, and it came back empty.

### What varies, and with what

| Part | Varies with | 300 wide | 500 wide |
|---|---|---|---|
| `01-SIDE-LEFT`, `02-SIDE-RIGHT` | **height only** | 862 × 300 | 862 × 300 |
| `03-BOTTOM`, `04-UP` | width | 300 × 300 | 500 × 300 |
| `05-SHELF-1`, `06-SHELF-2` | width | 261 × 255 | 461 × 255 |
| `07-BACK-1`, `07-BACK-1B` | width | 862 × 262 | 862 × 462 |
| `08-DOOR-1` | width | 896 × 297 | 896 × 497 |

**Two constant, seven variable.**

### Hand is a mirror about the panel centre

`AMFA Wall Unit 300 LH`'s left side against `AMFA Wall Unit 300 RH`'s right side — same 172 lines, same
operations, every X coordinate reflected about 431 (half of 862):

| Feature | LH left side | RH right side | check |
|---|---|---|---|
| Ø10 row | X = 71, 103, 135 | X = 791, 759, 727 | 862 − 71 = 791 ✓ |
| fitting macro 1 | 676.2 → 484.2 | 185.8 → 377.8 | 862 − 676.2 = 185.8 ✓ |
| fitting macro 2 | 382.6 → 190.6 | 479.4 → 671.4 | 862 − 382.6 = 479.4 ✓ |
| Ø5 row | X = 50, 304, 558, 812 | X = 50, 304, 558, 812 | already symmetric |

The Ø5 row is **self-symmetric** (862 − 50 = 812, 862 − 304 = 558), so it mirrors onto itself and does
not move. The two-byte size difference is entirely `71.0` becoming `791.0`.

**So per height there are four side programs** — left and right, each in two hands — but only **two
geometries**, each with its mirror.

### The mirror is being baked in at export

Every `worklist.xmlst` decoded carries `MIRROR = 0` on every row, while SmartCABINET emits
**pre-mirrored** `.TCN` files for the opposite hand. *The worklist format has a `MIRROR` column and it
is never used.* If TpaCAD honours it, the four side programs per height collapse to two.
**Unverified — this is the first check to make**, and it is a ten-minute test at the machine.

## What the measurement makes possible

### The shape of the opportunity

A unit's cost is not spread evenly across its nine parts. The two that never change carry almost all the
machining; the seven that change are rectangles with edge features. That means the expensive half of
every unit in the range **can be made before anybody orders it**, and the cheap half made to order.

That is the classic way a serial shop absorbs a load spike without buying a machine — and this shop is a
serial line (`../Processes/panel-production-route.md`: one saw, one bander, one borer, all fed by
`FA2306`). **It does not add capacity. It removes changeover**, which on a job shop is usually the
larger loss.

### Move 1 — make the side a stock item

Two blanks cover the whole library. Nesting them on the standard 2800 × 2070 sheet:

| Blank | Per sheet | = units' worth |
|---|---|---|
| 862 × 300 (900 high) | **18** | 9 |
| 682 × 300 (720 high) | **24** | 12 |

*My arithmetic, 4 mm kerf included, before edge trim; both figures hold in either orientation for the
862 and in the better orientation for the 682.*

**One sheet of sides is nine finished units' worth of the hard part.** Cut the sheet, drill the batch,
edge them, and they sit as stock. A job then pulls sides off the shelf and cuts seven simple panels.

### Move 2 — batch by part type, not by unit

This is the move that costs nothing and changes the most, because **it needs no change to any file** —
only to the order of work and to how the cutting list is grouped.

| 12-unit kitchen, 4 distinct widths | program loads |
|---|---|
| Unit at a time (today) | 12 × 9 = **108** |
| Batched by part type | 4 sides + (4 widths × 7 parts) = **32** |

*Both figures are counts of program loads, not machine hours — the cutting time is unchanged.* The
saving is in setup, program changeover and the operator decision between each one.

**What it costs:** somewhere to put work in progress, and labels on it. That is barcode **Phase 1**,
already designed in `../Processes/barcode-and-scan-event-system.md` and waiting on a scanner (T022).
Batching without labelling turns a stack of 24 near-identical panels into a sorting problem.

### Move 3 — close T016 before batching, not after

Every drilled hole in the library exports `#1002=<diameter> … #1001=0` — diameter given, no tool named.
Batching multiplies the consequence: a tool that does not resolve stops **24 sides**, not two. The fix is
two steps at the Vitap (`../Processes/tpacad-blind-bore-tool-id-fix.md`), done once.

**And the systemic half matters more under batching**: getting the post-processor to emit a Tool ID, so
step two is not repeated by hand on every operation. A batch run is the worst place to be doing manual
per-operation edits.

*If the `#205=1002` reading above is right, only the drilling is affected and the routed pockets solve
cleanly — which would explain why the pockets have never been the thing that failed.*

### Move 4 — settle the height question, because it is now an inventory question

The sides are constant **within a height**. Two height families means:

- two side blanks to hold rather than one,
- half the batch size on each,
- and a naming scheme where an unsuffixed folder means 720 in seven places and 900 in the master.

If both heights are commercial, that is simply the cost of the range. But the naming fix stops being
cosmetic the moment sides are held as stock: **picking the wrong blank wastes a sheet, not a panel.**

### Move 5 — the parametric question decides whether the range can grow

Sixteen folders that differ only by width and height are either sixteen hand-built units or one
parametric definition exported sixteen times. If SmartCABINET generates parts from a width, **adding a
width costs nothing** and the library is a parameter list. If it does not, every new width is seven
files made by hand. Nothing seen so far answers it, and it decides how far this method scales.

## What this does not do, and what it risks

- **It adds no capacity.** One saw, one bander, one borer, in series. This attacks changeover and lets
  the shop pre-build; it does not raise the ceiling.
- **Machined stock is a bet on the design.** This KB has already recorded one design move — the
  back-panel step-back went 15 → 16 mm. Sides made to a superseded spec are scrap, and the side is the
  expensive part. **Buffer, do not stockpile**: a sheet or two, not a pallet.
- **Batch errors scale.** A wrong setup ruins 24 parts rather than 2, so a first-off check stops being
  optional. That is a process discipline the shop does not currently have written down.
- **WIP storage becomes the constraint** once parts stop moving unit-by-unit.

## Suggested order

1. **Check `MIRROR`** at the machine — does the Vitap apply it from the worklist? Ten minutes, and it
   halves the side programs.
2. **Close T016**, both halves.
3. **Batch by part type on the next real kitchen** — no file changes, no stock commitment, and it is
   the move with the best ratio of saving to risk. Measure the changeover time saved.
4. **Only then hold side stock**, one sheet at a time, once the spec has been stable for a job or two.
5. **Answer the parametric question** before adding any more widths.

## Open questions

- **Does the Vitap apply `MIRROR` from the worklist?** Decides whether there are two or four side
  programs per height.
- **Are `05-SHELF-1` and `06-SHELF-2` the same program?** Their file sizes match, which proves nothing
  (§3). If they are identical the batched program-load count drops further.
- **Is `#205` the tool field on a routed setup?** If so, T016 is drilling-only. Checkable in the same
  visit as the T016 fix.
- **What are the three Ø10 holes at 32 mm centres?** Recorded as measured; *this KB does not assert what
  hardware they are for.*
- **Both heights, or one?** A commercial decision with a direct inventory consequence.
- **Does SmartCABINET generate parts parametrically from a width?** See Move 5.
