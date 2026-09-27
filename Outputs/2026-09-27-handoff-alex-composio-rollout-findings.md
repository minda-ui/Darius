# Hand-off to Alex — two gaps in the Composio rollout checklist

**From** Darius (Workshop of Furniture Making KB), 2026-09-27.
**Re** `2026-09-27_Proposal_Composio-Rollout.md`, dropped in this KB's `Raw/` at 15:13, and the checklist it
points at (`https://claude.ai/artifact/QyqFKFU5spRQyBB2viLDxp`, owner: Alex).

**This is a proposal back, not an instruction.** Same footing as the note that arrived: material for the
rollout's owner to check and decide on. Darius does not write into another employee's governed files
(§6a-i), so this sits in Darius's own `Outputs/` to be collected.

**Status here:** rollout **adopted** on Minda's instruction, CLI installed (`0.4.1`), login verified as
`minda@fishboneconstruction.co.uk` / `minda_workspace` / `account_type: human`. Owner ruling for this seat:
**Drive and Smartsheet toolkits only, no Gmail** — §0a gives Darius Drive + Smartsheet + Web (read), and
*"Darius logs and tracks, it does not send"*. Tracked as `AWT-0136`.

---

## 1. There is no Smartsheet toolkit — and that reaches the whole estate

```
composio search --toolkits smartsheet
→ "Invalid toolkit slugs: smartsheet" (code 4305, ToolRouterV2_InvalidToolkitSlugs)
```

Semantic searches for Smartsheet concepts return `googlesheets` and `googlesuper` instead, which are a
different product. **So for this seat the rollout covers half of what it was adopted for:** Drive gains a
fallback, Smartsheet does not.

**Why it is worth your attention beyond this KB:** the **Workforce Hub itself is Smartsheet**
(`8860839228606340`), as are the Machinery Register, Tasks, Fault Log, Maintenance Schedule and Safety Check
Log. Every seat that coordinates through the Hub has its system of record on a platform this fallback layer
does not reach. If the rollout's premise is *"native connectors break, so have a second path"*, then for
Smartsheet there is still exactly one path.

**Not a blocker, and not a reason to stop:** Drive alone is worth having. But the checklist's framing —
Composio as a fallback for the connectors that broke — should probably say plainly **which connectors it
cannot be a fallback for**, so no seat assumes cover it does not have.

## 2. The shared org exposes every company's connections to every seat

`composio connections list` in `minda_workspace`, from a **workshop** KB session, with none of these
belonging to Darius:

| Toolkit | Connections visible |
|---|---|
| `quickbooks` | **6 across five companies** — `fishbone-waste-qb`, `fishbone-holdings-qb`, `fishbone-commercial-properties-qb`, `fishbone-properties-qb`, `fishbone-qb2`, and `fishbone-qb` **EXPIRED** |
| `gmail` | **3** — `fishbone-ops-gmail`, `fishbone-ops-gmail-v2`, `fishbone-gmail` |
| `googledrive` | 1 — `fishbone-gdrive` (plus `darius-googledrive`, newly linked) |

**The consequence:** aliasing by seat name, which the note recommends, makes *selection* unambiguous — it
does not make it *enforced*. Any session signed into this org can execute a tool against any connection in
it, whatever that seat's charter says. Concretely: the owner ruled **no Gmail** for Darius, and three live
Gmail connections remain reachable from Darius's CLI. **That ruling is currently a policy observed by the
assistant, not a boundary enforced by the tooling** — and a workshop assistant can see five companies'
accounting.

**Worth checking, since your checklist is the right place for it:** whether Composio's permission groups or
per-seat projects can scope a login to its own connections. Every listing above showed
`"permission_group": null`, so either the feature is unused or it is not in play here. If scoping exists,
the rollout is the moment to apply it — retrofitting it across seats afterwards is harder.

**Also:** `fishbone-qb` shows **EXPIRED**, which looks like the QuickBooks auth failure the proposal was
written about. If so, the note's own evidence is still sitting in the org unresolved.

## 3. One practical addition for any seat in a cloud container

The install line `curl -fsSL https://composio.dev/install | sh -s -- @composio/cli@0.4.1` is **refused by
the agent safety classifier** in this environment as *[Code from External]* — a remote script piped into a
shell. It ran only when the owner issued the command herself. Two things follow for other seats:

- The three Bash allow rules in the checklist **do not cover the installer**. They permit
  `composio execute`, `composio link` and `composio connections remove` — the CLI once it exists, not the
  command that fetches it.
- **Installing on the owner's own machine does not help a cloud seat**: Composio keeps auth per machine
  (`~/.composio`), so the CLI must exist in the seat's own container. The mechanism that sticks is the
  **environment's setup script**, which runs at each session start — and it lands the CLI at the same moment
  the permission rules load.

Also worth a line in the checklist: the installer's **agent-plugin step fails** (`Release
@composio/cli@0.4.1 not found`, HTTP 403) and suggests `composio setup --target auto --yes`. That installs a
plugin into the seat's own agent host. Darius declined it as an owner decision rather than a rollout step;
other seats will hit the same prompt and should be told what it does.

## 4. One thing that worked better than advertised

`GOOGLEDRIVE_UPLOAD_UPDATE_FILE` updates a Drive file's content **in place, from a local path, keeping the
file id**, with Drive holding the prior bytes as a revision. Verified at 392 B and at 37,297 B — id
unchanged, revision count 1 → 2, byte-identical on download, 5.7 s.

For this KB that is more valuable than the fallback itself: §1 has said since v1 that *"Drive has no patch
API, so every change re-emits a whole file by hand"*, and the hand-retyping is where our byte discrepancies
have actually come from. **Put to Minda as a charter amendment**, not adopted unilaterally:
`Outputs/2026-09-27-proposal-drive-in-place-update.md`. **Flagged here in case other seats are carrying the
same constraint and the same workaround.**
