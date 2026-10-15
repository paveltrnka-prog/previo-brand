---
name: previo-brand
description: >-
  Applies the official Previo brand (colors, Inter typography, logo and composition rules) to any
  visual output: decks (.pptx), PDFs, HTML reports and dashboards, one-pagers, posters, banners and
  social graphics. Use it whenever something should look like it comes from Previo, even if the user
  does not mention branding; plain-text .md files and internal notes stay unbranded. The skill ships
  the brand tokens, the Inter font, the logo, the Alfred AI mascot and ready-made templates, so every
  output starts from a proven Previo layout instead of a generic one.
---

# Previo Brand: styling visual outputs

Unifies the look of visual outputs according to the official Previo brand. The tokens come from the
Previo design system in Figma (**P – design system**, variables), not from a random deck. This skill
is the source of truth and overrides the default palette and fonts of any tool.

## Files in this skill

All paths below are relative to **this skill's folder**, wherever it is installed. Never write an
absolute path or a path from your own machine into an output.

| Path | What it is |
|---|---|
| `tokens.md` | All values: colors, type scale, radius, spacing, CSS variables, RGB for pptx |
| `fonts/Inter-Regular.ttf`, `fonts/Inter-Medium.ttf` | Inter 400 and 500 (SIL OFL 1.1) |
| `logo/previo-logo-{color,black,white}.svg` | Logo in three variants |
| `alfred/alfred.svg`, `alfred/ai-icon.svg` | Alfred mascot and the AI icon |
| `templates/*.html` | Self-contained HTML templates (font and logo already embedded) |
| `templates/deck-structure.md` | Slide types and rules for `.pptx` |

## How people use it

Users do not need to know colors or fonts. They say what they want, e.g. "Make a one-pager about
Alfred for hoteliers", "Prepare a client deck, 8 slides", "Turn these numbers into a Q3 report". You
pick the right template, apply the brand and fill in their content. Write the output in the language
the user writes in. Before the output goes outside the company, remind the user to check numbers and
names: the brand controls the look, not the truth of the content.

## Templates

Ready-made starting points live in `templates/`. The HTML templates are **self-contained**: Inter and
the logo are embedded in the file, so a copy works anywhere without the `fonts/` and `logo/` folders.

- `onepager.html`: one-page material, fixed A4, one big number with facts beside it.
- `report.html`: report/dashboard, A4, one main visualization + table + recommendation.
- `social-feed.html`: social feed 4:5, 1080 × 1350 px, one big number.
- `social-story.html`: story / reel cover 9:16, 1080 × 1920 px, full red area, safe zones 250/340 px.
- `social-linkedin.html`: LinkedIn / OG image, 1200 × 627 px, claim + number.
- `deck-structure.md`: slide types and rules for `.pptx`.

**Copy the closest template and replace the `{{placeholders}}`**; do not rebuild the layout. Big
numbers (e.g. `42 %`) are replaced directly, without braces. Change the template only where the
content requires it (e.g. delete the steps block when the content is not sequential). Keep the rules
from "Use of red" and "Layout and composition". Export social graphics to PNG at the size in their
description (viewport = graphic size); within one campaign alternate the types, not a single layout.

## When to use it

Use it for anything visual: **presentations (.pptx), PDF, HTML dashboards/reports, one-pagers,
posters, banners, social graphics, e-mail visuals**. Apply the brand automatically, even when the
user does not ask for it.

**Do not use it** for plain-text `.md` files; keep those neutral unless the user explicitly asks for
branding. For `.docx` see the next section.

## .docx boundary

`.docx` is not excluded by default. Decide by the purpose of the document:

- **Apply the brand** (Inter Medium headings, red section labels, optionally a header/footer with
  the logo): client report, one-pager, offer, anything that leaves the company or goes to a shared
  space (SharePoint, external e-mail).
- **Keep it neutral**: internal notes, working drafts, meeting notes, anything that stays among
  colleagues and is never presented externally.

