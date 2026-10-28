# Change log — 2026-10-28 — workshop plans received

Darius, session 41.

## 1. Unit 30 plans filed
- Owner: *"This is a plan of workshop"* — two AutoCAD 2024 PDFs, A3, 1:100:
  - `GF_30.pdf` → `Raw/Unit 30 - Ground floor plan (GF_30, 22-05-2024).pdf` (`15rmCPSKiABU_6N6d0b1cmKV0mRe3wa9Y`):
    *Ground floor plan*, title block Fishbone Drylining Ltd, 22/05/2024, drawn Kindrat, checked Gaudiesius/Prutkovas,
    Unit 30, sheet 3; shows office, meeting room, server, canteen, two WCs and the open floor (drawn rotated).
  - `Unit_30.pdf` → `Raw/Unit 30 - dimensioned plan (Unit_30).pdf` (`1zmBHrsB-6d3Gflymqh2qUWR4BRYySDZK`): dimensioned
    plan, no title block — main hall **11,870 wide × 9,970 (right) / 6,900 (left) deep**, heights **H = 3,830** and
    **H = 4,760**; a 3,350 × 6,850 room with a 1,620 double door; rooms 4,300 × 2,470 (H = 2,300) and 4,300 × 5,230;
    two pairs of small rooms 1,005 / 1,400 × 1,970 / 1,960; corridor 3,920 / 4,735; entrance door 900, window 3,000.
  - Both byte-checked SAME. Which area is the workshop floor, and where the machines stand, not yet stated.
- Not yet in the Wiki or the Workshop Document Log — waiting for the owner's purpose (machine layout, fire plan, …).
- Owner: *"Ignore GF30 file"* — **`Unit_30.pdf` is the workshop plan; GF_30 is not to be used.** GF_30 left in Raw
  untouched (not deleted), marked here as ignored.

## 2. Extractor and compressor — proposed new position
- Owner marked a corner on **GF_30** (the lower hall's left corner, by a small rectangle drawn in blue): *"I want to place
  extractor and compressor in red circle area"*. (Same message thread had said "ignore GF30" — the mark is taken as a
  location only; dimensions still to come from Unit_30.)
- **Contradiction recorded, not resolved:** both plans are **Unit 30**; `Wiki/Machinery/aes-saf-10000-stk-extractor.md`
  says the machines *"have also since been moved to Unit 31"*. Asked which unit the workshop is in, or whether this is
  a planned move.
- Facts on file: extractor `FA2402` 1200 × 3170 × 2330 mm, 720 kg, 11 kW; compressor `FA2306` 15 kW, 455 kg, model
  string `GENESIS 15 500L` (receiver unconfirmed, T021) — **no compressor footprint on file**.
- Points raised: footprint and service space; the compressor's cooling air must not be the extractor's dusty/warm air;
  a dust collector's fire/explosion siting is an HSE question (Anna); two new three-phase supplies (11 + 15 kW) are an
  electrician's job; duct and air-line runs depend on where the F45, Hebrock and Vitap stand; forklift access and bin
  emptying; noise near the entrance.

## 3. Zones marked by the owner on GF_30
- **Workshop:** the L-shaped area — the large hall on the left plus the bay running down past the meeting room to the
  bottom-left corner (the extractor/compressor corner, on an external wall, beside a small blue square).
- **Storage:** the bay to its right, along the canteen side down to the bottom-right wall, with a dashed line along
  it. Plan dimensions there: **10,136** along the right-hand wall and **4,237** across the bottom (read off the drawing;
  where the 4,237 starts against the dashed line is not certain). The plan gives no dimensions inside the workshop bay.
- So GF_30 is used for **zones**, Unit_30 for room sizes; the owner's "ignore GF30" taken to mean its office detail.
- Owner: *"This is a plan for unit 30 and 31"* — **contradiction resolved**: one plan covers both units (title block
  reads "Unit 30"); the Wiki's "moved to Unit 31" stands. Which unit each zone sits in is not stated.
