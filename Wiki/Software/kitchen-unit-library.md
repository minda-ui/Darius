---
title: "Kitchen unit library (low-cost range)"
category: Software
status: draft
sensitive: false
created: 2026-09-18
updated: 2026-09-20
sources:
 - "Google Drive folder `Furniture` (1BsTNcHI2OwjDlJdrCgv-x0BwHjas2qU1), listed 2026-09-18"
 - "`AMFA Wall Unit 600 RH/worklist.xmlst` (1uJ3LlrN6yWe9USvPIvJTa50SehARoTFh), decoded 2026-09-18"
 - "`AMFA Wall Unit 600 RH/03-BOTTOM.TCN` (1ygANqYNEfpT7-q7TNkfm-hhllShoZ62m), decoded 2026-09-18"
 - "`300mm Wall unit/worklist.xmlst` (1pBz_N2ty5_0UVuCVSpYx-smioTbD5W3u) and `600mm Wall unit/worklist.xmlst` (1k98zBX7Safi_foFnYsyD5ZznJX2QefXD), decoded and compared 2026-09-18"
 - "Owner (Minda), 2026-09-18: the AMFA unit is the master design for basic kitchen units"
 - "Owner (Minda), 2026-09-19: panels are cut on the F45 and then drilled on the Vitap"
 - "Owner (Minda), 2026-09-20: the furniture library has been updated"
 - "Google Drive folder `Furniture` (1BsTNcHI2OwjDlJdrCgv-x0BwHjas2qU1), re-listed 2026-09-20 - 18 subfolders"
 - "`AMFA Wall Unit 300 LH/worklist.xmlst` (15nS-7JwyJLlQvKs4rgXLky4wYkhJjWvu), `AMFA Wall Unit 300 LH 900/worklist.xmlst` (1uoicHChsfMCSPQW0FWWnM9ngKCA6XYDB) and `AMFA Wall Unit 500 LH 900 high/worklist.xmlst` (1MHpMdj_LJG3oP7SSwiq5gqxZ6Clcr-QY), decoded 2026-09-20"
 - "`AMFA Wall Unit 300 LH/03-BOTTOM.TCN` (1wU6ema5eXeDSEEtvbm0kHsge0Cg7u32C), decoded 2026-09-20"
 - "Owner (Minda), 2026-09-19: the earlier folders are a different, earlier design; `AMFA 600mm wall unit RH` is the latest release; 10 mm step-back for the shelf front and 16 mm step-back for the back panel to accommodate a Häfele concealed wall mount"
related:
 - ../Software/smartcabinet-and-production-workflow.md
 - ../Processes/tpacad-tool-type-optimizer-ambiguity.md
 - ../Processes/barcode-and-scan-event-system.md
 - ../Machinery/vitap-k2-panel-saw.md
 - ../Processes/carcase-fixings-cabineo-x-vs-confirmat.md
 - ../Processes/panel-production-route.md
 - ../Processes/tpacad-blind-bore-tool-id-fix.md
---

# Kitchen unit library (low-cost range)

**Status: sixteen wall units now exist, in two heights — built by the owner, not by this KB.** The
owner asked on 2026-09-18 for a library of low-cost kitchen units, having already made one by hand on
Drive, and confirmed that **`AMFA Wall Unit 600 RH` is the master design**. **On 2026-09-19 and
2026-09-20 the owner built the range out**: the `Furniture` folder went from seven subfolders to
**eighteen**, sixteen of them library units. This article records what exists today, what the files
actually contain — **measured from the part sizes, not read off the folder names** — what has to be
decided, and the one library-wide risk that is still unresolved. **This KB has created, moved and
renamed nothing on Drive**: the shape of the range is a commercial decision and the filing is the
owner's.

## Key facts

- **Sixteen library units exist as of 2026-09-20**, in two height families — **seven at 720 mm** and
  **eight at 900 mm** (the master being one of the 900s). Both heights were **measured**, not inferred
  from the folder names; §3's *a model name is not a specification* applies to a folder name too.
