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
| ~~Drawer-side holes~~ → **the six hole groups are the CABINET-side rail holes** | `X` = from the cabinet front edge, `Y` = height above the bottom of the drawer side | **corrected 2026-10-03** — see §7, *The shop's imported row*. The 2026-10-02 reading ("leave empty") was wrong |
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

## 7. Check sheet for the imported Kosmosoft rails

Prepared 2026-10-02 so the owner's photo of the imported rows can be checked line by line. Every value is Blum's.

**Rail = cabinet profile `320` + height letter + NL×10 + `C` / `C15`.** It comes with the drawer side, and there is
**no separate rail part** in the catalogue. Heights: **N 54 · M 86 · K 118 · H 150**. N and M come in NL 270–550;
K and H in NL 350–550 (there is no 300 in any height).

| What to check in the imported row | Expected (Blum 2022/23) |
|---|---|
| Side clearance (`LX` or equivalent) | **15.5 mm per side**: the wooden parts are **LW − 31** wide *(drawing / printed)* |
| Hole groups (`X`/`Y`/`Ø`/`φ`) | **cabinet-side rail holes** (corrected 2026-10-03): `X` 37 + NL's rear hole; `Y` ≈ side height − 5 *(derived from the imported M row: 81)* |
| Box depth | **NL**; base NL − 2, inner drawer NL − 18 |
| Cabinet depth needed | ≥ **NL + 3** (inner drawer NL + 5, high front NL + 7; +2 with BLUMOTION) |
| **Cabinet-side holes from the front edge** (profile set back **2 mm**) | NL 270: **37, 229** · NL 300–350: **37, 261** · NL 400: **37, 357** · NL 450: **37, 389** · NL 500: **37, 453** · NL 550: **37, 165, 517** |
| Hole type | **Ø5 System 32** for system screws 661.1450.HG (B), or chipboard screws Ø4 × 15 (A); a small Ø3.5 screw (C) at the front lip |
| **Height of the hole line** | at least the **side height** above the part below it (**min. 54 / 86 / 118 / 150**, +2 with BLUMOTION), and at least **24 mm** below the part above *(drawing, read 2026-10-02)* |

**Then the real test:** draw one cabinet with one METABOX drawer and open the side panel's CN program. Look for
two Ø5 holes on one line, at 37 and the NL-dependent second position. If they are there, the import is complete.
If the side panel has no holes, SmartCabinet is not drilling METABOX rails, and that becomes the next question.

### First CN output checked — `Raw/Side Left.pdf`, 2026-10-03

The owner's SmartCabinet drilling drawing of a cabinet side: **`01 SIDE LEFT L851 × H570 × Z19`**, four METABOX
drawers. Read against this check sheet:

| Check | Drawing | Verdict |
|---|---|---|
| Rail holes present | **`C: 5x5`** (Ø5, 5 deep), one line per drawer, at **128.25 · 345.50 · 562.75 · 752** from the top end | **yes**: the import drills the rails |
| Front hole | **37** from the front edge | **matches** Blum |
| Further holes on each line | **165 · 261 · 357** from the front edge | **357 is NL 400's rear hole.** 165 and 261 line up with the NL 400 profile's intermediate holes *(drawing, p. 417)*. **No other NL uses 357**, so the rail drawn is **NL 400** |
| NL against the cabinet | side 570 deep; NL 400 needs ≥ 403 | fits, but **a 570-deep side would usually take NL 500** (≥ 503) — *if* the internal depth is ≥ 503. Is 400 intended? |
| **Bottom drawer clearance** | lowest line **752**: **99 mm** above the bottom panel (the shop's Cabineo joint puts the sides **on** the bottom panel, `cabineo-joint-geometry-reconciled.md`) | **N (54) and M (86) fit; K (118) and H (150) do not** (+2 with BLUMOTION). **Settled the same morning: the rail is M (`320M4000C`) — fits, 11 mm spare** |
| Spacing between drawers | 217.25 · 217.25 · 189.25 | fits any height, H included (needs ≥ 152) |
| Top drawer | line 128.25 → ~109 below the top rails | ≥ 24 ✓ |
| Hole depth | 5 mm | a pilot for chipboard screws Ø4 × 15 (A). **Too shallow to seat system screws Ø6 × 14.5 (B)**; the shop's own B holes elsewhere on this panel are 5 × 12 |

**Verdict:** the rails are being drilled at Blum's front position with an NL 400 rear hole. **Two questions for the
owner:** which height the **bottom** drawer is (K or H will not fit at 99 mm), and whether **NL 400** is the length
intended.

### The shop's imported row — `320M4000C METABOX`, read 2026-10-03

The owner's photo of *Tabelle CAM Accessori → Guide Cassetto*:

| Field | Imported | Blum | Verdict |
|---|---|---|---|
| Name | **320M4000C** — M (86), NL 400, screw-on | — | **the Side Left drawing is this rail**: M, not K/H |
| `LX` | **5** | 15.5 per side to the wood (LW − 31) | **consistent if SmartCabinet's METABOX box system counts a ~10.5 mm steel side** (5 + 10.5 = 15.5). Kosmosoft's LEGRABOX rows also say 5, and Blum's LEGRABOX base is LW − 35 with 12.8 sides: 4.7 a side. **So `LX` is per side, measured to the side's outer face.** *Check: the cutting list should give the METABOX base as **LW − 31**.* |
| `LY` | **18** | hole line ≥ 86 (+2 BLUMOTION) above the part below | 18 + `Y` 81 = **99**, exactly the Side Left drawing. **≥ 88 ✓, 11 mm to spare** |
| `CX` | 0 | no groove | ✓ |
| `LBox` | **398** | base NL − 2 = 398 | ✓ |
| Holes 1–4 | **X 37 · 165 · 261 · 357**, all **Y 81, Ø5, φ5** | fixing screws at **37 and 357** for NL 400; 165 and 261 are further profile holes | ✓. *Corrected 2026-10-03:* 165/261 are **Blum's own fixing holes** on the height-specific pages (K, PDF p. 403: 37, 165, 261 + the NL's rear hole); the general fixing page (p. 417) shows only the two main screws. **φ5 is a pilot**: fine for chipboard screws Ø4 × 15, too shallow for system screws Ø6 × 14.5 |
| `Y` 81 | hole height | the screw line sits ~5–6 mm below the top of an 86 side *(drawing)* | ✓ |

**Correction, owned:** on 2026-10-02 this article and the runner article read SmartCabinet's hole columns as holes in
the **drawer** sides (the manual says *"nei laterali dei cassetti"*) and told the reader to leave them empty for
steel sides. **The shop's own rows show they hold the cabinet-side runner positions.** Kosmosoft's LEGRABOX rows
carry exactly LEGRABOX's cabinet-profile holes (37, 69, 261, 293, 357), and the METABOX row produced the Side Left
holes. *The Italian was ambiguous. The shop's data was not.*

**Only one METABOX row (M, NL 400) is visible in the photo.** Every height and NL the shop builds needs its own
row: for another NL, the rear hole moves (229 / 261 / 357 / 389 / 453 / 165 + 517). For another height, `Y`
moves (≈ 49 N, 113 K, 145 H *(derived)*) and `LY` must keep `LY + Y` ≥ side height + 2.

## 7a. Drawer-box settings (`.SCS`) for METABOX K — what to set, and why

Written 2026-10-03 after the 350 mm unit's reviews kept producing **base 292 × 388 and back 302 × 103** against Blum's
**281 × 398 and 281 × 103**. Sources: SmartCabinet manual *Progettazione dei Cassetti* (Scatole) and Kosmosoft's
reference sheet **`legrabox_default_scs.pdf`** (fetched 2026-10-03), which lists the `.SCS` parameters for
prefabricated (metal) sides.

