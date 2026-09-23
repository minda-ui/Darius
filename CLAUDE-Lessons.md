# CLAUDE-Lessons.md — Workshop of Furniture Making Knowledge Base

**Part of Darius's charter. See `CLAUDE.md` for the core and the file map.**

**This file holds the workflow and the lessons.** It is separate because it is append-only and grows every time something is learned — split at **v31** (2026-09-23) so an
ordinary change re-emits this file rather than all 86,856 bytes of the old monolith
(`AWT-0082`; Drive has no patch API, so every edit is a whole-file rewrite).

*Sections keep their original numbers (§3) so every existing citation still resolves.*

## 3. Workflow for processing new items

Group workflow (Detect → Register → Read → Extract → Update → Check → Log → Output → Commit).
Lessons from Sessions 2–15, all on real incidents rather than invented ahead of time:
- For a multi-part scanned manual, extract via background sub-tasks (split across parallel agents
  for large sets, e.g. 8 parts as two 4-part agents) rather than reading everything inline; flag
  illegible/OCR'd figures and cross-part inconsistencies explicitly rather than silently picking one
  reading.
- **A fact stated with an explicit assumption must be revisited the moment real evidence arrives**,
  even if that means renumbering something already assigned (`FA2601`→`FA2301`) — and conversely,
  **ask for the evidence up front when a session's own numbering scheme depends on it** (asset
  acquisition year), rather than assuming and correcting later.
- A genuine compliance/regulatory finding (expired certificates, a mandatory documented check)
  should be surfaced prominently — in Key facts, not just Open questions — and given its own Task
  and, if it's a recurring process, its own `Wiki/Processes/` article and tracking sheet.
- **Manual-derived maintenance schedules and fault tables belong in the operational systems**
  (`Wiki/Processes/maintenance-schedule-*.md` + the Maintenance Schedule sheet;
  `Wiki/Troubleshooting/troubleshooting-*.md` + the Fault Log), not only inside the Machinery
  article. When a fix or diagnosis differs from the manual in practice, record that lesson in the
  troubleshooting article (the corner-rounding incident is the first example).
- **Two similarly-worded manual sections are not necessarily the same requirement.** The Vitap's §6.8
  "Safety Device Efficiency Check" looks, by name, like the F45's mandatory monthly check — but its
  text describes a pre-automatic-mode functional test with no stated interval or "log this"
  instruction. Don't extend a Processes article or a Smartsheet log to a new machine on
  name-similarity alone (Task T013).
- Don't assume one finding resolves another just because they're related — e.g. a new centralised
  extraction unit plausibly supersedes an older single-machine extractor, but that's a task to
  confirm, not a status to assert. **Closed 2026-09-17, and the restraint paid**: the answer to "did
  `FA2305` supersede `FA2302`?" was *neither*. Both were sold and replaced by a third machine
  (`FA2402`) that the register did not contain. Had either been marked "superseded" on plausibility,
  the correction would have had to unpick a status, a date and a relationship; as it was, nothing
  needed unpicking.
- **A formula validated on one invoice becomes evidence for others once repeated.** The 70%-balance
  cross-check was confirmed independently on invoices 100153, 100154 and 100155 — a third clean match
  closes the underlying question generally, not just for the invoice it was first raised on.
- **A manual that says "generic" or "extract" at the top means exactly that — check what it defers to
  before treating its silence on a topic as an answer.** The TPA CAD manual named three sibling
  manuals it doesn't include (`Workings.pdf`, `DxfCAD.pdf`, `DxfToTPA.pdf`) and said the copy given
  wasn't complete. Its silence on "Outfit Parameters"/"CN Tools"/"Solve" wasn't evidence those don't
  exist — it was evidence to go find the un-supplied files (Task T015).
- **A live shop-floor fault is worth documenting even mid-resolution.** The TpaCAD tool-ambiguity
  incident was written up with "workaround in place, permanent fix identified but not tried", then
  refined a second session, without ever being marked resolved prematurely (Task T016).
- **Two data points that should agree but don't are a live contradiction to record, not to silently
  resolve.** The SmartCabinet Wall Support session found two "measured from the back edge" hole
  positions needing opposite X signs; both were documented as actually used, with the disagreement
  itself flagged as the open question rather than guessing which is wrong (Task T017).
