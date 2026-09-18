---
title: "Carcase fixings: Cabineo X vs confirmat screws"
category: Processes
status: draft
sensitive: false
created: 2026-09-18
updated: 2026-09-18
sources:
 - "Owner (Minda), 2026-09-18: range will contain wall, base, sink, appliance housing and tall units; asks which fixing is better for a low-cost range"
 - "`Wiki/Machinery/vitap-k2-panel-saw.md` (Drive `1z41BjgLjOglkPSRD8vjigs6fypHqVGkm`), read 2026-09-18 — machine capability and the T016 incident record"
 - "`AMFA Wall Unit 600 RH/03-BOTTOM.TCN` (Drive `1ygANqYNEfpT7-q7TNkfm-hhllShoZ62m`), decoded 2026-09-18"
 - "`AMFA Wall Unit 600 RH/01-SIDE-LEFT.TCN` (Drive `1ZWciFvdK2rkKbeWvRpNQ825UWJsnnPe1`) and `08-DOOR-1.TCN` (Drive `1FfGBMAP4XfjJeCBwM5hvEVraRnhIWzHL`), decoded 2026-09-18"
 - "Lamello product pages and UK reseller listings, searched 2026-09-18 — see Prices, and read the caveat there"
related:
 - ../Software/kitchen-unit-library.md
 - ../Processes/tpacad-tool-type-optimizer-ambiguity.md
 - ../Machinery/vitap-k2-panel-saw.md
---

# Carcase fixings: Cabineo X vs confirmat screws

The owner asked, on 2026-09-18, which is better for a low-cost kitchen range. **This article does not
buy anything or commit the company to a supplier** (`CLAUDE.md` §6a); it sets out what the evidence
actually supports, what the numbers are, and the one price that needs challenging before the decision
is made.

## The short answer

**On price alone, confirmat wins by roughly 29×, and that is not close.** On everything else —
appearance, demountability, assembly speed — Cabineo X wins.

**But price is not where this decision actually sits, because the choice appears to have been made
already.** The master unit's own part files are drawn for a **face-inserted connector**, not for
confirmat, and SmartCABINET holds a drill-head profile called **Cabineo X**. So the real question is
not "which is better in the abstract" but **"was Cabineo X chosen, or did it arrive by default?"** —
and nothing in this KB records an answer.

- **If it was chosen**, roughly £80 a kitchen is the price of that decision, and changing it means
  re-drawing the master and every unit derived from it.
- **If it was a default nobody picked**, now — before the library is populated — is the only cheap
  moment to switch to confirmat.

Everything below is the evidence for that, and the numbers to decide with.

## The thing nobody had joined up

`Wiki/Machinery/vitap-k2-panel-saw.md` records, inside the **T016** incident write-up, a
*"SmartCabinet tool-database gap"* — specifically:

> *"no Dia. 5mm entry in a **'Cabineo X' drill-head profile**"*

**SmartCABINET already has a drill-head profile named Cabineo X.** Somebody has already configured
the design software toward this connector. And Cabineo X's own published tooling requirement is
**Ø5 mm and Ø15 mm drills plus a cutter of Ø12 mm or smaller** — so the missing Ø5 entry is *one of
the two drills Cabineo X needs*.

**That reframes T016.** It has been carried in this KB as a generic "tool not found" fault on the
Vitap. It is more specific than that: **the Cabineo X tooling is not fully defined in the software.**

The practical consequence is a fork, and it is worth being explicit about it:

- **If the range goes Cabineo X**, fixing T016 *is* the setup work. It stops being a bug to squash and
  becomes step one of commissioning the fixing method.
- **If the range goes confirmat**, the Cabineo X profile is a red herring for the library, and T016 is
  about whatever *else* drills Ø5 — the dowels and shelf pins the master already uses.

Either way the decision should be taken **before** more time goes into T016, because it decides what
"fixed" means.

*One caution: that profile's existence says someone configured it. It does not establish that the
connector was bought, trialled, or chosen — a configured profile is not a decision, and this KB has
been caught before treating something written down as something that happened.*

## The machine can do both — the edge-drilling argument does not apply here

