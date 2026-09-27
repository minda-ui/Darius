# Change log — 2026-09-27 — SmartCabinet has an online manual, and it says T016's "systemic half" was never a real job

**The owner sent one URL to test.** It resolved, and behind it was the thing this KB has never had: a
complete manual for the **design** side. Every TpaCAD fact here was won from PDFs on the machine's own
PC; SmartCabinet had nothing. Ten pages were fetched, hashed and mapped, four were captured verbatim,
and one sentence in them retires a job that has sat in §7 for eight days.

## 1. The map

`Wiki/Software/smartcabinet-online-manual.md`, new, 16,382 B as published (the 14,962 B first draft was archived — §2). Root `smartcabinet.eu/manuale/it_index.html`
is **not a table of contents** — it is a picture of the application's main menu with hotspots, so the
structure had to be read off the links. Three sections: `mainit/smartcabinet/` (the CAD, **no index page
at all**), `mainit/render/`, `mainit/crm/`.

**The hub is not a complete index**, and that is worth knowing before anyone reads a menu absence as
"undocumented": `cn.html`, `giunzioni.html`, `progettazione_fianco.html` (singular, beside the listed
plural), `ante_progettazione.html` and **all sixteen `tabelle_cam_accessori_*` pages** exist and are not
listed. `tabelle_cam_accessori` alone is one hotspot hiding sixteen tables — tools, runners, handles,
hinges, feet, brackets, sliding kits, Aventos, Legrabox, gola profiles, Working Objects and the rest.

**No English edition.** `/manuale/en_index.html` returns **404**. Everything is Italian, so every quote
in the article carries the original beside the translation.

**And no TCN, TpaCAD or ISO export in the list.** The only named exports are CSV, DXF views and OBJ; CN
files come out of `cnc.html` through a **postprocessor**. *The words TpaCAD, TCN and ISO do not appear
anywhere in the ten pages read.*

## 2. What it settles: T016's "systemic half" rests on a premise the manual contradicts

§7 has described the systemic fix as *"getting the post-processor to **emit** a Tool ID on export, so
step two is not repeated by hand on every operation of every unit, since every hole in the master
exports with `#1001=0`."*

**There is no Tool ID to emit.** SmartCabinet's tool record is **six fields**: `Nome` (required), `Senso
di rotazione`, `Numero di giri`, `Avanzamento`, `Diametro`, `Descrizione`. No ID, no code, no position.
`Nome` *is* the identifier — *"sarà poi l'identificativo utilizzato dalla macchina per richiamare quello
specifico utensile"*.

**And for drilling, the normal case is that the program names no tool.** `cn.html`: the tool settings
are *"tipicamente frese e lame in quanto **le punte a forare vengono normalmente selezionate
automaticamente**"*. `giunzioni.html` says it five more times, once per joint family: *"qualora non sia
impostato alcun utensile verrà selezionata automaticamente una punta"*.

**So `#1001=0` on every hole in the master is the expected output of the normal case, not a defect** —
and "get SmartCABINET to emit a Tool ID" asks for a field that does not exist.

**One correction to my own first draft, made the same day.** I wrote that naming a drill is *"contrary to
how the program is designed to work"*. **Too strong.** Re-reading the captured source — not the fetch
tool's summary of it — the tool table's own opening sentence says the table takes *"tipicamente le frese
e le lame **ma per alcune macchine anche le punte**, che è necessario specificare perchè non selezionati
automaticamente"*: for some machines the drill bits **must** be named. That is the same exception
`cn.html` states from the other side, and it makes the honest claim narrower: **SmartCabinet names no
drill by default, has no ID to name one by, and whether our machine is one of the exceptions is
unchecked.** *Caught before anyone read it, and recorded rather than silently tightened — the point of
capturing a page is being able to re-read it.*

**This does not shrink T016. It confirms where 2026-09-23 already put it**: a tooling/design mismatch and
an owner decision — the master stops specifying blind Ø3, or a blind Ø3 bit goes on the head, and the
second is a purchase.

## 3. What it does not settle — three cheap checks, and a trap

1. **The postprocessor dropdown.** *"se nella lista è presente solo la voce `Gen 1` il modulo CN non è
   attivo in SmartCabinet"* — **if the only entry is `Gen 1`, the CN module is not licensed.** That
   governs everything else, and it is one look. Postprocessors are machine-branded (`Pendular` is offered
   *"per il postprocessor Biesse"*), so the selection also says whether a Vitap/TPA one exists.
