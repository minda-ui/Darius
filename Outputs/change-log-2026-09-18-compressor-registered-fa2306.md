# Change log — 2026-09-18 — The compressor's purchase paperwork arrived: `FA2306` registered, a pressure-system question raised, and a stale claim found surviving in Smartsheet

_Append-only dated session file (Fishbone Group). See `CLAUDE.md` §4._

## Session 15 — 2026-09-18 (morning): one document closed the only blocking item in the KB

**Owner instruction (Minda):** *"Good morning Darius"* — no specific task. The §0 opening read found a
new file in `Raw/`, uploaded at **05:25 this morning**, and it turned out to be the one document the
KB had been waiting on.

### What arrived

`Raw/FISHBONE DRYLINING LTD.pdf` (468 KB, Drive `1_mdXdvr5QgIrYIFuRHz1tbQStTs3qGa-`) —
**proforma invoice 208027** from **Pneumatic Tools & Compressors Ltd**, Acton Road, Long Eaton,
Nottingham NG10 1FU, dated **14/11/2023**, order no 206542:

> *"1 X ABAC GENESIS C67 SCREW AIR COMP — 20HP 15KW 74 CFM 10 BAR 3 PHASE"*, product **4152025548**,
> **£9,696.00 net**, VAT £1,939.20, **£11,635.20 inc VAT**. Customer: **FISHBONE DRYLINING LTD**,
> Unit 31 Point Pleasant Industrial Estate, Wallsend NE28 6HA. *"Delivery as per inv address."*

This is the purchase paperwork for the **ABAC compressor found on 2026-09-17 to have never been
registered at all** — the machine that feeds the pneumatics of `FA2301`, `FA2303` and `FA2304`.
Task **T019** had named it as *"the only blocking item"* in the whole KB.

### The product number is what closed it, not the model name

The proforma's product number **`4152025548`** is **identical** to the one on the machine's type plate.
That, and not the model designation, is what ties the document to the machine standing in the workshop
— because the model designations **do not match**:

| Source | Designation |
|---|---|
| Type plate on the machine | **ABAC GENESIS 15 500L** |
| Proforma invoice 208027 | **ABAC GENESIS C67 SCREW AIR COMP** |

Every technical figure agrees — 15 kW, 10 bar, 3-phase. Only the string differs. **Recorded as a
contradiction, not resolved into one.** A vendor sales code sitting alongside a plate designation is
the obvious explanation, but that is an explanation, not evidence.

### `FA2306` assigned — and the honest caveat that came with it

Acquisition year **2023** → **`FA2306`** (`FA2301`–`FA2305` taken). Evidenced **before** the code was
assigned, which is the entire point of the `FA2601` lesson — the fourth time that discipline has been
applied, after `FA2305`, `FA2401` and `FA2402`.

**But the document is a proforma, and the KB says so plainly.** It states twice that it is not a
receipt: *"THIS IS NOT A VAT RECEIPT"* and *"PROFORMA INVOICE IS VALID FOR 30 DAYS"*. It evidences the
**order**, not payment and not delivery.

Two things make 2023 safe anyway, and both are written into the record rather than left implicit:

1. The proforma's own validity window runs **14/11/2023 – 14/12/2023**, entirely within 2023. Payment
   against *this* document could not have landed in 2024 without a fresh proforma.
2. The other five machines were invoiced **09/11/2023**, five days earlier — same fit-out.

And T019's own stated closing condition was *"the purchase invoice **or any dated purchase
paperwork**"*, so it closed on the terms it set itself. **The VAT invoice is still wanted**; its
absence is recorded, not glossed. The register's `Purchase Date` cell holds the **proforma date** and
the row says exactly that.

### A new fact the type plate never gave: 74 CFM

