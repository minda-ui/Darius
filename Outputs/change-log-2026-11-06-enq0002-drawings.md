# Change log — 2026-11-06 — ENQ-0002 drawer chest drawings, rounds 2–3

Darius, session 45. (Composio CLI still signed in from 05/11; machine replaced overnight per OS version, scratchpad kept.)

## 1. Round 2 (05:16) — carcase came out 19 mm
- Owner: *"I have uploaded new drawings to review folder"* — `Raw/Review folder/untitled` (`1tzG55TkGI4iPgHgNxaEf5_Vfgc1Yt2Q-`)
  replaced in place, 12 files, md5 = Drive. Sides/top/bottom **19 mm** (bottom 462), back 18 mm, drawer bottoms 387.
  ✗ reported: the job is priced and bought in 18 mm (no 19 mm W1100 ST9 price held); the material entry's 19 mm reached
  the parts instead of being set to 18. Innobox geometry still right at 19 (387 = 462 − 75; bottom line 75 = 19 + 56).

## 2. Round 3 (05:20) — back to 18 mm; a nesting file appeared
- Owner: same words. 13 files, md5 = Drive. Carcase **18 mm**; bottom/top/back/drawer-bottom programs **byte-identical
  to round 1**; runner holes 37/261, line 56 ✓.
- ✗ **`21-NESTING01-SP18-W1100.TCN`** (2800 × 2070 × 18): five through-cuts d-18 with **no tool** + the side holes —
  *don't run*; the shop cuts on the F45 and drills singles (library units dropped nesting sheets in 09/2026); nesting
  export setting to switch off. `22-NESTING02-SP16-U961` listed in the `.fnm`, not uploaded.
- ? **Back 6 mm further back**: side/bottom bores for the back at y 482.9 (round 1: 476.9) — back ≈ 8 from the rear edge
  instead of 14; asked if intended (Innobox depth still 474 ≥ 460).
- ? Fronts still have no single programs (they appear only as cut-outs in the nesting at 167.3 pitch) — need the knob
  hole and, after a bracket is measured, the Innobox F values.
