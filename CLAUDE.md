# CLAUDE.md — Workshop of Furniture Making Knowledge Base

**Version 12 — 2026-09-17.** Structure and conventions modelled on the Fishbone Commercial
Properties Ltd Knowledge Base, via the shared `Wiki/Process-Fishbone-Systems-House-Rules.md`
conventions used across all Fishbone group KBs. This file holds only what's specific to this KB,
and it is also **Darius's charter** (see §0a). README.md is a pointer; this file wins on conflict.

**Changed in v12 — a claim in this file was not true, and the reason it can't be made true.** §1 has
said since 2026-09-16 that the git mirror "is kept in step" with Drive. **It is not.** The mirror holds
this charter, `README.md`, `Wiki/index.md`, `Outputs/`, and the four Wiki articles written on
2026-09-17 — **not** the other fifteen Wiki articles, which exist on Drive only. Found while trying to
close that gap, and corrected here rather than left as the fourth unsourced claim of the day.

**And the gap cannot be closed by copying.** The Drive connector's read tool returns a *re-formatted*
rendering — punctuation escaped, hard-break spaces appended — not the bytes on disk. Reconstructing a
2 KB article from it landed **4 bytes out**, and the error is silent. Copying fifteen articles that way
would produce a mirror that looks right and differs from the source in ways nobody would notice, which
is worse than a mirror that is honestly incomplete. **So the mirror stays partial and says so**, and
the same finding rules out rewriting the three machinery articles just to add `related:` back-links —
a metadata fix is not worth re-authoring 75 KB of text through a lossy read. Both are recorded as debt
in §7. Also new in §3: *verify like with like* — a byte count is not a character count.
v11 (`1edazoWoadKnX-pz2vy-bEE0lCCOd1Gga`) is archived.

**Changed in v11 — the register caught up with the shop floor.** The third session-block of the same
day, after the owner walked the workshop photographing each machine as its asset label went on. Five
labels mapped (`0017`-`0021`); **both Inventair extractors sold** (`FA2302`, `FA2305`), which answers
the supersession question T014 had carried since Session 8 — by replacing both with one centralised
unit; **`FA2402` registered** (AES SAF 10,000 STK) with its acquisition year evidenced from invoice
22473 first and its full specification sourced from the vendor's quotation afterwards; and an **ABAC
screw compressor discovered that was never on the register at all** — the machine that feeds the
pneumatics of all three production machines. **No code was assigned to it**, because its plate carries
a *manufacture* year and this KB's convention needs an *acquisition* year: the `FA2601` lesson, applied
for the third time in one day. Unit 30's postcode confirmed (NE28 6HA), the `[confirm]` dropped. New
§3 lesson: *a register only contains what somebody thought to put in it.*
v10 (`1l4lgxmy5LJNdQQnTPIVVSC0YbY7mbcf4`) is archived.

**Changed in v10 — the workshop is at Unit 31, not Unit 32.** The second documented-fact correction of
the same day. §7 had recorded the workshop at **Unit 32** since the KB's first session. The owner corrected
it on 2026-09-17: **Unit 32 is no longer held.** The **workshop is Unit 31**; **office and warehouse are
Unit 30**. Evidenced by the lease cover page — *Forth England Limited* (landlord) and *Furniture by
Fishbone Limited* (tenant), **dated 25 June 2026**, for **Unit 31, Point Pleasant Industrial Estate,
Wallsend, Tyne and Wear NE28 6HA**. All six Machinery Register rows were corrected to Unit 31 and the three
machinery articles swept. **This also means the machines were physically moved**, which the KB had no record
of at all — see the re-commissioning question in §7. v9 (`1STw2KS1Ny7GKeDRMC_UbLxZtkjPtCr8z`) is archived.

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
on it, and cite across rather than duplicate. **This matters concretely**: every machine registered
here — `FA2301`–`FA2305` and `FA2402` — was invoiced to Fishbone Drylining Limited (now Fishbone
Construction Ltd), not to AMFA Furniture Ltd, and so was the SmartCABINET software. `FA2401` names no
company at all. The AMFA KB may hold the intercompany side of this that this KB doesn't have standing
to resolve on its own. See §7.

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
copy (`1ykYJERaptUNH0FDvkOVU26jh_x_hRtLz`). **Drive is the source of truth.**

