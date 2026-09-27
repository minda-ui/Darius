# Change log — 2026-09-27 — SmartCabinet has an online manual, and it says T016's "systemic half" was never a real job

**The owner sent one URL to test.** It resolved, and behind it was the thing this KB has never had: a
complete manual for the **design** side. Every TpaCAD fact here was won from PDFs on the machine's own
PC; SmartCabinet had nothing. Ten pages were fetched, hashed and mapped, four were captured verbatim,
and one sentence in them retires a job that has sat in §7 for eight days.

## 1. The map

`Wiki/Software/smartcabinet-online-manual.md`, new, 14,962 B. Root `smartcabinet.eu/manuale/it_index.html`
is **not a table of contents** — it is a picture of the application's main menu with hotspots, so the
structure had to be read off the links. Three sections: `mainit/smartcabinet/` (the CAD, **no index page
at all**), `mainit/render/`, `mainit/crm/`.

**The hub is not a complete index**, and that is worth knowing before anyone reads a menu absence as
"undocumented": `cn.html`, `giunzioni.html`, `progettazione_fianco.html` (singular, beside the listed
plural), `ante_progettazione.html` and **all sixteen `tabelle_cam_accessori_*` pages** exist and are not
listed. `tabelle_cam_accessori` alone is one hotspot hiding sixteen tables — tools, runners, handles,
hinges, feet, brackets, sliding kits, Aventos, Legrabox, gola profiles, Working Objects and the rest.

**No English edition.** `/manuale/en_index.html` returns **404**. Everything is Italian, so every quote
in the article carries the original beside the translation.

**And no TCN, TpaCAD or ISO export in the list.** The only named exports are CSV, DXF views and OBJ; CN
files come out of `cnc.html` through a **postprocessor**. *The words TpaCAD, TCN and ISO do not appear
anywhere in the ten pages read.*

## 2. What it settles: T016's "systemic half" rests on a premise the manual contradicts

§7 has described the systemic fix as *"getting the post-processor to **emit** a Tool ID on export, so
step two is not repeated by hand on every operation of every unit, since every hole in the master
exports with `#1001=0`."*

**There is no Tool ID to emit.** SmartCabinet's tool record is **six fields**: `Nome` (required), `Senso
di rotazione`, `Numero di giri`, `Avanzamento`, `Diametro`, `Descrizione`. No ID, no code, no position.
`Nome` *is* the identifier — *"sarà poi l'identificativo utilizzato dalla macchina per richiamare quello
specifico utensile"*.

**And for drilling the program names no tool at all, by design.** `cn.html`: the tool settings are
*"tipicamente frese e lame in quanto **le punte a forare vengono normalmente selezionate
automaticamente**"*. `giunzioni.html` says it five more times, once per joint family: *"qualora non sia
impostato alcun utensile verrà selezionata automaticamente una punta"*.

**So `#1001=0` on every hole in the master is the intended output, not a defect** — and "get SmartCABINET
to emit a Tool ID" was never a missing feature; for drills it runs against how the program works.

**This does not shrink T016. It confirms where 2026-09-23 already put it**: a tooling/design mismatch and
an owner decision — the master stops specifying blind Ø3, or a blind Ø3 bit goes on the head, and the
second is a purchase.

## 3. What it does not settle — three cheap checks, and a trap

1. **The postprocessor dropdown.** *"se nella lista è presente solo la voce `Gen 1` il modulo CN non è
   attivo in SmartCabinet"* — **if the only entry is `Gen 1`, the CN module is not licensed.** That
   governs everything else, and it is one look. Postprocessors are machine-branded (`Pendular` is offered
   *"per il postprocessor Biesse"*), so the selection also says whether a Vitap/TPA one exists.
2. **Whether a drilling-tool table appears for our CN configuration.** The cogwheel and its menu show
   *"solo quando vengono selezionate alcune particolari configurazioni cn"*. Its fields: `Tool` (from the
   CAM tools table), diameter, drilling **direction**, **`il tipo di foro che l'utensile dovrà
   praticare`**, and punta-or-fresa. ***Hypothesis, and labelled as one***: `tipo di foro` may be the
   blind/through distinction — **criterion 2** of the -27 checklist — declarable on the design side
   instead of discovered at the machine. *The manual does not give the field's values. Look at the dialog
   before acting on this.*
