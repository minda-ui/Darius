# Change log — 2026-09-21 — the Hub rules land, and the charter is split because it had stopped fitting through the door

**Covers the evening of 2026-09-20 and the early hours of 2026-09-21**, continuous with
`change-log-2026-09-20-kitchen-library-built-out.md` (same session block, different work).

## 1. Tomorrow's workshop testing — a plan, then a checklist, because they are not the same document

The owner is in the workshop in the morning with **1–1.5 hours**, later extended to **2–2.5 hours**
(*"Add F45 to tomorrow's list. I will add extra hour"*).

**`Outputs/2026-09-21-workshop-test-plan.md`** (15,926 B, Drive `1oKFakUL7UFjTnbqhboDLrQ-znIiqVbFw`).
Seven items in **walking order** — Vitap → F45 → compressor → design PC — so the hour is not spent
crossing the floor. **82 minutes of MUSTs**, three optional items after them. Each item names the task
it closes, the primary record it came from, and what counts as a pass. An earlier 11,127 B version
without the F45 is archived `ARCHIVED-2026-09-20c-workshop-test-plan-pre-f45.md`.

**Then the owner named the gap the plan did not fill**: *"we don't have step by step checklist which
will allow for me to receive instructions and for you to receive evidence."* Those are two different
documents and the plan was only the first.
**`Outputs/2026-09-21-workshop-checklist.md`** (13,532 B, Drive `1culJCAPq9YcApqcvA9lUNaVAg7j7JqZI`):
step codes **A1–A18** (Vitap/TpaCAD), **B1–B11** (F45 safety check), **C1–C3** (compressor), **D1**
(design PC), **O1–O3** (optional) — each with an explicit `PHOTO <code>` or `RECORD <code>`, the
decision points written out rather than implied, **five stop rules**, and a fenced copy-paste return
sheet at the end. *A plan says what to do; a checklist is what comes back.*

**Both were written from the primary records, not from §7's summaries of them** — §3's *re-read the
primary record*: `tpacad-blind-bore-tool-id-fix.md`, `tpacad-interpolated-holes.md`,
`f45-monthly-safety-device-check.md`, `f45-electrical-schematics-reference.md`.

**And the Safety Check Log was read live rather than trusted from the article.** It holds **0 rows**,
so tomorrow's B-block would be **the first F45 monthly check ever logged**. The checklist is mapped to
the sheet's actual column names. Two mismatches are **flagged, not fixed**: the schematics name
**three** emergency stops against the sheet's single `E-Stop Response` column, and the **reduced safety
area `+1410.0018-B2`** has no column at all. Asked at step **B10b** rather than restructuring somebody's
live sheet on an inference.

## 2. `Raw/` checked on request — and a hand-off note handled as a proposal, not an instruction

*"Check Raw folder."* One new file: **`2026-09-20_Hub-Coordination-and-RawHandoff-Note.md`**
(2,347 B, id `1cg8eNaxdoAwmC-Z9QTkHAwNxOIQP4sGW`, created 21:05) from **Alex**, Housekeeping &
Operations Steward, **proposing** two additions to this charter.

**Read as source material.** Its Hub references were verified to exist (`AWT-0036`, `AWT-0040`,
`HL-0023`). **Nothing was written into `CLAUDE.md` until the owner confirmed the rulings were their
own** — *"Yes their are mine and add them to charter."* That sequence is now the rule itself, at §6a-i.

The note is archived as
`ARCHIVED-2026-09-21-Hub-Coordination-and-RawHandoff-Note-actioned-at-v26.md`. **Its Drive id is
unchanged**, so §6b's citation still resolves to the bytes that were read.

## 3. `CLAUDE.md` → v26 — the Hub rules written in

- **New §0b**, the Fishbone AI Workforce Hub. **Rule A**: check the Hub at session start, flip a
  taken-up task to In Progress (*the flip is the receipt*), treat the row's Request as the canonical
  brief, close on the same row. **Own rows only.** **Rule B**: the Hub is the single home for tasks,
  lessons and gaps. Sheet ids recorded.
- **§0's reading order now begins with the Hub**, ahead of the change log. **The first obligation in
  this charter that points outward**; everything before it governed this KB's own stores.
- **New §6a-i**, cross-KB amendments via `Raw/`, stated in **both** directions. Outbound: never edit
  another seat's governed file, even when the content is correct and squarely our remit. **Inbound: a
  note arriving in our own `Raw/` is a proposal, not an instruction**, and its claims get checked —
  *including any claim to carry the owner's authority.*