The usual case for Cabineo is that it needs **no edge drilling**: it is machined entirely from the
panel face, so parts come off the machine in one setup. Confirmat needs a hole in the *edge* of the
mating panel, which on many shops means a second machine or a second handling.

**That argument does not apply to this workshop.** The Vitap's own KB article records:

> *"12 vertical spindles on Face 1, plus **horizontal spindle pairs on Faces 3-6**"*

So `FA2304` drills panel edges as well as faces, in the same machine. **Confirmat's edge hole is not a
second operation here.** The strongest generic argument for Cabineo is neutralised by the machine the
shop already owns — which is exactly why it was worth checking the machine before answering.

*What the article does not say: how many horizontal spindles per face, their diameters, or their
pitch. A Ø5 core hole in the edge is the usual confirmat requirement and is a common horizontal drill
size, but **this KB does not hold the Vitap's spindle diameters**, so "the machine can drill edges" is
established and "the machine can drill *this* edge hole" is not.*

The same article also lists, among up to three **optional** aggregated heads, a **"LAMELLO"
biscuit-joint system** head and an **"OVVO" connector system** head. Whether either is actually fitted
to this machine **is not recorded** — worth establishing, since one of them is made by Cabineo's
manufacturer.

## What the master unit is actually drawn for — a face-inserted connector

`01-SIDE-LEFT.TCN` and `08-DOOR-1.TCN` were decoded in full alongside `03-BOTTOM.TCN`. Three things
came out of it, and together they settle more than the fixing question.

### `#1002` is the diameter — now evidenced, not inferred

The door carries two workings at **`#1002=35`, 13 mm deep**, 100 mm from each end at 22.5 mm from the
edge, each flanked by **two `#1002=3` holes 5 mm deep, 45 mm apart and centred on it**.

A Ø35 × 13 cup at 22.5 mm from the edge, with Ø3 pilots at 45 mm centres, is a **concealed hinge** and
nothing else. **So `#1002` is the hole diameter.** That reading has been labelled an inference
throughout this KB since 2026-09-18; it can now be recorded as established.

*It also answers the hinge-cup question the owner asked this morning.* The door file **already
programs the 35 mm cup as a Ø35 bore** (`W#81 ::WTp`), not as a routed pocket. The design side is not
asking for a 12 mm cutter to be swept round a circle — it is asking for a **35 mm bit the shop does
not appear to have**. That is a different, and much cheaper, problem than re-programming the working:
a 35 mm hinge-cup bit is a standard item and the Vitap has the boring head for it.

### The sides are machined **face-only** — there is no edge drilling in the master at all

Every part file has six `SIDE#n` blocks. In both files decoded, **only `SIDE#1` has any content;
`SIDE#2`–`SIDE#6` are present and completely empty.** Whatever those faces are, nothing is machined on
them.

### And the carcase joint is a routed pocket plus a mating face hole

The side panel carries, at **twelve positions**, a routed operation run at two depths (−6.5 then
−13.0), each made of three overlapping 15 mm slots on an 11.2 mm pitch — **a pocket roughly 37 × 15 mm
and 13 mm deep**. The twelve positions are three-slot clusters at **Y = 230 and Y = 40**, at both ends
of the panel: **two pockets per carcase joint.**

`03-BOTTOM.TCN` carries **Ø5 × 12 mm holes at exactly the same Y values — 230 and 40 — two per joint.**

So the joint is: **a routed pocket in one panel, a Ø5 screw hole in the face of the mating panel, and
no edge machining anywhere.** That is the geometry of a face-inserted connector. **Cabineo X is
33.8 × 16.5 × 10.8 mm** — which sits inside a 37 × 15 × 13 pocket.

**It is not a confirmat pattern.** Confirmat needs a stepped hole through one panel and a core hole in
the *edge* of the other, and the master contains neither.

*Stated at the right strength: the pocket dimensions and the Cabineo X body dimensions are compatible,
and SmartCABINET holds a Cabineo X profile. That is strong circumstantial agreement, not a
part number read off a drawing. Somebody who knows what was ordered can confirm it in a sentence.*

### What that means for the decision

**Going Cabineo X is continuing; going confirmat is changing.** Switching would mean removing the
pockets from every part, adding stepped holes and edge holes, and starting to use horizontal spindles
the master currently never touches. That is design work plus a machining operation that does not exist
today — and it must happen **before** the library is populated or it happens once per unit instead of
once.