**The git mirror `minda-ui/Darius` is partial, and that is a deliberate, recorded state — not an
oversight.** It holds this charter, `README.md`, `Wiki/index.md`, everything in `Outputs/`, and the
four Wiki articles created on 2026-09-17. The other fifteen Wiki articles live on Drive only. Anything
authored in a session is written to both and verified with `wc -c` against Drive's reported size;
anything that predates the mirror stays on Drive, because **the connector's read tool cannot return a
file byte-for-byte** (§3), so back-filling would silently corrupt what it copied. *v8–v11 of this file
claimed the mirror "is kept in step". That was never true; corrected in v12.*

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
duplicate cleanup: **Machinery Register - Database** (`1754351980906372`, `FA2301`–`FA2305`,
`FA2401`, `FA2402`), **Document Register** (`838802392352644`), **Tasks** (`4087584374523780`), **Safety Check Log**
(`913380204480388`, F45 monthly safety check), **Maintenance Schedule** (`6753985971226500`, all
recurring maintenance tasks, RYGB by due date), **Fault Log** (`414932606781316`, faults & fixes,
RYGB by status) and **Scan Events** (`4828191892047748`, the append-only barcode scan log, RYGB by
Actioned — added 2026-09-17 as Phase 0 of the barcode system). These sheets, not any Wiki article, are
the live source for current status/dates; Wiki articles narrate and cite them. The Vitap's own §6.8 check is **not** yet added to the Safety
Check Log — see §7 (Task T013).

**Register conventions.** Per group document-numbering policy v1.3: `FA` prefix (Amfa Furniture),
7-digit document numbers on the shared group register (not yet used by this KB — see below), 4-digit
property/asset codes self-assigned locally as `FA` + 2-digit year + 2-digit sequence.

**Asset labels are a separate namespace.** The group uses pre-printed "PROPERTY OF FISHBONE GROUP"
tags carrying a QR code and a four-digit number. **The label number is the physical tag; the `FA` code
is this register's ID.** The two are joined by the Machinery Register's `Asset Label No.` column and are
never merged — assets are not renumbered to match labels. The master label register is **group-wide and
owned by Alex**, not this KB; see
`Outputs/2026-09-17-handoff-workshop-assets-for-group-register.md`.

**Mapped 2026-09-17** from the owner's photographs, one machine at a time: `0017` → the
**unregistered** ABAC compressor, `0018` → `FA2301`, `0019` → `FA2402`, `0020` → `FA2303`,
`0021` → `FA2304`. `FA2401` has no label yet. The series starts above `0001`, so `0001`–`0016` are
elsewhere in the estate. **What the QR codes actually decode to is still unknown** and blocks barcode
Phase 1 — a scanner has to know what it will receive. `0019` was held at `[confirm]` for several steps
rather than guessed: the owner photographed it on "our extractor" while two extractors were
registered, and the right answer turned out to be a third machine the register did not contain.

**Assigned so far**: `FA2301` (Hebrock F4, corrected 2026-09-15 from a wrongly-assumed `FA2601`),
`FA2302` (Inventair MK1 MTFA extractor — **Sold**), `FA2303` (Altendorf F45), `FA2304` (Vitap K2-2.0),
`FA2305` (Inventair MK2 MTFA — **Sold**; acquisition year had been confirmed from invoice 100154 before
the code was assigned, same discipline applied since the `FA2601` mistake), `FA2401` (Brother TD-4420DN
label printer — **the first 2024 asset**; the year was evidenced from its order receipt *before* a code
was assigned, which is exactly why it is not `FA26xx`), `FA2402` (AES SAF 10,000 STK fine dust extractor
— same discipline, year evidenced from invoice 22473 first).