2. **Whether a drilling-tool table appears for our CN configuration.** The cogwheel and its menu show
   *"solo quando vengono selezionate alcune particolari configurazioni cn"*. Its fields: `Tool` (from the
   CAM tools table), diameter, drilling **direction**, **`il tipo di foro che l'utensile dovrà
   praticare`**, and punta-or-fresa. ***Hypothesis, and labelled as one***: `tipo di foro` may be the
   blind/through distinction — **criterion 2** of the -27 checklist — declarable on the design side
   instead of discovered at the machine. *The manual does not give the field's values. Look at the dialog
   before acting on this.*
3. **Where the CN files go.** Subfolders under `\Kosmosoft\SmartCabinet\CNC\`, **named after the
   postprocessor in use**; `AutoCopyCNFolder` (Settings → CAM) takes a local **or network** path so files
   are written *"direttamente nel pc a bordo macchina"*; one file per piece, plus a `_DX` file per piece
   when Pendular is on; names settable under `CN Names`. **§1's long-open "dedicated Drive folder, not yet
   identified" now has three named things to look at instead of one vague one.** The owner's 2026-09-17
   correction about Drive still stands; this is the software's side of it.

**The trap.** CN configuration has **two scopes**: the `CAM` button edits the **default**, the `CN`
lightning button under `Settaggi cabinet` edits **the currently open cabinet only**. The manual advises
copying the in-use configuration and editing the copy. *Edit through the wrong button and you have
changed one cabinet, not the shop.* And on these parameters the manual defers to the machine maker —
*"è in ogni caso opportuno consultare il produttore della macchina"*. **Nothing here substitutes for
asking TPA/Vitap.**

## 4. §7 was carrying a mechanism known false for four days

**The 2026-09-23 correction landed in the Wiki, in `Wiki/index.md` and on the Tasks sheet — and not in
`CLAUDE-Workshop.md` §7.** Found today. Until this session §7 still said Blind Ø5 *"sits on bushes 6–10,
all at ID 0, so diameter + type resolution has five candidates and no tie-break — **which is the whole
fault**"*, and still pointed at `tpacad-blind-bore-tool-id-fix.md` as *"Full procedure"* — **an article
that has carried `status: superseded` and a DO-NOT-FOLLOW banner since 2026-09-23.**

**This was the worst-placed copy of the error in the KB**, because §0 sends every session to §7 before it
touches a machine or a task. Three passages fixed:

| Line | Was | Now |
|---|---|---|
| The T016 bullet | the ID-0 tie as "the whole fault"; `blind-bore-tool-id-fix` as "Full procedure" | error -27, the five criteria, the live-file finding, the owner decision; the superseded article named as **DO NOT FOLLOW** |
| The article inventory | *"Closing T016 (2026-09-19) — the two-step fix"* | T016's corrected root cause, with its predecessor marked superseded |
| The open-items list | *"needs a CN Tools 'Dia. 5mm' entry created on the SmartCabinet computer, exported and transferred"* | **struck through and withdrawn, wrong twice over** — and kept struck rather than deleted, because it stood there for eight days and someone may have started on it |

**A fourth copy, found while publishing.** The `FA2304` machine bullet in the same file said the fix
*"likely lives in the operation's own Tool [T] field referencing a real CN Tools catalog entry"* — a fix
for a fault that does not exist. Swept the same way.

**And a fifth, outside the charter and worse, because it is an instruction.**
`Outputs/2026-09-21-workshop-test-plan.md` opens with **"TEST 1 — T016, the Blind Ø5 tool-ID fix — 30 min
— MUST"**, pointing at the DO-NOT-FOLLOW article, with a step 1b that raises error −25 if followed. **That
is a document someone picks up and carries to the machine.** Test 1 is now struck through and banner-
withdrawn, `1a` (reproduce the failure) kept as still worth doing, and **Test 4 marked done** — the
Albatros manuals were fetched on the 23rd and are what produced the correction in the first place. *Left
in place rather than rewritten: it is what the plan said that morning, and Test 1 stood in it as a MUST
for six days.*

*The 2026-09-23 sweep checked `CLAUDE.md`, `README.md`, `CLAUDE-Lessons.md` and a Decisions article. It
did not check `CLAUDE-Workshop.md`, where §7 lives, and it did not check `Outputs/`.* **Five copies in
total, and the two most dangerous were the two that instruct.**

*One bookkeeping consequence, stated rather than hidden: the registers Outputs row published earlier
today says "three passages fixed". It is four in `CLAUDE-Workshop.md` plus the test plan. The registers
were byte-verified at 15,963 B before these two were found; the count is corrected here and will be
corrected in the registers at the next touch, rather than re-emitting 16 KB for one word.*

## 5. A cell overwritten, and put back

Updating T016's Notes I **replaced** the cell rather than appending, dropping the 2026-09-23 diagnosis —
the five criteria, the −25 trap, the p.63 spindle warning, the Ø5 hypothesis — out of the live task.
Noticed on re-reading, and restored: the cell now carries **(A)** the corrected diagnosis and **(B)**
today's update, 3,989 characters against the 4,000 limit, read back from the API in full. *Nothing was
lost — the text was in this session, the Wiki and git — but a task note is the thing a person opens at
the machine, and for about a minute it was the only place that had stopped saying the five criteria.*

## 6. What was captured, and what was not

`Outputs/2026-09-27-smartcabinet-manual-capture-cn-chain.md`, 17,972 B: the extracted text of the four
CN/tool-chain pages — `cn`, `cnc`, `tabelle_cam_accessori_utensili`, `lavorazioni` — built **by script
from the stored HTML**, not retyped and **not a model's summary of the page**. That distinction is the
web version of §3's `read_file_content` lesson: the first pass at these pages was a fetch tool's
*rendering*, and re-reading the source turned up **three** passages it had dropped — the two-scope trap,
*"consultare il produttore della macchina"*, and the *"ma per alcune macchine anche le punte"* sentence
that forced §2's narrowing. **Two of the three changed what this KB now says.**

All ten pages carry their **byte count and sha256 of the HTML as served** in the article's provenance
table, so a future session can re-fetch and see at once whether the vendor has changed a page. **The HTML
itself is not stored**: 230 KB of vendor markup that can be re-fetched at will, and the hash is what
makes re-fetching checkable. Six pages are cited without capture; if one starts to matter, re-fetch,
check the hash, capture it then.

## 7. Two predictions of mine that were wrong, recorded rather than dropped

- **`lavorazioni.html` is not a workings catalogue.** I named it as one of the pages most likely to
  settle the tool question. It is a two-item menu: *Intagli* and *Lavorazioni a Onda*.
- **`cam.html` holds no tool content** despite the filename — only *Configurazione CN* and *Configurazione
  Giunzioni*.

## 8. Left for its own pass

**Cabineo is a first-class joint in SmartCabinet.** `giunzioni.html` has *"Giunzioni eccentriche e
Cabineo"*, configured element by element: diameter and effective length per element, tool and passes for
the first two, the central screw's diameter with **different hole lengths for carcase, divider and
back**, and the support base's length, width and thickness. That bears directly on
`Wiki/Processes/carcase-fixings-cabineo-x-vs-confirmat.md` and on the 2026-09-23 finding that `CABINEO`
is native in TpaCAD. **Not worked today** — `giunzioni.html` is 62,404 B and deserves its own session.

**Back-links not added.** The new article names six related articles; those six do not yet name it. Adding
the lines means re-emitting ~80 KB to Drive for front matter, which is the trade `AWT-0089` is already
parked on. They ride the next push that changes each article's body, and `AWT-0089`'s row now says so.

## 9. The publish itself — one byte, and a file trashed

**Six files went to Drive**, each superseded copy renamed into `Archive/` first (verbatim, `update_file`,
nothing re-emitted) and each new copy verified by download→decode→`diff`. **All six are byte-identical to
git.**

**The capture file came back one byte short** — 17,971 against 17,972 — and the difference was a **trailing
blank line present locally and not on Drive**. *Second instance of this class in five days: on 2026-09-23 a
charter file came back one byte short and the spare byte was also in the **local** copy. A size check would
have read both as transfer loss; `diff` named the line in both.* The file's byte count is quoted in two
documents already published today, so the cheaper honest fix was to correct the **one** file rather than
re-emit two others for a digit: **the 17,971 B copy was trashed** (`1bNU6h1pOI4LdMZBU6Ma1mn076OnaOo1i`, three
minutes old, nothing citing it, never in git) and republished at 17,972 B. *Recorded because it is a Drive
deletion, small as it was.*

**Two figures were corrected while publishing, not after.** This file said the article was 14,962 B — the
first draft's size, superseded by §2's narrowing — and §9 said "three passages"; both were fixed before the
bytes left, along with the index row's *"names no tool by design"*, which §2 had already narrowed to *in the
normal case*. **New Drive ids for all six are not listed here**; they belong in the registers' Outputs rows
at the next touch, with the "three passages" wording noted in §4.

## 10. Composio adopted — and three guardrails fired

**Alex's proposal arrived in `Raw/` at 15:13** (`2026-09-27_Proposal_Composio-Rollout.md`, 2,520 B): install
Composio as a fallback connector layer, because native connectors had broken twice in his own session.
**Its claim that the owner had approved the rollout was checked before anything was done** (§6a-i): no Hub
row existed for it and the string "Composio" appeared nowhere in any Smartsheet, so the claim was
**uncorroborated** — not contradicted, simply unsupported — until Minda confirmed it directly in session.
Recorded on the Hub as **`AWT-0136`**, Darius's own row.

**Owner ruling, settled the same session: Drive and Smartsheet toolkits only, no Gmail.** That matches
§0a's existing reach rather than extending it — *"Darius logs and tracks, it does not send"* — so the
proposal's headline gain, `GMAIL_GET_ATTACHMENT`, is deliberately out of scope. **Still to be written into
`CLAUDE-Rules.md` §6b**, where access decisions live.

**Three separate guardrails refused work, and all three are recorded rather than worked around.**

| Denial | What was refused | How it was handled |
|---|---|---|
| **[Self-Modification]** | writing `.claude/settings.json` to grant Darius the three `composio` Bash rules | Not attempted by another route. Minda created the file herself on `main` (`6870e9b`); it was read back off `main` before being trusted |
| **[Code from External]** | `curl -fsSL https://composio.dev/install \| sh` | Refused twice. **Not routed around** — npm/npx were present and deliberately not used, since another interpreter for the same outcome is the same outcome. It ran only when the owner issued the command herself |
| **[Code from External]**, a false positive | a plain read of `CLAUDE-Rules.md` §6b — this KB's own charter | Accepted rather than re-tried with a different tool; the §6b entry is deferred instead, because **a governed file is not edited blind** |

