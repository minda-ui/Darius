# Change log — 2026-09-23 — T016's root cause was wrong for eight days, and the answer was on the shop's own hard drive

**Two workshop sessions (21 and 23 September), one correction, and the largest retraction this KB has
had to make.** Nothing from either session had been recorded before today; the owner was at the
machine and the evidence was arriving faster than it could be filed.

## 1. The correction: "Tool for this working not found" has only ever meant one thing

Since **2026-09-15** this KB has recorded that the error means *the optimiser found several equally
valid tools and could not choose between them*. It went into the contemporaneous article, then the
Smartsheet task note, then `CLAUDE.md` §7, then a whole fix procedure, then the kitchen-unit library's
blocking condition.

**TPA's own documentation for the optimiser module says the opposite.** Error **−27**:

> **Working: tool match not possible** — No tool can be used in execution of a drilling working
> programmed with diameter.

**The error fires when nothing matches.** There is no ambiguity failure in the module's error table at
all, and §1.5 says the optimiser checks *"if there is **at least one** tool which can work working"* —
several candidates are the normal case, and §1.6 deliberately aggregates holes across tools into
single drilling beats.

**The observations from 15 September were real.** Blind Ø5 failed; through Ø5 worked; the main bank sat
at ID 0. What was invented was the *mechanism* joining them — and it was never checked against a
document, because the document was believed not to exist.

### The five criteria — the diagnostic this KB has never had

A hole programmed by diameter resolves only if **all** hold: matching diameter (within epsilon); the
working's tool type matches the tool's type *(checked only if the working sets type > 0)*; the tool can
work that face; **the tool's useful length ≥ the programmed entry depth**; the position is within axis
limits. Fail one, for every tool on the head, and you get −27. **The message does not say which**,
which is why it has been so hard to read.

## 2. How it was found — checklist step A17, and the file nobody knew existed

