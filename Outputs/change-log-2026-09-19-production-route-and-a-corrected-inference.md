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

**And the article counts were wrong a fourth time.** This session's own registers and outstanding-items
list were drafted with 29 and 27 when `git ls-files` says **30**, twelve of them in the mirror. Both
corrected before upload, and the outstanding-items list now proposes the structural fix — **drop the
figure from `CLAUDE.md` and point at the registers instead** — because a number that changes every time
an article is written does not belong in a document revised weekly. *The eighteen Drive-only figure has
never drifted, because articles go to both stores in step; it is only the totals that rot.*

**Flushed a second time at session end**, after the T025 and T024 answers had moved three files again:
`carcase-fixings-cabineo-x-vs-confirmat.md` (**23,154**), `kitchen-unit-library.md` (**19,380**) and
`2026-09-19-outstanding-items.md` (**17,922**) — archive-then-create each, every upload byte-exact.
**The 60 KB of re-uploads were deliberately held** while the owner was mid-flow answering questions,
and stated as held rather than done quietly; a batched flush on request beats interrupting a run of
answers three times.

---

## T010 closed on instruction

The owner: **"T010 yes"** — closing the task the outstanding-items lists of both 2026-09-18 and
2026-09-19 had flagged as answered and ready.

T010 was *"review `FA2302` (Inventair MK1 MTFA) status once the new centralised extraction unit's manual
arrives"*. It closes because **both Inventairs were sold** (owner, 2026-09-17), so there is no status
left to review — and because the premise was wrong in a more interesting way: the centralised unit is
neither of them, it is **`FA2402`**, a third machine this KB had never heard of.

**The row is worth keeping for what its own note did right.** On 2026-09-15 it recorded the
"`FA2305` supersedes `FA2302`" idea as *plausible and NOT confirmed either way* rather than asserting
it. The answer turned out to be **neither** — both sold, both replaced by a machine not on the register
— so **nothing had to be unpicked**: no status, no date and no relationship had been set on a guess.
That is the §3 lesson *don't assume one finding resolves another just because they're related*, and
this is the row that earned it. The original wording is preserved verbatim inside the closing note so
the close can be checked rather than taken on trust.

**Nothing about `FA2302`'s own open items changes:** its **disposal date and sale proceeds are still
unknown**, and it carries a purchase price, so the disposal has a book consequence this KB cannot
compute. That stays in the outstanding-items list under documents wanted.

*`Outputs/kb-registers.md`'s one-line summary row for this session listed T026, T028, T029 and the T027
correction but not T010, and that gap was recorded here as a deliberate deferral rather than left as
drift — one clause did not justify an archive cycle on a 51 KB file. **It was discharged the same
session**, once T025 and T024 gave that file three closures to carry rather than one: the summary row,
the processed-items row and the Changes table all now name T010 alongside them. Worth noting because
this is the §3 lesson *a correction has to be swept through every store the claim reached* working as
intended — the deferral was written down, so it could be closed instead of forgotten.*

## T025 closed — Cabineo X chosen, confirmat kept as Plan B

The owner, in two statements a minute apart:

> **"Cabineo X was chosen, we ordered them."**
>
> **"But leave conformant as Plan B, we have them in stock too."**

**The first settles the specification; the second is the one that changes the plan.** I had written that
confirmat was *"no longer a candidate"* and that a mixed spec was *"no longer worth pursuing"* — too
absolute on both counts, and corrected mid-turn. A fallback that is already in stock is not a discarded
option, it is a second route that costs nothing to keep.

**What the decision costs, stated plainly:** ≈£0.87 per joint against confirmat's £0.03, eight carcase
fixings per unit, so **+£6.72 a unit and +£80.67 on a twelve-unit kitchen**. That is now settled cost
rather than an open question — bought for the hidden fixing, the demountability and the single-action
assembly. The one thing still worth doing is a **trade quote on the housing at 2,000**: £0.77 is a
single-unit retail listing and it is the weakest figure in the whole comparison. *A purchase, so the
owner's* (§6a).

**Three things fell out of the decision that were not obvious before it.**

**No Ø15 drill is needed.** Cabineo X's published tooling reads *"Ø5 and Ø15 drills, cutter Ø12 or
smaller"*, and the Ø15 was the one item this KB could not account for. But the housing fits *"a drilled
**or** routed recess"* — the two are **alternatives**, and **the master routes it**. There is no Ø15 hole
anywhere in the decoded parts. So everything Cabineo X needs is already on the machine: the Ø5 the master
already drills, and a cutter of 12 mm or less, of which the shop has two.