- Owner marked the units on GF_30: **Unit 31** = the large hall on the left plus the room above it (with the stair
  block); **Unit 30** = office, meeting room, server, canteen, WCs and the lower bays. So the **workshop spans both
  units**: its large hall is in 31, its lower bay — and the proposed extractor/compressor corner by the blue square —
  sits on the 30 side, at the boundary. **Storage is in Unit 30.**
- Owner marked **where the extractor stands now**: in the workshop bay against the wall beside the server room /
  meeting-room corner (Unit 31 side of the boundary). The proposed corner is further down the same bay — **about 7 m**
  (scaled off the drawing: the 10,136 dimension spans ≈ 286 px, so ≈ 35 mm/px; ≈ 195 px between the two marks). An
  estimate from a drawing, not a measurement.
- Owner marked **where the F45 stands now**: lower part of the Unit 31 hall, beside the extractor, its area drawn
  across the thin double line inside the hall — so that line is presumably not a wall any more (asked). Scaled off the
  drawing (≈ 35 mm/px): F45 to the extractor now ≈ 3.5–4 m; to the proposed corner ≈ 8 m. Estimates, not measurements.
- Owner marked **where the F4 (Hebrock) stands now**: in the hall above the F45, towards the stair block, also across
  the thin double line. Scaled: F4 to the extractor now ≈ 5.5 m; to the proposed corner ≈ 11.5 m (estimates).
- Owner marked **where the Vitap stands now**: at the far left of the Unit 31 hall, by the left wall.
- **Straight-line distances to the extractor, scaled off GF_30 (≈ 35 mm/px; estimates — real duct runs are longer):**

  | Machine | To the extractor now | To the proposed corner |
  |---|---|---|
  | F45 | ≈ 3.5–4 m | ≈ 8 m |
  | F4 (Hebrock) | ≈ 5.5 m | ≈ 11.5 m |
  | Vitap | ≈ 12 m | ≈ 16 m |

  The move adds roughly 4–6 m to every run. More duct means more resistance and less suction at each port; suction is
  reported "perfect" now (26/10, FL-003). Asked why the move, and where the compressor stands now.