- **A fact recorded without a source hardens into an assumption nobody revisits.** The "two computers,
  not networked" claim sat in §1 through six versions, was repeated into the Vitap/TpaCAD/SmartCabinet
  articles, and shaped real advice (a whole barcode-system design was built around an air gap that does
  not exist) before the owner corrected it on 2026-09-17. It carried no citation and no `[confirm]`
  marker, so nothing ever flagged it as inferred. **Infrastructure and environment facts get a source or
  a marker, exactly like a figure off an invoice.** *Confirmed twice over on the same day:* the workshop's
  address had said **Unit 32** since Session 1 and was also wrong (it is Unit 31), and a billing address was
  described as "residential" purely from its format when it is in fact the companies' registered office.
  Three unsourced statements, three corrections, one day. **If it was not read off a document, say so.**
  *A fourth surfaced the same evening — §1's claim that the git mirror "is kept in step" (v12) — and a
  fifth right after it: the compressor's 5.4 bar "low pressure", which was residual receiver pressure
  on a machine that was switched off (v13).* **A reading is only a reading of the state the thing was
  actually in.** A photograph shows a number; it does not show whether the machine was running, warm,
  loaded or mid-cycle. Establish the state, or record the number as uninterpreted.
- **A fact filed under the wrong name is worse than a missing one, because the KB stops looking for
  it.** `FA2303`'s serial number sat in the Machinery Register from Session 6 as *"Job No.
  23-11-12-005 (Altendorf internal; no confirmed serial number)"*. On 2026-09-18 two 10 MB schematic
  PDFs were put through extraction specifically to find that serial; both reported none present and
  recommended photographing a title block. **A photograph of the machine's own plate showed
  `23-11-12-005` sitting in the `S/N` field.** The KB had transcribed the right value and then told
  every future reader it was something else, so five sessions of work routed around it. **A missing
  fact advertises itself; a mislabelled one does not.** When a field is filled with a hedge —
  *"internal"*, *"working value"*, *"no confirmed…"* — that hedge is a claim in its own right and needs
  checking like any other.
- **Check what a multi-part scan actually contains before trusting any one part.** The TPA CAD manual's
  *"part 1"* and *"part 2"* are not two volumes: part 1 holds the **even** pages and part 2 the **odd**
  pages in reverse order — two sides of one duplex scan, with pages 1, 2 and 50 in neither. **Part 1
  alone gives materially wrong answers**, because the milling-setup compensation fields exist only in
  part 2. Extracting both parts independently is what exposed this; a single read would have produced a
  confident, incomplete answer. Same shape as the Vitap manual's two duplex pairs, and worth checking
  page numbering on any scanned set before quoting it.
- **Comparing siblings finds what reading one cannot.** The `AMFA Wall Unit 600 RH` cutting list read
  cleanly on its own — every number internally consistent, nothing to query. Decoding the `300mm` and
  `600mm Wall unit` lists and putting all three side by side did two things at once: it **corroborated**
  the derived 600 × 900 × 300 nominal, because the same width rules held across all three, and it
  **exposed** a shelf depth of 266 / 256 / 255 mm on three carcases that are all 300 deep. Neither was
  visible from one file. *A single artefact can only be checked for internal consistency; a family can
  be checked against itself.* Where several things are meant to be the same, read more than one before
  calling any of them the master — and when they disagree, record every value, because preferring the
  one labelled "master" is a guess wearing a title.
- **A printed delivery clause is not a delivery note.** Proforma 208027 carried the line *"DELIVERY AS
  PER INV ADDRESS"* against a Unit 31 address, and §7 recorded the compressor as delivered to Unit 31 —
  then built a premises conclusion on it (*"the group was using both units in November 2023"*). The owner
  corrected it within hours: **it went to Unit 32.** Unit 31 was the billing address. A supplier's
  boilerplate describes an intention at the moment of quoting, not an event; only a delivery note, a
  signature or somebody's memory records where a thing actually arrived. **The same family as the 5.4 bar
  gauge** — treating a mark on a page as a record of the physical world. Where a document gives an address,
  record *which* address it is (billing, correspondence, delivery), and if it does not say, say that.
