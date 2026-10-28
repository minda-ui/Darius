# Workshop layout plan — Units 30 and 31

Darius, started 28/10/2026, for Minda. **A working document**: it is filled in as the survey comes back and changes
each round. Change log: `Outputs/change-log-2026-10-28-workshop-plan.md`.

**Owner, 28/10:** *"Now we are removing a lot of things around both units. It would be accessible. So we gonna need to
plan where machines will go, off cut storage area, panel storage and etc. But first let's create existing and when we
will move to next phase planning."*

| Phase | What | Status |
|---|---|---|
| **1. Existing** | Record what stands where today, to scale | **Done 28/10** — owner's drawing confirmed as the layout now (§2a); only the compressor footprint still to measure |
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
so roughly 1:74 as printed. *The PDF's creation date is 14/10/2024; owner, 28/10: "that's the layout now" — nothing has moved since.* Covers the Unit 31 hall, the 6,000 × 5,720 room above it, the bay down past the server room, WC and tool
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
| Server room (drawn as "Tool storage") | 3,340 × 2,478 | beside the WC — the server rack moved in the week before 28/10; no tools there |
| **Wall removed** | — | the wall between the workshop bay and the Unit 30 bay (from the meeting-room corner down to the bottom wall) is **already gone** (owner, 28/10) — the two bays are one floor; GF_30 still draws it |
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

## 6a. Phase 2 — decisions so far

