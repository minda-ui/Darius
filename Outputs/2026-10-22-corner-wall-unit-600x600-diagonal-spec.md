# Corner wall unit 600 × 600, diagonal, 900 high — design spec v0.1

Darius, 2026-10-22, for Minda. **Status: proposal — to be modelled in SmartCabinet, then checked with
`pre-production-drawing-check` before anything is cut.**
Owner's choices (22/10): **diagonal, one angled door; 900 high; both LH and RH.**
Built to the library rules in `Wiki/Software/kitchen-unit-library.md` (master `AMFA Wall Unit 600 RH`).

## 1. Library rules carried over
- **19 mm board throughout** — sides, top, bottom, backs, shelf, door.
- **Sides sit between top and bottom** → side height = 900 − 2 × 19 = **862**.
- **Backs housed** inside the carcase, **16 mm stepped back** from the wall (void for the Häfele concealed wall mount).
- **Shelf 10 mm stepped back** from the carcase front; 1 mm running clearance on its length.
- **Door = height − 4 = 896** high.
- Carcase fixings: as the library (confirmat Plan B, every hole on the Vitap — `carcase-fixings-cabineo-x-vs-confirmat.md`).

## 2. Plan geometry (looking down; corner of the walls at 0,0)
- Back wall along X, side wall along Y. Footprint **600 × 600**, each wing **300 deep**.
- **Right side** at X 581–600, Y 0–300. **Left side** at Y 581–600, X 0–300.
- **Back B** (along the side wall) at X 16–35, Y 16–581. **Back A** (along the back wall) at Y 16–35, X 35–581.
- **Front: one diagonal** from (600, 300) to (300, 600) — **424.3 mm** long, at 45° to both sides.

## 3. Cutting list (per unit; same for LH and RH)
| Part | Qty | Size (mm) | Shape / note | Edges to band |
|---|---|---|---|---|
| Side | 2 | 862 × 300 × 19 | rectangle | front |
| Top | 1 | 600 × 600 × 19 blank | **pentagon**: corner cut on 45° from (600, 300) to (300, 600) | diagonal front (424.3) + the two 300 ends |
| Bottom | 1 | 600 × 600 × 19 blank | same pentagon as top | as top |
| Back A | 1 | 862 × 546 × 19 | rectangle, housed | none |
| Back B | 1 | 862 × 565 × 19 | rectangle, housed; runs past Back A into the corner | none |
| Shelf | 1 (2?) | 545.5 × 545.5 bounding | **pentagon**: (35,35) (580.5,35) (580.5,286.4) (286.4,580.5) (35,580.5) — front diagonal 415.9, 10 mm behind the sides' inner front corners | diagonal front |
| Door | 1 | 896 × **≈ 380–420** × 19 | width **set by the hinge** (§4) | all four |

*Shelf count: the 900 library units — check how many shelves the master carries and match it.*

## 4. Door and hinges — the open point
- The door sits **at 45° to both sides**, so a standard hinge does not fit: it needs Blum **CLIP top angled hinges for
  +45° corner cabinets** (in family **H1** of the Blum library — `blum-clip-top-hinges-smartcabinet-input.md`). **Part
  number, hinge count and the cup/plate positions to come from SmartCabinet's Blum library, not from me.**
- **The door width is set by the hinge's overlay at 45°**, so it is ~380–420 until the hinge is chosen. Door weight ≈
  4–5 kg (896 × 400 × 19 board).
- **LH / RH differ only in the hinge side:** cup holes on the door and plate holes on that side panel mirrored. The
  carcase is otherwise identical — one cutting list, two hinge programs.

## 5. Watch-outs before cutting
1. **Neighbouring doors.** The diagonal door's outer corners come close to the doors of the straight units either side
   (their fronts are 19 mm proud of the 300 carcase). **Check in SmartCabinet's 3D that both swing clear**; if they are
   tight, hinge the neighbours on the side **away** from the corner.
2. **45° cuts** on top, bottom and shelf: on the F45 with the angle fence, or routed on the Vitap (one program, no
   marking out). Your choice.
3. **Edgebanding the pentagons** on the Hebrock: the diagonal is a straight edge, but its ends meet the 300 edges at
   **135°**, not 90° — **check the end trim handles a 135° corner** before running good parts (one offcut test).
4. **Shelf pins**: 5 mm holes on both sides **and** both backs, so the pentagon shelf sits on four or five pins (all on
   the Vitap).
5. **Hanging**: Häfele concealed mounts in the same position as the library units, one per wing.

## 6. Names (proposed)
`AMFA Corner Wall Unit 600x600 Diagonal LH 900` and `… RH 900` — height in the name, per the library's naming-collision
note.

## 7. Next
1. Minda: model it in SmartCabinet (its diagonal corner wall cabinet type, if it has one), with the library's material
   and back/shelf set-backs; pick the +45° hinge from the Blum library.
2. Put the output folder in `Raw/Review folder` → Darius runs `pre-production-drawing-check` (parts vs this spec, hinge
   bores vs Blum, shelf pins, confirmat holes).
3. Cut and edge one **test set from offcuts** first (the 135° edge trim and the door clearance are the two unknowns).