**Where:** the drawer's *Scatole* → the button under the box height opens the box window. Save / load configurations
with the buttons at its foot. For a box system they are stored as `.SCS` files in
`\Kosmosoft\SmartCabinet\dati_server\system_sc\Data\`, selected on the METABOX row of *Tabelle CAM Accessori →
Scatola Cassetto* (**Box Config file**). *Copy the file before editing.*

| `.SCS` parameter (box-window field) | Meaning (Kosmosoft) | Set for METABOX K | Why |
|---|---|---|---|
| `cass01_dist_lat` | side distance = runner `LX` | **5.00** (keep) | the imported rail's `LX` |
| `cass03_dist_sot` | lowest drawer above the cabinet bottom = `LY` | **18.00** (keep) | the imported rail's `LY` |
| `cass05_spess` (➏a sides) | thickness of the prefabricated sides | **10.50** | *(derived)* LW − 31 needs 15.5 a side; 15.5 − 5 = 10.5. **This is the setting that makes the box 281 inside** |
| `cass_sot_dz` | how far the base enters the sides | **0.00** | the base sits **between** the steel sides on their flange, not in a groove |
| `cass_sp_sot` (➏b base) | base thickness | **16.00** | Blum's cutting list is 16 mm chipboard |
| `cass_sp_die` (➏d back) | back thickness | **16.00** | as above |
| `cass_sp_fro` (➏c front) | inner front thickness | **0.00** | METABOX has no inner front; 0 = not made |
| `bCassDDIE` (➐) | 0 = back across the sides' outer edges; **1 = back between the sides** | **1** | Blum's back is LW − 31, between the sides. *The 302-wide back is what `0` produces* |
| `bCassDIESOT` | 0 = back runs down past the base; **1 = back stands on the base** | ~~1~~ **0**, with `bCassDIESOTFILO=1` *(corrected 2026-10-03)* | Setting 1 made SmartCabinet take the base off the back's height (**back 87**) **without** lengthening the base (382), so neither part was Blum's. **0 + FILO 1 gives back 103 down past a 382 base, 398 overall**: Blum's overall box, with the base/back joint differing from Blum's drawing. *Not in the English window; edit the `.SCS`* |
| `cass_sot_dy` | base height above the bottom of the sides | **0.00** *(found 16.00 on 2026-10-03)* | **The cause of the 87 mm back**: the base was lifted 16 above the bottom of the steel sides, and with `DIESOT=0 / FILO=1` the back only runs down to the base's underside, so 103 − 16 = 87. METABOX's base sits on the steel side's bottom flange (Blum K: 16 base + 103 back ≈ the 118 side) |

**The shop runs the English version of SmartCabinet** (owner, 2026-10-03), but the online manual is **Italian only**: no English edition was found at `smartcabinet.eu/manuale/` (checked 2026-10-03). **The `.SCS` parameter names are the same in both languages**, so editing the file is the language-proof route. The English on-screen labels are still to be mapped from a screenshot. *Do not guess them.*

**The English *Drawer Box settings* window, mapped 2026-10-03 from the owner's screenshot** (icons are the same as
the Italian manual's; the window has almost no words). Values *as found* explain the bad parts exactly. **Box outer
302 (LW − 2 × 5)**, sides 16 with **10 mm grooves** each side: 302 − 32 + 20 ≈ base 292; back across the sides' outer
edges = **302**.

| Row (manual no.) | Icon | Found | Set for METABOX K |
|---|---|---|---|
| 1 (➌a/b) | box / front crossed out | off / off | leave off |
| 2 (➍) | gap, top box to cabinet | 18 | leave |
| 2 (➎) | box above front bottom / auto | 18, manual | leave |
| 2 (➏) | **thicknesses**: teal = **sides**, black = **base**, green = **front**, red = **back** | 16 / 16 / 16 / 16 | **sides 10.5** *(derived)*, base **16**, front **0**, back **16** |
| 2 (➐) | back-to-side joint: 1st = back across the sides, 2nd = sides past the back, 3rd = mitre | **1st** | **2nd**: the back goes **between** the sides → 281 |
| 3 (➑a, ➑b) | base into the back; *">130"* = only above a front height | off; 130 | leave off |
| 3 (➒) | base **under** front and back | off | **ON**: full-length base, back stands on it |
| 3 (➓) | base into the front | off | leave off |
| 4 (⓫a) | box back to cabinet back | 20 | leave |
| 4 (⓫b, ⓫c) | groove depth in sides (green) / front-back (red) | **10 / 10** | **0 / 0**: METABOX base sits on the steel flange, no groove |
| 4 (⓫d–g) | groove air / width / height / min. width | 0 / 16 / 16 / 0 | leave; check the base height in the result |
| 4 (⓬) | groove tool: cutter / **saw LAMA120**, 3.50, 1 pass | saw | irrelevant once the grooves are 0 |
| 5 (⓭–⓰) | box dowels Ø8 / bolts / Cabineo / Clamex | Ø8, 20, 15/20; others off | irrelevant (no wooden sides) |
| 5 (⓱) | front-to-box dowels | 0 | **leave 0**: the METABOX front fixes by brackets |
| foot | *Set as Default* · load · **save** | — | **Save as a named `.SCS` (e.g. `METABOX_K.scs`) and select it in *Box Config file*. Do NOT press *Set as Default*: it would change every wooden drawer too** |

**VERIFIED SET — 2026-10-03, 350 mm unit v9: SmartCabinet produced base 281 × 382 × 16 and back 281 × 103 × 16.**
In the METABOX `.SCS`, loaded on the METABOX row: `cass01_dist_lat=5.00` · `cass03_dist_sot=18.00` ·
**`cass05_spess=10.50`** · `cass_sp_sot=16.00` · `cass_sp_die=16.00` · **`cass_sp_fro=0.00`** · **`cass_sot_dy=0.00`** ·
`cass_sot_dz=0.00` · **`bCassDDIE=1`** · **`bCassDIESOT=0`** · **`bCassDIESOTFILO=1`**. The box is **398 deep overall** (382 base +
16 back standing behind it), matching Blum's NL − 2. *The base/back corner differs from Blum's drawing (base under
the back); this is the owner-accepted build.* **Use this set for every METABOX K job; recheck `BH` / heights for other
side heights (N/M/H).**

**What actually takes effect (proved 2026-10-03 on the 350 unit):** edit the `.SCS` in Notepad, restart SmartCabinet, and **load it through *Box Config file* on the METABOX row** of the drawer-box table. Values typed and saved in the *Drawer Box settings* window did **not** reach the box-system output. The first load fixed the back height (`cass_sot_dy=0`) and exposed that the file still lacked `cass05_spess=10.50`.

**Check after regenerating (METABOX K, NL 400, LW 312):** **base 281 × 398 × 16**, **back 281 × 103 × 16**, **no
`FRONT`/`FRONTAL` inner-front part**, base program **16 mm** with no grooving. If the back comes out ~87 high
instead of 103, the back-height rule has changed with `bCassDIESOT`. Adjust the height, not the width. *None of these
values is from a SmartCabinet METABOX template, which this KB has not seen: if Kosmosoft's import shipped a
METABOX `.SCS`, compare it first.*

## 8. What is still open

- Whether Import Accessori already offers METABOX (**check first** — §1).
- The runner hole line's **height**: read from the drawing 2026-10-02 (§7). `LY` is still to confirm on one drawer.
- The **M inner-drawer front height** printed as 61 mm, the same as N — likely a catalogue reuse; measure.
- Whether SmartCabinet emits the cabinet-side runner holes from the Guide table — check one CN output.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-10-02 | Created from the Blum 2022/2023 catalogue METABOX section and three SmartCabinet manual pages, on the owner's request | Session 26 |
| 2026-10-02 | §6 added: METABOX imported under its own category, not as runners — why the rails are missing, and the proposed fix | Session 26 |
| 2026-10-02 | §6: rails found in Kosmosoft's import and imported by the owner; manual fix superseded | Session 26 |
| 2026-10-02 | §7 check sheet for the imported rails, incl. hole-line height read from the drawing | Session 26 |
| 2026-10-03 | §7: first CN output (`Raw/Side Left.pdf`) checked; NL 400 pattern, bottom-drawer clearance 99 mm | Session 27 |
| 2026-10-03 | §7: the imported `320M4000C` row checked — M not K/H, so the bottom drawer fits. **§2 corrected: the hole groups are cabinet-side holes** | Session 27 |
| 2026-10-03 | §7a: drawer-box `.SCS` settings for METABOX K, from Kosmosoft's parameter sheet | Session 27 |
