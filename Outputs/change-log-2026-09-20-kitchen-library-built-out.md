# Change log — 2026-09-20 — The kitchen library built out, and a folder name that means two heights

**Session 17.** One instruction — *"i have updated furniture library, can you check on Furniture folder
on Google Drive"* — and the answer needed measuring rather than listing. The `Furniture` folder has gone
from **7 subfolders to 18**, sixteen of them library units, and the single most useful finding is one
that a listing would not have produced: **two of those folders share a naming pattern and are 180 mm
apart in height.**

---

## What changed on Drive

| | 2026-09-18 | 2026-09-20 |
|---|---|---|
| Subfolders | 7 | **18** |
| Library units | 1 (the master) | **16** |
| Earlier `300`–`600mm Wall unit` folders | 4 | **0 — no longer present** |
| Customer job folders | 2 | 2 (**not opened**, as before) |

Built in three bursts: **seven folders on 19 Sep 11:50–11:53**, **one at 14:43**, and **seven more on
20 Sep 05:49–05:51**.

**The two `ANVAR_KITCHEN_*` folders were again not opened.** A customer name on a folder is enough to
treat the contents as client data; the rule is *cite, never copy*.

## The heights were measured, not read

The folder names offer a height — seven of them end in `900` — and §3 says plainly that **a model name
is not a specification**. So three `worklist.xmlst` files were downloaded as exact bytes, decoded, and
run through the same arithmetic that derived the master's nominal on 2026-09-18: a side's `LENGTH` is
the overall height minus two 19 mm panels, and the door is the height minus a 4 mm gap.

| Unit | Side | Bottom | Shelf | Back | Door | → nominal |
|---|---|---|---|---|---|---|
| `AMFA Wall Unit 300 LH` | 682 × 300 | 300 × 300 | 261 × 255 | 682 × 262 | 716 × 297 | **300 × 720 × 300** |
| `AMFA Wall Unit 300 LH 900` | 862 × 300 | 300 × 300 | 261 × 255 | 862 × 262 | 896 × 297 | **300 × 900 × 300** |
| `AMFA Wall Unit 500 LH 900 high` | 862 × 300 | 500 × 300 | 461 × 255 | 862 × 462 | 896 × 497 | **500 × 900 × 300** |

682 + 38 = **720**. 862 + 38 = **900**. Every other rule from the master reproduces unchanged: back =
width − 38, shelf = back − 1, door = (height − 4) × (width − 3), shelf depth 255 throughout.

**This is the strongest corroboration the derived nominal has had.** It was first supported by three
units compared side by side on 2026-09-18; it now reproduces across **four widths and two heights**, on
files that did not exist when the derivation was written. *A derivation that predicts files made later
is worth more than one that fits the files it was made from.*

## The finding: an unsuffixed folder name means two different heights

The seven folders built on 19 September are **720 high and carry no height in their names**. The
master, `AMFA Wall Unit 600 RH`, is **900 high and also carries no height in its name**. In the same
folder, under the same pattern:

- `AMFA Wall Unit 600 LH` → **720**
- `AMFA Wall Unit 600 RH` → **900**

**Nothing but the hand distinguishes them, and the hand is not the thing that differs.** Picking
"600 RH" for a 720 kitchen yields a 900 carcase, and since nothing upstream of the saw states a unit's
height, that error surfaces as cut board rather than as a warning. **This is §3's recurring shape: a
fact that exists in the files and nowhere in the label.**

Two more from the same scheme, both cheap to fix and expensive to leave:

- **`AMFA Wall Unit 600 RH 900` now also exists**, describing the same nominal unit as the master.
  Two folders for one unit invites the wrong one being copied.
- **`AMFA Wall Unit 500 LH 900 high`** is the only folder using ` high`; its seven siblings say `900`.
  Measured, it is an ordinary 500-wide 900-high LH unit — **a name to tidy, not a unit to re-cut.**

**Proposed, not done**, because the filing is the owner's: put the height on **every** folder, including
the 720s, and retire or rename the unsuffixed master.

### Coverage

| Height | 300 | 400 | 500 | 600 | |
|---|---|---|---|---|---|
| **720** | LH RH | LH RH | LH RH | LH — | **7 of 8** |
| **900** | LH RH | LH RH | LH RH | LH RH | **8 of 8** |

