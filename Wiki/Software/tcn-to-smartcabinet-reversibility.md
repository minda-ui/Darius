---
title: "Can a project be rebuilt in SmartCabinet from its `.TCN` files? — what a CN file carries, and what it discards"
category: Software
status: active
sensitive: false
created: 2026-09-29
updated: 2026-09-29
sources:
 - "`AMFA Wall Unit 600 RH/01-SIDE-LEFT.TCN` (Drive `1ZWciFvdK2rkKbeWvRpNQ825UWJsnnPe1`, 21,020 B) — re-fetched and decoded 2026-09-29, UTF-16LE, whole file read and its section skeleton enumerated by script"
 - "`AMFA Wall Unit 600 RH/03-BOTTOM.TCN` (Drive `1ygANqYNEfpT7-q7TNkfm-hhllShoZ62m`, 2,036 B) — same, and small enough to print in full"
 - "`./smartcabinet-online-manual.md` §2 (the page map) and §5 (the CN chain) — the vendor manual's own list of what SmartCabinet opens, saves and exports, captured 2026-09-27, `giunzioni.html` re-checked 2026-09-28"
 - "`../Processes/cabineo-joint-geometry-reconciled.md` — the 2026-09-28 decode of the same two files, which established the working counts this article re-confirms"
 - "Owner (Minda), 2026-09-29: *\"Is it possible from a set of .tcn files recreate project in SmartCabinet?\"*, then *\"write it up\"*"
related:
 - ../Software/smartcabinet-online-manual.md
 - ../Software/smartcabinet-and-production-workflow.md
 - ../Processes/cabineo-joint-geometry-reconciled.md
---

# Can a project be rebuilt in SmartCabinet from its `.TCN` files?

**No — not as a project. Yes — as a complete set of parts.** A `.TCN` is what SmartCabinet's
postprocessor *emitted* for one panel on one face. It is downstream, machine-specific and **lossy by
design**, in the way G-code is lossy about the CAD model it came from.

**The evidence for that is stronger than the analogy.** It is not merely that the assembly information is
missing: **the TCN format has named sections that could carry it, and SmartCabinet's postprocessor writes
every one of them empty.** `VAR`, `SPEC`, `OPTI`, `LINK` and `PREV` are present and blank in both of the
master unit's files. And the files are **not self-contained** — four workings on the side panel call an
external macro by relative path, `..\custom\mcr\fittingx.tmcr`, which lives on the machine's PC and is not
in the file.

*This article answers a live question rather than a theoretical one, and it answers it by decoding the
shop's own output. Nothing below is taken from another article's description of these files.*

## 1. What a CN file carries

Both files have an identical skeleton. `03-BOTTOM.TCN` is small enough to show whole in outline:

```
TPA\ALBATROS\EDICAD\01.00:194:r0w0h0
$=SmartCabinet
::UNm DL=600.0 DH=300.0 DS=19.0 OX=0 OY=0 OZ=0
GEO{ ::NF=0 }GEO
OFFS{  #0=0.0|0 … #7=0|0  }OFFS
VARV{  #0=0.0|0 … #7=0.0|0  }VARV
VAR{ }VAR   SPEC{ }SPEC   OPTI{ }OPTI   LINK{ }LINK   PREV{ }PREV
SIDE#1{
  $=sopra
  ::LF=600.0 HF=300.0 SF=19.0
  W#81{ ::WTp #1002=5 #1=11.9 #2=230.0 #3=-12.0 … #1001=0 }W
  … 7 bores in all …
}SIDE
SIDE#2{ }SIDE … SIDE#6{ }SIDE
```

| What you get | Where |
|---|---|
| The **blank**: length, height, thickness | `::UNm DL= DH= DS=` |
| Origin offsets | `OX= OY= OZ=` — zero in both files |
| Which **face** is machined, and its own dimensions | `SIDE#1` … `SIDE#6`, `::LF= HF= SF=` |
| **Every operation, exactly** — bores, pockets, profiles, arcs, lines, depths, diameters, tool fields | the `W#…` workings |

**Only `SIDE#1` carries anything** in either file; `SIDE#2`–`#6` are present and empty. Working counts
re-confirmed against the 2026-09-28 decode: **127 in the side, 7 in the bottom.**