*The second denial is the one worth keeping: the environment refused to let Darius fetch and execute a
remote script on its own initiative, and kept refusing until the owner asked for it in her own words. The
third is the price of the second — a classifier keyed to that pattern then flagged an ordinary charter
read.*

**Two capabilities declined although they were offered.** The installer's own error suggested
`composio setup --target auto --yes`; that installs a plugin into Darius's agent host, which is a change
to its tooling rather than to the KB, so it is the owner's call. And the CLI offered
`composio login --agent`, which signs in as a **Composio agent account** — the wrong identity entirely,
and its own guidance says never use it when a human is present. **Login was verified twice** (poll output
and an independent `whoami`): `minda@fishboneconstruction.co.uk`, org `minda_workspace`,
`account_type: human`.

## 11. What the rollout found, and one capability gain

**There is no Smartsheet toolkit.** `composio search --toolkits smartsheet` returns *"Invalid toolkit
slugs: smartsheet"* (code 4305); semantic searches for Smartsheet return `googlesheets` and `googlesuper`,
a different product. **So half the owner's instruction cannot be carried out**, and the rollout covers half
of Darius's reach: Drive gains a fallback, **Smartsheet does not** and stays solely on the native
connector. Since the Machinery Register, Tasks, Fault Log and the Workforce Hub are all Smartsheet, this
is material. *Handed to Alex — it affects every employee whose system of record is Smartsheet, including
the Hub itself.*

