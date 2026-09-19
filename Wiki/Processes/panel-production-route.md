---
title: "The panel production route (design → cut → edge → drill → assemble)"
category: Processes
status: active
sensitive: false
created: 2026-09-19
updated: 2026-09-19
sources:
 - "Owner (Minda), 2026-09-19: \"SmartCabinet optimization module create panel cutting list for F45; after cutting panels go through F4 for edging and then to Vitp. After it is on assembly desk to assembly\""
 - "Owner (Minda), 2026-09-19 (earlier): panels are cut on the F45 and then drilled on the Vitap"
 - "Owner (Minda), 2026-09-19: \"Cutting list for F45 is producing finished size panels. F4 before applying edging trimming panel on the thickness of edging before attaching edging itself\""
 - "`AMFA Wall Unit 600 RH/worklist.xmlst` (Drive `1uJ3LlrN6yWe9USvPIvJTa50SehARoTFh`), decoded 2026-09-18"
related:
 - ../Software/kitchen-unit-library.md
 - ../Processes/carcase-fixings-cabineo-x-vs-confirmat.md
 - ../Machinery/hebrock-f4-next-edge-bander.md
 - ../Machinery/altendorf-f45-panel-saw.md
 - ../Machinery/vitap-k2-panel-saw.md
---

# The panel production route

**The first time this KB has held the actual production flow.** Five sessions documented three
machines in detail — manuals, fault tables, maintenance schedules — without recording the order parts
move through them. The owner gave it on 2026-09-19, and it answers one open task, opens another, and
sharpens two things the KB already knew.

## The route

| # | Stage | Machine / place | Asset |
|---|---|---|---|
| 1 | **Optimisation** — produces the panel cutting list | SmartCABINET, design computer | software |
| 2 | **Cut** to size | Altendorf F45 sliding-table saw | `FA2303` |
| 3 | **Edge** | Hebrock F4 edge bander | `FA2301` |
| 4 | **Drill** (and rout) | Vitap K2-2.0 | `FA2304` |
| 5 | **Assemble** | assembly desk | — |

Owner's words: *"SmartCabinet optimization module create panel cutting list for F45; after cutting
panels go through F4 for edging and then to Vitp. After it is on assembly desk to assembly."*

## What this answers — Task T028

T028 asked what the F45 operator works from, given that SmartCABINET's nesting output is TpaCAD
`.TCN` — the *Vitap's* format — while every F45 document says the ElmoDrive takes dimensions, not job
files. Three readings were offered; **the second was right: SmartCABINET's optimisation module
produces a panel cutting list for the saw.** So the saw works from a cutting list, not from a `.TCN`.

*What is still not established is what becomes of the two `NESTING` `.TCN` files in the master
(`09-NESTING01-SP19-W1100`, `10-NESTING02-SP19-U963`). They are the optimiser's own output in the
Vitap's format, and on this route nothing consumes them. They may be a by-product, or the cutting list
may be generated from them. Not guessed — see Open questions.*

## Edging: the cut size **is** the finished size

Edging sits between cutting and drilling, which raises an obvious question — does a panel grow by the
tape thickness before it is drilled? **It does not, and the answer is better than a convention:**

> **The cutting list produces finished-size panels. The F4 trims the panel by the thickness of the
> edging before applying the edging itself.** — owner, 2026-09-19

So the bander is **dimension-neutral**. A panel arrives at the F4 at size *S*, is trimmed to *S − t*,
receives tape of thickness *t*, and leaves at *S*. **There is no allowance to carry anywhere** — not in
the cutting list, not in the library, not in the part files. The Vitap therefore drills a panel that is
the size the design says it is.

**Three consequences, and the second is the useful one.**

1. **It confirms the derived nominal.** The master's door is `896.0 × 597.0` in a 900 × 600 opening, and
   those being finished sizes means the gaps are real: **4 mm on height, 3 mm on width.** Sensible door
   gaps, and the 600 × 900 × 300 derivation stands.
2. **The cutting list does not need to know which edges are edged.** Trim-then-tape nets to zero on
   every edge independently, so a part edged on one edge and a part edged on four both come out at their
   listed size. **That is a real simplification for the library**: part dimensions are independent of the
   edging pattern, so a unit can be defined without it. *(The edging pattern is still needed for tape
   metres and F4 cycle time — see costing. It is just not needed for dimensions.)*
3. **It makes the F4 dimension-critical, and that is a standing caution.** The scheme only nets to zero
   while **the trim depth matches the tape thickness**. Change to thicker or thinner tape without
   re-setting the pre-mill and every panel comes out wrong — by twice the difference on a part edged on
   two opposite edges, and in the same direction on every part, so it would show up as a whole batch
   that does not fit rather than as one bad panel. **Tape thickness and trim setting are one decision,
   not two.** Worth knowing on a machine with a history of setup-sensitive faults (the corner-rounding
   incident, FL-001).

