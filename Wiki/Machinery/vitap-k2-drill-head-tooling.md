---
title: "FA2304 Vitap K2-2.0 — drill-head tooling, as read on 2026-09-23"
category: Machinery
status: active
sensitive: false
created: 2026-09-23
updated: 2026-09-23
sources:
 - "Owner at the machine, 2026-09-23 — WscTecnoManager `Tool information` dialogs for bushes 2 and 3 (photographed, read field by field) and reported Comment lines for bushes 4 and 6-10"
 - "Owner, 2026-09-22/23 — the tooling changes recorded under \"What changed, and when\""
 - "Owner photograph, 2026-09-23 — WscTecnoManager full head layout view, bushes 1-12, 41-44, 51-54, 111"
 - "`Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md` — positions 101 and 4 as read on 2026-09-15"
 - "Vitap K2-2.0 operating manual, chapter 5 p.63 — through-drill placement and rotation-ring convention (owner photograph, 2026-09-23)"
related:
 - ./vitap-k2-panel-saw.md
 - ../Processes/tpacad-tool-match-criteria.md
 - ../Processes/tpacad-blind-bore-tool-id-fix.md
 - ../Processes/tpacad-tool-type-optimizer-ambiguity.md
---

# FA2304 Vitap K2-2.0 — drill-head tooling

> **This is a dated snapshot, not a standing fact.** Everything below was true on **2026-09-23**. The
> head changed on **2026-09-22** and again on **2026-09-23**, both times within a day of being read.
> **Anything that cites this article must cite the date with it.** See "Where this really belongs".

## Why the KB has this at all

Five sessions documented this machine without ever recording what is in its head. The layout existed
only as prose inside `tpacad-tool-type-optimizer-ambiguity.md`, written from two positions checked by
hand on 2026-09-15, and that prose was then relied on for eight days as though it described the
machine. It described the machine **as it was on 15 September**. *Same shape as the unregistered
compressor and the one-way `related:` links: a gap nothing inside the KB could announce.*

## What is fitted

**Provenance matters more than the table.** Two different qualities of evidence are mixed here and
they are marked:

- **`ARCHIVE`** — read directly off WscTecnoManager's own `Tool information` dialog. Authoritative.
- **`LAYOUT`** — my reading of diameters off a photograph of the head layout view. **An inference from
  a small on-screen graphic, not a reading of a record.** Diameters may be right and types are
  entirely unknown.

| Bush | Comment line / diameter | Evidence | Notes |
|---|---|---|---|
| 1 | **not established** | — | **never opened.** The only other position the layout suggests may be Ø3 |
| 2 | `Foratore passante Ø 5mm` | `ARCHIVE` | Tool Length 48, Lance Length 5, Ø5 |
| 3 | `Foratore passante Ø3mm` | `ARCHIVE` | Tool Length 53, Lance Length 3, Ø3. **The only Ø3 on the head** |
| 4 | `Foratore cieco 10mm` | `ARCHIVE` (Comment line) | **fitted 2026-09-22** |
| 5 | Ø35 | `LAYOUT` | the 35 mm hinge-cup head — confirms from the machine that one exists (T027) |
| 6 | `Foratore cieco 5mm` | `ARCHIVE` (Comment line) | |
| 7 | `Foratore cieco 5mm` | `ARCHIVE` (Comment line) | |
| 8 | `Foratore cieco 5mm` | `ARCHIVE` (Comment line) | |
| 9 | `Foratore cieco 5mm` | `ARCHIVE` (Comment line) | |
| 10 | `Foratore cieco 5mm` | `ARCHIVE` (Comment line) | |
| 11 | Ø8 | `LAYOUT` | |
| 12 | Ø12 | `LAYOUT` | **fitted 2026-09-22** |
| 41, 42 | Ø8 | `LAYOUT` | |
| 43, 44 | Ø5 | `LAYOUT` | **type unknown — see "The count question"** |
| 51, 54 | Ø8 `LONG` | `LAYOUT` | |
| 52, 53 | Ø5 | `LAYOUT` | **type unknown — see "The count question"** |
| 111 | 100 | `LAYOUT` | |
| 101 | `Fresa Ø10mm`, ID `1001` | 2026-09-15 reading | one of the special / aggregated tool-holder positions 101-104 |
| 102-104 | not established | — | |

