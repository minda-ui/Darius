# Change log — 2026-11-05 — corner unit fitted; session start

Darius, session 44.

## 1. Session start
- Hub: Darius rows unchanged except **new `AWT-1116`** (Eugene, barcode scanners in production — questions in Raw,
  `1R2GxCrTSOeddnT9CbNSAj3dkuZAzmJ45`). Raw: two files 04/11 15:26, `FC2614 - Fishbone price on Macdonald cost plan
  23.10.26 (labour only)` (.pdf, .xlsx) — not obviously workshop; asked the owner. Fault Log: nothing open. `main`
  already merged. Composio CLI still not signed in — 03–04/11 Drive publish still pending.

## 2. Corner wall unit — fitted on site
- Owner sent three photos of the unit fitted beside the cooker hood (dark grey matt fronts, bar handle on the neighbour),
  then: *"This is done today"*.
- Darius's read of the photos, given to the owner as a snag list, **not** a fault: the door stands off the carcase at
  the bottom (depth cam), the gap to the neighbouring door tapers to near-touching at the bottom and the two fronts are
  not in one plane (side screw / depth cam), handprints on the matt fronts. Adjustment is on the Blum hinges (±2 mm
  each way); also check the hood/duct is not touching the door.
- **Open item closed:** the corner unit (+45° hinge, 370.5 door question since 26/10) is **fitted** as of 05/11. Which
  hinge went on was not stated in this session.
- Owner: *"It is hand it over. We need to come back later to drawing board, because this unit is look horrible"* —
  **handed over to the client 05/11**; the owner is not happy with how it looks. **Open: redesign the 600 × 600 corner
  wall unit** before it is made again (library unit). Inputs to bring to that session: the 05/11 photos (door stands
  off the carcase, uneven/near-touching gap to the neighbour, fronts not in one plane next to the hood); the hinge
  history 22–26/10 (plates at 56 → 37, door 420 → 370.5 → 365.1, +45° I vs +45° II, square vs bevelled side —
  `change-log-2026-10-24-…`, `…-10-26-corner-door-45II.md`); `new-library-unit-design` as the method.

## 3. FC2614 in workshop Raw — not workshop work
- The two Raw files (`1m8f2QyW40s_69N2SboQ0BVbNrMfaoyey` PDF 62,003 B, `1OjIzdIYAVdrnSg8Pzg084ZIBVTbsXpK2` xlsx
  41,781 B; md5 = Drive) are a **Fishbone Construction** labour-only tender draft (Anna v0.9, not issued).
- Owner: *"Ignore it; that's our project for labour supply only"* — **not processed, not filed, not copied into this KB**;
  left where it is in `Raw/` (moving or deleting the owner's upload is the owner's call).

## 4. AWT-1116 — barcode scanners in production, facts to Eugene
- Owner: *"yes, go ahead with Eugene"*. Eugene's note (`1R2GxCrTSOeddnT9CbNSAj3dkuZAzmJ45`) asks 7 questions for a
  group scanner choice (InvenTree stock, Snipe-IT assets).
- KB gathered by an Explore agent (barcode article, printer article, CLAUDE-Workshop T022, layout plan, Anna HSE note).
  Reply written facts-and-gaps; **re-read against the sources and four lines cut back** (a "both hands at every
  machine" claim, "expect dusty labels", "the F4 has no input", "Phase 4 needs a keyboard-wedge") to what the KB says or
  labelled *my reading*.
- Delivered to Eugene's `Raw/` (`1qkD2xtFMJtZQVaBJFzHQPz842t8VxjHx`, KB root `1o4MBRcckZBspw-uT6qM2V-74H6OsRK9T`):
  `Darius-to-Eugene-barcode-scanners-production-2026-11-05.md` (`1CLxv6HuAaEUd2tNEKgrjJoYrlojRB1Yz`, 4,147 B = local);
  own copy `Outputs/2026-11-05-Darius-to-Eugene-barcode-scanners-production.md`. Hub `AWT-1116` Response written,
  **In Progress** pending Minda's three answers (hands-full stations, headcount, PC scanner vs handheld).

## 5. Drive publish of 03–05/11 — done
- Owner: *"Drive publishing from 3–4 Nov is still waiting"*. The Composio CLI was signed in by the owner through the
  login link (`composio login --no-browser --no-wait`, then `--poll`; account minda@, org minda_workspace) — no key
  handled by Darius.
- **Before overwriting**, each Drive copy's md5 was matched to a git version (index and registers = `508728d`,
  `Wiki/index.md` = `e506148`, skill register = `2f7f790`, 28/10 log = `2f7f790`) — nothing on Drive was newer than git.
