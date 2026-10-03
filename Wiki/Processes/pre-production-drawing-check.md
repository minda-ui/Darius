---
title: "Pre-production drawing check — SmartCabinet output reviewed before it goes to the machines"
category: Processes
status: active
sensitive: false
created: 2026-10-03
updated: 2026-10-03
sources:
 - "Session 27 (2026-10-03): the reviews of the 350 METABOX K unit (v1–v9), the 1050 corner unit (v1, v2, v2 regenerated) and the TV shelf unit — `Outputs/change-log-2026-10-03-metabox-side-left-check.md` sections (4)–(30)"
 - "Owner, 2026-10-03: *\"Today, we done great job with creating one extra quality control step. This drawings check before we send them to production. Save it as your new skill\"*"
related:
 - blum-metabox-smartcabinet-input.md
 - blum-legrabox-smartcabinet-input.md
 - blum-clip-top-hinges-smartcabinet-input.md
 - blum-runners-tandem-movento-smartcabinet-input.md
 - blum-aventos-lift-systems-smartcabinet-input.md
 - ../Software/smartcabinet-online-manual.md
 - ../Machinery/vitap-k2-drill-head-tooling.md
---

# Pre-production drawing check

**A quality-control step between SmartCabinet and the machines.** The owner puts a job's exported folder (TpaCAD `.TCN`
programs, `worklist.xmlst`, `.fnm` and, ideally, the cutting-list PDF) into **`Raw/Review folder/`** on Drive
(`1sSySf-DnGafA38Wz8rsjGxzBoAhqxAvE`). Darius decodes every program and checks the parts **against each other and against
the hardware maker's data**. The verdict is ✓ / ✗ / ? for each item. The owner fixes in SmartCabinet, regenerates, and the
check repeats until it is clean.

**Why it exists.** On its first day (2026-10-03) it caught, before any board was cut:

- drawer bottoms 292 × 388 × 10 instead of METABOX K's 281 × 382 × 16;
- an 87 mm drawer back where 103 was needed;
- a door 516 wide where 500 was wanted;
- a shelf split in two with its middle corners unsupported;
- stray tool-182 cuts in single drawer-bottom programs.

It took nine rounds on one unit. Each round was cheap; a wrong batch would not have been.

**It also runs as a Claude skill** in the git mirror: `.claude/skills/pre-production-drawing-check/` (`SKILL.md` and
the decoder `tcn_decode.py`). **This article is the checklist; the skill is how a session runs it.**

## 1. Get the files — all of them, every time

1. **List the job folder; do not filter by date.** *The 2026-10-03 morning check filtered `Raw/` by `modifiedTime` and
   missed a file created that morning.* Record each file's `md5Checksum`.
2. **On a re-review, compare the md5 list with the last round.** Only changed files need decoding again. A removed
   file (e.g. `08-BACK-1B` on the corner unit) is a finding in itself.
3. Download every file, and **check each download's md5 against Drive's**.

## 2. Decode

`tcn_decode.py <folder> [--diff <previous round>]` prints:

- the worklist sizes (L × H × T);
- the `.fnm` part list;
- every bore, profile start and hole-row macro per program and face;
- the cutting-list lines.

The `.TCN` codes it relies on:

| Code | Meaning |
|---|---|
| `W#81` | bore: `#1` X, `#2` Y, `#3` depth, `#1002` Ø, `WO=1` mirrored |
| `W#89` | profile start: `#205` tool, `#40` type |
| `W#1001` | *foro mul* hole row: start, end, pitch, depth, Y, Ø |

**A Cabineo pocket's start point is 7.5 mm (one Ø15 radius) from the circle's centre.** A file ending `B` is the B face;
`SIDE#3`… are edges.

**Three sources must agree on every part's size: the worklist, the program header (`DL/DH/DS`) and the cutting list.**
If one disagrees, that is the first finding.

## 3. The checklist

### a) Sizes and materials
- [ ] Every part on the cutting list has a program, and every program is on the list. Watch for **orphans and missing
      parts** (e.g. a cutting list naming parts that have no `.TCN`).
- [ ] Thickness per material is what the owner expects (carcass 19, drawer parts 16, fronts 19…), and the decor names
      are right.
- [ ] Overall unit size = the customer's size (width, height incl. legs/plinth, depth).

### b) Joints line up between mating parts
- [ ] **Dowels:** each Ø8 hole in one part has its partner in the other. *Checking trick:* positions along a mirrored
      edge **sum to a constant** (corner unit: bottom 107 … 459 ↔ rail 924 … 572, every pair summing to 1031).
- [ ] **Cabineo:** each pocket (Ø15, type 1) meets a Ø5 hole in the mating panel at the same position. Pockets
      **on a visible face** must be intended: **ask**.
- [ ] **Back:** the bores in the sides and bottom agree with each other. A back set forward may be deliberate: on
      2026-10-03 it was a **service void for pipes**. **Ask before calling it a fault.**
