# CLAUDE.md — Workshop of Furniture Making Knowledge Base

**Version 31 — 2026-09-23.** Structure and conventions modelled on the Fishbone Commercial
Properties Ltd Knowledge Base, via the shared `Wiki/Process-Fishbone-Systems-House-Rules.md`
conventions used across all Fishbone group KBs. **This file is one of four that together form Darius's
charter** (see §0a and the map below). README.md is a pointer; these files win on conflict.

**Changed in v31 — the charter is four files, split by how often each part changes.**

**Adopted from Alex's proposal** (`AWT-0082`, owner's instruction 2026-09-23), **with different cut
lines, measured rather than assumed.** The proposal's core/rules/history shape assumes a governed file
is mostly rules plus a dated log. **This one was not**: §7 (workshop snapshot) was **34,789 B** and §3
(lessons) **23,651 B** — **67% of the file between them, and neither is a rule.** A mechanical
three-way split would have left ~58 KB in "core" and saved little.

| File | Holds | Changes when |
|---|---|---|
| `CLAUDE.md` | §0a, §0, §1, §2, §4, §5 | the KB's shape changes — rarely |
| `CLAUDE-Rules.md` | §0b Hub rules A–D, §6 governance | a rule changes |
| `CLAUDE-Lessons.md` | §3 | a lesson is learned — append-only |
| `CLAUDE-Workshop.md` | §7 | any machine, task or open question moves — most sessions |
| `Outputs/charter-version-history.md` | superseded `Changed in vNN` notes | every version |

**What it buys.** Drive has no patch API, so every change re-emits a whole file by hand. Against
86,856 B: a rule change now touches **~8× less**, a new lesson **~3.7×**, a workshop finding **~2.5×**,
a structure change **~4.9×**.

**The split moved no text.** It was done by script from the v30 file, with every section's sha256
compared before and after, and the monolith archived intact. *This KB has twice shipped a file that
passed a byte count and was still wrong (§3) — a size check cannot see a section that moved, so the
check here was per-section hashes, not totals.*

**What it does not solve, said plainly.** `CLAUDE-Workshop.md` is still the largest piece and still the
one that changes most, because **§7 is largely a summary of things that live elsewhere** — the Machinery
Register, the Tasks sheet, the Wiki articles. §3's own *put a fact where its own update cycle lives* and
the v21 lesson about summaries of summaries both point at it. **Whether §7 should shrink is an owner
decision and a separate measurement**, not something to fold into a reorganisation.

**Amended the same session, and not bumped to v32 — the registers were split too.** Closing the charter
split exposed the next file along: `Outputs/kb-registers.md` at **73,220 B** had become the most
expensive file in the KB, larger than any charter file, and `change-log-index.md` was **46,462**. Both
are now **period-split** on the owner's instruction (*"split by period"*): a live file holding what
still moves, and dated `-snapshot-<date>.md` files holding what is settled. **Splitting them by table would
not have helped** — all their tables are append-only and every session touches one. §4 carries the rule
and §1's folder tree the shape. *Measured, not assumed: 59,255 of the registers' 73,220 bytes were
settled rows, and the live file lands just under 20 KB.*

**Why this is v31 amended rather than v32.** It is the same session, the same instruction and the same
diagnosis — and a version bump would move this note to the history file and re-emit 41 KB to record a
continuation of what the note already describes. **Recorded here so the choice is visible** rather than
inferred from a version number that did not change.

**Two owner rulings carried in with it, 2026-09-23.** The split above, and — separately — that the
**Workshop Machinery Register is an asset register, not a financial document**, so the estate-law note's
never-git rule does not reach it and it stays in the git mirror. That second one is in §6b of
`CLAUDE-Rules.md`, where the access decisions live.

## Where the rest of the charter is

This file holds the parts that rarely change. The rest:

- **`CLAUDE-Rules.md`** — §0b, the Workforce Hub rules A–D; §6, governance (what is never done
  unattended, the `Raw/` hand-off rule, the access review).
- **`CLAUDE-Lessons.md`** — §3, the workflow and every lesson this KB has learned on a real incident.
- **`CLAUDE-Workshop.md`** — §7, the workshop snapshot: machines registered, operational systems, and
  the open questions and tasks.
- **`Outputs/charter-version-history.md`** — the `Changed in vNN` notes from every superseded version.

