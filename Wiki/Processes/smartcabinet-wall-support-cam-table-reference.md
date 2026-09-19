---
title: "Process: SmartCabinet Wall Support Cam Table — column reference and worked example"
category: Processes
status: active
sensitive: false
created: 2026-09-16
updated: 2026-09-16
sources: []
related:
  - ../Processes/tpacad-tool-type-optimizer-ambiguity.md
---

# Process: SmartCabinet Wall Support Cam Table — column reference and worked example

Documents how to add a new hardware item to SmartCabinet's **Wall Support** hardware library (Cam
Table, internally labelled "Supporto Pensili" — Italian for "wall unit support"), reached from
SmartCabinet's hardware/fittings screen. Worked out live on 2026-09-16 while adding two new
hardware models: a Häfele "Concealed Cabinet Hanger, Dowel/Screw Mounting," and a separate
adjustable wall-bracket system with both side-panel and backrest holes. The second item's real,
software-confirmed values exposed a sign-convention discrepancy with the first — see the worked
examples and the flagged discrepancy note below before using either as a template for a third item.

## Where it lives

SmartCabinet → hardware library screen → **Wall Support** tab → **Cam Table: Wall Support**. Left
side lists existing hanger models (e.g. "Libra H2," "CAMAR 807 REGGIBASE Dietro," "CLASSIC WALL
RACKS"); right side is a parameter grid, one row per hole/recess for whichever model is selected.
**+** adds a new model row set, the trash icon deletes, a `.obj` icon opens a 3D-model file picker
for visualisation. The screen has its own built-in help text (accessible from within the software)
that gives the authoritative column definitions below — quoted directly from it, not inferred.

## Column reference (from the software's own help text)

| Column | Meaning |
|---|---|
| **B/S** | Which panel this row's parameters describe: **B** = backrest (back panel), **S** = sidewall (side panel). Every other column's meaning shifts depending on this setting. |
| **X** | Horizontal position of the hole relative to an edge. **If B/S = S** (side): positive moves the hole toward the **back**, negative toward the **front**. **If B/S = B** (backrest): positive moves it **in**, negative **out**. For a Side row, X's position is also affected by a separate CAM setting, `WallSupportDrillFromInternalBackpanel`: 0 = distance calculated from the backrest's outer edge, 1 = from its inner edge. |
| **Y** | Vertical position of the hole relative to the **top edge** of the panel. |
| **Ø** | Hole diameter. |
| **φ** | Hole **depth** — not diameter, not an angle, despite the symbol. Easy to misread; confirmed against the software's own help text before using it. |
| **Min H** | Minimum cabinet height this bracket/model can be mounted on. |
| **Max H** | Maximum cabinet height this bracket/model can be mounted on. |
| **D** | Forward displacement of the interlocking backrest and all side holes; this value overrides whatever the interlocking-backrest's own parameters say. Maximum permissible value 19mm (0.748"). Only relevant for cabinets built with an interlocking-backrest construction method. |
| **L** | Horizontal dimension of a recess cut into the upper corner of the backrest or side (whichever B/S is set to) — only needed if the hardware requires a notch. |
| **H** | Vertical dimension of that same corner recess. |

**One row per hole.** If a bracket has multiple holes at different heights, each needs its own row
(same B/S, X, Ø, φ if they're all identical in those respects — only Y differs).

## Worked example: Häfele Concealed Cabinet Hanger (Dowel/Screw Mounting)

A wall-mounted cabinet hanger with 4× Ø10mm holes on the cabinet's **side panel**, at 37mm from the
top edge then 32mm pitch for the remaining three (cumulative: 37, 69, 101, 133mm), 15mm in from the
**back** edge, 13mm hole depth. No cabinet height rating specified by the supplier for this
particular part. No interlocking-backrest displacement or corner recess needed.

Added as a new model (not editing an existing one) with 4 rows:

| Row | B/S | X | Y | Ø | φ | Min H | Max H | D | L | H |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | S | -15 | 37 | 10 | 13 | 0 | 0 | 0 | 0 | 0 |
| 2 | S | -15 | 69 | 10 | 13 | 0 | 0 | 0 | 0 | 0 |
| 3 | S | -15 | 101 | 10 | 13 | 0 | 0 | 0 | 0 | 0 |
| 4 | S | -15 | 133 | 10 | 13 | 0 | 0 | 0 | 0 | 0 |

**Why X = -15, not +15**: the 15mm was measured from the **back** edge of the side panel. Per the
column definition above, a Side row's X convention is "positive = toward the back, negative =
toward the front" — so a distance stated *from the back edge* is entered as the negative value.
This sign convention is the single easiest thing to get backwards in this table; worth double-
checking against the reference measurement's stated edge every time, not just assuming. **See the
second worked example below — its side-panel holes are also measured from the back edge, but ended
up needing the opposite sign. Read that discrepancy note before trusting this rule as stated.**

## Worked example 2: adjustable wall-bracket system with side + backrest holes

A different bracket system (not the Häfele hanger above) with two distinct hole groups on the same
job: 3 fixing holes on the cabinet's **side panel**, and 2 adjustment holes on the **backrest**.

**Side panel (3 holes):** Ø10mm, 13mm deep, 5mm from the edge nearest the backrest, first hole
71mm from the top edge, remaining two at 32mm pitch (71, 103, 135mm).

**Backrest (2 holes):** Ø12mm through-holes (entered as 20mm depth — deep enough to guarantee full
penetration through typical panel thickness, since a generic hardware entry has to work across
whatever thickness a given job uses), 18mm in from the edge nearest the side panel, first hole 75mm
from the top edge, second hole 50mm further down (125mm).

| Row | B/S | X | Y | Ø | φ | Min H | Max H | D | L | H |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | S | 5 | 71 | 10 | 13 | 0 | 0 | 0 | 0 | 0 |
| 2 | S | 5 | 103 | 10 | 13 | 0 | 0 | 0 | 0 | 0 |
| 3 | S | 5 | 135 | 10 | 13 | 0 | 0 | 0 | 0 | 0 |
| 4 | B | 18 | 75 | 12 | 20 | 0 | 0 | 0 | 0 | 0 |
| 5 | B | 18 | 125 | 12 | 20 | 0 | 0 | 0 | 0 | 0 |

**Discrepancy flagged, not resolved: side-panel X sign.** This job's side-panel holes are also
measured "from the back edge" (same wording as the Häfele hanger above), yet were confirmed to need
**X = +5** here, the opposite sign from the Häfele hanger's **X = -15**. Both can't be following the
same simple rule ("measured from back edge → always negative"). Left as-entered for each job since
each was the value actually confirmed/used, rather than forcing one to match the other's sign on the
assumption that only one is "right." Possible explanations, none confirmed: the two hardware items
might reference different internal defaults, the `WallSupportDrillFromInternalBackpanel` setting
mentioned in the column reference could be affecting one differently than the other, or one of the
two entries has a sign error that hasn't surfaced yet because it hasn't been used on a real job and
visually checked. **Do not treat either -15 or +5 "from the back edge" as a settled rule for a third
hardware item — re-derive the correct sign for each new item from how it previews/behaves in
SmartCabinet, not from this table.**

**Backrest X sign, for comparison**: 18mm "from the edge nearest the side panel," moving in toward
the backrest's centre, was entered as **+18** — positive, per "Backrest: positive = in." This one
wasn't flagged as inconsistent with anything else observed so far.

## Open questions

- **Side-panel X sign convention is unresolved — see the discrepancy note above.** Two hardware
  items, both described as "measured from the back edge," needed opposite signs (-15 vs +5). Not
  safe to generalise a rule from either one alone.
- Min H/Max H were left at 0 because the supplier's datasheet didn't state a rated cabinet height
  range for this specific part — not confirmed that 0 is the "no restriction" value in this
  software rather than "invalid/unset"; worth checking behaviour once this hardware is actually
  used on a job.
- Not confirmed whether `WallSupportDrillFromInternalBackpanel` (the separate CAM-section setting
  referenced in the X column's own definition) is set to 0 or 1 in this shop's SmartCabinet install
  — this could plausibly be *why* the two worked examples above disagree on sign, but that's a
  guess, not confirmed.
- The Häfele hanger's X = -15 has not yet been visually verified against a real preview in
  SmartCabinet (added first, before the sign discrepancy was noticed); the second item's X = +5 was
  the one actually confirmed. Worth re-checking the Häfele entry's hole placement next time it's
  used on a job.
