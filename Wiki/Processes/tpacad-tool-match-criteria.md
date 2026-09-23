---
title: "Process: how TpaCAD's optimiser matches a tool to a hole — and why \"Tool for this working not found\" has only ever meant one thing"
category: Processes
status: active
sensitive: false
created: 2026-09-23
updated: 2026-09-23
sources:
 - "`Raw/Albatros-help-en-GB-2026-09-23/CnCadOpti_eng.pdf` (Drive `1fm4v-f8u6suiR3fBULQxbI72jU3OmU_I`, 758,979 bytes, dated 26/11/2019, v. 2.3.8) — TPA's own documentation for the Optimize CnCadOpti module. Pages 1-3 and 6-11 read in full 2026-09-23; all 19 pages extracted to text"
 - "`Raw/Albatros-help-en-GB-2026-09-23/Workings_eng.pdf` (Drive `11oEu1FlzMdb9h0c-iqFvQA-ELLJIwb1L`, 3,728,330 bytes, dated 05/04/2020, v. 2.4.0) — the complete workings reference, 337 pages, all extracted; DRILLING, CIRCLE, CIRCLE EMPTYING, HINGE and CABINEO sections read in full"
 - "Owner at the machine, 2026-09-23 — WscTecnoManager readings of bushes 2, 3 and 6-10, and the failure of `03-BOTTOMB.TCN`"
 - "`Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md` — the contemporaneous 2026-09-15 record, re-read in full before this article was written"
related:
 - ./tpacad-tool-type-optimizer-ambiguity.md
 - ./tpacad-blind-bore-tool-id-fix.md
 - ./tpacad-interpolated-holes.md
 - ./carcase-fixings-cabineo-x-vs-confirmat.md
 - ../Machinery/vitap-k2-drill-head-tooling.md
 - ../Machinery/vitap-k2-panel-saw.md
---

# How TpaCAD's optimiser matches a tool to a hole

**This article supersedes the root-cause explanation in
`tpacad-tool-type-optimizer-ambiguity.md` and the whole procedure in
`tpacad-blind-bore-tool-id-fix.md`.** Both are left in place, corrected in their own words, because
the record of having been wrong is worth more than a tidy KB. Read this one before acting.

## The correction, stated first

Since 2026-09-15 this KB has recorded that *"Tool for this working not found"* means **the optimiser
found several equally valid tools and could not choose between them.** Every downstream document took
it up: the task note, `CLAUDE.md` §7, the fix procedure, and the kitchen-unit library's blocking
condition.

**That failure mode does not exist.** TPA's own documentation for the optimiser module lists every
error it can raise, and the relevant one is:

> **−27 · Working: tool match not possible** — No tool can be used in execution of a drilling working
> programmed with diameter.[^1]

**The error fires when nothing matches, not when several do.** And the module is built to *expect*
several: §1.5 says that for a hole programmed by diameter *"is first evaluated if there is **at least
one** tool which can work working"*, and §1.6 then aggregates similar holes across tools into single
drilling beats.[^1] Multiple candidates are the normal case, not the fault.

**Nothing in the 2026-09-15 session was faked or careless.** The observations were real: blind Ø5
failed, through Ø5 worked, and the main bank sat at ID 0. What went wrong is that a *mechanism* was
invented to join them, and the mechanism was never checked against a document — because the document
we needed was believed not to exist. It was on the machine's own hard drive the whole time (Task
T015, closed 2026-09-23).

## The five criteria — the diagnostic this KB has never had

A hole programmed **by diameter** (Diameter + Tool type, no explicit Tool) resolves to a tool only if
**every one** of these holds. Verbatim:[^1]

> - matching the diameter (less than epsilon)
> - the tool type of the working corresponds to that of the tool (the control is if working set type > 0)
> - the tool can work the face of application of the working
> - the useful length of the tool is greater than or equal to the depth of entry programmed
> - the required position is within the limits allowed for axe[s]

Fail any one, for **every** tool on the head, and you get −27. The message does not say which criterion
failed, which is why it has been so hard to read.

**Work it as a checklist, in this order** — it is cheap and it is exhaustive:

| # | Check | Where to look |
|---|---|---|
| 1 | Is there a tool of that **diameter** at all? | WscTecnoManager |
| 2 | Does its **type** match what the operation asks for? | Comment line: `passante` = through, `cieco` = blind |
| 3 | Can it **work that face**? | tool's working faces |
| 4 | Is its **useful length** ≥ the programmed depth? | Tool Length / effective length vs the `Z` on the operation |
| 5 | Is the **position within axis limits**? | X/Y of the operation |

Note criterion 2's parenthesis: *"the control is if working set type > 0"*. **A hole with `Tool type`
left unset skips the type check entirely.** That is a real lever, and a real trap — it will match a
tool of the wrong type without complaint.

## Applied: `03-BOTTOMB.TCN`, 2026-09-23 — confirmed

`600mm Base Appliance Housing unit/03-BOTTOMB.TCN`, face 1, working 11. The holes read
`HOLE EG0 X587.0 Y48.0 Z-13.0 TD3 TP0` — Ø3, no tool assigned, 13 mm deep in a 19 mm panel, so a
**blind** hole programmed by diameter.

| # | Criterion | Result |
|---|---|---|
| 1 | Ø3 exists | **Pass** — bush 3 |
| 2 | Type matches | **FAIL** — the operation asks blind; bush 3 is `Foratore passante Ø3mm`, and the owner confirmed Ø3 is *only* `passante` on this head |
| 3 | Face | Pass (presumed) |
| 4 | Useful length ≥ 13 | Pass — Tool Length 53 |
| 5 | Axis limits | Pass (presumed) |

**One criterion fails, and it fails for every tool on the head, because there is exactly one Ø3 and it
is the wrong type.** The optimiser was correct and precise; the KB had taught us to read it as
something else.

**This is a tooling/design mismatch, not a software fault.** SmartCABINET is exporting a hole the
machine cannot drill blind. Either the master should not specify blind Ø3, or a blind Ø3 bit belongs
on the head — **an owner's decision, and the second option is a purchase.** See
`vitap-k2-drill-head-tooling.md` for what is actually fitted.

## Applied: the 2026-09-15 Ø5 failure — unexplained, and stated as such

Bushes 6-10 were confirmed on 2026-09-23 to be `Foratore cieco 5mm` — **five blind Ø5 drills, exactly
as recorded in September.** So if the failing operation asked for blind Ø5, criterion 2 passed and
something else failed.

**Criterion 4 is the obvious candidate**: the module distinguishes a tool's *total* length from its
*effective* length,[^1] and −28 exists precisely for *"the useful length of the tool is less than the
programmed entry depth."* If the blind Ø5s' useful length falls short of those holes' depth while the
through Ø5 at bush 2 (Tool Length 48) clears it, the observed behaviour follows exactly.

**That is a hypothesis and it is not to be written up as anything else.** This KB has just spent eight
days acting on a confident mechanism that no document supported; the correct state here is *"we do not
know, and here is the one reading that would tell us."*

**To settle it: bushes 6-10's Tool Length and useful length, against the programmed `Z` of the holes
that failed on 2026-09-15.** One dialog, five clicks.

## Programming by tool — and the trap in the old procedure

The alternative is to set the operation's `[T] Tool` field explicitly. The Workings manual confirms
the precedence:

> **[TD] Diameter** — Tool diameter. … **The assignment of the Tool field prevails on the Diameter
> assignment.**
> **[T] Tool** — Tool number. **If set, it prevails on the Diameter assignment.**[^2]

But the type check does **not** go away:

> **−25** — The type of tool in working does not match the selected tool (working set a type > 0). …
> if programming a tool.[^1]

**So `tpacad-blind-bore-tool-id-fix.md`'s instruction to "leave `Tool type` alone" while setting an
explicit Tool is wrong.** Anyone following it with a mismatched type gets a *new* error, −25, and
reasonably concludes the fix failed. Either clear `Tool type` or make it agree with the tool.

