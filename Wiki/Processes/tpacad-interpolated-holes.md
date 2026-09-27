---
title: "Making holes with a cutter instead of a drill (TpaCAD interpolation)"
category: Processes
status: active
sensitive: false
created: 2026-09-19
updated: 2026-09-19
sources:
 - "Owner (Minda), 2026-09-19: has a 35 mm drilling head on the Vitap; 10 mm and 12 mm drills ordered but not arrived; proposes using a 10 mm cutter to make 12 mm holes"
 - "TPA CAD manual extract (both parts), `CIRCULAR INTERNAL WINDOW` under `CUSTOM WORKINGS: PROFILES` — 'a circle with internal emptying'"
 - "`AMFA Wall Unit 600 RH/01-SIDE-LEFT.TCN` and `08-DOOR-1.TCN`, decoded 2026-09-18"
related:
 - ../Processes/tpacad-tool-type-optimizer-ambiguity.md
 - ../Processes/panel-production-route.md
 - ../Machinery/vitap-k2-panel-saw.md
---

# Making holes with a cutter instead of a drill

A working note for the shop, written 2026-09-19 because the 10 mm and 12 mm drills were on order and
had not arrived. **The method is sound and it is standard practice**, not a bodge — but there are four
things that decide whether it produces a 12 mm hole or a 22 mm one.

## The arithmetic

A cutter removes material equal to its own diameter as it travels. So:

> **toolpath circle diameter = finished hole diameter − cutter diameter**

| Want | With cutter | Toolpath circle | Radius |
|---|---|---|---|
| **Ø12** | **Ø10** | **Ø2** | **1 mm** |
| Ø10 | Ø10 | **none — straight plunge** | 0 |
| Ø35 | Ø10 | Ø25 | 12.5 mm |
| Ø35 | Ø12 | Ø23 | 11.5 mm |

**One tool covers both sizes currently needed.** A 10 mm cutter plunged straight down gives **exactly
Ø10**; the same cutter orbiting a 2 mm circle gives **Ø12**. So while the drills are out, the 10 mm
cutter can do the Ø10 holes *and* the Ø12 holes — which is worth knowing, because the master's side
panel already carries Ø10 holes (three at 32 mm pitch, 13 mm deep) as well as Ø3 and Ø5.

## The one thing that will bite

**The TpaCAD manual extract this KB holds never states whether `CIRCULAR INTERNAL WINDOW`'s
`Diameter` field is the finished hole or the toolpath circle.** That ambiguity was flagged on
2026-09-18 for a 35 mm cup and it is unresolved (Task **T015** — the complete manual is on the shop's
Albatros PC and has not been fetched).

With a 10 mm cutter and a 12 mm target, the two readings are:

| If `Diameter` means | Enter | Wrong entry gives |
|---|---|---|
| the **finished hole** | `12` | entering 2 → a **12 mm hole from a 2 mm path**… i.e. a Ø2 path is inside the cutter, so it cuts Ø10 |
| the **toolpath circle** | `2` | entering 12 → **Ø22** |

**This is the cheapest possible case to test, and that is the point.** A wrong reading gives **22 mm
instead of 12 mm** — nearly double, unmistakable at a glance, on a piece of scrap. Compare the 35 mm
case, where a wrong reading gives 47 mm and you have already ruined a door.

> **Cut one 12 mm hole in scrap and measure it.** That single test settles the `Diameter` convention
> **permanently**, for every hole and every cutter, including the 35 mm cup. It is the highest-value
> two minutes available on this machine.

## Four practical points

1. **It must be the router/milling spindle, not a boring spindle.** Interpolation needs simultaneous
   X-Y motion. The Vitap's boring spindles plunge on Z only; the **pantograph milling unit** is what
   can drive a circle. A 10 mm cutter sitting in a boring position can only ever give a 10 mm hole.
2. **Do not plunge straight down at full diameter unless the cutter is rated for it.** A 2 mm orbit
   means the cutter must first get to depth. Straight-plunging a two-flute straight bit into 19 mm
   board burns the bottom and loads the tool. **Ramp or helix in** — enter at the centre and spiral
   down to depth, then take the 1 mm radial pass. On a Ø2 orbit there is very little room to ramp, so
   a helical entry at the centre before offsetting is the clean way.
3. **The bottom will be flat, not conical.** A drill leaves a brad-point or conical bottom; a cutter
   leaves a flat one. For a dowel, a connector body or a shelf pin this is fine or better. Check
   nothing relies on the point — and check the **depth** is measured the same way (13 mm deep means
   13 mm of full-diameter hole, which a flat bottom gives and a drill point does not).
4. **It is much slower than drilling.** A drilled hole is one plunge; an interpolated hole is a plunge
   plus a circle, per hole. Fine for a handful. If a panel carries a dozen Ø12 holes, the cycle time
   difference is real — this is a stopgap until the drills arrive, not a reason to cancel the order.

**Accuracy should be good here.** At Ø12 from a Ø10 cutter the radial engagement is only 1 mm, so
deflection is minimal — far less than interpolating a 35 mm hole with the same tool. Measure the first
one anyway: interpolated holes tend to come out a few hundredths off nominal depending on runout, and
a dowel hole that is 0.2 mm oversize is a loose joint.

## What this corrects

**A task raised on 2026-09-18 (T027) said the shop appeared not to have a 35 mm hinge-cup bit.** That
was wrong. **The owner confirms a 35 mm drilling head is fitted to the Vitap** (2026-09-19).

The error was a specific and familiar kind: the owner had asked how to cut a 35 mm hinge cup with a
12 mm cutter, and I read that as evidence the 35 mm tool did not exist. **Asking how to do something
another way is not evidence that the ordinary way is unavailable** — it is evidence of a problem,
which is what the owner actually said (*"I had a problem"*). The tool was there; something about using
it was not working. §3's rule applied here: if it was not read off a document or stated by someone who
knows, say so.

**What the problem with the 35 mm head actually was is still unrecorded**, and it is worth knowing,
because the obvious candidate is Task **T016** — the *"Tool for this working not found"* fault. The
door file programs each cup as `#1002=35` with `#1001=0`, i.e. **a Ø35 bore with no tool assigned**. A
35 mm head that exists physically but has no matching CN Tools entry would fail in exactly that way,
and would look, from the operator's side, like a machine that will not cut a hole it plainly has the
tool for. **Not asserted — the owner has not said what the problem was.**

## Open questions

- **Does `Diameter` mean the finished hole or the toolpath?** One scrap cut answers it for every
  working and every tool (T015 covers the manual that would also answer it).
- **What was the problem with the 35 mm drilling head?** If it was "tool for this working not found",
  it is T016 and the fix is a catalog entry, not a workaround.
- **Where are the Ø12 holes in the range?** The parts decoded so far carry Ø3, Ø5, Ø10 and Ø35 — no
  Ø12. So the 12 mm requirement comes from a part or a unit this KB has not seen.
- **Which spindle is the 10 mm cutter in** — the pantograph, or a boring position? Only the former can
  interpolate.
