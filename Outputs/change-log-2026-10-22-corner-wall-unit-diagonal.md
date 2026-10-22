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
