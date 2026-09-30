# Previo brand – instalace pro kolegy

Balíček obsahuje pravidla Previo brandu, písmo Inter, loga a šablony (onepager, report,
sociální grafiky, struktura prezentace). Claude je pak použije automaticky, když požádáte
o vizuální výstup.

## Instalace (jednou, 2 minuty)

**Claude Desktop / claude.ai**
1. Otevřete **Nastavení → Capabilities → Skills**.
2. Klikněte **Upload skill** a vyberte soubor `previo-brand.zip`.
3. Zapněte přepínač u skillu **previo-brand**.

**Claude Code (terminál)**
1. Rozbalte zip do složky `~/.claude/skills/` tak, aby vznikla `~/.claude/skills/previo-brand/`.
2. Spusťte nové sezení.

## Použití

Napište třeba: „Udělej onepager o Alfredovi pro hoteliéry“, „Sociální post s číslem 42 % …“,
„Prezentace pro klienta, 8 slidů.“ Pošlete jen obsah, vzhled řeší skill.

## Písmo Inter (jen pro PowerPoint a Word)

HTML a PDF výstupy nesou písmo v sobě a fungují vždy. Pokud budete otevírat `.pptx` nebo `.docx`
a chcete přesný vzhled, nainstalujte jednou oba soubory ze složky `fonts/`:
- **Mac:** dvojklik na `Inter-Regular.ttf` a `Inter-Medium.ttf`, tlačítko **Nainstalovat písmo**.
- **Windows:** pravý klik na oba soubory, **Nainstalovat pro všechny uživatele**.
Pak restartujte PowerPoint/Word. Bez instalace použijte PDF.

## Když něco nesedí

Barva `#b50000`, font Inter a logo jsou jediný zdroj pravdy. Pokud výstup vypadá jinak,
napište Claudovi „použij Previo brand skill“. Problémy hlaste Pavlu Trnkovi.
