---
title: "FA2306 — ABAC GENESIS rotary screw air compressor"
category: Machinery
status: active
sensitive: false
created: 2026-09-18
updated: 2026-09-18
sources:
 - ../../Raw/FISHBONE DRYLINING LTD.pdf
 - ../../Raw/ (asset-label and type-plate photographs, 2026-09-17)
related:
 - ../Suppliers/pneumatic-tools-and-compressors.md
 - ../Processes/barcode-and-scan-event-system.md
---

# FA2306 — ABAC GENESIS rotary screw air compressor

The machine that feeds the pneumatics of `FA2301` (Hebrock F4), `FA2303` (Altendorf F45) and
`FA2304` (Vitap K2-2.0) — and therefore **a single point of failure for the whole workshop**.

**It is also the machine that proved the register could not check itself.** Five sessions were spent
documenting three machines in detail — manuals, fault tables, maintenance schedules, re-commissioning
requirements — while this 15 kW compressor, on which all three depend, sat unregistered and
unmentioned. Nothing inside the knowledge base pointed at it, because nothing in a register can point
at what the register does not contain. It surfaced on 2026-09-17 only because the owner walked the
floor photographing asset labels, and it carried **label `0017`** — the first of the series to be
mapped, on the one machine that had no `FA` code to map it to.

It was registered as **`FA2306`** on 2026-09-18, when its purchase paperwork arrived.

## Key facts

| Item | Value | Source |
|---|---|---|
| Asset code | **`FA2306`** | assigned 2026-09-18 |
| Asset label | **`0017`** | [^2] |
| Manufacturer | ABAC, Montecchio Maggiore, Italy ("made in Italy") | [^2] |
| Model — **two designations, see below** | **GENESIS 15 500L** (type plate) / **GENESIS C67** (proforma) | [^2][^1] |
| Serial number | **ITJ717909** | [^2] |
| Product number | **4152025548** — *identical on plate and proforma* | [^2][^1] |
| Year on type plate | **2023** — this is *manufacture*, not acquisition | [^2] |
| Acquisition | **14/11/2023** (proforma date — see the caveat below) | [^1] |
| Supplier | [Pneumatic Tools & Compressors Ltd](../Suppliers/pneumatic-tools-and-compressors.md) | [^1] |
| Price | **£9,696.00 net**, VAT £1,939.20, **£11,635.20 inc VAT** | [^1] |
| Billed to | **Fishbone Drylining Ltd** — the seventh machine in the same pattern (Task T004) | [^1] |
| Delivered to | **Unit 31**, Point Pleasant Industrial Estate, Wallsend NE28 6HA | [^1] |
| Weight | 455 kg | [^2] |
| Compressor motor | **400 V, 50 Hz, 15 kW, 3-phase** (proforma also states **20 HP**) | [^2][^1] |
| Integrated dryer | 230 V, 50 Hz, 0.58 kW, 1-phase, refrigerant type | [^2] |
| Delivered air | **74 CFM** | [^1] |
| Working / max pressure | **10 bar** | [^2] |
| Max inlet / ambient temperature | 40 °C / 40 °C | [^2] |
| Refrigerant | **R513A, 0.5 kg = 316 kg CO₂e** | [^2] |
| Marks | CE, EAC, WEEE | [^2] |
| Status | In service | — |

## The two model designations — recorded, not resolved

The type plate on the machine reads **ABAC GENESIS 15 500L**. The proforma that bought it reads
**ABAC GENESIS C67 SCREW AIR COMP**. These are not the same string, and this KB does not merge them.

What ties the document to the machine is not the model name at all — it is the **product number
`4152025548`, which appears identically on both**. Every technical figure agrees as well: 15 kW,
10 bar, 3-phase. Only the designation differs, which is consistent with a vendor sales code sitting
alongside a manufacturer's plate designation — but that is an explanation, not evidence, and it is
recorded here as an open point rather than asserted.

## What the purchase document is, stated plainly

