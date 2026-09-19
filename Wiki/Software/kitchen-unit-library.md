---
title: "Kitchen unit library (low-cost range)"
category: Software
status: draft
sensitive: false
created: 2026-09-18
updated: 2026-09-18
sources:
 - "Google Drive folder `Furniture` (1BsTNcHI2OwjDlJdrCgv-x0BwHjas2qU1), listed 2026-09-18"
 - "`AMFA Wall Unit 600 RH/worklist.xmlst` (1uJ3LlrN6yWe9USvPIvJTa50SehARoTFh), decoded 2026-09-18"
 - "`AMFA Wall Unit 600 RH/03-BOTTOM.TCN` (1ygANqYNEfpT7-q7TNkfm-hhllShoZ62m), decoded 2026-09-18"
 - "`300mm Wall unit/worklist.xmlst` (1pBz_N2ty5_0UVuCVSpYx-smioTbD5W3u) and `600mm Wall unit/worklist.xmlst` (1k98zBX7Safi_foFnYsyD5ZznJX2QefXD), decoded and compared 2026-09-18"
 - "Owner (Minda), 2026-09-18: the AMFA unit is the master design for basic kitchen units"
 - "Owner (Minda), 2026-09-19: panels are cut on the F45 and then drilled on the Vitap"
related:
 - ../Software/smartcabinet-and-production-workflow.md
 - ../Processes/tpacad-tool-type-optimizer-ambiguity.md
 - ../Processes/barcode-and-scan-event-system.md
 - ../Machinery/vitap-k2-panel-saw.md
---

# Kitchen unit library (low-cost range)

**Status: started, nothing built.** The owner asked on 2026-09-18 for a library of low-cost kitchen
units, having already made one unit by hand on Drive, and confirmed that **`AMFA Wall Unit 600 RH`
is the master design**. This article records what exists today, what the master actually contains
(read out of the files, not assumed), what has to be decided before a second unit is cut, and the
one library-wide risk that is already visible. It does not create anything: no folder on Drive has
been moved, renamed or added, because the shape of the range is a commercial decision and the filing
is the owner's.

## Key facts

- **The master is `AMFA Wall Unit 600 RH`** (Drive `1HHPym8Y04_s2VUYYwVy89hBQ4boabZxv`, created
  2026-09-16 13:45). Owner's decision, 2026-09-18. Four earlier folders — `300mm`, `400mm`, `500mm`
  and `600mm Wall unit`, all created 2026-09-16 around 10:22 — are **not** the master, and the
  `600mm Wall unit` folder is a second, different 600 mm unit.
- **The master's carcase is 19 mm throughout** — sides, top, bottom, shelves, **back** and **door**
  all `THICKNESS = 19.0`. A 19 mm back and a 19 mm door are a material choice with a direct cost
  consequence for a range whose selling point is price; recorded here as a fact, not a criticism.
- **The unit's nominal size is not stated in any file.** It is derived below from the part sizes, and
  the derivation is shown so it can be checked rather than believed.
- **Shelf depth disagrees across the three units built so far** — 255, 256 and 266 mm for the same
  300 mm-deep carcase. A real inconsistency, found by comparing the three cutting lists, and worth
  settling before it is copied into a range.
- **Every hole in the master exports with no tool specified.** This is the same condition behind the
  live TpaCAD "Tool for this working not found" fault (Task **T016**) — see the risk section. It is
  the one finding here that could stop the whole library at the machine.

## What is on Drive today

The `Furniture` folder sits at the root of the owner's Drive (not inside this KB's folder tree) and
holds seven subfolders. Listed 2026-09-18:

| Folder | Created | Contents | Read as |
|---|---|---|---|
| `AMFA Wall Unit 600 RH` | 16 Sep 13:45 | 11 `.TCN` + `.fnm` + `worklist.xmlst` | **the master** |
| `600mm Wall unit` | 16 Sep 10:23 | 8 `.TCN` + `.fnm` + `worklist.xmlst` | earlier attempt |
| `500mm Wall unit` | 16 Sep 10:22 | 8 `.TCN` + `.fnm` + `worklist.xmlst` | earlier attempt |
| `400mm Wall unit` | 16 Sep 10:22 | 8 `.TCN` + `.fnm` + `worklist.xmlst` | earlier attempt |
| `300mm Wall unit` | 16 Sep 10:21 | 8 `.TCN` + `.fnm` + `worklist.xmlst` | earlier attempt |
| `ANVAR_KITCHEN_V2` | 15 Sep 10:22 | not opened | customer job |
| `ANVAR_KITCHEN_V3` | 16 Sep 08:47 | not opened | customer job |

