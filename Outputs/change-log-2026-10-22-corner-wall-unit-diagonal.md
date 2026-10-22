# Change log — 2026-10-22 — Corner wall unit 600 × 600 diagonal: spec, hinge, first drawing check

Session 37.

## (1) Session start
- **Hub:** `AWT-0089`, `AWT-0194` Blocked; `AWT-0127` In Progress; `AWT-0225` Blocked; `AWT-0871` Done by a work run
  (Amfa order hand-off v0.2 to Victoria). `AWT-0899` (Minda's ASK, Goathland costs) due 26/10. **Raw/:** Nadia's reply
  (already handled by the 18/10 run). **Fault Log:** `FL-003` In Progress (LRE16 fit not reported), `FL-005` Monitoring
  (week ended 21/10). **Git:** `main` had the owner's settings update (PR Darius#2, `AWT-0896`) — merged in, pushed.
- **Flagged to the owner, not acted on:** the merged settings no longer deny the native `mcp__Gmail__` send / reply /
  forward / trash tools, which `AWT-0896` says stay denied. Composio send remains denied; policy unchanged.

## (2) Corner wall unit 600 × 600 — spec `Outputs/2026-10-22-corner-wall-unit-600x600-diagonal-spec.md` v0.1 → v0.4
- Owner: **diagonal, one angled door, 900 high, LH and RH; two shelves; square-edged sides** (the Hebrock edges
  rectangular panels with square edges only — manual: not rated for non-rectangular work, no tilting unit).
- SmartCabinet: shape **"Angolare"** with the front joining the sides in a straight line (manual page
  `progettazione_misure-forma`, fetched today). A blank start raised two "Non Definito" accessories — advised starting
  from the master instead.
- Hinge from the Blum catalogue (pp. 118–121): **+45° I, set-back front, planning Nº 53 (square-edged side)** —
  **79B9658** screw-on BLUMOTION (INSERTA 79B9698), plate **173H7100**; door width = LW. +45° II (flush, bevelled sides)
  withdrawn with the bevel. Neither part is in SmartCabinet's `35 CERNIERE` list yet.

## (3) Drawing check, round 1 — `Raw/Review folder/600x600 Corner Wall Unit v2/` (13 files, all md5 OK)
- **✓** 11 programs = worklist = `.fnm`; all 19 mm; backs 862 × 565 / 546 (= spec); door cups Ø35 × 13 at 100 / 796,
  TB 5; plate pilots on the left side at 102 / 798 = cups + 2 (door 2 mm inside the 900 side); shelf/back joint heights
  agree between sides and backs (offset 19); shelf↔back pocket spacing 181.9 = back holes.
- **✗** shelf-to-side joints: side receiving rows at depth 74 / 210 (spacing 136); shelf side-edge pockets spacing 117,
  and the two side edges differ by 9.4 — they cannot all meet.
- **?** sides 900 full height with top/bottom 581 between them (library: sides between top and bottom); sides 319 deep,
  not 300; door 420 wide against ~370 between the sides' front corners (set-back door should = LW); door drilled
  Ø8 × 2 at 45 mm / 9.5 behind the cup (INSERTA or press-in, not screw-on 79B9658); back joints 23.1 from the side's rear
  (13.6 step-back vs the library's 16 — unconfirmed); shelves fixed by connectors on all four edges, not loose; hinges on
  the left only (LH) — RH to follow; two hinges; no cutting-list PDF.

## (4) Drawing check, round 2 — same folder, files replaced in place ("v3")
- md5 vs round 1: **changed** sides, top, bottom, both shelves, door, worklist; **unchanged** backs and `.fnm`.
- **✓ fixed:** sides now **862**, top and bottom **600 × 600** — sides between top and bottom, as the library. Door holes
  now **Ø3 pilots** at 45 mm / 9.5 behind the cup — the **screw-on** pattern for 79B9658. Side↔top/bottom joints at 110 mm
  spacing on both parts (positions offset 19 — consistent with the 319-deep sides standing 19 proud of the top/bottom front).
- **✗ still:** shelf-to-side joints — side rows now at 84 / 210 (spacing 126), shelf side-edge pockets spacing **107**
  (both moved 10 mm; the gap stays 19). Suggested fix: **loose shelves on 5 mm pins**, as the library units.
- **✗ door 420** — with sides 19 proud and the top/bottom diagonal between the sides' inner front corners, the opening is
  **≈ 370.5**; a +45° I set-back door must be **= LW**. 420 cannot fit between the sides.
- **? open:** sides 319 / 19 proud intended (set-back look); back 13.6 from the wall vs library 16; no cutting-list PDF;
  RH version.

## (5) Owner: shelves are loose — Cabineo shelf pins
- Round 1's "shelves fixed on all four edges" was **wrong**: Cabineo shelf pins, shelves loose. The depth alignment still
  matters (pin must meet the pocket): sides 126 vs shelf 107 — open.

## (6) "Check for updates" (evening)
- `01-SIDE-LEFT.TCN` re-saved 15:23 by **TpaCAD** (EDICAD 02.00, tcn 2.9.29, UTF-16). Its four `foro mul` shelf-pin rows
  now carry **no start X, depth or Y** (`#8510/#8513/#8518` absent; pairs identical). Either the decoder does not read the
  newer format or the positions were lost — **not to run until the owner checks the rows in TpaCAD**.
- Raw/: Eugene `AWT-0942` (sync git CLAUDE.md) — verified the working branch carries v37, `cmp` SAME with Drive; `main` is
  v31 pending the merge (`AWT-0225`). **Correction recorded on the row:** v37 grants ops@ read + create_draft only, not
  labelling (Eugene's note and the 13:00 run both said "+ label").
- Raw/: Victoria `AWT-0958` — framework v0.1 read (3 pp.); feedback written (`Outputs/2026-10-22_Darius-feedback-OS-framework-v0.1-AWT-0958.md`,
  `103ovUF-FjwZTIKA9GEHHGIxMS4ewgDtA`, SAME) and posted on the row, **Done**. Offered for Monday: an id/connection
  inventory and a master-only classification of the workshop KB.

## (7) `AWT-0967` — ids and connections inventory (Project A), Done
- Read live: Drive folder tree under the KB root, Composio connection list (own aliases only used), KB registers.
  `Outputs/2026-10-22_Darius-workshop-KB-ids-and-connections-inventory-AWT-0967.md` (`1hPlcVtnATho43q4JrEJPI8EbZl3wsgmu`, SAME);
  summary on the row, **Done** (due 24/10).
- **Findings stated as facts:** Drive connection = Minda's own account (confirmed by `GET_ABOUT`); Composio account shared
  (50 connections across seats); native Drive/Gmail/Calendar/QuickBooks connectors present but unused by the charter; an
  expired `darius-gmail-info` (removal is the owner's call); **the design↔machine share folder is unidentified**.

## (8) Open questions handed to Victoria (project curator)
- **Owner:** *"All questions can answer Victoria, she is curator of project."* Seven questions from `AWT-0958` / `AWT-0967`
  (business space of the workshop; Darius as gate resolver; exchange sheet vs Raw + Hub; supplier reads after ops@
  copying; standing route for Nadia's order hand-off; the design↔machine share folder id; ops@ labelling not in v37 —
  needs Minda's own word) sent as a Raw note to **Victoria's Raw** (`1rzRlNRLdg-qZnXU4MTHCnn3H2b1Z5L6G`, parent
  "Victoria - CEO's Assistant", checked), file `1g3UdeIBMxBC21TrxbZWZaK-HyGgtTwtN`, SAME; own copy `1rVxVAulQAjfRxPVOi3wBgw3QKaXOhrr_`.
  Hub row **`AWT-0971`** (Victoria, Open), id checked free before writing.

## (9) Victoria's reply on `AWT-0971` (Minda decided in chat)
- (3) Exchange sheet sits **beside** Raw notes + Hub rows; Raw stays for hand-offs between assistants.
- (4) Principle 8 (ops@ copying) is for **future businesses only** — the read-only supplier reads in info@ / minda@ continue.
- (5) Nadia → Darius order route **stays as today**.
- (7) **No charter change**: ops@ labelling beyond v37 needs Minda's own word. v37 stands (read + create_draft).
- (1) Workshop business-space ownership **parked** until Business 2; machines stay as invoiced.
- **Still open, Minda's:** (2) is Darius the gate resolver for workshop/machinery requests; (6) the Drive folder
  SmartCabinet uses to pass job files to the Vitap. Row In Progress until both answered.

## (10) Minda answers the last two (`AWT-0971` Q2, Q6)
- **Q2:** *"Yes you are"* — **Darius is the gate resolver for workshop and machinery requests.** Recorded on `AWT-0127`.
- **Q6:** *"'Furniture' on Google Drive"* — folder **`1BsTNcHI2OwjDlJdrCgv-x0BwHjas2qU1`** (My Drive; job folders inside,
  e.g. `600x600 Corner Wall Unit v2` `1uLqyCGVQXHxo0QQX-nrkzNC-sFB80PI9`). Inventory updated; recorded on `AWT-0967`.
  **Charter §1 still reads "not yet identified"** — correct at the next charter bump (owner's word).
- To Victoria: Raw note `2026-10-22_Darius-to-Victoria_AWT-0971-answers-Q2-Q6.md`, id `1clogVKgbn-ddq18Ztxgtl8oAHnVtJjwT`,
  written with the **native Drive connector** (Composio's Google route blocked by an SSRF guard all evening) and checked
  byte-identical with the native download. Her row is hers to close.
- **Drive copies behind git** until Composio recovers: this change log (from section 9) and the inventory file.

## (11) Good night — three skill decisions, all Adopt
- **`new-library-unit-design`** (new); **`pre-production-drawing-check`** extended (in-place replaced folders, TpaCAD-saved
  files, spacing test, shelf-pin pockets); **`end-of-day`** extended (Composio Google route blocked → native connector for
  new files, log the Drive copies behind git, catch up). Register rows added.
- Drive caught up tonight once Composio answered: this log, the inventory, the index, the registers, and an own copy of the
  Victoria Q2/Q6 note — all SAME.
- **Still open:** corner unit — left side's shelf-pin rows (TpaCAD), shelf-pin depths 126 vs 107, door 420 vs ~370, RH
  version; `FL-003` LRE16 results; `FL-005` close; charter §1 "machine-share folder not identified" → "Furniture" at the next
  bump; `AWT-0225` merge to `main`.
