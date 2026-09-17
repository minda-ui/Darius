# CLAUDE.md — Workshop of Furniture Making Knowledge Base

**Version 9 — 2026-09-17.** Structure and conventions modelled on the Fishbone Commercial
Properties Ltd Knowledge Base, via the shared `Wiki/Process-Fishbone-Systems-House-Rules.md`
conventions used across all Fishbone group KBs. This file holds only what's specific to this KB,
and it is also **Darius's charter** (see §0a). README.md is a pointer; this file wins on conflict.

**Changed in v9 — the networking claim corrected.** §1 stated since the KB's early sessions that the
design computer and the CNC control PC were **not** networked and that files moved by USB. The owner
corrected this on 2026-09-17: the workshop runs on a network served from an on-site server rack, a
WiFi 7 access point covers the whole floor, and **files are shared through Google Drive in a dedicated
folder**. The claim had no citation and no `[confirm]` marker, so nothing flagged it as inferred and it
survived six versions — see the new lesson in §3. Corrected here, with the downstream articles swept in
the same session. v8 (`1teaQsa5DRuZGbtvSSSRjmpAo6p6Uu0Gp`) is archived.

**Changed in v8 — fork reconciliation + owner assigned.** Two parallel session-lines on 2026-09-15/16
had each rewritten this file (and `Wiki/index.md` and `Outputs/kb-registers.md`) without seeing the
other: an *operational-systems* line (v5 — maintenance, troubleshooting, the SmartCabinet workflow,
the Maintenance Schedule + Fault Log sheets) and a *CAD-day* line (v7 — the SmartCabinet Wall Support
Cam Table reference and the refined TpaCAD tool-ambiguity fix). No content was lost — every dated
change-log file survived; only these three index files had split. v8 **unions both lines** into one
clean control layer and renumbers the sessions into a single timeline. Both prior `CLAUDE.md` copies
(v5 `1My3wCRZXG_sc8l_EY0zgfAUrJ8mbfQKl`, v7 `1zAIAKCoFufSqHCPVaL-tNlFsXlng12ZP`) are archived. At the
same time the KB gained a named owner — **Darius** — so this fork stops happening (one owner, one seat).

## 0a. Who owns this KB — Darius

**Darius** is the Fishbone Group's **fifth AI employee** and the **named owner of this Knowledge Base**:
the Workshop Operations Assistant. Everything in this KB is Darius's patch — the machinery, the
maintenance and fault systems, the SmartCabinet/CAD and TpaCAD knowledge, and the
design→production→Sales tracker. Owner-authorised (Minda) 2026-09-16; coordinated by **Victoria**
(CEO's Assistant, Fishbone Group). Git mirror **`minda-ui/Darius`**; connectors **Google Drive +
Smartsheet + Web (read)** — no Gmail (Darius logs and tracks, it does not send).

**Reach.** Darius **reads** its own KB and the estate it needs (the AMFA Furniture Ltd and Fishbone
Construction Ltd KBs — the asset-ownership question, §7); **writes, unattended,** its own KB and its
own Workshop Smartsheet sheets (Machinery Register, Document Register, Tasks, Safety Check Log,
Maintenance Schedule, Fault Log); and **needs a human** for everything in §6a — appending to the
shared group Document Register (confirmed access only), committing AMFA or Construction to any
purchase/contract/payment, replying to a supplier/insurer/inspector, filing with any regulator, or
touching another KB. The boundaries were already written into this KB's §6a; Darius just puts a name
to them. When two facts that should agree don't, Darius records the contradiction and asks — it never
guesses one into the other (§3).

## 0. Start every session here

Before doing anything — including a one-off question — read, in order:
1. The newest entries in `Outputs/change-log-*.md` (newest-first index: `Outputs/kb-registers.md`,
   section "Change-log entries").
2. The `pending` and `partial` rows of `Outputs/kb-registers.md`, section "Processed items".
3. `Wiki/index.md` for what's already known.

**Re-read the live control files immediately before editing them** (their current Drive id and size),
and author the edit onto that live copy — never a copy read earlier in the session. The 2026-09-15/16
fork happened because two sessions edited stale copies in parallel; with a single owner this is
avoided, but the discipline stands.

This KB shares a parent company (AMFA Furniture Ltd) with a separate, company-wide KB. If a fact
could be recorded in either, check the AMFA Furniture Ltd KB rather than assuming this one is silent
on it, and cite across rather than duplicate. **This matters concretely**: every asset registered so
far (`FA2301`–`FA2305`) was invoiced to Fishbone Drylining Limited (now Fishbone Construction Ltd),
not to AMFA Furniture Ltd — the AMFA KB may hold the intercompany side of this that this KB doesn't
have standing to resolve on its own. See §7.

## 1. Database structure

**Scope.** This KB covers the **machinery and equipment in the AMFA Furniture Ltd workshop** and,
from 2026-09-15, the **operational systems** for running it (maintenance, troubleshooting, the
SmartCabinet design-to-machine workflow) — not the company as a whole. This **includes the software**
used to design and program the machines' work: both the machine-side programming software (TpaCAD,
driving the Vitap) and the design-side CAD software (SmartCabinet, producing the job files TpaCAD
consumes). See the Decisions articles for why it's a separate KB and why the scope was extended.

