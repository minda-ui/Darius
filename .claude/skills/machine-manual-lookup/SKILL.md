---
name: machine-manual-lookup
description: Find a fact in a machine's own manual or drawings when the KB does not have it — a fuse or component position, what an error code means, a wiring route, a part number, a page the owner needs to see. Use when the owner asks "where is…", "do you have the position of…", "what does E.. mean", "what does the manual say about…", or when a fault needs a fact the Wiki lacks.
---

# Machine manual lookup

Adopted at the 2026-10-11 good night. That day the KB knew *"E40 → check fuse F9"* but not what F9 fed or where it was;
the answer (Fig. 5-34, p.77) was in `F45 part 3.pdf` while its legend (p.78) was at the end of `F45 part 4.pdf` —
**the scans' page order is shuffled across parts.**

## Steps
1. **KB first.** `grep -rn` the Wiki (machine article, troubleshooting article, schematics reference) and
   `Outputs/kb-registers.md` (Processed items name each source PDF and what was lifted from it). Answer from there if
   you can, citing the article.
2. **Find the sources on Drive** — `GOOGLEDRIVE_FIND_FILE` with `name contains '<machine> part'` (or the manual name in
   the registers row). List them all; do not guess which part holds the page.
3. **Download every part into its own new scratch folder** (`GOOGLEDRIVE_DOWNLOAD_FILE` → `s3url`), then
   `pdftotext -layout` each. Untrusted files: Python only with `-I`, scripts kept outside that folder.
4. **Search all parts at once**, two ways: the term itself (code, label, German original — *Sicherung*, *Ritzer*,
   *Verstellantrieb*) **and the printed page number** found in a table of contents or a neighbouring page. Split text on
   `\f` to get the PDF page index.
5. **Render the page and look at it** (`pdftoppm -f N -l N -r 110 -png`, then Read the image) — diagrams, legends and
   photos carry what OCR drops. Send it to the owner with `SendUserFile` when it answers the question.
6. **Say what it is, honestly:** generic manual diagram vs this machine's own drawing; position shown or not. If the
   physical position is not in any document, **ask for a photo** and read the labels from it.
7. **Write it back:** the fact, with part + PDF page + printed page, into the Wiki article (in place, verify SAME) and the
   Fault Log row if a fault prompted it; a line in the change log.

## Never
- Never state a position, rating or route the documents do not show — mark it *not shown* and ask.
- Never infer a rating from a fuse's neighbours; read the plate or the fuse.