The document is a **proforma invoice**, and it says so twice: *"PROFORMA INVOICE. THIS IS NOT A VAT
RECEIPT"* and *"PROFORMA INVOICE IS VALID FOR 30 DAYS"*.

**A proforma evidences the order, not the payment and not the delivery.** That matters, because this
KB's asset codes encode the *acquisition* year and the whole `FA2601`→`FA2301` lesson exists to stop
a code being assigned on an assumed year.

Two things make **2023** safe here regardless:

1. The proforma's own validity window runs **14/11/2023 – 14/12/2023**, entirely within 2023. Payment
   against this document could not have fallen in 2024 without a fresh proforma being issued.
2. The other five machines were invoiced on **09/11/2023**, five days earlier — the compressor was
   bought in the same fit-out.

Task T019's stated closing condition was *"the purchase invoice **or any dated purchase
paperwork**"*, so it closed on the terms it set itself. **The VAT invoice is still wanted** and would
settle payment properly; its absence is recorded, not glossed.

The `Purchase Date` on the Machinery Register row is therefore **the proforma date**, not a confirmed
payment or delivery date, and the row says so.

## Air supply and what the machines ask of it

The proforma's **74 CFM** is the first delivered-air figure this KB has held for the compressor — the
type plate carries none at all.

> **74 CFM ≈ 2,095 L/min.** *My arithmetic, at 28.3168 L/min per CFM — not a manufacturer statement.*
> The document does **not** say whether this figure is free air delivery or displacement, and the two
> are not interchangeable.

Against that, what the three machines are documented to want:

| Machine | Pressure | Consumption | Note |
|---|---|---|---|
| `FA2301` Hebrock F4 | **≥ 7 bar** | ~340 L/min | Its own pressure switch E-stops the machine below ~3.5 bar |
| `FA2303` Altendorf F45 | **8 bar** | *not recorded in this KB* | Air quality **ISO 8573-1:2010 [7:4:-]**; water separator + 40 µm filter required; hold-down gives 1000 N at 6 bar |
| `FA2304` Vitap K2-2.0 | **6–8 bar** | 750 NLt/min max | — |

The two machines whose consumption is recorded come to roughly **1,090 L/min**. **That is not a
total** — the F45's air consumption is not in this KB, so no headroom conclusion should be drawn from
the comparison yet. The pressure side is not in doubt: the plate rates the unit to **10 bar** against
a highest demand of 8 bar.

### The 5.4 bar reading was never a finding

A gauge photographed on 2026-09-17 read **5.4 bar**, and this KB recorded it as a low-pressure concern
"below what all three machines ask for". **That was wrong.** The owner corrected it the same evening:
**the compressor was switched off when it was photographed**, so 5.4 bar was residual pressure standing
in the receiver, not delivered line pressure, and it says nothing about what the machines get when
running.

The correction is kept visible rather than quietly deleted, because the mistake was of a specific and
repeatable kind — reading a number off a photograph and inferring an *operating* condition without
establishing what state the machine was in. It is the origin of the rule in `CLAUDE.md` §3: **a reading
is only a reading of the state the thing was actually in.**

Delivered pressure at each machine under load remains **unmeasured**, and a reading is still worth
taking — but as routine verification, **not** as the follow-up to a suspected fault. There is no
suspected fault.

## Maintenance — nothing is logged

The manufacturer's yellow service label on the machine carries a printed log table with columns
*Official Specialist / Latest Service / Running Hours / Type of Service*. **In the photograph that
table is completely blank.**

ABAC's own intervals, printed on that same label:

| Interval | Part |
|---|---|
| **MAX 2,000 hours (1 year)** | service kit **2200903268** |
| **MAX 4,000 hours (2 years)** | service kit **2200903269** |
| FluidTech lubricant | **6215715900** |

Note the wording — **2,000 hours *or* 1 year, whichever comes first**. A shop running one shift hits
the yearly limit long before the hours.

**A blank label is not proof the machine is unserviced.** Servicing may sit on an engineer's
paperwork, an invoice, or nowhere at all. That is the question in Task **T020**, and there is now an
obvious place to ask it: the supplier is a compressor specialist trading since 1963.