**`$=sopra` names the machined face, not the part** — `03-BOTTOM.TCN` says `sopra` ("above") too. *The trap
is one character wide and is recorded here as well as in the reconciliation article, because this is the
file a future session will read first when asking what a TCN contains.*

## 2. What it does not carry — and the format has the slots

**This is the finding.** TpaCAD's own format defines sections for variables, specifications, optimisation
and linking. In both of the shop's files:

```
GEO{ ::NF=0 }GEO      <- geometry: NF=0, nothing
OFFS{ … }OFFS         <- eight offsets, every one 0.0
VARV{ … }VARV         <- eight variables, every one 0.0
VAR{ }VAR             <- empty
SPEC{ }SPEC           <- empty
OPTI{ }OPTI           <- empty
LINK{ }LINK           <- empty
PREV{ }PREV           <- empty
```

**The postprocessor is not omitting the cabinet because the format cannot hold it. It discards it because a
boring machine does not need it.** *That distinction matters: an empty `LINK{}` is a deliberate silence, not
a format limitation, and it is why no amount of cleverness recovers the project from the file.*

**`$=SmartCabinet` is the entire provenance record.** It names the *program*. Not the project, not the
cabinet, not the job, not the customer, not the date.

**Absent, therefore, and not recoverable from a TCN:**

| Missing | Why it matters on a rebuild |
|---|---|
| Cabinet / unit identity and the job it belonged to | nothing ties a set of files to a unit except the folder they sit in |
| **Assembly relationships** | no file says *this side meets that bottom* |
| Material | no board product, no decor, no supplier — only a thickness |
| Edging | nothing at all; the cut size **is** the finished size in this shop, which is recorded elsewhere, not here |
| **Joint semantics** | the pocket geometry is present; *"Cabineo, structure, hole length 12.0"* is not — that lives in SmartCabinet's `giunzioni` configuration |
| Hardware products | a hinge pilot pattern is visible; the hinge is not named |
| Door and drawer configuration | absent |
| Parametric intent | a TCN holds one size, not the rule that generated it |

**Even the part name is convention, not data.** `01-SIDE-LEFT` and `03-BOTTOM` are filenames, and the
manual records that piece and file names are **settable under Settings → `CN Names`** (§5 of
`./smartcabinet-online-manual.md`). *A different shop's export of the same cabinet would name the same
panels differently.*

## 3. The files are not even self-contained

Four of the side panel's 127 workings are macro calls, all four to the same macro:

```
W#1001{ ::WT2 WS=2 W$=foro mul #8098=..\custom\mcr\fittingx.tmcr #6=1 #9505=0
        #8508=0 #8509=0 #8510=676.2 #8511=484.2 #8512=32.0 #8513=-12.0
        #8515=1 #8517=0 #8518=84.0 #8520=1 #8522=5.0 #8525=0 }W
```

**`#8098` is a relative path to a TpaCAD macro file on the machine's PC.** The TCN passes parameters to
`fittingx.tmcr`; it does not contain it. **So a set of `.tcn` files alone does not fully reproduce even the
*machining*** — it reproduces it only on a machine whose `custom\mcr\` folder holds that macro.

*Two coordinate-looking pairs appear across the four calls — `676.2, 484.2` twice and `382.6, 190.6`
twice — distinguished by `#8518` taking `84.0` or `191.0`. **What the macro actually does is not
established**, and `foro mul` is translated as "multiple hole" by me from the Italian, with `mul` read as an
abbreviation. Both are open (§6).*

## 4. Is there an import at all?

**Nothing documented.** The manual's page map (§2 of `./smartcabinet-online-manual.md`) lists as inbound
operations only `nuovo` (new) and `apri` (open — a SmartCabinet project), and as **outputs**:

> `export_csv` · `export_viste_dxf` · `export_obj` · `stampe` prints · `visualizzatore` viewer ·
> `esplodi` exploded views

**No TCN, TpaCAD or ISO import. No import of anything.** The CN chain runs one way through a
**machine-specific postprocessor**, and the manual is explicit that it is **one CN file per piece**.

