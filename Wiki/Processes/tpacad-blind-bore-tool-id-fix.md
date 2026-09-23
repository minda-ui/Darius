---
title: "Closing T016: the Blind-bore tool-ID fix, and a correction to what T016 was said to be"
category: Processes
status: superseded
sensitive: false
created: 2026-09-19
updated: 2026-09-23
sources:
 - "`Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md` (Drive `1eEGlEAeEfLQFUMrmNHF2ySZSjy5W1IeC`), read in full 2026-09-19 — the contemporaneous at-the-machine record of 2026-09-15"
 - "Smartsheet Tasks T016 (row `3054339713795972`), note read 2026-09-19"
 - "`Raw/TPA CAD part 2.pdf` — the HOLE working's Diameter / Tool / Tool type parameter definitions, quoted via the article above"
related:
 - ./tpacad-tool-type-optimizer-ambiguity.md
 - ./carcase-fixings-cabineo-x-vs-confirmat.md
 - ../Software/kitchen-unit-library.md
 - ../Machinery/vitap-k2-drill-head-tooling.md
 - ./tpacad-tool-match-criteria.md
---

# Closing T016: the Blind-bore tool-ID fix

> # SUPERSEDED 2026-09-23 — DO NOT FOLLOW THIS PROCEDURE
>
> **Its premise is false.** This article rests on the claim that
> *"Tool for this working not found"* is raised when several tools match and the optimiser cannot
> choose. **TPA's own documentation for the optimiser module says the error is raised when
> *nothing* matches** — error **−27**, *"Working: tool match not possible"*, and the module
> explicitly expects multiple candidates. See
> [`tpacad-tool-match-criteria.md`](./tpacad-tool-match-criteria.md), which replaces this one.
>
> **Two of its instructions are actively harmful:**
> 1. *"Leave `Tool type` alone"* while setting an explicit `Tool` — this triggers error **−25** if
>    the type does not match the tool, so the fix appears to fail when it has not been tried.
> 2. The whole article is silent on **manual chapter 5 p.63** — through-drills belong in the
>    indicated spindles, black ring right-hand, red ring left-hand, wrong placement damaging bits
>    and rollers. Any procedure that has someone re-tool a head must say so. *(Editing a bush's ID
>    moves nothing physical and is not affected by this.)*
>
> **What survives.** Everything this article says about *programming per tool overriding
> programming per diameter* is correct and confirmed by the Workings manual. Its correction of the
> **2026-09-19 reframing** — that T016 is at the Vitap, not the SmartCABINET catalog — also stands.
> It is kept, uncorrected below this line, because the record of what the KB believed and why is
> worth more than a tidy file. *This is the second time a T016 document has had to correct its
> predecessor; the first correction was right about the place and wrong about the mechanism.*

**Read the next section before going to the machine.** The fix this KB has been carrying in its task
note and in `CLAUDE.md` §7 since 2026-09-19 points at the wrong computer.

## The correction: T016 is not the missing SmartCabinet catalog row

**What the KB has been saying** (Smartsheet T016 as reframed 2026-09-19, and `CLAUDE.md` §7 v18–v20):

> *"the gap is a missing Ø5 entry in SmartCABINET's Cabineo X drill-head profile"* — so T016 is
> *"purely a software problem… a catalog entry and a test run"*.

**What the contemporaneous record actually says.** `tpacad-tool-type-optimizer-ambiguity.md` was
written on 2026-09-15 at the machine, with the Technology dialog open and two positions checked by
hand. It records both findings and then separates them explicitly:

> *"This is **unrelated** to the TpaCAD optimizer ambiguity above — it's a gap in SmartCabinet's own
> head/tool catalog, **not** the Vitap's tool archive (which does have 5mm tools, both Blind and
> Through)."*

and, on the catalog row itself:

> *"TpaCAD's exported `.TCN` files reference diameter + type (not SmartCabinet's own internal tool ID
> numbers), so **the new row's ID number doesn't need to match anything machine-side**."*

**So the Vitap is not missing a Ø5 tool. It has five of them.** That is the whole fault: **Blind Ø5 mm
is assigned to bushes 6, 7, 8, 9 and 10**, every one of them carrying **ID 0**, so when the optimiser
tries to resolve the operation by diameter + type it has five equally valid candidates and no
documented tie-break. Through Ø5 mm resolves cleanly for the opposite reason — it has exactly **one**
bush (bush 2), so auto-resolution never has to choose.

**How the KB got it wrong, because the shape of it is familiar.** On 2026-09-19 I connected two facts
that sit in the same article — *"a SmartCABINET drill-head profile named Cabineo X"* and *"no Dia. 5mm
entry in it"* — and concluded that the missing row was the cause of the Ø5 failure. **The article that
records both facts says in terms that they are unrelated, and I did not re-read it before reframing
the task.** That is `CLAUDE.md` §3's *a fact recorded without a source hardens into an assumption*
arriving from a new direction: **the source existed and was not consulted.** Same family as the
35 mm-head error three days earlier — a plausible connection asserted instead of checked.

**What it would have cost.** Someone follows the task note, drives to the design computer, adds a
`Dia. 5mm` row to the CN Tools list, exports again — and gets the identical error, because nothing
about the Vitap's five ID-0 bushes has changed. A wasted trip and a fix that looks like it failed.

*The catalog row is still worth adding. It is just not this task's fix — see "The CN Tools row" below.*