Why it matters beyond this machine: an unserviced screw compressor degrades *quietly*. Air quality
falls, moisture carries over, pressure sags — and the symptoms appear **at the machines**, not at the
compressor. The F45's ISO 8573-1 air-quality specification exists precisely to prevent what a
neglected dryer produces.

**`FA2306` is not yet on the Maintenance Schedule sheet.** It joins once T020 establishes whether any
service has been done, so that the intervals are anchored to a real last-service date rather than a
guessed one.

## Two compliance questions, both open

**1. The air receiver — Task T021.** The plate's model string reads `GENESIS 15 500L`, and read plainly
the "500L" is a 500 litre air receiver. **That is a reading of a model name, not a specification** —
the same move that produced the `STK 10000` caveat, and it is labelled here for the same reason.
Neither the plate nor the proforma states a receiver volume anywhere.

If there *is* a receiver of roughly that size at 10 bar, it is a pressure system well above the
commonly cited 250 bar-litre threshold, and the Pressure Systems Safety Regulations 2000 would call
for a **written scheme of examination** by a competent person plus examination in accordance with it.
**This KB holds no record of such a scheme, or of any examination.** That absence is a question, not a
conclusion — a scheme may well exist in insurance paperwork this KB has never seen. **This is not
regulatory advice.** One photograph of the receiver's own plate converts the whole question from
inference to fact.

**2. F-Gas — below the threshold on these figures, but confirm.** The integrated dryer holds **R513A,
0.5 kg, stated on the plate as 316 kg CO₂e** — that is **0.316 tonnes**, against the 5-tonne CO₂e
threshold at which periodic leak checking becomes mandatory for stationary refrigeration equipment. On
these figures the unit sits well below it. **To be confirmed by someone qualified**; thresholds and
the regulations themselves change. Either way, work on the refrigerant circuit and end-of-life
disposal must be done by suitably certified personnel. Task **T020**.

## Open questions

- **The VAT invoice** for this machine — the proforma evidences the order, not the payment.
- **Has it ever been serviced?** (T020) The label says no; the label may not be the record.
- **What is the air receiver, and does it need a written scheme of examination?** (T021)
- **Delivered pressure and flow at each machine under load** — unmeasured. Routine, not urgent.
- **Does the F45's required water separator and 40 µm filter exist in the installation?** Never checked.
- **Who owns it?** Billed to Fishbone Drylining Ltd, like every other machine here (T004).
- **Was it in Unit 31 while the machines it feeds were in Unit 32?** The proforma says *"delivery as
  per inv address"* and that address is **Unit 31**, dated 14/11/2023 — five days after `FA2301`,
  `FA2303` and `FA2304` were invoiced for delivery to **Unit 32** (invoice 100153). Both units were in
  use by the group in November 2023. A proforma is not a delivery note, so this is evidence, not a
  conclusion — but it is worth putting to the owner, and it bears on T004 and T018.
- **The second sticker** beside the type plate reads **"29 / Compressor"** with its own QR code — an
  installer's or third party's numbering, origin unknown. Not the group asset label, which is `0017`.
- **No operating manual.** Without one there are no filter-change criteria or fault table beyond the
  service label's intervals.

## What was deliberately not recorded

The proforma carries **bank details (sort code and account number)** and a **personal mobile number**.
Neither was copied into this article, the Machinery Register, or the Document Register — per
`CLAUDE.md` §6a. Recorded here so the omission reads as a decision rather than an oversight, the same
way it was for the MWM quotation.

---

[^1]: `Raw/FISHBONE DRYLINING LTD.pdf` — Pneumatic Tools & Compressors Ltd **proforma invoice 208027**,
order no 206542, 14/11/2023. Drive `1_mdXdvr5QgIrYIFuRHz1tbQStTs3qGa-`.
[^2]: Owner photographs of the machine's type plate, asset label and service label, `Raw/`,
2026-09-17.
