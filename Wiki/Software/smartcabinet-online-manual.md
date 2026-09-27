---
title: "SmartCabinet's online manual — map, and what it settles about T016"
category: Software
status: draft
sensitive: false
created: 2026-09-27
updated: 2026-09-27
sources:
 - "`https://www.smartcabinet.eu/manuale/it_index.html` and nine pages beneath it, fetched 2026-09-27 over HTTPS, all HTTP 200 — sizes and sha256 in the provenance table below"
 - "Extracted text of the four CN/tool-chain pages captured verbatim in `../../Outputs/2026-09-27-smartcabinet-manual-capture-cn-chain.md`"
 - "Owner (Minda), 2026-09-27: the URL to check, and the instruction to map the manual and go at T016"
 - "`Wiki/Processes/tpacad-tool-match-criteria.md` — the five criteria and error -27, from TPA's `CnCadOpti_eng.pdf`"
 - "Smartsheet Tasks `T016` (row `3054339713795972`), note read 2026-09-27"
related:
 - ../Software/smartcabinet-and-production-workflow.md
 - ../Software/kitchen-unit-library.md
 - ../Processes/tpacad-tool-match-criteria.md
 - ../Processes/carcase-fixings-cabineo-x-vs-confirmat.md
 - ../Machinery/vitap-k2-panel-saw.md
 - ../Machinery/vitap-k2-drill-head-tooling.md
---

# SmartCabinet's online manual — map, and what it settles about T016

**This KB has worked the TpaCAD side of the Vitap from PDFs found on the machine's own PC. The design
side had no manual at all until 2026-09-27**, when the owner supplied a URL. There is a complete online
manual at `smartcabinet.eu/manuale/`, in **Italian**, and it answers part of a question §1 of the
charter has carried as *unverified* since 2026-09-17.

**It is a vendor site, not our copy.** Every page cited here was fetched and hashed on 2026-09-27 so a
future session can re-fetch and tell whether it has changed; the four pages the findings rest on have
their text captured in `Outputs/2026-09-27-smartcabinet-manual-capture-cn-chain.md`. **A citation to a
vendor URL with no capture behind it rots silently**, which is why the capture exists.

**There is no English edition.** `/manuale/en_index.html` returns **404**. Everything below is
translated by me from the Italian, with the original quoted alongside — the same discipline the TpaCAD
material gets.

## 1. The shape of the manual

Root is `/manuale/it_index.html`, and it is **not a table of contents**: it is a picture of the
application's own main menu with clickable hotspots, so the structure has to be read off the links.
Three sections hang beneath it:

| Section | Path | Has an index page? |
|---|---|---|
| **SmartCabinet** — the CAD itself | `mainit/smartcabinet/` | **No** — only the main-menu hub |
| **Render** | `mainit/render/` | `_render_index.html` |
| **CRM** | `mainit/crm/` | `_crm_index.html` |

**The hub is not a complete index.** Pages exist that it does not list — `cn.html`, `giunzioni.html`,
`progettazione_fianco.html` (singular, beside the listed plural `_fianchi`), `ante_progettazione.html`,
and all sixteen `tabelle_cam_accessori_*` pages. **A menu absence is not evidence that something is
undocumented**; the only way to find a page is to follow in-page links.

## 2. The map

All paths relative to `mainit/smartcabinet/`.

**Design, part by part** — `progettazione_misure-forma` (dimensions and shape — the first window
opened) · `_cielo` top · `_fondo` bottom · `_fianchi` sides · `_zoccolo` plinth · `_divisori_v` /
`_divisori_h` dividers · `_ripiani` shelves · `_griglie` grilles · `_schienale` back · `_top` worktop ·
`_traverse` rails · `_telaio` carcase frame · `_cover` · `_ferramenta` hardware · `ante` +
`ante_test_apertura` doors and door-swing test · `cassetti` drawers

**Machine side** — `cn` (CN configuration) · `cam` (pick CN and junction configurations) · `cnc`
(generate the CN files) · `lavorazioni` · `ottimizzatore` + `pannello_ottimizzazioni` · `giunzioni`
(joints)

