# Change log — 2026-09-15 — F45 spare parts manual processed

**Session 7.** Owner asked to check `Raw/` for more F45 documents; found a 4-part spare parts
manual (doc 0000010101-006-2023 DE) uploaded separately from the operating/ElmoDrive manuals
already processed.

## What was found

- **Confirms the machine's tilt variant**: the catalogue's own title is "Beidseitige Schwenkung /
 Two-way tilt" — now recorded as a confirmed fact rather than inferred.
- **Does not confirm the serial number.** Like both operating manuals, this is a generic
 model/variant catalogue with no "Machine no." filled in — the serial number remains genuinely
 unconfirmed across all three documents now on file (Task T009 stays open).
- **Does not confirm the drive variant either** — lists ProDrive/EvoDrive/ElmoDrive as three equal
 options without saying which this specific machine has; that confirmation still rests solely on
 the previously-processed ElmoDrive control-unit manual.
- **Real manufacturer ordering contact**: phone, email, and the Altendorf spare-parts webshop —
 the first concrete supplier-type contact detail found for either machine so far.
- **Useful wear-part numbers**: main/scorer drive belts, riving-knife holder (rated to Ø450mm
 blades), saw shaft assembly, scorer blade diameter (Ø180mm), sub-roller/guide-roller parts.
- **Does not resolve two open questions**: no PTC resistor and no F1/F2/F8/F9/F15/F16 fuse
 cross-reference anywhere in the catalogue; the dust-extraction volume discrepancy (1150 vs
 1110 m³/h) also isn't addressed, since this document has no extraction section at all.
- Same duplex-scan pattern as the other manuals: parts 1-2 confirmed as an odd/even pair (pages
 2-98); parts 3-4 very likely a second such pair (pages ~99-147) but which file carries odd vs.
 even couldn't be pinned down from OCR alone — noted as a limitation rather than guessed at.

## What was done

- **Updated** `Wiki/Machinery/altendorf-f45-panel-saw.md`: added the spare parts manual to
 sources, confirmed the two-way-tilt variant in Key facts, added a new "Key spare/wear parts"
 subsection to the maintenance section, updated Open questions (PTC/fuses still unidentified,
 serial number still unconfirmed by any of the three documents now on file).
- **Created** `Wiki/Suppliers/altendorf-gmbh.md` — the manufacturer's contact/ordering details,
 explicitly distinguished from the still-unidentified actual UK seller on invoice 100153.
- **Smartsheet**: 4th Document Register row added for the spare parts manual (`Document No.`
 `pending`, same reasoning as the other documents).
- Updated `Wiki/index.md`, `kb-registers.md`.

## Judgement calls made, flagged for the owner

- **Did not treat "confirms two-way tilt" as also confirming ElmoDrive** — the two facts come from
 different documents and shouldn't be conflated just because they're both true of this machine.
- **Did not guess at PTC-resistor or fuse part numbers** from the closest-sounding components found
 (a brake resistor, a permanent-magnet brake) — recorded the search as a genuine negative result
 instead of a near-match.
- **Created a Suppliers article for the manufacturer, not the invoice's UK seller** — the two are
 not the same thing, and conflating them would misdirect anyone trying to actually order a part
 or query the original purchase.

## Open questions carried forward

See `Wiki/Machinery/altendorf-f45-panel-saw.md`, "Open questions" — unchanged in substance from
Session 6 except: serial number is now confirmed unconfirmed by all three documents (not just two),
and manufacturer contact details are now on file even though the actual seller still isn't.
