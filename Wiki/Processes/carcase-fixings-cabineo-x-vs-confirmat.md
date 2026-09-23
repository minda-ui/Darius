---
title: "Carcase fixings: Cabineo X vs confirmat screws"
category: Processes
status: draft
sensitive: false
created: 2026-09-18
updated: 2026-09-18
sources:
 - "Owner (Minda), 2026-09-18: range will contain wall, base, sink, appliance housing and tall units; asks which fixing is better for a low-cost range"
 - "Owner (Minda), 2026-09-19: panels are cut on the F45 and then drilled on the Vitap"
 - "Owner (Minda), 2026-09-19: \"Cabineo X was chosen, we ordered them\" — the decision, and the connectors are on order"
 - "Owner (Minda), 2026-09-19: \"leave conformant as Plan B, we have them in stock too\" — confirmat retained as the fallback, and held in stock"
 - "`Wiki/Machinery/vitap-k2-panel-saw.md` (Drive `1z41BjgLjOglkPSRD8vjigs6fypHqVGkm`), read 2026-09-18 — machine capability and the T016 incident record"
 - "`AMFA Wall Unit 600 RH/03-BOTTOM.TCN` (Drive `1ygANqYNEfpT7-q7TNkfm-hhllShoZ62m`), decoded 2026-09-18"
 - "`AMFA Wall Unit 600 RH/01-SIDE-LEFT.TCN` (Drive `1ZWciFvdK2rkKbeWvRpNQ825UWJsnnPe1`) and `08-DOOR-1.TCN` (Drive `1FfGBMAP4XfjJeCBwM5hvEVraRnhIWzHL`), decoded 2026-09-18"
 - "Lamello product pages and UK reseller listings, searched 2026-09-18 — see Prices, and read the caveat there"
related:
 - ../Software/kitchen-unit-library.md
 - ../Processes/tpacad-tool-type-optimizer-ambiguity.md
 - ../Machinery/vitap-k2-panel-saw.md
 - ../Processes/panel-production-route.md
 - ../Processes/tpacad-blind-bore-tool-id-fix.md
 - ../Processes/tpacad-tool-match-criteria.md
---

# Carcase fixings: Cabineo X vs confirmat screws

The owner asked, on 2026-09-18, which is better for a low-cost kitchen range. **This article does not
buy anything or commit the company to a supplier** (`CLAUDE.md` §6a); it sets out what the evidence
actually supports, what the numbers are, and the one price that needs challenging before the decision
is made.

## Decided: Cabineo X

> **"Cabineo X was chosen, we ordered them."** — owner, 2026-09-19

> **"But leave conformant as Plan B, we have them in stock too."** — owner, 2026-09-19

**So this article stops being a comparison and becomes a record — of a primary and a fallback.**
Cabineo X is the specification. **Confirmat is the fallback, and it is held in stock**, which changes
the risk picture more than it changes the spec: see "Plan B is genuinely viable" below. Everything here
is kept because it documents what the choice costs and what each route commits the shop to.

**What the decision settles:**

- **Roughly £80 a kitchen is settled cost**, not a question. Confirmat is ~29× cheaper per fixing (the
  numbers are in Prices below) and that gap is now the price of the appearance, the demountability and
  the single-action assembly. Still worth a **trade quote on the housing at 2,000** — £0.77 is a
  single-unit retail listing, and getting it nearer £0.30 is money for one phone call.
- **The master needs no re-drawing.** It was already drawn for a face-inserted connector, so the
  decision confirms the existing files rather than obsoleting them — see "What the master unit is
  actually drawn for".
- **T016 is now the setup work, not a bug.** This was the fork stated below, and the decision picks the
  branch: *if the range goes Cabineo X, fixing T016 **is** commissioning the fixing method.* It is the
  library's remaining blocker — **though a less severe one than it looked**, because of Plan B.
- **No new tooling is implied.** See the next section — this is the part worth reading before spending
  anything.

## Plan B is genuinely viable, and it de-risks T016

**A unit machined for Cabineo X can be assembled with confirmat instead, without re-drawing anything.**

The reason is the geometry already established: the connector pockets are **routed into the inside faces
of the carcase**, so a pocket left empty is **hidden inside the finished unit**. Nothing shows. The parts
do not change size, the holes that are there do no harm, and the cutting list is unaffected.

What a confirmat fallback additionally needs is its **core hole in the panel edge** — and that is
available two ways: on the Vitap, which has horizontal spindle pairs on Faces 3–6, or at the bench with
a stepped bit and a jig. The edge in question is a side's **end** edge, which sits inside the joint and
is **not edged**, so there is no tape to drill through either.

