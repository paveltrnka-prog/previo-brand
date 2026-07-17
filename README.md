# previo-brand

Claude skill, který aplikuje oficiální Previo brand (barvy, typografie, logo) na vizuální výstupy generované přes Claude — prezentace, PDF, HTML reporty, onepagery, dashboardy.

Zdroj pravdy pro hodnoty je Previo design systém (Figma: **P – design system**). Skill sám o sobě neřeší kompozici/layout — od v2 obsahuje aspoň základní pravidla, jak se vyhnout genericky vyhlížejícímu AI výstupu, ale pro bohatší vizuální výstupy se doporučuje kombinace s obecným `frontend-design` skillem.

**Nejnovější balíček ke stažení:** [previo-brand-v2.skill](https://github.com/paveltrnka-prog/previo-brand/releases/latest)

---

## Co skill dělá

Automaticky se spouští při tvorbě čehokoli vizuálního (`.pptx`, PDF, HTML dashboard/report, onepager, poster, banner, sociální grafika) — i bez explicitní zmínky brandu — a aplikuje:

| Oblast | Co dělá |
|---|---|
| **Barvy** | Primární červená `#b50000` jako jediná dominantní značková barva, škála šedých, sémantické barvy jen pro stav (viz [`tokens.md`](previo-brand/tokens.md)) |
| **Typografie** | Font Inter (Regular 400 / Medium 500), přibalený přímo ve skillu |
| **Logo** | Tři varianty (color/black/white) podle pozadí, přibalené jako SVG |
| **Radius / stín / spacing** | Jednotné hodnoty vycházející z Figma DS |

Textové `.md` výstupy skill nechává neutrální. U `.docx` rozhoduje podle účelu dokumentu (viz sekce „Hranice .docx" v [`SKILL.md`](previo-brand/SKILL.md)) — plošně to nevylučuje.

## Rychlý přehled barev

| Token | HEX | Použití |
|---|---|---|
| Primary | `#b50000` | Logo, akcenty, čísla, CTA, section labely |
| Primary Dark | `#910000` | Hover, důraz, tmavší varianta |
| Gray 600 | `#202124` | Nadpisy, hlavní text |
| Gray 500 | `#515151` | Sekundární text, popisky |
| Positive | `#1b6422` | Kladný stav |
| Negative | `#a30000` | Záporný stav (nezaměňovat s Primary Dark) |
| Warning | `#ff6d0a` | Varování |

Kompletní tabulka barev, typografie, radiusů a CSS proměnných je v [`tokens.md`](previo-brand/tokens.md).

## Jak to použít

1. Zabal obsah složky `previo-brand/` (`SKILL.md`, `tokens.md`, `fonts/`, `logo/`) do jednoho `.skill` souboru (zip) — buď jako `previo-brand/` uvnitř archivu.
2. Nahraj `.skill` soubor v Claude (Settings → Capabilities/Skills → Upload skill).
3. Skill se pak automaticky spouští při relevantních požadavcích (viz `description` v frontmatteru `SKILL.md`) — není potřeba ho explicitně zmiňovat, stačí požádat o prezentaci/report/onepager atd.

Pro rychlý balíček ze složky:
```bash
cd previo-brand-repo
zip -r -X previo-brand.skill previo-brand -x '.*'
```

Aktuální zabalená verze je vždy ke stažení v sekci [Releases](https://github.com/paveltrnka-prog/previo-brand/releases) — není nutné balit ručně, pokud stačí poslední vydaná verze.

## Struktura

```
previo-brand/
├── SKILL.md          pravidla — kdy a jak brand aplikovat
├── tokens.md          hodnoty — barvy, typografie, radius, spacing, CSS proměnné
├── fonts/
│   ├── Inter-Regular.ttf   (400, SIL OFL 1.1)
│   └── Inter-Medium.ttf    (500, samostatná family name, statická instance)
└── logo/
    ├── previo-logo-color.svg   default, světlé pozadí
    ├── previo-logo-black.svg   ČB tisk / scan-friendly kontext
    └── previo-logo-white.svg   tmavé nebo červené pozadí
```

## Přispívání

Změny se dělají přes pull request, ne přímo do `main`. Postup a pravidla pro balíčky/Releases jsou v [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Changelog — v2

Oproti první verzi (jen `SKILL.md` + `tokens.md`, bez přibalených assetů):

**Fonty**
- Přibalený Inter jako skutečné TTF (statické instance 400/500 z Inter Variable), ne jen odkaz na systémový font. Řeší, že `.pptx`/PDF export bez nainstalovaného fontu tiše spadne na fallback a brand vizuálně neplatí.
- Explicitní instrukce pro `.pptx` (systémová instalace + `fc-cache`) vs. HTML/PDF (`@font-face` na lokální cestu).
- Pravidlo: pokud se font nepodaří aplikovat, skill to má nahlásit, ne tiše nahradit jiným.

**Logo**
- Přidány 3 SVG varianty (color/black/white).
- Pravidlo volby podle pozadí + zákaz kombinací, které ztrácí kontrast (např. black varianta na barevném podkladu).

**Sémantické barvy**
- Sjednocený jednoznačný default pro každý význam (positive/negative/warning/info).
- Info nemá potvrzenou base barvu v aktuálním DS exportu → skill radí použít ikonu místo vymyšleného odstínu, dokud se hodnota neověří ve Figmě.

**Kolize barev**
- Negative (`#a30000`) a Primary Dark (`#910000`) jsou si vizuálně blízko → nové pravidlo je nekombinovat bez dalšího odlišení (ikona/label).

**Hranice `.docx`**
- Původní plošné „nebrandovat `.docx`" nahrazeno rozhodovacím pravidlem podle účelu dokumentu (externí report/onepager → brandovat, interní draft → neutrální).

**Layout a kompozice (nové)**
- Pojmenované vzorce, kterým se vyhnout, protože působí jako generický AI výstup: KPI trojice (velké číslo + label × 3), vynucené stejné sloupce pro nerovnocenný obsah, generický status pill, jednotný radius bez rozmyslu, vatová copy, plošně rozprostřená červená.
- Doporučení rozhodovat o tvaru layoutu podle skutečné struktury obsahu (sekvence → timeline, jedno klíčové číslo → hero moment) a nechat jedno místo v kompozici „nejvíc brandové", zbytek disciplinovaně tiché.
- Doporučená kombinace s `frontend-design` skillem pro kompoziční rozhodnutí u bohatších vizuálních výstupů.

**PDF page sizing**
- Poznámka pro onepager/jednostránkové PDF: nastavit výšku stránky podle skutečného obsahu (ne fixní A4), zkontrolovat počet stran po renderu.

## Zdroj a údržba

Tokeny odpovídají stavu Previo design systému (Figma: *P – design system*). Při změně DS stačí aktualizovat `tokens.md` — `SKILL.md` se typicky měnit nemusí.
