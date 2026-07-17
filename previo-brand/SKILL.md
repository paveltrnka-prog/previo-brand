---
name: previo-brand
description: >-
  Aplikuje oficiální Previo brand (barvy, typografii, styl) na vizuální výstupy.
  Použij VŽDY, když vzniká prezentace/deck (.pptx), PDF, HTML dashboard nebo report,
  onepager, poster, banner nebo jakýkoli vizuál, který má vypadat "jako od Previa" —
  i když uživatel branding nezmíní. Zdroj pravdy jsou tokeny z Previo design systému
  (P – design system): primární červená #b50000, font Inter (přibalený v fonts/), logo
  ve třech variantách (přibalené v logo/: color/black/white). Obsahuje i kompoziční pravidla
  proti generickému "AI slop" vzhledu (KPI trojice, stejné sloupce, status pill, atd.) —
  viz sekce "Layout a kompozice". Textové .md nech neutrální; u .docx viz sekce "Hranice .docx"
  — reporty a onepagery ve Wordu branding většinou chtějí, čistě interní poznámky ne.
---

# Previo Brand — styling vizuálních výstupů

Sjednocuje vzhled vizuálních výstupů podle oficiálního Previo brandu. Tokeny pocházejí
z Figma souboru **P – design system** (variables), ne z náhodného decku. Tenhle skill je
zdroj pravdy — přebíjí defaultní paletu a fonty jakéhokoli nástroje.

## Kdy použít

Spusť při tvorbě čehokoli vizuálního: **prezentace (.pptx), PDF, HTML dashboard/report,
onepager, poster, banner, sociální grafika, e-mailový vizuál**. Aplikuj brand automaticky,
i když o něj uživatel výslovně nepožádá.

**Nepoužívej** na čistě textové `.md` — ty nech neutrální, ledaže si uživatel branding
výslovně řekne. Pro `.docx` viz sekci **Hranice .docx** níže — není to plošné "ne".

## Hranice .docx

`.docx` není automaticky vyloučen. Rozhodni podle účelu dokumentu:

- **Aplikuj brand** (nadpisy Inter Medium, barevné section labely, případně hlavička/patička
  s logem): report pro klienta, onepager, nabídka, cokoli, co opustí firmu nebo jde na sdílenou
  plochu (SharePoint, e-mail navenek).
- **Nech neutrální**: interní poznámky, pracovní draft, meeting notes, cokoli co zůstává jen
  mezi kolegy a nikdy se neprezentuje ven.

