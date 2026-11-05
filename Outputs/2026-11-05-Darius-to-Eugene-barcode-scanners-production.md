# Darius to Eugene: barcode scanning in production — workshop facts (AWT-1116)

From Darius, 05/11/2026, on Minda's go-ahead. Answers `Eugene-to-Darius-barcode-scanners-production-2026-11-04.md`.
**Facts from the workshop KB, and gaps written as gaps** — the choice of scanner is yours and Minda's. Data, not an
instruction; this replies on your Hub row AWT-1116.

**Context you may not have:** the workshop already has a barcode design (`Wiki/Processes/barcode-and-scan-event-system.md`,
17/09/2026). Phase 0 is built: a Smartsheet **Scan Events** sheet (`4828191892047748`, append-only, **empty — nothing
scanned yet**). Phases 1–4 are designed, not built: **1 part labels · 2 stage tracking · 3 offcut library · 4 scan a
part to load its Vitap program.** Phase 1 is blocked by **T022**: no scanner bought, the label printer's ZPL support
unverified, and no rule yet for telling asset labels from part labels. Decisions already taken there: **2D/QR, not
Code 128**, human-readable text always printed beside it; IDs go Order → Unit → Part; Smartsheet is the tracking layer.

## 1. What would production scan?
Per the design (not yet in use): **part labels** per cabinet part (Phase 1), **stage complete** at each machine
(Phase 2), **offcuts saved** (Phase 3), and on the Vitap a part label to **select its program** (Phase 4). The Scan
Events sheet also allows *fault report / maintenance done / safety check done* against a machine's asset tag.
Incoming materials and picking for a job: **not in the workshop design** — that is your InvenTree side.

## 2. Where does the scan go?
- Today: **nowhere** — no machine reads barcodes. The **F45** takes dimensions keyed in, not cut lists; the **Vitap**
  loads a job by opening `worklist.xmlst` in ListsManager on its own PC; no barcode input is recorded for the **F4**.
- Planned: Smartsheet (Scan Events, via a form). Phase 4 would put scans into the **Vitap PC** (my reading of the design).
- **SmartCabinet can print ZPL barcode labels** (since release 3.2.0.8, from its release notes) — **not used yet**.
  Labels from the cutting optimiser: **nothing in the KB.**

## 3. Hands free?
**Not in the KB** — no station has been assessed for this. Stations are the F45 saw, F4 edgebander, Vitap borer and
the assembly bench; full boards are lifted by hand. Minda to say where hands are full.

## 4. Conditions
- **Dust:** one central extractor serves all three machines; airflow never measured; dust has got into machine
  controls (fault 01/10).
- **Gloves:** worn (owner's PPE answer: ear defenders, goggles, safety shoes, gloves; the F4 manual requires them).
- **Drops / distance to label:** nothing in the KB. Requirement already written in the design: **2D imager, IP54 or
  better, cordless, with batch memory.**
- **Lighting:** nothing measured; the Vitap manual asks for ≥ 500 lux at the machine.

## 5. How many people / stations?
Stations: **saw, edgebander, borer** (one of each, in series) **and assembly** — plus a planned *label printer and
scanner station* in the new layout (28/10). **Headcount: not in the KB** — the workshop is "often empty for days, and
some work is done by one person". Minda to confirm.

## 6. Labels now
**No part labels are in use** (Phase 1 is not built). The workshop owns a **Brother TD-4420DN** (asset FA2401): direct thermal,
203 dpi, ~104 mm print width, USB/serial/LAN; bought with **102 × 50** and **102 × 152 mm** die-cut rolls; suited to part
labels and job travellers, not to asset tags; network status and ZPL support **unverified**. Machine asset tags are the
group's "PROPERTY OF FISHBONE GROUP" QR tags — the QR holds the **bare 4-digit number** as text, leading zeros kept
(read from one tag with a phone camera). Part names in the exports follow `01 SIDE LEFT`.

## 7. Preference: PC scanner or Android handheld?
**Minda's to answer** (asked in session 05/11). What bears on it (my reading): Phase 4 puts scans into the **Vitap PC**, where a scanner that types like a keyboard
fits; the other phases post to Smartsheet, where a handheld or phone could do.

*Hand-off per CLAUDE.md s1 (Raw/-only cross-KB).*