**Codes are never retired or reused.** `FA2302` and `FA2305` were sold in the period before this KB
existed; their rows stay, marked `Sold`, because they carry purchase prices, an invoice trail and the
history of how the shop's extraction came to be centralised. A disposal changes an asset's status, not
its existence in the register.

**Registered ≠ complete.** The ABAC GENESIS 15 500L screw compressor — which supplies the pneumatics of
`FA2301`, `FA2303` and `FA2304`, and is therefore a single point of failure for the whole workshop — was
found on 2026-09-17 to have never been registered. It still has **no code**, deliberately: its type plate
gives a *manufacture* year (2023) and this KB's convention needs an *acquisition* year (Task T019). See
§3 and §7.

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
Lessons from Sessions 2–14, all on real incidents rather than invented ahead of time:
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
  confirm, not a status to assert. **Closed 2026-09-17, and the restraint paid**: the answer to "did
  `FA2305` supersede `FA2302`?" was *neither*. Both were sold and replaced by a third machine
  (`FA2402`) that the register did not contain. Had either been marked "superseded" on plausibility,
  the correction would have had to unpick a status, a date and a relationship; as it was, nothing
  needed unpicking.
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
  a marker, exactly like a figure off an invoice.** *Confirmed twice over on the same day:* the workshop's
  address had said **Unit 32** since Session 1 and was also wrong (it is Unit 31), and a billing address was
  described as "residential" purely from its format when it is in fact the companies' registered office.
  Three unsourced statements, three corrections, one day. **If it was not read off a document, say so.**
  *A fourth surfaced the same evening — §1's claim that the git mirror "is kept in step" (v12).*
- **A register only contains what somebody thought to put in it.** Five sessions were spent
  documenting three machines in detail — manuals, fault tables, maintenance schedules, re-commissioning
  requirements — while the compressor that feeds all three sat unregistered and unmentioned. It surfaced
  only because the owner photographed an asset label on it. **The gap was invisible from inside the
  KB**: nothing in the register pointed at a machine the register did not contain. Completeness is not
  something a knowledge base can check about itself; it needs a walk round the floor. The same walk
  turned up the first dealer sticker (R&J Machinery) in the whole KB, after three machines had been
  documented with no seller identified at all.
- **A model name is not a specification.** `STK 10000` was read as "probably 10,000 m³/h" and the
  reading was labelled, in the task itself, as *not* sourced — *"that is a reading of the model name,
  NOT a specification — do not rely on it."* It held for days until the vendor's quotation arrived and
  confirmed it. The label cost nothing and would have prevented a wrong number hardening into a fact if
  the guess had been wrong. **Label the inference, not just the conclusion.**
- **What a document excludes can matter more than what it states.** The AES quotation's specification
  table was useful; the two clauses saying the vendor supplies no cabling, no hose and no on-site
  electrical connection were more useful, because they moved the whole installation — ductwork,
  electrics, commissioning — into the group's own undocumented column. **Read the exclusions, the
  payment terms and the delivery conditions, not only the spec table.**
- **Trust the API's response, not its status code.** A 4,000-character Smartsheet cell value was
  **silently truncated mid-sentence** and still returned success. It was caught only by reading the
  stored value back out of the response. Long note fields go in compact, and get read back.
- **Verify like with like.** A Drive file's reported `fileSize` is **bytes**; Python's `len()` is
  **characters**. Comparing one against the other on a file full of `—`, `≥`, `³` and `Ø` showed a
  329-"byte" gap that did not exist, and cost a full withdraw-re-read-re-upload cycle plus a wrong
  "do not cite" label on an archived file that had nothing wrong with it. **Use `wc -c` both sides.**
