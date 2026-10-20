# CONTEXT — previo-brand

Stav k 2026-10-20. Pro autora a pro Claude v nové session. Uživatelská dokumentace je v `README.md`,
pravidla značky v `previo-brand/SKILL.md`.

## Jak to funguje

- `previo-brand/` je samotný skill; zabalí se do `.skill` (zip) a vydává jako GitHub Release.
  Balíčky `*.skill` jsou v `.gitignore`.
- Šablony se needitují v `previo-brand/templates/*.html`, ale v `tools/src/`. `tools/build.py` do nich
  vloží base64 font Inter, inline logo (`%%LOGO:color|white%%`) a ikony (`%%ICON:name%%`).
- `tools/examples.py` vyplní šablony ukázkovým obsahem a vykreslí `docs/examples/*.png` (headless Chrome).
- `tools/icons.py` vyrobí z `icons/*.svg` PNG ve třech barvách pro `.pptx` (`icons/png/`).
- Prezentace: `deck.html` je vizuální vzor i hotová HTML/PDF prezentace; `deck-structure.md` popisuje
  převod do `.pptx` (1 px = 7 144 EMU, 1 px = 0,5625 pt). Velikosti v `deck.html` jsou pro prezentaci
  ke čtení (text ≥ 12 pt).

## Rozhodnutí a proč

- **v5 (2026-10-19)** vznikla z prezentace kolegy (nabídka Marketing+ pro hotel): byla šedá, s deformovanými
  fotkami, porušeným pravidlem červené, malým písmem a nejednotným názvem produktu. Odtud červený rytmus
  (titulka/závěr/statement), ikony, pravidla pro fotky, velikosti písma a kontrola před předáním.
- **Repo je veřejné.** Ukázky v README musí být anonymizované (žádní klienti, kontakty, skutečné provize,
  fotky objektů). `docs/examples/deck-offer.png` je anonymizovaná verze reálné nabídky.
- Ikony jsou vlastní jednoduchá liniová sada (24px mřížka, tah 1,75, `currentColor`), ne cizí knihovna.

## Gotchy

- Na Macu není LibreOffice, PIL ani rsvg/ImageMagick — vše se rasterizuje přes headless Chrome.
- Headless Chrome se zasekne na zámku profilu: vždy vlastní `--user-data-dir` a `timeout`.
- Headless Chrome má minimální velikost okna: malé PNG (ikony, logo) vykreslit na 800×800 vycentrované
  a oříznout `sips -c` na střed. Jinak vznikají natažené nebo uříznuté obrázky.
- Kontaktní list s `<img width=…>` může vypadat natažený i u správných PNG — kontrolovat přímo PNG.
- `python-pptx` není v systému (PEP 668); instalovat do venv (`python3 -m venv … && pip install python-pptx`).
- Push do `paveltrnka-prog/previo-brand` jde jen z gh účtu `paveltrnka-prog`
  (`gh auth switch -u paveltrnka-prog && gh auth setup-git`); pod `trnkapavel` vrací 403.
- Merge PR přes Claude blokuje auto mode („merge bez review“) — merguje Pavel sám.

## Otevřené

- `.pptx` výstupy nejde lokálně vykreslit (chybí `soffice`); ověřuje se HTML náhledem se stejným
  rozvržením. Finální kontrola v PowerPointu/Keynote je na člověku.
- Zpětná vazba kolegy k v5 a předělané nabídce (v `~/Downloads/…_v2.pptx/.pdf`, mimo repo):
  potvrdit Meta Ads ve fázi 1, datum na titulce, oficiální název Marketing+ vs. M+.