**Materials and accessories** — `registro-materiali` · `anagrafica_accessori` ·
`tabelle_cam_accessori` (§3)

**Output** — `export_csv` · `export_viste_dxf` · `export_obj` · `stampe` prints · `visualizzatore`
viewer · `esplodi` exploded views

**Settings and housekeeping** — `settings` · `settaggi_cabinet` · `utility` · `bacchetta_magica` magic
wand · `misurazioni` · `viste` · `errors` (anomaly alerts) · `nuovo` / `apri` / `salva` / `chiudi` ·
`release_note` · `news` · `ticket` · `help_tasti_rapidi`

**3D / render entry points** — `ferramenta_3d` · `luce` · `render`

*Note what is not in that list: **no TCN, TpaCAD or ISO export**. The only named exports are CSV, DXF
views and OBJ. CN files are produced by `cnc`, through a postprocessor — see §5.*

## 3. The branch the main menu hides

`tabelle_cam_accessori` is one hotspot on the main menu and **sixteen pages beneath it** — the
configuration tables for everything the CAD can place:

`_utensili` **tools** · `_guide` drawer runners · `_maniglie` handles · `_cerniere` hinges · `_piedini`
feet · `_reggipensili` wall-unit brackets · `_scolapiatti` · `_appendiabiti` · `_scorrevole_int` /
`_scorrevole_ext` sliding kits · `_aventos` · `_barre` reinforcing bars · `_legrabox` · `_gole` gola
profiles · `_oggetti_lavorazioni` · `_wo` Working Objects

## 4. The tool table has no ID field

`tabelle_cam_accessori_utensili.html`. A tool record is **six fields**: `Nome` (required), `Senso di
rotazione`, `Numero di giri`, `Avanzamento`, `Diametro`, `Descrizione`. And the name is the identifier:

> `Nome` … *"sarà poi l'identificativo utilizzato dalla macchina per richiamare quello specifico
> utensile"*
> — will then be the identifier the machine uses to call that specific tool.

**There is no numeric tool ID, code or position field, and the page says nothing about where tool data
comes from or whether it is shared with, imported from or exported to the machine's own catalogue.**

**And the page's own first sentence says what goes in the table — including the exception that matters:**

> *"In questa finestra vanno inseriti gli utensili, tipicamente le frese e le lame **ma per alcune
> macchine anche le punte**, che è necessario specificare perchè non selezionati automaticamente."*
> — this window takes the tools, typically cutters and blades **but for some machines the drill bits
> too**, which have to be specified because they are *not* selected automatically.

**So naming a drill is machine-dependent, not impossible.** This is the same exception `cn.html` states
from the other side (§5) — and **whether the Vitap is one of those machines is precisely the open
question**, not something either page answers.

## 5. What the CN chain actually does

`cn.html` is the machine-configuration page. Three passages matter.

**Drill bits are chosen by the machine, not by SmartCabinet:**

> *"qui troviamo le impostazioni per svariati utensili, tipicamente frese e lame in quanto le punte a
> forare vengono normalmente selezionate automaticamente, questi utensili devono essere stati
> preventivamente inseriti in Tabelle CAM Accessori sotto Utensili"*
> — here are the settings for various tools, **typically cutters and blades, since drill bits are
> normally selected automatically**; these tools must have been entered beforehand in CAM Accessories
> Tables under Tools.

`giunzioni.html` says the same thing five separate times, once per joint family:

> *"qualora non sia impostato alcun utensile verrà selezionata automaticamente una punta"*
> — if no tool is set, a drill bit is selected automatically.

**The postprocessor is the whole translation layer, and it is machine-specific:**

> *"A sinistra in alto troviamo raggruppate in un menu a tendina la selezione del postprocessor da
> utilizzare con SmartCabinet, va selezionato quello che corrisponde alla macchina in uso, **se nella
> lista è presente solo la voce Gen 1 il modulo CN non è attivo in SmartCabinet**"*
> — the postprocessor dropdown; pick the one matching your machine; **if the list holds only `Gen 1`,
> the CN module is not active in SmartCabinet.**

