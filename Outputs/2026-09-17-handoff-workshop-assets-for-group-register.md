# Handoff — Workshop assets for the group asset/label register

_Prepared by Darius (Workshop Operations Assistant) on 2026-09-17, at the owner's request, for
**Alex** to seed the group-wide asset/label register. This KB does not write to that register — see
`CLAUDE.md` §6a. This file is the record of what was handed over._

**Why this exists.** The workshop received pre-printed asset labels reading *"PROPERTY OF FISHBONE
GROUP / TEL: 0191 605 2945"*, each carrying a QR code and a four-digit number (the two seen were
`0017` and `0018`). The owner decided on 2026-09-17 to hold **one group-wide register** of these
labels, built by Alex, rather than a per-KB list.

---

## The boundary — what goes where

| | Group register (Alex) | Workshop KB (Darius) |
|---|---|---|
| Label no. (`0017`) | the master list | join key only |
| One-line description | yes | yes, in full |
| Owning company / source KB | yes | yes |
| Location | yes | yes |
| Serial, manuals, maintenance schedule, fault history, finance, warranty | no | yes — 33 columns of it |

**The join key is the label number.** The group register answers *"what is 0017, and whose is it?"*;
the Workshop KB answers *"what is wrong with it and when was it last serviced?"* Mirroring the detail
columns across both would recreate the dual-source problem this KB corrected in v8/v9 — one fact, one
home.

The Workshop Machinery Register (`1754351980906372`) gained an **`Asset Label No.`** column on
2026-09-17 to hold the join key. It is deliberately separate from the `FA` asset code: **the label
number is the physical tag, the `FA` code is this register's ID.** Assets are never renumbered to
match labels.

---

## Proposed columns for the group register

`Asset Label No.` · `Asset Code` · `Description` · `Manufacturer` · `Model` · `Serial No.` ·
`Location` · `Status` · `Owning Entity` · `Source of Record` · `Notes`

Offered as a suggestion from the first contributor, not as a specification.

## The five rows

All five are at **Unit 32, Point Pleasant Industrial Estate, Wallsend NE28 6HA** and all are
currently **In service**. Label numbers are unassigned — they cannot be filled until someone
physically applies the stickers.

| Asset Label No. | Asset Code | Description | Manufacturer | Model | Serial No. |
|---|---|---|---|---|---|
| *(unassigned)* | `FA2301` | Edge banding machine | Maschinenbau Hebrock GmbH | F4 next | `F3809` — confirmed |
| *(unassigned)* | `FA2302` | Dust/fume extractor | Inventair | MK1 MTFA | `1971` |
| *(unassigned)* | `FA2303` | CNC sliding-table (panel) saw | Altendorf GmbH | F45 ElmoDrive (two-way tilt) | **none confirmed** — `23-11-12-005` is Altendorf's internal job number, not a serial |
| *(unassigned)* | `FA2304` | CNC boring / drilling / routing centre | VITAP S.p.A. | K2-2.0 | `320070 AT` — invoice-derived only; the manual's own type-plate field is blank |
| *(unassigned)* | `FA2305` | Dust/fume extractor | Inventair | MK2 MTFA | `1696` |

**Source of Record** for all five: Workshop of Furniture Making KB — Drive folder
`1ykYJERaptUNH0FDvkOVU26jh_x_hRtLz`, Smartsheet Machinery Register `1754351980906372`.

---

## Owning Entity — identical for all five, and not to be shortened

> Invoiced to **Fishbone Drylining Limited** (now Fishbone Construction Ltd), **not** AMFA Furniture
> Ltd. Operated by AMFA Furniture Ltd at Unit 32. **Formally unresolved** — Workshop KB Task T004.

Invoices, all dated 09/11/2023:

| Invoice | Ref | Covers |
|---|---|---|
| 100155 | OCN2311184 | `FA2301`, `FA2302` |
| 100153 | OCN231181 | `FA2303` |
| 100154 | OCN231185 | `FA2304`, `FA2305` |

**The physical labels read "PROPERTY OF FISHBONE GROUP". That wording must not be copied into this
column.** It is deterrent and identification labelling — sensible for a batch bought once and used
across every company — but it is not evidence of legal title. If assets land in the register as
"Fishbone Group" because that is what the sticker says, the ambiguity is baked in estate-wide and
becomes far harder to unpick. Same discipline as the `FA2601`→`FA2301` correction: be precise before
the number is assigned, not after.

