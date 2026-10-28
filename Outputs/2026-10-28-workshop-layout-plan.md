# Workshop layout plan — Units 30 and 31

Darius, started 28/10/2026, for Minda. **A working document**: it is filled in as the survey comes back and changes
each round. Change log: `Outputs/change-log-2026-10-28-workshop-plan.md`.

**Owner, 28/10:** *"Now we are removing a lot of things around both units. It would be accessible. So we gonna need to
plan where machines will go, off cut storage area, panel storage and etc. But first let's create existing and when we
will move to next phase planning."*

| Phase | What | Status |
|---|---|---|
| **1. Existing** | Record what stands where today, to scale | **In progress** — owner's dimensioned drawing received 28/10 (§2a); open: is the 2024 drawing still current? compressor footprint |
| **2. New layout** | Plan machines, panel and offcut storage, assembly, services | Starts when phase 1 is complete |

---

## 1. The base drawing

- **Plan:** `GF_30` — *Ground floor plan*, Fishbone Drylining, 22/05/2024, Units 30 and 31 (title block says "Unit 30").
  Drive: `Raw/Unit 30 - Ground floor plan (GF_30, 22-05-2024).pdf` (`15rmCPSKiABU_6N6d0b1cmKV0mRe3wa9Y`).
  Used for the outline and zones. *(The owner said "ignore GF30" earlier, then marked everything on it — it is the only
  plan that shows the whole workshop.)*
- **Room sizes:** `Unit_30` (`1zmBHrsB-6d3Gflymqh2qUWR4BRYySDZK`) — dimensioned, but does not show the workshop bays.
- **Scale — calibrate, don't trust "1:100".** The sheet says 1:100 on A3 (true 1:100 = **35.3 mm per PDF point**).
  Measured on the PDF's own vectors, its two dimension lines give **36.95 mm/pt** (10,136 over 274.3 pt) and
  **38.0 mm/pt** (4,237 over 111.4 pt) — the drawing is 5–8 % off true 1:100, and the two don't agree with each other.
  Every distance taken off it is an **estimate (± 5 %)** until the survey confirms two dimensions inside the workshop.
- **Units:** Unit 31 = the large hall (left) and the room above it; Unit 30 = offices, meeting room, server, canteen,
  WCs and the lower bays. **The workshop spans both units.**

## 2. Zones (owner, 28/10)

| Zone | Where | Size |
|---|---|---|
| Workshop | Unit 31 hall + the lower bay running down past the meeting room | not dimensioned on the plan |
| Assembly | top-left of the Unit 31 hall | — |
| Storage | Unit 30 bay along the canteen side | ≈ 10,136 × 4,237 (plan) |

Sketch with everything marked so far: `Outputs/2026-10-28-workshop-layout-current-and-proposed.png`
(`1aGW1CnwkIABMNQPVH0Crbxyk8sZ_lqLX`) — positions traced from the owner's marks, **not measured**.

## 2a. Existing layout — the owner's dimensioned drawing (28/10)

`Raw/last planning  furn.prod.shop.pdf` (`1_Itj0qPDKAI4qtGrrphf5btT2NCPMMGc`, 94,866 B) — AutoCAD, A3, **no scale
stated**; its own dimension lines measure ≈ **26 mm per PDF point** (4,500 / 4,374 / 4,200 / 3,200 all within 26.1–26.6),
so roughly 1:74 as printed. *The PDF's creation date is 14/10/2024; the owner calls it the newest, with machinery where it
stands now.* Covers the Unit 31 hall, the 6,000 × 5,720 room above it, the bay down past the server room, WC and tool
storage. **This replaces the traced positions in the 28/10 sketch.** Labelled copy: `Outputs/2026-10-28-workshop-existing-layout.png`.

