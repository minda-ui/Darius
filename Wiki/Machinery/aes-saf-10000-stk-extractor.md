---
title: "AES SAF 10,000 STK — Fine Dust Extractor (centralised)"
category: Machinery
status: active
sensitive: false
created: 2026-09-17
updated: 2026-09-17
sources:
 - ../../Raw/Invoice 22473.pdf
 - ../../Raw/Fishbone Drylining - AES 10,000.pdf
 - ../../Raw/AES Extractor.pdf
related:
 - ../Suppliers/markfield-woodworking-machinery.md
 - ../Machinery/hebrock-f4-next-edge-bander.md
 - ../Machinery/altendorf-f45-panel-saw.md
 - ../Machinery/vitap-k2-panel-saw.md
---

# AES SAF 10,000 STK — Fine Dust Extractor (centralised)

The workshop's asset `FA2402`: a single centralised three-phase fine dust extractor serving the
whole shop, bought in October 2024. It replaced **both** Inventair MK1 and MK2 units (`FA2302` and
`FA2305`), which have since been sold — so this is now the only extraction plant on site, and every
machine that produces dust depends on it.

**This article is unusual, and the reason matters.** For the three production machines, the KB has
full manufacturer's manuals: installation procedures, maintenance intervals, fault tables. For this
machine it has **a sales quotation, an invoice and a control-panel schematic, and no operating
manual at all.** Everything below is drawn from commercial documents. What that gets you is a
specification; what it does not get you is a maintenance schedule, filter-change criteria, safety
instructions or a fault table. `FA2402` is therefore **registered but not yet inside the
maintenance or troubleshooting systems** — see Open questions.

## Key facts

| Item | Value | Source |
|---|---|---|
| Asset code | `FA2402` (locally self-assigned 2026-09-17; acquisition year evidenced from the invoice **before** the code was assigned) | — |
| Asset label no. | `0019` — pre-printed "PROPERTY OF FISHBONE GROUP" tag | owner photograph, 2026-09-17 |
| Product designation | **AES SAF 10,000 STK** (quotation) / "AES STK 10000 DUST EXTRACTOR" (invoice) | [^1][^2] |
| Manufacturer | AES Elektronik Makina (Turkey) | [^2] |
| Serial | **A-077** | [^1] |
| Supplier stock code | T11021 | [^1] |
| Supplier | [Markfield Woodworking Machinery Ltd](../Suppliers/markfield-woodworking-machinery.md) | [^1][^2] |
| Machine type | Centralised fine dust extractor (bag/cartridge filter, direct-drive fan) | [^2] |
| **Extraction capacity** | **10,000 m³/h** | [^2] |
| Motor | 11 kW / 15 HP, **direct drive**, star-delta starter | [^2] |
| Suction connection diameter | **355 mm** | [^2] |
| Filters | **64 pcs, Ø160 × 940 mm**; total filter surface **30.22 m²** | [^2] |
| Waste collection | 3 metal buckets | [^2] |
| Dimensions | 1200 × 3170 × 2330 mm | [^2] |
| Weight | 720 kg | [^2] |
| Body construction | 1.2 mm sheet; propeller plate and blades ≥3 mm, metal, dynamically **and** statically balanced | [^2] |
| Guarding | **Part Holder** — stops parts larger than 25 × 25 mm reaching the propeller; protects fan balance and reduces fire risk | [^2] |
| Conformity | CE standards claimed by the vendor; design registered. **No Declaration of Conformity has been seen** | [^2] |
| Quotation date | 02/10/2024 (salesperson Taylor Preston) | [^2] |
| Purchase date | **08/10/2024** (invoice 22473 — six days after the quotation, at identical figures) | [^1] |
| Purchase price | £5,950 + £400 delivery = **£6,350 net**, £1,270 VAT, **£7,620 inc VAT**. Marked *paid in full*, which satisfies the invoice's retention-of-title clause | [^1][^2] |
| Payment terms quoted | 20% deposit, 80% balance prior to delivery | [^2] |
| Purchased by / billed to | **Fishbone Drylining Limited** (now Fishbone Construction Ltd) — *not* AMFA Furniture Ltd. Same pattern as every other machine; see Open questions | [^1] |
| **Location — current** | **Unit 31**, Point Pleasant Industrial Estate, Wallsend, Tyne and Wear NE28 6HA | owner, 2026-09-17 |
| Location — as delivered (2024) | **Unit 31**, same address. Unlike `FA2301`/`FA2303`/`FA2304`, this machine was delivered straight to the unit the workshop now occupies — see "What the delivery date implies" below | [^1] |