The same pattern holds beyond the machinery: the SmartCABINET software purchase (Kosmosoft
Engineering S.r.l., contract 22910, €1,000, 10/09/2026) was **also** billed to Fishbone Drylining Ltd
rather than AMFA — see the Fishbone Construction KB, `Wiki/Suppliers/kosmosoft-smartcabinet.md`.

---

## Row-level caveats

- **`FA2302`** — status under review. It may be superseded by `FA2305`, but that is **suspected, not
  confirmed** (Task T014). Do not mark it disposed on this KB's say-so.
- **`FA2303`** — no serial number appears in the operating manual, the ElmoDrive manual or the spare
  parts manual; it must be read off the physical type plate (Task T009). It also carries a live
  compliance issue — DGUV/GS/machine-safety certificates HM 220023-25 **expired 22.02.2024** (Task
  T007). That detail stays in the Workshop KB; noted here only so nobody is surprised by it.
- **`FA2304`** — serial is invoice-derived; confirm against the type plate (Task T012).
- **`FA2305`** — no manual received yet, so it is not in the maintenance or troubleshooting systems.

## A sixth asset, now evidenced — Brother TD-4420DN label printer

Order receipt **SOA2606351** from **Printerland** (Computer Risk Management Ltd, trading as
Printerland.co.uk, Altrincham), dated **9 May 2024**:

| Item | Product code | Price ex VAT |
|---|---|---|
| Brother TD-4420DN label printer | `TD4420DNZU1` | £211.58 |
| Brother direct thermal die-cut label roll, 102 × 50 mm | `BDE1J050102102` | £14.45 |
| Brother direct thermal die-cut label roll, 102 × 152 mm | `BDE1J152102058` | £5.57 |
| | Subtotal / VAT / **total inc. VAT** | £231.60 / £46.32 / **£277.92** |

Acquisition year is therefore **2024**, which makes the code **`FA2401`** — the first 2024 asset in
this register, not a continuation of the 2023 block. *This is precisely why the code was withheld: the
printer first came to notice in 2026, and numbered on that assumption it would have become `FA26xx` —
repeating the `FA2601`→`FA2301` mistake exactly.*

**Its ownership trail is messier than the machines', and is recorded unresolved rather than tidied:**

| Role | Named party |
|---|---|
| Ordered from mailbox | `minda@fishbonedrylining.co.uk` — Fishbone Drylining Ltd |
| **Invoiced to** | **Mindaugas Gaudiesius personally**, 6 Beverley Place, Wallsend NE28 7BH — an individual at a residential address, not a company |
| **Shipped to** | **Fishbone Waste, Unit 31**, Point Pleasant Industrial Estate, Wallsend NE28 6HA |
| In use at | Unit 32, the workshop — **assumed, not confirmed** |

Four different parties, and none of them is AMFA Furniture Ltd. Note also that this document is an
**order receipt, not an invoice** — the email states "an invoice will also follow", and that invoice
has not been seen. The order was paid by credit/debit card at the time.

**Not registered yet.** Whether this belongs on the *workshop's* register at all depends on where it
physically sits: the paperwork points at Unit 31 and Fishbone Waste, not Unit 32 and the workshop.
Pending the owner's confirmation.

---

## What this KB needs back

The **label number assigned to each machine**, once the stickers are physically applied. They will be
recorded in the Machinery Register's `Asset Label No.` column, which exists and is waiting.

Also outstanding, and relevant to whoever builds the register: **what the labels' QR codes actually
decode to** has not been established. If they encode the printed number, scanning resolves straight
through the register. If they encode a label vendor's own URL, the printed number is the usable
identifier instead. This has not been tested.

## Sources

- Smartsheet **Machinery Register - Database** `1754351980906372` — the five rows, as at 2026-09-17.
- `Wiki/Machinery/altendorf-f45-panel-saw.md` — `FA2303` serial, certificates, invoice 100153.
- `Wiki/Machinery/vitap-k2-panel-saw.md` — `FA2304`/`FA2305`, invoice 100154.
- `Wiki/Machinery/hebrock-f4-next-edge-bander.md` — `FA2301`/`FA2302`, invoice 100155.
- `Raw/Fishbone Drylining Ltd Mail - Order Receipt SOA2606351.pdf` — the Brother TD-4420DN order
  receipt, Printerland, 9 May 2024; the source for every printer figure and address above.
- Fishbone Construction KB, `Wiki/Suppliers/kosmosoft-smartcabinet.md` — the SmartCABINET purchase
  (read-only to this KB; cited, not copied).
- Owner's photograph of the asset labels, 2026-09-17.
