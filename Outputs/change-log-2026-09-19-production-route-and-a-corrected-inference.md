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

## `CLAUDE.md` v18 — the article count left the charter

The owner, on being shown that v17's *"nine / twenty-seven"* was already twelve / thirty on the day it
was written:

> **"I agree with dropping figures from Claude.md and pointing to registers. That makes process a bit
> lighter."**

**So v18 drops them.** §1 and §7 now say the mirror is partial, name what it holds by date rather than by
number, and **point at `Outputs/kb-registers.md`** — whose Wiki-structure rows carry the count at the
moment each article was added, with the command that produced it. To quote a live figure, run
`git ls-files 'Wiki/**/*.md' | wc -l`.

**Why this is a fix and not a shrug.** The count was wrong in v12, v13, v16 and v17 — four for four —
and not through carelessness: **an article written in any session invalidates it, and the charter is
revised weekly at best.** v17's response was to make recounting a standing rule, which is the obvious
answer and the wrong one: it went stale the same day it was written. **A rule that has to be obeyed on
every edit of a slow-moving document will be missed, and the miss is silent**, because a wrong number
reads exactly like a right one. Moving the fact to the file that is touched every session removes the
opportunity for error rather than asking harder for vigilance.

**New §3 lesson: *put a fact where its own update cycle lives.*** With the test that generalises it —
**ask what invalidates a figure and how often; if the answer is "more often than this document is
edited", it belongs elsewhere with a pointer left behind.** Applied back to the charter's other numbers,
the same test *keeps* the Drive file ids, the Smartsheet sheet ids and the machine specifications, which
change rarely or never. It is not an argument against figures in durable documents, only against
fast-moving ones.

*The figures v17 quoted are deliberately not repeated in v18's account of them.* A superseded count sitting
in a version note is exactly the thing that misleads a future reader, and the v16 note's wording is the
proof — it read as current until someone checked.

**Three claims elsewhere in §7 were swept in the same pass**, because a charter bump is the moment the
correction rule (§3) applies to the charter itself: the kitchen-library bullet no longer calls the shelf
depth a defect, the T016 bullet carries the software-only finding and the Plan B severity revision, and
the TpaCAD bullet records that the shop **has** the 35 mm head. Three new operational-systems entries
were added for the articles written on 2026-09-19. **v17 (`1XseIOKRWe7rMgnxU88FkHbpPJBxhV5Jy`) is
archived; v18 is live at `1wS22TUTeWjYX8RkQIkkrrQq98ZqJnpHy`, 79,337 bytes, byte-verified.**

## A verification failure worth recording: `wc -c` cannot see a reordering

While uploading this file and the registers, **the registers went up with two Outputs rows in the wrong
order** — I moved the *"Drive sync debt cleared"* row from before the v18 row to after it while pasting.
**The byte count came back 56,265, exactly matching local, and I reported it as byte-exact.**

It was. **And the file was still wrong**, because moving two rows of a table changes nothing about the
total. The check that has caught every other upload error in this KB — `wc -c` both sides, per §3's
*verify like with like* — **is blind to any error that permutes content rather than changing it.**
Reordering, and a swap of two equal-length values, both pass.

Caught by reading the row order back rather than trusting the number, which is §3's *trust the API's
response, not its status code* arriving from a new direction: the number in the response was true and
the conclusion drawn from it was not. Fixed by re-uploading in the right order; the wrong-order copy is
archived **`ARCHIVED-2026-09-19c-kb-registers.md`, labelled DO NOT CITE** with the reason, because its
content is correct and only its order is not — exactly the kind of file someone would otherwise cite in
good faith.

**Proposed for the next charter revision, not added unilaterally** (the same route the count fix took):
a §3 clause that **a size match is necessary and not sufficient — it proves nothing about order.** Where
order carries meaning, as it does in every append-only table in this KB, verify the order of the first and
last few rows as well as the byte count. The practical form is cheap: hash the lines that should be at
known positions before uploading, and read them back after.