The plate carried no delivered-air figure at all. The proforma gives **74 CFM** (and **20 HP**
alongside the plate's 15 kW).

> **74 CFM ≈ 2,095 L/min** — *my arithmetic at 28.3168 L/min per CFM, not a manufacturer statement.*
> The document does **not** say whether this is free air delivery or displacement, and the two are not
> interchangeable.

Against it, the two machines whose air consumption this KB records — Hebrock ~340 L/min, Vitap
750 NLt/min — come to roughly **1,090 L/min**. **That is deliberately not presented as a headroom
conclusion**: the F45's consumption is not in this KB, so it is not a total. The pressure side is not
in doubt — the plate rates 10 bar against a highest stated demand of 8 bar.

### A genuine compliance question, raised as its own task (T021)

The plate's model string reads `GENESIS 15 500L`. Read plainly, the "500L" is a 500 litre air
receiver — and a 500 litre vessel at 10 bar is a pressure system far above the commonly cited
250 bar-litre threshold, which under the Pressure Systems Safety Regulations 2000 would call for a
**written scheme of examination** by a competent person. **This KB holds no record of such a scheme,
or of any examination.**

**But the task does not start there, and that is the point.** *"500L" is a reading of a model name,
not a specification* — precisely the mistake this KB already made once with `STK 10000`. Neither the
plate nor the proforma states a receiver volume anywhere, and the proforma's description does not
mention a receiver at all. So **T021 begins by establishing whether there is a receiver and what it
actually is** — one photograph of its own plate converts the question from inference to fact — and only
then asks about the scheme.

Raised as a separate task rather than folded into T020, because servicing, F-Gas and pressure-system
examination are three different regimes. Flagged prominently per `CLAUDE.md` §3's rule on genuine
compliance findings. **This KB does not give regulatory advice and does not give any here** — it
records that the question is open and that absence of a record is not evidence of absence.

### A stale claim found surviving where the sweep had not reached

While reading the Tasks sheet, **T016 still contained the networking claim the owner corrected on
2026-09-17**:

> *"(2) export it and manually transfer it to the CNC computer **(the two are not networked -
> confirmed)**"*

The 2026-09-17 sweep of that correction covered `CLAUDE.md` and the Wiki articles. **It did not cover
Smartsheet note fields.** Corrected in place, with the correction left visible rather than silently
overwritten — and with the counter-warning kept: a shared network does **not** merge SmartCabinet's
CAM Tools table with TpaCAD's CN Tools catalog, which is still unverified and is exactly what T016
exists to establish.

**Lesson, now in `CLAUDE.md` §3:** *a sweep has to cover every store the claim reached.* The KB's
narrative layer and its live-data layer are two different places, and a correction applied to one is
not applied to the other.

### The premises picture moved — evidence, not conclusion

The proforma's delivery address is **Unit 31**, dated 14/11/2023. Invoice 100153, **five days
earlier**, gives its delivery site as **Unit 32**. Both were re-read this session rather than recalled.

So **the group was using both units in November 2023.** That sits alongside two data points already
held: the Brother printer shipped to *"Fishbone Waste, Unit 31"* in May 2024, and `FA2402` was
delivered to Unit 31 in October 2024.

**What this does not do** is overturn anything. The workshop was at Unit 32; AMFA took the Unit 31
lease on 25/06/2026; both remain evidenced. What it does is make the 2026 lease look less like a
relocation and more like **AMFA formalising a unit the group had already occupied for years** —
which is a question for the lease body and the intercompany side, both outside this KB.

It also raises a new one worth putting to the owner: **if the compressor was delivered to Unit 31 in
November 2023 while the three machines it feeds went to Unit 32, was it in a different building from
them?** *"Delivery as per inv address"* says it was — but a proforma is not a delivery note.

> **⚠ THIS WHOLE SECTION WAS WRONG AND IS RETRACTED — see "Correction, same day" at the end of this
> file.** The owner confirmed the compressor was **delivered to Unit 32**. It is left standing rather
> than deleted because the error, and how it was made, is the point.

### Written this session

| What | Where | Size |
|---|---|---|
| `FA2306` register row | Machinery Register (`1754351980906372`), row `8264104844855172` | — |
| Proforma 208027 | Document Register (`838802392352644`), row `4864414891771780`, `Document No.` = `pending` | — |
| **T019 closed** (`Done`) | Tasks (`4087584374523780`) | — |
| **T021 raised** — air receiver / written scheme of examination | Tasks, row `7869517609437060` | — |
| T020, T004 updated; **T016 corrected** | Tasks | — |
| `Wiki/Machinery/abac-genesis-screw-air-compressor.md` | new | 12,267 B |
| `Wiki/Suppliers/pneumatic-tools-and-compressors.md` | new | 4,881 B |
| `Wiki/index.md` | 23 → **25** articles | — |

**Article filename note:** the machinery article is `abac-genesis-screw-air-compressor.md`, not
`abac-genesis-15-500l-...`. With two competing model designations on the record, baking either into
the filename would have asserted the thing the article explicitly declines to resolve.

### Governance

- **Bank sort code and account number** on the proforma were **deliberately not copied** into the
  register, the Document Register, either Wiki article or this log. So was a **personal mobile number**
  printed on it. Recorded as a decision, not an oversight — the same treatment as the MWM quotation's
  banking details (`CLAUDE.md` §6a).