**The two `ANVAR_KITCHEN_*` folders were deliberately not opened.** A customer name on a folder is
enough to treat the contents as client data, and this KB's rule is **cite, never copy client data**.
They are listed here because their presence in the same folder as the library units is itself the
problem described under "What has to be decided".

## What the master contains

Read from `worklist.xmlst`, which is the unit's own cutting list — a UTF-16 XML file with one `Row`
per part carrying `LENGTH`, `HEIGHT`, `THICKNESS`, `MIRROR` and `REPETITIONS`. All eleven rows have
`MIRROR = 0` and `REPETITIONS = 1`.

| # | File | Length | Height | Thickness |
|---|---|---|---|---|
| 1 | `01-SIDE-LEFT.TCN` | 862.0 | 300.0 | 19.0 |
| 2 | `02-SIDE-RIGHT.TCN` | 862.0 | 300.0 | 19.0 |
| 3 | `03-BOTTOM.TCN` | 600.0 | 300.0 | 19.0 |
| 4 | `04-UP.TCN` | 600.0 | 300.0 | 19.0 |
| 5 | `05-SHELF-1.TCN` | 561.0 | 255.0 | 19.0 |
| 6 | `06-SHELF-2.TCN` | 561.0 | 255.0 | 19.0 |
| 7 | `07-BACK-1.TCN` | 862.0 | 562.0 | 19.0 |
| 8 | `07-BACK-1B.TCN` | 862.0 | 562.0 | 19.0 |
| 9 | `08-DOOR-1.TCN` | 896.0 | 597.0 | 19.0 |
| 10 | `09-NESTING01-SP19-W1100.TCN` | 2800.0 | 2070.0 | 19.0 |
| 11 | `10-NESTING02-SP19-U963.TCN` | 2800.0 | 2070.0 | 19.0 |

`LENGTH` and `HEIGHT` are the blank's X and Y **as it lies on the machine**, not "height" and "width"
in the assembled unit. Rows 10 and 11 are not parts: they are 2800 × 2070 nested sheets, the standard
board size, and they are job output rather than unit definition.

**The production route, confirmed by the owner 2026-09-19: panels are cut on the F45, then drilled on
the Vitap.** Two things follow. It **confirms that the nesting files are saw-side artefacts**, produced
per job against the boards actually in stock — which is the argument for keeping them out of a library
unit, now evidenced rather than asserted. And it explains why the 2800 × 2070 sheet is no problem
despite exceeding the Vitap's 1250 mm width: the Vitap only ever sees single panels.

### The nominal size, derived

Nothing in the files states the finished unit size. This arithmetic gives it, and every line is
checkable against the table above:

- Side length 862 = **900 − (2 × 19)** → the sides sit **between** top and bottom, so overall height **900**.
- Top and bottom length 600 → overall width **600**; back width 562 = 600 − (2 × 19) confirms it.
- Back height 862 = 900 − (2 × 19) → the back is housed **inside all four** panels, not rebated or overlaid.
- All panels 300 deep → carcase depth **300**.
- Shelves 561 × 255: 561 = 562 − 1 mm running clearance; 255 leaves 45 mm at the back (19 back + 26 set-back).
- Door 896 × 597 against a 900 × 600 face → **4 mm** on height and **3 mm** on width as gaps.

**So: a 600 wide × 900 high × 300 deep wall unit, 19 mm throughout, two shelves, one overlay door,
right-hand hung.** *This is my arithmetic, not a figure read off a document* — if the owner's intended
nominal is anything other than 600 × 900 × 300, the derivation is wrong and everything below moves.

### Corroborated against the two earlier units