The owner opened `C:\Albatros\help\` at the Vitap's own PC. It is organised by language; **`en-GB`
holds 29 files**, among them `Workings_eng.pdf` (337 pages), the complete `TpaCAD_eng.pdf` (7.7 MB),
`DxfCAD_eng.pdf` and `DxfToTpa_eng.pdf` — **all three "sibling manuals not present in `Raw/`" that the
2026-09-15 article named, plus the complete manual its own first page pointed at.** The whole folder is
now in `Raw/Albatros-help-en-GB-2026-09-23/`. **Task T015 closes.**

**But the file that actually broke T016 open was not one of them.** `CnCadOpti_eng.pdf` — 759 KB,
nineteen pages, dated 26/11/2019 — is the optimiser module's own documentation, and nobody knew it was
there. *We went looking for the manual we had been told about, and the answer was in the folder next to
it.*

**Both were byte-verified on the way in** (3,728,330 and 758,979, download → decode → `wc -c`) and
extracted locally to text rather than read through a lossy path.

## 3. `03-BOTTOMB.TCN` — the live failure, diagnosed and confirmed

On 21 September, `03-BOTTOM.TCN` from `AMFA Wall Unit 600 RH` **solved clean** (checklist A2), which
sent the checklist's own instruction to skip A3-A13. **I came close to recording "T016 does not
reproduce" as a finding.** The owner then found a file that did fail — *exactly the shape of the §3
lesson added at v28 two days earlier, and the reason it was not written down.*

`600mm Base Appliance Housing unit/03-BOTTOMB.TCN`, **face 1, working 11**. Holes read
`HOLE EG0 X587.0 Y48.0 Z-13.0 TD3 TP0` — Ø3, no tool, 13 mm deep in 19 mm, so **blind, programmed by
diameter**.

Against the five criteria: diameter passes (bush 3 is Ø3); **type fails** — the operation asks blind,
bush 3 is `Foratore passante Ø3mm`, and the owner confirmed from the archive that **Ø3 is only
`passante` on this head**; length passes (53 vs 13); face and limits presumed.

**One criterion fails, and it fails for every tool on the head, because there is exactly one Ø3 and it
is the wrong type.** The optimiser was correct and precise. **This is a tooling/design mismatch, not a
software fault** — SmartCABINET is exporting a hole the machine cannot drill blind, and whether the
master or the head is wrong is an owner's decision (the second is a purchase).

*It also explains why every earlier file was clean: they were Ø5. This was the first file with blind Ø3
holes.*

## 4. The head, as read on 2026-09-23 — and it changed twice in two days

**Confirmed from WscTecnoManager:** bush 2 `Foratore passante Ø 5mm` (Tool Length 48); bush 3
`Foratore passante Ø3mm` (53); bush 4 `Foratore cieco 10mm`; **bushes 6-10 all `Foratore cieco 5mm`**.

**Bushes 6-10 vindicate September.** Five blind Ø5, exactly as recorded — **the first time that claim
has been checked against the archive rather than repeated.** So the Ø5 half of the old diagnosis rests
on a real fact; only its mechanism was invented. *Why that operation failed is now **unexplained**,
with tool useful-length the leading hypothesis — recorded as a hypothesis, because this KB has just
spent eight days acting on a confident mechanism no document supported.*

**Tooling changed 2026-09-22:** Ø10 blind drill into bush 4, Ø12 into bush 12. **They are drills
(`Foratore`), not cutters** — so the interpolated-hole test in `tpacad-interpolated-holes.md` **stays
blocked**; it needs a `Fresa`. *I had suggested one offcut might close two questions. It will not.*

**I also wrote, one message before learning this, that "nothing suggests the outfit has changed since
September."** Something did; I had not asked. **A head layout is a point-in-time observation too** —
the v28 tense lesson arriving from a third direction in three days.

## 5. The bush 3 mismatch — a latent fault with no error attached

Until 2026-09-23, **bush 3 physically held a blind Ø3 while the archive described it as
`Foratore passante Ø3mm`.** Any program resolving a through Ø3 to bush 3 was drilled with a blind bit,
and **nothing would ever have reported it** — the optimiser reads the archive, not the spindle. The
owner replaced the bit so the two agree.

**It did not cause the −27**, which was a true absence and would have occurred either way. **Kept
separate deliberately** — merging them would give this KB a third wrong cause for one error message,
which is how it got into trouble in the first place.

**The general form:** the archive and the head are two stores of one fact and the software trusts only
one. **A tool change is not finished when the drill is in the spindle; it is finished when the archive
says what is in the spindle.**

## 6. What the manuals settled, and what they did not

| Question | Answer |
|---|---|
| `CABINEO` | **A native TpaCAD working.** `[EH] Enable drilling` = *"3 holes with a 15 mm diameter executed up to a 11 mm depth"*. The head has **no Ø15**, so routing the pocket stays the only route — confirming from the machine's own manual what the charter had from the vendor's page |
| The `Diameter` convention | **Not settled for our working.** `CIRCULAR INTERNAL WINDOW` appears **nowhere in 337 pages** — it is a custom working for this installation. But standard `CIRCLE` shows the mechanism: geometry is `[R] Radius`, the tool is handled separately by `[DN] Compensation` (Off/Left/Right) and `[D] Compensation radius`. **So look at the custom working's own fields before cutting anything** |
| `THREE HOLES HINGE` | **No such table exists.** Native `HINGE` takes X, Y, Z and a tool, nothing else. This KB has expected that table since 18 September and should stop |
| Whether `Z` is to the drill's shoulder or its tip | **Still open.** It decides whether a 13 mm blind hole drilled with a pointed through-drill breaks through 19 mm. `TpaCAD_eng.pdf` not yet read |

## 7. A trap in the old fix, and a stop rule of my own that had to be narrowed

**Error −25** — *"The type of tool in working does not match the selected tool"* — fires when
programming **by tool**. So `tpacad-blind-bore-tool-id-fix.md`'s instruction to *"leave `Tool type`
alone"* while setting an explicit `Tool` **produces a new error**, and anyone following it concludes
the fix failed when it was never tried.

**And the checklist's own stop rule 3** said *"never clear the T016 error by switching `Tool type` to
Through bore drill"* — which is exactly what I then spent an hour telling the owner to do. **Flagged
to him rather than passed over**, under the checklist's stop rule 5 (*when the machine contradicts the
checklist, the machine wins*). The rule was not wrong, it was **too wide**: at Ø5 switching category
jumps to a different physical drill; at Ø3 there is one drill on the whole head. **Narrowed, not
deleted.**

**Also missing from that procedure entirely: manual chapter 5 p.63** — through-drills belong in the
indicated spindles, **black ring right-hand, red ring left-hand**, wrong placement causing *"damage to
the drill bits and early wear of the rollers."* A procedure that has someone re-tool a head must say
so. *I overstated this at one point, implying p.63 made the ID edit unsafe; it does not — editing an ID
moves nothing physical. Corrected to the owner at the time.*

## 8. What was written

| File | Action |
|---|---|
| `Wiki/Processes/tpacad-tool-match-criteria.md` | **new**, 12,195 B — the corrected root cause, the five criteria as a checklist, the optimiser's tooling error codes, the confirmed `03-BOTTOMB` diagnosis, the −25 trap |
| `Wiki/Machinery/vitap-k2-drill-head-tooling.md` | **new**, 8,088 B — the head as read on 2026-09-23, every row marked `ARCHIVE` or `LAYOUT`, the two tooling changes, the bush 3 mismatch, p.63 |
| `Wiki/Processes/tpacad-blind-bore-tool-id-fix.md` | **`status: superseded`** + a DO-NOT-FOLLOW banner naming what survives and what is harmful. **Body left uncorrected below the line** |
| `Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md` | correction banner above `## The fault`; **nothing below it edited** |
| `Wiki/index.md` | two new entries, two rewritten |
| `CLAUDE.md` | **v29 back-filled from Drive** (Rule C), byte-identical at 84,568 — the mirror had been a version behind |

**Both superseded articles are kept, not deleted or quietly rewritten.** The record of what this KB
believed, and why, is worth more than a tidy file. `related:` graph re-checked symmetric after the
edits, and **both corrected bodies verified hash-identical below their banners** — the "nothing below
this line has been edited" claim is checked, not asserted.

