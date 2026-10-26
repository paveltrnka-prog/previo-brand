# Previo deck structure (.pptx)

**For a `.pptx`, use the generator `scripts/build_deck.py`** (see **Generator** below): you write the
content as JSON, the script places it on the fixed grid. Build slides by hand only for a slide type the
generator does not have, and then follow the measurements in **Grid**.
Use together with a pptx skill or library if one is available. Colors and fonts are in `tokens.md`,
the red rule in `SKILL.md` ("Use of red"). Format 16:9.

**Visual reference: `templates/deck.html`.** It shows every slide type below at 1280 × 720 px with
the right proportions, icons and red rhythm. For a `.pptx`, rebuild the same slide types (1 px in the
template = 7 144 EMU on a 10 in × 5.625 in slide). For a deck that is only sent and read, you may
fill `deck.html` directly and print it to PDF: fonts, logo and icons travel inside.

## Generator: `scripts/build_deck.py`

```
pip install python-pptx            # once, if missing
python3 scripts/build_deck.py outline.json deck.pptx --preview deck.html
```

Write the outline as JSON (complete example: `scripts/deck-example.json`), run the script, then open
the `--preview` HTML (same layout, renders in any browser; screenshot it when PowerPoint is not
available) and go through **Check before you hand it over**. The script draws every slide on the grid,
embeds icons and logo, crops photos, sets Inter and keeps the red rule (a `number` slide gets a gray
label and gray tiles). It measures every text with the Inter metrics and **refuses to build** when
something would overflow, collide or break the rhythm; the message says which slide and what to
shorten or split. Fix the content, never the positions. Warnings (e.g. three slides of one type in a
row) build the deck but should be fixed too.

Top level: `"lang"` (`"cs-CZ"`, `"en-GB"`, …; Czech/Slovak get non-breaking spaces after one-letter
words), `"footer"` (deck title on every white slide), `"slides"`. Every slide can have `"notes"`
(speaker notes). Icons are names from `icons/` without `.svg`.

| `type` | Fields (* required) | Limits |
|---|---|---|
| `cover` | `title`*, `label`, `subtitle`, `author`, `date`*, `photo` (path; right part, cropped) | title ≤ 3 lines |
| `list` | `label`, `title`*, `intro` (left column), `items`*: `[{icon, title, text}]`, `note` | 1–4 items |
| `columns` | `label`, `title`*, `columns`*: two × `{prefix, title, items}`, `note` | 1–3 items per column, rows aligned |
| `process` | `label`, `title`*, `steps`*: `[{icon, title, text, repeat, note}]` | 3–5 steps; `repeat: true` = dark tile |
| `statement` | `number`, `title`*, `text` | red; one per 8 slides |
| `number` | `label`, `title`*, `value`* (e.g. `"15 %"`), `caption`, `source`, `facts`: `[{icon, title, text}]` | value one line, ≤ 3 facts |
| `photo` | `label`, `title`*, `text`, `photo`* | photo on the right half, cropped |
| `closing` | `title`*, `text`, `name`, `email`, `phone` | contact on one row |

`note` is a gray box under the content for a remark that must not get lost (e.g. what is not
included). Headlines on white slides have room for two lines (≈ 22 characters per line at Inter
Medium): a headline that does not fit is a sign it is a sentence, not a claim.

## Rhythm: a deck is not all gray

A Previo deck opens and closes in red. Between them, white content slides alternate their type, and
one red statement slide may break up a longer deck.

```
red cover → content → content → [red statement] → content → content → red closing
```

- **Cover and closing are full red `#b50000` with white text** and the white logo. This is the
  default; a dark `#202124` closing is the exception (e.g. when a full-bleed photo is behind it).
- **Statement / section slide (full red):** one per deck of 8+ slides, or one per part of a long
  deck. A section number or one strong claim, nothing else. Never two red slides in a row.