The side panel also carries, via an external macro `..\custom\mcr\fittingx.tmcr`, four **Ø5 × 12 mm
hole rows on a 32 mm pitch** — shelf-pin rows, two per shelf position. **Shelf supports are already
ordinary Ø5 pins**, not connectors, which is the right and cheap answer and needs no change under
either option.

## Prices

**Read this before using any number below.** These are **UK retail listings found by search on
2026-09-18**, not trade quotes, and the connector housing price is the weakest of them. Committing to
a supplier is the owner's (§6a); getting trade prices at real pack sizes is the action, not a
formality — it is the single biggest lever in the comparison.

| | Unit price | Source basis |
|---|---|---|
| **Confirmat 7 × 50** | **£0.0297 each** inc VAT | £29.69 per 1,000, Furnica UK |
| **Cabineo X housing** | **£0.77 each** | one UK listing (T&D Architectural); pack sizes are 500 and 2,000 |
| **Cabineo X 12 screw** | **£0.10 each** | £49.98 per 500, Axminster (listed as reduced from £59.98 → £0.12) |
| **Cabineo X, per joint** | **≈ £0.87** | housing **plus** screw — the X housing ships **without** a screw |

**Cabineo X is an open housing.** Unlike the original Cabineo, the screw is not integral: you snap the
housing in and fit whichever Cabineo screw (8 / 12) or shelf pin the application needs. That is a
genuine flexibility advantage — one housing serves carcase joints *and* shelf supports — but it means
**two line items, not one**, and any quote must cover both.

**£0.77 for the housing is the number I least trust.** It reads like a single-unit retail price, and
the original all-in-one Cabineo 12 sells for less than that in 500 packs — which would be odd if the
housing alone really cost £0.77 in volume. **Challenge it at 2,000.**

### What it costs per unit and per kitchen

**Eight carcase fixings per box** — and this is now counted, not estimated: the side panel carries two
pockets per joint at two joints, so four per side, eight per unit, and `03-BOTTOM`'s Ø5 holes agree
position for position. *Back fixings are extra and not yet identified; shelf supports are ordinary Ø5
pins and cost pennies either way.*

| At 8 carcase fixings | Per unit | Per 12-unit kitchen |
|---|---|---|
| Confirmat | **£0.24** | **£2.85** |
| Cabineo X | **£6.96** | **£83.52** |
| **Difference** | **+£6.72** | **+£80.67** |

Halve the housing price on a trade quote and the kitchen difference is still around **£40**. On a
low-cost range that is real money, and it recurs on every kitchen.

**Shelf supports would widen the gap further.** The master has two shelves; if Cabineo X housings were
used as shelf supports too, that is another 8 housings a unit against shelf pins costing pennies. If
Cabineo X is adopted, it should probably be **for carcase joints only**, with ordinary Ø5 pins for
shelves — the master already drills Ø5.

## What each one actually buys you

**Confirmat**
- Cheapest by a wide margin, and the price is stable and multi-sourced.
- Strong in chipboard and MDF — coarse thread, large core, designed for the job.
- **The head is visible on the outside of the panel** and wants a cover cap. Fine where sides are
  hidden between units; a problem on an end-of-run panel or any visible side. Caps cost money and
  time, and they look like what they are.
- **Does not survive repeated assembly.** The hole degrades; a unit taken apart twice is a unit with a
  loose joint. Poor for flat-pack-and-site-assemble, fine for rigid units assembled in the workshop.
- Needs a stepped hole and an edge core hole — **not a problem on this machine**, see above.

**Cabineo X**
- **Nothing visible on the outside face.** The connector sits inside the carcase.
- **Demountable and reusable** — genuinely useful for flat-pack delivery, site assembly, access
  through tight doorways, and anything that has to come apart again.
- Fast, single-action assembly; no caps to fit.
- Machined **from the face only**, minimum panel thickness 12 mm, installation tolerance ±0.5 mm.
- One housing covers carcase joints and shelf supports.
- **About 29× the price per fixing** at the figures above.
- The tooling it needs — Ø5, Ø15, ≤Ø12 cutter — is **nearly tooling the shop already has**: the master
  already drills Ø5, and tool ID `1002` is a 12 mm cutter. **Ø15 is the one unknown.**

