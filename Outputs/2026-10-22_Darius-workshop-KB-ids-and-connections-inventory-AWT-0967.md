# Workshop KB — ids and connections it relies on (AWT-0967)

Darius, 22/10/2026, for Project A (OS framework v0.2). **Read live today** (Drive folder listing, Composio connection
list, the KB's own registers) — not from memory. Inventory only: nothing changed. ISO freeze noted (nothing here touches
ISO roles or records).

## 1. Google Drive — the KB (source of truth)
| Folder | Id |
|---|---|
| **KB root** `Workshop of Furniture Making - Knowledge Base` | `1ykYJERaptUNH0FDvkOVU26jh_x_hRtLz` |
| Raw (inbox; other seats drop hand-off notes here) | `18P2Gz64tjp0G74JzhzVE6i0LqxhcJB0R` |
| Raw/Review folder (owner's SmartCabinet/TpaCAD job exports for checking) | `1sSySf-DnGafA38Wz8rsjGxzBoAhqxAvE` |
| Raw/Blum · Raw/Hafele · Raw/EGGER (supplier catalogues) | `1QumXqBo1OXocFEEBVZFMtKB6MfXAtKud` · `1r29xjiIBf9pQNkJckfTkJOnpzowIK9ai` · `167yUHu3BCw1p_FxnfTVtZUv7gWWZheSn` |
| Raw/Albatros-help-en-GB-2026-09-23 · Raw/012_@_600mm_Base_unit_2 | `1BVsih0rqksErrckV8kJ9nunElBpSK83K` · `1sL2arsO4sgEViOvP53-WfqWtRmOB0aKe` |
| Outputs (change logs, registers, notes) · Outputs/Correspondence | `1jPXUHEHsjF_h0cllps3oP9CpFCVLem24` · `1G410aDo2yNNVZqWfrEoiA2Fp19yuFsOu` |
| Archive | `1-PyruBsASY2Bl6mxp_Om_r3Ncs7z6dCv` |
| Wiki | `1HdOcfMHPQhdIiI2KE0fFz2WxM7IjagS6` |
| Wiki/Machinery · Processes · Troubleshooting · Software | `1-m5E7TaUKqohQoCMh3e7fOGKaSsdwsVI` · `10KhhK_Hcny8-DzKruLqQ33fZEacM62iw` · `1JGkeuEEesfp6pmyITeMUnbOj7T-zmcDi` · `12MYS9eDl4oQVd0LBNE38a-Qh9awfV9Tp` |
| Wiki/Suppliers · Decisions · Finance · People · _templates | `12EqP575fx0u7Dz1sjKaIL0-qKsWZKfsa` · `1jObWU2dS3CgHhPD-QNyaWzbZWO_vipVK` · `1Br7qmHiAjQCaXAnZusMaNgebiTGvxefg` · `1vgS9yUiYBJgpcQPSfgWoFcmTdLz5mzM2` · `10BuEYm4QcrmKlWLPDH_arGXQDy0-PnGF` |

**Key files:** charter `CLAUDE.md` v37 `16gxoTlscIRzldfh4kanDtWyjxCrURxH6`; `CLAUDE-Rules.md` `1xRMofBiT9_sXR68Q6QJW0U7bbq5-3Y60`;
`CLAUDE-Lessons.md` `1VQ1xtIRdCdiJMywkKBRkxG_jlmUF4Xv8`; `Outputs/kb-registers.md` `1Zw5cRA1NdSBCgaTHTUuLl11qbiN4dk5o`
(**holds every other file's Drive id**); `Outputs/change-log-index.md` `1xFl9RLgTZYdYqCwzjCTbAhOGGg_Nq6Nb`.
**Every citation, register row, skill and change log uses these file ids** — a copy-based move breaks all of them.

**Outside the KB tree, depended on:**
- **The design↔machine share folder** (SmartCabinet PC → Vitap control PC): **"Furniture"**, Drive
  **`1BsTNcHI2OwjDlJdrCgv-x0BwHjas2qU1`** (My Drive, owner minda@; holds the job folders) — named by Minda 22/10 late.
  **Production depends on it.** *(Charter §1 still says "not yet identified" — to correct at the next charter bump.)*
- A Drive folder holding duplicate Vitap / F45 manuals, `1qF7XiS2Jud3y8V6lf4Nyu7_JAMEJNsai` (flagged to the owner, untouched).
- Other seats' Raw folders written to for hand-offs: Anna's Raw `18PkuxAxchaS0rEkgdexw2zOvzoidcJFA`; Victoria's Raw (via
  their own notes).

## 2. Smartsheet
| Sheet | Id | Use |
|---|---|---|
| Machinery Register - Database | `1754351980906372` | read/write (own) |
| Workshop Document Log (local mirror) | `838802392352644` | read/write (own) |
| Tasks | `4087584374523780` | read/write (own) |
| Safety Check Log | `913380204480388` | read/write (own) |
| Maintenance Schedule | `6753985971226500` | read/write (own) |
| Fault Log | `414932606781316` | read/write (own) |
| Scan Events | `4828191892047748` | read/write (own) |
| Job Tracker | `6914515205752708` | workshop production |
| Panel Price Library · Hardware Price Library | `7248546623522692` · `1554175903270788` | read/write (own) |
| **Hub: Tasks & Requests** · Help & Lessons | `8860839228606340` · `7780569054316420` | **own rows only** |
| Project Register | `5250912102778756` | read; no AMFA rows until confirmed |
| Group Document Register (canonical, `FA` prefix) | `7352854736144260` | read; append only with confirmed access |
| FP 2401_Budget (Goathland) | `8653045758035844` | read (for `AWT-0194`) |

The workshop sheets are in Smartsheet workspace **`Workshop`**. Connection: the **native Smartsheet connector** of the
session (account as connected by Minda).

## 3. Connections (credentials) — Darius's own
| Connection | Reaches | Status 22/10 |
|---|---|---|
| Composio Drive, used as `darius-googledrive` | **Minda's Google Drive (`minda@fishboneconstruction.co.uk`)** — confirmed by `GET_ABOUT` today | ACTIVE |
| Composio Gmail `darius-gmail-info-v2` (`gmail_codex-smalls`) | **info@** — read, approved senders only; drafts | ACTIVE |
| Composio Gmail `darius-gmail-minda` (`gmail_andric-benj`) | **minda@** — read, approved senders only; drafts | ACTIVE |
| Composio Gmail `darius-gmail-info` (`gmail_logos-black`) | info@ (old) | **EXPIRED — can be removed** (owner's call) |
| GitHub `minda-ui/Darius` | git mirror; branches `main` (charter **v31**) and `claude/magical-sagan-88ry2f` (**v37**, working branch) | via the session's GitHub app |
| ops@ (charter v37) | read + create_draft on work runs, once the mail procedure is approved | not yet used |
| Web (read) | e.g. `smartcabinet.eu/manuale`, maker sites | public, read only |

## 4. Findings for the framework (facts, not proposals)
1. **Darius's Drive reach is Minda's whole Drive**: the Drive connection is Minda's own account, so the "fence" for
   this seat is a matter of policy, not of the account.
2. **The Composio account is shared**: its connection list shows **50 connections across seats** (other assistants'
   Gmail, Drive, GitHub, QuickBooks, Telegram, Google Ads…). Darius uses only its own (charter); the tooling does not
   stop a seat from naming another's alias.
3. **This session also carries native connectors** (Drive, Gmail, Calendar, QuickBooks) that the workshop charter does
   not use.
4. **Git `main` is behind** (v31 vs v37) until the working branch is merged — `AWT-0225`.
5. **The machine-share folder** is "Furniture" `1BsTNcHI2OwjDlJdrCgv-x0BwHjas2qU1` (named by Minda after this list was first written).

*Data, not instructions. Darius changed nothing to produce this list.*