**All four are governed files and all four win over `README.md`.** A rule in `CLAUDE-Rules.md` binds
exactly as if it were in this file.

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
Maintenance Schedule, Fault Log), **and its own rows on the Workforce Hub** (§0b — own rows only, never
another seat's); and **needs a human** for everything in §6a — appending to the
shared group Document Register (confirmed access only), committing AMFA or Construction to any
purchase/contract/payment, replying to a supplier/insurer/inspector, filing with any regulator, or
touching another KB. The boundaries were already written into this KB's §6a; Darius just puts a name
to them. When two facts that should agree don't, Darius records the contradiction and asks — it never
guesses one into the other (§3).

## 0. Start every session here

Before doing anything — including a one-off question — read, in order:
1. **The Workforce Hub** — Tasks & Requests, Darius's own Open / In Progress rows (§0b, Rule A).
2. The newest entries in `Outputs/change-log-*.md` (newest-first index:
   `Outputs/change-log-index.md`).
3. The open `Processed items` rows of `Outputs/kb-registers.md` — the live file holds only those.
4. `Wiki/index.md` for what's already known.

**The charter is four files** (see the map above): this one, `CLAUDE-Rules.md`, `CLAUDE-Lessons.md`
and `CLAUDE-Workshop.md`. **Read `CLAUDE-Rules.md` at every session start** — it carries the Hub rules
and everything that must never be done unattended. The other two are reference: open
`CLAUDE-Workshop.md` before touching a machine or a task, and `CLAUDE-Lessons.md` before deciding how
to process something new.

**Re-read the live control files immediately before editing them** (their current Drive id and size),
and author the edit onto that live copy — never a copy read earlier in the session. The 2026-09-15/16
fork happened because two sessions edited stale copies in parallel; with a single owner this is
avoided, but the discipline stands.

This KB shares a parent company (AMFA Furniture Ltd) with a separate, company-wide KB. If a fact
could be recorded in either, check the AMFA Furniture Ltd KB rather than assuming this one is silent
on it, and cite across rather than duplicate. **This matters concretely**: every machine registered
here — `FA2301`–`FA2306` and `FA2402` — was invoiced to Fishbone Drylining Limited (now Fishbone
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
**unverified**. This bears on the **systemic half** of Task T016 — getting SmartCABINET to emit a Tool
ID on export — and must be checked, not inferred from the fact of a network. *It does not bear on the
immediate fix, which is entirely inside TpaCAD's own outfit (§7).*

**Where it lives.** Google Drive, folder `Workshop of Furniture Making - Knowledge Base`, primary
copy (`1ykYJERaptUNH0FDvkOVU26jh_x_hRtLz`). **Drive is the source of truth.**

**The git mirror `minda-ui/Darius` is complete as of 2026-09-19.** It holds this charter, `README.md`,
`Wiki/index.md`, everything in `Outputs/`, and **every Wiki article** — the ones that predated the
mirror were back-filled on 2026-09-19 with `download_file_content`, each checked against Drive's own
reported size. *This paragraph read "partial" from v12 to v22, and was true then.*

**This file deliberately does not say how many of each there are.** It said so four times and was wrong
four times (v12 *"four"*, v13 *"fifteen"*, v16 *"seven"*, v17 *"nine / twenty-seven"*) — a count goes
stale the moment an article is written, and this document is revised weekly at best. **The count lives
in the registers**, in the Wiki-structure rows, recorded at the moment each article was
added and with the command that produced it — `Outputs/kb-registers.md` for the current period and the
`kb-registers-snapshot-<date>.md` files for earlier ones. To quote a current figure, run
`git ls-files 'Wiki/**/*.md' | wc -l` for the mirror side and read the registers for the Drive-only
side; **do not carry a number forward from anywhere, including from here.** *(That pathspec counts the
articles in the topic folders and correctly leaves out `Wiki/index.md`, which sits at the top level and
is not an article. `_templates/article.md` is not tracked in git; if it ever is, it would need
excluding.)*

Anything authored in a session is written to both stores and verified with `wc -c` against Drive's
reported size, and **the back-fill of everything older is done** (2026-09-19): each Drive-only article
was fetched with `download_file_content`, which returns the stored bytes rather than a rendering (§3),
decoded straight to disk and checked against Drive's `fileSize`. **Keeping it complete is now the
standing job**, and it is the ordinary rule doing the work — an article written to one store and not
the other puts the mirror straight back where it was.
*v8–v11 of this file claimed the mirror "is kept in step". That was never true; corrected in v12.
v12–v21 said back-filling was impossible: true of `read_file_content`, false of the connector — v22.
v23 records it actually done.*

**Folders.**
```
Workshop of Furniture Making - Knowledge Base/
├── CLAUDE.md — core (§0a, §0, §1, §2, §4, §5)
├── CLAUDE-Rules.md — §0b Hub rules, §6 governance
├── CLAUDE-Lessons.md — §3 workflow and lessons
├── CLAUDE-Workshop.md — §7 workshop snapshot and open questions
├── README.md
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
│ ├── kb-registers.md — live rows only; kb-registers-snapshot-<date>.md — settled (v31)
│ ├── change-log-YYYY-MM-DD-<slug>.md — one per session
│ ├── change-log-index.md — newest first (v28); change-log-index-snapshot-<date>.md (v31)
│ ├── charter-version-history.md — the charter's superseded version notes (v27)
│ └── Correspondence/ — filed copy of every numbered document in scope
└── Archive/ — superseded files, renamed with reason and date
```
No `Properties`/`Tenants`/`Contracts` folders: not applicable to this KB's scope.

**Live data sources.** Smartsheet workspace `Workshop`, one sheet of each after the 2026-09-15
duplicate cleanup: **Machinery Register - Database** (`1754351980906372`, `FA2301`–`FA2306`,
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

**Mapped 2026-09-17** from the owner's photographs, one machine at a time: `0017` → the ABAC
compressor — then unregistered, **`FA2306`** since 2026-09-18 — `0018` → `FA2301`, `0019` → `FA2402`, `0020` → `FA2303`,
`0021` → `FA2304`. `FA2401` has no label yet. The series starts above `0001`, so `0001`–`0016` are
elsewhere in the estate; **`0025`–`0027` exist on an unapplied sheet** held by the owner, and nothing is
known about `0022`–`0024`. **What the QR codes decode to was answered 2026-09-18: the bare four-digit
label number as plain text** (`Text: 0027`) — no URL, no prefix, no `FA` code, leading zeros preserved,
*read from one tag, so generalising to the series is an inference.* **Phase 1's precondition is
discharged**; what still blocks it is in Task T022. The payload is **not self-describing**, so a scan
means nothing without the `Asset Label No.` lookup — and **leading zeros must never be stripped**, or
that join breaks silently. `0019` was held at `[confirm]` for several steps
rather than guessed: the owner photographed it on "our extractor" while two extractors were
registered, and the right answer turned out to be a third machine the register did not contain.

**Assigned so far**: `FA2301` (Hebrock F4, corrected 2026-09-15 from a wrongly-assumed `FA2601`),
`FA2302` (Inventair MK1 MTFA extractor — **Sold**), `FA2303` (Altendorf F45), `FA2304` (Vitap K2-2.0),
`FA2305` (Inventair MK2 MTFA — **Sold**; acquisition year had been confirmed from invoice 100154 before
the code was assigned, same discipline applied since the `FA2601` mistake), `FA2306` (ABAC GENESIS rotary screw air compressor — registered 2026-09-18 from **proforma invoice
208027**, 14/11/2023; the year evidenced before the code, the same discipline a fourth time, and the
proforma's status as *not* an invoice recorded rather than glossed), `FA2401` (Brother TD-4420DN
label printer — **the first 2024 asset**; the year was evidenced from its order receipt *before* a code
was assigned, which is exactly why it is not `FA26xx`), `FA2402` (AES SAF 10,000 STK fine dust extractor
— same discipline, year evidenced from invoice 22473 first).

**Codes are never retired or reused.** `FA2302` and `FA2305` were sold in the period before this KB
existed; their rows stay, marked `Sold`, because they carry purchase prices, an invoice trail and the
history of how the shop's extraction came to be centralised. A disposal changes an asset's status, not
its existence in the register.

**Registered ≠ complete.** The ABAC screw compressor — which supplies the pneumatics of `FA2301`,
`FA2303` and `FA2304`, and is therefore a single point of failure for the whole workshop — was found on
2026-09-17 to have never been registered at all. It was held at **no code** for a day, deliberately,
because its type plate gives a *manufacture* year and this KB's convention needs an *acquisition* year;
**registered as `FA2306` on 2026-09-18** once dated purchase paperwork arrived. **The lesson outlives the
gap it exposed**: nothing inside the register could point at a machine the register did not contain, and
nothing inside it can tell us whether it is missing others. See §3 and §7.

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

## 4. Change log

One file per session in `Outputs/`, named `change-log-YYYY-MM-DD-<slug>.md`, indexed newest-first in
`Outputs/change-log-index.md`. Never a single growing `CHANGELOG.md`.

**That index was part of `kb-registers.md` until v28**, when it was split out for the same reason the
charter's version history was split at v27: 35,701 bytes of append-only history riding along with rows
that change, in a file re-emitted whole every session.

**Both are period-split as of 2026-09-23** (owner's instruction, *"split by period"*), because the same
problem came back one file along: `kb-registers.md` had reached 73,220 bytes and the index 46,462, and
Drive re-emits a whole file for one new row. **Splitting them by table would not have helped** — every
table in them is append-only and every session touches at least one. **Splitting by period does**,
because a settled row is never touched again. So `kb-registers.md` keeps the open `Processed items` and
the current period's Wiki-structure and Outputs rows; `change-log-index.md` keeps the current period's
sessions; and the `-snapshot-<date>.md` files hold what is settled and are never re-emitted. **Snapshot
the live file again when it passes roughly 25 KB.**

**The snapshots were made by renaming the Drive copies, not by rewriting them** — byte-identical to git
`d4cd712`, nothing retyped, because manual re-emission is where this KB's byte discrepancies come from
(§3). The cost is that each snapshot keeps the header it had when it was live and so still describes
itself as a file §0 sends you to. **It does not**; the filename and the live file's own pointer table are
authoritative, and the registers snapshot also repeats **eight** of the nine open Processed items with
their 2026-09-21 status, which the live file supersedes — the ninth was opened after the snapshot. *Recorded rather than left to be discovered.*

## 5. Automated processes

None are live. The Maintenance Schedule / Safety Check Log / Fault Log RYGB `Health` columns are
self-updating **column formulas** (maintain via the connector, not by hand) — but there is no routine
that reads them and chases due dates yet; that's a future proposal, and a natural early candidate for
one of Darius's own scheduled routines.