**Two computers, one network.** The shop runs SmartCabinet on a design/office computer; the CNC
machine's own control PC runs TpaCAD/WSCM/Albatros. **They are networked** — the workshop runs on a
network served from an on-site server rack, with a **WiFi 7** access point covering the whole workshop
floor, and **files are shared between design and machines through Google Drive, in a dedicated
folder** (that folder not yet identified or examined — see §7). *Corrected 2026-09-17 by the owner;
v8 and earlier asserted the opposite.*

**Still open, and not to be assumed either way:** a shared network does not merge two programs'
internal catalogs. SmartCabinet's **CAM Tools** table and TpaCAD's **CN Tools** catalog are separate
application databases, and whether an entry added in one reaches the other automatically is
**unverified**. This bears directly on Task T016 and must be checked, not inferred from the fact of a
network.

**Where it lives.** Google Drive, folder `Workshop of Furniture Making - Knowledge Base`, primary
copy (`1ykYJERaptUNH0FDvkOVU26jh_x_hRtLz`). Git mirror `minda-ui/Darius` (seeded 2026-09-16); Drive
stays the source of truth, the mirror is kept in step.

**Folders.**
```
Workshop of Furniture Making - Knowledge Base/
├── CLAUDE.md, README.md
├── Raw/ — inbox; nothing stays here once filed elsewhere
├── Wiki/
│ ├── index.md, _templates/article.md
│ ├── Machinery/ — one article per machine or machine group
│ ├── Suppliers/ — manufacturers, dealers, service/calibration engineers
│ ├── People/ — operators, responsible/competent persons
│ ├── Finance/ — purchase cost, depreciation, insurance, HP/loan finance
│ ├── Processes/ — maintenance schedules, safety/PUWER compliance, training, and
│ │ design/programming-software behaviour & reference (TpaCAD, SmartCabinet)
│ ├── Troubleshooting/ — per-machine fault references + the fault-log system
│ ├── Software/ — SmartCabinet and the design→machine production workflow
│ └── Decisions/ — why this KB is shaped this way; numbers must be recounted, not trusted
├── Outputs/
│ ├── kb-registers.md, change-log-YYYY-MM-DD-<slug>.md
│ └── Correspondence/ — filed copy of every numbered document in scope
└── Archive/ — superseded files, renamed with reason and date
```
No `Properties`/`Tenants`/`Contracts` folders: not applicable to this KB's scope.

**Live data sources.** Smartsheet workspace `Workshop`, one sheet of each after the 2026-09-15
duplicate cleanup: **Machinery Register - Database** (`1754351980906372`, `FA2301`–`FA2305`),
**Document Register** (`838802392352644`), **Tasks** (`4087584374523780`), **Safety Check Log**
(`913380204480388`, F45 monthly safety check), **Maintenance Schedule** (`6753985971226500`, all
recurring maintenance tasks, RYGB by due date) and **Fault Log** (`414932606781316`, faults & fixes,
RYGB by status). These sheets, not any Wiki article, are the live source for current status/dates;
Wiki articles narrate and cite them. The Vitap's own §6.8 check is **not** yet added to the Safety
Check Log — see §7 (Task T013).