*Stated here rather than quietly fixed, because an upload I announced as verified was not.*

## `CLAUDE.md` v19 — the clause is in, and applying it immediately found its own limit

The owner approved the proposed clause (*"Yes, add that clause at v19"*), so §3's *verify like with like*
now carries: **a size match is necessary and not sufficient, and proves nothing about order.** With the
practical form — before uploading, note which rows should sit first and last in each table; after
uploading, read those positions back, not just the size — and the general shape, which is *trust the
API's response, not its status code* one level up: **the number in the response was true and the
inference drawn from it was false.** Plus the line worth keeping: *a check that has never failed is not a
check that cannot fail; know what yours is blind to.*

**And then the new rule could not be applied to the file that carries it.** v19 uploaded at **82,310
bytes, matching local**; the read-back to check order **returned empty**. Not an error — an empty
`fileContent`, the same failure mode as the 2.9 MB air-receiver photograph on 2026-09-18.

**That brackets the connector's read limit usefully**, which nothing in this KB had done before:

| File | Size | Read-back |
|---|---|---|
| `kb-registers.md` | **56,265 B** | **worked** — 60,323 characters returned |
| `CLAUDE.md` v19 | **82,310 B** | **empty** |

So the ceiling sits somewhere between **56 KB and 82 KB**, *two data points, not a measured threshold —
this is a bracket, not a limit.* **The consequence is specific and awkward: the order check cannot be
performed on `CLAUDE.md`, the largest and most important file in the KB.** The rule written into v19
therefore has a hole in it at exactly the place it is written.

**What can still be said about v19's upload:** the size matches, and it was assembled from one contiguous
source rather than by moving blocks about, so the failure mode that hit the registers — a row picked up
and put down elsewhere — did not have an opportunity to occur. **That is an argument about how the file
was produced, not a verification of the file**, and it is recorded as such rather than dressed up as one.

**Proposed for v20, not added unilaterally:** either state plainly in §3 that the order check is
unavailable above roughly 60 KB and say what stands in for it, or find a read path that returns large
files (the same mechanism the partial git mirror has been waiting for — something that returns bytes).
**The second would close two debts with one tool**, which is the better reason to look for it than either
debt alone.

*Recorded because a rule with a known gap is worth less than a rule whose gap is written down next to it.*

## `CLAUDE.md` v20 — both gaps written down, and the tool that would close them named

The owner: **"Add both v20 items now."** Neither was a new finding; both were things v19 had discovered
about itself and left as proposals.

**Item 1 — §3's order check now states its own limits.** v19 told a future reader to verify order by
reading the file back, and that instruction **silently fails above a size**: the connector returns an
**empty** `fileContent` rather than an error. **A rule that cannot run on the most important file in the
KB, and says nothing about it, is worse than no rule** — the reader assumes it ran. §3 now carries:

- **the bracket** — `kb-registers.md` read back fine at **58,410 bytes**, `CLAUDE.md` came back empty at
  **82,310**; *two points, so a bracket between roughly 58 KB and 82 KB, not a measured threshold;*
- **what stands in for the check above it** — build the upload from one contiguous source rather than by
  moving blocks about, so the pick-up-and-put-down failure has no opportunity to occur, **and say plainly
  that order was not verified.** *That is an argument about how the file was produced, not a verification
  of it, and must never be reported as one;*
