---
title: "SmartCabinet's online manual — map, and what it settles about T016"
category: Software
status: active
sensitive: false
created: 2026-09-27
updated: 2026-09-28
sources:
 - "`https://www.smartcabinet.eu/manuale/it_index.html` and nine pages beneath it, fetched 2026-09-27 over HTTPS, all HTTP 200 — sizes and sha256 in the provenance table below"
 - "Extracted text of the four CN/tool-chain pages captured verbatim in `../../Outputs/2026-09-27-smartcabinet-manual-capture-cn-chain.md`"
 - "Owner (Minda), 2026-09-27: the URL to check, and the instruction to map the manual and go at T016"
 - "`giunzioni.html` re-fetched 2026-09-28, HTTP 200, 62,404 B, sha256 unchanged at `111d4bb50659765b` — text captured and §7 written from it"
 - "Owner (Minda), 2026-09-28: how to joint a vertical divider into the top and bottom panels, with a SmartCabinet 3D wireframe"
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

## 7. Cabineo is a first-class joint — and the `giunzioni` pass, done 2026-09-28

*This section said **"Not worked here — it deserves its own pass"** for a day. The pass was made on
2026-09-28, prompted by the owner asking how to joint a vertical divider into the top and bottom panels.
The page was re-fetched and **its hash is unchanged** (62,404 B, `111d4bb50659765b`), so everything below
is the same document the 2026-09-27 map was built from — only read properly this time.*

### 7.1 Joints are configured per cabinet part, and a vertical divider is one of them

**This is the finding the owner's question turned on.** The page states plainly that the way joints are
inserted is **differentiated for each part of the cabinet**, and lists them:

`struttura` ➊ · **`divisori verticali` ➋** · `divisori orizzontali` ➌ · `catene` for the top or bottom ➍ ·
`traverse` ➎ · `zoccolo` ➏ · `cornice` ➐ · `pilastro` ➑ · `ripiani` ➒ · `schienale` ➓ · `griglia` ⓫

**A vertical divider is not an improvisation on the carcase case — it has its own configuration.** The
back ➓ is split further into *the part joined to the structure* and *the part joined to any dividers*;
the grille ⓫ likewise splits vertical from horizontal dividers. *The software's model of "what meets
what" is finer than this KB had assumed.*

### 7.2 Three ways in, and they differ in scope — this is the answer to "how do I add them"

| Opened from | What it changes |
|---|---|
| the **CAM** button, top right | the **default** joint configuration for all cabinets |
| the **Giunzioni** button, left, in the **Settaggi cabinet** menu | **only the cabinet currently open** |
| **Personalizza Giunzioni**, from the **Intagli** window | **individual pieces** of the open cabinet |

*Three scopes, one page. Reading `cam.html` alone — which is where the 2026-09-27 pass stopped — shows
only the first and makes the feature look global.*

### 7.3 What is set per part

Distance of the joint from the cabinet's **front** ⓬ and **back** ⓭; the **number of joints to insert**
⓮; an **offset to avoid conflicts between opposing joints** ⓯; the **joint type** ⓰ and the specific
joint from the dropdown ⓱.

***That offset is not a detail for this shop's case.*** A divider joints into the same top and bottom
panels that already carry the two carcase sides' Cabineo holes. **⓯ exists precisely so those two sets of
holes do not collide**, and it is the parameter to reach for if a divider's joints land on top of the
structure's.

**Five joint types**, selected by buttons — **and if none is selected, only dowels (`spine`) are
inserted:**

1. **Tiranti e Minifix** — for `catene`, `traverse`, `cornice`, `zoccolo` and `pilastro` a **minimum
   piece length** can be set, below which no joint is inserted.
2. **Giunzioni eccentriche e Cabineo** — *"in questa categoria rientrano anche le giunzioni laterali e i
   supporti per i ripiani Lamello, Clamex e Divario"*: the category also carries lateral joints and the
   Lamello / Clamex / Divario shelf supports.
3. **Binari per Giunzioni a Coda di rondine** — dovetail rail.
4. **Giunzione a incastro** — interlocking.
5. **Dado** — nut.

### 7.4 The Cabineo configuration itself

*"Giunzioni eccentriche, Cabineo e supporti per ripiani"*, with add ➊ / delete ➋ buttons at the bottom:

- **The three elements**, coloured **blue, orange and green**, counted **from the end opposite where the
  central screw exits**: per element a **diameter** ➌ and an **effective length relative to the next
  element** ➍; for the first two, a **tool and number of passes** ➎.
- **The internal screw**: **diameter** ➏, then ***different hole lengths depending on whether it mounts
  in the structure ➐, in the dividers ➑, or in the back ➒*** — each with its own tool. **This is the
  divider case, named by the software itself.**
- **Thickness of each element** ➓, identified by colour; last, in black, the **central pin's distance
  from the top**.
- The **support base**: length, width, thickness ⓫, with its tool.
- An optional **Database** ⓬ the joint belongs to — *must already exist in **Anagrafica Accessori**,
  group **Giunzioni e Tiranti***; used in printouts and the CRM module.

**An alternative layout exists: `Forature di testa` ⓭** (end boring), ticked at the top. The elements lie
**horizontally** and are orange, green and black; diameters ⓮, tool and passes for the first two ⓯, and
**again different hole lengths for structure ⓰ / dividers ⓱ / back ⓲**. Lengths ⓳ are then set for the
green element, for orange-plus-green, and for the black element's distance from the top.

*Two notes the page repeats:* **if no tool is set, a drill bit is selected automatically**; and if a joint
has fewer than three elements, set the unused parameters so they are ignored.

### 7.5 Centring a joint in the panel thickness

The page carries an explicit note: **to place a joint exactly at the centre of the panel's thickness,
tick `Aggiungi metà spessore pannello` and set the offsets to 0.** *Recorded here because a divider is the
case where "centre of the thickness" stops being automatic in one's head — it has material on both sides.*
*Read in a general note on the page rather than inside the Cabineo block, so **which joint families it
governs is not established** — check it against the dialogue before relying on it.*

### 7.6 What this does not settle

- **It is the vendor's manual, not this shop's settings.** Everything above is what SmartCabinet *can* be
  configured to do. **What the shop's installation actually has in `Configurazione Giunzioni` is unread**,
  and the only way to know is to open it.
- **No dimension here is the shop's.** The master's measured geometry — pocket ≈37 × 15 × 13 mm, `Ø5 × 12`
  face hole, `Y = 230` and `Y = 40` — comes from the decoded `.TCN` files, not from this page, and the two
  have **not** been reconciled. *That reconciliation is the obvious next pass and is deliberately not
  claimed here.*
- **Dowels are the silent default.** *"nel caso che nessun tipo di giunzione sia selezionato saranno
  inserite solo le spine"* — a divider configured with no joint type will still produce a part, with
  dowels. **Silence is a setting, not an error**, which makes it exactly the kind of thing to check.

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
| `giunzioni.html` | 62,404 | `111d4bb50659765b` | **yes — 2026-09-28** |
| `release_note.html` | 4,607 | `9b8bb9519984d73e` | no |

`release_note.html` is only a wrapper that displays a text file, so **it cannot tell us the shop's
version from here** — that has to be read off the installation. Five pages are still cited without their
text being captured; if one of them later matters, re-fetch it, check the hash, and capture it then.

***That instruction was followed on 2026-09-28 and it worked exactly as written*** — `giunzioni.html`
re-fetched, **hash identical**, text captured, §7 rewritten from it. *The hash is what made the re-fetch
safe to build on: without it, a year-old page and a silently-revised one look the same.*

**Two corrections from that re-fetch, both mine and both worth keeping.**

1. ***"Blocked by the egress proxy" was wrong.*** On 2026-09-28 this KB recorded that `smartcabinet.eu`
   had become unreachable and that `giunzioni.html` was therefore lost. **It had not.** Two faults were
   mistaken for one: the URL being requested was `/manuale/giunzioni.html`, which returns **HTTP 404** —
   and **this article's own §2 already says every path is relative to `mainit/smartcabinet/`** — while the
   connection itself is **intermittent**, one attempt resetting mid-exchange and the next returning 200.
   *A 404 and a refused tunnel are different failures; neither is a block, and I reported both as one.*
2. **A failure diagnosed once became a standing fact.** *"Unreachable"* was written without a timestamp
   and then relied on for the rest of the day, which is `HL-0032`'s lesson — **an absence is only an
   absence as of a timestamp** — arriving from the other side. **Re-test before repeating a negative.**
