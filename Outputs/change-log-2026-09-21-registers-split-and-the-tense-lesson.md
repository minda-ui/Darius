# Change log — 2026-09-21 — the registers split, and a lesson about tense

**One instruction, two approvals:** *"Yes split registers and add that §3 lesson."* Both had been
**proposed the night before rather than acted on**, which is the route this KB's charter changes have
taken since v18.

## 1. `Outputs/kb-registers.md` — 99,517 → 64,231 bytes

**The diagnosis was v27's, one file along.** Drive has no patch API, so every session re-emitted the
whole registers file; **35,701 bytes of it was the Change-log entries section** — eighteen rows,
append-only, never revised. Pure history riding along with rows that change.

**Moved verbatim to `Outputs/change-log-index.md`**, newest first, nothing rewritten or re-ordered.
Integrity checked rather than assumed: **18 rows out, 18 rows in**, first `2026-09-21 / Session 18`,
last `2026-09-14 / Session 1`, and the three surviving tables unchanged at **31 / 35 / 50 rows**
(Processed items, Wiki structure changes, Outputs produced).

**`kb-registers.md` keeps the tables still worked on.** Its Change-log section is now a four-line
pointer saying where the history went and why.

## 2. The reference sweep ran *first* this time

v27 moved the charter's version notes and **then** discovered it had broken four references. This time
the grep came before the move. Three live pointers named `kb-registers.md` as where change logs are
indexed, and all three now name the new file:

| File | What it said |
|---|---|
| `CLAUDE.md` §0 | reading order item 2 — *"newest-first index: `Outputs/kb-registers.md`, section 'Change-log entries'"* |
| `CLAUDE.md` §4 | *"indexed newest-first in `Outputs/kb-registers.md`"* |
| `README.md` | *"indexed newest-first in `Outputs/kb-registers.md`"* |

`CLAUDE.md` §1's folder listing gained the new file.

**One reference was deliberately left alone.**
`Wiki/Decisions/2026-09-14-kb-scope-and-structure-adopted.md` says the Fishbone house style includes
*"per-session change-log files indexed in `kb-registers.md`"*. That is **a dated record of what was
adopted on 2026-09-14**, and of the model KB's structure — not a pointer to our current filing.
Repointing it would misreport what was decided. *Same principle as the archived Drive ids in
`tpacad-blind-bore-tool-id-fix.md`: cite the path for the thing, and leave the record of what was true
then alone.*

**Historic change-log files were also left alone** — they describe the KB as it was when they were
written, which is their whole job.

## 3. `CLAUDE.md` → v28 — and the v27 rule worked on its own

**v27's note moved itself out.** The standing rule added at v27 — *the charter carries the current
version's note only* — had its first application here: v27's note is now the top entry in
`Outputs/charter-version-history.md` (which covers **v8–v27**, 20 notes), and v28's note took its place.
**Nothing had to be remembered; the rule did it.**

## 4. The new §3 lesson — *an absence is only an absence as of a timestamp*

The incident, stated with its timestamps because that is the point:

- Hub checked for Darius-assigned rows, **21:01–21:25 on 2026-09-20**. None found. True.
- **v26 committed 21:25:14**, carrying the sentence *"no Tasks & Requests row is assigned to Darius"*.
- **`AWT-0045` created 21:29:36** — four minutes later.

**True when written, false before anyone could read it**, and sitting in a charter revised weekly.
**The mistake is not the checking, it is the tense.** And the first correction was wrong too — it
blamed Smartsheet's eventually-consistent search, when the timestamps show there was nothing yet to
find; superseded **visibly on the row**, the wrong version kept above it.

**What generalises.** This is §3's *put a fact where its own update cycle lives* arriving from the
other side. That lesson asks what invalidates a figure and how often; for *"nothing is assigned to me"*
the answer is **at any moment, by somebody else, without telling you**. So: **a negative finding is a
measurement — date it, or do not write it down.** *"As of 21:25 on 2026-09-20, no row was assigned"* is
true forever. *"No row is assigned"* has a shelf life of minutes.

**It is not a one-off shape.** This KB has written *"no manual exists"*, *"nothing is in `Raw/`"* and
*"the Safety Check Log is empty"* — all of them the same construction, all of them cheap to date.

**Fourth lesson to take the propose-then-approve route**, after v18's count fix, v19's order clause and
v25's measurement clause.

## 5. What this says beyond this KB

**Two control files hit the same wall in two days.** `HL-0030` on the Workforce Hub carries both data
points. The reusable part is not *"split your charter"* — it is the test that finds the problem before
the wall: **ask which sections of a file are ever revised.** Any section that is only ever appended to,
inside a file that can only be written whole, is a size problem already in progress.
