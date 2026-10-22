# Corner wall unit 600 × 600, diagonal, 900 high — design spec v0.4

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
| Shelf | **2** | 545.5 × 545.5 bounding | **pentagon**: (35,35) (580.5,35) (580.5,286.4) (286.4,580.5) (35,580.5) — front diagonal 415.9, 10 mm behind the sides' inner front corners | diagonal front |
| Door | 1 | 896 × **≈ 380–420** × 19 | width **set by the hinge** (§4) | all four |

*Shelf count: **two**, as the 900 library units (owner, 22/10). Spaced equally unless the master's pin rows say otherwise: 862 inside ÷ 3 ≈ 268 mm clear openings with 19 mm shelves — the drawing check compares against the master's pin positions.*

## 4. Door and hinges — square-edged sides (owner, 22/10)
- **Owner: "square edges please".** The Hebrock edges rectangular panels with square edges only (its manual: *not rated
  for non-rectangular workpieces*; no tilting unit), so the **sides keep a square, Hebrock-edged front** — no 45° bevel.
- That rules out Blum's +45° II (flush front, assumes bevelled sides — spec v0.3, **withdrawn**). Blum's **+45° I, half
  overlay, "for corner cabinets with set back fronts"** has a planning case drawn with a **square-edged side**:
  **planning Nº 53, 45°** (catalogue p. 119: 34 / 5.5 / 5 / 20).
  | Item | Part no. |
  |---|---|
  | Hinge, CLIP top BLUMOTION +45° I, screw-on boss, 95° | **79B9658** (INSERTA: 79B9698; without soft-close: 78A9658.T) |
  | Mounting plate, 0 mm | **173H7100** |
- **The door sits set back** behind the sides' square front edges, which stay visible as an edged reveal either side.
  **Door width = LW**, the internal width between the sides at the door line (p. 118: FB = LW); 896 high. Opens **95°**.
- Set back inside the diagonal, the door **cannot clash** with the neighbouring units' doors.
- **SmartCabinet:** keep the sides' front edges at **90°** (the manual offers this for the chamfered shape — look for the
  same option on the corner shape or under Sides), and set the door as **set back / inset** on the diagonal. Add
  **79B9658** and **173H7100** to the `35 CERNIERE` list and its CAM hinge table — neither is there now (photo 22/10).
- **Still hand work:** the diagonal edges of top, bottom and both shelves meet the short edges at 135° — Hebrock with
  corner rounding off, ends trimmed by hand (8 short trims per unit). Everything else is normal Hebrock work.
- LH / RH: hinges on the left or right side only; the carcase is identical.

## 5. Watch-outs before cutting
1. **Neighbouring doors.** The diagonal door's outer corners come close to the doors of the straight units either side
   (their fronts are 19 mm proud of the 300 carcase). **Check in SmartCabinet's 3D that both swing clear**; if they are
   tight, hinge the neighbours on the side **away** from the corner.
2. **45° cuts** on top, bottom and shelf: on the F45 with the angle fence, or routed on the Vitap (one program, no
   marking out). Your choice.
3. **Edgebanding the pentagons** on the Hebrock: the diagonal is a straight edge, but its ends meet the 300 edges at
   **135°**, not 90° — **check the end trim handles a 135° corner** before running good parts (one offcut test).
4. **Shelf pins**: 5 mm holes on both sides **and** both backs, so each pentagon shelf sits on four or five pins — two
   shelves, so two sets (all on the Vitap).
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
