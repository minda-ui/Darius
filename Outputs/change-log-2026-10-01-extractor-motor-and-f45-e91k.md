# Change log — 2026-09-30 to 2026-10-01 — extractor motor failure, and an F45 error that names the wrong button

**Session 25.** One conversation across two days: the adoption read on 2026-09-30, then a full working day
on 2026-10-01. Written 2026-10-02 at the start of the next session — **a day late**, because the
2026-10-01 sign-off came without a change log and the end-of-day hook that would have prompted it is not
on this branch (see (1)).

## (1) Adoption and the git mirror (2026-09-30)

- Owner: *"Read and adopt Darius - Workshop Operations Assistant Folder on google drive."* That folder
  (`1xoCbqwoSDwgwK3O5U3_p_Yj8MQjwsBBU`) holds only a `README.md` pointer to this KB; read, and the
  session-start sequence run (Hub, Rules, charter).
- **Found: the git mirror is behind Drive.** `main` and `claude/magical-sagan-88ry2f` carried charter
  **v31**; Drive holds **v35**. The v32–v35 work (19 commits, 2026-09-27..29) exists only on the unmerged
  branch `claude/vigilant-bell-olevtr`; PR #1 had been merged to `main` from an older base.
- **Merge attempted and aborted.** The only conflict is `.claude/settings.json` (both sides added
  different hooks). Resolving it was **refused by the session's permission classifier as
  self-modification**, so nothing was forced. Proposed resolution: keep both — `SessionStart` hook and
  Composio MCP from `main`, the good-night `UserPromptSubmit` hook and the Gmail/Drive-delete denies from
  `vigilant-bell`.
- **Raised on the Hub as `AWT-0225`** (own row, Blocked, §0b Rule B). Still blocked on the owner.

## (2) `FL-003` — AES extractor `FA2402`: the 11 kW motor's insulation has failed

**Symptom (2026-10-01):** ran normally on 2026-09-30 until ~30 min before end of shift, then noise and
F1 (32 A MCB) tripped. Next morning: starts, runs at about half speed with noise, trips F1 if kept running.
Owner: nothing worked on.

**What was found, in order:**

| Step | Finding | Status |
|---|---|---|
| Visual, panel isolated | **Burnt terminal `T2` on `K1`** (LC1E1810 main contactor) | real; cable replaced, `K1` not |
| Restart | `K1` + `K3` in, never changed to delta | — |
| `K3` released | indicator returns — **not welded** | ruled out |
| `ZR1` (ENTES SER-λ/Δ) | ON + λ lit, Δ never; later did change over | not the fault |
| After changeover | **F1 trips instantly**; noisy in star too | — |
| Cable on `K1` `T2` | lands on motor `V1` — correct | ruled out |
| `K1`, `T1`, `K2`, `K3` poles | all 0 Ω pressed / OL released | ruled out |
| Motor terminal box | no burning; **several lugs badly crimped** (strands splayed) | remake, not the cause |
| 9-combination winding table from the panel | 3 windings continuous, no winding-to-winding short | — |
| **Insulation test, 500 V** (electrician, Kewtech KT63DL) | **Winding A to earth 0.169 MΩ**, repeated; **motor alone 0.176 MΩ** | **cause** |

**Cause established by measurement: insulation failure on one winding of motor M1**, inside the motor,
not the cables. Likely sequence (inference): the `K1` `T2` joint overheated and failed, the motor ran on
two phases, the winding overheated — and **`T1` did not protect it**: the fitted LRE22 (16–24 A) cannot be
set below 16 A, against a phase current of **11.6 A** from the nameplate (OMEGA 3MAS 160MA2, 11 kW 2-pole,
Δ/Y 400/690 V 20/11.6 A, frame 160M B5, serial 16240008410, **made 02/2024**).

**Two wrong turns, both mine, both retracted on the row the same day:**