- **The connector's read tool does not round-trip, so never "copy" a file with it.** It returns a
  re-formatted rendering — leading punctuation escaped, two-space hard breaks appended — not the bytes
  on disk. A 2 KB article reconstructed from it came back **4 bytes out, silently**. This is why the
  git mirror is deliberately partial (§1) rather than back-filled, and why a large article is never
  rewritten just to change one metadata field: **every rewrite through a lossy read risks drift in the
  99% you did not mean to touch.** Write new content to both stores from the same local copy and check
  `wc -c`; do not treat Drive as a source you can read back and re-emit.
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
Register, Tasks, Maintenance Schedule, Fault Log, Safety Check Log, Scan Events) and creating Wiki
articles here is normal KB work and allowed. Deleting whole Smartsheet sheets is a UI action the owner takes (the
connector has no delete-sheet tool); the 2026-09-15 duplicate cleanup was done that way.
**6b — access review:** 2026-09-14, initial setup — Drive KB and Smartsheet workspace created by the
owner (minda@fishboneconstruction.co.uk); no other access granted. Shared group Document Register
write access still not confirmed. 2026-09-16: git mirror `minda-ui/Darius` created (owner) + seeded;
**confirmed private by the owner 2026-09-17**. 2026-09-17: a supplier support ticket containing live
SIP trunk credentials was shown in a screenshot; **not recorded anywhere in this KB** per the
never-hold-a-credential rule, and the owner was advised to have the password rotated — with the point
made plainly that deleting the image does not un-expose a credential already shown. Same day:
**`AnyDesk.exe` and `putty-64bit-0.85-installer.msi` were found sitting in `Raw/`** — a remote-access
client and an SSH client in a document inbox. Flagged to the owner, **never opened, run or moved**; the
owner has since removed them (confirmed by folder listing). Same day: **bank sort code and account
number on the MWM quotation were deliberately not copied** into the register or the Document Register,
and the omission is recorded in the `FA2402` note so it reads as a decision, not an oversight.
**6c — revisit cadence:** none set yet.

## 7. Workshop snapshot and open questions

**Location:** **Unit 31, Point Pleasant Industrial Estate, Wallsend, Tyne and Wear NE28 6HA** — the
workshop. **Unit 30** on the same estate is office and warehouse — **also NE28 6HA** (owner, 2026-09-17;
the `[confirm]` that stood against this is discharged). **Unit 32 is no longer held**; everything in this
KB dated before 2026-09-17 that says Unit 32 was wrong or is historic.

Evidenced by the lease cover page: **Forth England Limited** (landlord) and **Furniture by Fishbone
Limited** (tenant), **dated 25 June 2026**. *Furniture by Fishbone Limited is this company's former name —
Companies House confirms it renamed to **AMFA Furniture Ltd** on 13 July 2026, three weeks after the lease
was signed (Fishbone Construction KB, `Wiki/Suppliers/amfa-furniture-ltd.md`, CH overview `FH0000019`).*
Same company, not a new one. **Unit 31's previous occupant was Fishbone Waste**, who have moved out — which
is why the 2024 Brother order receipt shows "Fishbone Waste, Unit 31" for what is now the workshop's address.

**The lease itself is not this KB's to hold** — §1 deliberately has no `Properties`/`Contracts` folders. It
belongs in the AMFA Furniture Ltd KB, along with **Forth England Limited** as a Suppliers entry. Flagged for
the owner/Victoria; only the cover page has been seen.

**Machines registered:**
- `FA2301` — Hebrock F4 edge banding machine, Serial F3809. CE-compliant. Corner-rounding fault
  (stop-screw misadjustment) resolved (FL-001). Maintenance schedule (MT-001…014) + troubleshooting
  reference built. See `Wiki/Machinery/hebrock-f4-next-edge-bander.md`.
