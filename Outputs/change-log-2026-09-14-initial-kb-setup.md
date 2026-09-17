# Change log — 2026-09-14 — Initial KB setup

**Session 1.** Owner asked for a new Google Drive Knowledge Base and matching Smartsheet
workspace for "Workshop of Furniture Making", following the Fishbone group's standard KB
structure modelled on the Fishbone Commercial Properties Ltd KB.

## What was checked before building anything

Before creating a folder tree, checked Drive and Smartsheet for name collisions, because the
request as first described (full company KB + document-numbering prefix) matched the shape of an
existing group entity's onboarding. Found: Smartsheet workspaces "AMFA Furniture" and "AMFA
Furniture Ltd" (the latter with its own Drive KB, retired local Document Register pointing at the
shared group register under prefix `FA`, a Property Register using `AMF`+digits codes, a Tasks
sheet, and a populated Reports & Dashboards folder), and a Companies House record for "Furniture by
Fishbone Ltd" (renamed AMFA Furniture Ltd, 13 July 2026). Asked the owner directly whether this new
KB was the same entity. Answer: no — this is the knowledge base for the machinery used in the AMFA
Furniture Ltd workshop specifically, not a duplicate company KB. See
`Wiki/Decisions/2026-09-14-kb-scope-and-structure-adopted.md` for the full reasoning.

## What was built

**Google Drive** — `Workshop of Furniture Making - Knowledge Base/`:
- `CLAUDE.md`, `README.md`
- `Raw/README.md`
- `Wiki/index.md`, `Wiki/_templates/article.md`, and topic folders `Machinery/`, `Suppliers/`,
 `People/`, `Finance/`, `Processes/`, `Decisions/` (with the first Decisions article)
- `Outputs/README.md`, `Outputs/kb-registers.md`, `Outputs/Correspondence/README.md`
- `Archive/` (empty — nothing superseded yet)

No `Properties`, `Tenants` or `Contracts` folders — this KB holds no property and no tenancies;
see the Decisions article and `CLAUDE.md` §1.

**Smartsheet** — workspace `Workshop`:
- `Machinery Register - Database` sheet, columns and RYGB formula conventions adapted from the
 Fishbone Commercial Properties Ltd / AMFA Furniture Ltd Property Register - Database sheets,
 with property-specific columns (tenure, lease, rent, tenant) replaced by machinery-specific ones
 (manufacturer, model, serial number, location, service/compliance dates, warranty, supplier)
- `Document Register` sheet, matching the group's current best-practice column set (contact-type
 Owner, RYGB `Health` formula), with a note that the canonical register is the shared group
 Document Register under AMFA Furniture Ltd's `FA` prefix
- `Tasks` sheet, matching the group's standard columns and RYGB `Health` formula
 (`1. General` / AMFA Furniture Ltd convention) with a contact-type Owner column
- `Reports & Dashboards` folder, created empty (sights/reports only, no data sheets)

## Document numbering adopted

Correspondence about workshop machinery: registered on the shared Fishbone Group Document
Register (sheet `7352854736144260`) under AMFA Furniture Ltd's own `FA` prefix, 7 digits
(`FA0000001`), deduped by Source key per group policy v1.3. Machine/asset codes: self-assigned
locally, `FA` + 2-digit acquisition year + 2-digit sequence (`FA2601`), 4 digits, mirroring the
`FM2301` property-code pattern used elsewhere in the group. Full reasoning and the one open
inconsistency found (AMFA's own Property Register uses `AMF`+digits, not `FA`+digits) are in
`CLAUDE.md` §1 and the Decisions article.

## Open questions carried forward

- Full inventory of workshop machinery — not started; nothing has been filed into `Raw/` yet.
- `AMF` vs `FA` property/asset-code inconsistency in AMFA Furniture Ltd's own Property Register —
 flagged for the owner, not resolved by this KB.
- Whether this KB should file correspondence in its own `Outputs/Correspondence/` (as built),
 the group's shared Collaboration Space (per v1.3 filing policy), or both.
