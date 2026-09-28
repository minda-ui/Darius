# CLAUDE.md — Workshop of Furniture Making Knowledge Base

**Version 34 — 2026-09-28.** Structure and conventions modelled on the Fishbone Commercial
Properties Ltd Knowledge Base, via the shared `Wiki/Process-Fishbone-Systems-House-Rules.md`
conventions used across all Fishbone group KBs. **This file is one of four that together form Darius's
charter** (see §0a and the map below). README.md is a pointer; these files win on conflict.

**Changed in v34 — the period split is over: the snapshots are merged back and the two live files hold
everything.**

**Owner's instruction, 2026-09-28: *"merge the snapshots back."*** The direct consequence of v33 — with no
size threshold there is nothing for a period split to serve. `kb-registers.md` **28,088 → 115,582 B** and
`change-log-index.md` **11,275 → 72,817 B**; §1's folder map and §4 lose the `-snapshot-<date>.md` files,
and **`kb-registers.md` is no longer "live rows only" — it is all 30 Processed items, all 36 Wiki-structure
changes, all 74 Outputs rows and both Drive-id tables.** The index holds **all 23 sessions**.

**Five snapshots, not the three v33 said.** *That figure was read off the registers' own header table, which
lists only its own three; the index had two more. Corrected by counting the files.* All five were verified
byte-identical to git `HEAD`, then **archived by rename into `Archive/`, ids preserved — merged, not
deleted.**

**Nothing was retyped, and the duplication the old headers warned about was handled rather than inherited.**
Every row was copied byte-for-byte by script. The nine open Processed items appeared in *all three* registers
snapshots as well as the live file, so a plain concatenation would have produced them four times: instead the
2026-09-21 order was walked and **the live row substituted wherever it was the authority (eight of them)**,
the ninth appended, and the two later Processed tables **dropped as exact duplicates — verified 9 of 9 each.**
*The Wiki, Outputs and session tables needed no such care, being disjoint by construction; that was checked,
not assumed, and the merged ordering was re-verified afterwards.*

