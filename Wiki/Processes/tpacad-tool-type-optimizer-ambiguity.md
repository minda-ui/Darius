---
title: "Process: TpaCAD tool-type auto-resolution ambiguity (\"Tool for this working not found\")"
category: Processes
status: active
sensitive: false
created: 2026-09-15
updated: 2026-09-15
sources:
  - ../../Raw/TPA CAD part 1.pdf
  - ../../Raw/TPA CAD part 2.pdf
related:
  - ../Machinery/vitap-k2-panel-saw.md
---

# Process: TpaCAD tool-type auto-resolution ambiguity ("Tool for this working not found")

This documents a real shop-floor fault found and worked through live on 2026-09-15 while
programming the Vitap K2-2.0 (`FA2304`) via **TpaCAD**, the CAD/CAM program used to build `.TCN`
work programs for it (title bar reads `<filename>.TCN - TpaCAD`; a separate program, **WSC**,
sequences finished `.TCN` files into a run list on the machine). See
`Wiki/Machinery/vitap-k2-panel-saw.md` → Incidents for the specific job this happened on.

## What TpaCAD is

A generic CAD/CAM system ("allows to create, modify and import work programs for the programming
of numerically controlled machines") used across a family of machines, not written specifically
for the Vitap — each installation is customised with machine-specific commands/descriptions.[^1]
Workflow: build/import geometry (DXF import, basic license) → program per-face workings (holes,
fittings, sawings, milling, etc.) → set optimisation (Automatic Sorting or manual Sequence order)
→ save as `.TCN` → load into a WSC run list → run in Automatic mode.[^1][^2]

**This 2-part scan is explicitly an abridged extract, not the complete manual.** Its own first page
says so directly: it's "a generic manual with a description of the TpaCAD standard composition,"
an extract of the complete manual every installation has locally at `Albatros\Help\TpaCad.pdf`,
and it repeatedly defers to three sibling manuals not present in `Raw/`: **`Workings.pdf`** (fuller
detail on every working command's parameters — most likely to cover exactly what's missing below),
`DxfCAD.pdf`, and `DxfToTPA.pdf`.[^1][^2] None of "Solve," "Group together," "Outfit Parameters,"
or "CN Tools" appear anywhere in this extract — that material almost certainly lives in one of
those three un-supplied files. **Open action: track down `Workings.pdf` and the complete
`TpaCad.pdf` from the shop's own Albatros PC** (`Albatros\Help\`) rather than treating this extract
as the full picture.

## The fault

Optimizing ("Solve") a `.TCN` program with a hole/fitting operation set to **Tool type = "Blind
bore drill"** at a diameter that the machine's tool archive (WSCM/TecnoManager) has assigned to
**more than one spindle position (bush) simultaneously** fails with:

> Program optimization encountered errors.
> Face: 1, Working: N, Tool for this working not found.

Confirmed on two different diameters on the same file (3mm and 5mm), both times with the Blind
category assigned to multiple bushes in the outfit. Switching the same operation's Tool type to
**"Through bore drill"** — which in both cases had only ONE bush assigned to that diameter — always
resolved cleanly and let the program optimize.

## Root cause, per the manual

The HOLE working's own parameter documentation explains the mechanism directly:

> **Diameter** — sets the hole diameter. **Tool** — sets the tool number **and prevails over the
> programming per diameter**. **Tool type** — selects the entry that corresponds to the type of
> drilling required. The selection will influence: the choice of the tool that will perform the
> drilling [when programming per diameter], [and] a validity check of the tool in case of
> programming per tool.[^2]

So there are two distinct ways to tell TpaCAD which physical tool/bush to use:
1. **Programming per diameter** (what SmartCabinet's export does by default): set Diameter + Tool
   type, and the optimizer auto-picks a matching tool from the archive. **No tie-breaking rule for
   multiple equally-valid candidates is documented anywhere in this extract.** This is the ambiguous
   path — when 5 bushes all match, auto-resolution apparently can't commit to one.
2. **Programming per tool**: set the **Tool** (ID) field explicitly. This **overrides diameter-based
   auto-selection outright** ("prevails over"), and Tool type becomes a validity check rather than
   a selector — removing the ambiguity entirely.

This is strong documentary support for what was observed: Through bore drill worked because it only
ever had one candidate bush, so auto-resolution never had to choose between several.

## Confirmed directly on the machine: the ID field is real, and it's unset for the whole main bank

TpaCAD's own per-position "Technology" dialog (Outfit `0`, Group `1` — opened from the TCN editor's
outfit view) has an explicit numeric **ID** field, separate from Position and Tool. Checked two
positions directly:
- **Position 101** (one of the four special/aggregated tool-holder positions, 101-104) → **ID
  1001**, Comment "Fresa Ø10mm." This is the *same numbering* as SmartCabinet's own "CN Tools"
  database (1001 = Dia. 10mm there too) — confirming the two systems' ID numbers genuinely
  correspond, at least for positions 101-104, rather than being independent internal references as
  first assumed.
- **Position 4** (part of the main vertical-spindle bank, 1-12/41-44/51-54 — the same bank the
  ambiguous Blind Ø5mm bushes 6-10 and Through Ø5mm bush 2 belong to) → **ID 0**. I.e. unassigned.

This is very likely true of every position in the main bank, not just position 4 — meaning **none**
of the main-bank tools (Blind or Through, any diameter) are currently set up for "programming per
tool"; they're all resolved purely by diameter + type. That's consistent with the fault: Through
Ø5mm still resolves fine with ID 0 because it only ever has one diameter+type match (bush 2); Blind
Ø5mm fails with the same ID 0 because it has five (bushes 6-10) and nothing breaks the tie.

## Fix

- **Immediate, per-file**: as found today, switching the ambiguous operation's Tool type to
  whichever category has only one assigned bush (e.g. Through bore drill) clears the error. This is
  a workaround, not the documented correct mechanism — see next point.
- **Correct fix per the manual, not yet tried on the shop floor (Task T016)**: since the whole main
  bank sits at ID 0, the fix has two parts, not one —
  1. Open the Technology dialog for **one** of the Blind Ø5mm bushes (e.g. bush 6) and give it a
     real, unused ID number (1001/1002/1006/1011/1012 are taken by positions 101-104, so pick
     outside that range).
  2. Then, on the specific failing `HOLE`/`FITTINGX` operation in the TCN program, set its **Tool**
     field explicitly to that new ID instead of leaving Tool type = "Blind bore drill" to
     auto-resolve by diameter. Per the manual, an explicit Tool ID "prevails over" diameter-based
     matching — this should remove the ambiguity outright once both steps are done.
  Neither step has been done yet — planned for the next time the owner is back at the machine.
- **Systemic fix** (affects every future job, not just one file): once step 1 above is done for each
  ambiguous Blind diameter, every future SmartCabinet-exported program still needs its Blind
  operations pointed at that explicit ID rather than left on diameter+type — which likely means
  either manually setting the Tool field per job, or (better, longer-term) getting SmartCabinet's
  post-processor to populate it on export automatically. Not yet actioned — raised for the owner and
  whoever maintains the SmartCabinet post-processor profile.

## Separately found: SmartCabinet's own tool database gap

While tracing this, a **related but distinct** gap was found in SmartCabinet's own tool database
(a "Cam Table: CN Tools" list under a machine/head profile named "Cabineo X" used for a multi-spindle
drill-head definition): it had no entry at all for Dia. 5mm, among five entries covering 10mm, 12mm,
20mm, and two 9.5mm variants. This is unrelated to the TpaCAD optimizer ambiguity above — it's a
gap in SmartCabinet's own head/tool catalog, not the Vitap's tool archive (which does have 5mm
tools, both Blind and Through). Confirmed the physical Vitap has real 5mm bits mounted; the fix
recommended on the day was adding a new "Dia. 5mm" row to that CN Tools list with a description
matching the archive naming convention, since TpaCAD's exported `.TCN` files reference diameter +
type (not SmartCabinet's own internal tool ID numbers), so the new row's ID number doesn't need to
match anything machine-side.

## Open questions

- Complete `TpaCad.pdf` and `Workings.pdf` manuals not yet obtained — would likely confirm the
  auto-resolution tie-breaking behaviour (if any) and give fuller Outfit Parameters/CN Tools
  documentation, and would confirm whether the ID-1000-series correspondence between TpaCAD and
  SmartCabinet's CN Tools holds beyond positions 101-104 (Task T015).
- The two-step fix above (assign a real ID to one Blind Ø5mm bush, then reference it explicitly on
  the failing operation) is planned but not yet tried on the shop floor — the owner was away from
  the machine when this was worked out (Task T016).
- No software version/edition number or vendor contact could be confirmed from this extract (the
  cover page carrying that information wasn't part of either scanned part).

## Sources

[^1]: `Raw/TPA CAD part 1.pdf` — even-ascending half of a duplex-scan pair, printed pages 4-48: software identification, workflow, optimisation settings, macro/UI reference, dashboard safety LEDs.
[^2]: `Raw/TPA CAD part 2.pdf` — odd-descending half of the same pair, printed pages 51-3: HOLE/milling working parameter definitions (incl. the Diameter/Tool/Tool-type mechanism above), DXF import/export licensing, WSC run-list workflow, clamp-machine dashboard (Vitap-branded).
