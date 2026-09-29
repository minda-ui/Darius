---
title: "The shop's Cabineo joint, reconciled against SmartCabinet's own parameters"
category: Processes
status: active
sensitive: false
created: 2026-09-28
updated: 2026-09-28
sources:
 - "`AMFA Wall Unit 600 RH/01-SIDE-LEFT.TCN` (Drive `1ZWciFvdK2rkKbeWvRpNQ825UWJsnnPe1`, 21,020 B) — re-fetched and re-decoded 2026-09-28, UTF-16LE, every working parsed by script rather than read by eye"
 - "`AMFA Wall Unit 600 RH/03-BOTTOM.TCN` (Drive `1ygANqYNEfpT7-q7TNkfm-hhllShoZ62m`, 2,036 B) — same"
 - "`../Software/smartcabinet-online-manual.md` §7 — the `giunzioni` page's Cabineo parameter list, captured 2026-09-28"
 - "`../Processes/carcase-fixings-cabineo-x-vs-confirmat.md` — the connector decision, the volume prices and the eight-per-box count"
 - "Owner (Minda), 2026-09-28: *\"reconcile the manual's Cabineo parameters with the TCN geometry\"*"
related:
 - ../Software/smartcabinet-online-manual.md
 - ../Processes/carcase-fixings-cabineo-x-vs-confirmat.md
 - ../Processes/tpacad-tool-match-criteria.md
 - ../Software/kitchen-unit-library.md
 - ../Machinery/vitap-k2-drill-head-tooling.md
 - ../Software/tcn-to-smartcabinet-reversibility.md
---

# The shop's Cabineo joint, reconciled against SmartCabinet's own parameters

**Two descriptions of the same joint existed in this KB and had never been put side by side.** One is
SmartCabinet's `giunzioni` page — what the software *lets you configure* — captured 2026-09-28. The other is
the master unit's own `.TCN` files — what the shop *actually cut*. This article reconciles them,
parameter by parameter.

**The short answer: eleven of the manual's parameters reconcile against measured numbers, one contradicts,
and the manual's central block — the three elements' diameters and lengths — does not describe the geometry
the master contains at all.** *That last is the finding worth having, and it was not predictable from either
source alone.*

**And one thing the reconciliation proves rather than assumes:** the manual says cutters must be named in
CAM Tools while drill bits are chosen by the machine. **The master's own files do exactly that** — every
routed operation carries a tool field, every bore carries `#1001=0`. See §4.1.

## 1. What was measured, and how

**Both files were re-fetched from Drive and re-decoded**, not quoted from the articles that describe them.
They are **UTF-16LE** text with a `TPA\ALBATROS\EDICAD\01.00` header, and **every working was parsed by
script** — 127 workings in the side, 7 in the bottom — so the numbers below are computed, not read off.

| Part | Drive id | Bytes | Panel | Workings |
|---|---|---|---|---|
| `01-SIDE-LEFT.TCN` | `1ZWciFvdK2rkKbeWvRpNQ825UWJsnnPe1` | 21,020 | 862 × 300 × 19 | 28 × `W#89` profile starts, 64 arcs, 20 lines, 11 bores, 4 macro calls |
| `03-BOTTOM.TCN` | `1ygANqYNEfpT7-q7TNkfm-hhllShoZ62m` | 2,036 | 600 × 300 × 19 | 7 bores, nothing else |

**One trap found immediately, and it is not about Cabineo.** Both files label their machined face
`$=sopra` — *"above"*. **It names the face, not the part**: `03-BOTTOM.TCN` says `sopra` too. *A future
session reading `$=sopra` in a file called `03-BOTTOM` and concluding it is the top would be wrong, and the
mistake is one character wide.*

**Only `SIDE#1` carries anything.** `SIDE#2`–`SIDE#6` are present and empty in both files, which is the
face-only machining this KB already recorded — re-confirmed rather than carried forward.

## 2. The master's Cabineo joint, measured

**Coordinates.** On the side panel, `X` runs along the 862 height (X = 0 and X = 862 are the ends that meet
the bottom and the top) and `Y` along the 300 depth. **Y = 0 is the front**, and that is cross-checked two
independent ways rather than assumed: the Ø3 hinge-plate pilots sit at Y = 37, and the back-fixing row sits
at Y = 276.9 — front hardware forward, back hardware aft.

### 2.1 The pocket is three overlapping Ø15 circles, cut twice

