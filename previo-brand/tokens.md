# Previo brand tokens

Source: Figma **P – design system** (variables). Source of truth for all values.

## Colors

### Primary
| Token | HEX | Use |
|---|---|---|
| Primary | `#b50000` | The one brand color: logo, hero (red area or biggest number), signals (section label, CTA, highlighted chart item). See "Use of red" in `SKILL.md` |
| Primary Dark | `#910000` | Hover, emphasis, darker variant |
| Primary Transparent | `#faeaeb` | Soft red background / highlight |

### Base
| Token | HEX |
|---|---|
| White | `#ffffff` |
| White Transparent | `#ffffff3d` (rgba 255,255,255,0.24) |
| Black | `#0a0a0a` |

### Grays
| Token | HEX | Typically |
|---|---|---|
| Gray 50 | `#fafafa` | Softest surface |
| Gray 100 | `#f2f2f2` | Card/block background |
| Gray 200 | `#e5e5e5` | Borders, dividers |
| Gray 300 | `#cccccc` | Stronger border |
| Gray 400 | `#b2b2b2` | Disabled / placeholder, non-highlighted chart items |
| Gray 500 | `#515151` | Secondary text, captions, gray section labels |
| Gray 600 | `#202124` | Headings, main text |

### Semantic (only for state/meaning, never decoration)

Each meaning has one **default**; use it unless you really need the hover/badge variant.

| Meaning | Default (text/icons) | Dark (hover/emphasis) | Transparent (badge background) |
|---|---|---|---|
| Positive | `#1b6422` | `#0d3211` | `#d9e7da` |
| Negative | `#a30000` | — *(do not use `#910000`, that is Primary Dark, see below)* | `#f0d6d6` |
| Warning | `#ff6d0a` | `#853600` | `#ffe8d8` |
| Info | *(not yet defined in the DS; until confirmed in Figma use Gray 600 + an icon, not a color)* | `#004466` | `#d6e4eb` |

**Collision warning:** the old Negative badge value `#f51818` and `Primary Dark #910000` are visually
close to `Negative #a30000`. Do not use `#f51818` as an alternative to negative; stick to `#a30000` +
transparent `#f0d6d6`. Never put Negative and Primary Dark next to each other in the same composition
(e.g. an error state at a red CTA): at first glance they blend. If it happens, give negative an
extra icon, not just the color.

**Info has no confirmed default color** in the current DS export (only dark `#004466`). Until it is
confirmed in Figma, never communicate info by color alone; add an icon/label. Do not invent your own
info shade.

### AI: Previo product UI (`--color-ai*` in the DS)
| Token | HEX | Use |
|---|---|---|
| AI | `#673AB7` | AI button (PBtnAi), AI labels and actions |
| AI Dark | `#4E2C8B` | End of the AI button gradient (135°) |
| AI Light | `#8B69C8` | AI elements on dark backgrounds, AI answers in charts |
| AI Transparent | `#E7DFF3` | AI label background ("Read with AI") |

### Alfred: mascot and Alfred guest app
| Token | HEX | Use |
|---|---|---|
| Alfred plum | `#6F2F6A` | The mascot `alfred/alfred.svg` and materials about the Alfred guest app. Not for Previo product UI |

Same values on screen and in print; no separate CMYK values are defined. Never mix the AI purple and
the Alfred plum on one surface.

### Reservation and payment states (Plachta)
| Token | HEX |
|---|---|
| resConfirmed (confirmed) | `#40A801` |
| resOption (option) | `#FA8200` |
| resCheckedIn (checked in) | `#0385BD` |
| resCheckedOut (checked out) | `#808080` |
| resCanceled / resNoShow / resOther / resWaitingList | `#9F0403` / `#976601` / `#8E369E` / `#2B2B2B` |
| payUnpaid / payPartially / payPaid | `#E40D01` / `#FB8EAC` / `#808080` |
| note ("Today" column) / noteDark ("Today" header) | `#FDEAA8` / `#F4D053` |
| primaryLight / primaryTransparent (DS) | `#D90000` / `#F9EBEB` |

## Typography

