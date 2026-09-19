# Change log — 2026-09-19 — The production route recorded at last, the edging question closed, and a wrong inference of mine withdrawn

**Session 16.** No documents arrived. Everything here came from four short statements by the owner, and
between them they closed **three tasks**, opened **one**, corrected **one of mine**, and gave the KB a
fact it had gone five sessions without: **the order parts move through the shop.**

---

## The route — and why its absence mattered

> *"Panels are cut on F45 and then drilled on Vitap."*
> *"SmartCabinet optimization module create panel cutting list for F45; after cutting panels go through
> F4 for edging and then to Vitp. After it is on assembly desk to assembly."*

| # | Stage | Machine | Asset |
|---|---|---|---|
| 1 | Optimisation → panel cutting list | SmartCABINET | software |
| 2 | Cut | Altendorf F45 | `FA2303` |
| 3 | **Edge** | Hebrock F4 | `FA2301` |
| 4 | Drill / rout | Vitap K2-2.0 | `FA2304` |
| 5 | Assemble | assembly desk | — |

**Five sessions documented three machines in detail** — manuals, fault tables, maintenance schedules,
re-commissioning requirements — **without recording the order they are used in.** The same shape as the
unregistered compressor: a gap invisible from inside the KB, because nothing in it pointed at the thing
missing. Recorded in a new article, `Wiki/Processes/panel-production-route.md`.

### T026 closed — there was no contradiction, only a missing process fact

Yesterday's open item was that the master's nesting sheets are **2800 × 2070** while the Vitap's
recorded panel capacity is **150–1250 mm wide** — 820 mm over. Three readings were offered and none
picked. **The first was right: the sheet is cut on the F45.** The Vitap only ever receives individual
panels, the largest of which is the 862 × 300 side, comfortably inside its range.

**Two sourced figures that appear to conflict can both be right, with the conflict living in an
unrecorded process step rather than in either number.** Worth keeping as the example.

### T028 closed — the saw works from a cutting list

Raised yesterday because SmartCABINET's nesting output is TpaCAD `.TCN`, the *Vitap's* format, while
every F45 document says the ElmoDrive takes dimensions rather than job files. Of the three readings
offered, **(b) was right**: the optimisation module produces a **panel cutting list** for the saw.

*Still not established, and deliberately not guessed: what consumes the two `NESTING` `.TCN` files.
Nothing on this route appears to. And what form the cutting list takes — printed, on screen, or the CSV
export the release notes mention.*

---

## The edging question, opened and closed the same morning

**Edging sits between cutting and drilling.** That is the right order — drilling after edging avoids
holes full of glue and tape — but it means a panel grows by the tape thickness *before* it is drilled,
so every dimension in the cutting list is either a cut size or a finished size. `worklist.xmlst` does
not say which, and **getting it wrong is systematic**: every unit oversize, or every door tight, in
exactly the same way. Raised as **T029**.

The plausibility arithmetic pointed one way — a 1 mm tape on all four edges of the 896 × 597 door
leaves 1 mm of total width gap, a door that binds — but that is plausibility, not a fact, so it was
recorded as an open question with a two-minute close: measure a finished door.

**The owner's answer is better than either option the task allowed for:**

> *"Cutting list for F45 is producing finished size panels. F4 before applying edging trimming panel on
> the thickness of edging before attaching edging itself."*

**The bander is dimension-neutral.** Panel in at *S*, trimmed to *S − t*, gains *t* of tape, leaves at
*S*. **There is no allowance to carry anywhere.**

**Three consequences:**

1. **It confirms the derived nominal.** The door's 4 mm and 3 mm gaps are real gaps, not figures with
   tape hidden in them. `600 × 900 × 300` stands.
2. **The cutting list does not need to know which edges are edged.** Trim-then-tape nets to zero on
   every edge independently. **A library unit can therefore be defined without its edging pattern** —
   a real simplification.
3. **It makes the F4 dimension-critical.** The scheme only nets to zero while **trim depth matches tape
   thickness**. Change tape without re-setting the pre-mill and every panel is wrong, by twice the
   difference on a two-edge part, in the same direction — **failing as a whole batch that does not fit,
   not as one bad panel.** Tape thickness and trim setting are one decision, not two. Worth knowing on
   a machine with FL-001 in its history.

**`LASERCORR = 0`** on all eleven rows is now *consistent* rather than merely unexercised: trim-then-tape
needs no per-part correction. *That the field relates to laser edgebanding remains a reading of its name.*