**The 720 set has no `600 RH`.** One folder either way, and worth settling before anybody quotes a
range that cannot be cut.

## Three things that got better

**The nesting sheets are gone.** Each new unit holds **nine** part files where the master's worklist had
eleven rows — the two 2800 × 2070 `NESTING` rows are absent. That is exactly the separation this KB
argued for on 2026-09-18 and evidenced on 2026-09-19 (nesting is a saw-stage job artefact, not part of a
unit's definition), now done in the files themselves. **Nobody was asked to do it**; recorded because an
argument that turns out to match what the owner already does is worth knowing about.

**The 255 mm shelf holds everywhere it was measured**, at 300 and 500 wide and at both heights. So the
`300 − 16 − 19 − 10` chain, the **16 mm back-panel step-back** for the Häfele concealed wall mount and
the **10 mm shelf-front step-back** are **range specification**, not one unit's quirk. That closes an
open question from 2026-09-19 — *do the other widths need the same two step-backs?* — **by measurement
rather than by the reasoning that predicted it.**

**Hand is settled in practice.** Both hands exist as separate folders and `MIRROR` is `0` in every row
of every worklist decoded, so nothing is mirrored at job time. *Recorded as what the files do, not as a
decision the owner has stated* — **T023** still wants it confirmed, because the alternative (one folder
per width, mirrored on demand) would halve the library.

## T016 is unchanged, and now stands in front of sixteen units

`03-BOTTOM.TCN` from `AMFA Wall Unit 300 LH` was decoded in full. Six Ø5 holes, every one reading:

```
W#81{ ::WTp #1002=5 #1=11.9 #2=230.0 #3=-12.0 #8015=0 #201=1 #203=1 #1001=0 }W
```

**`#1001=0` — diameter given, no tool named.** The same export condition as the master, in a unit built
two days and fifteen folders later. On 2026-09-18 this article predicted that *"every unit in the
library will export the same way"*; **that prediction has now been tested against files that did not
exist when it was made, and held.**

What changes is arithmetic, not diagnosis. The fix is still the two steps at the Vitap
(`Wiki/Processes/tpacad-blind-bore-tool-id-fix.md`), still done once, and the 2026-09-19 severity
revision still stands — with confirmat in stock as Plan B, T016 slows a job rather than stopping it.
What is different is the multiplier: **one fix, sixteen units.**

## The four earlier folders are gone

`300mm`, `400mm`, `500mm` and `600mm Wall unit` are no longer children of `Furniture`. The replacement
folders carry **fresh creation times**, so the four were **removed rather than renamed**.

**Recorded, not queried.** They were superseded by the owner's own account on 2026-09-19, so their
removal is consistent. The reason it is worth a line: those four files were the evidence base for the
**266 / 256 / 255 shelf-depth comparison** — the finding that "comparing siblings finds what reading one
cannot" was built on. That comparison is kept in the article in full, because **the article is now the
only record of what those files contained.**

## What was written

- **`Wiki/Software/kitchen-unit-library.md`** rewritten in place — 19,529 → 27,254 bytes. New section
  *"The two height families, and a naming collision"* with the measured table, the coverage grid, the
  T016 re-check, and four open questions closed or reframed. The **proposed `W600-RH` unit-code scheme
  is marked partly overtaken by events**: the owner's `AMFA Wall Unit <width> <hand> [height]` is a
  decision and the article now follows it, keeping the proposal's *content* (a `unit.md` per unit,
  library separated from jobs) rather than its naming.
- **`Wiki/index.md`** entry rewritten — it still described a draft with one unit.

**Nothing was created, moved or renamed on Drive.** This KB read the owner's working folder and wrote up
what it found.

## Still open

- **Which unit types beyond the wall unit** — base, sink, appliance housing and tall still have no
  master at all. The range is four widths of one type.
- **Whether both heights are the range**, or one of them is a trial.
- **The naming pass** — height on every folder; the duplicate 600 RH; the ` high` suffix.
- **The 720 set's missing `600 RH`.**
- **Two backs** (`07-BACK-1`, `07-BACK-1B`) on one blank — unchanged, and now replicated sixteen times,
  so it is worth one question rather than sixteen corrections.
- **T016**, which closes at the machine.
- **Whether SmartCABINET generates parts parametrically from a width** — sixteen folders that differ
  only by width and height is either sixteen hand-built units or one parametric definition exported
  sixteen times, and which it is decides whether a library is a folder tree or a parameter list.