- **Family/Main: Inter.** Fallback: `Inter, "Segoe UI", system-ui, sans-serif`.
- Weights: Regular **400**, Medium **500**.
- Fonts are bundled in `fonts/` (static instances from Inter Variable, SIL OFL 1.1):
  `Inter-Regular.ttf` (400) and `Inter-Medium.ttf` (500, as a separate family "Inter Medium").
  See **Fonts** in `SKILL.md` for embedding/installing per output type.

| Style | Size / Line height | Weight |
|---|---|---|
| Title 2 (Small) | 16 / 18 | Medium |
| Body 1 (Large) | 16 / 24 | Regular |
| Body 2 (Small) | 14 / 24 | Regular |
| Forms Label | 14 / 24 | Medium |
| Forms Body | 13 / 24 | Regular |
| Links / CTA | 14 / 24 | Medium |
| Badge | 12 / 24 | Regular |

## Radius
Zero 0 · SM 4 · MD 8 · LG 12 · XL 16 · Full = pill (tags, avatars)

## Elevation (shadow)
`Basic/300` = `0 4px 8px rgba(10, 10, 10, 0.12)`

## Spacing
8 px step. Scale: xs · sm · md · **lg = 24 px** (canonical gap between blocks) · etc.
> Note: spacing tokens in the DS are being migrated (xs/sm/md are being reordered). The `lg = 24 px`
> anchor is stable; check the finer scale in the current DS before relying on it.

## CSS variables (copy-paste for HTML/PDF)

Fonts: the HTML templates already embed Inter. When building HTML from scratch, add two `@font-face`
rules whose `src` is a base64 `data:` URI of `fonts/Inter-Regular.ttf` (family `"Inter"`, weight 400)
and `fonts/Inter-Medium.ttf` (family `"Inter Medium"`, weight 500), e.g.
`src: url("data:font/ttf;base64,…") format("truetype");`. Do not point `src` at a relative file path.

```css
:root {
  /* Primary */
  --previo-primary: #b50000;
  --previo-primary-dark: #910000;
  --previo-primary-tint: #faeaeb;

  /* Base */
  --previo-white: #ffffff;
  --previo-black: #0a0a0a;

  /* Grays */
  --previo-gray-50: #fafafa;
  --previo-gray-100: #f2f2f2;
  --previo-gray-200: #e5e5e5;
  --previo-gray-300: #cccccc;
  --previo-gray-400: #b2b2b2;
  --previo-gray-500: #515151;
  --previo-gray-600: #202124;

  /* Semantic: defaults only, see the table above for hover/transparent variants */
  --previo-positive: #1b6422;
  --previo-negative: #a30000;
  --previo-warning: #ff6d0a;
  --previo-info-dark: #004466; /* no confirmed default; pair with an icon, not color alone */

  /* AI: Previo product UI only */
  --previo-ai: #673AB7;
  --previo-ai-dark: #4E2C8B;
  --previo-ai-light: #8B69C8;
  --previo-ai-tint: #E7DFF3;
  --previo-ai-gradient: linear-gradient(135deg, #673AB7, #4E2C8B);

  /* Alfred: mascot and Alfred guest app only */
  --previo-alfred: #6F2F6A;

  /* Type */
  --previo-font: "Inter", "Segoe UI", system-ui, sans-serif;
  --previo-font-medium: "Inter Medium", "Segoe UI", system-ui, sans-serif;
  --previo-w-regular: 400;
  --previo-w-medium: 500;

  /* Radius */
  --previo-radius-sm: 4px;
  --previo-radius-md: 8px;
  --previo-radius-lg: 12px;
  --previo-radius-xl: 16px;

  /* Elevation */
  --previo-shadow: 0 4px 8px rgba(10, 10, 10, 0.12);

  /* Spacing anchor */
  --previo-space-lg: 24px;
}
```

## PPTX quick reference (RGB)
- Primary red: `181, 0, 0`
- Primary dark: `145, 0, 0`
- Negative (not interchangeable with primary dark): `163, 0, 0`
- Ink (headings/text): `32, 33, 36`
- Muted (secondary text, gray section labels): `81, 81, 81`
- Border: `229, 229, 229`
- Surface: `242, 242, 242`
- White: `255, 255, 255`
