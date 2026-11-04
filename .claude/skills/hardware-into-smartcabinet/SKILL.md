---
name: hardware-into-smartcabinet
description: >
  Turn a hardware maker's data (drawer system, runners, hinges, lift) into what SmartCabinet needs — runner/hardware
  table rows, a drawer-box .SCS file, the drilling — plus a one-unit proving step. Use when the owner says "we need to
  add <hardware> to SmartCabinet", "input <system> data into SmartCabinet", or uploads a maker's drawing/catalogue page
  for hardware the shop has not drawn with before.
---

# Hardware into SmartCabinet

Method from METABOX (2026-10-02/03, proved on the 350 unit), LEGRABOX (10-03) and Klug Innobox (2026-11-04).
Model articles: `Wiki/Processes/blum-metabox-smartcabinet-input.md` (the proved one) and
`Wiki/Processes/klug-innobox-smartcabinet-input.md`.

1. **Import first.** Ask the owner to search SmartCabinet's *Utility → Import Accessori* for the brand/system — a
   Kosmosoft import beats any hand entry. Only if it is not there, enter it by hand.
2. **Read the maker's data.** Use `machine-manual-lookup` for catalogues. A **scanned** drawing has no text layer:
   render at 400 dpi (`pdftoppm -r 400 -x -y -W -H`) and read crops. Mark every figure read off a drawing *(drawing)*
   and every one that needs a sample **⚠ measure**. Identify the product (a rebrand: Klug Innobox = Taiming 908SH-A86).
3. **Map to SmartCabinet** as the METABOX article does:
   - *Guide Cassetto* row **per NL**: `LX`, `LY`, `CX`, `LBox`, hole groups = **cabinet-side** runner holes (X from
     the front edge, Y so that `LY + Y` clears the part below);
   - drawer box: copy a proved `.SCS` (e.g. `METABOX_K.scs`), set the side allowance so the base/back come out at the
     maker's formula, **load it through *Box Config file*** (typed values did not take effect on METABOX);
   - fronts and other drilling — all holes on the Vitap (owner's rule, unless the owner makes an exception).
4. **Write the Wiki article** `Wiki/Processes/<brand>-<system>-smartcabinet-input.md` (front matter, sources, the
   mapping table, expected cut sizes for a real job, open ⚠ list) and its `Wiki/index.md` entry.
5. **Prove it on one unit:** owner draws one cabinet with one item → export to the Review folder →
   `pre-production-drawing-check` against the article's expected sizes → dry-fit against the real hardware before a
   batch. Only then add the other lengths/sizes.
6. Log, commit, push; publish the article to Drive.
