# Workshop test plan — 2026-09-21 morning, 2 to 2½ hours

**Seven items that need someone standing at the machine, plus three if there is time.** None of them
can be done from the KB side. Every one closes something that has been open for days.

**The one rule that makes the morning worth anything: reproduce the fault before you fix it.** A green
run only means something if you saw the red one first, on the same file, that morning.

**Order is walking order** — everything at the Vitap, then the F45, then the compressor, then the
design computer.

| | Where | Time | |
|---|---|---|---|
| 1 · T016, the Blind Ø5 tool-ID fix | Vitap / TpaCAD | 30 | **MUST** |
| 2 · Three free glances in the same dialog | Vitap / TpaCAD | 5 | **MUST** |
| 3 · Ø12 hole from the 10 mm cutter | Vitap | 10 | **MUST** |
| 4 · `TpaCad.pdf` + `Workings.pdf` off the Albatros PC | Vitap / Albatros | 5 | SHOULD |
| 5 · **F45 monthly safety-device check** | F45 | 25 | **MUST** |
| 6 · Two photographs | compressor | 5 | **MUST** |
| 7 · Name the shared job folder | design computer | 2 | SHOULD |
| | | **82 min** | |

That leaves **40–70 minutes** for the three optional items at the end — so on the extra hour they
become likely rather than wishful.

---

## Before you walk over — 5 minutes

- **Digital calipers** (a rule will do, but Test 3 wants 0.1 mm)
- **Two or three offcuts of 19 mm board** — scrap, nothing good
- **Phone** — photographs, and this list
- **Somewhere to write** — what you write down is the entire output of the morning
- **A USB stick**, in case the Albatros PC is not on the shared Drive folder (Test 4)

## The order, and why it is not the order I gave yesterday

`library-batch-production.md` says to check `MIRROR` first. **That was the order for the batch project,
not for a morning slot.** T016 blocks production *now* and stands in front of all sixteen units;
`MIRROR` optimises a method nobody has adopted. So T016 takes the protected slot and `MIRROR` drops to
the optional list. Said plainly rather than quietly reordered.

---

# TEST 1 — T016, the Blind Ø5 tool-ID fix — 30 min — **MUST**

**Where:** the TpaCAD station at the Vitap.
**Why:** every hole in every library unit exports as a diameter with no tool. One fix, sixteen units.
**Full procedure:** `Wiki/Processes/tpacad-blind-bore-tool-id-fix.md`.

### 1a — Reproduce the failure first, before touching anything

- Open **`03-BOTTOM.TCN`** from `AMFA Wall Unit 600 RH`. **Solve / optimise.**
- Expect: `Program optimization encountered errors. Face: 1, Working: N, Tool for this working not found.`
- **Write down the exact wording and the Working number.**

> **If it does not fail** — stop, write that down, and skip to Test 2. Something has changed and
> nothing below this line applies.

### 1b — Record the starting state — 2 min

