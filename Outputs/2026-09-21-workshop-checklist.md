# Workshop checklist — 2026-09-21

**Step-by-step. You follow it, I collect the evidence.** Work top to bottom and do not skip ahead —
several steps only mean something because the one before them was done first.

**The reasoning behind each block is in `2026-09-21-workshop-test-plan.md`.** This file is the doing.

---

## How evidence works

- **Every step has a code** — `A2`, `B6`, `C1`. Use the code when you report.
- **`PHOTO A2`** means take a photograph at that step. **The photo is named by the step code.** If you
  cannot rename on the phone, just shoot them in checklist order and tell me *"in order"*.
- **`RECORD`** means write something down — a number, a word, or the exact text on screen.
- **Blank is a real answer.** *"Did not get to it"* or *"could not find it"* is evidence. Guessing is not.
- **The return sheet at the bottom is the deliverable.** Copy it into a message and fill the blanks.

## Stop rules — read once before you start

1. **Any safety device that fails = stop using that function.** Do not finish the round and decide
   later. Note it, tell me, stop.
2. **Never run a program on good material.** Scrap only, all day.
3. **Never clear the T016 error by switching `Tool type` to "Through bore drill".** If the fix does not
   work, leave it failing and write down what happened.
4. **One change at a time** in the Technology dialog, or we will not know which change did it.
5. **If a step's result contradicts this checklist, the machine is right and the checklist is wrong.**
   Write what you actually saw.

## Kit

- [ ] Digital calipers
- [ ] 2–3 offcuts of 19 mm scrap
- [ ] Phone
- [ ] USB stick
- [ ] This list

---

# BLOCK A — at the Vitap / TpaCAD station

### A1 · Open the file
- [ ] Open **`03-BOTTOM.TCN`** from `AMFA Wall Unit 600 RH`.
- **RECORD A1:** opened yes / no.

### A2 · Reproduce the failure — before changing anything
- [ ] **Solve / optimise.** Change nothing first.
- **RECORD A2:** the exact error text, including the Working number.
- **PHOTO A2** — the error dialog.

> **If there is NO error:** write that in A2, **skip A3 to A13**, and go straight to **A14**. Something
> has changed and the rest of the fix does not apply.

### A3 · Open the outfit
- [ ] Open the per-position **Technology** dialog — Outfit `0`, Group `1`, from the TCN editor's
  outfit view.
- **PHOTO A3** — the whole bush list, as wide as will stay readable.

### A4 · Blind Ø5 — the fault itself
- [ ] Find every bush carrying **Blind bore Ø5 mm**.
- **RECORD A4:** the bush numbers, and the ID against each one.
  *(Expected: bushes 6, 7, 8, 9, 10 — all ID `0`. If it differs, A4 is the finding of the day.)*

### A5 · Which IDs are already taken
- [ ] Read down the list and note every ID that is **not** `0`.
- **RECORD A5:** the list of IDs in use.
- **PHOTO A5** — if the list is long, photograph rather than transcribe.

### A6 · Ø3 drills
- **RECORD A6:** how many bushes carry Ø3, and their IDs.

### A7 · The 35 mm head
- **RECORD A7:** how many bushes carry Ø35, and their IDs.
- **RECORD A7b:** *what actually went wrong with the 35 mm head, if you remember.* Your memory here is
  worth more than the bush count — we have never had this and I guessed at it once and was wrong.

### A8 · Positions 101–104
- **RECORD A8:** the ID against each of positions 101, 102, 103, 104.
  *(The KB says 101 = `1001`. This is checking that, not assuming it.)*

### A9 · Choose the new ID
- [ ] Pick a number that **does not appear in A5**.
- **RECORD A9:** the number you chose. *(`1050` unless A5 says otherwise.)*

### A10 · Step 1 of the fix — give bush 6 an ID
- [ ] Change **bush 6**'s ID from `0` to your A9 number. Apply / save.
- [ ] **Change nothing else in this dialog.**
- **RECORD A10:** done yes / no, and anything the dialog said.
- **PHOTO A10** — the bush row after the change.

### A11 · Step 2 of the fix — point the operation at it
- [ ] Back in `03-BOTTOM.TCN`, on the **failing `HOLE` operation** (the Working number from A2), set
  the **`Tool`** field to your A9 number.
- [ ] **Leave `Tool type` alone.**
- **PHOTO A11** — the operation's parameters showing `Tool` filled in.

### A12 · Solve again
- [ ] **Solve / optimise.**
- **RECORD A12:** clean, or the exact error text.
- **PHOTO A12** — the result.

> **If it still fails:** record it, **do not try the Through-bore workaround**, skip A13 and go to A14.

### A13 · Prove it on scrap
- [ ] Load a scrap panel and run the program.
- **RECORD A13:** which spindle / bush actually fired — did the machine use bush 6?
- **RECORD A13b:** measure one Ø5 hole. Diameter and depth.
- **PHOTO A13** — the drilled scrap.

