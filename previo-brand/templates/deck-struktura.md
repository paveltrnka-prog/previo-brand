# Struktura prezentace Previo (.pptx)

Použij spolu se skillem `pptx`. Barvy a fonty viz `tokens.md`. Formát 16:9.

## Typy slidů

| Slide | Pozadí | Obsah |
|---|---|---|
| **Cover** | plná červená `#b50000` | Logo `previo-logo-white.svg` vlevo nahoře, název (Inter Medium, bílá, velký), podtitul, jméno a datum. Jediná plná červená plocha v decku, kromě closing. |
| **Section** | bílá, případně `#202124` | Velké číslo sekce a název. Bez dalšího obsahu. |
| **Obsah – text + číslo** | bílá | Červený section label (12 pt, verzálky) nahoře, nadpis-tvrzení (Inter Medium), vlevo text, vpravo jedno dominantní číslo červeně. |
| **Obsah – proces** | bílá | Nadpis, 3–5 kroků na časové ose (šedé linky, číslo kroku šedě). Jen pro sekvenční obsah. |
| **Obsah – graf/tabulka** | bílá | Nadpis-tvrzení, jedna vizualizace: zvýrazněná položka červeně, zbytek šedě. |
| **Citát / reference** | `#f2f2f2` | Citát, jméno, hotel. |
| **Closing** | červená nebo `#202124` | Kontakt, logo bílé varianty. |

## Pravidla

- Každý obsahový slide má **nadpis jako tvrzení** („Alfred zkrátil check-in na 90 s“), ne téma („Check-in“).
- **Jedna myšlenka na slide**, max. 3 odrážky, text min. 18 pt.
- Font: nadpisy `Inter Medium`, text `Inter` (nainstalované ze `fonts/`). Když se nenainstalují, řekni to uživateli.
- Číslo stránky a malá patička (Gray 500, 10 pt) na všech slidech kromě coveru.
- Neopakuj stejný layout 3× po sobě; střídej typy slidů.
- Žádné 3 stejné KPI karty, žádné status pill, žádné ikonky z náhodné sady.

## RGB pro python-pptx

Primary `181,0,0` · Ink `32,33,36` · Muted `81,81,81` · Border `229,229,229` · Surface `242,242,242` · White `255,255,255`