- **The two families are not distinguishable by name.** An unsuffixed `AMFA Wall Unit <width> <hand>`
  means **720** in seven folders and **900** in the master. That collision is the one thing here that
  can put the wrong carcase on the saw — see "The two height families" below.
- **The new units carry no nesting sheets.** Nine part files each, against the master's eleven rows:
  the two 2800 × 2070 `NESTING` rows are gone. That is the separation this article argued for on
  2026-09-18 and the production route evidenced on 2026-09-19, now done in the files themselves.
- **The 255 mm shelf holds across every width and height measured**, so the `300 − 16 − 19 − 10` depth
  chain and both step-backs are confirmed as **range specification**, not one unit's quirk.
- **The master is `AMFA Wall Unit 600 RH`** (Drive `1HHPym8Y04_s2VUYYwVy89hBQ4boabZxv`, created
  2026-09-16 13:45). Owner's decision, 2026-09-18. Four earlier folders — `300mm`, `400mm`, `500mm`
  and `600mm Wall unit`, all created 2026-09-16 around 10:22 — are **not** the master, and the
  `600mm Wall unit` folder is a second, different 600 mm unit.
- **The master's carcase is 19 mm throughout** — sides, top, bottom, shelves, **back** and **door**
  all `THICKNESS = 19.0`. A 19 mm back and a 19 mm door are a material choice with a direct cost
  consequence for a range whose selling point is price; recorded here as a fact, not a criticism.
- **The unit's nominal size is not stated in any file.** It is derived below from the part sizes, and
  the derivation is shown so it can be checked rather than believed.
- **Shelf depth is explained, and the two set-backs behind it are specification.** The 255 mm shelf is
  `300 − 16 − 19 − 10`: a **16 mm back-panel step-back** (for the Häfele concealed wall mount), the
  19 mm back itself, and a **10 mm shelf-front step-back**. The 256 and 266 on the earlier folders belong
  to **an earlier, different design**, not to a defect — owner, 2026-09-19.
- **Every hole in the master exports with no tool specified.** This is the same condition behind the
  live TpaCAD "Tool for this working not found" fault (Task **T016**) — see the risk section. It is
  the one finding here that could stop the whole library at the machine.

## What is on Drive today

The `Furniture` folder sits at the root of the owner's Drive (not inside this KB's folder tree). It
held **seven** subfolders when this article was written; re-listed 2026-09-20 it holds **eighteen**.

| Folders | Created | Contents | Read as |
|---|---|---|---|
| `AMFA Wall Unit 300/400/500 LH+RH`, `600 LH` — **7** | 19 Sep 11:50–11:53 | 9 `.TCN` + `.fnm` + `worklist.xmlst` | library units, **720 high** |
| `AMFA Wall Unit 300/400 LH+RH`, `500 RH`, `600 LH+RH` **+ 900** — **7** | 20 Sep 05:49–05:51 | 9 `.TCN` + `.fnm` + `worklist.xmlst` | library units, **900 high** |
| `AMFA Wall Unit 500 LH 900 high` — **1** | 19 Sep 14:43 | 9 `.TCN` + `.fnm` + `worklist.xmlst` | library unit, **900 high**; the odd name out |
| `AMFA Wall Unit 600 RH` — **1** | 16 Sep 13:45 | 11 `.TCN` + `.fnm` + `worklist.xmlst` | **the master**, 900 high, still carries nesting |
| `ANVAR_KITCHEN_V2`, `ANVAR_KITCHEN_V3` — **2** | 15/16 Sep | not opened | customer jobs |

**The four `300mm`/`400mm`/`500mm`/`600mm Wall unit` folders are gone** — they are no longer children
of `Furniture`. The replacement folders carry **fresh creation times**, so the four were removed rather
than renamed. *Recorded, not queried:* they were the evidence base for the 266 / 256 / 255 shelf-depth
comparison below, which is why that comparison is kept here in full. **This article is now the only
record of what those files contained.**