Each element of the pocket is a **closed circle of Ø15**, written as two semicircular arcs
(`#8017=7.50`) sharing a diameter — *not* a slot. **Three of them at an 11.2 mm pitch** make one pocket:

| | X = 0 end | X = 862 end |
|---|---|---|
| circle centres | 3.6 · 14.8 · 26.0 | 836.0 · 847.2 · 858.4 |
| pocket extent | **−3.9 … 33.5** | **828.5 … 865.9** |
| length | **37.4** | **37.4** |
| width (Y) | **15.0**, centred on the axis | **15.0** |
| depth | **13.0**, in **two passes: −6.5 then −13.0** | same |

**So the pocket is 37.4 × 15.0 × 13.0 deep**, and this **confirms** the 37 × 15 × 13 figure this KB has
carried since 2026-09-18 rather than correcting it. *The three circles were the thing worth re-deriving: read
as slots they would have given a 52 mm pocket, and the arcs are closed circles.*

**It opens onto the end edge.** The outermost circle runs from X = −3.9, so **3.9 mm of it is cut in air**.
That is the screw's exit, and it is why the joint needs no edge machining.

**Four pockets per side panel** — two ends × two axes (Y = 40 and Y = 230) — which is the **eight carcase
fixings per box** already counted, re-derived from the file.

### 2.2 There is a second, shallower recess nobody had recorded

Concentric-ish with each pocket is a **2.1 mm deep stadium, 45.0 long × 18.9 wide** (`#8017=9.400`), four
of them, one per pocket:

| | X = 0 end | X = 862 end |
|---|---|---|
| extent | −9.4 … 35.6 | 826.4 … 871.4 |
| length × width × depth | **45.0 × 18.9 × 2.1** | same |
| centre | X = 13.1 | X = 848.9 |

**It is wider than the pocket (18.9 vs 15.0), reaches 2.1 mm further into the panel (35.6 vs 33.5), and
overhangs the end edge further (9.4 vs 3.9).** *It is not concentric: its centre sits 1.7 mm nearer the end
than the pocket's.* **This feature is absent from every existing article in this KB** — the 2026-09-18 decode
recorded the pocket and not the recess.

*One cosmetic note, because it looks like a discrepancy and is not: the recess measures 18.95 at Y = 40 and
18.90 at Y = 230. The file writes 49.450/49.50 and 239.450/239.45 — **file rounding, not two different
features.***

### 2.3 The mating hole, and where the screw axis actually sits

`03-BOTTOM.TCN` carries **Ø5 × 12 mm** bores at **X = 11.9 and 588.1** (11.9 from each outer face of a
600 mm panel), at **Y = 40 and Y = 230** — the same two axes as the side's pockets, position for position.

**So the screw axis lies 11.9 mm from the side panel's outer face, and 7.1 mm from its machined face.**
*Which face is machined is a reading, not a measurement — the file does not say. It must be the inner face,
or the connector would be visible outside, which is the one thing Cabineo is for.*

**And therefore the joint is not centred in the panel thickness.** Half of 19 is 9.5; the axis is at 7.1,
**2.4 mm off centre toward the machined face**. The pocket is 13.0 deep, leaving 6.0 mm of board, and the
axis at 7.1 sits inside the pocket void — all three numbers consistent.

## 3. The reconciliation

**Manual parameter → measured value → verdict.** The manual's numbering (➊⓫⓬…) is as captured in
`../Software/smartcabinet-online-manual.md` §7.

| Manual parameter | Measured in the master | Verdict |
|---|---|---|
| **Number of joints ⓮** | **2** per joint line (Y = 40, Y = 230) | **Reconciles** |
| **Distance from the front ⓬** | **40.0** mm | **Reconciles** |
| **Distance from the back ⓭** | **70.0** mm (300 − 230) | **Reconciles** — *and the two differ, which is the point of having both* |
| **Offset to avoid conflicts between opposing joints ⓯** | **0** — both sides' pockets and the bottom's holes share Y exactly | **Reconciles, unexercised** — there are no opposing joints in this unit |
| **Internal screw diameter ➏** | **Ø5** | **Reconciles** |
| **Hole length, structure ➐** | **12.0** mm | **Reconciles** |
| **Hole length, back ➒** | **12.0** mm (the Y = 276.9 row — see §4.3) | **Reconciles, but equal to the structure's** |
| **Hole length, dividers ➑** | **absent** | **Unexercised — the master has no divider** |
| **Number of passes ➎** | **2** — every circle cut at −6.5 then −13.0 | **Reconciles** |
| **Support base: length, width, thickness ⓫** | **45.0 × 18.9 × 2.1** | **Reconciles — and this is the best match in the table** (§2.2) |
| **Central pin's distance from the top** (black) | **7.1** mm from the machined face | **Reconciles** |
| **`Aggiungi metà spessore pannello`** (centre in the thickness) | **not used** — 7.1 against a 9.5 half-thickness | **Reconciles as "off"** |
| **Tool, per element and for the base ➎ ⓫** | **one tool for everything**, `#205=1002` on all 28 profile starts | **Partly** — the software allows a tool per element; the master uses one |
| **Three elements' diameters ➌ and effective lengths ➍** | **three Ø15 circles at 11.2 pitch, all identical** | ***Does not reconcile*** — see §4.2 |
| **Joint type / specific joint ⓰ ⓱** | not representable in a `.TCN` | **Not reconcilable from this evidence** |
| **Database ⓬ / `Anagrafica Accessori`** | not representable in a `.TCN` | **Not reconcilable from this evidence** |