**Why this matters more than it sounds.** T016 was recorded as a precondition for populating the library
— *"a Ø5 that does not resolve fails every unit identically"*. With confirmat in stock as a working
fallback, **a job is not stopped by T016**; it is made more slowly and with a visible screw head. That
turns T016 from a blocker into a priority: still the thing to fix first, no longer the thing that has to
be fixed before anything can be cut.

*One caveat, stated rather than assumed: this says the **carcase** can be assembled either way. It does
not establish that a Cabineo-drilled panel and a confirmat-screwed joint reach the same rigidity or the
same repeatability — a routed pocket removes material from the side's inside face near the joint, and
nobody has tested a mixed-history panel. If Plan B is ever used in anger, it is worth looking at the
first one.*

## No Ø15 drill is needed, and that matters

Cabineo X's published tooling requirement is **"Ø5 and Ø15 drills, cutter Ø12 or smaller"** — which
reads like a shopping list, and the Ø15 is the one item this KB could not account for. **It is not
needed here.**

The housing fits **"a drilled or routed recess, machined solely from the surface"** — drilling and
routing are **alternatives**, not both. And **the master routes it**: the pocket is three overlapping
slots at two depths, cut with a milling tool, not a Ø15 bore. There is no Ø15 hole anywhere in the
decoded parts (they carry Ø3, Ø5, Ø10 and Ø35).

**So everything Cabineo X needs is already on the machine** — the Ø5 the master already drills, and a
cutter of 12 mm or less, of which the shop has at least two (tool `1002` at 12 mm and the 10 mm now
being used for the interpolation stopgap).

**Which means T016 is purely a software problem.** There is no tool to buy, no head to fit and no lead
time to wait out: the missing Ø5 entry in SmartCABINET's Cabineo X drill-head profile is a catalog
entry, and closing it is the whole job.

*One figure not established: which cutter diameter the master's pocket assumes. The pocket's arc
segments carry `#8017=7.50`, which reads as a 7.5 mm radius and would imply a 15 mm effective pocket
width — but that is a reading of a parameter, not a stated tool size, and a 15 mm-wide pocket cannot be
cut in one pass by a 12 mm cutter. **Worth confirming against the real toolpath before the first
production run**, because it decides whether the pocket takes one pass or two.*

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

This was written as a fork, and the owner's decision of 2026-09-19 picks the branch:

> **The range goes Cabineo X, so fixing T016 *is* the setup work.** It stops being a bug to squash and
> becomes step one of commissioning the fixing method — and, per the section above, a **software-only**
> step with nothing to buy.

*The caution that stood here — "a configured profile is not a decision" — was the right caution and is
now discharged by the owner rather than by the profile. Worth keeping the shape of it: the profile's
existence never was the evidence; it only pointed at where to ask.*

## The production route

**Panels are cut on the F45 and then drilled on the Vitap** — owner, 2026-09-19. This KB had no record
of it, and it matters to everything below:

- The Vitap is the **drilling station**, and it receives **individual panels**, not sheets. Every part
  in the master is well inside its 150–1250 mm width (the largest is the 862 × 300 side).
- So the Vitap's capacity is not a limit on the nesting, and **the panel is handled at the Vitap
  anyway** — which means an edge-drilling pass there is a step in a cycle the part already goes
  through, not an extra handling.

## The machine can do both — the edge-drilling argument does not apply here

The usual case for Cabineo is that it needs **no edge drilling**: it is machined entirely from the
panel face, so parts come off the machine in one setup. Confirmat needs a hole in the *edge* of the
mating panel, which on many shops means a second machine or a second handling.

**That argument does not apply to this workshop.** The Vitap's own KB article records:

> *"12 vertical spindles on Face 1, plus **horizontal spindle pairs on Faces 3-6**"*

So `FA2304` drills panel edges as well as faces, in the same machine — and, now that the route is
known, **on a panel that is already loaded there to be drilled**. **Confirmat's edge hole is not a
second operation here, and not even a second handling.** The strongest generic argument for Cabineo is
neutralised by the machine the shop already owns and the way the shop already works.

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

## What to do now the decision is made

1. **Close T016 — it is the only thing between here and a populated library.** Software-only: a Ø5 entry
   in SmartCABINET's Cabineo X drill-head profile, then a test run end to end. Nothing to order.