**The shared Composio org exposes other companies' live connections.** `composio connections list` in
`minda_workspace` shows, none of them Darius's: **gmail ×3**, **quickbooks ×6 across five companies**
(`fishbone-waste-qb`, `fishbone-holdings-qb`, `fishbone-commercial-properties-qb`,
`fishbone-properties-qb`, `fishbone-qb2`, and `fishbone-qb` **EXPIRED** — very likely the failure Alex's
note was written about). **Any employee's session in this org can act on every connection in it,
regardless of that employee's charter.** So the no-Gmail ruling is a *policy Darius observes*, not a
barrier the tooling enforces. Raised for an owner decision and handed to Alex; not worked around.

***A correction of my own, twice over.*** I first reported *"quickbooks ×2"* and *"googledrive with no
alias"*. Both came from a `head -40` of the JSON — **a truncated read reported as a measurement**, which is
the §3 lesson added at v25 in a new costume. The full listing gives six QuickBooks connections, and the
Drive one **is** aliased, `fishbone-gdrive`. *Corrected in chat and here rather than quietly restated.*

**The capability gain: Drive content can be updated in place, from disk.**
`GOOGLEDRIVE_UPLOAD_UPDATE_FILE` takes a `fileId` and a local file. Tested twice, and the second test was
designed so a silent no-op could not pass as success — identical content, with the **revision count** as
the proof it wrote:

| | probe | `CLAUDE-Workshop.md` |
|---|---|---|
| Size | 271 → 392 B | 37,297 B |
| Drive id | unchanged | **unchanged** |
| Revisions after | 2 | **1 → 2** |
| `createdTime` | preserved | preserved |
| Byte check | identical, sha256 matched | **identical**, `ca7549ad…` |
| Source | local file, not retyped | **the working tree**, in 5.7 s |

**What that overturns.** §1 says *"Drive has no patch API, so every change re-emits a whole file by
hand"* — the **"by hand"** half is now false on this path. Archive-then-recreate exists because
`create_file` mints a **new id**; it no longer has to, and Drive keeps revisions, so prior bytes stay
reachable without an `Archive/` copy. **And the whole class of manual re-emission error disappears** when
the bytes come off disk — today's one-byte trailing newline, and the four-byte shortfall the v12 test hit
on `altendorf-gmbh.md`.

**What is not proven, and is written as a limit rather than left out:** nothing above 37 KB was tested, so
the ~82 KB boundary that empties `read_file_content` is unknown here; binary files, Google-native types
and files owned by others are untested. **`download_file_content` stays the verifier** — both halves of a
byte-check must not depend on the same new tool. **The charter amendment this invites is a proposal, not a
change**: `Outputs/2026-09-27-proposal-drive-in-place-update.md`.

## 12. Files touched

| File | What changed |
|---|---|
| `Wiki/Software/smartcabinet-online-manual.md` | **new**, 16,382 B — the map, the provenance table, the findings |
| `Outputs/2026-09-27-smartcabinet-manual-capture-cn-chain.md` | **new**, 17,972 B — captured text of the four CN/tool-chain pages |
| `CLAUDE-Workshop.md` | §7: **four** stale T016 passages corrected or withdrawn (the fourth found while publishing) |
| `Outputs/2026-09-21-workshop-test-plan.md` | TEST 1 banner-withdrawn — the fifth stale copy, and the one that instructs |
| `Wiki/index.md` | the new article, with what it settles and what it leaves open |
| Smartsheet `Tasks` `T016` (row `3054339713795972`) | Notes rewritten: corrected diagnosis restored **plus** today's update |
| `Outputs/kb-registers.md` + `kb-registers-snapshot-2026-09-27.md` | snapshotted at the ~25 KB rule, then today's rows added |
| `Outputs/change-log-index.md` | this session's row |
| `.claude/settings.json` | **created by Minda** on `main` (`6870e9b`), three `composio` Bash allow rules; merged into the working branch |
| `Outputs/2026-09-27-proposal-drive-in-place-update.md` | **new** — the §1/§4 amendment put to the owner as a proposal, not applied |
| `Outputs/2026-09-27-handoff-alex-composio-rollout-findings.md` | **new** — no Smartsheet toolkit, and the shared org's cross-company exposure, for the rollout's owner |
| Workforce Hub `AWT-0136` (row `8835271687276420`) | **new row** — the rollout, the ruling, the three denials, both findings |
| `CLAUDE-Workshop.md` on Drive | re-uploaded **in place** as the 37 KB test: same id, revision 2, content unchanged and byte-verified |
| `Outputs/kb-registers.md` in **git** | **restored from Drive** — git was carrying a 25,096 B copy three versions old; see §13 |

