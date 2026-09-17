# Change log — 2026-09-15 — Operational systems built (maintenance, troubleshooting, SmartCabinet)

**Session 9.** Owner request: *"create a system, which involves routine maintenance of machinery;
troubleshooting; work with design software SmartCabinet."* Confirmed via AskUserQuestion: SmartCabinet
= cabinet design/CNC **+ 3D visuals + CRM**; tracking = **Smartsheet-backed + Wiki**; build =
**framework + real content mined from the machine manuals** now, SmartCabinet a draft skeleton.

## What was built

**Smartsheet (Workshop workspace):**
- **Maintenance Schedule** (`6753985971226500`) — one row per recurring maintenance task, RYGB `Health`
 by due date (`Next Due = Last Done + Interval (days)`; Blue = untracked/condition-based, Green >14d,
 Yellow ≤14d, Red overdue). Seeded **30 tasks** from the manuals: Hebrock F4 MT-001…014, Altendorf
 F45 MT-020…028, Vitap K2 MT-030…036.
- **Fault Log** (`414932606781316`) — one row per fault, RYGB `Health` by Status (Red Open / Yellow In
 Progress / Blue Monitoring / Green Resolved). Seeded **FL-001** = the resolved Hebrock corner-rounding
 fault.
- Both mirror the existing Safety Check Log's RYGB pattern (formula set via `update_column`).

**Wiki (two new categories `Troubleshooting/` and `Software/`, plus Processes):**
- `Processes/machinery-maintenance-system.md` — the maintenance system overview.
- `Processes/maintenance-schedule-{hebrock-f4, altendorf-f45, vitap-k2}.md` — the three machines'
 manual Chapter-7 schedules, mapped to the MT-### rows.
- `Troubleshooting/troubleshooting-and-fault-log-system.md` — the troubleshooting system overview.
- `Troubleshooting/troubleshooting-{hebrock-f4, altendorf-f45, vitap-k2}.md` — per-machine fault
 references (Hebrock §8.2 + the resolved incident with its practical lesson; F45 mechanical fault
 table + full ElmoDrive error-code list; Vitap §7.8 table + §7.6 time-out).
- `Software/smartcabinet-and-production-workflow.md` — **draft**, anchored on the owner-provided
 furniture business-process map (`2026-01-27_BP scheme.pdf`, in the group KB Raw): the
 enquiry→quotation→engineering→production→delivery lifecycle, and how SmartCabinet (design + 3D
 visuals + CRM) drives the F45 (cutting), Vitap (boring/routing) and Hebrock (edge banding). Product
 specifics (name/version, file formats, where CRM data lives) flagged `[confirm]`.
- `Decisions/2026-09-15-operational-systems-scope-extension.md` — records the scope extension and
 choices.
- `index.md` updated; `CLAUDE.md` bumped to **v5** (new categories, new live sheets, §7 snapshot).

## Concurrency reconciliation (important)

This build overlapped **Session 8**, which was registering the **Vitap K2-2.0 (`FA2304`)** and the
**Inventair MK2 MTFA (`FA2305`)** at the same time. That was caught mid-build via `kb-registers.md`.
Reconciled: folded the Vitap into the maintenance + troubleshooting systems (added MT-030…036 and the
two Vitap articles), corrected `index.md`, `CLAUDE.md` §7 (which had briefly described the two machines
as "not registered"), and the SmartCabinet article. **Lesson recorded in CLAUDE.md §3: don't run two
sessions on this KB at once; re-read the live index/registers before recreating a control file.**

## Judgement calls / boundaries

- **Daily/Weekly cleaning tasks left un-dated (Blue)** — habitual; only the periodic
 (monthly/annual/2-yearly/hours) items carry due-date RYGB. Entering a `Last Done` date activates
 tracking on any row.
- **Vitap §6.8 safety check (MT-036) not added to the Safety Check Log** — its manual, unlike the
 F45's, states a pre-cycle functional test with no written-log requirement. Flagged for the owner
 (Task T013), not assumed equivalent.
- **`FA2302` / `FA2305` extractors not in the maintenance system** — no manuals yet.
- Built and recorded only; no company committed, no spend authorised, no regulator/manufacturer
 contacted, shared group Document Register untouched (§6a).

## Open for the owner

- **SmartCabinet specifics** to move the Software article out of draft: product/version, export file
 formats to each machine, where CRM/customer data lives (cite, never copy client personal data).
- **Duplicate Workshop Smartsheet sheets** (Document Register ×3, Machinery Register ×2, Tasks ×2)
 from setup — tidy to one of each.
- Carried machine items: `FA2303` expired certs (T007) + first monthly check (T008) + annual PTC
 check (T011); Vitap §6.8 (T013); `FA2305` supersession of `FA2302` (T010/T014); ownership (T004).