## What actually closes it — two steps, both at the Vitap

From the article's own "Fix" section, which is the documented mechanism rather than the workaround:

**Step 1 — give one Blind Ø5 mm bush a real ID.**
Open TpaCAD's per-position **Technology** dialog (Outfit `0`, Group `1`, from the TCN editor's outfit
view). Pick **one** of the Blind Ø5 mm bushes — bush 6 is the article's suggestion — and set its
numeric **ID** field from `0` to a real, unused number.

> **Check what is actually taken before choosing a number, rather than trusting this list.** The
> article records `1001`, `1002`, `1006`, `1011` and `1012` as taken by positions 101–104 — **five IDs
> for four positions**, which is either one position holding more than one tool or a slip in the
> original note. It was never reconciled. Read the live values off the dialog on the day.

**Step 2 — point the failing operation at that ID.**
On the failing `HOLE` / `FITTINGX` operation in the `.TCN`, set the **Tool** field explicitly to the
new ID, instead of leaving `Tool type = "Blind bore drill"` to auto-resolve by diameter.

The manual is unambiguous that this is the right lever:

> **Tool** — sets the tool number **and prevails over the programming per diameter**.
> **Tool type** — … influences the choice of the tool that will perform the drilling [when
> programming per diameter], [and] **a validity check of the tool** in case of programming per tool.

So with an explicit Tool ID, `Tool type` stops being a selector and becomes a check. **The ambiguity
does not get broken — it stops being consulted.**

**Both steps are needed.** Step 1 alone leaves the operation still resolving by diameter. Step 2 alone
has nothing to point at, because the whole main bank sits at ID 0.

## How to know it worked

**Reproduce the failure first**, on the same file, before changing anything — so that a later green
run means something. Expect:

> Program optimization encountered errors.
> Face: 1, Working: N, Tool for this working not found.

Then do steps 1 and 2, and **Solve the same program again** — it should optimise with no error.

**Then test the case that matters**: `03-BOTTOM.TCN` from `AMFA Wall Unit 600 RH`, whose seven Ø5
holes all carry `#1001=0`. If that solves, the library's blocking condition is gone.

**Do not use the Through-bore workaround to declare it closed.** Switching the operation's `Tool type`
to *"Through bore drill"* also clears the error — that is what was done on 2026-09-15 to get the job
out — but it works by picking a category that happens to have one bush, not by fixing the ambiguity.
It is a per-file dodge and it silently drills with the wrong tool category.

## The CN Tools row — worth doing, different job

Adding a `Dia. 5mm` row to SmartCabinet's **Cam Table: CN Tools** list under the `Cabineo X` head
profile (which currently holds 10 mm, 12 mm, 20 mm and two 9.5 mm variants) is **not** what clears the
optimiser error. It belongs to the **systemic** half of the problem, which the article states
separately:

> *every future SmartCabinet-exported program still needs its Blind operations pointed at that
> explicit ID rather than left on diameter+type — which likely means either manually setting the Tool
> field per job, or (better, longer-term) getting SmartCabinet's post-processor to populate it on
> export automatically.*

**That is the real prize.** Steps 1 and 2 fix one file. Getting the post-processor to emit a Tool ID
fixes every file, which matters precisely because **every hole in the master exports with `#1001=0`**
— so without it, step 2 has to be repeated by hand on every operation of every unit in the library.

**One thing to look at while you are in there**, because it decides whether the post-processor route
is even available: the article found that **position 101 → ID 1001, and SmartCabinet's CN Tools also
calls 1001 "Dia. 10mm"** — the two numbering schemes genuinely correspond, at least for positions
101–104. *Whether that correspondence extends to the main bank is unverified*, and it is the hinge:
if it holds, SmartCabinet can be made to emit IDs the Vitap will recognise; if it does not, the IDs
have to be maintained in two places by hand.

**And the standing caveat stays standing:** whether a catalog entry added on the SmartCabinet computer
reaches TpaCAD at all is **unverified** (`CLAUDE.md` §1). A shared network does not merge two
applications' internal databases. Establish it, do not assume it.

## What this does not settle

- **T027 — the 35 mm head.** The door programs each cup as `#1002=35` with `#1001=0`: a Ø35 bore with
  no tool assigned. **If the 35 mm head also sits at ID 0 with more than one candidate, it is the same
  fault and step 1 applies to it too** — but *the owner has not said what the problem was*, and this
  KB has already been caught guessing on exactly this point. **Ask, or check its bush count while the
  Technology dialog is open.** One glance answers it.
- **Whether the ambiguity has a documented tie-break after all.** The extract this KB holds has no
  rule, but it is an abridged extract; `Workings.pdf` and the complete `TpaCad.pdf` at
  the `Albatros` install's `Help` folder on the shop's own PC would settle it (Task **T015**).

## To close the task

T016 closes when **steps 1 and 2 are done and `03-BOTTOM.TCN` solves clean** — not before, and not on
the Through-bore workaround. Record, when it is done:

- which bush was given an ID, and **what ID** (so the next person can find it);
- whether the same fix was needed for other diameters — **Ø3 failed too** on 2026-09-15;
- whether the 35 mm head turned out to be the same fault (T027);
- whether SmartCabinet's post-processor can be made to emit the Tool ID, or whether this stays a
  per-job manual step.

**None of this can be done from the KB side.** It needs someone at the TpaCAD station with the outfit
open. Darius can record the outcome and sweep it through the stores the moment there is one.