- **anchors must be plain text.** The read tool escapes backticks and asterisks, so an anchor containing
  them is not found and the check reports a failure that is not there. **This KB produced exactly that
  false alarm on the check's first run and nearly believed it** — two landmarks came back NOT FOUND
  because they contained `` ` `` and `*`. Re-run with prose anchors: nine landmarks, all in order, 109
  table rows both sides.

**Item 2 — the byte-returning read path is now a named §7 debt, listed above the mirror bullet.** The
empty read and the partial git mirror have been carried as separate problems since 2026-09-17. **They are
one missing capability wearing two faces**: the read tool re-formats (so the mirror cannot be back-filled)
*and* gives up on size (so the order check cannot run). Candidates, none tried — an owner-side folder
download, a Drive-to-git sync outside this connector, or any API path that returns the stored bytes.
**Whoever goes looking should know it pays twice**, which is a better reason to spend an afternoon on it
than either debt alone, and neither bullet said so before v20.

**v20 itself could not have its order verified** — 85,763 bytes, well above the ceiling. Recorded here in
the form the new clause requires: **size matched, order not verified, assembled from one contiguous
source.** The rule's first application is to the file that introduced it, and it applies honestly rather
than conveniently.

## T016 — and the fix this KB was recommending was the wrong one

The owner: **"Close T016 next."** It cannot be closed from here — it closes at the TpaCAD station with
the outfit open — so the work was to produce the procedure. **Producing it found that the procedure
this KB has been giving since v18 points at the wrong computer.**

**What we were saying.** Smartsheet T016 (reframed earlier the same day), `CLAUDE.md` §7 and
`Wiki/index.md` all carried: *the gap is a missing Ø5 entry in SmartCABINET's Cabineo X drill-head
profile*, so T016 is *"a catalog entry and a test run"*.

**What the primary record says.** `Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md` was written
on 2026-09-15 **at the machine**, with TpaCAD's Technology dialog open and two positions read off by
hand. It records both findings and then separates them in terms:

> *"This is **unrelated** to the TpaCAD optimizer ambiguity above — it's a gap in SmartCabinet's own
> head/tool catalog, **not** the Vitap's tool archive (which does have 5mm tools, both Blind and
> Through)."*

and, of the catalog row itself, *"the new row's ID number doesn't need to match anything
machine-side."*

**The Vitap is not missing a Ø5 tool. It has five.** Blind Ø5 mm is assigned to **bushes 6, 7, 8, 9
and 10**, every one at **ID 0**, so diameter + type resolution has five equally valid candidates and no
documented tie-break. Through Ø5 resolves cleanly for the opposite reason — one bush. **That is the
entire fault**, and nothing about it changes if a row is added on the design computer.

**The actual fix, two steps, both at the Vitap:** give one Blind Ø5 bush a real unused ID in the
per-position Technology dialog, then set the failing operation's `Tool` field to it — which the manual
says *"prevails over the programming per diameter"*, turning `Tool type` into a validity check. Both
steps are needed: step 1 alone still resolves by diameter, step 2 alone has nothing to point at.
**Verify** by reproducing the failure first, re-Solving, then running `03-BOTTOM.TCN` — and **not** by
the Through-bore workaround, which clears the error by picking a category that happens to have one bush
and silently drills with the wrong one.

**Written up as `Wiki/Processes/tpacad-blind-bore-tool-id-fix.md`** (9,610 bytes) — a new article
rather than an edit to the 2026-09-15 one, per §3: that article is Drive-only and re-authoring it
through a lossy read would risk the 95% nobody meant to touch.

### How the error was made

I connected two facts sitting in the same article — a head profile named *"Cabineo X"* and a missing
`Dia. 5mm` row — and asserted the second caused the Ø5 failure. **I did not re-read the article that
says they are unrelated before reframing the task.**

**This is §3's *a fact recorded without a source* turned inside out: the source existed and was not
consulted.** New §3 lesson at v21: ***re-read the primary record before reframing what a task is***,
with the reason it will keep happening — *the risk scales with the KB's size.* The charter now
summarises articles it no longer quotes, and a summary of a summary drifts. Adding to a task is a small
edit; **saying what a task *is* redirects everyone who reads it next**, and deserves the primary
source open.

**What it would have cost:** a trip to the design computer, a row added, the identical error on the
next export, and a fix that looks like it failed.

### Swept, and what is still owed

Corrected in **Smartsheet T016** (title and note — the store that gives directions at the machine),
**`Wiki/index.md`** (whose carcase-fixings entry asserted the same thing), and **`CLAUDE.md` → v21**
(§7's T016 bullet rewritten; §1's CAM/CN Tools paragraph narrowed to the *systemic* half, since the
immediate fix is entirely inside TpaCAD's own outfit). v21 went up at **90,475 bytes** against **90,169**
local, and was recorded only as an **unexplained size mismatch** — which is what v20's clause allowed
for, and is not the same as a verification. *Resolved later in the same session, and it was not
corruption: see the v22 section below.* v21 is now archived and superseded by **v22**.

**The CN Tools row is still worth adding**, and the article says what for: the **systemic** fix, getting
SmartCABINET's post-processor to *emit* a Tool ID on export, so step two is not repeated by hand on
every operation of every unit — which matters because **every hole in the master exports with
`#1001=0`**. The hinge is whether the two ID schemes correspond beyond positions 101–104; the single
data point is that position 101 is ID 1001 in TpaCAD and `Dia. 10mm` is 1001 in SmartCABINET.

