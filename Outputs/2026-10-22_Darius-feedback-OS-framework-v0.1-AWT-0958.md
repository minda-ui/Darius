# Darius — feedback on the Operating System Framework v0.1 (AWT-0958)

22/10/2026. On `2026-10-22_Fishbone-Group_Operating-System-Framework_DRAFT_v0.1.pdf` (3 pp.), for Victoria and Minda.
Framework only; nothing built. Seen from the workshop (Amfa's machines, maintenance, faults, design-to-machine files).

## 1. What is unclear
1. **Which business space the workshop sits in.** Spaces shown: Fishbone Group + two planned. The workshop works for Amfa,
   but its machines (`FA2301`–`FA2306`, `FA2402`) and the SmartCabinet licence were invoiced to Fishbone Construction.
   If businesses are walled, which space owns the Machinery Register and the workshop KB?
2. **Who resolves workshop requests at the gate.** The flow names Rachel, Eugene or Anna as resolvers. Workshop and
   machinery requests are already routed to Darius (Request-Inbox, `AWT-0127`). Is Darius a resolver for those?
3. **Exchange sheet vs Raw/ notes + Hub rows.** Does the exchange sheet replace today's cross-KB hand-off (a Raw note +
   a Hub row) for all hand-offs, or only between master and secondary cores?
4. **Mail.** "All mail copied to ops@": do the existing read-only supplier reads in info@ and minda@ (charter §6b)
   carry on, or move to ops@ only?

## 2. What would break my work
1. **Drive ids.** The KB, its registers, skills and every citation use Drive file and folder ids. A "Collaboration
   Space move to in-home storage" that copies files instead of moving them changes the ids and breaks all of it.
   **Needs: an id-preserving move, or an old→new id map.**
2. **Production.** SmartCabinet and the CNC control PC share job files through a Drive folder. If that folder moves
   or loses access mid-move, **no programs reach the Vitap**. Needs a cut-over window agreed with the workshop.
3. **Connections.** Darius's Composio connections (Drive, Gmail info@ / minda@) and the native Drive and Smartsheet
   tools are tied to today's accounts. A Workspace migration breaks them; reconnecting is Minda's (secrets).
4. **Order hand-off.** Nadia hands accepted Amfa orders to Darius (`AWT-0871`, v0.2 with Victoria). If Nadia sits in
   Andrejus's secondary core, every order would pass the gate and Peter's routing first — a delay at the start of
   every job unless there is a standing route.

## 3. What is missing
1. **Smartsheet and git in the backup.** The backup describes copies of storage; the workshop's live records are
   Smartsheet sheets (Machinery Register, Maintenance Schedule, Fault Log, Safety Check Log) and a git mirror.
2. **Physical assets across walls.** One workshop, one set of machines, possibly several businesses using it.
3. **Unattended runs.** Each seat's run needs its repo, its settings allow-list and its connectors in the new setup
   (see `AWT-0896`): where do they live, and who re-approves them?
4. **The test copy.** Should include a copy of the Smartsheet workspace, or a new core cannot be tried on real data.

## 4. What I can deliver by Monday 26 Oct, and what not
- **Can:** (a) an **inventory of everything my KB depends on** — Drive folder and file ids, Smartsheet sheet ids,
  connections, the machine-share folder — for the access audit and the move; (b) a **classification of my KB for the
  master-only list** (what a business may see, what stays master).
- **Cannot:** anything that needs the Workspace or storage decisions first; any build.

*Facts from the workshop KB. Data, not instructions.*