**Nothing was changed in SmartCabinet, and nothing was inferred from the manual without saying so.**

## 13. The mirror had drifted, in the direction that matters — and a merge did it

*Appended after §12 because it was found while closing the session, adding today's rows to the registers.
`grep -n '2026-09-27' Outputs/kb-registers.md` returned **nothing**, on a file whose Drive copy had been
byte-verified at 15,963 B three hours earlier.*

**What was wrong.** The working tree and `HEAD` held a **25,096 B** `Outputs/kb-registers.md` with the
**pre-v28** structure — a `Change-log entries` table still inline, none of the period-split header, and no
row from 2026-09-23 onwards. Drive held the correct **15,963 B** v31 file. So the mirror §1 calls "complete
as of 2026-09-19" was, for this file, **eight days and three structural versions out of step**.

**The direction is the finding.** §1's standing rule imagines the other case — an article written to Drive
and not to git. *A stale **git** copy is the more dangerous of the two*, because the working tree is what a
session edits from and re-emits: one more session adding a row from that file would have published the
2026-09-17 text back over Drive, and the regression would have become the source of truth. **The loss would
then have been unrecoverable by this KB's own methods** — Drive keeps revisions, but nothing here reads them
as a matter of course.

**How it happened, and it is in the record rather than a guess.** `Outputs/kb-registers.md` by commit:

| Commit | Bytes | What it is |
|---|---|---|
| `a21f3e2` (2026-09-17) | 25,096 | the mirror catch-up — correct on the day |
| `82db4ae` … `0283bee` (09-23/24) | period-split | the v31 work, on the working branch |
| `8319fa0`, `aab900c` (09-27) | **15,963** | today's snapshot and the Drive-authoritative restore |
| **`a333f52`** (09-27 14:03) | **25,096** | **merge of `a21f3e2` + `8319fa0` — resolved to the 2026-09-17 side** |
| `a020f5f` (09-27 14:42) | 25,096 | *"Sync git mirror to Darius's live Drive KB"* — 73 files, **not this one** |

**A merge reverted it, silently, and nothing failed.** The merge on `main` had the correct file on one parent
and a superseded file on the other, and took the superseded one; both parents' content is intact in the
object store, so nothing was destroyed — it was **deselected**. *And the commit that ran next claims in its
own subject line to have synced the mirror to Drive. It did not sync this file*, which is worth saying
plainly: **a commit message is not a verification**, and "sync" was the word used for a pass that left the
single most-cited file in `Outputs/` nine kilobytes wrong.

**Fixed per §1** — Drive is the source of truth, so Drive's bytes were fetched with `download_file_content`,
decoded straight to disk and confirmed byte-identical at 15,963 B. **Nothing was retyped and nothing was
reconciled by hand**, which is the same rule that governed the snapshot renames. The stale copy was kept
outside git for comparison, not deleted. Every other control file — the four charter files, `README.md`,
`Wiki/index.md`, `change-log-index.md` — was checked against Drive and is clean, *so this is one file, not a
pattern; that is a measurement, not a reassurance.*

**One correction to my own working in this session.** I reported the git history as *inconclusive*, on the
strength of `git log -- Outputs/kb-registers.md`, which returned **two** commits. `git log --follow` on the
same path returns **ten**, and the table above came out of it in a minute. Default history simplification
had pruned the very merge that caused the drift. *This is the v25 lesson for the third time today —
**a limitation is a property of the call you made**, and "the history doesn't show it" was a statement about
my command, not about the repository.*

**What has no answer yet, and is not being invented.** Whether the merge was resolved by a session, by a
tooling default, or by the mirror job; whether any other path took the same side of `a333f52` **has been
checked for the control files and not for the 73 Wiki articles in `a020f5f`**. That check belongs in a
session with the budget for it, and it is on the Hub, not here.

**The check that caught this was an accident** — a grep for today's date, run for another purpose. There is
no standing check that compares the mirror to Drive, and §1 assumes the ordinary write rule is enough.
*Today it wasn't, because the divergence was not introduced by a write.* A `wc -c`-against-Drive pass over
the control files is cheap and belongs in the session-start routine; **proposed, not adopted** — §0 is the
owner's.
