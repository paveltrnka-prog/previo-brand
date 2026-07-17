# Previo brand tokeny

Zdroj: Figma **P – design system** (variables). Zdroj pravdy pro hodnoty.

## Barvy

### Primární
| Token | HEX | Použití |
|---|---|---|
| Primary | `#b50000` | Jediná značková barva — logo, akcenty, čísla, CTA, section labely |
| Primary Dark | `#910000` | Hover, důraz, tmavší varianta |
| Primary Transparent | `#faeaeb` | Jemné červené pozadí / highlight |

### Base
| Token | HEX |
|---|---|
| White | `#ffffff` |
| White Transparent | `#ffffff3d` (rgba 255,255,255,0.24) |
| Black | `#0a0a0a` |

### Grays
| Token | HEX | Typicky |
|---|---|---|
| Gray 50 | `#fafafa` | Nejjemnější plocha |
| Gray 100 | `#f2f2f2` | Pozadí karet/bloků |
| Gray 200 | `#e5e5e5` | Bordery, oddělovače |
| Gray 300 | `#cccccc` | Silnější border |
| Gray 400 | `#b2b2b2` | Disabled / placeholder |
| Gray 500 | `#515151` | Sekundární text, popisky |
| Gray 600 | `#202124` | Nadpisy, hlavní text |

### Sémantické (jen pro stav/význam, nikdy pro dekoraci)

Každý význam má jednoznačný **default** — ten použij, pokud nepotřebuješ vyloženě hover/badge variantu.

| Význam | Default (text/ikony) | Dark (hover/důraz) | Transparent (pozadí badge) |
|---|---|---|---|
| Positive | `#1b6422` | `#0d3211` | `#d9e7da` |
| Negative | `#a30000` | — *(nepoužívej `#910000`, to je Primary Dark — viz níže)* | `#f0d6d6` |
| Warning | `#ff6d0a` | `#853600` | `#ffe8d8` |
| Info | *(zatím neurčeno v DS — než potvrdíš ve Figmě, používej Gray 600 + ikonu, ne barvu)* | `#004466` | `#d6e4eb` |

**Pozor na kolizi:** `Negative` badge stav `#f51818` (starší hodnota) a `Primary Dark #910000` jsou vizuálně
blízko `Negative #a30000`. Nepoužívej `#f51818` jako alternativu k negative — drž se jen `#a30000` +
transparent `#f0d6d6`. Nikdy nekombinuj Negative a Primary Dark ve stejné kompozici vedle sebe (např. error
stav u červeného CTA) — na první pohled splývají. Pokud k tomu dojde, over-ride: negative dostane ikonu
navíc, ne jen barvu.

**Info nemá potvrzenou default barvu** v aktuálním exportu DS (jen dark `#004466`). Než se to ověří ve
Figmě, neinformuj čistě barvou — přidej ikonu/label. Nevymýšlej si vlastní odstín pro info default.

## Typografie

- **Family/Main: Inter.** Fallback: `Inter, "Segoe UI", system-ui, sans-serif`.
- Váhy: Regular **400**, Medium **500**.
- Fonty jsou přibalené v `fonts/` (statické instance z Inter Variable, licence SIL OFL 1.1):
  `Inter-Regular.ttf` (400) a `Inter-Medium.ttf` (500, jako samostatná rodina "Inter Medium").
  Viz sekce **Font handling** v `SKILL.md` pro instalaci/embed podle typu výstupu.

| Styl | Size / Line-height | Váha |
|---|---|---|
| Title 2 (Small) | 16 / 18 | Medium |
| Body 1 (Large) | 16 / 24 | Regular |
| Body 2 (Small) | 14 / 24 | Regular |
| Forms Label | 14 / 24 | Medium |
| Forms Body | 13 / 24 | Regular |
| Links / CTA | 14 / 24 | Medium |
| Badge | 12 / 24 | Regular |

## Radius
Zero 0 · SM 4 · MD 8 · LG 12 · XL 16 · Full = pill (tagy, avatary)

## Elevace (stín)
`Basic/300` = `0 4px 8px rgba(10, 10, 10, 0.12)`

## Spacing
Krok 8 px. Škála: xs · sm · md · **lg = 24 px** (kanonické odsazení mezi bloky) · atd.
> Pozn.: spacing tokeny v DS procházejí migrací (xs/sm/md se přerovnávají). Kotva `lg = 24 px` je stabilní; jemnější škálu ověř v aktuálním DS, než ji zafixuješ.

## CSS proměnné (copy-paste pro HTML/PDF)

```css
@font-face {
  font-family: "Inter";
  src: url("fonts/Inter-Regular.ttf") format("truetype");
  font-weight: 400;
  font-style: normal;
}
@font-face {
  font-family: "Inter Medium";
  src: url("fonts/Inter-Medium.ttf") format("truetype");
  font-weight: 500;
  font-style: normal;
}

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

  /* Semantic — defaults only, see table above for hover/transparent variants */
  --previo-positive: #1b6422;
  --previo-negative: #a30000;
  --previo-warning: #ff6d0a;
  --previo-info-dark: #004466; /* no confirmed default; pair with icon, not color alone */

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

## PPTX rychlá reference (RGB)
- Primary red: `181, 0, 0`
- Primary dark: `145, 0, 0`
- Negative (nepoužívat zaměnitelně s primary dark): `163, 0, 0`
- Ink (nadpisy/text): `32, 33, 36`
- Muted: `81, 81, 81`
- Border: `229, 229, 229`
- Surface: `242, 242, 242`
- White: `255, 255, 255`