**A related field, now explained.** Every row of `worklist.xmlst` carries a column **`LASERCORR`**,
value **`0`** throughout. Whatever it corrects for, **zero is consistent with what the owner
describes**: trim-then-tape needs no per-part correction. *That the field relates to laser edgebanding
is a reading of its name and remains unverified — but nothing in the master exercises it either way.*

## What this sharpens — the shop is a serial line with no redundancy

Every panel passes through **`FA2303` → `FA2301` → `FA2304`, in series.** There is no second saw, no
second bander, no second borer. **Any one of the three going down stops the whole shop**, not a
fraction of it.

And all three are fed by **`FA2306`**, the ABAC compressor — already recorded as *"a single point of
failure for the whole workshop"*. The route makes that concrete rather than notional: it is not that
three machines happen to share an air supply, it is that **one air supply sits behind every stage of a
line with no parallel path.** `FA2306`'s service log has been blank since November 2023 (Task
**T020**).

**This has a maintenance consequence worth acting on:** the Maintenance Schedule treats the three
machines as peers. On a serial line they are not peers with anything — they are all critical, and so
is the compressor, which is not on the schedule at all because it has no manual.

## What this sharpens — the fixings decision gets cleaner

Edging before drilling could have been a problem for confirmat, which needs a core hole in a panel
**edge**. It is not, and the geometry says why.

In the master the **sides sit between top and bottom** (side length 862 = 900 − 2 × 19). So a side's
**end edges** meet the top and bottom panels' faces, and those end edges are **inside the joint and
therefore not edged** — only the front edge of a carcase panel needs tape. A confirmat core hole
would go into an unedged, hidden edge. **No conflict with stage 3, and nothing drilled through tape.**

Combined with what was already established — the Vitap has horizontal spindles on Faces 3–6, and the
panel is loaded there anyway — confirmat's edge hole costs nothing extra on this route. *The argument
against confirmat was never machining; it remains only that the master is drawn for a face-inserted
connector and re-drawing it is work.*

## What this gives costing

The route is the cost model's skeleton: **five stages, each with its own rate and its own consumable.**

*The edging stage is dimension-neutral but not cost-neutral: it consumes tape by the metre and F4
minutes by the edge.*

| Stage | Consumable | Time driver |
|---|---|---|
| Optimisation | — | design time per unit (once per library unit, not per job) |
| Cut | **board** — 2800 × 2070 × 19 sheets | cuts per sheet; yield |
| Edge | **edging tape**, by metre | edged perimeter per part |
| Drill | tooling wear | holes and pockets per part |
| Assemble | **fixings**, hinges, shelf pins | minutes per unit at the desk |

**Two of those can be computed from the files this KB already holds** once the edging question is
settled: the **edged perimeter per unit** (metres of tape) and the **hole/pocket count per unit**
(drill cycle). **Board yield cannot** — it needs the real sheet layout, which is the optimiser's, and
**assembly minutes cannot** — that needs somebody timing a unit at the desk.

*Design time belongs to the library, not the job.* It is the strongest argument for the library
existing: stage 1 is paid once per unit type rather than once per kitchen.

## Open questions

- ~~**Do the cutting-list dimensions include edging, or not?**~~ — **answered by the owner 2026-09-19:
  the cutting list is finished sizes, and the F4 trims by the tape thickness before applying it.** No
  allowance anywhere. See above.
- **Which edges are edged, on each part?** **No longer needed for dimensions** (see consequence 2
  above), but still needed for the **tape metres** in a cost model and for F4 cycle time. The carcase
  convention (front edges only) is the obvious reading but is **not recorded**.
- **What is the pre-mill trim set to, and what tape is it set for?** The two must match. Nothing records
  either, and they are one decision rather than two.
- **What consumes the two `NESTING` `.TCN` files?** Nothing on this route appears to. Are they a
  by-product of the optimiser, the source the cutting list is generated from, or vestigial?
- **What form does the cutting list take** — printed, on screen, a CSV? The SmartCABINET release notes
  mention a custom CSV export splittable by material, which would fit.
- **What tape, and what thickness?** Material, thickness and colour range are all unrecorded, and the
  thickness is what the first question turns on.
- **Assembly minutes per unit** — nobody has timed it, and it is the only labour line in the model.
- **Does the Hebrock's schedule reflect that it is in every panel's path?** See the serial-line point
  above; this is a judgement for whoever owns the Maintenance Schedule, not a change made here.
