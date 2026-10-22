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
