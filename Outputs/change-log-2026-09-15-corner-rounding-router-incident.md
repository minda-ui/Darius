# Change log — 2026-09-15 — Corner-rounding router incident

**Session 4.** Owner reported a defect on the Hebrock F4 (`FA2301`): a gouge/chip-out in the edge
band right at the workpiece corner, on the HMI station whose icon shows two rollers converging on
a corner.

## What was done

**Identified the station.** Read the manual's own HMI icon legend (part 4.pdf, ch.6.2.5) and the
mechanism description (part 3.pdf, ch.4.1.11) to confirm the icon is the **Eckenabrundfräse**
(corner-rounding router) — two rollers (Abtastring/Anlaufring) trace the corner while the router
head moves vertically, top-to-bottom then bottom-to-top — not the radius scraper, which uses a
single tracer disc and no corner-converging geometry.

**Found the manual's own fault-table entry.** Parts 5 and 6 turned out to be the odd/even halves
of a duplex scan of the same page range (129-201) — read together they contain the full Chapter 7
(Wartung) and Chapter 8 (Störungsbehebung) that weren't in parts 2-4. §8.2's "Bauteil:
Eckenabrundfräse" block has an exact match for the reported symptom: *"Der Radius an der
Werkstückecke sieht 'hakelig' aus, evtl. Kantenüberstand"* → cause: stop screw (Anschlagschraube)
misadjusted → fix: loosen locknut, back the stop screw out so the feeler ring protrudes ~0.2mm+
into the workpiece line, retighten.

**Adjustment attempted, overcorrected.** Owner backed the stop screw out per the above. Result:
the station stopped rounding the corner entirely — now just rubs/marks the surface with no cutting
profile. This is the opposite direction from what the fault table's mechanism implies backing the
screw out should do, and wasn't resolved by re-reading the source text further — recorded as an
open discrepancy rather than explained away. Advised reversing direction (turn the screw back in
by a smaller amount than was backed out) and iterating in small steps between the two known bad
states, since the manual gives no numeric target beyond "0.2mm+" (a likely-truncated OCR range).

**Filed three fault photos** to `Raw/` (original gouge, HMI station icon, post-adjustment
marks-no-rounding) and updated `Wiki/Machinery/hebrock-f4-next-edge-bander.md` with a new
"Incidents" section documenting the full diagnosis, the fault-table quote, what was tried, and
what to check next if a stable adjustment can't be found (Abtastring/Anlaufring/Kopierschlitten
bearing wear — these have no scheduled inspection interval in the manual, unlike the main router
station's feeler discs, which are checked weekly).

**Correction to Session 2/3's own maintenance table**: re-reading Chapter 7 in full showed the
"check feeler-disc wipers weekly / check feeler discs for damage weekly" items reported earlier
belong to the main **Frässtation** (router station), not the Eckenabrundfräse. The corner router's
own Chapter 7 entries are limited to a daily clean and weekly guide-shaft oiling, both grouped
under "Kappsäge und Eckenabrundfräse." The Wiki article's maintenance table has been corrected to
say this explicitly, rather than leave the earlier, less precise attribution standing.

## Smartsheet

- Machinery Register: `FA2301` Status changed to **"Under repair"**; Note updated with the
 in-progress fault summary.
- Tasks: **T006** raised, Status "In Progress" — full diagnosis and next steps in the Notes field,
 cross-referenced to the Wiki article's Incidents section.

## Judgement calls made, flagged for the owner

- **Reported the overcorrection as an open discrepancy rather than inventing an explanation for
 it.** The fault table's stated mechanism (backing the screw out should increase engagement) does
 not obviously predict what was observed (backing it out further reduced engagement to zero). Two
 plausible explanations exist (simple overshoot, or the adjustment went the wrong way) but neither
 is confirmed — the advice given (reverse and iterate in small steps) works either way, so this
 was not resolved by picking one theory and asserting it as fact.
- **Did not mark T006 as resolved** — the corner still isn't rounding correctly as of this
 session's end. Left "In Progress" for whoever picks this up next.

## Open questions carried forward

See `Wiki/Machinery/hebrock-f4-next-edge-bander.md`, "Incidents" and "Open questions" —
corner-rounding adjustment (unresolved), owning entity, exact price, purchase-vs-order date, the
F2/F4/F5 dimension-table ambiguity, an illegible dust-extraction spec, and the PLC-battery
part-name mismatch.
