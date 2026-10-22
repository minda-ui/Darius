---
name: new-library-unit-design
description: Design a new cabinet or library unit for the workshop before it is drawn in SmartCabinet — a corner, wall, base, tall or special unit. Use when the owner says "design a … unit", "new corner/wall/base unit", "I need a … cabinet", or gives sizes for a unit that is not in the library yet. Produces a spec in Outputs, then hands over to pre-production-drawing-check.
---

# New library unit design

Adopted at the 2026-10-22 good night, from the 600 × 600 diagonal corner wall unit (spec v0.1 → v0.4 in one day) and the
LEGO drawer unit (2026-10-05). The rules it applies live in the Wiki — cite them, do not copy.

## Steps
1. **Ask only the real choices, in one question set** (`AskUserQuestion`): type/shape, height family (720 / 900), hand
   (LH / RH / both), shelves, door type, edge style. Recommend one option where the KB supports it.
2. **Apply the library rules** (`Wiki/Software/kitchen-unit-library.md`, master `AMFA Wall Unit 600 RH`): 19 mm board,
   sides between top and bottom, backs housed with the **16 mm** step-back (Häfele hanger), shelves **10 mm** back,
   door = height − 4, width − 3; carcase fixings per `carcase-fixings-cabineo-x-vs-confirmat.md` (every hole on the Vitap).
3. **Check the machines' limits before proposing geometry:** the **Hebrock edges rectangular panels, square edges only**
   (`hebrock-f4-next-edge-bander.md`: not rated for non-rectangular work; no bevel unit) — non-90° corners need hand
   trimming; bevels need the F45 tilt and cannot be edged. Say the cost in hand work.
4. **Hardware from the maker's data, not memory:** Blum full text `Raw/Blum/Blum-2022-23_full-text.txt`
   (`1UBmfS7dzkLdiBZur_DDlprsw47cFmewS`) — grep the application ("corner cabinet", "+45°"), then render the planning page
   from the family PDF and pick the planning case that matches the edge style. Give part numbers + mounting plate, and
   check they exist in SmartCabinet's accessory list (ask for a screenshot).
5. **SmartCabinet route:** fetch the manual page for the shape (`smartcabinet.eu/manuale/mainit/smartcabinet/…`, e.g.
   `progettazione_misure-forma`) and give field-by-field values; recommend **starting from the master** (Save As) so the
   library's accessories and settings come along (a blank start raised "Non Definito" accessories).
6. **Write the spec** `Outputs/<date>-<unit>-spec.md` (cutting list with arithmetic, hardware table, watch-outs, names with
   the height in them); version it as answers come in; publish and verify.
7. **Hand over:** the owner models it and puts the export in `Raw/Review folder` → `pre-production-drawing-check`
   against this spec.

## Never
- Never propose geometry the machines cannot make without saying so.
- Never give a hardware part number not read from the maker's data in this session.