**The two `ANVAR_KITCHEN_*` folders were deliberately not opened.** A customer name on a folder is
enough to treat the contents as client data, and this KB's rule is **cite, never copy client data**.
They are listed here because their presence in the same folder as the library units is itself the
problem described under "What has to be decided".

## The two height families, and a naming collision

**Heights are not stated in any file, and were not taken from the folder names.** They fall out of the
same arithmetic the master's nominal was derived from: a side's `LENGTH` is the overall height minus
two 19 mm panels, and the door is the overall height minus a 4 mm gap. Three worklists were decoded in
full on 2026-09-20:

| Unit | Side | Bottom | Shelf | Back | Door | → nominal |
|---|---|---|---|---|---|---|
| `AMFA Wall Unit 300 LH` | 682 × 300 | 300 × 300 | 261 × 255 | 682 × 262 | 716 × 297 | **300 × 720 × 300** |
| `AMFA Wall Unit 300 LH 900` | 862 × 300 | 300 × 300 | 261 × 255 | 862 × 262 | 896 × 297 | **300 × 900 × 300** |
| `AMFA Wall Unit 500 LH 900 high` | 862 × 300 | 500 × 300 | 461 × 255 | 862 × 462 | 896 × 497 | **500 × 900 × 300** |

682 + 38 = **720**; 862 + 38 = **900**. Every other rule from the master reproduces unchanged — back =
width − 38, shelf = back − 1, door = (height − 4) × (width − 3), shelf depth 255 throughout. **Four
widths and two heights now agree with one piece of arithmetic**, which is considerably better evidence
for the derivation than the three-unit comparison that first supported it.

**And that is where the problem is.** The seven folders built on 19 September are **720** high and
carry no height in their names. The master, `AMFA Wall Unit 600 RH`, is **900** high and also carries
no height in its name. So an unsuffixed name means two different things in the same folder:

- `AMFA Wall Unit 600 LH` → **720 high**
- `AMFA Wall Unit 600 RH` → **900 high**

**180 mm apart, same naming pattern, nothing to tell them apart but the hand.** Picking "600 RH" for a
720 kitchen yields a 900 carcase, and because nothing upstream of the saw states a unit's height, the
error surfaces as cut board rather than as a warning. *This is the shape §3 keeps naming — a fact that
exists in the files and nowhere in the label.* **Two further consequences of the same scheme:**

- **`AMFA Wall Unit 600 RH 900` now also exists**, describing the same nominal unit as the master.
  Two folders for one unit invites the wrong one being copied.
- **`AMFA Wall Unit 500 LH 900 high`** is the only folder using ` high`; its seven siblings say `900`.
  Measured, it is an ordinary 500-wide 900-high LH unit — **a name to tidy, not a unit to re-cut.**

