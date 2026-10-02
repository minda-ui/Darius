---
title: "Blum METABOX — data for SmartCabinet"
category: Processes
status: active
sensitive: false
created: 2026-10-02
updated: 2026-10-02
sources:
 - "`Raw/Blum_publication.pdf` — *Blum catalogue and technical manual 2022/2023* (KA-150), 758 pp., 548,904,350 B; METABOX is PDF pp. 394–417 (catalogue pp. 390–413). Extract: `Raw/Blum/Blum-2022-23_METABOX_pp394-417.pdf`"
 - "SmartCabinet online manual, `mainit/smartcabinet/tabelle_cam_accessori_guide.html`, `anagrafica_accessori.html`, `utility_import_accessori.html`, fetched 2026-10-02"
related:
 - ../Software/smartcabinet-online-manual.md
 - ../Software/smartcabinet-and-production-workflow.md
 - ../Machinery/vitap-k2-panel-saw.md
---

# Blum METABOX — data for SmartCabinet

**Owner, 2026-10-02: *"I need to input Metabox data into SmartCabinet as soon as we can."*** Every figure
below is from the Blum 2022/2023 catalogue. **Text values were extracted by script; values marked *(drawing)*
were read off a rendered drawing** and should be checked on a sample before a production run.

## 1. Try the import first — it may already be done for you

SmartCabinet has **Utilità → Import Accessori**: Kosmosoft publishes ready-configured hardware from many
brands, including the CAM parameters, and it is imported rather than typed. **Search it for `METABOX` or
filter by Fornitore = Blum before entering anything by hand.** Conditions from the manual: an internet
connection and a **valid Kosmosoft support contract**; an accessory whose *code* already exists is skipped,
so it cannot overwrite your own entries. Not every item comes with a 3D `.OBJ`.

**Only if METABOX is not offered there**, enter it manually with the data below.

## 2. Why METABOX does not fit SmartCabinet's runner table cleanly

SmartCabinet's **Tabelle CAM Accessori → Guide Cassetto** is built for runners screwed to **wooden drawer
sides**: `LX` side clearance, `LY` clearance under the drawer, `CX` groove width, `LBox` box depth, then up to
**six holes in the drawer sides** and four in the drawer back. **METABOX has steel sides** — the drawer side
*is* the runner — so the wooden parts are only a **base, a back and the front**, and the machined holes are
in the **cabinet sides** (runner) and the **front** (front fixing). Map it this way:

| SmartCabinet field | METABOX value | Note |
|---|---|---|
| `LX` (side clearance) | **15.5 mm** per side — wood is **LW − 31** | the 15.5 is *(drawing)*; LW − 31 is printed |
| `LY` (under the drawer) | **not printed** — the drawing shows the box on the cabinet profile; the only clearance figure given is **min. 24 mm above** the box | *(drawing)* — measure on a sample |
| `CX` (groove) | **none** — base sits on the steel side's flange, no groove | |
| `LBox` | **NL** (nominal length) | 270–550, see §3 |
| Drawer-side holes | **none** (steel sides) | leave the six side-hole groups empty |
| Back holes | **none** for the standard back fixing | back is fixed to the steel sides |

*Whether SmartCabinet then generates the **cabinet-side** runner holes from this table, or needs them set
elsewhere, is not stated in the manual pages read — check one cabinet's CN output before a batch.*

## 3. Product range — METABOX 320, single extension, 25 kg

| Height code | Side height | NL available (mm) | Back height (16 mm chipboard) | Inner-drawer front |
|---|---|---|---|---|
| **N** | **54** | 270, 350, 400, 450, 500, 550 | **39** | LW − 64 × **61** |
| **M** | **86** | 270, 350, 400, 450, 500, 550 | **71** | LW − 64 × **61** *(as printed — same as N; query)* |
| **K** | **118** | 350, 400, 450, 500, 550 | **103** | LW − 64 × **93** |
| **H** | **150** | 350, 400, 450, 500, 550 | **135** | LW − 64 × **125** |
| High front, gallery **B** | 86 + gallery | 350–550 | **127** | — |
| High front, gallery **D** | 86 + gallery | 350–550 | **191** | — |

**Cutting list (all 16 mm chipboard):**

| Part | Width | Depth / height |
|---|---|---|
| **Base** — drawer | **LW − 31** | **NL − 2** |
| **Base** — inner drawer | **LW − 31** | **NL − 18** |
| **Back** | **LW − 31** | per table above |
| **Front** — inner drawer | **LW − 64** | per table above |

**Minimum internal cabinet depth:** drawer **NL + 3**, inner drawer **NL + 5**, high front **NL + 7**.
**+2 mm** on the space requirement with BLUMOTION (+3 mm for an inner drawer with BLUMOTION).

## 4. Drilling

**Cabinet side — runner (cabinet profile) fixing**, first hole **37 mm** from the cabinet front edge, profile
set back **2 mm**; second hole from the first:

| NL | Holes from cabinet front edge (mm) |
|---|---|
| 270 | 37, **229** (37 + 192) |
| 300–350 | 37, **261** (37 + 224) |
| 400 | 37, **357** (37 + 320) |
| 450 | 37, **389** (37 + 352) |
| 500 | 37, **453** (37 + 416) |
| 550 | 37, **165** (37 + 128), **517** (165 + 352) |

Screws: **A** chipboard Ø4 × 15 · **B** system screw **Ø6 × 14.5, 661.1450.HG** (into **Ø5 System 32** holes) ·
**C** chipboard Ø3.5 × 15, 609.1500. *The vertical position of the hole line relative to the drawer is in
the drawing only and is not recorded here yet.*

**Front — EXPANDO / knock-in front fixing:** **Ø10 mm** (+0.2/−0.1), two holes **32 mm** apart vertically,
lowest **min. 13.5 mm** from the front's bottom edge (+2 with BLUMOTION), **12 mm** in from the edge *(drawing)*.

**Base — quick-assembly version:** **Ø5 mm**, two holes **32 mm** apart, **9 mm** from the edge, first hole at
**X = 69 mm** (drawer) / **53 mm** (inner drawer) *(drawing)*.

## 5. Part numbers

**Cabinet profiles + drawer sides, left/right pair**, colour R9001 cream: `320` + height letter + NL×10 + `C`
(screw-on) or `C15` (quick assembly) — e.g. **`320M4500C`** = M, NL 450, screw-on.

| Item | N | M / K / H |
|---|---|---|
| Front fixing bracket | standard **ZSF.1610** knock-in / **ZSF.1510** screw-on | CLIP **ZSF.130E** EXPANDO / **ZSF.1300** knock-in / **ZSF.1200** screw-on; or standard **ZSF.1800** / **ZSF.1700** |
| Cover caps | — | **ZAA.3700** (CLIP), **ZAA.3500** (standard) |
| Inner-drawer front fixing | **ZIF.3010** | M **ZIF.3000** · K **ZIF.3030** · H **ZIF.3050** |
| BLUMOTION soft close | **Z70.0320** | **Z70.0320** |
| Gallery rail (B/D) | — | **ZRE.321S.ID** (350) … **ZRE.521S.ID** (550) |
| BOXSIDE (D only) | — | **Z36H367SE01** (400) … **Z36H517SE01** (550) |

*No prices — the catalogue carries none. Costs come from invoices or a distributor list.*

## 6. What was found in the shop's SmartCabinet (2026-10-02)

From the owner's screenshot of **Anagrafica Accessori** after importing METABOX:

- **METABOX came in under its own category `30 METABOX`**, as two entries only — *METABOX H* and *METABOX K* —
  with **no nominal length**. Nothing METABOX sits under **`25 GUIDE CASSETTO`**, so the drawer's
  *Ferramenta → Guide* list does not offer it. **That is the "missing rails".**
- **LEGRABOX, also steel-sided, is set up as runners**: under `25 GUIDE CASSETTO`, **one entry per NL**
  (270–600). That is the model to copy.
- **Resolved the same evening by the owner: Kosmosoft's Import Accessori does carry METABOX rails, and they are now
  imported.** The manual fix below is **not needed**; it is kept only as the fallback. Owner to photograph the
  imported rail rows. *Superseded fallback:* add METABOX entries under `25 GUIDE CASSETTO`, one per NL, coded with
  Blum's part number (`320K3500C` … `320K5500C`, `320H3500C` … `320H5500C`; `C15` for quick assembly), then
  fill each row in *Guide Cassetto* per §2.
- **Physically nothing extra is bought** — Blum's `320…C` part is *cabinet profiles and drawer sides
  left/right*, rail and side together.
- **Asked of the owner:** a photo of the *Guide Cassetto* row for **LEGRABOX 450**, to copy Kosmosoft's `LY`
  and hole settings for a steel-sided box, and to see whether cabinet-side holes come from that table.
- SmartCabinet manual (*Ferramenta dei Cassetti*, *Scatola Cassetto*, fetched 2026-10-02): runners (**Guide**)
  and box systems (**Sistemi scatola**) are separate slots; a box system's **System = metallo** stops CN
  programs being made for its sides.

## 7. What is still open

- Whether Import Accessori already offers METABOX (**check first** — §1).
- The runner hole line's **height** and `LY` — drawing-only; confirm on one drawer.
- The **M inner-drawer front height** printed as 61 mm, the same as N — likely a catalogue reuse; measure.
- Whether SmartCabinet emits the cabinet-side runner holes from the Guide table — check one CN output.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-10-02 | Created from the Blum 2022/2023 catalogue METABOX section and three SmartCabinet manual pages, on the owner's request | Session 26 |
| 2026-10-02 | §6 added: METABOX imported under its own category, not as runners — why the rails are missing, and the proposed fix | Session 26 |
| 2026-10-02 | §6: rails found in Kosmosoft's import and imported by the owner; manual fix superseded | Session 26 |