*A clean solve with the wrong bush looks identical on screen. This step is the only thing that proves it.*

### A14 · The Ø12 test — set it up
- [ ] **10 mm cutter, in the pantograph / milling spindle.** Not a boring spindle.
- [ ] New program on scrap: working **`CIRCULAR INTERNAL WINDOW`**, **`Diameter = 12`**.
- [ ] Helical or ramped entry at the centre — do not straight-plunge.
- **PHOTO A14** — the working's parameters, showing `Diameter = 12`.

### A15 · The Ø12 test — cut it
- [ ] Run on scrap.
- **PHOTO A15** — the hole with the calipers across it, jaws readable.

### A16 · The Ø12 test — measure it
- **RECORD A16:** the measured diameter, to 0.1 mm.

| If it reads | I will conclude |
|---|---|
| ≈ 12 | `Diameter` = the finished hole |
| ≈ 10 | `Diameter` = the toolpath |
| ≈ 22 | `Diameter` = the toolpath |

*Do not adjust anything to "make it right" — the wrong number is the answer we want.*

### A17 · The Albatros help folder
- [ ] On the Albatros PC, open **`Albatros\Help\`**.
- **PHOTO A17** — the folder listing.
- **RECORD A17:** which of `TpaCad.pdf`, `Workings.pdf`, `DxfCAD.pdf`, `DxfToTPA.pdf` are there.

### A18 · Copy them out
- [ ] Copy them to the shared Drive folder, or a USB stick.
- **RECORD A18:** which files you copied, and where to.

---

# BLOCK B — at the F45 (`FA2303`) · the monthly safety check

**This is the machine's own mandatory check** — *"Carry out and document this check 1x month!"*,
manual part 1, §4.6.4. **It has never been logged: the Safety Check Log has zero rows.** Tomorrow's is
the first on record.

Each item is **Pass**, **Fail** or **N/A**.

### B1 · Who and when
- **RECORD B1:** the date, and your name as it should appear in `Checked By`.

### B2 · ON/OFF switch — clean and undamaged
- [ ] Look at it.
- **RECORD B2:** Pass / Fail / N-A, plus anything seen.
- **PHOTO B2**

### B3 · Protective hood — intact, correctly fitted, interlock works if fitted
- [ ] Inspect, and operate the interlock if there is one.
- **RECORD B3:** Pass / Fail / N-A, plus whether an interlock is fitted at all.
- **PHOTO B3**

### B4 · Sliding-table limit switch — `+1460.1000-S1`
- [ ] Test that it functions.
- **RECORD B4:** Pass / Fail / N-A, and what the machine did.
- **RECORD B4b:** did any fault code appear? *(The drawing associates **E44** with this switch.)*
- **PHOTO B4**

### B5 · Chip-duct / plate limit switch
- [ ] Test that it functions.
- **RECORD B5:** Pass / Fail / N-A, and what the machine did.
- **PHOTO B5**

### B6–B8 · The three emergency stops, one at a time

**There are three.** The process article says *"the E-stop"*, singular — which means if this check has
ever been done before, it was done against one button. *Machine running, no workpiece, blade clear —
that framing is mine, not the manual's; use your own judgement on the day.* Reset each one before
testing the next.

| Step | E-stop | Tag | Where the drawing puts it |
|---|---|---|---|
| **B6** | 1 | — | *"control panel on machine frame"* |
| **B7** | 2 | `+1405.1000-S1` | *"control panel at eye level"* |
| **B8** | 3 | `+1419.1007-S5` | not stated — **tell me where you find it** |

- [ ] B6 · press · machine stops? · reset — **RECORD B6:** Pass / Fail — **PHOTO B6**
- [ ] B7 · press · machine stops? · reset — **RECORD B7:** Pass / Fail — **PHOTO B7**
- [ ] B8 · press · machine stops? · reset — **RECORD B8:** Pass / Fail, **and where it is** — **PHOTO B8**

### B9 · The single column value
- **RECORD B9:** `E-Stop Response` = **Pass only if B6, B7 and B8 all passed.** Otherwise Fail.

### B10 · The reduced safety area — `+1410.0018-B2`
An inductive sensor releasing a **50 mm** reduced zone at the rip fence. **This KB did not know it
existed** until the schematics arrived on 2026-09-18, and **there is no column for it on the sheet.**

- [ ] Find it. Does this machine actually have it?
- **RECORD B10:** found / not found / not sure — and if found, what it does.
- **RECORD B10b:** **should it become a sixth column on the check?** Your call, and I would rather ask
  than restructure the sheet before the first check is even logged.
- **PHOTO B10** — if you find it.

### B11 · Any failures
- **RECORD B11:** anything that failed, and whether that function is now out of use.

*Any Fail is stop-work for that function until fixed — per the manual's own lockout rules. Tell me and
I will raise a Task against `FA2303`.*

---

# BLOCK C — at the compressor (`FA2306`)

### C1 · The air receiver's own plate
The 2026-09-18 photo came back unreadable at 2.9 MB. **Crop it, or shoot it smaller.**

- **PHOTO C1** — the receiver's plate, legible.
- **RECORD C1:** type out what it says — **volume in litres**, **max working pressure**, year,
  manufacturer, serial number.

*This is the whole of Task T021. Right now the KB has only a reading of the model name (`500L`), which
is not a specification.*

### C2 · The yellow service label
- **PHOTO C2**
- **RECORD C2:** still blank, or are there entries? If entries — dates and who.

### C3 · Hours meter
- **RECORD C3:** does the machine have one, and what does it read?
- **PHOTO C3** — if it has one.

---

# BLOCK D — at the design computer

### D1 · The shared job folder
- [ ] Find the Drive folder SmartCABINET and the machines exchange files through.
- **RECORD D1:** the folder name and roughly where it sits.

> **Type the name — do not screenshot the listing.** It probably has customer job folders in it, and
> the rule is cite, never copy client data.

---

# OPTIONAL — only if the must-do blocks are finished

### O1 · Is SmartCABINET parametric?
- [ ] Create a wall unit at **450** wide — a width the library does not have.
- **RECORD O1:** did it generate all nine parts on its own? Yes / no / partly.
- **PHOTO O1** — the resulting part list.

### O2 · Sheet yield, in the optimiser — not on the saw
- [ ] Feed it **18 parts at 862 × 300 × 19**, sheet 2800 × 2070.
- **RECORD O2:** do they fit on one sheet? How many actually fit?
- **PHOTO O2**
- [ ] Then **24 parts at 682 × 300 × 19**.
- **RECORD O2b:** same question. **PHOTO O2b**

### O3 · `MIRROR`
- [ ] Take a worklist, change one side's `MIRROR` from `0` to `1`, load it.
- **RECORD O3:** did the machine mirror the part? Yes / no / no visible difference.

---

# THE RETURN SHEET

Copy this into a message and fill it in. Leave blanks where you did not get to something — that is
useful too. Then send the photos, in order, or with their codes.

```
A1  opened:
A2  error text:
A3  photo: yes/no
A4  Blind O5 bushes + IDs:
A5  IDs already in use:
A6  O3 bushes + IDs:
A7  35mm bushes + IDs:
A7b what went wrong with the 35mm head:
A8  101/102/103/104 IDs:
A9  ID chosen:
A10 bush 6 changed:
A11 Tool field set:
A12 solve result:
A13 which spindle fired:
A13b O5 hole measured (dia / depth):
A14 Diameter=12 entered:
A15 photo: yes/no
A16 MEASURED HOLE:            mm
A17 files present in Albatros\Help\:
A18 files copied, and to where:

B1  date / checked by:
B2  ON-OFF switch:            Pass / Fail / N-A
B3  protective hood:          Pass / Fail / N-A   (interlock fitted? )
B4  sliding-table switch:     Pass / Fail / N-A   (fault code? )
B5  chip-duct switch:         Pass / Fail / N-A
B6  E-stop 1:                 Pass / Fail
B7  E-stop 2:                 Pass / Fail
B8  E-stop 3:                 Pass / Fail   location:
B9  E-Stop Response column:   Pass / Fail
B10 reduced safety area:      found / not found / not sure —
B10b should it be a 6th column?
B11 anything failed / function taken out of use:

C1  receiver plate — litres:        max pressure:
    year:        manufacturer:        serial:
C2  service label:
C3  hours meter:

D1  shared job folder name:

O1  parametric at 450:
O2  18 x 862x300 on one sheet:
O2b 24 x 682x300 on one sheet:
O3  MIRROR honoured:

Anything that surprised me, or that this list got wrong:
```

---

# What I do with it

| Your evidence | What moves |
|---|---|
| A2, A10, A12, A13 | **T016** closes or stays open, with the bush and ID recorded so the next person finds it |
| A6, A7, A7b | **T027**, and whether Ø3 is the same fault |
| A8 | whether SmartCABINET can ever emit IDs the Vitap recognises — the systemic half of T016 |
| A16 | the `Diameter` convention, settled permanently, including for the 35 mm cup |
| A17, A18 | **T015** |
| B1–B11 | the **first row** in the Safety Check Log, and **T008** closes |
| C1 | **T021** — whether the receiver needs a written scheme of examination |
| C2, C3 | **T020** |
| D1 | an open question since 2026-09-17 |
| O1, O2, O3 | the batch-production proposal stops being arithmetic and starts being measured |

**Send it however is easiest — typed, photographed, or dictated.** I will do the filing.
