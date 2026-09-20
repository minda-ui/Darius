# Workshop test plan — 2026-09-21 morning, 60–90 minutes

**Six tests that need someone standing at the machine, plus three if there is time.** None of them can
be done from the KB side. Every one closes something that has been open for days.

**The one rule that makes the morning worth anything: reproduce the fault before you fix it.** A green
run only means something if you saw the red one first, on the same file, that morning.

---

## Before you walk over — 5 minutes

- **Digital calipers** (a rule will do, but Test 3 wants 0.1 mm)
- **Two or three offcuts of 19 mm board** — scrap, nothing good
- **Phone** — photographs, and this list
- **Somewhere to write** — what you write down is the entire output of the morning
- **A USB stick**, in case the Albatros PC is not on the shared Drive folder (Test 5)

## The order, and why it is not the order I gave yesterday

`library-batch-production.md` says to check `MIRROR` first. **That was the order for the batch project,
not for a 90-minute slot.** T016 blocks production *now* and stands in front of all sixteen units;
`MIRROR` optimises a method nobody has adopted. So T016 takes the protected slot and `MIRROR` drops to
"if time". Said plainly rather than quietly reordered.

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

# TEST 4 — two photographs at the compressor — 5 min — **MUST**

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

# TEST 5 — the two manuals off the Albatros PC — 5 min — **SHOULD**

**`Albatros\Help\`** on the shop's Albatros PC. Copy out **`TpaCad.pdf`** and **`Workings.pdf`**, plus
`DxfCAD.pdf` and `DxfToTPA.pdf` if they are there. To the shared Drive folder, or a USB stick.

**Why:** open as **T015** since 2026-09-15. `Workings.pdf` holds the compensation semantics, the
entry/exit segments and the `THREE HOLES HINGE` parameter table. It would also answer Test 3's question
independently — and whether the five-way ID-0 tie has a documented tie-break after all, which the
abridged extract we hold does not say.

---

# TEST 6 — name the shared job folder — 2 min — **SHOULD**

At the design computer: **which Drive folder do SmartCABINET and the machines actually exchange files
through?** Folder name and where it sits. The KB has known since 2026-09-17 that one exists and has
never identified it.

**Just the name.** If it holds customer jobs, nothing gets copied — cite, never copy client data.

---

# IF TIME — three more, in this order

### A. Does SmartCABINET build a unit parametrically? — 10 min

Create a wall unit at a width the library does not have — **450** — and see whether it generates all
nine parts on its own.

- **Yes** → adding a width costs nothing, the library is a parameter list, and the whole folder
  question is smaller than it looks.
- **No** → every new width is seven files made by hand, and that caps how far the range can grow.

### B. Sheet yield, in the optimiser instead of on the saw — 5 min

Feed the optimiser **18 parts at 862 × 300 × 19** and see whether they fit one 2800 × 2070 sheet. Then
**24 at 682 × 300**. Those are my figures with a 4 mm kerf; the optimiser's answer is the real one, and
it costs no board. **Do not cut a sheet to find out.**

### C. `MIRROR` — 10 min

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
4. **Test 4** — the two photographs
5. **Tests 5 / 6** — done or not; the folder name
6. **Anything that surprised you**, including anything on this list that turned out to be wrong

Send that over and I will sweep it through both stores — **T016, T027, T021, T015**, the Machinery
Register, the task notes and four articles all move on those answers.

---

# What not to do

- **Do not** clear the T016 error with the Through-bore workaround.
- **Do not** run any program on good material until it has solved clean.
- **Do not** test the Ø12 hole on a boring spindle — only the pantograph can interpolate.
- **Do not** cut a sheet to check the yield; the optimiser answers it for free.
- **Do not** touch the F4's tape or pre-mill setting. Unrelated to today, and they are one decision
  rather than two — change one without the other and a whole batch fails.
- **Do not** change more than one thing at a time in the Technology dialog. If the fix works, we need
  to know which change did it.

---

# Not on this list, and still not done

**The F45's mandatory monthly safety-device check has never been logged once** (Task **T008**, sheet
`913380204480388`). It is not here because it needs its own slot rather than the tail end of a testing
session — but it is a documented legal requirement on a machine whose **safety certificates expired
22.02.2024** (T007), and it has been open since 2026-09-15. Worth putting in the diary on the way out.