**And a prior question nobody has asked.** The optimiser identifies a tool by *"number associated
tooling in the group (>= 1)"*.[^1] The September fix assumed the **ID** field in TpaCAD's per-position
Technology dialog is that number. **It may be; it is unverified.** If every main-bank bush really sits
at ID 0 and the optimiser requires ≥ 1, no main-bank tool can be programmed by tool at all until one is
given a number — which is what the old procedure guessed at, for the wrong reason. Worth establishing
before anyone edits an outfit.

## Error codes worth knowing

Drilling and tooling errors from the optimiser module, verbatim descriptions:[^1]

| Code | Label | Means |
|---|---|---|
| −23 | the programmed tool does not exist | a `Tool` number > 0 that is not in the archive |
| −24 | invalid programmed tool | `Tool` ≤ 0 on a setup or blade setup |
| −25 | *"Tipo utensile non valido"* (untranslated in the manual) | programming **by tool**, and the working's type ≠ the tool's type |
| −26 | invalid programmed diameter (≤0) | a drilling working with no tool and a zero/negative diameter |
| **−27** | **tool match not possible** | **programming by diameter, and nothing satisfies all five criteria** |
| −28 | depth greater than tool length | useful length < programmed entry depth |
| −30…−35 | over axis limit X / Y / Z | position outside the permitted travel |
| −40 | incoherent tool with the working face | the tool cannot work that face |

*The on-screen string the shop sees is "Tool for this working not found", which is not the manual's own
label for any of these. Mapping it to −27 is an inference from the meaning, not from the text — the
manual is dated 2019 and the UI string may have changed. It is the only entry whose description fits.*

## What this does not settle

- **The September Ø5 root cause.** Hypothesis only, above.
- **Whether TpaCAD's dialog "ID" is the optimiser's tool number.** Unverified.
- **`CIRCULAR INTERNAL WINDOW`'s `Diameter` field.** The string appears **nowhere in the 337 pages** of
  `Workings_eng.pdf`, so it is a custom working for this installation and TPA's manual cannot define it.
  What the manual does give is the general mechanism: the standard `CIRCLE` programs geometry as
  `[R] Radius` and handles the tool separately through `[DN] Compensation` (Off / Left / Right) and
  `[D] Compensation radius`.[^2] **So look at the custom working's own fields first** — if it exposes a
  compensation setting that is on, `Diameter` is the finished hole; if compensation is off, the tool
  centre follows the programmed circle and `Diameter` is the toolpath. That is a look, not a test cut.
- **`THREE HOLES HINGE`.** No such table exists in `Workings_eng.pdf`. The native `HINGE` working takes
  only X, Y, Z and a tool.[^2] This KB has expected that table since 2026-09-18; it should stop.
- **Whether `Z` is measured to the drill's shoulder or its tip.** Not answered in either manual read so
  far. It decides whether a 13 mm blind hole drilled with a pointed through-drill breaks through a
  19 mm panel. `TpaCAD_eng.pdf` (7.7 MB, not yet read) is the next place to look.

## Also found, and unrelated

**`CABINEO` is a native TpaCAD working**, not something this shop has to build. Its optional drilling
is specified exactly:

> **[EH] Enable drilling** — "Select this option to request the drilling working: it is **3 holes with
> a 15 mm diameter executed up to a 11 mm depth**."[^2]

The head carries Ø3, Ø5, Ø8, Ø10, Ø12 and Ø35 — **no Ø15**. So the native route is unavailable without
a bit, and routing the pocket remains the only option. That is the conclusion
`carcase-fixings-cabineo-x-vs-confirmat.md` already reached from the vendor's published figures; it is
now confirmed from the machine's own manual, with the depth as well as the diameter.

## Sources

[^1]: `CnCadOpti_eng.pdf` — "Project TpaCAD, Optimization of a program-piece, Optimize CnCadOpti v. 2.3.8", 26/11/2019. §1.1 Technology, §1.5 Technological optimization, §1.6 Match of drilling beats, §1.8 Error messages.
[^2]: `Workings_eng.pdf` — "Workings, TpaCAD 2.4.0", 05/04/2020. DRILLING (p.1), CIRCLE (p.146), HINGE (p.263), CABINEO (p.270); page numbers as printed in the document.