Pokud účel není jasný z kontextu, zeptej se jednou větou ("Má to být brandované, nebo interní
draft?"), než začneš stylovat.

## Font handling (kritické — bez tohoto brand nesedí)

Font **Inter** je přibalený přímo ve skillu ve složce `fonts/`:
- `fonts/Inter-Regular.ttf` — váha 400, family name `Inter`
- `fonts/Inter-Medium.ttf` — váha 500, samostatná family name `Inter Medium` (statická instance,
  ne variabilní — potřeba kvůli nástrojům jako PowerPoint/LibreOffice, které neumí osu `wght`)

Licence: SIL Open Font License 1.1 (Google Fonts distribuce Inter) — volně použitelné a
redistribuovatelné.

**Podle výstupu:**

- **HTML / PDF (přes HTML→PDF pipeline)**: vlož `@font-face` blok z `tokens.md` s relativní cestou
  k `fonts/*.ttf`. Nikdy nespoléhej na to, že systém Inter má — bez `@font-face` renderer tiše
  spadne na fallback (`Segoe UI` / `system-ui`) a brand vizuálně neplatí, i když kód barvy sedí.
- **.pptx**: nástroj (LibreOffice/python-pptx render) potřebuje font nainstalovaný v systému, ne
  jen odkázaný cestou. Před generováním nakopíruj oba `.ttf` do systémové fontové složky
  (např. `~/.local/share/fonts/` nebo `/usr/share/fonts/truetype/previo/`) a spusť `fc-cache -f`.
  Nadpisy/labely pak referencuj jako font `"Inter Medium"`, běžný text jako `"Inter"` — ne jako
  jeden font se dvěma řezy, protože PowerPoint/LibreOffice bez variabilní osy neumí přepnout váhu
  jen přes bold/regular přepínač spolehlivě.
- **Pokud font selže / nejde nainstalovat**: nepoužívej Trebuchet/Calibri/Arial potichu jako
  náhradu bez upozornění — řekni uživateli, že Inter nešlo aplikovat a použil se fallback
  `Segoe UI / system-ui`, ať ví, že finální vizuál není 1:1 s brandem.

## Barvy

Kompletní tokeny včetně hodnot jsou v `tokens.md`. Jádro:

- **Primární červená `#b50000`** je jediná výrazná značková barva — logo, akcenty, klíčová čísla,
  primární CTA, section labely. Tmavší varianta `#910000` (hover/důraz), jemné pozadí `#faeaeb`.
- **Text a plochy**: základ je bílá `#ffffff` + tmavý text z grays (`#202124` nadpisy, `#515151`
  sekundární). Škála šedých `#fafafa → #202124` na plochy, oddělovače a UI.
- **Sémantické** (jen když nesou význam, ne dekoraci): positive `#1b6422`, negative `#a30000`,
  warning `#ff6d0a`, info — zatím bez potvrzeného default odstínu, viz `tokens.md`.
- **Nekombinuj Negative (`#a30000`) a Primary Dark (`#910000`) vedle sebe** — jsou si vizuálně
  příliš blízko a bez rozdílu v ikonografii splývají (např. chybová hláška u červeného CTA).

## Typografie

- **Font: Inter** (celý brand, nadpisy i text). Přibalený v `fonts/`, viz **Font handling** výše.
- Váhy: **Regular 400** (text) a **Medium 500** (nadpisy, labely, CTA). Bold používej střídmě.
- Typová škála a line-heighty viz `tokens.md`. Line-height je vesměs 24 px, nadpisy těsnější.

## Radius, stíny, spacing

- Radius: SM 4 / MD 8 / LG 12 / XL 16 px, plné zaoblení (pill) pro tagy a avatary.
- Stín (elevace): `0 4px 8px rgba(10,10,10,0.12)`.
- Spacing: 8px základní krok, kanonický **LG = 24 px** (odsazení mezi bloky). Škála v `tokens.md`.

## Do's & Don'ts

**Do**
- Drž bílé/světlé pozadí a jednu značkovou červenou `#b50000` jako akcent.
- Červenou dávej na to, co má táhnout oko: čísla, CTA, section labely, klíčové slovo.
- Nadpisy Inter Medium, text Inter Regular; hierarchii dělej velikostí a váhou, ne barvami.
- Sémantické barvy jen pro stav/význam (chyba, úspěch), ne pro dekoraci — a vždy s ikonou, ne
  jen barvou samotnou (accessibility + kolize s primary dark).
- Cover / closing plochy smí být plná červená nebo tmavá (`#202124`) s bílým textem.

**Don't**
- Neměň odstín červené (žádné #D4202C, #FF0000 apod.) — kanonická je `#b50000`.
- Nepoužívej Trebuchet, Calibri, Arial ani default nástroje — vždy Inter (s fallbacky), a pokud
  se nepodaří font aplikovat, řekni to uživateli (viz Font handling).
- Nemíchej víc akcentních barev najednou; červená je jediná dominantní.
- Nedělej barevné duhy sémantickými barvami; nejsou paleta.
- Nezaplácej plochy tučným textem — Medium na nadpisy stačí.
- Nepoužívej Negative a Primary Dark vedle sebe bez dalšího odlišení (ikona/label).

## Instrukce pro výstupy

- **.pptx**: aplikuj barvy inline (skill `pptx`). Cover/section plná červená nebo tmavá plocha,
  obsahové slidy bílé s červeným section labelem, patičkou a číslem stránky. Nadpisy Inter Medium
  (font nainstalovaný ze složky `fonts/`, viz **Font handling**).
- **PDF / HTML**: definuj tokeny jako CSS proměnné (blok v `tokens.md`), `@font-face` na lokální
  `fonts/*.ttf`, radius a stín podle výše. Karty na `#f2f2f2`/bílé s borderem `#e5e5e5`.
  U onepageru/jednostránkového PDF nastav `@page` výšku podle skutečného obsahu (ne fixní A4) —
  vyrenderuj, zkontroluj počet stran a případně dolaď výšku, ať nevznikne prázdný spodek stránky
  ani přetečení na druhou stranu.
- **Dashboard/report**: KPI čísla červeně, grafy primárně červená + škála šedých, sémantické
  barvy jen pro stav — vždy s ikonou vedle barvy.

## Layout a kompozice — jak se vyhnout generickému vzhledu

Brand tokeny (barva, font, radius) samy o sobě negarantují, že výstup nebude vypadat jako
univerzální template. Tenhle skill řeší *jaké* barvy a fonty použít, ne *jak* je poskládat —
za kompozici odpovídá `frontend-design` skill, ale tady jsou konkrétní pravidla specifická pro
Previo výstupy, odpozorovaná z reálných chyb:

**Rozpoznané vzorce, kterým se vyhnout (AI slop):**
- **3 stejné KPI karty** (velké číslo + malý label, opakované 3×) — je to bezpečný default, ne
  rozhodnutí. Pokud data nejsou skutečně 3 rovnocenné metriky, nevynucuj tenhle tvar.
- **Sloupce se stejnou vahou pro nerovnocenný obsah** — pokud tři features/kroky nejsou skutečně
  rovnocenné nebo sekvenční, nedávej je do 3 stejně širokých sloupců jen kvůli symetrii.
- **Generický status pill s tečkou** (barevná tečka + text v zaoblené liště) — je to univerzální
  dashboard vzorec (Stripe/Linear), ne nic, co vzniklo z Previa nebo hotelnictví. Použij, jen
  pokud stav skutečně potřebuje vlastní vizuální kontejner, ne jako výchozí dekorace.
- **Stejný radius na všem** (karty, pill, obrázky) bez rozmyslu — je to neutrální "soft card"
  estetika. Radius je nástroj hierarchie (větší = důležitější blok), ne plošná dekorace.
- **Vatová copy** ("bezproblémové", "v rámci stejného flow", "recepce jen potvrzuje") — piš
  konkrétně, co produkt dělá jinak (čísla, kroky, mechanika), ne obecné SaaS věty.
- **Červená používaná stejně silně všude** (cover, čísla, labely najednou） — nech červenou
  udělat jednu věc pořádně (typicky nejdůležitější číslo nebo cover), zbytek ať stojí na
  šedé škále a velikosti textu.

**Co udělat místo toho:**
- Než začneš skládat layout, over-ridni bezpečný default: podívej se na skutečný obsah (kolik
  položek, jsou rovnocenné/sekvenční/jinak strukturované?) a teprve podle toho vyber tvar —
  timeline pro proces, jedna dominantní vizualizace pro jedno klíčové číslo, asymetrický layout
  pokud jedna věc je důležitější než zbytek.
- Jedno místo v kompozici smí být maximálně "brandové" (plná červená plocha, největší číslo,
  signature grafický prvek) — zbytek disciplinovaně tichý. Never spread the boldness evenly.
- Pokud výstup po sestavení vypadá jako šablona, která by fungovala pro jakoukoli jinou firmu se
  stejnými daty, projdi ho znovu a nahraď aspoň jeden prvek něčím, co vychází konkrétně z toho,
  co Previo/produkt dělá (ne z obecné "dashboard/onepager" estetiky).
- U vizuálně bohatších výstupů (onepager, cover slide, poster) zvaž kombinaci s `frontend-design`
  skillem pro kompoziční rozhodnutí — `previo-brand` dodá barvy/font/logo, `frontend-design`
  pomůže s tím, aby výsledný tvar nebyl univerzální.

## Logo

Značka je červené 3D „P" (paperclip) + wordmark **previo** malými písmeny. Logo drž s dostatečným
clear-space, needeformuj, nepřebarvuj mimo brand (žádné jiné odstíny než níže uvedené varianty).

Asset je přibalený v `logo/` ve třech variantách (SVG, vektor, škáluje bez ztráty kvality):

| Soubor | Použití |
|---|---|
| `logo/previo-logo-color.svg` | Výchozí — na bílém/světlém pozadí (`#ffffff`, `#fafafa`, `#f2f2f2`) |
| `logo/previo-logo-black.svg` | Na světlém pozadí, kde barevná verze nesedí kontextem (např. tiskové černobílé materiály, faxové/scan-friendly výstupy) |
| `logo/previo-logo-white.svg` | Na tmavém nebo plně červeném pozadí (`#202124`, `#b50000`, `#910000`) — cover/section plochy |

**Volba varianty podle pozadí:**
- Světlé pozadí → `previo-logo-color.svg` (default), `previo-logo-black.svg` jen když barva vyloženě nejde použít.
- Tmavé nebo červené pozadí → vždy `previo-logo-white.svg`. Nikdy barevnou verzi na červené ploše (splývá/špatný kontrast).
- Nikdy nekombinuj black variantu s barevným pozadím jiným než bílá/gray-50/gray-100 — na barevném podkladu ztrácí kontrast nebo vypadá jako chyba tisku.

**Rozměry a clear-space**: SVG má vlastní viewBox, nedeformuj poměr stran. Clear-space kolem loga =
minimálně výška wordmarku "previo" z každé strany (nezmenšovat blíž).

**Podle výstupu:**
- **.pptx**: vlož SVG jako obrázek na cover/section slide (bílé pozadí → color, červené/tmavé pozadí → white variant). Pokud nástroj pro export do PPTX neumí SVG přímo, převeď na PNG při zachování průhledného pozadí.
- **HTML/PDF**: `<img src="logo/previo-logo-color.svg">` (nebo white/black podle pozadí sekce), případně inline SVG pro čisté škálování v tisku.

## Zdroj pravdy a údržba

Tokeny odpovídají stavu Previo design systému (Figma: *P – design system*). Když se DS změní,
aktualizuj `tokens.md` — SKILL.md se měnit nemusí. Při pochybnosti o hodnotě vyhrává `tokens.md`,
ne odhad ani default nástroje. Info sémantická barva a přesná spacing škála (xs/sm/md) čekají na
potvrzení v aktuálním DS — nefixuj je bez ověření.