**And the merge pushed straight past v33's own new ceiling, so it was measured again.** At 115,582 B the
registers exceeded the 92 KB proven an hour earlier, so a third probe ran at **130,005 B** — same-size,
different-content, id stable, revisions 1 → 2, byte-identical, 6 s. **Limit 3 is now 130 KB.** *Twice in one
day the rule's own words — extend it by measuring — were what let the work proceed, and both times the
alternative was a slower path rather than a blocked one.*

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
own Workshop Smartsheet sheets (Machinery Register, Workshop Document Log, Tasks, Safety Check Log,
Maintenance Schedule, Fault Log), **and its own rows on the Workforce Hub** (§0b — own rows only,
never another seat's); and **needs a human** for everything in §6a — appending to the
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
3. The open `Processed items` rows of `Outputs/kb-registers.md` — **read those; the file holds all 30, the
   settled ones included, since v34 merged the snapshots back.**
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

**How a file on Drive is changed** (v32). Drive has **no partial-patch API**, so a change replaces a
file's whole content — **but it does not have to be retyped.** Content already on disk can be uploaded
**in place, keeping the file's id**, which is the default from v32; §4 carries the method and the cases
that still require archive-then-recreate. *Drive retains the previous bytes as a revision, but
`keepForever` is `false` by default, so that retention is **not** durable — a revision is not an archive.*

**The git mirror `minda-ui/Darius` is complete as of 2026-09-19.** It holds this charter, `README.md`,
`Wiki/index.md`, everything in `Outputs/`, and **every Wiki article** — the ones that predated the
mirror were back-filled on 2026-09-19 with `download_file_content`, each checked against Drive's own
reported size. *This paragraph read "partial" from v12 to v22, and was true then.*

**This file deliberately does not say how many of each there are.** It said so four times and was wrong
four times (v12 *"four"*, v13 *"fifteen"*, v16 *"seven"*, v17 *"nine / twenty-seven"*) — a count goes
stale the moment an article is written, and this document is revised weekly at best. **The count lives
in the registers**, in the Wiki-structure rows, recorded at the moment each article was
added and with the command that produced it — all of it in `Outputs/kb-registers.md`, which since **v34**
holds every row this KB has recorded. To quote a current figure, run
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
│ ├── kb-registers.md — every row, all three tables plus the Drive-id tables (v34)
│ ├── change-log-YYYY-MM-DD-<slug>.md — one per session
│ ├── change-log-index.md — every session, newest first (v28; un-split v34)
│ ├── charter-version-history.md — the charter's superseded version notes (v27)
│ └── Correspondence/ — filed copy of every numbered document in scope
└── Archive/ — superseded files, renamed with reason and date
```
No `Properties`/`Tenants`/`Contracts` folders: not applicable to this KB's scope.

**Live data sources.** Smartsheet workspace `Workshop`, one sheet of each after the 2026-09-15
duplicate cleanup: **Machinery Register - Database** (`1754351980906372`, `FA2301`–`FA2306`,
`FA2401`, `FA2402`), **Workshop Document Log (local mirror)**
(`838802392352644` — called **Document Register** until 2026-09-24, renamed by the owner under
`AWT-0087` to end an estate-wide collision of that name; same sheet, same id, and dated records keep
the old name), **Tasks** (`4087584374523780`), **Safety Check Log**
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

**They were period-split from 2026-09-23 to 2026-09-28, and are not any more.** The split was the owner's
instruction (*"split by period"*) when `kb-registers.md` had reached 73,220 bytes and the index 46,462 and
Drive re-emitted a whole file for one new row. Splitting by table would not have helped — every table in
them is append-only and every session touches at least one — whereas a settled row is never touched again.
**v33 removed the size threshold that justified it and v34 undid it**, on the owner's instruction *"merge the
snapshots back"*: five snapshots verified against git `HEAD`, merged back by script with **nothing retyped**,
and **archived by rename into `Archive/` with ids preserved.**

**So both files now hold everything, and neither is snapshotted on byte count again.** A future split needs a
reason of its own — the owner asking, or a file becoming genuinely hard to navigate. *Byte count is not that
reason: v32 removed the retyping the old re-emission cost, and v34's own merge then wrote 115,582 B in one
in-place call.*

*Two things the split leaves behind, worth knowing if the archived copies are ever read: each keeps the
header it had while it was live, so it still describes itself as a file §0 sends you to — **it does not**,
the filename says what it is — and the registers snapshots repeat the open `Processed items` that the live
file was always authoritative for. That overlap is exactly what the merge had to de-duplicate.*

**How a change reaches Drive** (v32, owner's instruction 2026-09-28; proposal
`Outputs/2026-09-27-proposal-drive-in-place-update.md`).

**Default — update in place, from disk.** Write the file locally, then upload it to its existing `fileId`.
The id does not change, so citations do not go stale, and **the bytes are never retyped**, which is where
this KB's byte discrepancies have actually come from (§3).

**Every write is still proved the same way:** `download_file_content` → decode → `diff` against the local
file. **The verifier stays the native connector** — both halves of a byte-check must not depend on the same
tool. Where the content is meant to be *identical*, a byte-check alone cannot tell a write from a no-op, so
check the **revision count** as well.

**Fallback — archive-then-recreate** (rename the superseded Drive copy into `Archive/` with a reason and
date, then create a new file, then verify). **Still mandatory for:**

1. **Anything whose superseded copy must be findable by name** — the charter files and their version bumps,
   a superseded Wiki article that other work cites, and any file being retired from the live tree. *The
   `-snapshot-<date>.md` files were this clause's other example until v34 merged them back; the five archived
   copies are named for what they were and why they went.*
2. **Anything whose superseded bytes must survive.** `keepForever` is **`false` by default** on Drive
   revisions, so Drive may purge them. Setting it is a separate PATCH per revision and is not done here.
3. **Anything outside what has been proven:** above **130 KB** — measured at v34 at **130,005 B**, after
   v33's probes at 46,035 B and 92,070 B, every one of them same-size/different-content so that neither a
   no-op nor a partial write could pass, and every one id-stable, revision-incremented and byte-identical —
   and on binary files, Google-native types and files this account does not own. *The 37 KB figure, the
   ~82 KB `read_file_content` cliff and then 92 KB were each retired by measurement, not by instruction:
   extend this the same way, and never by assuming.* **From ~46 KB the verification download is
   spilled to a file rather than returned inline** — decode it from there; it is a limit of the session, not
   of Drive, and it does not make the write unprovable.

*The in-place path runs through a third-party service and a CLI in an ephemeral container. If either is
unavailable the fallback is the whole rule, which is why it stays documented rather than deleted.*

## 5. Automated processes

None are live. The Maintenance Schedule / Safety Check Log / Fault Log RYGB `Health` columns are
self-updating **column formulas** (maintain via the connector, not by hand) — but there is no routine
that reads them and chases due dates yet; that's a future proposal, and a natural early candidate for
one of Darius's own scheduled routines.
