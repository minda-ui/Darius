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
appearance, demountability, assembly speed — Cabineo X wins. For a range whose selling point is
price, **confirmat is the default and Cabineo X has to justify about £80 a kitchen**.

**But there is a finding that changes the question**, and it was not in either product's
specification. See the next section.

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

## What the master unit currently uses — neither

`03-BOTTOM.TCN` was decoded in full. Its seven holes are all **Ø5 mm, 12 mm deep, in the panel face**
(`#1002=5`, `#3=-12.0`) — *reading `#1002` as diameter is mine and undocumented, as recorded in the
library article*. Ø5 × 12 deep in a face is a **dowel** pattern. It is neither a confirmat (which
wants a stepped hole and an edge core hole) nor a Cabineo X (which wants Ø15 and a routed recess).

**So choosing either fixing is a change to the master, and therefore to every unit derived from it.**
That is the strongest practical reason to settle this now rather than after the library is populated —
the same argument as T016, arriving from a different direction.

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

The master's `03-BOTTOM` carries **2 fixings per carcase corner**. Four corners gives **8 carcase
fixings per box** — *that is arithmetic from one decoded part, not a count of the whole unit; the
sides and top have not been decoded, and back fixings and shelf supports are extra.*

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

**Default to confirmat for the low-cost range, and hold Cabineo X for anything that needs to come
apart or be seen.** The price gap is large, recurring, and lands squarely on the one attribute the
range is being built around; and the argument that would normally justify Cabineo — no edge drilling —
is cancelled by the Vitap's horizontal spindles.

**Two things could overturn that, and both are cheap to check:**

1. **A trade quote on the Cabineo X housing at 2,000.** If it comes in nearer £0.30 than £0.77, the
   per-kitchen difference falls to roughly £30 and the labour and appearance advantages start to pay
   for themselves.
2. **How the units are delivered.** If they go out flat-packed and are assembled on site, confirmat's
   poor demountability is a warranty problem rather than a preference, and Cabineo X is worth the
   money. If they are assembled and delivered rigid, it is not.

**A mixed spec is legitimate and probably right:** confirmat throughout the carcase, Cabineo X on
visible end panels and on anything built to be dismantled. It costs one extra line in the unit spec
and saves the difference everywhere it does not matter.

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
- **Who configured the SmartCABINET "Cabineo X" drill-head profile, and why?** If a decision was already
  taken, it is not recorded anywhere in this KB.
- **The trade price of the Cabineo X housing at 2,000** — the number the whole comparison turns on.
- **How many fixings does a whole unit actually take?** Eight is arithmetic from one decoded panel.