## 8b. Smartsheet and the Hub

**Tasks (`4087584374523780`)** — `T015` **closed Done**. `T016`'s note replaced with the corrected
root cause, the five criteria, the −25 trap and p.63; **its Title also corrected**, because it read
*"it is an ID-0 tie in the Vitap outfit, NOT the missing SmartCabinet catalog row"* — a title that was
itself a diagnosis, and a wrong one. `T027` updated: Ø35 confirmed at bush 5 from the machine, and its
*"the obvious candidate is T016"* reasoning re-based on the corrected mechanism rather than left
pointing at a cause that no longer exists.

*The old T016 note was replaced rather than appended to, because the cell has a **4,000-character
silent truncation** (§3) and the combined text would have exceeded it. Its full text survives in
`tpacad-blind-bore-tool-id-fix.md` and in git, and the new note says so.* **Every cell was read back
out of the API response**, not trusted to the success code.

**Workforce Hub — `HL-0042`** (Help & Lessons, rowId `6144652783257476`, Open, High). Raised under
§0b Rule B: *nothing that is a task, a lesson or a gap may live only in a local log the coordinator
cannot see.* It carries both candidates below, framed for the estate rather than for this KB —
**every seat has tools it has not listed and documents it has recorded as missing.**

## 8c. Rule D, and a hand-off note that was wrong

**`AWT-0065` closed. `CLAUDE.md` → v30**, adding **Rule D — plain brief** (owner's standard,
2026-09-22, via Victoria): *say it in fewer words; make length earn itself; applies to every message,
charter, log, Hub row and doc.*

**It went in under its own heading, not as "Rule C".** This KB adopted a different Rule C at v29 one day
earlier. John flagged the collision estate-wide.

**The `Raw/` note and its Hub row disagreed, and the row was right.** The note said *"fold into your
charter §0"* — followed literally, that collides with our Rule C. `AWT-0065` said *"under its OWN
heading — do NOT relabel or overwrite any existing charter 'Rule C'"*. **Rule A makes the Hub row the
canonical brief**, so the row governed, and the owner confirmed directly before anything was written.
*This is the first time §6a-i's "a note is a proposal, not an instruction" has actually stopped an
error rather than just been observed.*

**One tension recorded, not glossed:** Rule D covers charters, and this charter is 86 KB. It is not
compliant, and the v30 note says so. **What the v27 and v28 splits treated as a storage problem, Rule D
treats as a writing problem** — which is the better diagnosis, and the same one behind the registers
observation below.

**A two-day debt closed alongside it.** v29's note admitted that folding v28's into
`charter-version-history.md` was *"not claimed as already done here"*. It was never done, and v29's note
then fell out too. **Both recovered verbatim from git** (v28 from `ed4e36e`) and appended; the history
file now covers v8–v29, 34,483 → 39,405 B. *The standing rule moves the outgoing note; nothing owned the
ones that had already fallen out.*

## 9. Offered to the owner, not added — two §3 candidates

**(a) *"Confirmed on two X" is one observation and one assumption sharing a sentence.*** The September
article said the fault was *"confirmed on two different diameters (3mm and 5mm), both times with the
Blind category assigned to multiple bushes."* **The Ø5 half was checked. The Ø3 half was never looked
at** — and there is no blind Ø3 at all. The giveaway is available at writing time: *for the second
instance, which record did I actually open?*

**(b) *A limitation is a property of the call you made* — second instance in five days, first outside
my own tooling.** §3 already carries this from `download_file_content`. Here the manual sat at the
exact path the scanned extract printed on its own first page, for eight days, while this KB answered
three separate questions badly for want of it. **Two occurrences is a pattern; one was an accident.**

## 10. Still open

- **Bush 1** — never opened. The only other position that might be Ø3.
- **Bushes 43, 44, 52, 53** — Ø5 on the layout, types unknown. September's "five blind Ø5" may be an
  undercount; it changes no fix, only the KB's description of the head.
- **Bushes 6-10's useful length**, against the depth of the holes that failed on 15 September — the one
  reading that would settle why Ø5 failed.
- **Whether TpaCAD's dialog "ID" is the optimiser's tool number.** The optimiser identifies tools by
  *"number associated tooling in the group (>= 1)"*. The old fix assumed these are the same field.
- **The Ø3 decision** — master or machine. Owner's, and the machine option is a purchase.
- **`TpaCAD_eng.pdf`, `TpaCadNt_eng.pdf`** — not yet read. The `Z`-datum question lives in one of them.
- **WSC has `Perform Routine Maintenance` and `Perform Extraordinary Maintenance` buttons** — seen in
  passing on a screenshot. This KB records no maintenance interface on the Vitap at all; MT-030…036
  were built entirely from the paper manual, so they may duplicate, contradict or miss what the machine
  already schedules.
- **`Google Drive` is pinned on the Vitap's PC** alongside job folders — first evidence toward D1, the
  shared job folder, open since 2026-09-17. Folder name to be typed, not screenshotted (client data).
