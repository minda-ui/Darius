# Change log — TpaCAD tool-ambiguity incident (2026-09-15)

Session 9. Live shop-floor troubleshooting session (not a Raw-folder-triage session): the owner hit
a real fault programming the Vitap K2-2.0 (`FA2304`) for its first real kitchen job, worked through
it interactively, then supplied the TpaCAD software manual (2 parts) for processing.

## What happened

- SmartCabinet-exported `.TCN` programs with hole/fitting operations set to Tool type = "Blind bore
 drill" failed to optimize ("Solve") with "Tool for this working not found," on two diameters
 (3mm, then 5mm) in the same file.
- Worked through the machine's own tool archive (WSCM/TecnoManager) live with the owner: confirmed
 both Blind and Through tools exist and are physically loaded for the affected diameters — ruling
 out a missing-tool explanation before it was assumed.
- Root cause, confirmed both from the TpaCAD manual text and directly on the machine: Blind bore
 drill at the affected diameters is assigned to *multiple* spindle positions (bushes) at once (e.g.
 5 bushes for Ø5mm), none of them carrying an explicit Tool ID (all sit at ID 0) — so TpaCAD's
 diameter+type auto-resolution has multiple equally-valid candidates and no documented tie-breaker.
 Through bore drill always resolved cleanly because it only ever had one matching bush.
- The manual's own HOLE-working documentation confirms an explicit Tool ID field "prevails over"
 diameter+type matching — i.e. the documented correct fix. Confirmed live on the machine that
 position 101 (a special tool-holder slot) does carry a real ID (1001) matching SmartCabinet's own
 "CN Tools" numbering, while position 4 (main spindle bank, same bank as the ambiguous bushes)
 sits at ID 0 — direct evidence the fix hasn't been applied anywhere in the main bank yet.
- Separately, found SmartCabinet's own "Cabineo X" drill-head tool database has no Dia. 5mm entry
 at all (only 10/12/20/9.5mm) — a related but distinct gap in SmartCabinet's own catalog, not the
 Vitap's tool archive.
- Owner was away from the machine at the point the two-step fix (assign a real Tool ID to one Blind
 Ø5mm bush, then reference it explicitly on the operation) was identified — not yet tried.
- Owner then supplied `TPA CAD part 1.pdf` / `part 2.pdf` from `Raw/` for KB processing: confirmed
 the same duplex-scan artefact as every other manual in this KB (even-ascending + odd-descending,
 reconstructing printed pages ~1-51), and confirmed this 51-page document is itself an **abridged
 extract** — the complete manual (`TpaCad.pdf`) and a fuller `Workings.pdf` live locally on the
 shop's Albatros PC (`Albatros\\Help\\`) and were not supplied.

## What was done

- Created `Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md`: full root-cause writeup, the
 documented fix mechanism, the live machine confirmation (ID field), the fix procedure, the
 separate SmartCabinet CN Tools finding, and open questions.
- Updated `Wiki/Machinery/vitap-k2-panel-saw.md`: added an Incidents section for this fault (status:
 workaround in place, permanent fix pending), added TPA CAD sources/related links, updated the
 Control row in Key facts and the Open questions list.
- Updated `Wiki/index.md` to list the new Processes article and reflect the Vitap article's new
 Incidents content.
- Updated `Outputs/kb-registers.md` and `CLAUDE.md` (v6) with this session's changes and lesson.
- Smartsheet Document Register: added a row for the TPA CAD manual (2 parts).
- Smartsheet Tasks: added T015 (track down the complete `TpaCad.pdf`/`Workings.pdf` manuals from the
 shop's own Albatros PC) and T016 (try the documented Tool-ID fix on the shop floor next session,
 confirm it resolves the ambiguity permanently).

## Judgement calls made, flagged for the owner

1. Treated the live troubleshooting conversation as a genuine Incident on `FA2304`'s own Wiki
 article (mirroring how the Hebrock F4's corner-rounding router fault was documented), rather than
 only writing it up as an abstract Processes article — because it's a real fault on a specific
 machine's first real job, not just a general software-behaviour note.
2. Did **not** assume the SmartCabinet CN Tools gap (missing Dia. 5mm) and the TpaCAD optimizer
 ambiguity (Blind bore drill "tool not found") were the same problem, despite surfacing in the
 same session — they're two distinct issues in two distinct systems (SmartCabinet's own head
 catalog vs. the Vitap's outfit/tool-ID resolution), documented separately in the Processes
 article rather than conflated.
3. Marked the fix as "identified but not yet tried" rather than "resolved," since the owner was away
 from the machine — the Incident stays open (and Task T016 stays open) until it's actually
 confirmed working, consistent with how the Hebrock corner-rounding incident wasn't marked
 resolved until the fix was confirmed on the real machine.
4. Did not attempt to guess at the software's version/edition or vendor contact details, since the
 cover page carrying that information wasn't present in either scanned part — recorded as unknown
 rather than inferred.