---

## The owner's observation, measured — and what it opens up

Later the same day: *"Mostly side elements are same through all units, it's only up, bottom and back
which are specific to width. Would that make a help for us to cope with bigger load on workshop?"*

**Measured rather than accepted, and it turned out to be stronger than stated.**

### The side is width-invariant to the byte

`01-SIDE-LEFT.TCN` was downloaded as exact bytes from `AMFA Wall Unit 300 LH 900` and from
`AMFA Wall Unit 500 LH 900 high` and diffed:

```
IDENTICAL - byte for byte     sha256 ac79530d4aa8ba14…   (both 20,400 B)
```

**Not the same blank — the same program.** Same Ø10 row, same Ø5 row, same routed pockets. Every
coordinate in the file is referenced to the side's own 862 × 300 face, so nothing in it *can* depend on
carcase width. *A size match would have proved nothing (§3); this is a diff of decoded bytes.*

**One correction to the observation, and it matters for the arithmetic:** shelves and the door are
width-specific too. **Two parts of nine are constant; seven vary.**

### Hand is a mirror, not a redesign

`300 LH`'s left side against `300 RH`'s right side — 172 lines each, same operations, every X reflected
about 431:

| Feature | LH left | RH right | check |
|---|---|---|---|
| Ø10 row | 71, 103, 135 | 791, 759, 727 | 862 − 71 = 791 |
| fitting macro 1 | 676.2 → 484.2 | 185.8 → 377.8 | 862 − 676.2 = 185.8 |
| fitting macro 2 | 382.6 → 190.6 | 479.4 → 671.4 | 862 − 382.6 = 479.4 |
| Ø5 row | 50, 304, 558, 812 | 50, 304, 558, 812 | already symmetric |

The Ø5 row mirrors onto itself. **The whole two-byte file-size difference is `71.0` becoming `791.0`.**

So per height: **four side programs, two geometries, each with its mirror** — and the mirror is being
baked in at export. Every worklist carries `MIRROR = 0` while SmartCABINET emits pre-mirrored files.
**If the Vitap honours that column, four programs become two.** Unverified; ten minutes at the machine.

### One more reading, offered as a reading

Every routed setup carries **`#205=1002`** — a tool actually named, and 1002 is the shop's 12 mm cutter.
Every drilled hole carries **`#1001=0`**. Consistent across three files. *The parameter indices are my
reading and are not documented in the extract this KB holds*, but if it is right, **T016 is a
drilling-only fault** — which would explain why the routed pockets have never been what failed.

### The proposal

Written up as **`Wiki/Processes/library-batch-production.md`** — *measured findings, proposed method,
nothing adopted.* The shape of it: **the constant part is the most machined one, and the seven that
vary are plain panels**, which is precisely the condition that lets the expensive half be pre-built and
the cheap half made to order.

- **Two blanks cover every side in the library** — 862 × 300 and 682 × 300. At 18 and 24 per sheet
  respectively (*my arithmetic, 4 mm kerf, before trim*), **one sheet of sides is nine to twelve units'
  worth of the hard part.**
- **Batching by part type instead of by unit** takes a 12-unit kitchen across four widths from
  **108 program loads to 32**, and needs **no change to any file** — only to the order of work.
- It **adds no capacity**: one saw, one bander, one borer, in series. It removes changeover and enables
  a buffer.
- Risks recorded rather than glossed: **stock obsolescence** (the back step-back has already moved
  15 → 16 mm once), **WIP storage**, **labelling** (barcode Phase 1, waiting on T022), and the fact that
  **batch errors scale** — a wrong setup ruins 24 parts, not 2, so a first-off check stops being
  optional.
- **T016 gets sharper under batching, not softer**, and the systemic half matters more.

### A rule obeyed on its author

The new article's `related:` block initially pointed at six articles; the link-graph check reported
**five asymmetric edges** — the exact debt closed on 2026-09-19. Rather than leave them or silently
edit five more articles, the block was **trimmed to the two that are genuinely bidirectional**
(`kitchen-unit-library`, `panel-production-route`, the latter given its back-link), with the rest kept
as ordinary body citations. Graph re-checked: **138 directed edges = 69 symmetric pairs, 0 asymmetric,
0 dangling, 0 self.** 32 articles.