***That is not proof, and this article will not overstate it.*** §1 of `./smartcabinet-online-manual.md`
records that the manual's hub is **not a complete index** — five pages and sixteen sub-pages exist that it
does not list — and states in as many words that **a menu absence is not evidence that something is
undocumented**. *So: nothing documented, and the question is closed properly by one look at the File menu of
the shop's own install, not by another pass over the manual.*

*Note a near-miss worth not confusing: **TpaCAD** has DXF import on its basic licence. That is the
machine-side program, not SmartCabinet.*

## 5. What the files are genuinely good for

**This is not a negative article.** A complete set of `.tcn` files is a valuable thing to hold:

1. **Re-cut any panel exactly, with no CAD involved.** TCN is TpaCAD's **native** format — open the file on
   the machine's control PC and run it. A damaged part is remade from its own file.
2. **Recover every dimension and every operation**, to the tenth of a millimetre.
3. **Infer the carcase** when you hold the full set for one unit. Side `862 × 300 × 19` plus bottom
   `600 × 300 × 19` gives a 600-wide, 862-high, 300-deep cabinet. *That is an inference from matching
   dimensions rather than a statement in the files, but a sound one.*
4. **Reverse-engineer detail this KB did not have.** Two of these files yielded the full Cabineo pocket
   geometry, the four blind Ø3 hinge-plate pilots per side, and a 45.0 × 18.9 × 2.1 recess no earlier decode
   had recorded — see `../Processes/cabineo-joint-geometry-reconciled.md`.

## 6. What a rebuild actually costs, and which case you are in

To get a **SmartCabinet project**, the unit is rebuilt by hand — dimensions and shape, material from
`registro-materiali`, edging, the joint family and its `giunzioni` parameters, hardware from the
`tabelle_cam_accessori_*` tables, doors and drawers, naming — **using the `.tcn` files as an accurate
dimensioned reference.** Realistic, and it ends with a *parametric* unit that can be resized, which the
files never give you. **The files cannot shortcut it; they can make it accurate.**

| If the situation is | Then |
|---|---|
| a panel was damaged or mis-cut | **re-run its TCN on the machine.** SmartCabinet is not involved |
| the SmartCabinet project is lost | **rebuild the unit by hand**, TCNs as the dimensioned reference. Parts stay cuttable throughout, so production is not blocked while you do it |
| someone sent `.tcn` files for a unit you want in the library | **same rebuild** — there is no import path to try first |

## 7. One incidental finding

**Drive returns these files with `mimeType: audio/mpeg`** — both of them, on both fetches. Harmless for
reading, and the bytes come back correctly, but **Drive mis-types `.TCN`**, which matters to anything that
branches on that field. *Recorded because §4 of the charter treats binary and Google-native types as outside
what has been proven for in-place writes, and a text file reported as audio is exactly the kind of thing that
makes such a rule fire on the wrong file.*

## 8. Open questions

1. **Does the shop's SmartCabinet install offer any import?** One look at its File menu. §4 gives the
   documented answer and its limit.
2. **What `fittingx.tmcr` does**, and what `#8510`–`#8525` mean to it. *Closeable from the machine PC —
   the macro is a file in `custom\mcr\`, and `Workings_eng.pdf` in `C:\Albatros\help\en-GB\` documents the
   parameter numbering.*
3. **Whether `foro mul` is "multiple hole"** — a translation of mine, with `mul` read as an abbreviation.
4. **Whether the empty `LINK{}` is always empty**, or whether some postprocessor configuration fills it.
   *Two files from one unit is the whole sample.* If it can be populated, the honest answer to this article's
   title would need revisiting — which is why it is written down rather than assumed settled.

## Sources

Listed in the front matter. **Both `.TCN` files were re-fetched from Drive and decoded for this article**,
and the section skeletons enumerated by script rather than read by eye; the working counts agree with the
independent 2026-09-28 decode.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-29 | Created on the owner's question. Records the CN file's contents, the **five empty metadata sections**, the **external `.tmcr` macro dependency**, the documented absence of any SmartCabinet import and the limit on that claim, what the files *are* good for, and the rebuild cost by case | Session 24, `change-log-2026-09-29-charter-v35-limit-3-to-1mb.md` |