| Item | Size on the drawing (mm) | Position / clearances on the drawing |
|---|---|---|
| **F45** (working zone) | **6,500 × 4,500** | against the bottom outside wall; **1,000** to the Vitap, **900** to the F4, **1,024** to the extractor |
| **F4** | **4,200 long**, 950 at the out-feed end (L-shape) | in the middle of the hall; **3,314** to the stair-block corner, **4,374** to the server-room wall |
| **Vitap** | **2,900 × 1,710** (manual: 2,940 × 1,710) | **800** to the mitre saw bench, **1,000** to the F45 zone, **2,786** to the bottom wall |
| **Extractor ("Hood")** | **3,200 × 1,200** (manual: 3,170 × 1,200) | in the bay by the server room; **700** to the server-room wall and **700** to the outside wall |
| Racking | 2,500 × 1,500 | top of the hall, against the 6,000 room's wall |
| Mitre saw bench | 1,200 deep, along the left wall | dashed |
| **Panel rack A** | **2,500 × 2,200**, red zone = loading space | below the WC wall (owner, 28/10) |
| **Panel rack B** | **2,500 × 1,200**, **500** each side, red zone = loading space | the bottom corner of the bay — the proposed extractor/compressor corner (owner, 28/10) |
| Room above the hall | 6,000 × 5,720 | double doors to the hall |
| Tool storage | 3,340 × 2,478 | beside the WC |
| **Compressor** | **footprint not measured** | in the **6,000 × 5,720 room** above the hall, its bottom-right corner by the stair block (owner's mark, 28/10) — a separate room from the dust |

**Early findings for phase 2** (from the drawing, not measured on site):
- **Vitap to the mitre saw bench is 800 mm**; the Vitap manual asks for **≥ 1,000 mm all round**.
- The extractor sits 1,024 mm from the F45's zone, so the duct runs are short today; the proposed corner is where
  **panel rack B** stands now — moving the extractor and compressor there means re-homing that rack.

## 3. Inventory — what has to go on the drawing

**Footprint** = the machine itself. **Working space** = what it needs around it to be used and serviced; for the saw and
the edgebander that is set by the **panel length**, not the machine. *Position* is to be measured in the survey (§4).

### Machines and plant

| Item | Code | Footprint L × W × H (mm) | Working space / clearance | Services | Source |
|---|---|---|---|---|---|
| Altendorf F45 sliding table saw | `FA2303` | **? — measure** (depends on the sliding-table length fitted) | in-feed and out-feed of a full sheet both ways (≈ 2 × 2,800 along the carriage) + rip width | 3-phase, extraction (top + bottom), air | Wiki F45 article; ~1,100 kg |
| Hebrock F4 edgebander | `FA2301` | **? — measure** (manual's dimension table is ambiguous) | **≥ 500 mm** all round per manual; in-feed and out-feed ≥ longest panel | 3-phase, extraction, air | Wiki F4 article |
| Vitap K2-2.0 drilling centre | `FA2304` | **2,940 × 1,710 × 1,900** | **≥ 1,000 mm all round** (manual) + panel loading side | 3-phase, extraction, air, network (TpaCAD PC) | Wiki Vitap article; 1,030 kg |
| AES SAF 10,000 STK extractor | `FA2402` | **1,200 × 3,170 × 2,330** | bin emptying + filter access | 3-phase 11 kW; main duct to all three machines | Wiki extractor article; 720 kg |
| ABAC Genesis screw compressor | `FA2306` | **? — measure** (incl. tank and dryer) | ≈ 1 m service + cooling air in / heat out | 3-phase 15 kW; air main; condensate drain | Wiki compressor article; 455 kg |

### Everything else (owner to add or strike out)

| Item | Count / size | Notes |
|---|---|---|
| Panel (full-sheet) storage | how many sheets, which sizes, racked or flat | 2,800 × 2,070 sheets; forklift / panel trolley access |
| Offcut storage | rack type | near the F45 out-feed |
| Edging rolls / consumables | shelving | near the F4 |
| Assembly benches / tables | how many, size | assembly zone |
| Tool and hardware cabinets | the OSB cabinets ("Lamello Cabineo", "Measurement", "Knife", "Runner"…) | |
| Finished-goods / staging area | for units waiting to go | near the loading door |
| Waste / skip / recycling | where offcuts and dust bags go | owner: transported to the local recycling centre |
| Label printer, scanner station | Brother `FA2401` | |
| Doors | roller shutter(s), fire exits, internal doors — width and swing | for the escape routes and the forklift route |
| Fire extinguishers ×3, first aid | positions | needed for the fire plan |
| Electrical | distribution board, 3-phase sockets / isolators | |
| Air drops, duct runs | routes and heights | |
| Network | server rack, Wi-Fi 7 access point | |

## 4. Survey — how to measure positions

For each item: **two distances to two fixed walls** (e.g. "Vitap front-left corner: 1,200 from the left wall, 3,400 from
the back wall"), its footprint, and one photo. A rough sketch with numbers is enough.

- **Start with two long dimensions inside the workshop** (e.g. the hall's width and length) — they calibrate the
  drawing.
- Photos for the extractor/compressor move: `Outputs/2026-10-28-photo-checklist-extractor-compressor-move.md`.

## 5. Already known — the extractor and compressor question

The owner proposes moving both to the bottom corner of the workshop bay (Unit 30 side, outside wall). Straight-line
distances to the extractor, scaled off the plan: F45 ≈ 3.7 → 8 m; F4 ≈ 5.5 → 11.5 m; Vitap ≈ 12 → 16 m — every duct
run gets 4–6 m longer. Carried into phase 2; detail in the change log of 28/10.

## 6. Phase 2 — what the new layout will be checked against (draft)

- One-way board flow: delivery → panel storage → F45 → F4 → Vitap → assembly → staging → loading door.
- Each machine's working space (§3), with no overlap with walkways.
- Walkways and the forklift / panel-trolley route kept clear; fire escape routes and exits kept clear.
- Short duct runs from the extractor; air and 3-phase power to each machine.
- Offcut storage next to the saw; edging next to the F4.
- Health and safety (Anna): extractor siting, fire plan, noise.