- `FA2302` — Inventair MK1 MTFA dust/fume extractor. **Sold** (owner, 2026-09-17). Never had a manual;
  never joined the maintenance system. **Disposal date and sale proceeds unknown** — it carries a
  purchase price, so the disposal has a book consequence.
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
- `FA2305` — Inventair MK2 MTFA dust/fume extractor, bought alongside `FA2304` on invoice 100154.
  **Sold** (owner, 2026-09-17). The promised manual never arrived and now never will. **Disposal date
  and sale proceeds unknown**, same book consequence as `FA2302`. *The long-running question of whether
  `FA2305` superseded `FA2302` is answered: neither did.* Both were sold and replaced by a single
  centralised unit, `FA2402`, that this KB had never heard of. The suspicion had been recorded as
  unconfirmed rather than asserted, so nothing had to be unpicked — see §3.
- `FA2401` — Brother TD-4420DN direct-thermal label printer, bought 09/05/2024 (Printerland order receipt
  SOA2606351, £211.58 ex VAT). Registered 2026-09-17. **Billing trail unresolved and recorded as such:** no
  company is named on the billing line — it is in the owner's name at the companies' registered office — and
  it shipped to Fishbone Waste at Unit 31, then a different occupant. **ZPL emulation unverified** (resellers
  claim it, Brother's own manual for this model never mentions it); direct thermal fades, so it suits
  short-life part labels, not asset or offcut labels. **No asset label applied yet.** See
  `Wiki/Machinery/brother-td-4420dn-label-printer.md`.
- `FA2402` — **AES SAF 10,000 STK fine dust extractor** (centralised, three-phase), serial **A-077**.
  Invoice **22473**, **08/10/2024**, **Markfield Woodworking Machinery Ltd**, £6,350 net / £7,620 inc
  VAT, paid in full. Asset label **`0019`**. Registered 2026-09-17, acquisition year evidenced before
  the code was assigned. **Specification sourced from the vendor's quotation of 02/10/2024** (six days
  before the invoice, identical figures): **10,000 m³/h**; 11 kW / 15 HP direct drive, star-delta; **355
  mm** suction; **64 filters at Ø160 × 940 mm, 30.22 m²**; three waste buckets; 720 kg; a Part Holder
  stopping parts over 25 × 25 mm reaching the propeller. **What the vendor did *not* supply is the
  important part** — *"not supplied with electrical cabling, extraction hose or blades"* and *"we do not
  electrically connect machinery on-site"* — so the ductwork and electrics were the group's own work and
  **nothing about that installation is recorded** (Task T014). *"Dust absorption rate 40 m/min"* is
  recorded verbatim and **unreconciled**: it matches neither the inlet velocity nor the filter face
  velocity, and is not to be used until a vendor or a real manual explains it. **Still no operating
  manual**, so it cannot join the Maintenance Schedule or Fault Log. Billed to Fishbone Drylining Ltd and
  **delivered to Unit 31 in October 2024 — nearly two years before AMFA's Unit 31 lease** (T004). See
  `Wiki/Machinery/aes-saf-10000-stk-extractor.md` and
  `Wiki/Suppliers/markfield-woodworking-machinery.md`.