- Owner: *"I need job code to rename folder"* — answered: none issued yet; ENQ-0002 becomes **AM2603** when the order is
  won and released (Nadia's note 04/11: issued by a human at step 3/4). Use `ENQ-0002 Drawer chest` now, rename on order
  — or the owner issues AM2603 now, her call.
- Not cleared.

## 3. ENQ-0002 won → AM2603
- Owner: *"Order is won and that's why we need two units of each"*. Job number **AM2603** given (next after AM2602; not on
  the Hub anywhere); folder to be `AM2603 Drawer chest`. Nadia told: note
  `2026-11-06-Darius-to-Nadia-ENQ-0002-won-AM2603.md` (`1inQNT5AEOozHXsU9Po_lDs81UbO0jXQL`, own copy
  `19zfEJzR63f7mfgFMZ7NY-pLvv7ab4U10`, md5 = local) + Hub **AWT-1125** (High). Order release (signed order / deposit) left
  to her and Minda.

## 4. Owner's answers on the round-3 open items
Owner: *"1. ok 2. needed 3. hand work 4. understand 5. only Backs top need edging"*
1. **Nesting export** — will be switched off. ✓
2. **Back 6 mm further back** — intended (*"needed"*). Closed; round 4 checks the back against the new y 482.9, not round 1.
3. **Drawer-front holes (knob + Innobox bracket)** — **done by hand** on AM2603, not on the Vitap. Owner's stated
   exception to the all-holes-on-the-Vitap rule, like the AM2602 handles. Fronts need no drilling program; the Innobox
   `F` columns can stay 0 for this job.
4. **Drawer-back width 389 vs ≈375** — understood; settled by measuring the first set before the drawer backs are cut.
5. **Edging on drawer parts** — **drawer backs: top edge only**; drawer bottoms not edged. 6 backs × 389 ≈ **2.3 m** of
   U961 edging. *Not in the v0.5 price (U961 edging not costed) — small (≈ £1.50 at the W1100 roll rate, proxy); left
   for the final cost reconciliation, not re-sent to Nadia.*

## 5. Round 4 — all four AM2603 units
- Owner: *"I have uploaded new drawings to review folder"* — `Raw/Review folder/AM2603_` (`15BS201tgum8wgYRFEm30jJSgm7Ut3r9G`),
  four sub-folders `005`/`006` Cupboard with Drawers 3/4, `007`/`008` Cupboard with Door (2); 44 files, md5 = Drive.
- **Drawer chests 005 = 006, byte-identical, and every program byte-identical to round 3**; nesting file gone and not in
  the `.fnm`. ✓ Ready (front holes by hand, §4).
- **Cupboards 007 = 008, byte-identical.** Top, bottom (both faces) and back byte-identical to the chests; left side = the
  chest's less the Innobox holes. ✓
  - Hinges RHH ✓: right side plate holes Ø3 at y 37, pairs 86/118 and 382/414 (centres 102 / 398). Door 496 high × 497
    wide; cups Ø35 d13 at 100 / 396, 22.5 from the edge; screw holes Ø3 45 apart, 9.5 behind the cup. Door centred
    (2 mm short of 500) → cups land on 102 / 398 exactly ✓.
  - ? **No shelf** — no shelf part and no pin holes. v0.4/v0.5 price an adjustable shelf + 4 pins per cupboard.
  - ? **No knob hole on the door** — assumed by hand, as the drawer fronts (§4).
- Not cleared yet: shelf answer.

## 6. Owner: "No knob" on the cupboard door; round 5 (shelves)
- Owner: *"No knob"* — the cupboard doors have **no knob**. Knobs 8 → **6** (drawer fronts only): −2 × £6.75 = −£13.50 at
  cost (−£15.53 ex VAT with the 15 %). Left for the final cost reconciliation; Nadia not re-priced (order already won).
  ? How the door opens without a knob (edge grip, or push-to-open, which would change the hinges) — asked.
- Owner: *"check new drawings with shelfs"* — new folder `Raw/Review folder/AM2603` (`14eGoO5w3odg1jwOBAylkpZDKffPz6dgJ`):
  `001`/`004` Cupboard with Door, `002`/`003` Cupboard with Drawers; 43 downloaded md5 = Drive, the 44th
  (`002/01-SIDE-LEFT`, proxy 403 on download) has Drive md5 = round 3's side.
- **Chests 002, 003: every program byte-identical to round 3** ✓.
- **Cupboards 001 = 004.** New `05-SHELF-1` **463 × 462 × 18**, joined by **4 Cabineo** (pockets at y 74 / 388 each end)
  — a **fixed** shelf. Sides, top, bottom, back and door **byte-identical to round 4**.
  - ✗ **The sides have no holes for the shelf** — no Cabineo Ø5 bores at shelf height (and no pin rows). As exported the
    shelf's Cabineo have nothing to lock into. Fix in SmartCabinet, then re-export the cupboards: either a **fixed** shelf
    with its joint to the sides generated (sides get Ø5 bores), or an **adjustable** shelf on pins as priced (sides get
    pin rows; shelf ≈ 462 wide with no Cabineo).
- Not cleared: cupboards (shelf joint; door opening). Chests still ready (front holes by hand).

## 7. Round 6 (06:01) — shelf holes in; folder holds two exports
- Owner: *"I have uploaded new drawings to review folder"* — same `AM2603` folder; listed with md5. It now holds **seven**
  sub-folders: the 06:01 export `001`/`002` Cupboard with Door (2), `003`/`004` Cupboard with Drawers (2), **and** three
  left from 05:51: `002_@_am2603_cupboard_with_drawers`, `003_@_AM2603_Cupboard_with_Drawers_2`,
  `004_@_AM2603_Cupboard_with_Door_2` (numbers clash with the new ones). ✗ The 05:51 `004 … Door_2` has the **old sides
  with no shelf holes**; the two old chest folders would double the chest count. Owner to delete the three 05:51
  folders before release (Darius does not touch the Review folder).
- **Chests (06:01 `003`, `004`): Drive md5 of every file = round 3** ✓.
- **Cupboards (06:01 `001` = `002` by md5; `002` downloaded, 11 files md5 = Drive):** only the two sides changed. Each side
  gets two `W1001` hole rows, Ø5 d12, pitch 32, three holes (219.9–283.9 on the left, mirrored 216.1–280.1 on the right),
  at **84 and 398 from the front**. *My reading:* 398 − 84 = 314 = the shelf's Cabineo spacing 388 − 74 → the shelf sits
  **10 back** from the carcase front and its 4 Cabineo lock into the rows — an **adjustable Cabineo shelf with 3
  positions, 32 apart**. Shelf rear 472 vs the back's front face ≈ 473.9 → ≈ 2 mm clear ✓. Shelf, door, top, bottom,
  back unchanged ✓.
- **Cleared for release** once the three 05:51 folders are deleted; release to Furniture on the owner's word. Still open,
  not blocking the Vitap: drawer-back width on the first Innobox set; how the knob-less door opens.

## 8. Released to Furniture
- Owner: *"Deleted, release to Furniture"*. At release the three 05:51 folders **still listed as not trashed** in Drive
  (sync lag, or deleted elsewhere) — so only the four checked 06:01 folders were released, picked by timestamp and md5.
- New folder **`Furniture/AM2603 Drawer chests and cupboards`** (`1QGYilcfTkqKI6EuvedcjeEcwXkleHccs`): `001`
  (`1P1UI-nER_1D6KkHr2tkUNt36bSzH62kV`) and `002` (`1nds2QB-IIcK7lSFcbEomFRSA6_ER_4Y7`) Cupboard with Door, `003`
  (`17ys3FWUCrPkXMcE-twH4PYj97Cv6MYG_`) and `004` (`114LUlLssO7Iq6-ll7-2xJZg1cdg-2XZA`) Cupboard with Drawers. Server-side
  copies; **46 / 46 md5 = source**, and every program = the checked round (chests round 3, cupboards round 6).
- Loading: WSC ListsManager → open each unit's `worklist.xmlst` (cupboard 9 programs, chest 10); Mirror unticked.
  By hand, not on the Vitap: drawer-front holes. Not programmed: drawer fronts, drawer backs (saw; width to measure on
  the first Innobox set before cutting), door with no knob.

## 9. Owner's photos of the printed Innobox leaflet (3 photos, not filed to Drive)
- Same document as `Raw/758810.pdf`, on paper; the A/B-140/164/204 page is sharp enough to settle one misread.
- **Correction:** drawer-front bracket holes are **2 × 32 apart, lowest ≥ 54, 10 deep**; the **Ø10 (12 deep)** is the
  gallery-rail hole of the taller versions only. The Klug article §5 said "Ø10" — fixed. Diameter not printed.
- **Drawer back:** 44.5 from the cabinet side each end, holes 9 from the back's end, 32 apart → **back = 464 − 89 = 375**
  on AM2603. SmartCabinet's 389 is the **base** width; the backs (not programmed, cut on the saw) should be cut **375**
  after a dry fit of one. Base 389 = 464 − 75 ✓.
- Components list: item 5 is a **metal drawer back**, shown as an option; AM2603 uses the wooden U961 back on the rear
  connecting brackets (item 4), as drawn.

## 10. Leaflet panel sizes — the released drawer bottoms are wrong
- Owner's photos, "Bottom and back panels measurement" (printed): **bottom LW − 75 × (NL − 5)**, **back (LW − 89) × 70**
  for A/B-86, 16 mm. AM2603 → **bottoms 389 × 445, backs 375 × 70**, 6 of each, U961.
- ✗ **Released bottoms `09`/`14`/`19-DRAWER-n-BOTTOM.TCN` are 389 × 408** — 37 short.
- ✗ **And each carries two tool-182 cuts, 8 deep**, at x 38 and x 351, from y 368 running off the 408 panel (≈ 40 mm on the
  part) — the "stray tool-182 cuts in single drawer-bottom programs" already on the checklist. **Missed in rounds 3–6**:
  I checked the size and passed them. Lesson: decode every program in full, every round, including parts that "need
  no holes".
- Recommendation: **do not run the drawer-bottom programs**; the bottoms need no machining — **cut 389 × 445 on the F45**.
  Backs **375 × 70** on the saw (top edge edged) after a dry fit. Remove the three bottom programs from the two chest
  worklists in Furniture — **on the owner's word only**. For future jobs: Drawer Box row H 71 → 70; `.SCS` back on the
  base (`bCassDIESOT=1`, my reading) and base length NL − 5, proved on one re-export.