**One loose thread found while reading, not resolved:** the article lists `1001/1002/1006/1011/1012` as
IDs taken by positions **101–104** — *five IDs for four positions*. Either a position holds more than
one tool or it is a slip in the original note. **The procedure says to read the live values off the
dialog rather than trust the list**, which costs nothing and settles it.

**T016 stays Open.** It closes when both steps are done and `03-BOTTOM.TCN` solves clean, and Darius
can record that the moment there is an outcome.

## `CLAUDE.md` v22 — the tool this KB called missing was in the connector all along

**The debt.** v20 named, on the owner's approval, the single most useful thing this KB did not have: *a
read path that returns bytes*. It would close two problems at once — a git mirror that could not be
back-filled because the read tool re-formats, and an order check that could not run above roughly 82 KB
because the read tool returns an empty string. v20 listed three candidates, none tried: an owner-side
folder download, a Drive-to-git sync outside the connector, or any API path handing back stored bytes.

**It took one call to find.** The Drive connector has **two** read tools. `read_file_content` — the one
every session has used, and the one the debt was measured against — returns a natural-language rendering.
`download_file_content` returns the stored bytes, base64-encoded. **It had never been called in the
KB's history.**

**Both halves verified, not assumed.**

- `tpacad-blind-bore-tool-id-fix.md` was downloaded, decoded and `diff`ed against its local copy:
  **byte-identical apart from one real eight-character difference.** No escaped punctuation, no appended
  hard breaks, no silent drift. **So the mirror can be back-filled**, and each copy can be *proved*
  rather than trusted.
- `CLAUDE.md` v21 came back **whole at 90,475 bytes** — well past the 58–82 KB bracket where
  `read_file_content` gives up. **The order check has no ceiling any more.** v22 was then uploaded and
  verified the real way: download, decode, diff — **byte-identical to local at 95,668 bytes**, the first
  time that check has ever actually run on this file rather than being argued for.

**Two unexplained numbers turned out to be one diff each, and both were mine.**

- The new article's **−8 bytes**. I had ruled out backslash escapes and nested blockquotes, found the
  gap constant and file-specific, **deliberately bounded it at three attempts and recorded it as
  unresolved.** It was local reading *"It has five of them."* against a Drive paste reading *"It has
  five."* — eight characters, one hunk. The article has been re-uploaded from local and now matches at
  9,610 bytes both sides; the stale copy is archived.
- This file's **+306 bytes**. Also not corruption: a single hunk, the Operational-systems bullet that was
  in the Drive paste and missing from local. **The 90 KB paste carried no drift whatsoever** — which is
  worth knowing in its own right, because the whole contiguous-source argument was built on the fear that
  it might. The bullet belonged in the charter, so it was added locally and v22 built on top.