- **The ABAC compressor — on the floor, on a label, not on the register.** ABAC **GENESIS 15 500L**
  rotary screw compressor with integrated dryer; asset label **`0017`**; serial **ITJ717909**, product
  4152025548, **plate year 2023**, 455 kg, **15 kW three-phase**, 0.58 kW dryer, max **10 bar**,
  refrigerant **R513A 0.5 kg = 316 kg CO₂e**. **No `FA` code assigned** — the plate year is manufacture,
  the convention needs acquisition; purchase paperwork requested (Task T019). **It feeds the pneumatics
  of `FA2301`, `FA2303` and `FA2304`.** Two live concerns: its gauge read **5.4 bar** against machines
  asking 6–8 bar, and the service log printed on its own yellow label is **blank** (Task T020). F-Gas:
  0.32 tonnes CO₂e is far below the 5-tonne leak-check threshold, so charge size triggers no periodic
  leak checking.

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
- **Barcode system, Phase 0 (2026-09-17)** — the **Scan Events** sheet (`4828191892047748`) and the
  Machinery Register's `Asset Label No.` column, documented in
  `Wiki/Processes/barcode-and-scan-event-system.md`. Phases 1–4 (part labels, stage tracking, the
  offcut library, Vitap program selection) are designed but not built; the sheet is still empty.

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
- **Were the machines re-commissioned after the move to Unit 31?** The KB holds no record that a move
  happened at all, yet the lease is dated 25 June 2026. The F45's own manual requires, after installation:
  a flat, level, load-bearing floor (~1100 kg, centre of gravity ~100 mm below the blade axis); swing-arm
  check (0.5 mm); sub-rollers; main-table height (0.1–0.2 mm); cross-slide height; free-cut both sides;
  angle-cut calibration by test cut (**< 0.2 mm**); an electrician to verify motor rotation direction; and
  extraction interlocked to machine power. Extraction also needs **≥ 20 m/s** through the ø140 mm connection,
  and new duct runs change the velocity actually achieved — which bears on the extraction-sizing question
  below. **Not assumed skipped; simply unrecorded.** *The owner has confirmed the machines are "up and
  running"* — which answers whether they work, **not** whether these checks were carried out. Recorded as
  partly answered, not closed (Task T018): "it runs" is not "it was commissioned", and treating one as the
  other is the inference §3 keeps warning about.
- **The Unit 31 lease body has not been seen** — only the cover page. Alterations, repair/reinstatement and
  nuisance clauses all bear on the workshop (extraction ducting, three-phase runs, fixing machines to the
  slab, noise and dust). The lease belongs in the AMFA KB, but those clauses affect this patch.
- **`0191 605 2945` is printed on every group asset label — and is in a SIP trunk migration.** The ticket
  (WebMate `T02530-15072026`) lists `+441916052945` among four DDIs migrating, with a stated completion date
  of **03/08/2026 that has already passed**. If that number does not survive, every asset label points at a
  dead line. Telephony is **not** this KB's scope; this is flagged only because the labels depend on it.
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
- **What do the asset labels' QR codes decode to?** *Which label goes on which machine is now answered*
  (`0017`–`0021`, §1), but the QR payload is still unknown and **Phase 1 cannot start until it is** — a
  scanner has to know what it will receive.
- **Who legally owns `FA2301`–`FA2305` and `FA2402`?** All invoiced to Fishbone Drylining Limited (now
  Fishbone Construction Ltd), not AMFA Furniture Ltd (Task T004) — and so was the SmartCABINET software.
  *Sharpened 2026-09-17:* AMFA Furniture Ltd holds the Unit 31 lease, so the picture is one company's
  machines operating in another's leased premises. **`FA2402` sharpens it again**: it was delivered to
  Unit 31 in **October 2024**, nearly two years before that lease was signed, which suggests the 2026
  "move" was AMFA taking a lease on a unit the group already occupied rather than a relocation. Evidence,
  not a conclusion — the lease body and the intercompany side both sit outside this KB.
- **`FA2303`'s expired safety certificates** — check with Altendorf/supplier (Task T007);
  **first F45 monthly safety check not yet logged** (Task T008); **`FA2303` serial/supplier
  unconfirmed** (Task T009); **`FA2303` annual PTC electrician check** needs scheduling (Task T011;
  Maintenance Schedule MT-025).