- **T020 now names a service route** (the supplier is a compressor specialist trading since 1963) with
  the boundary stated in the task itself: *asking* whether the machine was serviced is research;
  **booking the service commits the company to a payment and is the owner's action**. Darius can draft
  the enquiry; it does not send it.
- `Document No.` stays `pending` — shared group Document Register write access is still unconfirmed.

## Still open at session end

- **The VAT invoice** for proforma 208027 — payment and delivery remain unevidenced.
- **Has `FA2306` ever been serviced?** (T020) The yellow label's log table is blank and the machine was
  delivered in November 2023, so the gap is approaching **three years** against a *"2,000 hours or
  1 year, whichever comes first"* interval. A blank label is not proof; ask the supplier.
- **What is the air receiver, and does it need a written scheme of examination?** (T021) One photograph
  of its plate starts the answer.
- **`FA2306` is not on the Maintenance Schedule** — it joins once T020 anchors the intervals to a real
  last-service date rather than a guessed one.
- **No operating manual for `FA2306`**, so no filter-change criteria and no fault table beyond the
  service label.
- **Does the F45's required water separator and 40 µm filter exist in the installation?** Never checked;
  one trip to the compressor answers this, T020 and T021 together.
- **Delivered pressure and flow at each machine under load** — still unmeasured. Routine verification,
  **not** the follow-up to a fault. *The 5.4 bar reading was never a finding: the machine was off.*
- **Was the compressor in Unit 31 while the machines it feeds were in Unit 32?** New question, above.
  *Answered later the same day: no — see the correction below.*
- **The second sticker** on the compressor — *"29 / Compressor"* with its own QR — origin still unknown.
- Everything carried forward from Session 14 and unaffected by today: the anemometer readings (T014 /
  T018), the QR payload blocking barcode Phase 1, the `STK 10000` manual, `FA2303`'s expired
  certificates (T007) and first monthly check (T008), the Inventair disposal dates and proceeds, the
  Unit 31 lease body, `FA2401`'s missing asset label, the partial git mirror, and the non-bidirectional
  `related:` links.

---

## Correction, same day — the delivery address was not a delivery record

The owner corrected the one thing in the session above that I had inferred rather than read:

> *"Compressor was all the time unit 31, it was delivered to unit 32."*

**The compressor was delivered to Unit 32**, where `FA2301`, `FA2303` and `FA2304` already were. The
Unit 31 on proforma 208027 is the **billing and correspondence address**.

**What I did wrong.** The proforma prints **"DELIVERY AS PER INV ADDRESS"**. I read that as a record of
where the machine physically went, and then built on it — concluding in the section above that *"the
group was using both units in November 2023"*, and treating that as new evidence for T004 that pushed
the premises picture back a year earlier than `FA2402`'s October 2024 delivery.

**That conclusion is withdrawn.** A supplier's boilerplate describes an intention at the moment of
quoting, not an event. **Nothing in this KB now places the group in Unit 31 before 2024** — the two
surviving data points are `FA2402` delivered to Unit 31 in October 2024, and `FA2401` shipped to
"Fishbone Waste, Unit 31" in May 2024. Both stand; neither is a 2023 data point.

**What it does settle.** The open question *"was the compressor in a different building from the three
machines it feeds?"* is **answered: no.** It arrived with them and has moved with them.

**One clause I have not resolved, and have labelled rather than guessed.** I read *"was all the time
unit 31"* as referring to the **paperwork** address being Unit 31 throughout, not the machine's physical
location. That reading is mine. It is flagged as a reading in the register note, the Document Register
note and the machine's article, so that if it means the opposite, the correction lands in one place.

**This is the sixth unsourced inference corrected in two days**, and the same family as the 5.4 bar
gauge: treating a mark on a page as a record of the physical world. New `CLAUDE.md` §3 lesson — **a
printed delivery clause is not a delivery note**; where a document gives an address, record *which*
address it is, and if the document does not say, say that.

**Swept through every store the claim reached** — the v14 lesson applied to its own author, one day
later:

| Store | What changed |
|---|---|
| Machinery Register, `FA2306` row | Delivery paragraph rewritten; the withdrawn inference named |
| Document Register, proforma 208027 row | "Cite this document for the order, the price and the specification — not for where the machine went" |
| Tasks, **T004** | The "both units in use in November 2023" block replaced with the retraction and what survives |
| `Wiki/Machinery/abac-genesis-screw-air-compressor.md` | New section "Where it was delivered — a correction"; Key facts row now reads Unit 32; the open question struck through as answered |
| `Wiki/Suppliers/pneumatic-tools-and-compressors.md` | Delivery line reframed as a billing address |
| `CLAUDE.md` | **→ v15**: §7 machine entry and T004 bullet corrected, new §3 lesson |