**Register conventions.** Per group document-numbering policy v1.3: `FA` prefix (Amfa Furniture),
7-digit document numbers on the shared group register (not yet used by this KB — see below), 4-digit
property/asset codes self-assigned locally as `FA` + 2-digit year + 2-digit sequence.

**Assigned so far**: `FA2301` (Hebrock F4, corrected 2026-09-15 from a wrongly-assumed `FA2601`),
`FA2302` (Inventair MK1 MTFA extractor, status under review — possibly superseded, Task T014),
`FA2303` (Altendorf F45), `FA2304` (Vitap K2-2.0), `FA2305` (Inventair MK2 MTFA — acquisition year
confirmed from invoice 100154 before assigning the code, same discipline applied since the `FA2601`
mistake).

**Correspondence/documents** (invoices, manuals, certificates) are registered on the **shared group
Document Register** under AMFA Furniture Ltd's `FA` prefix, not a locally invented one — **appending
to that shared register is a deliberate, confirmed-access action, not a routine one** (none exercised
yet; candidate documents are logged locally with `Document No.` = `pending`).

**Housekeeping finding, not yet actioned:** a duplicate copy of the Vitap manual and F45 spare-parts
manual PDFs was found in a Drive folder (`1qF7XiS2Jud3y8V6lf4Nyu7_JAMEJNsai`) that is **not** a child
of this KB's folder tree — outside this KB's own `Raw/` (`18P2Gz64tjp0G74JzhzVE6i0LqxhcJB0R`). Not
touched; flagged for the owner in case it's an accidental duplicate upload elsewhere in Drive.

**Open flag for the owner, not resolved here:** AMFA Furniture Ltd's own Property Register uses
`AMF`+digits for property codes, not `FA`+digits — a different asset class, doesn't force this KB to
match, but worth the owner's attention if compared side by side.

## 2. Wiki maintenance guidelines

Front matter, citation, linking and stub rules: `Wiki/Process-Fishbone-Systems-House-Rules.md`
(Fishbone Group KB) and this KB's own `Wiki/_templates/article.md`.

## 3. Workflow for processing new items

Group workflow (Detect → Register → Read → Extract → Update → Check → Log → Output → Commit).
Lessons from Sessions 2–12, all on real incidents rather than invented ahead of time:
- For a multi-part scanned manual, extract via background sub-tasks (split across parallel agents
  for large sets, e.g. 8 parts as two 4-part agents) rather than reading everything inline; flag
  illegible/OCR'd figures and cross-part inconsistencies explicitly rather than silently picking one
  reading.
- **A fact stated with an explicit assumption must be revisited the moment real evidence arrives**,
  even if that means renumbering something already assigned (`FA2601`→`FA2301`) — and conversely,
  **ask for the evidence up front when a session's own numbering scheme depends on it** (asset
  acquisition year), rather than assuming and correcting later.
- A genuine compliance/regulatory finding (expired certificates, a mandatory documented check)
  should be surfaced prominently — in Key facts, not just Open questions — and given its own Task
  and, if it's a recurring process, its own `Wiki/Processes/` article and tracking sheet.
- **Manual-derived maintenance schedules and fault tables belong in the operational systems**
  (`Wiki/Processes/maintenance-schedule-*.md` + the Maintenance Schedule sheet;
  `Wiki/Troubleshooting/troubleshooting-*.md` + the Fault Log), not only inside the Machinery
  article. When a fix or diagnosis differs from the manual in practice, record that lesson in the
  troubleshooting article (the corner-rounding incident is the first example).
- **Two similarly-worded manual sections are not necessarily the same requirement.** The Vitap's §6.8
  "Safety Device Efficiency Check" looks, by name, like the F45's mandatory monthly check — but its
  text describes a pre-automatic-mode functional test with no stated interval or "log this"
  instruction. Don't extend a Processes article or a Smartsheet log to a new machine on
  name-similarity alone (Task T013).