- Owner marked the **assembly area**: top-left of the Unit 31 hall, behind the Vitap.
- **Layout sketch** `Outputs/2026-10-28-workshop-layout-current-and-proposed.png` (Drive `1aGW1CnwkIABMNQPVH0Crbxyk8sZ_lqLX`): every zone and machine
  the owner marked, drawn approximately over GF_30 (positions hand-traced from the owner's marks, not measured), board
  flow storage → F45 → F4 → Vitap → assembly, and duct lines from the proposed corner. Reading: the proposed corner is
  off the board route from storage, but every duct run gets longer; the Vitap, the furthest machine, goes to ≈ 16 m.
- Owner: *"Create for checklist for pictures to do"* → `Outputs/2026-10-28-photo-checklist-extractor-compressor-move.md`
  (Drive `1U6laXuE4tcX6r3jg6nproAOLKnp79jlj`): corner, compressor (incl. tank plate — also answers T021), extractor, ductwork, outside wall.

## 4. Workshop layout plan — phase 1 (existing) started
- Owner: *"I will need your help with planning workshop. Now we are removing a lot of things around both units. … But
  first let's create existing and when we will move to next phase planning."*
- `Outputs/2026-10-28-workshop-layout-plan.md` (Drive `1mTiTZr-6xvtETHErZrZcwxSK0Xe2H-eo`), a working document: base drawing and scale; zones;
  inventory of machines (footprints from the Wiki: Vitap 2,940 × 1,710, ≥ 1,000 clearance; extractor 1,200 × 3,170;
  F4 ≥ 500 clearance; **F45 and compressor footprints not on file**) and of everything else to place; survey method
  (two distances to two walls per item); phase-2 criteria (draft).
- **Scale finding:** GF_30 is not true 1:100 — its own dimension lines measure 36.95 and 38.0 mm per PDF point against
  35.3 for 1:100 (pdftocairo SVG, magenta dimension lines). Distances off it are ± 5 % estimates.

## 5. The owner's dimensioned drawing of the existing workshop
- Owner: *"i have uploaded newest drawing with exact position of machinery now to Raw folder"* →
  `Raw/last planning  furn.prod.shop.pdf` (`1_Itj0qPDKAI4qtGrrphf5btT2NCPMMGc`), AutoCAD A3, PDF created 14/10/2024, no
  scale stated (≈ 26 mm/pt measured from its dimension lines).
- Read and recorded in the layout plan §2a: F45 zone 6,500 × 4,500; F4 4,200; Vitap 2,900 × 1,710; extractor ("Hood")
  3,200 × 1,200 with 700 to two walls; racking 2,500 × 1,500; mitre saw bench 1,200 deep; two unlabelled items
  (2,500 × 2,200; 2,500 × 1,200 in the proposed corner); **no compressor on the drawing**.
- Finding: Vitap 800 mm from the mitre saw bench against the manual's ≥ 1,000 mm. Asked: the two unlabelled items,
  where the compressor is, and whether the 2024 drawing is still current.
- Owner: *"A and B is panel racks now"* — both unlabelled items are **panel racks** (2,500 × 2,200 and 2,500 × 1,200);
  rack B stands in the proposed extractor/compressor corner.
- Owner marked **the compressor**: in the 6,000 × 5,720 room above the hall, bottom-right corner by the stair block
  (a separate room from the dust). Labelled existing layout `Outputs/2026-10-28-workshop-existing-layout.png` (Drive `10FTtkIKnbJQ-bdlrfVwNl_tc_TriiN0r`) — the owner's drawing with the
  racks and compressor added; compressor footprint still to measure.
- Owner: *"No, that's the layout now"* — the 2024 drawing is current. **Phase 1 (existing) done**, bar the compressor
  footprint.

## 6. Phase 2 started
- Owner: *"Server room and panel racks are going for good"* — recorded in the layout plan §6a. Open: where the server
  rack / network equipment goes.
- Owner: *"Racking in assembly area going too"* — the 2,500 × 1,500 racking goes; recorded in §6a.
- Owner marked the **new full-panel storage**: Unit 30 bay at the bottom wall, straight in from the double doors for the forklift. Scaled ≈ 4.2 × 4.5–5.8 m; recorded in §6a with what is still to confirm.
- Owner: *"This wall is removed already"* — the wall between the workshop bay and the Unit 30 bay (meeting-room corner to the bottom wall) is gone; the bays are one floor. Recorded in §2a; GF_30 is out of date there.
- Owner: panel racking = panel size + 100 mm each side → **3,000 × 2,270 per bay**; two side by side (4,540) exceed the ≈ 4.2 m marked. Recorded in §6a.
- Owner: existing racking ≈ 3.6 m high, sheets flat, one shelf per colour. Recorded in §6a with the ceiling and forklift-lift checks.
- Owner: racks loaded from the short side; double door 2.4 m wide. Recorded in §6a (2,070 across the door, ≈ 165 mm clear each side; 2,270 rack face to the doors, 3,000 deep).
- Owner: vacuum lifter idea for moving panels → layout plan §6b: lifter picks from above only, so with multi-level racks the forklift feeds a buffer table by the F45; jib or aluminium rail crane; headroom check; first market look (Schmalz JumboErgo; used PSE140 €12,000 + VAT, woodweb.com).
- Owner: *"That's planning yet. No drafts needed at this stage"*; *"Let's work with 3.6m height"* — recorded as the planning height (§6b).
- Owner: lifter only rack → F45; afterwards parts move by trolley or pallet. Recorded in §6b with the two ways to bridge rack → saw.
- Owner: *"Server room is moved to tool storage"* — the server rack goes into the 3,340 × 2,478 tool-storage room; recorded in §6a. Open: where the tools go.
- Owner: *"No tools in that room. And rack is moved last week"* — the server rack is already in the room drawn as "Tool storage"; nothing to re-home. §2a and §6a corrected.