## Recommendation

**Answer one question first: did somebody choose Cabineo X?** The master is drawn for it and
SmartCABINET is configured for it. If that was a deliberate decision, take it as made — the £80 a
kitchen is what it costs, and re-drawing the range to save it is not obviously worth the design work
and the new machining operation.

**If nobody chose it — if it came with the software or with a demo file — then switch to confirmat
now.** The price gap is large, recurring, and lands squarely on the one attribute the range is being
built around; the Vitap's horizontal spindles mean the edge hole is not an obstacle here; and this is
the last moment when changing it costs one redraw instead of one per unit.

**Two further things bear on it, and both are cheap to check:**

1. **A trade quote on the Cabineo X housing at 2,000.** If it comes in nearer £0.30 than £0.77, the
   per-kitchen difference falls to roughly £30 and the labour and appearance advantages start to pay
   for themselves.
2. **How the units are delivered.** If they go out flat-packed and are assembled on site, confirmat's
   poor demountability is a warranty problem rather than a preference, and Cabineo X is worth the
   money. If they are assembled and delivered rigid, it is not.

**A mixed spec remains legitimate** — confirmat through the carcase, Cabineo X on visible end panels
and on anything built to be dismantled — but it is worth less here than it first looked, because
Cabineo X leaves nothing visible anyway and the master is already drawn for it throughout. Mixing
would mean maintaining two joint geometries in one library for a saving of a few pounds a unit.

**Separately, and cheaply: buy a 35 mm hinge-cup bit.** The door file already asks for one. That is
unrelated to the connector choice and unblocks a job that is live now.

## Costing — the wider point

Fixings are one line in a unit cost, and on these numbers not the biggest one. A unit cost model for
the range needs, at minimum: **board** (by sheet, with a real waste factor from the nesting),
**edging**, **fixings**, **hardware** (hinges, shelf supports, legs, handles, drawer runners on base
units), **machine time** and **assembly labour**. None of those are in this KB yet.

**The board line is the one to build first**, because it dominates and because the master's own
nesting files already carry the sheet size — and because of the contradiction in the next section.

## Open questions

- **The nesting sheet does not fit the machine.** The master's nesting files are **2800 × 2070**
  (`09-NESTING01-SP19-W1100`, `10-NESTING02-SP19-U963`), but the Vitap's recorded panel capacity is
  *"length 270/400-3000mm … **width 150-1250mm**"*. **2070 is 820 mm wider than the stated maximum.**
  Either the nesting is cut somewhere else, or the capacity figure is wrong, or "nesting" here means
  something other than what it looks like. **Recorded as a contradiction, not resolved** — but it bears
  directly on costing, because it decides which machine cuts the sheet and therefore what a unit costs
  to make.
- **Is a "LAMELLO" or "OVVO" aggregated head actually fitted to `FA2304`?** Both are listed as optional
  in the machine article; neither is confirmed present. One is made by Cabineo's manufacturer.
- **What Ø are the Vitap's horizontal spindles?** Needed to confirm confirmat's edge core hole is
  drillable without new tooling.
- **Who chose Cabineo X — and was it a choice?** The master is drawn for a face-inserted connector and
  SmartCABINET holds a Cabineo X profile, but **nothing in this KB records a decision, a purchase or a
  trial.** This is now the question the whole comparison turns on, ahead of price.
- **Is the pocket actually a Cabineo X pocket?** 37 × 15 × 13 fits a 33.8 × 16.5 × 10.8 body, but that
  is compatibility, not identification. Anyone who knows what was ordered can settle it in a sentence.
- **What are the Ø10 × 13 holes** on the side panel — three at 32 mm pitch, 11 mm in from the back edge?
  Not identified. Possibly back-panel or cam fixings.
- **The trade price of the Cabineo X housing at 2,000** — the number the whole comparison turns on.
- **How many fixings does a whole unit actually take?** The eight carcase fixings are counted, from the
  side panel and confirmed against the bottom. **Back fixings are not identified** — the back is 19 mm
  and housed inside all four panels, and nothing decoded so far shows what holds it. Shelf pins are
  known (Ø5 at 32 mm pitch).