Postprocessors are named by machine brand (`Pendular` is offered *"per il postprocessor Biesse"*), and
some options — non-90° cuts among them — are *"visibili solo per alcuni postprocessor"*. The manual
adds, about the origin settings, *"è in ogni caso opportuno consultare il produttore della macchina"* —
consult the machine manufacturer. **So the authority on what the Vitap's postprocessor emits is
TPA/Vitap, not this page and not me.**

**And there is a route to naming drilling tools explicitly — gated on the CN configuration:**

> *"Il menu ➌ e il relativo pulsante che raffigura una ruota dentata ➍ compaiono **solo quando vengono
> selezionate alcune particolari configurazioni cn** in cui è necessario specificare gli utensili per le
> forature … dal menu a tendina Tool ➏ selezionare l'utensile, che dev'essere stato preventivamente
> inserito in Tabelle CAM Accessori sotto Utensili. Oltre al diametro ➐ sono da selezionare poi la
> direzione ➑ della foratura, **il tipo ➒ di foro che l'utensile dovrà praticare** e se si tratta di una
> punta o di una fresa ➓"*
> — the menu and its cogwheel button appear **only when certain particular CN configurations are
> selected**, where drilling tools must be specified … pick the tool from the `Tool` dropdown; besides
> the diameter, set the drilling **direction**, **the type of hole the tool is to make**, and whether it
> is a drill or a cutter.

### Where the CN files go — and the charter's open question about it

`cnc.html`:

> *"I file CN vengono memorizzate in sottocartelle all'interno del percorso
> `\Kosmosoft\SmartCabinet\CNC\`, le sottocartelle avranno nomi inerenti al postprocessor CN in uso"*
> — CN files are written in subfolders under `\Kosmosoft\SmartCabinet\CNC\`, the subfolders named after
> the CN postprocessor in use.

> *"E' possibile nei Settaggi impostare un percorso locale o di rete per la generazione dei file CN, il
> parametro è `AutoCopyCNFolder` e si trova nel paragrafo CAM. Impostando questo percorso i file
> potranno essere memorizzati direttamente nel pc a bordo macchina."*
> — Settings can set a local **or network** path for CN file generation, parameter `AutoCopyCNFolder`
> in the CAM paragraph; with it set, the files can be written **straight to the PC on the machine**.

Also: **one CN file per piece** (plus optimised-cutting files if Nesting is active, plus a `_DX` file
per piece when Pendular is on), and piece and file names are settable under Settings → `CN Names`.

**§1 of the charter says files reach the machines "through Google Drive, in a dedicated folder (that
folder not yet identified or examined)".** That is the owner's correction of 2026-09-17 and it stands.
What this adds is three named things to look at instead of one vague one: the local output path, the
`AutoCopyCNFolder` value, and whether the subfolder name tells us the postprocessor in use.

**A trap worth knowing before anyone changes a setting.** CN configuration has **two scopes**: the
**default**, reached by the `CAM` button top right, and **the currently open cabinet only**, reached by
the `CN` (lightning) button under `Settaggi cabinet`. The manual advises copying the in-use
configuration before editing it rather than editing it in place. *Edit through the wrong button and you
have changed one cabinet, not the shop.*

## 6. What this settles about T016, and what it does not

**Settled: the "systemic half" of T016 rests on a premise the manual contradicts.** §7 of the charter
has described a systemic fix as *"getting the post-processor to emit a Tool ID on export, so step two is
not repeated by hand on every operation of every unit, since every hole in the master exports with
`#1001=0`."*

- SmartCabinet's tool record **has no ID field to emit** (§4). The identifier is the **name**.
- For drilling, the **normal** case is that the program names no tool and the machine chooses (§5),
  stated in two independent places.
- So **`#1001=0` on every hole in the master is the expected output of the normal case, not a defect** —
  and "get SmartCABINET to emit a Tool ID" asks for a field that does not exist.