- **In place** (`GOOGLEDRIVE_UPLOAD_UPDATE_FILE`, ids kept): `change-log-index.md`, `kb-registers.md` — **verified by
  the native connector** (download → `cmp` SAME); `Wiki/index.md`, `skill-candidates-register.md` (re-ordered: the
  04/11 rows had been inserted mid-table; now newest first), `change-log-2026-10-28-workshop-plan.md` — md5 SAME.
- **Created** (`GOOGLEDRIVE_UPLOAD_FILE`), all md5 SAME and in the right folder: three change logs (03, 04, 05/11), the
  workflow draft, the ENQ-0002 (v0.2, final), ENQ-0003 and the two test cost sheets, the Eugene note copy (Outputs) and
  `Wiki/Processes/klug-innobox-smartcabinet-input.md` (Processes). Ids in `kb-registers.md` → Drive ids.

## 6. Check on Nadia — ENQ-0002 now four units (AWT-1118 Done)
- Owner: *"check on Nadia"*. New: **AWT-1118** + note `19BxokdQ7SNpILrQjLQ2C0EstURoRZeZK` — *the customer asked for two of
  each unit*. Also seen (Nadia's rows, no action for Darius): AWT-1106 waits on the sales mark-up (AWT-1111, Victoria /
  Andrejus route, Minda's AWT-1112); AWT-1113 — Minda confirmed **AM2602 completed**, tracker *Ready to ship*.
- `Outputs/2026-11-05-ENQ-0002-workshop-price-v0.4-four-units.md` (3,031 B) → Nadia `Raw/` as
  `2026-11-05-from-Darius-ENQ-0002-workshop-price-v0.4-four-units.md` (`1mTkt1I3j9io1QMXVspSZcHA_gcj2MFGs`), own copy on
  Drive `1egGgWl-zgP0arPTRcI7mmJ_zQagd3b6h`; both md5 = local. **£1,427.19 ex VAT / £1,712.63 inc VAT** — 2 sheets,
  6 Innobox, 4 hinges, 8 knobs, 15.7 h (4.5 h machine); design once, so £100.51 under twice v0.3. Lead time 4–5 working
  days. Hub AWT-1118 → Done.

## 7. Klug Innobox into SmartCabinet — hand entry for ENQ-0002
- Owner: *"Next let's move to drawings for ENQ-0002, we need to add innobox to smartcabinet"*, then *"Not in import,
  I'll enter it by hand"*. Darius gave the entry card from `Wiki/Processes/klug-innobox-smartcabinet-input.md`: runner
  row `A86-450 INNOBOX` (LX 5, LY 18, CX 0, LBox 424, holes X 37 / 261 at Y 38, Ø5 × 5) and `INNOBOX_A86.scs` copied
  from `METABOX_K.scs` with `cass05_spess=32.50`; proving export of one ENQ-0002 chest to the Review folder, expected
  base 389 / back 375. Asked: base/back thickness, back height, a set in hand to measure. Article §1 updated.

## 8. ENQ-0002 drawer chest — first Innobox export, drawing check round 1
- Owner set up in SmartCabinet (photos): Register of Accessories `A86-450 INNOBOX` (group 25 DRAWER GUIDES); CAM *Drawer
  guides* row LX 5 / LY 18 / CX 0 / LBox 424 / holes X 37 & 261 at Y 38, Ø5 φ5 — **checked ✓**; `INNOBOX_A86.scs` copied
  from `Metabox.scs` (the file the Metabox rows use — not `METABOX_K` as Darius first said) with `cass05_spess=32.50`,
  rest = the proved Metabox set — **checked ✓**; *Drawer Box* row `INNOBOX 450`, Metallic, Box Config `INNOBOX_A86`.
  **H (back height) would not save — stays 0** (owner: *"Still zero everywhere"*); the Metabox rows show H = Blum's back
  heights (B 127, D 191, H 135, K 103, M 71, N 39).
- Owner: *"I have uploaded drawings to review folder"* — `Raw/Review folder/untitled` (`1tzG55TkGI4iPgHgNxaEf5_Vfgc1Yt2Q-`),
  12 files, all md5 = Drive. Drawer chest 500 × 500 × 500, 18 mm, 3 drawers.
- ✓ **Drawer base 389 × 408 × 16** — 389 = LW 464 − 75 (the `.SCS` works); 408 + 16 back = 424 = LBox.
- ✓ **Runner holes** Ø5 × 5 at **37 and 261** from the front, both sides, mirrored (left 426 / 275.7 / 109.3 = right
  500 − 74 / 224.3 / 390.7). **Bottom drawer line 74 from the bottom edge = 18 panel + 56** — Klug's minimum exactly.
- ✓ Carcase joints and inset back as previous cleared units (spacings 210 / 182 match across mating parts).
- **✗ Drawer backs missing:** `10/15/20-DRAWER-n-BACK` are in the `.fnm` but have no program and no worklist row —
  H = 0 makes a 0-high back. **✗ / ? Fronts missing:** `06/11/16-DRAWER-n-FRONT` likewise listed, not exported (no
  machining — F holes all 0 — so possibly no program; the cutting list must still carry them, and the bracket and knob
  holes are to be drilled on the Vitap).
- Info: runner lines from the bottom are 74 / 224.3 / 390.7 — spacing **150.3 then 166.4**: drawers 2 and 3 follow the
  166 front pitch, the bottom drawer is lifted to keep the 56 clearance, so its box sits ~16 mm higher inside its front
  than the other two. Fits (each box clears the one above); the front-bracket holes will sit higher on that front.
- **Not cleared.** Open: H = 71 to save (or measured), fronts and their holes, the folder name ("untitled").
- Owner (photo of SmartCabinet's Panel Optimization): *"Backs are on cutting plan"* — the backs exist (387 × 71 cut,
  no CN program); bottoms 387 × 408 cut. The plan showed **W1100 ST9 at 19 mm** and the drawer parts on **U961 ST7
  Graphite 16 mm** (9.6 % of a sheet). Darius also flagged the back width (= base, 389 finished, vs Klug drawing ≈ 375 —
  to measure on a set) and whether bottoms/backs should be edged.
- Owner: *"1. I will set it up to 18mm 2. It come from U961 ST7 Graphite"*. → ENQ-0002 **workshop price v0.5**:
  + 1 sheet U961 (18 mm web price £75.99 as proxy, no 16 mm price held) and +0.2 h saw = **£1,536.58 ex VAT /
  £1,843.90 inc VAT** (+£109.39 ex). Note `Outputs/2026-11-05-ENQ-0002-workshop-price-v0.5-graphite-drawer-boxes.md`
  (1,925 B) → Nadia `Raw/` (`1UJTX4Of6M46kpbzJIoGMGDWnmq8WbPBy`), own copy `1RvAxY9RIC2hULSE4_Jr2VtgkGOF6R_YA`, both
  md5 = local; Hub **AWT-1122** (Nadia, Open, duplicate guard clear).