## 4. The four findings that matter

### 4.1 The manual's claim about tools is confirmed by the master's own files

The manual says, from two directions, that **cutters must be entered in CAM Tools and named, while drill
bits are normally chosen by the machine** — *"qualora non sia impostato alcun utensile verrà selezionata
automaticamente una punta."*

**The master does exactly that.** Every routed operation carries a tool field (`#205=1002`); **every bore
carries `#1001=0`** — no tool named. Ø5, Ø3, Ø10 and the macro's Ø5 rows alike.

***This is the first time this KB has confirmed the manual against the shop's own output rather than
against another page of the manual.*** It also settles, from the evidence side, what the manual settled from
the documentation side: **`#1001=0` on every hole is the designed behaviour, not a defect** — which is
T016's *systemic half* closing for the second time, independently.

*One caution kept rather than glossed: `#205=1002` **reads** as tool 1002, and this KB elsewhere records tool
`1002` as a 12 mm cutter. But `#1002` is also the **diameter** parameter on a bore, so the number 1002 appears
in this KB meaning two different things, and `#205`'s meaning is **not** established from these files. If it
is a 12 mm cutter, then **a Ø15 circle cannot be plunged and must be interpolated** — which sharpens the
article's existing open question rather than answering it.*

### 4.2 The manual's Cabineo block does not describe this pocket

The manual's Cabineo configuration is **three elements of different diameters and effective lengths,
stacked, counted from the end opposite the screw exit** — the geometry of a **stepped bore**.

**The master's pocket is three circles of the same Ø15 at an 11.2 mm pitch, side by side along the panel** —
the geometry of a **routed pocket**. Same number, different kind. *Three elements and three circles is a
coincidence of the number three, and it would be easy to write a reconciliation that pretended otherwise.*

**Two explanations, and this evidence does not choose between them:**

1. **The shop's joint is not configured as Cabineo proper.** The manual's own category is *"Giunzioni
   eccentriche e Cabineo"* and explicitly also carries *"le giunzioni laterali e i supporti per i ripiani
   Lamello, Clamex e Divario"* — so a routed pocket may be a different member of the same category.
2. **A page beyond the ten captured describes the routed form.** The hub is known not to be an exhaustive
   index, and `intagli` — the notch window `Personalizza Giunzioni` opens from — has never been fetched.

**What settles it is one look at `Configurazione Giunzioni` on the design PC**, which §7.6 of the manual
article already named as unread.

### 4.3 The back fixings are located, and the reading of them is flagged

This KB has said since 2026-09-18 that *"back fixings are extra and not yet identified"*. **There is a row
that fits**, and it is the same spec as the carcase screw hole — **Ø5 × 12** — on both parts:

- side, four: **X = 50 · 304 · 558 · 812, Y = 276.9**
- bottom, three: **X = 69 · 300 · 531, Y = 276.9**

**Same Y on both parts, 23.1 mm in from the back edge.** *That it is the back fixing is a **reading**, and
one geometric objection is recorded rather than suppressed: 23.1 mm does not put the hole on the
mid-thickness of a 19 mm back at any obvious position, so either the back is not flush at the rear or these
holes are something else.* **Confirming it needs the back panel's own `.TCN`, which has not been decoded.**

*If it is the back, then this master sets the **back** hole length equal to the **structure** hole length —
12 mm both — even though the software keeps them as separate parameters.*

### 4.4 T016's blind Ø3 holes, finally located and counted