**Which makes T016 purely a software problem.** Nothing to buy, no head to fit, no lead time — the
missing Ø5 in SmartCABINET's Cabineo X drill-head profile is a catalog entry, and closing it is the whole
job.

**And Plan B is viable without re-drawing anything.** The connector pockets are routed into the *inside*
faces of the carcase, so **a pocket left empty is hidden in the finished unit**. Parts do not change size,
the cutting list is unaffected, and confirmat's extra requirement — a core hole in the panel edge — can be
drilled on the Vitap's horizontal spindles or at the bench. That edge is a side's **end** edge, which sits
inside the joint and is not taped, so there is no edging to drill through either.

**That last point revises T016's severity downward while leaving its priority alone.** T016 had been
recorded as a precondition for populating the library — *"a Ø5 that does not resolve fails every unit
identically"*. With confirmat in stock, **a job is not stopped by T016**; it is made more slowly and with
a visible screw head. Still the thing to fix first; no longer the thing that must be fixed before anything
can be cut.

*One caveat stated rather than assumed: this establishes that the **carcase** can be assembled either way.
It does not establish that a Cabineo-drilled panel and a confirmat-screwed joint reach the same rigidity —
the pocket removes material from the side's inside face near the joint, and nobody has tested a
mixed-history panel. Worth looking at the first one if Plan B is ever used in anger.*

---

## T024 half closed — the shelf depth is arithmetic, and two step-backs are specification

Yesterday's three-unit comparison found shelf depths of **266 / 256 / 255 mm** on three carcases that are
all 300 mm deep, and recorded all three values rather than preferring the master's. The owner explained it:

> **"I was working on a different design of a 600 mm wall unit. Amfa 600mm wall unit RH is the latest
> release. It's got a 10 mm step back for the shelf front, and we have a 16 mm step back for the back
> panel to accommodate Hafele conceal wall mount."**

**So there was no defect — there was a design that moved**, and four folders left behind at an earlier
point in it. And the master's figure is not merely the newest; it is the one that can be checked:

| | mm |
|---|---|
| Carcase depth | **300** |
| − back-panel step-back (the void the concealed wall mount sits in) | −16 |
| − back panel thickness | −19 |
| − shelf-front step-back | −10 |
| **= shelf depth** | **255** ✓ |

**Exactly what `05-SHELF-1` and `06-SHELF-2` carry.** The chain closes to the millimetre.

**The two step-backs are specification, not incidental, and they belong on every unit's spec card.** The
16 mm exists to leave a void between the back panel and the wall for the **Häfele concealed wall mount** —
a hardware decision driving a panel dimension, which is precisely the sort of figure that gets "tidied up"
by someone later if it is not written down anywhere.

**It also ties this geometry to work already in the KB.** The Häfele Concealed Cabinet Hanger is one of
the two hardware items added to SmartCabinet's Wall Support Cam Table on 2026-09-16 — the session that
raised **T017**, the unresolved X-sign discrepancy between those two items. The 16 mm set-back is that
hardware choice showing up as a panel dimension.

*Recorded as a labelled reading, because it affects nothing:* running the chain backwards, the 300 mm
unit's 266 needs the two step-backs to total 15 mm and the 600 mm unit's 256 needs 25, which both fit a
15 mm back step-back with the shelf step-back going **0 → 10 → 10** and the back step-back later
**15 → 16**. That is my arithmetic, not something the owner stated — offered because it reads as iteration
rather than inconsistency, and ignorable either way.

**T024 stays open on its other half.** `07-BACK-1` and `07-BACK-1B` are the same blank (862 × 562 × 19),
both in the cut list, with programs of 60,458 and 11,994 bytes — and **neither earlier unit has a second
back at all**. Worth re-asking now that the back is known to sit in a 16 mm void for a hanger, since a
hanger usually wants the back notched or cut. **Not asserted**, and the owner has not said.

## Still open at session end

- **T016** — now understood as the Cabineo X tooling being half-defined, and **software-only**: the
  library's one remaining blocker, though a less severe one than it looked, because Plan B exists.
- **T024's remainder — the two backs** on one blank in the master.
- **T027 — what was the problem with the 35 mm head?**
- **T029's remainder** — which edges are edged; the pre-mill setting and the tape it is set for.
- **Four of the five unit types have no master at all.** The owner's range is wall, base, sink,
  appliance housing and tall; only the wall unit exists.
- **`Outputs/kb-registers.md`** processed-items rows and this file's index entry — done in this session.