- [ ] **Shelves:** supported at **both ends and both corners**. A shelf split at a dummy divider leaves the middle
      unsupported. Check the pin or Cabineo rows match the shelf's slots (e.g. Y 84 / 377 ↔ 83.5 / 376.4).

### c) Hardware against the maker's data (the Blum articles)
- [ ] **Drawers:** base and back sizes against the system's formula. Examples:
      - METABOX K: base **LW − 31 × NL − 2** (or the shop's verified 281 × 382 with the back behind), back **LW − 31 × 103**.
      - LEGRABOX: base **LW − 35 × NL − 10**, back **LW − 38**.
      Runner holes at **37 + the NL's rear hole**, at a height that clears the part below (METABOX: ≥ side height, +2 with
      BLUMOTION).
- [ ] **NL fits the cabinet:** inside depth ≥ NL + 3.
- [ ] **Hinges:** cup **Ø35 × 13**, ~100 from each end, cup edge distance (TB) as set. The mounting-plate holes on the
      side are **on 37 / 32 and level with the cups**: *door edge + gap = side edge*, e.g. side + 19 = door + 2. Enough
      hinges for the door's height and weight. Overlay FA within the ±2 adjustment.
- [ ] **Lift systems / TIP-ON / special hardware:** against the relevant article, or flagged as unchecked.
- [ ] **Legs:** pattern from the CAM table (TD130: 64 × 64, Ø3 × 13); a middle pair where the span exceeds the
      cabinet's max-distance setting; **no extra pair at a dummy divider** unless wanted.

### d) Fronts
- [ ] Widths and heights are what the customer asked for (e.g. door **500**, not 516).
- [ ] Gaps are consistent, and **match neighbouring units**. Compare the top and bottom edges, not the inter-drawer gaps:
      1.6 vs 2.0 is only 0.4 mm at the edge.
- [ ] Fixed/blank fronts are dowelled to parts that exist, and the dowels align.

### e) Machining sanity
- [ ] **Single programs vs nesting:** if both exist, say which to run. Single drawer-bottom files once carried two
      **tool-182, 8 mm-deep cuts running off the panel**, while the nesting had none. **Unexplained cuts → "don't run
      that file".**
- [ ] **Tool numbers present** on profiles. Nesting contours with no tool: **confirm the cutter in TpaCAD's
      simulation**.
- [ ] Every diameter used exists on the K2 head. Check `vitap-k2-drill-head-tooling.md`, **and cite its date**. No Ø15 for
      native Cabineo; Ø10 only vertical.
- [ ] Hole depth < board thickness (no breakthrough on show faces).

### f) Use and safety
- [ ] Tall or narrow units: **wall fixing advised** (anti-tip).
- [ ] Anything heavy, electric (SERVO-DRIVE needs a socket, an electrician's job) or unusual: noted for the owner.

## 4. The verdict — how to report

Three lists, in this order, kept short:

- **✓ Correct**: what was checked and is right, with the key figure.
- **✗ To fix**: what is wrong, **the exact SmartCabinet change that fixes it** (e.g. "reduce space 2 by 16",
  "`cass05_spess=10.50` in the `.SCS` loaded on the METABOX row, then restart"), and which files **not** to run.
- **? Questions**: anything that might be intended. **Never guess intent.** The back void and the outer-face pockets were
  both intended.

A job is **ready** only when the ✗ list is empty and every ? is answered. **Darius does not release a job with an open ✗.**
Darius also never deletes or moves the owner's files in `Raw/Review folder/` unless asked.

## 5. Record

- One **change-log section per round**, with the folder, what changed since the last round (md5), the verdict, and the
  owner's answers.
- **`kb-registers.md` Processed items:** one row per job folder, `partial` until ready.
- Drive first, then git, each verified byte-for-byte.
- **New hardware knowledge** learned in a review goes into the relevant article, not only the change log. *The verified
  METABOX K `.SCS` set went into the METABOX article §7a.*

## 6. SmartCabinet things that bit us (2026-10-03)

- **Drawer-box settings only take effect from the `.SCS` file loaded on the box system's row** (*CAM Tables →
  Drawer Box → Box Config file*), edited in Notepad. **Restart SmartCabinet before reloading.** The values typed in the
  window did not take effect.
- `cass_sot_dy` lifts the base and **shortens the back by the same amount** when the back runs down to the base
  underside (`bCassDIESOT=0` + `FILO=1`).
- **One door per space:** to have a door plus a fixed blank, add a **dummy divider (thickness 0)** to make two spaces.
  **Then check shelves and legs**, because both follow the divider.
- **Legs:** the cabinet's *Legs* panel blue value = **maximum distance between legs**; lowering it adds a middle pair.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-10-03 | Created at the owner's request, from the day's reviews; skill in `.claude/skills/pre-production-drawing-check/` | Session 27 (38) |