1. ***"V winding open."*** Measured as `T1` out *n* to `K2` out *n* — the pairing the schematic implies.
   **The as-built panel does not pair them that way**: the delta phase shift is made in the wiring, and
   the schematic as drawn would not make a working delta at all. The motor terminal board's labels were
   also ambiguous, so the first motor-end readings were wrong pairs too. *Fixed by measuring all nine
   combinations, labels ignored.*
2. ***"3 Ω in the `T1` 2 loop."*** Repeatable from the panel, but every segment of that loop read 0, and
   the meter was on a kΩ range with 1-ohm resolution. **Recorded as unresolved, not as a finding.**

*The lesson is `FL-002`'s again, one level down: a drawing is not the as-built, and a pairing read off a
drawing is an inference. On this panel the drawing is wrong about the delta.*

**Open, owner's decisions (not ordered from this KB):** motor-shop test (clean/dry vs rewind) vs a
replacement; warranty via Markfield/AES (motor under two years old); fit the **9–13 A `T1` set at 11.6 A**
before any motor runs; remake the motor-box lugs; B, C and between-winding insulation readings still to
record. **The extractor is out of service.**

## (3) `FL-004` — Altendorf F45 `FA2303`: `E91K` names the STOP button, the fault was START

Screen: *"E91K: K-contact of Stop button faulty"*, on pressing the **yellow START** to position the fence.
**The owner found it**: dust in the yellow START button; compressed air cleared it. The ElmoDrive table has
**`E93K`** for a START K-contact fault, and it did not appear — **why the control reports it as `E91K` is
not known**, and is recorded as observed. My first framing (a STOP button pressed) was wrong and was
corrected on the row. **Status Monitoring**, since dust keeps building while the extractor is down.

**Owner: *"Yes, add both."*** Done:

- **Maintenance Schedule** sheet: **`MT-029`** (`FA2303`) — blow out control-panel buttons, **weekly
  (proposed, not a manufacturer interval)**.
- **`Wiki/Troubleshooting/troubleshooting-altendorf-f45.md`** (6,769 → **8,017 B**): new section *"E91K can
  mean the yellow START button, not a STOP button"*; the table row points to it.
- **`Wiki/Processes/maintenance-schedule-altendorf-f45.md`** (4,601 → **5,119 B**): `MT-029` added.

**Published by archive-then-recreate, not in place** — Composio is not signed in this session (`execute`
returns nothing; no API key in `~/.composio/config.json`), so §4's fallback applied. Old copies renamed into
`Archive/` with ids preserved; **new ids** `15GhXBr63eyV5CUd9GyJ5AKLPoVF4nOo5` and
`1J0vyP9AEIJqngSE6eLtd-mzhi_nSRauf`. **Both downloaded back and `cmp`-identical to git.** Mirror commit
`b3981af` on `claude/magical-sagan-88ry2f`.

## (4) Records touched

| Record | Change |
|---|---|
| Fault Log | `FL-003` opened (In Progress); `FL-004` opened (Monitoring, resolved 2026-10-01) |
| Maintenance Schedule | `MT-029` added |
| Hub Tasks & Requests | `AWT-0225` raised (Blocked) |
| Wiki | two F45 articles amended (above) |

## (5) Noticed, not acted on

- **`Outputs/` on Drive holds three files named `kb-registers.md`**: the live one
  (`1Zw5cRA1NdSBCgaTHTUuLl11qbiN4dk5o`, 154,189 B) and two older ones (`1xES9mYXXxoKzn8m-GYY68wUKEW2npxs8`,
  2026-09-20, 92,318 B; `1aMUdmhTushgxIrAq6O4KUSKTyxO5lomO`, 2026-09-19, 78,396 B) that look like
  superseded copies never moved to `Archive/`. A name search can land on the wrong one. **Flagged for the
  owner; not moved.**
- Composio sign-in is needed for in-place Drive updates again (`composio login` is an owner action).