3. **Where the CN files go.** Subfolders under `\Kosmosoft\SmartCabinet\CNC\`, **named after the
   postprocessor in use**; `AutoCopyCNFolder` (Settings → CAM) takes a local **or network** path so files
   are written *"direttamente nel pc a bordo macchina"*; one file per piece, plus a `_DX` file per piece
   when Pendular is on; names settable under `CN Names`. **§1's long-open "dedicated Drive folder, not yet
   identified" now has three named things to look at instead of one vague one.** The owner's 2026-09-17
   correction about Drive still stands; this is the software's side of it.

**The trap.** CN configuration has **two scopes**: the `CAM` button edits the **default**, the `CN`
lightning button under `Settaggi cabinet` edits **the currently open cabinet only**. The manual advises
copying the in-use configuration and editing the copy. *Edit through the wrong button and you have
changed one cabinet, not the shop.* And on these parameters the manual defers to the machine maker —
*"è in ogni caso opportuno consultare il produttore della macchina"*. **Nothing here substitutes for
asking TPA/Vitap.**

## 4. §7 was carrying a mechanism known false for four days

**The 2026-09-23 correction landed in the Wiki, in `Wiki/index.md` and on the Tasks sheet — and not in
`CLAUDE-Workshop.md` §7.** Found today. Until this session §7 still said Blind Ø5 *"sits on bushes 6–10,
all at ID 0, so diameter + type resolution has five candidates and no tie-break — **which is the whole
fault**"*, and still pointed at `tpacad-blind-bore-tool-id-fix.md` as *"Full procedure"* — **an article
that has carried `status: superseded` and a DO-NOT-FOLLOW banner since 2026-09-23.**

**This was the worst-placed copy of the error in the KB**, because §0 sends every session to §7 before it
touches a machine or a task. Three passages fixed:

| Line | Was | Now |
|---|---|---|
| The T016 bullet | the ID-0 tie as "the whole fault"; `blind-bore-tool-id-fix` as "Full procedure" | error -27, the five criteria, the live-file finding, the owner decision; the superseded article named as **DO NOT FOLLOW** |
| The article inventory | *"Closing T016 (2026-09-19) — the two-step fix"* | T016's corrected root cause, with its predecessor marked superseded |
| The open-items list | *"needs a CN Tools 'Dia. 5mm' entry created on the SmartCabinet computer, exported and transferred"* | **struck through and withdrawn, wrong twice over** — and kept struck rather than deleted, because it stood there for eight days and someone may have started on it |

*The 2026-09-23 sweep checked `CLAUDE.md`, `README.md`, `CLAUDE-Lessons.md` and a Decisions article. It
did not check `CLAUDE-Workshop.md`, which is where §7 lives.*

## 5. A cell overwritten, and put back

Updating T016's Notes I **replaced** the cell rather than appending, dropping the 2026-09-23 diagnosis —
the five criteria, the −25 trap, the p.63 spindle warning, the Ø5 hypothesis — out of the live task.
Noticed on re-reading, and restored: the cell now carries **(A)** the corrected diagnosis and **(B)**
today's update, 3,978 characters against the 4,000 limit, read back from the API in full. *Nothing was
lost — the text was in this session, the Wiki and git — but a task note is the thing a person opens at
the machine, and for about a minute it was the only place that had stopped saying the five criteria.*

## 6. What was captured, and what was not

`Outputs/2026-09-27-smartcabinet-manual-capture-cn-chain.md`, 17,972 B: the extracted text of the four
CN/tool-chain pages — `cn`, `cnc`, `tabelle_cam_accessori_utensili`, `lavorazioni` — built **by script
from the stored HTML**, not retyped and **not a model's summary of the page**. That distinction is the
web version of §3's `read_file_content` lesson: the first pass at these pages was a fetch tool's
*rendering*, and re-reading the source turned up two passages it had dropped — the two-scope trap and
*"consultare il produttore della macchina"*.

All ten pages carry their **byte count and sha256 of the HTML as served** in the article's provenance
table, so a future session can re-fetch and see at once whether the vendor has changed a page. **The HTML
itself is not stored**: 230 KB of vendor markup that can be re-fetched at will, and the hash is what
makes re-fetching checkable. Six pages are cited without capture; if one starts to matter, re-fetch,
check the hash, capture it then.

## 7. Two predictions of mine that were wrong, recorded rather than dropped

- **`lavorazioni.html` is not a workings catalogue.** I named it as one of the pages most likely to
  settle the tool question. It is a two-item menu: *Intagli* and *Lavorazioni a Onda*.
- **`cam.html` holds no tool content** despite the filename — only *Configurazione CN* and *Configurazione
  Giunzioni*.

## 8. Left for its own pass

**Cabineo is a first-class joint in SmartCabinet.** `giunzioni.html` has *"Giunzioni eccentriche e
Cabineo"*, configured element by element: diameter and effective length per element, tool and passes for
the first two, the central screw's diameter with **different hole lengths for carcase, divider and
back**, and the support base's length, width and thickness. That bears directly on
`Wiki/Processes/carcase-fixings-cabineo-x-vs-confirmat.md` and on the 2026-09-23 finding that `CABINEO`
is native in TpaCAD. **Not worked today** — `giunzioni.html` is 62,404 B and deserves its own session.

**Back-links not added.** The new article names six related articles; those six do not yet name it. Adding
the lines means re-emitting ~80 KB to Drive for front matter, which is the trade `AWT-0089` is already
parked on. They ride the next push that changes each article's body, and `AWT-0089`'s row now says so.

## 9. Files touched

| File | What changed |
|---|---|
| `Wiki/Software/smartcabinet-online-manual.md` | **new**, 14,962 B — the map, the provenance table, the findings |
| `Outputs/2026-09-27-smartcabinet-manual-capture-cn-chain.md` | **new**, 17,972 B — captured text of the four CN/tool-chain pages |
| `CLAUDE-Workshop.md` | §7: three stale T016 passages corrected or withdrawn |
| `Wiki/index.md` | the new article, with what it settles and what it leaves open |
| Smartsheet `Tasks` `T016` (row `3054339713795972`) | Notes rewritten: corrected diagnosis restored **plus** today's update |
| `Outputs/kb-registers.md` + `kb-registers-snapshot-2026-09-27.md` | snapshotted at the ~25 KB rule, then today's rows added |
| `Outputs/change-log-index.md` | this session's row |

**Nothing was changed in SmartCabinet, and nothing was inferred from the manual without saying so.**