The `300mm` and `600mm Wall unit` worklists were decoded the same way and compared byte for byte.
They are **genuinely different files** — same length, same structure, eight cell values differing on
six rows — so the earlier folders are a real attempt at a family, not copies.

| Part | 300mm unit | 600mm unit | AMFA master |
|---|---|---|---|
| `01-SIDE-LEFT` | 862.0 × 300.0 | 862.0 × 300.0 | 862.0 × 300.0 |
| `02-SIDE-RIGHT` | 862.0 × 300.0 | 862.0 × 300.0 | 862.0 × 300.0 |
| `03-BOTTOM` | 300.0 × 300.0 | 600.0 × 300.0 | 600.0 × 300.0 |
| `04-UP` | 300.0 × 300.0 | 600.0 × 300.0 | 600.0 × 300.0 |
| `05-SHELF-1` | 261.0 × **266.0** | 561.0 × **256.0** | 561.0 × **255.0** |
| `06-SHELF-2` | 261.0 × **266.0** | 561.0 × **256.0** | 561.0 × **255.0** |
| `07-BACK-1` | 862.0 × 262.0 | 862.0 × 562.0 | 862.0 × 562.0 |
| `07-BACK-1B` | — | — | 862.0 × 562.0 |
| `08-DOOR-1` | 896.0 × 297.0 | 896.0 × 597.0 | 896.0 × 597.0 |

Everything is 19 mm and every row is `MIRROR = 0`, `REPETITIONS = 1` in all three.

**This corroborates the derivation above.** Across three units the same rules hold: bottom length =
nominal width; back = nominal width − 38 (two 19 mm sides); shelf = back − 1 mm; door = nominal
width − 3 mm and 896 high against a 900 nominal. The sides never change, because a wall unit's height
and depth do not change with its width. So the family is **600 or 300 wide × 900 high × 300 deep**,
and the master is the 600.

**And it turns up one thing that does not hold.** Shelf depth is **266.0** on the 300 mm unit,
**256.0** on the 600 mm unit and **255.0** on the master — three values for what should be one
number, since all three carcases are 300 deep and a shelf's depth has nothing to do with the unit's
width. One of them is right and two are wrong, or they encode a set-back that changed between
16 September 10:22 and 13:45 and was never written down. **This is exactly the kind of drift a
library exists to prevent**, and it is already present in four folders made in one morning.

### Two backs, not one

`07-BACK-1` and `07-BACK-1B` are the **same blank** (862 × 562 × 19) and both are listed once in the
worklist, so both get cut. Their programs differ substantially in size — 60,458 bytes against 11,994 —
so they are not duplicates. **Neither earlier unit has a `07-BACK-1B` at all**, so the second back is
something the master gained, not something the family always had. Either the unit genuinely takes two
backs, or one is an alternative that should not be in the cut list. **Open — not guessed.**

## The one risk that affects the whole library

`03-BOTTOM.TCN` was decoded in full. Its seven holes all take the same form:

```
W#81{ ::WTp #1002=5 #1=11.9 #2=230.0 #3=-12.0 #8015=0 #201=1 #203=1 #1001=0 }W
```

Reading `#1002` as the hole diameter (5 mm) and `#1001` as the tool number (**unset**) — *both of
those readings are mine, from the shape of the data, and are not documented in the TpaCAD manual
extract this KB holds* — **SmartCABINET is exporting holes with no tool named, to be resolved by
diameter at the machine.** That is precisely the condition that produces the live "Tool for this
working not found" fault on Blind bore drill operations (Task **T016**).

If that reading is right, **T016 is not a one-off on one job.** Every unit in the library will export
the same way, so a Ø5 that does not resolve in the Vitap's CN Tools catalog fails every unit
identically. It follows that **T016 should be closed before the library is populated, not after** —
fixing one catalog entry once is cheap; re-cutting a range is not.

*Naming collision worth stating once:* `#1002` here is a TpaCAD **parameter index**, nothing to do
with the shop's **tool ID 1002** (the 12 mm cutter) in the 2026-09-18 hinge-cup question. Same four
digits, unrelated things.

## What is worth keeping

The part-file convention in the master is the strongest thing here and should survive into whatever
structure is chosen:

- **Numbered, role-named part files** — `01-SIDE-LEFT` … `08-DOOR-1`. Sorts in assembly order, reads
  without opening, and survives being copied into a job folder.
- **A `worklist.xmlst` per unit** — the cutting list in one machine-readable file. This is what makes
  a folder a *unit* rather than a pile of programs, and it is what any future tracker should read
  rather than re-deriving sizes from each `.TCN`.
- **A `.fnm` naming the unit** — a plain-text list of the unit's `.TCN` files, named after the unit.

## What has to be decided before anything is created

These are the owner's calls, not Darius's, and the library should not be built on a guess about any
of them.

1. **The range.** Which unit types (wall, base, tall), which widths, and whether the earlier
   `300`/`400`/`500`/`600mm Wall unit` folders are to be regenerated from the master or kept.
2. **"Low cost" — a name or a specification?** If it denotes a defined carcase spec (board grade,
   back thickness, edging, hinge and fixing type), that spec belongs in this article and every unit
   is checked against it. If it is just a range name, say so and nothing further is needed.
3. **Hand.** The master is `RH`. If hand is part of the unit's identity it goes in the unit code; if
   a unit is mirrored at job time (`MIRROR` is a column in the worklist and is `0` throughout the
   master), it does not.
4. **Where the library lives.** Library units and customer jobs currently share one folder. A library
   unit that is edited for a job stops being a library unit. Separating them is the single change with
   the most value and the least cost.

## Proposed structure

Offered for approval; **not created.**

```
Furniture/
├── Library/                      ← masters. Copied out, never edited in place.
│   ├── W600-RH/                  ← 01-… 08-…, worklist.xmlst, .fnm, unit.md
│   ├── W500-RH/
│   └── …
└── Jobs/                         ← one folder per customer job, copied from Library
    ├── ANVAR_KITCHEN_V2/
    └── ANVAR_KITCHEN_V3/
```

**Unit code:** type letter + width, plus hand only where a unit has one — `W600-RH` (wall, 600 wide,
right hand), `B800` (base, 800 wide), `T600` (tall). Height and depth stay out of the code while the
range has one of each; if a second height appears, the code becomes `W600-900-RH` and the earlier
codes are **not** retro-fitted, the same rule the `FA` asset codes follow.

**Nesting files do not belong in a library unit.** `09-NESTING01-SP19-W1100` and
`10-NESTING02-SP19-U963` are the output of optimising *this* cut against *these* boards. They are job
artefacts; a library unit holds parts, and nesting is re-run per job. **The owner's confirmation that
cutting happens on the F45 and drilling on the Vitap settles this**: the nesting belongs to the saw
stage of a job, not to the definition of a unit. (`SP19` reads as 19 mm
thickness and `W1100`/`U963` as material codes — *inference from the filename, not confirmed*.)

**One `unit.md` per library unit**, holding what no `.TCN` records: nominal W × H × D, the cutting
list, board and edging spec, hardware (hinge type, shelf support, fixings), hand, and which master it
was derived from. Without it a library unit cannot be quoted, costed or checked — only cut.

## Open questions

- Is the derived nominal **600 × 900 × 300** right? Everything above rests on it.
- **Two backs** (`07-BACK-1`, `07-BACK-1B`) on one blank — deliberate, or a stray file in the cut list?
- **Which shelf depth is right — 255, 256 or 266?** Three units, three answers, all 300 mm deep. This
  one should be settled before anything is copied, because a library propagates whichever value it is
  built on.
- Are the four `300`–`600mm Wall unit` folders to be kept, regenerated from the master, or archived?
  They predate the master by three hours, differ from it in shelf depth, lack the second back and the
  nesting files, and nothing records what changed between them.
- Is the **19 mm back and 19 mm door** intended for a low-cost range, or inherited from the master
  being drawn as a one-off?
- Does SmartCABINET generate a unit's parts **parametrically** from a width? If it does, the library
  is a list of parameters and this whole folder question is smaller than it looks. Nothing seen so far
  answers it, and it bears on the SmartCABINET-ERP question already open in `CLAUDE.md` §7.
- **T016 first.** See the risk section — the library should not be populated over an unresolved
  tool-resolution fault.