**Stated carefully, because the manual states the exception twice.** *"per alcune macchine anche le
punte … non selezionati automaticamente"* (§4) and the drilling-tool table that appears for *"alcune
particolari configurazioni cn"* (§5) both say drill bits **can** be named where the machine needs it. So
the correct claim is **not** "SmartCabinet cannot name a drill" — it is that **it names none by default,
there is no ID to name it by, and whether our machine is one of the exceptions is unchecked.** *An
earlier draft of this article said "contrary to how the program is designed to work". That was too
strong, and was corrected the same day from the page's own first sentence.*

**That does not make T016 smaller. It relocates it**, and it agrees with where the 2026-09-23 correction
already put it: the blind-Ø3 failure is a **tooling/design mismatch**, not a software fault, and the
decision is the owner's — either the master stops specifying blind Ø3, or a blind Ø3 bit goes on the
head, and the second is a purchase.

**Not settled, and explicitly labelled:**

1. **Whether the Vitap's postprocessor exposes the drilling-tool table.** It appears *"solo … alcune
   particolari configurazioni cn"*. If it does, then **`il tipo di foro`** — the type of hole the tool
   is to make — is plausibly the blind/through distinction, which is **criterion 2** of the -27
   checklist, declarable on the design side rather than discovered at the machine. **That inference is
   mine, from one sentence, and the field's permitted values are not documented.** Do not act on it
   before looking at the dialog.
2. **Whether SmartCabinet's tool names reach TpaCAD's CN Tools catalogue at all.** §1's question stands.
   The manual's silence is now informative — the join it describes is by **name**, machine-side — but
   silence is not an answer.
3. **Which postprocessor the shop is running**, and whether the CN module is licensed at all. One look
   at the dropdown answers both: only `Gen 1` means no CN module.

## 7. Cabineo is a first-class joint in SmartCabinet

`giunzioni.html` has a category *"Giunzioni eccentriche e Cabineo"*, configured element by element:
diameter and effective length per element, tool and number of passes for the first two, the central
screw's diameter with **different hole lengths depending on whether it mounts in the carcase, a divider
or the back**, and the length, width and thickness of the joint's support base. This bears directly on
`../Processes/carcase-fixings-cabineo-x-vs-confirmat.md`, and sits beside the 2026-09-23 finding that
`CABINEO` is a **native** working in TpaCAD. **Not worked here** — it deserves its own pass.

## 8. Two predictions of mine that were wrong

- **`lavorazioni.html` is not a workings catalogue.** I expected it to carry the tool mapping. It is a
  two-item menu: *Intagli* (notches) and *Lavorazioni a Onda* (wave machining). Nothing else.
- **`cam.html` holds no tool content** despite the filename — only *Configurazione CN* and
  *Configurazione Giunzioni*, create/modify/delete.

*Recorded because a wrong prediction that is quietly dropped gets made again.*

## Provenance

Ten pages, fetched 2026-09-27, all HTTP 200. `sha256` of the HTML as served, first 16 hex:

| Page | Bytes | sha256 | Text captured? |
|---|---|---|---|
| `it_index.html` | 23,986 | `2e319f5131a5137b` | no |
| `progettazione_misure-forma.html` | 54,050 | `5ae19054b8da87d5` | no |
| `cam.html` | 11,220 | `f15f7ae385f270b5` | no |
| `cn.html` | 46,271 | `be19a6481ce9e566` | **yes** |
| `tabelle_cam_accessori.html` | 9,379 | `95f696433e6a93c4` | no |
| `tabelle_cam_accessori_utensili.html` | 7,180 | `113fb21f3567c1dc` | **yes** |
| `lavorazioni.html` | 5,430 | `83ca5e731a08db15` | **yes** |
| `cnc.html` | 6,382 | `2f146991afe3a5c0` | **yes** |
| `giunzioni.html` | 62,404 | `111d4bb50659765b` | no |
| `release_note.html` | 4,607 | `9b8bb9519984d73e` | no |

`release_note.html` is only a wrapper that displays a text file, so **it cannot tell us the shop's
version from here** — that has to be read off the installation. Six pages are cited without their text
being captured; if one of them later matters, re-fetch it, check the hash, and capture it then.