- **Installed extraction performance (Task T014, rewritten).** The `FA2302`/`FA2305` half is closed —
  both sold, both replaced by `FA2402`. The sizing half is now a different question. `FA2402` is rated
  **10,000 m³/h**, against known demand of the Vitap's ~2000 m³/h plus roughly **1,110 m³/h** for the
  F45 — *that second figure is my own arithmetic from ≥20 m/s through ø140 mm, not a manufacturer
  number* — plus the Hebrock, whose duct diameter this KB does not hold, so its ≥25 m/s cannot be
  converted. Comfortable on paper. **But the vendor supplied no ducting, no cabling and no on-site
  connection, and the machines have since been moved**, so what each machine actually receives is
  decided by pipework nobody documented. **Closing action: an anemometer velocity reading at each
  machine's connection**, which also answers the extraction half of T018.
- **A real AES operating manual** — the quotation gives specification, the schematic gives the control
  panel; neither gives maintenance intervals, filter-change criteria, safety instructions or a fault
  table. Until one arrives `FA2402` stays outside the maintenance and troubleshooting systems. The
  consumables are known (64 filters, three buckets), so the schedule can be built the moment the
  intervals exist.
- **The ABAC compressor** — purchase paperwork before a code can be assigned (T019); service history and
  F-Gas position (T020); and the **5.4 bar gauge reading against machines asking 6–8 bar**, which wants
  checking on its own account rather than as paperwork.
- **Disposal dates and sale proceeds for `FA2302` and `FA2305`** — both carry purchase prices, so both
  disposals have a book consequence this KB cannot compute.
- **Vitap `FA2304` §6.8 safety check** — does it need a dated, logged record like the F45's, or is a
  pre-cycle functional test enough? Owner decision (Task T013); MT-036 holds the place meanwhile.
- **`FA2304` serial/manufacture year** — confirm invoice-derived Serial 320070 AT against the type
  plate (Task T012).
- **Who actually sold `FA2301`, `FA2303` and `FA2304`?** Invoices 100153/100154/100155 name the customer
  and the items but carry no seller letterhead. The Vitap wears an **R&J Machinery** dealer sticker
  (`01455`, Hinckley) — recorded **`[confirm]`**, because a sticker on a machine is not a document, but
  it is the first evidence there has been. **Markfield Woodworking Machinery Ltd** (`FA2402`) is by
  contrast fully evidenced and has its own `Wiki/Suppliers/` article — the first supplier entry in this
  KB derived from a purchase rather than from a manufacturer's manual.
- **Full inventory of workshop machinery — demonstrably still incomplete.** This was a soft open
  question until 2026-09-17, when a 15 kW compressor feeding all three production machines turned out
  never to have been registered. That is no longer a theoretical gap: **the register is known to be
  missing at least one machine class, and nothing inside the KB can tell us whether it is missing
  others.** Hand tools, extraction ductwork, the air receiver and the server rack itself have never been
  assessed. Closing it needs a walk round the floor, not a document (see §3).
- **The git mirror is partial and cannot be back-filled by copying** (§1, §3). Fifteen Wiki articles
  exist on Drive only. Closing it needs a mechanism that returns bytes — an owner-side folder download,
  or a Drive-to-git sync outside this connector — not a read-and-re-emit. Until then the mirror is a
  *partial* mirror and this file says so.
- **`related:` front-matter links are not bidirectional.** `aes-saf-10000-stk-extractor.md` and
  `brother-td-4420dn-label-printer.md` link out to the three machinery articles; those three do not
  link back, and `hebrock-f4-next-edge-bander.md` carries `related: []`. Deliberately **not** fixed:
  the fix means re-authoring three 21–30 KB articles through a lossy read to change one metadata
  field, which risks more than it repairs (§3). Fix it the next time one of those articles is being
  rewritten for a substantive reason anyway.
- `AMF` vs `FA` property/asset-code inconsistency in AMFA's own Property Register — still just flagged.
- ~~Exact price on the Hebrock invoice unconfirmed~~ — **resolved 2026-09-15** by the 70%-balance
  cross-check confirmed on three invoices (Task T005, closed Done).
- A duplicate copy of two manuals was found outside this KB's own Drive folder tree — see §1.
