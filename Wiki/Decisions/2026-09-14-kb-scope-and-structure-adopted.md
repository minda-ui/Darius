---
title: "Decision: KB scope and structure adopted"
category: Decisions
status: active
sensitive: false
created: 2026-09-14
updated: 2026-09-14
sources:
  - ../../CLAUDE.md
  - ../../Outputs/change-log-2026-09-14-initial-kb-setup.md
related: []
---

# Decision: KB scope and structure adopted

**Decided by** the owner, 2026-09-14, in the same conversation that requested this KB be set up.
The initial request described a full standalone-company knowledge base and Smartsheet workspace,
matching the Fishbone Commercial Properties Ltd model exactly. Before building anything, the
assistant checked Drive and Smartsheet for name collisions and found two other furniture-related
entities already on record: Smartsheet workspaces "AMFA Furniture" and "AMFA Furniture Ltd" (the
latter with its own mature Drive KB, Document Register, Property Register, Tasks sheet and Reports
& Dashboards folder), and a Companies House record for "Furniture by Fishbone Ltd" (renamed AMFA
Furniture Ltd on 13 July 2026). Standing up a second full company KB for what might be the same
entity risked exactly the kind of duplicate, conflicting source of truth the group's document and
property registers exist to prevent — so the owner was asked directly rather than guessing.

**The answer:** this is "the knowledge base for the machinery we are using in Amfa Furniture
workshop" — not a new company, not a duplicate of the AMFA Furniture Ltd company KB, but a
narrower KB scoped specifically to the workshop's machinery and equipment.

## Why a separate KB rather than a folder inside the AMFA Furniture Ltd KB

Not investigated to a conclusion — this is a judgement call, recorded so it can be revisited. A
topic this specific (one class of asset within one company) could equally have been a `Machinery/`
folder inside the existing AMFA Furniture Ltd KB. It was built as its own top-level KB because
that is what was explicitly asked for, and because a dedicated Machinery Register, Document
Register and Tasks sheet in their own Smartsheet workspace (rather than more sheets bolted onto
AMFA's existing workspace) keeps machinery-tracking self-contained and easy to hand to whoever
runs the workshop day-to-day, without needing access to AMFA's company-wide financial and property
data. If that separation turns out to be the wrong call, merging this KB's Wiki articles into the
AMFA KB as a `Machinery/` category is straightforward; the reverse (splitting a mixed KB apart)
would not have been.

## Why modelled on Fishbone Commercial Properties Ltd specifically

Asked for by name, as the group's most mature example. Its structure (four-folder root, wiki
front-matter template, per-session change-log files indexed in `kb-registers.md`, Archive naming
with a dated reason) is the shared Fishbone Systems house style, not something specific to
property — it transfers directly to a machinery-tracking KB with only the Wiki topic folders
changed (`Machinery`/`Suppliers`/`People`/`Finance`/`Processes`/`Decisions` in place of
`Properties`/`Tenants`).

## Document numbering — the judgement call, made explicit

The group's document-numbering policy (v1.3) centrally allocates one 2-letter prefix per legal
entity on one shared Document Register. This KB is not a legal entity, so it was not entitled to
request a new prefix. Instead: correspondence about workshop machinery is registered on the
shared group register under AMFA Furniture Ltd's own `FA` prefix (confirmed live and current from
AMFA's own Document Register sheet, which is explicitly marked retired in favour of exactly that
shared register and prefix); machine/asset codes — a self-assigned, locally-scoped namespace, like
a property code — use `FA` + 2-digit year + 2-digit sequence (`FA2601`), mirroring the `FM2301`
pattern used for properties elsewhere in the group. Full reasoning: `../../CLAUDE.md` §1.

One inconsistency was found and is deliberately left unresolved here: AMFA Furniture Ltd's own
Property Register - Database uses `AMF` + space + 4 digits for property codes, not `FA` + digits.
This KB does not have standing to edit AMFA's own sheets, so the inconsistency is recorded as an
open question in `../../CLAUDE.md` §7, not silently fixed or silently copied.

## The rule this KB is adopting from Fishbone Commercial Properties Ltd's own history

FCP's KB spent real sessions correcting numbers a previous session had stated as fact and never
rechecked — a corpus survey undercounted an archive folder by six files, and a wrong count was
then "corrected" by arithmetic on the wrong number rather than by recounting. The lesson written
into FCP's own `CLAUDE.md` (§6d) is adopted here from day one, before this KB has any history of
its own to learn it the hard way:

**A number, count, date or figure stated by an earlier session in this KB — in a change-log entry,
a Wiki article, or this Decisions article itself — is not evidence.** Before repeating it, recount
it from the primary source: the live Smartsheet register, the actual files in `Raw/` or
`Outputs/Correspondence/`, or an external record (Companies House, a supplier's own documentation).
This applies especially to anything this article states as a snapshot (e.g. "AMFA's Document
Register is retired, canonical register is sheet `7352854736144260`, prefix `FA`") — true as read
on 2026-09-14, not guaranteed to still be true later.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-14 | Created alongside the initial KB and Smartsheet workspace setup | Session 1, entry "Workshop of Furniture Making KB and Smartsheet workspace created" |
