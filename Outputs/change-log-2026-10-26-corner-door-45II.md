# Change log — 2026-10-26 — corner unit door for +45° II hinges; FL-005 closed

Darius, session 40.

## 1. Session start
- Hub: 5 Darius rows open (AWT-0089, 0127, 0194, 0225, 0942). AWT-0899 (Goathland costing ask to Minda) at its
  default date today; work runs are reporting on AWT-0194 daily. Raw: Victoria's note *Project A is a go* — nothing for
  the workshop. Faults: FL-003 In Progress (LRE16 fit results not reported), FL-005 Monitoring.
- Owner has copied v5 to the Furniture folder (`1y1BebnAuumibVoKej5TdDc45EeQ4rn5K`, seen 26/10).

## 2. Hinges: +45° II instead of +45° I
- Owner: *"I need to handover corner unit to customer. But I haven't received hinges. I managed to get +45 II hinges"*,
  then *"Is it possible to use them, I understand that I need to produce new door"*.
- Blum catalogue 2022/23 (`Raw/Blum_publication.pdf`): p.118 +45° I 79B9658, *set back fronts*, **FB = LW**; p.120
  +45° II 79B3558, *flush fronts*, **FB = LW − 5.4**, 110°. Both list case Nº 53 (45°) → p.119, **0 mm plate 173H7100**;
  p.121 (II) also gives 173H7100 at 45° (Nº 9). Same cup and plate positions, so no re-drilling.
- **Correction on record:** on 24/10 Darius told the owner +45° II "needs bevelled sides". The p.120 drawing shows a
  square-edged side; the real difference is set-back vs flush front and the door width.
- **v6 built** in `Raw/Review folder/600x600 Corner Wall Unit v6 (Darius - v5 + door 365.1 for +45 II hinges)`
  (`13JZzrhl5aW24O9YhKH_qfZvSEiSyvaoj`): v5 with `09-DOOR-1.TCN` DH/HF and worklist HEIGHT **370.5 → 365.1**; the other
  11 files md5-identical to v5; door (`1_zi_unMXEd3egmzHHOC9E4cpmCCk0u6k`), worklist and .fnm byte-checked SAME.
  Hinge cups (Y 22.5 from the hinge edge) and pilots unchanged. The owner's Furniture copy of v5 was not touched.

## 3. FL-005 closed
- Owner: *"FL-005. Close it"* → Fault Log Status **Resolved**, Date Resolved 2026-10-26; the setting changed on 14/10
  is still not named.

## 4. FL-003 — LRE16 fitted, extractor to Monitoring
- Owner: *"FL-003. It was fitted. Suction works perfectly, no dust in workshop!"* → Fault Log **In Progress →
  Monitoring**; Resolved after a clear week (to 2 Nov) with no trips. Phase currents not yet measured; old motor repair
  as a spare still open.

## 5. Door stands proud on the hinge side — root cause found, and it is Darius's
- Owner (photos, door closed): non-hinge side looks right, hinge side stands forward with a gap; *"The holes doesn't
  match for plate. I think we didn't take into account that top and bottom panels is sticking and door goes in front of
  it"*; then a photo of the bottom corner on the hinge side.
- **Measured in the programs:** side plate pilots (Ø2, pairs 32 apart at X 67/99 and 763/795) are at **Y 56 from the
  side's front edge** (Y 0 = front: the back-joint holes are at 295.9 = 319 − 23.1). Blum p.118/p.120 planning: **37**.
  56 − 37 = **19**.
- **Geometry (bottom program coords):** sides' inner front corners at (319, 19) and (581, 281); the line through them is
  370.5 long — the door width Darius set on 23/10. SmartCabinet's own door was **420**: (562 − c)·√2 = 420 → its door line
  sits **≈ 24.7 mm (perpendicular) further back** than the inner-corner line, fully behind the sides' front edges — a
  set-back door, consistent with plates at 56. That needs the top and bottom diagonal cut back to the door line.
- **What was built:** top and bottom cut on the inner-corner line (owner's photo: the bottom's diagonal meets the side
  at its inner front corner) — from Darius's spec, not from SmartCabinet (the bottom program has no contour). So the door
  cannot set back; it sits in front of top and bottom, 19+ mm forward of where the plate holes expect it.
- **Darius's error, on record:** the 23/10 door edit (420 → 370.5) and the spec's top/bottom line put the door on the
  inner-corner line without checking SmartCabinet's plate depth (56) against Blum (37). The drawing check never compared
  plate depth with Blum. The skill and spec need a plate-depth check and a stated door line.

## 6. "I think we need bigger door" — not with square sides
- Owner photos (from below): non-hinge side closes to the side's inner corner; hinge side shows an open gap between
  the side's front edge and the door. Owner: *"I think we need bigger door"*.
- Blum p.121 (+45° II planning): both 45° cases — **Nº 9 overlay (0 mm plate, 32.5 / 74 / 45.5 / 2.5 / 14)** and **Nº 24
  inset (18 mm plate)** — draw the **side's front edge bevelled at 45°**. The 24/10 statement "+45° II needs bevelled
  sides" was right; the 26/10 retraction (§2) was wrong. On square sides the side's outer front corner sits
  19/√2 = 13.4 mm in front of the inner-corner line, so a door widened past the inner corner meets it on closing; the
  usable widening is only the 2–3 mm the +45° II brings the door forward.
- Advice given: the carcase's hinge is **+45° I 79B9658** (p.118 draws a square side) on plates at 37, door 370.5. For the
  handover today, the +45° II stays a compromise.
