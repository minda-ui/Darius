# Change log — 2026-09-15 — Altendorf F45 registered

**Session 6.** Owner reported the workshop's second machine, an "F45", and uploaded 8 PDF parts to
`Raw/` (~74MB) — larger than the Hebrock F4's manual — followed by an invoice.

## What was found

Read via two parallel background extraction agents (parts 1-4 and parts 5-8), same approach used
for the Hebrock manual. Key findings:

- **Not a Hebrock/edge-bander product.** The F45 is an **Altendorf GmbH** CNC sliding-table (panel)
 saw — Altendorf being the parent group Hebrock belongs to, so the two machines share a corporate
 family but are otherwise unrelated products.
- **Two manuals in one set of files**: the main saw manual (doc 0000010074-011-2023, parts 1-6,
 itself three duplex-scan pairs reconstructing pages 1-183) and a separate manual for the
 "ElmoDrive" CNC touchscreen control unit (doc 0000010077-001, parts 7-8).
- **A genuine compliance gap**: the machine's DGUV/GS/machine-safety certificates (HM 220023-25)
 are dated 09.05.2022 and state outright they are "valid until 22.02.2024" — over 2.5 years
 expired. Flagged prominently, not buried in Open questions only.
- **A mandatory, documented monthly safety check** (E-stop, sliding-table limit switch, chip-duct
 limit switch, ON/OFF switch cleanliness, protective hood) — the manual's own words: "Carry out
 and document this check 1x month!" This isn't a normal machine fact to file away; it's a
 recurring compliance obligation, so it got its own process and its own log sheet rather than
 just a paragraph in the machine article.
- **Extraction requirement ~1110-1150 m³/h** — roughly 50-60x the Hebrock F4's ~20 m³/h. Owner
 confirmed a centralised extraction unit (manual pending) now serves both machines, which is the
 only way that gap makes sense; the Inventair MK1 MTFA (`FA2302`) is likely superseded — flagged
 as an open task rather than assumed.
- **Full fault-diagnosis tables** for both the mechanical saw (break-outs, burn marks, sub-roller
 issues) and the ElmoDrive control unit (a genuine E01-M11 electronic error-code table).

**Invoice 100153** (09/11/2023, same day as the Hebrock/Inventair purchase, same customer/site):
confirms the machine's **full price unambiguously** as £64,030.00 (the 70% balance shown,
£44,821.00, is exactly 70% of that) — no ambiguity like the Hebrock invoice's deferred-VAT
situation. Billed to Fishbone Drylining Limited (now Fishbone Construction Ltd), not AMFA
Furniture Ltd — same open owning-entity question as the other two assets.

## What was done

- **Asset code `FA2303`** assigned, using the confirmed 2023 purchase date — not guessed this time;
 the owner was asked for the acquisition year/invoice up front, learning from the `FA2601`
 mistake on the first machine.
- **Created** `Wiki/Machinery/altendorf-f45-panel-saw.md`: full key facts, installation/setup,
 safety, maintenance schedule (cleaning intervals + trigger-based lubrication), both fault tables,
 and Open questions.
- **Created** `Wiki/Processes/f45-monthly-safety-device-check.md`: the first article in
 `Processes/`, documenting the mandatory check and where it's logged.
- **Created** Smartsheet sheet **"Safety Check Log"** in the `Workshop` workspace — a proper
 recurring log with Pass/Fail/N-A columns for each of the five checked items, a Health RYGB
 formula, an evidence-link column (plus native Smartsheet row attachments for photos), and an
 auto-computed next-due date.
- **Smartsheet**: `FA2303` Machinery Register row added; 3 Document Register rows (main manual,
 ElmoDrive manual, invoice); 5 new Tasks (T007 expired certs, T008 first monthly check, T009
 confirm serial/supplier, T010 review FA2302 status, T011 annual PTC electrician check); T004
 updated to cover all three assets' owning-entity question.
- Updated `Wiki/index.md`, `kb-registers.md`.

## Judgement calls made, flagged for the owner

- **Did not guess the asset code this time** — asked for the acquisition year/invoice before
 minting `FA2303`, specifically because of the `FA2601` correction two sessions ago.
- **Flagged the expired certificates as a genuine compliance gap**, not just an Open Questions
 bullet — it's in the Key facts table and got its own Task (T007), since "the paperwork says this
 machine's safety testing lapsed 2.5 years ago" is a different order of finding than the usual
 "unconfirmed detail."
- **Did not assume the centralised extraction unit replaces `FA2302`** — logged it as a task to
 confirm (T010) once that unit's own manual arrives, rather than marking `FA2302` superseded on
 an inference.
- **Gave the monthly safety check its own Processes article and Smartsheet sheet**, rather than
 just noting it in the machine's Wiki article — it's a recurring compliance process, which is
 exactly what the `Processes/` folder exists for.

## Open questions carried forward

See `Wiki/Machinery/altendorf-f45-panel-saw.md`, "Open questions" — expired certificates, owning
entity, `FA2302` status, unconfirmed serial number/supplier, and two internal manual inconsistencies
(extraction volume, weight figures) that weren't resolved rather than guessed at.