- **A correction has to be swept through every store the claim reached.** The "not networked" claim was
  corrected on 2026-09-17, and the sweep covered this file and the Wiki articles. It did not cover
  Smartsheet, and on 2026-09-18 Task **T016** was still instructing a future reader to carry a file across
  by hand *"(the two are not networked - confirmed)"* — a retracted claim, still giving directions, with
  the word *confirmed* attached to it. **The narrative layer and the live-data layer are different
  places.** A correction is not finished when the article reads right; it is finished when every sheet
  note, task and register row that repeated it reads right too. Corrected in place and visibly, not
  quietly overwritten.
- **A register only contains what somebody thought to put in it.** Five sessions were spent
  documenting three machines in detail — manuals, fault tables, maintenance schedules, re-commissioning
  requirements — while the compressor that feeds all three sat unregistered and unmentioned. It surfaced
  only because the owner photographed an asset label on it. **The gap was invisible from inside the
  KB**: nothing in the register pointed at a machine the register did not contain. Completeness is not
  something a knowledge base can check about itself; it needs a walk round the floor. The same walk
  turned up the first dealer sticker (R&J Machinery) in the whole KB, after three machines had been
  documented with no seller identified at all.
- **A model name is not a specification.** `STK 10000` was read as "probably 10,000 m³/h" and the
  reading was labelled, in the task itself, as *not* sourced — *"that is a reading of the model name,
  NOT a specification — do not rely on it."* It held for days until the vendor's quotation arrived and
  confirmed it. The label cost nothing and would have prevented a wrong number hardening into a fact if
  the guess had been wrong. **Label the inference, not just the conclusion.**
- **What a document excludes can matter more than what it states.** The AES quotation's specification
  table was useful; the two clauses saying the vendor supplies no cabling, no hose and no on-site
  electrical connection were more useful, because they moved the whole installation — ductwork,
  electrics, commissioning — into the group's own undocumented column. **Read the exclusions, the
  payment terms and the delivery conditions, not only the spec table.**
- **Trust the API's response, not its status code.** A 4,000-character Smartsheet cell value was
  **silently truncated mid-sentence** and still returned success. It was caught only by reading the
  stored value back out of the response. Long note fields go in compact, and get read back.
- **Verify like with like.** A Drive file's reported `fileSize` is **bytes**; Python's `len()` is
  **characters**. Comparing one against the other on a file full of `—`, `≥`, `³` and `Ø` showed a
  329-"byte" gap that did not exist, and cost a full withdraw-re-read-re-upload cycle plus a wrong
  "do not cite" label on an archived file that had nothing wrong with it. **Use `wc -c` both sides.**
  **And a size match is necessary, not sufficient — it proves nothing about order.** On 2026-09-19
  `kb-registers.md` went up with two Outputs rows transposed; `wc -c` matched exactly, at 56,265 both
  sides, and the upload was reported as verified. It was verified, and it was wrong. **A permutation
  does not change a byte count**, so reordering — and a swap of two equal-length values — passes
  silently. Every table in this KB is append-only and order-carrying, so **where order means something,
  check the order too**: before uploading, note which rows should sit first and last in each table; after
  uploading, read those positions back, not just the size. Cheap form: hash the lines at known positions,
  or count rows per table and compare the sequence of a few distinctive row keys. The general shape is
  §3's other standing warning — *trust the API's response, not its status code* — one level up: **here the
  number in the response was true and the inference drawn from it was false.** A check that has never
  failed is not a check that cannot fail; know what yours is blind to.
  *`ARCHIVED-2026-09-19c-kb-registers.md` is labelled **DO NOT CITE** for this reason: correct content,
  wrong order. A mislabelled file advertises nothing, which is the same trap as the wrongly-named serial.*
  **Two limits on the check itself, both found by running it.** *(a)* **It has a size ceiling.** The
  connector's read returns an **empty** `fileContent` above some size rather than an error:
  `kb-registers.md` read back fine at **58,410 bytes**, `CLAUDE.md` came back empty at **82,310** —
  *two points, so a bracket between roughly 58 KB and 82 KB, not a measured threshold.* **So the order
  check cannot be run on this file**, the largest in the KB. What stands in for it above the ceiling:
  **build the upload from one contiguous source** rather than by moving blocks about, so the
  pick-up-and-put-down failure has no opportunity to occur, **and say plainly that order was not
  verified** — *that is an argument about how the file was produced, not a verification of it, and must
  never be reported as one.* Below the ceiling, run the real check.
  **The ceiling was lifted 2026-09-19**: it belongs to `read_file_content`, and
  `download_file_content` returned this file whole at **90,475 bytes**. **The order check now runs at any
  size, on exact bytes** — download, decode, `diff` against the local copy. Building the upload from one
  contiguous source stays good practice; it is no longer a *substitute* for a check, because the check
  is available. *(b)* **Anchors must be plain
  text.** The read tool escapes backticks and asterisks, so an anchor containing them is not found and
  the check reports a failure that is not there. This KB produced exactly that false alarm on its first
  run and nearly believed it. Pick anchors from ordinary prose — one per table, first row and last —
  and compare the sequence of their positions plus the row count per table.