- **Content slides are white.** Gray `#f2f2f2` is for one block that should recede, not the
  default for every card. Default card = white with a 1 px `#e5e5e5` border.
- Do not repeat the same layout 3× in a row; alternate the slide types below.

## Slide types

| Slide | Background | Content |
|---|---|---|
| **Cover** | full red | White logo top left; label (uppercase, white 80 %), title (Inter Medium 54+ pt, white), subtitle, **name and date** at the bottom. Optional photo of the client/hotel on the right part, edge to edge (see Photos). |
| **Content – intro + list** | white | Red section label, headline as a claim, short intro on the left (≈⅓), max. 3–4 items on the right, each with an **icon tile**. |
| **Content – two columns** | white | Red section label, headline, two groups side by side with sub-headings (A/B, 01/02, gray prefix), max. 3 items with icon tiles each; rows of both columns aligned. Optional gray **note** under them for a remark that must not get lost (e.g. what is not included). |
| **Content – process** | white | Red section label, headline, 3–5 steps on a timeline: icon tile per step on a gray line, small gray step numbers. A repeating step gets a dark tile. Only for sequential content. |
| **Statement / section** | full red | Big section number (white, 35 % opacity) or one strong claim, white. Nothing else. |
| **Content – text + number** | white | Section label **gray** `#515151` (the red number is the hero); headline as a claim; one dominant number in red; facts beside it with **gray** icon tiles. |
| **Content – chart/table** | white | Section label, headline as a claim, one visualization: the highlighted item red, the rest gray. Label gray when the highlighted item is the slide's hero, otherwise red. |
| **Content – photo** | white or photo | Photo of the property covering half the slide or the whole slide (cropped), short claim beside or over it. Good for breaking up text-heavy decks. |
| **Quote / reference** | `#f2f2f2` | Quote, name, hotel. Red section label allowed, no other red. |
| **Closing** | full red | White logo, closing line or next step (large, white), contact with white mail/phone icons. |

## Icons

Use only the bundled set in `icons/` (line icons, 24 px grid, 1.75 stroke). For `.pptx` insert the
PNGs from `icons/png/<name>-<red|ink|white>.png`; in HTML paste the SVG inline (it uses
`currentColor`).

- **Icon tile** = rounded square (radius ≈ ¼ of its size) with the icon centred at half its size:
  - slide without a red number: tile `#faeaeb`, icon **red** (`-red.png`);
  - slide with a red number hero: tile `#f2f2f2`, icon **ink** (`-ink.png`);
  - red slide: icon **white**, no tile.
- An icon marks **what kind of item** it is (web, campaign, price, report). One icon per list
  item, same size within a slide. No icons as decoration, no icons from another set, no emoji.
- Sizes: tile **0.5 in (64 px)** with a **0.25 in (32 px)** icon in lists and timelines; 0.44 in
  (56 px) tile with a 0.22 in icon in a compact facts box. Never smaller: a tile below 0.44 in reads
  as a dot, not an icon. The icon is always half the tile, centred.

## Grid: every content slide starts in the same place

Paging through the deck, the label, headline and content must not jump. Use these fixed positions
on **every** white content slide (px in `deck.html` → inches on a 10 × 5.625 in slide, 128 px = 1 in):

| Element | Position |
|---|---|
| Side margins | 80 px = 0.625 in left and right |
| Section label | top 64 px = 0.5 in |
| Headline box | top 100 px = 0.78 in, height **always two lines** (120 px = 0.94 in), even for a one-line headline; text anchored to the top |
| Content block | top **268 px = 2.09 in**, anchored to the top, never vertically centred |
| Footer | line at 656 px = 5.125 in |
| Intro + list | intro column 400 px = 3.125 in wide; list starts at x 560 px = 4.375 in |

- In python-pptx set the headline text frame to `vertical_anchor = TOP` and `auto_size = NONE`, the
  same size on every slide; never let PowerPoint shrink or grow it.