**Four Ø3 × 5 mm blind bores, at Y = 37, X = 67 · 99 and 763 · 795** — two pairs at 32 mm centres, one pair
near each end, close to the front edge. **That is a hinge mounting-plate pattern**, and it is the blind Ø3
this KB has discussed since 2026-09-15 without ever saying where it is or how many there are.

*Four per side, eight per unit — so the blind-Ø3 decision the owner holds (re-spec, or buy a blind Ø3 bit)
is eight holes a unit, not an incidental one.*

**Also measured, and still unidentified:** **three Ø10 × 13 bores at X = 71 · 103 · 135, Y = 289.0** — 32 mm
pitch, 11 mm from the back edge. ***The new fact is that they are at one end only.*** Back-panel or cam
fixings would be at both; three at one end is not that. *Recorded as still open, with the asymmetry as the
new evidence.*

## 5. What this gives the divider — the owner's question, one step on

`../Processes/carcase-fixings-cabineo-x-vs-confirmat.md` records that a divider is the same Cabineo joint
with its own configured hole length. **This pass supplies the numbers it would have to match:**

| For a divider, set | From this master |
|---|---|
| screw Ø | **5** |
| hole length in the divider ➑ | **unset today** — the structure's is 12.0, and 12 mm in 19 mm board is what the Cabineo 12 screw wants |
| pocket | **37.4 × 15.0 × 13.0**, three Ø15 circles at 11.2 pitch, two passes |
| support base | **45.0 × 18.9 × 2.1** |
| pin from the machined face | **7.1** |
| joints per line ⓮ | **2** |
| front ⓬ / back ⓭ | **40.0 / 70.0** |
| **offset ⓯** | **0 today — and this is the one that must change** |

***And the offset is narrower than it first looks — which is worth saying, because the fixings article
reaches for it.*** ⓯ is for **opposing** joints. A centre divider's screw holes land in the top and bottom at
its own X, and the sides' land at **X = 11.9 and 588.1**; on a 600 mm unit those are nowhere near each other,
so **a centre divider probably creates no collision at all** and ⓯ stays at 0.

**Where it does bite is the panel thickness, and there the arithmetic is unforgiving.** Every pocket measured
here is **13.0 deep in a 19.0 panel, leaving 6.0 mm**. So:

- **A divider taking shelf supports on both faces at the same height cannot have them**: two 13 mm pockets
  back to back need 26 mm of a 19 mm panel. ⓯ — or a height offset — is not optional there, it is the only
  way it works.
- **A divider close to a side** would bring the two sets of top/bottom holes together in plan, and that is
  ⓯'s in-plane case.

*That correction is mine against my own write-up of this morning, which named ⓯ as "the parameter that
matters here" without asking whether a centre divider actually collides with anything. **It probably does
not** — and the real constraint is the 6 mm of board left behind a pocket, which no article in this KB had
stated.*

## 6. Open, and how to close each

1. **What `#40` and `#205` mean.** `#40=1` on the pockets, `#40=2` on the base recesses — different tool
   compensation, presumably, which decides whether 15.0 is the **path** or the **finished width**.
   ***Closeable from a document the shop already owns***: `Workings_eng.pdf` (337 pp) in
   `C:\Albatros\help\en-GB\`, found on 2026-09-23.
2. **The 1.5 mm the pocket may be short.** This KB records Cabineo X as **33.8 × 16.5 × 10.8**; the pocket
   measures **37.4 × 15.0 × 13.0**. Length and depth are generous, **width is 1.5 mm under**. *Either the
   published width is wrong, the pocket is compensated wider than its path (item 1), or the pocket is not
   Cabineo X's.* **Recorded as a contradiction, not resolved** — a tape measure on one connector settles it.
3. **Which joint family the shop has configured** — §4.2. One look at `Configurazione Giunzioni`.
4. **Whether the Y = 276.9 row is the back fixing** — §4.3. Decode the back panel.
5. **The three Ø10 × 13 at one end** — §4.4.
6. **`WO=1`** appears on the bottom's X = 588.1 pair and on neither of the X = 11.9 pair. *Unexplained; noted
   because an unexplained flag on exactly half a symmetric pair is the kind of thing that turns out to matter.*
7. **Cutter diameter for a Ø15 circle** — the existing open question, now sharpened by item 1 rather than
   answered. **The depth half of it is answered: two passes of 6.5 mm.**

*No part of this article was taken from another article's description of these files. Where a number also
appears elsewhere in this KB it was re-derived, and §2.1 is a case where re-deriving changed the reasoning
while confirming the figure.*