- Open the per-position **Technology** dialog (Outfit `0`, Group `1`, from the TCN editor's outfit view).
- Confirm: **Blind Ø5 mm on bushes 6, 7, 8, 9 and 10, every one at ID `0`.** That five-way tie with no
  tie-break is the entire fault. **Photograph the dialog.**
- **List every ID already in use.** Do not trust the KB's list — it records `1001`, `1002`, `1006`,
  `1011`, `1012` against positions 101–104, which is five IDs for four positions and was never
  reconciled. Read the live values.

### 1c — Step 1: give one bush a real ID

- Take **bush 6**. Change its ID from `0` to an unused number.
- **`1050`** is a reasonable pick — clearly outside the existing block — unless the live list says otherwise.
- **Write down which bush and which ID.** The next person has to be able to find it.

### 1d — Step 2: point the failing operation at that ID

- On the failing `HOLE` operation in `03-BOTTOM.TCN`, set the **Tool** field to the new ID.
- **Leave `Tool type` alone.** With an explicit Tool the manual says it *"prevails over the programming
  per diameter"*, and `Tool type` stops being a selector and becomes a validity check.
- **Both steps are needed.** Step 1 alone still resolves by diameter; step 2 alone has nothing to point at.

### 1e — Solve again, then prove it on scrap

- **Solve.** No error = the software half works.
- **Then run it on scrap and watch which spindle fires.** A clean solve with the wrong bush still looks
  like success on screen. This is the only part that proves it.

> **Do not clear the error by switching `Tool type` to "Through bore drill".** It works — that is what
> got the job out on 2026-09-15 — but only because Through Ø5 happens to have exactly one bush. It
> silently drills with the wrong tool category and it is a per-file dodge. **If steps 1 and 2 do not
> work, write down what happened and leave it failing.** T016 does not close on the workaround.

---

# TEST 2 — three free glances while that dialog is open — 5 min — **MUST**

All three cost nothing extra and each closes a question that is otherwise a separate trip.

| Look at | Question | Why it matters |
|---|---|---|
| **Ø3 drills** | How many bushes, all at ID `0`? | Ø3 failed too on 2026-09-15. Same fault, or different? |
| **The 35 mm head** | How many bushes, what ID? | If it is ID `0` with more than one candidate it is **the same fault** — and probably what went wrong with it |
| **Positions 101–104** | Is 101 really ID `1001`? | The hinge for whether SmartCABINET can ever emit IDs the Vitap recognises |

**On the 35 mm head (T027):** we still do not know what actually went wrong with it. The KB guessed
once on this exact point and was corrected. **If you remember what the problem was, that is worth more
than the bush count.**

---

# TEST 3 — a Ø12 hole from the 10 mm cutter — 10 min — **MUST**

**Why this is the best-value ten minutes on the machine:** it settles the `Diameter`-field convention
**permanently**, for every working and every cutter — including the 35 mm hinge cup, where getting it
wrong costs a door instead of a scrap offcut.

- **Scrap 19 mm.** **Pantograph / milling spindle — not a boring spindle.** Interpolation needs
  simultaneous X-Y motion; a boring spindle plunges on Z only and can only ever give a 10 mm hole.
- Working: **`CIRCULAR INTERNAL WINDOW`** (under `CUSTOM WORKINGS: PROFILES`).
- Enter **`Diameter = 12`**. Helical or ramped entry at the centre, then the radial pass — do not
  straight-plunge a straight bit into 19 mm board.
- **Measure the hole.**

| Measures | Means | Then for a 35 mm cup you enter |
|---|---|---|
| **≈ 12 mm** | `Diameter` is the **finished hole** | `35` |
| **≈ 10 mm** | `Diameter` is the **toolpath**, and a Ø2 path sits inside the cutter | `35 − cutter Ø` |
| **≈ 22 mm** | `Diameter` is the **toolpath**, and it took 12 as the path | `35 − cutter Ø` |

**Write the measured figure to 0.1 mm.** The nominal-vs-actual gap matters too: interpolated holes run
a few hundredths off depending on runout, and a dowel hole 0.2 mm oversize is a loose joint.

---

# TEST 4 — the two manuals off the Albatros PC — 5 min — **SHOULD**

**`Albatros\Help\`** on the shop's Albatros PC. Copy out **`TpaCad.pdf`** and **`Workings.pdf`**, plus
`DxfCAD.pdf` and `DxfToTPA.pdf` if they are there. To the shared Drive folder, or a USB stick.

**Why:** open as **T015** since 2026-09-15. `Workings.pdf` holds the compensation semantics, the
entry/exit segments and the `THREE HOLES HINGE` parameter table. It would also answer Test 3's question
independently — and whether the five-way ID-0 tie has a documented tie-break after all, which the
abridged extract we hold does not say.

---

# TEST 5 — the F45 monthly safety-device check — 25 min — **MUST**

**Where:** the Altendorf F45 (`FA2303`).
**Process article:** `Wiki/Processes/f45-monthly-safety-device-check.md`. **Task T008.**

**This is not a recommendation.** The machine's own manual says, in its own words:

> **"Carry out and document this check 1x month!"** — F45 manual part 1, §4.6.4

**It has never been done on record.** I checked the Safety Check Log tonight: **zero rows**. T008 has
been open since 2026-09-15. And the machine's **DGUV safety certificates expired 22.02.2024** (T007) —
a separate gap, and the reason this check matters more rather than less.

### The five items the log records

Each one Pass / Fail / N-A. These are the exact columns on the sheet, in order:

| # | Column | What it is |
|---|---|---|
| 1 | **E-Stop Response** | the emergency stops trip the machine correctly |
| 2 | **Sliding-Table Limit Switch** | functions correctly |
| 3 | **Chip-Duct Limit Switch** | functions correctly |
| 4 | **ON-OFF Switch Cleanliness** | clean and undamaged |
| 5 | **Protective Hood Condition** | intact, correctly fitted, interlock works if fitted |

`Health` goes **green only if all five are Pass**, red on any Fail, yellow if anything is blank or N/A.
`Next Check Due` fills itself in at +30 days.

### Two things the schematics added that the sheet has no column for

**a. There are three emergency stops, not one.** The process article says *"the E-stop"*, singular —
so if this check had ever been done against one button it would have been incomplete. The schematics
name them:

| E-stop | Tag | Where |
|---|---|---|
| 1 | — | *"control panel on machine frame"* |
| 2 | `+1405.1000-S1` | *"control panel at eye level"* |
| 3 | `+1419.1007-S5` | — |

**Test all three individually and name them in `Notes`.** One column, three buttons.

While you are there, two more tags the schematics give, so the log can name devices instead of
describing them: **sliding-table switch `+1460.1000-S1`** (its fault code is **E44**) and **saw-blade
cover `+1480.0030-S1`**.

**b. The reduced safety area — `+1410.0018-B2`.** An inductive sensor releasing a **50 mm** reduced
zone at the rip fence. **This KB had no record that it existed** until the schematics arrived on
2026-09-18. There is no column for it.

**Check it, write what you find in `Notes`, and afterwards tell me whether it should become a sixth
column.** That is your call — I would rather not restructure the sheet and its `Health` formula the
night before the first check ever logged.

### Practical

- An E-stop test means the machine has to be running for the stop to demonstrate anything, and each
  button needs resetting before the next. *That is my note, not the manual's.*
- **Photograph what you check.** `Evidence Link` takes a Drive link, or attach photos straight to the
  Smartsheet row.
- **Check ID:** the sheet is empty, so this is row one. **`SC-001`** unless you would rather something
  else — proposed, not decided.
- `Checked By` is a contact column: your name.

### If anything fails

**A Fail is stop-work for that function until it is fixed**, per the manual's own lockout rules — do
not log it and carry on. Tell me and I will raise a Task against `FA2303`.

### Afterwards

Send me the five results plus your notes and **I will create the row and close T008** — or do it in the
app and I will sweep the articles. Either way it is the first safety check this machine has on record.

---

# TEST 6 — two photographs at the compressor — 5 min — **MUST**

The cheapest items on the list, and one of them is a regulatory question.

1. **The air receiver's own plate (T021)** — volume in litres, maximum working pressure, year,
   manufacturer, serial number. **Crop it or shoot it smaller**: the 2026-09-18 photo came back
   unreadable at 2.9 MB. This decides whether the receiver is a pressure system needing a written
   scheme of examination. Right now the KB has nothing but a reading of the model name (`500L`), which
   is not a specification.
2. **The yellow service label (T020)** — still blank? And the **hours meter**, if the machine has one.
   Delivered November 2023, so against *"2,000 hours or 1 year"* the gap is approaching three years.

*Neither is something the KB acts on: a scheme of examination is a competent person's job and booking a
service is yours. This is establishing the facts, not committing anybody to anything.*

---

# TEST 7 — name the shared job folder — 2 min — **SHOULD**

At the design computer: **which Drive folder do SmartCABINET and the machines actually exchange files
through?** Folder name and where it sits. The KB has known since 2026-09-17 that one exists and has
never identified it.

**Just the name.** If it holds customer jobs, nothing gets copied — cite, never copy client data.

---

# IF TIME — three more, in this order

### A. Does SmartCABINET build a unit parametrically? — 10 min — *design computer*

Create a wall unit at a width the library does not have — **450** — and see whether it generates all
nine parts on its own.

- **Yes** → adding a width costs nothing, the library is a parameter list, and the whole folder
  question is smaller than it looks.
- **No** → every new width is seven files made by hand, and that caps how far the range can grow.

### B. Sheet yield, in the optimiser instead of on the saw — 5 min — *design computer*

Feed the optimiser **18 parts at 862 × 300 × 19** and see whether they fit one 2800 × 2070 sheet. Then
**24 at 682 × 300**. Those are my figures with a 4 mm kerf; the optimiser's answer is the real one, and
it costs no board. **Do not cut a sheet to find out.**

### C. `MIRROR` — 10 min — *back at the Vitap*

Take a worklist, change one side's `MIRROR` from `0` to `1`, load it, and see whether the machine
mirrors the part. If it honours the column, four side programs per height collapse to two.

**Deliberately last.** It optimises a method nothing has adopted yet.

---

# What to write down

This is the only thing that leaves the building. Short is fine.

1. **Test 1** — did it fail first, and the exact error text · which bush, which ID · did it solve
   clean · did the right spindle fire
2. **Test 2** — Ø3 bush count + IDs · 35 mm bush count + ID · is 101 = 1001 · what the 35 mm problem
   actually was, if you remember
3. **Test 3** — the measured hole size
4. **Test 4** — got the manuals, or not
5. **Test 5** — the five Pass/Fail/N-A results · **all three E-stops, individually** · what the
   reduced safety area did · anything found that did not change a Pass/Fail · who checked, and the date
6. **Test 6** — the two photographs
7. **Test 7** — the folder name
8. **Anything that surprised you**, including anything on this list that turned out to be wrong

Send that over and I will sweep it through both stores — **T008, T016, T027, T021, T015**, the
Safety Check Log, the Machinery Register, the task notes and five articles all move on those answers.

---

# What not to do

- **Do not** clear the T016 error with the Through-bore workaround.
- **Do not** run any program on good material until it has solved clean.
- **Do not** test the Ø12 hole on a boring spindle — only the pantograph can interpolate.
- **Do not** log a safety Fail and carry on using that function. It is stop-work until fixed.
- **Do not** cut a sheet to check the yield; the optimiser answers it for free.
- **Do not** touch the F4's tape or pre-mill setting. Unrelated to today, and they are one decision
  rather than two — change one without the other and a whole batch fails.
- **Do not** change more than one thing at a time in the Technology dialog. If the fix works, we need
  to know which change did it.

---

# Still not on this list

**T007 — the F45's expired DGUV safety certificates** (`HM 220024` and `HM 220025`, expired
**22.02.2024**). It is not a shop-floor test; it is a question for Altendorf or whoever sold the
machine, and **contacting a manufacturer on the company's behalf is yours, not mine.** Tomorrow's
check does not replace it or close it — the two are separate, and doing the monthly check is exactly
what you would want to be able to show while the certificate position is being sorted out.