- **The connector's read tool does not round-trip, so never "copy" a file with it.** It returns a
  re-formatted rendering — leading punctuation escaped, two-space hard breaks appended — not the bytes
  on disk. A 2 KB article reconstructed from it came back **4 bytes out, silently**. This is why the
  git mirror is deliberately partial (§1) rather than back-filled, and why a large article is never
  rewritten just to change one metadata field: **every rewrite through a lossy read risks drift in the
  99% you did not mean to touch.** Write new content to both stores from the same local copy and check
  `wc -c`; do not treat Drive as a source you can read back and re-emit.
  **Corrected 2026-09-19: that is true of `read_file_content` and false of `download_file_content`**,
  which hands back the stored bytes base64-encoded and round-trips exactly — verified on a 9,602-byte
  article (byte-identical bar one real content difference) and on `CLAUDE.md` at 90,475 bytes. *The
  lesson that survives is the narrower one:* **the connector has two read paths and they are not
  interchangeable.** Never copy a file with the natural-language one; use the byte one, and diff.
  *The mirror was back-filled through the byte one on 2026-09-19 and every file matched (§1).*
- **Put a fact where its own update cycle lives.** This file carried a count of Wiki articles through
  four versions and was wrong in all four — *"four"*, *"fifteen"*, *"seven"*, *"nine / twenty-seven"* —
  not through carelessness but because **the figure changes every time an article is written and this
  document is revised weekly at best.** v17 responded by making recounting a standing rule, and went
  stale the same day it was written. **A rule that must be obeyed on every edit of a slow-moving
  document will be missed, and the miss is silent**, because a wrong number reads exactly like a right
  one. The fix is not more discipline, it is moving the fact: the count now lives in
  `Outputs/kb-registers.md`, which is touched every session, alongside the command that produces it.
  **Ask of any figure written into a durable document: what invalidates this, and how often? If the
  answer is "more often than this document is edited", it belongs somewhere else with a pointer left
  behind.** The same test flags the Drive file ids, the Smartsheet sheet ids and the machine
  specifications here — all of which change rarely or never, which is why they stay.
- **Re-read the primary record before reframing what a task is.** On 2026-09-19 T016 was recast from
  a generic TpaCAD fault into *"the Cabineo X tooling half-defined in SmartCABINET"*, and the charter,
  the task note and `Wiki/index.md` all took it up. **The article that records the incident says, in
  terms, that the two findings are unrelated** — and it had been written at the machine with the
  dialog open, which makes it better evidence than anything written about it since. **I did not
  re-read it before reframing.** The cost would have been a wasted trip to the wrong computer and a
  fix that appeared to fail. This is §3's *a fact recorded without a source* turned inside out: **the
  source existed and was not consulted.** *The risk scales with the KB's size* — this charter now
  summarises articles it no longer quotes, and a summary of a summary drifts. Before rewriting what a
  task **is** (as opposed to adding to it), open the primary record. Reframing is not a small edit; it
  redirects everyone who reads it next.