- Don't assume one finding resolves another just because they're related — e.g. a new centralised
  extraction unit plausibly supersedes an older single-machine extractor, but that's a task to
  confirm, not a status to assert (still open for `FA2302`/`FA2305`, Task T014).
- **A formula validated on one invoice becomes evidence for others once repeated.** The 70%-balance
  cross-check was confirmed independently on invoices 100153, 100154 and 100155 — a third clean match
  closes the underlying question generally, not just for the invoice it was first raised on.
- **A manual that says "generic" or "extract" at the top means exactly that — check what it defers to
  before treating its silence on a topic as an answer.** The TPA CAD manual named three sibling
  manuals it doesn't include (`Workings.pdf`, `DxfCAD.pdf`, `DxfToTPA.pdf`) and said the copy given
  wasn't complete. Its silence on "Outfit Parameters"/"CN Tools"/"Solve" wasn't evidence those don't
  exist — it was evidence to go find the un-supplied files (Task T015).
- **A live shop-floor fault is worth documenting even mid-resolution.** The TpaCAD tool-ambiguity
  incident was written up with "workaround in place, permanent fix identified but not tried", then
  refined a second session, without ever being marked resolved prematurely (Task T016).
- **Two data points that should agree but don't are a live contradiction to record, not to silently
  resolve.** The SmartCabinet Wall Support session found two "measured from the back edge" hole
  positions needing opposite X signs; both were documented as actually used, with the disagreement
  itself flagged as the open question rather than guessing which is wrong (Task T017).
- **A fact recorded without a source hardens into an assumption nobody revisits.** The "two computers,
  not networked" claim sat in §1 through six versions, was repeated into the Vitap/TpaCAD/SmartCabinet
  articles, and shaped real advice (a whole barcode-system design was built around an air gap that does
  not exist) before the owner corrected it on 2026-09-17. It carried no citation and no `[confirm]`
  marker, so nothing ever flagged it as inferred. **Infrastructure and environment facts get a source or
  a marker, exactly like a figure off an invoice.**
- **Don't run two sessions on this KB at once, and re-read the live index/registers before recreating
  a control file.** The 2026-09-15/16 fork (this file, `index.md`, `kb-registers.md` all split across
  two parallel lines) is the reason Darius now owns the KB as a single seat.

## 4. Change log

One file per session in `Outputs/`, named `change-log-YYYY-MM-DD-<slug>.md`, indexed newest-first in
`Outputs/kb-registers.md`. Never a single growing `CHANGELOG.md`.

## 5. Automated processes

None are live. The Maintenance Schedule / Safety Check Log / Fault Log RYGB `Health` columns are
self-updating **column formulas** (maintain via the connector, not by hand) — but there is no routine
that reads them and chases due dates yet; that's a future proposal, and a natural early candidate for
one of Darius's own scheduled routines.

## 6. Governance

**6a — never do unattended:** never file with Companies House/HMRC/any regulator; never commit AMFA
Furniture Ltd or Fishbone Construction Ltd to a purchase/contract/payment (incl. spares, service
visits, the electrician's PTC check); never reply on either company's behalf to a supplier/insurer/
inspector/manufacturer; never edit or delete a row on the shared group Document Register (append-only,
in-scope documents only, and only once write access is confirmed — not yet done); never touch AMFA
Furniture Ltd's own KB/Property Register/Document Register from this KB; never hold, type or request a
secret/credential. Appending to the Workshop workspace's own sheets (Machinery Register, Document
Register, Tasks, Maintenance Schedule, Fault Log, Safety Check Log) and creating Wiki articles here is
normal KB work and allowed. Deleting whole Smartsheet sheets is a UI action the owner takes (the
connector has no delete-sheet tool); the 2026-09-15 duplicate cleanup was done that way.
**6b — access review:** 2026-09-14, initial setup — Drive KB and Smartsheet workspace created by the
owner (minda@fishboneconstruction.co.uk); no other access granted. Shared group Document Register
write access still not confirmed. 2026-09-16: git mirror `minda-ui/Darius` created (owner) + seeded.
**6c — revisit cadence:** none set yet.

## 7. Workshop snapshot and open questions

