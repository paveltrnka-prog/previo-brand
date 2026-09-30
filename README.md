# previo-brand

Claude skill, který aplikuje oficiální Previo brand (barvy, typografie, logo) na vizuální výstupy generované přes Claude — prezentace, PDF, HTML reporty, onepagery, dashboardy.

Zdroj pravdy pro hodnoty je Previo design systém (Figma: **P – design system**). Skill obsahuje pravidla kompozice proti genericky vyhlížejícímu AI výstupu a hotové šablony, takže většinu výstupů zvládne sám. U bohatších vizuálů se dál hodí kombinace s obecným `frontend-design` skillem.

**Nejnovější balíček ke stažení:** [previo-brand-v3.skill](https://github.com/paveltrnka-prog/previo-brand/releases/latest)

---

## Co skill dělá

Automaticky se spouští při tvorbě čehokoli vizuálního (`.pptx`, PDF, HTML dashboard/report, onepager, poster, banner, sociální grafika) — i bez explicitní zmínky brandu — a aplikuje:

| Oblast | Co dělá |
|---|---|
| **Barvy** | Primární červená `#b50000` jako dominantní značková barva (jedinou výjimkou je AI fialová), škála šedých, sémantické barvy jen pro stav (viz [`tokens.md`](previo-brand/tokens.md)) |
| **Typografie** | Font Inter (Regular 400 / Medium 500), přibalený přímo ve skillu |
| **Logo** | Tři varianty (color/black/white) podle pozadí, přibalené jako SVG |
| **Radius / stín / spacing** | Jednotné hodnoty vycházející z Figma DS |
| **AI a Alfred** | Fialová `#673AB7` výhradně pro AI funkce, postavička Alfreda a AI ikona (`alfred/`) |
| **Stavy produktu** | Barvy stavů rezervací a plateb z Plachty (viz [`tokens.md`](previo-brand/tokens.md)) |
| **Šablony** | Hotové výchozí body v `templates/`: onepager, report, sociální grafiky (feed, story, LinkedIn), struktura prezentace |

Textové `.md` výstupy skill nechává neutrální. U `.docx` rozhoduje podle účelu dokumentu (viz sekce „Hranice .docx" v [`SKILL.md`](previo-brand/SKILL.md)) — plošně to nevylučuje.

## Jak s ním pracovat

Skill se spouští sám, stačí říct, co chceš. Pošli jen obsah (texty, čísla, cíl), vzhled řeší skill.

| Zadání | Co skill udělá |
|---|---|
| „Udělej onepager o Alfredovi pro hoteliéry.“ | Vezme `templates/onepager.html`, přepíše texty, jedno velké číslo a fakty vedle. A4. |
| „Z těchto čísel udělej report za Q3.“ | Použije `templates/report.html`: jedna hlavní vizualizace, tabulka, doporučení. |
| „Sociální post s číslem 42 %.“ | Feed 4:5 (1080 × 1350 px) ze `social-feed.html`, export do PNG. |
| „Story k novince v Plachtě.“ | Story 9:16 (1080 × 1920 px), celá plocha červená, bezpečné zóny. |
| „Obrázek na LinkedIn k článku.“ | `social-linkedin.html`, 1200 × 627 px, tvrzení + číslo. |
| „Prezentace pro klienta, 8 slidů.“ | `.pptx` podle typů slidů z `templates/deck-struktura.md`. |
| „Ukaž Alfreda, jak představuje novou funkci.“ | Postavička `alfred/alfred.svg` vedle obsahu, na světlé ploše, nedeformovaná. |
| „Mockup Plachty se stavy rezervací.“ | Barvy stavů z `tokens.md` (potvrzená, opce, ubytovaný…). |

Doladění jde běžnou řečí: „ať je to méně přeplácané“, „zvýrazni jen jedno číslo“, „bez fialové“.

**Co umí nového ve v3**
- **AI fialová jen pro AI**: AI tlačítka, štítky a odpovědi Alfreda mají `#673AB7`. Na červené ploše ji skill nepoužije a nemíchá ji jako druhý akcent.
- **Hotové šablony**: skill kopíruje nejbližší šablonu a přepisuje texty, netvoří layout znovu. HTML jsou samostatné, font i logo nesou v sobě.
- **Alfred**: maskot a AI ikona s pravidly (světlé pozadí, jen celek, gesto představuje obsah).
- **Stavy produktu**: věrné UI Plachty bez vymýšlení odstínů.
- **Pro kolegy**: [`INSTALACE.md`](previo-brand/INSTALACE.md), návod na 2 minuty. Výstup pro ostatní posílej jako PDF, `.pptx` a `.docx` font nenesou.

**Úprava šablon:** měň `previo-brand/src/*.html` a spusť `python3 previo-brand/build.py`. `templates/` se přegeneruje.

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
| AI | `#673AB7` | Jen AI funkce a Alfred (gradient do `#4E2C8B`) |

Kompletní tabulka barev (vč. stavů rezervací a plateb), typografie, radiusů a CSS proměnných je v [`tokens.md`](previo-brand/tokens.md).

## Jak to použít

1. Zabal složku `previo-brand/` do jednoho `.skill` souboru (zip) — buď jako `previo-brand/` uvnitř archivu.
2. Nahraj `.skill` soubor v Claude (Settings → Capabilities/Skills → Upload skill).
3. Skill se pak automaticky spouští při relevantních požadavcích (viz `description` v frontmatteru `SKILL.md`) — není potřeba ho explicitně zmiňovat, stačí požádat o prezentaci/report/onepager atd.

Pro rychlý balíček ze složky:
```bash
cd previo-brand-repo
zip -r -X previo-brand.skill previo-brand -x '.*'
```

Instalace pro kolegy je popsaná v [`INSTALACE.md`](previo-brand/INSTALACE.md).

Aktuální zabalená verze je vždy ke stažení v sekci [Releases](https://github.com/paveltrnka-prog/previo-brand/releases) — není nutné balit ručně, pokud stačí poslední vydaná verze.

## Struktura

```
previo-brand/
├── SKILL.md          pravidla — kdy a jak brand aplikovat
├── tokens.md         hodnoty — barvy, typografie, radius, spacing, CSS proměnné
├── INSTALACE.md      instalace pro kolegy
├── build.py          generuje templates/ ze src/
├── fonts/
│   ├── Inter-Regular.ttf   (400, SIL OFL 1.1)
│   ├── Inter-Medium.ttf    (500, samostatná family name, statická instance)
│   └── LICENSE-Inter.md
├── logo/
│   ├── previo-logo-color.svg   default, světlé pozadí
│   ├── previo-logo-black.svg   ČB tisk / scan-friendly kontext
│   └── previo-logo-white.svg   tmavé nebo červené pozadí
├── alfred/
│   ├── alfred.svg      postavička (maskot AI)
│   └── ai-icon.svg     AI ikona z design systému
├── src/                zdrojové HTML šablon (upravuj tady)
└── templates/          hotové samostatné šablony (generované, needitovat)
```

## Přispívání

Změny se dělají přes pull request, ne přímo do `main`. Postup a pravidla pro balíčky/Releases jsou v [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Changelog — v3

**AI a Alfred**
- Fialová pro AI: `#673AB7` → `#4E2C8B` (gradient 135°), světlá `#8B69C8`, tint `#E7DFF3`. Jen pro AI funkce, nikdy na červenou plochu. Je to jediná výjimka z pravidla o jedné dominantní barvě.
- Postavička Alfreda (`alfred/alfred.svg`) a AI ikona (`alfred/ai-icon.svg`) s pravidly použití.
- Nové CSS proměnné `--previo-ai*` v `tokens.md`.

**Stavy produktu**
- Barvy stavů rezervací a plateb z Plachty (potvrzená, opce, ubytovaný, odhlášený, nezaplaceno, sloupec „Dnes“). Jsou to barvy produktu, ne paleta pro grafy.

**Šablony**
- `templates/`: onepager, report, social feed 4:5, story 9:16, LinkedIn/OG a `deck-struktura.md`. HTML šablony jsou samostatné (font i logo vložené).
- `src/` + `build.py`: šablony se generují ze zdroje, upravuje se vždy `src/`.

**Pro kolegy**
- Sekce „Rychlý start“ v `SKILL.md` a `INSTALACE.md`.
- Poznámka, že `.pptx`/`.docx` font nenesou, proto posílat PDF nebo nainstalovat fonty.

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

Tokeny odpovídají stavu Previo design systému (Figma: *P – design system*). Při změně DS stačí aktualizovat `tokens.md` — `SKILL.md` se typicky měnit nemusí. Po změně loga nebo fontu spusť `python3 previo-brand/build.py`, aby se přegenerovaly `templates/`.