| Date | Decision (owner's words) | Consequence for the layout |
|---|---|---|
| 28/10 | *"Server room and panel racks are going for good"* | The server-room walls go, freeing the bay between the F4 and the extractor; **panel racks A and B go**, so all panel storage is new. *Where the network/server rack goes:* **into the room drawn as "Tool storage"** — **already done, the week before 28/10** (owner: *"No tools in that room. And rack is moved last week"*); 3,340 × 2,478, beside the WC. Nothing to re-home. |
| 28/10 | *"Racking in assembly area going too"* | The 2,500 × 1,500 racking at the top of the hall goes; the assembly corner is clear. |
| 28/10 | **Full-panel storage** in the Unit 30 bay, at the bottom wall — *"good area because fork truck can place panels easily because it is straight through double doors"* | Marked as a U on GF_30, roughly **4.2 m wide × 4.5–5.8 m deep** (scaled, ± 10 %). Full sheets 2,800 × 2,070: two packs side by side need 4,140 + gaps — tight in 4.2 m. **To confirm:** sheet count, flat stacks or racking, double-door width, forklift fork length. |
| 28/10 | *"Panel racking is the size of panels and 100mm on each side extra"* | One rack bay = **3,000 × 2,270** (2,800 × 2,070 + 100 each side). Two side by side = 4,540 wide — **more than the ≈ 4.2 m marked**, but the bay wall is gone so the area can widen towards the workshop. Still open: how many bays / levels, door width, fork length. |
| 28/10 | *"Racking we got is full height about 3.6m height. Panels will stored flat. For each colour will be dedicated shelf"* | Existing racking, **≈ 3.6 m high**, sheets **flat**, **one shelf per colour**. Shelf count = number of colours; with ~500–600 mm per level, ≈ 5–6 levels in 3.6 m per bay. Check: the ceiling over the storage area clears 3.6 m plus lifting room (the plans give H = 3,830 / 4,760 in places); the forklift lifts to the top shelf (~3 m). |
| 28/10 | Loaded from the **short side** — *"otherwise you can get through double door which are 2.4m wide"* | Packs come through the **2.4 m double door** with the **2,070 side across** (≈ 165 mm clear each side) and the 2,800 along the forks; each bay's **2,270 face looks at the doors** and the pack slides in **3,000 deep**. Bays stand side by side across the area: 2 bays = 4,540 wide, plus a clear run straight from the doors. |
| 28/10 | *"Max 5 to 6 colour's. Mostly is White colour panels, they are most used"* | **5–6 colours, white the main one.** One bay of 5–6 shelves would hold one shelf per colour, but white would run out first. Suggested (to confirm): **2 bays** (4,540 wide) — **bay 1 white** on several shelves, **bay 2 the other 4–5 colours**; and a **white working stack on the floor by the F45**, refilled by the forklift, which the vacuum lifter can pick from above directly. At ~600 mm per shelf a pack is ≈ 25 sheets of 18/19 mm. |
| 28/10 | *"It would be only one 3000x2270mm bay"* | **One bay, 3,000 × 2,270 × ≈ 3.6 m**, 5–6 shelves = one per colour. Fits the marked area with ≈ 1.9 m to spare across. Open: does white also get a working stack on the floor by the F45 (for the lifter), or two shelves in the bay? |

**Planning assumption (owner, 28/10): *"Let's work with 3.6m height"*** — 3.6 m is the usable height for planning
(racks, cranes, ducts) until measured on site. *Racks of ≈ 3.6 m then fill it; a forklift placing the top pack needs its
own clearance — check on site.*

## 6b. Panel handling — vacuum lifter (owner's idea, 28/10 — *planning only, no drafts or quotes yet*)

Owner: *"Ideally we need to plan some kind arm with vacuum sucker to move panels around."*

- **The load:** a 2,800 × 2,070 sheet ≈ 5.8 m²: 18 mm MFC ≈ 70 kg, 19 mm MDF ≈ 75–80 kg. Capacity is not the hard part;
  sheet size and the pad layout are (a US dealer rates a JumboErgo-85 for 4' × 8' and 5' × 10' only — ours is bigger).
- **The catch with the racks:** a vacuum lifter picks **from above**. It can take the top sheet of a stack, but **not a
  sheet from a shelf with another shelf over it**. With 3.6 m multi-level racks, the forklift brings a colour's pack
  out first.
- **Workable arrangement (draft):** forklift: rack → **buffer table** beside the F45 → vacuum lifter: buffer → F45
  sliding table (and later to the Vitap). Lifter on a **pillar jib crane** (reach ≈ 4–6 m) or an **aluminium rail crane**
  over the saw area.
- **Scope (owner, 28/10):** *"We need to move panel from rack to F45 only. Afterwards it is moved by trolley or pallet"* —
  the lifter's job ends at the F45; cut parts travel on trolleys or pallets.
- **Two ways to bridge rack → F45:** (1) forklift brings the colour's pack to a buffer table by the F45, the lifter feeds
  the saw (the racks stay as they are); (2) a **forklift-mounted vacuum attachment** picks single sheets straight off a
  shelf — only if each shelf leaves enough gap above its stack for the pad frame (roughly 200–300 mm; to check with a
  supplier).
- **Forklift (owner, 28/10):** *"Fork truck is diesel powered, so it is used only for bringing panels to rack"* — it
  does **not** shuttle packs from the rack to the saw, so option (1) above and the forklift-mounted attachment are out.
  That leaves the lifter needing a sheet it can reach **from above**:
  - **(a) Floor stacks under the lifter** — the working colours (white at least) stored flat on the floor within the
    crane's reach; the rack holds reserve stock. Uses floor, not height; refilling a floor stack from the rack still
    needs something to move a pack (the forklift at delivery, or an electric stacker).
  - **(b) Roll-out drawer racking** — each shelf pulls out into the open and the lifter picks from it. Lets the lifter
    serve every colour from the rack; heavy-duty and costly (a shelf of ~25 sheets is ≈ 1.8–2 t).
  - **(c) Electric pallet stacker** (battery, no fumes) for indoor moves rack → buffer by the F45.
  Diesel exhaust indoors is also a health-and-safety point for Anna (keep use short, doors open).
- **Checks:** ceiling / roof structure height over the saw (H = 3,830 in places) less crane and lift tube; floor for a
  jib's foundation; 400 V / 230 V supply for the vacuum blower; noise.
- **Market (first look):** Schmalz JumboErgo / JumboSprint (to 300 kg); a used JumboErgo PSE140 in Northern Ireland
  listed at €12,000 + VAT, said to lift 2 × 18 mm MFC (woodweb.com). New: quote needed — a Schmalz UK distributor,
  giving sheet size, weight and headroom. *No order without the owner (§6a).*

## 6. Phase 2 — what the new layout will be checked against (draft)

- One-way board flow: delivery → panel storage → F45 → F4 → Vitap → assembly → staging → loading door.
- Each machine's working space (§3), with no overlap with walkways.
- Walkways and the forklift / panel-trolley route kept clear; fire escape routes and exits kept clear.
- Short duct runs from the extractor; air and 3-phase power to each machine.
- Offcut storage next to the saw; edging next to the F4.
- Health and safety (Anna): extractor siting, fire plan, noise.