## What the vendor did *not* supply

Two clauses on the quotation are recorded verbatim, because between them they decide who owns the
risk on everything downstream of the fan:

> *"Our machinery is not supplied with electrical cabling, extraction hose or blades"*

> *"You are responsible for the electrical connection of your machinery, we do not electrically
> connect machinery on-site."*

The quotation also notes *"Customer has forklift for unloading"* — so offloading was the buyer's
job too.

**The consequence is the single most important fact in this article.** The ductwork, the hose runs,
the three-phase electrical connection and the commissioning were all the group's own work, carried
out by persons unknown, to a design that was never recorded. **Nothing about that installation
exists anywhere in this KB.**

A rated capacity of 10,000 m³/h is a *test-condition* figure for the fan alone. What each machine
actually receives at its own port is decided by duct diameter, run length, bend count, blast-gate
discipline and filter loading — none of which is documented. The machines have also since been
moved to Unit 31, which changes every duct run again.

## Is it big enough? — the arithmetic, and its limits

Rated capacity is **10,000 m³/h**. Against that, the demand this KB can actually evidence:

| Machine | Stated requirement | Converted to m³/h |
|---|---|---|
| `FA2304` Vitap K2-2.0 | ~2000 m³/h, stated directly in its manual | **~2,000** |
| `FA2303` Altendorf F45 | ≥20 m/s through the ø140 mm connection | **~1,110** — *my own arithmetic, see below* |
| `FA2301` Hebrock F4 | ≥25 m/s through a ø140 mm port | **cannot convert** — the manual's required-volume figure is illegible in the source scan |

**The F45 figure is derived, not quoted.** ø140 mm is 0.0154 m² of area; 20 m/s through that area is
0.308 m³/s, or about 1,110 m³/h. That is arithmetic performed here, **not a manufacturer's
specification**, and it is flagged as such wherever it appears. The Hebrock's port is the same
nominal diameter and it wants a *higher* velocity, so its figure would be larger again — but its
manual's own stated volume could not be read, and it is not being inferred from the F45's.

So: known demand of **at least ~3,100 m³/h**, plus the Hebrock, against 10,000 rated. On paper, with
all three machines open at once, the unit is comfortably large.

**On paper is the operative phrase.** See the section above. The number that matters is the one
measured at each machine's port, and it has never been taken.

## One figure that does not reconcile

The quotation lists **"Dust absorption rate 40 m/min"**. It is recorded here verbatim and
deliberately **not interpreted**, because it matches neither obvious reading:

- As **inlet velocity**: 10,000 m³/h through a 355 mm duct (0.099 m²) is about 28 m/s — i.e. roughly
  1,680 m/min, not 40.
- As **filter face velocity**: 10,000 m³/h over 30.22 m² is about 331 m/h, or about **5.5 m/min** —
  not 40 either.

It may be a translation artefact, a different measurement point, or a specification for something
else entirely. **Do not use this figure for any calculation** until the vendor or a real manual
explains what it measures.

## "SAF" — resolved, and worth recording

`Raw/AES Extractor.pdf` — the control-panel electrical schematic — is drawn for **SAF Technical
Ltd**, a name that appears nowhere on the invoice. Read on its own it looks like an unidentified
fourth party in the supply chain.

The quotation resolves it: the machine's full product designation is **"AES SAF 10,000 STK"**. *SAF
is part of the product name*, which is why the panel drawing carries it. **AES Elektronik Makina** is
the manufacturer; **Markfield** is the UK seller. There is no mystery third company.

Recorded because the alternative reading was plausible and would have sent someone chasing a
company that has nothing to do with this machine.

## What the delivery date implies

This machine was **invoiced to Fishbone Drylining Ltd and delivered to Unit 31 in October 2024** —
approximately **twenty months before** AMFA Furniture Ltd's Unit 31 lease was signed on 25 June
2026.