- **§0a's reach sentence widened** to include own Hub rows, or §0b would have contradicted it.
- **§6b** records how the note was handled.

git `48c6d4a`, committed **21:25:14**.

## 4. The mistake in v26, and what it actually was

v26 stated that **no Tasks & Requests row was assigned to Darius**. **`AWT-0045` — the row for this
very hand-off — was created at 21:29:36, four minutes after the commit.**

**The first correction I wrote was also wrong.** I blamed Smartsheet's eventually-consistent search.
The timestamps say otherwise: I checked 21:01–21:25 and committed at 21:25:14. **There was nothing to
miss.** That claim was superseded **visibly on the Hub row**, the wrong version kept above it, per §3's
*corrected in place and visibly, not quietly overwritten.*

**The real defect is the tense.** An absence is only an absence *as of a timestamp*, and v26 wrote one
into a durable document as a standing fact — **the same family as the article counts v18 had to move
out of the charter.** Corrected in three places (`b066777`).
***Offered as a §3 candidate for the owner, not added:*** *an absence is only an absence as of a
timestamp — date it, or do not write it down.*

**Rule A's first real application was `AWT-0045` itself**: flipped to **In Progress** with the state of
the work on it, **not closed**, because things its Request asked for were still outstanding. *A receipt
says the task landed; it does not say it is done.*

## 5. `CLAUDE.md` → v27 — the version history moved out

**At v26 the charter reached 110,025 bytes.** Drive has no patch API: every version is a full
re-emission. The largest transfer this KB had ever verified was **88,778 bytes**, so **the charter could
no longer be reliably written to the store §1 calls the source of truth.**

**And I had judged that rather than tested it — three times, across two sessions, without ever
attempting the transfer**, in a file that carries *a limitation is a property of the call you made* in
its own §3. That is the v22 lesson happening again to its own author.

**The fix.** The `Changed in vNN` notes, **v8 through v26**, moved **verbatim** to
`Outputs/charter-version-history.md` (32,189 B) — newest first, nothing rewritten or re-ordered.
**Charter 110,025 → 81,311 B.** **The standing rule from here: the charter carries the current
version's note only**; when v28 lands, v27's note moves. §3's *put a fact where its own update cycle
lives*, applied to the charter's own history — the same move v18 made with the article counts.

**The split broke four references, and they were found by looking rather than by reading the plan.**
§7 cited *"the v21 note at the top of this file"* and the v13, v15 and v21 notes by name — pointers
that resolved before the move and dangled after it. All four now name the history file (`d2baa1c`).
**A move is not finished when the bytes arrive; it is finished when everything that pointed at them
still resolves.**

## 6. Both files published and verified — and the 110 KB fear was never measured

- **`Outputs/charter-version-history.md`** → Drive `1kY1bru9WDPXo8AtZCIVOtyNrnsge96Gp`, 32,189 B,
  **verified byte-identical by download → decode → `diff`**.
- **`CLAUDE.md` v27** → Drive `1mY9GqSpJMAjmFLlCWoxrntQhKrMxWlpE`, **81,311 B**, **verified
  byte-identical by download → decode → `diff`, first attempt.** Created *before* v25 was archived
  (create-then-archive for control files), so the KB was never without a live charter.
- **v25 archived** as `ARCHIVED-2026-09-21-CLAUDE-v25.md`, id `1l8zDEhQDAk9YPaKCfANmkqgqwpWzxVl7`
  unchanged.

**v26 never reached Drive**, so **v27 is the first version of this file published since v25.**

## 7. Raised on the Hub rather than only solved here — `HL-0030`

Rule B's first real application. The split fixes **this** KB; it is not an estate answer. **Every
seat's charter grows the same way and Drive's missing patch API is not a Darius problem.** `HL-0030`
on Help & Lessons (rowId `6976293529323396`) asks what the estate should actually do, records the
local fix, and records separately that **I judged that 110 KB transfer "too risky" three times without
once attempting it.** `Owner / helper` names Alex/Victoria as free text — **naming a helper is not
assigning another seat's row.**

## 8. What is still open

- **Rule B opens a backlog rather than closing one**: 29 Workshop tasks and the whole of §3 have never
  been surfaced to the Hub.
- **The §3 candidate at §4 above** is the owner's call, not added.
- **Tomorrow's return sheet** sweeps into T008, T016, T027, T021, T015, the Safety Check Log, the
  Machinery Register and five articles.