**Diameters present on the head: Ø3, Ø5, Ø8, Ø10, Ø12, Ø35, plus a Ø10 cutter at 101.**
**Notably absent: Ø15** — which is what TpaCAD's native `CABINEO` working drills (3 × Ø15 × 11 mm
deep), so that route is unavailable without a purchase.

### There is no blind Ø3

Confirmed by the owner from the archive, 2026-09-23. **Bush 3 is the only Ø3 and it is `passante`.**
This is the direct cause of `03-BOTTOMB.TCN` failing to optimise — see
`../Processes/tpacad-tool-match-criteria.md`.

### The count question

September recorded **five** blind Ø5 bushes (6-10) and that is confirmed. But the layout photograph
shows Ø5 at **ten** positions: 2, 6-10, 43, 44, 52 and 53. Bush 2 is known to be `passante`; **43, 44,
52 and 53 have never been opened.** If any of them is `cieco`, the blind Ø5 count is higher than five.

*It changes no fix — the five criteria in `tpacad-tool-match-criteria.md` care whether at least one
tool qualifies, not how many. It changes the KB's description of the head, which has already proved
able to mislead. Four Comment lines close it.*

## What changed, and when

| Date | Change |
|---|---|
| **2026-09-22** | **Ø10 blind drill fitted to bush 4; Ø12 fitted to bush 12.** These are **drills** (`Foratore`), not cutters — so they do **not** unblock the interpolated-hole test in `../Processes/tpacad-interpolated-holes.md`, which needs a `Fresa` |
| **2026-09-23** | **Bush 3's physical drill replaced** — a blind Ø3 was in the spindle; a through Ø3 now is, matching the archive record |

### The bush 3 mismatch — a latent fault, found, with no error attached

Until 2026-09-23, **bush 3 physically held a blind drill while WscTecnoManager described it as
`Foratore passante Ø3mm`.** Any program resolving a through Ø3 to bush 3 would have been drilled with
a blind bit, and **nothing would have reported it** — the optimiser checks the archive, not the
spindle. It would only ever have shown up in the workpiece.

**This did not cause the `03-BOTTOMB` error**, which was a true absence of any blind Ø3 in the archive
and would have occurred either way. It is a separate find, and merging the two would give this KB a
third wrong cause for the same error message. *Keep them apart.*

**The general lesson is not about Ø3.** The archive and the head are two stores of one fact, and the
software trusts only one of them. **A tool change is not finished when the drill is in the spindle; it
is finished when the archive says what is in the spindle.** That is the same shape as §3's *a
correction has to be swept through every store the claim reached* — the narrative layer and the
live-data layer again, one turn of the screw further down.

## Before changing any tooling — manual chapter 5, p.63

The machine's own manual carries a constraint that appears **nowhere** in this KB's TpaCAD or
maintenance articles:

- **Through-drills must be fitted in the indicated spindles.**
- **Black ring = right-hand rotation. Red ring = left-hand rotation.**
- Wrong placement causes *"damage to the drill bits and early wear of the rollers."*

Bush 3's archive record carries `Through hole Exit Speed` and `Speed exit = True` — through-drill
fields — which together with p.63 is reason to treat **bush 3 as a designated through position**. A
blind bit in it was wrong twice over: wrong against the record and, on this reading, wrong against
p.63.

**Consequence for any fix that moves a drill:** check the ring colour against the spindle. Note that
editing a tool's **ID** in TpaCAD's Technology dialog moves nothing physical and is not affected by
this.

## Where this really belongs

**This head is live data.** It changed on two consecutive days, each time within hours of the KB
reading it. By this KB's own rule — *put a fact where its own update cycle lives* (`CLAUDE.md` §3) and
*the Smartsheet sheets, not any Wiki article, are the live source for current status* (§1) — **a
tooling table belongs on a sheet, with this article narrating and citing it.**

**Proposed to the owner 2026-09-23, not built.** A new Workshop sheet (`Vitap Tool Head`, one row per
bush: Bush, Comment, Diameter, Type, Tool Length, Useful Length, ID, Evidence, Last verified) would
also give the five-criteria checklist somewhere to read criterion 4 from without a trip to the machine.
Creating a sheet is a structural addition, so it waits on the owner's word.