**And on its third use the new check caught something the byte count could not — the exact blind spot
§3 has been circling since v19.** This change log was uploaded at **39,167 bytes, matching local
exactly**, and the `diff` still came back with a hunk: one paragraph wrapped across four lines
differently on the two sides. **A re-wrap trades a space for a newline one-for-one, so the byte total
does not move** — the same shape as the transposed table rows that started this whole thread, arriving
from a new direction. Under the old regime it would have passed as *"size verified"* and gone
unrecorded. *The defect was local's*, from a scripted edit that left a 110-character line; local was
brought into line with the hand-wrapped upload and both sides now diff clean. **Cosmetic in this
instance, and that is rather the point: the check does not know it is cosmetic, and next time it will
not be.**

**A label I put on and took off.** I archived the v21 copy as `DO NOT CITE` on suspicion alone, before
running the diff. Once the diff showed a single clean hunk the label came off — the file was correct. §3
already warns twice that a mislabelled file advertises nothing; **suspicion is not grounds for the
label**, and this is the third entry of that kind.

**What went into v22.** §7's debt bullet struck through and closed, naming what it unblocks as *work*
rather than *capability*. §1 and §7's *cannot be back-filled* downgraded to **not back-filled yet** —
the mirror is still partial today, and saying otherwise would be the stale-claim failure this file keeps
correcting. §3's *the read tool does not round-trip* narrowed to `read_file_content`, with the
round-trip evidence for the other. §3's order-check ceiling **lifted**, with the contiguous-source
argument demoted from substitute-for-a-check to good practice. And a new §3 lesson:

> **Check whether the tool you are blaming is the tool you used.** A limitation is a property of the
> call you made, not of the system, until you have looked at what else the system offers. The claim was
> true of one tool and was written down against *the connector* — a quiet widening of scope that nothing
> re-examined for nine versions, **because a debt that is written down reads as settled.** And its cheap
> half: *a discrepancy you cannot explain is usually a diff you have not run.*

**What this did not mean, as written at the time.** Nothing had been back-filled; the Drive-only articles
were still Drive-only, and v22 said so rather than claiming the outcome from the capability. *That
sentence held for about an hour — the back-fill is the next section.* **The distinction was still worth
drawing**: a capability is not an outcome, and a charter that blurs the two is how the mirror came to
claim it was "kept in step" for four versions while it was not.

## The mirror back-fill — done, and the file that proves it

The owner: **"Start the mirror back-fill."** v22 had just established the capability and said plainly
that **nothing had been back-filled yet**. This closes that gap.

**What was missing.** Drive holds **31** Wiki articles; git held **13**. The other **18** had existed on
Drive only since the mirror was created on 2026-09-16.

**How they were copied — the part that matters.** Each article was fetched with
`download_file_content`, which returns the stored bytes base64-encoded, then decoded **straight to
disk** by a script. **Nothing was re-typed and nothing passed through a rendering.** Each file's length
was then checked against Drive's own `fileSize`. **All 18 matched exactly.**

| | bytes |
|---|---|
| `Machinery/altendorf-f45-panel-saw.md` | 30,694 |
| `Machinery/vitap-k2-panel-saw.md` | 23,062 |
| `Machinery/hebrock-f4-next-edge-bander.md` | 21,325 |
| `Processes/tpacad-tool-type-optimizer-ambiguity.md` | 9,845 |
| `Software/smartcabinet-and-production-workflow.md` | 9,219 |
| `Processes/smartcabinet-wall-support-cam-table-reference.md` | 8,738 |
| `Troubleshooting/troubleshooting-altendorf-f45.md` | 6,769 |
| `Decisions/2026-09-14-kb-scope-and-structure-adopted.md` | 5,625 |
| `Processes/machinery-maintenance-system.md` | 4,648 |
| `Processes/maintenance-schedule-altendorf-f45.md` | 4,601 |
| `Troubleshooting/troubleshooting-hebrock-f4.md` | 3,934 |
| `Troubleshooting/troubleshooting-and-fault-log-system.md` | 3,642 |
| `Processes/maintenance-schedule-hebrock-f4.md` | 3,535 |
| `Processes/maintenance-schedule-vitap-k2.md` | 3,207 |
| `Troubleshooting/troubleshooting-vitap-k2.md` | 3,000 |
| `Decisions/2026-09-15-operational-systems-scope-extension.md` | 2,979 |
| `Processes/f45-monthly-safety-device-check.md` | 2,506 |
| `Suppliers/altendorf-gmbh.md` | 2,007 |