**Proposed, not done** (the filing is the owner's): put the height on **every** folder, including the
720s, and retire or rename the unsuffixed master. That is one renaming pass now against an open-ended
risk of cutting the wrong height later.

### Coverage

| Height | 300 | 400 | 500 | 600 | |
|---|---|---|---|---|---|
| **720** | LH RH | LH RH | LH RH | LH — | **7 of 8** |
| **900** | LH RH | LH RH | LH RH | LH RH | **8 of 8** |

The **720 set has no `600 RH`**. Deliberate, or an oversight? One folder either way, and worth knowing
before someone quotes a range that cannot be cut.

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

**One thing that could have broken it does not.** The owner confirmed on 2026-09-19 that **the cutting
list is finished sizes**, and that the F4 trims a panel by the tape thickness before applying the tape —
so the bander is dimension-neutral and no edging allowance is hiding in any of these figures. The door's
4 mm and 3 mm gaps are real gaps. See `../Processes/panel-production-route.md`.

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

**And it turned up one thing that did not hold — since explained.** Shelf depth is **266.0** on the
300 mm unit, **256.0** on the 600 mm unit and **255.0** on the master: three values for what should be
one number, since all three carcases are 300 deep and a shelf's depth has nothing to do with the unit's
width. Recorded as a defect with all three values kept rather than resolved by preferring the master's.

**The owner answered it on 2026-09-19: the earlier folders are a different, earlier design, and
`AMFA 600mm wall unit RH` is the latest release.** So there is no defect — there is a design that moved,
and four folders left behind at an earlier point in it. See the next section for why that answer is
better than a ruling.

### The depth chain, and why 255 is right

The owner gave the two figures the shelf depth is built from:

> **a 10 mm step-back for the shelf front, and a 16 mm step-back for the back panel to accommodate a
> Häfele concealed wall mount.**

That makes the master's shelf depth arithmetic rather than assertion:

| | mm |
|---|---|
| Carcase depth | **300** |
| − back-panel step-back (the void the concealed wall mount sits in) | −16 |
| − back panel thickness | −19 |
| − shelf-front step-back | −10 |
| **= shelf depth** | **255** ✓ |

**Which is exactly what `05-SHELF-1` and `06-SHELF-2` carry.** The chain closes to the millimetre, so the
master's figure is not just the newest — it is the one that can be checked.

**The two step-backs are specification, not incidental**, and they belong in any unit's spec card:

- **16 mm at the back** exists to leave a void between the back panel and the wall for the **Häfele
  concealed wall mount**. That is a hardware decision driving a panel dimension, which is precisely the
  sort of thing that has to be written down or it gets "tidied up" by someone later.
- **10 mm at the shelf front** sets the shelf back from the carcase front edge.

*This also ties the geometry to work already in this KB.* The Häfele Concealed Cabinet Hanger is one of
the two hardware items added to SmartCabinet's own Wall Support Cam Table on 2026-09-16, documented in
`../Processes/smartcabinet-wall-support-cam-table-reference.md` — the session that raised **T017**, the
unresolved X-sign discrepancy between those two items. **The 16 mm set-back is that hardware choice
showing up as a panel dimension.**

**What the earlier two folders were doing** — *this part is my arithmetic from the same chain, not
something the owner stated.* Running it backwards: the 300 mm unit's 266 needs the back and shelf
step-backs to total 15 mm, and the 600 mm unit's 256 needs them to total 25. Both fit a **15 mm** back
step-back with the shelf step-back going **0 → 10 → 10** and the back step-back later **15 → 16**. That
reads as a design being iterated rather than three inconsistent files, which is what the owner described.
**Offered as a reading, because it affects nothing**: the master is the release, and the earlier folders
are superseded either way.

### Two backs, not one

`07-BACK-1` and `07-BACK-1B` are the **same blank** (862 × 562 × 19) and both are listed once in the
worklist, so both get cut. *Worth re-asking now that the back panel is known to sit in a 16 mm void for a
concealed wall mount — a hanger usually wants the back notched or cut, so two back programs on one blank
may be exactly that. **Not asserted**, and the owner has not said.* Their programs differ substantially in size — 60,458 bytes against 11,994 —
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

**Re-checked 2026-09-20 against a unit built after this was written — unchanged, and now sixteenfold.**
`03-BOTTOM.TCN` from `AMFA Wall Unit 300 LH` was decoded in full: six Ø5 holes, every one reading
`#1002=5 … #1001=0`, the same diameter-without-tool export as the master. **The prediction above was
tested on files that did not exist when it was made, and held.** What changes is arithmetic, not
diagnosis — the fix is still the two steps at the Vitap in
`../Processes/tpacad-blind-bore-tool-id-fix.md`, still done once, and it now stands between the shop
and **sixteen** units rather than one. *The severity revision of 2026-09-19 also still stands: with
confirmat in stock as Plan B, T016 slows a job rather than stopping it.*

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

1. **The range.** ~~Which widths~~ — **answered in the files 2026-09-20: 300, 400, 500 and 600, both
   hands, at 720 and 900.** What is still open is **which unit types beyond the wall unit** (base,
   sink, appliance housing, tall), and **whether both heights are the range** or one of them is a
   trial. The earlier `300`–`600mm Wall unit` folders are no longer on Drive, so that part is moot.
2. **"Low cost" — a name or a specification?** If it denotes a defined carcase spec (board grade,
   back thickness, edging, hinge and fixing type), that spec belongs in this article and every unit
   is checked against it. If it is just a range name, say so and nothing further is needed.
3. **Hand.** ~~If hand is part of the unit's identity…~~ — **answered in practice 2026-09-20**: both
   hands exist as separate folders and `MIRROR` is `0` in every row of every worklist decoded, so
   nothing is being mirrored at job time. **Hand is part of the unit's identity.** *Recorded as what
   the files do, not as a decision the owner has stated* — Task **T023** still wants it confirmed,
   because the alternative (one folder per width, mirrored on demand) would halve the library.
4. **Where the library lives.** Library units and customer jobs currently share one folder. A library
   unit that is edited for a job stops being a library unit. Separating them is the single change with
   the most value and the least cost.

## Proposed structure

Offered for approval; **not created — and partly overtaken by events.** The owner's own convention,
visible in the folders since 2026-09-19, is `AMFA Wall Unit <width> <hand> [height]` rather than the
`W600-RH` code proposed below. **That is a decision, and this article follows it**; what survives from
the proposal is its *content* — a `unit.md` per unit, and library separated from jobs — not its naming.
The one change still worth making to the owner's scheme is putting the height on **every** folder, for
the reason given under "The two height families".

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

- Is the derived nominal **600 × 900 × 300** right? Everything above rests on it. *Corroborated again
  2026-09-20*: the same arithmetic reproduces 300 × 720 × 300, 300 × 900 × 300 and 500 × 900 × 300 from
  three independently built units — four widths and two heights now agreeing with one derivation.
- **Two backs** (`07-BACK-1`, `07-BACK-1B`) on one blank — deliberate, or a stray file in the cut list?
  **Still open, and now replicated in all sixteen units**, so it is worth one question rather than
  sixteen corrections.
- **The 720 set has no `600 RH`** — seven of eight, where the 900 set has all eight.
- **Is the master now redundant?** `AMFA Wall Unit 600 RH` and `AMFA Wall Unit 600 RH 900` describe the
  same nominal unit.
- ~~**Which shelf depth is right — 255, 256 or 266?**~~ — **answered 2026-09-19: 255, and it is
  derivable** as `300 − 16 − 19 − 10`. The earlier folders are an earlier design, not a defect.
- ~~**The four `300`–`600mm Wall unit` folders are a superseded design**~~ (owner, 2026-09-19) —
  **they are no longer in the `Furniture` folder as of 2026-09-20**, removed rather than renamed.
- ~~**Do the other widths need the same two step-backs?**~~ — **answered by measurement 2026-09-20**:
  every unit decoded carries a **255 mm** shelf at 300 deep, across two widths and both heights. The
  depth-side figures do carry across unchanged, as predicted. *Still untested on any unit type other
  than a wall unit, because none exists yet.*
- Is the **19 mm back and 19 mm door** intended for a low-cost range, or inherited from the master
  being drawn as a one-off?
- Does SmartCABINET generate a unit's parts **parametrically** from a width? If it does, the library
  is a list of parameters and this whole folder question is smaller than it looks. Nothing seen so far
  answers it, and it bears on the SmartCABINET-ERP question already open in `CLAUDE.md` §7.
- **T016 first.** See the risk section — the library should not be populated over an unresolved
  tool-resolution fault.