**Location:** Unit 32, Point Pleasant Industrial Estate, Wallsend NE28 6HA.

**Machines registered:**
- `FA2301` — Hebrock F4 edge banding machine, Serial F3809. CE-compliant. Corner-rounding fault
  (stop-screw misadjustment) resolved (FL-001). Maintenance schedule (MT-001…014) + troubleshooting
  reference built. See `Wiki/Machinery/hebrock-f4-next-edge-bander.md`.
- `FA2302` — Inventair MK1 MTFA dust/fume extractor. Status under review — likely superseded by
  `FA2305` (Task T014, not confirmed). No manual yet; not in the maintenance system.
- `FA2303` — Altendorf F45 ElmoDrive CNC sliding-table saw. **Safety certificates expired 22.02.2024
  — unresolved compliance gap, Task T007.** Mandatory monthly documented safety check required (Task
  T008, not yet performed). Maintenance schedule (MT-020…028) + troubleshooting reference built. See
  `Wiki/Machinery/altendorf-f45-panel-saw.md` and `Wiki/Processes/f45-monthly-safety-device-check.md`.
- `FA2304` — Vitap K2-2.0 CNC boring/drilling/routing centre. No real serial/manufacture year in the
  manual (invoice serial 320070 AT used; confirm against the type plate, Task T012). **Open incident:**
  TpaCAD "Tool for this working not found" on Blind bore drill operations — root cause refined (fix
  likely lives in the operation's own Tool [T] field referencing a real CN Tools catalog entry, not
  the outfit's per-bush ID), not yet tested end-to-end (Task T016). Maintenance schedule (MT-030…036)
  + troubleshooting reference built. See `Wiki/Machinery/vitap-k2-panel-saw.md`,
  `Wiki/Processes/tpacad-tool-type-optimizer-ambiguity.md`.
- `FA2305` — Inventair MK2 MTFA dust/fume extractor, bought alongside `FA2304` on invoice 100154. No
  manual yet ("will follow later" per the owner) — registered in the Machinery Register only, no Wiki
  article; can't join the maintenance/troubleshooting systems until a manual arrives. May supersede
  `FA2302` (Task T014).

**Operational systems (built 2026-09-15):**
- **Maintenance** — `Wiki/Processes/machinery-maintenance-system.md` + the Maintenance Schedule sheet
  (30 tasks: FA2301 MT-001…014, FA2303 MT-020…028, FA2304 MT-030…036) + three per-machine schedule
  articles.
- **Troubleshooting** — `Wiki/Troubleshooting/troubleshooting-and-fault-log-system.md` + the Fault Log
  sheet (FL-001 = resolved Hebrock corner-rounding fault) + three per-machine references (Hebrock
  §8.2; F45 mechanical + ElmoDrive error codes; Vitap §7.8).
- **SmartCabinet & production workflow** — `Wiki/Software/smartcabinet-and-production-workflow.md`
  (**draft**): the order-to-delivery process from the BP-scheme map, and how SmartCabinet (design +
  3D visuals + CRM) drives the machines. Product specifics flagged `[confirm]`. **This is the seed for
  Darius's first job — the design→production→Sales processes + tracker.**
- **SmartCabinet CAD reference** — `Wiki/Processes/smartcabinet-wall-support-cam-table-reference.md`:
  how to add hardware to SmartCabinet's Wall Support library, full column reference, two worked
  examples that exposed the X-sign discrepancy (Task T017).

**Open questions / tasks:**
- **SmartCabinet product specifics** — *partly resolved 2026-09-17.* **Vendor and product confirmed:**
  **SmartCABINET**, by **Kosmosoft Engineering S.r.l.** (Bagnolo San Vito, Italy), described as
  "CRM/CAD/CAM/ERP software for cabinet making"; offer/contract **22910**, 10/09/2026, **€1,000, paid**,
  registered `FCD0000024` in the *Construction* Document Register — **billed to Fishbone Drylining Ltd,
  not AMFA Furniture Ltd**, the same pattern as every machine (evidence for Task T004). Cited from the
  Fishbone Construction KB, `Wiki/Suppliers/kosmosoft-smartcabinet.md` — not duplicated here, and that
  KB is read-only to this one. **Outputs confirmed** from the release notes and the owner's screens:
  `.TCN` post (Vitap), custom CSV export splittable by material, real-shape nesting, ZPL barcode label
  printing, Panel Optimization with an offcut/cutout library. **Still `[confirm]`:** which version is
  actually *installed* (release notes list 3.2.0.9 of 07/07/2026 as newest released); whether the
  Hebrock gets any file at all; where CRM/customer data lives (cite, never copy client data).
- **SmartCabinet Wall Support hardware X-sign discrepancy** — two items both "measured from the back
  edge" needed opposite X signs (−15 vs +5); needs visual confirmation in SmartCabinet's own preview
  on a real job (Task T017).
- **TpaCAD Blind-bore-drill tool-ambiguity fix** refined but not fully tested — likely needs a real CN
  Tools "Dia. 5mm" entry created on the SmartCabinet computer, exported and transferred, then
  referenced in the failing operation's Tool [T] field (Task T016). **TpaCAD complete manual /
  `Workings.pdf`** not yet obtained — likely on the shop's Albatros PC at `Albatros\Help\` (Task T015).
- **The shared Google Drive job folder** — the dedicated folder through which SmartCabinet and the
  machines exchange files is not yet identified or examined. Its structure and naming convention
  constrain any barcode/tracking ID scheme, and it may hold customer data from SmartCABINET's CRM
  side (**cite, never copy client data**).
- **Does `FA2303` (F45) accept a digital cut list?** The ElmoDrive is a *positioning* control — rip
  fence, blade height, tilt, scorer, crosscut-fence angle, with tool management and per-axis
  calibration. Across all three F45 documents **no cut-list or job-file import is documented**, and the
  only data interface that appears is a USB drive, for firmware updates (`E21`/`E22`) and
  remote-maintenance files (`E23`). An "optimisation limit" error in the `E01`–`E15` block hints at some
  optimisation function on the control, but that block's OCR pairing was never reconstructed. **Working
  answer: the saw takes dimensions, not cut lists** — confirm against the ElmoDrive's own menus before
  recording it as fact.
- **Does SmartCABINET's own ERP module already do production tracking?** The vendor describes it as
  "CRM/CAD/CAM/ERP" (Fishbone Construction KB, `Wiki/Suppliers/kosmosoft-smartcabinet.md`). Building a
  parallel tracker without knowing what the purchased software already does risks duplicating it.
  Owner has chosen Smartsheet as the tracking layer regardless (2026-09-17); this remains worth
  establishing so the two don't fight.
- **Who legally owns `FA2301`–`FA2305`?** All invoiced to Fishbone Drylining Limited (now Fishbone
  Construction Ltd), not AMFA Furniture Ltd (Task T004).
- **`FA2303`'s expired safety certificates** — check with Altendorf/supplier (Task T007);
  **first F45 monthly safety check not yet logged** (Task T008); **`FA2303` serial/supplier
  unconfirmed** (Task T009); **`FA2303` annual PTC electrician check** needs scheduling (Task T011;
  Maintenance Schedule MT-025).
- **`FA2302`/`FA2305` relationship and extraction sizing for `FA2304`** — not confirmed; the Vitap
  alone needs ~2000 m³/h (Task T014).
- **Vitap `FA2304` §6.8 safety check** — does it need a dated, logged record like the F45's, or is a
  pre-cycle functional test enough? Owner decision (Task T013); MT-036 holds the place meanwhile.
- **`FA2304` serial/manufacture year** — confirm invoice-derived Serial 320070 AT against the type
  plate (Task T012).
- Full inventory of remaining workshop machinery beyond these five — advanced by the Vitap/Inventair
  MK2 additions; not necessarily complete.
- `AMF` vs `FA` property/asset-code inconsistency in AMFA's own Property Register — still just flagged.
- ~~Exact price on the Hebrock invoice unconfirmed~~ — **resolved 2026-09-15** by the 70%-balance
  cross-check confirmed on three invoices (Task T005, closed Done).
- A duplicate copy of two manuals was found outside this KB's own Drive folder tree — see §1.