**The smallest one is the point.** `altendorf-gmbh.md` at **2,007 bytes** is the article the v12
fidelity test rebuilt at **2,003 — four bytes short, silently.** That single result is what made the
mirror partial, and it is why eleven versions of the charter said back-filling would corrupt what it
copied. Through the byte path the same file lands **exact**. **The obstacle was never the file. It was
the tool being used to read it.**

**A security gate before anything was committed.** The F45 article is the one carrying a decision: the
**ElmoDrive remote-maintenance access code** was stripped from it on 2026-09-17, *before the mirror
existed*. A back-fill copies whatever the source holds, so the source was checked first — the Drive
copy still states the code is *"deliberately not reproduced here"* and its Changes table records the
removal. A scan of all eighteen for passwords, keys, tokens and access codes found nothing else. **The
one thing a bulk copy must not do is quietly re-import something a previous session deliberately took
out.**

**`git ls-files 'Wiki/**/*.md' | wc -l` now returns 31**, equal to Drive: Decisions 2, Machinery 6,
Processes 13, Software 2, Suppliers 4, Troubleshooting 4. **Drive-only is zero.** Committed as
`cb5e846`.

**What v23 does to the charter.** §1's *the mirror is partial* and §7's *cannot be back-filled* — the
claim carried from v12 to v22 — are struck through. **The debt is replaced by an upkeep rule rather
than by nothing**: an article written to one store and not the other re-opens the gap, so both stores
get it in the same session, which is what §1 asked for all along. The `related:` back-link debt also
gets easier and says so: all three machinery articles are now in git, so that fix is an ordinary local
edit. **The count is deliberately not written into the charter** — v18 moved it to the registers for
exactly this reason, and a completed mirror is no excuse to put it back.

**Worth stating plainly:** this took one afternoon. The bullet it closes stood for eleven versions. The
gap was never the work; it was **not having looked at what else the connector offered** — which is the
§3 lesson added hours earlier, arriving with a price tag attached.

## Still open at session end

- **T016** — **the fix is two steps at the Vitap**, not a SmartCABINET catalog row; that reframing was
  made and withdrawn within this session (see the T016 section). Still the library's one remaining
  blocker, and still less severe than it looked, because Plan B is in stock. **It closes at the machine,
  not here**: steps 1 and 2 done and `03-BOTTOM.TCN` solving clean.
- **T024's remainder — the two backs** on one blank in the master.
- **T027 — what was the problem with the 35 mm head?**
- **T029's remainder** — which edges are edged; the pre-mill setting and the tape it is set for.
- **Four of the five unit types have no master at all.** The owner's range is wall, base, sink,
  appliance housing and tall; only the wall unit exists.
- **`Outputs/kb-registers.md`** processed-items rows and this file's index entry — done in this session.
- ~~**The mirror back-fill has not been started.**~~ **Done this session** — all 18 Drive-only articles
  are in git, byte-checked; the mirror is complete and `CLAUDE.md` is at **v23**. What remains is
  upkeep, not a debt.
- **The `related:` back-links are still not fixed** — now an ordinary local edit, since all three
  machinery articles are in git. Not urgent; just no longer awkward.
- **The bracket where `read_file_content` returns empty (58–82 KB) was never measured**, and now never
  needs to be — but nothing else should be assumed about that tool from the download tool's behaviour.