2. **Get a trade quote on the housing at 2,000**, and on the matching screw. £0.77 is a single-unit
   retail listing and it is the weakest figure in this article. *A purchase, so the owner's* (§6a).
3. **File the order paperwork when it arrives.** It settles the last identification question below —
   which Cabineo X variant and which screw were actually bought — and it is a Document Register item.
   *Also worth recording what confirmat size is in stock*, since Plan B depends on it and the stepped
   pilot differs between 7×50 and 7×70.
4. **Confirm the pocket's assumed cutter diameter** before the first production run (see the Ø15
   section). One pass or two is a cycle-time and a fit question.
5. **Separately, and unrelated to the connector: the 35 mm hinge-cup question.** The shop has the head;
   what went wrong with it is T027, and T016 is the obvious candidate.

**A mixed spec by design is still not worth pursuing** — confirmat through the carcase with Cabineo X
only on visible panels would cost two joint geometries maintained in one library for a few pounds a unit,
and Cabineo X leaves nothing visible anyway, so the appearance argument for mixing never existed.
**That is a different thing from Plan B**, which is one geometry with a fallback assembly method, and
costs nothing to keep.

## Costing — the wider point

Fixings are one line in a unit cost, and on these numbers not the biggest one. A unit cost model for
the range needs, at minimum: **board** (by sheet, with a real waste factor from the nesting),
**edging**, **fixings**, **hardware** (hinges, shelf supports, legs, handles, drawer runners on base
units), **machine time** and **assembly labour**. None of those are in this KB yet.

**The board line is the one to build first**, because it dominates and because the master's own
nesting files already carry the sheet size — **2800 × 2070 × 19**, cut on the F45. What is still
missing for it is the **yield**: how many units come off a sheet in practice, which depends on what the
saw operator actually works from (see Open questions).

## Open questions

- ~~**The nesting sheet does not fit the machine.**~~ — **answered by the owner 2026-09-19: panels are
  cut on the F45 and then drilled on the Vitap.** So the 2800 × 2070 sheet never goes near the Vitap,
  and its 1250 mm width limit was never a constraint: the Vitap only ever sees individual panels, the
  largest of which is the 862 × 300 side. **There was no contradiction — only a missing process fact.**
  See "The production route" above. *What it leaves open is a different question: the nesting files are
  **TpaCAD `.TCN`**, the Vitap's own format, and this KB's working answer is that the F45 takes
  dimensions rather than job files. So what the saw operator actually works from is unrecorded.*
- **Is a "LAMELLO" or "OVVO" aggregated head actually fitted to `FA2304`?** Both are listed as optional
  in the machine article; neither is confirmed present. One is made by Cabineo's manufacturer.
- **What Ø are the Vitap's horizontal spindles?** Needed to confirm confirmat's edge core hole is
  drillable without new tooling.
- ~~**Who chose Cabineo X — and was it a choice?**~~ — **answered by the owner 2026-09-19: it was chosen
  and the connectors are ordered.** The profile was never the evidence; it only pointed at where to ask.
- **Which Cabineo X variant and which screw were ordered?** The housing takes a Cabineo 8 or 12 screw or
  a shelf pin, and the choice affects the mating hole. **The order paperwork settles it** — and would also
  confirm, by part number, that the master's pocket really is a Cabineo X pocket rather than merely a
  compatible one.
- **Which cutter diameter does the pocket assume?** The arc parameter reads as a 7.5 mm radius, implying a
  15 mm pocket width, which a 12 mm cutter cannot cut in one pass. One pass or two is a cycle-time and a
  fit question — confirm before the first production run.
- **What confirmat size is in stock, and how many?** Plan B depends on it, and the stepped pilot differs
  between 7 × 50 and 7 × 70. Not recorded anywhere.
- **Does a Cabineo-drilled panel assembled with confirmat behave the same?** The pocket removes material
  from the side's inside face near the joint. Untested, and only matters if Plan B is used in anger.
- **What are the Ø10 × 13 holes** on the side panel — three at 32 mm pitch, 11 mm in from the back edge?
  Not identified. Possibly back-panel or cam fixings.
- **The trade price of the Cabineo X housing at 2,000** — the number the whole comparison turns on.
- **How many fixings does a whole unit actually take?** The eight carcase fixings are counted, from the
  side panel and confirmed against the bottom. **Back fixings are not identified** — the back is 19 mm
  and housed inside all four panels, and nothing decoded so far shows what holds it. Shelf pins are
  known (Ø5 at 32 mm pitch).
