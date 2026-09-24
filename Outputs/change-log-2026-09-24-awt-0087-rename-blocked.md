# Change log — 2026-09-24 — AWT-0087: the rename cannot be done from here, the proposed name is wrong, and the charter line already exists

**A short session with three findings, none of them the one the task expected.** `AWT-0087` (Alex,
2026-09-23) asked for two things: rename this KB's Workshop `Document Register` Smartsheet away from
that name, and add a charter line confirming no write access to the shared group Document Register.
The owner authorised taking it up today. **Neither half completed, and for different reasons — both
recorded on the Hub row rather than left as a silence.** Status set to **Blocked**, not In Progress:
what remains is the owner's, so the row should read red.

## 1. There is no sheet-rename tool, in any toolset

Alex's proposal note said *"I don't have a tool that renames a Smartsheet's title — only its columns,
rows, and content"*, and assumed Darius or an editor would do it. **The same limit applies here, and it
was checked rather than assumed.** The default Smartsheet toolset offers `update_column` — *"Updates an
existing column's properties"* — and nothing at sheet level. The connector also hides six toolsets
behind `search_tools`; **`portfolio`, `ai_solutions`, `legacy_workapps`, `scenario_planning`,
`automations` and `smart_skills` were all searched. None renames a sheet.** (`sharing` and `users` were
not searched: both are access-control domains by definition, not sheet metadata. Recorded as the one
gap in the sweep rather than presented as a complete search.)

**Authority was not the blocker.** `get_sheet_path` reports `accessLevel: OWNER` on sheet
`838802392352644`, and the owner approved the rename this session. **The capability is missing, not the
permission** — a distinction worth keeping, because the two produce the same failure and need opposite
responses.

**Written into `CLAUDE-Rules.md` §6a**, alongside the delete-sheet limit already recorded there from the
2026-09-15 duplicate cleanup: renaming a sheet is a UI action the owner takes, for the same reason.
*Recorded so the next session does not spend a tool search rediscovering it.*

**The workaround was available and was not taken.** `create_sheet` plus copying rows would produce a
sheet with the right name and a **new sheet ID**, breaking every citation of `838802392352644` in the
charter, the change logs and the Wiki, and losing the cell history and the `Health` column formula. A
rename that changes the identifier is not a rename.

## 2. `Machinery & Asset Log` is the wrong name, and the columns say so

The proposal suggested it. **Reading the sheet's eleven columns first says otherwise**: `Health`,
`Document No.`, `Direction`, `Date`, `Category`, `Title`, `Entities involved`, `Description`, `Status`,
`Owner`, `File link`. Its `Status` options are `Draft` / `Issued` / `Superseded` / `Void`. **It is a
document register.** It holds no asset codes, no machines and no values.

Worse, the Workshop workspace **already** holds **Machinery Register - Database** (`1754351980906372`),
the actual asset register. `Machinery & Asset Log` would trade one estate-wide collision for a closer
and more confusing one **inside our own workspace** — the exact failure the task exists to prevent.

**Proposed instead: `Workshop Document Log (local mirror)`.** The sheet's own `Document No.` column
description already says what it is: *"This sheet mirrors machinery-relevant rows; the group register is
canonical for the next free number."* **The name follows the column note; the column note was not
written to fit a name.**

## 3. The charter line Alex asked for is already in the charter, twice

`CLAUDE-Rules.md` **§6a**: *"never edit or delete a row on the shared group Document Register
(append-only, in-scope documents only, and only once write access is confirmed — not yet done)"*.
**§6b**: *"Shared group Document Register write access still not confirmed."*

**So nothing was added.** A third line saying the same thing would make the charter longer and no
clearer, and §6a-i holds that an inbound `Raw/` note is a proposal whose claims get checked — including
its claim that something is missing. *This one asked for a line that was already there; the check was
reading the file it names.* If the owner wants different wording, that is a charter change and needs
their word, which is where the second half of `AWT-0087` now sits.

## 4. A correction carried here rather than into the file that holds the error

**`Outputs/change-log-index.md` is 9,177 B, not 9,172.** Three places say 9,172: §8f of
`change-log-2026-09-23-t016-root-cause-corrected.md` (twice, once in prose and once in its size table)
and the period-split row of `Outputs/kb-registers.md`. The figure was true when written and stopped
being true twenty minutes later, when the index was republished with size **ranges** in place of exact
cross-file figures — the 9,172 copy is in `Archive/` with the reason in its filename, and that republish
was never written down.

**The registers row is corrected, visibly. The 2026-09-23 change log is not**, and that is deliberate:
correcting three byte figures in it means re-emitting 26,479 B to Drive by hand, which is the same
trade `AWT-0089` was left open on — §3 forbids rewriting a large file for a metadata field, and manual
re-emission is where this KB's byte discrepancies come from. **The correction lives here instead, in
the file that is cheap to write, and the stale figures are named so they are found rather than
believed.**

## 5. What the owner does next

1. Rename sheet `838802392352644` in the Smartsheet UI — `Workshop Document Log (local mirror)`, or a
   name of their choosing.
2. Tell Darius the name. **The sweep is then small and is already scoped**: `CLAUDE.md` §1 (Live data
   sources), `CLAUDE-Rules.md` §6a (the allowed-sheets list) and `CLAUDE.md` §0a (Reach). Change logs,
   snapshots and archived copies **stay as written** — they are dated records of what the sheet was
   called at the time.
3. Confirm, or correct, whether the ruling Alex cites on the charter line is theirs. **Held, not
   assumed** — §6a-i, and nothing was written to the charter on it.

## 6. Files touched

| File | What changed |
|---|---|
| Smartsheet `Tasks & Requests` (`8860839228606340`), row `1646386163091332` | `AWT-0087` → **Blocked**, with all three findings and the blocking condition in `Response / result` |
| `CLAUDE-Rules.md` §6a | the UI-action sentence now covers renaming a sheet as well as deleting one |
| `Outputs/kb-registers.md` | the 9,172 figure corrected visibly; this session's Outputs row added |
| `Outputs/change-log-index.md` | this session's row, newest first |
| `Outputs/change-log-2026-09-24-awt-0087-rename-blocked.md` | this file |
| Smartsheet `Help & Lessons` (`7780569054316420`), row `7664378374129540` | **`HL-0050` raised** — see §7 |

## 7. Surfaced on the Hub, per §0b Rule B

**`HL-0050`**, Tooling / how-to, Open: *"I can't" has two causes that look identical and need opposite
responses — the permission is missing, or the tool is. Report which one, and check before reporting
either.* An access problem is escalated to whoever grants access; a capability gap is a UI action for a
human or a request for a connector tool. **Asking the wrong person costs a round trip**, and this task
would have read as an access problem — `accessLevel` is `OWNER`.

It carries the check (access level first, then whether the operation has a tool at all, *including behind
a progressive-disclosure search — a connector's visible toolset is not its whole toolset*) and the
refusal (**do not manufacture the capability**: rebuilding a sheet under the wanted name changes its ID).
**Raised, not assigned** — it is already actioned here, and the shape is estate-wide. Second cousin of
`HL-0042`, *a limitation is a property of the call you made*.

**Nothing was renamed, and nothing was written to the charter beyond §6a's capability note.**