- List items: fixed gap (24 px = 0.19 in) between items, title aligned to the top of the icon tile.
  Two columns on one slide share the same top and the same row positions.
- Same element = same position across slides: if slide 4 has a list at x 4.375 in, slide 7 does not
  put it at 4.1 in. Reuse the measurements, do not eyeball them.

## Photos

Photos of the client's property make a deck specific to them; use them when you have them.

- **Never stretch a photo.** Keep its aspect ratio and crop to fill the frame (`object-fit: cover`).
  In python-pptx: compare the image ratio with the frame ratio and set `picture.crop_left/right`
  (image wider than frame) or `crop_top/bottom` (image taller), half on each side, so the visible
  part has the frame's ratio. A 4:3 photo in a tall frame must be cropped, not squeezed.
- Photos go edge to edge (bleed) or into a frame with radius 16 px / 12 pt; no borders, no shadows.
- Never put text directly over a busy photo; put it on the red/white part next to it.

## Text size: projected vs. read

Pick by how the deck will be used and say which one you assumed:

| | Projected (talk) | Read (sent as offer / PDF) |
|---|---|---|
| Headline | 32–40 pt | 26–32 pt |
| Body text | min. 18 pt | min. 12 pt, ideally 14 pt |
| Items per slide | max. 3 | max. 5 |

If the content does not fit at these sizes, split the slide; never shrink below the minimum.
`deck.html` is set to the read sizes (1 px = 0.5625 pt: body 22 px ≈ 12.4 pt, headline 52 px ≈ 29 pt);
only section labels and the footer go down to 10 pt.

## Rules

- **One red hero per slide**: a full red area or the one red number. Small red signals (section
  label, icon tiles, CTA) only on slides without a red number.
- Every content slide has a **headline as a claim** ("Alfred cut check-in to 90 s"), not a topic
  ("Check-in"). **One idea per slide.**
- Use **one name** for the product/service throughout the deck (e.g. not "M+", "Program M+" and
  "Marketing+" mixed); introduce an abbreviation once on the cover or slide 2.
- Font: headings `Inter Medium`, text `Inter` (installed from the skill's `fonts/`). If they cannot be
  installed, tell the user. The .pptx does not carry the font: offer a PDF export for sharing.
- Page number and a small footer (Gray 500, 10 pt, color logo) on every white slide; not on red slides.
- No three identical KPI cards, no status pills or tag clouds of pills, no grid of identical gray cards.

## Check before you hand it over

Run `python3 scripts/check_deck.py deck.pptx --render out/`. It checks the grid without rendering
(label, headline and content position on every slide, tile sizes, fonts, edges) and then renders the
deck with LibreOffice into `out/slide-N.png` and `out/contact-sheet.png`, with Inter loaded so line
breaks match PowerPoint. Fix every ERROR, then look at **every** rendered slide:

1. Photos keep their proportions (no squeezed people, furniture or buildings).
2. No text overflows its box or overlaps another element; nothing touches the slide edge.
3. Red: exactly one hero per slide; a slide with a red number has a gray label and gray icon tiles.
4. Cover is red with name and date; closing is red with contact; at most one red statement slide in
   between and never two red slides in a row.
5. Text sizes match the projected/read table; no list longer than the limit.
6. Content is consistent: same product name everywhere, no slide promising what another excludes
   (e.g. "Meta Ads in phase 1" vs. "Meta campaigns are not included").
7. Fonts are Inter / Inter Medium on every run (no Calibri/Arial left from defaults).
8. Grid: page through the slides quickly; label, headline and content start at the same place on
   every content slide (see **Grid**). Nothing jumps.
9. Icons: tiles at least 0.5 in (0.44 in in a facts box), icon half the tile, same size on a slide.

## RGB for python-pptx

Primary `181,0,0` · Primary soft `250,234,235` · Ink `32,33,36` · Muted `81,81,81` · Gray 400 `178,178,178` · Border `229,229,229` · Surface `242,242,242` · White `255,255,255`