If the purpose is unclear, ask once in one sentence ("Should this be branded, or is it an internal
draft?") before styling.

## Fonts (critical: the brand does not hold without them)

Inter is bundled in `fonts/`:
- `fonts/Inter-Regular.ttf`: weight 400, family name `Inter`.
- `fonts/Inter-Medium.ttf`: weight 500, separate family name `Inter Medium` (static instance, not
  variable, because PowerPoint/LibreOffice cannot use the `wght` axis).

License: SIL Open Font License 1.1, free to use and redistribute (see `fonts/LICENSE-Inter.md`).

**By output type:**

- **HTML / PDF (via HTML→PDF)**: start from a template, which already embeds the font. When you
  build HTML from scratch, embed both TTF files as base64 `data:` URIs in `@font-face` (read them
  from this skill's `fonts/` folder). Do not link `fonts/...` relatively from the output file: the
  output lives somewhere else and the link breaks. Never rely on Inter being installed; without
  `@font-face` the renderer silently falls back to `Segoe UI` / `system-ui` and the brand is off even
  when the colors are right.
- **.pptx / .docx**: the file does not carry the font, the system that renders or opens it must
  have Inter installed. If your environment lets you install fonts, install both TTF files from
  `fonts/` into the system font folder (refresh the font cache if the OS needs it) before rendering.
  Reference headings and labels as font `"Inter Medium"` and body text as `"Inter"`, not as one
  family with two weights, because PowerPoint/LibreOffice cannot switch weight reliably without
  a variable axis.
- **Sharing .pptx / .docx**: tell the user that colleagues without Inter will see a substitute
  font. Recommend sending a PDF, or installing the two fonts from the skill's `fonts/` folder once.
- **If the font fails or cannot be installed**: do not silently substitute Trebuchet, Calibri or
  Arial. Tell the user that Inter could not be applied and the fallback `Segoe UI / system-ui` was
  used, so they know the result is not 1:1 with the brand.

## Colors

Full tokens with values are in `tokens.md`. The core:

- **Primary red `#b50000`** is the one brand color. How much of it to use is defined in
  **Use of red** below. Darker variant `#910000` (hover/emphasis), soft background `#faeaeb`.
- **Text and surfaces**: white `#ffffff` as the base, dark text from the grays (`#202124` headings,
  `#515151` secondary). Gray scale `#fafafa → #202124` for surfaces, dividers and UI.
- **Semantic** (only when they carry meaning, never decoration): positive `#1b6422`, negative
  `#a30000`, warning `#ff6d0a`, info has no confirmed default yet (see `tokens.md`).
- **Do not put Negative (`#a30000`) and Primary Dark (`#910000`) next to each other.** They are too
  close and blend together without a difference in iconography (e.g. an error message next to a
  red CTA).

### Use of red

Each page, slide or graphic has **exactly one hero** and may have a few **small signals**.

- **Hero (one per page/slide):** either a full red area (cover, closing, story) **or** the largest
  number in red. Never both, never two red numbers.
- **Signals (small, allowed):** the section label (12 px / 12 pt, uppercase), the primary CTA or
  link, and in a chart the one highlighted item that the hero talks about. They guide the eye, they
  do not compete with the hero.
- **Not allowed:** red keywords inside body text, red headings, several red numbers, red icons or
  borders as decoration, red series in charts beyond the one highlighted item.
- **Decks:** a content slide with a red number keeps its section label gray (`#515151`); a slide
  without a red number gets a red section label.
- Everything else stands on the gray scale and on type size and weight.

### AI and Alfred (purple)

There are two purples with clearly separate jobs. They are the same values on screen and in print;
the brand does not define separate print (CMYK) values, so leave the conversion to the printer.

| Color | Where it belongs |
|---|---|
| **AI `#673AB7` → AI Dark `#4E2C8B`** (135° gradient on the AI button), light `#8B69C8`, background `#E7DFF3` | AI features inside the **Previo product** UI: AI buttons, AI labels, AI answers, ScanID, Plachta optimization. Use it in mockups, screenshots-like UI, reports and decks whenever you show an AI feature of Previo. |
| **Alfred plum `#6F2F6A`** | The **Alfred mascot** illustration (`alfred/alfred.svg`) and materials about the **Alfred guest app** (the guest-facing app), where it is that app's own primary color. Not for Previo product UI. |

Rules for both:
- They are **only for AI / Alfred**, never a second accent or decoration. Red stays the brand color.
- Do not mix the two purples on one surface. Red (Previo) and one purple (AI or Alfred) may share a
  composition.
- Never put purple on a red area; it disappears there.

### Reservation and payment states (Plachta UI)

For a faithful product UI (Plachta, reservations) use the state colors from `tokens.md`: confirmed
`#40A801`, option `#FA8200`, checked-in `#0385BD`, checked-out `#808080`; unpaid `#E40D01`; "Today"
column `#FDEAA8`. These are product colors, not a palette for charts or decoration.

## Typography

- **Font: Inter** (whole brand, headings and text). Bundled in `fonts/`, see **Fonts** above.
- Weights: **Regular 400** (text) and **Medium 500** (headings, labels, CTA). Use bold sparingly.
- Type scale and line heights are in `tokens.md`. Line height is mostly 24 px, tighter for headings.

## Radius, shadow, spacing

- Radius: SM 4 / MD 8 / LG 12 / XL 16 px, full rounding (pill) for tags and avatars.
- Shadow (elevation): `0 4px 8px rgba(10,10,10,0.12)`.
- Spacing: 8 px base step, canonical **LG = 24 px** (gap between blocks). Scale in `tokens.md`.

## Do's and don'ts

**Do**
- Keep a white/light background and one brand red `#b50000`, used as described in **Use of red**.
- Inter Medium for headings, Inter Regular for text; build hierarchy with size and weight, not color.
- Semantic colors only for state/meaning (error, success), and always with an icon, never color
  alone (accessibility + the collision with Primary Dark).
- Cover and closing areas may be full red or dark (`#202124`) with white text.

**Don't**
- Do not change the red (no `#D4202C`, `#FF0000` etc.); the canonical value is `#b50000`.
- Do not use Trebuchet, Calibri, Arial or the tool default; always Inter (with fallbacks), and tell
  the user when the font could not be applied (see **Fonts**).
- Do not mix several accent colors; red is the only dominant one. The only exception is the AI /
  Alfred purple, and only for AI / Alfred.
- Do not make rainbows out of semantic colors; they are not a palette.
- Do not flood surfaces with bold text; Medium is enough for headings.
- Do not use Negative and Primary Dark next to each other without another distinction (icon/label).

## Output instructions

- **.pptx**: follow `templates/deck-structure.md`; apply colors inline (with a pptx skill or library
  if one is available). Cover/closing full red or dark, content slides white with section label,
  footer and page number. Headings Inter Medium (see **Fonts**).
- **PDF / HTML**: start from the closest template. If you build from scratch, take the CSS variables
  from `tokens.md` and embed the fonts as described in **Fonts**. Cards on `#f2f2f2` or white with a
  `#e5e5e5` border.
- **One-pager**: always **fixed A4** (210 × 297 mm), one page. Render it and check the page count.
  If the content overflows, shorten the text or drop the least important block; never stretch the
  page or let it spill onto a second page. If there is empty space at the bottom, give the hero more
  room rather than adding filler. A variable page height is only acceptable for a screen-only PDF
  when the user explicitly asks for it.
- **Report**: A4, multiple pages allowed. Same hero/signal rule per page.
- **Dashboard/report charts**: the one item that matters in red, everything else on the gray scale;
  semantic colors only for state, always with an icon or sign next to the color.

## Layout and composition: avoiding the generic look

Brand tokens (color, font, radius) alone do not stop an output from looking like a universal
template. These are concrete rules specific to Previo outputs, taken from real mistakes.

**Recognized patterns to avoid (AI slop):**
- **Three identical KPI cards** (big number + small label, repeated 3×). It is a safe default, not a
  decision. Unless the data really are three equal metrics, do not force this shape.
- **Equal-width columns for unequal content.** If three features/steps are not truly equal or
  sequential, do not put them into three equal columns just for symmetry.
- **Generic status pill with a dot** (colored dot + text in a rounded bar). It is a universal
  dashboard pattern (Stripe/Linear), nothing that comes from Previo or hospitality. Use it only if the
  state really needs its own visual container, not as default decoration.
- **The same radius on everything** (cards, pills, images) without thought. Radius is a hierarchy
  tool (bigger = more important block), not blanket decoration.
- **Filler copy** ("seamless", "within the same flow", "reception just confirms"). Write concretely
  what the product does differently (numbers, steps, mechanics), not generic SaaS sentences.
- **Red used equally strongly everywhere.** See **Use of red**: one hero, a few small signals.

**What to do instead:**
- Before composing, override the safe default: look at the real content (how many items, are they
  equal, sequential, structured differently?) and only then pick the shape: a timeline for a process,
  one dominant visualization for one key number, an asymmetric layout when one thing matters more.
- One place in the composition may be maximally "brand" (full red area, biggest number, signature
  element); the rest stays disciplined and quiet. Never spread the boldness evenly.
- If the finished output looks like a template that would work for any other company with the same
  data, go over it again and replace at least one element with something that comes specifically
  from what Previo / the product does.
- For richer visuals (one-pager, cover slide, poster), combine with a frontend/design skill if one is
  available: `previo-brand` supplies color/font/logo, the design skill helps keep the shape from
  being generic.

## Logo

The mark is a red 3D "P" (paperclip) plus the wordmark **previo** in lowercase. Keep enough clear
space, do not distort it, do not recolor it outside the variants below.

The logo is bundled in `logo/` in three SVG variants (vector, scales without loss):

| File | Use |
|---|---|
| `logo/previo-logo-color.svg` | Default, on white/light backgrounds (`#ffffff`, `#fafafa`, `#f2f2f2`) |
| `logo/previo-logo-black.svg` | On light backgrounds where color does not fit the context (e.g. black-and-white print, scan-friendly output) |
| `logo/previo-logo-white.svg` | On dark or full red backgrounds (`#202124`, `#b50000`, `#910000`): cover/section areas |

**Choosing the variant:**
- Light background → `previo-logo-color.svg` (default); `previo-logo-black.svg` only when color
  really cannot be used.
- Dark or red background → always `previo-logo-white.svg`. Never the color version on a red area.
- Never use the black variant on a colored background other than white / gray-50 / gray-100.

**Size and clear space:** keep the SVG's aspect ratio. Clear space around the logo = at least the
height of the "previo" wordmark on every side.

**By output type:**
- **.pptx**: insert the SVG as an image on cover/section slides (white background → color, red/dark
  background → white). If the tool cannot handle SVG, convert to PNG with a transparent background.
- **HTML/PDF**: paste the SVG markup inline (read it from `logo/`), as the templates do. Do not use
  `<img src="logo/...">`; the relative path does not exist next to the output file.

## Alfred (mascot)

`alfred/alfred.svg` (113 × 232) is the AI mascot: a hotel bellboy in a presenting gesture. It has
two colors, plum `#6F2F6A` and white. Rules:
- Place it **on white or light gray**, never on red. It works on dark, but Previo stands on light.
- Use its gesture (open palm towards the left) to **present the content**: it stands to the right
  of the UI or text being talked about.
- Do not distort, recolor or take it apart. Animate it as a whole (entrance, movement, subtle
  "breathing").
- `alfred/ai-icon.svg` is the AI icon from the design system (Alfred's head with sparkles, 24 × 20)
  for AI buttons and labels; it uses the AI purple, not the Alfred plum.

## Source of truth

The tokens match the Previo design system (Figma: *P – design system*). When in doubt about a value,
`tokens.md` wins over a guess or a tool default. The info semantic color and the exact spacing scale
(xs/sm/md) are still waiting for confirmation in the current design system; do not invent them.

## When something is missing: feedback for the skill author

If the user asks for something this skill does not cover (a new format, a missing color or asset,
a rule that is unclear or contradicts the request), do the best you can within the rules above, then
end your answer with a short note the user can forward to the skill author (Pavel Trnka, Previo).
Keep it to a few lines, in the user's language:

```
Feedback for previo-brand skill
Request: <what the user wanted, one sentence>
Missing / unclear: <what the skill did not cover>
What I did instead: <the decision you made>
Suggested change: <what to add or clarify in the skill>
```

Tell the user in one sentence that they can send this note to the author so the skill can be
improved. Do not suggest editing the skill files, cloning a repository or opening a pull request.