**What remains of T029 has moved to costing:** which edges are edged (tape metres, F4 minutes), and what
the pre-mill is set to and for which tape. Neither is recorded.

---

## A correction: the shop has the 35 mm head, and I should not have said otherwise

**T027 said the shop appeared not to have a 35 mm hinge-cup bit and that buying one was the action. That
was wrong.**

> *"I have on Vitap 35mm drilling head. I had a problem."*

How it happened: on 2026-09-18 the owner asked how to cut a 35 mm hinge hole with a 12 mm cutter, and
decoding `08-DOOR-1.TCN` showed the door already programs the cup as a Ø35 bore. I concluded the Ø35
tool must be absent. **Asking how to do something another way is not evidence that the ordinary way is
unavailable** — what the owner actually said was that there was a problem. Same family as the six
unsourced inferences already withdrawn in this KB.

**T027 is now "what was the problem with the 35 mm head?"** — still open, and the useful part. The
obvious candidate is **T016**: the door programs each cup as `#1002=35` with `#1001=0`, a Ø35 bore with
no tool assigned, and a head that exists physically but has no CN Tools entry would fail exactly as
*"Tool for this working not found"* — looking, from the operator's side, like a machine refusing a hole
it plainly has the tool for. **Not asserted.** The owner has not said, and this KB had just been caught
doing precisely this kind of guessing.

### The live question behind it, answered

> *"I have ordered 10mm and 12mm drills, but they not arrived. So I was thinking about plan B. To use
> 10mm cutter to create 12mm holes in panel."*

**Toolpath circle diameter = finished hole diameter − cutter diameter.** So Ø12 from a Ø10 cutter is a
**2 mm orbit**, and Ø10 from the same cutter is a **straight plunge** — **one tool covers both sizes**
while the drills are out. Written up as `Wiki/Processes/tpacad-interpolated-holes.md` with the four
things that decide whether it works: it must be the pantograph and not a boring spindle; helix in rather
than plunge at full diameter; the bottom is flat not conical; and it is much slower per hole.

**And it is the cheapest possible case in which to settle the `Diameter`-field ambiguity** that has been
open since yesterday. A wrong reading here gives **22 mm instead of 12** — unmistakable on scrap —
against the 35 mm case where a wrong reading gives 47 mm and a ruined door. One test cut settles the
convention permanently, for every hole and every cutter.

---

## Drive sync debt cleared

Five items had been running ahead of Drive and were brought level on request, each verified with
`wc -c` against Drive's reported size:

| File | Bytes | Note |
|---|---|---|
| `Wiki/Processes/carcase-fixings-cabineo-x-vs-confirmat.md` | 18,734 | clears two stale clauses carried for a day |
| `Wiki/Processes/barcode-and-scan-event-system.md` | 13,837 | Drive's copy predated the QR answer entirely |
| `Wiki/index.md` | 10,311 | and the Processes section put back into alphabetical order |
| `Wiki/Processes/panel-production-route.md` | 10,101 | new |
| `Wiki/Processes/tpacad-interpolated-holes.md` | 6,930 | new |
| `Wiki/Software/kitchen-unit-library.md` | 15,965 | — |

**Two things were found stale in the barcode article while syncing it**, and fixed rather than shipped:
label `0017` still read *"not registered, no code"* when its machine has been `FA2306` since 2026-09-18,
and the `Changes` table had no 2026-09-18 row at all. **The narrative layer drifts quietly when the
correction lands somewhere else** — the same lesson as the Smartsheet note on T016, arriving from the
other direction.

**One divergence was found in the opposite direction.** Uploading the index came back 476 bytes *larger*
than local, because the Processes entries had been re-ordered alphabetically while pasting — which the
file's own rule requires. Local was synced **up** to Drive rather than Drive down to local.

---

## Still open at session end

- **T025 — the fixing decision.** Was Cabineo X chosen, or did it arrive by default? Nothing records a
  decision, a purchase or a trial. Everything else about the library waits behind this and T016.
- **T016** — now understood as the Cabineo X tooling being half-defined, and a precondition for the
  library rather than one machine's fault.
- **T024 — shelf depth 255 / 256 / 266 mm** across three 300 mm-deep carcases.
- **T027 — what was the problem with the 35 mm head?**
- **T029's remainder** — which edges are edged; the pre-mill setting and the tape it is set for.
- **Four of the five unit types have no master at all.** The owner's range is wall, base, sink,
  appliance housing and tall; only the wall unit exists.
- **`Outputs/kb-registers.md`** processed-items rows and this file's index entry — done in this session.