- **Check whether the tool you are blaming is the tool you used.** For nine versions this KB recorded
  that *"the connector's read tool cannot return a file byte-for-byte"* and built two standing debts on
  it — a mirror that could not be back-filled, and an order check with a size ceiling. **The connector
  has a second read tool that does exactly what was wanted, and it had never been called.** The claim was
  true of `read_file_content` and was written down as true of *the connector*: a quiet widening of scope
  that nothing later re-examined, because a debt that is written down reads as settled. **A limitation is
  a property of the call you made, not of the system**, until you have looked at what else the system
  offers — *list the tools before concluding the capability is missing.* **And the cheap half of the same
  lesson:** two byte discrepancies that day — **−8** on a new article and **+306** on this file — were
  both recorded as unexplained, one after being deliberately bounded at three attempts. **Neither was a
  defect; each was one `diff` away.** A discrepancy you cannot explain is usually a diff you have not
  run — and *suspicion* is not grounds for a **DO NOT CITE** label: that went onto v21 of this file and
  came off within the hour, making mislabelling the third entry of its kind in §3.
  **The price is now measurable**: the mirror debt stood for eleven versions and the back-fill it
  blocked took one afternoon (§1, §7, v23).
- **A description of a gap is not a measurement of it.** §7 recorded the one-way `related:` front
  matter as *"the three machinery articles"* plus one empty list — four files. On 2026-09-19 the graph
  was **computed** rather than read off the bullet: **fifteen files, 52 missing back-links.** The
  bullet was not careless. It named the articles somebody had **noticed**, because the two 2024 assets
  had been written last and linked out to the three older machinery articles, so those three stood out
  *from the side that had the links*. **The other eleven were invisible from inside the KB** — nothing
  in a one-way link announces itself from the end that is missing, which is the unregistered
  compressor's shape exactly: *a register only contains what somebody thought to put in it.* **Where a
  gap can be computed, compute it before trusting the count somebody wrote down** — including a count
  in this file. The danger is not the wrong number, it is that **a written-down description of a defect
  reads as a specification of it**, so the fix gets scoped to the description and closes tidily against
  the wrong four. Cheap form: a dozen lines that walk the files and build the set, run *before* the fix
  is planned, so the plan is sized against the measurement. And the description had stood unexamined
  since 2026-09-17 — **an inaccurate account of a gap is more durable than the gap**, because closing
  the gap feels like closing the account of it. Owner's decision to add this, 2026-09-19 (*"Add that §3
  lesson at v25"*), after v24 proposed rather than added it — the same route the v18 count fix and the
  v19 order clause took.
- **An absence is only an absence as of a timestamp.** v26 of this file stated that **no Tasks &
  Requests row was assigned to Darius**. The check was real — the Hub was read between **21:01 and
  21:25** on 2026-09-20 against `AWT-0036`, `AWT-0040` and `HL-0023` — and v26 was committed at
  **21:25:14**. **`AWT-0045` was created at 21:29:36**, four minutes later. So the sentence was **true
  when written and false before anybody could read it**, and it was sitting in a charter revised weekly.
  **The mistake is not the checking, it is the tense**: a point-in-time observation was written down as
  a standing fact. *And the first correction was wrong too* — it blamed Smartsheet's eventually
  consistent search, when the timestamps show there was nothing yet to find; that claim was superseded
  visibly on the row rather than quietly replaced. **This is *put a fact where its own update cycle
  lives* arriving from the other side**: that lesson asks what invalidates a figure and how often, and
  the answer for "nothing is assigned to me" is *at any moment, by somebody else, without telling you*.
  **A negative finding is a measurement, so date it or do not write it down** — *"as of 21:25 on
  2026-09-20, no row was assigned"* is durable and true forever; *"no row is assigned"* has a shelf life
  of minutes. The same test catches *"no manual exists"*, *"nothing is in `Raw/`"* and *"the sheet is
  empty"* — all of which this KB has written. Owner's decision to add it, 2026-09-21 (*"add that §3
  lesson"*), after v27 proposed rather than added it: **the fourth lesson to take that route**, after
  v18's count fix, v19's order clause and v25's measurement clause.
- **Don't run two sessions on this KB at once, and re-read the live index/registers before recreating
  a control file.** The 2026-09-15/16 fork (this file, `index.md`, `kb-registers.md` all split across
  two parallel lines) is the reason Darius now owns the KB as a single seat.
