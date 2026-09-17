---
title: "Brother TD-4420DN — Direct Thermal Label Printer"
category: Machinery
status: active
sensitive: false
created: 2026-09-17
updated: 2026-09-17
sources:
 - ../../Raw/td-4210d_4410d_4420dn_4520dn_uke_ug_a.pdf
 - ../../Raw/Fishbone Drylining Ltd Mail - Order Receipt SOA2606351.pdf
related:
 - ../Processes/barcode-and-scan-event-system.md
---

# Brother TD-4420DN — Direct Thermal Label Printer

The workshop's asset `FA2401`, and the only non-machine-tool on the register: a 203 dpi networked
direct-thermal desktop label printer, bought in May 2024. It is registered here because it is the
hardware the **barcode system** depends on for printing anything the shop generates itself — part
labels off SmartCABINET, offcut tags, job travellers.

**The first 2024 asset in this register, and the reason it is not `FA26xx`.** The printer came to
notice in September 2026 and the obvious move was to code it as a 2026 acquisition. That is exactly
the mistake made once already with `FA2301` (registered `FA2601` on an assumed year, then corrected).
The code was withheld until the order receipt evidenced **9 May 2024**, and only then assigned.

## Key facts

| Item | Value | Source |
|---|---|---|
| Asset code | `FA2401` (locally self-assigned 2026-09-17; acquisition year evidenced **before** assignment) | — |
| Asset label no. | **None applied yet** — see Open questions | — |
| Manufacturer / model | Brother TD-4420DN | [^1][^2] |
| Print technology | **Direct thermal** (no ribbon; the media itself is heat-sensitive) | [^1] |
| Resolution | 203 dpi | [^1] |
| Max print width | **832 dots** (~104 mm). The TD-4520DN sibling does 1280 | [^1] |
| Interfaces | USB, serial, **and LAN 10BASE-T/100BASE-TX** — the wired network port is on the `4420DN`/`4520DN` models only, not the 4210D/4410D | [^1] |
| Order reference | Printerland order **SOA2606351** | [^2] |
| Purchase date | **9 May 2024** | [^2] |
| Purchase price | Printer £211.58 ex VAT; with two label rolls £231.60 + £46.32 VAT = **£277.92 inc VAT** | [^2] |
| Media bought with it | 102×50 mm direct-thermal die-cut roll (£14.45) and 102×152 mm die-cut roll (£5.57) | [^2] |
| Purchased by / billed to | **No company named.** Billed to Mindaugas Gaudiesius by name, at 6 Beverley Place — the companies' **registered office**. See "The billing trail" | [^2] |
| Shipped to | **Fishbone Waste, Unit 31** — that unit's occupant in 2024 | [^2] |
| **Location — current** | **Unit 31**, Point Pleasant Industrial Estate, Wallsend NE28 6HA — the workshop | owner, 2026-09-17 |
| ZPL / EPL emulation | **Unverified and contradicted** — see below | [^1] |

## The billing trail — recorded, not resolved

Four different parties appear on one £277.92 order:

1. **Ordered from** the Fishbone Drylining mailbox.
2. **Billed to** Mindaugas Gaudiesius *personally, by name* — no company on the billing line — at
   **6 Beverley Place**, which is the companies' **registered office**. *(An earlier version of this
   KB described that address as "residential" purely from the look of it. That was an unsourced
   inference and it was wrong; the owner corrected it. See `CLAUDE.md` §3.)*
3. **Shipped to** Fishbone Waste at Unit 31.
4. **Now used by** the AMFA Furniture Ltd workshop, in that same Unit 31.

No company is named as the buyer, so **the owning entity is genuinely unconfirmed** — this is the
`FA2401` instance of Task T004, and unlike the machines (all cleanly invoiced to Fishbone Drylining
Ltd) there is no company on the paperwork at all.

**It is also an order receipt, not an invoice.** The document itself says *"an invoice will also
follow"*. That invoice has never been seen.

## Suitability — what it is and is not good for

The decisive property is **direct thermal**. There is no ribbon; the image is burned into
heat-sensitive media, and Brother's own manual is blunt about what that means:

> *"Do not expose the RD Roll to direct sunlight, high temperature, high humidity, wind, or dust as
> it may cause labels to peel off or discolour"*

> *"Scratching the printed surface … can cause the colour to change or fade."*

A workshop is warm, dusty and full of things that scrape. So:

| Use | Verdict |
|---|---|
| **Part labels** on panels moving through the shop over hours or days | **Good.** The label's job is over before fade matters, and the 102×50 mm stock already owned is a workable size |
| **Job travellers / batch tickets** | **Good**, same reasoning |
| **Offcut rack tags** living for weeks or months in a dusty rack | **Poor** — the label outlives its own legibility |
| **Machine asset labels** | **Not needed, and not suitable.** The group already uses pre-printed durable "PROPERTY OF FISHBONE GROUP" tags; see the [barcode system](../Processes/barcode-and-scan-event-system.md) |

**Useful by-product of the receipt:** the shop already owns 102×50 mm die-cut direct-thermal stock,
so part-label trials need no purchase.

## The ZPL question — a contradiction, deliberately unresolved

This matters because **SmartCABINET prints barcode labels in ZPL** (confirmed in its release notes).
If this printer speaks ZPL, SmartCABINET can drive it directly and Phase 1 of the barcode system is
mostly a configuration job. If it does not, something has to translate.

The evidence points both ways:

- **Resellers and vendor listings** for the TD-4420DN claim **ZPL II / EPL2 / DPL emulation**.
- **Brother's own User's Guide for this exact model never mentions ZPL anywhere.** It documents only
  Brother's own stack: P-touch Editor, P-touch Template, Transfer Manager, mass-storage `.BIN`/`.BLF`
  command files, and an SDK.
- **Brother's published *ZPL II Emulation Guide* is branded for the TD-4420TN / TD-4520TN** — the
  thermal-**transfer** siblings, not this direct-thermal model.

Recorded as a contradiction rather than resolved by picking the more convenient answer.

**The decisive test takes five minutes:** open the **Printer Setting Tool** and look for an
emulation or `FBPL` tab. If it is there, the printer speaks ZPL; if not, it does not. Alternatively,
send one ZPL label and see what comes out.

## Manual coverage — a real gap

`Raw/td-4210d_4410d_4420dn_4520dn_uke_ug_a.pdf` covers four models (TD-4210D / 4410D / 4420DN /
4520DN), and **only pages 1–77 of 128 were extracted**. Drive's text extraction dropped:

- the **Specifications appendix** (p.113) — so the manufacturer's own spec table has never been read;
- **Routine Maintenance** — so no maintenance schedule can be built from it;
- **Troubleshooting** — so no fault table either.

Stated plainly rather than glossed. The figures in Key facts come from the pages that *did* extract.

## Open questions

- **Does it actually support ZPL?** The decisive test is above. This blocks the design of barcode
  Phase 1 (part labels), because it decides whether SmartCABINET can drive the printer directly.
- **No asset label applied.** `FA2401` is the only registered asset with no physical tag; labels
  `0017`–`0021` all went on machines. Apply the next number in the group series and record it.
- **Owning entity unconfirmed** — no company appears on the billing line at all (Task T004).
- **The actual invoice has never been seen**, only the order receipt.
- **Pages 78–128 of the manual have never been read** — including specifications, maintenance and
  troubleshooting. Re-extract or obtain a clean copy before building any maintenance entry.
- **Is it actually on the network?** It has a LAN port and the workshop is networked, but whether
  this printer is configured, addressed and reachable is not recorded. Relevant because network
  printing is what would let SmartCABINET print to it from the design PC.
- **No maintenance entry exists** (print-head cleaning, platen roller) and none can be written until
  the Routine Maintenance chapter is readable.

## Changes

| Date | Change | Change-log ref |
|---|---|---|
| 2026-09-17 | Assessed for workshop label printing from its User's Guide; ZPL contradiction recorded; **deliberately not registered** at this point, pending evidence of acquisition year | Session 14, entry "Networking correction and barcode scoping" |
| 2026-09-17 | Order receipt SOA2606351 processed — acquisition year 2024 evidenced, so registered as **`FA2401`**, not an assumed `FA26xx`; full billing trail recorded rather than tidied away; location confirmed as Unit 31 by the owner | Session 14, same entry |
| 2026-09-17 | Article created | Session 14, same entry |

## Sources

[^1]: [Brother TD-4210D/4410D/4420DN/4520DN User's Guide](../../Raw/td-4210d_4410d_4420dn_4520dn_uke_ug_a.pdf) — **pages 1–77 of 128 only**; the Specifications appendix, Routine Maintenance and Troubleshooting chapters did not extract
[^2]: [Printerland order receipt SOA2606351, 9 May 2024](<../../Raw/Fishbone Drylining Ltd Mail - Order Receipt SOA2606351.pdf>) — order confirmation from the Fishbone Drylining mailbox; an order receipt, not the invoice