## Also produced — `Outputs/2026-09-18-outstanding-items.md`

An outstanding-items list for the owner, prepared on request at the end of the session. **21 tasks
raised, 4 closed, 17 open**, ordered by *what it takes to close each item* rather than by task number.
Its headline: **eight open items close with one walk round the workshop** — the QR payload, the air
receiver's plate, the compressor's service label, an anemometer reading at each extraction port, the
F45's water separator and filter, two type plates, and an asset label for the Brother printer. It also
flags **T010 as answered and ready to close**, and separates genuine compliance items from recorded
debts that are deliberately not being fixed.

---

## Later the same day — four more `Raw/` deliveries, two tasks closed, and a lesson about our own filing

The compressor work above finished mid-morning. What followed came from the owner walking the floor
with a phone, and it closed more than the documents did.

### The QR payload — barcode Phase 1 unblocked

A screenshot of a phone camera decoding a tag from an unapplied label sheet read **`Text: 0027`**.

**The QR payload is the bare four-digit label number as plain text** — no URL, no prefix, no company
name, no `FA` code, leading zeros preserved. *One tag was scanned; that the series behaves identically
is an inference from them being one printed batch, and is labelled as such. A second scan on an applied
tag would settle it.*

**It vindicates the two-namespace design rather than merely confirming it.** A scan yields a *label
number*, which has to be looked up against the Machinery Register's `Asset Label No.` column to reach
an `FA` code — exactly the structure documented in Phase 0. Three constraints fall out, one of them a
proposal rather than a decision:

1. The payload is **not self-describing** — a bare `0027` says nothing about what kind of thing it is.
2. **A disambiguation rule will be needed** once part labels exist. *Proposed, not decided:* bare
   four-digit numeric = group asset label; anything else = part or offcut.
3. **Leading zeros must never be stripped.** `0027` is a string, not 27. Any import that coerces it to
   an integer breaks the join silently.

Also learned: labels **`0025`–`0027`** exist on a sheet held by the owner. **Nothing is known about
`0022`–`0024`** and nothing has been guessed. Task **T022** raised for Phase 1's remaining blockers —
no scanner bought, the Brother ZPL question unverified, the rule undecided.

### The F45 electrical schematics — one real move, badly scanned

Two ~10 MB PDFs, Altendorf drawing **`B1434.0220`**, ePlan, 17.10.2022, editor HK. Extracted via two
sub-agents per §3.

**The scan bounds everything.** OCR returned scattered labels, not circuits; **no wire could be traced
end to end in either part**; a third to two-thirds of sheets produced nothing.

**T018 moved.** The drawing states, on the main-saw converter load sheet (`+1432.0020`, near `-X1A`,
contact `53`): *"terminals to switch an external contactor to start an exhaust unit — max. control
current 1A — max. control voltage 240VAC"*. **The capability is confirmed from the manufacturer.**
Whether anything is *landed* on those terminals at Unit 31 is not — so the question stops being a
document hunt and becomes a look inside the cabinet.

**T008 gained device tags** — sliding table `+1460.1000-S1`, blade cover `+1480.0030-S1`, and
**three** emergency stops where the check article says "the E-stop", singular. Plus a **reduced 50 mm
safety zone at the rip fence** on an inductive sensor the KB had no record of at all.

**T011 gained a measurement point but not the number** — `-X3` `POT_1`/`POT_2` at the converter. Two
things recorded rather than resolved: the two parts **disagree** on where the circuit terminates, and
the drawing uses both `Thermokontakt` (bimetal, a continuity check) and "excess temperature resistor"
(PTC, a resistance measurement) in the same area. **The 150–1000 Ω figure is not in the schematics.**

Written up as `Wiki/Processes/f45-electrical-schematics-reference.md` — a **new** article rather than
an edit to the F45 machinery page, which is Drive-only and cannot be safely rewritten through a lossy
read (§3).

### Four type plates — and the most instructive find of the day