That is evidence about the shape of the "2026 move", which the rest of this KB has treated as a
relocation into new premises. It suggests instead that **the group already occupied Unit 31 in 2024,
and the 2026 lease formalised AMFA's tenancy of a unit that was already in use**. Note that
`FA2301`/`FA2303`/`FA2304` were delivered to **Unit 32** in 2023, so both units were evidently held
at different times.

**This is recorded as evidence, not as a conclusion.** The lease body has not been seen and the
intercompany arrangements sit outside this KB (Task T004).

## Consumables

Known from the quotation, and the only maintenance-adjacent information available:

- **64 filters, Ø160 × 940 mm** — no material, grade, or change interval stated.
- **3 metal waste buckets** — no capacity stated.

That is enough to build a spare-parts line, and **not** enough to build a maintenance schedule: a
filter-change schedule needs either an interval or a differential-pressure trigger, and the
documents give neither.

## Open questions

- **What does each machine actually receive?** (Task T014, rewritten 2026-09-17.) The unit is rated
  10,000 m³/h but the vendor supplied no ducting, no cabling and no on-site connection, and the
  installation is undocumented. **Closing action: an anemometer velocity reading at each machine's
  port**, compared against the Hebrock's ≥25 m/s, the F45's ≥20 m/s and the Vitap's ~2000 m³/h. One
  visit closes this and the extraction half of the post-move re-commissioning question (Task T018).
- **A real operating manual.** Until one exists this machine cannot join the Maintenance Schedule or
  the Fault Log — there are no intervals, no filter-change criteria, no fault table and no safety
  instructions. Request from Markfield or AES.
- **Was it ever commissioned, and by whom?** No electrician's record, no commissioning sheet, no
  test results. The vendor explicitly did not do it.
- **Is extraction interlocked to the machines?** The F45's manual requires extraction interlocked to
  machine power via a potential-free contact or current transformer; the Hebrock's allows it. Whether
  either interlock was ever wired is unknown — and the control-panel schematic is the one document
  that might answer it, if read properly by someone competent.
- **No Declaration of Conformity has been seen.** The quotation claims CE standards; that is a
  vendor's marketing statement, not a DoC. Compare with `FA2301`, where a genuine EC Declaration
  naming the exact machine number exists.
- **Owning entity unconfirmed** — billed to Fishbone Drylining Ltd, operating in AMFA Furniture
  Ltd's leased premises (Task T004).
- **Filter material and grade unknown** — relevant to whether the unit is suitable for the fine dust
  it is named for, and to any COSHH assessment of hardwood dust.
- **Banking details on the quotation were deliberately not recorded** here or anywhere in this KB.
  Stated so the omission reads as a decision, not an oversight.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-17 | `FA2402` registered in the Machinery Register from invoice 22473; acquisition year 2024 evidenced before the code was assigned; asset label `0019` matched to it, resolving which extractor the owner had photographed | Session 14, entry "Networking correction and barcode scoping" |
| 2026-09-17 | Full specification sourced from the MWM quotation of 02/10/2024, discharging T014's standing caveat that "10000" was only a reading of the model name; the vendor's exclusion clauses recorded; "SAF" resolved; the 40 m/min figure recorded as unreconciled | Session 14, same entry |
| 2026-09-17 | Article created | Session 14, same entry |

## Sources

[^1]: [Invoice 22473, 08/10/2024](<../../Raw/Invoice 22473.pdf>) — Markfield Woodworking Machinery Ltd to Fishbone Drylining Ltd; "1 X NEW AES STK 10000 DUST EXTRACTOR", serial A-077, stock code T11021, marked paid in full
[^2]: [MWM machinery quotation, 02/10/2024](<../../Raw/Fishbone Drylining - AES 10,000.pdf>) — specification table, construction notes, exclusion clauses and payment terms. *Note: the extracted text opens with the stray line "Breitbandschleifmaschine KÜNDIG Topiq-2 1100", almost certainly a leftover template title from an unrelated wide-belt sander; it has no bearing on this machine but is recorded because it is on the document*
[^3]: [AES control-panel schematic](<../../Raw/AES Extractor.pdf>) — 5-page scanned electrical drawing, drawn for SAF Technical Ltd. **Not an operating manual**: no intervals, no fault table, no safety instructions
