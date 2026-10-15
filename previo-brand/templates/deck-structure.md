# Previo deck structure (.pptx)

Use together with a pptx skill or library if one is available. Colors and fonts are in `tokens.md`,
the red rule in `SKILL.md` ("Use of red"). Format 16:9.

## Slide types

| Slide | Background | Content |
|---|---|---|
| **Cover** | full red `#b50000` | Logo `logo/previo-logo-white.svg` top left, title (Inter Medium, white, large), subtitle, name and date. The red area is the hero; the only full red slide in the deck apart from the closing. |
| **Section** | white, or `#202124` | Large section number and title. Nothing else. |
| **Content – text + number** | white | Section label (12 pt, uppercase) at the top, **gray** `#515151` because the red number is the hero; headline as a claim (Inter Medium); text on the left, one dominant number in red on the right. |
| **Content – process** | white | Red section label, headline, 3–5 steps on a timeline (gray lines, step numbers gray). Only for sequential content. |
| **Content – chart/table** | white | Section label, headline as a claim, one visualization: the highlighted item red, the rest gray. The label is gray when the highlighted item is the slide's hero, otherwise red. |
| **Quote / reference** | `#f2f2f2` | Quote, name, hotel. Red section label allowed, no other red. |
| **Closing** | red or `#202124` | Contact, white logo variant. |

## Rules

- **One red hero per slide**: a full red area or the one red number. Small red signals (section
  label, CTA) only when they do not compete with it; see the table above.
- Every content slide has a **headline as a claim** ("Alfred cut check-in to 90 s"), not a topic
  ("Check-in").
- **One idea per slide**, max. 3 bullets, text at least 18 pt.
- Font: headings `Inter Medium`, text `Inter` (installed from the skill's `fonts/`). If they cannot be
  installed, tell the user.
- Page number and a small footer (Gray 500, 10 pt) on every slide except the cover.
- Do not repeat the same layout 3× in a row; alternate slide types.
- No three identical KPI cards, no status pills, no icons from a random set.

## RGB for python-pptx

Primary `181,0,0` · Ink `32,33,36` · Muted `81,81,81` · Border `229,229,229` · Surface `242,242,242` · White `255,255,255`