| Machine | What the plate gave |
|---|---|
| `FA2303` Altendorf | **`S/N: 23-11-12-005`**, `F45 ElmoDrive`, 2023, 8,293 kVA, 13,34 A, blade 300–450 mm @ 2000–5000 rpm, DGUV **HM 220024** + **HM 220025** physically on the machine |
| `FA2304` Vitap | **`MATR. 320070 AT`**, 2023, **1385 kg**, 415 V, 19,3 A |
| `FA2402` AES | `STK - 10.000`, **`DUST CAPACITY 10.000 M³/H`**, 11 kW, `A-077`, **production year 2024**, 740 kg |
| `FA2301` Hebrock | `S/N F3809`, 2023, 400 V / 19,00 A / **7,08 kW**, Hebrock's own address at Hüllhorst |

**T009 closed — and the answer had been in the KB all along, under the wrong name.** `23-11-12-005`
sits in the plate's **S/N field**. This KB has held that number since Session 6 but recorded it as
*"an Altendorf internal job number"* with *"no confirmed serial number"*. Both schematic extracts were
sent hunting for a serial that morning; both came back empty and recommended photographing a title
block. **The answer was never in the document. It was on the machine, in a field we had already
transcribed and mislabelled.** New §3 lesson.

**T012 closed** — `320070 AT` on the plate is identical to the invoice-derived value.

Two discrepancies **recorded, not resolved**: `FA2304` weight **1385 kg on the plate vs 1030 kg** in
T018's levelling note (355 kg apart, and floor loading scales with it — the plate figure should be
preferred); `FA2402` weight **740 kg on the plate vs 720 kg** on the quotation.

**`FA2402`'s capacity is now plate-evidenced.** `DUST CAPACITY 10.000 M³/H` is its own field on the
plate, so the long-running *"10000 is a reading of the model name, not a specification"* caveat is
fully discharged. Manufacturer resolved to **AES ELEKTRİK MAKİNA SAN. VE TİC. A.Ş.** — *Elektrik*,
settling the two renderings the supplier article flagged as unreconciled.

The `FA2301` plate also carries a three-language warning worth knowing now that the compressor is
registered: **"Main switch does not disconnect the machine from compressed air supply!"**

### A live TpaCAD question, answered from the manual

The owner asked at the machine how to cut a **35 mm hinge-cup pocket with a 12 mm cutter (Tool 1002)**.
Both halves of the TPA CAD extract were read.

**The working is `CIRCULAR INTERNAL WINDOW`** — *"It programs a circle with internal emptying"* — under
the group **`CUSTOM WORKINGS: PROFILES`**. Parameters: X/Y centre, `Diameter`, `Final depth`,
`Intermediate depth` (the per-pass Z bite), `Tool`, and three speeds. It owns the clearing, so no
stepover arithmetic is needed.

**What the manual does not say, and it is the dangerous part:** whether `Diameter` is the finished hole
or the tool-centre path. The macro carries **no compensation parameter at all**, and the only
compensation values printed anywhere are `Off` / `Left` / `Right` — **no internal/external**. On a
12 mm tool that is the difference between a 35 mm hole and a 47 mm one. Advice given: **test cut in
scrap and measure** — 35 means finished size, 47 means enter 23 instead.

**Also absent entirely: entry and exit segments.** No helical, ramp or vertical entry is named
anywhere, though that section is visible in the operator's own dialog.

**Better route flagged:** a dedicated **`THREE HOLES HINGE`** working exists — cup and both screw holes
in one operation — if a 35 mm bit is in the boring head. Its parameter table sits on a cropped page and
did not survive the scan.

**A structural finding about our own copies:** *"part 1"* and *"part 2"* are **not two volumes**. Part 1
holds the **even** pages, part 2 the **odd** pages in reverse. Two sides of one duplex scan. Pages 1, 2
and 50 (and possibly 5 and 7) are in neither. **Reading part 1 alone gives materially wrong answers** —
the milling-setup compensation fields exist only in part 2. This explains why earlier sessions found
the extract patchy.

**T015 re-scoped from housekeeping to blocking**: `Workings.pdf`, at `Albatros\Help\` on the machine,
holds the compensation semantics, the entry/exit segments and the hinge parameter table — three of the
day's unknowns in one file.

**T016 gained documentary support.** The manual states of the setup's `Tool type` field: *"It is
automatically assigned by selecting the tool"* — so `T=1002` with `TP` blank is documented behaviour,
not a workaround. And on the `HOLE` working: *"Tool — sets the tool number **and prevails over the
programming per diameter**"*, with `Tool type` driving *"a validity check of the tool"*. That is the
mechanism this task inferred from the shop floor, in the manufacturer's own words. **Still untested end
to end.**
